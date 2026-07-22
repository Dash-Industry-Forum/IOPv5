# Guidelines-TimingModel integration plan

Generated: 2026-07-22

This plan defines how content from the DASH-IF Guidelines-TimingModel repository will be integrated into IOP v5 Parts 2, 3, and 4, following the precedence rule: **ISO/IEC 23009-1 > existing IOP v5 text > Guidelines-TimingModel**.

## Repository information

**Source:** https://github.com/Dash-Industry-Forum/Guidelines-TimingModel

**Local clone:** `c:\Users\tsto\OneDrive - Qualcomm\Projects\DASH-IF\Guidelines-TimingModel`

**Published output:** https://dashif.org/Guidelines-TimingModel/

**Content structure:**

```text
01-Intro.inc.md          - Purpose, interpretation, DASH/CMAF overview
21-Timing.inc.md         - MPD timeline, period timing, sample timeline
22-Addressing.inc.md     - Segment addressing modes (indexed, explicit, simple)
29-Misc.inc.md           - Additional topics
Guidelines-TimingModel.bs.md - Bikeshed master document
Diagrams/                - Timing model diagrams
Images/                  - Supporting images
```

## Precedence rule enforcement

### ISO/IEC 23009-1 takes absolute precedence

Any Guidelines-TimingModel content that conflicts with ISO/IEC 23009-1 normative requirements **must be excluded or adapted** to align with the standard.

### Existing IOP v5 text takes precedence over Guidelines-TimingModel

Where IOP v5 Parts 2, 3, or 4 already address a timing model concept, Guidelines-TimingModel content:

- **May supplement** existing text with additional explanation, examples, or diagrams
- **Must not contradict** existing IOP v5 requirements
- **Must not replace** existing IOP v5 text unless the Guidelines-TimingModel version is demonstrably superior and approved

### Guidelines-TimingModel fills gaps

Guidelines-TimingModel content is most valuable where:

- IOP v5 does not yet address a timing model concept
- Additional explanation or examples would improve understanding
- Diagrams or visual aids would clarify complex timing relationships

## Content analysis and integration mapping

### Section 1: Introduction and terminology (01-Intro.inc.md)

| Guidelines-TimingModel content | IOP v5 status | Integration approach |
|---|---|---|
| Purpose and interpretation | Part 1 covers scope; Part 2 may reference Guidelines-TimingModel for detailed timing model discussion | Add informative reference to Guidelines-TimingModel in Part 2 introduction |
| DASH and CMAF overview | Part 2 already covers CMAF basics | No integration needed; existing Part 2 text takes precedence |
| Structure of DASH presentation | Part 2 covers MPD/segment structure | Supplement with Guidelines-TimingModel diagrams if they add clarity |
| Terminology cross-reference (DASH/CMAF/ISOBMFF) | Part 2 may benefit from this table | Add terminology cross-reference table to Part 2 if not already present |
| Terminology choices (segment vs subsegment) | Part 2 should clarify this | Add editorial note in Part 2 explaining CMAF segment terminology alignment |

**Recommended Part 2 integration point:** After CMAF profile discussion, before detailed timing/addressing sections.

**Conflicts:** None identified. Guidelines-TimingModel introduction aligns with ISO/IEC 23009-1 and existing IOP v5 approach.

---

### Section 2: Timing model (21-Timing.inc.md)

| Guidelines-TimingModel content | IOP v5 status | Integration approach |
|---|---|---|
| MPD timeline concept | Part 2 may not explicitly define "MPD timeline" as distinct from sample timeline | **High-value addition:** Add MPD timeline definition and explanation to Part 2 |
| Static vs dynamic presentation timing | Parts 2, 3, and 4 cover this | Cross-reference Guidelines-TimingModel for detailed timing model discussion |
| Period timing (start, duration, consecutive non-overlapping) | Part 2 covers period basics; Part 5 covers multi-period ad insertion | Supplement Part 2 with Guidelines-TimingModel period timing rules and diagrams |
| First/last period timing in static presentations | Part 3 should cover this | **Add to Part 3:** First period starts at zero; last period has duration |
| First/last period timing in dynamic presentations | Part 4 should cover this | **Add to Part 4:** First period starts at/after zero; last period may have unlimited duration |
| Effective availability start time and leap seconds | Part 4 should cover this | **Add to Part 4:** Leap second handling and effective AST calculation |
| Period self-containment and connectivity | Part 2 should cover this | **Add to Part 2:** Period self-containment rule; reference Part 5 for period-connected representations |
| Zero-duration period prohibition | Part 2 should cover this | **Add to Part 2:** Periods shall not have zero duration |

