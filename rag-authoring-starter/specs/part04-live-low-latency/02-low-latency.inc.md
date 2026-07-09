<!--
  Low-Latency Live Services — migrated from
  rag/corpus/drafts/DASH-IF-IOPv5.0-Part4-DRAFT - r1.docx (clause 6),
  grounded via the local RAG index.
  Provenance: dashif-iop-v5-part4-draft-r1#102..#147
  Editorial: OCR artefacts from the source DOCX were corrected; normative
  keywords (shall/should/may) preserved from the source; tables and figures
  from the source are marked as Issue placeholders pending image/table triage.
-->

# Low-Latency Live Services # {#low-latency}

Note: This clause is migrated from the agreed Part 4 draft (clause 6). Tables and
figures referenced below are pending triage; see
`Images/dashif-iop-v5-part4-draft-r1-images.md`.

## Introduction ## {#ll-introduction}

Based on a report developed jointly between DVB and DASH-IF on Low-Latency DASH,
this clause defines details on how to support consistent latency in DASH for
linear TV services. Several latency definitions are repeated here for
consistency:

: <dfn>End-to-End Latency</dfn> (EEL)
:: The latency for an action that is captured by the camera until its visibility
    on the remote screen.
: <dfn>Encoder-Display Latency</dfn> (EDL)
:: The latency of the linear playout output (which typically serves as input to
    distribution encoder(s)) to the screen.
: <dfn export>Packager-Display Latency</dfn>
:: The latency after the output of the distribution encoder to the screen.
: <dfn export>CDN latency</dfn>
:: The delay caused by the CDN delivery from CDN input to CDN output.
: <dfn export>Live Edge Start-up Delay</dfn> (LSD)
:: The time between a user action (service access or service join) and the time
    until the first media sample of the service is perceived by the user when
    joining at the live edge; typically also the channel change time.
: <dfn export>Seek Start-up Delay</dfn> (SSD)
:: The time between a user action and the time until the first media sample of
    the service is perceived by the user when seeking to a position other than
    the live edge.

Start-up delay requirements are typically in the range of 1–2 seconds.

## Scenario and Architecture ## {#ll-architecture}

A typical workflow is presented in the reference figure. This figure does not
present a mandatory deployment architecture but is used to illustrate the
considered interfaces addressed in this clause. The source signal is encoded in
several resolutions/bitrates by the ABR encoder, which produces fragmented MP4 or
MP4/CMAF compliant elementary streams and eventually encrypts them. Those streams
are then ingested into the packager using a protocol suitable to deliver the data
in streams/chunks. The packager proceeds with the necessary operations such as
the transformation of the incoming streams' segment durations, DRM preparation of
the streams, and the generation of the DASH manifests.

Two ways are defined to generate low-latency Representations and Media
Presentations:

- Segments short enough to address the latency are generated; or
- the resulting set of files is made available on disk or RAM storage such that
    the origin server can load the chunks as they are produced (CMAF chunked
    delivery).

Issue: Redraw the source architecture figure as Mermaid/draw.io. Original at
`Images/dashif-iop-v5-part4-draft-r1-img01.png` (pending triage).

## Definitions ## {#ll-definitions}

