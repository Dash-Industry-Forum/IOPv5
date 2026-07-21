# F-0010-A validator matrix: Part 5 IF-3 SCTE-35 MPD Events

Generated: 2026-07-21

Feature bucket:

```text
F-0010-A Validator checks for IF-3 SCTE-35 MPD Events
```

Source anchors:

```text
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if3-ad-avail-signalling
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if3-scte35-opportunity-signalling
```

Related conformance anchor:

```text
specs/part12-conformance-reference-tools/01-conformance.inc.md#tools-part5-ad-insertion-conformance
```

## Scope

This matrix identifies validator checks and test vectors for opportunity
metadata carried as SCTE-35 DASH MPD Events in Part 5 IF-3.

## Classification key

| Classification | Meaning |
|---|---|
| Error | Deterministic validator error when violated. |
| Warning | Deterministic validator warning when suspicious or incomplete. |
| Informational | Validator reports feature presence/shape only. |
| Payload-dependent | Requires SCTE-35 payload parsing beyond MPD XML structure. |
| Manual review | Requires human or workflow-specific interpretation. |

## Validator matrix

| Topic | Current requirement / guidance | Classification | Proposed validator check | Test vector |
|---|---|---|---|---|
| MPD Event carriage | Opportunity metadata shall be carried through DASH MPD Events. | Error where Part 5 ad-insertion profile/feature is claimed | Check opportunity metadata appears in `EventStream` rather than only in-band when IF-3 feature is claimed. | MPD with inband-only SCTE-35 and no MPD Event. |
| `EventStream@schemeIdUri` | SCTE-35 MPD Events may use `urn:scte:scte35:2013:xml` or `urn:scte:scte35:2014:xml+bin`. | Error for unsupported SCTE-35 scheme when declared as IF-3 opportunity event | Check scheme URI against allowed SCTE-35 DASH event schemes. | EventStream using unknown SCTE-35 scheme. |
| Event syntax | DASH Event syntax must be valid. | Error | Reuse DASH EventStream/Event syntax checks. | Event missing required timing attributes where needed. |
| `@presentationTime` | Presentation time identifies splice point media time. | Error / Warning | Check present and parseable; compare with Period timing when possible. | Event without presentationTime; event outside Period bounds. |
| `@duration` | Duration represents expected or accurate opportunity duration. | Warning / Payload-dependent | Check parseable/non-negative if present; compare to SCTE-35 payload duration when parser available. | Negative duration; payload duration mismatch. |
| Event `@id` | Event id may be used to filter duplicate events. | Informational / Warning | Report duplicate IDs in same EventStream; warn if duplicate payloads appear ambiguous. | Duplicate events with same id and different payload. |
| `xml+bin` Binary payload | SCTE-35 payload is Base64 enclosed in `scte35:Binary`. | Error | For `urn:scte:scte35:2014:xml+bin`, require `scte35:Signal/scte35:Binary`; validate Base64. | Missing Binary; invalid Base64. |
| `time_signal()` | Common opportunity signal command. | Payload-dependent | If SCTE-35 parser available, identify command type. | Valid time_signal payload. |
| `segmentation_descriptor()` | Used with `time_signal()` to indicate opportunity boundaries. | Payload-dependent | If parser available, identify descriptor and segment type. | Payload without segmentation descriptor. |
| `splice_insert()` | Legacy command may be used. | Payload-dependent | If parser available, identify break duration and `out_of_network` semantics. | splice_insert start/end examples. |
| Opportunity start/end correlation | Segment start/end descriptors share `segmentation_event_id`. | Payload-dependent | Match start/end pairs if both events are available. | Start without end; mismatched IDs. |
| Expected vs accurate duration | Accurate duration calculated from matching segment pair. | Payload-dependent / Manual review | Compare Event duration with matched splice-time delta where payload parser and event pair exist. | Early termination; corrected duration. |
| Period boundary alignment | Opportunity may align with Period boundary or require later splitting. | Warning / Manual review | Report whether event presentation time aligns with Period start. | Non-boundary opportunity. |
| Presentation time offset | Large event presentation times may be adjusted by `@presentationTimeOffset`. | Warning | Check `EventStream@presentationTimeOffset` use where event times appear outside Period-local scale. | Event time requiring PTO but no PTO. |

## Positive test vectors

1. `urn:scte:scte35:2014:xml+bin` EventStream with valid Base64 Binary.
2. `time_signal()` plus `segmentation_descriptor()` opportunity start.
3. Matched segmentation start/end pair.
4. Legacy `splice_insert()` start and early termination.
5. Opportunity aligned with Period boundary.
6. Opportunity not aligned with Period boundary but sufficiently signalled.
7. EventStream with `@presentationTimeOffset`.

## Negative test vectors

1. Unsupported SCTE-35 scheme URI.
2. Missing `scte35:Binary` for `xml+bin`.
3. Invalid Base64 Binary payload.
4. Missing or unparsable `@presentationTime`.
5. Negative or unparsable `@duration`.
6. Duplicate Event `@id` with conflicting payloads.
7. Segment start/end descriptor mismatch.
8. Event time outside Period with no suitable offset.

## Implementation issues

### F-0010-A1: Implement MPD-level SCTE-35 EventStream checks

Acceptance criteria:

- Allowed SCTE-35 schemes are recognized.
- Invalid schemes fail when used as IF-3 opportunity events.
- `xml+bin` Binary presence and Base64 validity are checked.
- Event timing attributes are checked for parseability and basic Period bounds.

### F-0010-A2: Add SCTE-35 payload-aware checks

Acceptance criteria:

- Payload parser can identify `time_signal()`, `segmentation_descriptor()`, and
  `splice_insert()` where feasible.
- Start/end segmentation pairs can be correlated by event id.
- Expected vs accurate duration mismatches are classified as warning or error
  according to policy.

### F-0010-A3: Add IF-3 SCTE-35 test vectors

Acceptance criteria:

- Positive and negative vectors cover all MPD-level checks.
- Payload-dependent vectors are marked separately if parser support is not yet
  available.
- Vectors are cross-linked from Part 12 test-assets planning.