---
name: scaffold-project
description: "Bootstrap a new project following the AGENTS.md standard: guidance in AGENTS.md, state in PROJECT.md, spec-driven docs/ with a lint gate, git from day one."
whenToUse: When starting a new project, or when asked to "set up the project structure" or "scaffold" a project for agent work.
---

# Scaffold a project for agent work (AGENTS.md standard)

Give the agent strong hooks on goal and current status from the first commit.
Principle: **the conversation is a scratchpad; the repo is memory.**

Full reference for the spec layer (layout, lifecycle, the flip,
supersession, lint spec, worked example): `references/spec-layer.md`.

## Principles

- **Stable guidance and changing state live in separate files.**
  `AGENTS.md` (the cross-harness standard) holds what rarely changes;
  `PROJECT.md` holds what changes every session.
- Status is a **command's exit code, not prose**: one gate command answers
  "is the current state good?".
- **The spec layer is its own gated layer** (`docs/`): spec before code;
  each spec carries a `status` lifecycle (`proposed | accepted | active |
  superseded`); `accepted` is a standing order for implementation (design
  settled, no open questions), and the flip `accepted → active` — only after
  implementation — is a *rewrite* (future → present), not a field change.
  Day one is lean (flat numbered docs + a stdlib lint in the gate); at
  scale, graduate to the lifecycle/class/archive structure — see Growth
  path.
- Git from day one; commit at every green gate state (one-line messages).
- Every line in both files is a fact with evidence or an instruction —
  no narrative.
- `AGENTS.md` is plain markdown, no schema: any tool that reads it gets the
  same hooks, and harnesses that auto-inject it (several do — including
  nested per-directory files with scope) make the ritual structural, not
  conversational. Keep it lean (byte budgets exist) and pointer-heavy.
- **Layer 1 is harness-managed, not scaffolded.** The harness's user-global `AGENTS.md`
  (auto-loaded into every session of every workspace) carries
  deployment facts and standing personal habits; a new project's `AGENTS.md`
  must not copy that content — only project-specific content. Cross-project
  procedures live in personal skills (`~/.agents/skills/`), referenced, not
  inlined.

## Steps

1. Ask for: a one-paragraph goal + non-goals; what "done" looks like; whether
   a testable artifact exists (code, doc, data).
2. Create `AGENTS.md` at the root with these sections:
   - **Session ritual** (numbered): read `PROJECT.md` → run the gate → do
     *Next* → update *Status*, keep the gate green, commit.
   - **Goal** + non-goals (one paragraph).
   - **Gate** — one quoted command, exit 0 = green; fresh-clone bootstrap
     steps if dependencies are needed. Includes the spec lint (step 4).
   - **Spec workflow** — one line: specs live in `docs/` (rules in
     `docs/README.md`); spec before code, supersede before changing what a
     spec covers.
   - **Definition of done** — pointers to spec + gate, not copies.
   - **Binding rules** — the gotchas that must never be broken (each earned).
   - **File map** — path → one-line purpose.
   - **Skills** (optional) — if project skills exist: "load and follow a
     matching session skill".
3. Create `PROJECT.md` — **state only**: one-line pointer to `AGENTS.md`,
   then *Status* (phase, last gate result with date) and *Next* (1–3 concrete
   steps). No guidance, no commands — those belong in `AGENTS.md`.
4. Create the spec layer under `docs/` (paths relative to this skill's base
   directory): `docs/00-project-overview.md` (goal, architecture, testing
   strategy — guideline doc, no frontmatter, lint-exempt); `docs/README.md`
   (copy `templates/docs-readme-template.md`, adapt); `docs/spec-lint.py`
   (copy `tools/spec-lint.py` — stdlib only, no deps). If a first feature is
   known, add its spec from `templates/spec-template.md`
   (`NN-short-description.md`, status `proposed`); don't invent specs for
   features that don't exist yet. Wire the lint into the gate:
   `<test command> && python3 docs/spec-lint.py` (for non-code projects the
   lint *is* the verification step).
