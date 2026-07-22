# Guidelines-TimingModel Integration into IOP v5 Parts 2, 3, and 4

## Summary

This PR integrates timing model content from the DASH-IF Guidelines-TimingModel document into IOP v5 Parts 2 (Core CMAF), 3 (On-Demand), and 4 (Live/Low-Latency). The integration adds comprehensive timing model explanations, segment addressing modes, and period timing constraints while maintaining full compliance with ISO/IEC 23009-1.

## Changes Overview

### Part 2: Core CMAF (Phase 1)
- **MPD Timeline section** with definition and diagram (BasicMpdElements.png)
- **Period Timing section** with consecutive/non-overlapping rules and diagram (PeriodsMakeTheMpd.png)
- **First and Last Period Timing** subsection with rules for static and dynamic presentations
- **Segment addressing modes** (indexed, explicit, simple) with detailed explanations and diagram (IndexedAddressing.png)
- **Terminology Cross-Reference table** mapping DASH/CMAF/ISOBMFF terms
- **DASHIF-TIMING bibliographic reference**

### Part 3: On-Demand (Phase 2)
- **Period Timing section** with static presentation constraints:
  - First Period shall start at zero point of MPD timeline
  - Last Period shall have Period@duration
- Cross-references to Part 2 and Guidelines-TimingModel
- DASHIF-TIMING bibliographic reference

### Part 4: Live/Low-Latency (Phase 3)
- **Period Timing section** with dynamic presentation constraints:
  - First Period shall start at or after zero point of MPD timeline
  - Last Period may have Period@duration (fixed) or unlimited duration
  - Note about MPD validity duration constraining unlimited periods
- Cross-references to Part 2 and Guidelines-TimingModel
- DASHIF-TIMING bibliographic reference

## Commits

1. `e78bf8c` - Phase 1A: Timing model expansion
2. `c3716da` - Phase 1B: Segment addressing expansion
3. `4263c1c` - Phase 1C: Terminology clarification
4. `d8ed168` - Phase 1D: Validation and documentation
5. `4dd45f9` - Phase 2: Part 3 On-Demand timing constraints
6. `d3c43dc` - Phase 3: Part 4 Live/Low-Latency timing constraints

## Files Modified

**Part 2:**
- `specs/part02-core-cmaf/01-core-cmaf.inc.md` (~307 lines added)
- `specs/part02-core-cmaf/part02-core-cmaf.bs` (added DASHIF-TIMING reference)
- `specs/part02-core-cmaf/images/BasicMpdElements.png` (new)
- `specs/part02-core-cmaf/images/PeriodsMakeTheMpd.png` (new)
- `specs/part02-core-cmaf/images/IndexedAddressing.png` (new)

**Part 3:**
- `specs/part03-on-demand/01-on-demand.inc.md` (~21 lines added)
- `specs/part03-on-demand/part03-on-demand.bs` (added DASHIF-TIMING reference)

**Part 4:**
- `specs/part04-live-low-latency/00-live-services.inc.md` (~27 lines added)
- `specs/part04-live-low-latency/part04-live-low-latency.bs` (added DASHIF-TIMING reference)

**Documentation:**
- `rag/reports/reconcile-part02-core-cmaf.md` (new reconciliation report)
- `rag/reports/document-porting-status-map.md` (updated with Phase 1 completion)
- `rag/reports/part02-timing-model-integration-status.md` (updated)

**Total:** 16 files modified, ~581 lines added, 3 diagrams added

## Source Material

All integrated content is sourced from the DASH-IF Guidelines-TimingModel document:
- `01-Intro.inc.md` lines 104-140 (terminology)
- `21-Timing.inc.md` lines 9-94 (MPD timeline and period timing)
- `22-Addressing.inc.md` lines 1-448 (segment addressing modes)

## Precedence Rule Compliance

All integrated content follows the established precedence rule:

**ISO/IEC 23009-1 > existing IOP v5 text > Guidelines-TimingModel**

### Verification Results

✅ All integrated content aligns with ISO/IEC 23009-1 normative requirements  
✅ All integrated content supplements (not replaces) existing IOP v5 text  
✅ All integrated content accurately reflects Guidelines-TimingModel source material  
✅ No conflicts identified with ISO/IEC 23009-1 or existing IOP v5 text

## Modal Verb Usage

All integrated content uses RFC 2119 modal verbs consistently:
- `shall` - normative requirement
- `shall not` - normative prohibition
- `should` - normative recommendation
- `should not` - normative recommendation against
- `may` - optional/permissive

Modal verbs are wrapped in `<span class=modal-keyword>` tags for Bikeshed processing.

## Testing

- ✅ All Bikeshed files compile successfully
- ✅ All diagrams display correctly
- ✅ All cross-references resolve correctly
- ✅ All bibliographic references are valid

## Review Checklist

- [ ] Content accuracy verified against Guidelines-TimingModel source
- [ ] Precedence rule compliance verified
- [ ] Modal verb usage consistent
- [ ] Cross-references valid
- [ ] Diagrams display correctly
- [ ] Bikeshed syntax valid
- [ ] No conflicts with ISO/IEC 23009-1
- [ ] No conflicts with existing IOP v5 text

## Related Documents

- Integration plan: `rag/reports/guidelines-timing-model-integration-plan.md`
- Integration status: `rag/reports/part02-timing-model-integration-status.md`
- Reconciliation report: `rag/reports/reconcile-part02-core-cmaf.md`
- Session summary: `rag/reports/guidelines-timing-model-integration-session-summary.md`

## Reviewer Notes

This integration represents a significant enhancement to IOP v5's timing model documentation. The content:

1. **Improves clarity** - Provides comprehensive explanations of MPD timeline and period timing concepts
2. **Enhances interoperability** - Defines three segment addressing modes with detailed guidance
3. **Maintains compliance** - All content aligns with ISO/IEC 23009-1 and existing IOP v5 text
4. **Adds value** - Cross-references between parts and to Guidelines-TimingModel for detailed discussion

The integration is ready for editorial review and technical validation by the DASH-IF community.

## Questions for Reviewers

1. Are the timing model explanations clear and accurate?
2. Do the segment addressing mode descriptions provide sufficient guidance?
3. Are the period timing constraints correctly specified for static and dynamic presentations?
4. Should any additional Guidelines-TimingModel content be integrated in future work?

---

**Branch:** `tstockhammer-rag-workflow`  
**Base:** `main` (or appropriate base branch)  
**Author:** Thomas Stockhammer  
**Date:** 2026-07-22