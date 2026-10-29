#!/usr/bin/env bash
# The gate for this repo: one command answers "is the current state good?"
# Exit 0 = green.
#
# Checks: the repo's own docs/, demo/docs/, and seed/docs/ all pass the
# spec lint, and the fixtures behave as documented (docs-clean exits 0,
# docs-bad exits 1, a missing directory exits 2).

cd "$(dirname "$0")" || exit 2
fail=0

check() {
  dir=$1; want=$2
  python3 docs/spec-lint.py "$dir" >/dev/null 2>&1
  got=$?
  if [ "$got" -ne "$want" ]; then
    echo "gate: spec-lint on $dir: expected exit $want, got $got"
    fail=1
  fi
}

check docs 0
check demo/docs 0
check seed/docs 0
check fixtures/docs-clean 0
check fixtures/docs-bad 1
check fixtures/no-such-dir 2

if [ "$fail" -eq 0 ]; then
  echo "gate: green"
fi
exit $fail
