# Guidelines-TimingModel Integration Gap Analysis

**Date:** 2026-07-23  
**Status:** Phase 1-3 Complete (Limited Scope) - Significant Work Remaining

## Executive Summary

The initial integration (Phases 1-3) successfully established the **foundation** for timing model content in IOP v5, but represents only a **small fraction** (~10-15%) of the total Guidelines-TimingModel content. This document provides a comprehensive gap analysis and roadmap for completing the integration.

## What Was Integrated (Phases 1-3)

### Part 2: Core CMAF
✅ **MPD Timeline** (Section 2.4.1)
- Basic definition and diagram (BasicMpdElements.png)
- ~30 lines of content

✅ **Period Timing** (Section 2.4.2)
- Consecutive/non-overlapping rules
- Diagram (PeriodsMakeTheMpd.png)
- ~40 lines of content

✅ **First and Last Period Timing** (Section 2.4.3)
- Static and dynamic presentation rules
- ~25 lines of content

✅ **Segment Addressing Modes** (Section 2.5)
- Indexed addressing with diagram (IndexedAddressing.png)
- Explicit addressing
- Simple addressing
- ~200 lines of content

✅ **Terminology Cross-Reference** (Section 2.2)
- DASH/CMAF/ISOBMFF mapping table
- ~12 lines of content

**Total Part 2:** ~307 lines, 3 diagrams

### Part 3: On-Demand
✅ **Period Timing** (new section)
- Static presentation constraints
- ~21 lines of content

### Part 4: Live/Low-Latency
✅ **Period Timing** (new section)
- Dynamic presentation constraints
- ~27 lines of content

### Documentation
✅ Integration plan
✅ Status tracking
✅ Reconciliation report
✅ Session summary
✅ PR template

## What's Missing from Guidelines-TimingModel

### Missing Diagrams (26 of 29)

**High Priority (Core Timing Concepts):**
1. ❌ AvailabilityWindow.png - Segment availability timing
2. ❌ TimeShiftBuffer.png - TSB and live edge
3. ❌ WindowInteractions.png - Availability/TSB interactions
4. ❌ PresentationTimeOffset.png - PTO mechanics
5. ❌ TimelineAlignment.png - Multi-period alignment
6. ❌ ClockDrift.png - Client/server synchronization
7. ❌ ExplicitAddressing.png - SegmentTimeline details
8. ❌ SimpleAddressing.png - Template-based addressing

**Medium Priority (Advanced Topics):**
9. ❌ MpdUpdate - AddContent.png - Dynamic MPD updates
10. ❌ MpdUpdate - RemoveContent.png - Content removal
11. ❌ EmsgUpdates.png - Inband MPD signaling
12. ❌ PeriodConnectivity.png - Period boundaries
13. ❌ SegmentOverlapOnPeriodConnectivity.png - Overlap handling
14. ❌ SamplesOnPeriodBoundary.png - Sample alignment
15. ❌ MandatorySegmentReferencesInDynamicMpd.png - Dynamic requirements

**Lower Priority (Edge Cases):**
16. ❌ MissingSegment.png - Gap handling
17. ❌ MissingSegment-FixWithPeriodSplitting.png
18. ❌ MissingSegment-FixWithPlaceholder.png
19. ❌ InaccurateAddressing.png - Timing inaccuracies
20. ❌ StaticMpdMustBeCovered.png - Static coverage rules
21. ❌ SplitInTwoPeriods - Before/After.png - Period splitting
22. ❌ NonequalLengthTracks series (5 diagrams) - Track length handling
23. ❌ KID change.png - DRM key rotation

### Missing Content Sections

**From 21-Timing.inc.md (~841 lines total):**
- ❌ Lines 1-8: Introduction
- ❌ Lines 27-42: Period timing details (partially integrated)
- ❌ Lines 95-200: Segment availability timing (SAST/SAET)
- ❌ Lines 201-300: Time shift buffer
- ❌ Lines 301-400: Presentation time offset
- ❌ Lines 401-500: Period connectivity
- ❌ Lines 501-600: MPD updates
- ❌ Lines 601-700: Clock synchronization
- ❌ Lines 701-800: Advanced topics
- ❌ Lines 801-841: Edge cases

**Estimated missing:** ~750 lines of timing content

**From 22-Addressing.inc.md (~448 lines total):**
- ✅ Lines 1-200: Indexed addressing (integrated)
- ✅ Lines 201-350: Explicit addressing (integrated)
- ✅ Lines 351-448: Simple addressing (integrated)

**Estimated missing:** ~50 lines of addressing details

**From 01-Intro.inc.md:**
- ✅ Lines 104-140: Terminology (integrated)
- ❌ Lines 1-103: Introduction and overview
- ❌ Lines 141-end: Additional concepts