**Recommended Part 2 integration points:**

1. **After CMAF profile discussion:** Add MPD timeline concept and period timing basics
2. **Before segment addressing:** Establish timing foundation for addressing discussion

**Recommended Part 3 integration points:**

1. **Static presentation timing section:** Add first/last period timing rules for static presentations

**Recommended Part 4 integration points:**

1. **Dynamic presentation timing section:** Add first/last period timing rules, effective AST, leap second handling

**Conflicts:** None identified. Guidelines-TimingModel timing rules align with ISO/IEC 23009-1 and constrain it further for interoperability.

---

### Section 3: Segment addressing (22-Addressing.inc.md)

| Guidelines-TimingModel content | IOP v5 status | Integration approach |
|---|---|---|
| Addressing modes overview (indexed, explicit, simple) | Part 2 should cover this | **High-value addition:** Add addressing modes overview to Part 2 |
| Indexed addressing (SegmentBase) | Part 2 should cover this | **Add to Part 2:** Indexed addressing rules, byte-range requirements, sidx structure |
| Explicit addressing (SegmentTemplate with SegmentTimeline) | Part 2 should cover this; Part 4 uses this for live | **Add to Part 2:** Explicit addressing rules; cross-reference Part 4 for live usage |
| Simple addressing (SegmentTemplate with duration) | Part 2 should cover this | **Add to Part 2:** Simple addressing rules and applicability constraints |
| Addressing mode consistency within adaptation set | Part 2 should cover this | **Add to Part 2:** All representations in same adaptation set shall use same addressing mode |
| Addressing mode selection guidance | Part 2 should cover this | **Add to Part 2:** Content-generated-on-the-fly → explicit; pre-generated → indexed or explicit |

**Recommended Part 2 integration point:** Dedicated segment addressing section after timing model discussion.

**Conflicts:** None identified. Guidelines-TimingModel addressing rules align with ISO/IEC 23009-1 and DASH-CMAF.

---

### Section 4: Additional topics (29-Misc.inc.md)

Content analysis deferred until Sections 1-3 integration is complete. This section covers sample timeline, representation timing, segment availability, and other advanced topics that may require more careful precedence analysis.

---

## Integration execution plan

### Phase 1: Part 2 Core CMAF timing model foundation

**Objective:** Establish timing model foundation in Part 2 using Guidelines-TimingModel content.

**Steps:**

1. Read current Part 2 timing/addressing content to identify gaps
2. Add MPD timeline concept and definition
3. Add period timing rules (consecutive, non-overlapping, zero-duration prohibition, self-containment)
4. Add segment addressing modes overview (indexed, explicit, simple)
5. Add addressing mode selection guidance
6. Add terminology cross-reference table (DASH/CMAF/ISOBMFF)
7. Include relevant Guidelines-TimingModel diagrams
8. Add informative reference to Guidelines-TimingModel for detailed discussion

**Deliverable:** Updated `specs/part02-core-cmaf/01-core-cmaf.inc.md` with timing model foundation.

---

### Phase 2: Part 3 On-Demand timing constraints

**Objective:** Add static presentation timing constraints to Part 3.

**Steps:**

1. Read current Part 3 content to identify gaps
2. Add first/last period timing rules for static presentations
3. Cross-reference Part 2 timing model foundation
4. Cross-reference Guidelines-TimingModel for detailed timing model discussion

