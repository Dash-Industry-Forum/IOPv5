# PR: Guidelines-TimingModel Integration into IOP v5

**Branch:** `tstockhammer-rag-workflow`  
**Target:** `main`  
**Date:** 2026-07-28  
**Commits:** 15 (Phases 1-12)

## Summary

This PR integrates the DASH-IF Guidelines-TimingModel document into IOP v5 Parts 2, 3, 4, and 12. It brings ~95% of the Guidelines-TimingModel content into the normative IOP v5 document set, replacing the previous placeholder references with concrete normative text, diagrams, and conformance mappings.

## What Changed

### Part 2: Core CMAF (01-core-cmaf.inc.md)
**~1,200 lines added, 29 diagrams**

New sections added:
- **Terminology Choices** — explains CMAF vs DASH terminology, MPD timeline concept
- **MPD Timeline** — with `BasicMpdElements.png` diagram
- **Period Timing** — with `PeriodsMakeTheMpd.png` diagram
- **Representation Timing** — sample timeline, PTO, `TimelineAlignment.png`, `PresentationTimeOffset.png`
- **Necessary Segment References** — static (`StaticMpdMustBeCovered.png`) and dynamic (`MandatorySegmentReferencesInDynamicMpd.png`)
- **Clock Drift** — with `ClockDrift.png` diagram
- **Clock Synchronization** — UTCTiming requirements
- **Segment Addressing Modes** — indexed (`IndexedAddressing.png`), explicit, simple
- **Period Connectivity** — with `PeriodConnectivity.png` diagram
- **Segment Overlap on Period Connectivity** — with `SegmentOverlapOnPeriodConnectivity.png`
- **Period Continuity** — `urn:mpeg:dash:period-continuity:2015` signalling
- **Samples on Period Boundaries** — with `SamplesOnPeriodBoundary.png`
- **Non-Equal Length Tracks** — 4 strategies with 5 diagrams
- **Period Splitting** — with `SplitInTwoPeriods-Before/After.png` diagrams
- **Good Multi-Period CMAF Content** — continuous boundary requirements
- **Segment Loss Handling** — with 3 `MissingSegment*.png` diagrams
- **Stand-alone Text Track Timing** — IMSC1/WebVTT timing rules
- **Forbidden Techniques** — `@presentationDuration`, `@availabilityTimeComplete`
- **Timing Constraints** — ECMAScript 2⁵³ limit, xs:duration rules

### Part 3: On-Demand (01-on-demand.inc.md)
**~20 lines added, 1 diagram**

- Added static period coverage diagram (`StaticMpdMustBeCovered.png`) to Period Timing section
- Added cross-reference to Part 2 necessary segment references
- Created `images/` directory with README

### Part 4: Live Services (00-live-services.inc.md)
**~300 lines added, 5 diagrams**

New sections added:
- **Availability Window** — with `AvailabilityWindow.png` diagram
- **Time Shift Buffer** — with `TimeShiftBuffer.png` diagram
- **Presentation Delay** — with `WindowInteractions.png` diagram
- **MPD Snapshot Validity** — `minimumUpdatePeriod` semantics
- **Adding Content to the MPD** — with `MpdUpdate-AddContent.png` diagram
- **Removing Content from the MPD** — `EarliestRemovalPoint` algorithm, with `MpdUpdate-RemoveContent.png`
- **End of Live Content** — end-of-live signalling requirements
- **MPD Refreshes** — conditional GET, refresh logic

### Part 12: Conformance and Reference Tools (01-conformance.inc.md)
**~150 lines added**

New conformance mapping sections:
- **Part 2 core CMAF and timing model** — 10 features mapped to validator checks and test asset expectations
- **Part 3 on-demand service** — 6 features mapped
- **Part 4 live service** — 5 features mapped
- Change history updated to v0.5

### Supporting Files
- `specs/part02-core-cmaf/images/` — 29 PNG diagrams + graphml sources (full Guidelines-TimingModel diagram set)
- `specs/part04-live-low-latency/Images/` — 5 new PNG diagrams
- `specs/part03-on-demand/images/` — README with image copy instructions
- `tools/integrate_phase8.py` — Python integration script
- `rag/reports/` — gap analysis, phase plans, session summaries, status documents

## Source Material

All content is adapted from:
- **DASH-IF Guidelines-TimingModel** (`21-Timing.inc.md`, `22-Addressing.inc.md`, `29-Misc.inc.md`, `01-Intro.inc.md`)

## Precedence Rule Compliance

All content follows the IOP v5 precedence rule:
> **ISO/IEC 23009-1 > existing IOP v5 text > Guidelines-TimingModel**

- No conflicts with ISO/IEC 23009-1 introduced
- Guidelines-TimingModel content supplements (does not replace) existing IOP v5 text
- All normative keywords converted to IOP v5 modal-keyword span format
- ISO/IEC 23009-1 clause references added throughout

## Coverage

| Source file | Lines | Coverage |
|-------------|-------|----------|
| `21-Timing.inc.md` | 841 | ~100% |
| `22-Addressing.inc.md` | 448 | 100% |
| `29-Misc.inc.md` | 27 | 100% |
| `01-Intro.inc.md` | 140 | ~50% (key sections) |
| **Total** | **~1,456** | **~95%** |

## Commit History

1. Phase 1A: Integrate Guidelines-TimingModel timing model into Part 2
2. Phase 1B: Integrate Guidelines-TimingModel segment addressing into Part 2
3. Phase 1C: Add terminology cross-reference to Part 2
4. Phase 1D: Complete Phase 1 validation and documentation
5. Phase 2: Integrate Guidelines-TimingModel static presentation timing into Part 3
6. Phase 3: Integrate Guidelines-TimingModel dynamic presentation timing into Part 4
7. Add comprehensive PR template for Guidelines-TimingModel integration
8. Add gap analysis and Phase 4 implementation plan
9. Phase 4: Core timing expansion into Part 2
10. Phase 5A: Period connectivity and boundary timing integration
11. Phase 5B: Non-equal length tracks and period splitting integration
12. Phase 6: Live service timing integration into Part 4
13. Phase 7: Timing constraints integration into Part 2
14. Phase 6-9: Live service timing, MPD updates, segment loss, forbidden techniques
15. Phase 10: Terminology choices + diagram images
16. Phase 11: Part 12 conformance mappings for Part 2 and Part 4
17. Phase 12: Part 3 conformance mapping + Part 3 enhancement

## Review Notes

- The `images/` directory in Part 3 requires `StaticMpdMustBeCovered.png` to be copied from Part 2 (see `images/README.md`)
- Several open issues remain in Parts 2, 3, and 4 (marked with `Issue:` annotations) — these are intentional placeholders for future editorial work
- The Part 2 local validator (`tools/validation/validate_part2_core_cmaf_mpd.py`) should be updated to cover the 10 new timing model checks defined in the Part 12 conformance mapping

## Related Issues

- Guidelines-TimingModel integration tracking
- Part 2 open issues: SegmentTemplate parameter table, segment-list computation formulae
- Part 3 open issues: On-demand profile URI, sidx constraints, trick modes
- Part 4 open issues: Live-to-VoD conversion guidance