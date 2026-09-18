# Results

- run_id: 2026-09-18-a3f26e8
- date: 2026-09-18
- skill_commit: a3f26e8
- model: sonnet
- fixtures: 77
- n_entry: 1
- n_adversarial: 3
- notes: batch size 8 (16 batches; the last has 7); 127 subagents pinned to sonnet, launched in RUNLIST order; wall time 2026-09-18T16:20:55Z to 2026-09-18T17:32:43Z (71 min 48 s), first launch to last collected output; subagent tokens summed from the 127 transcripts: input 3,628; output 97,516; cache creation 11,732,892; cache read 104,515,712; total 116,349,748; contaminated samples: 0 (no reply reported reading, listing, or opening anything outside its directory; CONTAMINATED.txt is empty); every output.md byte-copied by the harness, none transcribed; no retries; no missing output.md; no tool errors reported; reply anomalies: 1 reply was the single word DONE, 26 replies carried a summary without DONE, the rest DONE plus a summary; 2 replies echoed the output text in the reply (file copied, reply unused); 17 replies noted that catalog/failures.md, RULINGS.md, or tools/ were absent from the staging directory and proceeded on SKILL.md and the reference files; 3 replies referred to the repository or its catalog path as existing outside the directory while reporting no read, list, or open (CUR-01.2, NOM-02.1, UNR-03.2); see Anomalies below for the per-sample log.

