<!--
  Part 7: Video.
  Restructured 2026-07-28:
  - Added DASH-IF Codec Registry section (dashif.org/codecs, GitHub Codecs repo)
  - H.264/AVC and H.265/HEVC codec requirements retained as normative baseline
  - HDR, UHD 4K, Dolby Vision, VP9 moved to informative Annex A
  - Video adaptation set constraints retained
  Source grounding:
  - Dash-Industry-Forum/DASH-IF-IOP branch v5-old-draft, 80-Codecs.inc.md
  - Dash-Industry-Forum/DASH-IF-IOP branch v5-old-draft, 27-AdaptationSets.inc.md
  - https://dashif.org/codecs/introduction/
  - https://github.com/Dash-Industry-Forum/Codecs
-->

# Scope # {#scope}

This document specifies DASH-IF IOP v5 Part 7: <b>Video</b>. It defines video
interoperability points, CMAF media profiles, codec signalling, DASH MPD
parameters, and video-specific constraints for DASH-IF compliant services and
clients.

The primary normative reference for supported video codecs is the
<b>DASH-IF Codec Registry</b> at [https://dashif.org/codecs/](https://dashif.org/codecs/).
This part defines the general requirements for video adaptation sets and provides
normative baseline requirements for the most widely deployed codecs (H.264/AVC
and H.265/HEVC). For the complete and up-to-date list of registered codecs,
services and clients <span class=modal-keyword>shall</span> consult the DASH-IF Codec Registry.

Services <span class=modal-keyword>shall</span> use only media codecs that are registered in the DASH-IF Codec
Registry or explicitly defined in this part. Clients <span class=modal-keyword>may</span> support any set of
codecs registered in the DASH-IF Codec Registry and <span class=modal-keyword>shall not</span> attempt to play
back Representations for which they do not have codec support.

Note: ETSI TS 103 285 [[DVBDASH]] (the "DVB-DASH" profile) defines its own
mandatory and optional video codec set (H.264/AVC, HEVC, VVC, and AVS3),
profile/level constraints, and HDR/HFR signalling that is narrower than the
DASH-IF Codec Registry. Alignment notes with DVB-DASH are provided in the
relevant clauses below.

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
- DASH-IF Codec Registry, *https://dashif.org/codecs/introduction/* [[DASHIF-CODECS]].

# Terms and Definitions # {#terms}

Terms and definitions are inherited from ISO/IEC 23009-1, ISO/IEC 23000-19, and
Part 2 unless defined in this part.

: <dfn export>video adaptation set</dfn>
:: An Adaptation Set that contains visual information for display to the user,
    identified by `@mimeType="video/mp4"`.

: <dfn export>DASH-IF Codec Registry</dfn>
:: The DASH-IF maintained registry of video and audio codecs supported for use
    in DASH-IF compliant services, available at
    [https://dashif.org/codecs/](https://dashif.org/codecs/).

# DASH-IF Codec Registry # {#codec-registry}

## Overview ## {#codec-registry-overview}

DASH-IF maintains a <b>Codec Registry</b> that serves as the authoritative and
continuously updated reference for codecs supported in DASH-IF compliant
services. The registry is available at:

- <b>Web interface:</b> [https://dashif.org/codecs/introduction/](https://dashif.org/codecs/introduction/)
- <b>Source data:</b> [https://github.com/Dash-Industry-Forum/Codecs](https://github.com/Dash-Industry-Forum/Codecs)

The registry provides:

- A structured list of supported video and audio codecs with their DASH MPD
    `@codecs` strings, CMAF profiles, and interoperability notes.
- Codec-specific requirements for `@mimeType`, `@codecs`, sample entry types,
    and decoder configuration.
- Guidance on codec selection for different service scenarios (on-demand, live,
    low-latency, HDR, etc.).
- A machine-readable dataset that can be integrated into validator tools and
    reference implementations.

## Using the Codec Registry ## {#codec-registry-usage}

Services <span class=modal-keyword>shall</span> use `@codecs` strings that are registered in the DASH-IF Codec
Registry for the codec and profile being used. The registry defines the
canonical `@codecs` string format for each supported codec.

Clients <span class=modal-keyword>should</span> use the DASH-IF Codec Registry to determine which codecs they
are expected to support for a given service scenario. The registry indicates
which codecs are mandatory, recommended, or optional for different client
categories.

Note: The DASH-IF Codec Registry is a living document that is updated as new
codecs are registered and existing codec requirements are refined. Services and
clients <span class=modal-keyword>should</span> consult the current version of the registry rather than relying
solely on the static codec tables in this part.

## Codec Registration Process ## {#codec-registry-process}

New codecs <span class=modal-keyword>may</span> be proposed for registration via the GitHub repository at
[https://github.com/Dash-Industry-Forum/Codecs](https://github.com/Dash-Industry-Forum/Codecs).
The registration process requires:

- A defined `@codecs` string format following [[!MPEGDASH]] conventions.
- A CMAF media profile or equivalent container format specification.
- Demonstrated interoperability with at least one DASH client and one DASH
    packager.
- Alignment with the DASH-IF IOP v5 framework.

# Video Codecs # {#codecs}

## General ## {#codecs-general}

The following clauses define normative baseline requirements for the most widely
deployed video codecs. For additional codecs, consult the
[[DASHIF-CODECS|DASH-IF Codec Registry]].

## H.264 (AVC) ## {#codecs-h264}

The H.264 (AVC) codec <span class=modal-keyword>may</span> be used by services for video adaptation sets. Clients
<span class=modal-keyword>should</span> support this codec.

For Representations up to 1280x720p resolution and up to 30 fps, the H.264
(AVC) Progressive High Profile Level 3.1 decoder <span class=modal-keyword>shall</span> be used.

For Representations up to 1920x1080p resolution and up to 30 fps, the H.264
(AVC) Progressive High Profile Level 4.0 decoder <span class=modal-keyword>shall</span> be used.

The encapsulation of H.264 data in DASH containers <span class=modal-keyword>shall</span> conform to
ISO/IEC 14496-15.

Clients <span class=modal-keyword>shall</span> support SPS/PPS storage both in the Initialization Segment
(sample entry `avc1`) and inband storage (sample entry `avc3`). Services
<span class=modal-keyword>may</span> use either form.

Note: Use of `avc3` is one of the factors that enables
[[#bitstream-switching-h264-h265|bitstream switching]].

<table class="data">
  <caption>Example `@codecs` strings for H.264 (AVC).</caption>
  <thead><tr><th>Profile<th>Level<th>`@codecs`
  <tbody>
    <tr><td rowspan="2">H.264 (AVC) Progressive High Profile<td>3.1<td>`avc1.64Y01F` / `avc3.64Y01F`
    <tr><td>4.0<td>`avc1.64Y028` / `avc3.64Y028`
</table>

Note: Other `@codecs` strings may also be compatible (a higher level decoder
can typically decode content intended for a lower level decoder). See the
[[DASHIF-CODECS|DASH-IF Codec Registry]] for the complete list of registered
H.264 `@codecs` strings.

Note: DVB-DASH [[DVBDASH]] mandates support for H.264/AVC High Profile up to
Level 4.0 (1920x1080p) for its base video profile, consistent with the H.264
Level 4.0 requirement in this clause. Services relying only on Level 3.1 for
DVB-DASH compatibility should verify against the current DVB-DASH Content
Provider Guidelines, as DVB-DASH devices are not required to support
resolutions or levels beyond those mandated there.

## H.265 (HEVC) ## {#codecs-h265}

The H.265 (HEVC) codec <span class=modal-keyword>may</span> be used by services for video adaptation sets.

For Representations up to 1280x720p at up to 30 fps, the HEVC Main Profile
Main Tier Level 3.1 decoder <span class=modal-keyword>shall</span> be used.

For Representations up to 2048x1080 at up to 60 fps at 8-bit frame depth, the
HEVC Main Profile Main Tier Level 4.1 decoder <span class=modal-keyword>shall</span> be used.

For Representations up to 2048x1080 at up to 60 fps at 10-bit frame depth, the
HEVC Main10 Profile Main Tier Level 4.1 decoder <span class=modal-keyword>shall</span> be used.

The encapsulation of H.265 data in DASH containers <span class=modal-keyword>shall</span> conform to
ISO/IEC 14496-15.

Clients <span class=modal-keyword>shall</span> support VPS/SPS/PPS storage both in the Initialization Segment
(sample entry `hvc1`) and inband storage (sample entry `hev1`). Services
<span class=modal-keyword>may</span> use either form.

Note: Use of `hev1` is one of the factors that enables
[[#bitstream-switching-h264-h265|bitstream switching]].

<table class="data">
  <caption>Example `@codecs` strings for H.265 (HEVC).</caption>
  <thead><tr><th>Profile<th>Level<th>`@codecs`
  <tbody>
    <tr><td rowspan="2">HEVC Main<td>3.1<td>`hev1.1.2.L93.B0` / `hvc1.1.2.L93.B0`
    <tr><td>4.1<td>`hev1.1.2.L123.B0` / `hvc1.1.2.L123.B0`
    <tr><td>HEVC Main-10<td>4.1<td>`hev1.2.4.L123.B0` / `hvc1.2.4.L123.B0`
</table>

Note: See the [[DASHIF-CODECS|DASH-IF Codec Registry]] for HEVC HDR, UHD, and
additional profile `@codecs` strings.

Note: DVB-DASH [[DVBDASH]] mandates support for HEVC Main and Main 10 Profile,
Main Tier, up to Level 5.1, with additional constraints for UHD and HDR (HLG10
and PQ10) services, in some cases exceeding the baseline Level 4.1 requirement
in this clause. Services targeting DVB-DASH UHD/HDR compatibility should
consult ETSI TS 103 285 clause 5 directly rather than relying solely on this
part's baseline HEVC requirements.

## Decoder configuration with H.264 and H.265 ## {#codecs-decoder-setup-h264-h265}

This clause applies only to video adaptation sets that use H.264 or H.265.

All Initialization Segments in the same video adaptation set <span class=modal-keyword>shall</span> use the same
sample description (i.e. no mixing of `avc1` and `avc3` is allowed).

In Representations using `avc1` or `hvc1` sample description:

* All decoding parameter sets referenced by NALs <span class=modal-keyword>shall</span> be indexed to that
    track's sample description table and decoder configuration record in the
    `avcC` or `hvcC` box contained in its Initialization Segment.
* Edit lists <span class=modal-keyword>may</span> be present.

In Representations using `avc3` or `hev1` sample description:

* All decoding parameter sets referenced by NALs <span class=modal-keyword>shall</span> be indexed to a
    Sequence Parameter NAL (SPS) and Picture Parameter NAL (PPS) stored prior
    to the first video sample in the same Media Segment.
* SPS and PPS stored in each Media Segment <span class=modal-keyword>shall</span> be used for decoding and
    display scaling.
* Every Initialization Segment <span class=modal-keyword>shall</span> include an `avcC` or `hvcC` box that
    <span class=modal-keyword>shall</span> include SPS and PPS NALs that equal the highest Tier, Profile, Level
    and vertical/horizontal sample count of any SPS in the Representation. HEVC
    Decoder Configuration Records <span class=modal-keyword>shall</span> also include a VPS NAL.
* SPS and PPS stored in the Initialization Segments <span class=modal-keyword>shall</span> be used only for
    decoder and display initialization.
* Edit lists <span class=modal-keyword>may</span> be present if using indexed addressing. Edit lists
    <span class=modal-keyword>shall not</span> be present when using any other addressing mode.

## Bitstream switching with H.264 and H.265 ## {#bitstream-switching-h264-h265}

This clause applies only to bitstream-switching adaptation sets that use H.264
or H.265.

All Representations <span class=modal-keyword>shall</span> be encoded using the `avc3` or `hev1` sample
description.

The first presented sample's composition time <span class=modal-keyword>shall</span> equal the first decoded
sample's decode time, which equals the `baseMediaDecodeTime` in the Track
Fragment Decode Time Box (`tfdt`).

Note: This requires the use of negative composition offsets in a v1 Track Run
Box (`trun`) for video samples, otherwise video sample reordering will result
in a delay of video relative to audio.

# Video Adaptation Set Constraints # {#video-constraints}

All Representations in the same video adaptation set <span class=modal-keyword>shall</span> be alternative
encodings of the same source content, encoded such that switching between them
does not produce visual glitches due to picture size or aspect ratio differences.

The encoded picture <span class=modal-keyword>shall</span> only contain the active video area, so that clients
can frame the height and width of the encoded video to the size and shape of
their currently selected display area without extraneous padding in the decoded
video, such as letterbox or pillarbox bars.

Representations in the same video adaptation set <span class=modal-keyword>shall not</span> differ in any of the
following parameters:

* Color Primaries
* Transfer Characteristics
* Matrix Coefficients

If different video adaptation sets differ in any of the above parameters, these
parameters <span class=modal-keyword>should</span> be signaled in the MPD on the adaptation set level by a
Supplemental Property Descriptor or an Essential Property Descriptor with
`@schemeIdUri="urn:mpeg:mpegB:cicp:<Parameter>"`, with `<Parameter>` being one
of `ColourPrimaries`, `TransferCharacteristics`, or `MatrixCoefficients`.

In any video adaptation set, the following <span class=modal-keyword>shall</span> be present:

* <code><b>AdaptationSet</b>@par</code> (the display aspect ratio)
* <code><b>Representation</b>@sar</code> (the sample aspect ratio)
* Either <code><b>Representation</b>@width</code> or <code><b>AdaptationSet</b>@width</code> (but not both)
* Either <code><b>Representation</b>@height</code> or <code><b>AdaptationSet</b>@height</code> (but not both)
* Either <code><b>Representation</b>@frameRate</code> or <code><b>AdaptationSet</b>@frameRate</code> (but not both)

Note: `@width` and `@height` indicate the number of encoded pixels. `@par`
indicates the final intended display aspect ratio and `@sar` is effectively the
ratio of aspect ratios (ratio of `@width x @height` to `@par`). The formula is:
display aspect ratio = picture aspect ratio / sample aspect ratio.

<div class="example">
Given a coded picture of 720x576 pixels with an intended display aspect ratio
of 16:9:

* `@width=720`
* `@height=576`
* `@par=16:9`
* `@sar=45:64` (720x576 is 5:4, which gives `@sar=5:4/16:9=45:64`)

</div>

In any video adaptation set, the following <span class=modal-keyword>should not</span> be present and <span class=modal-keyword>shall</span> be
ignored by clients if present, as these values are trivial to determine at
runtime:

* <code><b>AdaptationSet</b>@minWidth</code>, `@maxWidth`, `@minHeight`, `@maxHeight`,
    `@minFrameRate`, `@maxFrameRate`

`@scanType` <span class=modal-keyword>should not</span> be present and if present <span class=modal-keyword>shall</span> have the value
`progressive`. Non-progressive video is not interoperable.

Note: DVB-DASH [[DVBDASH]] additionally requires HDR-capable Adaptation Sets to
signal the applicable transfer characteristics (HLG or PQ) using the
`urn:mpeg:mpegB:cicp:TransferCharacteristics` Supplemental/Essential Property
descriptor referenced above, and imposes its own constraints on High Frame Rate
(HFR) signalling via `@maximumSAPPeriod` and frame-rate-dependent profile/level
selection. Services offering combined HDR/HFR content intended for DVB-DASH
players should consult ETSI TS 103 285 clause 5 for the complete set of
required descriptors.

# Open Issues and Work Items # {#open-issues}

<table class="data">
  <caption>Part 7 open issues and topics to progress.</caption>
  <thead><tr><th>Topic<th>Status<th>Next action
  <tbody>
    <tr><td>Codec Registry integration<td>Open<td>Embed or link the DASH-IF Codec Registry table from https://github.com/Dash-Industry-Forum/Codecs into this part, either via a build-time include or a live reference.
    <tr><td>Cross-part alignment<td>Open<td>Align terminology and references with Parts 1, 2, and 12.
    <tr><td>Conformance mapping<td>Open<td>Add Part 12 conformance mapping for Part 7 (codec signalling, adaptation set constraints).
    <tr><td>Validator-start tool<td>Open<td>Create `tools/validation/validate_part7_video_mpd.py` covering codec signalling, adaptation set constraints, and Codec Registry compliance.
    <tr><td>Legacy codec profiles<td>Deferred<td>HDR, UHD 4K, Dolby Vision, VP9 profiles from IOP v4.x are documented in Annex A for reference. Future normative support should be driven by Codec Registry registration.
</table>

# Change History # {#change-history}

<table class="data">
  <caption>Part 7 change history.</caption>
  <thead><tr><th>Version<th>Date<th>Change
  <tbody>
    <tr><td>0.1<td>Initial<td>Created initial Bikeshed/Markdown shell for Part 7.
    <tr><td>0.2<td>Migration<td>Migrated H.264/H.265 codec and video adaptation set constraints from DASH-IF-IOP v5-old-draft.
    <tr><td>0.3<td>Restructure<td>Added DASH-IF Codec Registry section (dashif.org/codecs, GitHub Codecs repo). Updated scope to reference registry as authoritative source. Moved HDR/UHD/VP9 to informative Annex A. Added codec registration process description.
</table>

# Annex A: Legacy Codec Profiles (Informative) # {#annex-legacy-codecs}


## General ## {#annex-legacy-codecs-general}

This annex documents codec profiles that were specified in earlier versions of
DASH-IF IOP (v4.x and earlier). These profiles are provided for reference only
and are not normative in IOP v5. Services wishing to use these codecs <span class=modal-keyword>should</span>
consult the [[DASHIF-CODECS|DASH-IF Codec Registry]] for current normative
requirements.

## HEVC HDR PQ10 ## {#annex-hevc-hdr}

Earlier IOP versions specified HEVC HDR PQ10 profiles including SMPTE 2094-10,
SMPTE 2094-40, and TS 103.433 dynamic metadata. These profiles are now tracked
in the DASH-IF Codec Registry at
[https://dashif.org/codecs/](https://dashif.org/codecs/).

## UHD HEVC 4K ## {#annex-uhd-4k}

Earlier IOP versions specified UHD HEVC 4K profiles (up to 3840x2160 at up to
60 fps). These profiles are now tracked in the DASH-IF Codec Registry.

## Dolby Vision Dual-Stream ## {#annex-dolby-vision}

Earlier IOP versions specified Dolby Vision dual-stream profiles. These profiles
are now tracked in the DASH-IF Codec Registry.

## VP9 ## {#annex-vp9}

Earlier IOP versions specified VP9 codec requirements. VP9 support is now
tracked in the DASH-IF Codec Registry.

Note: For all of the above legacy profiles, the DASH-IF Codec Registry at
[https://dashif.org/codecs/](https://dashif.org/codecs/) is the authoritative
and up-to-date reference. The GitHub repository at
[https://github.com/Dash-Industry-Forum/Codecs](https://github.com/Dash-Industry-Forum/Codecs)
contains the registry source data and accepts contributions for new codec
registrations.