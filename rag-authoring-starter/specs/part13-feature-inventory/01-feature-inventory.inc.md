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

<table class="data">
  <thead>
    <tr>
      <th>Part</th>
      <th>Scope</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part02-core-cmaf.html">Part 2 — Core Principles and CMAF Mapping</a></td>
      <td>Core DASH timing, addressing, CMAF mapping, UTCTiming, and MPD structure.</td>
    </tr>
    <tr>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part03-on-demand.html">Part 3 — On-demand Services</a></td>
      <td>On-demand service features and content offering constraints.</td>
    </tr>
    <tr>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part04-live-low-latency.html">Part 4 — Live and Low-Latency Services</a></td>
      <td>Dynamic MPDs, live timing, low-latency live, availability timing, ServiceDescription, and related client behavior.</td>
    </tr>
    <tr>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part05-ad-insertion.html">Part 5 — Ad Insertion and Content Replacement</a></td>
      <td>Period-based ad insertion, SGAI, SSAI, ad signalling, and content replacement.</td>
    </tr>
    <tr>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part06-content-protection.html">Part 6 — Content Protection and Security</a></td>
      <td>ContentProtection signalling, CENC, key rotation, Enhanced Clear Key, and security guidance.</td>
    </tr>
    <tr>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part07-video.html">Part 7 — Video</a></td>
      <td>Video profiles, codec signalling, representation constraints, and DASH/CMAF video interoperability.</td>
    </tr>
    <tr>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part08-audio.html">Part 8 — Audio</a></td>
      <td>Audio profiles, multi-audio, language, role, accessibility, and channel signalling.</td>
    </tr>
    <tr>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part09-text.html">Part 9 — Text</a></td>
      <td>Subtitles, captions, WebVTT, IMSC/TTML, and related text-track signalling.</td>
    </tr>
    <tr>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part10-events.html">Part 10 — Events</a></td>
      <td>MPD events, inband events, timed metadata, and application event handling.</td>
    </tr>
    <tr>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part11-additional-technologies.html">Part 11 — Additional Functionalities</a></td>
      <td>Thumbnails, query/token mechanisms, metadata tracks, and additional feature areas.</td>
    </tr>
    <tr>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part12-conformance-reference-tools.html">Part 12 — Conformance and Reference Tools</a></td>
      <td>Validator, dash.js, livesim2, reference assets, and conformance interpretation.</td>
    </tr>
  </tbody>
</table>

## DASH-IF-IOP extension specifications ## {#dash-if-iop-extensions}

