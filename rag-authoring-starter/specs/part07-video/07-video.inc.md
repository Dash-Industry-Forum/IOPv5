<!--
  Part 7: Video.
  Initial Bikeshed/Markdown shell following the IOPv5 authoring convention.
  Source grounding / migration target: iop-docs-overview / Part 2 media mapping placeholders.
  Normative content in this revision is migrated from:
  - Dash-Industry-Forum/DASH-IF-IOP branch v5-old-draft, 80-Codecs.inc.md
    (H.264/AVC, H.265/HEVC, decoder configuration, bitstream switching clauses)
  - Dash-Industry-Forum/DASH-IF-IOP branch v5-old-draft, 27-AdaptationSets.inc.md
    (video adaptation set constraints)
  HDR, UHD 4K, Dolby Vision dual-stream, and VP9 clauses from the same source
  file remain to be migrated; see the Open Issues table below.
-->

# Scope # {#scope}

This document specifies DASH-IF IOP v5 Part 7: **Video**. Video interoperability points, CMAF media profiles, codec signalling, DASH MPD parameters, and video-specific constraints.

Services <span class=modal-keyword>shall</span> use only the media codecs described in this part, in conformance with the requirements defined here. Clients <span class=modal-keyword>may</span> support any set of codecs described in this part and <span class=modal-keyword>shall not</span> attempt to play back Representations for which they do not have codec support.
# References # {#doc-references}

The following referenced documents are necessary for the application of this
part:

- ISO/IEC 23009-1 [[!MPEGDASH]].
- ISO/IEC 23000-19 [[!MPEGCMAF]].
- ISO/IEC 14496-15, *Carriage of network abstraction layer (NAL) unit structured video in the ISO base media file format*.
- ITU-T Rec. H.264 / ISO/IEC 14496-10, *Advanced Video Coding*.
- ITU-T Rec. H.265 / ISO/IEC 23008-2, *High Efficiency Video Coding*.
- DASH-IF IOP v5 Part 2, *Core Principles and CMAF Mapping*.
- DASH-IF IOP v5 Part 12, *Conformance and Reference Tools*.

# Terms and Definitions # {#terms}

Terms and definitions are inherited from ISO/IEC 23009-1, ISO/IEC 23000-19, and
Part 2 unless defined in this part.

A <dfn export>video adaptation set</dfn> is an Adaptation Set that contains visual information for display to the user, identified by `@mimeType="video/mp4"`.

# Video Codecs # {#codecs}

## H.264 (AVC) ## {#codecs-h264}

The H.264 (AVC) codec <span class=modal-keyword>may</span> be used by services for video adaptation sets. Clients <span class=modal-keyword>should</span> support this codec.

For Representations up to 1280x720p resolution and up to 30 fps, the H.264 (AVC) Progressive High Profile Level 3.1 decoder <span class=modal-keyword>shall</span> be used.

For Representations up to 1920x1080p resolution and up to 30 fps, the H.264 (AVC) Progressive High Profile Level 4.0 decoder <span class=modal-keyword>shall</span> be used.

The encapsulation of H.264 data in DASH containers <span class=modal-keyword>shall</span> conform to ISO/IEC 14496-15.

Clients <span class=modal-keyword>shall</span> support SPS/PPS storage both in the Initialization Segment (sample entry `avc1`) and inband storage (sample entry `avc3`). Services <span class=modal-keyword>may</span> use either form.

