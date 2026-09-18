#!/usr/bin/env python3
"""Stage one fixture for a subagent run.

Usage: python tools/stage_fixture.py <fixture-id>

Creates tests/.scratch/<fixture-id>/ holding a copy of skill/ and content.md,
a byte-for-byte copy of tests/fixtures/<fixture-id>.md. Nothing else is staged;
tests/expected/ is never copied (phase6-run-method). Prints the scratch path.
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "tests" / "fixtures"
SCRATCH = ROOT / "tests" / ".scratch"
SKILL = ROOT / "skill"


def main(argv):
    if len(argv) != 2:
        print("usage: python tools/stage_fixture.py <fixture-id>", file=sys.stderr)
        return 2
    fixture_id = argv[1]
    src = FIXTURES / f"{fixture_id}.md"
    if not src.is_file():
        print(f"error: fixture not found: {src.relative_to(ROOT)}", file=sys.stderr)
        return 1
    dest = SCRATCH / fixture_id
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    shutil.copytree(SKILL, dest / "skill")
    shutil.copyfile(src, dest / "content.md")
    print(dest)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
