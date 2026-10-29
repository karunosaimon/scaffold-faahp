# AGENTS.md — scaffold-faahp

The public home of the spec-driven scaffold process; scaffolded per its
own standard (`skills/scaffold-project/`).

## Session ritual

1. Read `PROJECT.md`.
2. Run the gate (below).
3. Do *Next*.
4. Update *Status* in `PROJECT.md`, keep the gate green, commit.

## Goal

Make the spec-driven scaffold adoptable by anyone: one self-contained
process doc, one copy-ready seed, one worked demo, one installable skill.
Non-goal: a product, CI, packaging, or any code beyond the lint.

## Gate

    bash gate.sh

exit 0 = green. Checks this repo's `docs/`, `demo/docs/`, and
`seed/docs/`, plus the fixture exit codes (clean 0 · bad 1 · missing 2).

## Spec workflow

Specs live in `docs/` — see `docs/README.md` for the rules. Spec before
code; update or supersede a spec before changing what it covers.

## Definition of done

Gate green and the specs in `docs/` current with the repo's contents.
Scope lives in `docs/00-project-overview.md`, not here.

## Binding rules

- Personal paths, home directories, and internal project names never
  appear in repo files.
- The copies of `spec-lint.py` (`docs/`, `seed/`,
  `skills/scaffold-project/tools/`) stay byte-identical; change all three
  together.
- Never edit a `superseded` spec — supersede it.
- The flip `accepted → active` is a rewrite (future → present), not a
  frontmatter change.
- `seed/` carries no feature specs: don't invent specs for features that
  don't exist yet.

## File map

- `README.md` — landing page: pitch, layout, quick start, sources.
- `PROCESS.md` — the self-contained process document.
- `gate.sh` — the gate (lints `docs/`, `demo/docs/`, `seed/docs/`; asserts fixture exits).
- `docs/00-project-overview.md` — goal/architecture/testing strategy.
- `docs/README.md` — spec workflow and rules.
- `docs/spec-lint.py` — the doc gate (stdlib Python, no deps).
- `docs/01-public-release.md` — this release, as an active spec.
- `seed/` — copy-ready scaffold for a new project.
- `demo/` — worked example (docs-only project).
- `skills/scaffold-project/` — the installable skill.
- `fixtures/` — lint test fixtures.
- `SPEC-LAYER.md` — the design record (decisions and why).
- `LICENSE` — MIT.

## Skills

For structural changes to the scaffold, load and follow
`skills/scaffold-project/SKILL.md` (this repo's copy of the installable
skill).
