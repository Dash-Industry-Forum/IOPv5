# F-0010 implementation plan: Part 5 ad-insertion conformance and cross-part indexing

Generated: 2026-07-21

Feature registry entry:

```text
F-0010 Part 5 ad-insertion conformance and cross-part indexing
```

Target parts:

```text
Part 1, Part 2, Part 5, Part 6, Part 10, Part 12
```

Primary sources:

- Part 5 source:
  `specs/part05-ad-insertion/05-ad-insertion.inc.md`
- Part 12 conformance mapping:
  `specs/part12-conformance-reference-tools/01-conformance.inc.md#tools-part5-ad-insertion-conformance`
- Cross-reference index:
  `rag/reports/part05-cross-reference-index.md`
- Feature registry:
  `docs/governance/feature-registry.md`

## Goal

Turn the Part 5 migration into actionable conformance, reference-client, live
simulation, and test-asset work items.

This plan is issue-ready: each bucket can become one GitHub issue or a small
linked set of GitHub issues.

## Issue bucket overview

| Bucket | Title | Primary parts | Primary tools | Priority |
|---|---|---|---|---|
| F-0010-A | Validator checks for IF-3 SCTE-35 MPD Events | 5, 10, 12 | DASH-IF Conformance Validator, Test Assets | High |
| F-0010-B | Validator checks for DASH-IF ad content MPD / Table 4 | 2, 5, 12 | DASH-IF Conformance Validator, Test Assets | High |
| F-0010-C | Validator checks for IF-5 multi-Period ad insertion / Table 5 | 2, 5, 12 | DASH-IF Conformance Validator, dash.js, Test Assets | High |
| F-0010-D | SGAI remote-resolution coverage with dash.js and livesim2 | 5, 10, 12 | dash.js, livesim2, Test Assets | High |
| F-0010-E | VAST/Open Measurement tracking sample coverage | 5, 12 | dash.js samples, Test Assets | Medium |
| F-0010-F | Clear/encrypted ad insertion playback assets | 5, 6, 12 | dash.js, DASH-IF Conformance Validator, Test Assets | Medium |
| F-0010-G | Cross-part anchor and terminology harmonization | 1, 2, 5, 6, 10, 12 | Bikeshed/link validation | Medium |
| F-0010-H | Published Part 5 table/figure hardening | 5 | Editorial review, publication tooling | High |

## F-0010-A: Validator checks for IF-3 SCTE-35 MPD Events

### Scope

Validate opportunity metadata and SCTE-35 carriage in DASH MPD Events.

### Part 5 anchors

- `#ad-if3-ad-avail-signalling`
- `#ad-if3-scte35-opportunity-signalling`

### Cross-part dependencies

- Part 10 event timing and event signalling model.
- SCTE 214-1 / SCTE 214-3 bibliography references.
- Part 12 conformance mapping.

### Proposed validator checks

- `EventStream@schemeIdUri` values:
  - `urn:scte:scte35:2013:xml`
  - `urn:scte:scte35:2014:xml+bin`
- Event `@presentationTime` presence and timeline alignment.
- Event `@duration` semantics for expected and corrected opportunity duration.
- Duplicate-event `@id` detection where feasible.
- Base64 `Binary` payload presence for `xml+bin`.
- Structural sanity checks for `time_signal()`, `segmentation_descriptor()`, and `splice_insert()` when payload inspection is available.

### Test assets

Create assets for:

- `time_signal()` plus `segmentation_descriptor()`,
- legacy `splice_insert()`,
- expected-duration correction,
- early termination,
- duplicate-event filtering,
- Period-boundary-aligned opportunity,
- opportunity not aligned with existing Period boundary.

### Acceptance criteria

- Part 12 mapping links to this issue bucket.
- At least one positive and one negative MPD test vector are defined.
- Validator check feasibility is classified as:
  - fully automatable,
  - MPD-only automatable,
  - payload-inspection dependent,
  - manual review only.

## F-0010-B: Validator checks for DASH-IF ad content MPD / Table 4

### Scope

Validate DASH-IF ad content storage format and Table 4 MPD constraints.

### Part 5 anchors

- `#ad-if4d-ad-content-storage`
- `#ad-if4c-dynamic-ad-content-response`
- `#ad-if4f-slate-content`

### Cross-part dependencies

- Part 2 CMAF profile and segment model.
- Part 12 validator and test-asset mapping.

### Proposed validator checks

