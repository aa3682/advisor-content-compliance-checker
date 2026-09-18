---
name: advisor-content-compliance-checker
description: First-pass pre-review of investment-adviser marketing content against SEC Rule 206(4)-1 (the Marketing Rule), returning a fix list in which every flag cites the rule paragraph and the documented SEC failure behind it. Use when the user shares advisor-facing marketing content and asks for a review, a check, or fixes. Pre-review only; never a compliance opinion and never a clearance.
---

# Advisor Content Compliance Checker

Rules last verified: 2026-09-18 (eCFR rule text).

## Purpose

First-pass review of advisor-facing marketing content against SEC Rule 206(4)-1. Output is a fix list. Every flag is backed by a documented SEC failure recorded in catalog/failures.md and cites the rule paragraph, the catalog ID, and the source. A pattern with no documented failure behind it is not a check and is never flagged.

## What this skill never does

- Never states or implies that content passes, is approved, is cleared, or meets the rule. No clearance language in any form.
- Never gives a compliance opinion or legal advice.
- Never resolves state-law divergence; state-registered advisers are pointed to their state's rule.
- Out of scope, never reviewed as if in scope: FINRA 2210 broker-dealer content, ERISA/retirement-plan marketing, private fund marketing, non-US rules.

## Procedure

PLACEHOLDER-SUBPHASE-4 — the review procedure and output contract are written in sub-phase 4 from rulings output-shape, unclassifiable-content, and state-divergence.

## Checks

PLACEHOLDER-SUBPHASE-3 — the check index is generated from catalog/failures.md in sub-phase 3 (ruling entries-to-checks). Never hand-edit this section.

## References

Open a reference file only when a check in its series fires or a Confirm item needs its definition. Each file carries the verbatim rule text for its paragraph(s) followed by the catalog entries resolved to it.

- skill/references/general-prohibitions.md — Rule 206(4)-1(a)
- skill/references/performance.md — Rule 206(4)-1(d)
- skill/references/testimonials-endorsements.md — Rule 206(4)-1(b)
- skill/references/third-party-ratings.md — Rule 206(4)-1(c)
- skill/references/definitions.md — Rule 206(4)-1(e)

## Mandatory closing line

Every output, including a no-match output, ends with this line exactly:

Pre-review only. Not legal or compliance advice. Confirm with your CCO or counsel.
