#!/usr/bin/env bash
set -euo pipefail

skill_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fixture_dir="$(mktemp -d "${TMPDIR:-/tmp}/code-review-tests.XXXXXX")"
trap 'rm -rf "$fixture_dir"' EXIT

mkdir -p "$fixture_dir/src"
printf '%s\n' 'function f(value: any) {' '  console.log(value) // TODO remove' '  try { run() } catch (e) {}' '}' > "$fixture_dir/src/example.ts"
PYTHONPYCACHEPREFIX="$fixture_dir/pycache" python3 -m py_compile "$skill_dir/scripts/code-review-signals.py"
python3 "$skill_dir/scripts/code-review-signals.py" "$fixture_dir" --json > "$fixture_dir/result.json"
python3 - "$fixture_dir/result.json" <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
ids = {x["rule"] for x in d["findings"]}
assert {"debug-artifact", "unfinished-marker", "typescript-any", "empty-handler"} <= ids, ids
PY
python3 - "$skill_dir" <<'PY'
import re, sys
from pathlib import Path
root = Path(sys.argv[1])
body = (root / "SKILL.md").read_text()
refs = re.findall(r"\]\((references/[^)]+)\)", body)
assert refs and not [x for x in refs if not (root / x).is_file()]
assert re.search(r"^name: code-review$", body, re.M)
PY
printf 'All code-review tests passed.\n'
