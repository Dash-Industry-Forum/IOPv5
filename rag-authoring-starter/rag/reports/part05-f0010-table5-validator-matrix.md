# F-0010-C validator matrix: Part 5 Table 5 IF-5 multi-Period ad insertion

Generated: 2026-07-21

Feature bucket:

```text
F-0010-C Validator checks for IF-5 multi-Period ad insertion / Table 5
```

Source anchor:

```text
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if5-media-presentation-requirements
```

Related conformance anchor:

```text
specs/part12-conformance-reference-tools/01-conformance.inc.md#tools-part5-ad-insertion-conformance
```

## Scope

This matrix classifies the DOCX-restructured Table 5 IF-5 MPD requirements for
content that combines main content, ad content, slate content, and return to
main content after ad insertion.

It replaces the earlier split between "main-content MPD rows" and "ad-content
rows" with the published Table 5 row groups extracted from
`DASH-IF-IOP-Part5-v5.0.0.docx`.

A rendered visual DOCX/PDF review is still recommended before final validator
implementation.

## Classification key

| Classification | Meaning |
|---|---|
| Error | Deterministic validator error when violated. |
| Warning | Deterministic validator warning when violated. |
| Informational | Validator reports feature presence/shape only. |
| Manual review | Requires human or scenario-specific interpretation. |
| Playback test | Best verified by dash.js/reference-player playback. |

## Table 5 validator matrix

