# Part 5 ad-insertion reconciliation and migration map

Generated: 2026-07-21

This report starts the clause-level migration map for DASH-IF IOP v5 Part 5,
*Ad Insertion in DASH*.

Source inputs:

- Published source:
  `rag/corpus/published/DASH-IF-IOP-Part5-v5.0.0.docx`
- Extracted text:
  `rag/corpus/published/DASH-IF-IOP-Part5-v5.0.0.docx.extracted.txt`
- Current Bikeshed source:
  `specs/part05-ad-insertion/05-ad-insertion.inc.md`

## Summary

Part 5 is currently a shell in the Bikeshed source. The published v5.0.0 source
is substantial: the extracted text has 941 lines and includes a full ad-insertion
architecture, terminology, interface model, interface-specific requirements, MPD
and segment requirements, ad metadata signalling, decisioning parameters, remote
resolution, tracking, and examples/tables.

The correct next action is **structured migration**, not small clause repair.
Part 5 should be migrated section-by-section from the published document into the
current Bikeshed source while preserving traceability and avoiding duplication
with Parts 1, 2, and 12.

Recommended status label for Part 5:

```text
Skeleton → Draft / published-content migration
```

## Published heading structure

The extracted published Part 5 heading candidates are:

- Executive summary
- Introduction
- Scope
- References
- Normative references
- Informative references
- Definition of terms, symbols and abbreviations
- Terms
- Symbols
- Abbreviations
- 4 Introduction
- 4.1 Use Cases and Scenarios
- 4.1.1 Overview
- 4.1.2 VoD
- 4.1.3 Live
- 4.1.4 Recorded Live
- 4.1.5 Pre-Roll into Live
- 4.1.6 Obfuscation of Inserted Ads
- 4.1.7 Changes that may happen at Transitions of Main Content and Ads
- 4.2 Architectures
- 4.3 Overview on Interfaces and Functions
- 5 Interfaces
- 5.1 IF-0: ABR Stream Source
- 5.1.1 General
- 5.1.2 Live Workflow Descriptive Metadata
- 5.1.3 VOD Workflow Descriptive Metadata
- 5.1.4 Abstracted Model
- 5.2 IF-1: Packager Ingest
- 5.3 IF-9: Reference Media Playback and Decryption
- 5.4 IF-2: Content Preparation
- 5.5 IF-3: Ad Avail Signalling
- 5.5.1 Introduction
- 5.5.2 Opportunity Signalling via SCTE-35
- 5.6 IF-4: Ad Decisioning and Exchange Interfaces
- 5.6.1 Introduction
- 5.6.2 IF-4a: Ad Decision request parameters
- 5.6.2.1 Decisioning Parameters
- 5.6.2.2 Decisioning Modes
- 5.6.3 IF-4b: Content Conditioning request parameters
- 5.6.4 IF-4e: Ad Selection Result format
- 5.6.4.1 Overview
- 5.6.4.2 IAB VAST
- 5.6.4.3 SCTE-130
- 5.6.5 IF-4d: DASH-IF Ad Content Storage format
- 5.6.6 IF-4f: DASH-IF Recommended Slate Content
- 5.6.7 IF-4c: Recommended Dynamic Ad Content Response format based on conditioning parameters
- 5.7 IF-5: MPD and Segments with Ad Placements
- 5.7.1 Overview
- 5.7.2 Media Presentation Requirements on IF-5
- 5.7.3 MPD Proxy Operation Guidelines
- 5.7.4 DASH Client Operation Requirements and Guidelines for Playback on Reference Platform
- 5.8 IF-6: Ad Metadata Signalling
- 5.8.1 Introduction
- 5.8.2 DASH Callback Event
- 5.9 IF-7: Ad Decisioning Parameters and Remote Resolution
- 5.9.1 Introduction
- 5.9.2 IF-7a: Decisioning Parameters via URL Parameters
- 5.9.3 IF-7b: Content Conditioning via URL Parameters
- 5.9.4 IF-7c: Late Binding via Remote Periods
- 5.10 IF-8: Ad Tracking and Measurement
- 5.10.1 Introduction
- 5.10.2 VAST View Tracking
- 5.10.3 Open Measurement SDK
- 5.10.4 Alternative Tracking Methods
- Annex A: Change History

