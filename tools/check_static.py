#!/usr/bin/env python3
"""Static assertions on the catalog, reference files, check index and expected files.

Usage: python tools/check_static.py

No run is needed. One named check each, per RULINGS.md:
  S1 check-index-generator: regenerating the check index changes nothing in skill/SKILL.md
     (computed on a copy; SKILL.md is never written).
  S2 entries-to-checks: no two catalog entries share both paragraph set and Pattern.
  S3 reference-file-shape / output-shape: every entry line in skill/references/*.md matches
     its catalog line: ID exists, Pattern equal, source field equal to the catalog's (so the
     first-listed source through the first ";" is equal too), and any "(catalog cite: …)"
     annotation equal to the catalog paragraph set.
  S4 entries-to-checks: every check-index line matches a catalog entry's Pattern and paragraph
     set, names only reference files that exist and carry that entry, and every catalog entry
     appears in the index exactly once.
  S5 skill-procedure / rules-last-verified: the closing line is in SKILL.md's template verbatim;
     "Rules last verified" carries one date across SKILL.md, README.md and every reference file;
     SKILL.md is at most 500 lines.
  S6 phase6-fixture-format: every catalog ID named in tests/expected/*.yaml exists in the catalog.
  S7 cite-token-shape: every catalog Rule field is paragraph tokens only, separated by ", "
     — no prose, no alternative separator. The field is parsed as a token set by this file's
     paragraph_set and by the scorer's U4, so prose in it is a format violation.
Prints one line per problem, then STATIC: PASS or STATIC: FAIL; exit code matches.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_check_index import (ROOT, SKILL, REFS_DIR, REF_ORDER, SEP, FIELD_SEP,  # noqa: E402
                               parse_catalog, reference_files_by_id, build_section)

try:
    import yaml
except ImportError:
    sys.stderr.write("check_static: PyYAML is required. Install it with: python -m pip install pyyaml\n")
    sys.exit(2)

README = ROOT / "README.md"
EXPECTED = ROOT / "tests" / "expected"
CLOSING = "Pre-review only. Not legal or compliance advice. Confirm with your CCO or counsel."
MAX_SKILL_LINES = 500
REF_LINE_RE = re.compile(r"^- ((?:GP|PERF|TE|TPR)-\d+) — (.*)$")
CITE_ANNOT_RE = re.compile(r"\s*\(catalog cite: ([^)]*(?:\([^)]*\))*[^)]*)\)$")
INDEX_LINE_RE = re.compile(r"^- ((?:GP|PERF|TE|TPR)-\d+) · (.*) · (\([^·]*) · (.*)$")
VERIFIED_RE = re.compile(r"Rules last verified: (\d{4}-\d{2}-\d{2})")
# cite-token-shape: (a) / (d)(1) / (b)(1)(i) / (e)(17) and so on; nothing else
PARA_TOKEN_RE = re.compile(r"^\((?:[a-z]|\d+)\)(?:\((?:\d+|[ivx]+|[a-z])\))*$")


def paragraph_set(rule_field):
    return frozenset(p.strip() for p in rule_field.split(","))


def main():
    problems = []
    entries = parse_catalog()
    cat = {e["id"]: e for e in entries}

    # S1 — regenerate on a copy
    section = build_section(entries, reference_files_by_id())
    text = SKILL.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    start = next((i for i, l in enumerate(lines) if l.rstrip("\n") == "## Checks"), None)
    end = next((i for i, l in enumerate(lines) if l.rstrip("\n") == "## References"), None)
    if start is None or end is None or end <= start:
        problems.append("S1: could not locate '## Checks' … '## References' in skill/SKILL.md")
    elif "".join(lines[:start]) + section + "".join(lines[end:]) != text:
        problems.append("S1: regenerating the check index would change skill/SKILL.md (drift)")

    # S2 — paragraph set + Pattern uniqueness
    seen = {}
    for e in entries:
        key = (paragraph_set(e["rule"]), e["pattern"])
        if key in seen:
            problems.append(f"S2: {e['id']} and {seen[key]} share paragraph set {e['rule']!r} and Pattern {e['pattern']!r}")
        seen[key] = e["id"]

    # S3 — reference lines match the catalog
    ref_has = {}
    for path in sorted(REFS_DIR.glob("*.md")):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            m = REF_LINE_RE.match(line)
            if not m:
                continue
            cid, rest = m.group(1), m.group(2)
            loc = f"{path.name}:{lineno}"
            if cid not in cat:
                problems.append(f"S3: {loc}: {cid} is not a catalog entry")
                continue
            ref_has.setdefault(cid, set()).add(path.name)
            annot = CITE_ANNOT_RE.search(rest)
            if annot:
                rest = rest[:annot.start()]
                if paragraph_set(annot.group(1)) != paragraph_set(cat[cid]["rule"]):
                    problems.append(f"S3: {loc}: catalog cite {annot.group(1)!r} != catalog {cat[cid]['rule']!r}")
            parts = rest.split(FIELD_SEP)
            if len(parts) != 2:
                problems.append(f"S3: {loc}: expected 'ID — Pattern — Source', got {len(parts) + 1} fields")
                continue
            pattern, source = parts
            if pattern != cat[cid]["pattern"]:
                problems.append(f"S3: {loc}: Pattern {pattern!r} != catalog {cat[cid]['pattern']!r}")
            if source != cat[cid]["source"]:
                problems.append(f"S3: {loc}: source {source!r} != catalog {cat[cid]['source']!r}")
            elif source.split(";")[0].strip() != cat[cid]["source"].split(";")[0].strip():
                problems.append(f"S3: {loc}: first-listed source differs from catalog")

    # S4 — index lines
    index_count = {}
    for lineno, line in enumerate(text.splitlines(), 1):
        m = INDEX_LINE_RE.match(line)
        if not m:
            continue
        cid, pattern, paras, files = m.groups()
        loc = f"SKILL.md:{lineno}"
        index_count[cid] = index_count.get(cid, 0) + 1
        if cid not in cat:
            problems.append(f"S4: {loc}: {cid} is not a catalog entry")
            continue
        if pattern != cat[cid]["pattern"]:
            problems.append(f"S4: {loc}: Pattern {pattern!r} != catalog {cat[cid]['pattern']!r}")
        if paragraph_set(paras) != paragraph_set(cat[cid]["rule"]):
            problems.append(f"S4: {loc}: paragraphs {paras!r} != catalog {cat[cid]['rule']!r}")
        for name in [f.strip() for f in files.split(",")]:
            if not (REFS_DIR / name).is_file():
                problems.append(f"S4: {loc}: reference file {name} does not exist")
            elif name not in ref_has.get(cid, set()):
                problems.append(f"S4: {loc}: {name} does not carry an entry line for {cid}")
    for cid in cat:
        n = index_count.get(cid, 0)
        if n != 1:
            problems.append(f"S4: {cid} appears {n} times in the check index, expected once")

    # S5 — closing line, verified date, length
    tmpl = re.search(r"^### Output contract\n.*?^```\n(.*?)^```", text, re.S | re.M)
    if not tmpl or CLOSING not in tmpl.group(1).splitlines():
        problems.append("S5: closing line not found verbatim in SKILL.md's fenced template")
    dates = {}
    for path in [SKILL, README] + [REFS_DIR / n for n in REF_ORDER]:
        m = VERIFIED_RE.search(path.read_text(encoding="utf-8")) if path.is_file() else None
        if not m:
            problems.append(f"S5: {path.relative_to(ROOT)}: no 'Rules last verified: <date>' line")
        else:
            dates.setdefault(m.group(1), []).append(path.name)
    if len(dates) > 1:
        problems.append(f"S5: Rules last verified dates differ: {dict(dates)}")
    n_lines = len(text.splitlines())
    if n_lines > MAX_SKILL_LINES:
        problems.append(f"S5: skill/SKILL.md is {n_lines} lines, over {MAX_SKILL_LINES}")

    # S6 — expected-file IDs
    for path in sorted(EXPECTED.glob("*.yaml")):
        try:
            d = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            problems.append(f"S6: {path.name}: does not parse: {str(exc).splitlines()[0]}")
            continue
        ids = list(d.get("targets") or []) + list(d.get("forbidden") or [])
        ids += [r if isinstance(r, str) else r.get("id") for r in (d.get("required") or [])]
        ids += [c for x in (d.get("confirm") or []) for c in (x.get("would_apply") or [])]
        for cid in ids:
            if cid not in cat:
                problems.append(f"S6: {path.name}: ID {cid!r} not in catalog")

    # S7 — Rule field is paragraph tokens only (cite-token-shape)
    for e in entries:
        rule = e["rule"]
        tokens = rule.split(", ")
        if rule != ", ".join(t.strip() for t in tokens) or not all(PARA_TOKEN_RE.match(t) for t in tokens):
            bad = [t for t in tokens if not PARA_TOKEN_RE.match(t)] or [rule]
            problems.append(
                f"S7: {e['id']}: Rule field {rule!r} is not comma-separated paragraph tokens "
                f"(offending: {', '.join(repr(b) for b in bad)}); prose belongs in Observed")

    for line in problems:
        print(line)
    print("STATIC: " + ("FAIL" if problems else "PASS"))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
