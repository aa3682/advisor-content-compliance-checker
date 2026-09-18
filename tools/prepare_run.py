#!/usr/bin/env python3
"""Prepare a recorded run: run directory, manifest, run list, staged fixtures.

Usage: python tools/prepare_run.py --model <id> --staging-root <dir> [--n-entry 1] [--n-adversarial 3] [--dry-run]

Executes nothing. Per RULINGS.md phase6-run-method and phase6-pass-criteria:
  run-id is <YYYY-MM-DD>-<short main hash>; refuses when the working tree is dirty or HEAD
  is not main (a dry run reports the guard result instead of refusing).
  Creates tests/runs/<run-id>/ with MANIFEST.md, RUNLIST.tsv (fixture_id, k, scratch_path,
  output_path; entry fixtures first in ID order, then adversarial) and SUBAGENT_PROMPT.md
  (a copy of tests/harness/SUBAGENT_PROMPT.md, so the run records the prompt it used).
  Stages one scratch directory per sample, <staging-root>/<fixture-id>.<k>/, with the
  stage_fixture logic; --staging-root must be outside the repository (run-isolation), and
  MANIFEST.md records it. RUNLIST scratch paths are absolute.
--dry-run does everything except create the run directory and prints what it would write.
"""
import argparse
import datetime as dt
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_check_index import ROOT  # noqa: E402
from stage_fixture import FIXTURES, SKILL  # noqa: E402

try:
    import yaml
except ImportError:
    sys.stderr.write("prepare_run: PyYAML is required. Install it with: python -m pip install pyyaml\n")
    sys.exit(2)

RUNS = ROOT / "tests" / "runs"
EXPECTED = ROOT / "tests" / "expected"
PROMPT = ROOT / "tests" / "harness" / "SUBAGENT_PROMPT.md"


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()


def stage(fixture_id, k, staging_root):
    src = FIXTURES / f"{fixture_id}.md"
    dest = staging_root / f"{fixture_id}.{k}"
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    shutil.copytree(SKILL, dest / "skill")
    shutil.copyfile(src, dest / "content.md")
    return dest


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True, help="subagent model alias pinned for this run")
    ap.add_argument("--model-reported", default="", help="model identifier the subagent reports for that alias")
    ap.add_argument("--staging-root", required=True,
                    help="directory outside the repository where per-sample scratch directories are staged (run-isolation)")
    ap.add_argument("--n-entry", type=int, default=1)
    ap.add_argument("--n-adversarial", type=int, default=3)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    staging_root = Path(a.staging_root).resolve()
    if staging_root == ROOT or ROOT in staging_root.parents:
        print("error: --staging-root must be outside the repository (run-isolation)", file=sys.stderr)
        return 1

    branch = git("rev-parse", "--abbrev-ref", "HEAD")
    dirty = git("status", "--porcelain")
    short = git("rev-parse", "--short", "HEAD")
    guard = []
    if branch != "main":
        guard.append(f"HEAD is on {branch!r}, not main")
    if dirty:
        guard.append(f"working tree is dirty ({len(dirty.splitlines())} path(s))")
    if guard and not a.dry_run:
        for g in guard:
            print(f"error: {g}", file=sys.stderr)
        return 1
    for g in guard:
        print(f"warning (dry run): {g}")

    run_id = f"{dt.date.today().isoformat()}-{short}"
    run_dir = RUNS / run_id
    if run_dir.exists() and not a.dry_run:
        print(f"error: run directory already exists: {run_dir.relative_to(ROOT)}", file=sys.stderr)
        return 1

    entry, adversarial = [], []
    for path in sorted(FIXTURES.glob("*.md")):
        fid = path.stem
        exp = EXPECTED / f"{fid}.yaml"
        if not exp.is_file():
            print(f"error: {fid} has no expected file", file=sys.stderr)
            return 1
        cat = (yaml.safe_load(exp.read_text(encoding="utf-8")) or {}).get("category")
        (entry if cat == "entry" else adversarial).append(fid)
    rows = []
    for fid in entry:
        for k in range(1, a.n_entry + 1):
            rows.append((fid, k))
    for fid in adversarial:
        for k in range(1, a.n_adversarial + 1):
            rows.append((fid, k))

    rel = lambda p: str(p.relative_to(ROOT))  # noqa: E731
    runlist = ["fixture_id\tk\tscratch_path\toutput_path"]
    for fid, k in rows:
        runlist.append(f"{fid}\t{k}\t{staging_root / f'{fid}.{k}'}\t{rel(run_dir / f'{fid}.{k}.md')}")
    manifest = "\n".join([
        "# Manifest",
        f"- run_id: {run_id}",
        f"- date: {dt.date.today().isoformat()}",
        f"- skill_commit: {short}",
        f"- model: {a.model}",
        f"- model_reported: {a.model_reported}",
        f"- staging_root: {staging_root}",
        f"- fixtures: {len(entry) + len(adversarial)}",
        f"- n_entry: {a.n_entry}",
        f"- n_adversarial: {a.n_adversarial}",
        "- notes: ",
    ]) + "\n"

    staging_root.mkdir(parents=True, exist_ok=True)
    for fid, k in rows:
        stage(fid, k, staging_root)

    if a.dry_run:
        print(f"dry run: would create {rel(run_dir)}/ with MANIFEST.md, RUNLIST.tsv, SUBAGENT_PROMPT.md")
        print("--- MANIFEST.md ---")
        print(manifest, end="")
        print(f"--- RUNLIST.tsv ({len(rows)} rows; first five and last five) ---")
        for line in runlist[:6] + ["..."] + runlist[-5:]:
            print(line)
    else:
        run_dir.mkdir(parents=True)
        (run_dir / "MANIFEST.md").write_text(manifest, encoding="utf-8")
        (run_dir / "RUNLIST.tsv").write_text("\n".join(runlist) + "\n", encoding="utf-8")
        shutil.copyfile(PROMPT, run_dir / "SUBAGENT_PROMPT.md")
    print(f"run_id: {run_id}")
    print(f"samples: {len(rows)} ({len(entry)} entry x {a.n_entry} + {len(adversarial)} adversarial x {a.n_adversarial})")
    print(f"staged: {len(rows)} sample directories under {staging_root}/")
    print(f"runlist: {rel(run_dir / 'RUNLIST.tsv')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
