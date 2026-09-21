# Results

- run_id: 2026-09-20-5168941
- date: 2026-09-20
- skill_commit: 5168941
- model: sonnet
- fixtures: 77
- n_entry: 3
- n_adversarial: 3
- notes: run 6, first run after anchor-migration-pass and ruling-62-te12-withdrawal. SKILL.md is byte-identical to run 5's; only expected anchors, TE-12-1's element line and the PERF-02-1 fixture changed, so the comparison with run 2026-09-20-5a62d91 isolates the migration. Reviewing model: sonnet (alias resolved to claude-sonnet-5); model_reported in LAUNCH.log may additionally list claude-haiku-4-5-20251001, the CLI's own side calls, not the reviewing model. Untouched and expected to still fail: CLR-02 GP-09, CNF-02 GP-06, TPR-02-1 TPR-02.

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
| CNF-02 | 1 | FAIL | P4: no Confirm block lists Would apply ['GP-06']; P5: Zero-flags line present but not expected |  |
| CNF-02 | 2 | FAIL | P4: no Confirm block lists Would apply ['GP-06']; P5: Zero-flags line present but not expected |  |
| CNF-02 | 3 | FAIL | P4: no Confirm block lists Would apply ['GP-06']; P5: Zero-flags line present but not expected |  |
| CNF-03 | 1 | PASS |  |  |
| CNF-03 | 2 | PASS |  |  |
| CNF-03 | 3 | PASS |  |  |
| CNF-04 | 1 | PASS |  |  |
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
| GP-04-1 | 2 | FAIL | P2: required GP-04 not flagged | GP-16 |
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
| GP-09-1 | 2 | PASS |  | GP-10 |
| GP-09-1 | 3 | PASS |  |  |
| GP-10-1 | 1 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-10-1 | 2 | PASS |  | TPR-01, TPR-05, TPR-06 |
| GP-10-1 | 3 | PASS |  | TPR-01, TPR-05, TPR-06 |
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
| GP-14-1 | 2 | PASS |  | GP-03, TPR-01, TPR-02 |
| GP-14-1 | 3 | FAIL | P2: required GP-14 not flagged | GP-03, TPR-01, TPR-05, TPR-06 |
| GP-15-1 | 1 | PASS |  |  |
| GP-15-1 | 2 | PASS |  |  |
| GP-15-1 | 3 | PASS |  |  |
| GP-16-1 | 1 | PASS |  |  |
| GP-16-1 | 2 | PASS |  |  |
| GP-16-1 | 3 | PASS |  |  |
| NOM-01 | 1 | PASS |  |  |
| NOM-01 | 2 | PASS |  |  |
| NOM-01 | 3 | FAIL | P3: forbidden GP-03 flagged; P5: Zero-flags line expected but absent |  |
| NOM-02 | 1 | PASS |  |  |
| NOM-02 | 2 | PASS |  |  |
| NOM-02 | 3 | PASS |  |  |
| NOM-03 | 1 | PASS |  |  |
| NOM-03 | 2 | PASS |  |  |
| NOM-03 | 3 | PASS |  |  |
| OVL-01 | 1 | FAIL | P2: TE-01 flagged but Where lacks any of ["a note from a family I've worked with since 2022"] | TE-08, TE-10 |
| OVL-01 | 2 | PASS |  | TE-06, TE-08, TE-10 |
| OVL-01 | 3 | FAIL | P2: TE-01 flagged but Where lacks any of ["a note from a family I've worked with since 2022"] | TE-08, TE-10 |
| OVL-02 | 1 | PASS |  |  |
| OVL-02 | 2 | PASS |  |  |
| OVL-02 | 3 | PASS |  |  |
| OVL-03 | 1 | PASS |  |  |
| OVL-03 | 2 | PASS |  |  |
| OVL-03 | 3 | PASS |  |  |
| PERF-01-1 | 1 | PASS |  | PERF-07, PERF-12 |
| PERF-01-1 | 2 | PASS |  | PERF-12 |
| PERF-01-1 | 3 | PASS |  | PERF-03, PERF-04, PERF-07, PERF-12, PERF-16 |
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
| PERF-06-1 | 1 | PASS |  |  |
| PERF-06-1 | 2 | PASS |  | PERF-03 |
| PERF-06-1 | 3 | PASS |  | PERF-03 |
| PERF-07-1 | 1 | PASS |  |  |
| PERF-07-1 | 2 | PASS |  |  |
| PERF-07-1 | 3 | PASS |  |  |
| PERF-08-1 | 1 | PASS |  |  |
| PERF-08-1 | 2 | PASS |  |  |
| PERF-08-1 | 3 | PASS |  |  |
| PERF-09-1 | 1 | PASS |  |  |
| PERF-09-1 | 2 | PASS |  | PERF-01, PERF-16 |
| PERF-09-1 | 3 | PASS |  | PERF-16 |
| PERF-10-1 | 1 | PASS |  |  |
| PERF-10-1 | 2 | PASS |  |  |
| PERF-10-1 | 3 | PASS |  |  |
| PERF-11-1 | 1 | FAIL | P2: required PERF-11 not flagged; P5: Zero-flags line present but not expected |  |
| PERF-11-1 | 2 | FAIL | P2: required PERF-11 not flagged; P5: Zero-flags line present but not expected |  |
| PERF-11-1 | 3 | PASS |  |  |
| PERF-12-1 | 1 | PASS |  |  |
| PERF-12-1 | 2 | PASS |  |  |
| PERF-12-1 | 3 | PASS |  |  |
| PERF-13-1 | 1 | PASS |  | PERF-01, PERF-07 |
| PERF-13-1 | 2 | PASS |  | PERF-01, PERF-07 |
| PERF-13-1 | 3 | PASS |  | PERF-07 |
| PERF-14-1 | 1 | PASS |  |  |
| PERF-14-1 | 2 | PASS |  |  |
| PERF-14-1 | 3 | PASS |  |  |
| PERF-15-1 | 1 | FAIL | P2: PERF-15 flagged but Where lacks any of ['Steady Income model, hypothetical results'] |  |
| PERF-15-1 | 2 | FAIL | P2: PERF-15 flagged but Where lacks any of ['Steady Income model, hypothetical results'] | PERF-12 |
| PERF-15-1 | 3 | FAIL | P2: PERF-15 flagged but Where lacks any of ['Steady Income model, hypothetical results'] |  |
| PERF-16-1 | 1 | PASS |  |  |
| PERF-16-1 | 2 | PASS |  |  |
| PERF-16-1 | 3 | PASS |  |  |
| SCP-01 | 1 | PASS |  |  |
| SCP-01 | 2 | PASS |  |  |
| SCP-01 | 3 | PASS |  |  |
| SCP-02 | 1 | FAIL | P2: TE-01 flagged but Where lacks any of ['one of the families I work with told me last week'] |  |
| SCP-02 | 2 | FAIL | P2: TE-01 flagged but Where lacks any of ['one of the families I work with told me last week'] |  |
| SCP-02 | 3 | FAIL | P2: TE-01 flagged but Where lacks any of ['one of the families I work with told me last week'] | TE-08, TE-10 |
| SCP-03 | 1 | PASS |  |  |
| SCP-03 | 2 | PASS |  |  |
| SCP-03 | 3 | PASS |  |  |
| SCP-04 | 1 | PASS |  |  |
| SCP-04 | 2 | PASS |  |  |
| SCP-04 | 3 | FAIL | U0: missing output |  |
| TE-01-1 | 1 | FAIL | P2: TE-01 flagged but Where lacks any of ['What families say about working with me'] |  |
| TE-01-1 | 2 | PASS |  |  |
| TE-01-1 | 3 | FAIL | P2: TE-01 flagged but Where lacks any of ['What families say about working with me'] |  |
| TE-02-1 | 1 | PASS |  | GP-12, TE-08, TE-10 |
| TE-02-1 | 2 | PASS |  | GP-12, TE-08, TE-10 |
| TE-02-1 | 3 | PASS |  | GP-12, TE-08, TE-09, TE-10 |
| TE-03-1 | 1 | FAIL | P4: no Confirm block lists Would apply ['TPR-06'] | GP-01, TE-13, TPR-03 |
| TE-03-1 | 2 | FAIL | P4: no Confirm block lists Would apply ['TPR-06'] | TPR-03 |
| TE-03-1 | 3 | FAIL | P4: no Confirm block lists Would apply ['TPR-06'] | TPR-03 |
| TE-04-1 | 1 | PASS |  | GP-01, TE-03, TE-08, TE-10 |
| TE-04-1 | 2 | PASS |  | TE-01 |
| TE-04-1 | 3 | PASS |  | TE-03, TE-08, TE-10 |
| TE-05-1 | 1 | PASS |  | TE-08, TE-09, TE-10 |
| TE-05-1 | 2 | PASS |  | TE-08, TE-09, TE-10 |
| TE-05-1 | 3 | PASS |  | TE-08, TE-10 |
| TE-06-1 | 1 | PASS |  |  |
| TE-06-1 | 2 | PASS |  |  |
| TE-06-1 | 3 | PASS |  |  |
| TE-07-1 | 1 | PASS |  | TE-06, TE-08, TE-09, TE-10 |
| TE-07-1 | 2 | PASS |  | TE-06, TE-08, TE-09, TE-10 |
| TE-07-1 | 3 | PASS |  | TE-06, TE-08, TE-10 |
| TE-08-1 | 1 | PASS |  | TE-10 |
| TE-08-1 | 2 | PASS |  | TE-10 |
| TE-08-1 | 3 | PASS |  | TE-10 |
| TE-09-1 | 1 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 2 | PASS |  | TE-08, TE-10 |
| TE-09-1 | 3 | FAIL | P2: TE-09 flagged but Where lacks any of ['$250 for each referral that becomes a client'] | TE-08, TE-10 |
| TE-10-1 | 1 | FAIL | U5: Confirm 1 Where quote 'he receives $300 for each referral that becomes a ' is not in the fixture / Confirm 2 Where quote 'he receives $300 for each referral that becomes a ' is not in the fixture | TE-08, TE-09 |
| TE-10-1 | 2 | PASS |  | TE-08, TE-09 |
| TE-10-1 | 3 | PASS |  | TE-08, TE-09 |
| TE-11-1 | 1 | PASS |  |  |
| TE-11-1 | 2 | PASS |  |  |
| TE-11-1 | 3 | PASS |  |  |
| TE-12-1 | 1 | PASS |  |  |
| TE-12-1 | 2 | PASS |  |  |
| TE-12-1 | 3 | PASS |  |  |
| TE-13-1 | 1 | FAIL | P2: TE-13 flagged but Where lacks any of ['They took the worry out of our retirement.', 'Every dollar has a purpose now.', 'The best money decision we ever made.'] |  |
| TE-13-1 | 2 | PASS |  |  |
| TE-13-1 | 3 | PASS |  |  |
| TPR-01-1 | 1 | PASS |  |  |
| TPR-01-1 | 2 | FAIL | P2: TPR-01 flagged but Where lacks any of ['gave the practice its 2025 Client Confidence rating'] |  |
| TPR-01-1 | 3 | FAIL | P2: TPR-01 flagged but Where lacks any of ['gave the practice its 2025 Client Confidence rating'] |  |
| TPR-02-1 | 1 | FAIL | P2: required TPR-02 not flagged; P4: no Confirm block lists Would apply ['TPR-05', 'TPR-06'] |  |
| TPR-02-1 | 2 | FAIL | P2: required TPR-02 not flagged; P4: no Confirm block lists Would apply ['TPR-05', 'TPR-06'] |  |
| TPR-02-1 | 3 | FAIL | P2: required TPR-02 not flagged |  |
| TPR-03-1 | 1 | PASS |  |  |
| TPR-03-1 | 2 | PASS |  |  |
| TPR-03-1 | 3 | PASS |  |  |
| TPR-04-1 | 1 | PASS |  |  |
| TPR-04-1 | 2 | PASS |  |  |
| TPR-04-1 | 3 | PASS |  |  |
| TPR-05-1 | 1 | PASS |  |  |
| TPR-05-1 | 2 | PASS |  |  |
| TPR-05-1 | 3 | PASS |  |  |
| TPR-06-1 | 1 | PASS |  | TPR-05 |
| TPR-06-1 | 2 | PASS |  | TPR-05 |
| TPR-06-1 | 3 | PASS |  | TPR-05 |
| TPR-07-1 | 1 | FAIL | P2: TPR-07 flagged but Where lacks any of ["that's the badge at the top of every page on our site"] |  |
| TPR-07-1 | 2 | PASS |  |  |
| TPR-07-1 | 3 | FAIL | P2: TPR-07 flagged but Where lacks any of ["that's the badge at the top of every page on our site"] |  |
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
| VRQ-03 | 1 | PASS |  | TE-08, TE-09, TE-10 |
| VRQ-03 | 2 | PASS |  | GP-01, TE-08, TE-09, TE-10 |
| VRQ-03 | 3 | PASS |  | GP-01, TE-08, TE-09, TE-10 |

