<!--
  Part 9: Text.
  Reconciled against DASH-IF IOP v5.0.0 Part 9 FINAL.
  Current status: Draft/reconciliation.
-->

# Introduction # {#part9-introduction}

This document specifies DASH-IF IOP v5 Part 9: **Text**.

The present document defines the CMAF Media Profiles and DASH signalling for
text tracks, including subtitles and captions, as well as open captions and
subtitles in video tracks. This work is derived from DASH-IF IOP v4.3, but does
not include non-CMAF profiles.

Issue: This part is under reconciliation against the published DASH-IF IOP
v5.0.0 Part 9 FINAL document. See
`rag/reports/reconcile-part09-text.md` for the clause crosswalk and remaining
table/reference verification items.

# Scope # {#scope}

This part defines CMAF media profiles and DASH signalling for text tracks,
including subtitles and captions, as well as open captions and subtitles in
video tracks.

The use of sidecar text files is not covered in this part.

# References # {#doc-references}

The following referenced documents are necessary for the application of this
part:

- ISO/IEC 23009-1 [[!MPEGDASH]].
- ISO/IEC 23000-19 [[!MPEGCMAF]].
- ISO/IEC 14496-30 [[!ISO14496-30]].
- SCTE 214-1 [[!SCTE214-1]].
- SCTE 128-1 [[SCTE128-1]].
- W3C TTML Profiles for Internet Media Subtitles and Captions 1.0.1 (IMSC1) [[IMSC1]].
- W3C WebVTT [[WEBVTT]].
- CTA-608-E [[CTA608-E]].
- CTA-708-E [[CTA708-E]].
- DASH-IF IOP v4.3 [[DASHIF-IOP43]].
- DASH-IF IOP v5 Part 7, *Video* [[DASHIF-IOP5-PART7]].
- DASH-IF IOP v5 Part 12, *Conformance and Reference Tools*.

# Terms and Definitions # {#terms}

Terms and definitions are inherited from ISO/IEC 23009-1, ISO/IEC 23000-19, and
Part 2 unless defined in this part.

For the purposes of this part, the following terms apply:

- <dfn export>caption</dfn>: Text that transcribes audio dialogue, often includes non-verbal sounds, and is primarily provided for accessibility.
- <dfn export>closed caption</dfn>: Caption encoded in a separate text track or encoded in video-track SEI messages.
- <dfn export>closed subtitle</dfn>: Subtitle encoded in a separate text track or encoded in video-track SEI messages.
- <dfn export>open caption</dfn>: Caption encoded in video-track pixels.
- <dfn export>open subtitle</dfn>: Subtitle encoded in video-track pixels.
- <dfn export>subtitle</dfn>: Text that transcribes audio dialogue, often in a language different from the audio, and is primarily provided for translation.

A <dfn export>text adaptation set</dfn> is an Adaptation Set that contains visual
overlay information to be rendered as auxiliary or accessibility information.
Such an Adaptation Set is identified by one of:

* `@mimeType="application/mp4"` and a `@codecs` parameter of a text coding technology defined in this part.
* `@mimeType="application/ttml+xml"` with no `@codecs` parameter.

## Symbols and abbreviations ## {#symbols-abbreviations}

For the purposes of this part, the following abbreviations apply:

<table class="data">
  <caption>Part 9 abbreviations.</caption>
  <thead><tr><th>Abbreviation<th>Meaning
  <tbody>
    <tr><td>CMAF<td>Common Media Application Format
    <tr><td>CTA<td>Consumer Technology Association
    <tr><td>DASH<td>Dynamic Adaptive Streaming over HTTP
    <tr><td>IEC<td>International Electrotechnical Commission
    <tr><td>IMSC<td>Internet Media Subtitles and Captions
    <tr><td>IOP<td>Interoperability Points
    <tr><td>ISO<td>International Organization for Standardization
    <tr><td>Kbps<td>Kilobits per second
    <tr><td>MPD<td>Media Presentation Description
    <tr><td>SEI<td>Supplemental Enhancement Information
    <tr><td>VTT<td>Video Text Tracks
    <tr><td>XML<td>Extensible Markup Language
</table>

# CMAF Media Profiles # {#text-cmaf-media-profiles}

Text CMAF media profiles <span class=modal-keyword>shall</span> be as defined
in [[!MPEGCMAF]] clauses 11, A.4 and A.5, including IMSC, WebVTT, and CTA
608/708. `@codecs` values for WebVTT and IMSC1 <span class=modal-keyword>shall</span>
be as defined in [[!ISO14496-30]].