**Deliverable:** Updated `specs/part03-on-demand/01-on-demand.inc.md` with static presentation timing constraints.

---

### Phase 3: Part 4 Live/Low-Latency timing constraints

**Objective:** Add dynamic presentation timing constraints to Part 4.

**Steps:**

1. Read current Part 4 content to identify gaps
2. Add first/last period timing rules for dynamic presentations
3. Add effective availability start time and leap second handling
4. Add segment availability window discussion (if not already present)
5. Cross-reference Part 2 timing model foundation
6. Cross-reference Guidelines-TimingModel for detailed timing model discussion

**Deliverable:** Updated `specs/part04-live-low-latency/00-live-services.inc.md` and/or `specs/part04-live-low-latency/02-low-latency.inc.md` with dynamic presentation timing constraints.

---

### Phase 4: Validation and reconciliation

**Objective:** Ensure integrated content follows precedence rules and does not conflict with ISO/IEC 23009-1 or existing IOP v5 text.

**Steps:**

1. Review all integrated content for conflicts
2. Run `tools/publication/check_links.py` to verify modal verb usage
3. Regenerate Part 2, 3, and 4 output documents
4. Create reconciliation reports for Parts 2, 3, and 4 (similar to existing Part 5, 6, and 9 reports)
5. Update `rag/reports/document-porting-status-map.md` to reflect Guidelines-TimingModel integration status

**Deliverable:** Reconciliation reports and updated porting status map.

---

## Identified conflicts and resolutions

### No conflicts identified in Sections 1-3

Initial analysis of Guidelines-TimingModel Sections 1-3 (Introduction, Timing, Addressing) reveals no conflicts with ISO/IEC 23009-1 or existing IOP v5 text. Guidelines-TimingModel content in these sections:

- Aligns with ISO/IEC 23009-1 normative requirements
- Constrains ISO/IEC 23009-1 for interoperability (which is the purpose of IOP)
- Provides explanatory content and diagrams that supplement existing IOP v5 text

### Potential conflicts in Section 4 (deferred)

Section 4 (29-Misc.inc.md) covers advanced topics including sample timeline, representation timing, segment availability, and period connectivity. These topics may overlap with existing IOP v5 content in Parts 2, 4, and 5. Conflict analysis deferred until Phases 1-3 are complete.

---

## Diagrams and visual aids

Guidelines-TimingModel includes valuable diagrams in `Diagrams/` and `Images/` directories. Recommended diagrams for integration:

| Diagram | Source | Target Part | Integration point |
|---|---|---|---|
| DASH structure overview | `Diagrams/DashStructure.png` | Part 2 | After CMAF profile discussion |
| MPD timeline and periods | `Images/Timing/PeriodsMakeTheMpd.png` | Part 2 | MPD timeline concept section |
| Indexed addressing | `Images/Timing/IndexedAddressing.png` | Part 2 | Indexed addressing section |
| Basic MPD elements | `Images/Timing/BasicMpdElements.png` | Part 2 | MPD timeline concept section |

Diagrams should be copied to `specs/part02-core-cmaf/images/` (or similar) and referenced using relative paths in the Bikeshed source.

---

## Next steps

1. **Execute Phase 1:** Integrate timing model foundation into Part 2
2. **Execute Phase 2:** Add static presentation timing constraints to Part 3
3. **Execute Phase 3:** Add dynamic presentation timing constraints to Part 4
4. **Execute Phase 4:** Validate and reconcile integrated content
5. **Analyze Section 4:** Review 29-Misc.inc.md for additional integration opportunities
6. **Update porting status map:** Reflect Guidelines-TimingModel integration completion

---

## References

- Guidelines-TimingModel repository: https://github.com/Dash-Industry-Forum/Guidelines-TimingModel
- Published Guidelines-TimingModel: https://dashif.org/Guidelines-TimingModel/
- ISO/IEC 23009-1 (DASH): Referenced throughout IOP v5
- Document porting status map: `rag/reports/document-porting-status-map.md`