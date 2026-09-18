# Results

- run_id: selftest
- date: 2026-09-18
- skill_commit: d17a00a
- model: none (crafted samples)
- fixtures: 1
- n_entry: 13
- n_adversarial: 0
- notes: scorer self-test; 13 crafted outputs for GP-01-1, see tests/selftest/EXPECTED.yaml

| fixture | k | verdict | failed checks | extras |
|---|---|---|---|---|
| GP-01-1 | 1 | PASS |  |  |
| GP-01-1 | 2 | PASS |  |  |
| GP-01-1 | 3 | PASS |  |  |
| GP-01-1 | 4 | FAIL | U1: closing line missing |  |
| GP-01-1 | 5 | FAIL | U1: text follows the closing line |  |
| GP-01-1 | 6 | FAIL | U2: term 'compliant' in line 'Fix: Rewrite: "I am paid only by planning fees; any conflict' |  |
| GP-01-1 | 7 | FAIL | U3: Flags: 2 but 1 Flag block(s) |  |
| GP-01-1 | 8 | FAIL | U3: Flag blocks not numbered 1..n without gaps |  |
| GP-01-1 | 9 | FAIL | U3: No-match line present with Flags: 1; P5: No-match line present but not expected |  |
| GP-01-1 | 10 | FAIL | U4: Flag 1 source 'RA-2025-12' != catalog 'RA-2024-04' |  |
| GP-01-1 | 11 | FAIL | U4: Flag 1 paragraph set '(a)(1)' != catalog '(a)(1), (a)(2)' |  |
| GP-01-1 | 12 | FAIL | P2: required GP-01 not flagged; P3: forbidden GP-02 flagged |  |
| GP-01-1 | 13 | FAIL | P1: expected 'none', got 'testimonial' |  |

## Totals

- entry: samples 3/13 pass; fixtures 0/1 pass
- adversarial: samples 0/0 pass; fixtures 0/0 pass

RUN: FAIL
