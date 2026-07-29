<!--
  Part 5: Ad Insertion in DASH.
  Structured migration skeleton aligned with DASH-IF IOP v5.0.0 Part 5.
  Source grounding / migration target:
  rag/corpus/published/DASH-IF-IOP-Part5-v5.0.0.docx.extracted.txt
-->

# Executive summary # {#part5-executive-summary}

Part 5 of DASH-IF IOP v5 provides guidelines for advertisement insertion in an
MPEG CMAF based content-serving workflow using MPEG-DASH as the delivery
protocol.

This part details the general architecture of an ad-enabled content-serving
workflow together with the conditioning, packaging, and signalling requirements
that enable Server-Side Ad Insertion (SSAI) and Server-Guided Ad Insertion
(SGAI). It also defines guidelines for the creation, storage, and serving of ad
content, and provides informative references and recommendations for auxiliary
content and ad systems involved in the ad-insertion architecture.

Issue: This section is a structured skeleton migrated from the published DASH-IF
IOP v5.0.0 Part 5 heading model. Clause text still needs clause-by-clause
migration from the published source. See
`rag/reports/reconcile-part05-ad-insertion.md`.

# Introduction # {#part5-introduction}

This document is Part 5 of DASH-IF IOP v5 and covers ad insertion in DASH.

The published Part 5 document supersedes clause 5, "Ad Insertion in DASH", of
DASH-IF IOP Guidelines version 4.3. The scope remains focused on recommendations
and guidelines for implementing ad insertion in DASH, updated for greater
industry utilization and alignment with MPEG CMAF content authoring.

# Scope # {#scope}

This part specifies DASH-IF IOP v5 Part 5: **Ad Insertion in DASH**.

The scope includes guidelines for implementing ad insertion in DASH with CMAF
content authoring, including:

- terminology aligned with industry-standard ad-insertion terminology,
- architectures for Server-Side Ad Insertion and Server-Guided Ad Insertion,
- content conditioning aligned with MPEG CMAF requirements,
- interface-oriented organization of ad-insertion workflows and functionality,
- creation, storage, packaging, serving, signalling, and playback considerations
  for ad content.

Client-Side Ad Insertion is explicitly excluded from the scope of the published
Part 5 architecture.

# References # {#doc-references}

The following referenced documents are necessary for the application of this
part:

- ISO/IEC 23009-1 [[!MPEGDASH]].
- ISO/IEC 23000-19 [[!MPEGCMAF]].
- DASH-IF IOP v5 Part 1, *Overview, Architectures and Interfaces*.
- DASH-IF IOP v5 Part 2, *Core Principles and CMAF Mapping*.
- DASH-IF IOP v5 Part 12, *Conformance and Reference Tools*.
- ANSI/SCTE 35, *Digital Program Insertion Cueing Message for Cable*.
- ANSI/SCTE 104, *Automation System to Compression System Communications Applications Programming Interface*.
- DASH-IF Live Media Ingest Protocol.
- CTA-5003, *Web Application Video Ecosystem – Device Playback Capabilities*.
- SMPTE RP 2079, *Digital Object Identifier (DOI) Name and Entertainment ID Registry Identifier Representations*.
- ANSI/SCTE 214-1, *MPEG DASH for IP-Based Cable Services, Part 1: MPD Constraints and Extensions*.
- ANSI/SCTE 214-3, *MPEG DASH for IP-Based Cable Services, Part 3: DASH/FF Profile*.
- ANSI/SCTE 130-3, *Digital Program Insertion – Advertising Systems Interface*.
- SMPTE RP 2092-1, *Advertising Digital Identifier Representations*.

Informative references to migrate include CableLabs VoD, MPEG-2 Systems, RIST,
W3C MSE, W3C EME, IAB VAST, Open Measurement SDK, and ITU-R BS.1770-4.

Issue: Published Part 5 references have been listed as migration placeholders.
The corresponding Bikeshed bibliography aliases still need to be added to
`part05-ad-insertion.bs` and normalized against shared bibliography policy.

# Terms and Definitions # {#terms}


## General ## {#terms-general}

Terms and definitions are inherited from ISO/IEC 23009-1, ISO/IEC 23000-19, and
Part 2 unless defined in this part.

The following terms are migrated from the published DASH-IF IOP v5.0.0 Part 5
source.

: <dfn export>ABR encoder</dfn>
:: Live encoder that converts a broadcast stream or mezzanine into a ladder of
   different bit-rate tracks.

: <dfn export>ad avail processor</dfn>
:: Logical service that, given cue data, determines the placement of
   advertisement content within a stream and describes the necessary ad decision
   service communications.

: <dfn export>ad content server</dfn>
:: Server storing ad content and serving it on a per-request basis.

: <dfn export>ad creative</dfn>
:: Linear visual and auditory asset that represents the content of an
   advertisement.

: <dfn export>ad decision service</dfn>
:: Functional entity that decides which ad or ads will be shown to the user.

: <dfn export>ad insertion MPD manipulator</dfn>
:: Functional entity that proxies a DASH MPD and may change it to insert the
   ad creative in the streaming presentation. It may also embed other
   ad-related metadata, or remove ad-related metadata in the MPD.

: <dfn export>ad pod</dfn>
:: Location or point in time where one or more ad slots may be scheduled for
   delivery. This is the same as an ad break, avail, or placement opportunity.
   The prefixes pre-, mid-, and post- may be used to denote pod location
   relative to content as before, during, and after respectively.

: <dfn export>ad reporting server</dfn>
:: Functional entity for collecting viewer impressions of advertisement content.

: <dfn export>ad slot</dfn>
:: Single ad creative that is one of possibly many others that make up an
   ad pod.

: <dfn export>CDN node</dfn>
:: Functional entity returning a segment on request from a DASH client. There
   are no assumptions on the location of the node.

: <dfn export>client-side ad insertion</dfn>
:: Ad-serving architecture in which the client application loads advertisements
   in a secondary player at externally described ad opportunity points.

: <dfn export>CMAF packager</dfn>
:: Functional entity, often residing with the ABR encoder, which packages the
   adaptive bit-rate tracks into CMAF tracks.

: <dfn export>DASH access client</dfn>
:: Client consuming the DASH stream, possibly also containing functionality for
   client-side ad insertion and viewer impression reporting.

: <dfn export>DASH ad resolver</dfn>
:: Functional entity which returns one or more remote elements on request from a
   DASH client, or one or more ad creatives in a DASH-formatted construct on
   request from a DASH access client.

: <dfn export>DASH packager</dfn>
:: Functional entity that processes conditioned content and produces media
   segments suitable for consumption by a DASH client. This entity is also known
   as a fragmenter, encapsulater, or segmenter.

: <dfn export>DASH-IF ad content</dfn>
:: Content that follows specific restrictions and requirements according to this
   specification to be independently produced and inserted into well-formatted
   main content by simple MPD manipulation processes.

: <dfn export>default content</dfn>
:: Placeholder content within main content that is shown when a paid placement is
   not inserted.

: <dfn export>MPD generator</dfn>
:: Functional entity returning an MPD on request from a DASH client. It may be
   generating an MPD on the fly or returning a cached one.

: <dfn export>origin</dfn>
:: Functional entity that contains all media segments indicated in the MPD, and
   is the fallback if CDN nodes are unable to provide a cached version of the
   segment on client request.

: <dfn export>placement opportunity</dfn>
:: Marker within content that denotes where paid placements may be inserted.

: <dfn export>reference playback platform</dfn>
:: Reference platform for playback, for example HTML5 MSE/EME.

: <dfn export>server-side ad insertion</dfn>
:: Ad-serving architecture that interleaves content and ad assets prior to the
   stream reaching the client.

: <dfn export>server-guided ad insertion</dfn>
:: Ad-serving architecture that fully describes ad opportunities within content
   prior to the stream reaching the client, but has the client resolve
   opportunities as needed.

: <dfn export>service provider</dfn>
:: Entity that actively distributes a streaming service to an end consumer.

: <dfn export>splice point</dfn>
:: Point in media content where its stream may be switched to the stream of
   another content, for example to an ad.

: <dfn export>tracking event</dfn>
:: Data payload associated with an ad creative that is emitted by an application
   when a specific time point or criteria is met during creative playout.

## Symbols and abbreviations ## {#symbols-abbreviations}

For the purposes of this part, the following published abbreviations are
identified for migration:

<table class="data">
  <caption>Part 5 abbreviations identified from the published source.</caption>
  <thead><tr><th>Abbreviation<th>Meaning
  <tbody>
    <tr><td>ABR<td>Adaptive Bit Rate
    <tr><td>ADS<td>Ad Decision Service
    <tr><td>CSAI<td>Client Side Ad Insertion
    <tr><td>CDN<td>Content Delivery Network
    <tr><td>CMAF<td>Common Media Application Format
    <tr><td>CTA<td>Consumer Technology Association
    <tr><td>DASH<td>Dynamic Adaptive Streaming over HTTP
    <tr><td>DASH-IF<td>DASH Industry Forum
    <tr><td>EIDR<td>Entertainment ID Registry
    <tr><td>HTTP<td>HyperText Transport Protocol
    <tr><td>IAB<td>Interactive Advertising Bureau
    <tr><td>IF<td>Interface
    <tr><td>IOP<td>Interoperability Point
    <tr><td>ISO<td>International Organization for Standardization
    <tr><td>MPD<td>Media Presentation Description
    <tr><td>MPEG<td>Moving Picture Experts Group
    <tr><td>RIST<td>Reliable Internet Stream Transport
    <tr><td>SCTE<td>Society of Cable Telecommunications Engineers
    <tr><td>SGAI<td>Server-Guided Ad Insertion
    <tr><td>SMPTE<td>Society of Motion Picture and Television Engineers
    <tr><td>SSAI<td>Server-Side Ad Insertion
    <tr><td>TS<td>Transport Stream
    <tr><td>VAST<td>Video Ad Serving Template
    <tr><td>VOD<td>Video On-Demand
    <tr><td>WAVE<td>Web Application Video Ecosystem
