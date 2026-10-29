# AGENTS.md — demo

Scaffolded per the `scaffold-project` skill: spec-layer demo (docs-only project).

## Session ritual

1. Read `PROJECT.md`.
2. Run the gate (below).
3. Do *Next*.
4. Update *Status* in `PROJECT.md`, keep the gate green, commit.

## Goal

Demonstrate the spec-driven scaffold: every feature is specified in `docs/`
before implementation, specs carry a `proposed → accepted → active`
lifecycle (`superseded` at any point after agreement), and a lint gate
keeps the mechanical contract honest.
Non-goal: any product code — the only artifact is the `docs/` layer.

## Gate

    python3 docs/spec-lint.py

exit 0 = green. Non-code project: the lint is the verification step. A
project with code would run its test suite first:
`<test suite> && python3 docs/spec-lint.py`.

## Spec workflow

Specs live in `docs/` — see `docs/README.md` for the full rules. Spec before
code; update or supersede a spec before changing what it covers.

## Definition of done

Gate green and the specs in `docs/` current with the (absent) code. Scope
lives in `docs/00-project-overview.md`, not here.

## Binding rules

- Never edit a `superseded` spec — supersede it.
- The flip `accepted → active` is a rewrite (future → present), not a
  frontmatter change.
- `docs/00-project-overview.md` has no frontmatter on purpose (exempt).

## File map

- `docs/00-project-overview.md` — goal/architecture/testing strategy (guideline doc).
- `docs/README.md` — spec workflow and rules.
- `docs/spec-lint.py` — the doc gate (stdlib Python, no deps).
- `docs/01-*.md` — feature specs (status lifecycle in frontmatter).
- `PROJECT.md` — current state: status + next steps.

## Skills

Load and follow a matching session skill (e.g. `scaffold-project` for
structural changes to the scaffold itself).
