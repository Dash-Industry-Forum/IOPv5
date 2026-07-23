# Phase 4 Implementation Plan: Core Timing Expansion

**Date:** 2026-07-23  
**Status:** Ready for Implementation  
**Priority:** High  
**Estimated Effort:** 3-4 hours

## Objective

Integrate essential timing concepts from Guidelines-TimingModel into Part 2 (Core CMAF), focusing on representation timing, sample timelines, segment availability, and clock synchronization.

## Content to Integrate

### 1. Representation Timing (Section 2.4.4)

**Source:** Guidelines-TimingModel 21-Timing.inc.md lines 113-174

**Key Concepts:**
- Representations as sequences of media segments
- Segment references
- Sample timeline definition and mapping to MPD timeline
- Timescale units
- Presentation time offset (@presentationTimeOffset)

**Diagrams:**
- TimelineAlignment.png (line 150)
- PresentationTimeOffset.png (line 167)

**Content (~60 lines):**
```markdown
## Representation Timing ## {#representation-timing}

Representations provide the content for periods. A representation is a sequence of media segments, an initialization segment, an optional index segment and related metadata (see ISO/IEC 23009-1 [[!MPEGDASH]] clauses 5.3.1 and 5.3.5).

The MPD describes each representation using a `Representation` element. For each representation, the MPD defines a set of <dfn>segment references</dfn> to the media segments and metadata describing the media samples provided by the representation.

### Sample Timeline ### {#timing-sampletimeline}

The samples within a representation exist on a linear <dfn>sample timeline</dfn> defined by the encoder that creates the samples. Sample timelines are mapped onto the MPD timeline by metadata stored in or referenced by the MPD (see ISO/IEC 23009-1 [[!MPEGDASH]] clause 7.3.2).

[Figure: TimelineAlignment.png]

The sample timeline does not determine what samples are presented. It merely connects the timing of the representation to the MPD timeline and allows the correct media segments to be identified when a DASH client makes scheduling decisions driven by the MPD timeline.

The same sample timeline <span class=modal-keyword>shall</span> be shared by all representations in the same adaptation set [[!MPEGCMAF]]. Representations in different adaptation sets <span class=modal-keyword>may</span> use different sample timelines.

A sample timeline is measured in <dfn>timescale units</dfn> defined as a number of units per second. This value (the <dfn>timescale</dfn>) <span class=modal-keyword>shall</span> be present in the MPD as `SegmentTemplate@timescale` or `SegmentBase@timescale` (depending on the addressing mode).

[Figure: PresentationTimeOffset.png]

The zero point of a sample timeline <span class=modal-keyword>may</span> be at the start of the period or at any earlier point. The point on the sample timeline indicated by `@presentationTimeOffset` is equivalent to the period start point on the MPD timeline (see ISO/IEC 23009-1 [[!MPEGDASH]] clause 5.3.9.2).

Note: To transform a sample timeline position `SampleTime` to an MPD timeline position, use the formula `MpdTime = Period@start + (SampleTime - @presentationTimeOffset) / @timescale`.

See the DASH-IF Guidelines-TimingModel document [[DASHIF-TIMING]] for detailed discussion of sample timeline mechanics.
```

### 2. Segment References (Section 2.4.5)

**Source:** Guidelines-TimingModel 21-Timing.inc.md lines 175-206

**Key Concepts:**
- Segment references addressing media segments
- Time span on sample timeline
- Necessary segment references in static presentations
- Necessary segment references in dynamic presentations
- Time shift buffer interaction

**Diagrams:**
- StaticMpdMustBeCovered.png (line 190)
- MandatorySegmentReferencesInDynamicMpd.png (line 199)

**Content (~30 lines):**
```markdown
### Referencing Media Segments ### {#timing-segment-references}

Each segment reference addresses a media segment that corresponds to a specific time span on the sample timeline. The exact mechanism used to define segment references depends on the addressing mode used by the representation.

#### Necessary Segment References in Static Presentations #### {#necessary-references-static}

In a static presentation, a representation <span class=modal-keyword>shall</span> provide enough media segments to cover the entire time span of the period.

[Figure: StaticMpdMustBeCovered.png]

#### Necessary Segment References in Dynamic Presentations #### {#necessary-references-dynamic}

In a dynamic presentation, a representation <span class=modal-keyword>shall</span> provide enough media segments to cover the time span of the period that intersects with the time shift buffer at any point during the MPD validity duration.

[Figure: MandatorySegmentReferencesInDynamicMpd.png]

Note: It is a valid and common situation that a media segment is required to be referenced but is not yet available. See ISO/IEC 23009-1 [[!MPEGDASH]] for segment availability timing rules.

See the DASH-IF Guidelines-TimingModel document [[DASHIF-TIMING]] for detailed discussion of segment reference requirements.
```

