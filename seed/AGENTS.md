# AGENTS.md — <project name>

## Session ritual

1. Read `PROJECT.md`.
2. Run the gate (below).
3. Do *Next*.
4. Update *Status* in `PROJECT.md`, keep the gate green, commit.

## Goal

<One paragraph: the goal.>
Non-goal: <what this project will not build.>

## Gate

    <test suite> && python3 docs/spec-lint.py

exit 0 = green. <Bootstrap steps if dependencies are needed; for a
docs-only project the lint is the gate.>

## Spec workflow

Specs live in `docs/` — see `docs/README.md` for the rules. Spec before
code; update or supersede a spec before changing what it covers.

## Definition of done

Gate green and the specs in `docs/` current with the code. Scope lives in
`docs/00-project-overview.md`, not here.

## Binding rules

- <The gotchas that must never be broken; each one earned.>

## File map

- `docs/00-project-overview.md` — goal/architecture/testing strategy (guideline doc).
- `docs/README.md` — spec workflow and rules.
- `docs/spec-lint.py` — the doc gate (stdlib Python, no deps).
- `docs/NN-*.md` — feature specs (status lifecycle in frontmatter).
- `PROJECT.md` — current state: status + next steps.
