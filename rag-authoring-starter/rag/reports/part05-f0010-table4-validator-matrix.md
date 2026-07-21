# F-0010-B validator matrix: Part 5 Table 4 DASH-IF ad content MPD

Generated: 2026-07-21

Feature bucket:

```text
F-0010-B Validator checks for DASH-IF ad content MPD / Table 4
```

Source anchor:

```text
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if4d-ad-content-storage
```

Related conformance anchor:

```text
specs/part12-conformance-reference-tools/01-conformance.inc.md#tools-part5-ad-insertion-conformance
```

## Scope

This matrix classifies the reconstructed Table 4 DASH-IF ad content MPD rows as
validator-error, validator-warning, informational, manual-review, or not
testable. It is based on the current Bikeshed reconstruction and still requires
visual DOCX/PDF review before implementation.

## Classification key

| Classification | Meaning |
|---|---|
| Error | A deterministic validator error should be emitted when violated. |
| Warning | A deterministic validator warning should be emitted when violated. |
| Informational | The validator can report the feature but should not fail/warn. |
| Manual review | Human review or deeper semantic interpretation is required. |
| Not testable | Not practical to test from MPD/segment inputs. |

## Table 4 validator matrix

| Context | Element / attribute | Current requirement summary | Classification | Proposed validator check | Negative test vector |
|---|---|---|---|---|---|
| `MPD` | `@profiles` | Should include DASH-IF ad-content profile and shall include DASH CMAF profile. | Error for missing CMAF profile; Warning for missing ad-content profile | Parse `MPD@profiles`; check for `urn:mpeg:dash:profile:cmaf:2019`; check optional `http://dashif.org/guidelines/dashif-ad-content`. | MPD missing CMAF profile; MPD missing ad-content profile. |
| `MPD` | `@type` | Shall be `static`. | Error | Check `MPD@type == "static"`. | MPD with `@type="dynamic"`. |
| `MPD` | `@mediaPresentationDuration` | Shall not be present. | Error | Check attribute absent. | Static ad MPD with `@mediaPresentationDuration`. |
| `MPD` | `@minimumUpdatePeriod` | Shall not be present. | Error | Check attribute absent. | Static ad MPD with `@minimumUpdatePeriod`. |
| `MPD` | `@minBufferTime` | Shall be present. | Error | Check attribute present. | MPD without `@minBufferTime`. |
| `MPD` | `@timeShiftBufferDepth` | Shall not be present. | Error | Check attribute absent. | Static ad MPD with `@timeShiftBufferDepth`. |
| `MPD` | `@suggestedPresentationDelay` | Shall not be present. | Error | Check attribute absent. | Static ad MPD with `@suggestedPresentationDelay`. |
| `MPD` | `@maxSegmentDuration` | Shall not be present. | Error | Check attribute absent. | Static ad MPD with `@maxSegmentDuration`. |
| `MPD` | `@maxSubsegmentDuration` | Shall not be present. | Error | Check attribute absent. | Static ad MPD with `@maxSubsegmentDuration`. |
| `MPD` | `ProgramInformation` | Should describe ad information. | Warning or Informational | Report presence; warn only if policy decides recommendation is testable. | MPD without `ProgramInformation`. |
| `MPD` | `BaseURL` | Shall not be present at MPD level. | Error | Check no MPD-level `BaseURL`. | MPD-level `BaseURL` present. |
| `MPD` | `Period` | Exactly one Period shall be present. | Error | Count `Period` elements equals 1. | MPD with zero or two Periods. |
| `Period` | `@xlink:href` | Shall be absent. | Error | Check attribute absent. | Period with `xlink:href`. |
| `Period` | `@xlink:actuate` | Shall be absent. | Error | Check attribute absent. | Period with `xlink:actuate`. |
| `Period` | `@start` | Shall be absent; assumed zero. | Error | Check attribute absent. | Period with `@start`. |
| `Period` | `@duration` | Shall be present and provide ad duration. | Error | Check attribute present and parseable as DASH duration. | Period without `@duration`; invalid duration. |
| `Period` | `BaseURL` | At least one shall be present. | Error | Check one or more Period-level `BaseURL`. | Period without `BaseURL`. |
| `Period` | `AssetIdentifier` | Should identify ad content. | Warning | Check zero or one `AssetIdentifier`; warn if absent; error if more than one if MPEG restriction applies. | Period without `AssetIdentifier`; Period with multiple identifiers. |
| `Period` | `EventStream` | Permitted for beaconing. | Informational | Report event streams and schemes. | None. |
| `Period` | `AdaptationSet` | At least one shall be present. | Error | Count one or more `AdaptationSet`. | Period without AdaptationSet. |
| `AdaptationSet` | `InbandEventStream` | Permitted for beaconing. | Informational | Report inband event streams and schemes. | None. |
| `AdaptationSet` | `SegmentBase@presentationTimeOffset` | Shall be absent. | Error | Check absent on segment addressing elements where applicable. | AdaptationSet with nonzero `presentationTimeOffset`. |
| `AdaptationSet` | `SegmentBase@eptDelta` | Shall be absent. | Error | Check absent where applicable. | AdaptationSet with `eptDelta`. |
| `AdaptationSet` | `SegmentBase@pdDelta` | May be present for non-video tracks; if present, non-negative and small. | Error for negative; Warning/manual for "small" | Check numeric non-negative; flag large values as warning if threshold is defined. | Negative `pdDelta`; very large `pdDelta`. |
| `AdaptationSet` | `@contentType` | Shall be present. | Error | Check `@contentType` present. | AdaptationSet without `@contentType`. |
| `AdaptationSet` | `SegmentList` | Shall be absent. | Error | Check no `SegmentList`. | AdaptationSet with SegmentList. |
| `AdaptationSet` | `Representation` | At least one shall be present. | Error | Count one or more Representation per AdaptationSet. | AdaptationSet without Representation. |
| `Period` | `EmptyAdaptationSet` | Shall be absent. | Error | Check no EmptyAdaptationSet. | Period with EmptyAdaptationSet. |
| `MPD` | `UTCTiming` | Shall not be present. | Error | Check absent. | MPD with UTCTiming. |
| `MPD` | `LeapSecondInformation` | Shall not be present. | Error | Check absent. | MPD with LeapSecondInformation. |