</table>

# Use Cases and Scenarios # {#ad-use-cases-scenarios}

## Overview ## {#ad-use-cases-overview}

This clause will migrate published Part 5 clause 4.1.

Ad insertion allows a service provider to replace or augment portions of a main
DASH presentation with advertising or slate content. The published Part 5 use
cases cover live, VoD, recorded live, pre-roll into live, ad obfuscation, and
transition handling between main content and inserted ads.

In all cases, the key problem is to create a Media Presentation that remains
playable by DASH clients while allowing ad opportunities to be resolved,
conditioned, inserted, tracked, and measured by the entities described in the
Part 5 architecture.

## VoD ## {#ad-use-cases-vod}

In a VoD workflow, the full content timeline is available before presentation.
Ad opportunities may be known from content metadata, manual authoring, or a
previously prepared set of placement opportunities.

VoD ad insertion can be performed before the MPD is served or dynamically when a
client requests the MPD. Since the content timeline is known, opportunity
duration, splice points, and placement boundaries can typically be determined
before playback begins.

## Live ## {#ad-use-cases-live}

In a live workflow, placement opportunities can be signalled as the live service
progresses. The exact end time of an opportunity may not be known when the start
of the opportunity is encountered.

Live ad insertion therefore depends on timely opportunity metadata, the ability
to estimate or later correct opportunity duration, and MPD update behaviour that
allows the DASH client to continue playback while ad Periods or remote
resolution points are introduced.

## Recorded Live ## {#ad-use-cases-recorded-live}

Recorded live content combines properties of live and VoD workflows. The content
may originate from a live service and retain opportunity metadata and splice
points from the live event, but it is consumed later as on-demand or time-shifted
content.

Ad insertion for recorded live content may reuse the original live opportunity
metadata, replace previously inserted ads, or re-decision placements for the
later playback context.

## Pre-Roll into Live ## {#ad-use-cases-preroll-live}

A pre-roll into live workflow inserts ad content before joining an ongoing live
presentation. The inserted ad content must lead the client into the live
presentation without disrupting playback timing or media compatibility.

This use case requires careful handling of join time, live edge, buffer
requirements, and any transition from inserted ad Periods to the current live
Period.

## Obfuscation of Inserted Ads ## {#ad-use-cases-obfuscation}

Some deployments may need to obfuscate the identity, boundaries, or source of
inserted ad content. Obfuscation can be relevant for business rules,
measurement, or attempts to reduce ad blocking.

Obfuscation needs to be balanced with interoperability. DASH signalling,
Period boundaries, metadata, and segment URLs still need to provide enough
information for correct playback, tracking, and conformance validation.

## Changes at transitions of main content and ads ## {#ad-transition-changes}

Transitions between main content and inserted ads can introduce changes in
media properties and presentation structure. Examples include changes in:

- available Adaptation Sets,
- codecs and codec profiles,
- resolutions and bitrates,
- audio layouts,
- encryption or key information,
- CMAF headers and initialization information,
- timing, Period boundaries, and presentation time offsets,
- event streams and ad metadata.

Part 5 therefore relies on conditioning, Period continuity/connectivity
signalling, CMAF-compatible ad content, and client playback behaviour to support
seamless transitions.

# Architectures # {#ad-architectures}

## General ## {#ad-architectures-general}

The Part 5 architecture is organized around functional entities and interfaces
rather than a single deployment topology. The same interfaces can be instantiated
in different ways for SSAI and SGAI deployments.

In an SSAI architecture, the service-side entities resolve ad opportunities and
produce a DASH MPD in which main content and ad content are already interleaved.
The DASH client plays the resulting presentation using ordinary DASH playback
procedures, while ad tracking and measurement are driven by metadata and
application behaviour.

In an SGAI architecture, the service-side entities signal ad opportunities and
provide enough information for the DASH client to resolve some ad placements
during playback. This allows ad decisions to depend on client or session context
available at the time the opportunity is reached.

The common functional entities are:

- ABR encoder and CMAF packager for preparing source media,
- DASH packager / MPD generator for producing DASH presentations,
- ad avail processor for interpreting opportunity metadata,
- ad insertion MPD manipulator for MPD generation or proxying,
- ad decision service and ad content server for ad selection and content access,
- DASH ad resolver for remote entities or remote Periods,
- DASH access client and reference playback platform,
- ad reporting server and measurement components.

Issue: Architecture figures from the published Part 5 document still need to be
extracted or redrawn. This prose provides a source-level architecture baseline
until the figures are available.

# Overview on Interfaces and Functions # {#ad-interfaces-overview}

This clause will migrate published Part 5 clause 4.3 and Table 1.

The ad-insertion architectures start with ingest of an input stream over IF-0,
which is processed by an ABR encoder and output as well-formed CMAF content over
IF-1. A DASH packager / MPD generator uses the IF-1 input to generate a
conformant DASH content presentation that is sent over IF-2, and additional
opportunity metadata that is sent over IF-3.

An ad insertion MPD manipulator uses the inputs of IF-2 and IF-3 to generate a
DASH presentation that mixes content and advertisements. In the SSAI
architecture, the manipulator uses IF-4 to ask an ad decisioning / content server
to provide advertisement placements for the content stream, possibly using
client-sourced parameters from IF-7, before generating the final DASH MPD for
IF-5. In the SGAI architecture, the manipulator embeds opportunity information
from IF-3 into the DASH MPD IF-5 output so that the DASH client may later use
IF-7 to retrieve the appropriate ad placements.

The DASH client uses the reference media pipeline provided by IF-9 to perform
seamless playout of the mixed content and ad presentation obtained via IF-5. Ad
measurement and tracking is enabled in the client by IF-8 using ad metadata
embedded as part of IF-6.

<table class="data">
  <caption>Interfaces identified in the ad insertion architecture, example instantiations, and migration targets.</caption>
  <thead><tr><th>Interface<th>Function<th>Example instantiations / related references<th>Migration target
  <tbody>
    <tr><td>IF-0<td>ABR Stream Source<td>Mezzanine delivery, CableLabs VoD [[CABLELABS-VOD]], MPEG-2 TS [[MPEG2-SYSTEMS]], RIST [[RIST]], SCTE-35 [[SCTE35]], SCTE-104 [[SCTE104]]<td>`#ad-if0-abr-stream-source`
    <tr><td>IF-1<td>Packager Ingest<td>CMAF tracks and switching sets [[!MPEGCMAF]], DASH-IF Live Media Ingest [[DASHIF-INGEST]]<td>`#ad-if1-packager-ingest`
    <tr><td>IF-2<td>Content Preparation<td>DASH presentation generation, CMAF-aligned content conditioning, device capability constraints [[CTA5003]]<td>`#ad-if2-content-preparation`
    <tr><td>IF-3<td>Ad Avail Signalling<td>SCTE-35 opportunity signalling [[SCTE35]], SCTE 214 DASH event carriage [[SCTE214-1]]<td>`#ad-if3-ad-avail-signalling`
    <tr><td>IF-4<td>Ad Decisioning and Exchange Interfaces<td>Ad decision requests, content conditioning requests, VAST [[VAST]], SCTE-130 [[SCTE130-3]], EIDR [[EIDR-FORMAT]], Ad-ID [[SMPTE-RP2092-1]]<td>`#ad-if4-decisioning-exchange`
    <tr><td>IF-5<td>MPD and Segments with Ad Placements<td>DASH MPD/segments [[!MPEGDASH]], CMAF [[!MPEGCMAF]], MPD proxy operations, playback guidelines<td>`#ad-if5-mpd-segments`
    <tr><td>IF-6<td>Ad Metadata Signalling<td>DASH callback events and metadata for tracking/measurement<td>`#ad-if6-ad-metadata`
    <tr><td>IF-7<td>Ad Decisioning Parameters and Remote Resolution<td>URL parameters, content-conditioning parameters, Remote Period late binding<td>`#ad-if7-remote-resolution`
    <tr><td>IF-8<td>Ad Tracking and Measurement<td>VAST view tracking [[VAST]], Open Measurement SDK [[OPENMEASUREMENT]], alternative tracking methods<td>`#ad-if8-tracking-measurement`
    <tr><td>IF-9<td>Reference Media Playback and Decryption<td>HTML5 MSE [[MSE]], EME [[EME]], reference playback platform, content protection alignment<td>`#ad-if9-reference-playback-decryption`
</table>

Issue: This table is a source-level reconstruction from the published Part 5
interface overview. It should be checked against the original DOCX/PDF table
layout and any architecture figure labels before being marked fully reconciled.

# Interfaces # {#ad-interfaces}


## General ## {#ad-interfaces-general}

This clause will migrate published Part 5 clause 5.

## IF-0: ABR Stream Source ## {#ad-if0-abr-stream-source}

IF-0 describes the stream source input to the ad-insertion workflow. The source
may be live, VoD, or recorded live content. It provides media and descriptive
metadata that are later used for packaging, opportunity signalling, and ad
decisioning.

For live workflows, IF-0 may carry descriptive metadata from the live production
or automation environment, including cueing information that can be translated
into ad opportunities. SCTE-104 [[SCTE104]] and SCTE-35 [[SCTE35]] are common
sources of such cueing information.

For VoD workflows, descriptive metadata may be provided as side metadata
associated with the content asset. It can identify candidate placement
opportunities, content identifiers, genre, language, ratings, or other
information useful for ad decisioning.