Some features are currently defined as standalone DASH-IF-IOP extension specifications. Until those features are incorporated or profiled directly in IOPv5, this inventory references the corresponding folders in [Dash-Industry-Forum/DASH-IF-IOP](https://github.com/Dash-Industry-Forum/DASH-IF-IOP).

<table class="data">
  <thead>
    <tr>
      <th>DASH-IF-IOP folder</th>
      <th>Feature inventory candidate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/cmcd"><code>specs/cmcd</code></a></td>
      <td>Common Media Client Data (CMCD).</td>
    </tr>
    <tr>
      <td><a href="https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/content-steering"><code>specs/content-steering</code></a></td>
      <td>Content Steering.</td>
    </tr>
    <tr>
      <td><a href="https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/l3d"><code>specs/l3d</code></a></td>
      <td>L3D-related distribution feature, pending closer mapping.</td>
    </tr>
    <tr>
      <td><a href="https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/lc-evc"><code>specs/lc-evc</code></a></td>
      <td>MPEG-5 Part 2 LCEVC carriage.</td>
    </tr>
    <tr>
      <td><a href="https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/live2vod"><code>specs/live2vod</code></a></td>
      <td>Live-to-VoD transition.</td>
    </tr>
    <tr>
      <td><a href="https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/mpd-patch"><code>specs/mpd-patch</code></a></td>
      <td>MPD Patching.</td>
    </tr>
    <tr>
      <td><a href="https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/varsub"><code>specs/varsub</code></a></td>
      <td>MPD Variable Substitution.</td>
    </tr>
  </tbody>
</table>

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

<table class="data">
  <thead>
    <tr>
      <th>Feature ID</th>
      <th>Feature</th>
      <th>Category</th>
      <th>IOPv5 reference</th>
      <th>DASH-IF-IOP reference</th>
      <th>Current tool/example lens</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>dynamic-mpd-live</code></td>
      <td>Dynamic MPD / Live DASH</td>
      <td>Live</td>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part04-live-low-latency.html">Part 4</a></td>
      <td>—</td>
      <td>dash.js Live samples; livesim2 dynamic live streams.</td>
    </tr>
    <tr>
      <td><code>segmenttemplate-number</code></td>
      <td>SegmentTemplate Number Addressing</td>
      <td>Core</td>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part02-core-cmaf.html">Part 2</a></td>
      <td>—</td>
      <td>livesim2 default addressing mode.</td>
    </tr>
    <tr>
      <td><code>segmenttimeline-time</code></td>
      <td>SegmentTimeline Time Addressing</td>
      <td>Core</td>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part02-core-cmaf.html">Part 2</a></td>
      <td>—</td>
      <td>livesim2 <code>segtimeline_1</code>; executable Part 4 example.</td>
    </tr>
    <tr>
      <td><code>utc-timing</code></td>
      <td>UTCTiming</td>
      <td>Core</td>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part02-core-cmaf.html">Part 2</a>, <a href="https://dashif.org/Guidelines/iop-v5/part04-live-low-latency.html">Part 4</a></td>
      <td>—</td>
      <td>livesim2 <code>utc_direct</code>; executable Part 4 example.</td>
    </tr>
    <tr>
      <td><code>availability-time-offset</code></td>
      <td>Availability Time Offset</td>
      <td>Live</td>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part04-live-low-latency.html">Part 4</a></td>
      <td>—</td>
      <td>dash.js Live sample; livesim2 <code>ato</code>; executable Part 4 examples.</td>
    </tr>
    <tr>
      <td><code>low-latency-live</code></td>
      <td>Low-Latency Live DASH</td>
      <td>Low latency</td>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part04-live-low-latency.html">Part 4</a></td>
      <td>—</td>
      <td>dash.js low-latency test player; livesim2 <code>chunkdur</code>, <code>ato</code>, <code>ltgt</code>.</td>
    </tr>
    <tr>
      <td><code>service-description-latency</code></td>
      <td>ServiceDescription Latency Signalling</td>
      <td>Low latency</td>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part04-live-low-latency.html">Part 4</a></td>
      <td>—</td>
      <td>dash.js ServiceDescription settings; livesim2 <code>ltgt</code>.</td>
    </tr>
    <tr>
      <td><code>cmaf-chunked-delivery</code></td>
      <td>CMAF Chunked Delivery</td>
      <td>Low latency</td>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part04-live-low-latency.html">Part 4</a></td>
      <td>—</td>
      <td>dash.js low-latency playback; livesim2 <code>chunkdur</code>.</td>
    </tr>
    <tr>
      <td><code>mpd-patching</code></td>
      <td>MPD Patching</td>
      <td>Live</td>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part04-live-low-latency.html">Part 4</a></td>
      <td><a href="https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/mpd-patch"><code>specs/mpd-patch</code></a></td>
      <td>dash.js MPD patching sample.</td>
    </tr>
    <tr>
      <td><code>cmcd</code></td>
      <td>Common Media Client Data</td>
      <td>Reporting</td>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part12-conformance-reference-tools.html">Part 12</a></td>
      <td><a href="https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/cmcd"><code>specs/cmcd</code></a></td>
      <td>dash.js CMCD samples; HTTP request observability.</td>
    </tr>
    <tr>
      <td><code>content-steering</code></td>
      <td>Content Steering</td>
      <td>Delivery</td>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part12-conformance-reference-tools.html">Part 12</a></td>
      <td><a href="https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/content-steering"><code>specs/content-steering</code></a></td>
      <td>dash.js Content Steering support.</td>
    </tr>
    <tr>
      <td><code>content-protection</code></td>
      <td>Content Protection</td>
      <td>Protection</td>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part06-content-protection.html">Part 6</a></td>
      <td>—</td>
      <td>dash.js DRM samples; browser/CDM dependent.</td>
    </tr>
    <tr>
      <td><code>text-tracks</code></td>
      <td>Text Tracks</td>
      <td>Media</td>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part09-text.html">Part 9</a></td>
      <td>—</td>
      <td>dash.js subtitle/caption samples; livesim2 generated time subtitles.</td>
    </tr>
    <tr>
      <td><code>multi-audio</code></td>
      <td>Multi-Audio</td>
      <td>Media</td>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part08-audio.html">Part 8</a></td>
      <td>—</td>
      <td>dash.js multi-audio samples; source asset dependent in livesim2.</td>
    </tr>
    <tr>
      <td><code>inband-emsg-events</code></td>
      <td>Inband <code>emsg</code> Events</td>
      <td>Events</td>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part10-events.html">Part 10</a>, <a href="https://dashif.org/Guidelines/iop-v5/part05-ad-insertion.html">Part 5</a></td>
      <td>—</td>
      <td>dash.js SCTE/emsg sample; usually requires app event handling.</td>
    </tr>
    <tr>
      <td><code>lcevc</code></td>
      <td>MPEG-5 Part 2 LCEVC Carriage</td>
      <td>Video</td>
      <td><a href="https://dashif.org/Guidelines/iop-v5/part07-video.html">Part 7</a></td>
      <td><a href="https://github.com/Dash-Industry-Forum/DASH-IF-IOP/tree/master/specs/lc-evc"><code>specs/lc-evc</code></a></td>
      <td>dash.js LCEVC sample; requires LCEVC-capable pipeline.</td>
    </tr>
  </tbody>
</table>

# Executable examples # {#executable-examples}

Executable examples are maintained separately from feature definitions and point back to the features they cover.

The current example registry is maintained at:

[`rag/examples/executable-examples.yaml`](https://github.com/Dash-Industry-Forum/IOPv5/blob/tstockhammer-rag-workflow/rag-authoring-starter/rag/examples/executable-examples.yaml)

The initial examples focus on Part 4 low-latency livesim2 streams.

<table class="data">
  <thead>
    <tr>
      <th>Example ID</th>
      <th>Covered feature IDs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>part04-ll-basic</code></td>
      <td><code>dynamic-mpd-live</code>, <code>low-latency-live</code>, <code>service-description-latency</code>, <code>cmaf-chunked-delivery</code>, <code>availability-time-offset</code></td>
    </tr>
    <tr>
      <td><code>part04-ll-ultra</code></td>
      <td><code>dynamic-mpd-live</code>, <code>low-latency-live</code>, <code>service-description-latency</code>, <code>cmaf-chunked-delivery</code>, <code>availability-time-offset</code></td>
    </tr>
    <tr>
      <td><code>part04-ll-segtimeline</code></td>
      <td><code>dynamic-mpd-live</code>, <code>low-latency-live</code>, <code>service-description-latency</code>, <code>cmaf-chunked-delivery</code>, <code>availability-time-offset</code>, <code>segmenttimeline-time</code></td>
    </tr>
    <tr>
      <td><code>part04-ll-utc</code></td>
      <td><code>dynamic-mpd-live</code>, <code>low-latency-live</code>, <code>service-description-latency</code>, <code>cmaf-chunked-delivery</code>, <code>availability-time-offset</code>, <code>utc-timing</code></td>
    </tr>
  </tbody>
</table>

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