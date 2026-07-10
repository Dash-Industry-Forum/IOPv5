<!--
  Part 3: On-demand services.
  Drafted from DASH-IF IOP v4.3 clause "On-Demand Services":
  dashif-iop-v4-3#72..#90, and aligned with Part 2 core principles.
-->

# Scope # {#scope}

This document specifies DASH-IF IOP v5 requirements and recommendations for
on-demand services. An on-demand service is a DASH Media Presentation for which
the media is available before playback and for which clients have flexibility to
start, pause, seek, and perform trick-mode operations subject to the advertised
MPD and media structure.

This part builds on Part 2. Media-specific constraints are defined in Parts 7, 8,
and 9. Content protection constraints are defined in Part 6.

# References # {#doc-references}

The following referenced documents are necessary for the application of this
part:

- ISO/IEC 23009-1 [[!MPEGDASH]].
- ISO/IEC 14496-12 [[!ISOBMFF]].
- ISO/IEC 23000-19 [[!MPEGCMAF]].
- DASH-IF IOP v5 Part 2, *Core Principles and CMAF Mapping*.

# Terms and Definitions # {#terms}

: <dfn export>On-Demand Service</dfn>
:: A DASH service offered using a static Media Presentation where the announced
    media is available independently of wall-clock publication over time.
: <dfn export>DASH-IF On-Demand Profile</dfn>
:: The DASH-IF on-demand interoperability profile historically identified by
    `http://dashif.org/guidelines/dash-if-ondemand`.
: <dfn export>Mixed On-Demand Content</dfn>
:: Multi-Period on-demand content in which different Periods may use different
    on-demand-compatible representation structures, subject to explicit profile
    signalling.

# On-Demand Services # {#on-demand-services}

## Introduction ## {#introduction}

MPEG-DASH provides several tools for on-demand streaming. A DASH Media
Presentation with `MPD@type="static"` indicates that all media announced in the
MPD is available for playback. This enables clients to start at different times,
pause playback, seek, and perform trick modes such as fast-forward where
supported by the media and MPD.

Earlier IOP versions described both on-demand services using live-profile
segment structures and on-demand services using the MPEG-DASH On-Demand profile.
IOP v5 keeps the distinction as an authoring choice, but Part 2 provides the
common timing and Segment information model.

## Common MPD Requirements ## {#common-mpd-requirements}

For an on-demand service:

- `MPD@type` shall be `static`.
- The Media Presentation duration shall be determinable from
    `MPD@mediaPresentationDuration` or from the duration of the last Period.
- `MPD@minimumUpdatePeriod` shall not be present.
- `MPD@timeShiftBufferDepth` should not be present; if present, a client is
    expected to ignore it.
- `MPD@suggestedPresentationDelay` should not be present; if present, a client is
    expected to ignore it.
- Segment availability shall not depend on wall-clock publication over time.

## Segment Information Derivation ## {#segment-information-derivation}

Based on the MPD, a DASH client derives the list of Segments for each
Representation in each Period. For each Period, the Period start and Period end
are computed using the rules of ISO/IEC 23009-1 and Part 2. For each
Representation, the Segment list is computed from `SegmentTemplate`,
`SegmentTimeline`, `SegmentBase`, or the selected on-demand profile structure.

For `SegmentTimeline`-based Representations, the `S` elements and their `@t`,
`@d`, and `@r` values define the media timeline, including any gaps. Each Media
Segment has an earliest presentation time and an accurate Segment duration,
which may be estimated from the MPD or determined from the Segment itself.

Synchronized playout and seamless switching are achieved by aligning
Representations according to presentation time within the Period. Clients shall
use presentation time, not download order, as the synchronization basis across
Adaptation Sets and within switchable Representations.

## On-Demand Services Using Live-Profile Segment Structures ## {#ondemand-live-profile-structures}

