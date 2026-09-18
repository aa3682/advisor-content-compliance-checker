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

Generated from catalog/failures.md by tools/build_check_index.py. Never hand-edit; rerun the script when the catalog changes. One check per catalog entry; 51 checks.

### GP (16)
- GP-01 · Any absolute no-conflict statement · (a)(1), (a)(2) · general-prohibitions.md
- GP-02 · Team language for a solo shop; credentials that can't be verified · (a)(1), (a)(2) · general-prohibitions.md
- GP-03 · Any named process, mandate, or client type the firm cannot show · (a)(1), (a)(2) · general-prohibitions.md
- GP-04 · Award claims without the award · (a)(1) · general-prohibitions.md
- GP-05 · Fiduciary status framed as unique · (a)(1), (a)(3) · general-prohibitions.md
- GP-06 · Product mentions with undisclosed pay · (a)(1) · general-prohibitions.md
- GP-07 · Media logos or "featured in" without "paid placement" · (a)(3) · general-prohibitions.md
- GP-08 · Celebrity photos in marketing · (a)(3) · general-prohibitions.md
- GP-09 · "SEC-registered" used as a quality signal; any SEC seal · (a)(3) · general-prohibitions.md
- GP-10 · Superlatives around awards; methodology absent · (a)(3) · general-prohibitions.md
- GP-11 · Reviews of someone else's product · (a)(3) · general-prohibitions.md
- GP-12 · Tiny/low-contrast/fast-scrolling disclosure text · (a)(7) · general-prohibitions.md
- GP-13 · "AI-powered," "AI-driven" process language the firm cannot show · (a)(1) · general-prohibitions.md
- GP-14 · Rating name or rank altered from the source · (a)(1) · general-prohibitions.md
- GP-15 · Association badges or "member of" lines · (a)(1) · general-prohibitions.md
- GP-16 · Personal award claims without the award · (a)(2) · general-prohibitions.md

### PERF (15)
- PERF-01 · Large dollar/percent profit totals · (a)(1) · general-prohibitions.md
- PERF-02 · Fund returns without share-class note · (a)(1) · general-prohibitions.md
- PERF-03 · "Net" figures; fee basis unstated · (a)(1) · general-prohibitions.md, performance.md
- PERF-04 · Returns without fee/expense disclosure · (a)(1) · general-prohibitions.md, performance.md
- PERF-05 · Any "vs. S&P 500" style line · (a)(3) · general-prohibitions.md
- PERF-06 · Stale figures; discontinued products · (a)(3) · general-prohibitions.md
- PERF-07 · Personal/paper track records; new-firm performance claims; bull-market periods without context · (a)(3) · general-prohibitions.md
- PERF-08 · Return figures in a post with no risk language · (a)(4) · general-prohibitions.md
- PERF-09 · Winner lists; "top picks" · (a)(5) · general-prohibitions.md
- PERF-10 · Returns without dates; mixed periods · (a)(6) · general-prohibitions.md, performance.md
- PERF-11 · "Realized" in the fine print, or no basis given · (a)(6) · general-prohibitions.md, performance.md
- PERF-12 · Any model, backtest, or projection in public content · (d)(6)(i) · performance.md
- PERF-13 · Annualized or extrapolated figures; "model" with no method · (d)(6)(ii), (a)(1) · general-prohibitions.md, performance.md
- PERF-14 · Projections with no risk/limitation language · (d)(6)(iii) · performance.md
- PERF-15 · Model results with no records behind them · (a)(1), (a)(2) · general-prohibitions.md

### TE (13)
- TE-01 · Quote with no status/compensation/conflict line · (b)(1)(i) · testimonials-endorsements.md
- TE-02 · "See disclosures" link; footnote-size text · (b)(1) · testimonials-endorsements.md
- TE-03 · Embedded Google/Yelp-style reviews · (b)(1)(i) · testimonials-endorsements.md
- TE-04 · Any incentive for reviews · (b)(1), (b)(2)(i) · testimonials-endorsements.md
- TE-05 · "Promoter may receive compensation" with no terms · (b)(1)(ii) · testimonials-endorsements.md
- TE-06 · Endorser relationship not stated · (b)(1)(iii) · testimonials-endorsements.md
- TE-07 · Referral or affiliate content with no endorsement treatment · (b), (e) definitions · testimonials-endorsements.md, definitions.md
- TE-08 · Paid promotion with no agreement on file · (b)(2)(ii) · testimonials-endorsements.md
- TE-09 · Repeated small referral payments · (b)(4)(i), (e)(2) · testimonials-endorsements.md, definitions.md
- TE-10 · Promoter background unchecked · (b)(3), (e)(9) · testimonials-endorsements.md, definitions.md
- TE-11 · Staff or partner quotes without affiliation stated · (b)(4)(ii) · testimonials-endorsements.md
- TE-12 · Sponsorship or "official partner" language · (b)(1)(i) · testimonials-endorsements.md
- TE-13 · Undated quotes attributed to "clients" · (b)(1)(i); testimonial definition (e) · testimonials-endorsements.md, definitions.md

### TPR (7)
- TPR-01 · Rating used with no methodology review on file · (c)(1) · third-party-ratings.md
- TPR-02 · "See our rating on X" links · (c)(2) · third-party-ratings.md
- TPR-03 · Undated badges; "2019–2024" with gaps · (c)(2)(i) · third-party-ratings.md
- TPR-04 · Badge without provider name · (c)(2)(ii) · third-party-ratings.md
- TPR-05 · Paid badges/reprints with no compensation line · (c)(2)(iii) · third-party-ratings.md
- TPR-06 · Nomination/application fees unmentioned · (c)(2)(iii) · third-party-ratings.md
- TPR-07 · Disclosure separated from the badge · (c)(2) · third-party-ratings.md

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
