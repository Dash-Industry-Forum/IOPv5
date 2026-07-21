# F-0010-H table/figure hardening report: Part 5 ad insertion

Generated: 2026-07-21

Feature bucket:

```text
F-0010-H Published Part 5 table/figure hardening
```

Primary source:

```text
rag/corpus/published/DASH-IF-IOP-Part5-v5.0.0.docx.extracted.txt
```

Primary migrated source:

```text
specs/part05-ad-insertion/05-ad-insertion.inc.md
```

Related reports:

```text
rag/reports/reconcile-part05-ad-insertion.md
rag/reports/part05-cross-reference-index.md
rag/reports/part05-f0010-implementation-plan.md
rag/reports/part05-f0010-github-issue-drafts.md
```

## Purpose

This report starts the visual/table hardening track for Part 5 before validator
and test-asset work depends on the migrated source. It identifies published
tables and figures found in the extracted source, maps them to current migrated
anchors, and assigns hardening status.

## Extraction caveat

The DOCX text extraction preserves table and figure captions, but it does not
preserve the full visual layout of embedded figures and appears to duplicate or
flatten some table hierarchy columns. Therefore:

- all tables reconstructed from extracted text need visual DOCX/PDF review,
- all figures need extraction/redrawing from the original DOCX/PDF,
- any table row derived from flattened extraction needs modal/hierarchy review.

## Published figures found in extract

| Figure | Published caption / extracted line | Source lines | Current status | Target source anchor | Hardening action |
|---|---:|---:|---|---|---|
| Figure 1 | Referenced as IF-1a/IF-1b/IF-1c architecture context | 306–308 | Not extracted | `#ad-architectures`, `#ad-interfaces-overview`, `#ad-if1-packager-ingest` | Locate in DOCX/PDF, extract/redraw, and verify IF labels. |
| Figure 3 | Abstracted Media Model with Splice Points | 301–303 | Not extracted | `#ad-if0-abr-stream-source` | Extract/redraw and verify `tsplice` model text. |
| Figure 4 | CMAF Encoder and Packager Options | 339–341 | Not extracted | `#ad-if0-abr-stream-source`, `#ad-if2-content-preparation` | Extract/redraw options 1/2/3 and align terms: Splice-Conditioned Packaging, Splice-Conditioned Encoding, Splice Point Signalling. |
| Figure 5 | CMAF Fragment to DASH Mapping for Option 1 and 3 | 404–405 | Not extracted | `#ad-if2-content-preparation` | Extract/redraw and verify mapping to Table 2 / Period generation. |
| Figure 6 | Recommended Ad Content Format | 547–548 | Not extracted | `#ad-if4d-ad-content-storage` | Extract/redraw or replace with source-level diagram for DASH-IF ad content format. |
| Figure 7 | MPD Manipulator Operation: Conforming IF-5 output | 570–586 | Not extracted | `#ad-if5-mpd-segments` | Extract/redraw and verify IF-2/IF-3/IF-4 to IF-5 flow. |

## Published tables found in extract

| Table | Published caption / extracted line | Source lines | Current status | Target source anchor | Hardening action |
|---|---:|---:|---|---|---|
| Table 1 | Interfaces identified in the ad insertion architecture, example instantiations, and references | inferred from clause 4.3 / prior migration | Reconstructed, needs visual review | `#ad-interfaces-overview` | Compare reconstructed rows IF-0 through IF-9 against DOCX/PDF. |
| Table 2 | DASH-IF Main live content MPD | 406–408 and surrounding 360–405 | Not fully reconstructed | `#ad-if2-content-preparation` | Reconstruct main live content MPD table from DOCX/PDF; extraction gives pre-table prose but not row layout. |
| Table 3 | Example of a SCTE-35 message embedded as an MPD event using SCTE 214 | 435–436 and surrounding 426–434 | Partially migrated as XML example | `#ad-if3-scte35-opportunity-signalling` | Verify XML/example layout and caption; ensure no table rows/payload were lost. |
| Table 4 | DASH-IF Ad content MPD | 546 and surrounding 520–545 | Reconstructed, needs visual review | `#ad-if4d-ad-content-storage` | Compare all MPD/Period/AdaptationSet rows and modal keywords against DOCX/PDF. |
| Table 5 | Ad Content spliced into main content | 599 and surrounding 594–620, plus extracted table rows later in source | Reconstructed, needs visual review | `#ad-if5-media-presentation-requirements` | Compare main-content and ad-content MPD rows; confirm whether split into two source tables is editorially acceptable. |