## Current Bikeshed heading structure

Current Part 5 source headings are only:

- Scope
- References
- Terms and Definitions
- Requirements and Recommendations
- Open Issues and Work Items
- Change History

## Clause migration map

| Published area | Current Bikeshed location | Status | Migration action |
|---|---|---|---|
| Executive summary / Introduction / Scope | `05-ad-insertion.inc.md` / `#scope` | Shell only | Replace shell scope with published scope summary and explicit exclusions, especially CSAI exclusion and CMAF-aligned scope. |
| References | `05-ad-insertion.inc.md` / `#doc-references`; likely `.bs` biblio | Partial | Add missing published references: IOP Part 1, SCTE 35, SCTE 104, DASH-IF Ingest, CTA-5003, SMPTE RP 2079, EIDR, SCTE 214-1, SCTE 214-3, SCTE 130-3, SMPTE RP 2092-1, CableLabs VoD, RIST, W3C MSE/EME, IAB VAST, Open Measurement SDK, ITU-R BS.1770-4. |
| Terms | `#terms` | Missing | Migrate published ad-insertion terms: ABR encoder, ad avail processor, ad content server, ad creative, ad decision service, ad insertion MPD manipulator, ad pod, ad reporting server, ad slot, CDN node, CSAI, CMAF packager, DASH ad resolver, DASH access client, DASH packager, DASH-IF ad content, default content, MPD generator, origin, placement opportunity, reference playback platform, SSAI, SGAI, service provider, splice point, tracking event. |
| Abbreviations | `#terms` or new abbreviations subsection | Missing | Migrate published abbreviations: ABR, ADS, CSAI, CDN, CMAF, CTA, DASH, DASH-IF, EIDR, HTTP, IAB, IF, IOP, ISO, MPD, MPEG, RIST, SCTE, SGAI, SMPTE, SSAI, TS, VAST, VOD, WAVE. |
| 4.1 Use Cases and Scenarios | New `#ad-use-cases-scenarios` | Missing | Create narrative subsections for VoD, Live, Recorded Live, Pre-Roll into Live, Obfuscation of Inserted Ads, and transition-change considerations. |
| 4.2 Architectures | New `#ad-architectures` | Missing | Migrate architecture overview and identify figures/tables needing reconstruction. |
| 4.3 Overview on Interfaces and Functions | New `#ad-interfaces-overview` | Missing | Migrate interface overview and Table 1. This should become the structural backbone of Part 5. |
| 5.1 IF-0 ABR Stream Source | New `#ad-if0-abr-stream-source` | Missing | Migrate general, live workflow descriptive metadata, VOD workflow descriptive metadata, and abstracted model. |
| 5.2 IF-1 Packager Ingest | New `#ad-if1-packager-ingest` | Missing | Migrate ingest requirements and align with DASH-IF Ingest reference. |
| 5.3 IF-9 Reference Media Playback and Decryption | New `#ad-if9-reference-playback-decryption` | Missing | Migrate playback/decryption interface guidance; align with Part 6 and Part 12. |
| 5.4 IF-2 Content Preparation | New `#ad-if2-content-preparation` | Missing | Migrate content conditioning/preparation requirements, including CMAF alignment and any Table 2 material. |
| 5.5 IF-3 Ad Avail Signalling | New `#ad-if3-ad-avail-signalling` | Missing | Migrate SCTE-35 opportunity signalling and Table 3 example. |
| 5.6 IF-4 Ad Decisioning and Exchange Interfaces | New `#ad-if4-decisioning-exchange` | Missing | Migrate request parameters, decisioning modes, conditioning request parameters, ad selection result formats, VAST/SCTE-130 references, ad content storage, slate content, and dynamic ad content response format. |
| 5.7 IF-5 MPD and Segments with Ad Placements | New `#ad-if5-mpd-segments` | Missing | High-priority normative migration. Migrate MPD/segment requirements, MPD proxy operation guidelines, and playback requirements. |
| 5.8 IF-6 Ad Metadata Signalling | New `#ad-if6-ad-metadata` | Missing | Migrate DASH callback event material. |
| 5.9 IF-7 Decisioning Parameters and Remote Resolution | New `#ad-if7-remote-resolution` | Missing | Migrate URL parameter decisioning, content conditioning parameters, and late binding via remote periods. |
| 5.10 IF-8 Ad Tracking and Measurement | New `#ad-if8-tracking-measurement` | Missing | Migrate VAST view tracking, Open Measurement SDK, and alternative tracking methods. |
| Annex A Change History | `#change-history` | Partial | Add published v5.0.0 row and migration-history row. |