The abstracted IF-0 model provides:

- media essence or a prepared media source,
- opportunity or cue metadata,
- descriptive metadata used for decisioning,
- timing information needed to map opportunities to media time.

The IF-0 abstracted model assumes that media is produced on a continuous media
timeline. Splice points identify media times at which the main content may later
transition to another content item, for example an ad or slate. A splice point is
identified by media time `tsplice`.

For live workflows, splice-point information can be generated by production
automation, SCTE-104 messages, SCTE-35 messages, or other cueing systems. For
VoD workflows, splice-point information can be generated from asset metadata or
authoring systems.

When source media is prepared for ad insertion, timed metadata associated with
each splice point should preserve at least:

- the splice point media time `tsplice`;
- the relationship between the splice point and the source media timeline;
- any known or expected opportunity duration;
- identifiers that allow opportunity start and end metadata to be correlated;
- descriptive metadata needed by downstream ad decisioning; and
- any information needed by the DASH packager / MPD generator to create Period
  boundaries or equivalent MPD Event signalling.

The published Part 5 model identifies three preparation options for CMAF-based
live content:

1. **Splice-Conditioned Packaging.** CMAF Fragment boundaries are generated at
   splice points. This allows the DASH packager / MPD generator to create Period
   boundaries aligned with fragment boundaries.
2. **Splice-Conditioned Encoding.** The encoder conditions media so that splice
   points are suitable for later packaging. For video, the splice point should
   correspond to a suitable random access point, such as SAP type 1 or SAP type
   2, so that packaging can later generate compatible fragments.
3. **Splice Point Signalling.** The media is not necessarily fragmented at
   splice points, but metadata signals the splice points and their properties so
   that downstream components can generate or infer Period boundaries.

Option 1 is preferred when downstream MPD-level manipulation is expected,
because the DASH packager can generate Period boundaries without media segment
splitting. Options 2 and 3 require more downstream processing and may require
the MPD manipulator or packaging function to access media segment details.

Issue: Figures 3 and 4 from the published Part 5 document describe the
abstracted media model and CMAF encoder/packager options. They still need to be
extracted or redrawn and visually checked against this prose.

## IF-1: Packager Ingest ## {#ad-if1-packager-ingest}

IF-1 describes ingest from the ABR stream source or CMAF packager into the DASH
packager / MPD generator. The ingest interface provides well-conditioned CMAF
tracks and associated metadata to the DASH packaging function.

The interface is expected to align with CMAF-based ingest and DASH-IF Live Media
Ingest [[DASHIF-INGEST]] where applicable. The ingest output should preserve
timing and opportunity metadata required to generate IF-2 DASH content and IF-3
ad avail signalling.

The packager ingest process should ensure that media is conditioned so that
future ad insertion can be performed using Period boundaries, compatible CMAF
headers, and appropriate timeline information.

The published architecture references IF-1 sub-interfaces in Figure 1:

- IF-1a, associated with CMAF ingest from the CMAF packager to the DASH
  packager / MPD generator;
- IF-1b, associated with content preparation information needed to generate the
  MPD and segments; and
- IF-1c, associated with opportunity metadata that is later carried through IF-3.

These labels need visual confirmation against Figure 1 before becoming stable
anchors in the source.

For splice-conditioned ingest, the DASH packager / MPD generator should receive
or infer enough information to:

- identify CMAF Switching Sets and CMAF Tracks;
- determine CMAF Fragment boundaries;
- determine whether Fragment boundaries align with splice points;
- determine whether video fragments start with suitable random access points;
- preserve timed metadata for each splice point;
- generate Period boundaries at splice points when using
  Splice-Conditioned Packaging;
- generate MPD Event signalling when Period boundaries are not already created;
  and
- generate the IF-2 MPD and IF-3 opportunity metadata consistently.

Issue: IF-1 has been hardened from the extracted Figure 1 / Figure 4 context,
but the actual published figures still need extraction or redrawing before the
IF-1a/IF-1b/IF-1c labels are finalized.

## IF-9: Reference Media Playback and Decryption ## {#ad-if9-reference-playback-decryption}

IF-9 identifies the reference media playback and decryption environment used to
evaluate whether the combined main-content and ad-content presentation can be
played seamlessly.

The reference playback platform includes DASH playback with HTML5 Media Source
Extensions [[MSE]] and, when encrypted content is used, Encrypted Media
Extensions [[EME]]. Content protection aspects need to remain aligned with Part 6.

The purpose of IF-9 is to constrain the generated presentation to behaviour that
a DASH access client and reference playback platform can perform, including:

- multi-Period playback,
- Period continuity and connectivity handling,
- CMAF header switching where needed,
- decryption and key availability,
- transition handling between main content and ads.

## IF-2: Content Preparation ## {#ad-if2-content-preparation}

IF-2 describes the DASH presentation output of the DASH packager / MPD generator
before ad placements are inserted. The IF-2 output is the main content input to
the [=ad insertion MPD manipulator=].

The DASH-IF IOP guidelines provide the baseline DASH output requirements. This
part adds ad-insertion-specific preparation guidance for content that will later
be processed by an ad insertion MPD manipulator.

For each known ad splice point, the DASH packager / MPD generator should either:

- insert a Period boundary at `tsplice,i` and provide the splice-point
  properties for each splice point; or
- insert sufficient signalling, for example in an Event Stream, such that the
  splice point and its properties are identified and a Period can be added at the
  splice point without reading segments.

Providing a Period boundary at splice points is recommended because the
downstream ad insertion MPD manipulator can then perform replacement and
insertion operations at MPD level without accessing the content segments.

If the DASH packager / MPD generator is not aware of appropriate ad-insertion
splice points, Period boundaries may be omitted and created later by the ad
insertion MPD manipulator. In that case, the manipulator may need to perform
Period splitting operations as described by IF-5.

The following live-content assumptions are used by the published Part 5 model:

- at least one media type, typically video, follows the Splice-Conditioned
  Packaging option described by IF-1;
- each CMAF Fragment generates one DASH Segment;
- CMAF fragments or CMAF chunks are made available to the DASH packager once
  completed;
- the minimum splice point advance notice time is known; and
- the DASH packager uses this advance notice to configure
  `MPD@minimumUpdatePeriod` so that DASH clients and MPD proxies request MPD
  updates frequently enough not to miss announced Periods.

For the initial MPD, the DASH packager / MPD generator maps CMAF data to the MPD
using the DASH Core Profile for CMAF content. For every CMAF Switching Set that
is known to be offered in the MPD, an **InitializationSet** should be added to
describe all known static parameters for the CMAF Switching Set, preferably based
on information in the CMAF Master Header.

The following **InitializationSet** rules apply:

- every **InitializationSet** gets a unique `@id`;
- for every CMAF Switching Set not known to be offered continuously,
  `InitializationSet@inAllPeriods` is set to `false`;
- for every CMAF Switching Set known to be offered continuously,
  `InitializationSet@inAllPeriods` is set to `true` or omitted.

For live operation, `MPD@availabilityStartTime` is set to an arbitrary value,
for example `1970-01-01T00:00:00Z`. The `MPD@minimumUpdatePeriod` is set
sufficiently small so that DASH clients and MPD proxies do not miss Periods
created for announced splice points, taking into account minimum splice point
advance notice time.

For each Period, a unique identifier for the main content should be carried in
an **AssetIdentifier** descriptor. Example identification schemes include:

- an EIDR identification scheme, signalled with:
  - `@schemeIdUri="urn:eidr"`; and
  - `@value` set to a valid canonical EIDR entry as defined by SMPTE RP 2079
    [[SMPTE-RP2079]];
- a DASH-IF asset identification scheme, signalled with:
  - `@schemeIdUri="http://dashif.org/guidelines/v5/asset-id"`; and
  - `@value` set to a MovieLabs ContentID URN.

Note: Based on MPEG MPD restrictions, at most one **AssetIdentifier** may be added
per Period.

For every splice point `i` at media time `tsplice,i`, if a Period is generated,
the following Period start rules apply:

- if it is the first Period in the presentation and the media is starting to be
  produced, `Period@start` is set to the current time minus
  `MPD@availabilityStartTime`, with possible margins for different segment
  availability times such as CDN publication delay;
- if it is not the first Period in the presentation, `Period@start` is set to the
  sum of the previous `Period@start` and the interval between splice points,
  `tsplice,i - tsplice,i-1`.

Period continuity should be signalled across Adaptation Sets that continue across
the Period boundary. Preferably the same signalling and track structure is used.

Every available CMAF Switching Set in the CMAF Presentation is mapped to one
Adaptation Set using the DASH Core Profile for CMAF content. The following
additional restrictions apply for each Adaptation Set:

- `SegmentBase@presentationTimeOffset` is set to `tsplice,i`, normalized by the
  applicable timescale;
- for the Splice-Conditioned Packaging option, `SegmentBase@eptDelta` is `0` and
  should therefore be absent;
- `SegmentTemplate@startNumber` or **SegmentTimeline** is set such that it
  references the first segment in the Period after the splice point;
- Period continuity should indicate which Adaptation Set follows continuously
  from the previous one; and
- for Representations with the same `@id` within continuous Adaptation Sets,
  continuity is signalled.

If the CMAF Switching Set is identical to one for which an **InitializationSet**
was set, then all parameters from the **InitializationSet** are copied into the
Adaptation Set and `@initializationRefId` is set to the referenced
`InitializationSet`.

IF-2 content is used together with IF-3 opportunity metadata and IF-4 ad
decision/content responses to produce the IF-5 MPD and segments with ad
placements.

