<!--
  Live Services — migrated from DASH-IF IOP v4.3 (clause 4, "Live Services")
  via the already-reconciled Part 4 draft clause 5, and aligned to the current
  MPEG-DASH baseline (ISO/IEC 23009-1).
  Provenance: dashif-iop-v4-3#91..#174 ; dashif-iop-v5-part4-draft-r1#30..#100 ;
  iso-iec-23009-1-2026-merged-r5 (UTCTiming, MPD@type, segment availability).
  Editorial: the outdated v4.3 "first/second edition" and "simple vs main live
  interoperability point" framing is intentionally replaced by generic
  references to MPEG-DASH (ISO/IEC 23009-1); normative keywords preserved.
-->

# Live Services # {#live-services-clause}

Note: This clause is migrated from DASH-IF IOP v4.3 (Live Services) and aligned
to the current edition of MPEG-DASH [[!MPEGDASH]]. References to specific past
editions of ISO/IEC 23009-1 have been removed in favour of the current edition.

## Introduction ## {#live-introduction}

MPEG-DASH [[!MPEGDASH]] provides several tools to support live services. This
clause provides requirements and recommendations for both content authoring and
client implementations. It clarifies and refines the interoperability details of
dynamic (live) service configurations and client behaviour, based on the features
of the current edition of ISO/IEC 23009-1.

