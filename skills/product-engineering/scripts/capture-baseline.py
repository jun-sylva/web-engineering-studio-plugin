#!/usr/bin/env python3
"""Capture a non-destructive change baseline without copying file contents."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def run_git(root: Path, *args: str):
    result = subprocess.run(["git", *args], cwd=root, text=True, capture_output=True, check=False)
    return result.stdout.strip() if result.returncode == 0 else None


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--change", required=True)
    parser.add_argument("--include", action="append", default=[])
    args = parser.parse_args()
    root, output = args.root.resolve(), args.output.resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    if output.exists():
        raise SystemExit(f"Refusing to overwrite baseline: {output}")
    files = []
    for relative in args.include:
        path = (root / relative).resolve()
        try:
            rel = path.relative_to(root)
        except ValueError:
            raise SystemExit(f"Included path escapes project: {relative}")
        if not path.is_file():
            raise SystemExit(f"Included path is not a file: {relative}")
        stat = path.stat()
        files.append({"path": str(rel), "sha256": digest(path), "size": stat.st_size})
    git_root = run_git(root, "rev-parse", "--show-toplevel")
    record = {
        "schema": 1,
        "change": args.change,
        "captured_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "project": str(root),
        "git": {
            "available": git_root is not None,
            "root": git_root,
            "head": run_git(root, "rev-parse", "HEAD") if git_root else None,
            "branch": run_git(root, "branch", "--show-current") if git_root else None,
            "status_porcelain": run_git(root, "status", "--porcelain=v1") if git_root else None,
        },
        "files": files,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(f"Captured baseline for {args.change} at {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