CTA 608/708 <span class=modal-keyword>may</span> be carried in a CMAF video track
in SEI messages and does not have a separate `@mimeType` or `@codecs` value in a
text Adaptation Set. Its presence is signalled using the applicable video file
brand and video Adaptation Set descriptors. Only CTA-608 is defined for use here,
but it is carried in a CTA-708 DTVCC wrapper and is therefore referred to as
CTA-608/708.

CTA 608/708 does not have an independent timing model; it is bound to video
frames. To the extent that video is properly groomed for the Period, the CTA
608/708 data is aligned with it.

Open captions and open subtitles are addressed in DASH-IF IOP v5 Part 7,
*Video* [[DASHIF-IOP5-PART7]].

<table class="data">
  <caption>CMAF Media Profile parameters.</caption>
  <thead><tr><th>Media Profile<th>File Brand<th>`@mimeType`<th>`@codecs`<th>Reference
  <tbody>
    <tr><td>IMSC1 Text<td>`im1t`<td>`application/mp4`<td>`stpp.ttml.im1t`<td>[[!MPEGCMAF]]
    <tr><td>IMSC1 Image<td>`im1i`<td>`application/mp4`<td>`stpp.ttml.im1i`<td>[[!MPEGCMAF]]
    <tr><td>WebVTT<td>`cwvt`<td>`application/mp4`<td>`wvtt`<td>[[!MPEGCMAF]]
    <tr><td>CTA 608/708<td>`ccea`<td>n/a<td>n/a<td>[[!MPEGCMAF]]
</table>

Additional non-CMAF text/subtitle profiles are outside the scope of this part
and can be found in [[DASHIF-IOP43]].

# Adaptation Set requirements and recommendations # {#adaptation-set-requirements}

Text adaptation sets <span class=modal-keyword>should</span> be annotated using
descriptors defined by DASH, specifically `Role`, `Accessibility`,
`EssentialProperty`, and `SupplementalProperty` descriptors.

# Content requirements # {#content-requirements}

## Text tracks ## {#text-tracks}

In addition to the general provisions defined in IOP v5 Part 2, text Adaptation
Sets <span class=modal-keyword>shall</span> comply with the provisions of the
following table.

<table class="data">
  <caption>Text track Adaptation Set attributes and elements.</caption>
  <thead><tr><th>DASH attribute or element<th>Use for media type<th>Detailed usage in DASH-IF IOPs
  <tbody>
    <tr><td>`@mimeType`<td>M<td>This <span class=modal-keyword>shall</span> be set to one of the `@mimeType` values defined in the CMAF Media Profile table.
    <tr><td>`@codecs`<td>M<td>If `@mimeType` is set to `application/mp4`, this attribute <span class=modal-keyword>shall</span> be present and set to one of the `@codecs` values defined in the CMAF Media Profile table.
    <tr><td>`@lang`<td>M<td>The `@lang` attribute <span class=modal-keyword>shall</span> be present and set according to DASH language rules. Language is used as the primary selection mechanism based on user preference.
    <tr><td>`Accessibility`<td>0 … N<td>If the text track is closed captions, an `Accessibility` descriptor <span class=modal-keyword>shall</span> be present with `@schemeIdUri="urn:mpeg:dash:role:2011"` and `@value="caption"`.
    <tr><td>`Role`<td>0 … N<td>`Role` descriptors <span class=modal-keyword>may</span> be present depending on the nature of the text. Subtitle tracks <span class=modal-keyword>should</span> use `@value="subtitle"`. Closed-caption tracks <span class=modal-keyword>shall</span> use `@value="caption"`. Text tailored to beginning readers <span class=modal-keyword>shall</span> use `@value="easyreader"` when signalled.
</table>

Text Adaptation Sets containing alternative content <span class=modal-keyword>shall</span>
differ by at least one of the following annotation labels:

- `@codecs`, specifying the codec present within the Representation.
- `@lang`, specifying the language of the subtitle with a non-null language code.
- An `Accessibility` descriptor with DASH role scheme `urn:mpeg:dash:role:2011` and value `caption`.
- One or more `Role` descriptors with DASH role scheme `urn:mpeg:dash:role:2011`.

## Video tracks ## {#video-tracks}

