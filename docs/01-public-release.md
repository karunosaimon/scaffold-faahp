---
description: The public release of the spec-driven scaffold in this repo.
status: active
---

# Public release

## Problem

The spec-driven scaffold process existed as a personal skill, an internal
design note, and a demo — three artifacts no outsider could read or
adopt in one sitting.

## Design

This repo is the public home of the process. At the root it contains:

- `README.md` — the landing page: pitch, layout, quick start, sources.
- `PROCESS.md` — the self-contained process document for a first-time
  reader.
- `seed/` — a copy-ready scaffold (`AGENTS.md`, `PROJECT.md`, `docs/`
  with the lint); no feature specs.
- `demo/` — a worked example: a docs-only project, gate green.
- `skills/scaffold-project/` — the installable skill (`SKILL.md`,
  reference, templates, lint).
- `fixtures/` — `docs-clean` (all pass) and `docs-bad` (seven seeded
  violations) for the lint.
- `gate.sh` — the repo gate: lints `docs/`, `demo/docs/`, `seed/docs/`,
  and asserts the fixture exit codes.
- `SPEC-LAYER.md` — the design record, sanitized for public reading.

The repo dogfoods its own standard: this file is an `active` spec written
in present tense, and the gate is one command (`bash gate.sh`, exit 0 =
green).

## Alternatives considered

**An internal doc only (the design note).** Rejected: it records
provenance and session history, not a first-time reader's explanation,
and it carried internal paths.

**A single skill without docs.** Rejected: the skill is pointer-heavy and
agent-oriented; a human with no agent setup gets no entry point.

**Publishing the design note verbatim.** Rejected: it contained home
directories, internal project names, and session-script details.

## Acceptance criteria

- A first-time reader can adopt the process from `PROCESS.md` + `seed/`
  alone.
- `bash gate.sh` exits 0.
- No file in the repo contains a personal path or an internal project
  name.
- The `seed/` and `skills/` copies of the lint are byte-identical to
  `docs/spec-lint.py`.

## Testing

- `fixtures/docs-clean` → exit 0; `fixtures/docs-bad` → exit 1; missing
  directory → exit 2. All three asserted by `gate.sh`.