### 3. Clock Drift (Section 2.4.6)

**Source:** Guidelines-TimingModel 21-Timing.inc.md lines 237-270

**Key Concepts:**
- Clock drift definition and problems
- Encoder clock tracking requirements
- Detection methods
- Workarounds (if encoder cannot be fixed)

**Diagrams:**
- ClockDrift.png (line 242)

**Content (~35 lines):**
```markdown
### Clock Drift ### {#no-clock-drift}

Some encoders experience clock drift - they do not produce exactly 1 second worth of output per 1 second of input, either stretching or compressing the sample timeline with respect to the MPD timeline.

[Figure: ClockDrift.png]

Clock drift not only causes timing model violations when an insufficient amount of data is produced but also leads to de-synchronization of content in tracks encoded based on different clocks. CMAF [[!MPEGCMAF]] clauses 6.3 and 6.6.8 require tracks to be synchronized.

A DASH service <span class=modal-keyword>shall not</span> publish content that suffers from clock drift.

The solution is to adjust the encoder so that it correctly tracks wall clock time, e.g. by performing regular small adjustments to the encoder clock to counteract any "natural" drift it may be experiencing.

#### Workarounds for Clock Drift #### {#clock-drift-workarounds}

If the encoder cannot be adjusted to not suffer from clock drift, DASH packagers <span class=modal-keyword>should</span> implement workarounds to ensure the presentation conforms to targeted standards. The following are examples of approaches a DASH packager could use:

1. Drop a span of content if input is produced faster than real-time.
2. Insert regular padding content if input is produced slower than real-time (silence, blank picture, repeating frames, or short-duration periods where affected representations are not present).

Such workarounds can be disruptive and only serve as a backstop to prevent complete playback failure caused by timing model violations.

See the DASH-IF Guidelines-TimingModel document [[DASHIF-TIMING]] for detailed discussion of clock drift issues and solutions.
```

### 4. Clock Synchronization (Section 2.4.7)

**Source:** Guidelines-TimingModel 21-Timing.inc.md lines 384-400

**Key Concepts:**
- Wall clock definition
- Synchronization requirements for dynamic presentations
- UTCTiming elements
- Client synchronization requirements

**Content (~20 lines):**
```markdown
### Clock Synchronization ### {#clock-sync}

During playback of dynamic presentations, a <dfn>wall clock</dfn> is used as the timing reference for DASH client decisions. This is a synchronized clock shared by the DASH client and service.

It is critical to synchronize the clocks of the DASH client and service when using a dynamic presentation because the MPD timeline of a dynamic presentation is mapped to wall clock time and many playback decisions are clock driven.

Clock synchronization mechanisms are described by `UTCTiming` elements in the MPD (see ISO/IEC 23009-1 [[!MPEGDASH]] clause 5.8.4.11).

The MPD of a dynamic presentation <span class=modal-keyword>shall</span> include at least one `UTCTiming` element that defines a clock synchronization mechanism.

A client presenting a dynamic presentation <span class=modal-keyword>shall</span> synchronize its local clock according to the `UTCTiming` elements in the MPD and <span class=modal-keyword>shall</span> emit a warning or error to application developers when clock synchronization fails.

A DASH client <span class=modal-keyword>shall not</span> use a synchronization method that is not listed in the MPD unless explicitly instructed to do so by the application developer.

See Part 4 for detailed requirements on clock synchronization in live services. See the DASH-IF Guidelines-TimingModel document [[DASHIF-TIMING]] for comprehensive discussion of clock synchronization.
```

## Diagrams to Copy

Copy the following diagrams from Guidelines-TimingModel to Part 2:

1. **TimelineAlignment.png** → `specs/part02-core-cmaf/images/TimelineAlignment.png`
   - Source: `../Guidelines-TimingModel/Images/Timing/TimelineAlignment.png`
   
2. **PresentationTimeOffset.png** → `specs/part02-core-cmaf/images/PresentationTimeOffset.png`
   - Source: `../Guidelines-TimingModel/Images/Timing/PresentationTimeOffset.png`
   
3. **StaticMpdMustBeCovered.png** → `specs/part02-core-cmaf/images/StaticMpdMustBeCovered.png`
   - Source: `../Guidelines-TimingModel/Images/Timing/StaticMpdMustBeCovered.png`
   
