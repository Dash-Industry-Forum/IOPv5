<!--


  Part 8: Audio.
  Initial Bikeshed/Markdown shell following the IOPv5 authoring convention.
  Source grounding / migration target: dashif-iop-v5-part8-draft# draft Part 8.
  Normative content in this revision is migrated from:
  - Dash-Industry-Forum/DASH-IF-IOP branch v5-old-draft, 80-Codecs.inc.md
    (HE-AACv2 stereo/multichannel, E-AC-3, Dolby TrueHD, AC-4, DTS-HD, MPEG
    Surround, MPEG-H 3D Audio, MPEG-D USAC clauses)
  - Dash-Industry-Forum/DASH-IF-IOP branch v5-old-draft, 27-AdaptationSets.inc.md
    (audio adaptation set constraints)
-->

# Scope # {#scope}

This document specifies DASH-IF IOP v5 Part 8: **Audio**. Audio interoperability points, coding profiles, ISO BMFF packaging, MPD parameters, and audio-specific constraints.

Services <span class=modal-keyword>shall</span> use only the media codecs described in this part, in conformance with the requirements defined here.
# References # {#doc-references}

The following referenced documents are necessary for the application of this
part:

- ISO/IEC 23009-1 [[!MPEGDASH]].
- ISO/IEC 23000-19 [[!MPEGCMAF]].
- ISO/IEC 14496-3, *Coding of audio-visual objects — Part 3: Audio* (MPEG-4 AAC family).
- ISO/IEC 23003-1, *MPEG Surround*.
- ISO/IEC 23008-3, *MPEG-H 3D Audio*.
- DASH-IF IOP v5 Part 2, *Core Principles and CMAF Mapping*.
- DASH-IF IOP v5 Part 12, *Conformance and Reference Tools*.

# Terms and Definitions # {#terms}

Terms and definitions are inherited from ISO/IEC 23009-1, ISO/IEC 23000-19, and
Part 2 unless defined in this part.

An <dfn export>audio adaptation set</dfn> is an Adaptation Set that contains sound information to be rendered to the user, identified by `@mimeType="audio/mp4"`.

# Audio Adaptation Set Constraints # {#audio-constraints}

`AdaptationSet@lang` <span class=modal-keyword>shall</span> be present on every audio adaptation set.

`@audioSamplingRate` <span class=modal-keyword>shall</span> be present either on the adaptation set or Representation level (but not both).

The `AudioChannelConfiguration` element <span class=modal-keyword>shall</span> be present either on the adaptation set or Representation level (but not both). The scheme and value <span class=modal-keyword>shall</span> conform to `ChannelConfiguration` as defined in ISO/IEC 23001-8.

# Audio Codecs # {#codecs}

## HE-AACv2 audio (stereo) ## {#codecs-heaacv2}

The codec for basic stereo audio support is MPEG-4 High Efficiency AAC v2 Profile, level 2.

Note: HE-AACv2 is also standardized as Enhanced aacPlus in 3GPP TS 26.401.

An HE-AACv2 Profile decoder can also decode any content that conforms to MPEG-4 AAC Profile or MPEG-4 HE-AAC Profile. Therefore, services are free to use any AAC version. Typical clients are expected to play AAC-LC, HE-AAC and HE-AACv2 encoded content.

For content with SBR, i.e. `@codecs=mp4a.40.5` or `@codecs=mp4a.40.29`, `@audioSamplingRate` signals the resulting sampling rate after SBR is applied, e.g. 48 kHz even if the AAC-LC core operates at 24 kHz.

For content with PS, i.e. `@codecs=mp4a.40.29`, the `AudioChannelConfiguration` element signals the resulting channel configuration after PS is applied, e.g. stereo even if the AAC-LC core operates at mono.

