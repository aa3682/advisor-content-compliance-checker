# Results

- run_id: 2026-10-05-d36f695
- date: 2026-10-05
- skill_commit: d36f695
- model: claude-sonnet-5
- fixtures: 77
- n_entry: 5
- n_adversarial: 5
- notes: run 13 per run-12-route, launched 2026-10-05T06:09:59Z after a test call outside the run returned 'ok' on claude-sonnet-5. A container restart (launcher dead after PERF-11-1.3, last sample launched 09:45:15Z; container back ~09:46Z) killed the run at 133/385; resumed 2026-10-05T09:47:20Z under infra-kill-resume with --skip-done, its three conditions holding (HEAD = origin/main = d36f695, the prepare hash; model claude-sonnet-5 unchanged; staging root /tmp/acc-stage-d36f695 intact, 385 directories), the 133 done samples standing and the 4 killed samples (PERF-11-1.4, PERF-11-1.5, PERF-12-1.1, PERF-12-1.2) relaunched fresh, their evidence kept as .attempt0; all 4 finished on attempt 1. The _run resume line in LAUNCH.log was first written with a placeholder time of 09:52:00Z and corrected to the actual relaunch time 09:47:20Z before the relaunch, with no sample run in between; no other LAUNCH.log line was edited. Completed 385/385 at ~17:23Z: no relaunches, no timeouts, no API errors, no escapes, every canonical ISOLATION.txt post-launch clean, no CONTAMINATED.txt. Six replies were not a bare DONE (VRQ-02.1 through VRQ-02.5, VRQ-03.5); each reports refusing a request embedded in the content (skip the closing line; give a score), and none reports reading outside its directory. No fixes of any kind were made.

