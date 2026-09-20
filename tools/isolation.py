#!/usr/bin/env python3
"""Structural run isolation (RULINGS.md run-isolation-sandbox). Standard library only.

A staged sample directory holds exactly skill/ and content.md, with no symlinks. The
harness records, at launch and before the subagent runs, the resolved working directory
and a recursive file listing of that directory to tests/runs/<run-id>/<fixture-id>.<k>.ISOLATION.txt.
The scorer refuses to score a sample whose evidence file is missing, names a working
directory other than the sample's, or lists any path outside skill/ and content.md.

ISOLATION.txt format (one field per line, then the listing):

    sample: <fixture-id>.<k>
    cwd: <resolved working directory, from pwd -P inside it>
    launched: <UTC timestamp>
    files:
    content.md
    skill/SKILL.md
    skill/references/definitions.md
    ...

Every line after "files:" is one file path relative to cwd, POSIX separators, sorted.
Unknown fields before "files:" are ignored by the scorer.
"""
import datetime as dt
import os
import subprocess
from pathlib import Path

REQUIRED_FILES = ("content.md", "skill/SKILL.md")
FILES_MARK = "files:"


def allowed(rel):
    """True when a relative path is content.md or lies under skill/."""
    return rel == "content.md" or rel.startswith("skill/")


def check_listing(entries):
    """Violations of the staging rule for a list of relative file paths."""
    problems = []
    for rel in entries:
        if not allowed(rel):
            problems.append(f"path outside skill/ and content.md: {rel}")
    for req in REQUIRED_FILES:
        if req not in entries:
            problems.append(f"{req} missing")
    return problems


def listing(staged):
    """Recursive file listing of a staged directory: (sorted relative paths, violations).

    Symlinks are never followed and are violations wherever they sit, so a staged
    directory cannot reach outside itself through one."""
    staged = Path(staged)
    entries, problems = [], []
    for dirpath, dirnames, filenames in os.walk(staged, followlinks=False):
        dirnames.sort()
        filenames.sort()
        rel_dir = Path(dirpath).relative_to(staged)
        for d in dirnames:
            if (Path(dirpath) / d).is_symlink():
                problems.append(f"symlink: {(rel_dir / d).as_posix()}/")
        for f in filenames:
            rel = (rel_dir / f).as_posix()
            if (Path(dirpath) / f).is_symlink():
                problems.append(f"symlink: {rel}")
            entries.append(rel)
    entries.sort()
    return entries, problems + check_listing(entries)


def resolved_cwd(staged):
    """The working directory as a process launched in it sees it (pwd -P)."""
    try:
        out = subprocess.run(["pwd", "-P"], cwd=str(staged), capture_output=True, text=True, check=True).stdout
        if out.strip():
            return out.strip()
    except (OSError, subprocess.CalledProcessError):
        pass
    return str(Path(staged).resolve())


def evidence_path(run_dir, fixture_id, k):
    return Path(run_dir) / f"{fixture_id}.{k}.ISOLATION.txt"


def write_evidence(staged, fixture_id, k, run_dir, extra=None):
    """Record cwd and the listing of a staged directory before launch. Returns
    (evidence path, violations). The evidence is written even when the staged
    directory violates the rule, so that the refusal is on the record."""
    entries, problems = listing(staged)
    fields = [("sample", f"{fixture_id}.{k}"),
              ("cwd", resolved_cwd(staged)),
              ("launched", dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))]
    fields += list((extra or {}).items())
    text = "".join(f"{key}: {value}\n" for key, value in fields) + FILES_MARK + "\n" + "".join(e + "\n" for e in entries)
    path = evidence_path(run_dir, fixture_id, k)
    path.write_text(text, encoding="utf-8")
    return path, problems


def parse_evidence(text):
    """Return (fields dict, entries list) from ISOLATION.txt text."""
    fields, entries, in_files = {}, [], False
    for line in text.splitlines():
        if in_files:
            if line.strip():
                entries.append(line.strip())
            continue
        if line.strip() == FILES_MARK:
            in_files = True
            continue
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip()
    if not in_files:
        fields["_no_files_section"] = "1"
    return fields, entries


def evidence_problems(run_dir, fixture_id, k):
    """Why a sample may not be scored, or [] when its isolation evidence is in order."""
    path = evidence_path(run_dir, fixture_id, k)
    if not path.is_file():
        return [f"{path.name} missing"]
    fields, entries = parse_evidence(path.read_text(encoding="utf-8"))
    problems = []
    if "_no_files_section" in fields:
        problems.append(f"{path.name} has no '{FILES_MARK}' section")
    cwd = fields.get("cwd", "")
    if not cwd:
        problems.append(f"{path.name} names no cwd")
    elif Path(cwd).name != f"{fixture_id}.{k}":
        problems.append(f"cwd {cwd!r} is not the sample's directory {fixture_id}.{k}")
    problems += check_listing(entries)
    return problems
