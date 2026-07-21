# F-0010 validator implementation issues: Table 4 and Table 5

Generated: 2026-07-21

This report converts the F-0010-B and F-0010-C validator matrices into
implementation-oriented issue scopes.

Related matrices:

```text
rag/reports/part05-f0010-table4-validator-matrix.md
rag/reports/part05-f0010-table5-validator-matrix.md
```

## Issue F-0010-B1: Implement DASH-IF ad content MPD structural validator checks

### Source

```text
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if4d-ad-content-storage
rag/reports/part05-f0010-table4-validator-matrix.md
```

### Scope

Implement deterministic MPD checks for DASH-IF ad content MPDs.

### Error checks

- `MPD@profiles` includes `urn:mpeg:dash:profile:cmaf:2019`.
- `MPD@type` is `static`.
- Forbidden MPD attributes are absent:
  - `@mediaPresentationDuration`
  - `@minimumUpdatePeriod`
  - `@timeShiftBufferDepth`
  - `@suggestedPresentationDelay`
  - `@maxSegmentDuration`
  - `@maxSubsegmentDuration`
- `MPD@minBufferTime` is present.
- MPD-level `BaseURL` is absent.
- Exactly one `Period` is present.
- `Period@xlink:href` and `Period@xlink:actuate` are absent.
- `Period@start` is absent.
- `Period@duration` is present and parseable.
- At least one Period-level `BaseURL` is present.
- At least one `AdaptationSet` is present.
- `AdaptationSet@contentType` is present.
- `SegmentList` is absent.
- At least one `Representation` exists in each `AdaptationSet`.
- `EmptyAdaptationSet` is absent.
- `UTCTiming` is absent.
- `LeapSecondInformation` is absent.

### Warning / informational checks

- Warn or report if DASH-IF ad-content profile is absent.
- Warn or report if `ProgramInformation` is absent.
- Warn if `AssetIdentifier` is absent.
- Report `EventStream` and `InbandEventStream` schemes.
- Report or warn on `SegmentBase@pdDelta` depending on threshold policy.

### Acceptance criteria

- Positive minimal ad-content MPD passes.
- Positive multi-variant ad-content MPD passes.
- Negative MPDs produce deterministic errors for every error check above.
- Warnings are configurable or documented.

## Issue F-0010-B2: Add DASH-IF ad content MPD test vectors

### Scope

Add positive and negative MPD vectors for Table 4 validator coverage.

### Positive vectors

- Minimal valid ad-content MPD.
- Valid ad-content MPD with DASH-IF ad-content profile.
- Valid ad-content MPD with `AssetIdentifier`.
- Valid slate-content MPD.
- Valid multi-variant ad-content MPD.

### Negative vectors

- Missing CMAF profile.
- Dynamic MPD.
- MPD-level `BaseURL`.
- Multiple Periods.
- Missing `Period@duration`.
- Period with `@start`.
- Missing Period-level `BaseURL`.
- AdaptationSet with `SegmentList`.
- Missing `AdaptationSet@contentType`.
- `SegmentBase@presentationTimeOffset` present.
- `SegmentBase@eptDelta` present.
- MPD with `UTCTiming`.
- MPD with `LeapSecondInformation`.

### Acceptance criteria

- Every F-0010-B1 error check has at least one negative vector.
- Positive vectors pass existing DASH/CMAF checks.
- Vectors are indexed in the Test Assets planning inventory.

## Issue F-0010-C1: Implement IF-5 multi-Period structural validator checks

### Source

```text
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if5-media-presentation-requirements
rag/reports/part05-f0010-table5-validator-matrix.md
```

### Scope

Implement validator checks for IF-5 final MPD outputs where mechanically
testable.

### Error checks

- One or more Periods are present.
- Main/content Periods have `Period@start`.
- Period starts are monotonic.
- `Period@xlink:href` and `Period@xlink:actuate` are absent.
- Each Period has at least one `AdaptationSet`.
- `AdaptationSet@contentType` is present.
- `SegmentList` is absent.
- Each `AdaptationSet` has at least one `Representation`.
- `EmptyAdaptationSet` is absent.
- Dynamic/live IF-5 MPDs have at least one `UTCTiming`.
- Inserted ad Period starts are consistent with opportunity timing when
  opportunity metadata is available.

### Warning / manual checks

- Warn when main Periods lack `AssetIdentifier`.
- Report `ServiceDescription` and `Latency@target`.
- Report `InitializationSet` and `@inAllPeriods`.
- Warn on suspicious Period continuity/connectivity descriptor gaps.
- Warn when split EventStreams appear to lack adjusted timing.
- Defer semantic validation of ad overrun/underrun handling to scenario tests.

### Acceptance criteria

- Basic live SSAI IF-5 MPD passes.
- Non-monotonic Period starts fail.
- Missing main Period `@start` fails.
- Missing live `UTCTiming` fails where live context applies.
- Warnings are emitted for non-fatal continuity/event issues.

## Issue F-0010-C2: Reuse Table 4 checks for source ad-content MPDs used by IF-5

### Scope

Integrate F-0010-B Table 4 checks into IF-5 validation where inserted ad content
is derived from DASH-IF ad-content MPDs.

### Acceptance criteria

- Shared code/module validates source ad MPDs for Table 4.
- IF-5 validation can cite inherited Table 4 failures.
- Duplicated Table 4/Table 5 checks are not implemented twice.

## Issue F-0010-C3: Add IF-5 SSAI scenario test vectors

### Positive vectors

- Exact-duration main/ad/main insertion.
- Ad overrun with truncation.
- Ad underrun with slate insertion.
- Multi-ad pod.
- Period continuity transition.
- EventStream copied/split across ad opportunity.
- Clear/encrypted playback variants for IF-9 follow-up.

### Negative vectors

- Inserted ad Period start not equal to `tsplice-out`.
- Non-monotonic Period starts.
- Source ad MPD with multiple Periods.
- Final live IF-5 MPD missing `UTCTiming`.
- Inserted Period retaining prohibited `@duration`.
- Main Period without `@start`.
- EventStream copied without adjusted timing.

### Acceptance criteria

- Each scenario is documented with expected validator result.
- Playback-dependent scenarios are marked for dash.js/reference-client testing.
- Assets are cross-linked to Part 12 test-assets planning.