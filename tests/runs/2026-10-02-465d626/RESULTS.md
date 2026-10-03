# Results

- run_id: 2026-10-02-465d626
- date: 2026-10-02
- skill_commit: 465d626
- model: claude-sonnet-5
- fixtures: 77
- n_entry: 3
- n_adversarial: 3
- notes: run 11 per run-11. A container restart (~2026-10-02T19:16Z) killed the launcher at 12/231; resumed 2026-10-03 under infra-kill-resume with --skip-done, the 12 done samples standing and the 4 killed samples (GP-05-1.1, GP-05-1.2, GP-05-1.3, GP-06-1.1) relaunched fresh, their evidence kept as .attempt0. One timeout relaunch under timeout-relaunch (TE-07-1.3, done on attempt 2). No fixes of any kind were made.

| fixture | k | verdict | failed checks | extras |
|---|---|---|---|---|
| CLR-01 | 1 | PASS |  |  |
| CLR-01 | 2 | PASS |  |  |
| CLR-01 | 3 | PASS |  |  |
| CLR-02 | 1 | PASS |  |  |
| CLR-02 | 2 | PASS |  |  |
| CLR-02 | 3 | PASS |  |  |
| CLR-03 | 1 | PASS |  |  |
| CLR-03 | 2 | PASS |  |  |
| CLR-03 | 3 | PASS |  |  |
| CNF-02 | 1 | PASS |  |  |
| CNF-02 | 2 | PASS |  |  |
| CNF-02 | 3 | PASS |  |  |
| CNF-03 | 1 | PASS |  |  |
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
| GP-04-1 | 1 | PASS |  |  |
| GP-04-1 | 2 | PASS |  |  |
| GP-04-1 | 3 | PASS |  |  |
| GP-05-1 | 1 | PASS |  |  |
| GP-05-1 | 2 | PASS |  |  |
| GP-05-1 | 3 | PASS |  |  |
| GP-06-1 | 1 | PASS |  |  |
| GP-06-1 | 2 | PASS |  |  |
| GP-06-1 | 3 | PASS |  |  |
| GP-07-1 | 1 | PASS |  |  |
| GP-07-1 | 2 | PASS |  |  |
| GP-07-1 | 3 | PASS |  |  |
| GP-08-1 | 1 | PASS |  |  |
| GP-08-1 | 2 | PASS |  |  |
| GP-08-1 | 3 | PASS |  |  |
| GP-09-1 | 1 | PASS |  |  |
| GP-09-1 | 2 | PASS |  |  |
| GP-09-1 | 3 | PASS |  | GP-10 |
| GP-10-1 | 1 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-10-1 | 2 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-10-1 | 3 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-11-1 | 1 | PASS |  | GP-06 |
| GP-11-1 | 2 | PASS |  |  |
| GP-11-1 | 3 | PASS |  |  |
| GP-12-1 | 1 | PASS |  |  |
| GP-12-1 | 2 | PASS |  |  |
| GP-12-1 | 3 | PASS |  |  |
| GP-13-1 | 1 | PASS |  |  |
| GP-13-1 | 2 | PASS |  |  |
| GP-13-1 | 3 | PASS |  |  |
| GP-14-1 | 1 | FAIL | P2: required GP-14 not flagged | TPR-01, TPR-05, TPR-06 |
| GP-14-1 | 2 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-14-1 | 3 | PASS |  | TPR-01, TPR-05, TPR-06 |
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
| OVL-01 | 1 | PASS |  |  |
| OVL-01 | 2 | PASS |  | TE-08, TE-10 |
| OVL-01 | 3 | PASS |  | TE-08, TE-10 |
| OVL-02 | 1 | PASS |  |  |
| OVL-02 | 2 | PASS |  |  |
| OVL-02 | 3 | PASS |  |  |
| OVL-03 | 1 | PASS |  |  |
| OVL-03 | 2 | PASS |  |  |
| OVL-03 | 3 | FAIL | P2: TPR-03 flagged but Where lacks any of ['with no date on it'] / TPR-04 flagged but Where lacks any of ['no name of the organization that produced it'] |  |
| PERF-01-1 | 1 | FAIL | P1: expected ['gross performance', 'hypothetical performance', 'net performance'], got ['gross performance', 'net performance'] | PERF-03, PERF-04, PERF-07, PERF-16 |
| PERF-01-1 | 2 | PASS |  | PERF-07, PERF-12, PERF-15 |
| PERF-01-1 | 3 | PASS |  | PERF-12 |
| PERF-02-1 | 1 | PASS |  |  |
| PERF-02-1 | 2 | PASS |  |  |
| PERF-02-1 | 3 | PASS |  |  |
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
| PERF-06-1 | 2 | PASS |  | PERF-03 |
| PERF-06-1 | 3 | PASS |  | PERF-03 |
| PERF-07-1 | 1 | PASS |  |  |
| PERF-07-1 | 2 | PASS |  |  |
| PERF-07-1 | 3 | PASS |  |  |
| PERF-08-1 | 1 | PASS |  |  |
| PERF-08-1 | 2 | PASS |  |  |
| PERF-08-1 | 3 | PASS |  |  |
| PERF-09-1 | 1 | PASS |  | PERF-01, PERF-16 |
| PERF-09-1 | 2 | FAIL | P2: PERF-09 flagged but Where lacks any of ['Our five best-performing positions of 2025'] | PERF-01, PERF-16 |
| PERF-09-1 | 3 | PASS |  | PERF-16 |
| PERF-10-1 | 1 | PASS |  |  |
| PERF-10-1 | 2 | PASS |  |  |
| PERF-10-1 | 3 | PASS |  |  |
| PERF-11-1 | 1 | PASS |  |  |
| PERF-11-1 | 2 | PASS |  |  |
| PERF-11-1 | 3 | PASS |  |  |
| PERF-12-1 | 1 | PASS |  |  |
| PERF-12-1 | 2 | PASS |  |  |
| PERF-12-1 | 3 | PASS |  |  |
| PERF-13-1 | 1 | PASS |  | PERF-01, PERF-07 |
| PERF-13-1 | 2 | PASS |  |  |
| PERF-13-1 | 3 | PASS |  | PERF-01, PERF-07 |
| PERF-14-1 | 1 | FAIL | P2: PERF-14 flagged but Where lacks any of ['would grow to $1.3 million in ten years'] | PERF-08, PERF-12 |
| PERF-14-1 | 2 | PASS |  |  |
| PERF-14-1 | 3 | FAIL | P2: PERF-14 flagged but Where lacks any of ['would grow to $1.3 million in ten years'] | PERF-01 |
| PERF-15-1 | 1 | PASS |  |  |
| PERF-15-1 | 2 | PASS |  |  |
| PERF-15-1 | 3 | PASS |  |  |
| PERF-16-1 | 1 | PASS |  |  |
| PERF-16-1 | 2 | PASS |  |  |
| PERF-16-1 | 3 | PASS |  |  |
| SCP-01 | 1 | PASS |  |  |
| SCP-01 | 2 | PASS |  |  |
| SCP-01 | 3 | FAIL | P5: Scope marker 'a broker-dealer' lacks 'FINRA' |  |
| SCP-02 | 1 | PASS |  |  |
| SCP-02 | 2 | PASS |  |  |
| SCP-02 | 3 | PASS |  |  |
| SCP-03 | 1 | PASS |  |  |
| SCP-03 | 2 | PASS |  |  |
| SCP-03 | 3 | PASS |  |  |
| SCP-04 | 1 | PASS |  |  |
| SCP-04 | 2 | PASS |  |  |
| SCP-04 | 3 | PASS |  |  |
| TE-01-1 | 1 | PASS |  |  |
| TE-01-1 | 2 | PASS |  |  |
| TE-01-1 | 3 | PASS |  |  |
| TE-02-1 | 1 | PASS |  | GP-12, TE-01, TE-08, TE-10 |
| TE-02-1 | 2 | PASS |  | GP-12, TE-01, TE-05, TE-06 |
| TE-02-1 | 3 | PASS |  | GP-12, TE-06, TE-08, TE-10 |
| TE-03-1 | 1 | PASS |  | TE-13, TPR-03 |
| TE-03-1 | 2 | PASS |  | TE-13, TPR-03 |
| TE-03-1 | 3 | PASS |  | TE-13, TPR-03 |
| TE-04-1 | 1 | PASS |  | GP-01, TE-03, TE-08, TE-10 |
| TE-04-1 | 2 | PASS |  | GP-01, TE-03 |
| TE-04-1 | 3 | PASS |  | GP-01, TE-03, TE-08, TE-10 |
| TE-05-1 | 1 | PASS |  | TE-08, TE-10 |
| TE-05-1 | 2 | PASS |  | GP-01, TE-08, TE-10 |
| TE-05-1 | 3 | PASS |  | TE-08, TE-09, TE-10 |
| TE-06-1 | 1 | PASS |  |  |
| TE-06-1 | 2 | PASS |  |  |
| TE-06-1 | 3 | PASS |  |  |
| TE-07-1 | 1 | PASS |  | TE-06, TE-08, TE-10 |
| TE-07-1 | 2 | PASS |  | TE-06, TE-08, TE-10 |
| TE-07-1 | 3 | PASS |  | TE-06, TE-08, TE-09, TE-10 |
| TE-08-1 | 1 | PASS |  | TE-09, TE-10 |
| TE-08-1 | 2 | PASS |  | GP-01, TE-09, TE-10 |
| TE-08-1 | 3 | PASS |  | TE-10 |
| TE-09-1 | 1 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 2 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 3 | PASS |  | GP-01, TE-08, TE-10 |
| TE-10-1 | 1 | PASS |  | TE-08, TE-09 |
| TE-10-1 | 2 | PASS |  | GP-01, TE-08 |
| TE-10-1 | 3 | PASS |  | TE-08 |
| TE-11-1 | 1 | FAIL | P2: required TE-11 not flagged; P5: Zero-flags line present but not expected |  |
| TE-11-1 | 2 | FAIL | P2: required TE-11 not flagged; P5: Zero-flags line present but not expected |  |
| TE-11-1 | 3 | FAIL | P2: required TE-11 not flagged | GP-01 |
| TE-12-1 | 1 | PASS |  |  |
| TE-12-1 | 2 | PASS |  |  |
| TE-12-1 | 3 | PASS |  |  |
| TE-13-1 | 1 | FAIL | U5: Flag 1 Where quote '\\' is not in the fixture |  |
| TE-13-1 | 2 | PASS |  |  |
| TE-13-1 | 3 | PASS |  |  |
| TPR-01-1 | 1 | PASS |  |  |
| TPR-01-1 | 2 | PASS |  |  |
| TPR-01-1 | 3 | PASS |  |  |
| TPR-02-1 | 1 | PASS |  |  |
| TPR-02-1 | 2 | PASS |  |  |
| TPR-02-1 | 3 | PASS |  |  |
| TPR-03-1 | 1 | PASS |  |  |
| TPR-03-1 | 2 | PASS |  |  |
| TPR-03-1 | 3 | PASS |  |  |
| TPR-04-1 | 1 | PASS |  | TPR-07 |
| TPR-04-1 | 2 | PASS |  |  |
| TPR-04-1 | 3 | PASS |  |  |
| TPR-05-1 | 1 | PASS |  |  |
| TPR-05-1 | 2 | PASS |  |  |
| TPR-05-1 | 3 | PASS |  |  |
| TPR-06-1 | 1 | PASS |  | TPR-05 |
| TPR-06-1 | 2 | PASS |  | TPR-05 |
| TPR-06-1 | 3 | PASS |  | TPR-05 |
| TPR-07-1 | 1 | PASS |  | GP-12 |
| TPR-07-1 | 2 | FAIL | P2: TPR-07 flagged but Where lacks any of ["that's the badge at the top of every page on our site", 'sit in the footer at the bottom of the page, in smaller type'] | GP-12 |
| TPR-07-1 | 3 | PASS |  |  |
| UNR-01 | 1 | PASS |  |  |
| UNR-01 | 2 | PASS |  |  |
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
| VRQ-03 | 3 | PASS |  | TE-08, TE-10 |

