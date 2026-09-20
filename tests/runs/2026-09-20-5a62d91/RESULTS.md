# Results

- run_id: 2026-09-20-5a62d91
- date: 2026-09-20
- skill_commit: 5a62d91
- model: sonnet
- fixtures: 77
- n_entry: 3
- n_adversarial: 3
- notes: run 5, the first run under run-isolation-sandbox: each subagent is a separate claude process whose working directory is its staged directory, launched by tests/harness/launch_sample.py, with tests/runs/<run-id>/<sample>.ISOLATION.txt recorded before launch. Reviewing model: sonnet (alias resolved to claude-sonnet-5). model_reported in LAUNCH.log may additionally list claude-haiku-4-5-20251001, which is the CLI's own side calls and not the reviewing model. No fixes of any kind were made during this run.

| fixture | k | verdict | failed checks | extras |
|---|---|---|---|---|
| CLR-01 | 1 | PASS |  |  |
| CLR-01 | 2 | PASS |  |  |
| CLR-01 | 3 | PASS |  |  |
| CLR-02 | 1 | FAIL | P2: required GP-09 not flagged; P5: Zero-flags line present but not expected |  |
| CLR-02 | 2 | PASS |  |  |
| CLR-02 | 3 | FAIL | P2: required GP-09 not flagged; P5: Zero-flags line present but not expected |  |
| CLR-03 | 1 | PASS |  |  |
| CLR-03 | 2 | PASS |  |  |
| CLR-03 | 3 | PASS |  |  |
| CNF-02 | 1 | PASS |  |  |
| CNF-02 | 2 | FAIL | P4: no Confirm block lists Would apply ['GP-06']; P5: Zero-flags line present but not expected |  |
| CNF-02 | 3 | FAIL | P4: no Confirm block lists Would apply ['GP-06']; P5: Zero-flags line present but not expected |  |
| CNF-03 | 1 | PASS |  | PERF-03 |
| CNF-03 | 2 | PASS |  |  |
| CNF-03 | 3 | PASS |  |  |
| CNF-04 | 1 | PASS |  | PERF-07 |
| CNF-04 | 2 | PASS |  | PERF-07 |
| CNF-04 | 3 | PASS |  | PERF-07 |
| CUR-01 | 1 | PASS |  |  |
| CUR-01 | 2 | PASS |  |  |
| CUR-01 | 3 | PASS |  |  |
| CUR-02 | 1 | PASS |  |  |
| CUR-02 | 2 | PASS |  |  |
| CUR-02 | 3 | PASS |  |  |
| CUR-03 | 1 | PASS |  |  |
| CUR-03 | 2 | PASS |  |  |
| CUR-03 | 3 | PASS |  |  |
| GP-01-1 | 1 | PASS |  |  |
| GP-01-1 | 2 | PASS |  |  |
| GP-01-1 | 3 | PASS |  |  |
| GP-02-1 | 1 | PASS |  |  |
| GP-02-1 | 2 | PASS |  |  |
| GP-02-1 | 3 | PASS |  |  |
| GP-03-1 | 1 | PASS |  |  |
| GP-03-1 | 2 | PASS |  |  |
| GP-03-1 | 3 | PASS |  |  |
| GP-04-1 | 1 | FAIL | P2: required GP-04 not flagged | GP-16 |
| GP-04-1 | 2 | PASS |  | GP-16 |
| GP-04-1 | 3 | FAIL | P2: required GP-04 not flagged | GP-16 |
| GP-05-1 | 1 | PASS |  |  |
| GP-05-1 | 2 | PASS |  |  |
| GP-05-1 | 3 | PASS |  |  |
| GP-06-1 | 1 | PASS |  |  |
| GP-06-1 | 2 | PASS |  |  |
| GP-06-1 | 3 | PASS |  | TE-07 |
| GP-07-1 | 1 | PASS |  |  |
| GP-07-1 | 2 | PASS |  |  |
| GP-07-1 | 3 | FAIL | P2: required GP-07 not flagged; P5: Zero-flags line present but not expected |  |
| GP-08-1 | 1 | PASS |  |  |
| GP-08-1 | 2 | PASS |  |  |
| GP-08-1 | 3 | PASS |  |  |
| GP-09-1 | 1 | PASS |  |  |
| GP-09-1 | 2 | PASS |  |  |
| GP-09-1 | 3 | PASS |  |  |
| GP-10-1 | 1 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-10-1 | 2 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-10-1 | 3 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-11-1 | 1 | PASS |  |  |
| GP-11-1 | 2 | PASS |  |  |
| GP-11-1 | 3 | PASS |  |  |
| GP-12-1 | 1 | PASS |  |  |
| GP-12-1 | 2 | PASS |  |  |
| GP-12-1 | 3 | PASS |  |  |
| GP-13-1 | 1 | PASS |  |  |
| GP-13-1 | 2 | PASS |  |  |
| GP-13-1 | 3 | PASS |  |  |
| GP-14-1 | 1 | PASS |  | GP-03, TPR-01, TPR-02, TPR-05, TPR-06 |
| GP-14-1 | 2 | FAIL | P2: GP-14 flagged but Where lacks any of ['one of its Top 12 Financial Advisors for 2024'] | TPR-01, TPR-05, TPR-06 |
| GP-14-1 | 3 | FAIL | P2: required GP-14 not flagged | TPR-01, TPR-02, TPR-05, TPR-06 |
| GP-15-1 | 1 | PASS |  |  |
| GP-15-1 | 2 | PASS |  |  |
| GP-15-1 | 3 | PASS |  |  |
| GP-16-1 | 1 | PASS |  |  |
| GP-16-1 | 2 | PASS |  |  |
| GP-16-1 | 3 | PASS |  |  |
| NOM-01 | 1 | PASS |  |  |
| NOM-01 | 2 | PASS |  |  |
| NOM-01 | 3 | PASS |  |  |
| NOM-02 | 1 | PASS |  |  |
| NOM-02 | 2 | PASS |  |  |
| NOM-02 | 3 | PASS |  |  |
| NOM-03 | 1 | PASS |  |  |
| NOM-03 | 2 | PASS |  |  |
| NOM-03 | 3 | PASS |  |  |
| OVL-01 | 1 | FAIL | P2: TE-01 flagged but Where lacks any of ["I've never worried once"] | PERF-10, TE-08, TE-10 |
| OVL-01 | 2 | PASS |  | TE-08, TE-10 |
| OVL-01 | 3 | FAIL | P2: TE-01 flagged but Where lacks any of ["I've never worried once"] | TE-06, TE-08, TE-10 |
| OVL-02 | 1 | PASS |  |  |
| OVL-02 | 2 | PASS |  |  |
| OVL-02 | 3 | PASS |  | GP-03 |
| OVL-03 | 1 | PASS |  |  |
| OVL-03 | 2 | PASS |  |  |
| OVL-03 | 3 | PASS |  |  |
| PERF-01-1 | 1 | PASS |  | PERF-07, PERF-12, PERF-16 |
| PERF-01-1 | 2 | PASS |  | PERF-07, PERF-12 |
| PERF-01-1 | 3 | PASS |  | PERF-10, PERF-12 |
| PERF-02-1 | 1 | FAIL | P2: PERF-02 flagged but Where lacks any of ['only one share class', 'whichever of its several share classes'] |  |
| PERF-02-1 | 2 | FAIL | P2: PERF-02 flagged but Where lacks any of ['only one share class', 'whichever of its several share classes'] |  |
| PERF-02-1 | 3 | FAIL | P2: PERF-02 flagged but Where lacks any of ['only one share class', 'whichever of its several share classes'] |  |
| PERF-03-1 | 1 | PASS |  |  |
| PERF-03-1 | 2 | PASS |  |  |
| PERF-03-1 | 3 | PASS |  |  |
| PERF-04-1 | 1 | PASS |  |  |
| PERF-04-1 | 2 | PASS |  |  |
| PERF-04-1 | 3 | PASS |  |  |
| PERF-05-1 | 1 | PASS |  |  |
| PERF-05-1 | 2 | PASS |  |  |
| PERF-05-1 | 3 | PASS |  |  |
| PERF-06-1 | 1 | PASS |  | PERF-03 |
| PERF-06-1 | 2 | PASS |  | PERF-03, PERF-07, PERF-12 |
| PERF-06-1 | 3 | PASS |  | PERF-03 |
| PERF-07-1 | 1 | PASS |  |  |
| PERF-07-1 | 2 | PASS |  |  |
| PERF-07-1 | 3 | PASS |  |  |
| PERF-08-1 | 1 | PASS |  |  |
| PERF-08-1 | 2 | PASS |  |  |
| PERF-08-1 | 3 | PASS |  |  |
| PERF-09-1 | 1 | PASS |  | PERF-01, PERF-16 |
| PERF-09-1 | 2 | PASS |  | PERF-01, PERF-16 |
| PERF-09-1 | 3 | PASS |  | PERF-01, PERF-03, PERF-16 |
| PERF-10-1 | 1 | PASS |  |  |
| PERF-10-1 | 2 | PASS |  |  |
| PERF-10-1 | 3 | PASS |  |  |
| PERF-11-1 | 1 | PASS |  |  |
| PERF-11-1 | 2 | PASS |  |  |
| PERF-11-1 | 3 | PASS |  |  |
| PERF-12-1 | 1 | PASS |  |  |
| PERF-12-1 | 2 | PASS |  |  |
| PERF-12-1 | 3 | PASS |  |  |
| PERF-13-1 | 1 | PASS |  |  |
| PERF-13-1 | 2 | PASS |  |  |
| PERF-13-1 | 3 | PASS |  | PERF-07 |
| PERF-14-1 | 1 | PASS |  |  |
| PERF-14-1 | 2 | PASS |  |  |
| PERF-14-1 | 3 | PASS |  |  |
| PERF-15-1 | 1 | PASS |  |  |
| PERF-15-1 | 2 | PASS |  |  |
| PERF-15-1 | 3 | FAIL | P2: PERF-15 flagged but Where lacks any of ['Model trade records from before 2022 were not retained'] |  |
| PERF-16-1 | 1 | PASS |  |  |
| PERF-16-1 | 2 | PASS |  |  |
| PERF-16-1 | 3 | PASS |  |  |
| SCP-01 | 1 | PASS |  |  |
| SCP-01 | 2 | PASS |  |  |
| SCP-01 | 3 | PASS |  |  |
| SCP-02 | 1 | FAIL | P2: TE-01 flagged but Where lacks any of ['Two years in, and I finally sleep well about retirement'] |  |
| SCP-02 | 2 | PASS |  |  |
| SCP-02 | 3 | PASS |  | TE-08, TE-10 |
| SCP-03 | 1 | FAIL | contaminated: unscoped Glob/Read of /home/user/advisor-content-compliance-checker; self-reported seeing tests/expected/ filenames in one directory listing, states it opened no answer-key file and redid the review from the staged copies |  |
| SCP-03 | 2 | PASS |  |  |
| SCP-03 | 3 | PASS |  |  |
| SCP-04 | 1 | PASS |  |  |
| SCP-04 | 2 | PASS |  |  |
| SCP-04 | 3 | PASS |  |  |
| TE-01-1 | 1 | FAIL | P2: TE-01 flagged but Where lacks any of ['Working with the practice for the past three years'] | TE-08, TE-10 |
| TE-01-1 | 2 | FAIL | P2: TE-01 flagged but Where lacks any of ['Working with the practice for the past three years'] | TE-08, TE-10 |
| TE-01-1 | 3 | FAIL | P2: TE-01 flagged but Where lacks any of ['Working with the practice for the past three years'] |  |
| TE-02-1 | 1 | PASS |  | GP-12 |
| TE-02-1 | 2 | PASS |  | GP-12 |
| TE-02-1 | 3 | PASS |  | GP-12, TE-01, TE-06, TE-08, TE-10 |
| TE-03-1 | 1 | FAIL | P4: no Confirm block lists Would apply ['TPR-06'] | TE-13, TPR-03 |
| TE-03-1 | 2 | FAIL | P4: no Confirm block lists Would apply ['TPR-06'] | TE-13, TPR-03 |
| TE-03-1 | 3 | FAIL | P4: no Confirm block lists Would apply ['TPR-05', 'TPR-06'] |  |
| TE-04-1 | 1 | PASS |  | TE-01, TE-03, TE-08, TE-10 |
| TE-04-1 | 2 | PASS |  | TE-03, TE-08, TE-10 |
| TE-04-1 | 3 | PASS |  | TE-03 |
| TE-05-1 | 1 | PASS |  | TE-08, TE-09, TE-10 |
| TE-05-1 | 2 | PASS |  | TE-08, TE-09, TE-10 |
| TE-05-1 | 3 | PASS |  | TE-08, TE-09, TE-10 |
| TE-06-1 | 1 | PASS |  |  |
| TE-06-1 | 2 | PASS |  |  |
| TE-06-1 | 3 | PASS |  |  |
| TE-07-1 | 1 | PASS |  | TE-06, TE-08, TE-09, TE-10 |
| TE-07-1 | 2 | PASS |  | TE-06, TE-08, TE-09, TE-10 |
| TE-07-1 | 3 | PASS |  | TE-06, TE-08, TE-09, TE-10 |
| TE-08-1 | 1 | FAIL | P2: TE-08 flagged but Where lacks any of ['there is nothing in writing'] | GP-01, TE-10 |
| TE-08-1 | 2 | FAIL | P2: TE-08 flagged but Where lacks any of ['there is nothing in writing'] | TE-10 |
| TE-08-1 | 3 | PASS |  | TE-10 |
| TE-09-1 | 1 | FAIL | P2: TE-09 flagged but Where lacks any of ['the arrangement is treated as de minimis'] | TE-08, TE-10 |
| TE-09-1 | 2 | FAIL | P2: TE-09 flagged but Where lacks any of ['the arrangement is treated as de minimis'] | TE-08, TE-10 |
| TE-09-1 | 3 | FAIL | P2: TE-09 flagged but Where lacks any of ['the arrangement is treated as de minimis'] | TE-08, TE-10 |
| TE-10-1 | 1 | PASS |  | TE-08 |
| TE-10-1 | 2 | PASS |  | TE-08 |
| TE-10-1 | 3 | PASS |  | TE-08 |
| TE-11-1 | 1 | PASS |  |  |
| TE-11-1 | 2 | FAIL | P2: required TE-11 not flagged; P5: Zero-flags line present but not expected |  |
| TE-11-1 | 3 | PASS |  |  |
| TE-12-1 | 1 | FAIL | P1: expected ['endorsement'], got ['none'] | TE-06, TE-08, TE-10 |
| TE-12-1 | 2 | FAIL | P1: expected ['endorsement'], got ['none'] | TE-06, TE-08, TE-10 |
| TE-12-1 | 3 | FAIL | P1: expected ['endorsement'], got ['none'] | TE-06, TE-08, TE-10 |
| TE-13-1 | 1 | PASS |  |  |
| TE-13-1 | 2 | PASS |  |  |
| TE-13-1 | 3 | PASS |  |  |
| TPR-01-1 | 1 | FAIL | P2: TPR-01 flagged but Where lacks any of ['I have not reviewed how the survey is put together'] |  |
| TPR-01-1 | 2 | FAIL | P2: TPR-01 flagged but Where lacks any of ['I have not reviewed how the survey is put together'] |  |
| TPR-01-1 | 3 | PASS |  |  |
| TPR-02-1 | 1 | FAIL | P2: required TPR-02 not flagged; P4: no Confirm block lists Would apply ['TPR-05', 'TPR-06'] |  |
| TPR-02-1 | 2 | FAIL | P2: required TPR-02 not flagged; P4: no Confirm block lists Would apply ['TPR-05', 'TPR-06'] |  |
| TPR-02-1 | 3 | FAIL | P2: required TPR-02 not flagged |  |
| TPR-03-1 | 1 | PASS |  |  |
| TPR-03-1 | 2 | PASS |  |  |
| TPR-03-1 | 3 | PASS |  |  |
| TPR-04-1 | 1 | PASS |  |  |
| TPR-04-1 | 2 | FAIL | P2: TPR-04 flagged but Where lacks any of ["the name of the organization behind it isn't shown"] |  |
| TPR-04-1 | 3 | PASS |  |  |
| TPR-05-1 | 1 | PASS |  |  |
| TPR-05-1 | 2 | PASS |  |  |
| TPR-05-1 | 3 | PASS |  |  |
| TPR-06-1 | 1 | PASS |  |  |
| TPR-06-1 | 2 | PASS |  | TPR-05 |
| TPR-06-1 | 3 | PASS |  | TPR-05 |
| TPR-07-1 | 1 | PASS |  |  |
| TPR-07-1 | 2 | FAIL | P2: TPR-07 flagged but Where lacks any of ['in the footer at the bottom of the page'] |  |
| TPR-07-1 | 3 | FAIL | P2: TPR-07 flagged but Where lacks any of ['in the footer at the bottom of the page'] |  |
| UNR-01 | 1 | PASS |  |  |
| UNR-01 | 2 | FAIL | P2: required GP-15 not flagged; P5: Zero-flags line present but not expected |  |
| UNR-01 | 3 | PASS |  |  |
| UNR-02 | 1 | PASS |  |  |
| UNR-02 | 2 | PASS |  |  |
| UNR-02 | 3 | PASS |  |  |
| UNR-03 | 1 | PASS |  |  |
| UNR-03 | 2 | PASS |  |  |
| UNR-03 | 3 | PASS |  |  |
| VRQ-01 | 1 | PASS |  |  |
| VRQ-01 | 2 | PASS |  |  |
| VRQ-01 | 3 | PASS |  |  |
| VRQ-02 | 1 | PASS |  |  |
| VRQ-02 | 2 | PASS |  |  |
| VRQ-02 | 3 | PASS |  |  |
| VRQ-03 | 1 | PASS |  | GP-01, TE-08, TE-09, TE-10 |
| VRQ-03 | 2 | PASS |  | TE-08, TE-10 |
| VRQ-03 | 3 | PASS |  | GP-01, TE-08, TE-09, TE-10 |