5. (Optional) Nested `AGENTS.md` in footgun directories (build/test/vendor):
   rules that only apply there — generated files, pinned tool versions,
   gitignored outputs. More specific files take precedence in harnesses that
   support nesting.
6. Add `.gitignore` for generated artifacts. First measure what is bulky
   (`du -sh`); **no inline comments in `.gitignore`** — text after a pattern
   becomes part of the pattern.
7. `git init`; if no identity is configured, set a repo-local placeholder and
   tell the user they can override it; make the first commit at green state.
8. Verify: `git ls-files` (right set tracked), `git check-ignore -v` on every
   ignore pattern, `git status` clean, `.git` size sane (a 300 MB `.git` in a
   text project means binaries leaked in).
9. Offer project-scoped skills under `.agents/skills/` (one directory per
   task, `SKILL.md` with `name`/`description`/`whenToUse` frontmatter) for
   focused recurring procedures — e.g. a spec-review skill. Keep skill bodies
   harness-agnostic (plain markdown + portable commands) so they survive a
   tool switch; the frontmatter schema is the harness-specific part. Front
   matter is strict YAML: quote any value containing a colon — unquoted, it
   fails to parse and the skill silently drops from the catalog.

## Growth path (when docs/ outgrows the lean layer)

The lean layer (flat numbered docs, status frontmatter, lint in the gate) is
the day-one default. Graduate to the scaled structure when the flat tree
stops being browseable — roughly 15–20 in-flight specs (`proposed` +
`accepted` + `active`), or the first time two specs fight over the same
mechanism: lifecycle folders (`proposed/` `implemented/` `rejected/`
`archived/` — `proposed/` holds both `proposed` and `accepted` specs; no
separate `accepted/` bucket), a closed classification per spec, a
supersession check on every new note, and a frozen archive with an
append-only manifest. A working reference implementation of the graduated
structure is the author's own agent-notes corpus (2,000+ notes, path-encoded
lifecycle × class, format enforced by gates). Graduation is a migration:
extend the lint, keep history — don't rewrite it.

## Gotchas (learned the expensive way)

- `.gitignore` inline comments silently break the pattern → verify with
  `git check-ignore -v`.
- To untrack binaries from a first commit: `git rm -r --cached …`,
  `git commit --amend`, `git reflog expire --expire=now --all`,
  `git gc --prune=now` (amend alone leaves the blobs in `.git`).
- Whitespace conventions can vary **per region within one file** (e.g. nested
  list continuations). Record the measured convention in AGENTS.md's binding
  rules and instruct: measure with a command before editing; anchor mid-line;
  use python heredocs for multi-line replacements.
- Never embed commit hashes in the status file (self-reference problem);
  `git log` is the hash source of truth.
- **Don't let `PROJECT.md` drift back into guidance**: if a line doesn't
  change between sessions, it belongs in `AGENTS.md`. The split is what keeps
  the always-loaded file stable and the state file short.
- For non-code projects the "gate" is a verification script (checklist
  runner, doc lint, data validation) — the pattern is the same: one command,
  exit code.
- **The flip is a rewrite, not a field change.** A `status: active` spec
  written in future/prescriptive tense is a spec posing as a record — readers
  can't tell law from plan. Agreement (`proposed → accepted`) settles the
  design and answers open questions without rewriting; the flip
  (`accepted → active`) happens only when the implementation is done: drop
  proposal-era headings, rewrite the body in present-tense shipped reality.
- Superseded specs are kept for history and never edited; the superseding
  spec must preserve every unique rationale from the old one. Never edit an
  old spec into its opposite — supersede it.
- Spec frontmatter is flat one-line `key: value`; quote values containing a
  colon (same strictness as skill frontmatter). The lint is strict on
  purpose: it is the only mechanical check on the spec layer.
- `docs/` rots two ways: specs that drift from the code, and superseded
  specs piling up. The first is the sync rule (spec updated in the same
  change as the code); the second is what the Growth path archive is for.
