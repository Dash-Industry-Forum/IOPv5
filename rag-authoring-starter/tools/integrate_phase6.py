#!/usr/bin/env python3
"""
Integrate Phase 6 content into Part 4 Live Services file.
This script inserts the availability window, time shift buffer, and presentation delay sections.
"""

import sys
from pathlib import Path

# Define the content to insert
PHASE6_CONTENT = """
### Availability Window ### {#availability-window}

A Media Segment is <dfn>available</dfn> when an HTTP request to acquire the Media
Segment can be started and successfully performed to completion by a client
[[!MPEGDASH]]. During playback of a dynamic presentation, new Media Segments
continuously become available and stop being available with the passage of time.

An <dfn>availability window</dfn> is a time span on the MPD timeline that
determines which Media Segments clients can expect to be available. Each Adaptation
Set has its own availability window. Services <span class=modal-keyword><span class=modal-keyword>shall</span> not</span> define MPD attributes
that affect the availability window on the Representation level.

<figure>
  <img src="images/AvailabilityWindow.png" />
  <figcaption>The availability window determines which Media Segments can be
  expected to be available, based on where their segment end point lies.</figcaption>
</figure>

Note: A DASH service will typically make Media Segments available some seconds
ahead of the current time, depending on its configuration and latency target.
Furthermore, some Periods <span class=modal-keyword>may</span> be entirely prepared in advance and available at all
times (e.g., ads inserted between truly live content).

The availability window is calculated as follows:

1. Let `now` be the current wall clock time according to the synchronized clock.
2. Let `AvailabilityWindowStart` be `now - MPD@timeShiftBufferDepth`.
   - If `MPD@timeShiftBufferDepth` is not defined, let `AvailabilityWindowStart`
     be the effective availability start time.
3. Let `TotalAvailabilityTimeOffset` be the sum of all `@availabilityTimeOffset`
   values that apply to the Adaptation Set, either via `SegmentBase`,
   `SegmentTemplate`, or `BaseURL` elements [[!MPEGDASH]].
4. The availability window is the time span from `AvailabilityWindowStart` to
   `now + TotalAvailabilityTimeOffset`.

Media Segments that have their segment end point inside or at the end of the
availability window are available [[!MPEGDASH]].

Clients <span class=modal-keyword>may</span> at any point attempt to acquire any Media Segments that the MPD signals
as available. Clients <span class=modal-keyword><span class=modal-keyword>shall</span> not</span> attempt to acquire Media Segments that the MPD
does not signal as available.

Despite best efforts, DASH services occasionally fail to achieve the availability
windows advertised in the MPD. To ensure robust behavior, clients <span class=modal-keyword>should not</span> assume
that Media Segments described by the MPD as available are available and <span class=modal-keyword>should</span>
implement appropriate retry/fallback behavior.

### Time Shift Buffer ### {#time-shift-buffer}

The <dfn>time shift buffer</dfn> is a time span on the MPD timeline that defines
the set of Media Segments that a client is allowed to present at the current moment
in time according to the wall clock (`now`).

This is the mechanism by which clients can introduce a <dfn>time shift</dfn> (an
offset) between wall clock time and the MPD timeline when presenting dynamic
presentations. The time shift is zero when a client is presenting the Media Segment
at the end point of the time shift buffer.

The following additional factors further constrain the set of Media Segments that
can be presented at the current time:

1. [[#availability-window]] - not every Media Segment in the time shift buffer is
   guaranteed to be available.
2. [[#presentation-delay]] - the service <span class=modal-keyword>may</span> define a delay that forbids the use of
   a section of the time shift buffer.

The time shift buffer extends from `now - MPD@timeShiftBufferDepth` to `now`. In
the absence of `MPD@timeShiftBufferDepth`, the start of the time shift buffer is
the effective availability start time.

<figure>
  <img src="images/TimeShiftBuffer.png" />
  <figcaption>Media Segments overlapping the time shift buffer may potentially be
  presented by a client if other constraints do not forbid it.</figcaption>
</figure>

Clients <span class=modal-keyword>may</span> present samples from Media Segments that overlap the time shift buffer,
assuming no other constraints forbid it. Clients <span class=modal-keyword><span class=modal-keyword>shall</span> not</span> present samples from Media
Segments that are entirely outside the time shift buffer.

A dynamic presentation <span class=modal-keyword>shall</span> contain a Period that ends at or overlaps the end
point of the time shift buffer, except when reaching the end of live content.

Clients <span class=modal-keyword><span class=modal-keyword>shall</span> not</span> allow seeking into regions of the time shift buffer that are not
covered by Periods.

### Presentation Delay ### {#presentation-delay}

There is a natural conflict between the availability window and the time shift
buffer. It is legal for a client to present Media Segments as soon as they overlap
the time shift buffer, yet such Media Segments might not yet be available.

The mechanism that allows DASH clients to resolve this conflict is the
<dfn>presentation delay</dfn>, which decreases the time shift buffer by moving its
end point into the past, creating an <dfn>effective time shift buffer</dfn> with a
reduced duration.

Clients <span class=modal-keyword>shall</span> calculate a suitable presentation delay to ensure that the Media
Segments it schedules for playback are available and that there is sufficient time
to download them once they become available.

Note: Calculating an optimal presentation delay requires knowledge of Segment
durations, availability timing, network conditions, and buffer requirements.

The information required to calculate an optimal presentation delay might not always
be available to DASH clients. Services <span class=modal-keyword>may</span> define the
`MPD@suggestedPresentationDelay` attribute to provide a suggested presentation
delay. Clients <span class=modal-keyword>should</span> use `MPD@suggestedPresentationDelay` when provided by the MPD.

<figure>
  <img src="images/WindowInteractions.png" />
  <figcaption>The interaction between availability window, time shift buffer, and
  presentation delay determines which Media Segments can be presented at any given
  time.</figcaption>
</figure>
"""

def main():
    # Path to the file to modify - use absolute path
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    file_path = repo_root / "specs" / "part04-live-low-latency" / "00-live-services.inc.md"
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        return 1
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find the insertion point (after line 178, before line 180)
    # Looking for the line with "SegmentTemplate` with `SegmentTimeline`."
    insertion_index = None
    for i, line in enumerate(lines):
        if "`SegmentTemplate` with `SegmentTimeline`." in line:
            # Insert after the blank line following this line
            insertion_index = i + 2  # Skip the line and the blank line after it
            break
    
    if insertion_index is None:
        print("Error: Could not find insertion point")
        return 1
    
    print(f"Found insertion point at line {insertion_index + 1}")
    
    # Insert the content
    new_lines = lines[:insertion_index] + [PHASE6_CONTENT] + lines[insertion_index:]
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"Successfully integrated Phase 6 content into {file_path}")
    print(f"Added ~150 lines with 3 sections and 3 diagrams")
    return 0

if __name__ == "__main__":
    sys.exit(main())