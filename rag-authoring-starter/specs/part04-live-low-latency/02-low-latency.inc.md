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

## Introduction ## {#ll-introduction}

Note: This clause is migrated from the agreed Part 4 draft (clause 6). Tables and
figures referenced below are pending triage; see
`Images/dashif-iop-v5-part4-draft-r1-images.md`.

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
    latency <span class=modal-keyword>may</span> be [=End-to-End Latency=] or [=Encoder-Display Latency=] as
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
according to this specification <span class=modal-keyword>should</span> be signalled with the `@profiles`
identifier `http://www.dashif.org/guidelines/low-latency-live-v5`.

If an MPD signals conformance to this profile, it <span class=modal-keyword>shall</span> follow the requirements
and recommendations of [[#ll-so-requirements]] and the referenced clauses.

A legacy service offering is documented in [[#ll-legacy]]. This legacy offering
does not conform to the DASH-IF [=Low-Latency Service Offering=] profile but <span class=modal-keyword>may</span>
be used in practice. DVB Low-Latency DASH is documented in ETSI TS 103 285;
compatibility aspects are documented in [[#ll-dvb]].

### General Service Offering Requirements and Recommendations ### {#ll-so-requirements}

A [=Low-Latency Service Offering=] follows these requirements and
recommendations:

- At least one <b>ServiceDescription</b> element <span class=modal-keyword>shall</span> be present.
- One or several <b>Scope</b> elements <span class=modal-keyword>may</span> be present. The <b>Scope</b> element specifies
    the scope of the service description element. If present, the service
    description only targets DASH clients within the scope of this descriptor.
    DASH clients not in scope (i.e. not recognizing any of the scope descriptor
    elements) are expected to ignore this service description.
- A <b>Latency</b> element <span class=modal-keyword>shall</span> be present including a `@target` attribute providing
    the service provider's preferred presentation latency in milliseconds
    computed relative to the producer reference time.

Note: The scope <span class=modal-keyword>may</span>, for example, be used to offer content to clients on
different network conditions for which the expectation of the target latency is
different. DASH-IF does not define a scope description at this stage; it focuses
on the interpretation of the Service Description assuming that the client is in
scope.

For protected content, the rules documented in the Content Protection clause
apply. Service implementation guidelines are provided in
[[#ll-guidelines]].

### Low-Latency Adaptation Set ### {#ll-adaptation-set}

A [=Low-Latency Adaptation Set=] follows these requirements and recommendations:

- It <span class=modal-keyword>shall</span> include at least one <b>ProducerReferenceTime</b> element with the
    following constraints:
    - `@id`: provide a unique id for this reference.
    - `@type`: <span class=modal-keyword>shall</span> be set either to `encoder` or `captured`.
    - A <b>UTCTiming</b> element that is identical to one present in the MPD <span class=modal-keyword>shall</span> be
        present and is used for deriving the value of `@wallclockTime`.
    - `@wallclockTime`: <span class=modal-keyword>shall</span> be present and provide the value at the
        `@presentationTime`.
    - `@presentationTime`: <span class=modal-keyword>shall</span> be the value of `@presentationTimeOffset`, if
        present, or 0 otherwise.
    - `@inband` <span class=modal-keyword>may</span> be set to `FALSE` or `TRUE`.
- A [=Low-Latency Adaptation Set=] <span class=modal-keyword>shall</span> be either a [=Low-Latency Segment
    Adaptation Set=] or a [=Low-Latency Chunked Adaptation Set=].
- One of the following <span class=modal-keyword>shall</span> be present: the <code><b>SegmentTemplate</b>@duration</code>
    attribute, or <code><b>SegmentTemplate</b>@media</code> with `$Number$` and `$Time$`.

The segment duration <span class=modal-keyword><span class=modal-keyword>shall</span> not</span> vary more than indicated in the MPD.

Note: The producer reference time is provided at the start of the Period.

### Low-Latency Segment Adaptation Set ### {#ll-segment-as}

A [=Low-Latency Segment Adaptation Set=] follows these requirements and
recommendations:

- It <span class=modal-keyword>shall</span> conform to a [=Low-Latency Adaptation Set=].
- Each Segment <span class=modal-keyword>should</span> include only a single movie fragment header (`moof`). If a
    Segment includes only a single `moof`, then it <span class=modal-keyword>may</span> carry an `smds` brand and
    <span class=modal-keyword>shall</span> signal this by including the `smds` brand in `@segmentProfiles`.
- `@availabilityTimeComplete` and `@availabilityTimeOffset` for all
    Representations <span class=modal-keyword>shall</span> be absent, indicating that the Segments are completely
    available when requested.
- The Segment duration <span class=modal-keyword><span class=modal-keyword>shall</span> not</span> exceed 50% of the target latency and <span class=modal-keyword><span class=modal-keyword>should</span> not</span>
    exceed 30% of the target latency.

A [=Low-Latency Segment Adaptation Set=] is identified by the settings above as
well as by the absence of the <b>Resync</b> element.

### Low-Latency Chunked Adaptation Set ### {#ll-chunked-as}

A [=Low-Latency Chunked Adaptation Set=] follows these requirements and
recommendations:

- It <span class=modal-keyword>shall</span> conform to a [=Low-Latency Adaptation Set=].
- Each Adaptation Set <span class=modal-keyword>shall</span> conform to an Adaptation Set according to the DASH
    profile for CMAF content as defined in MPEG DASH.
- Each Segment <span class=modal-keyword>shall</span> conform to a CMAF Fragment but <span class=modal-keyword>may</span> — and typically <span class=modal-keyword>should</span> —
    contain more than one CMAF chunk. CMAF chunks <span class=modal-keyword>should</span> be generated such that
    the range of presentation times contained in any CMAF chunk of the CMAF Track
    does not overlap with the range of presentation times in any other CMAF chunk
    of the same CMAF Track.
- A <b>Resync</b> element <span class=modal-keyword>should</span> be assigned to each Representation (possibly
    defaulted) signalling the properties of the Segments and the chunks used
    (chunk size, chunk duration, chunk properties). See [[#ll-resync]].

Note: The resynchronization feature was introduced in ISO/IEC
23009-1:2020/Amd.1. As correct handling is not guaranteed by legacy DASH clients
(including, for example, DVB LL-DASH clients), content authors <span class=modal-keyword>should</span> be careful
in relying on this information.

### Legacy Setup ### {#ll-legacy}

As low-latency DASH services have developed over time, this clause documents
legacy aspects compared to the DASH-IF [=Low-Latency Service Offering=] profile.
In such a legacy setup one or more of the following applies:

- The <b>ServiceDescription</b> element <span class=modal-keyword>may</span> not be present. In particular, the target
    latency <span class=modal-keyword>may</span> be absent, but <span class=modal-keyword>may</span> be provided by external means (for example by
    the application setting the value through an API).
- The <b>ProducerReferenceTime</b> element <span class=modal-keyword>may</span> not be present. In this case, the
    Period Start time is assumed to be used as the wall-clock time and the value
    of `@presentationTimeOffset` is assumed as the corresponding presentation
    time.
- The Segment durations for [=Low-Latency Segment Adaptation Set=]s <span class=modal-keyword>may</span> exceed
    the 50% target value.
- The [=Low-Latency Chunked Adaptation Set=]s <span class=modal-keyword>may</span> not conform to an Adaptation
    Set according to the DASH profile for CMAF content as defined in MPEG DASH.
- The <b>Resync</b> element <span class=modal-keyword>may</span> not be present.

### DVB Low-Latency DASH ### {#ll-dvb}

DVB Low-Latency DASH is documented in ETSI TS 103 285. As that specification was
completed prior to the DASH-IF specification, a few issues are documented here:

- Per TS 103 285 clause 10.20.3, DVB DASH clients consider themselves in scope
    where a <b>ServiceDescription</b> element contains a <b>Scope</b> element with
    `@schemeIdUri` set to `urn:dvb:dash:lowlatency:scope:2019`.
- The DVB-DASH Content Provider Guidelines (informative) recommend the use of
    `@duration` together with `$Number$`, whereas DASH-IF makes no such
    recommendation.
- DVB DASH does not mention the <b>Resync</b> element, but the presence of the element
    would not break a DVB-DASH client.
- DVB DASH signals Adaptation Sets used for low-latency purposes with an
    <b>EssentialProperty</b> or <b>SupplementalProperty</b> descriptor with `@schemeIdUri`
    set to `urn:dvb:dash:lowlatency:critical:2019` and `@value` set to `true`. If
    the <b>SupplementalProperty</b> descriptor is used, this does not impact regular
    low-latency DASH clients.

## Low-Latency Client ## {#ll-client}

For a DASH-IF [=Low-Latency DASH Client=] the following applies. The client <span class=modal-keyword>shall</span>
be able to consume content offered with the DASH-IF [=Low-Latency Service
Offering=] profile as defined in [[#ll-so-requirements]]. Specifically, this
includes:

- Support for media segments that contain more than one pair of `moof` and
    `mdat` boxes, where each `moof`/`mdat` pair <span class=modal-keyword>may</span> contain any number of ISO
    BMFF samples between 1 and the full segment duration inclusive.
- Support for playing two or more Adaptation Sets for which the Segments of one
    Adaptation Set do not align with the Segments of another (e.g. due to
    differing segment durations), or where the Segments of one Adaptation Set
    contain multiple `moof`/`mdat` pairs and the Segments of another have only a
    single `moof`/`mdat` pair.

## Guidelines for Low-Latency Service Offering (Informative) ## {#ll-guidelines}


### General ### {#ll-guidelines-general}

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

For <b>video</b>, to make each chunk displayable without waiting for more data, it
is important that all B-frames which <span class=modal-keyword>should</span> be displayed before the P-frame are
included in the chunk. As an example, hierarchical B-frames with the display
order `I0 B1 B2 B3 P4 | B5 B6 B7 P8 | ...` have a decode (send) order
`I0 P4 B1 B2 B3 | P8 B6 B5 B7 | ...`; the chunk <span class=modal-keyword>should</span> therefore be broken after
a multiple of 4–5 frames (160–200 ms for 25 Hz video). The general recommendation
is to place chunk boundaries so that all display times are before the earliest
display time of the next chunk.

For <b>audio</b>, the bitrate is relatively low (e.g. a 200 ms audio chunk at
64 kbps is ~1.6 kB), which <span class=modal-keyword>may</span> be too small to propagate through network or
receiver buffers. It <span class=modal-keyword>may</span> therefore make sense to use longer chunks (e.g. 0.5 s
for audio), or not apply chunking for audio and instead run at a shorter Segment
duration.

For <b>subtitles</b>, chunking is generally undesirable: an IMSC-1 sample is a TTML
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
ISO/IEC 14496-12. The information <span class=modal-keyword>may</span> be provided inband as part of the Segments
(in the `prft` box), in the MPD, or both.

### Service Description ### {#ll-service-description}

Annex K of ISO/IEC 23009-1 defines the DASH Service Description. In the DASH
model, the DASH client has significant control over the algorithms and user
perception for a DASH service (rate adaptation algorithm, buffer strategy, buffer
duration, and the resulting latency and channel access times). However, leaving
all decisions to the client <span class=modal-keyword>may</span> result in inconsistent behaviour across
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

The following is recommended: provide <b>Resync</b> signalling for each [=Low-Latency
Chunked Adaptation Set=] by adding a <b>Resync</b> element with the known parameters
(for example, on Adaptation Set level, `@dT` providing the maximum and nominal
duration of each chunk).

### Fast Switching Adaptation Sets ### {#ll-fast-switching}

Issue: Fast Switching Adaptation Set generation and signalling is for further
study. Reconciliation against Low-Latency CR r8/r9 (see
`rag/reports/reconcile-low-latency-r8-r9.md`) found no new normative construct:
both CRs specify resynchronization via the existing <b>Resync</b> element (see
[[#ll-resync]]) rather than a distinct "Addressable Resync Representation". The
ARR concept is retained only as a forward-looking term pending MPEG-DASH.

The following sequence illustrates fast tune-in (redrawn as Mermaid from the
source Word figure; see `Images/dashif-iop-v5-part4-draft-r1-images.md` for the
original figures pending triage).

<figure class="diagram" style="max-width:100%;overflow-x:auto;">
<pre class=mermaid>
%%{init: {'theme':'neutral','themeVariables':{'fontSize':'18px','fontFamily':'system-ui, Segoe UI, Arial, sans-serif','actorBkg':'#eef3f8','actorBorder':'#33475b','signalColor':'#333','noteBkgColor':'#fff7e6','noteBorderColor':'#c9a227'},'sequence':{'useMaxWidth':false,'mirrorActors':false,'messageFontSize':16,'actorFontSize':18}}}%%
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

#### Example: FFmpeg Configuration #### {#ll-ffmpeg-config}

The agreed Part 4 draft included an informative FFmpeg example for generating a
Low-Latency DASH representation. That text is restored here as historical
implementation guidance. FFmpeg option names and behavior evolve over time, so
implementers should verify the exact syntax against the current FFmpeg
documentation for the DASH muxer:
<a href="https://ffmpeg.org/ffmpeg-formats.html#dash-2">FFmpeg Formats Documentation — dash</a>.

FFmpeg provides settings that can be used to generate a low-latency DASH
representation, including DASH output, CMAF-oriented fragment formatting,
timeline/addressing control, producer reference time export, and a target
latency. A representative command-line skeleton derived from the source draft is
shown below:

<pre>
ffmpeg \
  -framerate ${INPUT_FPS} \
  -i ${INPUT} \
  -f lavfi -i sine \
  -pix_fmt yuv420p \
  -c:v ${VCODEC} -b:v:0 RBW[v,1] -b:v:1 RBW[v,2] ... \
  -map 0:v:0 -map 0:v:0 \
  -c:a ${ACODEC} -b:a RBW[a,1] -ac 2 \
  -map 1:a:0 \
  -use_timeline $TIMELINE \
  -utc_timing_url "UTCTime" \
  -format_options "movflags=cmaf" \
  -frag_type $DURATION \
  -adaptation_sets "id=0,seg_duration=SD[v],frag_duration=CD[v],streams=0,1 id=1,seg_duration=SD[a],frag_type=none,streams=NoSS" \
  -g:v 20 -keyint_min:v 20 -sc_threshold:v 0 -streaming $ASType -ldash $LLDASH -tune zerolatency \
  -export_side_data $PRFT \
  -write_prft $PRFT \
  -target_latency ${TargetLatency} \
  -color_primaries ${COLOR} -color_trc ${COLOR} -colorspace ${COLOR} \
  -f dash \
  ${HTTP_OPTS} \
  ${PROTO}://${SERVER}:${PORT}/${ID}/${ID}.mpd \
  ${TS_OUT_CMD}
</pre>

The source draft also mapped the main low-latency service parameters to FFmpeg
settings as follows:

- Low-latency presentation: `-ldash 1` together with `-streaming 1` for chunked
  operation.
- Target latency: `-target_latency &lt;TargetLatency&gt;` (in seconds).
- UTC timing source: `-utc_timing_url &lt;UTCTime&gt;`.
- Addressing scheme: `-use_template 1`, with `-use_timeline 0` for `@duration`
  based addressing or `-use_timeline 1` for `SegmentTimeline`, and media segment
  names based on `$RepresentationID$-$Number$.m4s` or
  `$RepresentationID$-$Time$.m4s`.
- Producer reference time: `-write_prft 1`.
- Nominal segment duration: `-seg_duration &lt;SD[i]&gt;` (noting in the draft that
  this could only be set globally).
- Nominal chunk duration: `-frag_duration &lt;CD[i]&gt;` (also noted in the draft as
  globally scoped).
- Fragment type: `-frag_type duration` for time-based chunking (other values:
  `none`, `every_frame`, `pframes`).
- Video representation bitrate ladder: `-c:v ${VCODEC} -b:v:0 ... -b:v:1 ...`.
- Audio representation settings: `-c:a ${ACODEC} -b:a RBW[a,1] -ac 2`.
- Adaptation sets: `-adaptation_sets "id=0,streams=v id=1,streams=a"` to group
  streams into separate adaptation sets.
- Format options for CMAF: `-format_options "movflags=cmaf"`.

Note: The above guidance reflects FFmpeg 9.0 syntax validated against the DASH
muxer. The historical command-line example in lines 388–411 uses shell variable
expansion and may require adjustment for the installed FFmpeg version. Key
differences from earlier FFmpeg releases:

- `-ldash`, `-streaming`, `-target_latency`, `-utc_timing_url`, `-write_prft`,
  `-use_template`, `-use_timeline`, `-seg_duration`, `-frag_duration`,
  `-frag_type`, and `-adaptation_sets` are all confirmed present in FFmpeg 9.0.
- `-export_side_data` (line 403) is a global codec option, not a DASH muxer
  option, and may not be required for producer reference time signalling when
  `-write_prft` is used.
- The `-frag_type` parameter accepts enumerated values (`none`, `every_frame`,
  `duration`, `pframes`), not arbitrary strings.

The draft also recorded limitations of the then-current FFmpeg support. In that
source snapshot, maximum latency, minimum latency, change lead time, reference
buffer duration, leap-second signalling, and MPD validity expiration events were
not supported directly by FFmpeg. Implementers should therefore treat FFmpeg as
one possible encoder/packager realization and verify which parts of the complete
[=Low-Latency Service Offering=] are realized in FFmpeg itself versus in
surrounding workflow components.

For a minimal validated low-latency DASH encoding example using FFmpeg 9.0 with
synthetic test sources, see the smoke-test script in the IOPv5 repository at
`rag-authoring-starter/tools/ll_dash_smoketest.bat` (or equivalent shell script
for non-Windows platforms).

#### FFmpeg Command-Line Examples #### {#ll-ffmpeg-examples}

The following examples demonstrate different FFmpeg configurations for low-latency
DASH, validated against FFmpeg 9.0. All examples use synthetic test sources for
reproducibility.

**Example 1: Basic Low-Latency Chunked DASH with $Number$ addressing**

This example creates a low-latency DASH stream with 1.5-second segments, 0.5-second
chunks, and simple `$Number$` addressing:

<pre>
ffmpeg -hide_banner -y \
  -f lavfi -i "testsrc2=size=1280x720:rate=25" \
  -f lavfi -i "sine=frequency=1000:sample_rate=48000" \
  -t 10 \
  -c:v libx264 -tune zerolatency -g 25 -keyint_min 25 -sc_threshold 0 \
  -b:v 2000k -maxrate 2200k -bufsize 4000k -pix_fmt yuv420p \
  -c:a aac -b:a 128k -ac 2 \
  -use_template 1 -use_timeline 0 \
  -utc_timing_url "https://time.akamai.com/?iso" \
  -format_options "movflags=cmaf" \
  -adaptation_sets "id=0,streams=v id=1,streams=a" \
  -seg_duration 1.5 \
  -frag_duration 0.5 \
  -frag_type duration \
  -streaming 1 \
  -ldash 1 \
  -write_prft 1 \
  -target_latency 3.5 \
  -f dash output.mpd
</pre>

**Example 2: Low-Latency DASH with SegmentTimeline ($Time$ addressing)**

This example uses `SegmentTimeline` for more precise timing control:

<pre>
ffmpeg -hide_banner -y \
  -f lavfi -i "testsrc2=size=1280x720:rate=30" \
  -f lavfi -i "sine=frequency=440:sample_rate=48000" \
  -t 10 \
  -c:v libx264 -tune zerolatency -g 30 -keyint_min 30 -sc_threshold 0 \
  -b:v 1500k -pix_fmt yuv420p \
  -c:a aac -b:a 96k -ac 2 \
  -use_template 1 -use_timeline 1 \
  -utc_timing_url "https://time.akamai.com/?iso" \
  -format_options "movflags=cmaf" \
  -adaptation_sets "id=0,streams=v id=1,streams=a" \
  -seg_duration 2.0 \
  -frag_duration 0.5 \
  -frag_type duration \
  -streaming 1 \
  -ldash 1 \
  -write_prft 1 \
  -target_latency 4.0 \
  -f dash output_timeline.mpd
</pre>

**Example 3: Multi-Bitrate ABR Ladder with Low-Latency**

This example creates multiple video representations for adaptive bitrate streaming:

<pre>
ffmpeg -hide_banner -y \
  -f lavfi -i "testsrc2=size=1920x1080:rate=25" \
  -f lavfi -i "sine=frequency=1000:sample_rate=48000" \
  -t 10 \
  -map 0:v -map 0:v -map 0:v -map 1:a \
  -c:v:0 libx264 -b:v:0 3000k -s:v:0 1920x1080 \
  -c:v:1 libx264 -b:v:1 1500k -s:v:1 1280x720 \
  -c:v:2 libx264 -b:v:2 800k -s:v:2 854x480 \
  -tune:v zerolatency -g:v 25 -keyint_min:v 25 -sc_threshold:v 0 -pix_fmt yuv420p \
  -c:a aac -b:a 128k -ac 2 \
  -use_template 1 -use_timeline 1 \
  -utc_timing_url "https://time.akamai.com/?iso" \
  -format_options "movflags=cmaf" \
  -adaptation_sets "id=0,streams=0,1,2 id=1,streams=3" \
  -seg_duration 2.0 \
  -frag_duration 0.5 \
  -frag_type duration \
  -streaming 1 \
  -ldash 1 \
  -write_prft 1 \
  -target_latency 4.0 \
  -f dash output_abr.mpd
</pre>

**Example 4: Low-Latency Segment Adaptation Set (no chunking)**

This example creates short segments without CMAF chunking, suitable for simpler
client implementations:

<pre>
ffmpeg -hide_banner -y \
  -f lavfi -i "testsrc2=size=1280x720:rate=25" \
  -f lavfi -i "sine=frequency=1000:sample_rate=48000" \
  -t 10 \
  -c:v libx264 -tune zerolatency -g 25 -keyint_min 25 -sc_threshold 0 \
  -b:v 2000k -pix_fmt yuv420p \
  -c:a aac -b:a 128k -ac 2 \
  -use_template 1 -use_timeline 1 \
  -utc_timing_url "https://time.akamai.com/?iso" \
  -format_options "movflags=cmaf" \
  -adaptation_sets "id=0,streams=v id=1,streams=a" \
  -seg_duration 1.0 \
  -frag_type none \
  -streaming 0 \
  -ldash 1 \
  -write_prft 1 \
  -target_latency 3.0 \
  -f dash output_segments.mpd
</pre>

**Example 5: Ultra-Low-Latency with Per-Frame Chunking**

This example demonstrates the most aggressive chunking strategy (experimental):

<pre>
ffmpeg -hide_banner -y \
  -f lavfi -i "testsrc2=size=640x360:rate=25" \
  -f lavfi -i "sine=frequency=1000:sample_rate=48000" \
  -t 5 \
  -c:v libx264 -tune zerolatency -g 25 -keyint_min 25 -sc_threshold 0 \
  -b:v 800k -pix_fmt yuv420p \
  -c:a aac -b:a 64k -ac 2 \
  -use_template 1 -use_timeline 1 \
  -utc_timing_url "https://time.akamai.com/?iso" \
  -format_options "movflags=cmaf" \
  -adaptation_sets "id=0,streams=v id=1,streams=a" \
  -seg_duration 1.0 \
  -frag_type every_frame \
  -streaming 1 \
  -ldash 1 \
  -write_prft 1 \
  -target_latency 1.5 \
  -f dash output_ultra_low.mpd
</pre>

Note: Per-frame chunking (`-frag_type every_frame`) creates very small chunks and
significantly increases HTTP overhead. It should only be used for ultra-low-latency
scenarios (< 2 seconds target latency) where the trade-off is acceptable.

**Example 6: Custom Segment and Chunk Durations per Adaptation Set**

This example shows different timing configurations for video and audio:

<pre>
ffmpeg -hide_banner -y \
  -f lavfi -i "testsrc2=size=1280x720:rate=25" \
  -f lavfi -i "sine=frequency=1000:sample_rate=48000" \
  -t 10 \
  -c:v libx264 -tune zerolatency -g 25 -keyint_min 25 -sc_threshold 0 \
  -b:v 2000k -pix_fmt yuv420p \
  -c:a aac -b:a 128k -ac 2 \
  -use_template 1 -use_timeline 1 \
  -utc_timing_url "https://time.akamai.com/?iso" \
  -format_options "movflags=cmaf" \
  -adaptation_sets "id=0,seg_duration=1.5,frag_duration=0.5,streams=v id=1,seg_duration=2.0,frag_type=none,streams=a" \
  -streaming 1 \
  -ldash 1 \
  -write_prft 1 \
  -target_latency 3.5 \
  -f dash output_custom.mpd
</pre>

Note: In FFmpeg 9.0, per-adaptation-set `seg_duration` and `frag_duration` can be
specified within the `-adaptation_sets` parameter, overriding the global values.

**Key Parameter Trade-offs:**

- **Segment Duration (`-seg_duration`)**: Shorter segments reduce latency but
  increase manifest size and HTTP request overhead. Recommended: 1–2 seconds for
  low-latency, 0.5–1 second for ultra-low-latency.
- **Chunk Duration (`-frag_duration`)**: Smaller chunks enable earlier playback
  start but increase overhead. Recommended: 0.5–1.0 seconds for video, 0.5–2.0
  seconds for audio.
- **Fragment Type (`-frag_type`)**: `duration` provides predictable timing,
  `every_frame` minimizes latency but maximizes overhead, `none` disables chunking.
- **Target Latency (`-target_latency`)**: Should be 2–3× the segment duration to
  allow for network jitter and buffering.
- **Streaming Mode (`-streaming`)**: Set to `1` for chunked transfer encoding
  (required for [=Low-Latency Chunked Adaptation Set=]s), `0` for complete segments.

#### livesim2 Low-Latency Configuration #### {#ll-livesim2-config}

The DASH-IF livesim2 tool provides a live DASH simulator that can be configured
for low-latency operation. livesim2 is available at
<a href="https://github.com/Dash-Industry-Forum/livesim2">github.com/Dash-Industry-Forum/livesim2</a>
and is deployed at <a href="https://livesim2.dashif.org">livesim2.dashif.org</a>.

**Basic Low-Latency Configuration**

livesim2 supports low-latency DASH through URL parameters. The general URL pattern
for low-latency streams is:

<pre>
https://livesim2.dashif.org/livesim2/chunkdur_&lt;CD&gt;/ato_&lt;ATO&gt;/ltgt_&lt;TL&gt;/&lt;content&gt;/Manifest.mpd
</pre>

Where:
- `chunkdur_<CD>`: CMAF chunk duration in seconds (e.g., `chunkdur_0.5` for 500ms chunks)
- `ato_<ATO>`: Availability Time Offset in seconds (e.g., `ato_7` for 7 seconds)
- `ltgt_<TL>`: Low-latency target latency in seconds (e.g., `ltgt_3.5` for 3.5s target)
- `<content>`: The base content path (e.g., `testpic_2s` for 2-second segments)

**Example 1: Basic Low-Latency Stream (3.5s target latency)**

<pre>
https://livesim2.dashif.org/livesim2/chunkdur_0.5/ato_7/ltgt_3.5/testpic_2s/Manifest.mpd
</pre>

This configuration provides:
- 2-second segments (`testpic_2s`)
- 0.5-second CMAF chunks (`chunkdur_0.5`)
- 7-second availability time offset (`ato_7`)
- 3.5-second target latency signalled in ServiceDescription (`ltgt_3.5`)

**Example 2: Ultra-Low-Latency Stream (2s target latency)**

<pre>
https://livesim2.dashif.org/livesim2/chunkdur_0.2/ato_4/ltgt_2.0/testpic_2s/Manifest.mpd
</pre>

This configuration provides:
- 2-second segments
- 0.2-second (200ms) CMAF chunks for ultra-low latency
- 4-second availability time offset
- 2.0-second target latency

**Example 3: Low-Latency with SegmentTimeline**

<pre>
https://livesim2.dashif.org/livesim2/segtimeline_1/chunkdur_0.5/ato_7/ltgt_4.0/testpic_2s/Manifest.mpd
</pre>

This configuration adds:
- `segtimeline_1`: Enables SegmentTimeline instead of `@duration`
- Provides more precise timing information

**Example 4: Low-Latency with Multiple Periods**

<pre>
https://livesim2.dashif.org/livesim2/periods_60/chunkdur_0.5/ato_7/ltgt_3.5/testpic_2s/Manifest.mpd
</pre>

This configuration adds:
- `periods_60`: Creates a new Period every 60 seconds
- Useful for testing Period transitions in low-latency scenarios

**Example 5: Low-Latency with UTC Timing**

<pre>
https://livesim2.dashif.org/livesim2/utc_direct/chunkdur_0.5/ato_7/ltgt_3.5/testpic_2s/Manifest.mpd
</pre>

This configuration adds:
- `utc_direct`: Includes UTCTiming element with direct time server
- Required for proper low-latency synchronization

**Example 6: Low-Latency Multi-Period with Continuous Timeline**

<pre>
https://livesim2.dashif.org/livesim2/continuous_1/periods_60/chunkdur_0.5/ato_7/ltgt_3.5/testpic_2s/Manifest.mpd
</pre>

This configuration adds:
- `continuous_1`: Maintains continuous timeline across Period boundaries
- Useful for testing seamless Period transitions

**Testing with dash.js Reference Player**

All livesim2 URLs can be tested directly in the dash.js reference player:

<pre>
https://reference.dashif.org/dash.js/latest/samples/dash-if-reference-player/index.html
</pre>

To test a low-latency stream:
1. Open the dash.js reference player URL above
2. Paste any of the livesim2 MPD URLs into the "Custom DASH URL" field
3. Click "Load"
4. Enable "Low Latency Mode" in the player settings
5. Monitor the latency metrics in the player's debug panel

**Direct dash.js Links for Testing**

The following links open the dash.js reference player with pre-configured low-latency
streams:

- <a href="https://reference.dashif.org/dash.js/latest/samples/dash-if-reference-player/index.html?url=https://livesim2.dashif.org/livesim2/chunkdur_0.5/ato_7/ltgt_3.5/testpic_2s/Manifest.mpd&lowLatencyMode=true">Basic Low-Latency (3.5s target)</a>
- <a href="https://reference.dashif.org/dash.js/latest/samples/dash-if-reference-player/index.html?url=https://livesim2.dashif.org/livesim2/chunkdur_0.2/ato_4/ltgt_2.0/testpic_2s/Manifest.mpd&lowLatencyMode=true">Ultra-Low-Latency (2s target)</a>
- <a href="https://reference.dashif.org/dash.js/latest/samples/dash-if-reference-player/index.html?url=https://livesim2.dashif.org/livesim2/segtimeline_1/chunkdur_0.5/ato_7/ltgt_4.0/testpic_2s/Manifest.mpd&lowLatencyMode=true">Low-Latency with SegmentTimeline</a>
- <a href="https://reference.dashif.org/dash.js/latest/samples/dash-if-reference-player/index.html?url=https://livesim2.dashif.org/livesim2/utc_direct/chunkdur_0.5/ato_7/ltgt_3.5/testpic_2s/Manifest.mpd&lowLatencyMode=true">Low-Latency with UTC Timing</a>

**Key livesim2 Parameters for Low-Latency**

- `chunkdur_<dur>`: CMAF chunk duration (0.2–1.0 seconds typical)
- `ato_<offset>`: Availability Time Offset in seconds
- `ltgt_<latency>`: Target latency signalled in ServiceDescription
- `segtimeline_1`: Enable SegmentTimeline
- `utc_direct`: Add UTCTiming element
- `continuous_1`: Continuous timeline across Periods
- `periods_<dur>`: Period duration in seconds
- `timeoffset_<offset>`: Start time offset for testing catch-up

**Recommended Configurations by Use Case**

- **Standard Low-Latency (3–5s)**: `chunkdur_0.5/ato_7/ltgt_3.5`
- **Ultra-Low-Latency (1–2s)**: `chunkdur_0.2/ato_4/ltgt_2.0`
- **Broadcast-Style (5–10s)**: `chunkdur_1.0/ato_10/ltgt_7.0`

Note: The availability time offset (`ato`) should be set to approximately 2× the
target latency to provide sufficient buffer for network jitter and client-side
buffering.

### MPD Generator and Packager Operation ### {#ll-packager}

This clause introduces a reference DASH packager for low-latency that also adds a
period boundary at indicated times. The implementation is an example only; other
approaches <span class=modal-keyword>may</span> be used. The basic operation of the DASH packager is as follows:

- The DASH packager creates an initial MPD based on the configuration
    information in [[#ll-config-params]].
- The DASH packager acts as a slave to the ABR encoder and incoming data formats.
- The DASH packager formats and generates MPDs dynamically and ingests the
    Segments into the CDN.
- The DASH packager ensures the Segment availability times in the MPD are correct
    at the origin.

Two backward-compatible reference profiles are described in the source:
<b>Simple Live</b> (using `$Number$` and `@duration` for duration signalling, with
`@minimumUpdatePeriod` or inband MPD validity expirations) and <b>Main Live</b>
(using `$Time$` and <b>SegmentTimeline</b>). In both, each CMAF fragment generates one
DASH segment and each CMAF chunk is offered as an HTTP chunk.

Issue: A <b>Broadcast TV Profile</b> extension is explicitly deferred to a future
version in both Low-Latency CR r8 (clause 6.6.4.4) and r9 (clause 9.X.6.4.4); no
normative text exists to migrate yet. Tracked as future work (see
`rag/reports/reconcile-low-latency-r8-r9.md`).

## Client Implementation Guidelines (Informative) ## {#ll-client-guidelines}


### General ### {#ll-client-guidelines-general}

The following <span class=modal-keyword>should</span> be considered for a low-latency client implementation:

- It <span class=modal-keyword>should</span> be configurable regarding using the low-latency mode and which
    configuration to use (e.g. how aggressive it is in latency maintenance).
- Updates and considerations in the ABR logic and throughput estimation apply
    (see [[#ll-bandwidth]]).
- Start-up operations <span class=modal-keyword>should</span> be considered to maintain latency and manage
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
