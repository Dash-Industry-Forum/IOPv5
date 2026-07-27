# F-0010 M1 Table 4 / Table 5 visual review start

Generated: 2026-07-21

Purpose: start visual review for the two reconstructed Part 5 tables that most
directly unblock validator implementation:

- Table 4: DASH-IF Ad content MPD
- Table 5: Ad Content spliced into main content / IF-5 MPD requirements

Visual DOCX/PDF review is still required before the reconstructed rows are
treated as final. This report identifies the current source rows, review
questions, and validator unblock decisions.

## Source anchors

```text
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if4d-ad-content-storage
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if5-media-presentation-requirements
```

## Related reports

```text
rag/reports/part05-f0010-table4-validator-matrix.md
rag/reports/part05-f0010-table5-validator-matrix.md
rag/reports/part05-f0010-validator-implementation-issues.md
rag/reports/part05-f0010-m1-visual-validator-start.md
```

## Table 4 review start

### Current reconstruction status

Current Table 4 is reconstructed in source as:

```text
DASH-IF ad content MPD requirements.
```

Current row groups:

- MPD rows,
- Period rows,
- AdaptationSet rows,
- EventStream/InbandEventStream rows,
- SegmentBase rows,
- UTCTiming/LeapSecondInformation rows.

### High-priority visual checks

| Check | Question | Validator impact |
|---|---|---|
| Caption | Is the caption exactly "DASH-IF Ad content MPD"? | Low; editorial |
| Row count | Are all rows present? | High |
| Column headings | Are Context / Element or attribute / Use / Requirement columns correct? | High |
| Use values | Are `M`, `R`, `OD`, `O`, and cardinalities correct? | High |
| MPD attributes | Are forbidden dynamic attributes complete? | High |
| BaseURL hierarchy | Is MPD-level BaseURL forbidden and Period-level BaseURL required? | High |
| Period count | Is exactly one Period required? | High |
| Period timing | Are `@start` absence and `@duration` presence correct? | High |
| SegmentBase PTO/eptDelta | Are absence requirements exact? | High |
| `pdDelta` | Is "non-negative and as small as possible" correctly captured? | Medium |
| UTCTiming/LeapSecondInformation | Are both forbidden in Table 4? | High |

### Preliminary validator unblock decision

F-0010-B1 can start with deterministic checks that are unlikely to change after
visual review:

- `MPD@type="static"`,
- exactly one Period,
- Period `@duration` present,
- Period `@start` absent,
- Period-level BaseURL present,
- MPD-level BaseURL absent,
- AdaptationSet and Representation presence,
- SegmentList absent,
- UTCTiming absent,
- LeapSecondInformation absent.

Potentially wait for visual review before finalizing:

- exact `@profiles` warning/error split,
- `ProgramInformation` recommendation handling,
- `AssetIdentifier` recommendation handling,
- `pdDelta` warning policy.

## Table 5 review start

### Current reconstruction status

Current Table 5 is reconstructed in source as two source-level tables:

```text
Main content MPD requirements relevant to IF-5 insertion.
Ad insertion content MPD requirements relevant to IF-5 insertion.
```

This split is editorial and may or may not match the published single-table
layout.

### High-priority visual checks

| Check | Question | Validator impact |
|---|---|---|
| Published layout | Is Table 5 one table or visually separable row groups? | Medium |
| Row count | Are all main/ad rows present? | High |
| Main MPD rows | Are `ServiceDescription`, `@profiles`, `InitializationSet`, and `UTCTiming` rows complete? | High |
| Main Period rows | Is `Period@start` mandatory and xlink absent? | High |
| Main EventStream | Is `EventStream@presentationTimeOffset` captured correctly? | High |
| Main AdaptationSet rows | Are xlink absence, PTO, contentType, SegmentList, Representation rows complete? | High |
| Ad content rows | Do they intentionally duplicate Table 4 rows? | High |
| Inserted Period timing | Does published text require inserted `Period@duration` removal? | High |
| Table 4 reuse | Which Table 5 ad-content rows should reuse Table 4 checks? | High |
| UTCTiming | Is main/live UTCTiming required and ad-source UTCTiming forbidden? | High |

### Preliminary validator unblock decision

F-0010-C1 can start with deterministic checks that are unlikely to change after
visual review:

- at least one Period,
- main Period `@start` present,
- Period starts monotonic,
- Period xlink attributes absent,
- AdaptationSet presence,
- AdaptationSet `@contentType` present,
- SegmentList absent,
- Representation presence,
- EmptyAdaptationSet absent,
- live/dynamic UTCTiming present.

Potentially wait for visual review before finalizing:

- exact EventStream splitting/PTO validation,
- exact inserted Period `@duration` handling,
- continuity/connectivity descriptor warnings,
- Table 4 reuse mechanics.

## Shared Table 4 / Table 5 reuse recommendation

Preliminary recommendation:

1. Implement a reusable "DASH-IF ad content MPD" validator module from Table 4.
2. Use that module for source ad-content MPDs and for any Table 5 ad-content row
   that applies before insertion.
3. Keep IF-5 final-output checks separate because inserted ad Periods may have
   different `@start` / `@duration` handling after MPD proxy manipulation.
4. Document this split in F-0010-H5.

## Immediate next manual visual-review tasks

1. Open the published Part 5 DOCX/PDF.
2. Navigate to Table 4 and compare every row against
   `#ad-if4d-ad-content-storage`.
3. Navigate to Table 5 and compare every row against
   `#ad-if5-media-presentation-requirements`.
4. Mark each row as:
   - confirmed,
   - corrected,
   - missing,
   - extra,
   - needs WG/editorial decision.