## Recommended migration order

Use small, auditable increments:

1. **Front matter and terminology**
   - Scope
   - references placeholders/biblio
   - terms
   - abbreviations
2. **Use cases and architecture**
   - 4.1 use cases
   - 4.2 architectures
   - 4.3 interfaces overview
3. **Interface skeleton**
   - add stable headings/anchors for IF-0 through IF-9
   - add TODO/provenance issue notes under each heading
4. **High-value normative sections**
   - IF-5 MPD and Segments with Ad Placements
   - IF-3 Ad Avail Signalling
   - IF-4 Ad Decisioning and Exchange Interfaces
5. **Examples/tables**
   - reconstruct Table 1 through Table 5 from published source
   - identify figures/images needing extraction or redrawing
6. **Conformance mapping**
   - create Part 5 feature ID after first source migration
   - add Part 12 ad-insertion mapping once requirements are stable

## First concrete implementation status

Completed: `specs/part05-ad-insertion/05-ad-insertion.inc.md` has been replaced
with a structured skeleton that mirrors the published document.

The first source edit added:

- published-scope summary,
- reference placeholders,
- terms list and abbreviations table from the published source,
- use-cases and architecture headings,
- IF-0 through IF-9 headings and subheadings,
- open-issue table that tracks migration by clause,
- published v5.0.0 change-history row.

This creates stable anchors and review structure without prematurely copying the
entire 941-line extracted source into one large Bikeshed edit.

Completed: the interface overview table has been reconstructed in
`specs/part05-ad-insertion/05-ad-insertion.inc.md`, and published Part 5
bibliography aliases have been added to `specs/part05-ad-insertion/part05-ad-insertion.bs`.

Completed: initial migration of IF-5 MPD and Segments with Ad Placements has
been added to `specs/part05-ad-insertion/05-ad-insertion.inc.md`.

The migrated IF-5 material covers:

- IF-5 overview and MPD manipulator assumptions,
- `tsplice-out` / `tsplice-in` timing concepts,
- ad-duration match, overrun, and underrun handling cases,
- Media Presentation requirement that IF-5 content conforms to the DASH Extended
  Profile for CMAF content with multi-period requirements,
- SSAI MPD proxy operation guidelines,
- inserted Period ordering and start-time rules,
- Period continuity signalling and EventStream copying guidance,
- termination/early-truncation/extension handling,
- SGAI deferred resolution note,
- DASH client playback guidance for Period continuity, Period connectivity, CMAF
  header switching, and timing adjustment cases.

Completed: published Part 5 Table 5 has been reconstructed in
`specs/part05-ad-insertion/05-ad-insertion.inc.md` as two source-level tables:

- main content MPD requirements relevant to IF-5 insertion,
- ad insertion content MPD requirements relevant to IF-5 insertion.

The reconstructed tables cover the extracted MPD, Period, EventStream,
AdaptationSet, Representation, BaseURL, UTCTiming, LeapSecondInformation, and
SegmentBase-related rows from published text lines 740–841.

Completed: IF-3 Ad Avail Signalling and the initial IF-4 Ad Decisioning and
Exchange Interfaces material have been migrated into
`specs/part05-ad-insertion/05-ad-insertion.inc.md`.

