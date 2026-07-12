<!--
  Part 9: Text.
  Initial Bikeshed/Markdown shell following the IOPv5 authoring convention.
  Source grounding / migration target: iop-docs-overview / media mapping placeholders.
  Normative content in this revision is migrated from:
  - Dash-Industry-Forum/DASH-IF-IOP branch v5-old-draft, 80-Codecs.inc.md
    (CEA-608/708 closed captioning, IMSC1 timed text clauses)
  - Dash-Industry-Forum/DASH-IF-IOP branch v5-old-draft, 27-AdaptationSets.inc.md
    (text adaptation set constraints)
-->

# Scope # {#scope}

This document specifies DASH-IF IOP v5 Part 9: **Text**. Subtitle and caption interoperability points, coding profiles, packaging, and DASH signalling.

# References # {#doc-references}

The following referenced documents are necessary for the application of this
part:

- ISO/IEC 23009-1 [[!MPEGDASH]].
- ISO/IEC 23000-19 [[!MPEGCMAF]].
- W3C TTML2 and the W3C IMSC1 text and image profiles.
- CEA-708 / SCTE 128-1, Digital Television (DTV) Closed Captioning.
- DASH-IF IOP v5 Part 2, *Core Principles and CMAF Mapping*.
- DASH-IF IOP v5 Part 12, *Conformance and Reference Tools*.

# Terms and Definitions # {#terms}

Terms and definitions are inherited from ISO/IEC 23009-1, ISO/IEC 23000-19, and
Part 2 unless defined in this part.

A <dfn export>text adaptation set</dfn> is an Adaptation Set that contains visual overlay information to be rendered as auxiliary or accessibility information. Such an Adaptation Set is identified by one of:

* `@mimeType="application/mp4"` and a `@codecs` parameter of a text coding technology defined in this part.
* `@mimeType="application/ttml+xml"` with no `@codecs` parameter.

# Text Adaptation Set Constraints # {#text-constraints}

Text adaptation sets <span class=modal-keyword>should</span> be annotated using descriptors defined by DASH, specifically `Role`, `Accessibility`, `EssentialProperty` and `SupplementalProperty` descriptors.

# CEA-608/708 Digital Television (DTV) Closed Captioning # {#codecs-cea608}

This clause defines requirements for interoperable use of CEA-608/708 Digital Television (DTV) Closed Captioning in DASH presentations.

Note: This clause is compatible with SCTE specification DVS 1208 and therefore SCTE URNs are used for the descriptor `@schemeIdUri`.

CEA-608/708 captions <span class=modal-keyword>shall</span> be carried in SEI messages embedded in Representations of a video adaptation set, with the encapsulation as defined in SCTE 128-1, section 8.1.

Every Representation in the video adaptation set <span class=modal-keyword>shall</span> have identical CEA-608/708 captions. Both CEA-608 and CEA-708 <span class=modal-keyword>may</span> be present simultaneously in the same video adaptation set.

The presence of CEA-608/708 captions <span class=modal-keyword>shall</span> be signaled by an `Accessibility` descriptor on the adaptation set level, with `@schemeIdUri="urn:scte:dash:cc:cea-608:2015"` or `@schemeIdUri="urn:scte:dash:cc:cea-708:2015"`, with an optional `@value`.

When present for CEA-608 captions, the `@value` of this descriptor <span class=modal-keyword>shall</span> describe the caption streams and languages in conformance to the ABNF below.

```
@value          = (channel *3 [";" channel]) / (language *3[";" language])
channel         = channel-number "=" language
channel-number  = CC1 | CC2 | CC3 | CC4
language        = 3ALPHA ; language code per ISO 639.2/B
```

Two variants of `@value` syntax for CEA-608 are described above: a variant with plain language codes and a variant with caption channel numbers. Services <span class=modal-keyword>should</span> use the variant with channel numbers.

Note: This part does not provide the `@value` syntax for CEA-708.

<div class="example">
Signaling of presence of CEA-608 closed caption service in English and German:

<xmp highlight="xml">
<Accessibility schemeIdUri="urn:scte:dash:cc:cea-608:2015" value="CC1=eng;CC3=deu"/>
</xmp>

</div>

# Timed Text (IMSC1) # {#codecs-imsc1}

This clause defines requirements for using IMSC1 text in DASH presentations.

W3C TTML and its various profiles — W3C IMSC1 (text and image profiles), SMPTE Timed Text, and EBU Timed Text — provide a rich feature set for text tracks. Beyond basic subtitles and closed captioning, graphics-based subtitles and closed captioning are also supported by IMSC1.

Advisement: Many clients only implement a subset of IMSC1. The exact feature sets used by clients and services may need careful alignment to ensure mutual compatibility. Do not assume that all of IMSC1 is supported by typical clients — this is unlikely.

Conversion of CEA-608 and CEA-708 into IMSC1 <span class=modal-keyword>shall</span> be done according to SMPTE 2052-10 and SMPTE 2052-11, respectively.

One of the following storage formats <span class=modal-keyword>shall</span> be used for IMSC1 Representations:

* ISO BMFF Media Segments.
* Stand-alone XML file (one file per Representation).

The ISO BMFF encapsulated form <span class=modal-keyword>should</span> be used, as stand-alone XML file storage has significant limitations.

The signaling in the MPD <span class=modal-keyword>shall</span> conform to the below table.

<table class="data">
  <caption>IMSC1 signaling parameters.</caption>
  <thead><tr><th>Codec<th>Storage<th>`@mimeType`<th>`@codecs`
  <tbody>
    <tr><td>IMSC1 Timed Text<td>Stand-alone XML file<td>`application/ttml+xml`<td rowspan="2">See W3C TTML Profile Registry
    <tr><td>IMSC1 Timed Text<td>ISO BMFF encapsulation<td>`application/mp4`
</table>

# Requirements and Recommendations # {#requirements}

Issue: The above clauses migrate the CEA-608/708 closed captioning, IMSC1 timed
text, and text-adaptation-set constraints from
Dash-Industry-Forum/DASH-IF-IOP branch v5-old-draft, 80-Codecs.inc.md and
27-AdaptationSets.inc.md. Remaining migration work: standalone-XML-file text
timing considerations (referenced as `#standalone-text-timing` in the source)
and reconciliation with the current edition of W3C TTML2/IMSC1.
[GROUNDED_BY=Dash-Industry-Forum/DASH-IF-IOP@v5-old-draft:80-Codecs.inc.md]

# Open Issues and Work Items # {#open-issues}

<table class="data">
  <caption>Part 9 open issues and topics to progress.</caption>
  <thead><tr><th>Topic<th>Status<th>Next action
  <tbody>
    <tr><td>Source migration<td>In progress<td>CEA-608/708 and IMSC1 clauses migrated from DASH-IF-IOP v5-old-draft. Standalone-XML-file text timing considerations remain to be migrated.
    <tr><td>Cross-part alignment<td>Open<td>Align terminology and references with Parts 1, 2, and 12.
    <tr><td>Conformance mapping<td>Open<td>Identify validator/test-asset/reference-player expectations and link them to Part 12.
</table>

# Change History # {#change-history}

<table class="data">
  <caption>Part 9 change history.</caption>
  <thead><tr><th>Version<th>Date<th>Change
  <tbody>
    <tr><td>0.1<td>Initial<td>Created initial Bikeshed/Markdown shell for Part 9.
    <tr><td>0.2<td>Migration<td>Migrated CEA-608/708 and IMSC1 text codec clauses from DASH-IF-IOP v5-old-draft.
</table>