## Hardening observations from extracted source

### IF-0 / Figures 3 and 4

Lines 301–341 provide substantial source text for the abstracted media model and
encoder/packager options. The current Part 5 source contains only a baseline
summary. The hardening pass should add more explicit coverage for:

- continuous media time carried through the ABR encoder,
- splice point media time `tsplice`,
- Option 1: Splice-Conditioned Packaging,
- Option 2: Splice-Conditioned Encoding,
- Option 3: Splice Point Signalling,
- CMAF Fragment boundary assumptions,
- SAP type 1/2 assumptions for options 2 and 3,
- timed metadata needed by the MPD proxy for each splice point.

### IF-1 / Figure 1 references

Lines 305–309 refer to IF-1a, IF-1b, and IF-1c in Figure 1. The current source
summarizes IF-1 but does not preserve these sub-interface labels. Figure 1
should be extracted before deciding whether to add IF-1a/IF-1b/IF-1c anchors.

### IF-2 / Figure 5 and Table 2

Lines 360–408 contain detailed IF-2 material that should be hardened before
validator work starts. Current Part 5 source has only a baseline summary. The
next source hardening step should incorporate:

- recommendation to insert Period boundaries at `tsplice,i`,
- alternative EventStream signalling if no Period boundary is inserted,
- minimum splice point advance notice time,
- `MPD@minimumUpdatePeriod` implications,
- Initialization Set generation,
- `InitializationSet@inAllPeriods`,
- `MPD@availabilityStartTime`,
- `AssetIdentifier` examples using EIDR and DASH-IF asset-id,
- Period start calculation rules,
- continuity signalling,
- `@presentationTimeOffset`,
- `@eptDelta`,
- segment addressing for first Segment after splice.

Table 2 itself needs DOCX/PDF visual reconstruction because the extraction only
shows the caption and surrounding prose.

### IF-3 / Table 3

Lines 426–436 establish Table 3 as the SCTE-35 MPD Event example. The migrated
source already includes an XML example, but it should be checked visually
against the published table/example layout and payload.

### IF-4 / Figure 6 and Table 4

Lines 520–548 confirm Table 4 and Figure 6. The current migration includes
Table 4 content, but it should be visually reviewed. Figure 6 should be
extracted or redrawn.

### IF-5 / Figure 7 and Table 5

Lines 570–620 confirm Figure 7 and Table 5 context. The current migration
includes Table 5 split into two source-level tables. The hardening decision is
whether this split should remain or whether the Bikeshed source should recreate
the published single-table layout.

## Table/figure status matrix

| Item | Status | Next action | Priority |
|---|---|---|---|
| Figure 1 | Missing | Extract/redraw and verify IF labels | High |
| Figure 3 | Missing | Extract/redraw abstracted media model | Medium |
| Figure 4 | Missing | Extract/redraw encoder/packager options | High |
| Figure 5 | Missing | Extract/redraw CMAF-to-DASH mapping | High |
| Figure 6 | Missing | Extract/redraw ad content format | Medium |
| Figure 7 | Missing | Extract/redraw MPD manipulator operation | High |
| Table 1 | Reconstructed, unreviewed | Visual compare against DOCX/PDF | High |
| Table 2 | Source prose hardened; table not reconstructed | Reconstruct row layout from DOCX/PDF | High |
| Table 3 | Example migrated, unreviewed | Visual compare XML/example payload | Medium |
| Table 4 | Reconstructed, unreviewed | Visual compare hierarchy/modal keywords | High |
| Table 5 | Reconstructed, unreviewed | Visual compare hierarchy/modal keywords | High |

## IF-0 / IF-1 hardening status

Completed: `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if0-abr-stream-source`
and `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if1-packager-ingest`
have been hardened using the extracted published Figure 1 / Figure 3 / Figure 4
context.

Added to IF-0 source:

- continuous media timeline model,
- splice point media time `tsplice`,
- live and VoD splice-point metadata sources,
- timed metadata preservation requirements,
- Option 1: Splice-Conditioned Packaging,
- Option 2: Splice-Conditioned Encoding,
- Option 3: Splice Point Signalling,
- CMAF Fragment boundary assumptions,
- SAP type 1 / SAP type 2 assumptions for video splice points,
- downstream processing implications of options 1, 2, and 3,
- explicit issue note that Figures 3 and 4 need extraction/redrawing.

