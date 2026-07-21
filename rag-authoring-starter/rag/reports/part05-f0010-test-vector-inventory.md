# F-0010 Part 5 validator test-vector inventory

Generated: 2026-07-21

This inventory tracks local Part 5 validator fixtures created during the F-0010
validator-start work. The fixtures are source-level examples for validator
development and are not yet DASH-IF published test assets.

## Validator tools

| Bucket | Validator | Scope |
|---|---|---|
| F-0010-A | `tools/validation/validate_part5_scte35_events.py` | IF-3 SCTE-35 MPD EventStream checks. |
| F-0010-B | `tools/validation/validate_part5_ad_content_mpd.py` | IF-4 DASH-IF ad-content MPD / Table 4 checks. |
| F-0010-C | `tools/validation/validate_part5_if5_spliced_mpd.py` | IF-5 final spliced-output MPD / Table 5 checks. |

## Current fixtures

| Bucket | Fixture | Expected result | Coverage |
|---|---|---|---|
| F-0010-A | `specs/part05-ad-insertion/examples/scte35/valid-scte35-eventstream.mpd` | Pass | `xml+bin` EventStream, valid Base64, parseable SCTE-35 command type. |
| F-0010-A | `specs/part05-ad-insertion/examples/scte35/invalid-scte35-eventstream.mpd` | Fail/warn | Unsupported scheme, missing presentation time, invalid duration, duplicate Event ID with conflicting payload, event outside Period, missing Binary. |
| F-0010-B | `specs/part05-ad-insertion/examples/table4/valid-ad-content.mpd` | Pass | Minimal valid DASH-IF ad-content MPD. |
| F-0010-B | `specs/part05-ad-insertion/examples/table4/invalid-ad-content.mpd` | Fail/warn | Aggregate negative fixture for profile, MPD type, forbidden MPD attributes, MPD BaseURL, Period timing/BaseURL, missing AssetIdentifier, xlink, PTO/eptDelta/pdDelta, missing Representation. |
| F-0010-C | `specs/part05-ad-insertion/examples/table5/valid-if5-spliced.mpd` | Pass | Minimal main/ad/main IF-5 spliced-output MPD. |
| F-0010-C | `specs/part05-ad-insertion/examples/table5/invalid-if5-spliced.mpd` | Fail/warn | Aggregate negative fixture for profiles, MUP syntax, missing Period starts, inserted ad/slate ID/BaseURL/ATO/AdaptationSet, retained durations, slate EventStream, missing return-main AdaptationSet. |
| F-0010-C | `specs/part05-ad-insertion/examples/table5/scenario-exact-duration.mpd` | Pass | SSAI exact-duration main/ad/main scenario baseline. |
| F-0010-C | `specs/part05-ad-insertion/examples/table5/scenario-underrun-slate.mpd` | Pass | SSAI underrun scenario with slate fill Period. |
| F-0010-B | `specs/part05-ad-insertion/examples/table4/per-rule/*.mpd` | Fail | Initial per-rule negative fixtures for selected deterministic Table 4 checks. |

## Planned fixture expansion

### F-0010-B2 per-rule Table 4 vectors

Add one negative fixture per deterministic Table 4 rule so CI failures can map
directly to the violated requirement. Initial per-rule fixtures now cover:

- missing CMAF profile,
- dynamic MPD,
- MPD-level BaseURL,
- Period start present,
- Period duration missing,
- SegmentList present,
- UTCTiming present.

Remaining per-rule fixtures to add:

- forbidden MPD timing attribute,
- multiple Periods,
- Period BaseURL missing,
- AdaptationSet xlink present,
- SegmentBase presentationTimeOffset present,
- SegmentBase eptDelta present,
- negative pdDelta,
- missing AdaptationSet contentType,
- SegmentList present,
- missing Representation,
- EmptyAdaptationSet present,
- UTCTiming present,
- LeapSecondInformation present.

### F-0010-C3 IF-5 SSAI scenario vectors

Add scenario-level fixtures and, where needed, playback assets:

- exact-duration main/ad/main insertion,
- ad overrun with truncation,
- ad underrun with slate insertion,
- multi-ad pod,
- Period continuity transition,
- EventStream copied/split across ad opportunity,
- clear/encrypted playback variants for IF-9 follow-up.

### F-0010-A2/A3 SCTE-35 payload vectors

Add payload-aware fixtures for:

- `time_signal()` with splice time,
- `time_signal()` plus `segmentation_descriptor()`,
- matched segmentation start/end pair,
- legacy `splice_insert()` with `out_of_network_indicator`,
- `splice_insert()` break duration,
- unsupported command type,
- malformed SCTE-35 table ID,
- descriptor mismatch.

## Part 12 cross-link

Part 12 now references the validator tools and fixture directories in:

```text
specs/part12-conformance-reference-tools/01-conformance.inc.md#tools-part5-ad-insertion-conformance
```

## Metanorma preparation

The following generated AsciiDoc smoke-test outputs are available:

```text
authoring/metanorma/generated/part05-ad-insertion.adoc
authoring/metanorma/generated/part12-conformance-reference-tools.adoc
```

They are generated from Bikeshed sources using:

```text
tools/metanorma/bikeshed_to_adoc.py
```

The converter is a proof-of-concept and the generated AsciiDoc should be treated
as derived output until a full Metanorma review is performed.