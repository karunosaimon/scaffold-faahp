# The Spec Layer

The spec layer installed by the `scaffold-project` skill: what it is, the
file conventions, the lifecycle, the workflow, and the gate. Read this when
you need the full contract; `SKILL.md` carries the condensed steps.

Principle: **the spec is the contract between what is decided and what is
built; the gate is the spec's exit code.**

## The three layers

| File | Role | Changes |
|---|---|---|
| `AGENTS.md` | Stable guidance: goal, gate, binding rules, file map | rarely |
| `PROJECT.md` | State: status, next steps | every session |
| `docs/` | Spec layer: what is decided / will be built, and why | at decision time |

The spec layer is *separate from* state: `PROJECT.md` says where work is
now; `docs/` says what the work must be. A line that doesn't change between
sessions belongs in `AGENTS.md` or a spec, never in `PROJECT.md`.

## Layout and naming

```
docs/
  00-project-overview.md   # guideline doc (goal, architecture, testing
                           # strategy). No frontmatter. Lint-exempt.
  README.md                # workflow + rules for this project's docs/.
                           # Lint-exempt.
  spec-lint.py             # the doc gate (stdlib Python, no deps).
  NN-short-description.md  # specs, numbered by creation order.
```

- Numbers are **creation order**, not priority.
- Names: lowercase, hyphen-separated, briefly descriptive.
- Cross-references use relative markdown links — never bare prose.
- `00-*` and `README.md` are exempt from the lint by design: they are
  guideline/workflow docs, not specs.

## Frontmatter

Every spec starts with flat frontmatter, one `key: value` per line:

```yaml
---
description: One sentence: what this doc covers.
status: proposed
# replacement: 02-other-spec.md   # required iff status: superseded
---
```

- `description` — mandatory, one sentence, scannable without opening the
  file.
- `status` — mandatory: `proposed | accepted | active | superseded`.
- `replacement` — mandatory when `status: superseded`; must name an existing
  doc in `docs/`.
- Values containing a colon must be quoted.

## Sections

Every spec follows one skeleton; the section order is the contract both the
lint and the readers rely on:

| Section | Required | Rule |
|---|---|---|
| `## Problem` | yes | Motivation, written to stand without the solution. |
| `## Design` | yes | The change. Future/prescriptive while proposed or accepted; present-tense shipped reality once active. Free-form subsections allowed. |
| `## Alternatives considered` | yes | Each genuine alternative and why it lost — recorded, never invented. |
| `## Acceptance criteria` | yes | Specific, testable bullets that determine done. |
| `## Testing` | yes* | What the unit tests must cover. *Omit for non-code projects. |
| `## Open questions` | proposed; in accepted only fully answered | Every question answered (answer documented in place) before the flip to `accepted`. The section may stay, for reference. |

`Alternatives considered` is mandatory because a decision recorded without
what it beat invites re-litigation — and re-litigation is the failure the
spec layer exists to prevent.

## Workflow

- **New feature** — spec first, then code. The human owns the spec; the
  agent reviews the spec and implements.
- **Change to existing behavior** — update or supersede the relevant spec
  *before* adjusting the code.
- **Bug fix** — check whether any spec is affected. Trivial fixes may skip
  the spec; larger fixes amend it in the same change.

The spec must always be in sync with the code, unless it is explicitly
`superseded`. Sync is a **same-change** obligation: the code change and the
spec change land together.

## The lifecycle

```
proposed ──agreement──▶ accepted ──flip (rewrite)──▶ active
                              └──supersession──▶ superseded  (at any point after agreement)
```

- `proposed` — decided enough to plan, not yet implemented. May carry open
  questions.
- `accepted` — the design is settled with the human; a **standing order for
  implementation** — a future-tense contract, agreed but not yet in the
  code. No open questions. Must move: to `active` when implemented, to
  `superseded` when the design is abandoned — no limbo.
- `active` — implemented and current with the code.
- `superseded` — no longer current. Kept for history, **never edited**.
- A `proposed` spec that dies before agreement is deleted (lean layer) or
  filed to `rejected/` (graduated structure) — supersession requires
  agreement first.

### The flips

