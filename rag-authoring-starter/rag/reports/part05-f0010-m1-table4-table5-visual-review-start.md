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

## Current blocker

The current environment has the extracted text and reconstructed source, but not
a visual table extraction suitable for confirming row layout. Therefore this
report starts the review and identifies safe validator-start areas, but it does
not claim Table 4 or Table 5 visual review completion.