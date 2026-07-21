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

This matrix classifies the reconstructed Table 5 IF-5 MPD requirements for
main-content and ad-content Periods after ad insertion. It is based on the
current Bikeshed reconstruction and still requires visual DOCX/PDF review before
validator implementation.

## Classification key

| Classification | Meaning |
|---|---|
| Error | Deterministic validator error when violated. |
| Warning | Deterministic validator warning when violated. |
| Informational | Validator reports feature presence/shape only. |
| Manual review | Requires human or scenario-specific interpretation. |
| Playback test | Best verified by dash.js/reference-player playback. |

## Main-content MPD rows

| Context | Element / attribute | Current requirement summary | Classification | Proposed validator check | Test vector |
|---|---|---|---|---|---|
| `MPD` | `@profiles` | Should include DASH CMAF profile. | Warning / Error if profile claim required | Parse profiles and check `urn:mpeg:dash:profile:cmaf:2019`. | MPD missing CMAF profile. |
| `MPD` | `ServiceDescription` | May be present. | Informational | Report presence and latency fields. | Low-latency ad insertion MPD. |
| `ServiceDescription` | `Latency@target` | Target latency may be provided. | Informational | Check parseable if present. | Invalid latency value. |
| `MPD` | `InitializationSet` | May be present; `@inAllPeriods` may express continuity. | Informational / Warning | Report InitializationSet usage; warn if claimed continuity conflicts with Period structure where detectable. | MPD with inconsistent initialization references. |
| `MPD` | `ProgramInformation` | Should describe main content. | Warning or Informational | Report presence; warn if policy decides recommendation is testable. | Main MPD without ProgramInformation. |
| `MPD` | `Period` | One or more Periods shall be present. | Error | Count Periods >= 1. | MPD without Period. |
| `Period` | `@xlink:href` | Shall be absent. | Error | Check absent. | Main Period with xlink href. |
| `Period` | `@xlink:actuate` | Shall be absent. | Error | Check absent. | Main Period with xlink actuate. |
| `Period` | `@start` | Shall be present. | Error | Check present and monotonic. | Period missing `@start`; non-monotonic starts. |
| `Period` | `AssetIdentifier` | Should identify main content. | Warning | Check zero or one; warn if absent. | Main Period without AssetIdentifier. |
| `Period` | `EventStream` | Events may terminate in proxy or continue across insertion. | Informational / Manual review | Report schemes and timing; check syntax. | EventStream split across ad opportunity. |
| `EventStream` | `@presentationTimeOffset` | Needed for multi-period split events. | Warning / Manual review | Warn when split events cross Period boundaries without suitable offset. | Split EventStream without offset. |
| `Period` | `AdaptationSet` | At least one shall be present. | Error | Count AdaptationSet >= 1. | Period without AdaptationSet. |
| `AdaptationSet` | `@xlink:href` | Shall be absent. | Error | Check absent. | AdaptationSet with xlink href. |
| `AdaptationSet` | `@xlink:actuate` | Shall be absent. | Error | Check absent. | AdaptationSet with xlink actuate. |
| `AdaptationSet` | `SegmentBase@presentationTimeOffset` | Shall be set correctly if presentation time is not zero. | Manual review / Error if mechanically inconsistent | Check parseability; compare with Period start and segment timing where available. | Incorrect PTO at Period boundary. |
| `AdaptationSet` | `@contentType` | Shall be present. | Error | Check present. | AdaptationSet missing contentType. |
| `AdaptationSet` | `SegmentList` | Shall be absent. | Error | Check no SegmentList. | AdaptationSet with SegmentList. |
| `AdaptationSet` | `Representation` | At least one shall be present. | Error | Count Representation >= 1. | AdaptationSet without Representation. |
| `Period` | `EmptyAdaptationSet` | Shall be absent. | Error | Check absent. | Period with EmptyAdaptationSet. |
| `MPD` | `UTCTiming` | At least one shall be present. | Error for dynamic/live IF-5 where applicable | Count UTCTiming >= 1 when live/dynamic context applies. | Live IF-5 MPD without UTCTiming. |

## Ad-content rows in IF-5

Ad-content rows in Table 5 largely overlap with Table 4. Implementations should
reuse the F-0010-B Table 4 validator module where possible.

