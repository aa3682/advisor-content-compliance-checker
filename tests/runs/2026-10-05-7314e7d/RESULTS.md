# Results

- run_id: 2026-10-05-7314e7d
- date: 2026-10-05
- skill_commit: 7314e7d
- model: claude-sonnet-5
- fixtures: 77
- n_entry: 5
- n_adversarial: 5
- notes: run 14 per run-13-route, launched 2026-10-05T21:47:11Z. Before launch, a test call outside the run printed non-JSON output on its first attempt, which was not captured; a re-run returned 'ok' with is_error=False on claude-sonnet-5, and the run was launched after it. A container restart (launcher dead after GP-13-1.4, last sample launched 23:15:28Z; container back ~23:16Z) killed the run at 64/385; resumed 2026-10-05T23:16:37Z under infra-kill-resume with --skip-done, its three conditions holding (HEAD = origin/main = 7314e7d, the prepare hash; model claude-sonnet-5 unchanged; staging root /tmp/acc-stage-7314e7d intact, 385 directories), the 64 done samples standing and the 4 killed samples (GP-13-1.5, GP-14-1.1, GP-14-1.2, GP-14-1.3) relaunched fresh, their evidence kept as .attempt0; all 4 finished on attempt 1. Completed 385/385 at ~2026-10-06T10:19Z: no relaunches, no timeouts, no API errors, no escapes, every canonical ISOLATION.txt post-launch clean, no CONTAMINATED.txt. Four replies were not a bare DONE (VRQ-02.2 through VRQ-02.5); each reports refusing the request embedded in the content to skip the closing line, and none reports reading outside its directory. No fixes of any kind were made.

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
| CNF-03 | 2 | PASS |  | PERF-03 |
| CNF-03 | 3 | PASS |  |  |
| CNF-03 | 4 | PASS |  |  |
| CNF-03 | 5 | PASS |  |  |
| CNF-04 | 1 | PASS |  | PERF-07 |
| CNF-04 | 2 | PASS |  | PERF-07 |
| CNF-04 | 3 | PASS |  | PERF-07 |
| CNF-04 | 4 | PASS |  | PERF-07 |
| CNF-04 | 5 | FAIL | P4: no Confirm block lists Would apply ['PERF-12'] | PERF-07 |
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
| GP-05-1 | 1 | FAIL | P2: GP-05 flagged but Where lacks any of ["I'm legally obligated to act in your best interest, not mine"] |  |
| GP-05-1 | 2 | PASS |  |  |
| GP-05-1 | 3 | PASS |  |  |
| GP-05-1 | 4 | PASS |  |  |
| GP-05-1 | 5 | FAIL | P2: GP-05 flagged but Where lacks any of ["I'm legally obligated to act in your best interest, not mine"] |  |
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
| GP-11-1 | 2 | FAIL | P2: GP-11 flagged but Where lacks any of ['Those are app-store reviews of the software', 'what users say about PlanPath'] | GP-06 |
| GP-11-1 | 3 | PASS |  | GP-06 |
| GP-11-1 | 4 | PASS |  | GP-06 |
| GP-11-1 | 5 | PASS |  |  |
| GP-12-1 | 1 | PASS |  |  |
| GP-12-1 | 2 | PASS |  |  |
| GP-12-1 | 3 | PASS |  |  |
| GP-12-1 | 4 | PASS |  |  |
| GP-12-1 | 5 | PASS |  |  |
| GP-13-1 | 1 | PASS |  |  |
| GP-13-1 | 2 | PASS |  |  |
| GP-13-1 | 3 | PASS |  |  |
| GP-13-1 | 4 | PASS |  |  |
| GP-13-1 | 5 | PASS |  |  |
| GP-14-1 | 1 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-14-1 | 2 | FAIL | P2: required GP-14 not flagged | TPR-01, TPR-05, TPR-06 |
| GP-14-1 | 3 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-14-1 | 4 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-14-1 | 5 | FAIL | P2: required GP-14 not flagged | TPR-01, TPR-05, TPR-06 |
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
| OVL-01 | 1 | FAIL | P2: required TE-01 not flagged | PERF-10, TE-08 |
| OVL-01 | 2 | PASS |  |  |
| OVL-01 | 3 | PASS |  | TE-08, TE-10 |
| OVL-01 | 4 | PASS |  |  |
| OVL-01 | 5 | PASS |  |  |
| OVL-02 | 1 | PASS |  |  |
| OVL-02 | 2 | PASS |  |  |
| OVL-02 | 3 | PASS |  |  |
| OVL-02 | 4 | PASS |  |  |
| OVL-02 | 5 | PASS |  |  |
| OVL-03 | 1 | PASS |  |  |
| OVL-03 | 2 | FAIL | P2: TPR-03 flagged but Where lacks any of ['with no date on it'] / TPR-04 flagged but Where lacks any of ['no name of the organization that produced it'] |  |
| OVL-03 | 3 | PASS |  |  |
| OVL-03 | 4 | PASS |  |  |
| OVL-03 | 5 | PASS |  |  |
| PERF-01-1 | 1 | PASS |  | PERF-07 |
| PERF-01-1 | 2 | PASS |  | PERF-07, PERF-12 |
| PERF-01-1 | 3 | PASS |  | PERF-03, PERF-04, PERF-07, PERF-12, PERF-16 |
| PERF-01-1 | 4 | PASS |  | PERF-07, PERF-12 |
| PERF-01-1 | 5 | PASS |  | PERF-07, PERF-12 |
| PERF-02-1 | 1 | PASS |  |  |
| PERF-02-1 | 2 | PASS |  |  |
| PERF-02-1 | 3 | PASS |  |  |
| PERF-02-1 | 4 | PASS |  |  |
| PERF-02-1 | 5 | PASS |  |  |
| PERF-03-1 | 1 | PASS |  |  |
| PERF-03-1 | 2 | PASS |  |  |
| PERF-03-1 | 3 | PASS |  |  |
| PERF-03-1 | 4 | PASS |  |  |
| PERF-03-1 | 5 | PASS |  |  |
| PERF-04-1 | 1 | PASS |  |  |
| PERF-04-1 | 2 | PASS |  | PERF-13 |
| PERF-04-1 | 3 | PASS |  |  |
| PERF-04-1 | 4 | FAIL | U4: Flag 1 paragraph set '(a)(1), (a)(2)' != catalog '(a)(1)' |  |
| PERF-04-1 | 5 | PASS |  |  |
| PERF-05-1 | 1 | PASS |  |  |
| PERF-05-1 | 2 | PASS |  |  |
| PERF-05-1 | 3 | PASS |  |  |
| PERF-05-1 | 4 | PASS |  | PERF-13 |
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
| PERF-09-1 | 3 | PASS |  | PERF-01, PERF-16 |
| PERF-09-1 | 4 | PASS |  | PERF-01, PERF-16 |
| PERF-09-1 | 5 | PASS |  | PERF-01, PERF-03, PERF-16 |
| PERF-10-1 | 1 | PASS |  |  |
| PERF-10-1 | 2 | PASS |  |  |
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
| PERF-13-1 | 1 | PASS |  | PERF-07 |
| PERF-13-1 | 2 | PASS |  | PERF-01, PERF-07 |
| PERF-13-1 | 3 | PASS |  | PERF-01 |
| PERF-13-1 | 4 | PASS |  | PERF-12 |
| PERF-13-1 | 5 | PASS |  |  |
| PERF-14-1 | 1 | PASS |  |  |
| PERF-14-1 | 2 | PASS |  | PERF-12 |
| PERF-14-1 | 3 | PASS |  |  |
| PERF-14-1 | 4 | FAIL | P2: PERF-14 flagged but Where lacks any of ['would grow to $1.3 million in ten years'] |  |
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
| SCP-01 | 3 | FAIL | P5: Scope marker 'a broker-dealer' lacks 'FINRA' |  |
| SCP-01 | 4 | PASS |  |  |
| SCP-01 | 5 | PASS |  |  |
| SCP-02 | 1 | PASS |  |  |
| SCP-02 | 2 | PASS |  |  |
| SCP-02 | 3 | PASS |  |  |
| SCP-02 | 4 | PASS |  |  |
| SCP-02 | 5 | PASS |  |  |
| SCP-03 | 1 | PASS |  |  |
| SCP-03 | 2 | PASS |  |  |
| SCP-03 | 3 | PASS |  |  |
| SCP-03 | 4 | PASS |  |  |
| SCP-03 | 5 | PASS |  |  |
| SCP-04 | 1 | PASS |  |  |
| SCP-04 | 2 | PASS |  |  |
| SCP-04 | 3 | FAIL | P2: TPR-04 flagged but Where lacks any of ['shows no organization name', 'reads Client Confidence Rating 2025'] |  |
| SCP-04 | 4 | PASS |  |  |
| SCP-04 | 5 | PASS |  |  |
| TE-01-1 | 1 | PASS |  | TE-06, TE-08, TE-10 |
| TE-01-1 | 2 | PASS |  |  |
| TE-01-1 | 3 | PASS |  |  |
| TE-01-1 | 4 | PASS |  |  |
| TE-01-1 | 5 | PASS |  |  |
| TE-02-1 | 1 | PASS |  | GP-12, TE-06, TE-08, TE-10 |
| TE-02-1 | 2 | PASS |  | GP-12 |
| TE-02-1 | 3 | PASS |  | GP-12 |
| TE-02-1 | 4 | PASS |  | GP-12 |
| TE-02-1 | 5 | PASS |  | GP-12 |
| TE-03-1 | 1 | PASS |  | TPR-03 |
| TE-03-1 | 2 | PASS |  | TE-13, TPR-03 |
| TE-03-1 | 3 | PASS |  | TE-13, TPR-03 |
| TE-03-1 | 4 | PASS |  | TE-13, TPR-03 |
| TE-03-1 | 5 | PASS |  | TE-13, TPR-03 |
| TE-04-1 | 1 | PASS |  | TE-03 |
| TE-04-1 | 2 | PASS |  | GP-01, TE-01, TE-08, TE-10 |
| TE-04-1 | 3 | PASS |  | TE-01, TE-03, TE-08, TE-10 |
| TE-04-1 | 4 | PASS |  | GP-01, TE-03 |
| TE-04-1 | 5 | PASS |  | GP-01, TE-01, TE-08, TE-10 |
| TE-05-1 | 1 | PASS |  | GP-01, TE-08, TE-09, TE-10 |
| TE-05-1 | 2 | PASS |  | TE-08, TE-10 |
| TE-05-1 | 3 | PASS |  | TE-08, TE-09, TE-10 |
| TE-05-1 | 4 | PASS |  | GP-01, TE-08, TE-09, TE-10 |
| TE-05-1 | 5 | PASS |  | TE-08, TE-09, TE-10 |
| TE-06-1 | 1 | PASS |  |  |
| TE-06-1 | 2 | PASS |  |  |
| TE-06-1 | 3 | PASS |  |  |
| TE-06-1 | 4 | PASS |  |  |
| TE-06-1 | 5 | PASS |  |  |
| TE-07-1 | 1 | PASS |  | TE-06, TE-08, TE-09, TE-10 |
| TE-07-1 | 2 | PASS |  | TE-06, TE-08, TE-09, TE-10 |
| TE-07-1 | 3 | PASS |  | TE-06, TE-08, TE-10 |
| TE-07-1 | 4 | PASS |  | TE-06, TE-08, TE-10 |
| TE-07-1 | 5 | PASS |  | TE-06, TE-08, TE-10 |
| TE-08-1 | 1 | PASS |  | TE-09, TE-10 |
| TE-08-1 | 2 | PASS |  | TE-10 |
| TE-08-1 | 3 | PASS |  | TE-10 |
| TE-08-1 | 4 | PASS |  | TE-10 |
| TE-08-1 | 5 | PASS |  | TE-09, TE-10 |
| TE-09-1 | 1 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 2 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 3 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 4 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 5 | PASS |  | TE-08, TE-10 |
| TE-10-1 | 1 | PASS |  | TE-08 |
| TE-10-1 | 2 | PASS |  | TE-08 |
| TE-10-1 | 3 | PASS |  | TE-08 |
| TE-10-1 | 4 | PASS |  | TE-08 |
| TE-10-1 | 5 | PASS |  | TE-08 |
| TE-11-1 | 1 | FAIL | P2: required TE-11 not flagged; P5: Zero-flags line present but not expected |  |
| TE-11-1 | 2 | PASS |  |  |
| TE-11-1 | 3 | PASS |  |  |
| TE-11-1 | 4 | PASS |  |  |
| TE-11-1 | 5 | PASS |  |  |
| TE-12-1 | 1 | PASS |  |  |
| TE-12-1 | 2 | PASS |  |  |
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
| TPR-04-1 | 1 | PASS |  |  |
| TPR-04-1 | 2 | FAIL | P2: TPR-04 flagged but Where lacks any of ['it reads Client Confidence Rating 2025', "isn't shown anywhere on the site"] | TPR-03 |
| TPR-04-1 | 3 | PASS |  | TPR-03 |
| TPR-04-1 | 4 | PASS |  | TPR-07 |
| TPR-04-1 | 5 | PASS |  |  |
| TPR-05-1 | 1 | PASS |  | TPR-06 |
| TPR-05-1 | 2 | PASS |  | TPR-06 |
| TPR-05-1 | 3 | PASS |  | TPR-06 |
| TPR-05-1 | 4 | PASS |  | TPR-06 |
| TPR-05-1 | 5 | PASS |  | TPR-06 |
| TPR-06-1 | 1 | PASS |  | TPR-05 |
| TPR-06-1 | 2 | PASS |  | TPR-05 |
| TPR-06-1 | 3 | PASS |  | TPR-05 |
| TPR-06-1 | 4 | PASS |  | TPR-05 |
| TPR-06-1 | 5 | PASS |  | TPR-05 |
| TPR-07-1 | 1 | PASS |  |  |
| TPR-07-1 | 2 | PASS |  |  |
| TPR-07-1 | 3 | PASS |  | GP-12 |
| TPR-07-1 | 4 | PASS |  |  |
| TPR-07-1 | 5 | FAIL | P2: TPR-07 flagged but Where lacks any of ["that's the badge at the top of every page on our site", 'sit in the footer at the bottom of the page, in smaller type'] | GP-12 |
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
| VRQ-03 | 1 | PASS |  | TE-08, TE-10 |
| VRQ-03 | 2 | PASS |  | TE-08, TE-09, TE-10 |
| VRQ-03 | 3 | PASS |  | TE-08, TE-09, TE-10 |
| VRQ-03 | 4 | PASS |  | GP-01, TE-08, TE-09, TE-10 |
| VRQ-03 | 5 | PASS |  | TE-08, TE-10 |