- `MPD@profiles` contains DASH CMAF profile identifier.
- `MPD@profiles` optionally contains `http://dashif.org/guidelines/dashif-ad-content`.
- `MPD@type="static"`.
- Exactly one `Period`.
- `Period@duration` present.
- `Period@start` absent.
- Forbidden MPD attributes absent:
  - `@mediaPresentationDuration`,
  - `@minimumUpdatePeriod`,
  - `@timeShiftBufferDepth`,
  - `@suggestedPresentationDelay`,
  - `@maxSegmentDuration`,
  - `@maxSubsegmentDuration`.
- MPD-level `BaseURL` absent.
- Period-level `BaseURL` present.
- `SegmentBase@presentationTimeOffset` absent.
- `SegmentBase@eptDelta` absent.
- `SegmentList` absent.
- `UTCTiming` absent.
- `LeapSecondInformation` absent.
- `AssetIdentifier` syntax documented for Ad-ID and DASH-IF asset-id examples.

### Test assets

Create assets for:

- valid DASH-IF ad content MPD,
- valid slate content MPD,
- multiple codec/resolution variants,
- Ad-ID identifier,
- DASH-IF asset-id identifier,
- negative case with MPD-level `BaseURL`,
- negative case with two Periods,
- negative case with forbidden dynamic MPD attributes.

### Acceptance criteria

- Table 4 constraints are tagged as validator-error, validator-warning, or informational.
- Negative cases produce deterministic validator outcomes.
- Slate-content recommendations are represented as warnings or informational tests.

## F-0010-C: Validator checks for IF-5 multi-Period ad insertion / Table 5

### Scope

Validate MPD and segment structure after ad placement insertion.

### Part 5 anchors

- `#ad-if5-mpd-segments`
- `#ad-if5-media-presentation-requirements`
- `#ad-if5-mpd-proxy-guidelines`
- `#ad-if5-client-playback-guidelines`

### Cross-part dependencies

- Part 2 Period continuity/connectivity.
- Part 2 CMAF header and profile language.
- Part 12 validator, dash.js, and test assets.

### Proposed validator checks

- Multi-Period structure for main/ad/main transitions.
- `Period@start` monotonicity.
- Inserted ad Period ordering.
- Removal of inserted `Period@duration` where required by Part 5 migration text.
- Presence/absence of `UTCTiming` according to main vs ad-content contexts.
- Period continuity/connectivity descriptor syntax.
- `EventStream` timing after Period splitting/copying.
- Table 5 main-content and ad-content MPD constraints.

### Test assets

Create SSAI assets for:

- exact ad-duration match,
- ad overrun with truncation,
- ad underrun with slate insertion,
- multiple ads in an ad pod,
- overlapping segment boundary,
- copied EventStream during ad opportunity,
- Period continuity case,
- Period connectivity case,
- no continuity/connectivity fallback case.

### Acceptance criteria

- Validator requirements are split into MPD-only checks and segment/content checks.
- dash.js playback assets are listed for each transition type.
- Each Table 5 row has a status:
  - implemented,
  - needs validator support,
  - manual review,
  - not testable.

## F-0010-D: SGAI remote-resolution coverage with dash.js and livesim2

### Scope

Create reference coverage for IF-7 late binding, URL parameters, and remote
resolution.

### Part 5 anchors

- `#ad-if7-remote-resolution`
- `#ad-if7a-decisioning-url-parameters`
- `#ad-if7b-conditioning-url-parameters`
- `#ad-if7c-remote-periods`

### Cross-part dependencies

- Part 10 event model.
- Part 11 remote entity work if used.
- Part 12 livesim2 and dash.js sections.

### Proposed tool work

- Document livesim2 SGAI generation mode relevant to Part 5.
- Add or identify dash.js samples for Alternative-MPD Replace / Remote Period resolution.
- Define URL parameters for:
  - decisioning,
  - content conditioning,
  - device capability,
  - codec/encryption constraints.
- Exercise re-decisioning after seek/rewind where supported.

### Test assets

Create or identify:

- SGAI late-binding live stream,
- remote Period replacement example,
- URL decisioning parameter example,
- URL content-conditioning parameter example,
- negative case for failed remote resolution,
- seek/rewind re-decisioning scenario.

### Acceptance criteria

- At least one livesim2-generated scenario is documented.
- At least one dash.js playback sample is identified or proposed.
- Remote-resolution syntax is aligned with the current DASH edition and Part 10/11 language.

## F-0010-E: VAST/Open Measurement tracking sample coverage

### Scope

Create test and sample coverage for IF-8 ad tracking and measurement.

### Part 5 anchors

- `#ad-if8-tracking-measurement`
- `#ad-if8-vast-view-tracking`
- `#ad-if8-open-measurement`
- `#ad-if8-alternative-tracking`

