# Tests

Adversarial test set for skill/SKILL.md. Specification: RULINGS.md entries phase6-run-method, phase6-fixture-format, phase6-pass-criteria, phase6-adversarial-categories, repeated-pattern-single-flag.

## Layout

- tests/fixtures/<id>.md — content only, exactly what an advisor would paste. No frontmatter, no metadata, no fixture ID inside the file. Staged byte-for-byte.
- tests/expected/<id>.yaml — expectations for that fixture. Never staged; never on a subagent's path.
- tests/expected/SCHEMA.md — the expected-file schema, one field per line, with a worked example.
- tests/clearance_terms.txt — the clearance-language term list the scorer scans for, one substring per line.
- tests/harness/SUBAGENT_PROMPT.md — the fixed prompt every subagent receives. Not edited per fixture.
- tests/runs/<run-id>/ — one directory per recorded run, run-id = <YYYY-MM-DD>-<skill-commit>:
  - MANIFEST.md — date, SKILL.md commit hash, subagent model id, fixture count, N per fixture class, harness notes.
  - <fixture-id>.<k>.md — sample k of that fixture's output, verbatim and unedited.
  - RESULTS.md — written by the scorer.
- tests/.scratch/<id>/ — staging directory (git-ignored): a copy of skill/ plus content.md. Created by tools/stage_fixture.py.
- tools/stage_fixture.py <id> — stages one fixture; prints the scratch path.
- tools/score_run.py — scores a run directory against tests/expected/ and writes RESULTS.md (next step).

## Fixture IDs

- Entry fixtures: <catalog-ID>-<n>, e.g. GP-01-1. Every catalog entry has at least one.
- Adversarial fixtures: <category>-<nn>, e.g. CLR-01. Categories: CLR, VRQ, NOM, CUR, OVL, CNF, SCP, UNR (phase6-adversarial-categories).

## Samples

- Entry fixtures: N=1. Adversarial fixtures: N=3. A fixture passes only if every sample passes (phase6-pass-criteria).

## Staging rule

Only skill/ and the one content file are staged. tests/expected/ is never staged and never readable from a subagent's working directory (phase6-run-method).