SAP type <span class=modal-keyword>shall</span> be 1. The `@codecs` string <span class=modal-keyword>shall</span> have a value from the below table.
<table class="data">
  <caption>Permitted HE-AACv2 `@codecs` values.</caption>
  <thead><tr><th>Profile<th>`@codecs`
  <tbody>
    <tr><td>MPEG-4 AAC Profile<td>`mp4a.40.2`
    <tr><td>MPEG-4 HE-AAC Profile<td>`mp4a.40.5`
    <tr><td>MPEG-4 HE-AAC v2 Profile<td>`mp4a.40.29`
</table>

## HE-AACv2 audio (multichannel) ## {#codecs-heaacv2-multichannel}

This clause extends HE-AACv2 requirements with multichannel scenarios. All constraints defined for the stereo scenario also apply here.

Support for multichannel content is available in the HE-AACv2 Profile, starting with level 4 for 5.1 and level 6 for 7.1. Decoders implementing MPEG-4 HE-AACv2 multichannel profiles are fully compatible with content encoded in conformance to the HE-AACv2 stereo requirements defined above.

Decoders <span class=modal-keyword>shall</span> support decoding of loudness and dynamic range related information, i.e. `dynamic_range_info()` and `MPEG4_ancillary_data()` in the bitstream.

## Enhanced AC-3 (Dolby Digital Plus) ## {#codecs-eac3}

The `@codecs` parameter <span class=modal-keyword>shall</span> be `ec-3`. SAP type <span class=modal-keyword>shall</span> be `1`.

