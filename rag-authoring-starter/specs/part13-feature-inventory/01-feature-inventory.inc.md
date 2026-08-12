# Introduction # {#introduction}

<div class="note" role="note">
  <p><strong>Early draft — work in progress.</strong> This part is at a very early,
  exploratory stage. The feature model, the taxonomy, the inventory tables, and the
  tool/example lenses below are <em>preliminary placeholders</em> intended to
  establish structure and to seed discussion. Nothing in this part is stable, complete,
  or agreed. Feature names, groupings, granularity, references, and support claims are
  expected to change substantially, and entries may be added, merged, split, or removed
  without notice. Do not treat this part as an authoritative statement of DASH-IF
  feature support or of IOPv5 scope.</p>
</div>

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

# Related feature-review activities # {#related-feature-reviews}

Feature inventories and feature-selection reviews are being carried out in other
organizations as well. These are valuable inputs for scoping Part 13 and for deciding
which DASH features are relevant for interoperable deployment. They are summarized here
as editorial context only; none of the assessments below are DASH-IF positions.

## DVB feature review of MPEG DASH editions ## {#dvb-feature-review}

DVB has begun a systematic review of what has been added to MPEG DASH (ISO/IEC 23009-1)
from the 3rd edition onward, with the aim of deciding which additions are relevant for
DVB-DASH. This is directly useful for Part 13 because it frames each DASH feature in
terms of concrete use cases, HLS equivalence, reference-tool support, and deployment
relevance.

Key observations from the DVB review that are relevant to this inventory:

- ISO withdraws older DASH editions when a new one is published (e.g. the 4th edition
    was withdrawn when the 5th was published), which complicates stable referencing and
    argues for a curated, editorially-maintained feature view such as Part 13.
- Investment in reference tools and unit tests for additions after the 3rd edition is
    still limited, so tool/example support is an important dimension when assessing a
    feature's readiness.
- Each added feature is best characterized by: a short summary, a use case or scenario,
    an HLS equivalent (if any), the relevant DASH clause references, the closest existing
    DVB-DASH functionality, and open-source support status (dash.js, livesim2, Shaka,
    hls.js, and others).

The following table summarizes DASH features highlighted by the DVB review, grouped by
the edition in which they were introduced. The "DVB relevance" column reflects the DVB
review's own preliminary assessment and is included here purely as external context.

