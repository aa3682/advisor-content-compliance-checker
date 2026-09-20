# Expected-file schema

One YAML file per fixture at tests/expected/<id>.yaml. Spec: phase6-fixture-format; assertions: phase6-pass-criteria. Catalog IDs are read only from the named fields below, never by regex over fixture IDs or prose. The scorer requires PyYAML and fails loudly with the install command if it is absent.

## Fields

- id — string, required. Equals the file's basename. Consumed by: run/fixture matching.
- category — string, required. `entry` for entry fixtures; the category code (CLR, VRQ, NOM, CUR, OVL, CNF, SCP, UNR) for adversarial fixtures. Consumed by: N per fixture class; RESULTS.md grouping.
- targets — list of catalog IDs, required. The entries the fixture was built from. Consumed by: RESULTS.md only; not an assertion.
- elements — list of term names, required. The exact set the Elements detected line must list, drawn from: testimonial, endorsement, third-party rating, gross performance, net performance, hypothetical performance. An empty list means the line must read `none`. Consumed by: per-fixture assertion, elements exact set match.
- required — list, required (may be empty). Each item is a catalog ID string, or a mapping with `id` (catalog ID) and optional `where`: a substring or a list of substrings, and the flag passes when its Where line contains any one (where-anyof). Each anchor is at most 60 characters and as short as remains distinctive. Omission-type entries (a missing statement, a stale date, a wrong basis) carry no where. Consumed by: per-fixture assertion, every required ID present and on one of its where anchors when given.
- forbidden — list of catalog IDs, optional. Must appear neither as a flag nor under Would apply. Consumed by: per-fixture assertion, no forbidden ID.
- confirm — list, optional. Each item is a mapping with `would_apply` (list of catalog IDs, scored exactly). `where` and `depends_on` may be present as documentation; they are not scored strictly. Consumed by: per-fixture assertion, each would_apply matched.
- scope — string or null, optional (default null). The marker the Scope line must name, or null when no Scope line is expected. Consumed by: per-fixture assertion, Scope line present exactly when expected.
- not_reviewed — string or null, optional (default null). The image or attachment the Not reviewed line must name, or null when no Not reviewed line is expected. Consumed by: per-fixture assertion, Not reviewed line present exactly when expected.
- no_match — boolean, optional (default false). True when `Flags: 0`, `Confirm: 0` and the Zero flags line ("Zero flags is not a clearance — the catalog covers documented failures only.") are expected; never true alongside a `confirm` expectation (zero-flags-line-scope). Consumed by: per-fixture assertion, Zero-flags line present exactly when expected.

Most files carry only id, category, targets, elements, required.

Flags or Would apply IDs beyond `required` and not in `forbidden` pass when they are valid catalog IDs and are listed as extras in RESULTS.md.

## Example: tests/expected/GP-01-1.yaml

```yaml
id: GP-01-1
category: entry
targets: [GP-01]
elements: []
required:
  - id: GP-01
    where: "completely free of conflicts of interest"
```
