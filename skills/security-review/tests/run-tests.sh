#!/usr/bin/env bash
set -euo pipefail

skill_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fixture_dir="$(mktemp -d "${TMPDIR:-/tmp}/security-review-tests.XXXXXX")"
trap 'rm -rf "$fixture_dir"' EXIT

mkdir -p "$fixture_dir/src"
printf '%s\n' 'const apiKey = "super-secret-value";' 'el.innerHTML = input;' 'process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";' > "$fixture_dir/src/example.js"
PYTHONPYCACHEPREFIX="$fixture_dir/pycache" python3 -m py_compile "$skill_dir/scripts/security-signals.py"
python3 "$skill_dir/scripts/security-signals.py" "$fixture_dir" --json > "$fixture_dir/result.json"
if grep -q 'super-secret-value' "$fixture_dir/result.json"; then
  printf 'FAIL secret leaked in report\n' >&2
  exit 1
fi
python3 - "$fixture_dir/result.json" <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
ids = {x["rule"] for x in d["findings"]}
assert {"possible-secret", "unsafe-html", "tls-verification-disabled"} <= ids, ids
PY
python3 - "$skill_dir" <<'PY'
import re, sys
from pathlib import Path
root = Path(sys.argv[1])
body = (root / "SKILL.md").read_text()
refs = re.findall(r"\]\((references/[^)]+)\)", body)
assert refs and not [x for x in refs if not (root / x).is_file()]
assert re.search(r"^name: security-review$", body, re.M)
PY
printf 'All security-review tests passed.\n'