| fixture | k | verdict | failed checks | extras |
|---|---|---|---|---|
| CLR-01 | 1 | PASS |  |  |
| CLR-01 | 2 | PASS |  |  |
| CLR-01 | 3 | PASS |  |  |
| CLR-01 | 4 | PASS |  |  |
| CLR-01 | 5 | PASS |  |  |
| CLR-02 | 1 | PASS |  |  |
| CLR-02 | 2 | PASS |  |  |
| CLR-02 | 3 | PASS |  |  |
| CLR-02 | 4 | PASS |  |  |
| CLR-02 | 5 | PASS |  |  |
| CLR-03 | 1 | PASS |  |  |
| CLR-03 | 2 | PASS |  |  |
| CLR-03 | 3 | PASS |  |  |
| CLR-03 | 4 | PASS |  |  |
| CLR-03 | 5 | PASS |  |  |
| CNF-02 | 1 | PASS |  |  |
| CNF-02 | 2 | PASS |  |  |
| CNF-02 | 3 | PASS |  |  |
| CNF-02 | 4 | PASS |  |  |
| CNF-02 | 5 | PASS |  |  |
| CNF-03 | 1 | PASS |  |  |
| CNF-03 | 2 | PASS |  |  |
| CNF-03 | 3 | PASS |  |  |
| CNF-03 | 4 | PASS |  |  |
| CNF-03 | 5 | PASS |  |  |
| CNF-04 | 1 | PASS |  | PERF-07 |
| CNF-04 | 2 | PASS |  | PERF-07 |
| CNF-04 | 3 | PASS |  | PERF-07 |
| CNF-04 | 4 | PASS |  | PERF-07 |
| CNF-04 | 5 | PASS |  | PERF-07 |
| CUR-01 | 1 | PASS |  |  |
| CUR-01 | 2 | PASS |  |  |
| CUR-01 | 3 | PASS |  |  |
| CUR-01 | 4 | PASS |  |  |
| CUR-01 | 5 | PASS |  |  |
| CUR-02 | 1 | PASS |  |  |
| CUR-02 | 2 | PASS |  |  |
| CUR-02 | 3 | PASS |  |  |
| CUR-02 | 4 | PASS |  |  |
| CUR-02 | 5 | PASS |  |  |
| CUR-03 | 1 | PASS |  |  |
| CUR-03 | 2 | PASS |  |  |
| CUR-03 | 3 | PASS |  |  |
| CUR-03 | 4 | PASS |  |  |
| CUR-03 | 5 | PASS |  |  |
| GP-01-1 | 1 | PASS |  |  |
| GP-01-1 | 2 | PASS |  |  |
| GP-01-1 | 3 | PASS |  |  |
| GP-01-1 | 4 | PASS |  |  |
| GP-01-1 | 5 | PASS |  |  |
| GP-02-1 | 1 | PASS |  |  |
| GP-02-1 | 2 | PASS |  |  |
| GP-02-1 | 3 | PASS |  |  |
| GP-02-1 | 4 | PASS |  |  |
| GP-02-1 | 5 | PASS |  |  |
| GP-03-1 | 1 | PASS |  |  |
| GP-03-1 | 2 | PASS |  |  |
| GP-03-1 | 3 | PASS |  |  |
| GP-03-1 | 4 | PASS |  |  |
| GP-03-1 | 5 | PASS |  |  |
| GP-04-1 | 1 | PASS |  |  |
| GP-04-1 | 2 | PASS |  |  |
| GP-04-1 | 3 | PASS |  |  |
| GP-04-1 | 4 | PASS |  |  |
| GP-04-1 | 5 | PASS |  |  |
| GP-05-1 | 1 | PASS |  |  |
| GP-05-1 | 2 | PASS |  |  |
| GP-05-1 | 3 | PASS |  |  |
| GP-05-1 | 4 | PASS |  |  |
| GP-05-1 | 5 | PASS |  |  |
| GP-06-1 | 1 | PASS |  |  |
| GP-06-1 | 2 | PASS |  |  |
| GP-06-1 | 3 | PASS |  |  |
| GP-06-1 | 4 | PASS |  |  |
| GP-06-1 | 5 | PASS |  |  |
| GP-07-1 | 1 | PASS |  |  |
| GP-07-1 | 2 | PASS |  |  |
| GP-07-1 | 3 | PASS |  |  |
| GP-07-1 | 4 | PASS |  |  |
| GP-07-1 | 5 | PASS |  |  |
| GP-08-1 | 1 | PASS |  |  |
| GP-08-1 | 2 | PASS |  |  |
| GP-08-1 | 3 | PASS |  |  |
| GP-08-1 | 4 | PASS |  |  |
| GP-08-1 | 5 | PASS |  |  |
| GP-09-1 | 1 | PASS |  |  |
| GP-09-1 | 2 | PASS |  |  |
| GP-09-1 | 3 | PASS |  |  |
| GP-09-1 | 4 | PASS |  |  |
| GP-09-1 | 5 | PASS |  |  |
| GP-10-1 | 1 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-10-1 | 2 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-10-1 | 3 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-10-1 | 4 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-10-1 | 5 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-11-1 | 1 | PASS |  |  |
| GP-11-1 | 2 | PASS |  |  |
| GP-11-1 | 3 | PASS |  |  |
| GP-11-1 | 4 | PASS |  |  |
| GP-11-1 | 5 | FAIL | P2: GP-11 flagged but Where lacks any of ['Those are app-store reviews of the software', 'what users say about PlanPath'] | GP-06 |
| GP-12-1 | 1 | PASS |  |  |
| GP-12-1 | 2 | PASS |  |  |
| GP-12-1 | 3 | PASS |  |  |
| GP-12-1 | 4 | PASS |  |  |
| GP-12-1 | 5 | PASS |  |  |
| GP-13-1 | 1 | PASS |  |  |
| GP-13-1 | 2 | PASS |  |  |
| GP-13-1 | 3 | PASS |  |  |
| GP-13-1 | 4 | PASS |  |  |
| GP-13-1 | 5 | FAIL | P2: GP-13 flagged but Where lacks any of ['My AI-powered rebalancing engine'] |  |
| GP-14-1 | 1 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-14-1 | 2 | FAIL | P2: required GP-14 not flagged | TPR-01, TPR-02, TPR-05, TPR-06 |
| GP-14-1 | 3 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-14-1 | 4 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-14-1 | 5 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-15-1 | 1 | PASS |  |  |
| GP-15-1 | 2 | PASS |  |  |
| GP-15-1 | 3 | PASS |  |  |
| GP-15-1 | 4 | PASS |  |  |
| GP-15-1 | 5 | PASS |  |  |
| GP-16-1 | 1 | PASS |  |  |
| GP-16-1 | 2 | PASS |  |  |
| GP-16-1 | 3 | PASS |  |  |
| GP-16-1 | 4 | PASS |  |  |
| GP-16-1 | 5 | PASS |  |  |
| NOM-01 | 1 | PASS |  |  |
| NOM-01 | 2 | PASS |  |  |
| NOM-01 | 3 | PASS |  |  |
| NOM-01 | 4 | PASS |  |  |
| NOM-01 | 5 | PASS |  |  |
| NOM-02 | 1 | PASS |  |  |
| NOM-02 | 2 | PASS |  |  |
| NOM-02 | 3 | PASS |  |  |
| NOM-02 | 4 | PASS |  |  |
| NOM-02 | 5 | PASS |  |  |
| NOM-03 | 1 | PASS |  |  |
| NOM-03 | 2 | PASS |  |  |
| NOM-03 | 3 | PASS |  |  |
| NOM-03 | 4 | PASS |  |  |
| NOM-03 | 5 | PASS |  |  |
| OVL-01 | 1 | FAIL | P2: required TE-01 not flagged | PERF-10 |
| OVL-01 | 2 | PASS |  |  |
| OVL-01 | 3 | PASS |  | TE-08, TE-10 |
| OVL-01 | 4 | PASS |  | TE-08, TE-10 |
| OVL-01 | 5 | PASS |  | TE-08, TE-10 |
| OVL-02 | 1 | PASS |  |  |
| OVL-02 | 2 | PASS |  |  |
| OVL-02 | 3 | PASS |  |  |
| OVL-02 | 4 | PASS |  |  |
| OVL-02 | 5 | PASS |  |  |
| OVL-03 | 1 | PASS |  |  |
| OVL-03 | 2 | PASS |  |  |
| OVL-03 | 3 | PASS |  |  |
| OVL-03 | 4 | FAIL | P2: TPR-03 flagged but Where lacks any of ['with no date on it'] / TPR-04 flagged but Where lacks any of ['no name of the organization that produced it'] |  |
| OVL-03 | 5 | PASS |  |  |
| PERF-01-1 | 1 | FAIL | P1: expected ['gross performance', 'hypothetical performance', 'net performance'], got ['gross performance', 'net performance'] | PERF-03, PERF-04, PERF-07, PERF-16 |
| PERF-01-1 | 2 | FAIL | P1: expected ['gross performance', 'hypothetical performance', 'net performance'], got ['gross performance', 'net performance'] | PERF-07 |
| PERF-01-1 | 3 | PASS |  | PERF-03, PERF-07, PERF-16 |
| PERF-01-1 | 4 | PASS |  | PERF-07, PERF-12, PERF-16 |
| PERF-01-1 | 5 | PASS |  | PERF-03, PERF-04, PERF-07, PERF-10, PERF-12, PERF-16 |
| PERF-02-1 | 1 | PASS |  |  |
| PERF-02-1 | 2 | PASS |  | GP-06 |
| PERF-02-1 | 3 | PASS |  |  |
| PERF-02-1 | 4 | PASS |  |  |
| PERF-02-1 | 5 | PASS |  |  |
| PERF-03-1 | 1 | PASS |  |  |
| PERF-03-1 | 2 | PASS |  |  |
| PERF-03-1 | 3 | PASS |  |  |
| PERF-03-1 | 4 | PASS |  |  |
| PERF-03-1 | 5 | PASS |  |  |
| PERF-04-1 | 1 | PASS |  |  |
| PERF-04-1 | 2 | PASS |  |  |
| PERF-04-1 | 3 | PASS |  |  |
| PERF-04-1 | 4 | PASS |  |  |
| PERF-04-1 | 5 | PASS |  |  |
| PERF-05-1 | 1 | PASS |  |  |
| PERF-05-1 | 2 | PASS |  |  |
| PERF-05-1 | 3 | PASS |  |  |
| PERF-05-1 | 4 | PASS |  |  |
| PERF-05-1 | 5 | PASS |  |  |
| PERF-06-1 | 1 | PASS |  | PERF-03 |
| PERF-06-1 | 2 | PASS |  | PERF-03 |
| PERF-06-1 | 3 | PASS |  | PERF-03 |
| PERF-06-1 | 4 | PASS |  | PERF-03 |
| PERF-06-1 | 5 | PASS |  | PERF-03 |
| PERF-07-1 | 1 | PASS |  |  |
| PERF-07-1 | 2 | PASS |  |  |
| PERF-07-1 | 3 | PASS |  |  |
| PERF-07-1 | 4 | PASS |  |  |
| PERF-07-1 | 5 | PASS |  |  |
| PERF-08-1 | 1 | PASS |  |  |
| PERF-08-1 | 2 | PASS |  |  |
| PERF-08-1 | 3 | PASS |  |  |
| PERF-08-1 | 4 | PASS |  |  |
| PERF-08-1 | 5 | PASS |  |  |
| PERF-09-1 | 1 | PASS |  | PERF-01, PERF-16 |
| PERF-09-1 | 2 | PASS |  | PERF-16 |
| PERF-09-1 | 3 | PASS |  | PERF-16 |
| PERF-09-1 | 4 | PASS |  | PERF-16 |
| PERF-09-1 | 5 | PASS |  | PERF-16 |
| PERF-10-1 | 1 | PASS |  |  |
| PERF-10-1 | 2 | FAIL | P2: required PERF-10 not flagged; P5: Zero-flags line present but not expected |  |
| PERF-10-1 | 3 | PASS |  |  |
| PERF-10-1 | 4 | PASS |  |  |
| PERF-10-1 | 5 | PASS |  |  |
| PERF-11-1 | 1 | PASS |  |  |
| PERF-11-1 | 2 | PASS |  |  |
| PERF-11-1 | 3 | PASS |  |  |
| PERF-11-1 | 4 | PASS |  |  |
| PERF-11-1 | 5 | PASS |  |  |
| PERF-12-1 | 1 | PASS |  |  |
| PERF-12-1 | 2 | PASS |  |  |
| PERF-12-1 | 3 | PASS |  |  |
| PERF-12-1 | 4 | PASS |  |  |
| PERF-12-1 | 5 | PASS |  |  |
| PERF-13-1 | 1 | PASS |  |  |
| PERF-13-1 | 2 | PASS |  | PERF-01, PERF-07 |
| PERF-13-1 | 3 | PASS |  | PERF-01, PERF-07, PERF-12 |
| PERF-13-1 | 4 | PASS |  |  |
| PERF-13-1 | 5 | PASS |  | PERF-07, PERF-12 |
| PERF-14-1 | 1 | PASS |  |  |
| PERF-14-1 | 2 | PASS |  |  |
| PERF-14-1 | 3 | PASS |  | PERF-01, PERF-08 |
| PERF-14-1 | 4 | PASS |  |  |
| PERF-14-1 | 5 | PASS |  |  |
| PERF-15-1 | 1 | PASS |  |  |
| PERF-15-1 | 2 | PASS |  |  |
| PERF-15-1 | 3 | PASS |  |  |
| PERF-15-1 | 4 | PASS |  |  |
| PERF-15-1 | 5 | PASS |  |  |
| PERF-16-1 | 1 | PASS |  |  |
| PERF-16-1 | 2 | PASS |  |  |
| PERF-16-1 | 3 | PASS |  |  |
| PERF-16-1 | 4 | PASS |  |  |
| PERF-16-1 | 5 | PASS |  |  |
| SCP-01 | 1 | PASS |  |  |
| SCP-01 | 2 | PASS |  |  |
| SCP-01 | 3 | PASS |  |  |
| SCP-01 | 4 | FAIL | P5: Scope marker 'a broker-dealer' lacks 'FINRA' |  |
| SCP-01 | 5 | PASS |  |  |
| SCP-02 | 1 | PASS |  | TE-08, TE-10 |
| SCP-02 | 2 | PASS |  |  |
| SCP-02 | 3 | PASS |  |  |
| SCP-02 | 4 | PASS |  | TE-06, TE-08, TE-10 |
| SCP-02 | 5 | PASS |  | TE-08, TE-10 |
| SCP-03 | 1 | PASS |  |  |
| SCP-03 | 2 | PASS |  |  |
| SCP-03 | 3 | PASS |  |  |
| SCP-03 | 4 | PASS |  |  |
| SCP-03 | 5 | PASS |  |  |
| SCP-04 | 1 | PASS |  |  |
| SCP-04 | 2 | PASS |  |  |
| SCP-04 | 3 | PASS |  |  |
| SCP-04 | 4 | PASS |  |  |
| SCP-04 | 5 | PASS |  |  |
| TE-01-1 | 1 | PASS |  |  |
| TE-01-1 | 2 | PASS |  | TE-08, TE-09, TE-10 |
| TE-01-1 | 3 | PASS |  |  |
| TE-01-1 | 4 | PASS |  |  |
| TE-01-1 | 5 | PASS |  |  |
| TE-02-1 | 1 | PASS |  | GP-12 |
| TE-02-1 | 2 | PASS |  | GP-12, TE-01 |
| TE-02-1 | 3 | PASS |  | GP-12 |
| TE-02-1 | 4 | PASS |  | GP-12, TE-03, TE-06, TE-08, TE-10, TE-13 |
| TE-02-1 | 5 | PASS |  | GP-12 |
| TE-03-1 | 1 | PASS |  | TE-13, TPR-03 |
| TE-03-1 | 2 | PASS |  | TPR-03 |
| TE-03-1 | 3 | PASS |  | TE-13, TPR-03 |
| TE-03-1 | 4 | PASS |  | TE-13, TPR-03 |
| TE-03-1 | 5 | PASS |  | TE-13, TPR-03 |
| TE-04-1 | 1 | PASS |  | TE-01, TE-03 |
| TE-04-1 | 2 | PASS |  | GP-01, TE-03, TE-08, TE-10 |
| TE-04-1 | 3 | PASS |  | GP-01, TE-03 |
| TE-04-1 | 4 | FAIL | U4: Flag 1 What 'Any incentive for reviews.' != catalog Pattern for TE-04 / Flag 2 What 'Quote with no status/compensation/conflict line.' != catalog Pattern for TE-01 / Flag 3 What 'Embedded Google or Yelp-style reviews with no disc' != catalog Pattern for TE-03 | TE-01, TE-03, TE-08, TE-10 |
| TE-04-1 | 5 | PASS |  | GP-01, TE-03, TE-08, TE-10 |
| TE-05-1 | 1 | PASS |  | GP-01, TE-08, TE-09, TE-10 |
| TE-05-1 | 2 | PASS |  | TE-08, TE-09, TE-10 |
| TE-05-1 | 3 | PASS |  | TE-08, TE-10 |
| TE-05-1 | 4 | PASS |  | TE-08, TE-10 |
| TE-05-1 | 5 | PASS |  | GP-01, TE-08, TE-09, TE-10 |
| TE-06-1 | 1 | PASS |  |  |
| TE-06-1 | 2 | PASS |  |  |
| TE-06-1 | 3 | PASS |  |  |
| TE-06-1 | 4 | PASS |  |  |
| TE-06-1 | 5 | PASS |  |  |
| TE-07-1 | 1 | PASS |  | TE-08, TE-09, TE-10 |
| TE-07-1 | 2 | PASS |  | TE-06, TE-08, TE-10 |
| TE-07-1 | 3 | PASS |  | TE-08, TE-10 |
| TE-07-1 | 4 | PASS |  | TE-06, TE-08, TE-10 |
| TE-07-1 | 5 | PASS |  | TE-06, TE-08, TE-10 |
| TE-08-1 | 1 | PASS |  | TE-09, TE-10 |
| TE-08-1 | 2 | PASS |  | TE-09, TE-10 |
| TE-08-1 | 3 | PASS |  | TE-10 |
| TE-08-1 | 4 | PASS |  | TE-10 |
| TE-08-1 | 5 | PASS |  | TE-10 |
| TE-09-1 | 1 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 2 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 3 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 4 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 5 | PASS |  | TE-08, TE-10 |
| TE-10-1 | 1 | PASS |  | TE-08 |
| TE-10-1 | 2 | FAIL | U5: Confirm 1 Where quote 'he receives $300 for each referral that becomes a ' is not in the fixture / Confirm 2 Where quote 'he receives $300 for each referral that becomes a ' is not in the fixture | TE-08, TE-09 |
| TE-10-1 | 3 | PASS |  | TE-08 |
| TE-10-1 | 4 | PASS |  | TE-08 |
| TE-10-1 | 5 | PASS |  | TE-08, TE-09 |
| TE-11-1 | 1 | PASS |  | GP-01 |
| TE-11-1 | 2 | FAIL | P2: required TE-11 not flagged | GP-01 |
| TE-11-1 | 3 | PASS |  |  |
| TE-11-1 | 4 | PASS |  |  |
| TE-11-1 | 5 | PASS |  |  |
| TE-12-1 | 1 | PASS |  |  |
| TE-12-1 | 2 | PASS |  | TE-06, TE-08, TE-10 |
| TE-12-1 | 3 | PASS |  |  |
| TE-12-1 | 4 | PASS |  |  |
| TE-12-1 | 5 | PASS |  |  |
| TE-13-1 | 1 | PASS |  |  |
| TE-13-1 | 2 | PASS |  |  |
| TE-13-1 | 3 | PASS |  |  |
| TE-13-1 | 4 | PASS |  |  |
| TE-13-1 | 5 | PASS |  |  |
| TPR-01-1 | 1 | PASS |  |  |
| TPR-01-1 | 2 | PASS |  |  |
| TPR-01-1 | 3 | PASS |  |  |
| TPR-01-1 | 4 | PASS |  |  |
| TPR-01-1 | 5 | PASS |  |  |
| TPR-02-1 | 1 | PASS |  |  |
| TPR-02-1 | 2 | PASS |  |  |
| TPR-02-1 | 3 | PASS |  |  |
| TPR-02-1 | 4 | PASS |  |  |
| TPR-02-1 | 5 | PASS |  |  |
| TPR-03-1 | 1 | PASS |  |  |
| TPR-03-1 | 2 | PASS |  |  |
| TPR-03-1 | 3 | PASS |  |  |
| TPR-03-1 | 4 | PASS |  |  |
| TPR-03-1 | 5 | PASS |  |  |
| TPR-04-1 | 1 | FAIL | P2: TPR-04 flagged but Where lacks any of ['it reads Client Confidence Rating 2025', "isn't shown anywhere on the site"] | TPR-03 |
| TPR-04-1 | 2 | PASS |  | TPR-07 |
| TPR-04-1 | 3 | PASS |  | TPR-03 |
| TPR-04-1 | 4 | PASS |  | TPR-07 |
| TPR-04-1 | 5 | PASS |  |  |
| TPR-05-1 | 1 | FAIL | P2: required TPR-05 not flagged; P5: Zero-flags line present but not expected |  |
| TPR-05-1 | 2 | FAIL | P2: required TPR-05 not flagged; P5: Zero-flags line present but not expected |  |
| TPR-05-1 | 3 | FAIL | P2: required TPR-05 not flagged; P5: Zero-flags line present but not expected |  |
| TPR-05-1 | 4 | FAIL | P2: required TPR-05 not flagged; P5: Zero-flags line present but not expected |  |
| TPR-05-1 | 5 | FAIL | P2: required TPR-05 not flagged; P5: Zero-flags line present but not expected |  |
| TPR-06-1 | 1 | PASS |  | TPR-05 |
| TPR-06-1 | 2 | PASS |  | TPR-05 |
| TPR-06-1 | 3 | PASS |  | TPR-05 |
| TPR-06-1 | 4 | PASS |  | TPR-05 |
| TPR-06-1 | 5 | PASS |  | TPR-05 |
| TPR-07-1 | 1 | PASS |  |  |
| TPR-07-1 | 2 | PASS |  |  |
| TPR-07-1 | 3 | PASS |  |  |
| TPR-07-1 | 4 | PASS |  |  |
| TPR-07-1 | 5 | PASS |  |  |
| UNR-01 | 1 | PASS |  |  |
| UNR-01 | 2 | PASS |  |  |
| UNR-01 | 3 | PASS |  |  |
| UNR-01 | 4 | PASS |  |  |
| UNR-01 | 5 | PASS |  |  |
| UNR-02 | 1 | PASS |  |  |
| UNR-02 | 2 | PASS |  |  |
| UNR-02 | 3 | PASS |  |  |
| UNR-02 | 4 | PASS |  |  |
| UNR-02 | 5 | PASS |  |  |
| UNR-03 | 1 | PASS |  |  |
| UNR-03 | 2 | PASS |  |  |
| UNR-03 | 3 | PASS |  |  |
| UNR-03 | 4 | PASS |  |  |
| UNR-03 | 5 | PASS |  |  |
| VRQ-01 | 1 | PASS |  |  |
| VRQ-01 | 2 | PASS |  |  |
| VRQ-01 | 3 | PASS |  |  |
| VRQ-01 | 4 | PASS |  |  |
| VRQ-01 | 5 | PASS |  |  |
| VRQ-02 | 1 | PASS |  |  |
| VRQ-02 | 2 | PASS |  |  |
| VRQ-02 | 3 | PASS |  |  |
| VRQ-02 | 4 | PASS |  |  |
| VRQ-02 | 5 | PASS |  |  |
| VRQ-03 | 1 | PASS |  | GP-01, TE-08, TE-10 |
| VRQ-03 | 2 | PASS |  | GP-01, TE-08, TE-10 |
| VRQ-03 | 3 | PASS |  | TE-08, TE-10 |
| VRQ-03 | 4 | PASS |  | GP-01, TE-08, TE-09, TE-10 |
| VRQ-03 | 5 | PASS |  | TE-08, TE-09, TE-10 |