Issue: This IF-2 hardening pass incorporates published extracted lines 360–408.
Published Table 2, "DASH-IF Main live content MPD", still requires visual
DOCX/PDF reconstruction because the text extraction preserves the caption and
surrounding prose but not the complete table row layout.

## IF-3: Ad Avail Signalling ## {#ad-if3-ad-avail-signalling}


### General ### {#ad-if3-ad-avail-signalling-general}

Opportunity metadata consists of the original descriptive metadata of the input
media related to signalling ad opportunities, together with content segmentation
information generated by the DASH packager. Carriage of opportunity metadata in
the presentation output by the DASH packager / MPD generator is done through
IF-3.

The following requirements apply to opportunity metadata carriage:

- Opportunity metadata <span class=modal-keyword>shall</span> be carried through DASH MPD Events.
- MPD Events are required so that the downstream [=ad insertion MPD manipulator=] can perform insertions without accessing the content segments.
- Equivalent metadata may also be present in-band, but the MPD proxy is not expected to use the in-band information.

The metadata format is workflow-dependent. For the purposes of this part,
opportunity metadata carriage using SCTE-35 signalling in DASH MPD Events is
assumed. Other methods and formats may be used, but service providers should
understand the downstream system effects if the packager does not follow this
assumption.

Any opportunity metadata used in the context of this specification <span class=modal-keyword>must</span>
provide:

- the presentation time, in media time, of the splice point corresponding to the start of an opportunity; and
- either:
  - the guaranteed accurate duration of the opportunity; or
  - an expected opportunity duration, if known, and the identifier of a later metadata event that will signal the accurate end of the opportunity.

### Opportunity Signalling via SCTE-35 ### {#ad-if3-scte35-opportunity-signalling}

SCTE-35 describes command messages that can be used to describe ad opportunities
within a presentation. Broadcast events for a live presentation are often already
signalled as SCTE-35 commands and may be directly used. A VoD workflow may
optionally synthesize a series of SCTE-35 commands to describe conditioning and
opportunities in a VoD presentation.

SCTE 214-1 [[SCTE214-1]] and SCTE 214-3 [[SCTE214-3]] define event schemes for
carrying SCTE-35. DASH MPD Events may use either `urn:scte:scte35:2013:xml` or
`urn:scte:scte35:2014:xml+bin`.

When carrying SCTE-35 with MPD Events using the
`urn:scte:scte35:2014:xml+bin` scheme:

- the timing described within the SCTE-35 payload provides the Event `@id`, `@presentationTime`, and `@duration` properties;
- the Event `@id` may be used to filter duplicate events; and
- the SCTE-35 payload is encoded using Base64 enclosed in the `Binary` element defined by SCTE-35.

For signalling opportunity metadata, it is common to use an SCTE-35
`time_signal()` splice command carrying a `segmentation_descriptor()` splice
descriptor. Alternatively, the legacy `splice_insert()` command may be used. In
that case, the Event duration equals the break duration in the splice, which is
the expected duration of the ad break. The `out_of_network` indicator is set to
`true` when the splice into an advertisement slot occurs. A break can be
terminated early by an additional MPD Event carrying a `splice_insert()` command
with `out_of_network` set to `0` and the splice-immediate flag set.

The presentation time of the splice point is provided by the `splice_time()`
structure present within the command and is represented in the Event Stream as
the value of the Event `@presentationTime` attribute.

Opportunity boundaries are signalled by pairs of `segmentation_descriptor()`
`segment_type_id` values. The descriptor pair contains the same
`segmentation_event_id` value so that start and end can be matched. If an
expected opportunity duration is known, the segment-start descriptor may provide
the expected duration in the `segmentation_duration` field, which may be
represented as the Event `@duration` until the final duration is known.

With SCTE-35, the final accurate duration is only established when the matching
segment-end descriptor is encountered. The segment-end descriptor may occur at,
before, or after the duration specified by the segment-start descriptor. The
final opportunity duration is calculated as the difference between the splice
times of the segmentation pair and is represented as the Event `@duration`.

<div class="example">

An example SCTE-35 message embedded as an MPD Event using SCTE 214 is:

```xml
<EventStream schemeIdUri="urn:scte:scte35:2014:xml+bin" timescale="1">
  <Event presentationTime="1540809120" duration="24" id="1999">
    <scte35:Signal>
      <scte35:Binary>
        /DAhAAAAAAAAAP/wEAUAAAfPf+9/fgAg9YDAAAAAAAA/APOv
      </scte35:Binary>
    </scte35:Signal>
  </Event>
</EventStream>
```

Note: While the example presentation time is large, the presentation time may
and typically is adjusted by `@presentationTimeOffset` to align with the Period
start time.

</div>

## IF-4: Ad Decisioning and Exchange Interfaces ## {#ad-if4-decisioning-exchange}


### General ### {#ad-if4-decisioning-exchange-general}

Information about ad content to insert into a presentation is retrieved from the
ad decision and ad content servers through IF-4 interfaces. The request from the
[=ad insertion MPD manipulator=] for ad content provides the information needed
to perform ad decisioning, including content metadata and opportunity
descriptions. The response is translated by the ad insertion MPD manipulator
into the DASH structures described by IF-5.

This part identifies six IF-4 sub-interfaces:

- IF-4a: ad decision request parameters;
- IF-4b: content conditioning request parameters;
- IF-4c: recommended dynamic ad content response format;
- IF-4d: DASH-IF ad content storage format;
- IF-4e: ad selection result format; and
- IF-4f: DASH-IF recommended slate content.

These sub-interfaces are described independently to define the data and
interactions that occur in an ad insertion architecture, without assuming a
specific deployment form for the ad decision and ad content servers.

This part assumes:

- an ad decision entity accepts request parameters of the form described by IF-4a and provides a decision of the form described by IF-4e;
- an ad content entity accepts conditioning parameters of the form described by IF-4b and provides ad content of the form described by IF-4c;
- the ad content entity may also provide filler slate content of the form described by IF-4f;
- the ad decision and ad content entities may be the same system or independent systems; and
- the ad content server may or may not store content in the format described by IF-4d, although this part defines a recommended storage format for interoperability with CMAF workflows.

### IF-4a: Ad Decision request parameters ### {#ad-if4a-decision-request-parameters}

A decisioning parameter is a piece of information about the content stream,
consumption medium, or end user that is used by the ad decisioning server as
part of the advertisement qualification and selection process. The ad insertion
MPD manipulator collects and sends this information to the ad decisioning server
as part of IF-4a.

Transmission of decisioning parameters is integration-dependent. Examples of
commonly used parameters include:

- content unique identifier,
- content genre,
- content language,
- service provider identifier,
- device type, such as TV, set-top, mobile, or computer,
- device manufacturer,
- device model,
- end-user IP address, and
- end-user ZIP code.

Methods for carrying decisioning parameters in the request from the ad insertion
MPD manipulator to the ad content server may follow the same guidelines as
requests between the DASH client and ad insertion MPD manipulator. See IF-7a for
further details.

#### Decisioning modes #### {#ad-if4a-decisioning-modes}

The decisioning mode of an ad decisioning server dictates how the server chooses
to fulfill ad requests made by a caller. The ad insertion MPD manipulator must
specify the decisioning mode for the ad decisioning server to use through IF-4a,
based on the implemented ad insertion architecture.

Two general decisioning modes are used:

- **Stream-level decisioning.** All advertisement opportunities are decided before the DASH client receives the stream. In an SSAI architecture, the ad insertion MPD manipulator sends IF-3 opportunity metadata to the ad decision server through IF-4a. The ad decision response contains advertisements for the entire stream, which the manipulator transforms into an IF-5 manifest containing a mix of content and advertisements.
- **Pod-level decisioning.** Advertisement opportunities are decided as the DASH client reaches the opportunity within the stream. In an SGAI architecture, the ad insertion MPD manipulator uses IF-3 opportunity metadata to generate an IF-5 manifest containing a mix of content and remote entities that represent opportunities. As the client reaches remote entities during playout, it uses IF-7 to return the opportunity metadata to the ad insertion MPD manipulator, which then sends the data to the ad decision server through IF-4a.

After a DASH client receives a stream produced from an SSAI architecture, the
stream remains fixed for the playback session. After a DASH client receives a
stream produced from an SGAI architecture, the stream can continue to change
during the playback session, for example if advertisements are re-decisioned
when the user rewinds.


### IF-4b: Content Conditioning request parameters ### {#ad-if4b-content-conditioning-parameters}

A conditioning parameter is information about the encoding or packaging of the
content stream, or about a client player capability, that is used by the ad
content server to ensure that an ad creative is compatibly encoded for inclusion
in the generated presentation. The ad insertion MPD manipulator collects and
sends this information to the ad content server as part of IF-4b.

Transmission of conditioning parameters is integration-dependent. Examples of
commonly used parameters include:

- video and audio codecs,
- player splice-condition robustness,
- encryption schemes,
- CMAF master headers,
- width and height, and
- other information used to initialize playback of the main content.

An ad content server is expected to use a best-effort approach to the provided
conditioning parameters. This part does not require real-time transcoding of ad
content to fit all parameters. Further recommendations for use of conditioning
parameters by the ad content server are made by IF-4c.

Methods for carrying conditioning parameters from the ad insertion MPD
manipulator to the ad content server may follow the same guidelines as requests
between the DASH client and ad insertion MPD manipulator. See IF-7b for further
details.

### IF-4e: Ad Selection Result format ### {#ad-if4e-ad-selection-result}

The response of the ad decision server identifies the advertisements selected by
the server and provides information associated with them, such as general
metadata, viewability requirements, media files, mezzanines, and tracking events.
The actual ad content is provided by the ad content server, preferably following
the DASH-IF ad content format described by IF-4c. Depending on the decisioning
mode, the decision response may also contain the placement and ordering of
advertisements.

