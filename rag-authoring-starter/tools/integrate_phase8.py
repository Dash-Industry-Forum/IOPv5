#!/usr/bin/env python3
"""
Phase 8 Integration Script
Copies required images and commits Phase 6, 7, and 8 changes.

Usage: python integrate_phase8.py
Run from the IOPv5-tstock-worktree directory.
"""

import os
import shutil
import subprocess
import sys

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKTREE = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
SOURCE_IMAGES = os.path.abspath(os.path.join(
    WORKTREE, '..', '..', 'Guidelines-TimingModel', 'Images', 'Timing'))
PART2_IMAGES = os.path.join(WORKTREE, 'rag-authoring-starter', 'specs',
                             'part02-core-cmaf', 'images')
PART4_IMAGES = os.path.join(WORKTREE, 'rag-authoring-starter', 'specs',
                             'part04-live-low-latency', 'Images')

# Images needed for Part 2 (Segment Loss Handling)
PART2_NEW_IMAGES = [
    ('MissingSegment.png', 'MissingSegment.png'),
    ('MissingSegment-FixWithPeriodSplitting.png', 'MissingSegment-FixWithPeriodSplitting.png'),
    ('MissingSegment-FixWithPlaceholder.png', 'MissingSegment-FixWithPlaceholder.png'),
]

# Images needed for Part 4 (MPD Updates)
PART4_NEW_IMAGES = [
    ('MpdUpdate - AddContent.png', 'MpdUpdate-AddContent.png'),
    ('MpdUpdate - RemoveContent.png', 'MpdUpdate-RemoveContent.png'),
]


def copy_images(source_dir, dest_dir, image_list):
    """Copy images from source to destination."""
    os.makedirs(dest_dir, exist_ok=True)
    copied = []
    for src_name, dst_name in image_list:
        src = os.path.join(source_dir, src_name)
        dst = os.path.join(dest_dir, dst_name)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"  Copied: {src_name} -> {dst_name}")
            copied.append(dst_name)
        else:
            print(f"  WARNING: Source not found: {src}")
    return copied


def run_git(args, cwd=None):
    """Run a git command and return output."""
    cmd = ['git'] + args
    result = subprocess.run(cmd, cwd=cwd or WORKTREE,
                            capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  Git error: {result.stderr.strip()}")
    return result


def main():
    print("=" * 60)
    print("Phase 8 Integration Script")
    print("=" * 60)
    print(f"Worktree: {WORKTREE}")
    print(f"Source images: {SOURCE_IMAGES}")
    print()

    # Step 1: Copy Part 2 images
    print("Step 1: Copying Part 2 images (Segment Loss Handling)...")
    part2_copied = copy_images(SOURCE_IMAGES, PART2_IMAGES, PART2_NEW_IMAGES)
    print(f"  Copied {len(part2_copied)} images to Part 2")
    print()

    # Step 2: Copy Part 4 images
    print("Step 2: Copying Part 4 images (MPD Updates)...")
    part4_copied = copy_images(SOURCE_IMAGES, PART4_IMAGES, PART4_NEW_IMAGES)
    print(f"  Copied {len(part4_copied)} images to Part 4")
    print()

    # Step 3: Check git status
    print("Step 3: Checking git status...")
    result = run_git(['status', '--short'])
    if result.returncode == 0:
        print(result.stdout)
    print()

    # Step 4: Stage all changes
    print("Step 4: Staging all changes...")
    result = run_git(['add', '-A'])
    if result.returncode == 0:
        print("  All changes staged successfully")
    print()

    # Step 5: Commit Phase 6 + 7 + 8 together
    print("Step 5: Committing Phase 6, 7, and 8...")
    commit_msg = """Phase 6-8: Live service timing, timing constraints, MPD updates, segment loss

Phase 6: Live service timing integration into Part 4
- Availability Window (Section 4.2.3.4) with diagram
- Time Shift Buffer (Section 4.2.3.5) with diagram
- Presentation Delay (Section 4.2.3.6) with diagram
Source: Guidelines-TimingModel lines 419-512

Phase 7: Timing constraints integration into Part 2
- Large Timescales and Time Values
- Representing Durations in XML
Source: Guidelines-TimingModel 29-Misc.inc.md

Phase 8: MPD updates, period continuity, segment loss handling
Part 4 additions:
- MPD Snapshot Validity
- Adding Content to the MPD (with diagram)
- Removing Content from the MPD (with diagram)
- End of Live Content
- MPD Refreshes
Source: Guidelines-TimingModel lines 514-682

Part 2 additions:
- Period Continuity (subsection of Period Connectivity)
- Segment Loss Handling (new section with 3 diagrams)
Source: Guidelines-TimingModel lines 290-348, 683-741

Total: ~400 lines, 7 diagrams
Follows precedence rule: ISO/IEC 23009-1 > IOP v5 > Guidelines-TimingModel"""

    result = run_git(['commit', '-m', commit_msg])
    if result.returncode == 0:
        print("  Commit successful!")
        # Show the commit hash
        hash_result = run_git(['log', '--oneline', '-1'])
        if hash_result.returncode == 0:
            print(f"  Commit: {hash_result.stdout.strip()}")
    else:
        print(f"  Commit failed: {result.stderr}")
    print()

    # Step 6: Push to remote
    print("Step 6: Pushing to remote...")
    result = run_git(['push', 'origin', 'tstockhammer-rag-workflow'])
    if result.returncode == 0:
        print("  Push successful!")
    else:
        print(f"  Push failed: {result.stderr}")
        print("  You may need to push manually:")
        print("  git push origin tstockhammer-rag-workflow")
    print()

    print("=" * 60)
    print("Phase 8 Integration Complete!")
    print("=" * 60)
    print()
    print("Summary:")
    print(f"  Part 2 images copied: {len(part2_copied)}")
    print(f"  Part 4 images copied: {len(part4_copied)}")
    print()
    print("Content integrated:")
    print("  Part 4: MPD Snapshot Validity, Add/Remove Content, End of Live, MPD Refreshes")
    print("  Part 2: Period Continuity, Segment Loss Handling")
    print()
    print("Next steps:")
    print("  - Phase 9: Standalone text timing + forbidden techniques")
    print("  - Phase 10: 01-Intro.inc.md content")
    print("  - Phase 11: Examples and test vectors")


if __name__ == '__main__':
    main()