The migrated IF-3 material covers:

- opportunity metadata composition,
- DASH MPD Events as the required carriage mechanism,
- required opportunity metadata fields,
- SCTE-35 opportunity signalling,
- SCTE 214 event schemes,
- `time_signal()` / `segmentation_descriptor()` usage,
- `splice_insert()` legacy usage,
- `@presentationTime` and `@duration` derivation,
- example SCTE-35 MPD Event.

The migrated IF-4 material covers:

- IF-4 introduction and six sub-interface model,
- assumptions about ad decision and ad content entities,
- IF-4a ad decision request parameters,
- stream-level and pod-level decisioning modes,
- IF-4b content-conditioning request parameters,
- IF-4e ad selection result format,
- IAB VAST mapping, and
- SCTE-130 mapping.

Next implementation target: continue IF-4 with IF-4d DASH-IF Ad Content Storage
format, IF-4f DASH-IF Recommended Slate Content, IF-4c Recommended Dynamic Ad
Content Response format, and published Table 4.

## Terminology migration status

Completed: published Part 5 term definitions have been migrated into
`specs/part05-ad-insertion/05-ad-insertion.inc.md` in Bikeshed definition-list
form.

Migrated terms:

- ABR encoder
- ad avail processor
- ad content server
- ad creative
- ad decision service
- ad insertion MPD manipulator
- ad pod
- ad reporting server
- ad slot
- CDN node
- client-side ad insertion
- CMAF packager
- DASH access client
- DASH ad resolver
- DASH packager
- DASH-IF ad content
- default content
- MPD generator
- origin
- placement opportunity
- reference playback platform
- server-side ad insertion
- server-guided ad insertion
- service provider
- splice point
- tracking event

Remaining terminology work:

- review exact editorial wording against the published DOCX/PDF,
- decide whether repeated terms should be shared across parts,
- normalize abbreviations against shared glossary policy.

## Bibliography and interface overview status

Completed: `part05-ad-insertion.bs` now contains local bibliography aliases for
the published Part 5 references, including MPEG-DASH, CMAF, IOP Part 1,
SCTE-35, SCTE-104, DASH-IF Ingest, CTA-5003, SMPTE/EIDR/Ad-ID references,
SCTE 214, SCTE 130, CableLabs VoD, MPEG-2 Systems, RIST, W3C MSE/EME, IAB VAST,
Open Measurement SDK, and ITU-R BS.1770-4.

Completed: `05-ad-insertion.inc.md` now includes a reconstructed interface
overview table for IF-0 through IF-9. The table maps each interface to its
function, example instantiations / related references, and the stable migration
target anchor in the Part 5 source.

Remaining review work:

- compare the reconstructed table against the published DOCX/PDF Table 1 layout,
- confirm whether all references should remain local aliases or move to shared
  Bikeshed/shared-bibliography names,
- extract or redraw the published architecture figure labels that correspond to
  the IF-0 through IF-9 table.

## IF-5 migration status

Completed: the first IF-5 migration pass is in
`specs/part05-ad-insertion/05-ad-insertion.inc.md` under
`#ad-if5-mpd-segments`.

Migrated subsections:

- `#ad-if5-mpd-segments`
- `#ad-if5-media-presentation-requirements`
- `#ad-if5-mpd-proxy-guidelines`
- `#ad-if5-client-playback-guidelines`

Remaining IF-5 work:

- visually check reconstructed Table 5 against the published DOCX/PDF because
  the DOCX extraction duplicated hierarchy columns and may have lost formatting,
- review exact modal strength against the published source,
- align Period continuity/connectivity language with Part 2,
- align SGAI deferred-resolution language with current event/remote-resolution
  work in other parts,
- add conformance mapping after Table 5 review.

## IF-3 and IF-4 migration status

Completed: IF-3 Ad Avail Signalling was migrated from published clause 5.5 into
`#ad-if3-ad-avail-signalling`, including SCTE-35 MPD Event signalling and the
published XML example.

