# Seed

A copy-ready scaffold for a new project, following the spec-driven
process ([../PROCESS.md](../PROCESS.md)).

## Use

1. Copy this directory's contents (except this README) into your repo
   root: `AGENTS.md`, `PROJECT.md`, `.gitignore`, `docs/`, and
   `spec-template.md`.
2. Copy `spec-template.md` into `docs/` as `NN-short-description.md` for
   your first known feature — or delete it if you don't have one yet
   (a seed ships no feature specs).
3. Fill in the `<...>` placeholders in `AGENTS.md` and `PROJECT.md`.
4. `git init`; make the first commit at green gate state.

The `docs/` layer is complete as-is: `docs/README.md` (workflow rules),
`docs/00-project-overview.md` (fill in goal/architecture/testing),
`docs/spec-lint.py` (the gate; stdlib Python, no dependencies). A project
with code wires the gate as `<test suite> && python3 docs/spec-lint.py`;
a docs-only project uses the lint alone.
