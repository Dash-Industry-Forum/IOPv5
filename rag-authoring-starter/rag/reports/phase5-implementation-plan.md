# Phase 5 Implementation Plan: Part 2 Multi-Period Content

**Date:** 2026-07-23  
**Status:** Ready for Implementation  
**Priority:** High  
**Estimated Effort:** 4-5 hours

## Objective

Integrate multi-period timing concepts from Guidelines-TimingModel into Part 2 (Core CMAF), focusing on period connectivity, period boundaries, non-equal length tracks, and period splitting strategies.

## Content to Integrate

### 1. Period Connectivity (Section 2.4.8)

**Source:** Guidelines-TimingModel 21-Timing.inc.md (to be located)

**Key Concepts:**
- Period-connected vs period-disconnected representations
- Continuous playback across period boundaries
- Decoder state preservation
- Switching set continuity

**Diagrams:**
- PeriodConnectivity.png
- SegmentOverlapOnPeriodConnectivity.png

**Content:** ~40-50 lines

### 2. Samples on Period Boundaries (Section 2.4.9)

**Source:** Guidelines-TimingModel 21-Timing.inc.md (to be located)

**Key Concepts:**
- Sample alignment at period boundaries
- Presentation time continuity
- Decode time handling
- Random access point requirements

**Diagrams:**
- SamplesOnPeriodBoundary.png

**Content:** ~30-40 lines

### 3. Non-Equal Length Tracks (Section 2.4.10)

**Source:** Guidelines-TimingModel 21-Timing.inc.md (to be located)

**Key Concepts:**
- Handling tracks of different durations
- Padding strategies
- Cutting strategies
- Period splitting strategies
- Mixed approaches

**Diagrams:**
- NonequalLengthTracks - Initial.png
- NonequalLengthTracks - PadEverything.png
- NonequalLengthTracks - CutEverything.png
- NonequalLengthTracks - MakePeriods.png
- NonequalLengthTracks - Mix.png

**Content:** ~60-80 lines

### 4. Period Splitting (Section 2.4.11)

**Source:** Guidelines-TimingModel 21-Timing.inc.md (to be located)

**Key Concepts:**
- When to split periods
- How to split periods
- Maintaining continuity
- Decoder compatibility

**Diagrams:**
- SplitInTwoPeriods - Before.png
- SplitInTwoPeriods - After.png

**Content:** ~30-40 lines

## Diagrams to Copy

Copy the following diagrams from Guidelines-TimingModel to Part 2:

1. **PeriodConnectivity.png** → `specs/part02-core-cmaf/images/PeriodConnectivity.png`
   - Source: `../Guidelines-TimingModel/Images/Timing/PeriodConnectivity.png`
   
2. **SegmentOverlapOnPeriodConnectivity.png** → `specs/part02-core-cmaf/images/SegmentOverlapOnPeriodConnectivity.png`
   - Source: `../Guidelines-TimingModel/Images/Timing/SegmentOverlapOnPeriodConnectivity.png`
   
3. **SamplesOnPeriodBoundary.png** → `specs/part02-core-cmaf/images/SamplesOnPeriodBoundary.png`
   - Source: `../Guidelines-TimingModel/Images/Timing/SamplesOnPeriodBoundary.png`
   
4. **NonequalLengthTracks - Initial.png** → `specs/part02-core-cmaf/images/NonequalLengthTracks-Initial.png`
   - Source: `../Guidelines-TimingModel/Images/Timing/NonequalLengthTracks - Initial.png`
   
5. **NonequalLengthTracks - PadEverything.png** → `specs/part02-core-cmaf/images/NonequalLengthTracks-PadEverything.png`
   - Source: `../Guidelines-TimingModel/Images/Timing/NonequalLengthTracks - PadEverything.png`
   
6. **NonequalLengthTracks - CutEverything.png** → `specs/part02-core-cmaf/images/NonequalLengthTracks-CutEverything.png`
   - Source: `../Guidelines-TimingModel/Images/Timing/NonequalLengthTracks - CutEverything.png`
   
7. **NonequalLengthTracks - MakePeriods.png** → `specs/part02-core-cmaf/images/NonequalLengthTracks-MakePeriods.png`
   - Source: `../Guidelines-TimingModel/Images/Timing/NonequalLengthTracks - MakePeriods.png`
   
8. **NonequalLengthTracks - Mix.png** → `specs/part02-core-cmaf/images/NonequalLengthTracks-Mix.png`
   - Source: `../Guidelines-TimingModel/Images/Timing/NonequalLengthTracks - Mix.png`
   
9. **SplitInTwoPeriods - Before.png** → `specs/part02-core-cmaf/images/SplitInTwoPeriods-Before.png`
   - Source: `../Guidelines-TimingModel/Images/Timing/SplitInTwoPeriods - Before.png`
   
