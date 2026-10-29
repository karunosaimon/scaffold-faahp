#!/usr/bin/env python3
"""spec-lint.py — mechanical gate for the docs/ spec layer.

Checks every spec in a docs/ directory (default: ./docs relative to CWD):

  - filename: NN-short-description.md (creation-order number prefix)
  - frontmatter: flat single-line `key: value` pairs between leading `---`
  - description: present and non-empty (one-sentence summary)
  - status: present, one of proposed | accepted | active | superseded
  - replacement: required when status is superseded; must name an existing
    doc in the same directory
  - open questions: accepted/active/superseded specs may not carry an
    unanswered `## Open questions` item (proxy: no list item ending in `?`)
    — accepted means the design is settled (standing order to implement)
  - flip hygiene: active/superseded specs may not carry proposal-era
    headings (`## Proposal`, `## Plan`, `## Migration plan`) — accepted
    specs may keep them (standing orders are still future-tense)

Exempt: README.md (the workflow doc) and 00-*.md (overview/guideline docs).

Usage:  python3 spec-lint.py [docs-dir]
Exit:   0 all specs pass · 1 violations found · 2 usage or IO error

Stdlib only. If a project has no python3, port the six checks into the
project's language — the checks, not this implementation, are the contract.
"""
import re
import sys
from pathlib import Path

VALID_STATUS = ("proposed", "accepted", "active", "superseded")
EXEMPT_RE = re.compile(r"^(README\.md|00-.+\.md)$")
NAME_RE = re.compile(r"^\d{2,}-[a-z0-9][a-z0-9-]*\.md$")
PROPOSAL_HEADINGS = ("## Proposal", "## Plan", "## Migration plan")


def parse_frontmatter(lines):
    """Return (fields, error). Flat `key: value` pairs only."""
    fields = {}
    for i, line in enumerate(lines):
        if i == 0:
            if line.strip() != "---":
                return None, "missing frontmatter (file must start with ---)"
            continue
        if line.strip() == "---":
            return fields, None
        if not line.strip():
            continue
        if ":" not in line:
            return None, (
                "frontmatter line %d is not `key: value`: %r" % (i + 1, line.strip())
            )
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip("'\"")
    return None, "unterminated frontmatter (no closing ---)"


def open_question_lines(lines):
    """Yield line numbers of list items ending in '?' inside ## Open questions."""
    in_oq = False
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith("## "):
            in_oq = s == "## Open questions"
            continue
        if in_oq and s[:2] in ("- ", "* ") and s.endswith("?"):
            yield i


def lint_file(path, docs_dir, problems):
    name = path.name
    if not NAME_RE.match(name):
        problems.append("%s: filename must be NN-short-description.md" % name)
    lines = [l.rstrip("\r\n") for l in path.read_text(encoding="utf-8").splitlines()]
    fields, err = parse_frontmatter(lines)
    if err:
        problems.append("%s: %s" % (name, err))
        return
    if not fields.get("description", "").strip():
        problems.append("%s: frontmatter `description` missing or empty" % name)
    status = fields.get("status", "").strip()
    if not status:
        problems.append("%s: frontmatter `status` missing" % name)
    elif status not in VALID_STATUS:
        problems.append(
            "%s: status must be one of %s (got %r)" % (name, " | ".join(VALID_STATUS), status)
        )
    if status == "superseded":
        rep = fields.get("replacement", "").strip()
        if not rep:
            problems.append(
                "%s: status superseded requires `replacement: <doc name>`" % name
            )
        elif not (docs_dir / rep).exists():
            problems.append(
                "%s: replacement %r does not exist in %s/" % (name, rep, docs_dir.name)
            )
    if status in ("accepted", "active", "superseded"):
        for i in open_question_lines(lines):
            problems.append(
                "%s: line %d: unanswered Open question in a %s spec" % (name, i, status)
            )
    if status in ("active", "superseded"):
        for line in lines:
            s = line.strip()
            for h in PROPOSAL_HEADINGS:
                if s == h:
                    problems.append(
                        "%s: %s heading not allowed in a %s spec (the flip is a rewrite)"
                        % (name, h, status)
                    )
                    break


def main(argv):
    docs_dir = Path(argv[1]) if len(argv) > 1 else Path("docs")
    if not docs_dir.is_dir():
        print("spec-lint: %s/ not found (run from the repo root)" % docs_dir,
              file=sys.stderr)
        return 2
    problems = []
    checked = 0
    for path in sorted(docs_dir.glob("*.md")):
        if EXEMPT_RE.match(path.name):
            continue
        checked += 1
        lint_file(path, docs_dir, problems)
    for p in problems:
        print("spec-lint: %s" % p)
    print("spec-lint: %d spec(s) checked, %d violation(s)" % (checked, len(problems)))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
