# Guidelines-TimingModel integration session summary

Generated: 2026-07-22

This document summarizes the work completed in the Guidelines-TimingModel integration session and outlines the remaining work.

## Session accomplishments

### 1. Cloned Guidelines-TimingModel repository

**Location:** `c:\Users\tsto\OneDrive - Qualcomm\Projects\DASH-IF\Guidelines-TimingModel`

**Content reviewed:**
- 01-Intro.inc.md (Purpose, interpretation, terminology)
- 21-Timing.inc.md (MPD timeline, period timing)
- 22-Addressing.inc.md (Segment addressing modes)

### 2. Created comprehensive integration plan

**File:** `rag/reports/guidelines-timing-model-integration-plan.md`

**Key elements:**
- Precedence rule: ISO/IEC 23009-1 > existing IOP v5 text > Guidelines-TimingModel
- Content analysis for Sections 1-3 (Introduction, Timing, Addressing)
- 4-phase execution plan
- No conflicts identified with ISO/IEC 23009-1 or existing IOP v5 text

### 3. Created document porting status map

**File:** `rag/reports/document-porting-status-map.md`

**Tracks:**
- Porting status for all 12 IOP v5 parts
- Validator-start coverage
- Reconciliation report status
- Guidelines-TimingModel integration requirements

### 4. Created Part 2 integration status report

**File:** `rag/reports/part02-timing-model-integration-status.md`

**Tracks:**
- Current Part 2 timing model content
- Guidelines-TimingModel content available for integration
- Integration approach (Steps 1-2)
- Precedence rule verification
- Diagrams to integrate
- Implementation checklist (Phases 1A-1D)

### 5. Completed Phase 1A: Timing model expansion

**Commit:** e78bf8c "Phase 1A: Integrate Guidelines-TimingModel timing model into Part 2"

**Changes:**
- Expanded DASH Timing Model section in Part 2
- Added MPD Timeline subsection with definition and diagram
- Added Period Timing subsection with consecutive/non-overlapping rules
- Added First and Last Period Timing subsection
- Added zero-duration period prohibition
- Added period self-containment rule
- Added cross-references to Parts 3, 4, and 5
- Added DASHIF-TIMING bibliographic reference
- Copied BasicMpdElements.png and PeriodsMakeTheMpd.png diagrams

**Files modified:**
- `specs/part02-core-cmaf/01-core-cmaf.inc.md` (107 insertions, 12 deletions)
- `specs/part02-core-cmaf/part02-core-cmaf.bs` (added DASHIF-TIMING reference)
- `specs/part02-core-cmaf/images/BasicMpdElements.png` (new)
- `specs/part02-core-cmaf/images/PeriodsMakeTheMpd.png` (new)
- `rag/reports/part02-timing-model-integration-status.md` (updated)

---

## Remaining work

### Phase 1B: Segment addressing expansion (NOT STARTED)

**Objective:** Expand Part 2 segment addressing section with detailed addressing mode explanations.

**Tasks:**
1. Read Guidelines-TimingModel 22-Addressing.inc.md (addressing modes overview)
2. Draft addressing modes overview for Part 2
3. Draft indexed addressing subsection for Part 2
4. Draft explicit addressing subsection for Part 2
5. Draft simple addressing subsection for Part 2
6. Copy IndexedAddressing.png diagram to Part 2 images directory
7. Insert expanded segment addressing content into Part 2

**Content to integrate:**

- **Addressing modes overview** (lines 1-27)
  - Three addressing modes: indexed, explicit, simple
  - Addressing mode selection guidance
  - Addressing mode consistency within adaptation set

- **Indexed addressing (SegmentBase)** (lines 28-150)
  - CMAF track file structure
  - Index segment (sidx) requirements
  - Byte-range addressing
  - Initialization segment byte-range
  - sidx box structure and field definitions

- **Explicit addressing (SegmentTemplate + SegmentTimeline)** (lines 151-270)
  - $Time$ or $Number$ substitution
  - SegmentTimeline S element structure
  - Media-time addressing benefits
  - Variable duration support

- **Simple addressing (SegmentTemplate + duration)** (lines 271-350)
  - $Number$ or $Time$ substitution with duration
  - Regular segment duration
  - eptDelta for period start point adjustment
  - Inaccuracy tolerance (±50% of nominal duration)

**Estimated scope:** 150-200 lines of content plus 1 diagram

---

### Phase 1C: Terminology clarification (NOT STARTED)

**Objective:** Add DASH/CMAF/ISOBMFF terminology cross-reference table to Part 2.