`proposed → accepted` — **agreement, not a rewrite**: the design is settled
with the human, every open question is answered in place, and the spec
becomes a standing order for implementation (still future tense).

`accepted → active` — **a rewrite, not a field change**, and the only flip
that happens once implementation is done. A `status: active` spec written in
future tense is a spec posing as a record — readers can't tell law from
plan. The flip changes the `status` line and:

1. Re-verifies every `## Open questions` item is answered (answer documented
   in place; the section may stay).
2. Rewrites the body in present-tense shipped reality — what was built, not
   what will be.
3. Drops proposal-era headings (`## Proposal`, `## Plan`, `## Migration
   plan`) and folds plans into what shipped.
4. States what now pins the behavior (e.g. `## Testing` in present tense).

The lint rejects the mechanical half (open questions, proposal-era
headings); the prose tense is on the author.

### Supersession

When a decision is replaced:

1. Write the new spec first — it becomes the owner of the decision.
2. The new spec **preserves every unique rationale, alternative, and
   consequence** from the old one. Consolidation is *into* the new doc, not
   away from history.
3. Mark the old spec `superseded` with `replacement: <new doc name>` in the
   same change.
4. Never edit a superseded spec; never edit an old spec *into* its opposite.

## The gate: spec-lint

`docs/spec-lint.py` — stdlib Python, no dependencies. Wire it into the
project gate:

```bash
<test suite> && python3 docs/spec-lint.py
```

(For non-code projects the lint *is* the verification step.)

| Check | Violation |
|---|---|
| filename | not `NN-short-description.md` |
| frontmatter | missing, unterminated, or not flat `key: value` |
| description | missing or empty |
| status | missing, or not one of `proposed \| accepted \| active \| superseded` |
| replacement | missing on superseded, or names a non-existent doc |
| open questions | list item ending in `?` inside `## Open questions` of an accepted/active/superseded spec |
| flip hygiene | `## Proposal` / `## Plan` / `## Migration plan` heading in an active/superseded spec |

Exit codes: `0` all pass · `1` violations (one per line) · `2` usage/IO.
Exempt: `README.md`, `00-*.md`.

The lint checks **well-formedness, not truth**: that an `active` spec
actually matches the code is the sync obligation above, and no gate can
verify it. That is the known, accepted blind spot of the design.

## Worked example

A docs-only scaffold (`demo/` in this repo; gate = the lint alone) shows
the full shape: `AGENTS.md` with the Gate and Spec workflow lines, `PROJECT.md` as
state, and `docs/` containing the overview, the workflow README, the lint,
and one `status: proposed` spec carrying an open question and an answered
one. Its first flip — agreement, answering the open question — takes it to
`accepted`; once implemented, the rewrite flip to `active` (`## Design` in
present-tense shipped reality) lands in the same change as the code.

## Growth path

The lean layer is the day-one default. Graduate to the scaled structure
when the flat tree stops being browseable — roughly **15–20 in-flight
specs** (`proposed` + `accepted` + `active`), or the first time two specs
fight over the same mechanism:

- lifecycle folders: `proposed/` `implemented/` `rejected/` `archived/` —
  `proposed/` holds both `proposed` and `accepted` specs; the frontmatter
  `status` stays the source of truth, and there is no separate `accepted/`
  bucket (a transient state doesn't earn a stable home)
- a closed classification per spec (`feature`, `architecture`, `process`, …)
- a supersession check on every new spec
- a frozen archive with an append-only manifest

A working reference implementation of the graduated structure is the
author's own agent-notes corpus (2,000+ notes, path-encoded lifecycle ×
class, format enforced by gates).
Graduation is a migration: move files, extend the lint, keep history —
don't rewrite it.

## Sources

- **DustToDominion** (scorbo2/DustToDominion) — the day-one shape: numbered
  specs, frontmatter status, the open-questions gate, the
  human-owns-spec/agent-implements split.
- **The author's agent-notes corpus** (2,000+ notes) — the scaled
  end-state: mandatory alternatives, flip-as-rewrite, supersession
  discipline, frozen archive.
- Design record with per-decision rationale: `SPEC-LAYER.md` at the root
  of this repo.
