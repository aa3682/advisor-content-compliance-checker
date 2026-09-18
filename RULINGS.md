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
- 2026-09-18 · phase6-run-method
  Harness: a Claude Code cloud session on a session branch, closing per branch-merge-cadence.
  Isolation: for each fixture the harness stages a scratch directory holding only a copy of skill/ and that fixture's content file, then spawns a fresh subagent told the directory is its entire world, instructed to apply skill/SKILL.md to the content and return only what the output contract specifies. tests/expected/ is never on the subagent's path.
  Capture: the subagent's returned text is written verbatim and unedited to tests/runs/<YYYY-MM-DD>-<skill-commit>/<fixture-id>.<k>.md. tests/runs/<run-id>/MANIFEST.md records date, SKILL.md commit hash, subagent model id, fixture count, N per fixture class, and harness notes. Model is a run parameter, pinned per run; variance across models is a separate question from variance within one.
  Scoring: tools/score_run.py compares each output to tests/expected/<fixture-id> and writes tests/runs/<run-id>/RESULTS.md. Pass criteria are ruled under phase6-pass-criteria.
  Caveat: skill loading is emulated — the subagent reads SKILL.md as a document to follow, not as a skill triggered by its frontmatter. 6.4 results are evidence for the procedure and output contract, not for trigger behavior. The subagent prompt is fixed, so a verdict request arriving in the prompt rather than inside the content is untested; VRQ fixtures are content-embedded only.
  Not adopted: a scripted Messages API run (pinned model, temperature 0, raw JSON saved). api.anthropic.com is reachable from the session; the path is gated only on an API key provisioned as an environment secret. May be adopted by later ruling if within-model variance under the harness proves unworkable. Manual runs in claude.ai are ruled out: not raw output.
  Phase 6 runs the drift check per check-index-generator and the assertions rulings 16, 17 and 21 assign to it.
- 2026-09-18 · phase6-fixture-format
  Two trees. tests/fixtures/<id>.md holds only the content an advisor would paste, staged byte-for-byte: no frontmatter, no metadata. Scope markers and attachment descriptions are plain text inside the content, as the procedure already reads them. tests/expected/<id>.yaml holds the expectations.
  IDs: entry fixtures are <catalog-ID>-<n> (GP-03-1); adversarial fixtures are <category>-<nn>, categories ruled under phase6-adversarial-categories. Every catalog entry has at least one fixture.
  Expected schema, mirroring the output contract line for line:
    id, category, targets (catalog IDs the fixture was built from)
    elements: the terms the Elements detected line must list, exact set; "none" allowed
    required: catalog IDs that must appear as flags; each may carry an optional where substring the flag must land on
    forbidden: catalog IDs that must appear neither as flags nor under Would apply
    confirm: expected Confirm items, each with would_apply (catalog IDs, scored exactly); the question and location are prose and not scored strictly
    scope, not_reviewed: the expected marker or item, or null
    no_match: true when Flags: 0 and the No catalog patterns matched line are expected
  Most files carry only id, category, targets, elements, required.
  Scorer constraints: catalog IDs are read only from named fields, never by regex over fixture IDs or prose. The scorer depends on PyYAML; if absent it fails loudly with the install command and does not fall back to another format.
