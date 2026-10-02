#!/usr/bin/env python3
"""Launch subagents for a prepared run, one process per sample, inside its staged directory.

Usage:
  python tests/harness/launch_sample.py <run-id> <fixture-id> <k> [options]
  python tests/harness/launch_sample.py <run-id> --all [--jobs N] [options]
Options:
  --model <alias>     subagent model; default: the model line of the run's MANIFEST.md
  --max-turns <n>     turn cap per subagent (default 40)
  --timeout <s>       wall-clock cap per subagent in seconds (default 1500)
  --jobs <n>          concurrent launches with --all (default 4)
  --skip-done         with --all, skip samples whose output file already exists

Implements RULINGS.md run-isolation-sandbox and sandbox-escape-handling. For each
sample listed in tests/runs/<run-id>/RUNLIST.tsv:

  1. The sample is staged fresh under a neutral temp path, tempfile.mkdtemp(prefix=
     "acc-run-<run-id>-")/<fixture-id>.<k>/, holding exactly skill/ and content.md; the
     RUNLIST scratch_path column (under the CLI's own scratchpad tree) is not used, so no
     path segment spells the repository location. The staged directory is listed
     (tools/isolation.py) and the evidence is written to
     tests/runs/<run-id>/<fixture-id>.<k>.ISOLATION.txt: resolved cwd (pwd -P inside it),
     launch time, and every file under it. A staged directory holding anything but skill/
     and content.md, or any symlink, is refused: the evidence is recorded and no subagent runs.
  2. Before launch, the repo working tree is snapshotted: git status --porcelain plus an
     mtime listing of every tracked and untracked file. A separate `claude -p` process is
     then started with the staged directory as its working directory. Its argv carries the
     prompt text from the run's SUBAGENT_PROMPT.md (relative paths only), the model, and the
     tool set Read, Glob, Grep, Write; no MCP servers, no settings files, no skills, no
     session persistence. Its environment is the harness environment minus every variable
     whose value names the repository path, minus the additional-directories variables, and
     with PWD set to the staged directory. A bare Glob or Read therefore resolves inside the
     sample and cannot reach the repository.
  3. After the subprocess exits, the repo working tree is swept against the snapshot. Any
     path new or modified since launch, outside tests/runs/<run-id>/, is a sandbox escape:
     it is deleted, its path is recorded in a "post-launch:" section appended to that
     sample's ISOLATION.txt, and the sample is marked status "escaped" with no output
     credited, whatever staged/output.md holds. Otherwise "post-launch: clean" is appended
     and output.md, if the subagent wrote it, is copied byte for byte to the sample's output
     path. A sample with no output.md is a recorded failure (phase6-run-model).
  4. A sample is relaunched only on a CLI-reported API error (api-error-relaunch, amending
     phase6-run-model): exit status non-zero and a reply matching
     ^API Error:\s*(5\d\d\b|.*[Cc]onnection), i.e. a 529, another 5xx, or a connection
     error; or on a timeout that left no output.md (timeout-relaunch, amending
     api-error-relaunch), relaunched the same way and recorded with status
     "timeout-relaunched". Never on the turn cap, never on an escaped sample; an
     escape is checked first and is final even when the reply was an API error. An errored
     attempt earns no credit: any output.md it left is ignored. Each relaunch waits 60
     seconds (outside the escape lock), restages the sample fresh and writes new isolation
     evidence; the errored attempt's evidence, post-launch section included, is kept as
     <fixture-id>.<k>.attempt<n>.ISOLATION.txt and the final attempt's stays at the
     canonical <fixture-id>.<k>.ISOLATION.txt. At most 3 attempts in all; a sample whose
     three attempts are all API errors ends with status "api-error", which score_run.py
     fails U0 with reason "api-error".
  The subagent's reply, the model it reported, and the exit status are appended to
  tests/runs/<run-id>/LAUNCH.log as one JSON line per attempt, carrying "attempt" and
  "max_attempts"; an API-error attempt that is relaunched has status
  "api-error-relaunched". A reply that reports reading outside the directory is the
  operator's cue for CONTAMINATED.txt, which stays the manual channel.
"""
import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from isolation import write_evidence  # noqa: E402
from stage_fixture import FIXTURES, SKILL  # noqa: E402