Added to IF-1 source:

- IF-1a / IF-1b / IF-1c figure-reference tracking,
- CMAF Switching Set and CMAF Track identification expectations,
- CMAF Fragment boundary identification,
- splice-point/fragment-boundary alignment expectations,
- random access point suitability expectations,
- timed metadata preservation,
- Period-boundary generation input requirements,
- MPD Event signalling input requirements,
- consistency expectations for IF-2 MPD and IF-3 opportunity metadata generation,
- explicit issue note that Figure 1 must be extracted/redrawn before the IF-1a,
  IF-1b, and IF-1c labels are stabilized.

## IF-2 hardening status

Completed: `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if2-content-preparation`
has been hardened using the extracted published source lines 360–408.

Added to source:

- Period-boundary vs EventStream signalling choices at `tsplice,i`,
- rationale for Period boundaries enabling MPD-only manipulation,
- fallback where the MPD manipulator later creates Period boundaries,
- live content assumptions,
- minimum splice point advance notice time,
- `MPD@minimumUpdatePeriod` implications,
- `InitializationSet` generation,
- `InitializationSet@inAllPeriods`,
- `MPD@availabilityStartTime`,
- `AssetIdentifier` examples using EIDR and DASH-IF asset-id,
- Period start calculation rules,
- Period continuity signalling,
- `SegmentBase@presentationTimeOffset`,
- `SegmentBase@eptDelta`,
- `SegmentTemplate@startNumber` / `SegmentTimeline` addressing,
- `@initializationRefId` handling,
- explicit issue note that Table 2 still requires visual DOCX/PDF reconstruction.

## Table reconstruction / review planning

The next F-0010-H step should shift from prose hardening to table and figure
hardening.

### Table 2

Status: source prose hardened, row layout not reconstructed.

Next action:

- visually inspect DOCX/PDF Table 2,
- reconstruct the row layout in Bikeshed table form,
- map each row to the IF-2 prose that is now present,
- classify each row as requirement, recommendation, informational, or
  non-testable,
- identify which rows feed F-0010-C Table 5 validation.

### Table 4

Status: reconstructed, needs visual review.

Next action:

- compare reconstructed Table 4 against the DOCX/PDF,
- verify `Use` column values (`M`, `O`, `R`, `OD`, cardinalities),
- verify modal strength in every row,
- identify automatable validator checks for F-0010-B,
- identify negative MPD test vectors.

### Table 5

Status: reconstructed, needs visual review.

Next action:

- compare reconstructed Table 5 against the DOCX/PDF,
- decide whether the current two-table source split should remain or whether a
  single published-style table should be recreated,
- verify `UTCTiming`, `EventStream`, `presentationTimeOffset`, Period
  continuity, and ad-content rows,
- identify automatable validator checks for F-0010-C,
- identify positive/negative multi-Period MPD test vectors.

## Recommended next source edit

The highest-value next source edit is Table 2 reconstruction if the DOCX/PDF
visual table layout is available. If visual table layout is not available, the
next best edit is Table 4 / Table 5 validator classification because those tables
are already reconstructed.

Recommended next report/source targets:

```text
rag/reports/part05-f0010-table2-reconstruction.md
rag/reports/part05-f0010-table4-validator-matrix.md
rag/reports/part05-f0010-table5-validator-matrix.md
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if2-content-preparation
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if4d-ad-content-storage
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if5-media-presentation-requirements
```

## Acceptance criteria for F-0010-H

- [x] Identify published figure captions in extract.
- [x] Identify published table captions in extract.
- [x] Map each table/figure to Part 5 source anchors.
- [x] Identify missing figures.
- [x] Identify tables requiring visual DOCX/PDF review.
- [ ] Extract or redraw figures.
- [x] Harden IF-0 / IF-1 source prose from extracted Figure 1 / Figure 3 / Figure 4 context.
- [x] Harden IF-2 source prose from extracted Figure 5 / Table 2 context.
- [ ] Reconstruct Table 2 row layout from DOCX/PDF.
- [ ] Visually review Tables 1, 3, 4, and 5.
- [ ] Create Table 4 validator matrix for F-0010-B.
- [ ] Create Table 5 validator matrix for F-0010-C.
- [ ] Update Part 5 source after visual review.
- [ ] Update reconciliation report with final status.