4. **MandatorySegmentReferencesInDynamicMpd.png** → `specs/part02-core-cmaf/images/MandatorySegmentReferencesInDynamicMpd.png`
   - Source: `../Guidelines-TimingModel/Images/Timing/MandatorySegmentReferencesInDynamicMpd.png`
   
5. **ClockDrift.png** → `specs/part02-core-cmaf/images/ClockDrift.png`
   - Source: `../Guidelines-TimingModel/Images/Timing/ClockDrift.png`

## Integration Location

Add to `specs/part02-core-cmaf/01-core-cmaf.inc.md` after the existing Section 2.4.3 (First and Last Period Timing):

```
## DASH Timing Model ## {#timing-model}

### MPD Timeline ### {#timing-mpd-timeline}
[Existing content from Phase 1]

### Period Timing ### {#timing-period}
[Existing content from Phase 1]

### First and Last Period Timing ### {#timing-first-last-period}
[Existing content from Phase 1]

### Representation Timing ### {#representation-timing}
[NEW - Phase 4 content]

### Referencing Media Segments ### {#timing-segment-references}
[NEW - Phase 4 content]

### Clock Drift ### {#no-clock-drift}
[NEW - Phase 4 content]

### Clock Synchronization ### {#clock-sync}
[NEW - Phase 4 content]
```

## ISO/IEC 23009-1 Cross-References to Add

Throughout the new content, add specific references to ISO/IEC 23009-1:
- Clause 5.3.1: Representation element
- Clause 5.3.5: Segment information
- Clause 5.3.9.2: presentationTimeOffset
- Clause 5.8.4.11: UTCTiming
- Clause 7.2.1: Period boundaries
- Clause 7.3.2: Sample timeline mapping

## Precedence Rule Verification

Before integration, verify:
1. ✅ No conflicts with ISO/IEC 23009-1 normative requirements
2. ✅ Content supplements (not replaces) existing Part 2 text
3. ✅ Content accurately reflects Guidelines-TimingModel source
4. ✅ Modal verbs (shall/should/may) used correctly

## Implementation Steps

1. **Copy diagrams** (5 files)
   ```bash
   cp ../Guidelines-TimingModel/Images/Timing/TimelineAlignment.png \
      IOPv5-tstock-worktree/rag-authoring-starter/specs/part02-core-cmaf/images/
   # Repeat for other 4 diagrams
   ```

2. **Integrate content** into `01-core-cmaf.inc.md`
   - Add 4 new subsections after Section 2.4.3
   - Total ~145 lines of new content
   - Include all 5 diagrams with proper figure captions

3. **Add ISO/IEC 23009-1 references**
   - Add [[!MPEGDASH]] references with specific clause numbers
   - Ensure cross-references to Part 4 for live-specific content

4. **Test Bikeshed build**
   ```bash
   cd IOPv5-tstock-worktree/rag-authoring-starter
   bikeshed spec specs/part02-core-cmaf/part02-core-cmaf.bs
   ```

5. **Commit work**
   ```bash
   git add specs/part02-core-cmaf/
   git commit -m "Phase 4: Integrate core timing expansion into Part 2

- Added Representation Timing section with sample timeline concepts
- Added Segment References section with static/dynamic requirements
- Added Clock Drift section with detection and workarounds
- Added Clock Synchronization section with UTCTiming requirements
- Integrated 5 diagrams: TimelineAlignment, PresentationTimeOffset, 
  StaticMpdMustBeCovered, MandatorySegmentReferencesInDynamicMpd, ClockDrift
- Added comprehensive ISO/IEC 23009-1 cross-references

Source: Guidelines-TimingModel 21-Timing.inc.md lines 113-400
Total: ~145 lines, 5 diagrams
Follows precedence rule: ISO/IEC 23009-1 > existing IOP v5 > Guidelines-TimingModel"
   ```

## Success Criteria

Phase 4 will be considered complete when:
- ✅ All 5 diagrams copied and displaying correctly
- ✅ All 4 new subsections integrated into Part 2
- ✅ ISO/IEC 23009-1 references added throughout
- ✅ Bikeshed builds successfully
- ✅ Content verified against precedence rule
- ✅ Work committed and pushed to branch

## Next Phase

After Phase 4 completion, proceed to **Phase 5: Advanced Addressing** which will add:
- Presentation time offset mechanics (expanded)
- Timeline alignment details
- Explicit addressing details
- Simple addressing details
- 4 additional diagrams

## Notes

- Phase 4 focuses on core timing concepts that are essential for understanding DASH timing model
- Content is carefully selected to avoid duplication with Part 4 (Live) content
- Clock synchronization section provides foundation, with Part 4 providing live-specific details
- All content maintains consistency with existing Phase 1-3 integration