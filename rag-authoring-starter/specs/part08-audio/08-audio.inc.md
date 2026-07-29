<!--
  Part 8: Audio.
  Restructured 2026-07-28:
  - Added DASH-IF Codec Registry section (dashif.org/codecs, GitHub Codecs repo)
  - All audio codec requirements retained as normative baseline
  - Updated scope to reference registry as authoritative source
  Source grounding:
  - Dash-Industry-Forum/DASH-IF-IOP branch v5-old-draft, 80-Codecs.inc.md
  - Dash-Industry-Forum/DASH-IF-IOP branch v5-old-draft, 27-AdaptationSets.inc.md
  - https://dashif.org/codecs/introduction/
  - https://github.com/Dash-Industry-Forum/Codecs
  - https://dashif.org/identifiers/audio_source_metadata/
-->

# Scope # {#scope}

This document specifies DASH-IF IOP v5 Part 8: **Audio**. It defines audio
interoperability points, coding profiles, ISO BMFF packaging, MPD parameters,
and audio-specific constraints for DASH-IF compliant services and clients.

The primary normative reference for supported audio codecs is the
**DASH-IF Codec Registry** at [https://dashif.org/codecs/](https://dashif.org/codecs/).
This part defines the general requirements for audio adaptation sets and provides
normative baseline requirements for the most widely deployed audio codecs. For
the complete and up-to-date list of registered codecs, services and clients
<span class=modal-keyword>shall</span> consult the DASH-IF Codec Registry.

Services <span class=modal-keyword>shall</span> use only media codecs that are registered in the DASH-IF Codec
Registry or explicitly defined in this part. Clients <span class=modal-keyword>may</span> support any set of
codecs registered in the DASH-IF Codec Registry and <span class=modal-keyword>shall not</span> attempt to play
back Representations for which they do not have codec support.

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
- DASH-IF Codec Registry, *https://dashif.org/codecs/introduction/* [[DASHIF-CODECS]].
- DASH-IF Identifier Registry, *https://dashif.org/identifiers/audio_source_metadata/* [[DASHIF-IDENTIFIERS]].

# Terms and Definitions # {#terms}

Terms and definitions are inherited from ISO/IEC 23009-1, ISO/IEC 23000-19, and
Part 2 unless defined in this part.

: <dfn export>audio adaptation set</dfn>
:: An Adaptation Set that contains sound information to be rendered to the user,
    identified by `@mimeType="audio/mp4"`.

: <dfn export>DASH-IF Codec Registry</dfn>
:: The DASH-IF maintained registry of video and audio codecs supported for use
    in DASH-IF compliant services, available at
    [https://dashif.org/codecs/](https://dashif.org/codecs/).

# DASH-IF Codec Registry # {#codec-registry}

## Overview ## {#codec-registry-overview}

DASH-IF maintains a **Codec Registry** that serves as the authoritative and
continuously updated reference for codecs supported in DASH-IF compliant
services. The registry is available at:

- **Web interface:** [https://dashif.org/codecs/introduction/](https://dashif.org/codecs/introduction/)
- **Source data:** [https://github.com/Dash-Industry-Forum/Codecs](https://github.com/Dash-Industry-Forum/Codecs)

For audio codecs, the registry provides:

- A structured list of supported audio codecs with their DASH MPD `@codecs`
    strings, CMAF profiles, and interoperability notes.
- Codec-specific requirements for `@mimeType`, `@codecs`, **AudioChannelConfiguration**,
    and SAP type.
- Guidance on codec selection for different service scenarios (stereo, multichannel,
    immersive audio, speech, etc.).
- A machine-readable dataset that can be integrated into validator tools and
    reference implementations.

Note: The DASH-IF Identifier Registry at
[https://dashif.org/identifiers/audio_source_metadata/](https://dashif.org/identifiers/audio_source_metadata/)
provides the `@schemeIdUri` values for **AudioChannelConfiguration** elements.
This is a separate registry from the Codec Registry.

## Using the Codec Registry ## {#codec-registry-usage}

Services <span class=modal-keyword>shall</span> use `@codecs` strings that are registered in the DASH-IF Codec
Registry for the codec and profile being used. The registry defines the
canonical `@codecs` string format for each supported audio codec.

Clients <span class=modal-keyword>should</span> use the DASH-IF Codec Registry to determine which audio codecs
they are expected to support for a given service scenario. The registry indicates
which codecs are mandatory, recommended, or optional for different client
categories.

Note: The DASH-IF Codec Registry is a living document that is updated as new
codecs are registered and existing codec requirements are refined. Services and
clients <span class=modal-keyword>should</span> consult the current version of the registry rather than relying
solely on the static codec tables in this part.

# Audio Adaptation Set Constraints # {#audio-constraints}

**AdaptationSet**@lang <span class=modal-keyword>shall</span> be present on every audio adaptation set.

`@audioSamplingRate` <span class=modal-keyword>shall</span> be present either on the adaptation set or
Representation level (but not both).

The **AudioChannelConfiguration** element <span class=modal-keyword>shall</span> be present either on the
adaptation set or Representation level (but not both). The scheme and value
<span class=modal-keyword>shall</span> conform to `ChannelConfiguration` as defined in ISO/IEC 23001-8.

# Audio Codecs # {#codecs}

## General ## {#codecs-general}

The following clauses define normative baseline requirements for the audio codecs
supported in DASH-IF compliant services. For the complete and up-to-date list of
registered audio codecs, consult the [[DASHIF-CODECS|DASH-IF Codec Registry]].

## HE-AACv2 audio (stereo) ## {#codecs-heaacv2}

The codec for basic stereo audio support is MPEG-4 High Efficiency AAC v2
Profile, level 2.

Note: HE-AACv2 is also standardized as Enhanced aacPlus in 3GPP TS 26.401.

An HE-AACv2 Profile decoder can also decode any content that conforms to MPEG-4
AAC Profile or MPEG-4 HE-AAC Profile. Therefore, services are free to use any
AAC version. Typical clients are expected to play AAC-LC, HE-AAC and HE-AACv2
encoded content.

For content with SBR, i.e. `@codecs=mp4a.40.5` or `@codecs=mp4a.40.29`,
`@audioSamplingRate` signals the resulting sampling rate after SBR is applied,
e.g. 48 kHz even if the AAC-LC core operates at 24 kHz.

For content with PS, i.e. `@codecs=mp4a.40.29`, the **AudioChannelConfiguration**
element signals the resulting channel configuration after PS is applied, e.g.
stereo even if the AAC-LC core operates at mono.

SAP type <span class=modal-keyword>shall</span> be 1. The `@codecs` string <span class=modal-keyword>shall</span> have a value from the below
table.

<table class="data">
  <caption>Permitted HE-AACv2 `@codecs` values.</caption>
  <thead><tr><th>Profile<th>`@codecs`
  <tbody>
    <tr><td>MPEG-4 AAC Profile<td>`mp4a.40.2`
    <tr><td>MPEG-4 HE-AAC Profile<td>`mp4a.40.5`
    <tr><td>MPEG-4 HE-AAC v2 Profile<td>`mp4a.40.29`
</table>

## HE-AACv2 audio (multichannel) ## {#codecs-heaacv2-multichannel}

This clause extends HE-AACv2 requirements with multichannel scenarios. All
constraints defined for the stereo scenario also apply here.

Support for multichannel content is available in the HE-AACv2 Profile, starting
with level 4 for 5.1 and level 6 for 7.1. Decoders implementing MPEG-4 HE-AACv2
multichannel profiles are fully compatible with content encoded in conformance to
the HE-AACv2 stereo requirements defined above.

Decoders <span class=modal-keyword>shall</span> support decoding of loudness and dynamic range related
information, i.e. `dynamic_range_info()` and `MPEG4_ancillary_data()` in the
bitstream.

## Enhanced AC-3 (Dolby Digital Plus) ## {#codecs-eac3}

The `@codecs` parameter <span class=modal-keyword>shall</span> be `ec-3`. SAP type <span class=modal-keyword>shall</span> be `1`.

The **AudioChannelConfiguration** element <span class=modal-keyword>shall</span> use
`@schemeIdUri="tag:dolby.com,2014:dash:audio_channel_configuration:2011"` with
`@value` as defined in the [[DASHIF-IDENTIFIERS|DASH-IF Identifier Registry]].

## Dolby TrueHD ## {#codecs-truehd}

The `@codecs` parameter <span class=modal-keyword>shall</span> be `mlpa`. SAP type <span class=modal-keyword>shall</span> be `1`.

## AC-4 ## {#codecs-ac4}

The `@codecs` parameter <span class=modal-keyword>shall</span> be `ac-4`. SAP type <span class=modal-keyword>shall</span> be `1`.

The **AudioChannelConfiguration** element <span class=modal-keyword>shall</span> use
`@schemeIdUri="tag:dolby.com,2014:dash:audio_channel_configuration:2011"` with
`@value` as defined in the [[DASHIF-IDENTIFIERS|DASH-IF Identifier Registry]].

## DTS-HD ## {#codecs-dts-hd}

DTS-HD comprises a number of profiles optimized for specific applications. For
all DTS formats, SAP is always 1.

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

MPEG Surround is a scheme for coding multichannel signals based on a down-mixed
signal of the original multichannel signal, and associated spatial parameters.
The down-mix <span class=modal-keyword>shall</span> be coded with MPEG-4 High Efficiency AAC v2.

MPEG Surround used in DASH <span class=modal-keyword>shall</span> comply with level 4 of the Baseline MPEG
Surround profile. SAP type <span class=modal-keyword>shall</span> be `1`. `@codecs` <span class=modal-keyword>shall</span> be `mp4a.40.30`.

## MPEG-H 3D Audio ## {#codecs-mpegh-3d}

MPEG-H 3D Audio encoded content <span class=modal-keyword>shall</span> comply with Level 1, 2 or 3 of the
MPEG-H Low Complexity (LC) Profile.

In addition to ISO/IEC 23008-3, the following constraints <span class=modal-keyword>shall</span> apply to storage
of raw MPEG-H audio frames in DASH containers:

* One audio ISO BMFF sample <span class=modal-keyword>shall</span> consist of a single `mpegh3daFrame()` structure.
* The parameters carried in the `MHADecoderConfigurationRecord()` <span class=modal-keyword>shall</span> be
    consistent with the configuration of the audio bitstream. In particular,
    `mpegh3daProfileLevelIndication` <span class=modal-keyword>shall</span> be set to `0x0B`, `0x0C`, or `0x0D`
    for MPEG-H Audio LC Profile Level 1, Level 2, or Level 3, respectively.
* The `referenceChannelLayout` field carried in the
    `MHADecoderConfigurationRecord()` <span class=modal-keyword>shall</span> be equivalent to what is signaled by
    `ChannelConfiguration` according to ISO/IEC 23001-8.
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

MPEG-D Unified Speech and Audio Coding (USAC) has been designed to provide
consistently high audio quality with a variety of content that comprises a
mixture of audio and speech signals, enabling adaptive switching capability from
12 kbps stereo up to transparency.

Usage of USAC in DASH presentations <span class=modal-keyword>shall</span> conform to the `xHE-AAC` media
profile, providing support up to 5.1 multichannel coding.

SAP type <span class=modal-keyword>shall</span> be `1`. `@codecs` <span class=modal-keyword>shall</span> be `mp4a.40.42`.

# Open Issues and Work Items # {#open-issues}

<table class="data">
  <caption>Part 8 open issues and topics to progress.</caption>
  <thead><tr><th>Topic<th>Status<th>Next action
  <tbody>
    <tr><td>Codec Registry integration<td>Open<td>Embed or link the DASH-IF Codec Registry audio table from https://github.com/Dash-Industry-Forum/Codecs into this part, either via a build-time include or a live reference.
    <tr><td>Codec string verification<td>Open<td>Re-verify `@codecs` values and normative references against current codec registration authorities and the DASH-IF Identifier Registry before this part is finalized.
    <tr><td>Cross-part alignment<td>Open<td>Align terminology and references with Parts 1, 2, and 12.
    <tr><td>Conformance mapping<td>Open<td>Add Part 12 conformance mapping for Part 8 (codec signalling, adaptation set constraints, AudioChannelConfiguration).
    <tr><td>Validator-start tool<td>Open<td>Create `tools/validation/validate_part8_audio_mpd.py` covering codec signalling, adaptation set constraints, and Codec Registry compliance.
</table>

# Change History # {#change-history}

<table class="data">
  <caption>Part 8 change history.</caption>
  <thead><tr><th>Version<th>Date<th>Change
  <tbody>
    <tr><td>0.1<td>Initial<td>Created initial Bikeshed/Markdown shell for Part 8.
    <tr><td>0.2<td>Migration<td>Migrated audio codec and audio adaptation set constraints from DASH-IF-IOP v5-old-draft.
    <tr><td>0.3<td>Restructure<td>Added DASH-IF Codec Registry section (dashif.org/codecs, GitHub Codecs repo). Updated scope to reference registry as authoritative source. Added DASHIF-IDENTIFIERS reference for AudioChannelConfiguration. Updated open issues.
</table>