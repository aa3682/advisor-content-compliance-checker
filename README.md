# Advisor Content Compliance Checker
An Agent Skill (SKILL.md standard) that performs a first-pass marketing-compliance review of advisor-facing content against the SEC Marketing Rule (Rule 206(4)-1), returning a cited fix list. Pre-review only — never a compliance opinion.

Status: Phase 6 (adversarial test set) closed 2026-10-06 on run 14 (ac16f55) — 52 checks, 77 fixtures. Rules last verified: 2026-09-18 (eCFR rule text).

Scope:
- Default reader: state-registered solo and two-person RIAs. State divergences are flagged, not resolved.
- In scope: testimonials and endorsements, third-party ratings, performance claims, the general prohibitions, substantiation, required disclosures.
- Out of scope: FINRA 2210 broker-dealer content, ERISA and retirement-plan marketing, private fund marketing, non-US rules.

Layout:
- skill/ — the shipped skill (SKILL.md + references/)
- catalog/ — failure catalog built from SEC risk alerts, sweep actions, and enforcement releases
- tests/ — adversarial test set
- tools/ — check-index builder, fixture and static checks, and test-run tooling
- RULINGS.md — dated rulings, cited by date and slug
- OPEN.md — open questions

Requirements: tools need Python 3 and PyYAML.

Every skill output ends with: "Pre-review only. Not legal or compliance advice. Confirm with your CCO or counsel."