In addition to text tracks, CTA 608/708 captions can be carried in video tracks.
This can be done by open subtitles or open captions coded into video pixels, or
by carrying closed captions in video SEI messages according to [[SCTE128-1]].
This section addresses closed captions in video SEI messages.

<table class="data">
  <caption>Video track Adaptation Set attributes and elements for text-related signaling.</caption>
  <thead><tr><th>DASH attribute or element<th>Use for media type<th>Detailed usage in DASH-IF IOPs
  <tbody>
    <tr><td>`Accessibility`<td>0 … N<td>If the video Adaptation Set contains CTA 608/708 closed captions, this element <span class=modal-keyword>shall</span> be present and used as defined by DASH and [[!SCTE214-1]] caption-service signalling. For other uses of `Accessibility` with a video track, including open captions and open subtitles, see DASH-IF IOP v5 Part 7 [[DASHIF-IOP5-PART7]].
</table>

Since this is a video Adaptation Set, `@mimeType` and `@codecs` are set according
to the video codec.

# CEA-608/708 Digital Television (DTV) Closed Captioning # {#codecs-cea608}

This clause defines requirements for interoperable use of CEA-608/708 Digital
Television (DTV) Closed Captioning in DASH presentations.

Note: This clause is compatible with SCTE specification DVS 1208 and therefore
SCTE URNs are used for the descriptor `@schemeIdUri`.

CEA-608/708 captions <span class=modal-keyword>shall</span> be carried in SEI
messages embedded in Representations of a video Adaptation Set, with the
encapsulation as defined in SCTE 128-1, section 8.1.

Every Representation in the video Adaptation Set <span class=modal-keyword>shall</span>
have identical CEA-608/708 captions. Both CEA-608 and CEA-708
<span class=modal-keyword>may</span> be present simultaneously in the same video
Adaptation Set.

The presence of CEA-608/708 captions <span class=modal-keyword>shall</span> be
signaled by an `Accessibility` descriptor on the Adaptation Set level, with
`@schemeIdUri="urn:scte:dash:cc:cea-608:2015"` or
`@schemeIdUri="urn:scte:dash:cc:cea-708:2015"`, with an optional `@value`.

When present for CEA-608 captions, the `@value` of this descriptor
<span class=modal-keyword>shall</span> describe the caption streams and languages
in conformance to the ABNF below.

```
@value          = (channel *3 [";" channel]) / (language *3[";" language])
channel         = channel-number "=" language
channel-number  = CC1 | CC2 | CC3 | CC4
language        = 3ALPHA ; language code per ISO 639.2/B
```

Two variants of `@value` syntax for CEA-608 are described above: a variant with
plain language codes and a variant with caption channel numbers. Services
<span class=modal-keyword>should</span> use the variant with channel numbers.

When there is only a single caption channel present, the language-only form
<span class=modal-keyword>may</span> be used.

When more than one caption channel is present, the language-only form
<span class=modal-keyword>should not</span> be used.

Note: This part does not provide the `@value` syntax for CEA-708.

<div class="example">
Signaling of presence of CEA-608 closed caption service in English and Spanish:

<xmp highlight="xml">
<Accessibility schemeIdUri="urn:scte:dash:cc:cea-608:2015" value="CC1=eng;CC3=spa"/>
</xmp>

</div>

# Timed Text (IMSC1) # {#codecs-imsc1}

This clause defines requirements for using IMSC1 text in DASH presentations.

W3C TTML and its various profiles — W3C IMSC1 text and image profiles, SMPTE
Timed Text, and EBU Timed Text — provide a rich feature set for text tracks.
Beyond basic subtitles and closed captioning, graphics-based subtitles and closed
captioning are also supported by IMSC1.

Advisement: Many clients only implement a subset of IMSC1. The exact feature
sets used by clients and services may need careful alignment to ensure mutual
compatibility. Do not assume that all of IMSC1 is supported by typical clients.

Conversion of CEA-608 and CEA-708 into IMSC1 <span class=modal-keyword>shall</span>
be done according to SMPTE 2052-10 and SMPTE 2052-11, respectively.

One of the following storage formats <span class=modal-keyword>shall</span> be
used for IMSC1 Representations:

* ISO BMFF media segments.
* Stand-alone XML file, one file per Representation.

The ISO BMFF encapsulated form <span class=modal-keyword>should</span> be used,
as stand-alone XML file storage has significant limitations.

The signaling in the MPD <span class=modal-keyword>shall</span> conform to the
below table.