The `AudioChannelConfiguration` element <span class=modal-keyword>shall</span> use `@schemeIdUri="tag:dolby.com,2014:dash:audio_channel_configuration:2011"` with `@value` as defined in the [DASH-IF identifier registry](https://dashif.org/identifiers/audio_source_metadata/).

## Dolby TrueHD ## {#codecs-truehd}

The `@codecs` parameter <span class=modal-keyword>shall</span> be `mlpa`. SAP type <span class=modal-keyword>shall</span> be `1`.

## AC-4 ## {#codecs-ac4}

The `@codecs` parameter <span class=modal-keyword>shall</span> be `ac-4`. SAP type <span class=modal-keyword>shall</span> be `1`.

The `AudioChannelConfiguration` element <span class=modal-keyword>shall</span> use `@schemeIdUri="tag:dolby.com,2014:dash:audio_channel_configuration:2011"` with `@value` as defined in the [DASH-IF identifier registry](https://dashif.org/identifiers/audio_source_metadata/).

## DTS-HD ## {#codecs-dts-hd}

DTS-HD comprises a number of profiles optimized for specific applications. For all DTS formats, SAP is always 1.
<table class="data">
  <caption>DTS `@codecs` values.</caption>
  <thead><tr><th>Codec<th>`@codecs`
  <tbody>
    <tr><td>DTS Digital Surround<td>`dtsc`
    <tr><td>DTS-HD High Resolution and DTS-HD Master Audio<td>`dtsh`
    <tr><td>DTS Express<td>`dtse`
    <tr><td>DTS-HD Lossless (no core)<td>`dtsl`
</table>

## MPEG Surround ## {#codecs-mpeg-surround}

MPEG Surround is a scheme for coding multichannel signals based on a down-mixed signal of the original multichannel signal, and associated spatial parameters. The down-mix <span class=modal-keyword>shall</span> be coded with MPEG-4 High Efficiency AAC v2.

MPEG Surround used in DASH <span class=modal-keyword>shall</span> comply with level 4 of the Baseline MPEG Surround profile. SAP type <span class=modal-keyword>shall</span> be `1`. `@codecs` <span class=modal-keyword>shall</span> be `mp4a.40.30`.

## MPEG-H 3D Audio ## {#codecs-mpegh-3d}

MPEG-H 3D Audio encoded content <span class=modal-keyword>shall</span> comply with Level 1, 2 or 3 of the MPEG-H Low Complexity (LC) Profile.

In addition to ISO/IEC 23008-3, the following constraints <span class=modal-keyword>shall</span> apply to storage of raw MPEG-H audio frames in DASH containers:

* One audio ISO BMFF sample <span class=modal-keyword>shall</span> consist of a single `mpegh3daFrame()` structure.
* The parameters carried in the `MHADecoderConfigurationRecord()` <span class=modal-keyword>shall</span> be consistent with the configuration of the audio bitstream. In particular, `mpegh3daProfileLevelIndication` <span class=modal-keyword>shall</span> be set to `0x0B`, `0x0C`, or `0x0D` for MPEG-H Audio LC Profile Level 1, Level 2, or Level 3, respectively.
* The `referenceChannelLayout` field carried in the `MHADecoderConfigurationRecord()` <span class=modal-keyword>shall</span> be equivalent to what is signaled by `ChannelConfiguration` according to ISO/IEC 23001-8.
* Each Media Segment <span class=modal-keyword>shall</span> start with a SAP of type 1 (e.g. a sync sample).

<table class="data">
  <caption>Permitted MPEG-H 3D Audio `@codecs` values.</caption>
  <thead><tr><th>Codec<th>`@codecs`
  <tbody>
    <tr><td>MPEG-H 3D audio LC profile level 1<td>`mhm1.0x0B`
    <tr><td>MPEG-H 3D audio LC profile level 2<td>`mhm1.0x0C`
    <tr><td>MPEG-H 3D audio LC profile level 3<td>`mhm1.0x0D`
</table>

## MPEG-D Unified Speech and Audio Coding ## {#codecs-mpegd-speech-and-audio}

MPEG-D Unified Speech and Audio Coding (USAC) has been designed to provide consistently high audio quality with a variety of content that comprises a mixture of audio and speech signals, enabling adaptive switching capability from 12 kbps stereo up to transparency.

Usage of USAC in DASH presentations <span class=modal-keyword>shall</span> conform to the `xHE-AAC` media profile, providing support up to 5.1 multichannel coding.

SAP type <span class=modal-keyword>shall</span> be `1`. `@codecs` <span class=modal-keyword>shall</span> be `mp4a.40.42`.

# Requirements and Recommendations # {#requirements}

Issue: The above clauses migrate the HE-AACv2 (stereo/multichannel), E-AC-3,
Dolby TrueHD, AC-4, DTS-HD, MPEG Surround, MPEG-H 3D Audio, MPEG-D USAC, and
audio-adaptation-set constraints from Dash-Industry-Forum/DASH-IF-IOP branch
v5-old-draft, 80-Codecs.inc.md and 27-AdaptationSets.inc.md. Codec version
numbers, `@codecs` values, and referenced clause numbers <span class=modal-keyword>should</span> be re-verified
against current codec registration authorities and the DASH-IF identifier
registry before this part is finalized.
[GROUNDED_BY=Dash-Industry-Forum/DASH-IF-IOP@v5-old-draft:80-Codecs.inc.md]

# Open Issues and Work Items # {#open-issues}

<table class="data">
  <caption>Part 8 open issues and topics to progress.</caption>
  <thead><tr><th>Topic<th>Status<th>Next action
  <tbody>
    <tr><td>Source migration<td>In progress<td>Core audio codec clauses migrated from DASH-IF-IOP v5-old-draft. Verify codec identifier strings and normative references against current registries.
    <tr><td>Cross-part alignment<td>Open<td>Align terminology and references with Parts 1, 2, and 12.
    <tr><td>Conformance mapping<td>Open<td>Identify validator/test-asset/reference-player expectations and link them to Part 12.
</table>

# Change History # {#change-history}

<table class="data">
  <caption>Part 8 change history.</caption>
  <thead><tr><th>Version<th>Date<th>Change
  <tbody>
    <tr><td>0.1<td>Initial<td>Created initial Bikeshed/Markdown shell for Part 8.
    <tr><td>0.2<td>Migration<td>Migrated audio codec and audio adaptation set constraints from DASH-IF-IOP v5-old-draft.
</table>