**Estimated missing:** ~150 lines of introductory content

### Missing from Other Guidelines-TimingModel Files
- ❌ 23-Samples.inc.md - Sample timing and alignment
- ❌ 24-Inband.inc.md - Inband events and signaling
- ❌ 25-Examples.inc.md - Worked examples
- ❌ 26-Recommendations.inc.md - Best practices

**Estimated missing:** ~500+ lines

## Total Gap Estimate

| Category | Integrated | Missing | Total | % Complete |
|----------|-----------|---------|-------|------------|
| Content (lines) | ~355 | ~1,450 | ~1,805 | 20% |
| Diagrams | 3 | 26 | 29 | 10% |
| Sections | 8 | ~25 | ~33 | 24% |

**Overall completion: ~15% of Guidelines-TimingModel content**

## Additional Missing Elements

### 1. ISO/IEC 23009-1 References
**Current state:** Minimal references to ISO/IEC 23009-1
**Gap:** Need systematic cross-referencing to:
- Clause 5: MPD structure
- Clause 6: Segment formats
- Clause 7: Media Presentation description semantics
- Annex A: Timing model (normative)
- Annex B: Addressing modes

**Action:** Add [[!MPEGDASH]] references throughout with specific clause numbers

### 2. MPEG DASHSchema Examples
**Current state:** No integration of MPEG DASHSchema examples
**Gap:** The MPEG DASHSchema repository (https://github.com/MPEGGroup/DASHSchema) contains:
- Conformant MPD examples
- Test vectors
- Schema validation examples

**Action:** Review and integrate relevant examples into:
- Part 2: Core timing examples
- Part 3: On-demand examples
- Part 4: Live examples
- Part 12: Conformance test vectors

### 3. Part 12 Structure
**Current state:** Test assertions mixed with conformance tools
**Gap:** Part 12 currently combines:
- Conformance tool descriptions
- Test assertions
- Validation procedures

**Recommendation:** Restructure Part 12:
- **Clause 5:** Conformance Tools (current content)
- **Clause 6:** Test Assertions (new, extracted from current content)
  - 6.1: MPD Conformance Assertions
  - 6.2: Segment Conformance Assertions
  - 6.3: Timing Model Assertions
  - 6.4: Addressing Mode Assertions

### 4. Examples and Test Vectors
**Current state:** Limited examples
**Gap:** Need comprehensive examples for:
- Each addressing mode
- Static vs. dynamic presentations
- Period boundaries
- MPD updates
- Time shift buffer
- Presentation time offset

## Recommended Next Phases

### Phase 4: Core Timing Expansion (High Priority)
**Scope:** Integrate essential timing concepts
**Content:**
- Segment availability timing (SAST/SAET)
- Time shift buffer
- Availability window
- Window interactions
- Clock synchronization

**Diagrams:**
- AvailabilityWindow.png
- TimeShiftBuffer.png
- WindowInteractions.png
- ClockDrift.png

**Target:** Part 2, Section 2.4 expansion
**Estimated effort:** 3-4 hours
**Lines added:** ~200-250

### Phase 5: Advanced Addressing (High Priority)
**Scope:** Complete addressing mode coverage
**Content:**
- Presentation time offset mechanics
- Timeline alignment
- Explicit addressing details
- Simple addressing details

**Diagrams:**
- PresentationTimeOffset.png
- TimelineAlignment.png
- ExplicitAddressing.png
- SimpleAddressing.png

**Target:** Part 2, Section 2.5 expansion
**Estimated effort:** 2-3 hours
**Lines added:** ~150-200

### Phase 6: Period Management (Medium Priority)
**Scope:** Period connectivity and boundaries
**Content:**
- Period connectivity rules
- Segment overlap handling
- Sample alignment on boundaries
- Period splitting strategies

**Diagrams:**
- PeriodConnectivity.png
- SegmentOverlapOnPeriodConnectivity.png
- SamplesOnPeriodBoundary.png
- SplitInTwoPeriods series

**Target:** Part 2, new Section 2.6
**Estimated effort:** 3-4 hours
**Lines added:** ~200-250

### Phase 7: Dynamic Presentation Details (Medium Priority)
**Scope:** MPD updates and live services
**Content:**
- MPD update mechanics
- Content addition/removal
- Inband signaling
- Mandatory segment references

**Diagrams:**
- MpdUpdate - AddContent.png
- MpdUpdate - RemoveContent.png
- EmsgUpdates.png
- MandatorySegmentReferencesInDynamicMpd.png

**Target:** Part 4, Section expansion
**Estimated effort:** 3-4 hours
**Lines added:** ~200-250

### Phase 8: Edge Cases and Best Practices (Lower Priority)
**Scope:** Advanced topics and recommendations
**Content:**
- Missing segment handling
- Inaccurate addressing
- Track length variations
- DRM key rotation
- Best practices

**Diagrams:**
- MissingSegment series
- InaccurateAddressing.png
- NonequalLengthTracks series
- KID change.png

**Target:** Part 2, new Section 2.7 (Advanced Topics)
**Estimated effort:** 4-5 hours
**Lines added:** ~250-300

### Phase 9: Examples and Test Vectors (Medium Priority)
**Scope:** Integrate MPEG DASHSchema examples
**Content:**
- Review MPEG DASHSchema repository
- Select relevant examples
- Integrate into appropriate parts
- Create test vector inventory

**Target:** All parts, examples/ directories
**Estimated effort:** 3-4 hours
**Files added:** 10-15 example MPDs

### Phase 10: Part 12 Restructuring (Medium Priority)
**Scope:** Separate test assertions from tools
**Content:**
- Extract test assertions from Part 12
- Create new Clause 6: Test Assertions
- Organize by category
- Cross-reference to parts

**Target:** Part 12, new structure
**Estimated effort:** 2-3 hours
**Lines reorganized:** ~200-300

### Phase 11: ISO/IEC 23009-1 Cross-Referencing (Ongoing)
**Scope:** Systematic cross-referencing
**Content:**
- Add [[!MPEGDASH]] references throughout
- Include specific clause numbers
- Link to normative annexes
- Ensure precedence rule compliance

**Target:** All parts
**Estimated effort:** 2-3 hours (ongoing)
**References added:** 50-100

## Total Remaining Work Estimate

| Phase | Priority | Effort | Lines | Diagrams |
|-------|----------|--------|-------|----------|
| Phase 4 | High | 3-4h | 200-250 | 4 |
| Phase 5 | High | 2-3h | 150-200 | 4 |
| Phase 6 | Medium | 3-4h | 200-250 | 4 |
| Phase 7 | Medium | 3-4h | 200-250 | 4 |
| Phase 8 | Lower | 4-5h | 250-300 | 10 |
| Phase 9 | Medium | 3-4h | - | - |
| Phase 10 | Medium | 2-3h | 200-300 | - |
| Phase 11 | Ongoing | 2-3h | - | - |
| **Total** | | **22-30h** | **~1,200-1,550** | **26** |

## Precedence Rule Compliance

All future integration work must continue to follow the precedence rule:

**ISO/IEC 23009-1 > existing IOP v5 text > Guidelines-TimingModel**

This means:
1. ✅ Verify no conflicts with ISO/IEC 23009-1
2. ✅ Supplement (not replace) existing IOP v5 content
3. ✅ Accurately reflect Guidelines-TimingModel source
4. ✅ Add cross-references to both standards

## Recommendations

### Immediate Actions (Next Session)
1. **Phase 4:** Integrate core timing concepts (SAST/SAET, TSB, availability window)
2. **Phase 9:** Begin MPEG DASHSchema example review
3. **Phase 11:** Start systematic ISO/IEC 23009-1 cross-referencing

### Short-Term (Next 2-3 Sessions)
1. Complete Phases 4-5 (core timing and advanced addressing)
2. Integrate selected MPEG DASHSchema examples
3. Add comprehensive ISO/IEC 23009-1 references

### Medium-Term (Next 5-10 Sessions)
1. Complete Phases 6-8 (period management, dynamic presentations, edge cases)
2. Restructure Part 12 (separate test assertions)
3. Complete example integration

### Long-Term
1. Maintain alignment with Guidelines-TimingModel updates
2. Incorporate feedback from DASH-IF review
3. Expand examples and test vectors based on community needs

## Success Criteria

The Guidelines-TimingModel integration will be considered complete when:

✅ **Content coverage:** 90%+ of relevant Guidelines-TimingModel content integrated  
✅ **Diagram coverage:** 90%+ of relevant diagrams integrated  
✅ **Cross-references:** Comprehensive ISO/IEC 23009-1 references throughout  
✅ **Examples:** Representative examples from MPEG DASHSchema integrated  
✅ **Structure:** Part 12 restructured with separate test assertions  
✅ **Precedence:** All content verified against precedence rule  
✅ **Review:** DASH-IF technical review complete and feedback addressed

## Conclusion

The initial integration (Phases 1-3) successfully established the foundation, but represents only ~15% of the total Guidelines-TimingModel content. Completing the integration will require an estimated **22-30 hours** of focused work across **8 additional phases**.

The work is well-structured and can be completed incrementally, with each phase adding value independently. Priority should be given to Phases 4-5 (core timing and advanced addressing) as these provide the most immediate benefit to IOP v5 users.