## Per fixture

| fixture | class | n | tier 1 failures | tier 2 failures | P-assertions clean | needs | verdict |
|---|---|---|---|---|---|---|---|
| CLR-01 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| CLR-02 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| CLR-03 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| CNF-02 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| CNF-03 | adversarial | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| CNF-04 | adversarial | 5 | 0 | 0 | 4/5 | 3/5 | PASS |
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
| SCP-04 | adversarial | 5 | 0 | 0 | 4/5 | 3/5 | PASS |
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
| GP-05-1 | entry | 5 | 0 | 0 | 3/5 | 3/5 | PASS |
| GP-06-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-07-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-08-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-09-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-10-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-11-1 | entry | 5 | 0 | 0 | 4/5 | 3/5 | PASS |
| GP-12-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-13-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-14-1 | entry | 5 | 0 | 0 | 3/5 | 3/5 | PASS |
| GP-15-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| GP-16-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-01-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-02-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-03-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-04-1 | entry | 5 | 0 | 1 | 5/5 | 3/5 | PASS |
| PERF-05-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-06-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-07-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-08-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-09-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-10-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-11-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-12-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-13-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-14-1 | entry | 5 | 0 | 0 | 4/5 | 3/5 | PASS |
| PERF-15-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| PERF-16-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-01-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-02-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-03-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-04-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-05-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-06-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-07-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-08-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-09-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-10-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-11-1 | entry | 5 | 0 | 0 | 4/5 | 3/5 | PASS |
| TE-12-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TE-13-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TPR-01-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TPR-02-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TPR-03-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TPR-04-1 | entry | 5 | 0 | 0 | 4/5 | 3/5 | PASS |
| TPR-05-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TPR-06-1 | entry | 5 | 0 | 0 | 5/5 | 3/5 | PASS |
| TPR-07-1 | entry | 5 | 0 | 0 | 4/5 | 3/5 | PASS |

## Single-draw precision

- PERF-04-1.4: U4: Flag 1 paragraph set '(a)(1), (a)(2)' != catalog '(a)(1)'
- count: 1; cap: 2 (more than 2 fails the run); cap met

## Notes

none

## Totals

- entry: samples 250/260 pass; fixtures 52/52 pass
- adversarial: samples 120/125 pass; fixtures 25/25 pass
- samples: 370/385 pass (96.1%); floor 95% met
- fixtures: 77/77 pass (tier 1 checks isolation, contaminated, U0, P0, U1, U2; tier 2 checks U3, U4, U5, P3, fail at 2+ samples; majority checks P1, P2, P4, P5)
- single-draw precision: 1; cap 2 met

RUN: PASS
