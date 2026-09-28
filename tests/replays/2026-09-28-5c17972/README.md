# Replay of run 2026-09-27-5c17972 against expected files at 5a8df22

Purpose: per 2026-09-28 · replay-before-run-8. This replay counts toward no close condition; run 2026-09-27-5c17972 stands as recorded at 198/231.

Inputs: run 2026-09-27-5c17972's saved outputs; fixtures, expected files and tools/score_run.py at 5a8df22. RESULTS.md in this directory is the scorer's output, unedited.

## Totals

- All fixtures: samples 209/231 (90.5%), fixtures 70/77.
- Excluding CLR-02 and GP-16-1: samples 207/225 (92.0%), fixtures 70/75.

Run 7 as recorded, for reference: samples 198/231 (85.7%), fixtures 68/77; excluding CLR-02 and GP-16-1, samples 195/225 (86.7%), fixtures 67/75.

## Not comparable

A saved output is not comparable when a later ruling changes the fixture or the catalog text it is scored against. Two fixtures meet that test here; their rows are reported but excluded from the second totals.

- CLR-02: its fixture was rebuilt under clr-02-conforms-to-observed after these outputs were produced.
- GP-16-1: sample 3 prints GP-04's Pattern as it stood before gp-04-step-2-routing renamed it; U4 compares the What line to the current catalog, so the sample fails on wording, not behaviour.

## Not measurable by replay

The SKILL.md edits under tpr-02-step-5-alongside, gp-04-step-2-routing and cannot-show-fires cannot change saved outputs; run 8 measures them.

## Precision fixtures named in cannot-show-fires

| fixture | samples passing | fixture verdict | failed checks |
|---|---|---|---|
| NOM-01 | 3/3 | PASS | — |
| NOM-03 | 3/3 | PASS | — |
| SCP-02 | 3/3 | PASS | — |
| SCP-03 | 3/3 | PASS | — |
| CLR-02 | 0/3 | FAIL | k1, k2, k3: P2: required GP-09 not flagged; P5: Zero-flags line present but not expected |
| CLR-03 | 3/3 | PASS | — |

## Fixtures changed versus run 7 as recorded

| fixture | run 7 | replay | ruling responsible |
|---|---|---|---|
| GP-16-1 | 3/3 PASS | 2/3 FAIL | gp-04-step-2-routing (k3: U4, the saved What line "Award claims without the award" no longer matches GP-04's amended Pattern); not comparable |
| OVL-01 | 2/3 PASS | 3/3 PASS | omission-span-audit (k1) |
| PERF-08-1 | 1/3 FAIL | 3/3 PASS | perf-08-anchor-length (k1, k3) |
| PERF-15-1 | 2/3 PASS | 3/3 PASS | omission-span-audit (k2) |
| SCP-04 | 2/3 PASS | 3/3 PASS | omission-span-audit (k1) |
| TE-03-1 | 0/3 FAIL | 3/3 PASS | te-03-1-tpr-06 (k1, k2, k3: P4 on TPR-06); omission-span-audit (k1: P2) |
| TE-08-1 | 2/3 PASS | 3/3 PASS | omission-span-audit (k1) |
| TE-11-1 | 1/3 FAIL | 2/3 PASS | omission-span-audit (k3) |
| TPR-04-1 | 2/3 PASS | 3/3 PASS | omission-span-audit (k3) |
| VRQ-02 | 2/3 PASS | 3/3 PASS | omission-span-audit (k1) |

GP-16-1's change is a scoring artifact of the Pattern rename, not a change in skill behaviour: U4 compares a flag's What line to the current catalog Pattern, and the saved output predates the rename. It is the one sample that moved PASS to FAIL; twelve moved FAIL to PASS.