| Context | Element / attribute | Current requirement summary | Classification | Proposed validator check | Test vector |
|---|---|---|---|---|---|
| `MPD` | `@profiles` | Should include DASH-IF ad-content profile and shall include CMAF profile. | Error / Warning | Reuse Table 4 profile checks. | Inserted ad content without CMAF profile. |
| `MPD` | `@type` | Shall be static. | Error | Reuse Table 4 check. | Dynamic ad-content MPD. |
| `MPD` | dynamic-only attributes | `@mediaPresentationDuration`, `@minimumUpdatePeriod`, `@timeShiftBufferDepth`, `@suggestedPresentationDelay`, `@maxSegmentDuration`, `@maxSubsegmentDuration` shall not be present. | Error | Reuse Table 4 forbidden-attribute checks. | Ad MPD with dynamic attributes. |
| `MPD` | `BaseURL` | Shall not be present at MPD level. | Error | Reuse Table 4 check. | MPD-level BaseURL in ad MPD. |
| `MPD` | `Period` | Exactly one Period shall be present in ad-content MPD before insertion. | Error | Reuse Table 4 check for source ad MPD; for final IF-5, check inserted Period sequence separately. | Ad MPD with multiple Periods. |
| `Period` | `@start` | Shall be absent in ad-content MPD; inserted IF-5 Period start is assigned by proxy. | Error / Scenario check | Source ad MPD: absent. Final IF-5: inserted Period starts equal `tsplice-out` and cumulative durations. | Source ad MPD with `@start`; final IF-5 with wrong inserted start. |
| `Period` | `@duration` | Shall be present in source ad MPD; removed from inserted Periods by proxy flow. | Error / Scenario check | Source ad MPD: present. Final IF-5 inserted Periods: removed where required. | Source ad MPD missing duration; inserted Period retains duration when prohibited. |
| `Period` | `BaseURL` | At least one shall be present. | Error | Reuse Table 4 check. | Ad Period without BaseURL. |
| `Period` | `AssetIdentifier` | Should identify ad content. | Warning | Reuse Table 4 check. | Ad Period without AssetIdentifier. |
| `Period` | `EventStream` | Permitted for beaconing. | Informational | Report event streams and callback schemes. | Ad Period with tracking events. |
| `Period` | `AdaptationSet` | At least one shall be present. | Error | Reuse Table 4 check. | Ad Period without AdaptationSet. |
| `AdaptationSet` | `InbandEventStream` | Permitted for beaconing. | Informational | Report inband event streams. | Inband ad beacon example. |
| `AdaptationSet` | `SegmentBase@presentationTimeOffset` | Shall be absent in DASH-IF ad content. | Error | Reuse Table 4 check. | Ad content with PTO. |
| `AdaptationSet` | `SegmentBase@eptDelta` | Shall be absent. | Error | Reuse Table 4 check. | Ad content with eptDelta. |
| `AdaptationSet` | `SegmentBase@pdDelta` | May be present for non-video; non-negative and small. | Error / Warning | Reuse Table 4 pdDelta checks. | Negative pdDelta. |
| `AdaptationSet` | `@contentType` | Shall be present. | Error | Reuse Table 4 check. | Missing contentType. |
| `AdaptationSet` | `SegmentList` | Shall be absent. | Error | Reuse Table 4 check. | SegmentList present. |
| `AdaptationSet` | `Representation` | At least one shall be present. | Error | Reuse Table 4 check. | AdaptationSet without Representation. |
| `Period` | `EmptyAdaptationSet` | Shall be absent. | Error | Reuse Table 4 check. | EmptyAdaptationSet present. |
| `MPD` | `UTCTiming` / `LeapSecondInformation` | Shall not be present in source ad-content MPD. | Error | Reuse Table 4 check. | Source ad MPD with UTCTiming. |

## IF-5 scenario checks

| Scenario | Classification | Proposed check | Test vector |
|---|---|---|---|
| Main/ad/main Period structure | Error / Playback test | Check Period starts are monotonic and ad Periods are inserted at opportunity time. | SSAI exact-duration match. |
| Ad overrun | Playback test / Manual review | Verify ad Periods after `tsplice-in` are removed/truncated and main Period resumes. | Ad content longer than opportunity. |
| Ad underrun | Playback test / Manual review | Verify additional ad or slate Period is inserted. | Ad content shorter than opportunity. |
| Ad pod ordering | Error / Manual review | Check inserted Period ordering follows declared decision response where metadata is available. | Multi-ad pod. |
| Period continuity | Warning / Playback test | Check continuity descriptors when compatible CMAF headers exist. | Continuous main-to-ad transition. |
| EventStream copying/splitting | Warning / Manual review | Check event syntax and presentation times after Period split/copy. | EventStream spanning ad opportunity. |
| UTCTiming in live IF-5 | Error | Check at least one UTCTiming in dynamic/live output. | Live SSAI MPD without UTCTiming. |

## Positive test vectors

1. Live SSAI exact-duration ad insertion.
2. Live SSAI ad overrun with truncation.
3. Live SSAI ad underrun with slate.
4. Multi-ad pod with ordered inserted Periods.
5. Main/ad/main transition with Period continuity.
6. EventStream split/copied across ad insertion.
7. Clear and encrypted variants for IF-9 playback follow-up.

## Negative test vectors

1. Inserted ad Period start not equal to opportunity `tsplice-out`.
2. Non-monotonic Period starts.
3. Source ad MPD with multiple Periods.
4. Final IF-5 live MPD missing UTCTiming.
5. Inserted Period retaining prohibited `@duration`.
6. Main Period without required `@start`.
7. AdaptationSet missing `@contentType`.
8. SegmentList used in ad content.
9. EventStream copied without adjusted presentation timing.

## Open review questions

- Confirm Table 5 row layout and hierarchy against DOCX/PDF.
- Confirm whether the source should remain split into main-content and
  ad-content tables or be merged into a published-style single table.
- Confirm which Table 5 rows are final-output IF-5 checks versus source-ad-MPD
  checks inherited from Table 4.
- Confirm exact handling of `Period@duration` removal for inserted Periods.
- Confirm how much EventStream copying/splitting can be validator-automated.