On-demand content may use Segment structures also used by live services, for
example `SegmentTemplate` with `$Number$` or `$Time$`. This can simplify reuse of
live packagers and client logic. When such structures are used for an on-demand
service, the MPD remains static and the dynamic-service attributes listed in
[[#common-mpd-requirements]] shall not be used.

Issue: Reconstruct the v4.3 table "Information related to Segment Information
for Using Live Profiles for On-Demand Services" and align it with the Part 2
SegmentTemplate parameter table. [GROUNDED_BY=dashif-iop-v4-3#74..#80]

## On-Demand Services Using the MPEG-DASH On-Demand Profile ## {#ondemand-profile}

On-demand services may use on-demand DASH profiles defined by ISO/IEC 23009-1.
Historically, DASH-IF defined the DASH-IF On-Demand Profile identified by
`http://dashif.org/guidelines/dash-if-ondemand`.

The DASH-IF On-Demand Profile is based on the MPEG-DASH Extended ISO BMFF
On-Demand profile. The following requirements apply unless superseded by an IOP
v5 profile decision:

- Each Representation shall contain one Segment that complies with the Indexed
    Self-Initializing Media Segment structure.
- `@indexRange` shall be present in the MPD.
- Only a single `sidx` box shall be present for the Representation index.
- The `sidx` box shall describe the subsegments (movie fragments) needed for
    client request construction.

Note: v4.3 emphasized operational advantages of the on-demand profile: fewer
files, easier content management, improved cache behaviour, and lower
packager/origin/CDN complexity.

Issue: Confirm whether `http://dashif.org/guidelines/dash-if-ondemand` remains
the IOP v5 profile identifier, is deprecated, or is replaced by a new v5 URI.
[GROUNDED_BY=dashif-iop-v4-3#82..#84]

## Service Offering Requirements and Guidelines ## {#service-offering}

An on-demand service offering shall provide all MPD information required by the
selected Segment information mode or profile. If the On-Demand profile is used,
`@indexRange` shall allow the client to retrieve the Segment Index. The Segment
Index should be sufficient to build the subsegment request timeline for the
Representation.

For multi-Period on-demand content, Period timing shall be explicit and
consistent. Adjacent Periods that are intended for continuous playout should
follow the Good Multi-Period CMAF Content requirements of Part 2.

## Client Operation, Requirements and Guidelines ## {#client-operation}

A client supporting on-demand services shall parse the MPD, determine the Period
and Representation timing, derive the Segment or byte-range request list, and
schedule playback according to presentation time.

For the On-Demand profile, the client typically requests the initialization data
and the Segment Index, parses the `sidx` box, and constructs a list of URL and
byte-range requests for the referenced subsegments. A client may retrieve only
the initial portion of a Representation index to reduce startup delay, provided
it can continue retrieving index information as needed without violating the
presentation timeline.

## Mixed On-Demand Content ## {#mixed-on-demand}

On-demand content may be offered as multiple Periods. Earlier IOP versions
identified a DASH-IF Mixed Profile `http://dashif.org/guidelines/dash-if-mixed-ondemand`.
A mixed on-demand service may contain multiple Periods, and each Period shall
explicitly signal the applicable profile or representation structure.

A client claiming support for mixed on-demand content shall support multi-Period
playback and the representation structures used by the Periods. Mixed on-demand
content does not imply support for dynamic services.

Issue: Confirm the status of the DASH-IF Mixed On-Demand profile URI in IOP v5
and define the relationship to Part 2 Good Multi-Period CMAF Content.
[GROUNDED_BY=dashif-iop-v4-3#90]

# Open Issues and Work Items # {#open-issues}

<table class="data">
  <caption>Part 3 open issues and topics to progress.</caption>
  <thead><tr><th>Topic<th>Status<th>Source grounding<th>Next action
  <tbody>
    <tr><td>Live-profile segment structures for on-demand<td>Partial<td>`dashif-iop-v4-3#74..#80`<td>Rebuild the MPD/Segment information table and align with Part 2.
    <tr><td>DASH-IF On-Demand profile URI<td>Open<td>`dashif-iop-v4-3#82..#84`<td>Confirm keep/deprecate/replace for IOP v5.
    <tr><td>`sidx` constraints<td>Partial<td>`dashif-iop-v4-3#87..#89`<td>Review against current ISO BMFF and MPEG-DASH editions.
    <tr><td>Mixed on-demand profile<td>Open<td>`dashif-iop-v4-3#90`<td>Confirm URI/status and align with Part 2 multi-Period CMAF.
    <tr><td>Trick modes<td>Open<td>v4.3 related clauses<td>Decide whether on-demand trick-mode requirements live in Part 3 or Part 11.
</table>

# Change History # {#change-history}

<table class="data">
  <caption>Part 3 change history.</caption>
  <thead><tr><th>Version<th>Date<th>Change
  <tbody>
    <tr><td>0.1<td>Initial<td>Initial Bikeshed draft from DASH-IF IOP v4.3 on-demand services, aligned with Part 2.
</table>