Completed: an initial IF-4 migration was added under
`#ad-if4-decisioning-exchange`, covering the IF-4 introduction, IF-4a, IF-4b,
and IF-4e including VAST and SCTE-130 mappings.

Completed: the remaining initial IF-4 sections were migrated into
`specs/part05-ad-insertion/05-ad-insertion.inc.md`.

Additional migrated IF-4 material:

- IF-4d DASH-IF Ad Content Storage format,
- reconstructed Table 4 DASH-IF ad content MPD requirements,
- IF-4f DASH-IF Recommended Slate Content,
- IF-4c Recommended Dynamic Ad Content Response format.

The initial IF-4 migration now covers published clauses 5.6.1 through 5.6.7 at
source level.

Remaining IF-4 work:

- visually review reconstructed Table 4 against the published DOCX/PDF because
  extraction may have lost hierarchy/formatting,
- verify exact modal strength against the published source and current drafting
  policy,
- confirm whether Table 4 and IF-5 Table 5 should share a single canonical table
  or remain duplicated at each interface location,
- add conformance mapping once IF-4 table and modal review is complete.

## IF-6, IF-7, and IF-8 migration status

Completed: initial IF-6 Ad Metadata Signalling was migrated into
`#ad-if6-ad-metadata`, including a DASH Callback Event baseline.

Completed: initial IF-7 Ad Decisioning Parameters and Remote Resolution was
migrated into `#ad-if7-remote-resolution`, including:

- IF-7a decisioning parameters via URL parameters,
- IF-7b content conditioning via URL parameters,
- IF-7c late binding via Remote Periods.

Completed: initial IF-8 Ad Tracking and Measurement was migrated into
`#ad-if8-tracking-measurement`, including:

- VAST view tracking,
- Open Measurement SDK,
- alternative tracking methods.

Remaining IF-6/IF-7/IF-8 work:

- verify exact DASH Callback Event scheme, payload structure, and examples
  against the published DOCX/PDF,
- align IF-6 with current Part 10 event guidance,
- align IF-7c with the current DASH remote entity model and SGAI work,
- verify detailed VAST event/callback rules and Open Measurement wording,
- add conformance/test-assets mapping for tracking and remote-resolution
  behaviour.

## Use cases, architecture, and early-interface migration status

Completed: initial use-case and scenario prose was migrated into
`#ad-use-cases-scenarios`, including VoD, live, recorded live, pre-roll into
live, obfuscation of inserted ads, and transition changes between main content
and ads.

Completed: an initial architecture baseline was migrated into
`#ad-architectures`, covering SSAI, SGAI, and the common functional entities in
the Part 5 architecture.

Completed: initial source-level baselines were migrated for the early interfaces:

- IF-0 ABR Stream Source,
- IF-1 Packager Ingest,
- IF-9 Reference Media Playback and Decryption,
- IF-2 Content Preparation.

Remaining work for these sections:

- compare the use-case and architecture prose against the published DOCX/PDF,
- extract or redraw the published architecture figures,
- review exact live/VOD metadata examples for IF-0,
- review ingest details against DASH-IF Ingest for IF-1,
- align IF-9 playback/decryption constraints with Parts 6 and 12,
- reconstruct IF-2 content-preparation Table 2 material if present in the
  published table layout.

## Cross-part indexing and conformance status

Completed: feature `F-0010` was added to
`docs/governance/feature-registry.md` to track Part 5 ad-insertion conformance
and cross-part indexing across Parts 1, 2, 5, 6, 10, and 12.

Completed: Part 12 now contains an initial Part 5 ad-insertion conformance
mapping at:

```text
specs/part12-conformance-reference-tools/01-conformance.inc.md#tools-part5-ad-insertion-conformance
```

The Part 12 mapping covers:

- IF-3 opportunity metadata and SCTE-35 MPD Events,
- IF-4 DASH-IF ad content storage and Table 4 requirements,
- IF-5 MPD and segments with ad placements,
- IF-6 ad metadata and DASH Callback Events,
- IF-7 remote resolution and URL parameter decisioning,
- IF-8 ad tracking and measurement,
- IF-9 reference playback and decryption.

