#!/usr/bin/env bash
set -euo pipefail

skill_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fixture_dir="$(mktemp -d "${TMPDIR:-/tmp}/project-memory-tests.XXXXXX")"
trap 'rm -rf "$fixture_dir"' EXIT

printf '# Existing project instructions\n' > "$fixture_dir/CLAUDE.md"
printf 'Sample specification v1\n' > "$fixture_dir/spec.txt"
PYTHONPYCACHEPREFIX="$fixture_dir/pycache" python3 -m py_compile "$skill_dir/scripts/project-memory.py"
python3 "$skill_dir/scripts/project-memory.py" init "$fixture_dir" --project "Test Project" --link-claude >/dev/null
test -f "$fixture_dir/PROJECT_MEMORY.md"
grep -q '# Existing project instructions' "$fixture_dir/CLAUDE.md"
test "$(grep -c '@PROJECT_MEMORY.md' "$fixture_dir/CLAUDE.md")" -eq 1
python3 "$skill_dir/scripts/project-memory.py" validate "$fixture_dir/PROJECT_MEMORY.md" >/dev/null
test "$(python3 "$skill_dir/scripts/project-memory.py" next-id "$fixture_dir/PROJECT_MEMORY.md" DEC)" = "DEC-001"
python3 "$skill_dir/scripts/project-memory.py" fingerprint "$fixture_dir/spec.txt" | grep -Eq '^sha256=[0-9a-f]{64} size='
if python3 "$skill_dir/scripts/project-memory.py" init "$fixture_dir" --project "Overwrite" >/dev/null 2>&1; then
  printf 'FAIL memory overwrite guard\n' >&2
  exit 1
fi
python3 - "$skill_dir" <<'PY'
import re, sys
from pathlib import Path
root = Path(sys.argv[1])
body = (root / "SKILL.md").read_text()
refs = re.findall(r"\]\((references/[^)]+)\)", body)
assert refs and not [x for x in refs if not (root / x).is_file()]
assert re.search(r"^name: project-memory$", body, re.M)
PY
printf 'All project-memory tests passed.\n'