<table class="data">
  <thead>
    <tr>
      <th>Feature / clause</th>
      <th>Introduced</th>
      <th>Summary</th>
      <th>DVB relevance (per DVB review)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Producer Reference Time (5.12)</td>
      <td>4th edition</td>
      <td>Signalling and mapping of media time to wall-clock time, including capture/encoding context.</td>
      <td>Relevant</td>
    </tr>
    <tr>
      <td>Leap seconds (5.13)</td>
      <td>4th edition</td>
      <td>Support for client timing calculations when leap seconds occur.</td>
      <td>Relevant</td>
    </tr>
    <tr>
      <td>Service Description (Annex K)</td>
      <td>4th edition</td>
      <td>Provider signalling on how a service is expected to be consumed.</td>
      <td>Relevant</td>
    </tr>
    <tr>
      <td>Missing Content Segment (6.2.6)</td>
      <td>4th edition</td>
      <td>Signals that content is missing while conveying the media duration of the gap.</td>
      <td>Probably (live)</td>
    </tr>
    <tr>
      <td>Location and reference resolution (Annex A.11)</td>
      <td>4th edition</td>
      <td>Consistent URL/reference resolution for MPD updates, segments, and other MPD resources.</td>
      <td>Probably</td>
    </tr>
    <tr>
      <td>Failover Content Signalling (5.3.9.7/5.3.9.8)</td>
      <td>4th edition</td>
      <td>Offering failover content in place of properly-encoded main content on ingest/encoding errors.</td>
      <td>Uncertain</td>
    </tr>
    <tr>
      <td>Initialization Set / Group / Presentation (5.3.12)</td>
      <td>4th edition</td>
      <td>Simplifies playback across Period boundaries.</td>
      <td>Uncertain</td>
    </tr>
    <tr>
      <td>Resynchronization (5.3.13, 6.3.2.5, Annex A.12)</td>
      <td>5th edition</td>
      <td>In-segment resynchronization and early access; fast tune-in, loss recovery, seek accuracy.</td>
      <td>Uncertain</td>
    </tr>
    <tr>
      <td>MPD Patch framework (5.15)</td>
      <td>5th edition</td>
      <td>Transmit only changed parts of a dynamic MPD to reduce bandwidth/processing overhead.</td>
      <td>Perhaps (currently recommended against in DVB)</td>
    </tr>
    <tr>
      <td>DASH profile for CMAF content (8.12)</td>
      <td>5th edition</td>
      <td>Prescriptive mapping of CMAF structures/timelines to DASH.</td>
      <td>Partial</td>
    </tr>
    <tr>
      <td>Output protection / robustness signalling (5.8.4.12, 5.8.5.14)</td>
      <td>5th edition</td>
      <td>Efficient content-protection signalling, robustness levels, and HDCP output-protection descriptor.</td>
      <td>Relevant</td>
    </tr>
    <tr>
      <td>Event/timed-metadata client reference model (Annex A.13)</td>
      <td>5th edition</td>
      <td>Timing and processing model for MPD/inband event streams and timed metadata tracks.</td>
      <td>Uncertain</td>
    </tr>
    <tr>
      <td>Variable bitrate bandwidth signalling (5.3.5.6)</td>
      <td>5th edition</td>
      <td>More flexible bandwidth signalling for VBR encoding.</td>
      <td>Uncertain</td>
    </tr>
    <tr>
      <td>Alternative Media Presentation (5.16, 8.14, Annex A.14) and Media Presentation Insertion events</td>
      <td>6th edition</td>
      <td>Switching between main and alternative presentations (e.g. preroll/midroll ads, blackouts); enables SGAI.</td>
      <td>Not yet; potential broadband ad-insertion alternative</td>
    </tr>
    <tr>
      <td>Content Steering (K.3.6)</td>
      <td>6th edition</td>
      <td>Interoperable server-centric multi-CDN steering (HLS-equivalent exists).</td>
      <td>Overlaps with DVB multiple BaseURLs (client-centric)</td>
    </tr>
    <tr>
      <td>Enhanced segment sequences / fast tune-in (5.3.5.7, 5.3.9.7, "L3D")</td>
      <td>6th edition</td>
      <td>Faster time-to-first-video on join; relevant for ultra-low-latency services.</td>
      <td>Relevant</td>
    </tr>
    <tr>
      <td>Segment duration patterns (5.3.9.6.5)</td>
      <td>6th edition</td>
      <td>Compact MPDs for fractional frame rates and when audio/video durations differ.</td>
      <td>Relevant outside 50 Hz markets</td>
    </tr>
    <tr>
      <td>CMCD reporting via service description (K.3.7)</td>
      <td>6th edition</td>
      <td>In-manifest CMCD (v1) configuration without a bespoke application.</td>
      <td>Relevant (relates to DVB metrics)</td>
    </tr>
    <tr>
      <td>Event and playback restrictions via service description (K.3.8)</td>
      <td>6th edition</td>
      <td>Signals ff/seek restrictions (e.g. no skipping during ads).</td>
      <td>Relevant for ad insertion</td>
    </tr>
    <tr>
      <td>Improved query parameters and header extensions (Annex I.3.6, I.4)</td>
      <td>6th edition</td>
      <td>Token pass-through and richer URL parameterization; CDN authorization tokens.</td>
      <td>Uncertain</td>
    </tr>
    <tr>
      <td>Addressable Resource Index (ARI) Tracks (Annex M)</td>
      <td>6th edition</td>
      <td>Exact quality/bitrate and inband-message presence for segments/chunks.</td>
      <td>Uncertain</td>
    </tr>
    <tr>
      <td>Alternative codecs via preselection (G.30)</td>
      <td>6th edition</td>
      <td>A track decodable by more than one codec (e.g. HEVC / MV-HEVC / LCEVC).</td>
      <td>Uncertain</td>
    </tr>
    <tr>
      <td>Nonlinear playback / interactive storylines (Annex L)</td>
      <td>6th edition</td>
      <td>User-driven nonlinear Period selection (Bandersnatch-style experiences).</td>
      <td>Not relevant to DVB (app-level)</td>
    </tr>
    <tr>
      <td>Multi-key encryption (G.25)</td>
      <td>6th edition</td>
      <td>Different keys across CMAF-aligned switching sets (e.g. HD vs UHD).</td>
      <td>Uncertain</td>
    </tr>
    <tr>
      <td>ISO BMFF Advanced Linear / List / Single-Period Static profiles (8.13–8.15)</td>
      <td>5th/6th edition</td>
      <td>Profiles for long-running linear content and imported/list MPDs supporting SGAI and blackouts.</td>
      <td>Potential input for feature selection</td>
    </tr>
  </tbody>
