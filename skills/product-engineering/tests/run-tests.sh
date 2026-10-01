#!/usr/bin/env bash
set -euo pipefail
skill_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fixture_dir="$(mktemp -d "${TMPDIR:-/tmp}/product-engineering-tests.XXXXXX")"
trap 'rm -rf "$fixture_dir"' EXIT
printf 'baseline source\n' > "$fixture_dir/source.txt"
PYTHONPYCACHEPREFIX="$fixture_dir/pycache" python3 -m py_compile "$skill_dir/scripts/capture-baseline.py"
python3 "$skill_dir/scripts/capture-baseline.py" "$fixture_dir" --change CHG-001 --output "$fixture_dir/baseline.json" --include source.txt >/dev/null
python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); assert d["change"]=="CHG-001"; assert len(d["files"][0]["sha256"])==64' "$fixture_dir/baseline.json"
if python3 "$skill_dir/scripts/capture-baseline.py" "$fixture_dir" --change CHG-001 --output "$fixture_dir/baseline.json" >/dev/null 2>&1; then
  printf 'FAIL baseline overwrite guard\n' >&2
  exit 1
fi
python3 - "$skill_dir" <<'PY'
import re, sys
from pathlib import Path
root = Path(sys.argv[1]); body = (root / "SKILL.md").read_text()
refs = re.findall(r"\]\((references/[^)]+)\)", body)
assert refs and not [x for x in refs if not (root / x).is_file()]
assert re.search(r"^name: product-engineering$", body, re.M)
assert "revert" in body.lower() and "CHG-*" in body
PY
printf 'All product-engineering tests passed.\n'