<table class="data">
  <caption>IMSC1 signaling parameters.</caption>
  <thead><tr><th>Codec<th>Storage<th>`@mimeType`<th>`@codecs`
  <tbody>
    <tr><td>IMSC1 Timed Text<td>Stand-alone XML file<td>`application/ttml+xml`<td rowspan="2">See W3C TTML Profile Registry
    <tr><td>IMSC1 Timed Text<td>ISO BMFF encapsulation<td>`application/mp4`
</table>

# Chunks and gaps # {#chunks-and-gaps}

Text is low bitrate, but has different characteristics compared to audio. In
particular, for IMSC1 there is typically only one sample/document in each
segment. Text <span class=modal-keyword>should not</span> be chunked but
delivered as separate segments/documents.

Even with short segment duration, encoders <span class=modal-keyword>shall</span>
conform to the IMSC1 Hypothetical Render Model (HRM), applied inter-segment.

When a text track contains a period of no content, continuous segments
<span class=modal-keyword>shall</span> still be present and
<span class=modal-keyword>shall</span> contain the empty document as defined in
ISO/IEC 14496-30.

# Client recommendations # {#client-recommendations}

It is expected that DASH clients conforming to this IOP recognize the
descriptors, elements, attributes, and values documented in the text-track and
video-track Adaptation Set tables.

If caption or subtitle text rendering is enabled, the client selects text
Adaptation Sets as follows:

1. Any text Adaptation Set for which an `EssentialProperty` descriptor is present and for which the scheme or value is not understood by the DASH client is excluded from the selection.
2. Any text Adaptation Set for which the client does not have a decoder, such as CTA 608/708, IMSC1, or WebVTT, is excluded from the selection.
3. If text language preference settings are provided to the client by the system, any Adaptation Set for which `@lang` is absent, null, or set to `und` is excluded from the selection, and any Adaptation Set that is not in the preferred text language is excluded from the selection.
4. Any text Adaptation Set with one or more `Role` descriptors using `@schemeIdUri="urn:mpeg:dash:role:2011"` where none of the `@value` values is described in this part is excluded from the selection.
5. If multiple text Adaptation Sets remain, the one with the highest `@selectionPriority` value is chosen.
6. If multiple text Adaptation Sets remain after the above steps, the DASH client makes a choice for itself.

Note: Text in video tracks does not affect video-track selection.

# Requirements and Recommendations # {#requirements}

Issue: The above clauses reconcile the initial Part 9 Bikeshed source with the
published DASH-IF IOP v5.0.0 Part 9 FINAL structure. Remaining migration work is
to verify exact values in the published tables, confirm bibliographic aliases,
and link testable requirements to Part 12 conformance mapping.
[GROUNDED_BY=rag/corpus/published/DASH-IF-IOPv5.0.0-Part9-FINAL.docx.extracted.txt]

# Open Issues and Work Items # {#open-issues}

<table class="data">
  <caption>Part 9 open issues and topics to progress.</caption>
  <thead><tr><th>Topic<th>Status<th>Next action
  <tbody>
    <tr><td>Published v5.0.0 reconciliation<td>In progress<td>Initial structure and core requirements migrated. Verify exact published table values against `rag/reports/reconcile-part09-text.md`.
    <tr><td>Reference mapping<td>Open<td>Confirm bibliographic aliases for ISO/IEC 14496-30, SCTE 214-1, IMSC1/TTML, DASH-IF IOP v4.3, and Part 7 Video.
    <tr><td>Cross-part alignment<td>Open<td>Align terminology and references with Parts 1, 2, 7, and 12.
    <tr><td>Conformance mapping<td>Open<td>Identify validator/test-asset/reference-player expectations and link them to Part 12.
</table>

# Change History # {#change-history}

<table class="data">
  <caption>Part 9 change history.</caption>
  <thead><tr><th>Version<th>Date<th>Change
  <tbody>
    <tr><td>0.1<td>Initial<td>Created initial Bikeshed/Markdown shell for Part 9.
    <tr><td>0.2<td>Migration<td>Migrated CEA-608/708 and IMSC1 text codec clauses from DASH-IF-IOP v5-old-draft.
    <tr><td>0.3<td>Reconciliation<td>Added published DASH-IF IOP v5.0.0 Part 9 FINAL structure, CMAF media-profile table, adaptation-set requirements, chunks/gaps, and client recommendations.
    <tr><td>5.0.0<td>2022-01-04<td>Version published as Part 9 v5.0.0.
</table>