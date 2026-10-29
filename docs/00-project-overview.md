# Spec-driven scaffold — overview

Guideline document (no frontmatter; the lint exempts `00-*.md`).

## Goal

Publish the spec-driven scaffold process so anyone can adopt it: a
self-contained process doc, a copy-ready seed, a worked demo, and an
installable agent skill.

## Architecture

A docs-only repo — the content is the artifact: `README.md` (landing
page), `PROCESS.md` (the process), `seed/` (a scaffold for a new project),
`demo/` (a small project built on the scaffold),
`skills/scaffold-project/` (the skill), `fixtures/` (lint test cases),
`SPEC-LAYER.md` (the design record), and `gate.sh` (this repo's gate).

## Testing strategy

The gate is `bash gate.sh`: it lints this repo's `docs/`, `demo/docs/`,
and `seed/docs/`, and asserts the fixture behavior (`docs-clean` exits 0,
`docs-bad` exits 1, a missing directory exits 2).
