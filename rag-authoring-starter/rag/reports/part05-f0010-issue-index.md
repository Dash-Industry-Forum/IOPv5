# F-0010 issue index: Part 5 ad-insertion conformance and cross-part indexing

Generated: 2026-07-21

Feature registry entry:

```text
F-0010 Part 5 ad-insertion conformance and cross-part indexing
```

Target parts:

```text
Part 1, Part 2, Part 5, Part 6, Part 10, Part 12
```

## Purpose

This is the single index for all generated F-0010 planning reports and the final
issue set to create in GitHub or another tracker.

It consolidates:

- Part 5 table/figure hardening,
- Table 2 reconstruction status,
- Table 4 DASH-IF ad content MPD validation,
- Table 5 IF-5 multi-Period ad insertion validation,
- IF-3 SCTE-35 MPD Event validation,
- SGAI runtime/reference-client testing,
- clear/encrypted playback testing,
- VAST/Open Measurement tracking testing,
- cross-part anchor and terminology harmonization.

## Source and planning reports

| Report | Purpose |
|---|---|
| `rag/reports/part05-cross-reference-index.md` | Cross-part index mapping Part 5 anchors to dependencies and conformance/test targets. |
| `rag/reports/part05-f0010-implementation-plan.md` | Original F-0010 implementation plan and issue-bucket definitions. |
| `rag/reports/part05-f0010-github-issue-drafts.md` | Copy/paste GitHub issue drafts for F-0010-A through F-0010-H. |
| `rag/reports/part05-f0010-table-figure-hardening.md` | Table/figure hardening status for Part 5, including IF-0/IF-1/IF-2 source hardening. |
| `rag/reports/part05-f0010-table2-reconstruction.md` | Table 2 reconstruction status; records that visual DOCX/PDF inspection is required. |
| `rag/reports/part05-f0010-table4-validator-matrix.md` | Validator matrix for Table 4 DASH-IF ad content MPD. |
| `rag/reports/part05-f0010-table5-validator-matrix.md` | Validator matrix for Table 5 IF-5 multi-Period ad insertion. |
| `rag/reports/part05-f0010-validator-implementation-issues.md` | Concrete implementation issue scopes for F-0010-B and F-0010-C. |
| `rag/reports/part05-f0010-scte35-validator-matrix.md` | Validator matrix and implementation scopes for F-0010-A SCTE-35 MPD Events. |
| `rag/reports/part05-f0010-runtime-test-planning.md` | Runtime/test planning for F-0010-D, F-0010-F, and F-0010-E. |
| `rag/reports/reconcile-part05-ad-insertion.md` | Part 5 migration/reconciliation status roll-up. |

## Primary source anchors

| Area | Anchor |
|---|---|
| IF-0 ABR Stream Source | `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if0-abr-stream-source` |
| IF-1 Packager Ingest | `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if1-packager-ingest` |
| IF-2 Content Preparation | `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if2-content-preparation` |
| IF-3 Ad Avail Signalling | `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if3-ad-avail-signalling` |
| IF-3 SCTE-35 Opportunity Signalling | `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if3-scte35-opportunity-signalling` |
| IF-4 DASH-IF Ad Content Storage | `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if4d-ad-content-storage` |
| IF-5 Media Presentation Requirements | `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if5-media-presentation-requirements` |
| IF-5 Client Playback Guidelines | `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if5-client-playback-guidelines` |
| IF-7 Remote Resolution | `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if7-remote-resolution` |
| IF-8 Tracking and Measurement | `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if8-tracking-measurement` |
| IF-9 Reference Playback and Decryption | `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if9-reference-playback-decryption` |
| Part 12 Part 5 conformance mapping | `specs/part12-conformance-reference-tools/01-conformance.inc.md#tools-part5-ad-insertion-conformance` |

## Final GitHub issue set in implementation order

### Phase 1: stabilize source tables and figures

| Order | Issue ID | Title | Source report | Dependencies |
|---:|---|---|---|---|
| 1 | F-0010-H1 | Harden Part 5 figures against published DOCX/PDF | `part05-f0010-table-figure-hardening.md` | none |
| 2 | F-0010-H2 | Reconstruct Part 5 Table 2 row layout from DOCX/PDF | `part05-f0010-table2-reconstruction.md` | F-0010-H1 optional |
| 3 | F-0010-H3 | Visually review Part 5 Table 4 DASH-IF ad content MPD | `part05-f0010-table-figure-hardening.md`, `part05-f0010-table4-validator-matrix.md` | none |
| 4 | F-0010-H4 | Visually review Part 5 Table 5 IF-5 multi-Period ad insertion | `part05-f0010-table-figure-hardening.md`, `part05-f0010-table5-validator-matrix.md` | none |
| 5 | F-0010-H5 | Decide Table 4/Table 5 canonical table reuse strategy | `part05-f0010-table4-validator-matrix.md`, `part05-f0010-table5-validator-matrix.md` | F-0010-H3, F-0010-H4 |

### Phase 2: implement structural validator coverage

| Order | Issue ID | Title | Source report | Dependencies |
|---:|---|---|---|---|
| 6 | F-0010-B1 | Implement DASH-IF ad content MPD structural validator checks | `part05-f0010-validator-implementation-issues.md`, `part05-f0010-table4-validator-matrix.md` | F-0010-H3 |
| 7 | F-0010-B2 | Add DASH-IF ad content MPD positive and negative test vectors | `part05-f0010-validator-implementation-issues.md`, `part05-f0010-table4-validator-matrix.md` | F-0010-B1 |
| 8 | F-0010-C1 | Implement IF-5 multi-Period structural validator checks | `part05-f0010-validator-implementation-issues.md`, `part05-f0010-table5-validator-matrix.md` | F-0010-H4 |
| 9 | F-0010-C2 | Reuse Table 4 checks for source ad-content MPDs used by IF-5 | `part05-f0010-validator-implementation-issues.md` | F-0010-B1, F-0010-C1 |
| 10 | F-0010-C3 | Add IF-5 SSAI scenario test vectors | `part05-f0010-validator-implementation-issues.md`, `part05-f0010-table5-validator-matrix.md` | F-0010-C1 |

