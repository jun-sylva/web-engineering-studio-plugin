#!/usr/bin/env bash
set -u

project_root="${1:-.}"

if [[ ! -d "$project_root" ]]; then
  printf 'ERROR: project directory not found: %s\n' "$project_root" >&2
  exit 2
fi

cd "$project_root" || exit 2

printf 'PROJECT_ROOT\t%s\n' "$(pwd)"

printf '\nMANIFESTS\n'
for manifest in package.json pnpm-workspace.yaml yarn.lock pnpm-lock.yaml package-lock.json bun.lockb bun.lock vite.config.ts vite.config.js next.config.js next.config.mjs astro.config.mjs svelte.config.js nuxt.config.ts tsconfig.json; do
  [[ -e "$manifest" ]] && printf '%s\n' "$manifest"
done

printf '\nDESIGN_CONTRACTS\n'
for contract in PRODUCT.md DESIGN.md THREE-D.md CLAUDE.md AGENTS.md; do
  [[ -e "$contract" ]] && printf '%s\n' "$contract"
done

printf '\nPACKAGE_SIGNALS\n'
if [[ -f package.json ]]; then
  if command -v rg >/dev/null 2>&1; then
    rg -o '"(next|react|vue|svelte|astro|nuxt|three|@react-three/fiber|@react-three/drei|gsap|motion|framer-motion|tailwindcss)"[[:space:]]*:' package.json | sort -u || true
  else
    grep -Eo '"(next|react|vue|svelte|astro|nuxt|three|@react-three/fiber|@react-three/drei|gsap|motion|framer-motion|tailwindcss)"[[:space:]]*:' package.json | sort -u || true
  fi
fi

printf '\nSOURCE_DIRS\n'
for source_dir in src app pages components public assets styles tests e2e; do
  [[ -d "$source_dir" ]] && printf '%s\n' "$source_dir"
done

printf '\nUI_FILE_COUNTS\n'
if command -v rg >/dev/null 2>&1; then
  for extension in tsx jsx vue svelte css scss html; do
    count="$(rg --files -g "*.${extension}" -g '!node_modules/**' -g '!dist/**' -g '!build/**' -g '!.claude/**' -g '!.agents/**' -g '!.codex/**' | wc -l | tr -d ' ')"
    [[ "$count" != "0" ]] && printf '%s\t%s\n' "$extension" "$count"
  done
else
  printf 'rg unavailable; file counts skipped\n'
fi

printf '\nAVAILABLE_SCRIPTS\n'
if [[ -f package.json ]] && command -v node >/dev/null 2>&1; then
  node -e 'const p=require("./package.json"); for (const [k,v] of Object.entries(p.scripts||{})) console.log(`${k}\t${v}`)' 2>/dev/null || printf 'package.json could not be parsed with node\n'
fi

printf '\nGIT_STATE\n'
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git status --short 2>/dev/null || true
else
  printf 'not a git worktree\n'
fi
