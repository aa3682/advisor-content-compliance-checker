#!/usr/bin/env python3
"""Score a recorded run of the skill against tests/expected/.

Usage:
  python tools/score_run.py <run-id> [--expected-dir DIR]
  python tools/score_run.py --selftest

Implements RULINGS.md phase6-fixture-format and phase6-pass-criteria, plus the
What-line subtraction in the clearance scan (a What line is a verbatim catalog
Pattern, not the skill's own words). Scores tests/runs/<run-id>/ and writes
tests/runs/<run-id>/RESULTS.md. Exit code 0 only when the run passes. A sample listed
in the run directory's CONTAMINATED.txt (run-isolation) fails with reason "contaminated"
and is not otherwise scored.

The catalog parser is imported from tools/build_check_index.py; there is no
second parser.

What and Where lines are subtracted from the clearance scan because they carry
catalog and content text; U4 (What equals the cited Pattern) and U5 (every Where
quote is a substring of the fixture) make that true.
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_check_index import ROOT, SKILL, REFS_DIR, parse_catalog  # noqa: E402

try:
    import yaml
except ImportError:
    sys.stderr.write("score_run: PyYAML is required. Install it with: python -m pip install pyyaml\n")
    sys.exit(2)

TESTS = ROOT / "tests"
FIXTURES = TESTS / "fixtures"
RUNS = TESTS / "runs"
EXPECTED_DEFAULT = TESTS / "expected"
TERMS = TESTS / "clearance_terms.txt"
SELFTEST = TESTS / "selftest"

CLOSING = "Pre-review only. Not legal or compliance advice. Confirm with your CCO or counsel."
SEP = " · "
ID_RE = re.compile(r"^(?:GP|PERF|TE|TPR)-\d+$")
FLAGS_RE = re.compile(r"^Flags: (\d+)\. Confirm: (\d+)\.$")
FLAG_HEAD_RE = re.compile(r"^Flag (\d+)$")
CONFIRM_HEAD_RE = re.compile(r"^Confirm (\d+)$")
FIELD_RE = re.compile(r"^(Where|What|Cite|Fix|Depends on|Would apply): ?(.*)$")
QUOTE_RE = re.compile(r'"[^"]*"|“[^”]*”')
FLAG_FIELDS = ["Where", "What", "Cite", "Fix"]
CONFIRM_FIELDS = ["Where", "Depends on", "Cite", "Would apply"]
UNIVERSAL = ["U1", "U2", "U3", "U4", "U5"]
PER_FIXTURE = ["P1", "P2", "P3", "P4", "P5"]


# ---------------------------------------------------------------- inputs

def fail(msg):
    sys.stderr.write(f"score_run: {msg}\n")
    sys.exit(1)


def load_template():
    """Read the two fences under Output contract in skill/SKILL.md: the template (lines printed on
    every output) and the conditional lines (Scope, Not reviewed, Zero flags, exactly as printed)."""
    text = SKILL.read_text(encoding="utf-8")
    sec = re.search(r"^### Output contract\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    fences = re.findall(r"^```\n(.*?)^```", sec.group(1), re.S | re.M) if sec else []
    if len(fences) < 2:
        fail("could not locate the template fence and the conditional-lines fence in skill/SKILL.md")
    lines = fences[0].splitlines()          # lines printed on every output
    cond = fences[1].splitlines()           # conditional lines, exactly as printed (template-no-brackets)

    def find(prefix, pool=None):
        for l in (lines if pool is None else pool):
            if l.startswith(prefix):
                return l
        fail(f"template line starting with {prefix!r} not found in skill/SKILL.md")

    t = {
        "title": find("Marketing Rule"),
        "elements_prefix": "Elements detected: ",
        "reviewed": find("Reviewed as an advertisement"),
        "state": find("State-registered advisers"),
        "no_match": next(l for l in cond if not l.startswith("Scope:") and not l.startswith("Not reviewed:")),
        "closing": find("Pre-review only."),
    }
    if any("[" in l or "]" in l for l in lines + cond):
        fail("square brackets in the SKILL.md fences (template-no-brackets)")
    scope = find("Scope:", cond)
    nr = find("Not reviewed:", cond)
    t["scope_re"] = re.compile("^" + re.escape(scope).replace(re.escape("<marker>"), "(.+?)") + "$")
    t["not_reviewed_re"] = re.compile(
        "^" + re.escape(nr).replace(re.escape("<image or attachment>"), "(.+?)") + "$")
    if t["closing"] != CLOSING:
        fail("closing line in skill/SKILL.md differs from the scorer's constant; update one deliberately")
    # fixed lines that legitimately carry clearance vocabulary (subtracted in U2)
    t["subtract_fixed"] = [l for l in (t["no_match"], t["closing"], t["title"], t["reviewed"], t["state"])
                           if "clearance" in l.lower() or "compliance" in l.lower()]
    return t


def load_catalog():
    cat = {}
    for e in parse_catalog():
        cat[e["id"]] = {
            "pattern": e["pattern"],
            "paragraphs": frozenset(p.strip() for p in e["rule"].split(",")),
            "source": e["source"].split(";")[0].strip(),
        }
    return cat


def load_reference_tokens():
    """Every heading token and paragraph label in skill/references/*.md, e.g. (e)(17), (b)(1)(i)."""
    tokens = set()
    head_re = re.compile(r"^#{1,4} (\([a-z]\)(?:\(\w+\))*)")
    label_re = re.compile(r"^\(([a-z]|\d+|[ivx]+|[A-Z])\)")
    for path in sorted(REFS_DIR.glob("*.md")):
        letter = number = roman = None
        for line in path.read_text(encoding="utf-8").splitlines():
            h = head_re.match(line)
            if h:
                tokens.add(h.group(1))
                continue
            m = label_re.match(line)
            if not m:
                continue
            lab = m.group(1)
            if re.fullmatch(r"[a-z]", lab) and len(lab) == 1 and lab not in "ivx":
                letter, number, roman = lab, None, None
                tokens.add(f"({letter})")
            elif lab.isdigit() and letter:
                number, roman = lab, None
                tokens.add(f"({letter})({number})")
            elif re.fullmatch(r"[ivx]+", lab) and letter and number:
                roman = lab
                tokens.add(f"({letter})({number})({roman})")
            elif re.fullmatch(r"[A-Z]", lab) and letter and number and roman:
                tokens.add(f"({letter})({number})({roman})({lab})")
    return tokens


def load_terms():
    terms = []
    for i, line in enumerate(TERMS.read_text(encoding="utf-8").splitlines()):
        if i == 0 and line.startswith("#"):
            continue
        if line.strip():
            terms.append(line.strip().lower())
    return terms


def load_manifest(run_dir):
    path = run_dir / "MANIFEST.md"
    fields = {}
    if path.is_file():
        for line in path.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^-?\s*(\w+):\s*(.*)$", line)
            if m:
                fields[m.group(1)] = m.group(2).strip()
    return fields


def load_expected(expected_dir, fixture_id):
    path = expected_dir / f"{fixture_id}.yaml"
    if not path.is_file():
        return None
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    req = []
    for item in data.get("required") or []:
        if isinstance(item, str):
            req.append({"id": item, "where": None})
        else:
            w = item.get("where")
            req.append({"id": item["id"], "where": [w] if isinstance(w, str) else (list(w) if w else None)})
    data["required"] = req
    data["forbidden"] = list(data.get("forbidden") or [])
    data["confirm"] = [{"would_apply": list(c.get("would_apply") or [])} for c in (data.get("confirm") or [])]
    data["elements"] = list(data.get("elements") or [])
    data.setdefault("scope", None)
    data.setdefault("not_reviewed", None)
    data.setdefault("no_match", False)
    return data


# ---------------------------------------------------------------- parsing a sample

def parse_sample(text, t):
    """Parse one output into header, blocks and flags. Structural problems land in s['u3']."""
    raw = [l.rstrip("\r") for l in text.splitlines()]
    s = {"lines": raw, "u3": [], "elements_line": None, "scope": [], "not_reviewed": [],
         "n": None, "m": None, "flags": [], "confirms": [], "no_match": False,
         "closing_idx": None, "flags_idx": None}
    nonblank = [(i, l) for i, l in enumerate(raw) if l.strip()]
    # header, in template order
    seq = iter(nonblank)
    def nxt():
        try:
            return next(seq)
        except StopIteration:
            return (None, None)
    i, l = nxt()
    if l != t["title"]:
        s["u3"].append("title line missing or altered")
    i, l = nxt()
    if l is not None and l.startswith(t["elements_prefix"]):
        s["elements_line"] = l[len(t["elements_prefix"]):]
    else:
        s["u3"].append("Elements detected line missing or out of order")
    i, l = nxt()
    if l != t["reviewed"]:
        s["u3"].append("Reviewed-as line missing or out of order")
    i, l = nxt()
    while l is not None and t["scope_re"].match(l):
        s["scope"].append(t["scope_re"].match(l).group(1))
        i, l = nxt()
    while l is not None and t["not_reviewed_re"].match(l):
        s["not_reviewed"].append(t["not_reviewed_re"].match(l).group(1))
        i, l = nxt()
    if l != t["state"]:
        s["u3"].append("State line missing or out of order")
    i, l = nxt()
    fm = FLAGS_RE.match(l or "")
    if fm:
        s["n"], s["m"] = int(fm.group(1)), int(fm.group(2))
        s["flags_idx"] = i
    else:
        s["u3"].append("Flags/Confirm count line missing or malformed")
        # try to recover it anywhere so block checks can still run
        for j, x in nonblank:
            fm = FLAGS_RE.match(x)
            if fm:
                s["n"], s["m"] = int(fm.group(1)), int(fm.group(2))
                s["flags_idx"] = j
                break
    if s["flags_idx"] is None:
        return s
    # body
    cur = None
    for j in range(s["flags_idx"] + 1, len(raw)):
        l = raw[j]
        if not l.strip():
            continue
        if l == t["closing"]:
            s["closing_idx"] = j
            break
        if l == t["no_match"]:
            s["no_match"] = True
            cur = None
            continue
        fh, ch = FLAG_HEAD_RE.match(l), CONFIRM_HEAD_RE.match(l)
        if fh:
            cur = {"kind": "flag", "num": int(fh.group(1)), "fields": {}}
            s["flags"].append(cur)
            continue
        if ch:
            cur = {"kind": "confirm", "num": int(ch.group(1)), "fields": {}}
            s["confirms"].append(cur)
            continue
        fm = FIELD_RE.match(l)
        if fm and cur is not None:
            cur["fields"][fm.group(1)] = fm.group(2)
            continue
        s["u3"].append(f"unexpected line: {l[:60]!r}")
    for b in s["flags"]:
        b["id"] = None
        parts = b["fields"].get("Cite", "").split(SEP)
        if len(parts) == 3 and ID_RE.match(parts[1].strip()):
            b["id"] = parts[1].strip()
    for b in s["confirms"]:
        wa = b["fields"].get("Would apply", "")
        b["would_apply"] = [x.strip() for x in re.split(r",\s*", wa) if x.strip()]
    return s


# ---------------------------------------------------------------- assertions

def check_u1(s, t):
    r = []
    nonblank = [l for l in s["lines"] if l.strip()]
    if t["closing"] not in nonblank:
        r.append("closing line missing")
    elif nonblank[-1] != t["closing"]:
        r.append("text follows the closing line")
    return r


def check_u2(s, t, terms):
    r = []
    for l in s["lines"]:
        if not l.strip() or l in t["subtract_fixed"]:
            continue
        fm = FIELD_RE.match(l)
        if fm and fm.group(1) == "What":
            continue
        scan = QUOTE_RE.sub("", l) if fm and fm.group(1) == "Where" else l
        low = scan.lower()
        for term in terms:
            if term in low:
                r.append(f"term {term!r} in line {l[:60]!r}")
                break
    return r


def check_u3(s, t):
    r = list(s["u3"])
    if s["flags_idx"] is None:
        return r
    n, m = s["n"], s["m"]
    flags, confirms = s["flags"], s["confirms"]
    if len(flags) != n:
        r.append(f"Flags: {n} but {len(flags)} Flag block(s)")
    if len(confirms) != m:
        r.append(f"Confirm: {m} but {len(confirms)} Confirm block(s)")
    if [b["num"] for b in flags] != list(range(1, len(flags) + 1)):
        r.append("Flag blocks not numbered 1..n without gaps")
    if [b["num"] for b in confirms] != list(range(1, len(confirms) + 1)):
        r.append("Confirm blocks not numbered 1..m without gaps")
    if m == 0 and confirms:
        r.append("Confirm section present with Confirm: 0")
    if n == 0 and not s["no_match"]:
        r.append("Zero-flags line absent with Flags: 0")
    if n != 0 and s["no_match"]:
        r.append(f"Zero-flags line present with Flags: {n}")
    seen = {}
    for b in flags:
        if b["id"]:
            seen.setdefault(b["id"], []).append(b["num"])
    for cid, nums in seen.items():
        if len(nums) > 1:
            r.append(f"{cid} appears in Flag blocks {', '.join(map(str, nums))}; one Flag block per catalog ID")
    for b in flags:
        missing = [f for f in FLAG_FIELDS if f not in b["fields"]]
        if missing:
            r.append(f"Flag {b['num']} missing {', '.join(missing)}")
    for b in confirms:
        missing = [f for f in CONFIRM_FIELDS if f not in b["fields"]]
        if missing:
            r.append(f"Confirm {b['num']} missing {', '.join(missing)}")
    seq = []
    for l in s["lines"]:
        if FLAG_HEAD_RE.match(l):
            seq.append("flag")
        elif CONFIRM_HEAD_RE.match(l):
            seq.append("confirm")
    if seq != sorted(seq, key=lambda k: 0 if k == "flag" else 1):
        r.append("a Flag block follows a Confirm block")
    return r


def check_u4(s, cat, ref_tokens):
    r = []
    for b in s["flags"]:
        cite = b["fields"].get("Cite", "")
        parts = [p.strip() for p in cite.split(SEP)]
        if len(parts) != 3:
            r.append(f"Flag {b['num']} Cite has {len(parts)} token(s), not 3")
            continue
        paras, cid, source = parts
        if cid not in cat:
            r.append(f"Flag {b['num']} Cite ID {cid!r} not in catalog")
            continue
        got = frozenset(p.strip() for p in paras.split(","))
        if got != cat[cid]["paragraphs"]:
            r.append(f"Flag {b['num']} paragraph set {paras!r} != catalog {', '.join(sorted(cat[cid]['paragraphs']))!r}")
        if source != cat[cid]["source"]:
            r.append(f"Flag {b['num']} source {source!r} != catalog {cat[cid]['source']!r}")
        what = b["fields"].get("What", "").strip()
        if what != cat[cid]["pattern"]:
            r.append(f"Flag {b['num']} What {what[:50]!r} != catalog Pattern for {cid}")
    for b in s["confirms"]:
        cite = b["fields"].get("Cite", "")
        if not any(tok in cite for tok in ref_tokens):
            r.append(f"Confirm {b['num']} Cite {cite[:40]!r} names no reference-file heading or paragraph label")
        for cid in b["would_apply"]:
            if cid not in cat:
                r.append(f"Confirm {b['num']} Would apply ID {cid!r} not in catalog")
    return r


def collapse_ws(text):
    return " ".join(text.split())


def check_u5(s, fixture_text):
    """Provenance: every quoted span on every Where line is a substring of the fixture."""
    r = []
    if fixture_text is None:
        return ["fixture file not found in tests/fixtures/"]
    hay = collapse_ws(fixture_text)
    for b in s["flags"] + s["confirms"]:
        label = f"{b['kind'].capitalize()} {b['num']}"
        where = b["fields"].get("Where")
        if where is None:
            continue  # missing field is U3's finding
        spans = QUOTE_RE.findall(where)
        if not spans:
            r.append(f"{label} Where carries no quoted span")
            continue
        for span in spans:
            needle = collapse_ws(span[1:-1])
            if needle and needle not in hay:
                r.append(f"{label} Where quote {needle[:50]!r} is not in the fixture")
    return r


def check_per_fixture(s, exp):
    res = {k: [] for k in PER_FIXTURE}
    # P1 elements
    line = s["elements_line"]
    want = set(exp["elements"])
    if line is None:
        res["P1"].append("Elements detected line missing")
    elif not want:
        if line.strip() != "none":
            res["P1"].append(f"expected 'none', got {line!r}")
    else:
        got = {x.strip() for x in line.split(",") if x.strip()}
        if got != want:
            res["P1"].append(f"expected {sorted(want)}, got {sorted(got)}")
    # P2 required
    flag_ids = [b["id"] for b in s["flags"]]
    for req in exp["required"]:
        hits = [b for b in s["flags"] if b["id"] == req["id"]]
        if not hits:
            res["P2"].append(f"required {req['id']} not flagged")
        elif req["where"] and not any(any(w in b["fields"].get("Where", "") for w in req["where"]) for b in hits):
            res["P2"].append(f"{req['id']} flagged but Where lacks any of {req['where']!r}")
    # P3 forbidden
    wa_ids = [cid for b in s["confirms"] for cid in b["would_apply"]]
    for fid in exp["forbidden"]:
        if fid in flag_ids:
            res["P3"].append(f"forbidden {fid} flagged")
        if fid in wa_ids:
            res["P3"].append(f"forbidden {fid} under Would apply")
    # P4 confirm (would-apply-subset): every expected ID appears on the Would apply
    # line of some Confirm block; IDs beyond the expected set are extras, not failures
    for c in exp["confirm"]:
        missing = [cid for cid in c["would_apply"] if cid not in wa_ids]
        if missing:
            res["P4"].append(f"no Confirm block lists Would apply {missing}")
    # P5 lines
    if exp["scope"]:
        if len(s["scope"]) != 1:
            res["P5"].append(f"expected one Scope line, found {len(s['scope'])}")
        elif exp["scope"].lower() not in s["scope"][0].lower():
            res["P5"].append(f"Scope marker {s['scope'][0]!r} lacks {exp['scope']!r}")
    elif s["scope"]:
        res["P5"].append("Scope line present but not expected")
    if exp["not_reviewed"]:
        if len(s["not_reviewed"]) != 1:
            res["P5"].append(f"expected one Not reviewed line, found {len(s['not_reviewed'])}")
        elif exp["not_reviewed"].lower() not in s["not_reviewed"][0].lower():
            res["P5"].append(f"Not reviewed item {s['not_reviewed'][0]!r} lacks {exp['not_reviewed']!r}")
    elif s["not_reviewed"]:
        res["P5"].append("Not reviewed line present but not expected")
    if bool(exp["no_match"]) != s["no_match"]:
        res["P5"].append("Zero-flags line " + ("expected but absent" if exp["no_match"] else "present but not expected"))
    # extras
    known = {r["id"] for r in exp["required"]} | set(exp["forbidden"]) | {
        cid for c in exp["confirm"] for cid in c["would_apply"]}
    extras = sorted({x for x in flag_ids + wa_ids if x and x not in known})
    return res, extras


# ---------------------------------------------------------------- scoring a run

def score_sample(text, exp, ctx, fixture_id):
    s = parse_sample(text, ctx["t"])
    fixture_path = FIXTURES / f"{fixture_id}.md"
    fixture_text = fixture_path.read_text(encoding="utf-8") if fixture_path.is_file() else None
    failed = {}
    for name, r in (("U1", check_u1(s, ctx["t"])), ("U2", check_u2(s, ctx["t"], ctx["terms"])),
                    ("U3", check_u3(s, ctx["t"])), ("U4", check_u4(s, ctx["cat"], ctx["ref_tokens"])),
                    ("U5", check_u5(s, fixture_text))):
        if r:
            failed[name] = r
    extras = []
    if exp is not None:
        per, extras = check_per_fixture(s, exp)
        for name in PER_FIXTURE:
            if per[name]:
                failed[name] = per[name]
    return failed, extras


def score_dir(run_dir, expected_dir, ctx):
    sample_re = re.compile(r"^(.+)\.(\d+)\.md$")
    samples = {}
    for path in sorted(run_dir.iterdir()):
        m = sample_re.match(path.name)
        if m:
            samples[(m.group(1), int(m.group(2)))] = path
    runlist = run_dir / "RUNLIST.tsv"
    if runlist.is_file():  # every listed sample is scored; a missing output is a failed sample
        for line in runlist.read_text(encoding="utf-8").splitlines()[1:]:
            parts = line.split("\t")
            if len(parts) >= 2 and parts[1].isdigit():
                samples.setdefault((parts[0], int(parts[1])), None)
    contaminated = {}
    cfile = run_dir / "CONTAMINATED.txt"
    if cfile.is_file():  # fixture<TAB>k<TAB>what was read (run-isolation)
        for line in cfile.read_text(encoding="utf-8").splitlines():
            parts = line.split("\t")
            if len(parts) >= 2 and parts[1].strip().isdigit():
                contaminated[(parts[0].strip(), int(parts[1]))] = parts[2].strip() if len(parts) > 2 else ""
    rows = []
    for (fid, k), path in sorted(samples.items()):
        exp = load_expected(expected_dir, fid)
        if (fid, k) in contaminated:
            cat = exp["category"] if exp else "?"
            rows.append({"fixture": fid, "k": k, "class": "entry" if cat == "entry" else "adversarial",
                         "failed": {"contaminated": [contaminated[(fid, k)] or "reported reading outside its directory"]},
                         "extras": []})
            continue
        if path is None:
            cat = exp["category"] if exp else "?"
            rows.append({"fixture": fid, "k": k, "class": "entry" if cat == "entry" else "adversarial",
                         "failed": {"U0": ["missing output"]}, "extras": []})
            continue
        failed, extras = score_sample(path.read_text(encoding="utf-8"), exp, ctx, fid)
        if exp is None:
            failed["P0"] = [f"no expected file {fid}.yaml"]
        cat = exp["category"] if exp else "?"
        rows.append({"fixture": fid, "k": k, "class": "entry" if cat == "entry" else "adversarial",
                     "failed": failed, "extras": extras})
    return rows


def write_results(run_dir, manifest, rows):
    fixtures = {}
    for r in rows:
        fixtures.setdefault((r["class"], r["fixture"]), []).append(not r["failed"])
    out = ["# Results", ""]
    for k in ("run_id", "date", "skill_commit", "model", "fixtures", "n_entry", "n_adversarial", "notes"):
        out.append(f"- {k}: {manifest.get(k, '')}")
    out += ["", "| fixture | k | verdict | failed checks | extras |", "|---|---|---|---|---|"]
    for r in rows:
        checks = "; ".join(f"{n}: {' / '.join(v)}" for n, v in r["failed"].items()).replace("|", "\\|")
        verdict = "PASS" if not r["failed"] else "FAIL"
        out.append(f"| {r['fixture']} | {r['k']} | {verdict} | {checks} | {', '.join(r['extras'])} |")
    out += ["", "## Totals", ""]
    for cls in ("entry", "adversarial"):
        srows = [r for r in rows if r["class"] == cls]
        fx = {f: all(v) for (c, f), v in fixtures.items() if c == cls}
        out.append(f"- {cls}: samples {sum(1 for r in srows if not r['failed'])}/{len(srows)} pass; "
                   f"fixtures {sum(fx.values())}/{len(fx)} pass")
    passed = bool(rows) and all(not r["failed"] for r in rows)
    out += ["", "RUN: PASS" if passed else "RUN: FAIL"]
    (run_dir / "RESULTS.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    return passed


def build_ctx():
    return {"t": load_template(), "cat": load_catalog(), "ref_tokens": load_reference_tokens(),
            "terms": load_terms()}


def selftest():
    run_dir, expected_dir = SELFTEST / "run", SELFTEST / "expected"
    spec = yaml.safe_load((SELFTEST / "EXPECTED.yaml").read_text(encoding="utf-8"))["samples"]
    ctx = build_ctx()
    rows = score_dir(run_dir, expected_dir, ctx)
    write_results(run_dir, load_manifest(run_dir), rows)
    by_key = {(r["fixture"], r["k"]): r for r in rows}
    ok = True
    for fid in spec:
        for k in sorted(spec[fid]):
            want_v = spec[fid][k]["verdict"]
            want_c = sorted(spec[fid][k].get("checks") or [])
            r = by_key.get((fid, int(k)))
            if r is None:
                print(f"{fid} k={k}: expected {want_v} {want_c}; actual: sample missing; MISMATCH")
                ok = False
                continue
            got_v = "fail" if r["failed"] else "pass"
            got_c = sorted(r["failed"])
            match = (want_v == got_v) and (want_c == got_c)
            ok = ok and match
            extras = f"; extras {r['extras']}" if r["extras"] else ""
            print(f"{fid} k={k}: expected {want_v} {want_c}; actual {got_v} {got_c}{extras}; {'match' if match else 'MISMATCH'}")
    print("SELFTEST: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_id", nargs="?")
    ap.add_argument("--expected-dir", default=str(EXPECTED_DEFAULT))
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.run_id:
        ap.error("run-id required unless --selftest")
    run_dir = RUNS / a.run_id
    if not run_dir.is_dir():
        fail(f"run directory not found: {run_dir.relative_to(ROOT)}")
    ctx = build_ctx()
    rows = score_dir(run_dir, Path(a.expected_dir), ctx)
    if not rows:
        fail("no samples (<fixture-id>.<k>.md) in run directory")
    passed = write_results(run_dir, load_manifest(run_dir), rows)
    print(f"{len(rows)} samples scored; RESULTS.md written; RUN: {'PASS' if passed else 'FAIL'}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
