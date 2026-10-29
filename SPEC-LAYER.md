# Spec layer for scaffolded projects — design note (2026-10-03)

The spec layer ships as the `scaffold-project` skill (in `skills/`). This
note records what was decided, where each piece came from, and what was
verified.

## What it is

A lean, gated spec layer for new projects:

- `docs/` holds numbered specs `NN-short-description.md` (creation order).
- Flat frontmatter: `description` (one sentence) + `status: proposed |
  accepted | active | superseded`; `superseded` requires
  `replacement: <existing doc>`.
- Canonical sections: `Problem`, `Design`, `Alternatives considered`
  (mandatory), `Acceptance criteria`, `Testing`, `Open questions`
  (proposed only; every question answered before the flip to `accepted`).
- The flip `accepted → active` is a **rewrite** (future → present), not a
  field change; proposal-era headings (`## Proposal`, `## Plan`) are banned
  in active/superseded docs.
- `docs/spec-lint.py` (stdlib-only Python) is part of the one-command gate:
  `<test command> && python3 docs/spec-lint.py`.
- `docs/README.md` (workflow: roles, status/flip/supersession rules) and
  `docs/00-project-overview.md` (guideline doc, frontmatter-exempt)
  complete the layer.

## Sources

- **DustToDominion** ([scorbo2/DustToDominion](https://github.com/scorbo2/DustToDominion))
  — the day-one shape: numbered flat specs, `description`/`status`
  frontmatter, `Configuration`/`Testing`/`Acceptance criteria` sections,
  `Open questions` that must close before the flip,
  human-owns-spec/agent-implements role split, spec-before-code and
  supersede-before-change workflow, and the "gate is the test suite"
  stance.
- **The author's agent-notes corpus** (2,000+ notes) — the rules adopted
  from the scaled end-state: mandatory `Alternatives considered`
  (anti-re-litigation), the flip-is-a-rewrite discipline (tense tells you
  authority), supersession discipline (superseded docs are history, never
  edited; the successor preserves unique rationale), and the growth path
  (lifecycle × class folders, supersession check, frozen archive).

## Decisions and why

| Decision | Why |
|---|---|
| Day one = the DustToDominion shape, no doc machinery beyond the lint | Ritual cost must stay below the value of recorded decisions; DustToDominion proves spec-first works with zero doc tooling. |
| Adopt mandatory `Alternatives considered` on day one | One section, high anti-re-litigation value, zero tooling. |
| Adopt the flip-is-a-rewrite | DustToDominion's `active` docs stay in spec voice ("may", "should include") — a gate can't read tense, so the flip must force it. |
| Keep the `Open questions` gate, add a lint proxy | "No list item ending in `?` in accepted/active/superseded" is the mechanical half of "all answered before the flip". |
| Lint is strict (status required, flat frontmatter, name pattern) | It is the *only* mechanical check on the spec layer; convention-only discipline is exactly DustToDominion's weak point. |
| `00-*.md` and `README.md` exempt | The overview is a guideline doc, not a spec (DustToDominion's own convention). |
| Growth path at ~15–20 in-flight specs or first mechanism collision | Below that the flat tree is browsable; the scaled structure earns its cost above it. |

## What was deliberately not adopted

- **i18n triplets** (EN/ZH/sidecar) — project-specific to the author's
  notes audience; an opt-in module, not a scaffold default.
- **Closed class taxonomy and lifecycle folders on day one** — that's the
  growth path, not the start.
- **Frozen archive + append-only manifest** — same reason; the day-one
  superseded-docs rule (keep, never edit, point via `replacement`) is the
  cheap version.
- **Per-note supersession ritual as a skill on day one** — a single
  "supersede before changing what a spec covers" line in `docs/README.md`
  suffices until the tree is big enough to search badly.

## Verification

- `fixtures/docs-clean` → exit 0 (3 specs checked, 0 violations).
- `fixtures/docs-bad` → exit 1, all 7 seeded violations caught (missing
  description, invalid status, superseded without replacement, ghost
  replacement, open question in active, `## Plan` in active, bad filename).
- missing docs dir → exit 2.
- `demo/`: gate green, first commit at green state.

## Open follow-ups (not blocking)

- Staleness of `proposed` specs is ungoverned on day one: a future lint
  could warn on proposed specs older than N days.
- Symbol-freshness for `active` specs (do the named files/symbols still
  exist?) is the natural next lint check — the same blind spot both source
  systems share, since truth isn't regex-checkable.

## Addendum (2026-10-08): the `accepted` status

The lifecycle gains an intermediate status: `proposed → accepted → active`
(`superseded` at any point after agreement). Found in a real project: a
design settled with the user and implemented in one session jumped
`proposed → active` in a single flip while the code didn't exist yet —
conflating design agreement with implementation done, and leaving the
implementing agent unsure whether to flip before or after writing the
code.

| Decision | Why |
|---|---|
| `accepted` = standing order for implementation: design settled with the human, open questions answered in place, future tense, must move to `active` (implemented) or `superseded` (abandoned) — no limbo | The old single flip conflated two different kinds of statement. Two flips, two triggers: agreement (a conversation event) and implementation done (a code event). |
| `proposed → accepted` is agreement, not a rewrite; `accepted → active` is the rewrite, only after implementation; `accepted` may keep proposal-era headings | An `active` spec is a record (present tense); an `accepted` spec is a contract (future tense). Tense tells the reader law from plan. |
| Lint: the open-question proxy extends to `accepted`; proposal-era headings stay banned only in `active`/`superseded` | The mechanical half of the same rule: standing orders are still future-tense. |
| Graduated folders: `proposed/` holds both `proposed` and `accepted`; no separate `accepted/` bucket (frontmatter `status` stays the source of truth) | `accepted` is transient by design; a folder is a stable home. |
| A `proposed` spec that dies before agreement is deleted (lean layer) or filed to `rejected/` (graduated structure); supersession requires agreement first | There is no decision to supersede before agreement. |
| Growth threshold counts in-flight specs (`proposed` + `accepted` + `active`), not only `status: active` | `accepted` is a real population; browseability is about the flat tree. |

Applied 2026-10-08 via anchored, anchor-validated edits to the skill's
`SKILL.md` and `references/spec-layer.md`; `tools/spec-lint.py` and
`templates/docs-readme-template.md` updated verbatim, `templates/spec-template.md`
via two anchored edits. Re-verified: all fixtures in this repo pass.
