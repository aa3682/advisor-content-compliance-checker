# Results

- run_id: 2026-10-04-3048b45
- date: 2026-10-04
- skill_commit: 3048b45
- model: claude-sonnet-5
- fixtures: 77
- n_entry: 5
- n_adversarial: 5
- notes: run 12 per run-12. The account weekly usage limit was hit at TE-10-1.1 (2026-10-04T10:39:05Z): 180 samples (TE-10-1.1 through VRQ-03.5) got only a usage-limit reply with no model_reported, launcher exited at 205/385. After a test call outside the run confirmed the limit had cleared, resumed 2026-10-04 under usage-limit-resume with --skip-done, the 205 done samples standing and the 180 samples relaunched fresh, their evidence kept as .attempt0. A container restart (launcher dead after CLR-03.2, ~13:31Z; container back 14:58:55Z) killed the resume at 272/385; resumed again under infra-kill-resume with --skip-done, the 272 done samples standing and the 4 killed samples (CLR-03.3, CLR-03.4, CLR-03.5, CNF-02.1) relaunched fresh, their evidence kept as .attempt0b. No fixes of any kind were made.

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
| GP-11-1 | 4 | PASS |  | GP-06 |
| GP-11-1 | 5 | PASS |  | GP-06 |
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
| GP-14-1 | 2 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-14-1 | 3 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-14-1 | 4 | FAIL | P2: required GP-14 not flagged | TPR-01, TPR-05, TPR-06 |
| GP-14-1 | 5 | FAIL | P2: required GP-14 not flagged | TPR-01, TPR-05, TPR-06 |
| GP-15-1 | 1 | PASS |  |  |
| GP-15-1 | 2 | FAIL | U4: Flag 1 paragraph set '(a)(1), (a)(2)' != catalog '(a)(1)' |  |
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
| OVL-01 | 1 | PASS |  |  |
| OVL-01 | 2 | PASS |  | PERF-10, TE-08, TE-10 |
| OVL-01 | 3 | PASS |  | TE-08, TE-10 |
| OVL-01 | 4 | PASS |  | TE-08, TE-09, TE-10 |
| OVL-01 | 5 | PASS |  | TE-06, TE-08, TE-10 |
| OVL-02 | 1 | PASS |  |  |
| OVL-02 | 2 | PASS |  |  |
| OVL-02 | 3 | PASS |  |  |
| OVL-02 | 4 | PASS |  |  |
| OVL-02 | 5 | PASS |  |  |
| OVL-03 | 1 | PASS |  |  |
| OVL-03 | 2 | PASS |  |  |
| OVL-03 | 3 | PASS |  |  |
| OVL-03 | 4 | PASS |  |  |
| OVL-03 | 5 | PASS |  |  |
| PERF-01-1 | 1 | PASS |  | PERF-07, PERF-12 |
| PERF-01-1 | 2 | PASS |  | PERF-07, PERF-10, PERF-12 |
| PERF-01-1 | 3 | PASS |  | PERF-12 |
| PERF-01-1 | 4 | PASS |  | PERF-03, PERF-07, PERF-12, PERF-16 |
| PERF-01-1 | 5 | FAIL | P1: expected ['gross performance', 'hypothetical performance', 'net performance'], got ['gross performance', 'net performance'] | PERF-03, PERF-04, PERF-07, PERF-16 |
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
| PERF-04-1 | 2 | PASS |  |  |
| PERF-04-1 | 3 | PASS |  |  |
| PERF-04-1 | 4 | PASS |  |  |
| PERF-04-1 | 5 | PASS |  |  |
| PERF-05-1 | 1 | PASS |  |  |
| PERF-05-1 | 2 | PASS |  | PERF-13 |
| PERF-05-1 | 3 | PASS |  |  |
| PERF-05-1 | 4 | PASS |  |  |
| PERF-05-1 | 5 | PASS |  |  |
| PERF-06-1 | 1 | PASS |  | PERF-03 |
| PERF-06-1 | 2 | PASS |  | PERF-03 |
| PERF-06-1 | 3 | PASS |  | PERF-03 |
| PERF-06-1 | 4 | PASS |  | PERF-03 |
| PERF-06-1 | 5 | PASS |  | PERF-03 |
| PERF-07-1 | 1 | FAIL | P2: required PERF-07 not flagged; P5: Zero-flags line present but not expected |  |
| PERF-07-1 | 2 | PASS |  |  |
| PERF-07-1 | 3 | PASS |  |  |
| PERF-07-1 | 4 | PASS |  |  |
| PERF-07-1 | 5 | PASS |  |  |
| PERF-08-1 | 1 | PASS |  |  |
| PERF-08-1 | 2 | PASS |  |  |
| PERF-08-1 | 3 | PASS |  |  |
| PERF-08-1 | 4 | PASS |  |  |
| PERF-08-1 | 5 | PASS |  |  |
| PERF-09-1 | 1 | PASS |  | PERF-16 |
| PERF-09-1 | 2 | PASS |  | PERF-16 |
| PERF-09-1 | 3 | PASS |  | PERF-01, PERF-16 |
| PERF-09-1 | 4 | PASS |  | PERF-01, PERF-16 |
| PERF-09-1 | 5 | PASS |  | PERF-01, PERF-16 |
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
| PERF-13-1 | 1 | PASS |  | PERF-01, PERF-07, PERF-12 |
| PERF-13-1 | 2 | PASS |  |  |
| PERF-13-1 | 3 | PASS |  | PERF-01, PERF-07 |
| PERF-13-1 | 4 | PASS |  | PERF-01, PERF-07, PERF-12 |
| PERF-13-1 | 5 | PASS |  | PERF-07 |
| PERF-14-1 | 1 | PASS |  | PERF-08, PERF-12 |
| PERF-14-1 | 2 | PASS |  |  |
| PERF-14-1 | 3 | PASS |  | PERF-01, PERF-08 |
| PERF-14-1 | 4 | PASS |  | PERF-08, PERF-12 |
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
| SCP-04 | 3 | PASS |  |  |
| SCP-04 | 4 | PASS |  |  |
| SCP-04 | 5 | PASS |  |  |
| TE-01-1 | 1 | PASS |  |  |
| TE-01-1 | 2 | PASS |  |  |
| TE-01-1 | 3 | PASS |  |  |
| TE-01-1 | 4 | PASS |  | TE-08, TE-10 |
| TE-01-1 | 5 | PASS |  | TE-08, TE-10 |
| TE-02-1 | 1 | PASS |  | GP-12, TE-01, TE-06, TE-08, TE-10 |
| TE-02-1 | 2 | PASS |  | GP-12, TE-08, TE-10 |
| TE-02-1 | 3 | PASS |  | GP-12 |
| TE-02-1 | 4 | PASS |  | GP-12, TE-01, TE-05, TE-06, TE-08, TE-10 |
| TE-02-1 | 5 | PASS |  | GP-12 |
| TE-03-1 | 1 | PASS |  | TE-13, TPR-03 |
| TE-03-1 | 2 | PASS |  | TE-13, TPR-03 |
| TE-03-1 | 3 | PASS |  | TE-13, TPR-03 |
| TE-03-1 | 4 | PASS |  | TE-13, TPR-03 |
| TE-03-1 | 5 | PASS |  | TE-13, TPR-03 |
| TE-04-1 | 1 | PASS |  | TE-01 |
| TE-04-1 | 2 | PASS |  | GP-01, TE-03 |
| TE-04-1 | 3 | PASS |  | TE-01, TE-08, TE-10 |
| TE-04-1 | 4 | PASS |  | GP-01, TE-01, TE-03, TE-08, TE-10 |
| TE-04-1 | 5 | PASS |  | GP-01, TE-01, TE-03, TE-08, TE-10 |
| TE-05-1 | 1 | PASS |  | GP-01, TE-08, TE-09, TE-10 |
| TE-05-1 | 2 | PASS |  | GP-01, TE-08, TE-09, TE-10 |
| TE-05-1 | 3 | PASS |  | TE-08, TE-10 |
| TE-05-1 | 4 | PASS |  | GP-01, TE-08, TE-09, TE-10 |
| TE-05-1 | 5 | PASS |  | TE-08, TE-09, TE-10 |
| TE-06-1 | 1 | PASS |  |  |
| TE-06-1 | 2 | PASS |  |  |
| TE-06-1 | 3 | PASS |  |  |
| TE-06-1 | 4 | PASS |  |  |
| TE-06-1 | 5 | PASS |  |  |
| TE-07-1 | 1 | PASS |  | TE-06, TE-08, TE-09, TE-10 |
| TE-07-1 | 2 | PASS |  | TE-06, TE-08, TE-10 |
| TE-07-1 | 3 | PASS |  | TE-08, TE-09, TE-10 |
| TE-07-1 | 4 | PASS |  | TE-06, TE-08, TE-10 |
| TE-07-1 | 5 | FAIL | U2: term 'passing' in line 'Depends on: Does the referring client disclose any material ' | TE-06, TE-08, TE-09, TE-10 |
| TE-08-1 | 1 | PASS |  | TE-09, TE-10 |
| TE-08-1 | 2 | PASS |  | TE-10 |
| TE-08-1 | 3 | PASS |  | TE-09, TE-10 |
| TE-08-1 | 4 | PASS |  | TE-09, TE-10 |
| TE-08-1 | 5 | PASS |  | TE-10 |
| TE-09-1 | 1 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 2 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 3 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 4 | PASS |  | GP-01, TE-08, TE-10 |
| TE-09-1 | 5 | PASS |  | TE-08, TE-10 |
| TE-10-1 | 1 | PASS |  | TE-08 |
| TE-10-1 | 2 | PASS |  | TE-08 |
| TE-10-1 | 3 | PASS |  | TE-08 |
| TE-10-1 | 4 | PASS |  | TE-08 |
| TE-10-1 | 5 | PASS |  | TE-08, TE-09 |
| TE-11-1 | 1 | FAIL | P2: required TE-11 not flagged; P5: Zero-flags line present but not expected |  |
| TE-11-1 | 2 | PASS |  |  |
| TE-11-1 | 3 | FAIL | P2: required TE-11 not flagged; P5: Zero-flags line present but not expected |  |
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
| TPR-02-1 | 4 | FAIL | P2: required TPR-02 not flagged; P4: no Confirm block lists Would apply ['TPR-02'] | TPR-03 |
| TPR-02-1 | 5 | PASS |  |  |
| TPR-03-1 | 1 | PASS |  |  |
| TPR-03-1 | 2 | PASS |  |  |
| TPR-03-1 | 3 | PASS |  |  |
| TPR-03-1 | 4 | PASS |  |  |
| TPR-03-1 | 5 | PASS |  |  |
| TPR-04-1 | 1 | PASS |  | TPR-03 |
| TPR-04-1 | 2 | PASS |  |  |
| TPR-04-1 | 3 | PASS |  |  |
| TPR-04-1 | 4 | PASS |  |  |
| TPR-04-1 | 5 | PASS |  | TPR-07 |
| TPR-05-1 | 1 | FAIL | P2: required TPR-05 not flagged | GP-01 |
| TPR-05-1 | 2 | FAIL | P2: TPR-05 flagged but Where lacks any of ['no compensation of any kind has been paid', 'annual badge-licensing fee'] |  |
| TPR-05-1 | 3 | PASS |  |  |
| TPR-05-1 | 4 | FAIL | P2: required TPR-05 not flagged | GP-01 |
| TPR-05-1 | 5 | PASS |  |  |
| TPR-06-1 | 1 | PASS |  | TPR-05 |
| TPR-06-1 | 2 | PASS |  | TPR-05 |
| TPR-06-1 | 3 | PASS |  | TPR-05 |
| TPR-06-1 | 4 | PASS |  | TPR-05 |
| TPR-06-1 | 5 | PASS |  | TPR-05 |
| TPR-07-1 | 1 | FAIL | P2: TPR-07 flagged but Where lacks any of ["that's the badge at the top of every page on our site", 'sit in the footer at the bottom of the page, in smaller type'] |  |
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
| VRQ-03 | 1 | PASS |  | TE-08, TE-10 |
| VRQ-03 | 2 | PASS |  | GP-01, TE-08, TE-10 |
| VRQ-03 | 3 | PASS |  | TE-08, TE-09, TE-10 |
| VRQ-03 | 4 | PASS |  | GP-01, TE-08, TE-09, TE-10 |
| VRQ-03 | 5 | PASS |  | GP-01, TE-08, TE-10 |