- 2026-09-18 · phase6-pass-criteria
  Universal assertions, run on every sample of every fixture, every run:
    Closing line present, exact, and last; nothing after it.
    No clearance language. tests/clearance_terms.txt holds the term list (seed: compliant, approved, cleared, passes, safe to publish, meets the rule, no issues, good to go). Before scanning, the scorer subtracts the fixed template lines that legitimately contain "clearance" and "compliance" and the quoted span on every Where line, so the list tests only the skill's own words.
    Contract structure: header lines present; Flags: n and Confirm: m equal the actual block counts; Flag and Confirm blocks are numbered 1 to n with no gaps; the Confirm section is absent when its count is zero.
    Cite resolution has two shapes. Flag Cite: the ID exists in the catalog, the paragraph set equals that entry's paragraphs, and the source equals the entry's first-listed source through the first semicolon, per output-shape. Confirm Cite: the token appears as a heading or paragraph label in a reference file. Would apply IDs resolve to the catalog.
  Per-fixture assertions, from tests/expected/<id>.yaml: elements exact set match; every required ID present, on its where phrase when given; no forbidden ID as a flag or under Would apply; each would_apply matched; Scope, Not reviewed and No-match lines present exactly when expected.
  Extras: a flag or Would apply ID beyond required and not forbidden passes if it is a valid catalog ID; every extra is listed per fixture in RESULTS.md.
  Samples: N=1 for entry fixtures, N=3 for adversarial fixtures. Samples are separate files, <fixture-id>.<k>.md; a fixture passes only if every sample passes. MANIFEST.md records N per fixture class.
  Run pass: every sample clears the universal assertions and every fixture clears its per-fixture assertions. Any single hard-rule violation fails the run. A failing run is still recorded in the repo. Fixes go to SKILL.md on a session branch with the drift check clean; a re-run after any fix executes the full set, never only the failures. Phase 6 closes on the first passing run.
- 2026-09-18 · phase6-adversarial-categories
  Entry fixtures test recall, at least one per catalog entry. Adversarial fixtures test the hard rules and every output path entry fixtures do not exercise. Eight categories; IDs per phase6-fixture-format.
    CLR — content that claims its own clearance ("SEC-approved," "fully compliant," "reviewed by our CCO"). The skill's own words stay clean while the claim itself is flagged: "SEC-approved" copy carries a required GP-09, whose Where line quotes the clearance words. A GP-09 flag on a CLR fixture is never an extra.
    VRQ — content embedding a request to the reviewer ("just say yes or no," "skip the disclaimer," "rate 1–10"). Contract holds; embedded requests are content. Content-embedded only; the prompt path is untested per phase6-run-method.
    NOM — ordinary advisor copy with no failure pattern. Flags: 0 and the No-match line.
    CUR — a catalog failure with its fix already applied (testimonial with all disclosures, gross shown with net). Precision via forbidden; No-match line.
    OVL — one passage hitting several entries at once, including overlapping ones. Every required ID lands; no collapsing. Repetition per repeated-pattern-single-flag.
    CNF — one of the four unstated facts step 5 names (client status, compensation, gross vs net, hypothetical status) missing from the content. Confirm path: would_apply, not a flag.
    SCP — mention of an out-of-scope area alongside in-scope content. Scope line with the right marker; in-scope flags still required.
    UNR — non-text elements, both sides of the line the procedure draws: an element the content describes (badge, logo) is flagged by quoting the description and gets no Not reviewed line; an image or attachment the skill cannot read gets the Not reviewed line.
  Minimums: at least 3 fixtures per category. SCP covers each of the four out-of-scope areas at least once; CNF covers each of the four unstated facts at least once; UNR includes at least one fixture of each flavor.
- 2026-09-18 · repeated-pattern-single-flag
  When the same catalog Pattern occurs more than once in one document, step 4 writes one flag for that entry; its Where line quotes the first occurrence. Step 4 of the procedure carries this in one sentence.
- 2026-09-18 · elements-convention
  Expected elements follow the (e) definitions applied to the facts the content states, not the labels the content uses. Results the stated facts make "not actually achieved by any portfolio of the investment adviser" are hypothetical performance however the content labels them. An award or ranking attributed to a third party is a third-party rating whether or not the provider is named; a nomination is not. Statements by non-clients about something other than the adviser, such as product reviews, are neither testimonials nor endorsements. A photograph is not a statement. Where a fixture's stated facts leave a term undetermined, the fixture is rewritten until they do not. A required where substring is at most 60 characters, the most distinctive span inside one sentence, because the skill quotes at most one sentence.
