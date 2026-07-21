# F-0010 M1 work package: Part 5 visual review and validator start

Generated: 2026-07-21

Work package:

```text
WP-2026-07-Part5-Visual-Review-and-Validator-Start
```

Milestone:

```text
M1 Part 5 / F-0010 stabilization
```

Baseline planning:

```text
rag/reports/project-migration-execution-plan.md
rag/reports/part05-f0010-issue-index.md
```

## Purpose

This report starts execution of M1 by turning the F-0010 issue index into a
working checklist for Part 5 visual review, table stabilization, and initial
validator implementation readiness.

## Scope

M1 covers:

- F-0010-H1 through F-0010-H5,
- F-0010-B1 through F-0010-B2,
- F-0010-C1 through F-0010-C3,
- F-0010-A1 through F-0010-A3,
- Part 12 synchronization for Part 5 validator/test-asset mapping.

## M1 execution checklist

| Order | Issue | Action | Current status | Required input | Output |
|---:|---|---|---|---|---|
| 1 | F-0010-H1 | Harden Part 5 figures against published DOCX/PDF | Ready to start | Published DOCX/PDF visual access | Figure status table and source figure placeholders/extracted assets |
| 2 | F-0010-H2 | Reconstruct Table 2 row layout | Blocked on visual table | Published DOCX/PDF Table 2 | Bikeshed Table 2 or formal deferral |
| 3 | F-0010-H3 | Visually review Table 4 | Ready to start | Published DOCX/PDF Table 4 | Confirmed/revised Table 4 rows |
| 4 | F-0010-H4 | Visually review Table 5 | Ready to start | Published DOCX/PDF Table 5 | Confirmed/revised Table 5 rows |
| 5 | F-0010-H5 | Decide Table 4/Table 5 reuse strategy | Pending H3/H4 | Reviewed Tables 4/5 | Canonical reuse decision |
| 6 | F-0010-B1 | Implement Table 4 structural validator checks | Ready after H3 | Reviewed Table 4 | Validator implementation issue |
| 7 | F-0010-B2 | Add Table 4 test vectors | Ready after B1 | Validator check list | Positive/negative MPD assets |
| 8 | F-0010-C1 | Implement IF-5 structural checks | Ready after H4 | Reviewed Table 5 | Validator implementation issue |
| 9 | F-0010-C2 | Reuse Table 4 checks for IF-5 source ad MPDs | Ready after B1/C1 | Validator module design | Shared validation strategy |
| 10 | F-0010-C3 | Add IF-5 SSAI scenario vectors | Ready after C1 | Scenario definitions | Positive/negative SSAI assets |
| 11 | F-0010-A1 | Implement MPD-level SCTE-35 EventStream checks | Ready to start | SCTE-35 matrix | Validator implementation issue |
| 12 | F-0010-A2 | Add payload-aware SCTE-35 checks | Pending A1/parser choice | SCTE-35 parser capability | Payload-aware validation scope |
| 13 | F-0010-A3 | Add IF-3 SCTE-35 test vectors | Ready after A1 | EventStream examples | Positive/negative SCTE-35 MPD assets |
| 14 | Part 12 | Synchronize conformance mapping | Continuous | Decisions above | Updated Part 12 mapping |

## GitHub issue creation queue

Create issues in this order:

1. F-0010-H1: Harden Part 5 figures against published DOCX/PDF.
2. F-0010-H2: Reconstruct Part 5 Table 2 row layout from DOCX/PDF.
3. F-0010-H3: Visually review Part 5 Table 4 DASH-IF ad content MPD.
4. F-0010-H4: Visually review Part 5 Table 5 IF-5 multi-Period ad insertion.
5. F-0010-H5: Decide Table 4/Table 5 canonical table reuse strategy.
6. F-0010-A1: Implement MPD-level SCTE-35 EventStream checks.
7. F-0010-B1: Implement DASH-IF ad content MPD structural validator checks.
8. F-0010-C1: Implement IF-5 multi-Period structural validator checks.
9. F-0010-B2: Add DASH-IF ad content MPD positive and negative test vectors.
10. F-0010-C2: Reuse Table 4 checks for source ad-content MPDs used by IF-5.
11. F-0010-C3: Add IF-5 SSAI scenario test vectors.
12. F-0010-A2: Add SCTE-35 payload-aware checks.
13. F-0010-A3: Add IF-3 SCTE-35 positive and negative test vectors.