</table>

Additional editorial context from the DVB review:

- <strong>MPD Chaining (5.11)</strong> and <strong>Flexible Insertion of URL Parameters
    (Annex I)</strong> were noted as, respectively, largely unused and only beginning to
    see adoption; Annex I is relevant for CDN authorization tokens (e.g. Common Access
    Token) and has partial dash.js support.
- The DVB review draws on the DASH-IF April 2024 special presentation on the 6th edition
    ([SpecialPresentation-6thEdition.pdf](https://github.com/Dash-Industry-Forum/Dash-Industry-Forum.github.io/files/14887658/SpecialPresentation-6thEdition.pdf))
    as background material.

## DASH core feature timeline (ISO/IEC 23009-1 editions) ## {#dash-core-feature-timeline}

This subsection collects the DASH features added in successive editions of
ISO/IEC 23009-1, extracted from clause 4 (Overview) and clause 5 (Media Presentation
Description) of the 6th edition, using the authoritative per-edition schema-addition
list in subclause 5.2.3 ("Elements and Attributes added in revisions and amendments") as
the backbone. Clause numbers use the 6th-edition numbering and should be re-verified
against the final published text.

The full extraction, including the per-edition element/attribute lists and the mapping
from each feature to its defining clause, is maintained as a working report:
`rag/reports/iso-23009-1-6th-edition-feature-extraction.md`.

<table class="data">
  <thead>
    <tr>
      <th>Feature ID</th>
      <th>Feature</th>
      <th>Edition introduced</th>
      <th>Primary clause (6th ed.)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>utc-timing</code></td><td>UTCTiming</td><td>3rd</td><td>5.8.5</td></tr>
    <tr><td><code>preselections</code></td><td>Preselections</td><td>3rd</td><td>5.3.11</td></tr>
    <tr><td><code>random-access-signalling</code></td><td>RandomAccess signalling</td><td>3rd</td><td>5.3.5</td></tr>
    <tr><td><code>switching-signalling</code></td><td>Switching signalling</td><td>3rd</td><td>5.3.5</td></tr>
    <tr><td><code>labels-group-labels</code></td><td>Labels and Group Labels</td><td>3rd</td><td>5.3.10</td></tr>
    <tr><td><code>service-description</code></td><td>Service Description</td><td>4th</td><td>Annex K</td></tr>
    <tr><td><code>initialization-set-group-presentation</code></td><td>Initialization Set / Group / Presentation</td><td>4th</td><td>5.3.12</td></tr>
    <tr><td><code>producer-reference-time</code></td><td>Producer Reference Time</td><td>4th</td><td>5.12</td></tr>
    <tr><td><code>leap-seconds</code></td><td>Leap seconds</td><td>4th</td><td>5.13</td></tr>
    <tr><td><code>content-popularity-rate</code></td><td>Content Popularity Rate</td><td>4th</td><td>5.14</td></tr>
    <tr><td><code>failover-content</code></td><td>Failover Content Signalling</td><td>4th</td><td>5.3.9.7</td></tr>
    <tr><td><code>availability-time-offset</code></td><td>Availability Time Offset</td><td>2nd/4th</td><td>5.3.9.5</td></tr>
    <tr><td><code>mpd-content-protection</code></td><td>MPD/Period-level ContentProtection</td><td>5th</td><td>5.8.4</td></tr>
    <tr><td><code>mpd-patching</code></td><td>MPD Patch Framework</td><td>5th</td><td>5.15</td></tr>
    <tr><td><code>resync</code></td><td>Resynchronization</td><td>5th</td><td>5.3.13 / 6.3.2.5</td></tr>
    <tr><td><code>extended-bandwidth</code></td><td>Extended / variable bitrate bandwidth signalling</td><td>5th</td><td>5.3.5</td></tr>
    <tr><td><code>output-protection</code></td><td>Output protection + robustness</td><td>5th</td><td>5.8.4</td></tr>
    <tr><td><code>container-profiles</code></td><td>Container profile signalling</td><td>5th</td><td>5.3.5</td></tr>
    <tr><td><code>content-steering</code></td><td>Content Steering</td><td>6th</td><td>Annex K.3.6 (+ 5.6.5)</td></tr>
    <tr><td><code>segment-sequences</code></td><td>Segment Sequences</td><td>6th</td><td>5.3.9.7</td></tr>
    <tr><td><code>duration-patterns</code></td><td>Duration Patterns</td><td>6th</td><td>5.3.9.6.5</td></tr>
    <tr><td><code>cmcd-reporting</code></td><td>CMCD reporting via Service Description</td><td>6th</td><td>Annex K.3.7</td></tr>
    <tr><td><code>playback-restrictions</code></td><td>Event &amp; playback restrictions</td><td>6th</td><td>Annex K.3.8</td></tr>
    <tr><td><code>request-params</code></td><td>Improved query parameters / header extensions</td><td>6th</td><td>Annex I</td></tr>
    <tr><td><code>alternative-media-presentation</code></td><td>Alternative Media Presentations + insertion/replacement events</td><td>6th</td><td>5.16</td></tr>
    <tr><td><code>supplementary-video</code></td><td>Supplementary video services + descriptor</td><td>5th/6th</td><td>5.8.5.16</td></tr>
    <tr><td><code>edrap-esr</code></td><td>Main and External Stream Representations (EDRAP/ESR)</td><td>6th</td><td>5.8.x</td></tr>
  </tbody>
</table>

<div class="note" role="note">
  <p>This timeline is derived from a merged 6th-edition working draft and is itself an
  early extraction. Segment-format and profile additions (clauses 6–8, e.g. ISO BMFF
  Advanced Linear, List, and Single-Period Static profiles), Addressable Resource Index
  (ARI) tracks (Annex M), nonlinear playback (Annex L), and multi-key encryption are
  outside clause 4/5 and are tracked separately via the DVB feature review above.</p>
</div>

## Features beyond IOPv5 ## {#features-beyond-iopv5}

A separate, longer-term "features beyond IOPv5" exploration collects candidate features
and technologies that are not (yet) in scope for IOPv5 but may become relevant in future
guidelines. It is maintained as a living document:

- [Features beyond IOPv5 (Google Doc)](https://docs.google.com/document/d/1x5CPEG0KYp20U84PEvcnonkHbVr4OUMAhcBc9IOotkU/edit?usp=sharing)

<div class="note" role="note">
  <p>The "features beyond IOPv5" document has not been updated recently, so some entries
  may be stale. It is nonetheless a useful source of candidate features and open
  questions when extending this inventory.</p>
</div>

# Open editorial issues # {#open-editorial-issues}

The following issues require review:

- Whether DASH-IF-IOP extensions should remain external references or become IOPv5 feature definitions.
- Whether feature granularity should be finer for codec, DRM, audio, and text options.
- Whether Part 13 should eventually become a generated document from `rag/features/feature-inventory.yaml`.
- Which features require conformance validator checks, executable examples, or custom test applications.