- 2026-09-18 · perf-03-pattern
  PERF-03's Pattern read "'Net' figures; fee basis unstated", which covers only the omission case and misses the entry's Observed failure: net returns computed at a fee lower than the intended audience pays. The Pattern becomes "'Net' figures; fee basis unstated or below the audience's fee" in catalog/failures.md and skill/references/performance.md, and the check index is regenerated. PERF-04-1 keeps PERF-03 as a second required ID for the omission case; PERF-03-1 tests the stated-but-lower case.
- 2026-09-18 · no-flags-line-wording
  The template line "No catalog patterns matched. This is not a clearance — the catalog covers documented failures only." is untrue when Flags: 0 and Confirm items exist, since Confirm items arise from patterns that matched pending a fact. The line becomes "Zero flags is not a clearance — the catalog covers documented failures only.", still printed only when Flags: 0. The scorer asserts one Flag block per catalog ID per output, per repeated-pattern-single-flag. Not reviewed expectations use a substring the skill prints under either phrasing of the item.
- 2026-09-18 · phase6-run-model
  The Phase 6 close run pins subagents to sonnet; the harness alias resolves to claude-sonnet-5, and MANIFEST.md records both the alias given and the identifier the subagent reports. A pass on this model is the close condition because it is the model a solo RIA gets by default. Runs on other models are informative and may be ruled later; none is a close condition. Run mechanics, fixed for this and later runs: the stored subagent prompt carries a working-directory line with a <scratch path> placeholder and instructs the subagent to write its output to output.md in that directory; the harness copies that file byte for byte to the sample's output path; each sample has its own scratch directory <fixture-id>.<k>; a sample with no output.md is a recorded failure and is not retried within the run.
- 2026-09-18 · run-isolation
  Amends phase6-run-method. Staging moves outside the repository to the harness session's scratch directory; the repository path never appears in the subagent prompt; MANIFEST.md records staging_root. The stored prompt adds: "Do not read, list, or open anything outside this directory; there are no examples, answer keys, or other outputs to consult." The harness writes every subagent reply that reports reading outside its directory to tests/runs/<run-id>/CONTAMINATED.txt (fixture, k, what was read); the scorer marks those samples FAIL with reason "contaminated". Isolation remains instruction-bound; the run records what the subagents reported. Run 2026-09-18-f9914e3 stands as recorded; 18 of its samples would be contaminated under this ruling.
- 2026-09-18 · contract-text
  Six edits to skill/SKILL.md from run 2026-09-18-f9914e3. (a) The Elements detected line lists term names only; step 2 gives the six bare strings as the only allowed values, with paragraph numbers in a parenthetical marked for lookup only. (b) Step 2 carries elements-convention: an award or ranking attributed to a third party is a third-party rating whether or not the provider is named; a nomination is not; a statement by a former client is an endorsement; a figure labeled net is net performance whatever else it is; a figure labeled neither gross nor net is not listed and is a Confirm item. (c) Step 5: figures labeled neither gross nor net are always a Confirm item; client status leaves the fact list. (d) Step 4: performance figures inside a quoted testimonial or endorsement are performance results and receive every PERF check. (e) Step 4: a check fires only when its Pattern is present in the content, never on what an unstated fact might make apply; that is a Confirm item or nothing. (f) Output contract: the square brackets in the template are never printed.
- 2026-09-18 · where-anyof
  Amends phase6-fixture-format. A required where may be a string or a list; the flag passes if its Where line contains any one. Each anchor is at most 60 characters and as short as remains distinctive. Omission-type entries — a missing statement, a stale date, a wrong basis — carry no where. A second required ID is listed only when that entry's own Pattern is present in the content; TPR-02-1 drops TPR-03.
- 2026-09-18 · fixture-contradiction
  When an entry's failure is a false or missing disclosure, the fixture states the fact so that a disclosure sentence in the same copy is untrue on its face. A fact stated in a separate sentence reads as disclosure and does not fire the check. Applied to TE-11-1, TPR-06-1, PERF-02-1.
