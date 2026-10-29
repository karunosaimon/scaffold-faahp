---
description: A `demo greet` command that prints a configurable greeting.
status: proposed
---

# Greeting command

## Problem

The demo has no feature yet; the scaffold needs one concrete spec to exercise
the proposed → active lifecycle end to end.

## Design

A `demo greet [--name NAME]` command prints `Hello, <name>!` (default name
`world`). The greeting prefix is a constant in code, not configuration.

## Alternatives considered

**A full templating engine for greetings.** Rejected: overkill for one
string; a constant keeps the acceptance criteria trivially testable.

**Make the greeting configurable.** Rejected: configuration machinery is not
justified by a single constant.

## Acceptance criteria

- `demo greet` prints `Hello, world!` and exits 0.
- `demo greet --name Ada` prints `Hello, Ada!`.
- Both behaviors are covered by unit tests.

## Testing

- Greeting default and override cases.
- Exit-code assertions.

## Open questions

- Should unknown flags fail with exit 2?
- Should `--name` accept an empty string? — yes: an empty name prints
  `Hello, !` (decided during spec review; matches flag semantics).
