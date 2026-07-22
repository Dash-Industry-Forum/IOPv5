# Part 2 timing model integration status

Generated: 2026-07-22

This report tracks the integration of Guidelines-TimingModel content into Part 2 Core CMAF, following Phase 1 of the integration plan.

## Current Part 2 timing model content

**Location:** `specs/part02-core-cmaf/01-core-cmaf.inc.md` lines 167-190

**Current content:**

- Brief 4-domain timing model overview (MPD timeline, media presentation time, segment addressing time, wall-clock availability time)
- Reference to `@presentationTimeOffset` and Period start time
- Reference to dynamic service availability constraints
- **Issue note:** "Carry over the full v4.3 timing-model explanatory text and formulae where they add interoperability value beyond ISO/IEC 23009-1."

**Assessment:** The current timing model section is a placeholder that needs substantial expansion.

---

## Guidelines-TimingModel content available for integration

### High-value additions identified

1. **MPD timeline concept** (Guidelines-TimingModel 21-Timing.inc.md lines 9-26)
   - Definition of MPD timeline as baseline for scheduling
   - Zero point and relative timing
   - Relationship to periods and representations

2. **Period timing rules** (Guidelines-TimingModel 21-Timing.inc.md lines 43-94)
   - Consecutive, non-overlapping periods
   - Period start and duration specification
   - Zero-duration period prohibition
   - Period self-containment
   - First/last period timing for static presentations
   - First/last period timing for dynamic presentations

3. **Terminology cross-reference** (Guidelines-TimingModel 01-Intro.inc.md lines 104-130)
   - DASH/CMAF/ISOBMFF term mapping
   - Segment vs subsegment clarification

4. **Segment addressing modes** (Guidelines-TimingModel 22-Addressing.inc.md lines 1-448)
   - Indexed addressing (SegmentBase)
   - Explicit addressing (SegmentTemplate with SegmentTimeline)
   - Simple addressing (SegmentTemplate with duration)
   - Addressing mode selection guidance

---

## Integration approach

### Step 1: Expand timing model section

**Target location:** After line 190 in `specs/part02-core-cmaf/01-core-cmaf.inc.md`

**Content to add:**

1. **MPD Timeline subsection**
   - Define MPD timeline concept
   - Explain zero point and relative timing
   - Clarify relationship to periods and sample timelines
   - Add diagram from Guidelines-TimingModel

2. **Period Timing subsection**
   - Consecutive, non-overlapping period rule
   - Period start/duration specification
   - Zero-duration period prohibition
   - Period self-containment rule
   - Cross-reference Part 3 for static presentation first/last period rules
   - Cross-reference Part 4 for dynamic presentation first/last period rules
   - Cross-reference Part 5 for multi-period ad insertion

3. **Terminology clarification**
   - Add DASH/CMAF/ISOBMFF terminology cross-reference table
   - Clarify segment vs subsegment usage (CMAF segment terminology)

### Step 2: Expand segment addressing section

**Target location:** After line 246 in `specs/part02-core-cmaf/01-core-cmaf.inc.md`

**Content to add:**

1. **Addressing Modes Overview**
   - Define three addressing modes (indexed, explicit, simple)
   - Addressing mode selection guidance
   - Addressing mode consistency within adaptation set

2. **Indexed Addressing (SegmentBase)**
   - CMAF track file structure
   - Index segment (sidx) requirements
   - Byte-range addressing
   - Initialization segment byte-range

3. **Explicit Addressing (SegmentTemplate + SegmentTimeline)**
   - $Time$ substitution
   - SegmentTimeline S element structure
   - Media-time addressing benefits

4. **Simple Addressing (SegmentTemplate + duration)**
   - $Number$ substitution
   - Regular segment duration
   - Applicability constraints

---

## Precedence rule verification

### ISO/IEC 23009-1 precedence

All Guidelines-TimingModel content reviewed aligns with ISO/IEC 23009-1 normative requirements. No conflicts identified.

### Existing IOP v5 text precedence

Current Part 2 timing model section is a placeholder. Guidelines-TimingModel content will **supplement and expand** existing text, not replace it.

Current Part 2 segment information section (lines 207-246) already covers SegmentTemplate modes. Guidelines-TimingModel content will **supplement** with detailed addressing mode explanations.

**No conflicts identified.**

---

## Diagrams to integrate