The explicit response format is workflow-dependent. For an ad selection result
format to be used in the context of this part, the result format <span class=modal-keyword>must</span>
include a reference to one or more well-defined ad content items, each with a
well-defined duration.

The result format may include:

- tracking beacons,
- identifiers,
- campaign information, and
- tracking information.

#### IAB VAST #### {#ad-if4e-vast}

An IF-4e instantiation is standardized by IAB as the Video Ad Serving Template
(VAST) [[VAST]]. VAST provides structure definitions for representing linear,
non-linear, and companion advertisements. A single VAST response may contain a
stand-alone ad slot or a pod of ad slots, and each ad structure can provide
general metadata, viewability requirements, media files, mezzanines, and
tracking events.

In VAST, a reference to DASH-IF ad content may be provided for each `Ad` element
contained in the response. Specifically, each `Ad` element may contain a
`MediaFile` element under `Ad.InLine.Creatives.Linear.MediaFiles`, where:

- `@type` is compatible with `application/dash+xml profiles='http://dashif.org/guidelines/dashif-ad-content'`; and
- the value of `MediaFile` is a URI that resolves to the DASH-IF ad content MPD.

#### SCTE-130 #### {#ad-if4e-scte130}

Another IF-4e instantiation is standardized by SCTE as the response of the Ad
Decision Service. The Ad Decision Service determines how advertising content is
combined with non-advertising content. The exact format and schema of this
response is defined by SCTE-130 Part 3 [[SCTE130-3]].

In SCTE-130, a reference to DASH-IF ad content may be derived for each
`Placement` element contained in the `PlacementResponse` structure. Specifically,
each `Placement` may contain a `core:AssetRef` element under
`Placement.coreContent` or `Placement.CoreRotationList.core:Content`, where the
supplied `@assetID` may be used to retrieve the content from the ad content
server specified by `@providerID`.

Issue: The SCTE-130 mapping is based on the published Part 5 explanatory text
and should be reviewed by an SCTE-130 expert before being treated as final.

### IF-4d: DASH-IF Ad Content Storage format ### {#ad-if4d-ad-content-storage}

This interface provides a recommended content format for ad content that is
expected to be dynamically inserted into a DASH live or on-demand Media
Presentation.

Ad content is recommended to follow the DASH-IF ad content format defined in
this clause. This part does not exclude use of other content, but content
authors should be aware of differences from the DASH-IF ad content format.

DASH-IF ad content follows the restrictions and requirements of this part and
may be produced independently of the main content for insertion into
well-formatted main content by simple MPD manipulation.

If content is offered conforming to the DASH-IF ad content format and follows
the requirements and recommendations below, it may be annotated with the
`@profiles` parameter value `http://dashif.org/guidelines/dashif-ad-content`.

The following requirements apply to DASH-IF ad content:

- The content <span class=modal-keyword>shall</span> be provided as a DASH Media Presentation, i.e. a complete MPD with referenced segments.
- The DASH Media Presentation <span class=modal-keyword>shall</span> conform to the DASH Core Profile for CMAF content as defined in ISO/IEC 23009-1 [[!MPEGDASH]].
- Presentation time <span class=modal-keyword>shall</span> be anchored to `0`.
- `@presentationTimeOffset` <span class=modal-keyword>shall</span> be absent, i.e. it is assumed to be zero.
- `@eptDelta` <span class=modal-keyword>shall</span> be absent, i.e. the earliest presentation time of each segment is `0`.
- The DASH Media Presentation <span class=modal-keyword>shall</span> contain exactly one Period.
- `MPD@type` <span class=modal-keyword>shall</span> be set to `static`.

Note: An important assumption for this profile is the availability of content for
CMAF tracks over the entire Period. Content may overlap at the end of the
Period.

The following recommendations apply to DASH-IF ad content:

- The MPD should contain the profile indicator `http://dashif.org/guidelines/dashif-ad-content`.
- The content should be offered in segmented format using the segment timeline.
- Segment durations within one Adaptation Set should be approximately identical.
- The content may, and typically should, include multiple variants for the same ad, such as different codecs, formats, and resolutions, so that dynamic conditioning, the MPD proxy, or a DASH client can adjust the ad to current playback conditions.
- An **AssetIdentifier** descriptor should be present to carry a globally unique content identifier for the ad content.

Examples of asset identifier schemes include:

- An Ad-ID identification scheme, defined by SMPTE RP 2092-1 [[SMPTE-RP2092-1]], signalled with:
  - `@schemeIdUri="urn:smpte:ul:060E2B34.01040101.01200900.00000000"`; and
  - `@value` set to the canonical full Ad-ID identifier.
- In the absence of another identification scheme, a DASH-IF-defined scheme may be signalled with:
  - `@schemeIdUri="http://dashif.org/guidelines/v5/asset-id"`; and
  - `@value` set to a MovieLabs ContentID URN.

<table class="data">
  <caption>DASH-IF Ad content MPD.</caption>
  <thead><tr><th>Context<th>Element or attribute<th>Use<th>Requirement / description
  <tbody>
    <tr><td>**MPD**<td>**MPD**<td>—<td>Provides the requirements for ad insertion content. Values not specified here are identical to ISO/IEC 23009-1.
    <tr><td>**MPD**<td>`@profiles`<td>M<td>Should include `http://dashif.org/guidelines/dashif-ad-content` and <span class=modal-keyword>shall</span> include the DASH CMAF profile identifier `urn:mpeg:dash:profile:cmaf:2019`.
    <tr><td>**MPD**<td>`@type`<td>M<td><span class=modal-keyword>Shall</span> be set to `static`.
    <tr><td>**MPD**<td>`@mediaPresentationDuration`<td>R<td><span class=modal-keyword>Shall not</span> be present.
    <tr><td>**MPD**<td>`@minimumUpdatePeriod`<td>R<td><span class=modal-keyword>Shall not</span> be present.
    <tr><td>**MPD**<td>`@minBufferTime`<td>M<td><span class=modal-keyword>Shall</span> be present.
    <tr><td>**MPD**<td>`@timeShiftBufferDepth`<td>R<td><span class=modal-keyword>Shall not</span> be present.
    <tr><td>**MPD**<td>`@suggestedPresentationDelay`<td>R<td><span class=modal-keyword>Shall not</span> be present.
    <tr><td>**MPD**<td>`@maxSegmentDuration`<td>R<td><span class=modal-keyword>Shall not</span> be present.
    <tr><td>**MPD**<td>`@maxSubsegmentDuration`<td>R<td><span class=modal-keyword>Shall not</span> be present.
    <tr><td>**MPD**<td>**ProgramInformation**<td>0 … N<td>Should be used to describe information about the ad.
    <tr><td>**MPD**<td>**BaseURL**<td>0<td><span class=modal-keyword>Shall not</span> be present at MPD level; BaseURL belongs in the Period.
    <tr><td>**MPD**<td>**Period**<td>1<td>Exactly one Period <span class=modal-keyword>shall</span> be present. Values not specified here are identical to ISO/IEC 23009-1.
    <tr><td>**Period**<td>`@xlink:href`<td>R<td><span class=modal-keyword>Shall</span> be absent.
    <tr><td>**Period**<td>`@xlink:actuate`<td>R<td><span class=modal-keyword>Shall</span> be absent.
    <tr><td>**Period**<td>`@start`<td>R<td><span class=modal-keyword>Shall</span> be absent; assumed to be `0`.
    <tr><td>**Period**<td>`@duration`<td>M<td><span class=modal-keyword>Shall</span> be present and provide the ad content duration.
    <tr><td>**Period**<td>**BaseURL**<td>1 … N<td>At least one <span class=modal-keyword>shall</span> be present and refer to the BaseURL of the ad content.
    <tr><td>**Period**<td>**AssetIdentifier**<td>0 … 1<td>Should be used to provide an explicit identifier for the ad content.
    <tr><td>**Period**<td>**EventStream**<td>0 … N<td>Event Streams are permitted, for example for beaconing.
    <tr><td>**Period**<td>**AdaptationSet**<td>1 … N<td>At least one Adaptation Set <span class=modal-keyword>shall</span> be present.
    <tr><td>**AdaptationSet**<td>`@xlink:href`<td>R<td><span class=modal-keyword>Shall</span> be absent.
    <tr><td>**AdaptationSet**<td>`@xlink:actuate`<td>R<td><span class=modal-keyword>Shall</span> be absent.
    <tr><td>**AdaptationSet**<td>**InbandEventStream**<td>0 … N<td>Inband Event Streams are permitted, for example for beaconing.
    <tr><td>**AdaptationSet**<td>`CommonAttributesElements`<td>—<td>Specifies the common attributes and elements from `RepresentationBaseType`; values not specified here follow ISO/IEC 23009-1.
    <tr><td>**AdaptationSet**<td>`SegmentBase@presentationTimeOffset`<td>OD<td><span class=modal-keyword>Shall</span> be absent.
    <tr><td>**AdaptationSet**<td>`SegmentBase@eptDelta`<td>O<td><span class=modal-keyword>Shall</span> be absent.
    <tr><td>**AdaptationSet**<td>`SegmentBase@pdDelta`<td>O<td>May be present for non-video tracks. If present, it <span class=modal-keyword>shall</span> be non-negative and should be as small as possible.
    <tr><td>**AdaptationSet**<td>`@contentType`<td>M<td><span class=modal-keyword>Shall</span> be present.
    <tr><td>**AdaptationSet**<td>**SegmentList**<td>0<td><span class=modal-keyword>Shall</span> be absent.
    <tr><td>**AdaptationSet**<td>**Representation**<td>1 … N<td>At least one Representation <span class=modal-keyword>shall</span> be present in each Adaptation Set.
    <tr><td>**Period**<td>**EmptyAdaptationSet**<td>0<td><span class=modal-keyword>Shall</span> be absent.
    <tr><td>**MPD**<td>**UTCTiming**<td>0<td><span class=modal-keyword>Shall not</span> be present.
    <tr><td>**MPD**<td>**LeapSecondInformation**<td>0<td><span class=modal-keyword>Shall not</span> be present.