## Per fixture

| fixture | class | n | hard failures | P-assertions clean | needs | verdict |
|---|---|---|---|---|---|---|
| CLR-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CLR-02 | adversarial | 3 | 0 | 0/3 | 2/3 | FAIL |
| CLR-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CNF-02 | adversarial | 3 | 0 | 0/3 | 2/3 | FAIL |
| CNF-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CNF-04 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CUR-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CUR-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| CUR-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| NOM-01 | adversarial | 3 | 1 | 2/3 | 2/3 | FAIL |
| NOM-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| NOM-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| OVL-01 | adversarial | 3 | 0 | 1/3 | 2/3 | FAIL |
| OVL-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| OVL-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| SCP-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| SCP-02 | adversarial | 3 | 0 | 0/3 | 2/3 | FAIL |
| SCP-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| SCP-04 | adversarial | 3 | 1 | 3/3 | 2/3 | FAIL |
| UNR-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| UNR-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| UNR-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| VRQ-01 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| VRQ-02 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| VRQ-03 | adversarial | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-01-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-02-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-03-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| GP-04-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
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
| PERF-01-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-02-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-03-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-04-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-07-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-08-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-09-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-10-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-11-1 | entry | 3 | 0 | 1/3 | 2/3 | FAIL |
| PERF-12-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-13-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-14-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| PERF-15-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| PERF-16-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-01-1 | entry | 3 | 0 | 1/3 | 2/3 | FAIL |
| TE-02-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-03-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| TE-04-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-07-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-08-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-09-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| TE-10-1 | entry | 3 | 1 | 3/3 | 2/3 | FAIL |
| TE-11-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-12-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TE-13-1 | entry | 3 | 0 | 2/3 | 2/3 | PASS |
| TPR-01-1 | entry | 3 | 0 | 1/3 | 2/3 | FAIL |
| TPR-02-1 | entry | 3 | 0 | 0/3 | 2/3 | FAIL |
| TPR-03-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-04-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-05-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-06-1 | entry | 3 | 0 | 3/3 | 2/3 | PASS |
| TPR-07-1 | entry | 3 | 0 | 1/3 | 2/3 | FAIL |

## Totals

- entry: samples 134/156 pass; fixtures 44/52 pass
- adversarial: samples 62/75 pass; fixtures 19/25 pass
- samples: 196/231 pass (84.8%); floor 95% NOT met
- fixtures: 63/77 pass (hard checks isolation, contaminated, U0, U1, U2, U3, U4, U5, P0, P3; majority checks P1, P2, P4, P5)

RUN: FAIL
