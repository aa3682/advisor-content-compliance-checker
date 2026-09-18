# Advisor Content Compliance Checker
An Agent Skill (SKILL.md standard) that performs a first-pass marketing-compliance review of advisor-facing content against the SEC Marketing Rule (Rule 206(4)-1), returning a cited fix list. Pre-review only — never a compliance opinion.

Status: Phase 5 (SKILL.md body) closed 2026-09-18 — skill/SKILL.md at 145 lines; next: Phase 6 (adversarial test set). Rules last verified: 2026-09-18 (eCFR rule text).

Layout:
- skill/ — the shipped skill (SKILL.md + references/)
- catalog/ — failure catalog built from SEC risk alerts, sweep actions, and enforcement releases
- tests/ — adversarial test set
- RULINGS.md — dated rulings, cited by date and slug
- OPEN.md — open questions

Every skill output ends with: "Pre-review only. Not legal or compliance advice. Confirm with your CCO or counsel."
