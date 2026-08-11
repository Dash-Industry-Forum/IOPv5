<!--
  Part 7: Video.
  Converted 2026-08-10:
  - Added DASH-IF Codec Registry section (dashif.org/codecs, GitHub Codecs repo)
  - H.264/AVC and H.265/HEVC codec requirements retained as normative baseline
  - HDR, UHD 4K, Dolby Vision, VP9 moved to informative Annex A
  - Video adaptation set constraints retained
  Source grounding:
  - Dash-Industry-Forum/DASH-IF-IOP v5 Google Doc: https://docs.google.com/document/d/14FSYrs2OrUrI1jJu7xhpWShjABik63Ts/
-->

# Executive summary # {#exec_summary}

The present document defines the CMAF Media Profiles and the DASH signalling for video tracks. This work was derived from IOP v4.3 [[DASHIF-IOP4_3]], but does not contain non-CMAF profiles.

# Introduction # {#intro}

The present document is Part 7 of a multipart set of documents, collectively called “IOP V5.0.0”.  All the parts are:

1. Overview, architecture and interfaces  
2. Core principles and CMAF mapping  
3. On-demand services  
4. Live and low-latency live services  
5. Ad insertion  
6. Content protection  
7. Video  
8. Audio  
9. Text  
10. Events  
11. Additional functionalities  
12. Conformance and reference tools

# Scope # {#scope}

The present document defines the CMAF Media Profiles and the DASH signalling for video tracks. This work was derived from IOP v4.3 [[DASHIF-IOP4_3]], but does not contain non-CMAF profiles.
<!--
# References # {#references_local}

## Normative references ## {#normative-references}

References are either specific (identified by date of publication and/or edition number or version number) or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies.

NOTE:	While any hyperlinks included in this clause were valid at the time of publication, DASH-IF cannot guarantee their long-term validity.

The following referenced documents are necessary for the application of the present document.

1. DASH-IF IOP v5.0.0, Part 2, “Core principles and CMAF mapping”

2. ISO/IEC 23009-1: “Information technology — Dynamic adaptive streaming over HTTP (DASH) — Part 1: Media presentation description and segment formats” [[!MPEGDASH]].

3. ISO/IEC 23000-19 “Information technology — Multimedia application format (MPEG-A) — Part 19: Common media application format (CMAF) for segmented media” [[!MPEGCMAF]].

4. ISO/IEC 14496-12: Information technology — Coding of audio-visual objects -Part 12: ISO base media file format [[!ISOBMFF]].

5. ISO/IEC 14496-15: Information technology — Coding of audio-visual objects — Part 15: Carriage of network abstraction layer (NAL) unit structured video in ISO base media file format [[!NALUFF]].

6. ITU-T Rec. H.264: Advanced video coding for generic audiovisual services | ISO/IEC 14496-10: Information technology — Coding of audio-visual objects —Part 10: Advanced Video Coding [[!AVC]].

7. ITU-T Rec. H.265: High efficiency video coding | ISO/IEC 23008-2: Information technology — High efficiency coding and media delivery in heterogeneous environments — Part 2: High efficiency video coding [[!HEVC]].

8. ITU-T Rec. H.266: Versatile video coding | ISO/IEC 23090-3: Information technology — Coded representation of immersive media — Part 3: Versatile video coding [[!VVC]].

9. ITU-T Rec. H.274: Versatile supplemental enhancement information messages for coded video bitstreams | ISO/IEC 23002-7: Information technology — MPEG video technologies — Part 7: Versatile supplemental enhancement information messages for coded video bitstreams [[!ITU_H274]].

10. ISO/IEC 23094-1: Information technology — General video coding – Part 1: Essential video coding [[!MPEG5EVC]].

11. ISO/IEC 23094-2: Information technology – General video coding — Part 2: Low complexity enhancement video coding [[!MPEG5LCEVC]].

12. SCTE 215-1-1:2020b, “HEVC Video Constraints for Cable Television Part 1-1 HDR”

13. ITU-T Rec. H.273: Coding-independent code points for video signal type identification | ISO/IEC 23091-2: Information technology — Coding-independent code points — Part 2: Video

14. ISO/IEC 23091-1: Information technology — Coding-independent code points — Part 1: Systems

15. ISO/IEC 13818-1: Information technology — Generic coding of moving pictures and associated audio information — Part 1: Systems