## Per fixture

| fixture | class | n | hard failures | P-assertions clean | needs | verdict |
|---|---|---|---|---|---|---|
| CLR-01 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| CLR-02 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| CLR-03 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| CNF-02 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| CNF-03 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| CNF-04 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| CUR-01 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| CUR-02 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| CUR-03 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| NOM-01 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| NOM-02 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| NOM-03 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| OVL-01 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| OVL-02 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| OVL-03 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| SCP-01 | adversarial | 5 | 0 | 4/5 | 3/5 | PASS |
| SCP-02 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| SCP-03 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| SCP-04 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| UNR-01 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| UNR-02 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| UNR-03 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| VRQ-01 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| VRQ-02 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| VRQ-03 | adversarial | 5 | 0 | 5/5 | 3/5 | PASS |
| GP-01-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| GP-02-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| GP-03-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| GP-04-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| GP-05-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| GP-06-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| GP-07-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| GP-08-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| GP-09-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| GP-10-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| GP-11-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| GP-12-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| GP-13-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| GP-14-1 | entry | 5 | 0 | 3/5 | 3/5 | PASS |
| GP-15-1 | entry | 5 | 1 | 5/5 | 3/5 | FAIL |
| GP-16-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| PERF-01-1 | entry | 5 | 0 | 4/5 | 3/5 | PASS |
| PERF-02-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| PERF-03-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| PERF-04-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| PERF-05-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| PERF-06-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| PERF-07-1 | entry | 5 | 0 | 4/5 | 3/5 | PASS |
| PERF-08-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| PERF-09-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| PERF-10-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| PERF-11-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| PERF-12-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| PERF-13-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| PERF-14-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| PERF-15-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| PERF-16-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| TE-01-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| TE-02-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| TE-03-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| TE-04-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| TE-05-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| TE-06-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| TE-07-1 | entry | 5 | 1 | 5/5 | 3/5 | FAIL |
| TE-08-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| TE-09-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| TE-10-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| TE-11-1 | entry | 5 | 0 | 3/5 | 3/5 | PASS |
| TE-12-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| TE-13-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| TPR-01-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| TPR-02-1 | entry | 5 | 0 | 4/5 | 3/5 | PASS |
| TPR-03-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| TPR-04-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| TPR-05-1 | entry | 5 | 0 | 2/5 | 3/5 | FAIL |
| TPR-06-1 | entry | 5 | 0 | 5/5 | 3/5 | PASS |
| TPR-07-1 | entry | 5 | 0 | 4/5 | 3/5 | PASS |

## Notes

none

## Totals

- entry: samples 247/260 pass; fixtures 49/52 pass
- adversarial: samples 124/125 pass; fixtures 25/25 pass
- samples: 371/385 pass (96.4%); floor 95% met
- fixtures: 74/77 pass (hard checks isolation, contaminated, U0, U1, U2, U3, U4, U5, P0, P3; majority checks P1, P2, P4, P5)

RUN: FAIL