| Context | Element / attribute | Current requirement summary | Classification | Proposed validator check | Test vector |
|---|---|---|---|---|---|
| `MPD` | `MPD` | Combined main/ad presentation; unspecified values follow ISO/IEC 23009-1. | Informational | Identify candidate IF-5 MPD from profiles, Period layout, and ad metadata. | None. |
| `MPD` | `ServiceDescription` | Service description information may be present. | Informational | Report presence. | Low-latency IF-5 MPD with ServiceDescription. |
| `ServiceDescription` | `Latency@target` | Target latency is provided when applicable. | Informational / Warning | Check parseable if present; warn if malformed. | Invalid latency value. |
| `MPD` | `@profiles` | Set to CMAF or CMAF-extended profile; proxy can switch to CMAF-extended if ads cannot be exactly conditioned. | Error / Warning | Check for `urn:mpeg:dash:profile:cmaf:2019` or `urn:mpeg:dash:profile:cmaf-extended:2019`; warn on profile transitions that conflict with content shape. | IF-5 MPD missing both profiles. |
| `MPD` | `@minimumUpdatePeriod` | Adjusted according to operation. | Informational / Manual review | Report value; for dynamic/live outputs, check parseable duration. | Invalid MUP value. |
| `MPD` | `InitializationSet` | If `@inAllPeriods=true`, proxy must either maintain compatibility, set false, or remove it. | Warning / Manual review | Report InitializationSet use; warn if `@inAllPeriods=true` and inserted ad/slate Periods lack compatible references where detectable. | InitializationSet inAllPeriods true with incompatible inserted ad Period. |
| `Period (Main content)` | `Period` | Main-content Period reused except specified differently. | Informational | Classify Periods before ad insertion point using metadata/timeline context. | Main/ad/main example. |
| `Period (Main content)` | `@duration` | Shall not be present; duration determined by next Ad Period `@start`. | Error | Check main-content Period immediately preceding inserted ad Period has no `@duration`. | Pre-ad main Period with `@duration`. |
| `Period (Main content)` | `EventStream` | Reused from main content. | Informational / Manual review | Report EventStreams; check syntax. | EventStream spanning opportunity. |
| `Period (Main content)` | `AdaptationSet` | Reused from main content. | Error | Check at least one AdaptationSet. | Main Period without AdaptationSet. |
| `Period (Main content)` | `AssetIdentifier` | Reused from main content. | Warning / Informational | Report presence; warn if policy requires main content identifiers. | Main Period without AssetIdentifier. |
| `Period (Ad Content)` | `Period` | Zero or more Ad Content Periods; reused except specified differently. | Informational / Error for malformed sequence | Identify inserted ad Periods from metadata, placement, or Period position. | IF-5 with inserted ad Period. |
| `Period (Ad Content)` | `@id` | Mandatory unique identifier, preferably reused where applicable. | Error | Check present and unique among Periods. | Inserted ad Period without `@id`; duplicate IDs. |
| `Period (Ad Content)` | `@start` | Mandatory; set to `tsplice-out`. | Error / Manual review | Check present and monotonic; if splice metadata is available, compare to `tsplice-out`. | Inserted ad Period missing or wrong `@start`. |
| `Period (Ad Content)` | `@duration` | Optional / typically removed. | Warning / Manual review | Report if present; warn if policy requires removal for the scenario. | Inserted ad Period retaining duration when removal expected. |
| `Period (Ad Content)` | `BaseURL` | One or more; reused from remote Ad Content Period unless moved. | Error | Check at least one BaseURL unless content is otherwise addressable by allowed mechanism. | Inserted ad Period without BaseURL. |
| `Period (Ad Content)` | `@availabilityTimeOffset` | Mandatory; set so client can download according to live schedule. | Error for live/dynamic IF-5; Warning otherwise | Check present where live/dynamic context applies and parseable. | Live inserted ad Period without ATO. |
| `Period (Ad Content)` | `EventStream` | Reused unless proxy removes based on business rules. | Informational / Manual review | Report ad EventStreams and schemes. | Ad Period with tracking events. |
| `Period (Ad Content)` | `AdaptationSet` | One or more; subset may be selected; compatible sets should reference InitializationSet. | Error / Warning | Check at least one AdaptationSet; warn when InitializationSet compatibility appears missing. | Ad Period without AdaptationSet. |
| `Period (Ad Content)` | `AssetIdentifier` | Reused from remote Ad Content Period. | Warning / Informational | Report presence; warn if ad identification policy requires it. | Ad Period without AssetIdentifier. |
| `Period (Slate Content)` | `Period` | Zero or more Slate Content Periods; reused except specified differently. | Informational / Error for malformed sequence | Identify slate Periods from metadata or position after ad underrun. | IF-5 with slate fill. |
| `Period (Slate Content)` | `@id` | Mandatory unique slate identifier. | Error | Check present and unique among Periods. | Slate Period without `@id`; duplicate IDs. |
| `Period (Slate Content)` | `@start` | Mandatory; typically `tsplice-out + previous ad duration`. | Error / Manual review | Check present and monotonic; compare to prior ad end if durations/metadata are available. | Slate Period with wrong start. |
| `Period (Slate Content)` | `@duration` | Optional / typically removed. | Warning / Manual review | Report if present; warn if policy requires removal. | Slate Period retaining duration when removal expected. |
| `Period (Slate Content)` | `BaseURL` | One or more; reused unless moved. | Error | Check at least one BaseURL unless content is otherwise addressable by allowed mechanism. | Slate Period without BaseURL. |
| `Period (Slate Content)` | `@availabilityTimeOffset` | Mandatory; set so client can download according to live schedule. | Error for live/dynamic IF-5; Warning otherwise | Check present where live/dynamic context applies and parseable. | Live slate Period without ATO. |
| `Period (Slate Content)` | `EventStream` | Reused unless proxy removes; slate is not expected to carry Events. | Informational / Warning | Report EventStreams; warn if slate Period carries unexpected events. | Slate Period with EventStream. |
| `Period (Slate Content)` | `AdaptationSet` | One or more; subset may be selected; compatible sets should reference InitializationSet. | Error / Warning | Check at least one AdaptationSet; warn when InitializationSet compatibility appears missing. | Slate Period without AdaptationSet. |
| `Period (Slate Content)` | `AssetIdentifier` | Reused from slate content Period. | Warning / Informational | Report presence; warn if slate identification policy requires it. | Slate Period without AssetIdentifier. |
| `Period (Main Content)` | `Period` | Return-to-main-content Period reused except specified differently. | Informational | Classify first main Period after ad/slate sequence. | Main/ad/main example. |
| `Period (Main Content)` | `@start` | Mandatory; set to `tsplice-in`. | Error / Manual review | Check present and monotonic; compare to `tsplice-in` if splice metadata is available. | Return Period missing or wrong `@start`. |
| `Period (Main Content)` | `@duration` | Shall not be present. | Error | Check absent. | Return Period with `@duration`. |
| `Period (Main Content)` | `EventStream` | Reused from main content. | Informational / Manual review | Report EventStreams; check syntax. | Return Period EventStream continuity case. |
| `Period (Main Content)` | `AdaptationSet` | Reused from main content. | Error | Check at least one AdaptationSet. | Return main Period without AdaptationSet. |
| `Period (Main Content)` | `AssetIdentifier` | Reused from main content. | Warning / Informational | Report presence; warn if main content identification policy requires it. | Return main Period without AssetIdentifier. |
| All Table 5 rows | xlink caveat | Conditions hold without `xlink:href`; if linking is used, attributes are optional and `minOccurs=0`. | Manual review / Informational | If xlink is present, switch deterministic checks into xlink-aware mode or defer. | IF-5 using linked Periods. |

