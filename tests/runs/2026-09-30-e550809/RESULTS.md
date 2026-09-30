# Results

- run_id: 2026-09-30-e550809
- date: 2026-09-30
- skill_commit: e550809
- model: claude-sonnet-5
- fixtures: 77
- n_entry: 3
- n_adversarial: 3
- notes: run 8 pinned rerun per run-model-drift. A first launch was killed at 21/231 by the session's background time limit, and was discarded and restarted clean; no fixes of any kind were made.

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
| GP-03-1 | 2 | FAIL | P2: required GP-03 not flagged; P5: Zero-flags line present but not expected |  |
| GP-03-1 | 3 | FAIL | P2: required GP-03 not flagged; P5: Zero-flags line present but not expected |  |
| GP-04-1 | 1 | PASS |  |  |
| GP-04-1 | 2 | PASS |  |  |
| GP-04-1 | 3 | PASS |  |  |
| GP-05-1 | 1 | PASS |  |  |
| GP-05-1 | 2 | PASS |  |  |
| GP-05-1 | 3 | PASS |  |  |
| GP-06-1 | 1 | PASS |  |  |
| GP-06-1 | 2 | PASS |  |  |
| GP-06-1 | 3 | PASS |  |  |
| GP-07-1 | 1 | FAIL | P2: required GP-07 not flagged; P5: Zero-flags line present but not expected |  |
| GP-07-1 | 2 | FAIL | P2: required GP-07 not flagged; P5: Zero-flags line present but not expected |  |
| GP-07-1 | 3 | PASS |  |  |
| GP-08-1 | 1 | PASS |  |  |
| GP-08-1 | 2 | PASS |  |  |
| GP-08-1 | 3 | PASS |  |  |
| GP-09-1 | 1 | PASS |  |  |
| GP-09-1 | 2 | PASS |  |  |
| GP-09-1 | 3 | PASS |  |  |
| GP-10-1 | 1 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-10-1 | 2 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-10-1 | 3 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-11-1 | 1 | FAIL | P2: GP-11 flagged but Where lacks any of ['Those are app-store reviews of the software', 'what users say about PlanPath'] | GP-06 |
| GP-11-1 | 2 | PASS |  |  |
| GP-11-1 | 3 | PASS |  |  |
| GP-12-1 | 1 | PASS |  |  |
| GP-12-1 | 2 | PASS |  |  |
| GP-12-1 | 3 | PASS |  |  |
| GP-13-1 | 1 | FAIL | P2: required GP-13 not flagged; P5: Zero-flags line present but not expected |  |
| GP-13-1 | 2 | PASS |  |  |
| GP-13-1 | 3 | PASS |  |  |
| GP-14-1 | 1 | PASS |  | TPR-01, TPR-05, TPR-06 |
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
| OVL-01 | 1 | PASS |  | TE-08, TE-10, TE-13 |
| OVL-01 | 2 | PASS |  | TE-05, TE-08 |
| OVL-01 | 3 | PASS |  | TE-05, TE-08, TE-10 |
| OVL-02 | 1 | PASS |  |  |
| OVL-02 | 2 | PASS |  |  |
| OVL-02 | 3 | PASS |  |  |
| OVL-03 | 1 | PASS |  |  |
| OVL-03 | 2 | PASS |  |  |
| OVL-03 | 3 | PASS |  |  |
| PERF-01-1 | 1 | PASS |  | PERF-07, PERF-12 |
| PERF-01-1 | 2 | PASS |  | PERF-03, PERF-04, PERF-07, PERF-12, PERF-16 |
| PERF-01-1 | 3 | PASS |  | PERF-07, PERF-12, PERF-13 |
| PERF-02-1 | 1 | FAIL | P2: PERF-02 flagged but Where lacks any of ['the fund returned 9.6% for 1 year'] |  |
| PERF-02-1 | 2 | FAIL | P2: PERF-02 flagged but Where lacks any of ['the fund returned 9.6% for 1 year'] |  |
| PERF-02-1 | 3 | FAIL | P2: PERF-02 flagged but Where lacks any of ['the fund returned 9.6% for 1 year'] |  |
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
| PERF-09-1 | 1 | PASS |  | PERF-16 |
| PERF-09-1 | 2 | PASS |  | PERF-01, PERF-16 |
| PERF-09-1 | 3 | PASS |  | PERF-16 |
| PERF-10-1 | 1 | PASS |  |  |
| PERF-10-1 | 2 | PASS |  |  |
| PERF-10-1 | 3 | PASS |  |  |
| PERF-11-1 | 1 | FAIL | P2: required PERF-11 not flagged; P5: Zero-flags line present but not expected |  |
| PERF-11-1 | 2 | FAIL | P2: required PERF-11 not flagged; P5: Zero-flags line present but not expected |  |
| PERF-11-1 | 3 | FAIL | P2: required PERF-11 not flagged; P5: Zero-flags line present but not expected |  |
| PERF-12-1 | 1 | PASS |  |  |
| PERF-12-1 | 2 | PASS |  |  |
| PERF-12-1 | 3 | PASS |  |  |
| PERF-13-1 | 1 | PASS |  | PERF-07 |
| PERF-13-1 | 2 | PASS |  |  |
| PERF-13-1 | 3 | PASS |  | PERF-01, PERF-07 |
| PERF-14-1 | 1 | PASS |  | PERF-08 |
| PERF-14-1 | 2 | PASS |  |  |
| PERF-14-1 | 3 | PASS |  |  |
| PERF-15-1 | 1 | PASS |  |  |
| PERF-15-1 | 2 | PASS |  |  |
| PERF-15-1 | 3 | PASS |  |  |
| PERF-16-1 | 1 | PASS |  |  |
| PERF-16-1 | 2 | PASS |  |  |
| PERF-16-1 | 3 | PASS |  |  |
| SCP-01 | 1 | PASS |  |  |
| SCP-01 | 2 | PASS |  |  |
| SCP-01 | 3 | PASS |  |  |
| SCP-02 | 1 | PASS |  | TE-08, TE-10 |
| SCP-02 | 2 | PASS |  |  |
| SCP-02 | 3 | PASS |  | TE-13 |
| SCP-03 | 1 | PASS |  |  |
| SCP-03 | 2 | PASS |  |  |
| SCP-03 | 3 | PASS |  |  |
| SCP-04 | 1 | PASS |  |  |
| SCP-04 | 2 | PASS |  |  |
| SCP-04 | 3 | PASS |  |  |
| TE-01-1 | 1 | PASS |  |  |
| TE-01-1 | 2 | PASS |  |  |
| TE-01-1 | 3 | PASS |  | TE-03 |
| TE-02-1 | 1 | PASS |  | GP-12, TE-06, TE-08, TE-10 |
| TE-02-1 | 2 | PASS |  | GP-12, TE-06, TE-08, TE-10 |
| TE-02-1 | 3 | PASS |  | GP-12, TE-06, TE-08, TE-10 |
| TE-03-1 | 1 | PASS |  | TE-13, TPR-03 |
| TE-03-1 | 2 | PASS |  | TE-13, TPR-03, TPR-06 |
| TE-03-1 | 3 | PASS |  | GP-01, TE-13, TPR-03 |
| TE-04-1 | 1 | PASS |  | GP-01, TE-01, TE-03, TE-08, TE-10 |
| TE-04-1 | 2 | PASS |  | TE-01, TE-03, TE-08, TE-09, TE-10 |
| TE-04-1 | 3 | PASS |  | TE-01, TE-03 |
| TE-05-1 | 1 | PASS |  | TE-08, TE-09, TE-10 |
| TE-05-1 | 2 | PASS |  | GP-01, TE-08, TE-09, TE-10 |
| TE-05-1 | 3 | PASS |  | TE-08, TE-10 |
| TE-06-1 | 1 | PASS |  |  |
| TE-06-1 | 2 | PASS |  |  |
| TE-06-1 | 3 | PASS |  |  |
| TE-07-1 | 1 | PASS |  | TE-08, TE-09, TE-10 |
| TE-07-1 | 2 | PASS |  | TE-06, TE-08, TE-10 |
| TE-07-1 | 3 | PASS |  | TE-06, TE-08, TE-10 |
| TE-08-1 | 1 | PASS |  | TE-09, TE-10 |
| TE-08-1 | 2 | PASS |  | TE-09, TE-10 |
| TE-08-1 | 3 | PASS |  | TE-09, TE-10 |
| TE-09-1 | 1 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 2 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 3 | PASS |  | TE-08, TE-10 |
| TE-10-1 | 1 | PASS |  | TE-08 |
| TE-10-1 | 2 | PASS |  | TE-08, TE-09 |
| TE-10-1 | 3 | PASS |  | TE-08, TE-09 |
| TE-11-1 | 1 | PASS |  |  |
| TE-11-1 | 2 | FAIL | P2: required TE-11 not flagged; P5: Zero-flags line present but not expected |  |
| TE-11-1 | 3 | PASS |  |  |
| TE-12-1 | 1 | PASS |  |  |
| TE-12-1 | 2 | PASS |  |  |
| TE-12-1 | 3 | PASS |  | TE-06, TE-08, TE-10 |
| TE-13-1 | 1 | PASS |  |  |
| TE-13-1 | 2 | PASS |  |  |
| TE-13-1 | 3 | PASS |  |  |
| TPR-01-1 | 1 | PASS |  |  |
| TPR-01-1 | 2 | PASS |  |  |
| TPR-01-1 | 3 | PASS |  |  |
| TPR-02-1 | 1 | PASS |  |  |
| TPR-02-1 | 2 | FAIL | P4: no Confirm block lists Would apply ['TPR-05', 'TPR-06'] |  |
| TPR-02-1 | 3 | PASS |  |  |
| TPR-03-1 | 1 | PASS |  |  |
| TPR-03-1 | 2 | PASS |  |  |
| TPR-03-1 | 3 | PASS |  |  |
| TPR-04-1 | 1 | PASS |  |  |
| TPR-04-1 | 2 | PASS |  | TPR-07 |
| TPR-04-1 | 3 | PASS |  |  |
| TPR-05-1 | 1 | PASS |  |  |
| TPR-05-1 | 2 | PASS |  |  |
| TPR-05-1 | 3 | PASS |  |  |
| TPR-06-1 | 1 | PASS |  | TPR-05 |
| TPR-06-1 | 2 | PASS |  | TPR-05 |
| TPR-06-1 | 3 | PASS |  | TPR-05 |
| TPR-07-1 | 1 | PASS |  |  |
| TPR-07-1 | 2 | PASS |  |  |
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
| VRQ-03 | 1 | PASS |  | GP-01, TE-08, TE-10 |
| VRQ-03 | 2 | PASS |  | TE-08, TE-09, TE-10 |
| VRQ-03 | 3 | PASS |  | TE-08, TE-09, TE-10 |

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
| OVL-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| SCP-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
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
| GP-03-1 | entry | 3 | 0 | 1/3 | 2/3 | FAIL |
| GP-04-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-07-1 | entry | 3 | 0 | 1/3 | 2/3 | FAIL |
| GP-08-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-09-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-10-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-11-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| GP-12-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-13-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| GP-14-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
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
| PERF-11-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| PERF-12-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-13-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-14-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
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
| TE-11-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| TE-12-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-13-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-01-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-02-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| TPR-03-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-04-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-07-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |

## Totals

- entry: samples 142/156 pass; fixtures 48/52 pass
- adversarial: samples 75/75 pass; fixtures 25/25 pass
- samples: 217/231 pass (93.9%); floor 95% NOT met
- fixtures: 73/77 pass (hard checks isolation, contaminated, U0, U1, U2, U3, U4, U5, P0, P3; majority checks P1, P2, P4, P5)

RUN: FAIL
