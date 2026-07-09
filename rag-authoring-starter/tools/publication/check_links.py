#!/usr/bin/env python3
"""
Basic publication checks over authored Markdown/Bikeshed sources in specs/.

Current checks (stdlib only, no network by default):
- Relative link targets exist on disk.
- Figure/image references resolve.
- Duplicate top-level headings within a file.
- Reports counts of normative modal verbs (shall/should/may/must) per file,
  which DASH-IF authoring guidelines care about.

Usage:
    python tools/publication/check_links.py
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPECS = ROOT / "specs"

LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
IMAGE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
MODALS = ("shall", "should", "may", "must", "shall not", "should not")


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#"))


def check_file(path: Path) -> list[str]:
    issues: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    rel = path.relative_to(ROOT)

    headings: Counter[str] = Counter()
    for line in text.splitlines():
        m = HEADING.match(line.strip())
        if m:
            headings[m.group(2).strip().lower()] += 1
    for title, count in headings.items():
        if count > 1:
            issues.append(f"{rel}: duplicate heading '{title}' ({count}x)")

    for match in LINK.finditer(text):
        target = match.group(1).split(" ")[0].split("#")[0]
        if not target or is_external(target):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            issues.append(f"{rel}: broken link target -> {target}")

    modal_counts = Counter()
    lowered = text.lower()
    for modal in MODALS:
        modal_counts[modal] = len(re.findall(rf"\b{re.escape(modal)}\b", lowered))
    total_modals = sum(modal_counts.values())
    if total_modals:
        summary = ", ".join(f"{k}={v}" for k, v in modal_counts.items() if v)
        print(f"[modals] {rel}: {summary}")

    return issues


def main() -> None:
    if not SPECS.exists():
        print("No specs/ directory found.")
        return

    md_files = sorted(SPECS.rglob("*.md")) + sorted(SPECS.rglob("*.bs"))
    if not md_files:
        print("No authored specs (*.md / *.bs) found under specs/ yet.")
        return

    all_issues: list[str] = []
    for path in md_files:
        all_issues.extend(check_file(path))

    print()
    if all_issues:
        print(f"Found {len(all_issues)} issue(s):")
        for issue in all_issues:
            print(f"  - {issue}")
        raise SystemExit(1)
    print(f"OK: checked {len(md_files)} file(s), no issues found.")


if __name__ == "__main__":
    main()
