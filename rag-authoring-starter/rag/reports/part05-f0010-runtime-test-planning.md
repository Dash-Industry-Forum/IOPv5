# F-0010 runtime/test planning: SGAI, encrypted playback, and tracking

Generated: 2026-07-21

This report starts planning for the runtime/reference-client and test-asset
buckets after the Table 4 / Table 5 / SCTE-35 validator matrices.

Covered buckets:

```text
F-0010-D SGAI remote-resolution coverage with dash.js and livesim2
F-0010-F Clear/encrypted ad insertion playback assets
F-0010-E VAST/Open Measurement tracking sample coverage
```

## F-0010-D: SGAI remote-resolution coverage with dash.js and livesim2

### Source anchors

```text
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if7-remote-resolution
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if7a-decisioning-url-parameters
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if7b-conditioning-url-parameters
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if7c-remote-periods
specs/part12-conformance-reference-tools/01-conformance.inc.md#tools-livesim2
```

### Goal

Create reference coverage for Server-Guided Ad Insertion where ad opportunity
resolution is deferred until playback time.

### Test scenarios

| Scenario | Tool target | Expected outcome |
|---|---|---|
| SGAI live stream with remote opportunity | livesim2 + dash.js | Client resolves remote entity/Period and continues playback. |
| URL decisioning parameters | dash.js sample / app harness | Request includes content/opportunity/device parameters. |
| URL conditioning parameters | dash.js sample / app harness | Request includes codec, format, encryption, and capability parameters. |
| Remote resolution failure | dash.js | Client handles resolution failure according to policy. |
| Seek/rewind re-decisioning | dash.js / livesim2 if supported | Client can re-resolve opportunity after seeking or rewinding. |
| Low-latency SGAI | livesim2 | MPD updates and remote resolution remain compatible with live latency constraints. |

### Implementation issues

#### F-0010-D1: Document livesim2 SGAI scenario mapping

Acceptance criteria:

- livesim2 SGAI mode is mapped to Part 5 IF-7 concepts.
- Example URLs are identified.
- Limitations are documented.

#### F-0010-D2: Add or identify dash.js SGAI sample coverage

Acceptance criteria:

- At least one dash.js sample exercises remote resolution.
- Decisioning and conditioning URL parameters are visible in sample/application code.
- Failure behaviour is documented.

#### F-0010-D3: Add SGAI test-asset entries

Acceptance criteria:

- Test assets include positive and negative remote-resolution cases.
- Assets are linked to Part 12 conformance/test-assets planning.

## F-0010-F: Clear/encrypted ad insertion playback assets

### Source anchors

```text
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if9-reference-playback-decryption
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if5-client-playback-guidelines
specs/part06-content-protection/06-content-protection.inc.md
specs/part12-conformance-reference-tools/01-conformance.inc.md#tools-dashjs
```

### Goal

Validate playback and decryption across main/ad Period transitions using
dash.js, MSE, EME, and Part 6 content-protection alignment.

### Test scenarios

| Scenario | Expected coverage |
|---|---|
| clear main + clear ad | Baseline Period transition and continuity. |
| encrypted main + clear ad | Key-system state does not block clear ad playback. |
| clear main + encrypted ad | License/key acquisition during ad transition. |
| encrypted main + encrypted ad, same key | Continuity with common key. |
| encrypted main + encrypted ad, key change | Key transition at Period boundary. |
| CMAF header switch at ad boundary | MSE init segment handling. |
| Period continuity with encrypted content | Continuity descriptors and key availability. |
| Period connectivity with encrypted content | Timing adjustment and decryption continuity. |

### Implementation issues

#### F-0010-F1: Define Part 6 alignment points for IF-9

Acceptance criteria:

- Content-protection signalling requirements are cross-referenced.
- Key-change and common-key scenarios are listed.
- Clear/encrypted combinations are assigned test status.

#### F-0010-F2: Add dash.js playback test assets

Acceptance criteria:

- At least one clear scenario and one encrypted scenario are playable.
- Expected playback outcome is documented.
- Failures can be distinguished between MPD authoring, DRM setup, and player behaviour.

## F-0010-E: VAST/Open Measurement tracking sample coverage

### Source anchors

```text
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if8-tracking-measurement
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if8-vast-view-tracking
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if8-open-measurement
specs/part05-ad-insertion/05-ad-insertion.inc.md#ad-if8-alternative-tracking
```

### Goal

Create reference sample coverage for tracking events associated with inserted ad
Periods and ad metadata.

### Test scenarios

| Scenario | Expected coverage |
|---|---|
| VAST single ad | impression, start, quartiles, complete. |
| VAST ad pod | tracking per ad creative and pod order. |
| Truncated ad | tracking timeline adjusted to actual playback. |
| Slate-filled break | no ad-completion event for slate unless explicitly signalled. |
| Pause/resume/mute/unmute/skip | user-interaction event callbacks. |
| Open Measurement metadata association | measurement session associated with inserted Period/ad creative. |

### Implementation issues

#### F-0010-E1: Define VAST tracking callback timeline assets

Acceptance criteria:

- Expected callback timestamps are listed.
- Callback events are mapped to inserted Periods.
- Truncated and slate-filled cases are documented.

#### F-0010-E2: Define Open Measurement integration sample

Acceptance criteria:

- Metadata association model is documented.
- Scope boundary between DASH-IF IOP and application integration is explicit.
- Sample references IF-4/IF-6/IF-8 metadata relationships.

## Recommended execution order

1. F-0010-D1 / D2: identify actual livesim2 and dash.js SGAI capabilities.
2. F-0010-F1: define Part 6 alignment for clear/encrypted transitions.
3. F-0010-F2: identify or create playback assets.
4. F-0010-E1: define VAST callback timeline assets.
5. F-0010-E2: define Open Measurement sample scope.