RUNS = ROOT / "tests" / "runs"
TOOLS = "Read,Glob,Grep,Write"
DROP_ENV = {"CLAUDE_ADDITIONAL_DIRECTORIES", "CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD",
            "GITHUB_TOKEN", "GIT_ASKPASS", "OLDPWD"}
MAX_ATTEMPTS = 3  # api-error-relaunch: first launch plus at most two relaunches
RELAUNCH_WAIT = 60  # seconds between attempts, slept outside ESCAPE_LOCK
API_ERROR_RE = re.compile(r"^API Error:\s*(5\d\d\b|.*[Cc]onnection)")
LOG_LOCK = threading.Lock()
ESCAPE_LOCK = threading.Lock()  # serializes snapshot -> subprocess -> sweep so concurrent samples can't misattribute an escape


def classify_attempt(exit_code, reply, timed_out):
    """One attempt's outcome under api-error-relaunch: "timeout", "api-error",
    "done-candidate" (exit 0) or "other-failure". "api-error" is a positive match only:
    a non-zero exit and a reply naming a 5xx status or a connection error."""
    if timed_out:
        return "timeout"
    if exit_code != 0 and API_ERROR_RE.match(reply or ""):
        return "api-error"
    if exit_code == 0:
        return "done-candidate"
    return "other-failure"


def attempt_evidence_path(run_dir, fid, k, attempt):
    return run_dir / f"{fid}.{k}.attempt{attempt}.ISOLATION.txt"


def child_env(staged):
    root = str(ROOT)
    env = {}
    for key, value in os.environ.items():
        if key in DROP_ENV or key.startswith("GIT_CONFIG_"):
            continue
        if root in value:
            continue
        env[key] = value
    env["PWD"] = str(staged)
    return env


