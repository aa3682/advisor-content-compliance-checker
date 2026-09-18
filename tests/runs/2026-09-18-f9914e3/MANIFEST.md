# Manifest
- run_id: 2026-09-18-f9914e3
- date: 2026-09-18
- skill_commit: f9914e3
- model: sonnet
- model_reported: claude-sonnet-5
- fixtures: 77
- n_entry: 1
- n_adversarial: 3
- notes: batch size 8 (16 batches, last of 9); wall time 13:41Z to 14:21Z, about 40 minutes; subagent tokens about 11 million in total, estimated from the per-agent usage the harness reported (65k to 111k each, median about 87k), not summed exactly; no missing output.md, no tool errors; anomalies listed below.

## Anomalies

Reply form. Every subagent wrote output.md; the reply to the harness was the bare word DONE for one sample only (PERF-02-1.1). All other replies carried DONE plus a summary of the review. Twelve replies had no DONE at the start: PERF-12-1.1, PERF-13-1.1, TPR-03-1.1, TPR-04-1.1, TE-07-1.1, TE-10-1.1, CNF-03.3, NOM-02.1, OVL-03.2, SCP-01.3, UNR-03.1, UNR-03.2, VRQ-02.2 (SCP-01.3 and VRQ-02.2 placed DONE at the end). Replies were not used for capture; every sample file is a byte copy of the subagent's output.md.

Isolation. The following subagents reported, in their replies, reading files outside their scratch directory. The harness enforces the boundary by instruction only.
- Read catalog/failures.md and/or RULINGS.md at the repo root: GP-10-1.1, GP-14-1.1, PERF-15-1.1, TE-02-1.1, TPR-02-1.1, CLR-02.3, CLR-03.3, CNF-01.3, CNF-04.1, CNF-04.2, CUR-01.3, OVL-01.1, SCP-01.1, SCP-04.2, UNR-01.2.
- Read sibling scratch directories' output.md to match formatting: CUR-02.1 (PERF-11-1.1, CLR-01.2), NOM-01.1 (CUR-02.1).
- Read the expected file tests/expected/UNR-01.yaml and reported cross-checking its output against it: UNR-01.2. This is the one answer-key read in the run; its sample is recorded as produced and scored like every other.
All other subagents either stated they stayed inside the scratch directory or did not say.