Rationale:

- visual table/figure issues should be opened first because they may alter row
  details and modal strength;
- MPD-level SCTE-35, Table 4, and Table 5 structural validators can start in
  parallel after visual review starts;
- payload-aware SCTE-35 checks depend on parser capability and should follow the
  MPD-level checks.

## Visual review requirements

### Figures

Published figures requiring final status:

| Figure | Target source area | Required decision |
|---|---|---|
| Figure 1 | Architecture / IF-1 sub-interface labels | Extract/redraw or defer |
| Figure 3 | IF-0 abstracted media model | Extract/redraw or replace with source diagram |
| Figure 4 | CMAF encoder/packager options | Extract/redraw or replace with source diagram |
| Figure 5 | IF-2 CMAF-to-DASH mapping | Extract/redraw or replace with source diagram |
| Figure 6 | IF-4 ad content format | Extract/redraw or replace with source diagram |
| Figure 7 | IF-5 MPD manipulator operation | Extract/redraw or replace with source diagram |

### Tables

Published tables requiring final status:

| Table | Current status | Required decision |
|---|---|---|
| Table 1 | Reconstructed; not visually reviewed | Confirm rows/references |
| Table 2 | Prose hardened; row layout missing | Reconstruct or formally defer |
| Table 3 | XML example migrated; not visually reviewed | Confirm caption/example layout |
| Table 4 | Reconstructed; validator matrix exists | Confirm rows/modal strength |
| Table 5 | Reconstructed; validator matrix exists | Confirm rows/modal strength and split-table strategy |

## Validator-start readiness

### F-0010-A SCTE-35

Ready inputs:

```text
rag/reports/part05-f0010-scte35-validator-matrix.md
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if3-scte35-opportunity-signalling
```

First implementation-ready checks:

- allowed SCTE-35 EventStream schemes,
- `xml+bin` Binary presence,
- Base64 validation,
- Event timing parseability,
- duplicate event id warning.

### F-0010-B Table 4

Ready inputs:

```text
rag/reports/part05-f0010-table4-validator-matrix.md
rag/reports/part05-f0010-validator-implementation-issues.md
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if4d-ad-content-storage
```

First implementation-ready checks:

- static MPD type,
- CMAF profile,
- forbidden dynamic MPD attributes,
- exactly one Period,
- `Period@duration`,
- Period-level `BaseURL`,
- AdaptationSet/Representation presence,
- forbidden `UTCTiming` and `LeapSecondInformation`.

### F-0010-C Table 5

Ready inputs:

```text
rag/reports/part05-f0010-table5-validator-matrix.md
rag/reports/part05-f0010-validator-implementation-issues.md
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if5-media-presentation-requirements
```

First implementation-ready checks:

- Period presence,
- main Period `@start`,
- monotonic Period starts,
- AdaptationSet/Representation presence,
- `AdaptationSet@contentType`,
- SegmentList absence,
- live/dynamic `UTCTiming`,
- reusable Table 4 checks for source ad-content MPDs.

## Part 12 synchronization points

After M1 updates, revise:

```text
specs/part12-conformance-reference-tools/01-conformance.inc.md#tools-part5-ad-insertion-conformance
```

Recommended Part 12 row categories:

- IF-3 SCTE-35 MPD Event validator checks,
- IF-4 DASH-IF ad content MPD validator checks,
- IF-5 multi-Period ad insertion validator checks,
- IF-5 SSAI scenario/reference-client checks,
- IF-7 SGAI/livesim2/dash.js checks,
- IF-8 tracking sample checks,
- IF-9 clear/encrypted playback checks.

## M1 acceptance criteria

M1 is complete when:

- all F-0010-H issues have final review status;
- first F-0010-A/B/C validator issue scopes are ready for implementation;
- initial positive/negative test-vector lists are linked from Part 12;
- Part 12 reflects the current Part 5 conformance plan;
- `check_links.py` passes.

## Current blockers

- Table 2 row layout cannot be reconstructed from extracted text alone.
- Figures require DOCX/PDF visual extraction or redrawing.
- Exact Table 4/Table 5 row hierarchy and modal strength require visual review.
- Payload-aware SCTE-35 validation requires parser capability or scoped deferral.