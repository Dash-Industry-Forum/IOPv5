# F-0010-H Table 2 reconstruction status: DASH-IF Main live content MPD

Generated: 2026-07-21

Feature bucket:

```text
F-0010-H Published Part 5 table/figure hardening
```

Source anchor:

```text
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if2-content-preparation
```

## Status

Table 2 row layout is not reconstructable from the currently available extracted
text alone.

The extracted source preserves the Table 2 caption and surrounding IF-2 prose,
but not the full row/column layout. The IF-2 prose has therefore been hardened
in the Part 5 source, while Table 2 row reconstruction remains blocked pending
visual DOCX/PDF inspection.

## Available extracted source context

The extracted source around Table 2 provides enough information to harden IF-2
prose for:

- Period boundary generation at splice points,
- EventStream signalling when Period boundaries are not generated,
- minimum splice point advance notice time,
- `MPD@minimumUpdatePeriod`,
- `InitializationSet`,
- `InitializationSet@inAllPeriods`,
- `MPD@availabilityStartTime`,
- `AssetIdentifier`,
- Period start calculation,
- Period continuity,
- `SegmentBase@presentationTimeOffset`,
- `SegmentBase@eptDelta`,
- first segment addressing after a splice point.

This material is already incorporated into:

```text
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if2-content-preparation
```

## Required visual review

To complete Table 2 reconstruction, inspect the published DOCX/PDF and capture:

- table title and exact caption,
- complete row count,
- column headings,
- row hierarchy,
- `Use` column values if present,
- modal keywords in each row,
- notes associated with the table,
- whether Figure 5 is required to interpret any row.

## Proposed Table 2 reconstruction workflow

1. Open the published Part 5 DOCX/PDF at the IF-2 / Table 2 location.
2. Capture the exact table rows into a temporary Markdown table.
3. Compare each row to the current IF-2 prose.
4. Add a reconstructed Bikeshed table under `#ad-if2-content-preparation`.
5. Add an issue note marking the table as visually reconstructed and requiring
   WG/editorial review.
6. Update this report and `reconcile-part05-ad-insertion.md`.

## Provisional row topics expected from prose

The following row topics are expected but not confirmed as exact Table 2 rows:

| Expected topic | Current IF-2 prose coverage | Reconstruction status |
|---|---|---|
| MPD profile / CMAF profile | Covered generally by DASH Core Profile for CMAF content | Needs visual row |
| `MPD@availabilityStartTime` | Covered | Needs visual row |
| `MPD@minimumUpdatePeriod` | Covered | Needs visual row |
| `InitializationSet` | Covered | Needs visual row |
| `InitializationSet@id` | Covered | Needs visual row |
| `InitializationSet@inAllPeriods` | Covered | Needs visual row |
| `Period@start` | Covered | Needs visual row |
| `AssetIdentifier` | Covered with EIDR and DASH-IF asset-id examples | Needs visual row |
| `AdaptationSet` mapping from CMAF Switching Set | Covered | Needs visual row |
| `SegmentBase@presentationTimeOffset` | Covered | Needs visual row |
| `SegmentBase@eptDelta` | Covered | Needs visual row |
| `SegmentTemplate@startNumber` / `SegmentTimeline` | Covered | Needs visual row |
| Period continuity | Covered | Needs visual row |
| `@initializationRefId` | Covered | Needs visual row |

## Conclusion

Do not create a normative-looking Table 2 in the source from extraction alone.
The source prose is hardened, but the table row layout should remain open until
the DOCX/PDF visual table is inspected.