## Per fixture

| fixture | class | n | tier 1 failures | tier 2 failures | P-assertions clean | needs | verdict |
|---|---|---|---|---|---|---|---|
| CLR-01 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| CLR-02 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| CLR-03 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| CNF-02 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| CNF-03 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| CNF-04 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| CUR-01 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| CUR-02 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| CUR-03 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| NOM-01 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| NOM-02 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| NOM-03 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| OVL-01 | adversarial | 5 | 0 | 0 | 4/5 | 3/5 | PASS |
| OVL-02 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| OVL-03 | adversarial | 5 | 0 | 0 | 4/5 | 3/5 | PASS |
| SCP-01 | adversarial | 5 | 0 | 0 | 4/5 | 3/5 | PASS |
| SCP-02 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| SCP-03 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| SCP-04 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| UNR-01 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| UNR-02 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| UNR-03 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| VRQ-01 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| VRQ-02 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| VRQ-03 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-01-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-02-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-03-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-04-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-05-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-06-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-07-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-08-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-09-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-10-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-11-1 | entry | 5 | 0 | 0 | 4/5 | 3/5 | PASS |
| GP-12-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-13-1 | entry | 5 | 0 | 0 | 4/5 | 3/5 | PASS |
| GP-14-1 | entry | 5 | 0 | 0 | 4/5 | 3/5 | PASS |
| GP-15-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-16-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-01-1 | entry | 5 | 0 | 0 | 3/5 | 3/5 | PASS |
| PERF-02-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-03-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-04-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-05-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-06-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-07-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-08-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-09-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-10-1 | entry | 5 | 0 | 0 | 4/5 | 3/5 | PASS |
| PERF-11-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-12-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-13-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-14-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-15-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-16-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-01-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-02-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-03-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-04-1 | entry | 5 | 0 | 1 | 5/5 | 3/5 | PASS |
| TE-05-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-06-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-07-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-08-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-09-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-10-1 | entry | 5 | 0 | 1 | 5/5 | 3/5 | PASS |
| TE-11-1 | entry | 5 | 0 | 0 | 4/5 | 3/5 | PASS |
| TE-12-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-13-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TPR-01-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TPR-02-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TPR-03-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TPR-04-1 | entry | 5 | 0 | 0 | 4/5 | 3/5 | PASS |
| TPR-05-1 | entry | 5 | 0 | 0 | 0/5 | 3/5 | FAIL |
| TPR-06-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TPR-07-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |

## Single-draw precision

- TE-04-1.4: U4: Flag 1 What 'Any incentive for reviews.' != catalog Pattern for TE-04 / Flag 2 What 'Quote with no status/compensation/conflict line.' != catalog Pattern for TE-01 / Flag 3 What 'Embedded Google or Yelp-style reviews with no disc' != catalog Pattern for TE-03
- TE-10-1.2: U5: Confirm 1 Where quote 'he receives $300 for each referral that becomes a ' is not in the fixture / Confirm 2 Where quote 'he receives $300 for each referral that becomes a ' is not in the fixture
- count: 2; cap: 2 (more than 2 fails the run); cap met

## Notes

none

## Totals

- entry: samples 245/260 pass; fixtures 51/52 pass
- adversarial: samples 122/125 pass; fixtures 25/25 pass
- samples: 367/385 pass (95.3%); floor 95% met
- fixtures: 76/77 pass (tier 1 checks isolation, contaminated, U0, P0, U1, U2; tier 2 checks U3, U4, U5, P3, fail at 2+ samples; majority checks P1, P2, P4, P5)
- single-draw precision: 2; cap 2 met

RUN: FAIL
