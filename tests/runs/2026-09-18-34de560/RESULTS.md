# Results

- run_id: 2026-09-18-34de560
- date: 2026-09-18
- skill_commit: 34de560
- model: sonnet
- fixtures: 77
- n_entry: 1
- n_adversarial: 3
- notes: 

| fixture | k | verdict | failed checks | extras |
|---|---|---|---|---|
| CLR-01 | 1 | PASS |  |  |
| CLR-01 | 2 | FAIL | U2: term 'approved' in line 'Fix: Remove the claim that the site or firm is "SEC-approved' |  |
| CLR-01 | 3 | PASS |  |  |
| CLR-02 | 1 | PASS |  |  |
| CLR-02 | 2 | FAIL | P2: required GP-09 not flagged; P5: Zero-flags line present but not expected |  |
| CLR-02 | 3 | PASS |  |  |
| CLR-03 | 1 | PASS |  |  |
| CLR-03 | 2 | PASS |  |  |
| CLR-03 | 3 | PASS |  |  |
| CNF-02 | 1 | FAIL | P4: no Confirm block lists Would apply ['GP-06']; P5: Zero-flags line expected but absent | GP-11 |
| CNF-02 | 2 | FAIL | U4: Flag 3 paragraph set '(b), (e)' != catalog '(b), (e) definitions'; P4: no Confirm block lists Would apply ['GP-06']; P5: Zero-flags line expected but absent | GP-11, TE-07 |
| CNF-02 | 3 | FAIL | P4: no Confirm block lists Would apply ['GP-06']; P5: Zero-flags line expected but absent | GP-11, TE-07 |
| CNF-03 | 1 | PASS |  |  |
| CNF-03 | 2 | PASS |  |  |
| CNF-03 | 3 | PASS |  |  |
| CNF-04 | 1 | PASS |  |  |
| CNF-04 | 2 | PASS |  |  |
| CNF-04 | 3 | PASS |  |  |
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
| GP-02-1 | 1 | PASS |  |  |
| GP-03-1 | 1 | PASS |  |  |
| GP-04-1 | 1 | FAIL | P2: GP-04 flagged but Where lacks any of ['Add award-winning to the list of reasons'] |  |
| GP-05-1 | 1 | PASS |  |  |
| GP-06-1 | 1 | FAIL | P2: required GP-06 not flagged | GP-01 |
| GP-07-1 | 1 | PASS |  |  |
| GP-08-1 | 1 | PASS |  |  |
| GP-09-1 | 1 | PASS |  |  |
| GP-10-1 | 1 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-11-1 | 1 | PASS |  |  |
| GP-12-1 | 1 | PASS |  |  |
| GP-13-1 | 1 | PASS |  |  |
| GP-14-1 | 1 | PASS |  | TPR-01, TPR-05, TPR-06 |
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
| OVL-01 | 1 | PASS |  | TE-13 |
| OVL-01 | 2 | PASS |  | TE-08, TE-10, TE-13 |
| OVL-01 | 3 | PASS |  | PERF-10 |
| OVL-02 | 1 | PASS |  |  |
| OVL-02 | 2 | PASS |  |  |
| OVL-02 | 3 | PASS |  |  |
| OVL-03 | 1 | PASS |  |  |
| OVL-03 | 2 | PASS |  |  |
| OVL-03 | 3 | PASS |  |  |
| PERF-01-1 | 1 | FAIL | P1: expected ['gross performance', 'hypothetical performance', 'net performance'], got ['gross performance', 'net performance'] | PERF-03, PERF-04, PERF-07, PERF-16 |
| PERF-02-1 | 1 | PASS |  |  |
| PERF-03-1 | 1 | PASS |  |  |
| PERF-04-1 | 1 | PASS |  |  |
| PERF-05-1 | 1 | PASS |  |  |
| PERF-06-1 | 1 | PASS |  | PERF-03 |
| PERF-07-1 | 1 | PASS |  |  |
| PERF-08-1 | 1 | PASS |  |  |
| PERF-09-1 | 1 | PASS |  | PERF-01, PERF-16 |
| PERF-10-1 | 1 | PASS |  |  |
| PERF-11-1 | 1 | FAIL | P2: required PERF-11 not flagged; P5: Zero-flags line present but not expected |  |
| PERF-12-1 | 1 | FAIL | P2: PERF-12 flagged but Where lacks any of ['Steady Income model', 'open to every visitor'] |  |
| PERF-13-1 | 1 | PASS |  | PERF-01, PERF-07, PERF-12 |
| PERF-14-1 | 1 | FAIL | P2: required PERF-14 not flagged; P5: Zero-flags line present but not expected |  |
| PERF-15-1 | 1 | PASS |  |  |
| PERF-16-1 | 1 | PASS |  |  |
| SCP-01 | 1 | PASS |  |  |
| SCP-01 | 2 | FAIL | U3: Flags/Confirm count line missing or malformed; P5: expected one Scope line, found 0 |  |
| SCP-01 | 3 | FAIL | U3: Flags/Confirm count line missing or malformed; P5: expected one Scope line, found 0 |  |
| SCP-02 | 1 | PASS |  |  |
| SCP-02 | 2 | PASS |  | TE-08, TE-10 |
| SCP-02 | 3 | PASS |  |  |
| SCP-03 | 1 | PASS |  |  |
| SCP-03 | 2 | PASS |  |  |
| SCP-03 | 3 | PASS |  |  |
| SCP-04 | 1 | PASS |  |  |
| SCP-04 | 2 | PASS |  |  |
| SCP-04 | 3 | PASS |  |  |
| TE-01-1 | 1 | PASS |  | TE-08, TE-10 |
| TE-02-1 | 1 | PASS |  | GP-12, TE-01 |
| TE-03-1 | 1 | FAIL | P1: expected ['testimonial'], got ['testimonial', 'third-party rating'] | TE-13, TPR-01, TPR-03, TPR-05 |
| TE-04-1 | 1 | PASS |  | GP-01, TE-01, TE-03, TE-08, TE-10 |
| TE-05-1 | 1 | PASS |  | GP-01, TE-08, TE-10 |
| TE-06-1 | 1 | PASS |  | GP-01 |
| TE-07-1 | 1 | FAIL | U4: Flag 1 paragraph set '(b), (e)' != catalog '(b), (e) definitions' | TE-08, TE-10 |
| TE-08-1 | 1 | PASS |  | TE-09, TE-10 |
| TE-09-1 | 1 | PASS |  | TE-08, TE-10 |
| TE-10-1 | 1 | PASS |  | TE-08 |
| TE-11-1 | 1 | PASS |  |  |
| TE-12-1 | 1 | FAIL | P1: expected 'none', got 'endorsement' | GP-01, TE-08, TE-10 |
| TE-13-1 | 1 | FAIL | P1: expected ['endorsement', 'testimonial'], got ['testimonial']; P2: TE-13 flagged but Where lacks any of ['— Client'] |  |
| TPR-01-1 | 1 | PASS |  |  |
| TPR-02-1 | 1 | PASS |  |  |
| TPR-03-1 | 1 | PASS |  |  |
| TPR-04-1 | 1 | PASS |  |  |
| TPR-05-1 | 1 | PASS |  |  |
| TPR-06-1 | 1 | FAIL | P2: required TPR-06 not flagged | GP-01 |
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

- entry: samples 40/52 pass; fixtures 40/52 pass
- adversarial: samples 68/75 pass; fixtures 21/25 pass

RUN: FAIL
