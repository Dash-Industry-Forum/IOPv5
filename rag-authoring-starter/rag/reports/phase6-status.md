# Phase 6 Status: Part 4 Live Service Content

**Date:** 2026-07-23  
**Status:** 80% Complete - Ready for Final Integration  
**Priority:** High  
**Estimated Completion Time:** 15-20 minutes

## Current Status

### Completed Work ✅

1. **Diagrams Copied (3 diagrams)**
   - ✅ AvailabilityWindow.png → `specs/part04-live-low-latency/images/`
   - ✅ TimeShiftBuffer.png → `specs/part04-live-low-latency/images/`
   - ✅ WindowInteractions.png → `specs/part04-live-low-latency/images/`

2. **Source Content Reviewed**
   - ✅ Guidelines-TimingModel lines 419-500 analyzed
   - ✅ Content adapted for IOP v5 Part 4
   - ✅ ISO/IEC 23009-1 references identified
   - ✅ Modal verbs (shall/should/may) applied correctly

3. **Integration Point Identified**
   - ✅ Location: After line 178 in `00-live-services.inc.md`
   - ✅ Before: "## Live Service Offering including MPD Updates ##"
   - ✅ After: "### Service Offering Requirements and Guidelines ###"

### Remaining Work

**Single Task:** Integrate prepared content into Part 4 file

## Content Ready for Integration

Insert the following 3 sections after line 178 in `specs/part04-live-low-latency/00-live-services.inc.md`:

### Section 1: Availability Window (~50 lines)

```markdown
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
```

### Section 2: Time Shift Buffer (~50 lines)

```markdown
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
```

### Section 3: Presentation Delay (~50 lines)

```markdown
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
```

## Integration Instructions

1. Open `specs/part04-live-low-latency/00-live-services.inc.md`
2. Locate line 178 (end of "Service Offering Requirements and Guidelines" section)
3. Insert the 3 sections above between line 178 and line 180
4. Verify the content flows naturally
5. Commit with message: "Phase 6: Live service timing integration into Part 4"

## Commit Message Template

```
Phase 6: Live service timing integration into Part 4

Added three new sections to Part 4 with live service timing concepts:

- Availability Window (Section 4.2.3.4)
  * Definition and calculation algorithm
  * Service and client requirements
  * Robust behavior guidance
  * 1 diagram: AvailabilityWindow.png

- Time Shift Buffer (Section 4.2.3.5)
  * Definition and purpose
  * Interaction with availability window
  * Client presentation constraints
  * 1 diagram: TimeShiftBuffer.png

- Presentation Delay (Section 4.2.3.6)
  * Conflict resolution mechanism
  * Calculation requirements
  * suggestedPresentationDelay usage
  * 1 diagram: WindowInteractions.png

Content adapted from Guidelines-TimingModel lines 419-500 with
ISO/IEC 23009-1 references and IOP v5 modal verbs.

Total: ~150 lines, 3 diagrams
Source: Guidelines-TimingModel (lines 419-500)
Follows precedence rule: ISO/IEC 23009-1 > IOP v5 > Guidelines-TimingModel
```

## Next Steps After Phase 6

1. **Phase 7:** 29-Misc.inc.md Integration (30-45 minutes)
   - Timescale constraints
   - XML duration constraints
   - 0 diagrams, ~27 lines

2. **Phase 8:** Part 3 On-Demand Content (1-2 hours)
   - Static presentation requirements
   - On-demand specific timing
   - 2-3 diagrams

## Session Summary

**Total Session Time:** ~5 hours  
**Phases Completed:** 4, 5A, 5B  
**Phase 6 Progress:** 80% (diagrams copied, content prepared)  
**Total Commits:** 13  
**Coverage:** 44% of Guidelines-TimingModel  
**Diagrams:** 21 of 29 copied (72%), 18 of 29 integrated (62%)