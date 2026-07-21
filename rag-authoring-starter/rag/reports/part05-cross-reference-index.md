# Part 5 ad-insertion cross-reference index

Generated: 2026-07-21

This report starts cross-part indexing for DASH-IF IOP v5 Part 5, *Ad Insertion
in DASH*. It tracks the relationships between Part 5 ad-insertion requirements,
shared concepts in other parts, and Part 12 conformance/test tooling.

## Feature tracking

Governance feature:

```text
F-0010 Part 5 ad-insertion conformance and cross-part indexing
```

Tracked in:

```text
docs/governance/feature-registry.md
```

Target parts:

```text
Part 1, Part 2, Part 5, Part 6, Part 10, Part 12
```

## Source anchors

Primary Part 5 source:

```text
specs/part05-ad-insertion/05-ad-insertion.inc.md
```

Primary Part 12 conformance mapping:

```text
specs/part12-conformance-reference-tools/01-conformance.inc.md#tools-part5-ad-insertion-conformance
```

## Cross-part index

| Part 5 anchor | Topic | Cross-part dependency | Conformance / test target |
|---|---|---|---|
| `#ad-use-cases-scenarios` | Use cases: VoD, live, recorded live, pre-roll, obfuscation, transitions | Part 1 architecture vocabulary; Part 2 CMAF/multi-period model | Test-assets scenario taxonomy for SSAI/SGAI and transition cases |
| `#ad-architectures` | SSAI and SGAI architecture baseline | Part 1 architectures and interface model | Feature F-0010 issue set and architecture-figure review |
| `#ad-interfaces-overview` | IF-0 through IF-9 interface overview | Part 1 interface terminology; Part 12 tooling model | Table 1 review and cross-reference link checks |
| `#ad-if0-abr-stream-source` | ABR stream source and cue metadata | SCTE-35/SCTE-104 references; Part 1 source/packaging model | Test inputs with live and VoD cue metadata |
| `#ad-if1-packager-ingest` | Packager ingest | DASH-IF Ingest; Part 2 CMAF mapping | Ingest-oriented test streams and opportunity metadata preservation checks |
| `#ad-if2-content-preparation` | Content preparation before insertion | Part 2 Period, AdaptationSet, Representation, CMAF header, continuity/connectivity model | Main-content MPDs conditioned for ad insertion and Period splitting |
| `#ad-if3-ad-avail-signalling` | SCTE-35 opportunity metadata in MPD Events | Part 10 event timing/signalling; SCTE 214 references | Validator checks EventStream syntax/timing; assets for `time_signal()`, `segmentation_descriptor()`, `splice_insert()`, early termination |
| `#ad-if4-decisioning-exchange` | Ad decisioning, conditioning, VAST/SCTE-130, ad-content storage | IAB VAST, SCTE-130, Part 2 CMAF, Part 12 test assets | Validator checks DASH-IF ad-content MPD constraints; VAST/SCTE-130 mapping review |
| `#ad-if5-mpd-segments` | MPD and segments with ad placements | Part 2 multi-period, Period continuity/connectivity, CMAF profile | Validator checks multi-Period ad insertion; assets for match/overrun/underrun/slate |
| `#ad-if6-ad-metadata` | DASH Callback Events and ad metadata | Part 10 event/callback guidance | Event-dispatch samples and callback timing tests |
| `#ad-if7-remote-resolution` | URL parameters and Remote Period late binding | Part 10/11 remote entity model; livesim2 SGAI support | livesim2/dash.js SGAI examples; URL decisioning/conditioning parameter tests |
| `#ad-if8-tracking-measurement` | VAST tracking, Open Measurement, alternatives | IAB VAST, Open Measurement SDK, Part 12 test assets | Tracking-event callback samples for impression/start/quartiles/complete |
| `#ad-if9-reference-playback-decryption` | Reference playback and decryption | Part 6 content protection; Part 12 dash.js/MSE/EME | Clear and encrypted multi-Period ad insertion playback assets |

## F-0010 issue buckets

The following concrete issue buckets are defined in
`rag/reports/part05-f0010-implementation-plan.md` and should be used when
creating GitHub issues or downstream implementation tasks.

