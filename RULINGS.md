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
