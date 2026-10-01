#!/usr/bin/env python3
"""Read-only, deterministic code-review signals. Findings require human confirmation."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SKIP = {".git", ".claude", "node_modules", "vendor", "dist", "build", "coverage", ".next"}
EXTENSIONS = {".js", ".jsx", ".ts", ".tsx", ".py", ".go", ".rs", ".java", ".kt", ".rb", ".php", ".cs", ".swift"}
RULES = [
    ("debug-artifact", re.compile(r"\bdebugger\b|\bconsole\.log\s*\("), "Debug artifact may have escaped review."),
    ("suppressed-check", re.compile(r"@ts-ignore|eslint-disable|noinspection|#\s*type:\s*ignore"), "A static check is suppressed; verify the reason and scope."),
    ("empty-handler", re.compile(r"catch\s*\([^)]*\)\s*\{\s*\}|except(?:\s+[^:]*)?:\s*(?:pass|\.\.\.)\s*$"), "An empty error handler may hide a failure."),
    ("unfinished-marker", re.compile(r"\b(?:TODO|FIXME|HACK|XXX)\b", re.I), "An unfinished marker remains in executable code."),
    ("typescript-any", re.compile(r"(?::|<|,\s*)\s*any\b|\bas\s+any\b"), "A broad TypeScript any may weaken a contract."),
]


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
            continue
        if any(part in SKIP for part in path.relative_to(root).parts):
            continue
        yield path


def scan(root: Path):
    findings = []
    for path in iter_files(root):
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for number, line in enumerate(lines, 1):
            for rule, pattern, message in RULES:
                if pattern.search(line):
                    findings.append({"rule": rule, "path": str(path.relative_to(root)), "line": number, "message": message})
        if len(lines) > 800:
            findings.append({"rule": "large-file", "path": str(path.relative_to(root)), "line": 1, "message": f"File has {len(lines)} lines; inspect cohesion before proposing a split."})
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    findings = scan(root)
    if args.json:
        print(json.dumps({"root": str(root), "findings": findings}, indent=2))
    else:
        for item in findings:
            print(f"{item['path']}:{item['line']} [{item['rule']}] {item['message']}")
        print(f"{len(findings)} signal(s); confirm each in context.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
