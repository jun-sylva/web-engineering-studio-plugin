#!/usr/bin/env bash
set -euo pipefail

skill_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills_root="$(cd "$skill_dir/.." && pwd)"
plugin_assets="$(cd "$skills_root/../plugin-assets" && pwd)"
skill_names=(project-memory product-engineering immersive-web-designer code-review security-review qa-engineering release-engineering)
output_arg="${1:-}"
force="${2:-}"

if [[ -z "$output_arg" ]]; then
  printf 'Usage: package-plugin.sh <output-directory> [--force]\n' >&2
  exit 2
fi

output_parent="$(dirname "$output_arg")"
mkdir -p "$output_parent"
output_dir="$(cd "$output_parent" && pwd)/$(basename "$output_arg")"

if [[ "$output_dir" == "/" || "$output_dir" == "$HOME" || "$output_dir" == "$skill_dir" || "$output_dir" == "$skills_root" ]]; then
  printf 'Refusing unsafe output directory: %s\n' "$output_dir" >&2
  exit 2
fi

if [[ -e "$output_dir" ]]; then
  if [[ "$force" != "--force" ]]; then
    printf 'Output exists: %s. Pass --force to replace this package directory.\n' "$output_dir" >&2
    exit 2
  fi
  rm -rf "$output_dir"
fi

mkdir -p "$output_dir/.claude-plugin" "$output_dir/skills" "$output_dir/evals"
for skill_name in "${skill_names[@]}"; do
  source_dir="$skills_root/$skill_name"
  if [[ ! -f "$source_dir/SKILL.md" ]]; then
    printf 'Missing required skill: %s\n' "$source_dir/SKILL.md" >&2
    exit 2
  fi
  mkdir -p "$output_dir/skills/$skill_name"
  cp -R "$source_dir/." "$output_dir/skills/$skill_name/"
  if [[ -d "$output_dir/skills/$skill_name/plugin-evals" ]]; then
    cp -R "$output_dir/skills/$skill_name/plugin-evals/." "$output_dir/evals/"
    rm -rf "$output_dir/skills/$skill_name/plugin-evals"
  fi
done

for document in README.md INSTALL.md ATTRIBUTIONS.md; do
  if [[ ! -f "$plugin_assets/$document" ]]; then
    printf 'Missing plugin document: %s\n' "$plugin_assets/$document" >&2
    exit 2
  fi
  cp "$plugin_assets/$document" "$output_dir/$document"
done

printf '%s\n' \
  '{' \
  '  "name": "web-engineering-studio",' \
  '  "description": "A traceable Claude Code product-delivery team covering memory and change control, full-stack implementation, immersive design, code and security review, QA, release, and safe rollback.",' \
  '  "version": "4.0.1",' \
  '  "author": { "name": "SIELINOU GAMENI Sylvain Junior" }' \
  '}' > "$output_dir/.claude-plugin/plugin.json"

printf 'Packaged Claude Code plugin at %s\n' "$output_dir"
printf 'Test with: claude --plugin-dir %q\n' "$output_dir"