10. **SplitInTwoPeriods - After.png** → `specs/part02-core-cmaf/images/SplitInTwoPeriods-After.png`
    - Source: `../Guidelines-TimingModel/Images/Timing/SplitInTwoPeriods - After.png`

**Note:** Diagram filenames with spaces need to be renamed to use hyphens for web compatibility.

## Integration Location

Add to `specs/part02-core-cmaf/01-core-cmaf.inc.md` after Section 2.4.7 (Clock Synchronization):

```
### Clock Synchronization ### {#clock-sync}
[Existing Phase 4 content]

### Period Connectivity ### {#period-connectivity}
[NEW - Phase 5 content]

### Samples on Period Boundaries ### {#samples-on-period-boundaries}
[NEW - Phase 5 content]

### Non-Equal Length Tracks ### {#non-equal-length-tracks}
[NEW - Phase 5 content]

### Period Splitting ### {#period-splitting}
[NEW - Phase 5 content]

## DASH Representation Structures and Signalling ## {#representation-structures}
[Existing content continues]
```

## ISO/IEC 23009-1 Cross-References to Add

Throughout the new content, add specific references to ISO/IEC 23009-1:
- Clause 5.3.2: Period element
- Clause 5.3.2.1: Period start and duration
- Clause 7.2.1: Period boundaries
- Clause 7.2.2: Period connectivity
- Any other relevant clauses discovered during content review

## CMAF Cross-References to Add

Add references to ISO/IEC 23000-19 (CMAF):
- Clause 7.3.4: CMAF switching set
- Clause 7.3.5: CMAF selection set
- Any other relevant clauses for track continuity

## Precedence Rule Verification

Before integration, verify:
1. ✅ No conflicts with ISO/IEC 23009-1 normative requirements
2. ✅ Content supplements (not replaces) existing Part 2 text
3. ✅ Content accurately reflects Guidelines-TimingModel source
4. ✅ Modal verbs (shall/should/may) used correctly

## Implementation Steps

### Step 1: Locate Source Content (30 minutes)

Search Guidelines-TimingModel for multi-period content:

```bash
# Search for period-related content
grep -n "period" Guidelines-TimingModel/21-Timing.inc.md
grep -n "connectivity" Guidelines-TimingModel/21-Timing.inc.md
grep -n "boundary" Guidelines-TimingModel/21-Timing.inc.md
```

Read relevant sections to identify exact line numbers for each topic.

### Step 2: Copy Diagrams (15 minutes)

```bash
cd IOPv5-tstock-worktree/rag-authoring-starter

# Copy all 10 diagrams
cp "../../../Guidelines-TimingModel/Images/Timing/PeriodConnectivity.png" \
   "specs/part02-core-cmaf/images/"

cp "../../../Guidelines-TimingModel/Images/Timing/SegmentOverlapOnPeriodConnectivity.png" \
   "specs/part02-core-cmaf/images/"

cp "../../../Guidelines-TimingModel/Images/Timing/SamplesOnPeriodBoundary.png" \
   "specs/part02-core-cmaf/images/"

# Copy and rename NonequalLengthTracks diagrams (spaces to hyphens)
cp "../../../Guidelines-TimingModel/Images/Timing/NonequalLengthTracks - Initial.png" \
   "specs/part02-core-cmaf/images/NonequalLengthTracks-Initial.png"

cp "../../../Guidelines-TimingModel/Images/Timing/NonequalLengthTracks - PadEverything.png" \
   "specs/part02-core-cmaf/images/NonequalLengthTracks-PadEverything.png"

cp "../../../Guidelines-TimingModel/Images/Timing/NonequalLengthTracks - CutEverything.png" \
   "specs/part02-core-cmaf/images/NonequalLengthTracks-CutEverything.png"

cp "../../../Guidelines-TimingModel/Images/Timing/NonequalLengthTracks - MakePeriods.png" \
   "specs/part02-core-cmaf/images/NonequalLengthTracks-MakePeriods.png"

cp "../../../Guidelines-TimingModel/Images/Timing/NonequalLengthTracks - Mix.png" \
   "specs/part02-core-cmaf/images/NonequalLengthTracks-Mix.png"

# Copy and rename SplitInTwoPeriods diagrams
cp "../../../Guidelines-TimingModel/Images/Timing/SplitInTwoPeriods - Before.png" \
   "specs/part02-core-cmaf/images/SplitInTwoPeriods-Before.png"

cp "../../../Guidelines-TimingModel/Images/Timing/SplitInTwoPeriods - After.png" \
   "specs/part02-core-cmaf/images/SplitInTwoPeriods-After.png"
```

### Step 3: Integrate Content (3-4 hours)

For each section:

