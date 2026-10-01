#!/usr/bin/env python3
"""Deterministic helpers for PROJECT_MEMORY.md."""

from __future__ import annotations

import argparse
import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path

REQUIRED_HEADINGS = [
    "Métadonnées",
    "Vision et résultat attendu",
    "État courant",
    "Sources",
    "Exigences et critères d’acceptation",
    "Matrice de traçabilité",
    "Architecture et contraintes",
    "Changements et reverts",
    "Décisions",
    "Risques",
    "Validations",
    "Releases et incidents",
    "Definition of Done",
    "Journal des jalons",
    "Historique de routage",
    "Prochaine validation attendue",
]
PREFIXES = {"SRC", "REQ", "CHG", "TST", "DEC", "RSK", "VAL", "REL", "INC", "LOG"}
MANAGED_BLOCK = "<!-- web-engineering-studio:memory:start -->\n@PROJECT_MEMORY.md\n<!-- web-engineering-studio:memory:end -->"


def utc_date() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def command_init(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    if not root.is_dir():
        raise SystemExit(f"Not a directory: {root}")
    memory = root / "PROJECT_MEMORY.md"
    if memory.exists():
        raise SystemExit(f"Refusing to overwrite existing memory: {memory}")
    template = Path(__file__).resolve().parent.parent / "assets" / "PROJECT_MEMORY.template.md"
    content = template.read_text(encoding="utf-8")
    content = content.replace("{{PROJECT_NAME}}", args.project).replace("{{UPDATED_AT}}", utc_date())
    memory.write_text(content, encoding="utf-8")
    print(f"Created {memory}")
    if args.link_claude:
        claude_file = root / "CLAUDE.md"
        existing = claude_file.read_text(encoding="utf-8") if claude_file.exists() else ""
        if "@PROJECT_MEMORY.md" not in existing:
            separator = "" if not existing else ("\n" if existing.endswith("\n") else "\n\n")
            claude_file.write_text(existing + separator + MANAGED_BLOCK + "\n", encoding="utf-8")
            print(f"Linked memory from {claude_file}")
        else:
            print(f"Memory already linked from {claude_file}")
    return 0


def command_fingerprint(args: argparse.Namespace) -> int:
    path = args.path.resolve()
    if not path.is_file():
        raise SystemExit(f"Not a file: {path}")
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    modified = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(timespec="seconds")
    print(f"sha256={digest.hexdigest()} size={path.stat().st_size} modified={modified} path={path}")
    return 0


def read_memory(path: Path) -> str:
    if not path.is_file():
        raise SystemExit(f"Not a file: {path}")
    return path.read_text(encoding="utf-8")


def command_next_id(args: argparse.Namespace) -> int:
    prefix = args.prefix.upper()
    if prefix not in PREFIXES:
        raise SystemExit(f"Unsupported prefix: {prefix}. Choose from {', '.join(sorted(PREFIXES))}")
    body = read_memory(args.memory.resolve())
    values = [int(value) for value in re.findall(rf"\b{prefix}-(\d{{3,}})\b", body)]
    print(f"{prefix}-{max(values, default=0) + 1:03d}")
    return 0


def command_validate(args: argparse.Namespace) -> int:
    body = read_memory(args.memory.resolve())
    errors = []
    for heading in REQUIRED_HEADINGS:
        if not re.search(rf"^##\s+{re.escape(heading)}\s*$", body, re.MULTILINE):
            errors.append(f"missing heading: {heading}")
    seen: dict[str, int] = {}
    for match in re.finditer(r"\b(?:SRC|REQ|CHG|TST|DEC|RSK|VAL|REL|INC|LOG)-\d{3,}\b", body):
        value = match.group(0)
        seen[value] = seen.get(value, 0) + 1
    # Repeated references are valid. Only duplicate registry definitions (table row starts) are invalid.
    definitions: dict[str, int] = {}
    for value in re.findall(r"^\|\s*((?:SRC|REQ|CHG|TST|DEC|RSK|VAL|REL|INC|LOG)-\d{3,})\s*\|", body, re.MULTILINE):
        definitions[value] = definitions.get(value, 0) + 1
    errors.extend(f"duplicate definition: {key}" for key, count in definitions.items() if count > 1)
    if "- Décision :" not in body:
        errors.append("missing next validation decision")
    if re.search(r"(?i)(?:api[_-]?key|token|password|secret)\s*[:=]\s*\S{8,}", body):
        errors.append("possible secret value in memory")
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print(f"Valid PROJECT_MEMORY.md ({len(definitions)} registered item(s), {len(seen)} referenced ID(s)).")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init")
    init_parser.add_argument("root", type=Path)
    init_parser.add_argument("--project", required=True)
    init_parser.add_argument("--link-claude", action="store_true")
    init_parser.set_defaults(func=command_init)

    fingerprint_parser = subparsers.add_parser("fingerprint")
    fingerprint_parser.add_argument("path", type=Path)
    fingerprint_parser.set_defaults(func=command_fingerprint)

    next_parser = subparsers.add_parser("next-id")
    next_parser.add_argument("memory", type=Path)
    next_parser.add_argument("prefix")
    next_parser.set_defaults(func=command_next_id)

    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("memory", type=Path)
    validate_parser.set_defaults(func=command_validate)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