## Table 4 reuse boundary

Table 5 is now treated as the final IF-5 spliced-output table, not as a duplicate
of source ad-content MPD Table 4.

Reuse the F-0010-B Table 4 validator module for:

- source DASH-IF ad content MPDs before insertion,
- source slate MPDs before insertion,
- remote ad/slate Period inputs when they are still complete ad-content MPDs.

Do not directly apply all Table 4 checks to final IF-5 inserted Periods because
Table 5 intentionally changes `Period@start`, commonly removes
`Period@duration`, and adds live availability requirements.

## IF-5 scenario checks

| Scenario | Classification | Proposed check | Test vector |
|---|---|---|---|
| Main/ad/main Period structure | Error / Playback test | Check Period starts are monotonic and ad Periods are inserted at opportunity time. | SSAI exact-duration match. |
| Ad overrun | Playback test / Manual review | Verify ad Periods after `tsplice-in` are removed/truncated and main Period resumes. | Ad content longer than opportunity. |
| Ad underrun | Playback test / Manual review | Verify additional ad or slate Period is inserted. | Ad content shorter than opportunity. |
| Ad pod ordering | Error / Manual review | Check inserted Period ordering follows declared decision response where metadata is available. | Multi-ad pod. |
| Period continuity | Warning / Playback test | Check continuity descriptors when compatible CMAF headers exist. | Continuous main-to-ad transition. |
| InitializationSet compatibility | Warning / Manual review | Check inserted ad/slate Periods are compatible with retained `InitializationSet@inAllPeriods=true`. | Incompatible ad Period with retained InitializationSet. |
| EventStream copying/splitting | Warning / Manual review | Check event syntax and presentation times after Period split/copy. | EventStream spanning ad opportunity. |
| Live availability timing | Error / Playback test | Check `@availabilityTimeOffset` on inserted ad/slate Periods in live IF-5 output. | Live inserted ad without ATO. |

## Positive test vectors

1. Live SSAI exact-duration ad insertion.
2. Live SSAI ad overrun with truncation.
3. Live SSAI ad underrun with slate.
4. Multi-ad pod with ordered inserted Periods.
5. Main/ad/main transition with Period continuity.
6. EventStream split/copied across ad insertion.
7. Retained compatible InitializationSet across main/ad/slate Periods.
8. Clear and encrypted variants for IF-9 playback follow-up.

## Negative test vectors

1. Inserted ad Period start not equal to opportunity `tsplice-out`.
2. Non-monotonic Period starts.
3. Pre-ad main Period retaining prohibited `@duration`.
4. Inserted ad Period missing `@id`.
5. Inserted ad Period missing `@start`.
6. Live inserted ad Period missing `@availabilityTimeOffset`.
7. Inserted ad Period without `BaseURL`.
8. Slate Period carrying unexpected EventStream.
9. Return main Period missing `@start`.
10. Return main Period retaining prohibited `@duration`.
11. InitializationSet retained with `@inAllPeriods=true` despite incompatible inserted Period.
12. EventStream copied without adjusted presentation timing.

## Open review questions

- Confirm rendered Table 5 row layout and hierarchy against DOCX/PDF.
- Confirm whether `Latency@target` Use value should remain represented as `0`
  or should be editorially normalized.
- Confirm whether `@minimumUpdatePeriod` should remain informational or become
  scenario-specific warning/error.
- Confirm exact handling of `Period@duration` removal for inserted ad and slate
  Periods.
- Confirm how much EventStream copying/splitting can be validator-automated.
- Confirm whether slate EventStreams should always warn or only warn when a
  policy flag is enabled.