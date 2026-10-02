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

Follow these steps in order for every review. The wording of every fixed line below is set by RULINGS.md (output-shape, entries-to-checks, unclassifiable-content, state-divergence). Do not vary it.

1. Read the whole content before flagging anything. If the user asks for a verdict ("is this okay?", "does this pass?"), do not answer the question; return this review.
2. Detect elements. Scan for the six rule-defined elements and record the ones present using these exact names and no others: testimonial, endorsement, third-party rating, gross performance, net performance, hypothetical performance (their paragraphs, for lookup only and never printed: (e)(17), (e)(5), (e)(18), (e)(7), (e)(10), (e)(8)). Apply the definitions to the facts the content states, not to its labels: a third-party rating is present when the content names the provider or displays the rating itself — a score, stars, a rank, a badge; a title or award merely asserted, with neither, is not a third-party rating and GP-04 reviews it when asserted for the firm, GP-16 when asserted for a principal; a nomination is not; a statement the content attributes to an identified former client is an endorsement, per (e)(5); quotes attributed to "clients" where the content does not say which are former are recorded as testimonials, and the former-client possibility is TE-13's flag, not a second element; a customer review or quote whose speaker's client status the content does not state is recorded as a testimonial, and TE-03 and TE-13 carry the unknown-status failure; a figure labeled net is net performance whatever else it is; a figure labeled neither gross nor net is not listed and becomes a Confirm item (step 5). Performance is hypothetical when no actual portfolio achieved it — model, backtest, paper-traded, targeted or projected results, per (e)(8)(i). Results actually achieved in a real account that was not a client account (a personal account) are not hypothetical on that ground — (e)(11) defines portfolio to include a portfolio for the account of the adviser or its advisory affiliate; record them by their gross/net labels and let PERF-07 govern. A named model, strategy or allocation whose actual-account status is unstated stays a Confirm item. Open skill/references/definitions.md when a term's boundary is unclear. Never describe the content by format.
3. Note scope markers. If the content mentions a broker-dealer or FINRA, a private fund, an ERISA or retirement-plan offering, or a non-US regulator, record the marker for the scope line. The review still runs. If part of the content is an image or attachment you cannot read, record it for the not-reviewed line.
4. Run every check in the Checks section, GP through TPR, in index order. Elements detected: none does not skip this step; GP checks apply to content with no element present. A check fires only when the content contains the check's Pattern, never on what an unstated fact might make apply; that is a Confirm item (step 5) or nothing. For the recognition Patterns GP-04, GP-08, GP-10, GP-15 and GP-16, the check fires when the content presents the claim, and the Fix asks for substantiation. Performance figures inside a quoted testimonial or endorsement are performance results and receive every PERF check. When the same Pattern occurs more than once in one document, write one flag for that entry; the Where line quotes the first occurrence. For each firing check:
   a. Open the reference file(s) named on the check line and find the entry by ID.
   b. Confirm the content matches the entry's Observed failure. If the match depends on a fact the content does not state, it is a Confirm item (step 5), not a flag.
   c. Write the flag. Where quotes the exact phrase, one sentence max; for a non-text element the content describes (a badge, logo, photo), quote the content's own description of it. When a Pattern names an omission, Where preferably quotes the sentence that presents the item whose disclosure is missing — the review-source line, the description of the promoter, the list header — though the omission or testimonial statement itself is also acceptable. For a compound Pattern (a thing shown plus something omitted), Where quotes the thing shown. What is the check's Pattern, verbatim. Cite is copied from the entry: rule paragraphs · ID · the first-listed source through the first ";". Fix is the smallest edit that removes the matched pattern: a rewrite of the phrase, "remove", or "supply X" naming the missing disclosure. A rewrite never adds a claim the content did not make and never asserts the rewritten phrase is acceptable.
   A phrase matching several entries gets one flag per entry. Never collapse, rank, or tier flags.