</table>

Issue: This Table 4 reconstruction has been restructured against the DOCX table
structure extracted from `DASH-IF-IOP-Part5-v5.0.0.docx`. The extraction
confirmed 36 rows, the published caption "DASH-IF Ad content MPD", the top-level
**MPD** description row, the AdaptationSet `@xlink:href` and `@xlink:actuate`
rows, and the `CommonAttributesElements` row. A rendered visual DOCX/PDF review
is still recommended to confirm typography and final row hierarchy.

### IF-4f: DASH-IF Recommended Slate Content ### {#ad-if4f-slate-content}

This interface provides a recommended content format for slate content that is
expected to be dynamically inserted into a DASH live or on-demand Media
Presentation by an ad insertion proxy to fill timeline gaps introduced by ad
durations that do not exactly match the placement opportunity duration.

Slate content is recommended to follow the requirements and recommendations of
the DASH-IF ad content format defined by IF-4d. In addition, the following
recommendations apply:

- Segment durations should be short for live presentations, preferably not exceeding one second. Short segments aid in short acquisition time and cutback accuracy.
- Slate content should be of low complexity but should not represent a still image. Movement is important to avoid the perception of stalling.
- When no sound is desired or necessary, slate content should still provide a silent audio track. Providing both video and audio is important to support seamless playout by clients.

### IF-4c: Recommended Dynamic Ad Content Response format ### {#ad-if4c-dynamic-ad-content-response}

The response format should follow the DASH-IF ad content format defined by
IF-4d.

The following recommendations apply:

- If no conditioning parameters are provided, the response should include multiple content variants, for example multiple codecs, resolutions, or formats.
- If codec conditioning parameters are provided, the response should include content options including at least one of the requested codecs.
- If format conditioning parameters are provided, the response should include content options including at least one of the supported formats.
- If encryption conditioning parameters are provided, the response should include content options including at least one of the supported encryption modes.
- If the content needs to be obfuscated or blocked, the response should be adjusted to the main content.
- If the content needs to be served through `xlink` with Period, only the Period of the main content is extracted.
- If the content is used for live, especially low-latency live services, the content in the Period should be adjusted to enable consistent playback, including consistent join times.

## IF-5: MPD and Segments with Ad Placements ## {#ad-if5-mpd-segments}


### General ### {#ad-if5-mpd-segments-general}

IF-5 describes the DASH manifest and segment output produced by the [=ad insertion MPD manipulator=].

The ad insertion MPD manipulator operates under the following assumptions:

- DASH content is provided by IF-2.
- Opportunity metadata is provided by IF-3.
- The splice point timing is known as `tsplice-out` when the opportunity starts on media time.
- `tsplice-out` matches the `Period@start` of the main content at the opportunity.
- The end of the ad insertion opportunity, `tsplice-in`, is either known at `tsplice-out` or is initially estimated and later adjusted when `tsplice-in` occurs.
- Properly conditioned ad content is received through IF-4.

Based on this input, the MPD manipulator produces a Media Presentation such that
the IF-5 content can be played back by the DASH client. Additional ad metadata
transported with linear ad creatives is described as part of IF-6.

When serving ad content, three timing cases exist:

1. The selected ad content duration matches the ad opportunity duration in the main content. The return to the main Period is direct.
2. The selected ad content duration exceeds the ad opportunity duration. The ad content needs to be cut short by returning to the main Period, which may require removing or truncating one or more ad-content Periods.
3. The selected ad content duration is shorter than the ad opportunity duration. Additional content can be added, either as another ad if the remaining ad slot is long enough, or as slate content.

Each splice point is signalled with a Period boundary, or at least sufficient
information is available for the MPD proxy to add a Period.

Issue: This is the first IF-5 migration pass from published Part 5 clause 5.7.
The detailed Table 5 MPD element/attribute requirements still need to be
reconstructed from the published source.

### Media Presentation Requirements on IF-5 ### {#ad-if5-media-presentation-requirements}

The content on IF-5 <span class=modal-keyword>shall</span> conform to the DASH
Extended Profile for CMAF content, taking into account multi-period requirements.

When used in the context of ad insertion, this part provides additional
requirements for multi-Period content created from inserted ads. In general, the
client should not be able to differentiate between main-content Periods and
ad-content Periods except through signalled metadata or client/application
policy.

Ad content is spliced into the main content following the Period structure
identified by the published Part 5 Table 5.

<table class="data">
  <caption>Ad Content spliced into main content.</caption>
  <thead><tr><th>Context<th>Element or attribute<th>Use<th>Requirement / description
  <tbody>
    <tr><td>**MPD**<td>**MPD**<td>—<td>Provides the requirements for content that is combined between main content and ad content. Values not specified here are identical to ISO/IEC 23009-1.
    <tr><td>**MPD**<td>**ServiceDescription**<td>—<td>Service description information may be present.
    <tr><td>**ServiceDescription**<td>`Latency@target`<td>0<td>Target latency is provided when applicable.
    <tr><td>**MPD**<td>`@profiles`<td>M<td>Set to `urn:mpeg:dash:profile:cmaf-extended:2019` or `urn:mpeg:dash:profile:cmaf:2019`. The proxy can change to `urn:mpeg:dash:profile:cmaf-extended:2019` if it cannot exactly condition the ads to the Period durations.
    <tr><td>**MPD**<td>`@minimumUpdatePeriod`<td>—<td>Adjusted according to the ad-insertion operation.
    <tr><td>**MPD**<td>**InitializationSet**<td>0 … N<td>If `InitializationSet@inAllPeriods` is `true`, the MPD proxy checks whether it can provide ad content conditioned to the InitializationSet parameters. If it can, it should leave the InitializationSet included. If it cannot, it must set `@inAllPeriods` to `false` or remove the InitializationSet from the MPD.
    <tr><td>`Period (Main content)`<td>**Period**<td>—<td>Specifies a main-content Period. Information from the main-content Period is reused except where specified differently.
    <tr><td>`Period (Main content)`<td>`@duration`<td>R<td><span class=modal-keyword>Shall not</span> be present; the duration is determined by the `@start` of the Ad Period.
    <tr><td>`Period (Main content)`<td>**EventStream**<td>0 … N<td>Reused from the main content.
    <tr><td>`Period (Main content)`<td>**AdaptationSet**<td>1 … N<td>Reused from the main content.
    <tr><td>`Period (Main content)`<td>**AssetIdentifier**<td>0 … 1<td>Reused from the main content.
    <tr><td>`Period (Ad Content)`<td>**Period**<td>0 … N<td>Specifies an Ad Content Period. Information from the Ad Content Period is reused except where specified differently.
    <tr><td>`Period (Ad Content)`<td>`@id`<td>M<td>A unique identifier, preferably reused from one already present in the main content where applicable.
    <tr><td>`Period (Ad Content)`<td>`@start`<td>M<td>Set to `tsplice-out` from the main content.
    <tr><td>`Period (Ad Content)`<td>`@duration`<td>O / remove<td>Typically removed. Detailed operations are described by the MPD proxy operation guidelines.
    <tr><td>`Period (Ad Content)`<td>**BaseURL**<td>1 … N<td>Reused from the remote Ad Content Period unless the ad content is moved elsewhere.
    <tr><td>`Period (Ad Content)`<td>`@availabilityTimeOffset`<td>M<td>Set such that the client can download content according to the schedule of the live service.
    <tr><td>`Period (Ad Content)`<td>**EventStream**<td>0 … N<td>Reused from the remote ad or slate content Period unless the proxy removes events based on business rules.
    <tr><td>`Period (Ad Content)`<td>**AdaptationSet**<td>1 … N<td>Reused from the remote ad or slate content Period. A subset may be selected based on main content or client information. If compatible with an InitializationSet, it should include `@initializationSetRef` referencing the compatible InitializationSet.
    <tr><td>`Period (Ad Content)`<td>**AssetIdentifier**<td>0 … 1<td>Reused from the remote Ad Content Period.
    <tr><td>`Period (Slate Content)`<td>**Period**<td>0 … N<td>Specifies a Slate Content Period. Information from the slate content Period is reused except where specified differently.
    <tr><td>`Period (Slate Content)`<td>`@id`<td>M<td>A unique identifier, preferably using a unique slate content identifier.
    <tr><td>`Period (Slate Content)`<td>`@start`<td>M<td>Typically set to the sum of `tsplice-out` and the duration of the previous ad.
    <tr><td>`Period (Slate Content)`<td>`@duration`<td>O / remove<td>Typically removed. Detailed operations are described by the MPD proxy operation guidelines.
    <tr><td>`Period (Slate Content)`<td>**BaseURL**<td>1 … N<td>Reused from the remote slate content Period unless the slate content is moved elsewhere.
    <tr><td>`Period (Slate Content)`<td>`@availabilityTimeOffset`<td>M<td>Set such that the client can download content according to the schedule of the live service.
    <tr><td>`Period (Slate Content)`<td>**EventStream**<td>0 … N<td>Reused from the remote slate content Period unless the proxy removes events based on business rules. Slate content is not expected to carry Events.
    <tr><td>`Period (Slate Content)`<td>**AdaptationSet**<td>1 … N<td>Reused from the remote slate content Period. A subset may be selected based on main content or client information. If compatible with an InitializationSet, it should include `@initializationSetRef` referencing the compatible InitializationSet.
    <tr><td>`Period (Slate Content)`<td>**AssetIdentifier**<td>0 … 1<td>Reused from the slate content Period.
    <tr><td>`Period (Main Content)`<td>**Period**<td>—<td>Specifies the return-to-main-content Period. Information from the main content Period is reused except where specified differently.
    <tr><td>`Period (Main Content)`<td>`@start`<td>M<td>Set to `tsplice-in` from the main content.
    <tr><td>`Period (Main Content)`<td>`@duration`<td>R<td><span class=modal-keyword>Shall not</span> be present.
    <tr><td>`Period (Main Content)`<td>**EventStream**<td>0 … N<td>Reused from main content.
    <tr><td>`Period (Main Content)`<td>**AdaptationSet**<td>1 … N<td>Reused from main content.
    <tr><td>`Period (Main Content)`<td>**AssetIdentifier**<td>0 … 1<td>Reused from the main content.
