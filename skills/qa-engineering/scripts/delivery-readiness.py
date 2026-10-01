#!/usr/bin/env python3
"""Deterministic PROJECT_MEMORY delivery-readiness checks."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

PASSING = {"pass", "passed", "complete", "completed", "done", "not-applicable", "accepted-risk"}
BLOCKING = {"pending", "fail", "failed", "blocked", "in-progress", "not-run"}


def section(body: str, heading: str) -> str:
    match = re.search(rf"^##\s+{re.escape(heading)}\s*$([\s\S]*?)(?=^##\s+|\Z)", body, re.MULTILINE)
    return match.group(1) if match else ""


def rows(text: str):
    for line in text.splitlines():
        if not line.startswith("|") or re.match(r"^\|[\s:-]+\|", line):
            continue
        cells = [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        if cells and cells[0] not in {"ID", "Exigence"}:
            yield cells


def analyze(body: str, require_release: bool):
    blockers, warnings = [], []
    requirements = {}
    for item in rows(section(body, "Exigences et critères d’acceptation")):
        if len(item) >= 6 and re.fullmatch(r"REQ-\d{3,}", item[0]):
            requirements[item[0]] = {"priority": item[2].lower(), "status": item[5].lower()}
            if item[5].lower() not in {"confirmed", "accepted"}:
                blockers.append(f"{item[0]} is not confirmed ({item[5]})")

    traced = set(re.findall(r"\bREQ-\d{3,}\b", section(body, "Matrice de traçabilité")))
    for req_id, data in requirements.items():
        if data["priority"] in {"haute", "high", "critical", "critique"} and req_id not in traced:
            blockers.append(f"{req_id} has no traceability row")

    dod = section(body, "Definition of Done")
    dod_items = re.findall(r"^-\s+([^:]+):\s*([^\n]+)$", dod, re.MULTILINE)
    if not dod_items:
        blockers.append("Definition of Done has no status items")
    for label, raw_status in dod_items:
        status = raw_status.strip().lower().split()[0]
        if status in BLOCKING or status not in PASSING:
            blockers.append(f"DoD '{label.strip()}' is {raw_status.strip()}")

    open_risks = []
    for item in rows(section(body, "Risques")):
        if len(item) >= 7 and re.fullmatch(r"RSK-\d{3,}", item[0]) and item[6].lower() in {"open", "unaccepted"}:
            open_risks.append(item[0])
    if open_risks:
        warnings.append("Open risks require explicit disposition: " + ", ".join(open_risks))

    if require_release and not re.search(r"^\|\s*REL-\d{3,}\s*\|", section(body, "Releases et incidents"), re.MULTILINE):
        blockers.append("No release record found")
    return blockers, warnings, len(requirements), len(traced)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("memory", type=Path)
    parser.add_argument("--require-release", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    body = args.memory.read_text(encoding="utf-8")
    blockers, warnings, requirements, traced = analyze(body, args.require_release)
    result = {"ready": not blockers, "requirements": requirements, "traced_requirement_ids": traced, "blockers": blockers, "warnings": warnings}
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("READY" if result["ready"] else "NOT READY")
        for item in blockers:
            print(f"BLOCKER {item}")
        for item in warnings:
            print(f"WARNING {item}")
    return 0 if result["ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