Completed: a Part 5 cross-reference index was created at:

```text
rag/reports/part05-cross-reference-index.md
```

The index maps Part 5 anchors to cross-part dependencies and conformance/test
targets. It starts the cross-reference work for Part 1 architecture vocabulary,
Part 2 Period/CMAF/continuity concepts, Part 6 playback/decryption alignment,
Part 10 event/callback alignment, Part 11 remote-entity considerations, and
Part 12 validator/dash.js/livesim2/test-assets planning.

Completed: an issue-ready F-0010 implementation plan was created at:

```text
rag/reports/part05-f0010-implementation-plan.md
```

The implementation plan defines concrete issue buckets:

- F-0010-A: Validator checks for IF-3 SCTE-35 MPD Events,
- F-0010-B: Validator checks for DASH-IF ad content MPD / Table 4,
- F-0010-C: Validator checks for IF-5 multi-Period ad insertion / Table 5,
- F-0010-D: SGAI remote-resolution coverage with dash.js and livesim2,
- F-0010-E: VAST/Open Measurement tracking sample coverage,
- F-0010-F: clear/encrypted ad insertion playback assets,
- F-0010-G: cross-part anchor and terminology harmonization,
- F-0010-H: published Part 5 table/figure hardening.

Completed: `rag/reports/part05-cross-reference-index.md` was updated with the
same F-0010 issue buckets, their related Part 5 anchors, and their primary
cross-part dependencies.

Completed: copy/paste-ready GitHub issue drafts for F-0010-A through F-0010-H
were created at:

```text
rag/reports/part05-f0010-github-issue-drafts.md
```

The issue drafts include titles, scope, source anchors, proposed checks or
tasks, test assets where applicable, and acceptance criteria.

Started: F-0010-H table/figure hardening. A table/figure hardening report was
created at:

```text
rag/reports/part05-f0010-table-figure-hardening.md
```

The report identifies published figure captions and table captions found in the
extracted Part 5 source, maps them to Part 5 anchors, and assigns initial
hardening status.

Published figures identified as missing from the Bikeshed source:

- Figure 1: IF-1a/IF-1b/IF-1c architecture context,
- Figure 3: Abstracted Media Model with Splice Points,
- Figure 4: CMAF Encoder and Packager Options,
- Figure 5: CMAF Fragment to DASH Mapping for Option 1 and 3,
- Figure 6: Recommended Ad Content Format,
- Figure 7: MPD Manipulator Operation: Conforming IF-5 output.

Published tables tracked for hardening:

- Table 1: interface overview, reconstructed but not visually reviewed,
- Table 2: DASH-IF Main live content MPD, not reconstructed,
- Table 3: SCTE-35 MPD Event example, partially migrated and not visually
  reviewed,
- Table 4: DASH-IF Ad content MPD, reconstructed but not visually reviewed,
- Table 5: Ad Content spliced into main content, reconstructed but not visually
  reviewed.

Completed: IF-2 content preparation was hardened in:

```text
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if2-content-preparation
```

The IF-2 hardening incorporated the published extracted material around lines
360–408, including:

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
- explicit issue note that Table 2 still requires visual DOCX/PDF
  reconstruction.

The hardening report was updated to record IF-2 as hardened while leaving Table
2 row-layout reconstruction open.

Completed: IF-0 and IF-1 were hardened in:

```text
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if0-abr-stream-source
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if1-packager-ingest
```

The IF-0 / IF-1 hardening added:

- continuous media timeline model,
- splice point media time `tsplice`,
- live and VoD splice-point metadata sources,
- timed metadata preservation expectations,
- Option 1: Splice-Conditioned Packaging,
- Option 2: Splice-Conditioned Encoding,
- Option 3: Splice Point Signalling,
- CMAF Fragment boundary assumptions,
- SAP type 1 / SAP type 2 assumptions for video splice points,
- downstream processing implications of the preparation options,
- IF-1a / IF-1b / IF-1c figure-reference tracking,
- CMAF Switching Set / CMAF Track identification expectations,
- Period-boundary and MPD Event signalling inputs for IF-2 / IF-3 generation.

