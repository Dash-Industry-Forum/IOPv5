#!/usr/bin/env python3
"""Update all .bs files (except Part 1) to:
1. Replace 'Repository: Dash-Industry-Forum/IOPv5' with a custom !Repository entry
2. Add !Issue Tracking pointing to IOPv5 GitHub + Part 1 §1.3
3. Add !Document Status pointing to Part 1 §1

Usage: python tools/update_bs_metadata.py
Run from the rag-authoring-starter directory.
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
SPECS = ROOT / "specs"

# Part number extraction from shortname
PART_LABELS = {
    "iop-v5-part2": ("Part 2", "0.1"),
    "iop-v5-part3": ("Part 3", "0.1"),
    "iop-v5-part4": ("Part 4", "0.1"),
    "iop-v5-part5": ("Part 5", "0.1"),
    "iop-v5-part6": ("Part 6", "0.1"),
    "iop-v5-part7": ("Part 7", "0.3"),
    "iop-v5-part8": ("Part 8", "0.3"),
    "iop-v5-part9": ("Part 9", "0.1"),
    "iop-v5-part10": ("Part 10", "0.4"),
    "iop-v5-part11": ("Part 11", "0.1"),
    "iop-v5-part12": ("Part 12", "0.6"),
}

PART1_DOC_STATUS_URL = "https://dashif.org/Guidelines/iop-v5/part01-overview.html#document-status"
PART1_ISSUE_URL = "https://dashif.org/Guidelines/iop-v5/part01-overview.html#issue-reporting"
IOPV5_ISSUES = "https://github.com/Dash-Industry-Forum/IOPv5/issues"
IOPV5_REPO = "https://github.com/Dash-Industry-Forum/IOPv5"


def update_bs_file(bs_path: Path) -> bool:
    text = bs_path.read_text(encoding="utf-8")

    # Extract shortname to determine part label
    shortname_m = re.search(r'^Shortname:\s*(\S+)', text, re.MULTILINE)
    if not shortname_m:
        print(f"  SKIP {bs_path.name}: no Shortname found")
        return False
    shortname = shortname_m.group(1)

    if shortname == "iop-v5-part1":
        print(f"  SKIP {bs_path.name}: Part 1 already updated manually")
        return False

    part_label, version = PART_LABELS.get(shortname, ("Part N", "0.1"))
    part_num = part_label.split()[-1]  # e.g. "2"

    # Check if already updated
    if "!Repository:" in text:
        print(f"  SKIP {bs_path.name}: already has !Repository")
        return False

    # Build replacement lines
    repo_line = f'!Repository: <a href="{IOPV5_REPO}">Dash-Industry-Forum/IOPv5</a>'
    issue_line = (
        f'!Issue Tracking: File issues at <a href="{IOPV5_ISSUES}">IOPv5 GitHub</a>. '
        f'Use label <code>{part_label}</code> or prefix <code>[Part {part_num}]:</code>. '
        f'See <a href="{PART1_ISSUE_URL}">Part 1 §1.3</a>.'
    )
    status_line = (
        f'!Document Status: Working Draft ({version}). '
        f'See <a href="{PART1_DOC_STATUS_URL}">Part 1 §1 Document Status</a> for versioning and workflow.'
    )

    # Replace 'Repository: Dash-Industry-Forum/IOPv5' with the three new lines
    old = "Repository: Dash-Industry-Forum/IOPv5"
    new = f"{repo_line}\n{issue_line}\n{status_line}"

    if old not in text:
        print(f"  WARN {bs_path.name}: '{old}' not found, skipping")
        return False

    new_text = text.replace(old, new, 1)
    bs_path.write_text(new_text, encoding="utf-8")
    print(f"  OK   {bs_path.name}: updated ({part_label})")
    return True


def main():
    bs_files = sorted(SPECS.rglob("*.bs"))
    print(f"Found {len(bs_files)} .bs files\n")
    updated = 0
    for f in bs_files:
        if update_bs_file(f):
            updated += 1
    print(f"\nUpdated {updated} file(s).")


if __name__ == "__main__":
    main()