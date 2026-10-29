# Spec-Driven Scaffold

A spec-driven workflow for projects built by agents — or by hand: stable
guidance lives in `AGENTS.md`, changing state in `PROJECT.md`, and
decisions in a gated `docs/` spec layer. One command answers "is the
current state good?".

**Principle: the conversation is a scratchpad; the repo is memory.**

## Why

Chat context is lost; decisions should not be. Every session — human or
agent — starts from what the repo says, not from what someone remembered.
Decisions live in specs with an explicit lifecycle, and a lint gate keeps
the mechanical half of that contract honest.

## The process, in a minute

[PROCESS.md](PROCESS.md) is the self-contained explanation, written for a
first-time reader.

## What's in this repo

| Path | What it is |
|---|---|
| [PROCESS.md](PROCESS.md) | The process, self-contained: layers, lifecycle, flips, gate, adoption |
| [seed/](seed/) | A copy-ready scaffold for your own project (`AGENTS.md`, `PROJECT.md`, `docs/`) |
| [demo/](demo/) | A worked example: a small docs-only project, gate green |
| [skills/scaffold-project/](skills/scaffold-project/) | The installable skill for agent harnesses |
| [fixtures/](fixtures/) | Lint fixtures: `docs-clean` (passes) and `docs-bad` (7 seeded violations) |
| [SPEC-LAYER.md](SPEC-LAYER.md) | The design record: decisions and why |
| [gate.sh](gate.sh) | This repo's gate: one command, exit 0 = green |

## Quick start

- **You use an agent harness that auto-injects `AGENTS.md` and skills**:
  copy `skills/scaffold-project/` into your personal skills directory
  (e.g. `~/.agents/skills/`), then ask the agent to scaffold a project.
- **You work by hand**: copy the contents of `seed/` into your repo root,
  fill in the placeholders, `git init`, make the first commit at green
  state. Details in [seed/README.md](seed/README.md).

## Sources

The idea grew out of [DustToDominion](https://github.com/scorbo2/DustToDominion)
and the author's scaled agent-notes corpus; [SPEC-LAYER.md](SPEC-LAYER.md)
records what came from where and why.

## License

MIT — see [LICENSE](LICENSE).