16. CTA-5003-B: Web Application Video Ecosystem (WAVE): Device Playback Capabilities Specification, 2024 edition, available at [https://shop.cta.tech/products/cta-5003](https://shop.cta.tech/products/cta-5003) [https://cdn.cta.tech/cta/media/media/resources/standards/pdfs/cta-5003-final.pdf](https://cdn.cta.tech/cta/media/media/resources/standards/pdfs/cta-5003-final.pdf)

17. ETSI TS 103 285: “Digital Video Broadcasting (DVB); MPEG-DASH Profile for Transport of ISOBMFF Based DVB Services over IP Based Networks”

## Informative references ## {#informative-references}

References are either specific (identified by date of publication and/or edition number or version number) or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies.

NOTE:	While any hyperlinks included in this clause were valid at the time of publication, ETSI cannot guarantee their long-term validity.

The following referenced documents are not necessary for the application of the present document, but they assist the user with regard to a particular subject area.

1. DASH-IF IOP v4.3, “Guidelines for Implementation: DASH-IF Interoperability Points”  
2. SCTE 214-1: 2024: “MPEG DASH for IP-Based Cable Services, Part 1: MPD Constraints and Extensions”  
3. SMPTE ST 2094-10:2021: "Dynamic Metadata for Color Volume Transform - Application #1".  
4. SMPTE ST 2094-40:2020: "Dynamic Metadata for Color Volume Transform - Application #4".  
5. ETSI TS 103 433-2: "High-Performance Single Layer High Dynamic Range (HDR) System for use in Consumer Electronics devices; Part 2: Enhancements for Perceptual Quantization (PQ) transfer function based High Dynamic Range (HDR) Systems (SL-HDR2)".
-->
# Definition of terms, symbols and abbreviations # {#definition-of-terms,-symbols-and-abbreviations}

## Terms ## {#terms}

For the purposes of the present document, the following terms apply:

## Symbols ## {#symbols}

For the purposes of the present document, the following symbols apply:

## Abbreviations ## {#abbreviations}

For the purposes of the present document, the following abbreviations apply:

: <dfn export>CMAF</dfn>
:: Common Media Application Format  
: <dfn export>DASH</dfn>
:: 	Dynamic Adaptive Streaming over HTTP  
: <dfn export>IEC</dfn>
:: 	International Electrotechnical Commission  
: <dfn export>IOP</dfn>
:: 	InterOperability Points  
: <dfn export>ISO</dfn>
:: 	International Standards Organization  
: <dfn export>Kbps</dfn>
:: 	Kilobits per second  
: <dfn export>MPD</dfn>
:: 	Media Presentation Description  
: <dfn export>SEI</dfn>
:: 	Supplemental Enhancement Information  
: <dfn export>VUI</dfn>
:: 	Video Usability information

# CMAF Media Profiles # {#cmaf-media-profiles}

All video tracks <span class=modal-keyword>should</span> conform to CMAF Media Profiles, as outlined in draft DASH-IF v5.0.0, Part 2 [[!DASHIF-IOP5_2]]. DASH-IF IOPs do not require support for any specific codecs, but rather permits to add different codecs as long as they are addressing basic CMAF media profile related requirements. Codecs validated to fulfill these requirements are documented in the online DASH-IF specification repository found here: [https://dashif.org/codecs/video/](https://dashif.org/codecs/text) including the Media profile name, the CMAF brand, a reference to the relevant specifications, a recommended <code>`@codecs`</code> parameter and any additional information.

Additional non-CMAF video profiles can be found in DASH-IF IOP v4.3 [[DASHIF-IOP4_3]].

# Mapping to delivery # {#mapping-to-delivery}

## CMAF track definition ## {#cmaf-track-definition}

If video media conforming to a particular media profile is provided in an CMAF track, then the CMAF track <span class=modal-keyword>shall</span> conform with all of the following:

* The requirements of the ISO BMFF track defined in subclause 5.1 for the particular media profile,

* The general CMAF track constraints in ISO/IEC 23000-19 [[!MPEGCMAF]] clause 7, and

* The general video track constraints defined in ISO/IEC 23000-19 [[!MPEGCMAF]] clause 9.

## CMAF switching set definition ## {#cmaf-switching-set-definition}

If video media conforming to a particular media profile is provided in an CMAF switching set, then each CMAF track in the CMAF switching set <span class=modal-keyword>shall</span> conform with all of the following:

* The requirements of CMAF track in specified in subclause 5.2,

* The general CMAF switching set constraints in ISO/IEC 23000-19 [[!MPEGCMAF]] clause 7, and

* The general CMAF switching set constraints defined in ISO/IEC 23000-19 [[!MPEGCMAF]] clause 9.

## Content requirements ## {#content-requirements}

In addition to the general provisions defined in draft IOP V5 part 2 [[DASHIF-IOP5_2]] additionally Adaptation Sets <span class=modal-keyword>shall</span> comply with the provisions of the [table below](#t_video_adaptationset_attr_elem).

<table id="t_video_adaptationset_attr_elem" class="data">
  <caption>Video track Adaptation Set attributes and elements</caption>
  <thead><tr><th>DASH Attribute or Element<th>Use for media type<th>Detailed Usage in DASH-IF IOPs
  <tbody>
    <tr>
      <td><code>@mimeType</code></td>
      <td>M</td>
      <td>See ISO/IEC 23009-1 [[!MPEGDASH]], clause 5.3.7.2, Table 14.<br>
        This <span class=modal-keyword>shall</span> be set to <code>“video/mp4”</code>.</td>
    </tr>
    <tr>
      <td><code>`@codecs`</code></td>
      <td>M</td>
      <td>See ISO/IEC 23009-1 [[!MPEGDASH]], clause 5.3.7.2, Table 14.<br>
        This element <span class=modal-keyword>shall</span> be present and set to a valid value, including the codec, profile and level. See [https://dashif.org/codecs/video/](https://dashif.org/codecs/text) for example values for this attribute.</td>
    </tr>
    <tr>
      <td><code>@lang</code></td>
      <td>O</td>
      <td>See ISO/IEC 23009-1 [[!MPEGDASH]], clause 5.3.3.2, Table 5.<br>
        If present with <code><b>Accessibility</b></code>**, the <code>@lang</code> attribute signals the language of closed signing present in the video.</td>
    </tr>
    <tr>
      <td><code><b>Accessibility</b></code></td>
      <td>0 … N</td>
      <td>See ISO/IEC 23009-1 [[!MPEGDASH]], clause 5.3.4.2, Table 8.<br>
      In DASH-IF IOPs the following two schemes for accessibility are defined:
      <ul>
        <li>the Role scheme as defined by MPEG-DASH (ISO/IEC 23009-1 [[!MPEGDASH]]), clause 5.8.5.5, i.e., <code>“urn:mpeg:dash:role:2011”</code>, <span class=modal-keyword>should</span> be used</li>
      </ul>
      The DASH role scheme with the following values is expected to be recognized by a DASH-IF client for media type <code>“video”</code> together with the <code><b>Accessibility</b></code> descriptor:
      <ul>
        <li><code>sign</code></li>
        <li><code>captions</code></li>
        <li>the scheme when CEA-608 is used as defined in clause 6.4.3.3, with <code>@schemeIdUri</code> set to <code>"urn:scte:dash:cc:cea-608:2015"</code>
      </ul>
      If the video contains open or closed signing, the <code><b>Accessibility</b></code> element <span class=modal-keyword>shall</span> be present. In DASH IOPs only the Role scheme as defined in ISO/IEC 23009-1 [[!MPEGDASH]], clause 5.8.5.5, <span class=modal-keyword>should</span> be used, with `@schemIdUri` set to <code>urn:mpeg:dash:role:2011</code>; and the <code>@value</code> <span class=modal-keyword>shall</span> be set to "caption"</td>
    </tr>
    <tr>
      <td><code><b>Role</b></code></td>
      <td>0 … N</td>
      <td>See ISO/IEC 23009-1 [[!MPEGDASH]], clause 5.3.3.2, Table 5.<br>
      In DASH-IF IOPs only the Role scheme as defined by MPEG-DASH  (ISO/IEC 23009-1 [[!MPEGDASH]]), clause 5.8.5.5, <span class=modal-keyword>should</span> be used, with <code>@schemIdUri</code> set to <code>urn:mpeg:dash:role:2011</code>.<br>
      The DASH role scheme with the following values is expected to be recognized by a DASH-IF client for media type “video” together with the Role descriptor:
      <ul>
        <li><code>caption</code></li>
        <li><code>subtitle</code></li>
        <li><code>main</code></li>
        <li><code>alternate</code></li>
        <li><code>supplementary</code></li>
        <li><code>sign</code></li>
        <li><code>emergency</code></li>
      </ul>
      If not present, the role is assumed to be <code>main</code>.</td>
    </tr>
  </tbody>
</table>

## Video source metadata signalling ## {#video-source-metadata-signalling}

### General ### {#5.45.1-general}

Video source data <span class=modal-keyword>may</span> be used to provide details of the video content source. In general, such characteristics of video are logically independent of the compression format. In the context of DASH they are typically used in order to select a proper Adaptation Set. This clause focuses on source format description using either an <code><b>EssentialProperty</b></code> or <code><b>SupplementalProperty</b></code> descriptor.

The [table below](#t_video_src_metadata) lists a set of `@schemeIdUri` values (defined in this document or other documents) for identifying such video source characteristics.

<table id="t_video_src_metadata" class="data">
  <caption>`@schemeIdUri` values of descriptors that signal video source metadata</caption>
  <thead><tr><th>`@schemeIdUri`<th>Reference<th>Clause<th>Comment
  <tbody>
    <tr>
      <td>`urn:mpeg:mpegB:cicp:ColourPrimaries`
      <td>ISO/IEC 23091-2 [[!MPEGCICP_2]]
      <td>8.1
      <td>Indicating the chromaticity coordinates of the source colour primaries. The `@value` is the value as defined for <code><b>ColourPrimaries</b></code> in [[!MPEGCICP_2]].
    <tr>
      <td>`urn:mpeg:mpegB:cicp:TransferCharacteristics`
      <td>ISO/IEC 23091-2 [[!MPEGCICP_2]]
      <td>8.2
      <td>Indicating the opto-electronic transfer characteristic of the source colour primaries. The `@value` is the value as defined for <code><b>TransferCharacteristics</b></code> in [[!MPEGCICP_2]].
    <tr>
      <td>`urn:mpeg:mpegB:cicp:MatrixCoefficients`
      <td>ISO/IEC 23091-2 [[!MPEGCICP_2]]
      <td>8.3
      <td>Indicating the matrix coefficients used in deriving luma and chroma signals from the green, blue, and red primaries. The `@value` is the value as defined for <code><b>MatrixCoefficients</b></code> in [[!MPEGCICP_2]].
    <tr>
      <td>`urn:mpeg:mpegB:cicp:VideoFullRangeFlag`
      <td>ISO/IEC 23091-2 [[!MPEGCICP_2]]
      <td>8.3
      <td>Indicating the scaling and offset values applied in association with the matrix colour coefficients. The`@value`is the value as defined for <code><b>VideoFullRangeFlag</b></code> in [[!MPEGCICP_2]].
    <tr>
      <td>`urn:dvb:dash:hdr-dmi`
      <td>ETSI TS 103 285 [[!DVBDASH]]
      <td>5.2.6<br>5.4.8
      <td>Indicating the presence of HDR dynamic metadata information. See clause 5.5.2 for a list of defined values.
    <tr>
      <td>`urn:mpeg:mpegB:cicp:VideoFramePackingType`
      <td>ISO/IEC 23091-2 [[!MPEGCICP_2]]
      <td>8.4
      <td>Indicating the type of packing arrangement used in video frames. The`@value`is the value as defined for <code><b>VideoFramePackingType</b></code> in [[!MPEGCICP_2]].
    <tr>
      <td>`urn:mpeg:mpegB:cicp:QuincunxSamplingFlag`
      <td>ISO/IEC 23091-2 [[!MPEGCICP_2]]
      <td>8.4
      <td>Indicating whether a quincunx sampling structure is used in the frame packed video representation. The`@value`is the value as defined for <code><b>QuincunxSamplingFlag</b></code> in [[!MPEGCICP_2]].
    <tr>
      <td>`urn:mpeg:mpegB:cicp:PackedContentInterpretationType`
      <td>ISO/IEC 23091-2 [[!MPEGCICP_2]]
      <td>8.5
      <td>Indicating the intended interpretation of the constituent frames. The`@value`is the value as defined for <code><b>PackedContentInterpretationType</b></code> in [[!MPEGCICP_2]].
    <tr>
      <td>`urn:mpeg:dash:14496:10:frame_packing_arrangement_type:2011`
      <td>[[MPEGDASH]] ISO/IEC 23009-1 [[!MPEGDASH]]
      <td>5.8.5.3
      <td>For Adaptation Sets or Representations that contain a video component that conforms to ISO/IEC 14496-10 [[!AVC]], this value of `@schemeIdUri` (in this case the descriptor becomes the <code><b>FramePacking</b></code> element as defined in [[!MPEGDASH]]) <span class=modal-keyword>may</span> also be used for backward-compatibility. In this case the `@value` is the value as defined for <code><b>VideoFramePackingType</b></code> in [[!MPEGCICP_2]]. However, it is recommended to use the value `urn:mpeg:mpegB:cicp:VideoFramePackingType` instead.
    <tr>
      <td>`urn:mpeg:dash:13818:1:stereo_video_format_type:2011`
      <td>ISO/IEC 23009-1 [[!MPEGDASH]]
      <td>5.8.5.3
      <td>For Adaptation Sets or Representations that contain a video component that conforms to ISO/IEC 13818-1 [[!MPEG_TS]], this value of `@schemeIdUri` (in this case the descriptor becomes the <code><b>FramePacking</b></code> element as defined in [[!MPEGDASH]]) <span class=modal-keyword>may</span> also be used for backward-compatibility. In this case the `@value` is the value as defined for <code><b>VideoFramePackingType</b></code> in [[!MPEGCICP_2]]. However, it is recommended to use the value `urn:mpeg:mpegB:cicp:VideoFramePackingType` instead.
    <tr>
      <td>`urn:mpeg:dash:stereoid:2011`
      <td>ISO/IEC 23009-1 [[!MPEGDASH]]
      <td>5.8.5.6
      <td>When this value of `@schemeIdUri` is in use, the descriptor is also referred to as a <code><b>Role</b></code> element as specified in [[!MPEGDASH]], clause 5.8.5.6. If N views are available that can be combined into M valid stereo pairs, the <code><b>Role</b>@schemeIdURI</code> equal to this identifier signals which views form a stereo pair and which one is the left view and which one is the right view of each stereo pair. The `@value` of the <code><b>Role</b></code> element contains a space-delimited list of view indicators ‘li‘ or ‘rj’ where i, j are non-negative decimal integers.
</table>

NOTE:	The composition of the overall `@schemeIdUri` string for all codepoints defined in ISO/IEC 23091-2 [[!MPEGCICP_2]] is specified in ISO/IEC 23091-1 [[!MPEGCICP_1]].

### Source metadata signalling for HDR video ### {#5.45.2-source-metadata-signalling-for-hdr-video}

Information on colour primaries, matrix coefficients and transfer characteristics <span class=modal-keyword>may</span> be signalled using <code><b>EssentialProperty</b></code> or <code><b>SupplementalProperty</b></code> descriptors. This signalling <span class=modal-keyword>shall</span> only be applied at the <code><b>AdaptationSet</b></code> level, i.e. all Representations in one <code><b>AdaptationSet</b></code> are required to have the same colour primaries, matrix coefficients and transfer characteristics. In each case, where no descriptor is present, it <span class=modal-keyword>may</span> be assumed that the Recommendation Recommendation ITU-R BT.709 [[ITU_BT709]] value applies.

In general, <code><b>EssentialProperty</b></code> descriptors <span class=modal-keyword>shall</span> be used to indicate that the player has to support the specified colour primaries, matrix coefficients and transfer characteristics in order to correctly present any <code><b>Representation</b></code> within the <code><b>AdaptationSet</b></code>. A <code><b>SupplementalProperty</b></code> descriptor <span class=modal-keyword>may</span> be used to indicate that the <code><b>Representation</b></code>s of this <code><b>AdaptationSet</b></code> have transfer characteristics that are better described by this descriptor than any <code><b>EssentialProperty</b></code> descriptor with the same `@schemeIdUri`. This value <span class=modal-keyword>should</span> be used in preference by players that support it.

If the ColourInformationBox with a `colour_type` set to `nclx` is present in the VisualSampleEntry of the initialisation segment, this information <span class=modal-keyword>should</span> be used to write video source metadata <code><b>EssentialProperty</b></code> or <code><b>SupplementalProperty</b></code> descriptors. Otherwise, the video source metadata <span class=modal-keyword>should</span> match the respective fields of the VUI.

The [table below](#t_hdr_config) lists parameter sets for typical Wide Color Gamut (WCG) and HDR configurations.

<table  id="t_hdr_config" class="data">
  <caption>Values for typical HDR configurations</caption>
  <thead>
    <tr><th><th>SDR with BT.2020<th>HLG10 + BT.2100<th>PQ10 + BT.2100
    <tr><th>`@schemeIdUri`<th colspan=3>@value
  <tbody>
    <tr><td>`"urn:mpeg:mpegB:cicp:ColourPrimaries"`<td>9<td>9<td>9
    <tr><td>`"urn:mpeg:mpegB:cicp:MatrixCoefficients"`<td>9<td>9<td>9
    <tr><td>`"urn:mpeg:mpegB:cicp:TransferCharacteristics"`<td>14<td>18<td>16
</table>

### Signalling for presence of HDR dynamic mapping information ### {#5.45.3-signalling-for-presence-of-hdr-dynamic-mapping-information}

In addition to parameters in clause 5.5.1, if a bitstream using PQ10 contains SEI messages carrying HDR dynamic mapping information, the presence of HDR dynamic mapping information <span class=modal-keyword>should</span> be signalled using a <code><b>SupplementalProperty</b></code> with `@schemeIdUri="urn:dvb:dash:hdr-dmi"` as defined in ETSI TS 103 285 [[!DVBDASH]], with the`@value`set to one of the following options: 

* "ST2094-10": used for dynamic mapping information according to SMPTE ST 2094-10 [[SMPTE_2094_10]]  
* "ST2094-40": used for dynamic mapping information according to SMPTE ST 2094-40 [[SMPTE_2094_40]]  
* "SL-HDR2": used for dynamic mapping information according to ETSI 103 433-2 [[ETSI_103_433-2]]

Additionally, for SCTE-214 [[SCTE_214-1]] compliant systems, the presence of HDR dynamic mapping information <span class=modal-keyword>may</span> also be signalled using `scte214:supplementalCodecs` attribute with appropriate codec parameters that indicate the specific HDR dynamic metadata scheme being used.

For broader compatibility with targeted players, content providers might wish to provide the content with multiple different HDR dynamic mapping information schemes. Since the data overhead for each of these schemes is low, the provided HDR dynamic mapping information metadata tracks <span class=modal-keyword>should</span> be multiplexed into the same video base track.

When multiple different schemes are included in a bitstream, multiple instances of this descriptor <span class=modal-keyword>shall</span> be used: For each HDR dynamic metadata scheme one descriptor with `@schemeIdUri="urn:dvb:dash:hdr-dmi"` and the respective `@value` <span class=modal-keyword>shall</span> be present. Similarly, when using SCTE-214 signalling, corresponding `scte214:supplementalCodecs` entries <span class=modal-keyword>should</span> be included for each HDR dynamic metadata scheme.

It is important to note that HDR dynamic metadata can be carried in different types of SEI messages and other NAL units at the elementary stream (ES) level: These <span class=modal-keyword>may</span> include standard SEI messages defined in the video coding specifications as well as user data registered SEI messages (ITU T.35 SEI messages) that carry dynamic metadata according to SMPTE ST 2094-10 [[SMPTE_2094_10]], SMPTE ST 2094-40 [[SMPTE_2094_40]], or ETSI SL-HDR2 [[ETSI_103_433-2]]. While the coding specification of each HDR dynamic metadata scheme defines the exact location and is constrained e.g. by ETSI TS 101 154, clause L.3.3.10.4 [[ETSI_101_154]], the manifest-level signaling using a descriptor with  `@schemeIdUri="urn:dvb:dash:hdr-dmi"` or `scte214:supplementalCodecs` provides a high-level indication of the presence and type of dynamic metadata to help players determine compatibility before selecting the stream.

## Codec-specific signaling ## {#codec-specific}

### “Backward-compatible” scalable LCEVC ### {#LCEVC_NBC}

General Requirements:

1. The mapping of the CMAF content to DASH <span class=modal-keyword>shall</span> follow the DASH profile for CMAF content in ISO/IEC 23009-1.  
2. DASH packager <span class=modal-keyword>shall</span> conform to ISO/IEC 23000-19:2024/Amd 1:2024 (support for LCEVC CMAF profile and LCEVC codecs string);

<code><b>AdaptationSet</b></code> /<code><b>Representation</b></code> specific requirements:

1. One video <code><b>AdaptationSet</b></code> <span class=modal-keyword>shall</span> be present that <span class=modal-keyword>may</span> include one or multiple <code><b>Representation</b></code>s and the content of the <code><b>AdaptationSet</b></code> conforms to a base layer video codec.  
2. A second <code><b>AdaptationSet</b></code> <span class=modal-keyword>shall</span> be present, the following holds:  
   1. Each Video <code><b>Representation</b></code> <span class=modal-keyword>shall</span> conform to ISO/IEC 23094-2:2021 and Amendment 1 ISO/IEC 23094-2:2021/Amd 1:2024 (support for LCEVC);  
   2. The encoded video <span class=modal-keyword>shall</span> conform to ISO/IEC 14496-15:2022/Amd 1:2023, or <span class=modal-keyword>shall</span> conform to ISO/IEC 14496-15:2024 in which the former is incorporated (support for LCEVC in ISOBMFF, separate tracks);  
3. If a <code><b>SupplementalProperty</b></code> with `@schemeIdUri` set to `"urn:mpeg:dash:adaptation-set-switching:2016"` is present in both Enhancement Layer (EL) and Base Layer (BL) Adaptation Sets then all <code><b>Representation</b></code>s in both <code><b>AdaptationSet</b></code>s <span class=modal-keyword>should</span> have the attribute @qualityRanking as a hint to the quality level associated to each <code><b>Representation</b></code>.  
4. Both the EL and BL <code><b>AdaptationSet</b></code>s <span class=modal-keyword>may</span> signal a <code><b>SupplementalProperty</b></code> descriptor with `@schemeIdUri` set to `"urn:mpeg:dash:adaptation-set-switching:2016"`. If present in the EL <code><b>AdaptationSet</b></code>, it <span class=modal-keyword>shall</span> have a `@value`equal to the`@id`of the BL <code><b>AdaptationSet</b></code>;  
5. EL <code><b>Representation</b></code>s <span class=modal-keyword>shall</span> have attribute `@mimeType` equal to `"video/mp4"`;  
6. EL <code><b>Representation</b></code>s <span class=modal-keyword>shall</span> have attributes `@width`, `@height` and `@sar` equal to the LCEVC enhanced output video attributes as signalled in the ISO/IEC 23094-2 elementary stream and in the ISOBMFF initialisation segment;  
7. EL <code><b>Representation</b></code>s <span class=modal-keyword>shall</span> have attribute `@bandwidth` equal to the sum of the bandwidths of the EL <code><b>Representation</b></code> itself and its BL <code><b>Representation</b></code> it depends on, referenced via the `@dependencyId` attribute. This is already a normative requirement from Section 5.3.5.2 Table 9 of of ISO/IEC 23009-1:2022;

### Non-scalable LCEVC ### {#LCEVC_NS}

General Requirements:

1.  The mapping of the CMAF content to DASH <span class=modal-keyword>shall</span> follow the DASH profile for CMAF content in ISO/IEC 23009-1.  
2. DASH packager <span class=modal-keyword>shall</span> conform to ISO/IEC 23000-19:2024/Amd 1:2024 (support for LCEVC CMAF profile and LCEVC codecs string);

<code><b>AdaptationSet</b></code> / <code><b>Representation</b></code> specific requirements:

1. Video <code><b>Representation</b></code>s carrying LCEVC enhancement data <span class=modal-keyword>shall</span> conform to ISO/IEC 23094-2:2021 and ISO/IEC 23094-2:2021/Amd 1:2024.  
2. The encoded video <span class=modal-keyword>shall</span> conform to ISO/IEC 14496-15:2024.  
3. A <code><b>Representation</b></code> carrying LCEVC enhancement as additional track, <span class=modal-keyword>should</span> contain a <code><b>SubRepresentation</b></code> element.  
4. If present, the <code><b>SubRepresentation</b></code> element <span class=modal-keyword>should</span> signal characteristics of the LCEVC enhancement, as per <code><b>SubRepresentation</b></code> semantics defined in ISO/IEC 23009-1, as applicable, the following attributes <span class=modal-keyword>shall</span> be included:  
   1. `@codecs`;  
   2. `@width`;  
   3. `@height`;  
   4. `@sar`.  
5. The <code><b>SubRepresentation</b>@width</code>, <code><b>SubRepresentation</b>@height</code> and <code><b>SubRepresentation</b>@sar</code> <span class=modal-keyword>shall</span> correspond to the characteristics of the LCEVC-enhanced output video.  
6. The <code><b>SubRepresentation</b></code> element <span class=modal-keyword>shall</span> not include the <code>@bandwidth</code> attribute, to avoid ambiguity with the <code>@bandwidth</code> attribute of the parent <code><b>Representation</b></code> element.

# Playback requirements and recommendations # {#playback-requirements-and-recommendations}

## General ## {#6.1-general}

For a client supporting a media profile as outlined in clause 4, the following applies:

* It <span class=modal-keyword>shall</span> support the following playback requirements as documented in clause 8 of CTA-WAVE 5003 [[!CTA_WAVE]] for any content conforming to a CMAF switching set as defined in subclause 5.3:

  * 8.2 Sequential Track Playback

  * 8.3	Random Access to Fragment

  * 8.4 Random Access to Time

  * 8.5 Switching Set Playback

  * 8.6 Regular Playback of Chunked Content

  * 8.7 Regular Playback of Chunked Content, non-aligned append

* It <span class=modal-keyword>should</span> support the following playback requirements as documented in clause 8 of CTA-WAVE 5003 [[!CTA_WAVE]] for any content conforming to a CMAF switching set as defined in subclause 5.3:

  * 8.9 Out-Of-Order Loading

  * 8.10 Overlapping Fragments

  * 8.12 Playback of Encrypted Content

## Recommendations for track selection ## {#6.2-recommendations-for-track-selection}

It is expected that DASH clients conforming to this IOP recognize the descriptors, elements, and attributes and their values as documented in clause 5.4.

Based on the video Adaptation Sets the client selects one from the signalling as follows:

1. Any video Adaptation Set for which  
   1. the client does not have a decoder (based on the `@codecs` string), or  
   2. an <code><b>EssentialProperty</b></code> descriptor is present for which the scheme or value is not understood by the DASH client, or  
   3. the DRM system in the <code><b>ContentProtection</b></code> element string is not supported, or  
   4. the client does not have rendering capabilities (per clause 6.3)

   is excluded from the selection.

2. If video language preference settings are provided to the client by the system, the client prioritizes them based on the following descriptors, elements and attributes:  
   1. <code><b>Viewpoint</b></code>  
   2. <code><b>Role</b></code>  
   3. <code><b>Accessibility</b></code>  
   4. <code><b>SupplementalProperty</b></code> and <code><b>EssentialProperty</b></code>  
   5. `@lang`
   6. Others

   If accessibility preferences (e.g. burned-in captions, sign language) are provided to the client by the system, any Adaptation Set from the selection where the <code><b>Accessibility</b></code> descriptor matches the accessibility preferences is prioritized. Otherwise, if no accessibility preferences are provided to the client by the system, any Adaptation Set from the selection where no <code><b>Accessibility</b></code> descriptor is present is prioritized.

3. If multiple video Adaptation Sets remain, then the ones with the highest value of `@selectionPriority` is chosen.  
4. If multiple video Adaptation Sets remain, then the DASH client makes a choice for itself, possibly on a random basis.

## Capability discovery for HDR metadata ## {#6.3-capability-discovery-for-hdr-metadata}

### General ### {#6.3.1-general}

This clause provides guidance on how HDR video source metadata parameters specified in clause 5.5.2 <span class=modal-keyword>should</span> be mapped to media capabilities API fields for capability discovery. This mapping enables DASH clients to properly assess device capabilities before selecting HDR content streams.

### Video metadata parameter mapping ### {#6.3.2-video-metadata-parameter-mapping}

The video metadata parameters including SDR and HDR  signaled through <code><b>EssentialProperty</b></code> or <code><b>SupplementalProperty</b></code> descriptors as defined in clause 5.5.2 <span class=modal-keyword>may</span> be mapped to the corresponding media capabilities API fields as specified in the tables below. Note that tables document additional code points beyond those identified in clause 5.

Also note that CTA-5003-B [[!CTA_WAVE]] provides detailed mapping recommendations for a selected list of video media profiles.

<table id="t_mca_colorPrim" class="data">
  <caption>Mapping of DASH descriptors with `@schemeIdUri="urn:mpeg:mpegB:cicp:ColourPrimaries"` to W3C MediaCapabilities-API `colorGamut`</caption>
  <thead><tr><th>DASH descriptor `@value`<th>Media Capabilities API value for `colorGamut`
  <tbody>
    <tr><td>1, 5, 6, 7<td>`srgb`
    <tr><td>9<td>`rec2020`
    <tr><td>11, 12<td>`p3`
</table>

<table id="t_mca_transfer" class="data">
  <caption>Mapping of DASH descriptors with `@schemeIdUri="urn:mpeg:mpegB:cicp:TransferCharacteristics"` to W3C MediaCapabilities-API `transferFunction` field</caption>
  <thead><tr><th>DASH descriptor `@value`<th>Media Capabilities API value for `transferFunction`
  <tbody>
    <tr><td>1, 6, 13, 14, 15<td>`srgb`
    <tr><td>16<td>`pq`
    <tr><td>18<td>`hlg`
</table>

Note: Media Capabilities API does not provide a direct mapping for DASH descriptor values with `@schemeIdUri="urn:mpeg:mpegB:cicp:MatrixCoefficients"`.

### HDR dynamic metadata capability mapping ### {#6.3.3-hdr-dynamic-metadata-capability-mapping}

When HDR dynamic metadata is present as signaled by a descriptor with `@schemeIdUri="urn:dvb:dash:hdr-dmi"`, it is recommended that the capability discovery includes dynamic metadata support assessment as specified in the [table below](#t_mca_hdr-dmi).


<table id="t_mca_hdr-dmi" class="data">
  <caption>Mapping of DASH descriptors with `@schemeIdUri=”urn:dvb:dash:hdr-dmi”` to W3C MediaCapabilities-API `hdrMetadataType`</caption>
  <thead><tr><th>DASH descriptor `@value`<th>Media Capabilities API value for `hdrMetadataType`<th>
  <tbody>
    <tr><td>ST2094-10<td>`smpte2094-10`
    <tr><td>ST2094-40<td>`smpte2094-40`
    <tr><td>SL-HDR2<td>`sl-hdr2`
</table>

## Codec-specific considerations ## {#playback_codec-specific}

### Support for “backward-compatible” scalable LCEVC ### {#playback_LCEVC_BC}

In general terms, in addition to supporting LCEVC decoding:

1. Client supports a Switching Set from two merged <code><b>AdaptationSet</b></code>s (BL + EL), see `schemeIdUri="urn:mpeg:dash:adaptation-set-switching:2016"`
2. Client supports “dependent representations” as defined in section 3.1.12, 5.3.5 of ISO/IEC 23009-1 and therefore supports two stream processing pipelines for both dependent (EL) and complementary representation (BL).   
3. Client supports parsing of BL and EL encoded data from separate buffer input streams   
4. Client supports the `@selectionPriority` attribute with the <code><b>AdaptationSet</b></code> element, in all use cases where the adaptation-set-switching property is not used, in order to prioritize the EL <code><b>AdaptationSet</b></code> over the BL one.

### Support for non-scalable LCEVC ### {#playback_LCEVC_NS}

A client supporting this feature <span class=modal-keyword>should</span> inspect the <code><b>SubRepresentation</b></code> element associated with a <code><b>Representation</b></code>.

If a <code><b>SubRepresentation</b></code> element is present and signals an LCEVC codec, the client <span class=modal-keyword>may</span> use the information signalled therein to initialize LCEVC-specific processing prior to retrieval of the initialization segment.

Clients that do not support this feature <span class=modal-keyword>should</span> ignore the <code><b>SubRepresentation</b></code> element in accordance with existing DASH processing rules.

# Annex A (informative) # {#annex}
## Change History ## {#change_history}

<table class="data">
  <caption>Part 7 Video - Change History</caption>
  <thead><tr><th>Date<th>Version<th>Information about changes
  <tbody>
    <tr>
      <td>2021-07-09
      <td>Initial draft
      <td> By Michael Dolan, with a Skelton of which codecs <span class=modal-keyword>should</span> be in this document, with the intent to capture all known CMAF video profiles and aligning with WAVE.
    <tr>
      <td>2021-09-02
      <td>Second draft
      <td>By Ye-Kui Wang, with the following changes made, along with various minor improvements:
        <ul>
          <li>Added a bunch of references, including for the codec specs, some additional file format specs, the latest CICP video and systems specs, and CTA-5003.
          <li>Split the VVC and EVC media profiles to a separate table, such that they are “CMAF Video Media Profiles provided for information”, while the AVC and HEVC media profiles are “Recommended CMAF Video Media Profiles”.
          <li>Added four columns to the tables, for video codec, profile, tier, and level, and added missing example `@codecs`values.
          <li>Changed the title of Clause 5 from “Adaption Set requirements and recommendations” to “Mapping to delivery”, in a manner similar to what is in 3GPP TS 26.511, and then added the following subclauses similarly as in 3GPP TS 26.511:
            <ul>
              <li>5.1 File format track definition
              <li>5.2 CMAF track definition
              <li>5.3 CMAF switching set definition
            </ul>
          <li>Added a subclause with the integration of the video source metadata signalling (i.e., the`@schemeIdUri`values) from [https://dashif.org/identifiers/video_source_metadata/](https://dashif.org/identifiers/video_source_metadata/), with some updates, e.g., by referencing to the latest CICP specs, etc.
          <li>Added Clause 6, titled "Playback requirements and recommendations", similarly as in 3GPP TS 26.511.
        </ul>
    <tr>
      <td>2021-12-29
      <td>Third draft
      <td>By Ye-Kui Wang, with the following changes made:
        <ul>
          <li>Added executive summary,
          <li>updated references,
          <li>removed some of the video media profiles, and
          <li>added a pointer to the DASH-IF video codec registration page
        </ul>
    <tr>
      <td>2022-05-31
      <td>V5.0.0
      <td>Published on DASH-IF web page
    <tr>
      <td>2025-02-14
      <td>V5.0.1
      <td>By Stephan Schreiner, with the following changes:
        <ul>
          <li>Added Source Metadata for HDR Video and HDR dynamic mapping information,
          <li>added track selection recommendations,
          <li>fixed references to MPEG-CICP in Table 2
        </ul>
    <tr>
      <td>2025-12-17
      <td>v5.0.2
      <td>DASH-IF WG Call addressing updates
    <tr>
      <td>2026-08-10
      <td>v5.0.3
      <td>By Stephan Schreiner, with the following changes:
        <ul>
          <li>added LCEVC per amendment document,
          <li>converted to Bikeshed
        </ul>
</table>