1. **Read source content** from Guidelines-TimingModel
2. **Adapt content** for Part 2 context
3. **Add ISO/IEC 23009-1 references** with specific clause numbers
4. **Add CMAF references** where appropriate
5. **Include diagrams** with proper figure captions
6. **Use replace_in_file** to insert content after Section 2.4.7

**Integration order:**
1. Period Connectivity (~1 hour)
2. Samples on Period Boundaries (~45 minutes)
3. Non-Equal Length Tracks (~1.5 hours)
4. Period Splitting (~45 minutes)

### Step 4: Test Bikeshed Build (15 minutes)

```bash
cd IOPv5-tstock-worktree/rag-authoring-starter
bikeshed --die-on=nothing spec specs/part02-core-cmaf/part02-core-cmaf.bs
```

Review output for errors and warnings.

### Step 5: Commit Work (15 minutes)

```bash
git add specs/part02-core-cmaf/
git commit -m "Phase 5: Multi-period timing integration into Part 2

- Added Period Connectivity section with 2 diagrams
- Added Samples on Period Boundaries section with 1 diagram
- Added Non-Equal Length Tracks section with 5 diagrams
- Added Period Splitting section with 2 diagrams
- Integrated 10 diagrams total
- Added comprehensive ISO/IEC 23009-1 cross-references
- Added CMAF cross-references for track continuity

Source: Guidelines-TimingModel 21-Timing.inc.md
Total: ~160-210 lines, 10 diagrams
Follows precedence rule: ISO/IEC 23009-1 > IOP v5 > Guidelines-TimingModel"

git push origin tstockhammer-rag-workflow
```

## Success Criteria

Phase 5 will be considered complete when:
- ✅ All 10 diagrams copied and displaying correctly
- ✅ All 4 new subsections integrated into Part 2
- ✅ ISO/IEC 23009-1 references added throughout
- ✅ CMAF references added where appropriate
- ✅ Bikeshed builds successfully (or issues documented)
- ✅ Content verified against precedence rule
- ✅ Work committed and pushed to branch

## Next Phase

After Phase 5 completion, proceed to **Phase 6: Part 4 Live Service Content** which will add:
- Availability windows
- Time shift buffer
- Presentation delay
- 3 additional diagrams

## Notes

- Phase 5 is the largest integration phase so far (10 diagrams, ~160-210 lines)
- Multi-period content is complex and requires careful attention to detail
- Content should emphasize practical guidance for content authors
- Examples and use cases should be included where helpful
- Cross-references to Part 5 (Ad Insertion) may be appropriate for some multi-period scenarios

## Time Breakdown

- **Step 1:** Locate source content - 30 minutes
- **Step 2:** Copy diagrams - 15 minutes
- **Step 3:** Integrate content - 3-4 hours
  - Period Connectivity: 1 hour
  - Samples on Period Boundaries: 45 minutes
  - Non-Equal Length Tracks: 1.5 hours
  - Period Splitting: 45 minutes
- **Step 4:** Test build - 15 minutes
- **Step 5:** Commit work - 15 minutes

**Total:** 4.5-5.5 hours

## Preparation Checklist

Before starting Phase 5 execution:
- [ ] Review this implementation plan
- [ ] Ensure Guidelines-TimingModel repository is accessible
- [ ] Verify all diagram files exist in source location
- [ ] Check Part 2 current state (should end with Section 2.4.7)
- [ ] Confirm git branch is up to date
- [ ] Allocate 4-5 hours of uninterrupted time

## Risk Mitigation

**Risk:** Source content location unclear
- **Mitigation:** Use grep/search to locate content before starting integration

**Risk:** Diagrams have spaces in filenames
- **Mitigation:** Rename during copy to use hyphens (already planned)

**Risk:** Content overlaps with Part 5 (Ad Insertion)
- **Mitigation:** Focus on general multi-period concepts, defer ad-specific content to Part 5

**Risk:** Time estimate too optimistic
- **Mitigation:** Can split into Phase 5A and 5B if needed (2 sections each)

## Alternative: Split into Two Phases

If 4-5 hours is too long for a single session, consider splitting:

**Phase 5A: Period Connectivity and Boundaries (2-2.5 hours)**
- Period Connectivity (2 diagrams)
- Samples on Period Boundaries (1 diagram)
- Total: 3 diagrams, ~70-90 lines

**Phase 5B: Track Length and Splitting (2-2.5 hours)**
- Non-Equal Length Tracks (5 diagrams)
- Period Splitting (2 diagrams)
- Total: 7 diagrams, ~90-120 lines

This approach provides natural breakpoints and allows for progress validation between phases.

## Status

**Created:** 2026-07-23  
**Status:** Ready for execution  
**Dependencies:** Phase 4 complete  
**Estimated Start:** Next session  
**Estimated Completion:** 4-5 hours after start