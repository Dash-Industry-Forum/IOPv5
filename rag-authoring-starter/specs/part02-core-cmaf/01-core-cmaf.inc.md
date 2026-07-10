<!--
  Part 2: Core principles and CMAF mapping.
  Drafted from:
  - dashif-iop-v5-part2-draft#10..#129 (Part 2 working draft)
  - dashif-iop-v4-3#30..#42 (timing/adaptation-set basics)
  - dashif-iop-v4-3#74..#90 (on-demand/live-profile and multi-period basics)
  - dashif-iop-v4-3#192..#206, #242..#247 (period/adaptation-set carry-over)
  - iso-iec-23009-1-2026-merged-r5 and iso-iec-23000-19-2024 as normative baselines
  This is intentionally a consolidated working draft with Issues marking topics
  that still need editorial or technical closure.
-->

# Scope # {#scope}

This document specifies the core principles for DASH-IF IOP v5 and the mapping of
CMAF content structures to DASH Media Presentations. It defines the shared DASH
and CMAF concepts used by the other parts, including the Media Presentation,
DASH timing model, Segment information, CMAF-to-DASH mappings, multi-Period CMAF
content, bandwidth signalling, static and dynamic services, MPD updates, MPD and
Segment locations, and gap handling.

This part is normative for the common structures used by the other IOP v5 parts.
Media-specific constraints are defined in Parts 7, 8, and 9; live and low-latency
service constraints are defined in Part 4; on-demand-service constraints are
defined in Part 3; content protection constraints are defined in Part 6; ad
insertion and content replacement constraints are defined in Part 5.

