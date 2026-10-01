#!/usr/bin/env bash
set -euo pipefail

skill_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fixture_dir="$(mktemp -d "${TMPDIR:-/tmp}/iwd-tests.XXXXXX")"
trap 'rm -rf "$fixture_dir"' EXIT

pass() { printf 'PASS %s\n' "$1"; }
fail() { printf 'FAIL %s\n' "$1" >&2; exit 1; }

bash -n "$skill_dir/scripts/project-inventory.sh"
bash -n "$skill_dir/scripts/ui-signals.sh"
bash -n "$skill_dir/scripts/package-plugin.sh"
PYTHONPYCACHEPREFIX="$fixture_dir/pycache" python3 -m py_compile "$skill_dir/scripts/design-audit.py" "$skill_dir/scripts/build-comparison-board.py"
node --check "$skill_dir/scripts/generate-threejs.mjs"
node --check "$skill_dir/assets/live-inspector.js"
pass 'script syntax'

node "$skill_dir/scripts/generate-threejs.mjs" "$skill_dir/assets/three-spec.example.json" "$fixture_dir/model.generated.js" >/dev/null
node --check "$fixture_dir/model.generated.js"
grep -q 'createProceduralScene' "$fixture_dir/model.generated.js" || fail 'generated scene API missing'
if node "$skill_dir/scripts/generate-threejs.mjs" "$skill_dir/assets/three-spec.example.json" "$fixture_dir/model.generated.js" >/dev/null 2>&1; then
  fail 'generator overwrote an existing file without --force'
fi
pass 'procedural generator and overwrite guard'

mkdir -p "$fixture_dir/web"
printf '%s\n' '.hero { min-height: 100vh; transition: all 200ms; outline: none; animation: pulse 1s infinite; }' > "$fixture_dir/web/styles.css"
printf '%s\n' '<img src="hero.png"><div onClick={() => go()}>Everything you need</div>' > "$fixture_dir/web/Hero.tsx"
python3 "$skill_dir/scripts/design-audit.py" "$fixture_dir/web" --json > "$fixture_dir/audit.json"
python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); ids={x["rule"] for x in d["findings"]}; required={"a11y-outline-removed","motion-transition-all","motion-reduced-missing","a11y-image-alt","copy-generic-claim"}; missing=required-ids; assert not missing, missing' "$fixture_dir/audit.json"
pass 'deterministic audit rules'

printf '%s' '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="30"><rect width="40" height="30" fill="#fff"/><circle cx="20" cy="15" r="8" fill="#c50"/></svg>' > "$fixture_dir/reference.svg"
printf '%s' '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="30"><rect width="40" height="30" fill="#fff"/><circle cx="21" cy="15" r="7" fill="#b40"/></svg>' > "$fixture_dir/render.svg"
python3 "$skill_dir/scripts/build-comparison-board.py" --reference "$fixture_dir/reference.svg" --render "$fixture_dir/render.svg" --output "$fixture_dir/compare.html" >/dev/null
grep -q 'Difference map' "$fixture_dir/compare.html" || fail 'comparison board missing controls'
pass 'self-contained comparison board'

python3 - "$skill_dir" <<'PY'
import re, sys
from pathlib import Path
root = Path(sys.argv[1])
body = (root / "SKILL.md").read_text()
references = re.findall(r"\]\((references/[^)]+)\)", body)
missing = [item for item in references if not (root / item).is_file()]
assert not missing, missing
assert body.startswith("---\n")
assert re.search(r"^name: immersive-web-designer$", body, re.M)
PY
pass 'skill frontmatter and references'

"$skill_dir/scripts/package-plugin.sh" "$fixture_dir/plugin" >/dev/null
python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); assert d["name"]=="web-engineering-studio"; assert d["version"]=="4.0.1"' "$fixture_dir/plugin/.claude-plugin/plugin.json"
python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); assert d["author"]["name"]=="SIELINOU GAMENI Sylvain Junior"' "$fixture_dir/plugin/.claude-plugin/plugin.json"
for document in README.md INSTALL.md ATTRIBUTIONS.md; do
  test -f "$fixture_dir/plugin/$document" || fail "packaged document missing: $document"
done
for packaged_skill in project-memory product-engineering immersive-web-designer code-review security-review qa-engineering release-engineering; do
  test -f "$fixture_dir/plugin/skills/$packaged_skill/SKILL.md" || fail "packaged skill missing: $packaged_skill"
done
test -f "$fixture_dir/plugin/evals/create-proposal/prompt.md" || fail 'packaged eval suite missing'
test -f "$fixture_dir/plugin/evals/code-review-plan/prompt.md" || fail 'packaged code-review eval missing'
test -f "$fixture_dir/plugin/evals/security-scope-first/prompt.md" || fail 'packaged security-review eval missing'
test -f "$fixture_dir/plugin/evals/brief-routing/prompt.md" || fail 'packaged project-memory eval missing'
test -f "$fixture_dir/plugin/evals/build-feature/prompt.md" || fail 'packaged product-engineering eval missing'
test -f "$fixture_dir/plugin/evals/acceptance-gate/prompt.md" || fail 'packaged qa-engineering eval missing'
test -f "$fixture_dir/plugin/evals/release-plan/prompt.md" || fail 'packaged release-engineering eval missing'
test ! -d "$fixture_dir/plugin/skills/immersive-web-designer/plugin-evals" || fail 'eval suite duplicated inside packaged skill'
python3 - "$fixture_dir/plugin/evals" <<'PY'
import sys
from pathlib import Path
root = Path(sys.argv[1])
prompts = list(root.glob("*/prompt.md"))
assert prompts, "no eval prompts"
for path in prompts:
    body = path.read_text()
    assert body.startswith("---\n"), path
    for key in ("max_turns:", "timeout_seconds:", "allowed_tools:"):
        assert key in body.split("---", 2)[1], (path, key)
graders = list(root.glob("*/graders/*.md"))
assert graders, "no eval graders"
for path in graders:
    body = path.read_text()
    assert body.startswith("---\n") and "type:" in body.split("---", 2)[1], path
assert not list(root.glob("*/graders/*.json")), "legacy JSON grader found"
PY
pass 'Claude Code plugin package'

"$skill_dir/../code-review/tests/run-tests.sh"
"$skill_dir/../security-review/tests/run-tests.sh"
"$skill_dir/../project-memory/tests/run-tests.sh"
"$skill_dir/../product-engineering/tests/run-tests.sh"
"$skill_dir/../qa-engineering/tests/run-tests.sh"
"$skill_dir/../release-engineering/tests/run-tests.sh"
pass 'companion skills'

printf 'All immersive-web-designer tests passed.\n'
