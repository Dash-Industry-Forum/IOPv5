# DASH Feature Inventory: First Analysis

This document proposes a first feature inventory model for DASH-IF IOP v5. It
uses three perspectives:

- **IOPv5 / DASH-IF-IOP specification view**: where a feature is defined and what
  requirements or recommendations apply.
- **dash.js client view**: whether a feature is implemented, configurable, or
  demonstrated by dash.js samples.
- **livesim2 content/offering view**: whether a feature can be generated or
  exercised through livesim2 URL parameters or assets.

The intent is to create an editorial inventory first, then publish selected
summaries into Part 1 and Part 12 once the taxonomy is stable.

## Feature definition

A feature is a named interoperability capability that can be described by one or
more of:

- MPD signalling.
- Inband signalling.
- HTTP signalling.
- Content offering requirements and recommendations.
- Client requirements and recommendations.
- Tool support.
- Executable examples.
- Conformance or reference-tool coverage.

Features are not examples. Examples instantiate one or more features.

## Granularity

The inventory uses three levels.

### Feature

A feature is a recognizable interoperability capability, for example:

- Low-Latency Live DASH.
- MPD Patching.
- CMCD.
- Content Steering.
- Content Protection.
- Multi-Period.
- Multi-Audio.
- Text Tracks.
- Events.
- LCEVC.
- Variable Substitution.

### Sub-feature

A sub-feature has independent signalling or client behavior, for example:

- ServiceDescription latency signalling.
- ProducerReferenceTime.
- Resync.
- SegmentTimeline addressing.
- CMCD header mode.
- CMCD query-argument mode.
- ClearKey.
- Widevine.
- PlayReady.
- MPD `EventStream`.
- inband `emsg`.
- WebVTT.
- IMSC/TTML.
- CEA-608/708.

### Option

An option is a parameterization of a feature or sub-feature, for example:

- `chunkdur_0.5` versus `chunkdur_0.2`.
- `ltgt_3500` versus `ltgt_2000`.
- AVC versus HEVC versus AV1 under video codec support.
- Specific languages or roles in audio/text tracks.

## dash.js perspective

The dash.js sample catalog is a useful client-oriented feature taxonomy. The
major current sample sections are:

| dash.js section | Feature areas |
|---|---|
| Getting Started | load modes, custom settings, control bar, events, log levels, URL parameters |
| Live | live delay, fragment-count delay, catch-up, availabilityTimeOffset, MPD patching |
| Live Low Latency | low-latency test player |
| ABR | ABR algorithms, custom rules, bitrate limits, fast switching, throughput modes |
| Buffer | buffer target, cleanup, initial buffer target |
| DRM | Widevine, PlayReady, FairPlay, ClearKey, license/certificate handling, key-system priority |
| Multi Period | VoD and live multi-period playback |
| Subtitles and Captions | WebVTT, CEA-608/708, multi-track captions, TTML/EBU-TT, subtitle events |
| Multi-Audio | multiple tracks, codec variants, initial track, language/accessibility |
| Thumbnails | thumbnail tracks |
| Audio only | audio-only playback |
| Advanced | monitoring, SCTE/emsg, autoplay policy, network interceptor, capability filters, MPD anchors |
| CMCD | CMCD v1, CMCD from manifest, CMCD v2 |
| MSS | Microsoft Smooth Streaming |
| MPEG-5 Part 2 - LCEVC | LCEVC carriage and debug residuals |

dash.js should be represented as a **client support lens**, not as the master
taxonomy. It helps answer:

- Is there a working client implementation?
- Is there a sample?
- Which API/settings are used?
- Is the feature player-observable?
- Does it require a custom application or only the reference player?

## livesim2 perspective

livesim2 is a content/offering and server-side exerciser. Current feature areas
include:

| livesim2 area | Feature areas |
|---|---|
| Live simulation | wall-clock synchronized dynamic MPDs from looped VoD assets |
| Addressing modes | SegmentTemplate `$Number$`, SegmentTimeline `$Time$`, SegmentTimeline `$Number$` |
| Timing | availability timing, UTC-aligned generation, time-shift behavior |
| Low latency | `chunkdur`, `ato`, `ltgt`, chunked low-latency operation |
| Subtitles | generated segmented TTML/STPP via `timesubsstpp`, WebVTT via `timesubswvtt` |
| Periods/timelines | multi-period generation, continuous timeline options, period duration |
| UTCTiming | UTC timing modes such as `utc_direct` |
| Asset handling | VoD asset ingestion, segment timing metadata |
| CMAF ingest | live CMAF segment pushing and ingest receiver testing |
| URL parameterization | feature combinations by path parameters and `/urlgen` |

