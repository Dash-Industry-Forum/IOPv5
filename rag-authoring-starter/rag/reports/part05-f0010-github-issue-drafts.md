# F-0010 GitHub issue drafts: Part 5 ad-insertion conformance and cross-part indexing

Generated: 2026-07-21

These drafts convert `rag/reports/part05-f0010-implementation-plan.md` into
copy/paste-ready GitHub issue text.

Labels suggested for all issues:

```text
part-5
feature:F-0010
conformance
cross-part
```

## F-0010-A: Validator checks for IF-3 SCTE-35 MPD Events

### Title

```text
F-0010-A: Add validator/test coverage for Part 5 IF-3 SCTE-35 MPD Events
```

### Body

Part of F-0010: Part 5 ad-insertion conformance and cross-part indexing.

#### Scope

Add conformance/test coverage for Part 5 IF-3 opportunity metadata and SCTE-35
carriage in DASH MPD Events.

#### Source anchors

- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if3-ad-avail-signalling`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if3-scte35-opportunity-signalling`
- `specs/part12-conformance-reference-tools/01-conformance.inc.md#tools-part5-ad-insertion-conformance`

#### Proposed checks

- Validate SCTE-35 EventStream scheme identifiers:
  - `urn:scte:scte35:2013:xml`
  - `urn:scte:scte35:2014:xml+bin`
- Check Event `@presentationTime` presence and timing alignment.
- Check Event `@duration` use for expected and corrected opportunity duration.
- Detect duplicate Event `@id` where feasible.
- Check Base64 `Binary` payload presence for `xml+bin`.
- Classify payload checks for `time_signal()`, `segmentation_descriptor()`, and
  `splice_insert()` as automatable or manual.

#### Test assets

- `time_signal()` plus `segmentation_descriptor()`
- legacy `splice_insert()`
- expected-duration correction
- early termination
- duplicate-event filtering
- Period-boundary-aligned opportunity
- non-Period-boundary-aligned opportunity

#### Acceptance criteria

- [ ] Validator feasibility classification exists for each proposed check.
- [ ] At least one positive MPD test vector is identified.
- [ ] At least one negative MPD test vector is identified.
- [ ] Part 12 mapping references this bucket.

## F-0010-B: Validator checks for DASH-IF ad content MPD / Table 4

### Title

```text
F-0010-B: Add validator/test coverage for Part 5 DASH-IF ad content MPD Table 4
```

### Body

Part of F-0010: Part 5 ad-insertion conformance and cross-part indexing.

#### Scope

Add conformance/test coverage for the DASH-IF ad content storage format and
Table 4 MPD constraints.

#### Source anchors

- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if4d-ad-content-storage`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if4c-dynamic-ad-content-response`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if4f-slate-content`

#### Proposed checks

- `MPD@profiles` includes DASH CMAF profile identifier.
- `MPD@profiles` may include `http://dashif.org/guidelines/dashif-ad-content`.
- `MPD@type="static"`.
- Exactly one `Period`.
- `Period@duration` present.
- `Period@start` absent.
- Forbidden dynamic MPD attributes absent.
- MPD-level `BaseURL` absent.
- Period-level `BaseURL` present.
- `SegmentBase@presentationTimeOffset` absent.
- `SegmentBase@eptDelta` absent.
- `SegmentList` absent.
- `UTCTiming` absent.
- `LeapSecondInformation` absent.
- `AssetIdentifier` syntax documented for Ad-ID and DASH-IF asset-id examples.

#### Test assets

- valid DASH-IF ad content MPD
- valid slate content MPD
- multiple codec/resolution variants
- Ad-ID identifier example
- DASH-IF asset-id identifier example
- invalid MPD-level `BaseURL`
- invalid two-Period ad content MPD
- invalid dynamic MPD attributes

#### Acceptance criteria

- [ ] Each Table 4 row is classified as error, warning, informational, or not testable.
- [ ] Negative cases produce deterministic validator outcomes.
- [ ] Slate-content recommendations are represented as warnings or informational tests.

## F-0010-C: Validator checks for IF-5 multi-Period ad insertion / Table 5

### Title

```text
F-0010-C: Add validator/test coverage for Part 5 IF-5 multi-Period ad insertion Table 5
```

### Body

Part of F-0010: Part 5 ad-insertion conformance and cross-part indexing.

#### Scope

Add conformance/test coverage for IF-5 MPD and segment structure after ad
placement insertion.

#### Source anchors

- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if5-mpd-segments`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if5-media-presentation-requirements`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if5-mpd-proxy-guidelines`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if5-client-playback-guidelines`

#### Proposed checks

- Multi-Period main/ad/main structure.
- `Period@start` monotonicity.
- Inserted ad Period ordering.
- Inserted `Period@duration` handling.
- `UTCTiming` expectations in main vs ad-content contexts.
- Period continuity/connectivity descriptor syntax.
- EventStream timing after Period splitting/copying.
- Table 5 main-content and ad-content MPD constraints.

#### Test assets

- exact ad-duration match
- ad overrun with truncation
- ad underrun with slate insertion
- multiple ads in an ad pod
- overlapping segment boundary
- copied EventStream during ad opportunity
- Period continuity case
- Period connectivity case
- no continuity/connectivity fallback case

#### Acceptance criteria

- [ ] Checks are split into MPD-only and segment/content checks.
- [ ] dash.js playback assets are listed for each transition type.
- [ ] Each Table 5 row has status: implemented, needs validator support, manual review, or not testable.