| Bucket | Title | Related Part 5 anchors | Primary cross-part dependencies |
|---|---|---|---|
| F-0010-A | Validator checks for IF-3 SCTE-35 MPD Events | `#ad-if3-ad-avail-signalling`, `#ad-if3-scte35-opportunity-signalling` | Part 10 event timing, Part 12 validator/test assets |
| F-0010-B | Validator checks for DASH-IF ad content MPD / Table 4 | `#ad-if4d-ad-content-storage`, `#ad-if4c-dynamic-ad-content-response`, `#ad-if4f-slate-content` | Part 2 CMAF profile/segment model, Part 12 validator/test assets |
| F-0010-C | Validator checks for IF-5 multi-Period ad insertion / Table 5 | `#ad-if5-mpd-segments`, `#ad-if5-media-presentation-requirements`, `#ad-if5-mpd-proxy-guidelines`, `#ad-if5-client-playback-guidelines` | Part 2 Period continuity/connectivity, Part 12 validator/dash.js/test assets |
| F-0010-D | SGAI remote-resolution coverage with dash.js and livesim2 | `#ad-if7-remote-resolution`, `#ad-if7a-decisioning-url-parameters`, `#ad-if7b-conditioning-url-parameters`, `#ad-if7c-remote-periods` | Part 10 events, Part 11 remote entity work, Part 12 livesim2/dash.js |
| F-0010-E | VAST/Open Measurement tracking sample coverage | `#ad-if8-tracking-measurement`, `#ad-if8-vast-view-tracking`, `#ad-if8-open-measurement`, `#ad-if8-alternative-tracking` | IAB VAST, Open Measurement SDK, Part 12 samples/test assets |
| F-0010-F | Clear/encrypted ad insertion playback assets | `#ad-if9-reference-playback-decryption`, `#ad-if5-client-playback-guidelines` | Part 6 content protection, Part 2 continuity/connectivity, Part 12 dash.js/MSE/EME |
| F-0010-G | Cross-part anchor and terminology harmonization | All Part 5 anchors | Parts 1/2/6/10/12 cross-document linking and terminology |
| F-0010-H | Published Part 5 table/figure hardening | `#ad-use-cases-scenarios`, `#ad-architectures`, `#ad-interfaces-overview`, `#ad-if2-content-preparation`, `#ad-if3-ad-avail-signalling`, `#ad-if4d-ad-content-storage`, `#ad-if5-media-presentation-requirements` | Published DOCX/PDF, publication tooling, Part 5 source stabilization |

Recommended sequence:

1. F-0010-H
2. F-0010-B
3. F-0010-C
4. F-0010-A
5. F-0010-D
6. F-0010-F
7. F-0010-E
8. F-0010-G

## Initial Part 12 mapping

Part 12 now contains an initial Part 5 conformance mapping for:

- IF-3 opportunity metadata and SCTE-35 MPD Events,
- IF-4 DASH-IF ad content storage and Table 4 requirements,
- IF-5 MPD and segments with ad placements,
- IF-6 ad metadata and DASH Callback Events,
- IF-7 remote resolution and URL parameter decisioning,
- IF-8 ad tracking and measurement,
- IF-9 reference playback and decryption.

## Remaining Part 5 completion work

The Part 5 source now has initial coverage for all major published sections, but
the remaining completion work is editorial/conformance hardening:

1. Visually compare migrated prose against the published DOCX/PDF.
2. Extract or redraw architecture figures.
3. Review and reconstruct any remaining Table 2 and Table 3 material.
4. Review Table 4 and Table 5 hierarchy and modal strength.
5. Decide whether Table 4 and Table 5 share a canonical table or remain
   duplicated.
6. Align IF-2 and IF-5 continuity/connectivity language with Part 2.
7. Align IF-6 and IF-7 event/remote-resolution language with Part 10 and any
   remote-entity work in Part 11.
8. Align IF-9 playback/decryption constraints with Part 6 and Part 12.
9. Convert the Part 12 mapping into concrete validator, dash.js, livesim2, and
   Test Assets issues using F-0010-A through F-0010-H.
