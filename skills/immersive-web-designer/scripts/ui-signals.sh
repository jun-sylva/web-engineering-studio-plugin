#!/usr/bin/env bash
set -u

project_root="${1:-.}"
skill_script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ ! -d "$project_root" ]]; then
  printf 'ERROR: project directory not found: %s\n' "$project_root" >&2
  exit 2
fi

if ! command -v rg >/dev/null 2>&1; then
  printf 'ERROR: rg is required for this read-only signal scan\n' >&2
  exit 2
fi

cd "$project_root" || exit 2

if command -v python3 >/dev/null 2>&1 && [[ -f "$skill_script_dir/design-audit.py" ]]; then
  exec python3 "$skill_script_dir/design-audit.py" .
fi

scan_globs=(-g '*.css' -g '*.scss' -g '*.sass' -g '*.less' -g '*.html' -g '*.js' -g '*.jsx' -g '*.ts' -g '*.tsx' -g '*.vue' -g '*.svelte' -g '!node_modules/**' -g '!dist/**' -g '!build/**' -g '!coverage/**')

run_signal() {
  local label="$1"
  local pattern="$2"
  printf '\n[%s]\n' "$label"
  rg -n -i --max-count 40 "$pattern" "${scan_globs[@]}" . || printf 'none\n'
}

printf 'UI SIGNAL SCAN\n'
printf 'These matches are review prompts, not automatic defects. Inspect context before changing code.\n'

run_signal 'transition-all' 'transition[[:space:]]*:[[:space:]]*all|transition-all'
run_signal 'outline-removal' 'outline[[:space:]]*:[[:space:]]*(none|0)|outline-none'
run_signal 'viewport-height' '100vh|min-h-screen|h-screen'
run_signal 'continuous-animation' 'animation[[:space:]]*:[^;]*infinite|animation-iteration-count[[:space:]]*:[[:space:]]*infinite|repeat[[:space:]]*:[[:space:]]*Infinity|repeat:[[:space:]]*infinity'
run_signal 'heavy-blur' 'backdrop-blur|filter[[:space:]]*:[^;]*blur|blur-3xl'
run_signal 'generic-gradient' "from-(purple|violet|indigo)-[^[:space:]\"']+[[:space:]].*to-(blue|cyan)-|linear-gradient\\([^)]*(purple|violet)[^)]*(blue|cyan)"
run_signal 'decorative-status-dot' '(status|pulse|ping)[-_ ]?(dot|indicator)|animate-ping'
run_signal 'three-dimensional-runtime' "@react-three|from[[:space:]]+[\"']three[\"']|new[[:space:]]+THREE\\."

printf '\n[reduced-motion-presence]\n'
if rg -n -i 'prefers-reduced-motion|useReducedMotion|reducedMotion' "${scan_globs[@]}" . >/dev/null; then
  printf 'present\n'
else
  printf 'not found; review if the interface contains non-trivial motion\n'
fi

printf '\n[design-contracts]\n'
for contract in PRODUCT.md DESIGN.md THREE-D.md; do
  [[ -f "$contract" ]] && printf '%s\n' "$contract"
done
