# Results

- run_id: 2026-09-19-e12ab12
- date: 2026-09-19
- skill_commit: e12ab12
- model: sonnet
- fixtures: 77
- n_entry: 3
- n_adversarial: 3
- notes: batch size up to 20 (harness cap CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS=20); contaminated samples: 4 (NOM-02.1, CUR-02.1, PERF-13-1.2, TE-12-1.2) — in each, the subagent issued a Glob call with no path, which resolved against the repository root rather than the staged scratch directory and listed tests/expected/*.yaml and catalog/failures.md; each subagent reported listing filenames only and not opening the files, and each is failed as contaminated under run-isolation regardless. Duplicate run: CUR-02.1 was dispatched twice (relaunched while its first agent was still in flight); the recorded output.md is whichever agent wrote last. Reply conformance: most subagents replied DONE plus an unrequested summary; several noted that catalog/failures.md and RULINGS.md are absent from staging, which is the staging rule working as intended.

| fixture | k | verdict | failed checks | extras |
|---|---|---|---|---|
| CLR-01 | 1 | PASS |  |  |
| CLR-01 | 2 | PASS |  |  |
| CLR-01 | 3 | PASS |  |  |
| CLR-02 | 1 | PASS |  |  |
| CLR-02 | 2 | FAIL | P2: required GP-09 not flagged; P5: Zero-flags line present but not expected |  |
| CLR-02 | 3 | PASS |  |  |
| CLR-03 | 1 | PASS |  |  |
| CLR-03 | 2 | PASS |  |  |
| CLR-03 | 3 | PASS |  |  |
| CNF-02 | 1 | FAIL | P4: no Confirm block lists Would apply ['GP-06'] |  |
| CNF-02 | 2 | FAIL | P4: no Confirm block lists Would apply ['GP-06']; P5: Zero-flags line expected but absent |  |
| CNF-02 | 3 | FAIL | P4: no Confirm block lists Would apply ['GP-06'] |  |
| CNF-03 | 1 | PASS |  | PERF-03 |
| CNF-03 | 2 | PASS |  |  |
| CNF-03 | 3 | PASS |  |  |
| CNF-04 | 1 | PASS |  | PERF-07 |
| CNF-04 | 2 | PASS |  | PERF-07 |
| CNF-04 | 3 | PASS |  | PERF-07 |
| CUR-01 | 1 | PASS |  |  |
| CUR-01 | 2 | PASS |  |  |
| CUR-01 | 3 | PASS |  |  |
| CUR-02 | 1 | FAIL | contaminated: unscoped Glob listed repo root incl. tests/expected/CUR-02.yaml |  |
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
| GP-09-1 | 3 | PASS |  |  |
| GP-10-1 | 1 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-10-1 | 2 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-10-1 | 3 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-11-1 | 1 | PASS |  |  |
| GP-11-1 | 2 | FAIL | P2: GP-11 flagged but Where lacks any of ['Those are app-store reviews of the software', 'what users say about PlanPath'] |  |
| GP-11-1 | 3 | PASS |  |  |
| GP-12-1 | 1 | PASS |  |  |
| GP-12-1 | 2 | PASS |  |  |
| GP-12-1 | 3 | PASS |  |  |
| GP-13-1 | 1 | FAIL | P2: GP-13 flagged but Where lacks any of ['My AI-powered rebalancing engine'] | GP-03 |
| GP-13-1 | 2 | PASS |  |  |
| GP-13-1 | 3 | PASS |  | GP-03 |
| GP-14-1 | 1 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-14-1 | 2 | FAIL | P2: required GP-14 not flagged | GP-03, TPR-01, TPR-05, TPR-06 |
| GP-14-1 | 3 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-15-1 | 1 | PASS |  |  |
| GP-15-1 | 2 | PASS |  |  |
| GP-15-1 | 3 | PASS |  |  |
| GP-16-1 | 1 | FAIL | P1: expected 'none', got 'third-party rating' | TPR-01, TPR-04, TPR-05, TPR-06 |
| GP-16-1 | 2 | FAIL | P1: expected 'none', got 'third-party rating' | TPR-01, TPR-04, TPR-05, TPR-06 |
| GP-16-1 | 3 | FAIL | P1: expected 'none', got 'third-party rating' | TPR-01, TPR-04, TPR-05, TPR-06 |
| NOM-01 | 1 | PASS |  |  |
| NOM-01 | 2 | PASS |  |  |
| NOM-01 | 3 | PASS |  |  |
| NOM-02 | 1 | FAIL | contaminated: unscoped Glob listed repo root incl. tests/expected/*.yaml |  |
| NOM-02 | 2 | PASS |  |  |
| NOM-02 | 3 | PASS |  |  |
| NOM-03 | 1 | PASS |  |  |
| NOM-03 | 2 | PASS |  |  |
| NOM-03 | 3 | PASS |  |  |
| OVL-01 | 1 | PASS |  | TE-08, TE-10 |
| OVL-01 | 2 | PASS |  | TE-08, TE-10 |
| OVL-01 | 3 | PASS |  | TE-08, TE-10, TE-13 |
| OVL-02 | 1 | PASS |  |  |
| OVL-02 | 2 | PASS |  |  |
| OVL-02 | 3 | PASS |  |  |
| OVL-03 | 1 | PASS |  |  |
| OVL-03 | 2 | PASS |  |  |
| OVL-03 | 3 | PASS |  |  |
| PERF-01-1 | 1 | PASS |  | PERF-07, PERF-12 |
| PERF-01-1 | 2 | PASS |  | PERF-03, PERF-04, PERF-07, PERF-12, PERF-15, PERF-16 |
| PERF-01-1 | 3 | PASS |  | PERF-07 |
| PERF-02-1 | 1 | FAIL | P1: expected ['gross performance', 'net performance'], got ['none'] |  |
| PERF-02-1 | 2 | PASS |  |  |
| PERF-02-1 | 3 | PASS |  |  |
| PERF-03-1 | 1 | PASS |  |  |
| PERF-03-1 | 2 | PASS |  |  |
| PERF-03-1 | 3 | PASS |  |  |
| PERF-04-1 | 1 | PASS |  |  |
| PERF-04-1 | 2 | PASS |  |  |
| PERF-04-1 | 3 | FAIL | P2: required PERF-04 not flagged |  |
| PERF-05-1 | 1 | PASS |  |  |
| PERF-05-1 | 2 | PASS |  |  |
| PERF-05-1 | 3 | PASS |  |  |
| PERF-06-1 | 1 | PASS |  | PERF-03 |
| PERF-06-1 | 2 | PASS |  | PERF-03 |
| PERF-06-1 | 3 | PASS |  | PERF-03 |
| PERF-07-1 | 1 | FAIL | P1: expected ['gross performance', 'net performance'], got ['gross performance', 'hypothetical performance', 'net performance'] |  |
| PERF-07-1 | 2 | FAIL | P1: expected ['gross performance', 'net performance'], got ['gross performance', 'hypothetical performance', 'net performance'] |  |
| PERF-07-1 | 3 | FAIL | P1: expected ['gross performance', 'net performance'], got ['gross performance', 'hypothetical performance', 'net performance'] |  |
| PERF-08-1 | 1 | PASS |  |  |
| PERF-08-1 | 2 | PASS |  |  |
| PERF-08-1 | 3 | PASS |  |  |
| PERF-09-1 | 1 | FAIL | P2: PERF-09 flagged but Where lacks any of ['Our five best-performing positions of 2025'] | PERF-01, PERF-16 |
| PERF-09-1 | 2 | FAIL | P2: PERF-09 flagged but Where lacks any of ['Our five best-performing positions of 2025'] | PERF-01, PERF-07, PERF-16 |
| PERF-09-1 | 3 | FAIL | P2: PERF-09 flagged but Where lacks any of ['Our five best-performing positions of 2025'] | PERF-16 |
| PERF-10-1 | 1 | PASS |  |  |
| PERF-10-1 | 2 | PASS |  |  |
| PERF-10-1 | 3 | PASS |  |  |
| PERF-11-1 | 1 | PASS |  |  |
| PERF-11-1 | 2 | PASS |  |  |
| PERF-11-1 | 3 | FAIL | P2: required PERF-11 not flagged; P5: Zero-flags line present but not expected |  |
| PERF-12-1 | 1 | PASS |  |  |
| PERF-12-1 | 2 | PASS |  |  |
| PERF-12-1 | 3 | PASS |  |  |
| PERF-13-1 | 1 | PASS |  | PERF-01, PERF-07 |
| PERF-13-1 | 2 | FAIL | contaminated: unscoped Glob listed repo root incl. tests/expected/PERF-13-1.yaml |  |
| PERF-13-1 | 3 | FAIL | P1: expected ['hypothetical performance', 'net performance'], got ['hypothetical performance'] | PERF-01, PERF-07, PERF-12 |
| PERF-14-1 | 1 | PASS |  |  |
| PERF-14-1 | 2 | PASS |  | PERF-08 |
| PERF-14-1 | 3 | FAIL | P2: PERF-14 flagged but Where lacks any of ['would grow to $1.3 million in ten years'] | PERF-01, PERF-08, PERF-12 |
| PERF-15-1 | 1 | PASS |  |  |
| PERF-15-1 | 2 | PASS |  |  |
| PERF-15-1 | 3 | FAIL | P1: expected ['gross performance', 'hypothetical performance', 'net performance'], got ['hypothetical performance'] | PERF-03 |
| PERF-16-1 | 1 | PASS |  |  |
| PERF-16-1 | 2 | PASS |  |  |
| PERF-16-1 | 3 | PASS |  |  |
| SCP-01 | 1 | PASS |  |  |
| SCP-01 | 2 | PASS |  |  |
| SCP-01 | 3 | PASS |  |  |
| SCP-02 | 1 | PASS |  |  |
| SCP-02 | 2 | PASS |  | TE-08, TE-10 |
| SCP-02 | 3 | PASS |  | TE-08, TE-10 |
| SCP-03 | 1 | PASS |  |  |
| SCP-03 | 2 | PASS |  |  |
| SCP-03 | 3 | PASS |  |  |
| SCP-04 | 1 | PASS |  |  |
| SCP-04 | 2 | PASS |  |  |
| SCP-04 | 3 | PASS |  |  |
| TE-01-1 | 1 | PASS |  |  |
| TE-01-1 | 2 | PASS |  | TE-08, TE-10 |
| TE-01-1 | 3 | PASS |  |  |
| TE-02-1 | 1 | PASS |  | GP-12 |
| TE-02-1 | 2 | PASS |  | GP-12 |
| TE-02-1 | 3 | PASS |  | GP-12, TE-01 |
| TE-03-1 | 1 | FAIL | P1: expected ['testimonial', 'third-party rating'], got ['testimonial']; P2: required TE-03 not flagged | TE-13 |
| TE-03-1 | 2 | FAIL | P1: expected ['testimonial', 'third-party rating'], got ['testimonial']; P2: TE-03 flagged but Where lacks any of ['Google', 'imported directly'] |  |
| TE-03-1 | 3 | FAIL | P2: TE-03 flagged but Where lacks any of ['Google', 'imported directly'] | TPR-01 |
| TE-04-1 | 1 | PASS |  | GP-01, TE-03, TE-08, TE-10 |
| TE-04-1 | 2 | PASS |  | GP-01, TE-01 |
| TE-04-1 | 3 | PASS |  | GP-01, TE-01, TE-03, TE-08, TE-10 |
| TE-05-1 | 1 | PASS |  | GP-01, TE-08, TE-09, TE-10 |
| TE-05-1 | 2 | PASS |  | GP-01, TE-08, TE-10 |
| TE-05-1 | 3 | PASS |  | GP-01, TE-08, TE-10 |
| TE-06-1 | 1 | FAIL | P2: required TE-06 not flagged | GP-01 |
| TE-06-1 | 2 | PASS |  |  |
| TE-06-1 | 3 | FAIL | P2: required TE-06 not flagged | GP-01 |
| TE-07-1 | 1 | PASS |  | TE-08, TE-09, TE-10 |
| TE-07-1 | 2 | PASS |  | TE-08, TE-09, TE-10 |
| TE-07-1 | 3 | PASS |  | TE-08, TE-09, TE-10 |
| TE-08-1 | 1 | PASS |  | TE-09, TE-10 |
| TE-08-1 | 2 | PASS |  | TE-10 |
| TE-08-1 | 3 | PASS |  | TE-10 |
| TE-09-1 | 1 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 2 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 3 | PASS |  | TE-08, TE-10 |
| TE-10-1 | 1 | PASS |  | TE-08, TE-09 |
| TE-10-1 | 2 | PASS |  | TE-08, TE-09 |
| TE-10-1 | 3 | PASS |  | GP-01, TE-08, TE-09 |
| TE-11-1 | 1 | FAIL | P2: TE-11 flagged but Where lacks any of ['has no affiliation with the firm', 'answers the phone when you call our office'] | GP-01 |
| TE-11-1 | 2 | FAIL | P2: TE-11 flagged but Where lacks any of ['has no affiliation with the firm', 'answers the phone when you call our office'] |  |
| TE-11-1 | 3 | FAIL | P2: TE-11 flagged but Where lacks any of ['has no affiliation with the firm', 'answers the phone when you call our office'] |  |
| TE-12-1 | 1 | FAIL | P2: required TE-12 not flagged; P5: Zero-flags line present but not expected | TE-08, TE-10 |
| TE-12-1 | 2 | FAIL | contaminated: unscoped Glob listed repo root incl. catalog/failures.md, RULINGS.md, tests/expected/*.yaml |  |
| TE-12-1 | 3 | FAIL | P1: expected ['endorsement'], got ['none'] | GP-01, TE-08, TE-10 |
| TE-13-1 | 1 | FAIL | P1: expected ['testimonial'], got ['endorsement', 'testimonial'] |  |
| TE-13-1 | 2 | FAIL | P1: expected ['testimonial'], got ['endorsement', 'testimonial'] |  |
| TE-13-1 | 3 | FAIL | P1: expected ['testimonial'], got ['endorsement', 'testimonial'] |  |
| TPR-01-1 | 1 | PASS |  |  |
| TPR-01-1 | 2 | PASS |  |  |
| TPR-01-1 | 3 | PASS |  |  |
| TPR-02-1 | 1 | FAIL | P2: required TPR-02 not flagged; P5: Zero-flags line present but not expected |  |
| TPR-02-1 | 2 | PASS |  |  |
| TPR-02-1 | 3 | FAIL | P2: required TPR-02 not flagged; P5: Zero-flags line present but not expected |  |
| TPR-03-1 | 1 | PASS |  |  |
| TPR-03-1 | 2 | PASS |  |  |
| TPR-03-1 | 3 | PASS |  |  |
| TPR-04-1 | 1 | PASS |  |  |
| TPR-04-1 | 2 | PASS |  |  |
| TPR-04-1 | 3 | PASS |  |  |
| TPR-05-1 | 1 | PASS |  |  |
| TPR-05-1 | 2 | PASS |  |  |
| TPR-05-1 | 3 | PASS |  |  |
| TPR-06-1 | 1 | FAIL | P5: Zero-flags line present but not expected | TPR-05 |
| TPR-06-1 | 2 | FAIL | P5: Zero-flags line present but not expected | TPR-05 |
| TPR-06-1 | 3 | FAIL | P5: Zero-flags line present but not expected | TPR-05 |
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
| UNR-03 | 3 | PASS |  | GP-03 |
| VRQ-01 | 1 | PASS |  |  |
| VRQ-01 | 2 | PASS |  |  |
| VRQ-01 | 3 | PASS |  |  |
| VRQ-02 | 1 | PASS |  |  |
| VRQ-02 | 2 | PASS |  |  |
| VRQ-02 | 3 | PASS |  |  |
| VRQ-03 | 1 | PASS |  | GP-01, TE-08, TE-09, TE-10 |
| VRQ-03 | 2 | PASS |  | GP-01, TE-08, TE-09, TE-10 |
| VRQ-03 | 3 | PASS |  | GP-01, TE-08, TE-09, TE-10 |

## Per fixture

| fixture | class | n | hard failures | P-assertions clean | needs | verdict |
|---|---|---|---|---|---|---|
| CLR-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CLR-02 | adversarial | 3 | 0 | 2/3 | 2/3 | PASS |
| CLR-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CNF-02 | adversarial | 3 | 0 | 0/3 | 2/3 | FAIL |
| CNF-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CNF-04 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CUR-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CUR-02 | adversarial | 3 | 1 | 3/3 | 2/3 | FAIL |
| CUR-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| NOM-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| NOM-02 | adversarial | 3 | 1 | 3/3 | 2/3 | FAIL |
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
| GP-03-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-04-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-07-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-08-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-09-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-10-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-11-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| GP-12-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-13-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| GP-14-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| GP-15-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-16-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| PERF-01-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-02-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| PERF-03-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-04-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| PERF-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-07-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| PERF-08-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-09-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| PERF-10-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-11-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| PERF-12-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-13-1 | entry | 3 | 1 | 2/3 | 2/3 | FAIL |
| PERF-14-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| PERF-15-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| PERF-16-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-01-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-02-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-03-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| TE-04-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-06-1 | entry | 3 | 0 | 1/3 | 2/3 | FAIL |
| TE-07-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-08-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-09-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-10-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-11-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| TE-12-1 | entry | 3 | 1 | 1/3 | 2/3 | FAIL |
| TE-13-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| TPR-01-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-02-1 | entry | 3 | 0 | 1/3 | 2/3 | FAIL |
| TPR-03-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-04-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-06-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| TPR-07-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |

## Totals

- entry: samples 118/156 pass; fixtures 41/52 pass
- adversarial: samples 69/75 pass; fixtures 22/25 pass
- samples: 187/231 pass (81.0%); floor 95% NOT met
- fixtures: 63/77 pass (hard checks contaminated, U0, U1, U2, U3, U4, U5, P0, P3; majority checks P1, P2, P4, P5)

RUN: FAIL
