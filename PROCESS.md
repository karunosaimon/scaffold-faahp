# The spec-driven process

This document is self-contained: it explains the process, why it works,
and how to adopt it. A worked example lives in `demo/`; a copy-ready
scaffold in `seed/`.

## The problem

Work with an agent — or across your own sessions — dies three ways:

1. **Context loss.** The conversation that settled a decision is gone; the
   next session re-derives it — or re-litigates it.
2. **Law/plan confusion.** A doc can no longer tell you what is decided
   versus what is planned.
3. **Silent drift.** Code and docs diverge, and nobody notices until
   something breaks.

The fix is a convention, not a tool: three files at the repo root with
sharply separated jobs, plus one gate command.

## The three layers

| File | Job | Changes |
|---|---|---|
| `AGENTS.md` | Stable guidance: goal, non-goals, gate, session ritual, binding rules, file map | rarely |
| `PROJECT.md` | State: current phase, last gate result, 1–3 concrete next steps | every session |
| `docs/` | The spec layer: what is decided, what will be built, and why | at decision time |

**Stable guidance and changing state live in separate files.** A line that
doesn't change between sessions belongs in `AGENTS.md` or a spec, never in
`PROJECT.md`. Status is a *command's exit code, not prose*: the gate
answers "is the current state good?" in one run.

`AGENTS.md` is plain markdown, no schema — any reader (human or agent)
gets the same hooks, and harnesses that auto-inject it make the ritual
structural, not conversational. Keep it lean and pointer-heavy.

## The session ritual

Every session, in order:

1. Read `PROJECT.md` (state), then `AGENTS.md` (guidance).
2. Run the gate. Red gate: fix before anything else.
3. Do *Next*.
4. Update *Status* in `PROJECT.md`, keep the gate green, commit
   (one-line messages).

Git from day one; commit at every green gate state.

## The spec layer

Specs live in `docs/`, named `NN-short-description.md` (number = creation
order). Each spec carries flat frontmatter:

```yaml
---
description: One sentence: what this doc covers.
status: proposed
# replacement: 02-other-spec.md   # required iff status: superseded
---
```

Canonical sections, in order: `Problem`, `Design`, `Alternatives
considered` (mandatory), `Acceptance criteria`, `Testing` (omit for
non-code projects), `Open questions` (while proposed).

`Alternatives considered` is mandatory because a decision recorded without
what it beat invites re-litigation — and re-litigation is the failure this
layer exists to prevent.

### The lifecycle

```
proposed ──agreement──▶ accepted ──flip (rewrite)──▶ active
                               └──supersession──▶ superseded
```

- **proposed** — not yet agreed; may carry open questions; every question
  must be answered in place before agreement.
- **accepted** — the design is settled with the human: a *standing order
  for implementation*. Future tense, no open questions, and no limbo: it
  must move to `active` (implemented) or `superseded` (abandoned).
- **active** — implemented and current with the code. Present tense.
- **superseded** — no longer current; points at its `replacement`; kept for
  history and **never edited**.

Two flips, two different triggers — that split is the whole point:

- `proposed → accepted` is **agreement, not a rewrite**: a conversation
  event. It settles the design and closes the open questions.
- `accepted → active` is **a rewrite, not a field change**: a code event,
  only after implementation. The body moves to present-tense shipped
  reality; proposal-era headings (`## Proposal`, `## Plan`) go. A
  `status: active` spec written in future tense is a spec posing as a
  record — readers can't tell law from plan.

When a decision is replaced, write the new spec first (it preserves every
unique rationale from the old one), then mark the old one `superseded` in
the same change. Never edit an old spec into its opposite.

### Sync rule

The spec must always be in sync with the code, unless it is explicitly
marked `superseded` — and sync is a *same-change* obligation: the code
change and the spec change land together.

### The gate

One quoted command in `AGENTS.md`; exit 0 = green. A project with code:

```
<test suite> && python3 docs/spec-lint.py
```

For non-code projects the lint *is* the verification step.
`docs/spec-lint.py` (stdlib Python, no dependencies) checks the
mechanical half of the contract: filename pattern, flat frontmatter,
`description`, valid `status`, `replacement` existence on superseded, no
unanswered open questions in accepted/active/superseded specs, no
proposal-era headings in active/superseded specs.

The lint checks **well-formedness, not truth** — that an `active` spec
matches the code is the sync rule, and no gate can verify it. That is the
known, accepted blind spot of the design.

## The growth path

Day one is deliberately lean: flat numbered docs, status frontmatter, a
lint in the gate. When the flat tree stops being browseable — roughly
15–20 in-flight specs, or the first time two specs fight over the same
mechanism — graduate to lifecycle folders (`proposed/` `implemented/`
`rejected/` `archived/`), a closed classification per spec, a supersession
check on every new spec, and a frozen archive with an append-only
manifest. Graduation is a migration: move files, extend the lint, keep
history — don't rewrite it.

## How to adopt

- **With an agent harness**: install the `scaffold-project` skill
  (`skills/scaffold-project/` in this repo) into your personal skills
  directory; the skill walks through the scaffold in a session.
- **By hand**: copy `seed/` into your repo root, fill in the
  placeholders, `git init`, first commit at green state. Ten minutes.

## What it deliberately doesn't do

- No doc tooling beyond the lint on day one — ritual cost must stay below
  the value of the recorded decisions.
- No enforcement of truth — the sync rule is a convention, kept honest by
  the same-change obligation and by the gate's existence.
- No classification folders, no archives, no extras until they earn their
  cost (the growth path).
