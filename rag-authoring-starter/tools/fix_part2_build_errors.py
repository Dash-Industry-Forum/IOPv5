#!/usr/bin/env python3
"""Fix Bikeshed build errors in Part 2 (01-core-cmaf.inc.md).

Fixes:
1. Remove trailing / from <img ... /> void elements
2. Fix duplicate <dfn>MPD timeline</dfn> in Terminology Choices section
3. Fix duplicate <dfn>period continuity</dfn> in Period Continuity section
4. Fix obsolete [[!RFC7233]] references
5. Add export to unexported dfns

Usage: python fix_part2_build_errors.py
Run from the IOPv5-tstock-worktree directory.
"""

import re
from pathlib import Path

WORKTREE = Path(__file__).parent.parent.parent
PART2 = WORKTREE / "rag-authoring-starter" / "specs" / "part02-core-cmaf" / "01-core-cmaf.inc.md"


def fix_file(path: Path) -> int:
    """Apply all fixes and return number of changes made."""
    text = path.read_text(encoding="utf-8")
    original = text
    changes = 0

    # Fix 1: Remove trailing / from <img ... /> void elements
    # Pattern: <img src="..." /> -> <img src="...">
    new_text = re.sub(r'(<img\s[^>]*?)\s*/>', r'\1>', text)
    if new_text != text:
        n = len(re.findall(r'(<img\s[^>]*?)\s*/>', text))
        print(f"  Fixed {n} <img /> self-closing slashes")
        text = new_text
        changes += n

    # Fix 2: Remove duplicate <dfn>MPD timeline</dfn> in Terminology Choices
    # The one in the Terminology Choices section (line ~93) conflicts with
    # the one in the MPD Timeline section (line ~250)
    # Keep the one in MPD Timeline section, remove from Terminology Choices
    old = 'This document\'s concept of the <dfn>MPD timeline</dfn> is not directly expressed'
    new = 'This document\'s concept of the MPD timeline is not directly expressed'
    if old in text:
        text = text.replace(old, new, 1)
        print("  Fixed duplicate <dfn>MPD timeline</dfn> in Terminology Choices")
        changes += 1

    # Fix 3: Add export to <dfn>MPD timeline</dfn> in MPD Timeline section
    # This is the canonical definition
    old = 'The MPD defines the <dfn>MPD timeline</dfn> of a DASH Media Presentation, which'
    new = 'The MPD defines the <dfn export>MPD timeline</dfn> of a DASH Media Presentation, which'
    if old in text:
        text = text.replace(old, new, 1)
        print("  Added export to <dfn>MPD timeline</dfn> in MPD Timeline section")
        changes += 1

    # Fix 4: Fix duplicate <dfn>period continuity</dfn>
    # The section heading {#period-continuity} creates an anchor, and the dfn also creates one
    # Add export to make it the canonical definition
    old = 'defines\n<dfn>period continuity</dfn>. Continuity is a special case'
    new = 'defines\n<dfn export>period continuity</dfn>. Continuity is a special case'
    if old in text:
        text = text.replace(old, new, 1)
        print("  Added export to <dfn>period continuity</dfn>")
        changes += 1
    else:
        # Try alternative pattern
        old2 = 'defines\r\n<dfn>period continuity</dfn>. Continuity is a special case'
        new2 = 'defines\r\n<dfn export>period continuity</dfn>. Continuity is a special case'
        if old2 in text:
            text = text.replace(old2, new2, 1)
            print("  Added export to <dfn>period continuity</dfn> (CRLF)")
            changes += 1
        else:
            # Try single-line pattern
            old3 = 'defines\n<dfn>period continuity</dfn>'
            if old3 in text:
                text = text.replace(old3, 'defines\n<dfn export>period continuity</dfn>', 1)
                print("  Added export to <dfn>period continuity</dfn> (alt)")
                changes += 1

    # Fix 5: Fix obsolete RFC7233 references
    old = '[[!RFC7233]]'
    new = '[[!RFC7233 obsolete]]'
    count = text.count(old)
    if count > 0:
        text = text.replace(old, new)
        print(f"  Fixed {count} [[!RFC7233]] -> [[!RFC7233 obsolete]]")
        changes += count

    # Fix 6: Add export to other unexported dfns (warnings, not errors)
    unexported_dfns = [
        ('<dfn>segment references</dfn>', '<dfn export>segment references</dfn>'),
        ('<dfn>sample timeline</dfn>', '<dfn export>sample timeline</dfn>'),
        ('<dfn>timescale units</dfn>', '<dfn export>timescale units</dfn>'),
        ('<dfn>timescale</dfn>', '<dfn export>timescale</dfn>'),
        ('<dfn>wall clock</dfn>', '<dfn export>wall clock</dfn>'),
        ('<dfn>addressing modes</dfn>', '<dfn export>addressing modes</dfn>'),
    ]
    for old_dfn, new_dfn in unexported_dfns:
        if old_dfn in text:
            text = text.replace(old_dfn, new_dfn, 1)
            print(f"  Added export to {old_dfn}")
            changes += 1

    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"\nTotal changes: {changes}")
        print(f"File saved: {path}")
    else:
        print("No changes made.")

    return changes


if __name__ == "__main__":
    print(f"Fixing Part 2 build errors in: {PART2}")
    if not PART2.exists():
        print(f"ERROR: File not found: {PART2}")
        exit(1)
    changes = fix_file(PART2)
    print(f"\nDone. {changes} changes applied.")