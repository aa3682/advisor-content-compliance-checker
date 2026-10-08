# Advisor Content Compliance Checker
An Agent Skill (SKILL.md standard) that performs a first-pass marketing-compliance review of advisor marketing content against the SEC Marketing Rule (Rule 206(4)-1), returning a cited fix list. Pre-review only — never a compliance opinion.

Status: Phase 6 (adversarial test set) closed 2026-10-06 on run 14 (ac16f55) — 52 checks, 77 fixtures; synthetic demo added in demo/. Rules last verified: 2026-09-18 (eCFR rule text).

Scope:
- Default reader: state-registered solo and two-person RIAs. State divergences are flagged, not resolved.
- In scope: testimonials and endorsements, third-party ratings, performance claims, the general prohibitions, substantiation, required disclosures.
- Out of scope: FINRA 2210 broker-dealer content, ERISA and retirement-plan marketing, private fund marketing, non-US rules.

How to use:
1. Install the skill/ folder as a skill named advisor-content-compliance-checker. In Claude Code, copy it to ~/.claude/skills/advisor-content-compliance-checker/. In the Claude apps, zip that folder and upload it as a custom skill in settings.
2. Share a marketing draft (a post, web page, email or one-pager) and ask for a review.
3. You get a fix list. Each flag quotes the phrase, names the pattern, cites the rule paragraph, catalog ID and source, and proposes the smallest fix. Confirm items name facts the draft does not state that would decide whether a check applies.
4. Asking whether content passes returns the same review, never a verdict. See demo/ for a full before-and-after run.

Layout:
- skill/ — the shipped skill (SKILL.md + references/)
- catalog/ — failure catalog built from SEC risk alerts, sweep actions, and enforcement releases
- tests/ — adversarial test set
- tools/ — check-index builder, fixture and static checks, and test-run tooling
- demo/ — synthetic before/after example (fictional firm)
- RULINGS.md — dated rulings, cited by date and slug
- OPEN.md — open questions

Requirements: tools need Python 3 and PyYAML.

License: MIT (see LICENSE).

Every skill output ends with: "Pre-review only. Not legal or compliance advice. Confirm with your CCO or counsel."