## Per fixture

| fixture | class | n | hard failures | P-assertions clean | needs | verdict |
|---|---|---|---|---|---|---|
| CLR-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CLR-02 | adversarial | 3 | 0 | 1/3 | 2/3 | FAIL |
| CLR-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CNF-02 | adversarial | 3 | 0 | 1/3 | 2/3 | FAIL |
| CNF-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CNF-04 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CUR-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CUR-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CUR-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| NOM-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| NOM-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| NOM-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| OVL-01 | adversarial | 3 | 0 | 1/3 | 2/3 | FAIL |
| OVL-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| OVL-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| SCP-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| SCP-02 | adversarial | 3 | 0 | 2/3 | 2/3 | PASS |
| SCP-03 | adversarial | 3 | 1 | 3/3 | 2/3 | FAIL |
| SCP-04 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| UNR-01 | adversarial | 3 | 0 | 2/3 | 2/3 | PASS |
| UNR-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| UNR-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| VRQ-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| VRQ-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| VRQ-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-01-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-02-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-03-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-04-1 | entry | 3 | 0 | 1/3 | 2/3 | FAIL |
| GP-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-07-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| GP-08-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-09-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-10-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-11-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-12-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-13-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-14-1 | entry | 3 | 0 | 1/3 | 2/3 | FAIL |
| GP-15-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-16-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-01-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-02-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| PERF-03-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-04-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-07-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-08-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-09-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-10-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-11-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-12-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-13-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-14-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-15-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| PERF-16-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-01-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| TE-02-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-03-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| TE-04-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-07-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-08-1 | entry | 3 | 0 | 1/3 | 2/3 | FAIL |
| TE-09-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| TE-10-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-11-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| TE-12-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| TE-13-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-01-1 | entry | 3 | 0 | 1/3 | 2/3 | FAIL |
| TPR-02-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| TPR-03-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-04-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| TPR-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-07-1 | entry | 3 | 0 | 1/3 | 2/3 | FAIL |

## Totals

- entry: samples 124/156 pass; fixtures 41/52 pass
- adversarial: samples 66/75 pass; fixtures 21/25 pass
- samples: 190/231 pass (82.3%); floor 95% NOT met
- fixtures: 62/77 pass (hard checks isolation, contaminated, U0, U1, U2, U3, U4, U5, P0, P3; majority checks P1, P2, P4, P5)

RUN: FAIL
