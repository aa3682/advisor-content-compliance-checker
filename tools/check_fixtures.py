#!/usr/bin/env python3
"""Validate the fixture set without running anything.

Usage: python tools/check_fixtures.py [--final]

Checks pairing between tests/fixtures/ and tests/expected/, the expected-file
schema (tests/expected/SCHEMA.md), fixture-file hygiene, where-substrings, and
coverage against RULINGS.md phase6-fixture-format and
phase6-adversarial-categories. Coverage is informational by default; with
--final any shortfall fails. Uses the catalog parser from
tools/build_check_index.py. Prints one line per problem, the coverage block,
then CHECK: PASS or CHECK: FAIL; exit code matches.
"""
import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_check_index import ROOT, parse_catalog  # noqa: E402

try:
    import yaml
except ImportError:
    sys.stderr.write("check_fixtures: PyYAML is required. Install it with: python -m pip install pyyaml\n")
    sys.exit(2)

FIXTURES = ROOT / "tests" / "fixtures"
EXPECTED = ROOT / "tests" / "expected"
CATEGORIES = ["CLR", "VRQ", "NOM", "CUR", "OVL", "CNF", "SCP", "UNR"]
MIN_PER_CATEGORY = 3
MAX_WHERE = 60  # ruling elements-convention
ENTRY_ID_RE = re.compile(r"^((?:GP|PERF|TE|TPR)-\d+)-(\d+)$")
ADV_ID_RE = re.compile(r"^(" + "|".join(CATEGORIES) + r")-(\d{2})$")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--final", action="store_true", help="coverage shortfalls fail the check")
    a = ap.parse_args()

    catalog_ids = [e["id"] for e in parse_catalog()]
    catalog = set(catalog_ids)
    problems = []
    warnings = []

    fixture_ids = {p.stem for p in FIXTURES.glob("*.md")}
    expected_ids = {p.stem for p in EXPECTED.glob("*.yaml")}
    for fid in sorted(fixture_ids - expected_ids):
        problems.append(f"{fid}: fixture has no expected file")
    for fid in sorted(expected_ids - fixture_ids):
        problems.append(f"{fid}: expected file has no fixture")

    entry_cover = Counter()
    adv_count = Counter()
    scp_scopes = set()
    unr_with = unr_without = 0

    for fid in sorted(fixture_ids & expected_ids):
        content = (FIXTURES / f"{fid}.md").read_text(encoding="utf-8")
        if not content.strip():
            problems.append(f"{fid}: fixture file is empty")
        if content.startswith("---"):
            problems.append(f"{fid}: fixture first line starts with '---' (frontmatter is not allowed)")
        if fid in content:
            problems.append(f"{fid}: fixture contains its own fixture ID")
        try:
            data = yaml.safe_load((EXPECTED / f"{fid}.yaml").read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            problems.append(f"{fid}: expected file does not parse: {str(exc).splitlines()[0]}")
            continue
        if not isinstance(data, dict):
            problems.append(f"{fid}: expected file is not a mapping")
            continue
        if data.get("id") != fid:
            problems.append(f"{fid}: id field {data.get('id')!r} != filename stem")
        cat = data.get("category")
        if cat != "entry" and cat not in CATEGORIES:
            problems.append(f"{fid}: category {cat!r} is not entry or one of {' '.join(CATEGORIES)}")
        targets = list(data.get("targets") or [])
        required = []
        for item in data.get("required") or []:
            if isinstance(item, str):
                required.append({"id": item, "where": None})
            elif isinstance(item, dict) and "id" in item:
                required.append({"id": item["id"], "where": item.get("where")})
            else:
                problems.append(f"{fid}: required item {item!r} is neither an ID nor a mapping with id")
        forbidden = list(data.get("forbidden") or [])
        would_apply = [cid for c in (data.get("confirm") or []) for cid in (c.get("would_apply") or [])]
        for field, ids in (("targets", targets), ("required", [r["id"] for r in required]),
                           ("forbidden", forbidden), ("confirm.would_apply", would_apply)):
            for cid in ids:
                if cid not in catalog:
                    problems.append(f"{fid}: {field} ID {cid!r} not in catalog")
        if "elements" not in data:
            problems.append(f"{fid}: elements field missing")
        m_entry, m_adv = ENTRY_ID_RE.match(fid), ADV_ID_RE.match(fid)
        if cat == "entry":
            if not m_entry:
                problems.append(f"{fid}: entry fixture ID is not <catalog-ID>-<n>")
            else:
                if m_entry.group(1) not in targets:
                    problems.append(f"{fid}: entry fixture's catalog ID {m_entry.group(1)} is not in targets")
                if m_entry.group(1) in catalog:
                    entry_cover[m_entry.group(1)] += 1
        elif cat in CATEGORIES:
            if not m_adv:
                problems.append(f"{fid}: adversarial fixture ID is not <category>-<nn>")
            elif m_adv.group(1) != cat:
                problems.append(f"{fid}: ID prefix {m_adv.group(1)} != category {cat}")
            adv_count[cat] += 1
            if cat == "SCP":
                scp_scopes.add(str(data.get("scope")))
            if cat == "UNR":
                if data.get("not_reviewed"):
                    unr_with += 1
                else:
                    unr_without += 1
        for r in required:
            anchors = [r["where"]] if isinstance(r["where"], str) else list(r["where"] or [])
            for w in anchors:  # where may be a string or an any-of list (where-anyof)
                if w not in content:
                    problems.append(f"{fid}: required {r['id']} where {w!r} is not a substring of the fixture")
                if len(w) > MAX_WHERE:
                    warnings.append(f"{fid}: required {r['id']} where is {len(w)} characters, over {MAX_WHERE} (elements-convention)")

    for line in problems:
        print(line)
    for line in warnings:
        print("warning: " + line)

    uncovered = [cid for cid in catalog_ids if entry_cover[cid] == 0]
    shortfalls = []
    print("Coverage:")
    print(f"  entry fixtures: {sum(entry_cover.values())} across {len(catalog_ids) - len(uncovered)}/{len(catalog_ids)} catalog entries")
    print(f"  catalog entries with zero entry fixtures ({len(uncovered)}): {', '.join(uncovered) if uncovered else 'none'}")
    if uncovered:
        shortfalls.append(f"{len(uncovered)} catalog entries without an entry fixture")
    for c in CATEGORIES:
        n = adv_count[c]
        flag = "" if n >= MIN_PER_CATEGORY else f"  (below minimum {MIN_PER_CATEGORY})"
        print(f"  {c}: {n}{flag}")
        if n < MIN_PER_CATEGORY:
            shortfalls.append(f"{c} has {n} fixtures, minimum {MIN_PER_CATEGORY}")
    print(f"  SCP distinct scope values ({len(scp_scopes)}): {', '.join(sorted(scp_scopes)) if scp_scopes else 'none'}")
    if len(scp_scopes) < 4:
        shortfalls.append(f"SCP covers {len(scp_scopes)} distinct scope values, minimum 4")
    print(f"  UNR with not_reviewed: {unr_with}; without: {unr_without}")
    if unr_with < 1 or unr_without < 1:
        shortfalls.append("UNR needs at least one fixture with and one without not_reviewed")

    failed = bool(problems) or (a.final and bool(shortfalls))
    if a.final and shortfalls:
        for sf in shortfalls:
            print(f"coverage shortfall: {sf}")
    print("CHECK: " + ("FAIL" if failed else "PASS"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
