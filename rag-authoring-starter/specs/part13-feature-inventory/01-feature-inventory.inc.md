# Introduction # {#introduction}

This part provides an editorial inventory of DASH interoperability features used across DASH-IF IOP v5.

The inventory is intended to connect feature definitions to:

- the relevant IOPv5 parts;
- DASH-IF-IOP extension specifications in [Dash-Industry-Forum/DASH-IF-IOP](https://github.com/Dash-Industry-Forum/DASH-IF-IOP);
- MPD, inband, and HTTP signalling;
- content offering requirements and recommendations;
- client requirements and recommendations;
- reference implementations and tools such as [dash.js](https://github.com/Dash-Industry-Forum/dash.js) and [livesim2](https://github.com/Dash-Industry-Forum/livesim2);
- executable examples.

This part is initially non-normative and editorial. It is expected to evolve as the feature taxonomy is reviewed by the DASH-IF community.

# Feature model # {#feature-model}

A feature is a named interoperability capability that can be described by one or more of:

- MPD signalling;
- inband signalling;
- HTTP signalling;
- content offering requirements and recommendations;
- client requirements and recommendations;
- reference-tool support;
- executable examples;
- conformance or validation coverage.

Features are not examples. Examples instantiate one or more features.

## Granularity ## {#feature-granularity}

The inventory distinguishes three levels.

<dl>
  <dt>Feature</dt>
  <dd>A recognizable interoperability capability, such as Low-Latency Live DASH, MPD Patching, CMCD, Content Steering, Content Protection, Multi-Period, Multi-Audio, Text Tracks, Events, LCEVC, or Variable Substitution.</dd>

  <dt>Sub-feature</dt>
  <dd>A feature component with independent signalling or client behavior, such as ServiceDescription latency signalling, ProducerReferenceTime, Resync, SegmentTimeline addressing, CMCD header mode, ClearKey, WebVTT, MPD EventStream, or inband <code>emsg</code>.</dd>

  <dt>Option</dt>
  <dd>A parameterization of a feature or sub-feature, such as a specific target latency, chunk duration, codec, language, role, or DASH-IF-IOP extension mode.</dd>
</dl>

# Feature sources # {#feature-sources}

## IOPv5 parts ## {#iopv5-parts}

Features may be defined, constrained, or referenced by the following IOPv5 parts:

| Part | Scope |
|---|---|
| [Part 2 — Core Principles and CMAF Mapping](https://dashif.org/Guidelines/iop-v5/part02-core-cmaf.html) | Core DASH timing, addressing, CMAF mapping, UTCTiming, and MPD structure. |
| [Part 3 — On-demand Services](https://dashif.org/Guidelines/iop-v5/part03-on-demand.html) | On-demand service features and content offering constraints. |
| [Part 4 — Live and Low-Latency Services](https://dashif.org/Guidelines/iop-v5/part04-live-low-latency.html) | Dynamic MPDs, live timing, low-latency live, availability timing, ServiceDescription, and related client behavior. |
| [Part 5 — Ad Insertion and Content Replacement](https://dashif.org/Guidelines/iop-v5/part05-ad-insertion.html) | Period-based ad insertion, SGAI, SSAI, ad signalling, and content replacement. |
| [Part 6 — Content Protection and Security](https://dashif.org/Guidelines/iop-v5/part06-content-protection.html) | ContentProtection signalling, CENC, key rotation, Enhanced Clear Key, and security guidance. |
| [Part 7 — Video](https://dashif.org/Guidelines/iop-v5/part07-video.html) | Video profiles, codec signalling, representation constraints, and DASH/CMAF video interoperability. |
| [Part 8 — Audio](https://dashif.org/Guidelines/iop-v5/part08-audio.html) | Audio profiles, multi-audio, language, role, accessibility, and channel signalling. |
| [Part 9 — Text](https://dashif.org/Guidelines/iop-v5/part09-text.html) | Subtitles, captions, WebVTT, IMSC/TTML, and related text-track signalling. |
| [Part 10 — Events](https://dashif.org/Guidelines/iop-v5/part10-events.html) | MPD events, inband events, timed metadata, and application event handling. |
| [Part 11 — Additional Functionalities](https://dashif.org/Guidelines/iop-v5/part11-additional-technologies.html) | Thumbnails, query/token mechanisms, metadata tracks, and additional feature areas. |
| [Part 12 — Conformance and Reference Tools](https://dashif.org/Guidelines/iop-v5/part12-conformance-reference-tools.html) | Validator, dash.js, livesim2, reference assets, and conformance interpretation. |

## DASH-IF-IOP extension specifications ## {#dash-if-iop-extensions}

Some features are currently defined as standalone DASH-IF-IOP extension specifications. Until those features are incorporated or profiled directly in IOPv5, this inventory references the corresponding folders in [Dash-Industry-Forum/DASH-IF-IOP](https://github.com/Dash-Industry-Forum/DASH-IF-IOP).

| DASH-IF-IOP folder | Feature inventory candidate |
|---|---|
| [`specs/cmcd`](https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/cmcd) | Common Media Client Data (CMCD). |
| [`specs/content-steering`](https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/content-steering) | Content Steering. |
| [`specs/l3d`](https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/l3d) | L3D-related distribution feature, pending closer mapping. |
| [`specs/lc-evc`](https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/lc-evc) | MPEG-5 Part 2 LCEVC carriage. |
| [`specs/live2vod`](https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/live2vod) | Live-to-VoD transition. |
| [`specs/mpd-patch`](https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/mpd-patch) | MPD Patching. |
| [`specs/varsub`](https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/varsub) | MPD Variable Substitution. |

## dash.js perspective ## {#dashjs-perspective}

The [dash.js sample catalog](https://reference.dashif.org/dash.js/latest/samples/) provides a client-oriented view of feature support. The inventory uses dash.js as a support lens for:

- client implementation status;
- relevant player settings and APIs;
- sample availability;
- player-observable behavior;
- features requiring a custom application rather than only the reference player.

Major dash.js sample areas include live playback, low latency, ABR, buffering, DRM, multi-period playback, subtitles and captions, multi-audio, thumbnails, audio-only playback, SCTE/emsg events, CMCD, MPD patching, MediaCapabilities filtering, MPD anchors, and LCEVC.

## livesim2 perspective ## {#livesim2-perspective}

The [livesim2](https://github.com/Dash-Industry-Forum/livesim2) live source simulator provides a content/offering-oriented view of feature support. The inventory uses livesim2 as a support lens for:

- generated MPDs;
- URL-parameter-controlled feature combinations;
- live and low-latency test streams;
- SegmentTemplate and SegmentTimeline modes;
- generated subtitles;
- UTC timing;
- CMAF chunking and ingest-related behavior.

# Initial feature inventory # {#initial-feature-inventory}

The machine-readable source for the seed inventory is maintained at:

[`rag/features/feature-inventory.yaml`](https://github.com/Dash-Industry-Forum/IOPv5/blob/tstockhammer-rag-workflow/rag-authoring-starter/rag/features/feature-inventory.yaml)

The current seed is intentionally incomplete. It is included here to establish the publication structure and to support review of feature granularity.

| Feature ID | Feature | Category | IOPv5 reference | DASH-IF-IOP reference | Current tool/example lens |
|---|---|---|---|---|---|
| `dynamic-mpd-live` | Dynamic MPD / Live DASH | Live | [Part 4](https://dashif.org/Guidelines/iop-v5/part04-live-low-latency.html) | — | dash.js Live samples; livesim2 dynamic live streams. |
| `segmenttemplate-number` | SegmentTemplate Number Addressing | Core | [Part 2](https://dashif.org/Guidelines/iop-v5/part02-core-cmaf.html) | — | livesim2 default addressing mode. |
| `segmenttimeline-time` | SegmentTimeline Time Addressing | Core | [Part 2](https://dashif.org/Guidelines/iop-v5/part02-core-cmaf.html) | — | livesim2 `segtimeline_1`; executable Part 4 example. |
| `utc-timing` | UTCTiming | Core | [Part 2](https://dashif.org/Guidelines/iop-v5/part02-core-cmaf.html), [Part 4](https://dashif.org/Guidelines/iop-v5/part04-live-low-latency.html) | — | livesim2 `utc_direct`; executable Part 4 example. |
| `availability-time-offset` | Availability Time Offset | Live | [Part 4](https://dashif.org/Guidelines/iop-v5/part04-live-low-latency.html) | — | dash.js Live sample; livesim2 `ato`; executable Part 4 examples. |
| `low-latency-live` | Low-Latency Live DASH | Low latency | [Part 4](https://dashif.org/Guidelines/iop-v5/part04-live-low-latency.html) | — | dash.js low-latency test player; livesim2 `chunkdur`, `ato`, `ltgt`. |
| `service-description-latency` | ServiceDescription Latency Signalling | Low latency | [Part 4](https://dashif.org/Guidelines/iop-v5/part04-live-low-latency.html) | — | dash.js ServiceDescription settings; livesim2 `ltgt`. |
| `cmaf-chunked-delivery` | CMAF Chunked Delivery | Low latency | [Part 4](https://dashif.org/Guidelines/iop-v5/part04-live-low-latency.html) | — | dash.js low-latency playback; livesim2 `chunkdur`. |
| `mpd-patching` | MPD Patching | Live | [Part 4](https://dashif.org/Guidelines/iop-v5/part04-live-low-latency.html) | [`specs/mpd-patch`](https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/mpd-patch) | dash.js MPD patching sample. |
| `cmcd` | Common Media Client Data | Reporting | [Part 12](https://dashif.org/Guidelines/iop-v5/part12-conformance-reference-tools.html) | [`specs/cmcd`](https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/cmcd) | dash.js CMCD samples; HTTP request observability. |
| `content-steering` | Content Steering | Delivery | [Part 12](https://dashif.org/Guidelines/iop-v5/part12-conformance-reference-tools.html) | [`specs/content-steering`](https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/content-steering) | dash.js Content Steering support. |
| `content-protection` | Content Protection | Protection | [Part 6](https://dashif.org/Guidelines/iop-v5/part06-content-protection.html) | — | dash.js DRM samples; browser/CDM dependent. |
| `text-tracks` | Text Tracks | Media | [Part 9](https://dashif.org/Guidelines/iop-v5/part09-text.html) | — | dash.js subtitle/caption samples; livesim2 generated time subtitles. |
| `multi-audio` | Multi-Audio | Media | [Part 8](https://dashif.org/Guidelines/iop-v5/part08-audio.html) | — | dash.js multi-audio samples; source asset dependent in livesim2. |
| `inband-emsg-events` | Inband `emsg` Events | Events | [Part 10](https://dashif.org/Guidelines/iop-v5/part10-events.html), [Part 5](https://dashif.org/Guidelines/iop-v5/part05-ad-insertion.html) | — | dash.js SCTE/emsg sample; usually requires app event handling. |
| `lcevc` | MPEG-5 Part 2 LCEVC Carriage | Video | [Part 7](https://dashif.org/Guidelines/iop-v5/part07-video.html) | [`specs/lc-evc`](https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/lc-evc) | dash.js LCEVC sample; requires LCEVC-capable pipeline. |

# Executable examples # {#executable-examples}

Executable examples are maintained separately from feature definitions and point back to the features they cover.

The current example registry is maintained at:

[`rag/examples/executable-examples.yaml`](https://github.com/Dash-Industry-Forum/IOPv5/blob/tstockhammer-rag-workflow/rag-authoring-starter/rag/examples/executable-examples.yaml)

The initial examples focus on Part 4 low-latency livesim2 streams.

| Example ID | Covered feature IDs |
|---|---|
| `part04-ll-basic` | `dynamic-mpd-live`, `low-latency-live`, `service-description-latency`, `cmaf-chunked-delivery`, `availability-time-offset` |
| `part04-ll-ultra` | `dynamic-mpd-live`, `low-latency-live`, `service-description-latency`, `cmaf-chunked-delivery`, `availability-time-offset` |
| `part04-ll-segtimeline` | `dynamic-mpd-live`, `low-latency-live`, `service-description-latency`, `cmaf-chunked-delivery`, `availability-time-offset`, `segmenttimeline-time` |
| `part04-ll-utc` | `dynamic-mpd-live`, `low-latency-live`, `service-description-latency`, `cmaf-chunked-delivery`, `availability-time-offset`, `utc-timing` |

# Maintenance workflow # {#maintenance-workflow}

The feature inventory is maintained editorially using the following workflow:

1. Add or update feature records in `rag/features/feature-inventory.yaml`.
2. Link executable examples to feature IDs using `covers_features`.
3. Use dash.js and livesim2 references as support lenses rather than as normative feature definitions.
4. Reference DASH-IF-IOP extension folders until the corresponding functionality is incorporated into IOPv5 text.
5. Periodically regenerate or update the published Part 13 summary from the machine-readable registry.

The dash.js sample catalog can be normalized using:

```bash
python tools/features/extract_dashjs_samples.py
```

The executable example registry can be URL-validated using:

```bash
python tools/validation/check_executable_examples.py rag/examples/executable-examples.yaml
```

# Open editorial issues # {#open-editorial-issues}

The following issues require review:

- Whether DASH-IF-IOP extensions should remain external references or become IOPv5 feature definitions.
- Whether feature granularity should be finer for codec, DRM, audio, and text options.
- Whether Part 13 should eventually become a generated document from `rag/features/feature-inventory.yaml`.
- Which features require conformance validator checks, executable examples, or custom test applications.