#!/usr/bin/env python3
"""Launch subagents for a prepared run, one process per sample, inside its staged directory.

Usage:
  python tests/harness/launch_sample.py <run-id> <fixture-id> <k> [options]
  python tests/harness/launch_sample.py <run-id> --all [--jobs N] [options]
Options:
  --model <alias>     subagent model; default: the model line of the run's MANIFEST.md
  --max-turns <n>     turn cap per subagent (default 40)
  --timeout <s>       wall-clock cap per subagent in seconds (default 900)
  --jobs <n>          concurrent launches with --all (default 4)
  --skip-done         with --all, skip samples whose output file already exists

Implements RULINGS.md run-isolation-sandbox. For each sample listed in
tests/runs/<run-id>/RUNLIST.tsv:

  1. The staged directory is listed (tools/isolation.py) and the evidence is written to
     tests/runs/<run-id>/<fixture-id>.<k>.ISOLATION.txt: resolved cwd (pwd -P inside it),
     launch time, and every file under it. A staged directory holding anything but skill/
     and content.md, or any symlink, is refused: the evidence is recorded and no subagent runs.
  2. A separate `claude -p` process is started with the staged directory as its working
     directory. Its argv carries the prompt text from the run's SUBAGENT_PROMPT.md (relative
     paths only), the model, and the tool set Read, Glob, Grep, Write; no MCP servers, no
     settings files, no skills, no session persistence. Its environment is the harness
     environment minus every variable whose value names the repository path, minus the
     additional-directories variables, and with PWD set to the staged directory. A bare
     Glob or Read therefore resolves inside the sample and cannot reach the repository.
  3. output.md, if the subagent wrote it, is copied byte for byte to the sample's output
     path. A sample with no output.md is a recorded failure and is not retried
     (phase6-run-model). The subagent's reply, the model it reported, and the exit status
     are appended as one JSON line to tests/runs/<run-id>/LAUNCH.log; a reply that reports
     reading outside the directory is the operator's cue for CONTAMINATED.txt, which stays
     the manual channel.
"""
import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from isolation import write_evidence  # noqa: E402

RUNS = ROOT / "tests" / "runs"
TOOLS = "Read,Glob,Grep,Write"
DROP_ENV = {"CLAUDE_ADDITIONAL_DIRECTORIES", "CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD",
            "GITHUB_TOKEN", "GIT_ASKPASS", "OLDPWD"}
LOG_LOCK = threading.Lock()


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


def launch(run_dir, row, prompt, model, max_turns, timeout):
    fid, k, staged = row["fixture"], row["k"], row["scratch"]
    name = f"{fid}.{k}"
    record = {"sample": name, "started": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "cwd": str(staged), "model": model}
    if not staged.is_dir():
        record.update({"status": "not-staged"})
        log(run_dir, record)
        print(f"{name}: not staged: {staged}")
        return record
    _, problems = write_evidence(staged, fid, k, run_dir,
                                 extra={"launcher": "tests/harness/launch_sample.py", "tools": TOOLS, "model": model})
    if problems:
        record.update({"status": "refused", "problems": problems})
        log(run_dir, record)
        print(f"{name}: refused, staged directory violates the staging rule: {'; '.join(problems)}")
        return record
    argv = ["claude", "-p", prompt, "--model", model,
            "--tools", TOOLS, "--allowedTools", TOOLS,
            "--strict-mcp-config", "--setting-sources", "", "--disable-slash-commands",
            "--no-session-persistence", "--max-turns", str(max_turns), "--output-format", "json"]
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
        record.update({"exit": None, "status": "timeout"})
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
    print(f"{name}: {record['status']}; reply: {(record.get('reply') or '')[:120]!r}")
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
    ap.add_argument("--timeout", type=int, default=900)
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
    with ThreadPoolExecutor(max_workers=max(1, a.jobs if a.all else 1)) as pool:
        records = list(pool.map(lambda r: launch(run_dir, r, prompt, model, a.max_turns, a.timeout), rows))
    done = sum(1 for r in records if r.get("status") == "done")
    print(f"{done}/{len(records)} samples produced output.md; evidence in {run_dir.relative_to(ROOT)}/<sample>.ISOLATION.txt; log in LAUNCH.log")
    return 0 if done == len(records) else 1


if __name__ == "__main__":
    sys.exit(main())