Completed: the F-0010-H hardening report was updated to record IF-0 / IF-1
hardening and to shift the next work from prose hardening to table/figure
hardening and validator classification.

Completed: a Table 4 validator matrix for F-0010-B was created at:

```text
rag/reports/part05-f0010-table4-validator-matrix.md
```

It classifies reconstructed Table 4 rows as validator errors, warnings,
informational checks, manual-review items, or not-testable items, and proposes
positive and negative MPD test vectors for DASH-IF ad content MPDs.

Completed: Table 2 reconstruction status was documented at:

```text
rag/reports/part05-f0010-table2-reconstruction.md
```

The report records that the current extraction preserves the Table 2 caption and
surrounding IF-2 prose, but not the row layout. Therefore, IF-2 prose is
hardened, while normative-looking Table 2 reconstruction remains blocked pending
visual DOCX/PDF inspection.

Completed: a Table 5 validator matrix for F-0010-C was created at:

```text
rag/reports/part05-f0010-table5-validator-matrix.md
```

It classifies reconstructed Table 5 main-content and ad-content rows, identifies
which checks should reuse the Table 4 validator module, and proposes scenario
checks and test vectors for multi-Period SSAI outputs.

Completed: validator implementation issue scopes for F-0010-B and F-0010-C were
created at:

```text
rag/reports/part05-f0010-validator-implementation-issues.md
```

The implementation issue report defines:

- F-0010-B1: DASH-IF ad content MPD structural validator checks,
- F-0010-B2: DASH-IF ad content MPD test vectors,
- F-0010-C1: IF-5 multi-Period structural validator checks,
- F-0010-C2: Table 4 check reuse for IF-5 source ad-content MPDs,
- F-0010-C3: IF-5 SSAI scenario test vectors.

Completed: a SCTE-35 validator matrix for F-0010-A was created at:

```text
rag/reports/part05-f0010-scte35-validator-matrix.md
```

It covers MPD-level SCTE-35 EventStream checks, payload-dependent checks,
positive/negative vectors, and implementation issues for MPD-level SCTE-35
checking, payload-aware checking, and IF-3 SCTE-35 test vectors.

Completed: runtime/test planning for F-0010-D, F-0010-F, and F-0010-E was
created at:

```text
rag/reports/part05-f0010-runtime-test-planning.md
```

It covers:

- SGAI remote-resolution coverage with dash.js and livesim2,
- clear/encrypted ad insertion playback assets,
- VAST/Open Measurement tracking sample coverage.

Completed: a single F-0010 issue index was created at:

```text
rag/reports/part05-f0010-issue-index.md
```

The issue index links all generated F-0010 planning reports and defines the
final GitHub issue set in implementation order across five phases:

1. source tables and figures,
2. structural validator coverage,
3. SCTE-35 opportunity-event coverage,
4. runtime/reference-client/test-assets coverage,
5. cross-part link and terminology integration.

The final indexed issue set contains F-0010-H1 through F-0010-H5, F-0010-B1
through F-0010-B2, F-0010-C1 through F-0010-C3, F-0010-A1 through F-0010-A3,
F-0010-D1 through F-0010-D3, F-0010-F1 through F-0010-F2, F-0010-E1 through
F-0010-E2, and F-0010-G1 through F-0010-G3.

Remaining cross-part work:

- create GitHub issues from the prepared F-0010-A through F-0010-H drafts,
- link Part 5 anchors to Part 2/6/10/12 anchors once stable cross-document
  linking policy is finalized,
- reconcile the Part 12 mapping with actual validator, dash.js, livesim2, and
  Test Assets coverage,
- add Part 5 conformance requirements to Part 12 once modal/table review is
  complete.

## Validation

After each Part 5 migration edit, run:

```powershell
python tools/publication/check_links.py
```

Bikeshed HTML build validation remains dependent on resolving the corporate
TLS/Bikeshed remote-data update issue already documented in the Part 6
reconciliation report.