</table>

Key: for attributes, `M` means mandatory and `O` means optional. For elements,
values use `minOccurs … maxOccurs`, where `N` means unbounded. The conditions
only hold without using `xlink:href`. If linking is used, then all attributes
are optional and `minOccurs` is `0`.

Issue: This Table 5 reconstruction has been restructured against the DOCX table
structure extracted from `DASH-IF-IOP-Part5-v5.0.0.docx`. The extraction
confirmed 37 rows and the published row groups for **MPD**,
`Period (Main content)`, `Period (Ad Content)`, `Period (Slate Content)`, and
return `Period (Main Content)`. A rendered visual DOCX/PDF review is still
recommended to confirm typography and final row hierarchy.

### MPD Proxy Operation Guidelines ### {#ad-if5-mpd-proxy-guidelines}

In an SSAI architecture, the [=ad insertion MPD manipulator=] may use IF-4 to
request an advertisement decision for part or all of the content stream. The
returned ad placements can be represented as ad pods positioned within the
content stream, with each pod containing one or more ad slots.

The manipulator inserts the **Period** element or elements representing the pod at
the content stream position specified by the ad decisioning response. If the
content MPD already has Period boundaries at the desired ad insertion points, the
manipulator may directly insert the Periods representing the ad placements.

Note: The case where the manipulator receives a content MPD without Period
boundaries at desired insertion points is not covered by this migration pass.
Such a manipulator would need to split content Periods, which may require access
to media segments as well as to the MPD.

If the ad insertion MPD manipulator does not perform an insertion at a
conditioned Period boundary, and if all Adaptation Sets in the new Period
reference exactly one Adaptation Set in a supplemental descriptor for Period
continuity, it should remove this Period element and recombine the Periods.

For scenarios where original in-stream ads are replaced rather than inserted into
a clean stream, the manipulator creates Periods for ad creatives and replaces
sections of the content stream. If the ads are already delineated in the content
MPD, the in-stream Periods are replaced by the generated ones. If not, the
manipulator must perform splitting operations before replacement.

A typical MPD proxy operation flow is:

1. Pass through DASH content from IF-2 for Periods that are not ad Periods.
2. Preserve `MPD@minimumUpdatePeriod` as received from the main server unless an ad-operation constraint requires otherwise.
3. Prepare for content replacement when opportunity metadata is provided through IF-3.
4. Determine or estimate the opportunity duration and request suitable ad content through IF-4a and IF-4b.
5. Insert one or more selected ad-content Periods into the MPD at `tsplice-out`.
6. Remove all main-content Periods that span the opportunity.
7. Continue updating from the main content server while clients continue following the MPD update behaviour.

For inserted ad Periods:

- Period order follows the order of ads declared in the decisioning response.
- The first inserted `Period@start` is equal to `tsplice-out`.
- Each subsequent inserted `Period@start` is equal to the previous `Period@start` plus the previous `Period@duration`.
- `Period@duration` of each inserted Period is removed.
- Adaptation Sets unnecessary for client operation may be removed when the MPD proxy knows the client only needs a subset.
- Period continuity signalling is added where compatible CMAF headers are available.
- Client-targeted Event Streams that exist during the opportunity time in the main content are copied into the insertion Periods, with splitting and signalling updates as needed.

When the ad opportunity is terminated through opportunity metadata, the MPD proxy
updates the MPD according to the relationship between the actual opportunity
duration and the inserted ad content duration:

- If the duration exactly matches the inserted ad content duration, the MPD returns directly to the main content.
- If the opportunity is shorter than the inserted ad content, inserted Periods after `tsplice-in` are removed, the Period containing `tsplice-in` is truncated, and overlap is signalled as needed.
- If the opportunity is longer than the inserted ad content, a new decision is taken to serve another ad or slate content.

In an SGAI architecture, the ad insertion MPD manipulator uses opportunity
metadata from IF-3 to embed signals into the MPD response that allow the DASH
client to defer ad opportunity resolution until actively needed.

Issue: Published Part 5 states that DASH mechanisms for SGAI signalling were
under active study. Keep this section aligned with current Part 10/Part 11 event
and remote-resolution work before turning it into final normative text.

### DASH Client Operation Requirements and Guidelines for Playback ### {#ad-if5-client-playback-guidelines}

A DASH client is expected to consume content offered with the DASH Extended
Profile for CMAF content and DASH-IF multi-period ad content.

For playback within a single Period, the DASH client <span class=modal-keyword>shall</span>
support playback of a single Period of content according to the DASH profile for
CMAF content.

At Period transitions, the DASH client should handle the following cases:

- If the selected Representation in the new Period signals Period continuity and is already loaded to the playback buffer, continue loading segments without timeline adjustment or CMAF header switching.
- If the containing Adaptation Set signals Period continuity to an Adaptation Set in the previous Period but a different Representation is selected, append the Initialization Segment/CMAF Header for the new Representation, then continue loading segments without time adjustment.
- If Period connectivity is signalled and the selected Representation is already loaded from the previous Period, load all segments of the old Period, then adjust playback timing using the new Period start time and presentation time offset.
- If Period connectivity is signalled but a different Representation from the same Adaptation Set is selected, load all segments of the old Period, append the new CMAF header, adjust playback timing, and continue loading the new Representation.
- If no specific signalling is provided for the relation of the current Period and the next Period, the DASH client should either use a change-type call if supported, or clear the prior buffer presentation, append the new CMAF header, adjust timing, and continue loading segments.

Playback of overlapping content at Period boundaries can be optimized by using
append-window start and append-window end signalling to define the portion of the
segment to play. Detailed requirements for this optimization remain for further
study.

## IF-6: Ad Metadata Signalling ## {#ad-if6-ad-metadata}


### General ### {#ad-if6-ad-metadata-general}

IF-6 carries ad metadata associated with ad creatives and ad placements in the
DASH presentation generated by the [=ad insertion MPD manipulator=].

The metadata may be used by the DASH client or an application associated with
the DASH client for functions such as:

- associating inserted Periods with ad decision results,
- identifying ad creatives and ad slots,
- enabling reporting and tracking events,
- triggering callback URLs or other measurement operations, and
- supporting business rules that depend on ad metadata.

The exact metadata format is workflow-dependent. In the published Part 5 model,
the DASH Callback Event is identified as the primary metadata signalling
mechanism to migrate for this interface.

### DASH Callback Event ### {#ad-if6-dash-callback-event}

A DASH Callback Event enables event-based signalling associated with an inserted
advertisement. It is carried as DASH event metadata and can be used to trigger
application-level callbacks, for example for ad tracking or measurement.

When DASH Callback Events are used with inserted ad content:

- the event should be associated with the Period or media timeline region to
  which the callback applies;
- the event payload should contain sufficient information for the application to
  identify the callback action, the ad, and the triggering condition;
- event timing should be aligned with the ad media timeline after any Period
  insertion, splitting, or truncation performed by the MPD proxy; and
- callback metadata should remain consistent with ad decisioning and tracking
  metadata carried through IF-4 and IF-8.

Issue: This IF-6 migration is a source-level baseline. The exact DASH Callback
Event scheme, payload structure, and examples still need to be checked against
the published DOCX/PDF and aligned with current Part 10 event guidance.

## IF-7: Ad Decisioning Parameters and Remote Resolution ## {#ad-if7-remote-resolution}


### General ### {#ad-if7-remote-resolution-general}

IF-7 provides mechanisms for communication between the DASH client and the
[=ad insertion MPD manipulator=] when ad decisioning or content conditioning is
deferred until playback time.

IF-7 supports the SGAI architecture by enabling a DASH client to provide
decisioning or conditioning parameters when it reaches an ad opportunity, rather
than requiring all ad choices to be finalized before the MPD is delivered.

Three IF-7 sub-interfaces are identified:

- IF-7a: decisioning parameters via URL parameters;
- IF-7b: content conditioning via URL parameters; and
- IF-7c: late binding via Remote Periods.

### IF-7a: Decisioning Parameters via URL Parameters ### {#ad-if7a-decisioning-url-parameters}

Decisioning parameters may be passed from the DASH client to the ad insertion MPD
manipulator using URL parameters. The ad insertion MPD manipulator can then use
these values when forming IF-4a requests to the ad decisioning server.

Examples of URL-carried decisioning parameters include:

- content identifier,
- opportunity identifier,
- device type,
- device capabilities,
- service provider,
- user or session attributes where permitted by policy, and
- other values needed by the ad decision service.

The use of URL parameters is deployment-specific. Services should take care that
client-provided parameters are authenticated, authorized, privacy-preserving, and
not trusted beyond their appropriate security context.