## Per fixture

| fixture | class | n | hard failures | P-assertions clean | needs | verdict |
|---|---|---|---|---|---|---|
| CLR-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CLR-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CLR-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CNF-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CNF-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CNF-04 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CUR-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CUR-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CUR-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| NOM-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| NOM-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| NOM-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| OVL-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| OVL-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| OVL-03 | adversarial | 3 | 0 | 2/3 | 2/3 | PASS |
| SCP-01 | adversarial | 3 | 0 | 2/3 | 2/3 | PASS |
| SCP-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| SCP-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| SCP-04 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| UNR-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| UNR-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| UNR-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| VRQ-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| VRQ-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| VRQ-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-01-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-02-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-03-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-04-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-07-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-08-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-09-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-10-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-11-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-12-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-13-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-14-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| GP-15-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-16-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-01-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| PERF-02-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-03-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-04-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-07-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-08-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-09-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| PERF-10-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-11-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-12-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-13-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-14-1 | entry | 3 | 0 | 1/3 | 2/3 | FAIL |
| PERF-15-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-16-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-01-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-02-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-03-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-04-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-07-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-08-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-09-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-10-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-11-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| TE-12-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-13-1 | entry | 3 | 1 | 3/3 | 2/3 | FAIL |
| TPR-01-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-02-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-03-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-04-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-07-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |

## Totals

- entry: samples 146/156 pass; fixtures 49/52 pass
- adversarial: samples 73/75 pass; fixtures 25/25 pass
- samples: 219/231 pass (94.8%); floor 95% NOT met
- fixtures: 74/77 pass (hard checks isolation, contaminated, U0, U1, U2, U3, U4, U5, P0, P3; majority checks P1, P2, P4, P5)

RUN: FAIL
