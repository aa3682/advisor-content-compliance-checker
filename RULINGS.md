# Rulings
Cited by date and slug.

- 2026-09-18 · repo-name-visibility — Repo is advisor-content-compliance-checker, private until the adversarial test set (Phase 6) passes, then public.
- 2026-09-18 · scope-out — Out of scope: FINRA 2210 broker-dealer content, ERISA/retirement-plan marketing, private fund marketing, non-US rules.
- 2026-09-18 · no-clearance-language — The skill never outputs "compliant" or equivalent clearance language.
- 2026-09-18 · cited-flags-only — Every flag cites a rule section or a named SEC risk alert / enforcement action.
- 2026-09-18 · failure-backed-checks — A check with no documented real failure behind it does not ship.
- 2026-09-18 · own-content-dogfooding — The author's own public content is run through the skill as private dogfooding only; it is not a stated use case. Stated audience stays operating solo/two-person RIAs.
- 2026-09-18 · parent-brand — The checker's parent is the "AI workflows for finance professionals" brand direction, not a Claude Project; no brand project exists. The AI for the Solo Advisor guide holds the Tools entry; the RIA content pipeline holds the demo as a pillar-2 track.
- 2026-09-18 · pointer-compliance-checker — Cross-project pointers placed in the project instructions of AI for the Solo Advisor, AI Stackroom, and RIA content pipeline. Those three are the complete list; no other project references the checker.
- 2026-09-18 · catalog-id-scheme — Failure catalog entries use four series keyed to rule paragraphs: GP (general prohibitions, 206(4)-1(a)), PERF (performance, (a) and (d)), TE (testimonials/endorsements, (b)), TPR (third-party ratings, (c)). Enforcement-derived entries join the same series; no separate enforcement series.
- 2026-09-18 · catalog-entry-shape — Every catalog entry is one line: ID — Observed (what examiners found) — Pattern (what it looks like in content) — Rule paragraph — Source code. Source codes (RA-, EA-, AR, FAQ dates) are defined at the top of catalog/failures.md. An entry with no rule cite or no source does not exist.
- 2026-09-18 · catalog-program-findings — Program-level findings (Compliance Rule, Books and Records Rule, Form ADV, recordkeeping, hedge clauses) are out of checker scope but retained in a closing section of catalog/failures.md for Phase 6 documentation. They never become checks.
- 2026-09-18 · perf-d-reference-scope — Ruled: write. Phase 4 writes (d)(1)–(d)(2) reference text into the performance file on the strength of PERF-03, PERF-04, PERF-10, PERF-11 (gross/net and time-period substance). Their catalog cites stay (a)(1) and (a)(6) as the alerts gave them; the reference file, not the catalog, carries the link to (d)(1)–(d)(2).
- 2026-09-18 · reference-file-layout — skill/references/ holds one file per top-level paragraph of Rule 206(4)-1 that the catalog cites: general-prohibitions.md (a), testimonials-endorsements.md (b), third-party-ratings.md (c), performance.md (d), definitions.md (e). A paragraph or definition with no catalog entry behind it is omitted and named as omitted inside the file; it is added when a documented failure cites it. Current omissions: (d)(3), (d)(4), (d)(5), (d)(7); definitions (e)(6), (e)(12), (e)(14).
- 2026-09-18 · reference-file-shape — Every reference file is: header (source, Rules last verified date, record pointer, definitions-used pointer, paragraphs carried) → rule text verbatim from eCFR with links and italics stripped → "Catalog entries by paragraph," generated from catalog/failures.md by exact cite-token match, one line per entry as ID — Pattern — Source. Entries placed under a paragraph their catalog cite does not name go in a separate section titled for the ruling that placed them, with the catalog cite shown. The catalog is the record; reference files are lookups and are regenerated, never hand-edited.
- 2026-09-18 · rules-last-verified — "Rules last verified" is the date the rule text was checked against eCFR, not the date sources were fetched. First verification 2026-09-18 (eCFR current through 2026-09-16; section last amended 87 FR 22447, Apr. 15, 2022). Each reference file carries the date; README carries it in the status line; SKILL.md carries it from Phase 5. Re-verify quarterly.
- 2026-09-18 · output-shape
  Fix list = one flag per finding, in document order, no severity tiers, no tables.
  Header: Elements detected (per unclassifiable-content); flag count; names Rule 206(4)-1 once.
  Each flag carries four fields:
    Where — exact phrase quoted verbatim, one sentence max
    What  — one line naming the pattern, taken from the catalog Pattern field
    Cite  — <catalog rule paragraphs> · <catalog ID> · <first-listed source, verbatim through the first ";">;
            every token copied from catalog/failures.md, never re-derived;
            multi-paragraph entries carry all paragraphs as listed (GP-01 → (a)(1), (a)(2));
            cross-refs stay in the catalog, the ID is the pointer to them
    Fix   — rewrite, "remove", or "supply X" when the issue is a missing disclosure
  Flags are four fields; no fifth line, per state-divergence.
  No-match case: "No catalog patterns matched. This is not a clearance — the catalog covers documented failures only."
  Every output ends with the mandatory closing line.
  Example Cite: (a)(1) · PERF-03 · RA-2024-04
