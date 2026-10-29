# Demo project — overview

Guideline document (no frontmatter; the lint exempts `00-*.md`).

## Goal

Demonstrate the spec-driven scaffold: every feature is specified in `docs/`
before implementation; specs carry a `proposed → accepted → active`
lifecycle (`superseded` at any point after agreement); the lint gate keeps
the mechanical contract honest.

## Architecture

No code in this demo. The only artifact is the `docs/` layer: an overview
(this file), a workflow doc (`README.md`), the lint (`spec-lint.py`), and
feature specs named `NN-short-description.md`.

## Testing strategy

The gate is `python3 docs/spec-lint.py`. A project with code would run its
test suite first: `<test suite> && python3 docs/spec-lint.py`.