Issue: This Part 2 draft is a consolidated migration from the Part 2 working
draft and v4.3. Several tables and precise formulae from the working draft remain
to be reconstructed and reviewed against the current edition of ISO/IEC 23009-1
and ISO/IEC 23000-19. See [[#open-issues]].

# References # {#doc-references}

The following referenced documents are necessary for the application of this
part:

- ISO/IEC 23009-1, *Dynamic adaptive streaming over HTTP (DASH) — Part 1: Media
    presentation description and segment formats* [[!MPEGDASH]].
- ISO/IEC 23000-19, *Common media application format (CMAF) for segmented media*
    [[!MPEGCMAF]].
- ISO/IEC 14496-12, *ISO base media file format* [[!ISOBMFF]].
- DASH-IF IOP v5 Part 1, *Overview, Architecture and Interfaces*.
- DASH-IF IOP v5 Part 12, *Conformance and Reference Tools*.

# Terms, Definitions, Symbols and Abbreviations # {#terms}

## Terms and Definitions ## {#terms-definitions}

For the purposes of this document, the terms and definitions in ISO/IEC 23009-1
[[!MPEGDASH]], ISO/IEC 23000-19 [[!MPEGCMAF]], and the following apply.

: <dfn export>DASH-IF Media Presentation</dfn>
:: A DASH Media Presentation that conforms to the requirements and
    recommendations of the applicable DASH-IF IOP v5 parts.
: <dfn export>CMAF Presentation</dfn>
:: A presentation as defined by CMAF, consisting of CMAF Selection Sets and CMAF
    Tracks intended for synchronized playback.
: <dfn export>CMAF Selection Set</dfn>
:: A CMAF grouping of alternative CMAF Switching Sets from which one Switching
    Set can be selected for a media component.
: <dfn export>CMAF Switching Set</dfn>
:: A CMAF set of CMAF Tracks that are alternatives for switching during playback.
: <dfn export>CMAF Track</dfn>
:: A CMAF media track carried in a CMAF Track File or as a sequence of CMAF
    Segments.
: <dfn export>CMAF Header</dfn>
:: CMAF initialization information for a CMAF Track, analogous in DASH to an
    Initialization Segment.
: <dfn export>CMAF Segment</dfn>
:: A CMAF addressable media object, analogous in DASH to a Media Segment.
: <dfn export>CMAF Chunk</dfn>
:: A CMAF sub-segment object that may be made available progressively; relevant
    for low-latency services in Part 4.
: <dfn export>Good Multi-Period CMAF Content</dfn>
:: Multi-Period DASH content whose Period boundaries and CMAF Track structure
    permit continuous playback, switching, and decoder operation across Periods
    under the requirements of this part.

## Symbols and Abbreviations ## {#symbols-abbreviations}

<table class="data">
  <caption>Common symbols and abbreviations used in Part 2.</caption>
  <thead><tr><th>Term<th>Meaning
  <tbody>
    <tr><td>AST<td>`MPD@availabilityStartTime`
    <tr><td>EPT<td>Earliest presentation time of a Segment
    <tr><td>MPD<td>Media Presentation Description
    <tr><td>PS<td>Period start time on the MPD timeline
    <tr><td>PT<td>Presentation time
    <tr><td>PTO<td>`@presentationTimeOffset`
    <tr><td>SAST<td>Segment Availability Start Time
    <tr><td>SAET<td>Segment Availability End Time
    <tr><td>TSB<td>Time Shift Buffer
</table>

# Overview # {#overview}

Part 2 provides the common model used by the rest of the IOP v5 document set:

- a mapping between CMAF structures and DASH MPD structures;
- the timing model that relates Period time, media presentation time, decode
    time, and wall-clock availability time;
- Segment addressing and segment-list derivation using `SegmentTemplate`,
    `$Number$`, `$Time$`, `@duration`, and `SegmentTimeline`;
- common service types (`static`, `dynamic`, MPD updates, locations); and
- interoperability requirements for multi-Period CMAF content and gap handling.

# Introduction to CMAF and DASH Mapping Principles # {#cmaf-dash-principles}

## CMAF Structural Data Model ## {#cmaf-structural-model}

CMAF defines a content model consisting of CMAF Presentations, CMAF Selection
Sets, CMAF Switching Sets, CMAF Tracks, CMAF Headers, CMAF Segments, CMAF
Fragments, and CMAF Chunks [[!MPEGCMAF]]. The relevant addressable CMAF objects
for DASH delivery are:

- **CMAF Headers**, which map to DASH Initialization Segments;
- **CMAF Segments**, which map to DASH Media Segments;
- **CMAF Chunks**, which map to addressable or progressively delivered subparts
    of Segments for low-latency operation; and
- **CMAF Track Files**, which in practical DASH usage are analogous to
    self-initializing Media Segments or single-file Representations.

A DASH-IF Media Presentation shall use CMAF-compliant media tracks when the part
or profile requires CMAF content. A DASH client consumes CMAF media through the
DASH MPD, not directly through the CMAF content model; therefore the CMAF model
is mapped into Periods, Adaptation Sets, Representations, Initialization
Segments, Media Segments, and Subsegments.

## CMAF to DASH Mapping Considerations ## {#mapping-considerations}

A CMAF Presentation is represented as a DASH Media Presentation. A CMAF Selection
Set is typically represented by one or more DASH Adaptation Sets for a media
component. A CMAF Switching Set is typically represented by one DASH Adaptation
Set containing Representations that are switchable under ISO/IEC 23009-1 and the
media-specific IOP part. A CMAF Track maps to a DASH Representation.

The mapping shall preserve:

- synchronization between media components;
- random access and switching points required by the relevant media profiles;
- decoder-configuration compatibility within switching sets;
- Segment timing and addressing information sufficient for the client to derive
    the list of available Segments; and
- metadata and content-protection signalling required by the applicable parts.

# DASH Media Presentation — Core Functionalities # {#dash-core}

## DASH-IF Media Presentation ## {#dashif-media-presentation}

A DASH-IF Media Presentation shall conform to ISO/IEC 23009-1 [[!MPEGDASH]] and
the applicable DASH-IF IOP v5 parts. Unless otherwise specified, DASH-IF IOP v5
uses CMAF media as the segment format baseline. The MPD shall provide sufficient
information for a DASH client to select Adaptation Sets, choose Representations,
derive Segment URLs, map Segment media times to presentation times, and schedule
Segment requests.

## Media Presentation Description ## {#mpd}

The MPD is the entry point for a DASH-IF Media Presentation. It describes the
Media Presentation timeline, Periods, Adaptation Sets, Representations, Segment
information, BaseURL/Location information, and supplemental descriptors. The MPD
shall be authored so that each referenced Segment can be resolved using the
reference-resolution rules of ISO/IEC 23009-1.

## DASH Timing Model ## {#timing-model}

The DASH timing model relates four domains:

1. **MPD timeline**: Period start times and Period durations.
2. **Media presentation time**: sample presentation times inside the media.
3. **Segment addressing time**: `$Time$`, `$Number$`, and SegmentTimeline values.
4. **Wall-clock availability time**: used for dynamic services and Segment
    availability.

For each Representation in a Period, the mapping between Segment media time and
presentation time is determined by the Period start time and any
`@presentationTimeOffset`. The client shall use the MPD timing information and
media timing information to present samples at the intended Media Presentation
time.

For dynamic services, availability is additionally constrained by
`MPD@availabilityStartTime`, `@availabilityTimeOffset`, Segment duration, and the
rules for Segment Availability Start Time and Segment Availability End Time in
ISO/IEC 23009-1 and Part 4.

Issue: Carry over the full v4.3 timing-model explanatory text and formulae where
they add interoperability value beyond ISO/IEC 23009-1. Avoid duplicating formulae
that are now fully specified in the current MPEG-DASH edition.

## DASH Representation Structures and Signalling ## {#representation-structures}

### General ### {#representation-general}

Representations in an Adaptation Set are alternatives for the same media
component unless otherwise signalled. Adaptation Sets and Representations shall
carry sufficient codec, profile, resolution, language, role, accessibility,
content-protection, and essential/supplemental property signalling for a client
to select and play the content.

Adaptation Set constraints from v4.3 remain applicable unless superseded by the
media-specific parts: Representations in an Adaptation Set should be switchable
at defined switching points and should use compatible decoder configurations
where switching is expected.

### Segment Information ### {#segment-information}

DASH-IF IOP v5 uses the Segment information mechanisms of ISO/IEC 23009-1. This
part distinguishes three common `SegmentTemplate` modes:

<table class="data">
  <caption>Common SegmentTemplate modes.</caption>
  <thead><tr><th>Mode<th>Addressing<th>Timeline information<th>Typical use
  <tbody>
    <tr><td>Number + Duration<td>`$Number$`<td>`@duration`<td>Regular Segment duration.
    <tr><td>Number + SegmentTimeline<td>`$Number$`<td>`SegmentTimeline`<td>Variable durations or gaps with sequence-number addressing.
    <tr><td>Time + SegmentTimeline<td>`$Time$`<td>`SegmentTimeline`<td>Media-time addressing; accurate timeline signalling.
</table>

A SegmentTemplate-based Representation shall include all attributes and elements
required by ISO/IEC 23009-1 for the selected mode. Attributes and elements not
specified by this part are governed by ISO/IEC 23009-1.

### Segment List Computation ### {#segment-list-computation}

A DASH client derives the Segment list for a Representation from the MPD. For
`@duration`-based addressing, the segment sequence is derived from Period timing,
`@duration`, `@timescale`, `@startNumber`, and `@presentationTimeOffset`. For
`SegmentTimeline`-based addressing, the sequence is derived from the ordered `S`
elements and their `@t`, `@d`, and `@r` values.

For `$Time$` addressing, the value substituted into the URL is the media time of
the Segment as signalled by the SegmentTimeline. For `$Number$` addressing, the
value substituted into the URL is the segment number starting at `@startNumber`.

Issue: Reconstruct the full Part 2 draft Table 5 (mandatory/optional/default
SegmentTemplate parameters for the three modes) and the detailed segment-list
computation examples. [GROUNDED_BY=dashif-iop-v5-part2-draft#45..#51]

### Subsegment Information ### {#subsegment-information}

Subsegment information may be used by clients for byte-range access, random
access, trick modes, low-latency operation, and other optimizations. Where CMAF
Chunks are used, the low-latency constraints of Part 4 apply. Subsegment
information shall be consistent with the media data and Segment addressing.

### Segment and Representation to Media Presentation Time Mapping ### {#segment-time-mapping}

For each Segment, the media presentation time is derived from media timestamps,
`@timescale`, `@presentationTimeOffset`, and the Period start. The authoring shall
ensure that the mapping is unambiguous and continuous unless a gap or discontinuity
is intentionally signalled.

# CMAF to DASH Mappings # {#cmaf-to-dash}

## Introduction ## {#cmaf-to-dash-intro}

The CMAF-to-DASH mapping shall preserve CMAF constraints while exposing DASH
client operations through the MPD. In particular:

- a CMAF Header maps to an Initialization Segment;
- a CMAF Segment maps to a DASH Media Segment;
- a CMAF Track maps to a DASH Representation;
- CMAF Switching Sets map to switchable DASH Representation sets; and
- CMAF Selection Sets map to alternative media-component selections.

The MPD shall not signal switching or selection capabilities that are not
supported by the underlying CMAF media.

## Good Multi-Period CMAF Content ## {#good-multi-period}

Multi-Period content is common for ad insertion, program boundaries, blackout
replacement, and service operations. For continuous CMAF multi-Period content,
the Period boundary shall not require decoder reset or visible/audible disruption
unless such discontinuity is intentionally signalled and expected by the service.

A service offering continuous multi-Period CMAF content should ensure:

- Period boundaries align with random access points for the affected media;
- decoder configurations are compatible across Periods where continuity is
    expected;
- the same media component semantics are preserved across adjacent Periods; and
- Period start times and Segment timing are consistent with the intended media
    presentation timeline.

Issue: The Part 2 draft contains substantial unfinished text on Good
Multi-Period CMAF Content, including continuous CMAF multi-Period content,
service-offering requirements, client-processing requirements, and profile
signalling. This draft captures the core intent only; the detailed profile text
must be completed with Part 5 ad-insertion alignment. [GROUNDED_BY=dashif-iop-v5-part2-draft#73..#93]

## Multi-Period Content Profile Signalling ## {#multi-period-profile-signalling}

Where a DASH-IF profile or identifier is used to signal multi-Period CMAF
constraints, the signalling shall be present at the MPD or Period level as
specified by that profile. Clients that claim support for the profile shall
support the associated multi-Period processing rules.

Issue: Confirm whether legacy v4.3 profile identifiers such as the DASH-IF Mixed
On-Demand profile remain valid, are deprecated, or are replaced by IOP v5
identifiers. [GROUNDED_BY=dashif-iop-v4-3#90]

# Common Service Functions # {#common-service-functions}

## Bandwidth Signalling ## {#bandwidth-signalling}

`Representation@bandwidth` shall be authored according to ISO/IEC 23009-1 and
shall reflect the bandwidth needed for stable retrieval and playback of the
Representation. Content authors should ensure that bandwidth values are
sufficiently accurate for adaptation logic and are consistent across equivalent
Representations.

Issue: Reconcile the Part 2 draft bandwidth-signalling requirements and client
processing guidance with the current MPEG-DASH definition of `@bandwidth` and
with media-specific constraints. [GROUNDED_BY=dashif-iop-v5-part2-draft#94..#97]

## Static Services ## {#static-services}

A static service uses `MPD@type="static"`. All media announced in the MPD is
available for consumption without requiring MPD updates. Static services may use
any Segment or Subsegment information mode permitted by this part and the
applicable profile.

For static services:

- `MPD@type` shall be `static`;
- the Media Presentation duration shall be determinable from the MPD;
- `MPD@minimumUpdatePeriod` shall not be present; and
- dynamic-service-only attributes such as `MPD@timeShiftBufferDepth` and
    `MPD@suggestedPresentationDelay` should not be present.

Client implementations shall ignore dynamic-only timing information if it is
erroneously present in a static service unless a referenced profile specifies
otherwise.

## Dynamic Services ## {#dynamic-services}

A dynamic service uses `MPD@type="dynamic"`. Media availability evolves over
wall-clock time, and the client derives Segment availability from the MPD and the
time-synchronization rules in Part 4. Dynamic services may be MPD-controlled or
may use segment-based signalling for MPD validity and updates.

The generic timing and addressing principles in this part apply to dynamic
services; live-service-specific requirements are defined in Part 4.

## MPD Updates ## {#mpd-updates}

An MPD update publishes a new MPD instance for the same Media Presentation. The
updated MPD shall maintain a consistent MPD timeline and shall update
`MPD@publishTime` whenever the MPD content changes. Clients use the MPD update
mechanisms of ISO/IEC 23009-1, including `MPD@minimumUpdatePeriod`, MPD validity
expiry events, and `MPD.Location` where applicable.

Issue: Complete the Part 2 draft MPD update rules and reconcile with Part 4 live
service text to avoid duplication. [GROUNDED_BY=dashif-iop-v5-part2-draft#105..#108]

## MPD and Segment Locations ## {#locations}

The `MPD.Location` element may be used to redirect clients to another MPD update
location. `BaseURL` elements at MPD, Period, Adaptation Set, Representation, or
Segment levels may be used to resolve Segment URLs, support replication, and
offer content through multiple CDNs. Content authors shall ensure that reference
resolution is deterministic and follows ISO/IEC 23009-1.

A service may use multiple `BaseURL` elements for redundancy, load distribution,
or CDN selection. Client behaviour for multiple Base URLs is governed by
ISO/IEC 23009-1 and any applicable DASH-IF part.

## Gap Handling ## {#gap-handling}

Gaps may occur when a Representation has missing media for a portion of the MPD
timeline. Gaps shall be signalled using the mechanisms of ISO/IEC 23009-1 and the
selected Segment information mode. A client shall not infer media availability in
an interval that is not signalled by the MPD or media data.

Issue: The Part 2 draft has a placeholder for gap handling. Complete normative
service-offering and client-processing rules, including alignment with
SegmentTimeline gaps, Period boundaries, and low-latency resynchronization.
[GROUNDED_BY=dashif-iop-v5-part2-draft#111..#115]

# Content Annotation and Media Mapping # {#content-annotation}

Content annotation and media-specific mapping are handled by the media parts and
by descriptors defined in ISO/IEC 23009-1. This part defines only common
principles: descriptors shall be used consistently, shall not contradict the
media data, and shall provide enough information for a DASH client and the
application to perform selection, switching, accessibility handling, and
protection processing.

Issue: The Part 2 draft contains a future framework for content annotation and
media mapping (including client processing reference model text). This needs to
be reconciled with Parts 7, 8, 9, 10, and HTML5/MSE platform processing before it
can become normative. [GROUNDED_BY=dashif-iop-v5-part2-draft#116..#129]

# Open Issues and Work Items # {#open-issues}

The following work items remain before Part 2 can be considered complete:

<table class="data">
  <caption>Part 2 open issues and topics to progress.</caption>
  <thead><tr><th>Topic<th>Status<th>Source grounding<th>Next action
  <tbody>
    <tr><td>Overview clause<td>Drafted<td>`dashif-iop-v5-part2-draft#10`<td>Replace the draft's "To be done" with reviewed overview text.
    <tr><td>CMAF structural model figure<td>Open<td>`dashif-iop-v5-part2-draft#13..#17`<td>Redraw the CMAF content model as a clean diagram or table.
    <tr><td>SegmentTemplate parameter table<td>Open<td>`dashif-iop-v5-part2-draft#45..#51`<td>Recreate Table 5 (M/O/defaults for Number+Duration, Number+SegmentTimeline, Time+SegmentTimeline).
    <tr><td>Segment-list computation formulae<td>Partial<td>`dashif-iop-v5-part2-draft#46..#51`; `dashif-iop-v4-3#75..#80`<td>Carry over only formulae that add interoperability value beyond current MPEG-DASH.
    <tr><td>Subsegment information<td>Partial<td>`dashif-iop-v5-part2-draft#52..#56`<td>Complete relationship to CMAF chunks and Part 4 low-latency.
    <tr><td>Good Multi-Period CMAF Content<td>Partial<td>`dashif-iop-v5-part2-draft#73..#93`; `dashif-iop-v4-3#90`<td>Complete continuous-boundary requirements and profile signalling; align with Part 5.
    <tr><td>Bandwidth signalling<td>Partial<td>`dashif-iop-v5-part2-draft#94..#97`<td>Define exact `@bandwidth` interpretation and validator expectations.
    <tr><td>Static/dynamic split<td>Partial<td>`dashif-iop-v5-part2-draft#98..#104`; `dashif-iop-v4-3#74..#80`<td>Deduplicate with Part 3 and Part 4.
    <tr><td>MPD updates<td>Partial<td>`dashif-iop-v5-part2-draft#105..#108`<td>Consolidate with live-service update rules in Part 4.
    <tr><td>Locations/BaseURL<td>Partial<td>`dashif-iop-v5-part2-draft#109..#110`<td>Add normative client and content-author guidance.
    <tr><td>Gap handling<td>Open<td>`dashif-iop-v5-part2-draft#111..#115`<td>Complete service-offering and client-processing rules.
    <tr><td>Content annotation framework<td>Open<td>`dashif-iop-v5-part2-draft#116..#129`<td>Reconcile with media parts and event/metadata parts.
</table>

# Change History # {#change-history}

<table class="data">
  <caption>Part 2 change history.</caption>
  <thead><tr><th>Version<th>Date<th>Change
  <tbody>
    <tr><td>0.1<td>Initial<td>Consolidated initial Bikeshed draft from the Part 2 working draft and carried-over v4.3 timing/on-demand/multi-period basics; added explicit open issues.
</table>