- 2026-09-18 · entries-to-checks
  One check per catalog entry, 1:1 with catalog/failures.md. No check without an entry; no entry without a check.
  SKILL.md body carries a check index grouped by ID series in catalog order (GP, PERF, TE, TPR).
  Each check is one line: <catalog ID> · <catalog Pattern field> · <catalog rule paragraphs> · <reference file(s) where the entry appears>; every token copied from the catalog; reference file(s) derived from the cite tokens the same way the reference files are.
  Entry detail stays in skill/references/; the check points there.
  The index is generated from the catalog by Claude Code, never hand-edited; Phase 6 diffs index against catalog.
  Overlap: a phrase matching more than one entry produces one flag per entry; no collapsing, no tie-break. Duplicate flags are impossible while no two entries share paragraph set and Pattern; Phase 6 asserts that on the catalog.
- 2026-09-18 · unclassifiable-content
  Header "content type" becomes "Elements detected": a fixed list of rule-defined terms — testimonial (e)(17), endorsement (e)(5), third-party rating (e)(18), gross performance (e)(7), net performance (e)(10), hypothetical performance (e)(8) — tokens copied from skill/references/definitions.md. Extracted, predecessor, and related performance join when their definitions do, per reference-file-layout. Formats (blog, email, social post) are never named.
  Header carries one fixed assumption line: "Reviewed as an advertisement under (e)(1); whether (e)(1) covers this communication is not assessed."
  Out-of-scope markers (broker-dealer/FINRA, private fund, ERISA/retirement plan, non-US regulator): review proceeds; header carries one fixed scope line naming the marker seen and stating the skill does not cover it.
  Fact-dependent matches: a check that would fire only on a fact the content does not state (client status, compensation, gross vs net, hypothetical status) becomes a Confirm item, not a flag. Confirm section sits after the flags; omitted when empty.
  Each Confirm item, four fields:
    Where       — exact phrase, verbatim
    Depends on  — the missing fact as one question
    Cite        — the rule token that decides it: the (e) term, or the (b)/(c)/(d) paragraph that conditions on the fact; copied from the reference file
    Would apply — the catalog ID(s) that fire if the answer is yes
  No Confirm item without at least one catalog ID in Would apply.
  Nothing in the header or a Confirm item states or implies clearance; the no-match sentence and closing line apply unchanged.
- 2026-09-18 · state-divergence
  Header carries one fixed state line: "State-registered advisers are subject to their state's rule, which may differ from any flag below; differences are not resolved here."
  No per-flag state notes in v1. Flags are four fields (Where, What, Cite, Fix); no fifth line.
  Per-flag state notes require a verified state source in catalog/sources.md and a per-entry marker in the catalog; neither exists, and adding them is a separate sourcing ruling, not a Phase 5 task.
  The state line never names a state, a state rule, or a direction of divergence.
- 2026-09-18 · branch-merge-cadence
  Cloud sessions commit on session branches; main is fast-forwarded (--ff-only) at every sub-phase close. A sub-phase or phase closes only on a main hash.
- 2026-09-18 · check-index-generator
  The check index in skill/SKILL.md is produced by tools/build_check_index.py from catalog/failures.md and is never hand-edited. Rerunning the script is the drift check: Phase 6 and every quarterly re-verify run it and require no change to SKILL.md.
- 2026-09-18 · skill-procedure
  Runtime Cite tokens are copied from the entry in the reference file named on the check line, not from the check index. Content the skill cannot read gets one fixed header line: "Not reviewed: <image or attachment>." A request for a verdict is answered with the review, never with yes or no; the output contract carries the prohibited-phrasing list.
