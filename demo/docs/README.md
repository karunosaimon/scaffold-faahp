# Docs

Architecture docs and specifications for this project. This is a
**spec-driven project**: specs gate the code.

## Workflow

- **New feature**: spec first (`NN-short-description.md`, numbered by
  creation order), then code. The human owns the spec; the agent reviews and
  implements.
- **Change to existing behavior**: update or supersede the relevant spec
  *before* adjusting the code.
- **Bug fix**: check whether any spec is affected. Trivial fixes may skip
  the spec; larger fixes amend it in the same change.

The spec must always be in sync with the code, unless explicitly marked
`superseded`.

## Status and flip rules

Every spec carries flat frontmatter: `description` (one sentence) and
`status: proposed | accepted | active | superseded`.

The lifecycle is `proposed → accepted → active` (or `superseded` at any
point after agreement). Each status is a different kind of statement:

- **`proposed`** — not yet agreed. May carry an `## Open questions`
  section; **every question must be answered before the flip to
  `accepted`**. Written as a proposal: what we might build and why.
- **`accepted`** — the design is settled with the human and the spec is a
  **standing order for implementation**: a future-tense contract, agreed but
  not yet in the code. No open questions. An accepted spec must move — to
  `active` when implemented, or to `superseded` when the design is
  abandoned; it must not sit in limbo.
- **`active`** — implemented and current with the code (present tense). The
  flip from `accepted` is a **rewrite, not a field change**: the body moves
  to present-tense shipped reality and proposal-era headings (`## Proposal`,
  `## Plan`, `## Migration plan`) must go.
- **`superseded`** — no longer current. Set `replacement: <doc name>` (an
  existing doc). Superseded docs are kept for history and never edited; the
  superseding spec preserves every unique rationale from it.

`docs/spec-lint.py` enforces the mechanical part of this contract and is
part of the project gate.