Note: Earlier versions of this document distinguished a "simple live" and a
"main live" interoperability point tied to the 2012 and 2014 editions of
MPEG-DASH. That distinction is no longer maintained: the current edition of
ISO/IEC 23009-1 provides a unified set of live tools, and this clause is written
against that baseline. Low-latency operation is specified separately in
[[#low-latency]].

## Overview: Dynamic and Live Media Presentations ## {#live-overview}

A DASH Media Presentation with `MPD@type` set to `dynamic` allows media to be
made available over time, and its availability <span class=modal-keyword>may</span> also be removed over time.
This has two major effects:

1. The content author can announce a DASH Media Presentation for which not all
    content is yet available, but only becomes available over time.
2. Clients follow a timed playout schedule as intended by the content author.

Dynamic services <span class=modal-keyword>may</span> be used for different types of service:

: <dfn export>Dynamic Distribution of Available Content</dfn>
:: Content that is made available as dynamic content but is entirely generated
    prior to distribution. The details of the Media Presentation — in particular
    the Segments (duration, URLs) — are known and can be announced in a single
    MPD without MPD updates.
: <dfn export>MPD-controlled Live Service</dfn>
:: A live service for which the client polls and reloads the MPD following
    `MPD@minimumUpdatePeriod` to discover newly available Segments and Periods.
: <dfn export>MPD- and Segment-controlled Live Service</dfn>
:: A live service for which the client is additionally informed of MPD changes
    by inband information carried in the Segments (for example, MPD validity
    expiry events), reducing reliance on periodic MPD polling.

## Dynamic Segment Download ## {#live-segment-download}

### Background and Assumptions ### {#live-download-background}

The dynamic segment download function is a key component of live services and <span class=modal-keyword>may</span>
also be used for scheduling a playout. In this clause it is assumed, unless
stated otherwise, that the client has access to a single instance of an MPD and
that all information about the entire Media Presentation is contained in that
MPD; MPD updates are addressed in [[#live-mpd-updates]].

We refer to such a service as a *dynamic service*: its defining feature is that
Segments are made available over time following the schedule of the media
timeline. Dynamic services are documented primarily to explain the timing model
of Segment availability, which forms the basis for live services.

### Segment Availability Timing Model ### {#live-timing-model}

Segment availability is governed by the timing model of ISO/IEC 23009-1. For a
Media Presentation accessible at time `NOW` at its location:

- All Segments for all Representations in all Periods announced in an MPD <span class=modal-keyword>shall</span> be
    available no later than their announced Segment Availability Start Time
    (SAST) at their derived URLs.
- All such Segments <span class=modal-keyword>shall</span> remain available at least until their announced Segment
    Availability End Time (SAET) at their derived URLs.
- For all Media Segments, the Segment in a Period is available no later than the
    sum of the Period start (in wall-clock time), the earliest presentation time,
    and the segment duration.

Note: The derivation of SAST, SAET, and Segment URLs follows the addressing and
timing rules of ISO/IEC 23009-1 (`SegmentTemplate`, `SegmentTimeline`,
`@availabilityStartTime`, `@availabilityTimeOffset`, `@presentationTimeOffset`).

### Segment Information Derivation ### {#live-segment-derivation}

Based on an MPD available at time `NOW` on the server, a synchronized DASH client
derives the list of Segments for each Representation in each Period. The following
definitions, aligned with ISO/IEC 23009-1, apply:

: <dfn export>available Segment</dfn>
:: A Segment that is accessible at its assigned HTTP-URL: an HTTP GET to the URL
    returns the Segment with a 2xx status code.
: <dfn export>valid Segment URL</dfn>
:: An HTTP-URL that is promised to reference a Segment during its Segment
    availability period.
: <dfn export>NOW</dfn>
:: The wall-clock time on the content server. All wall-clock-related information
    in the MPD is expressed relative to `NOW`.

**MPD information.** For a dynamic service without MPD updates: `MPD@type` <span class=modal-keyword>shall</span>
be `dynamic`; `MPD@mediaPresentationDuration` <span class=modal-keyword>shall</span> be present, or the
`Period@duration` of the last Period <span class=modal-keyword>shall</span> be present; `MPD@minimumUpdatePeriod`
<span class=modal-keyword><span class=modal-keyword>shall</span> not</span> be present. It is recommended to provide `MPD@timeShiftBufferDepth` and
`MPD@suggestedPresentationDelay`.

**Period information.** Each Period *i* is assigned a Period start time in
wall-clock time (PSwc[i]) and a Period end time in wall-clock time (PEwc[i]),
determined per ISO/IEC 23009-1:

- If `Period@start` is present, PSwc[i] is the sum of `MPD@availabilityStartTime`
    (AST) and `@start`.
- Otherwise, if the previous Period has `@duration`, PSwc[i] is the previous
    Period start plus that duration (`@start`, if also present, takes precedence).
- The Period end time PEwc[i] is the start of the next Period (PSwc[i+1]); for the
    last Period it derives from `MPD@mediaPresentationDuration` or the last
    `Period@duration`, and an MPD update <span class=modal-keyword>may</span> extend it.

**Representation information.** For a Period *i*, when `SegmentTemplate.SegmentTimeline`
is present (and `SegmentTemplate@duration` is not), the `SegmentTimeline` contains
`S` elements with `@t` (start time), `@d` (duration), and `@r` (repeat count),
from which the number and timing of Segments — and hence SAST/SAET and URLs — are
derived using `@timescale` and any applicable `@availabilityTimeOffset`. A
negative `@r` repeats until the next `@t` or the Period end. Gaps are possible and
indicate that no media is present for the gap.

**Media time information.** Each Media Segment *k* has an earliest presentation
time (EPT[k,r,i]) and an accurate duration, measured in media presentation time.
EPT <span class=modal-keyword>may</span> be estimated from the MPD (SAST minus announced segment duration) or
determined accurately from the Segment itself.

### Service Offering Requirements and Guidelines ### {#live-so-requirements}

For dynamic service offerings, the MPD <span class=modal-keyword>shall</span> conform to DASH-IF IOP and <span class=modal-keyword>shall</span> at
least contain the mandatory information required by ISO/IEC 23009-1 for a dynamic
Media Presentation:

- `MPD@type` <span class=modal-keyword>shall</span> be set to `dynamic`.
- `MPD@availabilityStartTime` <span class=modal-keyword>shall</span> be present and provides the wall-clock anchor
    for the Media Presentation timeline.
- `MPD@publishTime` <span class=modal-keyword>shall</span> be present and <span class=modal-keyword>shall</span> be updated whenever the MPD content
    changes, so that clients can detect a changed MPD.
- Where the presentation end time is not known in advance,
    `MPD@minimumUpdatePeriod` <span class=modal-keyword>shall</span> be present; the Period end time of the last
    Period is then obtained as the sum of `NOW` and `MPD@minimumUpdatePeriod`.

Content <span class=modal-keyword>may</span> be offered as a single Period or as multiple Periods (for example for
ad insertion opportunities, program changes, or operational purposes). Segment
information <span class=modal-keyword>may</span> be provided using `SegmentTemplate` with `@duration`, or using
`SegmentTemplate` with `SegmentTimeline`.

## Live Service Offering including MPD Updates ## {#live-mpd-updates}

### Preliminaries ### {#live-updates-preliminaries}

To offer a live service with an unknown presentation end time using a single
evolving MPD, the service provider publishes an initial MPD prior to the
presentation start so that clients <span class=modal-keyword>may</span> access it in advance. The MPD is assigned
a publish time, and clients reload the MPD over time to discover newly available
Segments and Periods.

### Service Offering Requirements and Guidelines ### {#live-updates-requirements}

For a live service offering that relies on MPD updates:

- The same general dynamic service requirements in [[#live-so-requirements]]
    apply at any time `NOW` that the MPD is present on the server.
- `MPD@minimumUpdatePeriod` <span class=modal-keyword>shall</span> be set to a value consistent with the rate at
    which the timeline is extended and with any change lead time the service
    guarantees.
- On each change, the service <span class=modal-keyword>shall</span> write a new MPD with an updated
    `MPD@publishTime`; clients detect the change by comparing publish times.
- `MPD@minimumUpdatePeriod` <span class=modal-keyword>may</span> be set to `0` to indicate that the client <span class=modal-keyword>should</span>
    revalidate the MPD before requesting each Segment when the timeline is not
    predictable.

Note: MPD updates are the baseline mechanism for live. Additional, lower-latency
signalling of MPD changes is provided by the segment-based mechanism in
[[#live-segment-based]].

## MPD- and Segment-based Live Service Offering ## {#live-segment-based}

### Preliminaries ### {#live-segment-based-preliminaries}

In addition to periodic MPD polling, ISO/IEC 23009-1 allows the client to be
informed of MPD changes by inband information carried in the Segments. This
reduces the need for frequent MPD requests and allows the timeline to be extended
and terminated with lower signalling latency.

### Service Offering Requirements and Guidelines ### {#live-segment-based-requirements}

For a service offering that relies on segment-based MPD update signalling:

- The service <span class=modal-keyword>shall</span> carry inband events indicating MPD validity expiry (the
    `urn:mpeg:dash:event:2012` scheme, or the applicable scheme of the current
    edition) so that clients learn when the current MPD is no longer valid.
- The `InbandEventStream` element <span class=modal-keyword>shall</span> be signalled for the Adaptation Sets or
    Representations that carry these events.
- When segment-based updates are used, the client <span class=modal-keyword>may</span> extend the timeline based
    on Segment information without reloading the MPD until an MPD validity expiry
    event indicates that a new MPD is required.

## Availability Time Synchronization between Client and Server ## {#live-time-sync}

### Background ### {#live-sync-background}

According to ISO/IEC 23009-1, in order to correctly access MPDs and Segments that
become available over time, DASH servers and clients <span class=modal-keyword>should</span> synchronize their
clocks to a globally accurate time standard. Segment availability times are
announced in wall-clock time in the MPD, and the client needs access to the same
time base as the MPD generation in order to request Segments at the right time.

### Service Provider Requirements and Guidelines ### {#live-sync-service}

If the Media Presentation is dynamic, or if `MPD@availabilityStartTime` is
present, the service <span class=modal-keyword>shall</span> provide a Media Presentation as follows:

- The Segment availability times announced in the MPD <span class=modal-keyword>should</span> be generated from a
    device synchronized to a globally accurate timing source, preferably using
    NTP.
- The MPD <span class=modal-keyword>should</span> contain at least one `UTCTiming` element with `@schemeIdUri` set
    to one of the schemes defined by ISO/IEC 23009-1, namely:
    - `urn:mpeg:dash:utc:http-xsdate:2014`
    - `urn:mpeg:dash:utc:http-iso:2014`
    - `urn:mpeg:dash:utc:http-ntp:2014`
    - `urn:mpeg:dash:utc:ntp:2014`
    - `urn:mpeg:dash:utc:http-head:2014`
    - `urn:mpeg:dash:utc:direct:2014`
- If the MPD does not contain any `UTCTiming` element, then the Segments <span class=modal-keyword>shall</span> be
    available no later than the announced Segment availability time using a
    globally accurate timing source.

Note: The MPD time does not track leap seconds; if a leap second occurs during a
live service it <span class=modal-keyword>may</span> advance or retard the media against real time. DVB-DASH
requires support for `http-xsdate` and `http-head`.

### Client Requirements and Guidelines ### {#live-sync-client}

If the Media Presentation is dynamic, or if `MPD@availabilityStartTime` is
present, the client <span class=modal-keyword>should</span> do the following:

- If the MPD does not contain any `UTCTiming` element, the client <span class=modal-keyword>should</span> acquire
    an accurate wall-clock time from its system. The anticipated inaccuracy of the
    timing source <span class=modal-keyword>should</span> be taken into account when requesting Segments close to
    their availability-time boundaries.
- If the MPD contains one or more `UTCTiming` elements, the client <span class=modal-keyword>should</span> use at
    least one of the announced timing methods to synchronize its clock. The client
    must not request Segments prior to their Segment Availability Start Time with
    reference to the chosen `UTCTiming` method.

## Client Operation, Requirements and Guidelines ## {#live-client}

### General ### {#live-client-general}

A DASH client offering a live service consumes the MPD and, using a clock
synchronized per [[#live-time-sync]], derives the available Segments per
[[#live-segment-derivation]]. The client schedules requests so that a Segment is
requested no earlier than its Segment Availability Start Time and no later than
its Segment Availability End Time, and manages a buffer to absorb throughput
variation while maintaining the presentation schedule.

### Joining, Initial Buffering and Playout ### {#live-client-joining}

When joining a live service, the client <span class=modal-keyword>should</span>:

- Determine the live edge from the MPD timeline and the synchronized wall-clock
    time, taking `MPD@suggestedPresentationDelay` into account where present to
    select the initial presentation time.
- Begin playout at a presentation time that leaves sufficient buffer within the
    time-shift buffer (`MPD@timeShiftBufferDepth`) to avoid rebuffering, while
    honouring any latency target of the service.
- Prefer to start at a random access point rather than presenting stale media,
    to keep the join latency consistent.
- Not request Segments prior to their Segment Availability Start Time with
    reference to the chosen `UTCTiming` method (see [[#live-sync-client]]).

Note: Detailed low-latency joining, buffer management, and resynchronisation are
specified in [[#low-latency]].

## Provisioning of Live Content in On-Demand Mode ## {#live-to-vod}

A completed live service <span class=modal-keyword>may</span> be offered subsequently as an on-demand service. In
this case the Media Presentation is converted to `MPD@type` set to `static`, the
timeline is finalised, and `MPD@minimumUpdatePeriod` and live-only signalling
(such as `UTCTiming` for availability) are removed or adjusted per ISO/IEC
23009-1.

Issue: Reconcile detailed live-to-VoD conversion guidance with the DASH-IF
Live-to-VoD guideline and the Part 4 draft; migrate remaining v4.3 detail (trick
mode for live, reliable/consistent-delay live) in a subsequent pass.