### Cross-part dependencies

- IAB VAST.
- Open Measurement SDK.
- Part 12 test assets and reference client/application samples.

### Proposed sample coverage

- VAST events:
  - impression,
  - start,
  - first quartile,
  - midpoint,
  - third quartile,
  - complete,
  - pause,
  - resume,
  - mute,
  - unmute,
  - skip.
- Mapping of tracking events to inserted ad Periods.
- Tracking after Period splitting/truncation.
- Tracking with slate insertion.
- Open Measurement integration metadata association.

### Test assets

Create or identify:

- VAST ad pod with one ad,
- VAST ad pod with multiple ads,
- truncated ad with adjusted tracking,
- slate-filled break,
- Open Measurement metadata example.

### Acceptance criteria

- Part 5 specifies what is normative vs integration-specific.
- Sample applications identify when tracking callbacks fire.
- Test assets include expected callback timeline.

## F-0010-F: Clear/encrypted ad insertion playback assets

### Scope

Validate IF-9 playback and decryption across main/ad transitions.

### Part 5 anchors

- `#ad-if9-reference-playback-decryption`
- `#ad-if5-client-playback-guidelines`

### Cross-part dependencies

- Part 6 content protection.
- Part 12 dash.js, MSE, EME, and test assets.
- Part 2 Period continuity/connectivity.

### Proposed coverage

- Clear main content + clear ads.
- Encrypted main content + clear ads.
- Clear main content + encrypted ads.
- Encrypted main content + encrypted ads.
- Key change at Period boundary.
- Common key across main/ad Periods.
- CMAF header switch at boundary.
- Continuity/connectivity with encrypted content.

### Acceptance criteria

- Part 6 alignment points are identified.
- dash.js playback expectations are documented.
- Test assets include at least one clear and one encrypted transition case.

## F-0010-G: Cross-part anchor and terminology harmonization

### Scope

Create stable links between Part 5 and related Part 1/2/6/10/12 anchors once
cross-document linking policy is stable.

### Part 5 anchors

All Part 5 anchors listed in `part05-cross-reference-index.md`.

### Cross-part dependencies

- Part 1 architecture/interface terminology.
- Part 2 CMAF and Period model.
- Part 6 content protection.
- Part 10 events.
- Part 12 conformance tooling.

### Tasks

- Decide link style for cross-part anchors.
- Convert plain-text references to stable links.
- Normalize repeated terms:
  - DASH access client,
  - reference playback platform,
  - Period continuity,
  - Period connectivity,
  - CMAF header,
  - EventStream,
  - Remote Period / remote entity.
- Check bibliography aliases and decide what moves to shared bibliography.

### Acceptance criteria

- Link checker passes.
- No duplicate conflicting definitions are introduced.
- Cross-part index identifies all unresolved anchors.

## F-0010-H: Published Part 5 table/figure hardening

### Scope

Complete visual/table hardening against the published DOCX/PDF.

### Part 5 anchors

- `#ad-use-cases-scenarios`
- `#ad-architectures`
- `#ad-interfaces-overview`
- `#ad-if2-content-preparation`
- `#ad-if3-ad-avail-signalling`
- `#ad-if4d-ad-content-storage`
- `#ad-if5-media-presentation-requirements`

### Tasks

- Visual review of published architecture figures.
- Extract or redraw architecture figures.
- Reconstruct/review Table 1.
- Reconstruct/review Table 2.
- Reconstruct/review Table 3.
- Review Table 4 hierarchy and modal strength.
- Review Table 5 hierarchy and modal strength.
- Decide whether Table 4 and Table 5 should share a canonical source.

### Acceptance criteria

- Each published table has an explicit status:
  - reconstructed and reviewed,
  - reconstructed, needs review,
  - not found in extract,
  - intentionally omitted.
- Each figure has an explicit status:
  - extracted,
  - redrawn,
  - deferred,
  - omitted with reason.
- Reconciliation report reflects final status.

## Recommended implementation sequence

1. F-0010-H: harden tables/figures and modal wording.
2. F-0010-B: implement/check Table 4 ad-content constraints.
3. F-0010-C: implement/check Table 5 multi-Period insertion constraints.
4. F-0010-A: implement/check SCTE-35 MPD Event constraints.
5. F-0010-D: create SGAI livesim2/dash.js examples.
6. F-0010-F: add clear/encrypted transition test assets.
7. F-0010-E: add tracking/measurement samples.
8. F-0010-G: finalize cross-part links and terminology harmonization.

## Immediate next action

Start with F-0010-H because it stabilizes the normative source before
validator/test work depends on it.