### Recommended diagrams from Guidelines-TimingModel

1. **Basic MPD elements** (`Images/Timing/BasicMpdElements.png`)
   - Shows MPD, Period, AdaptationSet, Representation hierarchy
   - Target: MPD timeline subsection

2. **Periods make the MPD** (`Images/Timing/PeriodsMakeTheMpd.png`)
   - Shows consecutive non-overlapping periods
   - Target: Period timing subsection

3. **Indexed addressing** (`Images/Timing/IndexedAddressing.png`)
   - Shows CMAF track file with index segment
   - Target: Indexed addressing subsection

4. **DASH structure** (`Diagrams/DashStructure.png`)
   - Shows DASH/CMAF/ISOBMFF relationship
   - Target: CMAF structural model section (already exists at line 111)

### Diagram integration steps

1. Copy diagrams from Guidelines-TimingModel to `specs/part02-core-cmaf/images/`
2. Reference diagrams using relative paths in Bikeshed source
3. Add figure captions adapted from Guidelines-TimingModel

---

## Implementation checklist

### Phase 1A: Timing model expansion

- [ ] Read Guidelines-TimingModel 21-Timing.inc.md lines 9-100 (MPD timeline and period timing)
- [ ] Draft MPD timeline subsection for Part 2
- [ ] Draft period timing subsection for Part 2
- [ ] Add cross-references to Parts 3, 4, and 5
- [ ] Copy relevant diagrams to Part 2 images directory
- [ ] Insert expanded timing model content into Part 2
- [ ] Verify modal verb usage with check_links.py

### Phase 1B: Segment addressing expansion

- [ ] Read Guidelines-TimingModel 22-Addressing.inc.md lines 1-200 (addressing modes)
- [ ] Draft addressing modes overview for Part 2
- [ ] Draft indexed addressing subsection for Part 2
- [ ] Draft explicit addressing subsection for Part 2
- [ ] Draft simple addressing subsection for Part 2
- [ ] Copy indexed addressing diagram to Part 2 images directory
- [ ] Insert expanded segment addressing content into Part 2
- [ ] Verify modal verb usage with check_links.py

### Phase 1C: Terminology clarification

- [ ] Read Guidelines-TimingModel 01-Intro.inc.md lines 104-140 (terminology)
- [ ] Add DASH/CMAF/ISOBMFF terminology cross-reference table to Part 2
- [ ] Add editorial note on segment vs subsegment terminology
- [ ] Verify consistency with existing Part 2 terms section

### Phase 1D: Validation and commit

- [ ] Run check_links.py to verify modal verb usage
- [ ] Regenerate Part 2 output document
- [ ] Create Part 2 reconciliation report
- [ ] Update document-porting-status-map.md
- [ ] Commit and push Phase 1 integration

---

## Estimated scope

**Lines to add:** Approximately 200-300 lines of content plus diagrams

**Sections affected:**

- Timing model section (expansion)
- Segment addressing section (expansion)
- Terms section (terminology table addition)

**Files to modify:**

- `specs/part02-core-cmaf/01-core-cmaf.inc.md`

**Files to create:**

- `specs/part02-core-cmaf/images/BasicMpdElements.png` (copy from Guidelines-TimingModel)
- `specs/part02-core-cmaf/images/PeriodsMakeTheMpd.png` (copy from Guidelines-TimingModel)
- `specs/part02-core-cmaf/images/IndexedAddressing.png` (copy from Guidelines-TimingModel)
- `rag/reports/reconcile-part02-core-cmaf.md` (new reconciliation report)

---

## Next steps

1. **Execute Phase 1A:** Expand timing model section
2. **Execute Phase 1B:** Expand segment addressing section
3. **Execute Phase 1C:** Add terminology clarification
4. **Execute Phase 1D:** Validate and commit
5. **Proceed to Phase 2:** Part 3 On-Demand timing constraints
6. **Proceed to Phase 3:** Part 4 Live/Low-Latency timing constraints

---

## References

- Guidelines-TimingModel integration plan: `rag/reports/guidelines-timing-model-integration-plan.md`
- Part 2 source: `specs/part02-core-cmaf/01-core-cmaf.inc.md`
- Guidelines-TimingModel repository: `c:\Users\tsto\OneDrive - Qualcomm\Projects\DASH-IF\Guidelines-TimingModel`