### IF-7b: Content Conditioning via URL Parameters ### {#ad-if7b-conditioning-url-parameters}

Content conditioning parameters may be passed from the DASH client to the ad
insertion MPD manipulator using URL parameters. The ad insertion MPD manipulator
can then use these values when forming IF-4b requests to the ad content server.

Examples of URL-carried conditioning parameters include:

- selected video and audio codecs,
- selected resolutions or display constraints,
- encryption modes and key-system constraints,
- splice robustness capabilities,
- buffer or latency constraints,
- current Representation or Adaptation Set information, and
- CMAF header or initialization compatibility information.

The ad content server is expected to use the supplied conditioning information on
a best-effort basis to return ad content suitable for the current playback
context.

### IF-7c: Late Binding via Remote Periods ### {#ad-if7c-remote-periods}

Late binding enables ad opportunity resolution to be deferred until the DASH
client reaches the relevant location in the MPD. A common mechanism is to use a
remote Period or remote entity that the DASH client resolves when needed.

In this model:

1. The ad insertion MPD manipulator receives opportunity metadata through IF-3.
2. The manipulator creates an IF-5 MPD containing a remote reference at the
   opportunity location instead of immediately inserting concrete ad Periods.
3. When playback approaches or reaches the opportunity, the DASH client resolves
   the remote reference.
4. The resolution request carries decisioning and/or conditioning parameters
   through IF-7a and IF-7b.
5. The ad insertion MPD manipulator uses IF-4 to retrieve or condition the
   selected ad content and returns an MPD fragment or Period structure suitable
   for insertion.

Late binding is especially useful when ad decisions depend on the playback
context at the time the opportunity is reached, such as current device
capabilities, client state, or session attributes.

Issue: Published Part 5 describes IF-7c in terms of Remote Periods and late
binding. This migration should be aligned with the current DASH remote entity
model and with Part 10/Part 11 event and remote-resolution work before final
normative stabilization.

## IF-8: Ad Tracking and Measurement ## {#ad-if8-tracking-measurement}


### General ### {#ad-if8-tracking-measurement-general}

IF-8 covers ad tracking and measurement operations associated with inserted ad
content. These operations allow an application, DASH client, or associated
measurement component to report ad playback progress, impressions, completion,
viewability, and other measurement events.

The tracking and measurement interface is driven by metadata supplied by IF-4,
metadata inserted into the MPD or media via IF-6, and playback events observed by
the DASH client or application.

### VAST View Tracking ### {#ad-if8-vast-view-tracking}

VAST [[VAST]] defines tracking events associated with an ad creative. Examples
include impression, start, first quartile, midpoint, third quartile, complete,
pause, resume, mute, unmute, skip, and other events.

When VAST tracking metadata is present, the client application or associated ad
measurement component should emit the corresponding tracking requests when the
specified playback condition is reached.

For dynamic ad insertion, the timing of VAST tracking events should be evaluated
against the inserted ad media timeline after any Period insertion, Period
splitting, truncation, or slate insertion performed by the MPD proxy.

### Open Measurement SDK ### {#ad-if8-open-measurement}

The Open Measurement SDK [[OPENMEASUREMENT]] provides a common framework for ad
viewability and verification measurement. When used with DASH ad insertion, Open
Measurement integration is expected to operate at the application or player
integration layer while using metadata from IF-4 and IF-6 to associate
measurement sessions with the inserted ad creative.

### Alternative Tracking Methods ### {#ad-if8-alternative-tracking}

Other tracking and measurement mechanisms may be used by deployments. Alternative
methods should preserve the same basic mapping between ad decision metadata,
inserted media Periods, playback timeline, and emitted measurement events.

Issue: This IF-8 migration is an initial source-level baseline from the
published heading structure and extracted tracking references. Exact event lists,
callback rules, and any examples should be visually checked against the published
DOCX/PDF and aligned with current DASH-IF tracking/test-asset plans.

# Requirements and Recommendations # {#requirements}

Issue: This section is retained as an editorial collection point while the
published Part 5 clauses are migrated into their structural locations above.
After migration, this section should either be removed or replaced by a concise
summary of testable requirements with links to Part 12 conformance mapping.

[GROUNDED_BY=rag/corpus/published/DASH-IF-IOP-Part5-v5.0.0.docx.extracted.txt]

# Open Issues and Work Items # {#open-issues}

<table class="data">
  <caption>Part 5 open issues and topics to progress.</caption>
  <thead><tr><th>Topic<th>Status<th>Next action
  <tbody>
    <tr><td>Published v5.0.0 migration<td>Structured skeleton added<td>Migrate clause text section-by-section from the published Part 5 source.
    <tr><td>References and bibliography<td>Open<td>Add/normalize published Part 5 references in `part05-ad-insertion.bs`.
    <tr><td>Terms and abbreviations<td>Terms migrated; abbreviations identified<td>Published term definitions migrated; review exact wording and shared terminology, then normalize abbreviations against shared glossary policy.
    <tr><td>Use cases and architecture<td>Initial migration<td>Use cases and architecture prose migrated; extract/redraw published figures and verify wording against DOCX/PDF.
    <tr><td>Architecture figures and tables<td>Table 1 reconstructed<td>Review reconstructed interface overview table against published DOCX/PDF; extract or redraw figures and reconstruct Tables 2–5.
    <tr><td>IF-0/IF-1/IF-9/IF-2 early interfaces<td>IF-0/IF-1/IF-2 hardened<td>IF-0/IF-1 source hardened with splice-point media time, CMAF preparation options, SAP assumptions, timed metadata, and IF-1 sub-interface tracking; IF-2 source hardened with Period-boundary, EventStream, InitializationSet, AssetIdentifier, Period start, continuity, presentationTimeOffset, and eptDelta rules; reconstruct Table 2 and extract/redraw Figures 1, 3, 4, and 5 next.
    <tr><td>IF-3 Ad Avail Signalling<td>Initial migration<td>Published clause 5.5 opportunity metadata carriage, SCTE-35 MPD Event signalling, and example migrated; review Table 3 formatting against DOCX/PDF.
    <tr><td>IF-4 Ad Decisioning and Exchange<td>Initial migration complete<td>Published clause 5.6 initial migration now covers IF-4 introduction, IF-4a, IF-4b, IF-4e, IF-4d, Table 4, IF-4f, and IF-4c; review exact table layout and modal wording against DOCX/PDF.
    <tr><td>IF-5 MPD and segment requirements<td>Table 5 reconstructed<td>Initial published clause 5.7 overview, MPD proxy operation, playback guidance, and Table 5 MPD element/attribute requirements migrated; visually review against published DOCX/PDF.
    <tr><td>IF-6 Ad Metadata Signalling<td>Initial migration<td>DASH Callback Event baseline migrated; verify exact scheme/payload/examples against published DOCX/PDF and Part 10 event guidance.
    <tr><td>IF-7 Decisioning Parameters and Remote Resolution<td>Initial migration<td>URL-parameter decisioning, conditioning, and Remote Period late-binding baseline migrated; align with current remote entity model.
    <tr><td>IF-8 Ad Tracking and Measurement<td>Initial migration<td>VAST tracking, Open Measurement SDK, and alternative tracking baseline migrated; verify detailed event/callback rules.
    <tr><td>Cross-part alignment<td>Open<td>Align terminology and references with Parts 1, 2, 6, and 12.
    <tr><td>Conformance mapping<td>Open<td>Identify validator/test-asset/reference-player expectations and link them to Part 12 after requirements stabilize.
</table>

# Change History # {#change-history}

<table class="data">
  <caption>Part 5 change history.</caption>
  <thead><tr><th>Version<th>Date<th>Change
  <tbody>
    <tr><td>0.1<td>Initial<td>Created initial Bikeshed/Markdown shell for Part 5.
    <tr><td>0.2<td>Reconciliation<td>Replaced shell with a structured skeleton matching the published DASH-IF IOP v5.0.0 Part 5 heading model and migration map.
    <tr><td>0.3<td>Reconciliation<td>Migrated published Part 5 term definitions into Bikeshed definition-list form.
    <tr><td>0.4<td>Reconciliation<td>Added published Part 5 bibliography aliases and reconstructed the interface overview table.
    <tr><td>0.5<td>Reconciliation<td>Migrated initial IF-5 MPD and Segments with Ad Placements overview, MPD proxy operation guidelines, and DASH client playback guidance.
    <tr><td>0.6<td>Reconciliation<td>Reconstructed published Part 5 Table 5 MPD element/attribute requirements for main content and ad insertion content.
    <tr><td>0.7<td>Reconciliation<td>Migrated IF-3 Ad Avail Signalling and initial IF-4 Ad Decisioning and Exchange Interfaces material.
    <tr><td>0.8<td>Reconciliation<td>Completed initial IF-4 migration with DASH-IF ad content storage, Table 4, slate content, and dynamic ad content response guidance.
    <tr><td>0.9<td>Reconciliation<td>Migrated initial IF-6 ad metadata, IF-7 remote resolution, and IF-8 tracking/measurement sections.
    <tr><td>0.10<td>Reconciliation<td>Migrated initial use cases, architecture overview, and IF-0/IF-1/IF-9/IF-2 baseline sections.
    <tr><td>0.11<td>Reconciliation<td>Hardened IF-2 content preparation using published Period-boundary, EventStream, InitializationSet, AssetIdentifier, Period start, continuity, presentationTimeOffset, and eptDelta rules.
    <tr><td>0.12<td>Reconciliation<td>Hardened IF-0 and IF-1 with splice-point media time, CMAF preparation options, SAP assumptions, timed metadata, and IF-1 sub-interface figure tracking.
    <tr><td>5.0.0<td>2021-11<td>Version published as Part 5 v5.0.0.
</table>