def stage_sample(base, fid, k):
    """Stage <base>/<fid>.<k>/ fresh, holding exactly skill/ and content.md (sandbox-escape-handling).

    base is a neutral temp directory (tempfile.mkdtemp), never the CLI's scratchpad tree,
    so no path segment spells the repository location. Mirrors tools/prepare_run.py's stage()."""
    dest = base / f"{fid}.{k}"
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    shutil.copytree(SKILL, dest / "skill", symlinks=False, ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copyfile(FIXTURES / f"{fid}.md", dest / "content.md")
    return dest


def _git(*args):
    return subprocess.run(["git", *args], cwd=str(ROOT), capture_output=True, text=True, check=True).stdout


def repo_snapshot():
    """git status --porcelain plus an mtime listing of every tracked and untracked file
    (sandbox-escape-handling). Used to detect a post-launch write outside the sandbox."""
    porcelain = _git("status", "--porcelain")
    paths = set(_git("ls-files").splitlines()) | set(_git("ls-files", "--others", "--exclude-standard").splitlines())
    mtimes = {}
    for rel in paths:
        p = ROOT / rel
        try:
            mtimes[rel] = p.stat().st_mtime
        except OSError:
            continue
    return porcelain, mtimes


def detect_escape(before_mtimes, run_id):
    """Paths under the repo, outside tests/runs/<run-id>/, new or modified since `before_mtimes`."""
    exclude = f"tests/runs/{run_id}/"
    paths = set(_git("ls-files").splitlines()) | set(_git("ls-files", "--others", "--exclude-standard").splitlines())
    escaped = []
    for rel in sorted(paths):
        if rel.startswith(exclude):
            continue
        p = ROOT / rel
        try:
            mtime = p.stat().st_mtime
        except OSError:
            continue
        if rel not in before_mtimes or mtime != before_mtimes[rel]:
            escaped.append(rel)
    return escaped


def read_runlist(run_dir):
    rows = []
    for line in (run_dir / "RUNLIST.tsv").read_text(encoding="utf-8").splitlines()[1:]:
        parts = line.split("\t")
        if len(parts) >= 4 and parts[1].isdigit():
            rows.append({"fixture": parts[0], "k": int(parts[1]), "scratch": Path(parts[2]),
                         "output": ROOT / parts[3]})
    return rows


def manifest_model(run_dir):
    for line in (run_dir / "MANIFEST.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("- model:"):
            return line.split(":", 1)[1].strip()
    return ""


def log(run_dir, record):
    with LOG_LOCK:
        with (run_dir / "LAUNCH.log").open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def launch(run_dir, run_id, base, row, prompt, model, max_turns, timeout):
    fid, k = row["fixture"], row["k"]
    name = f"{fid}.{k}"
    argv = ["claude", "-p", prompt, "--model", model,
            "--tools", TOOLS, "--allowedTools", TOOLS,
            "--strict-mcp-config", "--setting-sources", "", "--disable-slash-commands",
            "--no-session-persistence", "--max-turns", str(max_turns), "--output-format", "json"]
    for attempt in range(1, MAX_ATTEMPTS + 1):
        staged = stage_sample(base, fid, k)  # fresh every attempt; an errored attempt's output.md goes with it
        record = {"sample": name, "attempt": attempt, "max_attempts": MAX_ATTEMPTS,
                  "started": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                  "cwd": str(staged), "model": model}
        iso_path, problems = write_evidence(staged, fid, k, run_dir,
                                            extra={"launcher": "tests/harness/launch_sample.py", "tools": TOOLS, "model": model})
        if problems:
            record.update({"status": "refused", "problems": problems})
            log(run_dir, record)
            print(f"{name}: refused, staged directory violates the staging rule: {'; '.join(problems)}")
            return record
        timed_out = False
        with ESCAPE_LOCK:  # snapshot -> subprocess -> sweep as one unit, so a concurrent sample can't be misattributed
            _, before_mtimes = repo_snapshot()
            try:
                proc = subprocess.run(argv, cwd=str(staged), env=child_env(staged), capture_output=True, text=True,
                                      timeout=timeout)
                record["exit"] = proc.returncode
                try:
                    result = json.loads(proc.stdout)
                except ValueError:
                    result = {}
                record["reply"] = result.get("result", proc.stdout[-2000:] if not result else "")
                record["num_turns"] = result.get("num_turns")
                record["model_reported"] = ",".join(sorted(result.get("modelUsage", {}).keys()))
                if proc.returncode != 0:
                    record["stderr"] = proc.stderr[-2000:]
            except subprocess.TimeoutExpired:
                timed_out = True
                record.update({"exit": None, "status": "timeout"})
            escaped = detect_escape(before_mtimes, run_id)
            if escaped:
                for rel in escaped:
                    p = ROOT / rel
                    try:
                        if p.is_dir() and not p.is_symlink():
                            shutil.rmtree(p)
                        elif p.exists() or p.is_symlink():
                            p.unlink()
                    except OSError:
                        pass
                with iso_path.open("a", encoding="utf-8") as fh:
                    fh.write("post-launch:\n" + "".join(rel + "\n" for rel in escaped))
            else:
                with iso_path.open("a", encoding="utf-8") as fh:
                    fh.write("post-launch: clean\n")
        kind = classify_attempt(record.get("exit"), record.get("reply"), timed_out)
        if escaped:  # an escape is final, whatever the reply said (api-error-relaunch)
            record["output"] = None
            record["status"] = "escaped"
            record["escaped"] = escaped
        elif kind == "api-error":  # no credit for this attempt; staged/output.md is ignored
            record["output"] = None
            if attempt < MAX_ATTEMPTS:
                record["status"] = "api-error-relaunched"
                iso_path.replace(attempt_evidence_path(run_dir, fid, k, attempt))
                log(run_dir, record)
                print(f"{name}: attempt {attempt}/{MAX_ATTEMPTS} api-error, relaunching in {RELAUNCH_WAIT}s; "
                      f"reply: {(record.get('reply') or '')[:120]!r}")
                time.sleep(RELAUNCH_WAIT)  # outside ESCAPE_LOCK
                continue
            record["status"] = "api-error"
        elif kind == "timeout" and not (staged / "output.md").is_file():  # timeout-relaunch: nothing to score
            record["output"] = None
            if attempt < MAX_ATTEMPTS:
                record["status"] = "timeout-relaunched"
                iso_path.replace(attempt_evidence_path(run_dir, fid, k, attempt))
                log(run_dir, record)
                print(f"{name}: attempt {attempt}/{MAX_ATTEMPTS} timeout with no output, relaunching in {RELAUNCH_WAIT}s")
                time.sleep(RELAUNCH_WAIT)  # outside ESCAPE_LOCK
                continue
            record["status"] = "timeout"
        else:
            out = staged / "output.md"
            if out.is_file():
                row["output"].parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(out, row["output"])
                record["output"] = str(row["output"].relative_to(ROOT))
                record.setdefault("status", "done")
            else:
                record["output"] = None
                record.setdefault("status", "no-output")
        log(run_dir, record)
        print(f"{name}: {record['status']} (attempt {attempt}/{MAX_ATTEMPTS}); reply: {(record.get('reply') or '')[:120]!r}")
        return record


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_id")
    ap.add_argument("fixture_id", nargs="?")
    ap.add_argument("k", nargs="?", type=int)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--model", default=None)
    ap.add_argument("--max-turns", type=int, default=40)
    ap.add_argument("--timeout", type=int, default=1500)
    ap.add_argument("--skip-done", action="store_true")
    a = ap.parse_args()
    run_dir = RUNS / a.run_id
    if not run_dir.is_dir():
        print(f"error: run directory not found: {run_dir}", file=sys.stderr)
        return 1
    prompt = (run_dir / "SUBAGENT_PROMPT.md").read_text(encoding="utf-8").strip()
    if str(ROOT) in prompt:
        print("error: the run's SUBAGENT_PROMPT.md names the repository path (run-isolation-sandbox)", file=sys.stderr)
        return 1
    model = a.model or manifest_model(run_dir)
    if not model:
        print("error: no model: pass --model or set it in MANIFEST.md", file=sys.stderr)
        return 1
    rows = read_runlist(run_dir)
    if a.all:
        if a.skip_done:
            rows = [r for r in rows if not r["output"].is_file()]
    else:
        if not a.fixture_id or a.k is None:
            ap.error("give <fixture-id> <k>, or --all")
        rows = [r for r in rows if r["fixture"] == a.fixture_id and r["k"] == a.k]
        if not rows:
            print(f"error: {a.fixture_id}.{a.k} is not in RUNLIST.tsv", file=sys.stderr)
            return 1
    base = Path(tempfile.mkdtemp(prefix=f"acc-run-{a.run_id}-"))  # neutral temp path (sandbox-escape-handling); never the scratchpad tree
    with ThreadPoolExecutor(max_workers=max(1, a.jobs if a.all else 1)) as pool:
        records = list(pool.map(lambda r: launch(run_dir, a.run_id, base, r, prompt, model, a.max_turns, a.timeout), rows))
    done = sum(1 for r in records if r.get("status") == "done")
    escaped = sum(1 for r in records if r.get("status") == "escaped")
    api_error = sum(1 for r in records if r.get("status") == "api-error")
    print(f"{done}/{len(records)} samples produced output.md ({escaped} escaped, {api_error} api-error); evidence in {run_dir.relative_to(ROOT)}/<sample>.ISOLATION.txt; log in LAUNCH.log")
    return 0 if done == len(records) else 1


if __name__ == "__main__":
    sys.exit(main())