5. Write Confirm items for matches that turn on an unstated fact. The unstated facts are: compensation, including compensation for a rating; gross vs net; hypothetical status, including performance of a named model, strategy, or allocation where the content does not state whether any client account held it; whether a compensated promoter has a written agreement; whether a promoter was checked for disqualification; the adviser's own basis for believing a rating's survey was not designed to produce a predetermined result; the promoter's material conflicts of interest arising from a relationship with the adviser; whether a linked rating page carries the (c)(2) disclosures — for TPR-02 this is always a Confirm item, because this review does not read linked pages, and it is written alongside the TPR-02 flag when the advertisement itself carries no rating disclosures. When the content presents a third-party rating and does not state whether compensation was provided in connection with obtaining or using it, always write one Confirm item citing (c)(2)(iii) with TPR-05 under Would apply, adding TPR-06 unless the rating has no nomination or application process. A check that turns on one of these fires as a flag only when the content states the fact; otherwise it is a Confirm item with that check under Would apply. Figures labeled neither gross nor net are always a Confirm item. Cite is the (e) term and token that decides the fact, or the (b)/(c)/(d) paragraph that conditions on it, copied from the reference file: (b)(2)(ii) for the written agreement, (b)(3) for the disqualification check, (c)(1) for the survey basis, (c)(2)(iii) for rating compensation, (b)(1)(iii) for the promoter's conflicts, (c)(2) for the linked rating page. Would apply lists every catalog ID that would fire if the answer is yes. No Confirm item without at least one ID.
6. Assemble the output from the template below, exactly. Flags in document order. Confirm section omitted when empty. The Zero flags line appears only when Flags: 0 and Confirm: 0. Every output ends with the mandatory closing line.

### Output contract

Fixed lines are written verbatim. The template holds only the lines printed on every output. The three conditional lines are shown in the second fence exactly as printed; each appears only under its condition, at its stated position. Nothing is added outside the template: no summary, no overall assessment, no remarks after the mandatory closing line.

The Scope line appears only when a scope marker is present, immediately after the "Reviewed as an advertisement" line.
The Not reviewed line appears only when part of the content cannot be read, immediately after the "Reviewed as an advertisement" line (after the Scope line when both appear).
Both sit between the "Reviewed as an advertisement" line and the "State-registered advisers" line, which the template fence shows adjacent because neither conditional line is printed on every output.
The Zero flags line appears only when Flags: 0 and Confirm: 0, immediately before the closing line.

Never describe content as approved, cleared, passing, safe to publish, meeting the rule, or any equivalent, including the adjective form of the word "compliance". Never state which flags matter most.

```
Marketing Rule pre-review — SEC Rule 206(4)-1
Elements detected: <the six terms present, or "none">
Reviewed as an advertisement under (e)(1); whether (e)(1) covers this communication is not assessed.
State-registered advisers are subject to their state's rule, which may differ from any flag below; differences are not resolved here.
Flags: <n>. Confirm: <m>.

Flag 1
Where: "<exact phrase>"
What: <Pattern>
Cite: <rule paragraphs> · <ID> · <source>
Fix: <rewrite | remove | supply X>

Confirm 1
Where: "<exact phrase>"
Depends on: <one question>
Cite: <(e) term and token, or the (b)/(c)/(d) paragraph>
Would apply: <ID(s)>

Pre-review only. Not legal or compliance advice. Confirm with your CCO or counsel.
```

Conditional lines:

```
Scope: content mentions <marker>; this skill does not cover it.
Not reviewed: <image or attachment>.
Zero flags is not a clearance — the catalog covers documented failures only.
```

## Checks

Generated from catalog/failures.md by tools/build_check_index.py. Never hand-edit; rerun the script when the catalog changes. One check per catalog entry; 52 checks.

### GP (16)
- GP-01 · Any absolute no-conflict statement · (a)(1), (a)(2) · general-prohibitions.md
- GP-02 · Team language for a solo shop; credentials that can't be verified · (a)(1), (a)(2) · general-prohibitions.md
- GP-03 · Any named process, mandate, or client type the firm cannot show · (a)(1), (a)(2) · general-prohibitions.md
- GP-04 · Firm award claims without the award · (a)(1) · general-prohibitions.md
- GP-05 · Fiduciary status framed as unique · (a)(1), (a)(3) · general-prohibitions.md
- GP-06 · Product mentions with undisclosed pay · (a)(1) · general-prohibitions.md
- GP-07 · "As seen on," "featured in," or media logos without "paid placement" · (a)(3) · general-prohibitions.md
- GP-08 · Celebrity images implying an endorsement the firm cannot show · (a)(3) · general-prohibitions.md
- GP-09 · SEC registration or approval cited as a quality signal; any SEC seal · (a)(3) · general-prohibitions.md
- GP-10 · Superlatives implying sole or highest recognition the firm cannot show; methodology absent · (a)(3) · general-prohibitions.md
- GP-11 · Third-party product testimonials or user reviews presented as evidence about the adviser · (a)(3) · general-prohibitions.md
- GP-12 · Tiny/low-contrast/fast-scrolling disclosure text · (a)(7) · general-prohibitions.md
- GP-13 · "AI-powered," "AI-driven" process language the firm cannot show · (a)(1) · general-prohibitions.md
- GP-14 · Rating name or rank altered from the source · (a)(1) · general-prohibitions.md
- GP-15 · Association badges or "member of" lines the firm cannot show · (a)(1) · general-prohibitions.md
- GP-16 · Personal award claims without the award · (a)(2) · general-prohibitions.md

