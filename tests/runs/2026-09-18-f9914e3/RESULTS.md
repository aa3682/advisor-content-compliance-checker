# Results

- run_id: 2026-09-18-f9914e3
- date: 2026-09-18
- skill_commit: f9914e3
- model: sonnet
- fixtures: 77
- n_entry: 1
- n_adversarial: 3
- notes: batch size 8 (16 batches, last of 9); wall time 13:41Z to 14:21Z, about 40 minutes; subagent tokens about 11 million in total, estimated from the per-agent usage the harness reported (65k to 111k each, median about 87k), not summed exactly; no missing output.md, no tool errors; anomalies listed below.

| fixture | k | verdict | failed checks | extras |
|---|---|---|---|---|
| CLR-01 | 1 | PASS |  |  |
| CLR-01 | 2 | FAIL | P2: required GP-09 not flagged; P5: Zero-flags line present but not expected |  |
| CLR-01 | 3 | PASS |  |  |
| CLR-02 | 1 | PASS |  |  |
| CLR-02 | 2 | PASS |  |  |
| CLR-02 | 3 | FAIL | P3: forbidden GP-09 flagged; P5: Zero-flags line expected but absent |  |
| CLR-03 | 1 | FAIL | P1: expected ['testimonial'], got ['testimonial (e)(17)'] |  |
| CLR-03 | 2 | PASS |  |  |
| CLR-03 | 3 | PASS |  |  |
| CNF-01 | 1 | FAIL | P4: no Confirm block with Would apply ['GP-08']; P5: Zero-flags line expected but absent |  |
| CNF-01 | 2 | FAIL | P4: no Confirm block with Would apply ['GP-08']; P5: Zero-flags line expected but absent |  |
| CNF-01 | 3 | FAIL | P4: no Confirm block with Would apply ['GP-08']; P5: Zero-flags line expected but absent |  |
| CNF-02 | 1 | PASS |  |  |
| CNF-02 | 2 | FAIL | P4: no Confirm block with Would apply ['GP-06']; P5: Zero-flags line expected but absent | GP-11 |
| CNF-02 | 3 | FAIL | P4: no Confirm block with Would apply ['GP-06']; P5: Zero-flags line expected but absent | GP-11, PERF-09 |
| CNF-03 | 1 | FAIL | P1: expected 'none', got 'gross performance'; P4: no Confirm block with Would apply ['PERF-03'] |  |
| CNF-03 | 2 | FAIL | P1: expected 'none', got 'gross performance'; P4: no Confirm block with Would apply ['PERF-03'] |  |
| CNF-03 | 3 | FAIL | P1: expected 'none', got 'gross performance'; P4: no Confirm block with Would apply ['PERF-03'] |  |
| CNF-04 | 1 | FAIL | P1: expected ['gross performance', 'net performance'], got ['gross performance (e)(7)', 'net performance (e)(10)'] |  |
| CNF-04 | 2 | FAIL | P1: expected ['gross performance', 'net performance'], got ['gross performance', 'hypothetical performance', 'net performance']; P4: no Confirm block with Would apply ['PERF-12']; P5: Zero-flags line expected but absent | PERF-03 |
| CNF-04 | 3 | FAIL | P1: expected ['gross performance', 'net performance'], got ['gross performance', 'hypothetical performance', 'net performance']; P4: no Confirm block with Would apply ['PERF-12']; P5: Zero-flags line expected but absent | PERF-03 |
| CUR-01 | 1 | PASS |  |  |
| CUR-01 | 2 | PASS |  |  |
| CUR-01 | 3 | PASS |  |  |
| CUR-02 | 1 | PASS |  |  |
| CUR-02 | 2 | FAIL | U3: unexpected line: '[Zero flags is not a clearance — the catalog covers document' / Zero-flags line absent with Flags: 0; P5: Zero-flags line expected but absent |  |
| CUR-02 | 3 | PASS |  |  |
| CUR-03 | 1 | FAIL | P1: expected ['third-party rating'], got ['third-party rating (e)(18)'] |  |
| CUR-03 | 2 | PASS |  |  |
| CUR-03 | 3 | PASS |  |  |
| GP-01-1 | 1 | PASS |  |  |
| GP-02-1 | 1 | PASS |  |  |
| GP-03-1 | 1 | PASS |  |  |
| GP-04-1 | 1 | PASS |  |  |
| GP-05-1 | 1 | PASS |  |  |
| GP-06-1 | 1 | PASS |  |  |
| GP-07-1 | 1 | PASS |  |  |
| GP-08-1 | 1 | PASS |  |  |
| GP-09-1 | 1 | PASS |  |  |
| GP-10-1 | 1 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-11-1 | 1 | PASS |  |  |
| GP-12-1 | 1 | PASS |  |  |
| GP-13-1 | 1 | PASS |  |  |
| GP-14-1 | 1 | FAIL | P1: expected ['third-party rating'], got ['third-party rating (e)(18)'] | TPR-01, TPR-05, TPR-06 |
| GP-15-1 | 1 | PASS |  |  |
| GP-16-1 | 1 | FAIL | P1: expected ['third-party rating'], got ['none'] |  |
| NOM-01 | 1 | PASS |  |  |
| NOM-01 | 2 | PASS |  |  |
| NOM-01 | 3 | PASS |  |  |
| NOM-02 | 1 | PASS |  |  |
| NOM-02 | 2 | PASS |  |  |
| NOM-02 | 3 | PASS |  |  |
| NOM-03 | 1 | PASS |  |  |
| NOM-03 | 2 | PASS |  |  |
| NOM-03 | 3 | PASS |  |  |
| OVL-01 | 1 | FAIL | P2: required PERF-04 not flagged |  |
| OVL-01 | 2 | PASS |  | PERF-01, PERF-10, TE-08, TE-10 |
| OVL-01 | 3 | PASS |  | PERF-10, TE-08 |
| OVL-02 | 1 | PASS |  |  |
| OVL-02 | 2 | PASS |  |  |
| OVL-02 | 3 | PASS |  |  |
| OVL-03 | 1 | PASS |  |  |
| OVL-03 | 2 | PASS |  |  |
| OVL-03 | 3 | PASS |  |  |
| PERF-01-1 | 1 | PASS |  | PERF-07, PERF-12, PERF-15 |
| PERF-02-1 | 1 | FAIL | P2: required PERF-02 not flagged; P5: Zero-flags line present but not expected |  |
| PERF-03-1 | 1 | PASS |  |  |
| PERF-04-1 | 1 | FAIL | P1: expected ['gross performance', 'net performance'], got ['gross performance (e)(7)', 'net performance (e)(10)']; P2: PERF-03 flagged but Where lacks '10 years 8.4% gross, 7.3% net' |  |
| PERF-05-1 | 1 | PASS |  |  |
| PERF-06-1 | 1 | FAIL | P2: PERF-06 flagged but Where lacks 'for the periods ending December 31, 2018' | PERF-03 |
| PERF-07-1 | 1 | FAIL | P2: PERF-07 flagged but Where lacks 'My personal brokerage account, not any client account' |  |
| PERF-08-1 | 1 | PASS |  |  |
| PERF-09-1 | 1 | PASS |  |  |
| PERF-10-1 | 1 | PASS |  |  |
| PERF-11-1 | 1 | PASS |  |  |
| PERF-12-1 | 1 | FAIL | P2: PERF-12 flagged but Where lacks 'What the Steady Income model would have done' | PERF-03 |
| PERF-13-1 | 1 | FAIL | P1: expected ['hypothetical performance', 'net performance'], got ['hypothetical performance'] | PERF-07 |
| PERF-14-1 | 1 | FAIL | P1: expected ['hypothetical performance', 'net performance'], got ['hypothetical performance (e)(8)', 'net performance (e)(10)'] | PERF-03, PERF-08, PERF-12 |
| PERF-15-1 | 1 | PASS |  | PERF-03 |
| SCP-01 | 1 | PASS |  |  |
| SCP-01 | 2 | PASS |  | GP-03 |
| SCP-01 | 3 | PASS |  |  |
| SCP-02 | 1 | PASS |  | TE-13 |
| SCP-02 | 2 | PASS |  | TE-13 |
| SCP-02 | 3 | PASS |  |  |
| SCP-03 | 1 | PASS |  |  |
| SCP-03 | 2 | PASS |  |  |
| SCP-03 | 3 | PASS |  |  |
| SCP-04 | 1 | PASS |  |  |
| SCP-04 | 2 | PASS |  |  |
| SCP-04 | 3 | PASS |  |  |
| TE-01-1 | 1 | FAIL | P1: expected ['testimonial'], got ['testimonial (e)(17)'] |  |
| TE-02-1 | 1 | PASS |  | GP-12 |
| TE-03-1 | 1 | FAIL | P2: TE-03 flagged but Where lacks 'imported directly from Google as written' | TE-13 |
| TE-04-1 | 1 | PASS |  | GP-01, TE-03 |
| TE-05-1 | 1 | PASS |  |  |
| TE-06-1 | 1 | FAIL | P2: TE-06 flagged but Where lacks 'there are no conflicts of interest to report' | GP-01 |
| TE-07-1 | 1 | PASS |  | TE-08, TE-09, TE-10 |
| TE-08-1 | 1 | PASS |  |  |
| TE-09-1 | 1 | PASS |  | TE-08, TE-10 |
| TE-10-1 | 1 | PASS |  | TE-08, TE-09 |
| TE-11-1 | 1 | FAIL | P2: required TE-11 not flagged; P5: Zero-flags line present but not expected |  |
| TE-12-1 | 1 | PASS |  |  |
| TE-13-1 | 1 | FAIL | P1: expected ['endorsement', 'testimonial'], got ['testimonial'] |  |
| TPR-01-1 | 1 | PASS |  |  |
| TPR-02-1 | 1 | FAIL | P2: required TPR-03 not flagged |  |
| TPR-03-1 | 1 | PASS |  |  |
| TPR-04-1 | 1 | PASS |  |  |
| TPR-05-1 | 1 | PASS |  |  |
| TPR-06-1 | 1 | FAIL | P2: required TPR-06 not flagged; P5: Zero-flags line present but not expected |  |
| TPR-07-1 | 1 | PASS |  |  |
| UNR-01 | 1 | PASS |  |  |
| UNR-01 | 2 | PASS |  |  |
| UNR-01 | 3 | PASS |  |  |
| UNR-02 | 1 | PASS |  |  |
| UNR-02 | 2 | PASS |  |  |
| UNR-02 | 3 | FAIL | P5: Zero-flags line expected but absent | GP-03 |
| UNR-03 | 1 | PASS |  |  |
| UNR-03 | 2 | PASS |  |  |
| UNR-03 | 3 | PASS |  |  |
| VRQ-01 | 1 | PASS |  |  |
| VRQ-01 | 2 | PASS |  |  |
| VRQ-01 | 3 | PASS |  |  |
| VRQ-02 | 1 | PASS |  |  |
| VRQ-02 | 2 | PASS |  |  |
| VRQ-02 | 3 | FAIL | P1: expected ['gross performance', 'net performance'], got ['gross performance (e)(7)', 'net performance (e)(10)'] | PERF-03 |
| VRQ-03 | 1 | PASS |  | GP-01, TE-08, TE-10 |
| VRQ-03 | 2 | PASS |  | GP-01, TE-08, TE-10 |
| VRQ-03 | 3 | PASS |  | TE-08, TE-10 |

## Totals

- entry: samples 35/51 pass; fixtures 35/51 pass
- adversarial: samples 59/78 pass; fixtures 14/26 pass

RUN: FAIL
