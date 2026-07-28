#!/usr/bin/env python3
"""Fix hanging paragraphs in all IOP v5 spec .inc.md files.

A "hanging paragraph" is text that appears directly under a section heading
that also has subsections. Bikeshed/HTML spec style requires that if a section
has subsections, all content must be in subsections.

Fix: insert a "General" subsection before the hanging text.

Usage: python fix_hanging_paragraphs.py [--dry-run]
Run from the IOPv5-tstock-worktree directory.
"""

import re
import sys
from pathlib import Path

WORKTREE = Path(__file__).parent.parent
SPECS_DIR = WORKTREE / "rag-authoring-starter" / "specs"

# Heading pattern: ## Title ## {#id} or ### Title ### {#id} etc.
HEADING_RE = re.compile(r'^(#{1,6})\s+(.+?)\s+\1\s*(?:\{#[^}]+\})?\s*$')

def heading_level(line: str) -> int:
    """Return heading level (1-6) or 0 if not a heading."""
    m = HEADING_RE.match(line.rstrip())
    if m:
        return len(m.group(1))
    return 0

def heading_id(line: str) -> str:
    """Extract the {#id} from a heading line, or generate one."""
    m = re.search(r'\{#([^}]+)\}', line)
    if m:
        return m.group(1)
    # Generate from heading text
    text_m = HEADING_RE.match(line.rstrip())
    if text_m:
        text = text_m.group(2).lower()
        text = re.sub(r'[^a-z0-9]+', '-', text).strip('-')
        return text
    return 'general'

def make_general_heading(parent_level: int, parent_id: str) -> str:
    """Create a General subsection heading one level below parent."""
    child_level = parent_level + 1
    hashes = '#' * child_level
    return f"{hashes} General {hashes} {{#{parent_id}-general}}\n"

def is_content_line(line: str) -> bool:
    """Return True if line has non-whitespace, non-comment content."""
    stripped = line.strip()
    if not stripped:
        return False
    if stripped.startswith('<!--'):
        return False
    return True

def fix_hanging_paragraphs(path: Path, dry_run: bool = False) -> int:
    """Fix hanging paragraphs in a file. Returns number of fixes made."""
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines(keepends=True)
    
    # Build a list of (line_index, level, id) for all headings
    headings = []
    for i, line in enumerate(lines):
        lvl = heading_level(line)
        if lvl > 0:
            hid = heading_id(line)
            headings.append((i, lvl, hid))
    
    if not headings:
        return 0
    
    # For each heading, check if it has:
    # 1. Content lines before the first subsection
    # 2. At least one subsection
    insertions = []  # list of (insert_before_line_index, text_to_insert)
    
    for hi, (h_idx, h_lvl, h_id) in enumerate(headings):
        # Find the range of this section: from h_idx+1 to the next same-or-higher heading
        next_same_or_higher = len(lines)
        for hj in range(hi + 1, len(headings)):
            if headings[hj][1] <= h_lvl:
                next_same_or_higher = headings[hj][0]
                break
        
        # Find the first subsection (level = h_lvl + 1) within this section
        first_subsection_idx = None
        for hj in range(hi + 1, len(headings)):
            if headings[hj][0] >= next_same_or_higher:
                break
            if headings[hj][1] == h_lvl + 1:
                first_subsection_idx = headings[hj][0]
                break
        
        if first_subsection_idx is None:
            # No subsections - no hanging paragraph possible
            continue
        
        # Check if there's content between h_idx+1 and first_subsection_idx
        has_content = False
        first_content_idx = None
        for li in range(h_idx + 1, first_subsection_idx):
            if is_content_line(lines[li]):
                has_content = True
                first_content_idx = li
                break
        
        if not has_content:
            continue
        
        # Check if a "General" subsection already exists right after the heading
        # (i.e., the first subsection is already named "General" or "Overview" or "Introduction")
        first_sub_line = lines[first_subsection_idx].strip()
        if re.search(r'(General|Overview|Introduction|Background)', first_sub_line, re.IGNORECASE):
            # Already has a general subsection - but check if there's still content before it
            # If the first content is before the first subsection, we still have a hanging paragraph
            # unless the first subsection IS the general one
            # In this case, skip
            continue
        
        # We have a hanging paragraph. Insert a "General" subsection before the first content line.
        # Find the right insertion point: after any blank lines following the heading
        insert_idx = h_idx + 1
        # Skip blank lines immediately after the heading
        while insert_idx < first_content_idx and not lines[insert_idx].strip():
            insert_idx += 1
        
        general_heading = make_general_heading(h_lvl, h_id)
        insertions.append((insert_idx, general_heading))
        
        heading_text = lines[h_idx].strip()
        print(f"  [{path.name}] Hanging paragraph in: {heading_text[:60]}")
        print(f"    -> Insert '{general_heading.strip()}' before line {insert_idx + 1}")
    
    if not insertions:
        return 0
    
    if dry_run:
        return len(insertions)
    
    # Apply insertions in reverse order to preserve line indices
    insertions.sort(key=lambda x: x[0], reverse=True)
    for insert_idx, insert_text in insertions:
        # Insert: blank line before heading, heading, blank line after
        lines.insert(insert_idx, '\n')
        lines.insert(insert_idx, insert_text)
        lines.insert(insert_idx, '\n')
    
    new_text = ''.join(lines)
    path.write_text(new_text, encoding='utf-8')
    return len(insertions)


def find_spec_files(specs_dir: Path) -> list:
    """Find all .inc.md files in the specs directory."""
    files = []
    for f in sorted(specs_dir.rglob('*.inc.md')):
        # Skip files in examples/ or figures/ subdirectories
        if any(part in ('examples', 'figures', 'sources', 'images', 'Images') 
               for part in f.parts):
            continue
        files.append(f)
    return files


if __name__ == '__main__':
    dry_run = '--dry-run' in sys.argv
    
    if dry_run:
        print("DRY RUN - no files will be modified\n")
    
    spec_files = find_spec_files(SPECS_DIR)
    print(f"Found {len(spec_files)} spec files\n")
    
    total_fixes = 0
    for f in spec_files:
        fixes = fix_hanging_paragraphs(f, dry_run=dry_run)
        if fixes:
            total_fixes += fixes
            print(f"  -> {fixes} fix(es) in {f.relative_to(SPECS_DIR)}\n")
    
    if dry_run:
        print(f"\nDRY RUN: Would make {total_fixes} fix(es) total.")
    else:
        print(f"\nDone. Made {total_fixes} fix(es) total.")