## Positive test vectors

Recommended positive MPD assets:

1. Minimal valid DASH-IF ad content MPD with one Period, one Period-level
   `BaseURL`, one AdaptationSet, one Representation, static type, CMAF profile,
   and `Period@duration`.
2. Valid ad content MPD with DASH-IF ad-content profile, AssetIdentifier,
   ProgramInformation, EventStream, and InbandEventStream.
3. Valid slate content MPD following Table 4 plus slate-specific recommendations.
4. Valid multi-variant ad MPD with multiple AdaptationSets/Representations and
   one Period.

## Negative test vectors

Recommended negative MPD assets:

1. Missing CMAF profile.
2. `MPD@type="dynamic"`.
3. MPD-level `BaseURL`.
4. Two Periods.
5. Missing `Period@duration`.
6. Period with `@start`.
7. Missing Period-level `BaseURL`.
8. AdaptationSet with `SegmentList`.
9. AdaptationSet missing `@contentType`.
10. AdaptationSet with `SegmentBase@presentationTimeOffset`.
11. AdaptationSet with `SegmentBase@eptDelta`.
12. MPD with `UTCTiming`.
13. MPD with `LeapSecondInformation`.

## Open review questions

- Confirm Table 4 row layout and hierarchy against DOCX/PDF.
- Confirm whether missing `ProgramInformation` should produce a warning or only
  informational output.
- Confirm whether missing `AssetIdentifier` should produce a warning.
- Confirm exact validator handling for `SegmentBase@pdDelta` "should be as small
  as possible".
- Confirm whether rows duplicated in Table 5 should share one validator module.