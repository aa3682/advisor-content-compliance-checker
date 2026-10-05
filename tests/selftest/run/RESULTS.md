# Results

- run_id: selftest
- date: 2026-09-18
- skill_commit: d17a00a
- model: none (crafted samples)
- fixtures: 4
- n_entry: 19
- n_adversarial: 4
- notes: scorer self-test; 20 crafted outputs for GP-01-1, 2 for GP-02-1, 2 for CLR-01, 2 for SCP-01, see tests/selftest/EXPECTED.yaml; every sample's <sample>.ISOLATION.txt is crafted evidence (cwd under /scratch/selftest/), not a recorded launch

| fixture | k | verdict | failed checks | extras |
|---|---|---|---|---|
| CLR-01 | 20 | PASS |  |  |
| CLR-01 | 21 | FAIL | U2: term 'compliant' in line 'Fix: Remove the claim; do not replace it with "fully complia' |  |
| GP-01-1 | 1 | PASS |  |  |
| GP-01-1 | 2 | FAIL | U5: Flag 1 Where quote 'I am completely free of conflicts of interest, an ' is not in the fixture |  |
| GP-01-1 | 3 | FAIL | U4: Flag 1 What 'Any absolute no-conflict statement; any claim of a' != catalog Pattern for GP-01 |  |
| GP-01-1 | 4 | FAIL | U1: closing line missing |  |
| GP-01-1 | 5 | FAIL | U1: text follows the closing line |  |
| GP-01-1 | 6 | FAIL | U2: term 'compliant' in line 'Fix: Rewrite: "I am paid only by planning fees; any conflict' |  |
| GP-01-1 | 7 | FAIL | U3: Flags: 2 but 1 Flag block(s) |  |
| GP-01-1 | 8 | FAIL | U3: Flag blocks not numbered 1..n without gaps / GP-01 appears in Flag blocks 1, 3; one Flag block per catalog ID |  |
| GP-01-1 | 9 | FAIL | U3: Zero-flags line present with Flags: 1, Confirm: 0; P5: Zero-flags line present but not expected |  |
| GP-01-1 | 10 | FAIL | U4: Flag 1 source 'RA-2025-12' != catalog 'RA-2024-04' |  |
| GP-01-1 | 11 | FAIL | U4: Flag 1 paragraph set '(a)(1)' != catalog '(a)(1), (a)(2)' |  |
| GP-01-1 | 12 | FAIL | P2: required GP-01 not flagged; P3: forbidden GP-02 flagged |  |
| GP-01-1 | 13 | FAIL | P1: expected 'none', got 'testimonial' |  |
| GP-01-1 | 14 | FAIL | U5: Flag 1 Where quote 'Being completely free of conflicts of interest is ' is not in the fixture |  |
| GP-01-1 | 15 | FAIL | U3: GP-01 appears in Flag blocks 1, 2; one Flag block per catalog ID |  |
| GP-01-1 | 16 | FAIL | contaminated: reported reading tests/expected/GP-01-1.yaml |  |
| GP-01-1 | 19 | PASS |  |  |
| GP-01-1 | 24 | FAIL | isolation: GP-01-1.24.ISOLATION.txt missing |  |
| GP-01-1 | 25 | FAIL | isolation: path outside skill/ and content.md: tests/expected/GP-01-1.yaml |  |
| GP-01-1 | 26 | FAIL | isolation: cwd '/scratch/selftest/GP-01-1.99' is not the sample's directory GP-01-1.26 |  |
| GP-02-1 | 1 | PASS |  | GP-05 |
| GP-02-1 | 2 | FAIL | P4: no Confirm block lists Would apply ['GP-03'] | GP-05 |
| SCP-01 | 22 | PASS |  |  |
| SCP-01 | 23 | FAIL | P5: expected one Scope line, found 2 |  |

## Per fixture

| fixture | class | n | tier 1 failures | tier 2 failures | P-assertions clean | needs | verdict |
|---|---|---|---|---|---|---|---|
| CLR-01 | adversarial | 2 | 1 | 0 | 2/2 | 2/2 | FAIL |
| SCP-01 | adversarial | 2 | 0 | 0 | 1/2 | 2/2 | FAIL |
| GP-01-1 | entry | 20 | 7 | 10 | 17/20 | 11/20 | FAIL |
| GP-02-1 | entry | 2 | 0 | 0 | 1/2 | 2/2 | FAIL |

## Single-draw precision

- count: 0; cap: 2 (more than 2 fails the run); cap met

## Notes

none

## Totals

- entry: samples 3/22 pass; fixtures 0/2 pass
- adversarial: samples 2/4 pass; fixtures 0/2 pass
- samples: 5/26 pass (19.2%); floor 95% NOT met
- fixtures: 0/4 pass (tier 1 checks isolation, contaminated, U0, P0, U1, U2; tier 2 checks U3, U4, U5, P3, fail at 2+ samples; majority checks P1, P2, P4, P5)
- single-draw precision: 0; cap 2 met

RUN: FAIL
