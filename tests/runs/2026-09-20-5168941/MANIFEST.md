# Manifest
- run_id: 2026-09-20-5168941
- date: 2026-09-20
- skill_commit: 5168941
- model: sonnet
- model_reported: claude-sonnet-5
- staging_root: /tmp/claude-0/-home-user-advisor-content-compliance-checker/ae502e5e-0fbb-53ec-9f8a-5e9b2ae89a02/scratchpad/staging-5168941
- fixtures: 77
- n_entry: 3
- n_adversarial: 3
- notes: run 6, first run after anchor-migration-pass and ruling-62-te12-withdrawal. SKILL.md is byte-identical to run 5's; only expected anchors, TE-12-1's element line and the PERF-02-1 fixture changed, so the comparison with run 2026-09-20-5a62d91 isolates the migration. Reviewing model: sonnet (alias resolved to claude-sonnet-5); model_reported in LAUNCH.log may additionally list claude-haiku-4-5-20251001, the CLI's own side calls, not the reviewing model. Untouched and expected to still fail: CLR-02 GP-09, CNF-02 GP-06, TPR-02-1 TPR-02.
  Container restart: the session container restarted with SCP-04.3 in flight; 230 of 231 samples had already been launched and recorded and the launcher was killed before it exited. No sample was relaunched (phase6-run-model: a sample with no output.md is a recorded failure and is not retried within the run).
  Sandbox escape, SCP-04.3: the subagent ran with the correct working directory, took 17 turns, exited 0 and replied DONE, but wrote no output.md into its staged directory. Its output was found at the repository root, /home/user/advisor-content-compliance-checker/output.md, matching SCP-04's content. It is preserved as SCP-04.3.ESCAPED-OUTPUT.txt and the stray file was removed; the sample is recorded as a missing output (U0) and is not credited. Unlike run 5's SCP-03.1 this was not self-reported, so CONTAMINATED.txt could not have caught it: the reply was a bare DONE. Probable mechanism: the staging root sits under a scratchpad directory whose own name, -home-user-advisor-content-compliance-checker, encodes the repository path, so pwd hands a subagent the path run-isolation-sandbox intends to withhold. This needs a ruling; run-isolation-sandbox's pre-launch listing cannot see a post-launch write, and the manual channel depends on self-report.