| fixture | k | verdict | failed checks | extras |
|---|---|---|---|---|
| CLR-01 | 1 | PASS |  |  |
| CLR-01 | 2 | PASS |  |  |
| CLR-01 | 3 | PASS |  |  |
| CLR-02 | 1 | FAIL | P3: forbidden GP-09 flagged; P5: Zero-flags line expected but absent |  |
| CLR-02 | 2 | FAIL | P3: forbidden GP-09 flagged; P5: Zero-flags line expected but absent |  |
| CLR-02 | 3 | FAIL | P3: forbidden GP-09 flagged; P5: Zero-flags line expected but absent |  |
| CLR-03 | 1 | PASS |  |  |
| CLR-03 | 2 | FAIL | U3: unexpected line: '[Zero flags is not a clearance — the catalog covers document' / Zero-flags line absent with Flags: 0; P5: Zero-flags line expected but absent |  |
| CLR-03 | 3 | PASS |  |  |
| CNF-02 | 1 | FAIL | P4: no Confirm block lists Would apply ['GP-06'] |  |
| CNF-02 | 2 | FAIL | P4: no Confirm block lists Would apply ['GP-06'] |  |
| CNF-02 | 3 | FAIL | P4: no Confirm block lists Would apply ['GP-06'] |  |
| CNF-03 | 1 | PASS |  |  |
| CNF-03 | 2 | PASS |  |  |
| CNF-03 | 3 | PASS |  |  |
| CNF-04 | 1 | FAIL | P4: no Confirm block lists Would apply ['PERF-12'] | PERF-03 |
| CNF-04 | 2 | FAIL | P4: no Confirm block lists Would apply ['PERF-12'] | PERF-03 |
| CNF-04 | 3 | FAIL | P4: no Confirm block lists Would apply ['PERF-12'] | PERF-03 |
| CUR-01 | 1 | PASS |  |  |
| CUR-01 | 2 | PASS |  |  |
| CUR-01 | 3 | PASS |  |  |
| CUR-02 | 1 | PASS |  |  |
| CUR-02 | 2 | PASS |  |  |
| CUR-02 | 3 | PASS |  |  |
| CUR-03 | 1 | PASS |  |  |
| CUR-03 | 2 | PASS |  |  |
| CUR-03 | 3 | FAIL | P3: forbidden TPR-01 under Would apply |  |
| GP-01-1 | 1 | PASS |  |  |
| GP-02-1 | 1 | PASS |  |  |
| GP-03-1 | 1 | PASS |  |  |
| GP-04-1 | 1 | PASS |  |  |
| GP-05-1 | 1 | PASS |  |  |
| GP-06-1 | 1 | FAIL | U3: unexpected line: '[Zero flags is not a clearance — the catalog covers document' / Zero-flags line absent with Flags: 0; P2: required GP-06 not flagged |  |
| GP-07-1 | 1 | PASS |  |  |
| GP-08-1 | 1 | PASS |  |  |
| GP-09-1 | 1 | PASS |  |  |
| GP-10-1 | 1 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-11-1 | 1 | FAIL | P2: GP-11 flagged but Where lacks any of ['Those are app-store reviews of the software'] |  |
| GP-12-1 | 1 | PASS |  |  |
| GP-13-1 | 1 | PASS |  |  |
| GP-14-1 | 1 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-15-1 | 1 | PASS |  |  |
| GP-16-1 | 1 | PASS |  | TPR-01, TPR-06 |
| NOM-01 | 1 | PASS |  |  |
| NOM-01 | 2 | PASS |  |  |
| NOM-01 | 3 | PASS |  |  |
| NOM-02 | 1 | PASS |  |  |
| NOM-02 | 2 | PASS |  |  |
| NOM-02 | 3 | PASS |  |  |
| NOM-03 | 1 | PASS |  |  |
| NOM-03 | 2 | PASS |  |  |
| NOM-03 | 3 | PASS |  |  |
| OVL-01 | 1 | FAIL | P2: required PERF-04 not flagged | PERF-16 |
| OVL-01 | 2 | FAIL | P2: required PERF-04 not flagged | PERF-16, TE-05, TE-08, TE-10 |
| OVL-01 | 3 | FAIL | P2: required PERF-04 not flagged | PERF-10, PERF-16, TE-08, TE-10, TE-13 |
| OVL-02 | 1 | PASS |  |  |
| OVL-02 | 2 | PASS |  |  |
| OVL-02 | 3 | PASS |  |  |
| OVL-03 | 1 | PASS |  |  |
| OVL-03 | 2 | PASS |  |  |
| OVL-03 | 3 | PASS |  | TPR-01 |
| PERF-01-1 | 1 | PASS |  | PERF-12, PERF-13, PERF-14 |
| PERF-02-1 | 1 | PASS |  |  |
| PERF-03-1 | 1 | PASS |  |  |
| PERF-04-1 | 1 | PASS |  |  |
| PERF-05-1 | 1 | PASS |  |  |
| PERF-06-1 | 1 | PASS |  | PERF-03 |
| PERF-07-1 | 1 | PASS |  |  |
| PERF-08-1 | 1 | PASS |  |  |
| PERF-09-1 | 1 | PASS |  | PERF-01, PERF-16 |
| PERF-10-1 | 1 | FAIL | P2: required PERF-10 not flagged; P5: Zero-flags line present but not expected |  |
| PERF-11-1 | 1 | PASS |  |  |
| PERF-12-1 | 1 | PASS |  | PERF-03 |
| PERF-13-1 | 1 | FAIL | P2: PERF-13 flagged but Where lacks any of ['a 2,700% annualized return'] | PERF-01, PERF-03, PERF-07 |
| PERF-14-1 | 1 | PASS |  | PERF-03 |
| PERF-15-1 | 1 | PASS |  | PERF-03 |
| PERF-16-1 | 1 | PASS |  |  |
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
| SCP-04 | 2 | FAIL | U5: Flag 1 Where quote 'The badge at the top of our site reads Client Conf' is not in the fixture |  |
| SCP-04 | 3 | PASS |  | TPR-07 |
| TE-01-1 | 1 | PASS |  |  |
| TE-02-1 | 1 | PASS |  |  |
| TE-03-1 | 1 | PASS |  | TE-13 |
| TE-04-1 | 1 | PASS |  | GP-01, TE-03, TE-08, TE-10 |
| TE-05-1 | 1 | PASS |  | GP-01, TE-08, TE-10 |
| TE-06-1 | 1 | PASS |  | GP-01 |
| TE-07-1 | 1 | PASS |  | TE-08, TE-09, TE-10 |
| TE-08-1 | 1 | PASS |  |  |
| TE-09-1 | 1 | PASS |  |  |
| TE-10-1 | 1 | PASS |  | TE-08, TE-09 |
| TE-11-1 | 1 | PASS |  |  |
| TE-12-1 | 1 | FAIL | P1: expected ['endorsement'], got ['none'] | GP-01, TE-08, TE-10 |
| TE-13-1 | 1 | PASS |  |  |
| TPR-01-1 | 1 | PASS |  |  |
| TPR-02-1 | 1 | PASS |  |  |
| TPR-03-1 | 1 | FAIL | P2: TPR-03 flagged but Where lacks any of ['We did not receive the rating in 2021 or 2022'] |  |
| TPR-04-1 | 1 | PASS |  |  |
| TPR-05-1 | 1 | FAIL | P2: required TPR-05 not flagged; P5: Zero-flags line present but not expected |  |
| TPR-06-1 | 1 | PASS |  |  |
| TPR-07-1 | 1 | PASS |  |  |
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
| VRQ-03 | 2 | PASS |  | GP-01, TE-08, TE-10 |
| VRQ-03 | 3 | PASS |  | GP-01, TE-08, TE-10 |

## Totals

- entry: samples 45/52 pass; fixtures 45/52 pass
- adversarial: samples 60/75 pass; fixtures 18/25 pass

RUN: FAIL