### PERF (16)
- PERF-01 · Large dollar/percent profit totals · (a)(1) · general-prohibitions.md
- PERF-02 · Fund returns without share-class note · (a)(1) · general-prohibitions.md
- PERF-03 · "Net" figures; fee basis unstated or below the audience's fee · (a)(1) · general-prohibitions.md, performance.md
- PERF-04 · Returns without fee/expense disclosure · (a)(1) · general-prohibitions.md, performance.md
- PERF-05 · Index comparisons where the index is undefined, silent on dividends, or uncontextualized as to why it is comparable · (a)(3) · general-prohibitions.md
- PERF-06 · Stale figures, or discontinued products shown at costs lower than those charged now · (a)(3) · general-prohibitions.md
- PERF-07 · Personal or paper track records; performance claimed by a firm that cannot show client accounts behind it; bull-market periods without context · (a)(3) · general-prohibitions.md
- PERF-08 · Return figures in a post with no risk language · (a)(4) · general-prohibitions.md
- PERF-09 · Winner lists or "top picks" excluding losses or write-offs with no stated rationale · (a)(5) · general-prohibitions.md
- PERF-10 · Returns without dates; mixed periods · (a)(6) · general-prohibitions.md, performance.md
- PERF-11 · Returns computed from realized positions only, unrealized excluded · (a)(6) · general-prohibitions.md, performance.md
- PERF-12 · Any model, backtest, or projection in public content · (d)(6)(i) · performance.md
- PERF-13 · Annualized or extrapolated figures, or a model, presented without the criteria and assumptions behind them · (d)(6)(ii), (a)(1) · general-prohibitions.md, performance.md
- PERF-14 · Projections with no risk/limitation language · (d)(6)(iii) · performance.md
- PERF-15 · Model results with no records behind them · (a)(1), (a)(2) · general-prohibitions.md
- PERF-16 · Gross figures with no net figure alongside · (d)(1) · performance.md

### TE (13)
- TE-01 · Quote with no status/compensation/conflict line · (b)(1)(i) · testimonials-endorsements.md
- TE-02 · "See disclosures" link; footnote-size text · (b)(1) · testimonials-endorsements.md
- TE-03 · Embedded Google or Yelp-style reviews with no disclosure that the reviewers are current or former clients · (b)(1)(i) · testimonials-endorsements.md
- TE-04 · Any incentive for reviews · (b)(1), (b)(2)(i) · testimonials-endorsements.md
- TE-05 · "Promoter may receive compensation" with no terms · (b)(1)(ii) · testimonials-endorsements.md
- TE-06 · Endorser relationship not stated · (b)(1)(iii) · testimonials-endorsements.md
- TE-07 · Referral or affiliate content with no endorsement treatment · (b), (e)(5) · testimonials-endorsements.md, definitions.md
- TE-08 · Paid promotion with no agreement on file · (b)(2)(ii) · testimonials-endorsements.md
- TE-09 · Referral payments whose twelve-month total to one person exceeds the de minimis threshold · (b)(4)(i), (e)(2) · testimonials-endorsements.md, definitions.md
- TE-10 · Promoter background unchecked · (b)(3), (e)(9) · testimonials-endorsements.md, definitions.md
- TE-11 · Staff or partner quotes without affiliation stated · (b)(4)(ii) · testimonials-endorsements.md
- TE-12 · Sponsorship or "official partner" language · (b)(1)(i) · testimonials-endorsements.md
- TE-13 · Undated quotes attributed to "clients" · (b)(1)(i), (e)(17) · testimonials-endorsements.md, definitions.md

### TPR (7)
- TPR-01 · Rating used with no methodology review on file · (c)(1) · third-party-ratings.md
- TPR-02 · "See our rating on X" links where the advertisement itself carries no rating disclosures · (c)(2) · third-party-ratings.md
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