5. Update:
   - `part05-f0010-table4-validator-matrix.md`,
   - `part05-f0010-table5-validator-matrix.md`,
   - `05-ad-insertion.inc.md`,
   - Part 12 mapping if validation categories change.

## DOCX table extraction pass

The published Part 5 DOCX is available locally at:

```text
rag/corpus/published/DASH-IF-IOP-Part5-v5.0.0.docx
```

A DOCX table extraction helper was added at:

```text
tools/ingest/extract_part5_tables.py
```

The extraction found six tables in the DOCX and identified:

```text
Table 4: 36 rows
Table 5: 37 rows
```

This is not a visual rendering review, but it is stronger than plain extracted
text because it reads the DOCX table structure directly.

## Table 4 extraction findings

DOCX Table 4 confirms the reconstructed Table 4 is largely aligned, including:

- `MPD@profiles`,
- `MPD@type`,
- removed dynamic MPD attributes,
- `MPD@minBufferTime`,
- `ProgramInformation`,
- MPD-level `BaseURL` absence,
- exactly one `Period`,
- `Period@start` absence,
- `Period@duration` presence,
- Period-level `BaseURL`,
- `AssetIdentifier`,
- `EventStream`,
- `AdaptationSet`,
- `InbandEventStream`,
- `SegmentBase@presentationTimeOffset`,
- `SegmentBase@eptDelta`,
- `SegmentBase@pdDelta`,
- `@contentType`,
- `SegmentList`,
- `Representation`,
- `EmptyAdaptationSet`,
- `UTCTiming`,
- `LeapSecondInformation`.

### Table 4 source deltas to review

The DOCX extraction includes rows that are not currently explicit in the source
Table 4:

| DOCX row | Current source status | Recommended action |
|---|---|---|
| `AdaptationSet@xlink:href` with Use `R` | Missing from source Table 4 | Add to source Table 4. |
| `AdaptationSet@xlink:actuate` with Use `R` | Missing from source Table 4 | Add to source Table 4. |
| `CommonAttributesElements` row | Not explicit in source Table 4 | Optional editorial row; likely not needed for validator but note in matrix. |

The DOCX extraction confirms `SegmentBase@pdDelta` has Use `O`, not `OD`, and
the reconstructed source already matches this.

## Table 5 extraction findings

DOCX Table 5 confirms that the current source is a simplified reconstruction and
does not yet mirror the published Table 5 row hierarchy.

The published DOCX Table 5 has these major row groups:

1. `MPD`,
2. `ServiceDescription` / `Latency@target`,
3. `@profiles`,
4. `@minimumUpdatePeriod`,
5. `InitializationSet`,
6. `Period (Main content)`,
7. `Period (Ad Content)`,
8. `Period (Slate Content)`,
9. final `Period (Main Content)`.

### Table 5 source deltas to review

| DOCX row or group | Current source status | Recommended action |
|---|---|---|
| `@minimumUpdatePeriod` adjusted according to operation | Missing from current source Table 5 | Add row or note. |
| `InitializationSet` operational rules for `@inAllPeriods` | Simplified in source | Replace with fuller DOCX wording. |
| `Period (Main content) @duration` removed | Missing from current main-content table | Add row. |
| `Period (Main content) EventStream/AdaptationSet/AssetIdentifier` reused | Partially represented | Align wording. |
| `Period (Ad Content)` group | Not represented as inserted Period group | Add or restructure source Table 5. |
| `Period (Ad Content) @id`, `@start`, `@duration`, `BaseURL`, `@availabilityTimeOffset`, `EventStream`, `AdaptationSet`, `AssetIdentifier` | Not represented as a distinct inserted Period group | Add rows. |
| `Period (Slate Content)` group | Missing | Add rows or document deferral. |
| final `Period (Main Content)` return group | Missing | Add rows or document deferral. |
| Table key says conditions hold only without `xlink:href`; if linking is used, attributes are optional and minOccurs is 0 | Missing from source note | Add to source key/note. |

## Updated validator unblock decision

### F-0010-B1

F-0010-B1 can start, but the Table 4 validator matrix should first be updated to
include deterministic absence checks for:

- `AdaptationSet@xlink:href`,
- `AdaptationSet@xlink:actuate`.

The rest of the deterministic Table 4 checks remain safe to start.

### F-0010-C1

F-0010-C1 should not be finalized directly from the current source Table 5. The
DOCX extraction shows that source Table 5 needs a restructuring pass before the
Table 5 validator matrix is treated as final.

Safe C1 checks that can still start:

- Period sequence is present,
- inserted ad Period `@start` is present,
- inserted ad Period `@duration` is optional/typically removed,
- inserted ad/slate Period `@availabilityTimeOffset` is mandatory,
- inserted ad/slate Period `BaseURL` is present,
- return main Period `@start` is present,
- return main Period `@duration` is removed.

## Recommended next source updates

1. Add the two missing `AdaptationSet` xlink rows to source Table 4.
2. Update the Table 4 validator matrix for those two removed attributes.
3. Restructure source Table 5 to follow the DOCX groups:
   - MPD,
   - Period (Main content),
   - Period (Ad Content),
   - Period (Slate Content),
   - Period (Main Content).
4. Update the Table 5 validator matrix after restructuring.
5. Update Part 12 if the validator categories change.

## Current blocker

The current environment can extract DOCX table structure, but still cannot
provide a rendered visual table comparison. Therefore Table 4 is now partially
confirmed by DOCX table extraction, while Table 5 is confirmed to require a
source restructuring pass before visual review can be considered complete.
