# Tests

Adversarial test set for skill/SKILL.md. Specification: RULINGS.md entries phase6-run-method, phase6-fixture-format, phase6-pass-criteria, phase6-adversarial-categories, repeated-pattern-single-flag.

## Layout

- tests/fixtures/<id>.md — content only, exactly what an advisor would paste. No frontmatter, no metadata, no fixture ID inside the file. Staged byte-for-byte.
- tests/expected/<id>.yaml — expectations for that fixture. Never staged; never on a subagent's path.
- tests/expected/SCHEMA.md — the expected-file schema, one field per line, with a worked example.
- tests/clearance_terms.txt — the clearance-language term list the scorer scans for, one substring per line.
- tests/harness/SUBAGENT_PROMPT.md — the fixed prompt every subagent receives. Not edited per fixture. Relative paths only: no repository path, no placeholder (run-isolation-sandbox).
- tests/harness/launch_sample.py <run-id> (<fixture-id> <k> | --all) — launches each subagent as a separate `claude -p` process whose working directory is the sample's staged directory, records the isolation evidence, and copies output.md to the sample's output path.
- tests/runs/<run-id>/ — one directory per recorded run, run-id = <YYYY-MM-DD>-<skill-commit>:
  - MANIFEST.md — date, SKILL.md commit hash, subagent model id, staging root, fixture count, N per fixture class, harness notes.
  - RUNLIST.tsv — fixture_id, k, scratch_path, output_path; written by prepare_run.py.
  - SUBAGENT_PROMPT.md — the prompt the run used, copied by prepare_run.py.
  - <fixture-id>.<k>.md — sample k of that fixture's output, verbatim and unedited.
  - <fixture-id>.<k>.ISOLATION.txt — isolation evidence recorded at launch (format below). Required by the scorer.
  - LAUNCH.log — one JSON line per launch: sample, cwd, exit status, turns, model reported, the subagent's reply. The reply is what the operator reads for CONTAMINATED.txt.
  - CONTAMINATED.txt — optional, manual: `fixture<TAB>k<TAB>what was read`, one line per sample the operator judged to have read outside its directory (run-isolation).
  - RESULTS.md — written by the scorer.
- tests/.scratch/<id>/ — single-fixture staging directory (git-ignored) for hand checks, created by tools/stage_fixture.py; recorded runs never stage inside the repository.
- tools/stage_fixture.py <id> — stages one fixture for a hand check; prints the scratch path.
- tools/isolation.py — the staging rule, the listing, and the ISOLATION.txt reader and writer shared by prepare_run.py, launch_sample.py and score_run.py.
- tools/score_run.py — scores a run directory against tests/expected/ and writes RESULTS.md (phase6-pass-criteria, phase6-majority-bar).
- tools/check_fixtures.py [--final] — validates the fixture set and coverage without running anything (phase6-fixture-format, phase6-adversarial-categories).
- tools/check_static.py — the static assertions: index drift (check-index-generator), paragraph-set/Pattern uniqueness (entries-to-checks), reference-file and index consistency (reference-file-shape), closing line and verified date, expected-file IDs.
- tools/prepare_run.py --model <id> --staging-root <dir> [--dry-run] — creates tests/runs/<run-id>/ with MANIFEST.md, RUNLIST.tsv and the prompt copy, and stages every sample outside the repository (phase6-run-method, run-isolation), verifying each staged directory holds only skill/ and content.md.

## Fixture IDs

- Entry fixtures: <catalog-ID>-<n>, e.g. GP-01-1. Every catalog entry has at least one.
- Adversarial fixtures: <category>-<nn>, e.g. CLR-01. Categories: CLR, VRQ, NOM, CUR, OVL, CNF, SCP, UNR (phase6-adversarial-categories).

## Samples

- Entry fixtures: N=1. Adversarial fixtures: N=3. A fixture passes only if every sample passes (phase6-pass-criteria).

## Staging rule

Only skill/ and the one content file are staged. tests/expected/ is never staged and never readable from a subagent's working directory (phase6-run-method). Staging is outside the repository (run-isolation), and isolation is structural (run-isolation-sandbox): each sample's staged directory, <staging-root>/<fixture-id>.<k>/, holds exactly skill/ and content.md with no symlinks; prepare_run.py verifies the listing after staging and refuses otherwise. The subagent runs as a separate process with that directory as its working directory, no repository path in its prompt, arguments or environment, and only the Read, Glob, Grep and Write tools, so a bare Glob resolves inside the sample and cannot reach the repository. CONTAMINATED.txt remains the manual channel for anything the listing does not catch.

## Isolation evidence

tests/harness/launch_sample.py writes tests/runs/<run-id>/<fixture-id>.<k>.ISOLATION.txt before the subagent starts:

```
sample: GP-01-1.1
cwd: /abs/staging-root/GP-01-1.1
launched: 2026-09-20T14:02:11Z
launcher: tests/harness/launch_sample.py
tools: Read,Glob,Grep,Write
model: sonnet
files:
content.md
skill/.gitkeep
skill/SKILL.md
skill/references/.gitkeep
skill/references/definitions.md
skill/references/general-prohibitions.md
skill/references/performance.md
skill/references/testimonials-endorsements.md
skill/references/third-party-ratings.md
```

`cwd` is `pwd -P` run inside the staged directory; every line after `files:` is one file path relative to it, POSIX separators, sorted; fields the scorer does not know are ignored. score_run.py refuses to score a sample whose evidence file is missing, whose `cwd` does not end in `<fixture-id>.<k>`, or whose listing carries any path other than content.md and paths under skill/ (or lacks either content.md or skill/SKILL.md); the sample fails with reason `isolation`, a hard check, and is not otherwise scored.
