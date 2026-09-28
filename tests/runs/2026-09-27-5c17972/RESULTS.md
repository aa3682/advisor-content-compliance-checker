# Results

- run_id: 2026-09-27-5c17972
- date: 2026-09-27
- skill_commit: 5c17972
- model: sonnet
- fixtures: 77
- n_entry: 3
- n_adversarial: 3
- notes: run 7, first run under sandbox-escape-handling and where-anchor-either-span, and the first on SKILL.md at 5c17972 (SKILL.md changed since run 6's 5168941). launch_sample.py staged each sample fresh under a neutral temp path, /tmp/acc-run-2026-09-27-5c17972-6t4m29m7/<fixture>.<k>/; the RUNLIST scratch_path column (/tmp/acc-stage-5c17972) was staged by prepare_run.py but not used for launch. Reviewing model: sonnet (alias resolved to claude-sonnet-5); model_reported in LAUNCH.log may additionally list claude-haiku-4-5-20251001, the CLI's own side calls, not the reviewing model. No fixes of any kind were made during this run.

| fixture | k | verdict | failed checks | extras |
|---|---|---|---|---|
| CLR-01 | 1 | PASS |  |  |
| CLR-01 | 2 | PASS |  |  |
| CLR-01 | 3 | PASS |  |  |
| CLR-02 | 1 | FAIL | P2: required GP-09 not flagged; P5: Zero-flags line present but not expected |  |
| CLR-02 | 2 | FAIL | P2: required GP-09 not flagged; P5: Zero-flags line present but not expected |  |
| CLR-02 | 3 | FAIL | P2: required GP-09 not flagged; P5: Zero-flags line present but not expected |  |
| CLR-03 | 1 | PASS |  |  |
| CLR-03 | 2 | PASS |  |  |
| CLR-03 | 3 | PASS |  |  |
| CNF-02 | 1 | PASS |  |  |
| CNF-02 | 2 | FAIL | P4: no Confirm block lists Would apply ['GP-06']; P5: Zero-flags line present but not expected |  |
| CNF-02 | 3 | FAIL | P4: no Confirm block lists Would apply ['GP-06']; P5: Zero-flags line present but not expected |  |
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
| GP-03-1 | 1 | FAIL | P2: GP-03 flagged but Where lacks any of ['a process validated by leading professional institutions'] |  |
| GP-03-1 | 2 | PASS |  |  |
| GP-03-1 | 3 | PASS |  |  |
| GP-04-1 | 1 | FAIL | P2: required GP-04 not flagged | GP-16 |
| GP-04-1 | 2 | FAIL | P2: required GP-04 not flagged | GP-16 |
| GP-04-1 | 3 | FAIL | P2: required GP-04 not flagged | GP-16 |
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
| GP-10-1 | 3 | PASS |  | TPR-01, TPR-06 |
| GP-11-1 | 1 | PASS |  |  |
| GP-11-1 | 2 | PASS |  |  |
| GP-11-1 | 3 | PASS |  |  |
| GP-12-1 | 1 | PASS |  |  |
| GP-12-1 | 2 | PASS |  |  |
| GP-12-1 | 3 | PASS |  |  |
| GP-13-1 | 1 | PASS |  | GP-03 |
| GP-13-1 | 2 | PASS |  |  |
| GP-13-1 | 3 | PASS |  |  |
| GP-14-1 | 1 | PASS |  | TPR-01, TPR-02, TPR-05, TPR-06 |
| GP-14-1 | 2 | PASS |  | TPR-01, TPR-02, TPR-05, TPR-06 |
| GP-14-1 | 3 | PASS |  | GP-03, TPR-01, TPR-05, TPR-06 |
| GP-15-1 | 1 | PASS |  |  |
| GP-15-1 | 2 | PASS |  |  |
| GP-15-1 | 3 | PASS |  |  |
| GP-16-1 | 1 | PASS |  |  |
| GP-16-1 | 2 | PASS |  |  |
| GP-16-1 | 3 | PASS |  | GP-04 |
| NOM-01 | 1 | PASS |  |  |
| NOM-01 | 2 | PASS |  |  |
| NOM-01 | 3 | PASS |  |  |
| NOM-02 | 1 | PASS |  |  |
| NOM-02 | 2 | PASS |  |  |
| NOM-02 | 3 | PASS |  |  |
| NOM-03 | 1 | PASS |  |  |
| NOM-03 | 2 | PASS |  |  |
| NOM-03 | 3 | PASS |  |  |
| OVL-01 | 1 | FAIL | P2: PERF-08 flagged but Where lacks any of ['up 14% before fees this year'] | TE-08 |
| OVL-01 | 2 | PASS |  | PERF-04, TE-08, TE-10 |
| OVL-01 | 3 | PASS |  | TE-06, TE-08, TE-09, TE-10 |
| OVL-02 | 1 | PASS |  |  |
| OVL-02 | 2 | PASS |  |  |
| OVL-02 | 3 | PASS |  |  |
| OVL-03 | 1 | PASS |  |  |
| OVL-03 | 2 | PASS |  |  |
| OVL-03 | 3 | PASS |  |  |
| PERF-01-1 | 1 | FAIL | P1: expected ['gross performance', 'hypothetical performance', 'net performance'], got ['gross performance', 'net performance'] | PERF-03, PERF-07, PERF-16 |
| PERF-01-1 | 2 | PASS |  | PERF-03, PERF-04, PERF-07, PERF-10, PERF-11, PERF-16 |
| PERF-01-1 | 3 | PASS |  | PERF-03, PERF-07, PERF-10, PERF-12, PERF-13, PERF-14, PERF-16 |
| PERF-02-1 | 1 | PASS |  |  |
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
| PERF-07-1 | 1 | PASS |  |  |
| PERF-07-1 | 2 | PASS |  |  |
| PERF-07-1 | 3 | PASS |  |  |
| PERF-08-1 | 1 | FAIL | P2: PERF-08 flagged but Where lacks any of ['1 year 11.2% gross, 10.1% net; 5 years 7.8% gross, 6.7% net'] |  |
| PERF-08-1 | 2 | PASS |  |  |
| PERF-08-1 | 3 | FAIL | P2: PERF-08 flagged but Where lacks any of ['1 year 11.2% gross, 10.1% net; 5 years 7.8% gross, 6.7% net'] |  |
| PERF-09-1 | 1 | PASS |  | PERF-01, PERF-03, PERF-16 |
| PERF-09-1 | 2 | PASS |  | PERF-16 |
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
| PERF-13-1 | 1 | PASS |  |  |
| PERF-13-1 | 2 | PASS |  | PERF-07 |
| PERF-13-1 | 3 | PASS |  |  |
| PERF-14-1 | 1 | PASS |  | PERF-12 |
| PERF-14-1 | 2 | PASS |  |  |
| PERF-14-1 | 3 | PASS |  |  |
| PERF-15-1 | 1 | PASS |  |  |
| PERF-15-1 | 2 | FAIL | P2: PERF-15 flagged but Where lacks any of ['Steady Income model, hypothetical results', 'Model trade records from before 2022 were not retained.'] |  |
| PERF-15-1 | 3 | PASS |  |  |
| PERF-16-1 | 1 | PASS |  |  |
| PERF-16-1 | 2 | PASS |  |  |
| PERF-16-1 | 3 | PASS |  |  |
| SCP-01 | 1 | PASS |  |  |
| SCP-01 | 2 | PASS |  |  |
| SCP-01 | 3 | PASS |  |  |
| SCP-02 | 1 | PASS |  |  |
| SCP-02 | 2 | PASS |  | TE-08, TE-10 |
| SCP-02 | 3 | PASS |  |  |
| SCP-03 | 1 | PASS |  |  |
| SCP-03 | 2 | PASS |  |  |
| SCP-03 | 3 | PASS |  |  |
| SCP-04 | 1 | FAIL | P2: TPR-04 flagged but Where lacks any of ['shows no organization name'] |  |
| SCP-04 | 2 | PASS |  |  |
| SCP-04 | 3 | PASS |  |  |
| TE-01-1 | 1 | PASS |  | TE-08, TE-10 |
| TE-01-1 | 2 | PASS |  | TE-06, TE-08, TE-10 |
| TE-01-1 | 3 | PASS |  | TE-08, TE-10 |
| TE-02-1 | 1 | PASS |  | GP-12, TE-08, TE-10 |
| TE-02-1 | 2 | PASS |  | GP-12, TE-08, TE-10 |
| TE-02-1 | 3 | PASS |  | GP-12, TE-08, TE-10 |
| TE-03-1 | 1 | FAIL | P2: TE-03 flagged but Where lacks any of ['Straight from our Google listing', 'imported directly from Google']; P4: no Confirm block lists Would apply ['TPR-06'] | TE-13, TPR-03 |
| TE-03-1 | 2 | FAIL | P4: no Confirm block lists Would apply ['TPR-06'] | TE-13, TPR-03 |
| TE-03-1 | 3 | FAIL | P4: no Confirm block lists Would apply ['TPR-06'] | TE-13, TPR-03 |
| TE-04-1 | 1 | PASS |  | GP-01, TE-03 |
| TE-04-1 | 2 | PASS |  | TE-01, TE-03, TE-08, TE-09, TE-10 |
| TE-04-1 | 3 | PASS |  | TE-01, TE-03 |
| TE-05-1 | 1 | PASS |  | TE-08, TE-09, TE-10 |
| TE-05-1 | 2 | PASS |  | TE-08, TE-10 |
| TE-05-1 | 3 | PASS |  | TE-08, TE-09, TE-10 |
| TE-06-1 | 1 | PASS |  |  |
| TE-06-1 | 2 | PASS |  |  |
| TE-06-1 | 3 | PASS |  |  |
| TE-07-1 | 1 | PASS |  | TE-06, TE-08, TE-10 |
| TE-07-1 | 2 | PASS |  | TE-06, TE-08, TE-10 |
| TE-07-1 | 3 | PASS |  | TE-06, TE-08, TE-10 |
| TE-08-1 | 1 | FAIL | P2: TE-08 flagged but Where lacks any of ['she is paid $500 per month for the recommendation'] | TE-09, TE-10 |
| TE-08-1 | 2 | PASS |  | TE-09, TE-10 |
| TE-08-1 | 3 | PASS |  | TE-09, TE-10 |
| TE-09-1 | 1 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 2 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 3 | PASS |  | TE-08, TE-10 |
| TE-10-1 | 1 | PASS |  | TE-08, TE-09 |
| TE-10-1 | 2 | PASS |  | TE-08, TE-09 |
| TE-10-1 | 3 | PASS |  | TE-08 |
| TE-11-1 | 1 | PASS |  |  |
| TE-11-1 | 2 | FAIL | P2: required TE-11 not flagged; P5: Zero-flags line present but not expected |  |
| TE-11-1 | 3 | FAIL | P2: TE-11 flagged but Where lacks any of ['has no affiliation with the firm', 'answers the phone when you call our office'] |  |
| TE-12-1 | 1 | PASS |  |  |
| TE-12-1 | 2 | PASS |  |  |
| TE-12-1 | 3 | PASS |  |  |
| TE-13-1 | 1 | PASS |  |  |
| TE-13-1 | 2 | PASS |  |  |
| TE-13-1 | 3 | PASS |  |  |
| TPR-01-1 | 1 | PASS |  |  |
| TPR-01-1 | 2 | PASS |  | GP-10 |
| TPR-01-1 | 3 | PASS |  |  |
| TPR-02-1 | 1 | FAIL | P4: no Confirm block lists Would apply ['TPR-02'] |  |
| TPR-02-1 | 2 | FAIL | P2: required TPR-02 not flagged; P4: no Confirm block lists Would apply ['TPR-05', 'TPR-06'] |  |
| TPR-02-1 | 3 | FAIL | P2: required TPR-02 not flagged |  |
| TPR-03-1 | 1 | PASS |  |  |
| TPR-03-1 | 2 | PASS |  |  |
| TPR-03-1 | 3 | PASS |  |  |
| TPR-04-1 | 1 | PASS |  | TPR-07 |
| TPR-04-1 | 2 | PASS |  | TPR-07 |
| TPR-04-1 | 3 | FAIL | P2: TPR-04 flagged but Where lacks any of ['it reads Client Confidence Rating 2025'] | TPR-07 |
| TPR-05-1 | 1 | PASS |  |  |
| TPR-05-1 | 2 | FAIL | P2: required TPR-05 not flagged | GP-01 |
| TPR-05-1 | 3 | PASS |  |  |
| TPR-06-1 | 1 | PASS |  | TPR-05 |
| TPR-06-1 | 2 | PASS |  | TPR-05 |
| TPR-06-1 | 3 | PASS |  | TPR-05 |
| TPR-07-1 | 1 | PASS |  |  |
| TPR-07-1 | 2 | PASS |  |  |
| TPR-07-1 | 3 | PASS |  |  |
| UNR-01 | 1 | FAIL | P2: required GP-15 not flagged; P5: Zero-flags line present but not expected |  |
| UNR-01 | 2 | FAIL | P2: required GP-15 not flagged; P5: Zero-flags line present but not expected |  |
| UNR-01 | 3 | FAIL | P2: required GP-15 not flagged; P5: Zero-flags line present but not expected |  |
| UNR-02 | 1 | PASS |  |  |
| UNR-02 | 2 | PASS |  |  |
| UNR-02 | 3 | PASS |  |  |
| UNR-03 | 1 | PASS |  |  |
| UNR-03 | 2 | PASS |  |  |
| UNR-03 | 3 | PASS |  |  |
| VRQ-01 | 1 | PASS |  |  |
| VRQ-01 | 2 | PASS |  |  |
| VRQ-01 | 3 | PASS |  |  |
| VRQ-02 | 1 | FAIL | P2: PERF-05 flagged but Where lacks any of ['versus 8.1% for a broad U.S. stock index'] |  |
| VRQ-02 | 2 | PASS |  |  |
| VRQ-02 | 3 | PASS |  |  |
| VRQ-03 | 1 | FAIL | U0: missing output |  |
| VRQ-03 | 2 | FAIL | U0: missing output |  |
| VRQ-03 | 3 | PASS |  | GP-01, TE-08, TE-09, TE-10 |

## Per fixture

| fixture | class | n | hard failures | P-assertions clean | needs | verdict |
|---|---|---|---|---|---|---|
| CLR-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CLR-02 | adversarial | 3 | 0 | 0/3 | 2/3 | FAIL |
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
| OVL-01 | adversarial | 3 | 0 | 2/3 | 2/3 | PASS |
| OVL-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| OVL-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| SCP-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| SCP-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| SCP-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| SCP-04 | adversarial | 3 | 0 | 2/3 | 2/3 | PASS |
| UNR-01 | adversarial | 3 | 0 | 0/3 | 2/3 | FAIL |
| UNR-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| UNR-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| VRQ-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| VRQ-02 | adversarial | 3 | 0 | 2/3 | 2/3 | PASS |
| VRQ-03 | adversarial | 3 | 2 | 3/3 | 2/3 | FAIL |
| GP-01-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-02-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-03-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| GP-04-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| GP-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-07-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-08-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-09-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-10-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-11-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-12-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-13-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-14-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-15-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-16-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-01-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| PERF-02-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-03-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-04-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| PERF-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-07-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-08-1 | entry | 3 | 0 | 1/3 | 2/3 | FAIL |
| PERF-09-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-10-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-11-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-12-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-13-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-14-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-15-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| PERF-16-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-01-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-02-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-03-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| TE-04-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-07-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-08-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| TE-09-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-10-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-11-1 | entry | 3 | 0 | 1/3 | 2/3 | FAIL |
| TE-12-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-13-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-01-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-02-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| TPR-03-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-04-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| TPR-05-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| TPR-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-07-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |

## Totals

- entry: samples 136/156 pass; fixtures 47/52 pass
- adversarial: samples 62/75 pass; fixtures 21/25 pass
- samples: 198/231 pass (85.7%); floor 95% NOT met
- fixtures: 68/77 pass (hard checks isolation, contaminated, U0, U1, U2, U3, U4, U5, P0, P3; majority checks P1, P2, P4, P5)

RUN: FAIL