livesim2 should be represented as a **content generation/support lens**. It helps
answer:

- Can a test MPD be generated?
- Which URL parameters create the feature?
- Is the MPD/player behavior observable?
- Does the feature depend on a specific source asset?

## DASH-IF-IOP extension perspective

The DASH-IF-IOP repository contains standalone extension/guideline specs that
map naturally into feature inventory entries:

| DASH-IF-IOP spec | Feature inventory candidate |
|---|---|
| `specs/cmcd` | CMCD |
| `specs/content-steering` | Content Steering |
| `specs/l3d` | L3D / low-latency or distribution-related extension, pending review |
| `specs/lc-evc` | MPEG-5 Part 2 LCEVC carriage |
| `specs/live2vod` | Live-to-VoD transition |
| `specs/mpd-patch` | MPD Patching |
| `specs/varsub` | MPD Variable Substitution |

These should be cross-referenced from IOPv5 features as external or extension
definitions.

## Proposed registry schema

The machine-readable inventory should be stored in:

```text
rag/features/feature-inventory.yaml
```

Each feature should follow this model:

```yaml
id: live-low-latency
title: Low-Latency Live DASH
status: draft
category: live
granularity: feature
parent:
children: []

defined_by:
  iopv5_parts:
    - part04-live-low-latency
  dash_if_iop:
    - mpd-patch
  external_specs:
    - ISO/IEC 23009-1
    - CMAF

signalling:
  mpd:
    elements: []
    attributes: []
    descriptors: []
  inband:
    boxes: []
    events: []
  http:
    headers: []
    query_parameters: []

content_offering:
  requirements: []
  recommendations: []

client:
  requirements: []
  recommendations: []

dashjs:
  support_status: supported
  samples: []
  settings: []
  apis: []
  caveats: []

livesim2:
  support_status: supported
  url_parameters: []
  examples: []
  caveats: []

examples:
  executable: []
  snippets: []

validation:
  mpd_observable: true
  player_observable: true
  requires_drm: false
  requires_custom_app: false

notes: []
```

## First seed feature set

The first inventory should seed a limited number of features so the model can be
reviewed before expanding.

Recommended initial seed:

1. SegmentTemplate Number addressing.
2. SegmentTimeline Time addressing.
3. Multi-Period.
4. UTCTiming.
5. Dynamic MPD / live.
6. availabilityTimeOffset.
7. MPD Patching.
8. Low-Latency Live.
9. ServiceDescription latency.
10. ProducerReferenceTime.
11. CMAF chunked delivery.
12. Resync.
13. CMCD.
14. Content Steering.
15. ABR switching.
16. Fast switching.
17. Content Protection.
18. ClearKey.
19. Widevine.
20. PlayReady.
21. Multi-audio.
22. Audio language/role selection.
23. WebVTT.
24. IMSC/TTML.
25. CEA-608/708.
26. Thumbnails.
27. MPD EventStream.
28. inband `emsg`.
29. SCTE/emsg events.
30. Period-based ad insertion.
31. LCEVC.
32. Live2VoD.
33. Variable substitution.
34. Audio-only.
35. Capability filtering / MediaCapabilities API.
36. MPD anchors.

## Relationship to executable examples

The existing executable examples registry should reference feature IDs. For
example:

```yaml
id: part04-ll-basic
covers_features:
  - dynamic-mpd-live
  - low-latency-live
  - service-description-latency
  - cmaf-chunked-delivery
  - availability-time-offset
```

This enables:

- feature-to-example lookup;
- example-to-feature lookup;
- gap analysis for features without examples;
- identification of dash.js-supported features without livesim2 examples;
- identification of IOPv5 features with no executable coverage.

## Recommended next steps

1. Create `rag/features/feature-inventory.yaml` with a small seed set.
2. Add `covers_features` to existing executable examples.
3. Add a dash.js sample extraction helper that converts `samples.json` into a
   normalized list for inventory mapping.
4. Add a validation script that checks:
   - feature IDs are unique;
   - parent/child references exist;
   - example `covers_features` references exist;
   - dash.js sample references are syntactically valid.
5. Generate `docs/feature-inventory.md` from the YAML once the schema stabilizes.
6. Later, link selected summary tables from Part 1 and Part 12.