## F-0010-D: SGAI remote-resolution coverage with dash.js and livesim2

### Title

```text
F-0010-D: Add SGAI remote-resolution coverage with dash.js and livesim2
```

### Body

Part of F-0010: Part 5 ad-insertion conformance and cross-part indexing.

#### Scope

Create reference coverage for IF-7 late binding, URL parameters, and remote
resolution.

#### Source anchors

- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if7-remote-resolution`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if7a-decisioning-url-parameters`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if7b-conditioning-url-parameters`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if7c-remote-periods`

#### Tasks

- Document livesim2 SGAI generation mode relevant to Part 5.
- Add or identify dash.js samples for Alternative-MPD Replace / Remote Period resolution.
- Define URL parameters for decisioning and content conditioning.
- Exercise re-decisioning after seek/rewind where supported.

#### Test assets

- SGAI late-binding live stream
- remote Period replacement example
- URL decisioning parameter example
- URL content-conditioning parameter example
- failed remote-resolution negative case
- seek/rewind re-decisioning scenario

#### Acceptance criteria

- [ ] At least one livesim2-generated scenario is documented.
- [ ] At least one dash.js playback sample is identified or proposed.
- [ ] Remote-resolution syntax is aligned with current DASH edition and Part 10/11 language.

## F-0010-E: VAST/Open Measurement tracking sample coverage

### Title

```text
F-0010-E: Add VAST/Open Measurement tracking sample coverage for Part 5 IF-8
```

### Body

Part of F-0010: Part 5 ad-insertion conformance and cross-part indexing.

#### Scope

Create sample/test coverage for IF-8 ad tracking and measurement.

#### Source anchors

- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if8-tracking-measurement`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if8-vast-view-tracking`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if8-open-measurement`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if8-alternative-tracking`

#### Coverage

- VAST impression/start/quartile/complete events.
- Pause/resume/mute/unmute/skip events.
- Mapping tracking events to inserted ad Periods.
- Tracking after Period splitting/truncation.
- Tracking with slate insertion.
- Open Measurement metadata association.

#### Acceptance criteria

- [ ] Part 5 normative vs integration-specific tracking scope is clear.
- [ ] Sample applications identify when callbacks fire.
- [ ] Test assets include expected callback timeline.

## F-0010-F: Clear/encrypted ad insertion playback assets

### Title

```text
F-0010-F: Add clear/encrypted ad insertion playback assets for IF-9
```

### Body

Part of F-0010: Part 5 ad-insertion conformance and cross-part indexing.

#### Scope

Validate IF-9 playback and decryption across main/ad transitions.

#### Source anchors

- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if9-reference-playback-decryption`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if5-client-playback-guidelines`

#### Coverage

- clear main + clear ads
- encrypted main + clear ads
- clear main + encrypted ads
- encrypted main + encrypted ads
- key change at Period boundary
- common key across main/ad Periods
- CMAF header switch at boundary
- continuity/connectivity with encrypted content

#### Acceptance criteria

- [ ] Part 6 alignment points are identified.
- [ ] dash.js playback expectations are documented.
- [ ] At least one clear and one encrypted transition case are identified.

## F-0010-G: Cross-part anchor and terminology harmonization

### Title

```text
F-0010-G: Harmonize Part 5 cross-part anchors and terminology
```

### Body

Part of F-0010: Part 5 ad-insertion conformance and cross-part indexing.

#### Scope

Create stable links between Part 5 and related Part 1/2/6/10/12 anchors once
cross-document linking policy is stable.

#### Tasks

- Decide link style for cross-part anchors.
- Convert plain-text references to stable links.
- Normalize repeated terms:
  - DASH access client
  - reference playback platform
  - Period continuity
  - Period connectivity
  - CMAF header
  - EventStream
  - Remote Period / remote entity
- Check bibliography aliases and decide what moves to shared bibliography.

#### Acceptance criteria

- [ ] Link checker passes.
- [ ] No duplicate conflicting definitions are introduced.
- [ ] Cross-part index identifies all unresolved anchors.

## F-0010-H: Published Part 5 table/figure hardening

### Title

```text
F-0010-H: Harden Part 5 tables and figures against published DOCX/PDF
```

### Body

Part of F-0010: Part 5 ad-insertion conformance and cross-part indexing.

#### Scope

Complete visual/table hardening against the published DOCX/PDF before validator
work depends on the migrated source.

#### Source anchors

- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-use-cases-scenarios`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-architectures`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-interfaces-overview`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if2-content-preparation`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if3-ad-avail-signalling`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if4d-ad-content-storage`
- `specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if5-media-presentation-requirements`

#### Tasks

- Visual review of published architecture figures.
- Extract or redraw architecture figures.
- Reconstruct/review Table 1.
- Reconstruct/review Table 2.
- Reconstruct/review Table 3.
- Review Table 4 hierarchy and modal strength.
- Review Table 5 hierarchy and modal strength.
- Decide whether Table 4 and Table 5 should share a canonical source.

#### Acceptance criteria

- [ ] Each published table has explicit status: reconstructed and reviewed, reconstructed needs review, not found in extract, or intentionally omitted.
- [ ] Each figure has explicit status: extracted, redrawn, deferred, or omitted with reason.
- [ ] Reconciliation report reflects final table/figure status.