Note: Use of `avc3` is one of the factors that enables [[#bitstream-switching-h264-h265|bitstream switching]].
<table class="data">
  <caption>Example `@codecs` strings for H.264 (AVC).</caption>
  <thead><tr><th>Profile<th>Level<th>`@codecs`
  <tbody>
    <tr><td rowspan="2">H.264 (AVC) Progressive High Profile<td>3.1<td>`avc1.64Y01F` / `avc3.64Y01F`
    <tr><td>4.0<td>`avc1.64Y028` / `avc3.64Y028`
</table>

Note: Other `@codecs` strings may also be compatible (a higher level decoder can typically decode content intended for a lower level decoder).

## H.265 (HEVC) ## {#codecs-h265}

The H.265 (HEVC) codec <span class=modal-keyword>may</span> be used by services for video adaptation sets.

For Representations up to 1280x720p at up to 30 fps, the HEVC Main Profile Main Tier Level 3.1 decoder <span class=modal-keyword>shall</span> be used.

For Representations up to 2048x1080 at up to 60 fps at 8-bit frame depth, the HEVC Main Profile Main Tier Level 4.1 decoder <span class=modal-keyword>shall</span> be used.

For Representations up to 2048x1080 at up to 60 fps at 10-bit frame depth, the HEVC Main10 Profile Main Tier Level 4.1 decoder <span class=modal-keyword>shall</span> be used.

The encapsulation of H.265 data in DASH containers <span class=modal-keyword>shall</span> conform to ISO/IEC 14496-15.

Clients <span class=modal-keyword>shall</span> support VPS/SPS/PPS storage both in the Initialization Segment (sample entry `hvc1`) and inband storage (sample entry `hev1`). Services <span class=modal-keyword>may</span> use either form.

Note: Use of `hev1` is one of the factors that enables [[#bitstream-switching-h264-h265|bitstream switching]].
<table class="data">
  <caption>Example `@codecs` strings for H.265 (HEVC).</caption>
  <thead><tr><th>Profile<th>Level<th>`@codecs`
  <tbody>
    <tr><td rowspan="2">HEVC Main<td>3.1<td>`hev1.1.2.L93.B0` / `hvc1.1.2.L93.B0`
    <tr><td>4.1<td>`hev1.1.2.L123.B0` / `hvc1.1.2.L123.B0`
    <tr><td>HEVC Main-10<td>4.1<td>`hev1.2.4.L123.B0` / `hvc1.2.4.L123.B0`
</table>

## Decoder configuration with H.264 and H.265 ## {#codecs-decoder-setup-h264-h265}

This clause applies only to video adaptation sets that use H.264 or H.265.

All Initialization Segments in the same video adaptation set <span class=modal-keyword>shall</span> use the same sample description (i.e. no mixing of `avc1` and `avc3` is allowed).

In Representations using `avc1` or `hvc1` sample description:

* All decoding parameter sets referenced by NALs <span class=modal-keyword>shall</span> be indexed to that track's sample description table and decoder configuration record in the `avcC` or `hvcC` box contained in its Initialization Segment.
* Edit lists <span class=modal-keyword>may</span> be present.

In Representations using `avc3` or `hev1` sample description:

* All decoding parameter sets referenced by NALs <span class=modal-keyword>shall</span> be indexed to a Sequence Parameter NAL (SPS) and Picture Parameter NAL (PPS) stored prior to the first video sample in the same Media Segment.
* SPS and PPS stored in each Media Segment <span class=modal-keyword>shall</span> be used for decoding and display scaling.
* Every Initialization Segment <span class=modal-keyword>shall</span> include an `avcC` or `hvcC` box that <span class=modal-keyword>shall</span> include SPS and PPS NALs that equal the highest Tier, Profile, Level and vertical/horizontal sample count of any SPS in the Representation. HEVC Decoder Configuration Records <span class=modal-keyword>shall</span> also include a VPS NAL.
* SPS and PPS stored in the Initialization Segments <span class=modal-keyword>shall</span> be used only for decoder and display initialization.
* Edit lists <span class=modal-keyword>may</span> be present if using indexed addressing. Edit lists <span class=modal-keyword>shall not</span> be present when using any other addressing mode.

## Bitstream switching with H.264 and H.265 ## {#bitstream-switching-h264-h265}

This clause applies only to bitstream-switching adaptation sets that use H.264 or H.265.

All Representations <span class=modal-keyword>shall</span> be encoded using the `avc3` or `hev1` sample description.

The first presented sample's composition time <span class=modal-keyword>shall</span> equal the first decoded sample's decode time, which equals the `baseMediaDecodeTime` in the Track Fragment Decode Time Box (`tfdt`).

Note: This requires the use of negative composition offsets in a v1 Track Run Box (`trun`) for video samples, otherwise video sample reordering will result in a delay of video relative to audio.

# Video Adaptation Set Constraints # {#video-constraints}

All Representations in the same video adaptation set <span class=modal-keyword>shall</span> be alternative encodings of the same source content, encoded such that switching between them does not produce visual glitches due to picture size or aspect ratio differences.

The encoded picture <span class=modal-keyword>shall</span> only contain the active video area, so that clients can frame the height and width of the encoded video to the size and shape of their currently selected display area without extraneous padding in the decoded video, such as letterbox or pillarbox bars.

Representations in the same video adaptation set <span class=modal-keyword>shall not</span> differ in any of the following parameters:

* Color Primaries
* Transfer Characteristics
* Matrix Coefficients

If different video adaptation sets differ in any of the above parameters, these parameters <span class=modal-keyword>should</span> be signaled in the MPD on the adaptation set level by a Supplemental Property Descriptor or an Essential Property Descriptor with `@schemeIdUri="urn:mpeg:mpegB:cicp:<Parameter>"`, with `<Parameter>` being one of `ColourPrimaries`, `TransferCharacteristics`, or `MatrixCoefficients`.

In any video adaptation set, the following <span class=modal-keyword>shall</span> be present:

* `AdaptationSet@par` (the display aspect ratio)
* `Representation@sar` (the sample aspect ratio)
* Either `Representation@width` or `AdaptationSet@width` (but not both)
* Either `Representation@height` or `AdaptationSet@height` (but not both)
* Either `Representation@frameRate` or `AdaptationSet@frameRate` (but not both)

Note: `@width` and `@height` indicate the number of encoded pixels. `@par` indicates the final intended display aspect ratio and `@sar` is effectively the ratio of aspect ratios (ratio of `@width x @height` to `@par`). The formula is: display aspect ratio = picture aspect ratio / sample aspect ratio.

<div class="example">
Given a coded picture of 720x576 pixels with an intended display aspect ratio of 16:9:

* `@width=720`
* `@height=576`
* `@par=16:9`
* `@sar=45:64` (720x576 is 5:4, which gives `@sar=5:4/16:9=45:64`)

</div>

In any video adaptation set, the following <span class=modal-keyword>should not</span> be present and <span class=modal-keyword>shall</span> be ignored by clients if present, as these values are trivial to determine at runtime:

* `AdaptationSet@minWidth`, `@maxWidth`, `@minHeight`, `@maxHeight`, `@minFrameRate`, `@maxFrameRate`

`@scanType` <span class=modal-keyword>should not</span> be present and if present <span class=modal-keyword>shall</span> have the value `progressive`. Non-progressive video is not interoperable.

# Requirements and Recommendations # {#requirements}

Issue: The above clauses migrate the H.264/H.265 codec, decoder configuration,
bitstream-switching, and video-adaptation-set constraints from
Dash-Industry-Forum/DASH-IF-IOP branch v5-old-draft, 80-Codecs.inc.md and
27-AdaptationSets.inc.md. Remaining migration work: thumbnail image tile
adaptation sets (candidate for Part 11), UHD HEVC 4K, HEVC HDR PQ10 (including
SMPTE 2094-10/2094-40 and TS 103.433 dynamic metadata), UHD Dual-Stream (Dolby
Vision), and VP9. [GROUNDED_BY=Dash-Industry-Forum/DASH-IF-IOP@v5-old-draft:80-Codecs.inc.md]

# Open Issues and Work Items # {#open-issues}

<table class="data">
  <caption>Part 7 open issues and topics to progress.</caption>
  <thead><tr><th>Topic<th>Status<th>Next action
  <tbody>
    <tr><td>Source migration<td>In progress<td>H.264/H.265 codec, decoder configuration, bitstream switching, and video adaptation set constraints migrated from DASH-IF-IOP v5-old-draft. HDR/UHD/Dolby Vision/VP9 clauses remain to be migrated and reconciled with current MPEG-DASH/CMAF editions.
    <tr><td>Cross-part alignment<td>Open<td>Align terminology and references with Parts 1, 2, and 12.
    <tr><td>Conformance mapping<td>Open<td>Identify validator/test-asset/reference-player expectations and link them to Part 12.
</table>

# Change History # {#change-history}

<table class="data">
  <caption>Part 7 change history.</caption>
  <thead><tr><th>Version<th>Date<th>Change
  <tbody>
    <tr><td>0.1<td>Initial<td>Created initial Bikeshed/Markdown shell for Part 7.
    <tr><td>0.2<td>Migration<td>Migrated H.264/H.265 codec and video adaptation set constraints from DASH-IF-IOP v5-old-draft.
</table>

