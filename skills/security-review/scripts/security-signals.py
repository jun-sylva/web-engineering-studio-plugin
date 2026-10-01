#!/usr/bin/env python3
"""Passive security signal scanner. It never prints matched secret values."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SKIP = {".git", ".claude", "node_modules", "vendor", "dist", "build", "coverage", ".next"}
EXTENSIONS = {".js", ".jsx", ".ts", ".tsx", ".py", ".go", ".rs", ".java", ".kt", ".rb", ".php", ".cs", ".yml", ".yaml", ".json", ".toml", ".env"}
RULES = [
    ("possible-secret", re.compile(r"(?i)\b(?:api[_-]?key|secret|token|password|passwd)\b\s*[:=]\s*['\"][^'\"]{8,}['\"]"), "Possible hard-coded credential; value redacted."),
    ("dynamic-execution", re.compile(r"\b(?:eval|exec)\s*\("), "Dynamic execution requires untrusted-input tracing."),
    ("unsafe-html", re.compile(r"\b(?:innerHTML|outerHTML)\s*=|dangerouslySetInnerHTML"), "HTML injection sink requires provenance and sanitization review."),
    ("shell-exec", re.compile(r"\b(?:exec|execSync|system|popen)\s*\("), "Shell/process execution requires argument and input review."),
    ("tls-verification-disabled", re.compile(r"rejectUnauthorized\s*:\s*false|verify\s*=\s*False|NODE_TLS_REJECT_UNAUTHORIZED\s*=\s*['\"]?0"), "TLS certificate verification appears disabled."),
    ("weak-hash", re.compile(r"\b(?:md5|sha1)\s*\(", re.I), "Weak hash use needs purpose-specific review."),
    ("permissive-cors", re.compile(r"Access-Control-Allow-Origin[^\n]*\*|cors\s*\(\s*\)"), "Broad CORS policy may expose authenticated data."),
    ("unsafe-deserialization", re.compile(r"pickle\.loads?\s*\(|yaml\.load\s*\("), "Deserialization API requires trust-boundary review."),
    ("local-storage-token", re.compile(r"localStorage\.setItem\s*\([^,]*(?:token|jwt|auth)", re.I), "Browser token storage may increase XSS impact."),
]


def files(root: Path):
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.suffix.lower() in EXTENSIONS and not any(p in SKIP for p in path.relative_to(root).parts):
            yield path


def scan(root: Path):
    findings = []
    for path in files(root):
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for number, line in enumerate(lines, 1):
            for rule, pattern, message in RULES:
                if pattern.search(line):
                    findings.append({"rule": rule, "path": str(path.relative_to(root)), "line": number, "message": message})
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
        print(f"{len(findings)} passive signal(s); confirm each in context.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
