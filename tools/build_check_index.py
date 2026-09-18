#!/usr/bin/env python3
"""Generate the "## Checks" section of skill/SKILL.md from catalog/failures.md.

Ruling entries-to-checks (RULINGS.md): one check per catalog entry, 1:1; every
token copied from the catalog; reference file(s) derived from where the entry
appears in skill/references/. Never hand-edit the generated section; rerun this
script when the catalog changes. Standard library only.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog" / "failures.md"
SKILL = ROOT / "skill" / "SKILL.md"
REFS_DIR = ROOT / "skill" / "references"

SERIES = ["GP", "PERF", "TE", "TPR"]  # catalog order (ruling catalog-id-scheme)
REF_ORDER = [
    "general-prohibitions.md",
    "performance.md",
    "testimonials-endorsements.md",
    "third-party-ratings.md",
    "definitions.md",
]
EXPECTED_ENTRIES = 51
SEP = " · "
FIELD_SEP = " — "
ENTRY_RE = re.compile(r"^- ((?:GP|PERF|TE|TPR)-\d+)" + re.escape(FIELD_SEP))
REF_ID_RE = re.compile(r"^- ((?:GP|PERF|TE|TPR)-\d+)" + re.escape(FIELD_SEP))


def fail(msg):
    sys.stderr.write(f"build_check_index: {msg}\n")
    sys.exit(1)


def parse_catalog():
    """Return entries in catalog order as dicts with the five catalog-entry-shape fields."""
    entries = []
    for lineno, line in enumerate(CATALOG.read_text(encoding="utf-8").splitlines(), 1):
        if not ENTRY_RE.match(line):
            continue
        fields = line[2:].split(FIELD_SEP)
        if len(fields) != 5:
            fail(f"{CATALOG.name}:{lineno}: expected 5 fields, got {len(fields)}")
        entry = dict(zip(["id", "observed", "pattern", "rule", "source"], fields))
        for k, v in entry.items():
            if not v.strip():
                fail(f"{CATALOG.name}:{lineno}: empty field {k}")
        entries.append(entry)
    ids = [e["id"] for e in entries]
    if len(ids) != len(set(ids)):
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        fail(f"duplicate IDs: {dupes}")
    if len(entries) != EXPECTED_ENTRIES:
        fail(f"expected {EXPECTED_ENTRIES} entries, found {len(entries)}")
    return entries


def reference_files_by_id():
    """Map ID -> list of reference filenames (REF_ORDER) whose entry lines carry it."""
    found = {}
    for name in REF_ORDER:
        path = REFS_DIR / name
        if not path.is_file():
            fail(f"missing reference file {path}")
        for line in path.read_text(encoding="utf-8").splitlines():
            m = REF_ID_RE.match(line)
            if m:
                found.setdefault(m.group(1), [])
                if name not in found[m.group(1)]:
                    found[m.group(1)].append(name)
    return found


def build_section(entries, refs):
    for e in entries:
        if e["id"] not in refs:
            fail(f"{e['id']} appears in no reference file")
    by_series = {s: [e for e in entries if e["id"].split("-")[0] == s] for s in SERIES}
    unknown = [e["id"] for e in entries if e["id"].split("-")[0] not in SERIES]
    if unknown:
        fail(f"IDs outside the four series: {unknown}")
    out = [
        "## Checks",
        "",
        f"Generated from catalog/failures.md by tools/build_check_index.py. "
        f"Never hand-edit; rerun the script when the catalog changes. "
        f"One check per catalog entry; {len(entries)} checks.",
        "",
    ]
    for s in SERIES:
        out.append(f"### {s} ({len(by_series[s])})")
        for e in by_series[s]:
            out.append(SEP.join([f"- {e['id']}", e["pattern"], e["rule"], ", ".join(refs[e["id"]])]))
        out.append("")
    return "\n".join(out) + "\n"


def splice(section):
    text = SKILL.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    start = next((i for i, l in enumerate(lines) if l.rstrip("\n") == "## Checks"), None)
    end = next((i for i, l in enumerate(lines) if l.rstrip("\n") == "## References"), None)
    if start is None or end is None or end <= start:
        fail("could not locate '## Checks' … '## References' in SKILL.md")
    new = "".join(lines[:start]) + section + "".join(lines[end:])
    if new != text:
        SKILL.write_text(new, encoding="utf-8")
        return True
    return False


def main():
    entries = parse_catalog()
    refs = reference_files_by_id()
    changed = splice(build_section(entries, refs))
    print(f"{len(entries)} checks; SKILL.md {'updated' if changed else 'unchanged'}")


if __name__ == "__main__":
    main()