### Phase 3: implement SCTE-35 opportunity-event coverage

| Order | Issue ID | Title | Source report | Dependencies |
|---:|---|---|---|---|
| 11 | F-0010-A1 | Implement MPD-level SCTE-35 EventStream checks | `part05-f0010-scte35-validator-matrix.md` | none |
| 12 | F-0010-A2 | Add SCTE-35 payload-aware checks | `part05-f0010-scte35-validator-matrix.md` | F-0010-A1 |
| 13 | F-0010-A3 | Add IF-3 SCTE-35 positive and negative test vectors | `part05-f0010-scte35-validator-matrix.md` | F-0010-A1 |

### Phase 4: implement runtime/reference-client/test-assets coverage

| Order | Issue ID | Title | Source report | Dependencies |
|---:|---|---|---|---|
| 14 | F-0010-D1 | Document livesim2 SGAI scenario mapping | `part05-f0010-runtime-test-planning.md` | F-0010-A1 optional |
| 15 | F-0010-D2 | Add or identify dash.js SGAI sample coverage | `part05-f0010-runtime-test-planning.md` | F-0010-D1 |
| 16 | F-0010-D3 | Add SGAI remote-resolution test-asset entries | `part05-f0010-runtime-test-planning.md` | F-0010-D1, F-0010-D2 |
| 17 | F-0010-F1 | Define Part 6 alignment points for IF-9 clear/encrypted transitions | `part05-f0010-runtime-test-planning.md` | none |
| 18 | F-0010-F2 | Add dash.js clear/encrypted ad insertion playback test assets | `part05-f0010-runtime-test-planning.md` | F-0010-F1, F-0010-C3 |
| 19 | F-0010-E1 | Define VAST tracking callback timeline assets | `part05-f0010-runtime-test-planning.md` | F-0010-C3 |
| 20 | F-0010-E2 | Define Open Measurement integration sample | `part05-f0010-runtime-test-planning.md` | F-0010-E1 |

### Phase 5: cross-part link and terminology integration

| Order | Issue ID | Title | Source report | Dependencies |
|---:|---|---|---|---|
| 21 | F-0010-G1 | Harmonize Part 5 cross-part anchors with Parts 1, 2, 6, 10, and 12 | `part05-cross-reference-index.md`, `part05-f0010-implementation-plan.md` | F-0010-H1 through F-0010-H5 |
| 22 | F-0010-G2 | Normalize Part 5 terminology and bibliography across parts | `part05-cross-reference-index.md`, `reconcile-part05-ad-insertion.md` | F-0010-G1 |
| 23 | F-0010-G3 | Update Part 12 conformance mapping after validator/test planning stabilizes | `01-conformance.inc.md#tools-part5-ad-insertion-conformance`, all F-0010 reports | F-0010-B/C/A/D/F/E issues |

## Labels

Suggested labels for all F-0010 issues:

```text
feature:F-0010
part-5
ad-insertion
conformance
cross-part
```

Additional labels by issue family:

| Family | Labels |
|---|---|
| F-0010-H | `editorial`, `tables`, `figures`, `published-source-review` |
| F-0010-A | `scte35`, `events`, `validator`, `test-assets` |
| F-0010-B | `validator`, `mpd`, `dash-if-ad-content`, `test-assets` |
| F-0010-C | `validator`, `multi-period`, `ssai`, `test-assets` |
| F-0010-D | `sgai`, `dash.js`, `livesim2`, `remote-resolution` |
| F-0010-E | `vast`, `open-measurement`, `tracking`, `samples` |
| F-0010-F | `content-protection`, `eme`, `mse`, `playback` |
| F-0010-G | `terminology`, `anchors`, `cross-reference`, `part-12` |

## Milestone grouping

Recommended milestone split:

| Milestone | Issues |
|---|---|
| F-0010 Source stabilization | F-0010-H1 through F-0010-H5 |
| F-0010 Validator MVP | F-0010-B1, F-0010-B2, F-0010-C1, F-0010-C2, F-0010-A1 |
| F-0010 Validator extended | F-0010-C3, F-0010-A2, F-0010-A3 |
| F-0010 Runtime/reference coverage | F-0010-D1 through F-0010-D3, F-0010-F1 through F-0010-F2, F-0010-E1 through F-0010-E2 |
| F-0010 Cross-part integration | F-0010-G1 through F-0010-G3 |

## Completion criteria for F-0010

F-0010 can be considered complete when:

- Part 5 Tables 1–5 have a final status:
  - visually reviewed and reconstructed,
  - intentionally deferred,
  - or intentionally omitted with reason;
- Figures 1, 3, 4, 5, 6, and 7 have a final status:
  - extracted,
  - redrawn,
  - intentionally deferred,
  - or intentionally omitted with reason;
- validator checks for F-0010-A/B/C are implemented or explicitly deferred;
- positive and negative test vectors for F-0010-A/B/C are listed in test-assets planning;
- SGAI, encrypted playback, and tracking sample coverage is either implemented or explicitly scoped;
- Part 12 conformance mapping is updated to reference concrete validator/test/client coverage;
- cross-part anchors and terminology are stable.