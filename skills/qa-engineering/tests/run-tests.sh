#!/usr/bin/env bash
set -euo pipefail
skill_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fixture_dir="$(mktemp -d "${TMPDIR:-/tmp}/qa-engineering-tests.XXXXXX")"
trap 'rm -rf "$fixture_dir"' EXIT
PYTHONPYCACHEPREFIX="$fixture_dir/pycache" python3 -m py_compile "$skill_dir/scripts/delivery-readiness.py"
printf '%s\n' \
  '## Exigences et critères d’acceptation' \
  '| ID | Exigence | Priorité | Critère observable | Source | Statut |' \
  '|---|---|---|---|---|---|' \
  '| REQ-001 | Works | haute | observable | SRC-001 | confirmed |' \
  '## Matrice de traçabilité' \
  '| Exigence | Changement | Test/preuve | Résultat | Risque/validation |' \
  '|---|---|---|---|---|' \
  '| `REQ-001` | CHG-001 | TST-001 | pass | VAL-001 |' \
  '## Risques' \
  '| ID | Risque | Probabilité/impact | Réponse | Propriétaire | Source | Statut |' \
  '|---|---|---|---|---|---|---|' \
  '## Releases et incidents' \
  '| ID | Date | Version/environnement | Changements | Résultat | Rollback/risque | Statut |' \
  '|---|---|---|---|---|---|---|' \
  '## Definition of Done' \
  '- Exigences et traçabilité : pass' \
  '- Implémentation : complete' \
  '- Validation finale : accepted-risk' > "$fixture_dir/ready.md"
python3 "$skill_dir/scripts/delivery-readiness.py" "$fixture_dir/ready.md" --json > "$fixture_dir/result.json"
python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); assert d["ready"] is True' "$fixture_dir/result.json"
if python3 "$skill_dir/scripts/delivery-readiness.py" "$fixture_dir/ready.md" --require-release >/dev/null 2>&1; then
  printf 'FAIL readiness accepted missing release\n' >&2
  exit 1
fi
python3 - "$skill_dir" <<'PY'
import re, sys
from pathlib import Path
root = Path(sys.argv[1]); body = (root / "SKILL.md").read_text()
refs = re.findall(r"\]\((references/[^)]+)\)", body)
assert refs and not [x for x in refs if not (root / x).is_file()]
assert re.search(r"^name: qa-engineering$", body, re.M)
assert all(x in body for x in ("PASS", "CONDITIONAL", "FAIL", "BLOCKED"))
PY
printf 'All qa-engineering tests passed.\n'
