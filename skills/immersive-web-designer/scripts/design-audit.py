#!/usr/bin/env python3
import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Rule:
    rule_id: str
    severity: str
    category: str
    message: str
    pattern: re.Pattern
    extensions: frozenset[str]


WEB = frozenset({".html", ".css", ".scss", ".sass", ".less", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte"})
MARKUP = frozenset({".html", ".jsx", ".tsx", ".vue", ".svelte"})
STYLE = frozenset({".css", ".scss", ".sass", ".less", ".jsx", ".tsx", ".vue", ".svelte"})
SCRIPT = frozenset({".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte"})


def rx(pattern: str) -> re.Pattern:
    return re.compile(pattern, re.IGNORECASE | re.MULTILINE)


RULES = [
    Rule("a11y-outline-removed", "P1", "accessibility", "Focus outline removed; confirm an equally visible focus-visible replacement.", rx(r"outline\s*:\s*(?:none|0)\b|\boutline-none\b"), STYLE),
    Rule("a11y-positive-tabindex", "P1", "accessibility", "Positive tabindex creates a custom focus order.", rx(r"tabindex\s*=\s*[\"'{]?\s*[1-9]\d*"), MARKUP),
    Rule("a11y-clickable-static", "P1", "accessibility", "Static div/span has a click handler; prefer a native control or supply full keyboard semantics.", rx(r"<(?:div|span)\b(?=[^>]*\bonClick\s*=)(?![^>]*\b(?:role|tabIndex)\s*=)[^>]*>"), frozenset({".jsx", ".tsx", ".vue", ".svelte"})),
    Rule("a11y-image-alt", "P1", "accessibility", "Image tag appears to lack alt text.", rx(r"<img\b(?![^>]*\balt\s*=)[^>]*>"), MARKUP),
    Rule("a11y-new-window", "P2", "accessibility", "target=_blank appears without rel=noopener/noreferrer.", rx(r"<a\b(?=[^>]*target\s*=\s*[\"']_blank[\"'])(?![^>]*rel\s*=\s*[\"'][^\"']*(?:noopener|noreferrer))[^>]*>"), MARKUP),
    Rule("a11y-autofocus", "P2", "accessibility", "Autofocus can move focus unexpectedly.", rx(r"\bautoFocus\b|\bautofocus\b"), MARKUP),
    Rule("a11y-canvas-fallback", "P2", "accessibility", "Canvas appears empty; ensure adjacent HTML content or an accessible alternative exists.", rx(r"<canvas\b[^>]*>\s*</canvas>"), MARKUP),
    Rule("motion-transition-all", "P2", "motion", "transition: all can animate unintended and expensive properties.", rx(r"transition\s*:\s*all\b|\btransition-all\b"), STYLE),
    Rule("motion-infinite", "P2", "motion", "Continuous animation needs a purpose, pause strategy and reduced-motion behavior.", rx(r"animation\s*:[^;{}]*\binfinite\b|animation-iteration-count\s*:\s*infinite\b|repeat\s*:\s*Infinity\b"), WEB),
    Rule("motion-layout-property", "P2", "motion", "Animation appears to target layout properties; prefer transform/opacity when equivalent.", rx(r"@keyframes[\s\S]{0,1200}?(?:\btop\s*:|\bleft\s*:|\bwidth\s*:|\bheight\s*:|\bmargin\s*:)|animate\([^)]{0,500}(?:width|height|top|left)"), STYLE | SCRIPT),
    Rule("motion-scroll-smooth", "P3", "motion", "Global smooth scrolling can conflict with user preferences.", rx(r"scroll-behavior\s*:\s*smooth|scrollBehavior\s*:\s*[\"']smooth"), WEB),
    Rule("performance-will-change", "P2", "performance", "Persistent will-change can increase memory use; apply it narrowly and temporarily.", rx(r"will-change\s*:\s*(?:all|transform|opacity)"), STYLE),
    Rule("performance-fixed-background", "P2", "performance", "Fixed background attachment is costly on many mobile browsers.", rx(r"background-attachment\s*:\s*fixed"), STYLE),
    Rule("performance-preserve-buffer", "P1", "performance", "preserveDrawingBuffer increases WebGL memory cost; keep only for a proven capture requirement.", rx(r"preserveDrawingBuffer\s*:\s*true"), SCRIPT),
    Rule("performance-unbounded-dpr", "P1", "performance", "Renderer pixel ratio appears unbounded; cap devicePixelRatio for high-density screens.", rx(r"setPixelRatio\s*\(\s*(?:window\.)?devicePixelRatio\s*\)"), SCRIPT),
    Rule("responsive-legacy-vh", "P2", "responsive", "100vh can mis-size mobile layouts; consider dynamic viewport units with fallback.", rx(r"\b100vh\b|\bh-screen\b|\bmin-h-screen\b"), STYLE | MARKUP),
    Rule("design-common-gradient", "P3", "design", "Common purple/blue gradient detected; verify it belongs to the approved visual direction.", rx(r"from-(?:purple|violet|indigo)-\S+[^\n]{0,160}to-(?:blue|cyan)-|linear-gradient\([^)]*(?:purple|violet)[^)]*(?:blue|cyan)"), WEB),
    Rule("design-heavy-blur", "P3", "design", "Heavy blur/glass treatment detected; verify hierarchy, contrast and performance.", rx(r"\bbackdrop-blur(?:-\w+)?\b|backdrop-filter\s*:[^;]*blur|\bblur-3xl\b"), STYLE),
    Rule("design-decorative-pulse", "P3", "design", "Pulsing/status-dot treatment detected; ensure it communicates a real state.", rx(r"\banimate-ping\b|(?:status|pulse|ping)[-_ ]?(?:dot|indicator)"), WEB),
    Rule("design-section-numbering", "P3", "design", "Decorative section numbering detected; verify it helps navigation rather than simulating editorial character.", rx(r">\s*(?:0?\d{1,2}\s*[./·—-]\s*)?(?:index|capabilities|features|services|process)\s*<|[\"']0{1,2}\d\s*[./·—-]"), MARKUP),
    Rule("copy-generic-claim", "P3", "content", "Generic marketing claim detected; replace with a specific user outcome when possible.", rx(r"\b(?:everything you need|unlock your potential|next[- ]generation|revolutionize your|seamless experience|move faster|work smarter)\b"), MARKUP),
    Rule("design-extreme-z", "P3", "design", "Extreme z-index detected; verify the layering system instead of escalating values.", rx(r"z-index\s*:\s*(?:9999\d*|2147483647)|\bz-\[(?:9999\d*|2147483647)\]"), STYLE),
]

EXCLUDED_DIRS = {"node_modules", ".git", ".claude", ".agents", ".codex", ".iwd", "dist", "build", "coverage", ".next", ".nuxt", ".svelte-kit", "vendor"}


def line_context(text: str, start: int) -> tuple[int, str]:
    line_number = text.count("\n", 0, start) + 1
    line_start = text.rfind("\n", 0, start) + 1
    line_end = text.find("\n", start)
    if line_end == -1:
        line_end = len(text)
    excerpt = re.sub(r"\s+", " ", text[line_start:line_end]).strip()
    return line_number, excerpt[:240]


def scan(root: Path, max_per_rule: int) -> tuple[list[dict], dict]:
    findings: list[dict] = []
    counts = {rule.rule_id: 0 for rule in RULES}
    scanned_files = 0
    has_motion = False
    has_reduced_motion = False
    three_files: list[tuple[Path, str]] = []

    for file_path in root.rglob("*"):
        if not file_path.is_file() or any(part in EXCLUDED_DIRS for part in file_path.parts):
            continue
        extension = file_path.suffix.lower()
        if extension not in WEB or file_path.stat().st_size > 2_000_000:
            continue
        try:
            text = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        scanned_files += 1
        relative = str(file_path.relative_to(root))
        if re.search(r"animation|transition|requestAnimationFrame|\bmotion\b|\bgsap\b", text, re.I):
            has_motion = True
        if re.search(r"prefers-reduced-motion|useReducedMotion|reducedMotion", text, re.I):
            has_reduced_motion = True
        if re.search(r"@react-three|from\s+[\"']three[\"']|new\s+THREE\.", text):
            three_files.append((file_path, text))

        for rule in RULES:
            if extension not in rule.extensions:
                continue
            for match in rule.pattern.finditer(text):
                if counts[rule.rule_id] >= max_per_rule:
                    break
                line, excerpt = line_context(text, match.start())
                findings.append({"rule": rule.rule_id, "severity": rule.severity, "category": rule.category, "file": relative, "line": line, "message": rule.message, "excerpt": excerpt})
                counts[rule.rule_id] += 1

    if has_motion and not has_reduced_motion:
        findings.append({"rule": "motion-reduced-missing", "severity": "P1", "category": "motion", "file": ".", "line": 1, "message": "Motion exists but no reduced-motion handling was found in scanned source files.", "excerpt": "project-level signal"})

    for file_path, text in three_files:
        relative = str(file_path.relative_to(root))
        if re.search(r"new\s+(?:THREE\.)?WebGLRenderer", text) and not re.search(r"\.dispose\s*\(", text):
            findings.append({"rule": "three-dispose-missing", "severity": "P1", "category": "performance", "file": relative, "line": 1, "message": "A WebGL renderer is created but no dispose call was found in this file.", "excerpt": "file-level lifecycle signal"})
        if re.search(r"requestAnimationFrame\s*\(", text) and not re.search(r"cancelAnimationFrame\s*\(", text):
            findings.append({"rule": "animation-cancel-missing", "severity": "P2", "category": "performance", "file": relative, "line": 1, "message": "Animation frames are requested but no cancellation was found in this file.", "excerpt": "file-level lifecycle signal"})

    summary = {"root": str(root), "filesScanned": scanned_files, "findingCount": len(findings), "bySeverity": {}, "byCategory": {}}
    for finding in findings:
        summary["bySeverity"][finding["severity"]] = summary["bySeverity"].get(finding["severity"], 0) + 1
        summary["byCategory"][finding["category"]] = summary["byCategory"].get(finding["category"], 0) + 1
    return sorted(findings, key=lambda item: (item["severity"], item["file"], item["line"])), summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Read-only deterministic frontend design audit.")
    parser.add_argument("root", nargs="?", default=".", type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--max-per-rule", type=int, default=40)
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        raise SystemExit(f"Project directory not found: {root}")
    findings, summary = scan(root, max(1, args.max_per_rule))
    if args.json:
        print(json.dumps({"summary": summary, "findings": findings}, ensure_ascii=False, indent=2))
        return
    print(f"Scanned {summary['filesScanned']} files; {summary['findingCount']} review signals.")
    for finding in findings:
        print(f"{finding['severity']} {finding['rule']} {finding['file']}:{finding['line']} — {finding['message']}")
        if finding["excerpt"]:
            print(f"  {finding['excerpt']}")
    print("Signals require contextual review; they are not automatic defects.")


if __name__ == "__main__":
    main()