**Tasks:**
1. Read Guidelines-TimingModel 01-Intro.inc.md lines 104-140 (terminology)
2. Add DASH/CMAF/ISOBMFF terminology cross-reference table to Part 2 terms section
3. Add editorial note on segment vs subsegment terminology
4. Verify consistency with existing Part 2 terms section

**Content to integrate:**

From Guidelines-TimingModel 01-Intro.inc.md lines 108-130:

| DASH | CMAF | ISOBMFF |
|---|---|---|
| (media) segment, subsegment | CMAF segment, CMAF fragment | |
| initialization segment | CMAF header | |
| index segment, segment index | | segment index box (sidx) |

**Estimated scope:** 20-30 lines of content

---

### Phase 1D: Validation and commit (NOT STARTED)

**Objective:** Validate integrated content and create reconciliation report.

**Tasks:**
1. Run check_links.py to verify modal verb usage
2. Regenerate Part 2 output document
3. Create Part 2 reconciliation report (similar to Parts 5, 6, 9)
4. Update document-porting-status-map.md to reflect Phase 1 completion
5. Commit and push Phase 1 integration

**Estimated scope:** Validation and documentation work

---

### Phase 2: Part 3 On-Demand timing constraints (NOT STARTED)

**Objective:** Add static presentation timing constraints to Part 3.

**Tasks:**
1. Read current Part 3 content to identify gaps
2. Add first/last period timing rules for static presentations
3. Cross-reference Part 2 timing model foundation
4. Cross-reference Guidelines-TimingModel for detailed timing model discussion

**Content already available in Guidelines-TimingModel:**
- First period starts at zero (line 84)
- Last period has duration (line 86)

**Estimated scope:** 30-50 lines of content

---

### Phase 3: Part 4 Live/Low-Latency timing constraints (NOT STARTED)

**Objective:** Add dynamic presentation timing constraints to Part 4.

**Tasks:**
1. Read current Part 4 content to identify gaps
2. Add first/last period timing rules for dynamic presentations
3. Add effective availability start time and leap second handling
4. Add segment availability window discussion (if not already present)
5. Cross-reference Part 2 timing model foundation
6. Cross-reference Guidelines-TimingModel for detailed timing model discussion

**Content already available in Guidelines-TimingModel:**
- First period starts at/after zero (line 90)
- Last period may have unlimited duration (line 92)
- Effective availability start time (line 37)
- Leap second handling (line 37)

**Estimated scope:** 50-80 lines of content

---

## Summary statistics

**Total commits:** 3
- Document porting status map and integration plan
- Part 2 timing model integration status report
- Phase 1A: Timing model expansion

**Total files modified:** 8
- 3 planning/status reports
- 2 Part 2 source files
- 2 Part 2 diagrams
- 1 integration status report

**Total lines added:** ~450 lines (planning + content)

**Completion status:**
- Phase 1A: ✓ COMPLETE (100%)
- Phase 1B: NOT STARTED (0%)
- Phase 1C: NOT STARTED (0%)
- Phase 1D: NOT STARTED (0%)
- Phase 2: NOT STARTED (0%)
- Phase 3: NOT STARTED (0%)

**Overall progress:** ~25% of Guidelines-TimingModel integration complete

---

## Next session recommendations

1. **Complete Phase 1B:** Expand segment addressing section (highest priority)
2. **Complete Phase 1C:** Add terminology clarification
3. **Complete Phase 1D:** Validate and create reconciliation report
4. **Begin Phase 2:** Part 3 On-Demand timing constraints
5. **Begin Phase 3:** Part 4 Live/Low-Latency timing constraints

**Estimated remaining work:** 3-4 hours to complete Phases 1B-1D, 2-3 hours for Phases 2-3

---

## Key achievements

1. **Established precedence rule framework** - Clear guidance on how to handle conflicts
2. **Created comprehensive integration plan** - Detailed roadmap for all phases
3. **Successfully integrated timing model foundation** - Part 2 now has solid MPD timeline and period timing explanations
4. **No conflicts identified** - All integrated content aligns with ISO/IEC 23009-1 and existing IOP v5 text
5. **Established integration workflow** - Repeatable process for future integration work

---

## References

- Guidelines-TimingModel repository: `c:\Users\tsto\OneDrive - Qualcomm\Projects\DASH-IF\Guidelines-TimingModel`
- Integration plan: `rag/reports/guidelines-timing-model-integration-plan.md`
- Part 2 integration status: `rag/reports/part02-timing-model-integration-status.md`
- Document porting status map: `rag/reports/document-porting-status-map.md`
- Branch: tstockhammer-rag-workflow
- Latest commit: e78bf8c