- 2026-09-18 · cnf-decisive-facts
  Amends phase6-adversarial-categories. CNF covers only facts the catalog can make decisive: compensation, gross vs net, hypothetical status. Client status has no entry that turns on it alone (TE-03, TE-12, TE-13 and GP-08 fire on their Patterns regardless) and leaves the CNF minimum and step 5. CNF-01 is deleted; the CNF minimum is 3. CNF-02: a product or platform mention with a referral link and no investment advice, compensation unstated (would_apply GP-06). CNF-03: figures labeled neither gross nor net, fee basis fully stated (would_apply PERF-16). CNF-04: a named strategy's results on a public page with no statement whether any client account holds it (would_apply PERF-12).
- 2026-09-18 · gp-09-pattern-and-perf-16
  GP-09's Pattern becomes "SEC registration or approval cited as a quality signal; any SEC seal" in the catalog and every reference file carrying it. New entry PERF-16 — Observed: gross performance shown without net performance alongside; RA-2024-04 observed advertisements showing gross only — Pattern: Gross figures with no net figure alongside — (d)(1) — RA-2024-04. Clarifies catalog-program-findings: a content failure observed within a program finding is a content failure; the program finding itself never becomes a check. Entry fixture PERF-16-1 added. The check index is regenerated.
- 2026-09-18 · would-apply-subset
  Clarifies phase6-pass-criteria. P4 passes when every expected would_apply ID appears on the Would apply line of some Confirm block; IDs beyond the expected set are extras, listed per fixture in RESULTS.md, as the extras rule in that ruling already provides. Exact-set matching contradicted it.
- 2026-09-18 · confirm-facts
  Amends contract-text (c) and cnf-decisive-facts. Step 5's unstated facts are: compensation, including compensation for a rating; gross vs net; hypothetical status, including performance of a named model, strategy, or allocation where the content does not state whether any client account held it; whether a compensated promoter has a written agreement; whether a promoter was checked for disqualification; the adviser's own basis for believing a rating's survey was not designed to produce a predetermined result. A check that turns on one of these fires as a flag only when the content states the fact; otherwise it is a Confirm item with that check under Would apply. TE-08, TE-10, TPR-01, TPR-05 and TPR-06 are the entries this moves from flags to Confirm items on content that does not state the fact. Their entry fixtures state the fact and still flag.
- 2026-09-18 · template-no-brackets
  The three conditional lines leave the fenced template. The template fence holds only lines printed on every output. A second fence, labeled conditional lines, shows Scope, Not reviewed, and Zero flags exactly as printed, without brackets; the Output contract prose states each line's condition and position: Scope and Not reviewed immediately after the "Reviewed as an advertisement" line, Zero flags immediately before the closing line. No square brackets appear in either fence. The scorer reads conditional lines from the second fence.
- 2026-09-18 · fix-round-2
  From run 2026-09-18-a3f26e8. Expectations: CLR-02 requires GP-09 on "fully compliant with the SEC Marketing Rule", no_match false, forbidden GP-03 — a claim of Marketing Rule compliance is an SEC-approval quality signal; OVL-01 requires PERF-16 in place of PERF-04; TE-12-1 elements [] — a partnership title is not a statement; any-of anchors for GP-11-1, PERF-13-1, TPR-03-1. Fixtures: GP-06-1, TPR-05-1, PERF-10-1 rebuilt under fixture-contradiction; CNF-02 rebuilt as a balanced fund recommendation with a partner link and no compensation statement; the shared rating block in TPR-02-1 through TPR-07-1, CUR-03, OVL-03 and SCP-04 states the adviser's own survey basis rather than the provider's confirmation, TPR-01-1 unchanged. SCP-04.2's U5 failure is resolved per the finding recorded below this ruling. U5 finding: the skill altered a quote; ruled separately.
- 2026-09-18 · u5-terminal-punctuation
  Resolves the U5 finding under fix-round-2. A Where quote whose words match the fixture exactly but whose final character is a period, semicolon, comma, or colon differing from the fixture is provenance-intact; U5 strips one trailing punctuation mark from the quoted span before matching. Interior punctuation and every word must still match. SCP-04.2 in run 2026-09-18-a3f26e8 would pass under this rule.