: <dfn>Low-Latency Service Offering</dfn>
:: A Service Offering that contains information to support a [=Low-Latency DASH
    Client=] to provide the service in the target latency of typically 2 to 10
    seconds; the target latency can be defined by the service provider. Target
    latency may be [=End-to-End Latency=] or [=Encoder-Display Latency=] as
    defined in [[#ll-introduction]].
: <dfn>Low-Latency Adaptation Set</dfn>
:: An Adaptation Set that can be consumed based on the low-latency service
    offering.
: <dfn>Low-Latency Chunked Adaptation Set</dfn>
:: A [=Low-Latency Adaptation Set=] offered containing Representations that
    provide early access to Segments as well as CMAF chunked content.
: <dfn>Low-Latency Segment Adaptation Set</dfn>
:: A [=Low-Latency Adaptation Set=] offered containing Representations that
    provide short enough Segments to be consumed as a low-latency service.
: <dfn>Low-Latency DASH Client</dfn>
:: A client that follows this specification in order to consume the Media
    Presentation of a [=Low-Latency Service Offering=].

## Low-Latency Service Offering ## {#ll-service-offering}

### General ### {#ll-so-general}

A Media Presentation that follows a DASH-IF [=Low-Latency Service Offering=]
according to this specification should be signalled with the `@profiles`
identifier `http://www.dashif.org/guidelines/low-latency-live-v5`.

If an MPD signals conformance to this profile, it shall follow the requirements
and recommendations of [[#ll-so-requirements]] and the referenced clauses.

A legacy service offering is documented in [[#ll-legacy]]. This legacy offering
does not conform to the DASH-IF [=Low-Latency Service Offering=] profile but may
be used in practice. DVB Low-Latency DASH is documented in ETSI TS 103 285;
compatibility aspects are documented in [[#ll-dvb]].

### General Service Offering Requirements and Recommendations ### {#ll-so-requirements}

A [=Low-Latency Service Offering=] follows these requirements and
recommendations:

- At least one `ServiceDescription` element shall be present.
- One or several `Scope` elements may be present. The `Scope` element specifies
    the scope of the service description element. If present, the service
    description only targets DASH clients within the scope of this descriptor.
    DASH clients not in scope (i.e. not recognizing any of the scope descriptor
    elements) are expected to ignore this service description.
- A `Latency` element shall be present including a `@target` attribute providing
    the service provider's preferred presentation latency in milliseconds
    computed relative to the producer reference time.

Note: The scope may, for example, be used to offer content to clients on
different network conditions for which the expectation of the target latency is
different. DASH-IF does not define a scope description at this stage; it focuses
on the interpretation of the Service Description assuming that the client is in
scope.

For protected content, the rules documented in the Content Protection clause
apply. Service implementation guidelines are provided in
[[#ll-guidelines]].

### Low-Latency Adaptation Set ### {#ll-adaptation-set}

A [=Low-Latency Adaptation Set=] follows these requirements and recommendations:

- It shall include at least one `ProducerReferenceTime` element with the
    following constraints:
    - `@id`: provide a unique id for this reference.
    - `@type`: shall be set either to `encoder` or `captured`.
    - A `UTCTiming` element that is identical to one present in the MPD shall be
        present and is used for deriving the value of `@wallclockTime`.
    - `@wallclockTime`: shall be present and provide the value at the
        `@presentationTime`.
    - `@presentationTime`: shall be the value of `@presentationTimeOffset`, if
        present, or 0 otherwise.
    - `@inband` may be set to `FALSE` or `TRUE`.
- A [=Low-Latency Adaptation Set=] shall be either a [=Low-Latency Segment
    Adaptation Set=] or a [=Low-Latency Chunked Adaptation Set=].
- One of the following shall be present: the `SegmentTemplate@duration`
    attribute, or `SegmentTemplate@media` with `$Number$` and `$Time$`.

The segment duration shall not vary more than indicated in the MPD.

Note: The producer reference time is provided at the start of the Period.

### Low-Latency Segment Adaptation Set ### {#ll-segment-as}

A [=Low-Latency Segment Adaptation Set=] follows these requirements and
recommendations:

- It shall conform to a [=Low-Latency Adaptation Set=].
- Each Segment should include only a single movie fragment header (`moof`). If a
    Segment includes only a single `moof`, then it may carry an `smds` brand and
    shall signal this by including the `smds` brand in `@segmentProfiles`.
- `@availabilityTimeComplete` and `@availabilityTimeOffset` for all
    Representations shall be absent, indicating that the Segments are completely
    available when requested.
- The Segment duration shall not exceed 50% of the target latency and should not
    exceed 30% of the target latency.

A [=Low-Latency Segment Adaptation Set=] is identified by the settings above as
well as by the absence of the `Resync` element.

### Low-Latency Chunked Adaptation Set ### {#ll-chunked-as}

A [=Low-Latency Chunked Adaptation Set=] follows these requirements and
recommendations:

- It shall conform to a [=Low-Latency Adaptation Set=].
- Each Adaptation Set shall conform to an Adaptation Set according to the DASH
    profile for CMAF content as defined in MPEG DASH.
- Each Segment shall conform to a CMAF Fragment but may — and typically should —
    contain more than one CMAF chunk. CMAF chunks should be generated such that
    the range of presentation times contained in any CMAF chunk of the CMAF Track
    does not overlap with the range of presentation times in any other CMAF chunk
    of the same CMAF Track.
- A `Resync` element should be assigned to each Representation (possibly
    defaulted) signalling the properties of the Segments and the chunks used
    (chunk size, chunk duration, chunk properties). See [[#ll-resync]].

Note: The resynchronization feature was introduced in ISO/IEC
23009-1:2020/Amd.1. As correct handling is not guaranteed by legacy DASH clients
(including, for example, DVB LL-DASH clients), content authors should be careful
in relying on this information.

### Legacy Setup ### {#ll-legacy}

As low-latency DASH services have developed over time, this clause documents
legacy aspects compared to the DASH-IF [=Low-Latency Service Offering=] profile.
In such a legacy setup one or more of the following applies:

- The `ServiceDescription` element may not be present. In particular, the target
    latency may be absent, but may be provided by external means (for example by
    the application setting the value through an API).
- The `ProducerReferenceTime` element may not be present. In this case, the
    Period Start time is assumed to be used as the wall-clock time and the value
    of `@presentationTimeOffset` is assumed as the corresponding presentation
    time.
- The Segment durations for [=Low-Latency Segment Adaptation Set=]s may exceed
    the 50% target value.
- The [=Low-Latency Chunked Adaptation Set=]s may not conform to an Adaptation
    Set according to the DASH profile for CMAF content as defined in MPEG DASH.
- The `Resync` element may not be present.

### DVB Low-Latency DASH ### {#ll-dvb}

DVB Low-Latency DASH is documented in ETSI TS 103 285. As that specification was
completed prior to the DASH-IF specification, a few issues are documented here:

- Per TS 103 285 clause 10.20.3, DVB DASH clients consider themselves in scope
    where a `ServiceDescription` element contains a `Scope` element with
    `@schemeIdUri` set to `urn:dvb:dash:lowlatency:scope:2019`.
- The DVB-DASH Content Provider Guidelines (informative) recommend the use of
    `@duration` together with `$Number$`, whereas DASH-IF makes no such
    recommendation.
- DVB DASH does not mention the `Resync` element, but the presence of the element
    would not break a DVB-DASH client.
- DVB DASH signals Adaptation Sets used for low-latency purposes with an
    `EssentialProperty` or `SupplementalProperty` descriptor with `@schemeIdUri`
    set to `urn:dvb:dash:lowlatency:critical:2019` and `@value` set to `true`. If
    the `SupplementalProperty` descriptor is used, this does not impact regular
    low-latency DASH clients.

## Low-Latency Client ## {#ll-client}

For a DASH-IF [=Low-Latency DASH Client=] the following applies. The client shall
be able to consume content offered with the DASH-IF [=Low-Latency Service
Offering=] profile as defined in [[#ll-so-requirements]]. Specifically, this
includes:

- Support for media segments that contain more than one pair of `moof` and
    `mdat` boxes, where each `moof`/`mdat` pair may contain any number of ISO
    BMFF samples between 1 and the full segment duration inclusive.
- Support for playing two or more Adaptation Sets for which the Segments of one
    Adaptation Set do not align with the Segments of another (e.g. due to
    differing segment durations), or where the Segments of one Adaptation Set
    contain multiple `moof`/`mdat` pairs and the Segments of another have only a
    single `moof`/`mdat` pair.

## Guidelines for Low-Latency Service Offering (Informative) ## {#ll-guidelines}

This clause provides further guidelines and considerations for a [=Low-Latency
Service Offering=] beyond the requirements and recommendations in
[[#ll-service-offering]]. It is not meant to provide a normative implementation
but provides a reference implementation as well as a set of guidelines on how to
operate a headend for low-latency distribution.

Note: This clause is a starting point; more information is expected to be added
over time.

### Encoding and CMAF Chunk Duration ### {#ll-chunk-duration}

CMAF chunks are a way to reduce streaming latency without decreasing the IDR
frame frequency and the DASH segment sizes. In the general case — for example
with typical efficient encoding configurations using B-frames — creating chunks
with a duration of one sample per chunk is not desirable. This applies not only
to video but also to audio and possibly subtitles.

For **video**, to make each chunk displayable without waiting for more data, it
is important that all B-frames which should be displayed before the P-frame are
included in the chunk. As an example, hierarchical B-frames with the display
order `I0 B1 B2 B3 P4 | B5 B6 B7 P8 | ...` have a decode (send) order
`I0 P4 B1 B2 B3 | P8 B6 B5 B7 | ...`; the chunk should therefore be broken after
a multiple of 4–5 frames (160–200 ms for 25 Hz video). The general recommendation
is to place chunk boundaries so that all display times are before the earliest
display time of the next chunk.

For **audio**, the bitrate is relatively low (e.g. a 200 ms audio chunk at
64 kbps is ~1.6 kB), which may be too small to propagate through network or
receiver buffers. It may therefore make sense to use longer chunks (e.g. 0.5 s
for audio), or not apply chunking for audio and instead run at a shorter Segment
duration.

For **subtitles**, chunking is generally undesirable: an IMSC-1 sample is a TTML
XML document with relatively large boilerplate (~2 kB) even for a short sentence.
Splitting a 2 s subtitle segment into 10 chunks would increase the bitrate by an
order of magnitude and increase client XML parsing. It is therefore suggested
that subtitles are not chunked but delivered as separate segments every 1 s or
so.

### Producer Reference Time ### {#ll-prft}

The Producer Reference Time supplies times corresponding to the production of
associated media. This information permits, among others, to (i) provide media
clients with information to enable consumption and production to proceed at
equivalent rates, thus avoiding possible buffer overflow or underflow, and
(ii) enable measuring and potentially controlling the latency between production
of the media time and playout. The Producer Reference Time (`prft`) is defined in
ISO/IEC 14496-12. The information may be provided inband as part of the Segments
(in the `prft` box), in the MPD, or both.

### Service Description ### {#ll-service-description}

Annex K of ISO/IEC 23009-1 defines the DASH Service Description. In the DASH
model, the DASH client has significant control over the algorithms and user
perception for a DASH service (rate adaptation algorithm, buffer strategy, buffer
duration, and the resulting latency and channel access times). However, leaving
all decisions to the client may result in inconsistent behaviour across
implementations. Hence, Annex K defines a service description reference model for
the client that the content provider indicates is appropriate for automatically
adjusting playback latency and buffer occupancy during normal playback.

### Resynchronization Points ### {#ll-resync}

Consistent insertion and signalling of Resynchronization Points is recommended,
following ISO/IEC 23009-1:2020/Amd.1. Signalling Resynchronization Points can be
used by DASH clients for several purposes:

- Fast random access while maintaining low latency.
- Quick resynchronization after buffer underruns.
- In-Segment downswitching when buffer draining is observed.
- Understanding the applied chunk size and duration and hence support for rate
    adaptation.

The following is recommended: provide `Resync` signalling for each [=Low-Latency
Chunked Adaptation Set=] by adding a `Resync` element with the known parameters
(for example, on Adaptation Set level, `@dT` providing the maximum and nominal
duration of each chunk).

### Fast Switching Adaptation Sets ### {#ll-fast-switching}

Issue: Fast Switching Adaptation Set generation and signalling is for further
study. Reconciliation against Low-Latency CR r8/r9 (see
`rag/reports/reconcile-low-latency-r8-r9.md`) found no new normative construct:
both CRs specify resynchronization via the existing `Resync` element (see
[[#ll-resync]]) rather than a distinct "Addressable Resync Representation". The
ARR concept is retained only as a forward-looking term pending MPEG-DASH.

The following sequence illustrates fast tune-in (redrawn as Mermaid from the
source Word figure; see `Images/dashif-iop-v5-part4-draft-r1-images.md` for the
original figures pending triage).

<figure>
<pre class=mermaid>
sequenceDiagram
    participant C as Client
    participant O as Origin
    C->>O: Request low-latency segments (chunked transfer)
    O-->>C: CMAF chunks (early availability)
    Note over C,O: Fast tune-in via Addressable Resync Representation
</pre>
<figcaption>Fast tune-in with an Addressable Resync Representation.</figcaption>
</figure>

### MPD Generation for CMAF Media ### {#ll-mpd-cmaf}

It is recommended to apply the DASH Profile for CMAF content in case CMAF content
is used.

### Service Configuration Parameters ### {#ll-config-params}

Issue: Migrate configuration-parameter tables (Table 1–4 in the source) once
tables are triaged. For [=Low-Latency Segment Adaptation Set=]s, the chunk
duration is identical to the Segment Duration; the Segment Duration is at most 30%
of the target latency. For [=Low-Latency Chunked Adaptation Set=]s with multiple
Representations, if the Segment Duration is larger than 50% of the target
latency, a Representation is added whose bitrate is identical to the lowest
bitrate Representation and whose chunks create Resync Marker Points.

Note: A reference FFmpeg configuration is provided in the source draft; in the
final version this is expected to be replaced by a reference rather than inline
command lines.

### MPD Generator and Packager Operation ### {#ll-packager}

This clause introduces a reference DASH packager for low-latency that also adds a
period boundary at indicated times. The implementation is an example only; other
approaches may be used. The basic operation of the DASH packager is as follows:

- The DASH packager creates an initial MPD based on the configuration
    information in [[#ll-config-params]].
- The DASH packager acts as a slave to the ABR encoder and incoming data formats.
- The DASH packager formats and generates MPDs dynamically and ingests the
    Segments into the CDN.
- The DASH packager ensures the Segment availability times in the MPD are correct
    at the origin.

Two backward-compatible reference profiles are described in the source:
**Simple Live** (using `$Number$` and `@duration` for duration signalling, with
`@minimumUpdatePeriod` or inband MPD validity expirations) and **Main Live**
(using `$Time$` and `SegmentTimeline`). In both, each CMAF fragment generates one
DASH segment and each CMAF chunk is offered as an HTTP chunk.

Issue: A **Broadcast TV Profile** extension is explicitly deferred to a future
version in both Low-Latency CR r8 (clause 6.6.4.4) and r9 (clause 9.X.6.4.4); no
normative text exists to migrate yet. Tracked as future work (see
`rag/reports/reconcile-low-latency-r8-r9.md`).

## Client Implementation Guidelines (Informative) ## {#ll-client-guidelines}

The following should be considered for a low-latency client implementation:

- It should be configurable regarding using the low-latency mode and which
    configuration to use (e.g. how aggressive it is in latency maintenance).
- Updates and considerations in the ABR logic and throughput estimation apply
    (see [[#ll-bandwidth]]).
- Start-up operations should be considered to maintain latency and manage
    start-up delays; joining needs to be done carefully (it is better to wait for
    the next RAP than to play out stale content).

If requested to act as a low-latency client, the client is preferably configured
with the Low-Latency Service Parameters, using parameters from different sources
of information in priority order (MPD Service Description first, then other MPD
information such as the legacy service offering, then the client's own logic).

### Connection Bandwidth Estimation ### {#ll-bandwidth}

If the connection bandwidth available for downloading media segments is lower than
the required bitrate of all the Representations being played, this leads to
reduced buffer occupancy at the player and the need for downward adaptation can be
detected straightforwardly. Excess connection bandwidth is more difficult to
observe. One possible approach could involve measuring HTTP/1.1 chunked
transfer-encoding chunks or HTTP/2 frames, provided these are of sufficient size.
If the HTTP chunk/frame structure is not visible (e.g. in a browser-based client
using the Fetch API), this estimation is harder.

### Reference Playback ### {#ll-reference-playback}

The reference playback platform is expected to support the CTA WAVE Device
Playback Specification requirements, in particular playback of low-latency and
chunked content.

## Low-Latency DASH and Multicast ## {#ll-multicast}

Note: This will be addressed in future versions.
