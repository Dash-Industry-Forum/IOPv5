<!--
  Live Services — migrated from DASH-IF IOP v4.3 (clause 4, "Live Services")
  via the already-reconciled Part 4 draft clause 5, and aligned to the current
  MPEG-DASH baseline (ISO/IEC 23009-1).
  Provenance: dashif-iop-v4-3#91..#174 ; dashif-iop-v5-part4-draft-r1#30..#100 ;
  iso-iec-23009-1-2026-merged-r5 (UTCTiming, MPD@type, segment availability).
  Editorial: the outdated v4.3 "first/second edition" and "simple vs main live
  interoperability point" framing is intentionally replaced by generic
  references to MPEG-DASH (ISO/IEC 23009-1); normative keywords preserved.
  Fixed 2026-07-28: removed <img /> self-closing slashes, fixed duplicate dfn
  IDs, updated obsolete RFC7232 reference.
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

### Period Timing ### {#live-period-timing}

For a live service (dynamic presentation):

- The first Period <span class=modal-keyword>shall</span> start at or after the zero point of the MPD timeline
  (with a `Period@start` value of 0 seconds or greater).
- The last Period <span class=modal-keyword>may</span> have a `Period@duration`, in which case it has a fixed
  duration. If without `Period@duration`, the last Period in a dynamic
  presentation has an unlimited duration that may later be shortened by an MPD
  update.

Note: A Period with an unlimited duration can be converted to fixed duration by
an MPD update, so even a nominally unlimited duration is effectively constrained
by the MPD validity duration of the current MPD snapshot.

These constraints enable live services to start at any point on the MPD timeline
and support both fixed-duration and open-ended Periods for ongoing live content.

See Part 2 for general period timing rules that apply to all DASH-IF Media
Presentations. See the DASH-IF Guidelines-TimingModel document [[DASHIF-TIMING]]
for detailed discussion of the DASH timing model.

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


### Availability Window ### {#availability-window}

A Media Segment is <dfn export>available</dfn> when an HTTP request to acquire the Media
Segment can be started and successfully performed to completion by a client
[[!MPEGDASH]]. During playback of a dynamic presentation, new Media Segments
continuously become available and stop being available with the passage of time.

An <dfn export>availability window</dfn> is a time span on the MPD timeline that
determines which Media Segments clients can expect to be available. Each Adaptation
Set has its own availability window. Services <span class=modal-keyword><span class=modal-keyword>shall</span> not</span> define MPD attributes
that affect the availability window on the Representation level.

<figure>
  <img src="images/AvailabilityWindow.png">
  <figcaption>The availability window determines which Media Segments can be
  expected to be available, based on where their segment end point lies.</figcaption>
</figure>

Note: A DASH service will typically make Media Segments available some seconds
ahead of the current time, depending on its configuration and latency target.
Furthermore, some Periods <span class=modal-keyword>may</span> be entirely prepared in advance and available at all
times (e.g., ads inserted between truly live content).

The availability window is calculated as follows:

1. Let `now` be the current wall clock time according to the synchronized clock.
2. Let `AvailabilityWindowStart` be `now - MPD@timeShiftBufferDepth`.
   - If `MPD@timeShiftBufferDepth` is not defined, let `AvailabilityWindowStart`
     be the effective availability start time.
3. Let `TotalAvailabilityTimeOffset` be the sum of all `@availabilityTimeOffset`
   values that apply to the Adaptation Set, either via `SegmentBase`,
   `SegmentTemplate`, or `BaseURL` elements [[!MPEGDASH]].
4. The availability window is the time span from `AvailabilityWindowStart` to
   `now + TotalAvailabilityTimeOffset`.

Media Segments that have their segment end point inside or at the end of the
availability window are available [[!MPEGDASH]].

Clients <span class=modal-keyword>may</span> at any point attempt to acquire any Media Segments that the MPD signals
as available. Clients <span class=modal-keyword><span class=modal-keyword>shall</span> not</span> attempt to acquire Media Segments that the MPD
does not signal as available.

Despite best efforts, DASH services occasionally fail to achieve the availability
windows advertised in the MPD. To ensure robust behavior, clients <span class=modal-keyword>should not</span> assume
that Media Segments described by the MPD as available are available and <span class=modal-keyword>should</span>
implement appropriate retry/fallback behavior.

### Time Shift Buffer ### {#time-shift-buffer}

The <dfn export>time shift buffer</dfn> is a time span on the MPD timeline that defines
the set of Media Segments that a client is allowed to present at the current moment
in time according to the wall clock (`now`).

This is the mechanism by which clients can introduce a <dfn export>time shift</dfn> (an
offset) between wall clock time and the MPD timeline when presenting dynamic
presentations. The time shift is zero when a client is presenting the Media Segment
at the end point of the time shift buffer.

The following additional factors further constrain the set of Media Segments that
can be presented at the current time:

1. [[#availability-window]] - not every Media Segment in the time shift buffer is
   guaranteed to be available.
2. [[#presentation-delay]] - the service <span class=modal-keyword>may</span> define a delay that forbids the use of
   a section of the time shift buffer.

The time shift buffer extends from `now - MPD@timeShiftBufferDepth` to `now`. In
the absence of `MPD@timeShiftBufferDepth`, the start of the time shift buffer is
the effective availability start time.

<figure>
  <img src="images/TimeShiftBuffer.png">
  <figcaption>Media Segments overlapping the time shift buffer may potentially be
  presented by a client if other constraints do not forbid it.</figcaption>
</figure>

Clients <span class=modal-keyword>may</span> present samples from Media Segments that overlap the time shift buffer,
assuming no other constraints forbid it. Clients <span class=modal-keyword><span class=modal-keyword>shall</span> not</span> present samples from Media
Segments that are entirely outside the time shift buffer.

A dynamic presentation <span class=modal-keyword>shall</span> contain a Period that ends at or overlaps the end
point of the time shift buffer, except when reaching the end of live content.

Clients <span class=modal-keyword><span class=modal-keyword>shall</span> not</span> allow seeking into regions of the time shift buffer that are not
covered by Periods.

### Presentation Delay ### {#presentation-delay}

There is a natural conflict between the availability window and the time shift
buffer. It is legal for a client to present Media Segments as soon as they overlap
the time shift buffer, yet such Media Segments might not yet be available.

The mechanism that allows DASH clients to resolve this conflict is the
<dfn export>presentation delay</dfn>, which decreases the time shift buffer by moving its
end point into the past, creating an <dfn export>effective time shift buffer</dfn> with a
reduced duration.

Clients <span class=modal-keyword>shall</span> calculate a suitable presentation delay to ensure that the Media
Segments it schedules for playback are available and that there is sufficient time
to download them once they become available.

Note: Calculating an optimal presentation delay requires knowledge of Segment
durations, availability timing, network conditions, and buffer requirements.

The information required to calculate an optimal presentation delay might not always
be available to DASH clients. Services <span class=modal-keyword>may</span> define the
`MPD@suggestedPresentationDelay` attribute to provide a suggested presentation
delay. Clients <span class=modal-keyword>should</span> use `MPD@suggestedPresentationDelay` when provided by the MPD.

<figure>
  <img src="images/WindowInteractions.png">
  <figcaption>The interaction between availability window, time shift buffer, and
  presentation delay determines which Media Segments can be presented at any given
  time.</figcaption>
</figure>
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

### MPD Snapshot Validity ### {#live-mpd-snapshot-validity}

The MPD of a dynamic presentation remains valid not only at its moment of initial
publishing but through the entire <dfn export>MPD validity duration</dfn>, which is a
time span of duration `MPD@minimumUpdatePeriod` starting from the moment the MPD
download is started by a client [[!MPEGDASH]].

Clients <span class=modal-keyword>shall</span> process state changes that occur during the MPD validity duration.
For example, new Media Segments will become available over time if they are
referenced by the MPD and old ones become unavailable, even without downloading a
new snapshot of the MPD.

The presence or absence of `MPD@minimumUpdatePeriod` <span class=modal-keyword>shall</span> be used by DASH services
to signal whether and when the MPD might be updated:

- A nonzero value for `MPD@minimumUpdatePeriod` defines the MPD validity duration
    of the present snapshot of the MPD, starting from the moment its download was
    initiated. This allows the service to provide regular updates to the MPD while
    limiting the refresh interval to avoid overload.
- The value 0 for `MPD@minimumUpdatePeriod` indicates that the MPD has no
    validity after the moment it is retrieved. In such a situation, the client
    <span class=modal-keyword>shall</span> acquire a new MPD whenever it wants to make new Media Segments available.
- Absence of the `MPD@minimumUpdatePeriod` attribute indicates an infinite
    validity (the MPD will never be updated).

### Adding Content to the MPD ### {#live-mpd-add-content}

[[!MPEGDASH]] allows the following mechanisms for adding content to a dynamic
presentation:

- Additional Segment references <span class=modal-keyword>may</span> be added to the last Period.
- Additional Periods <span class=modal-keyword>may</span> be added to the end of the MPD.

Segment references <span class=modal-keyword>shall</span> not be added to any Period other than the last Period.

<figure>
  <img src="images/MpdUpdate-AddContent.png">
  <figcaption>MPD updates can add both Segment references and Periods (additions
  highlighted in blue).</figcaption>
</figure>

A live service will typically use a Period with an unlimited duration to
continuously add new Segment references. An MPD update that adds content <span class=modal-keyword>may</span> be
combined with an MPD update that removes content.

### Removing Content from the MPD ### {#live-mpd-remove-content}

[[!MPEGDASH]] allows the following mechanisms for removing content from a dynamic
presentation:

- The last Period <span class=modal-keyword>may</span> change from unlimited duration to fixed duration.
- The duration of the last Period <span class=modal-keyword>may</span> be shortened.
- One or more Periods <span class=modal-keyword>may</span> be removed entirely from the end of the MPD timeline.
- Expired Periods and Segment references that no longer overlap the time shift
    buffer <span class=modal-keyword>may</span> be removed from the start of the MPD timeline.

Removal of content is only allowed if the content to be removed is expired or not
yet available to clients and guaranteed not to become available within the MPD
validity duration of any MPD snapshot potentially downloaded by clients.

To determine the content that may be removed, calculate `EarliestRemovalPoint` as
follows for each Adaptation Set:

1. Let `PublishingDelay` be the end-to-end delay for MPD update publishing (the
    time between the MPD generator creating a new version and it becoming published
    to all clients on the CDN edge).
2. Let `AvailabilityWindowEnd` be the end point of the availability window.
3. Let `EarliestRemovalPoint` be `AvailabilityWindowEnd + MPD@minimumUpdatePeriod + PublishingDelay`.

An MPD update removing content <span class=modal-keyword>shall</span> not remove any Segment references to Media
Segments with a segment start point before or at `EarliestRemovalPoint`.

<figure>
  <img src="images/MpdUpdate-RemoveContent.png">
  <figcaption>MPD updates can remove both Segment references and Periods (removals
  highlighted in red).</figcaption>
</figure>

Explicitly defined Segment references (`S` elements) <span class=modal-keyword>shall</span> be removed when they
have expired (i.e. the segment end point has fallen out of the time shift buffer).
Periods with their end points before the time shift buffer <span class=modal-keyword>shall</span> be removed.

### End of Live Content ### {#live-mpd-end}

Live services can reach a point where no more content will be produced. When an
MPD is updated to a state that describes the final content of a live service, the
service <span class=modal-keyword>shall</span>:

- Define a fixed duration for the last Period.
- Remove the `MPD@minimumUpdatePeriod` attribute.
- Cease performing MPD updates.

This signals to clients that no more content will be added to the MPD.

Upon detecting the removal of `MPD@minimumUpdatePeriod`, clients <span class=modal-keyword>should</span> present a
user experience suitable for end of live content.

Note: A common mistake is to treat the eventual cessation of new content as a
transient or fatal error, resulting in potentially infinite loading even before
the final Media Segment is presented to the user.

If the ending live service is to be converted to a static presentation for
on-demand viewing, the service <span class=modal-keyword>may</span> change `MPD@type` to `static` when
`MPD@minimumUpdatePeriod` is removed or do so at a later time. Clients <span class=modal-keyword>shall</span> not
lose track of the playback position if a dynamic presentation becomes a static
presentation.

### MPD Refreshes ### {#live-mpd-refreshes}

To stay informed of MPD updates, clients need to perform <dfn export>MPD refreshes</dfn>
at appropriate moments to download updated MPD snapshots.

Clients presenting dynamic presentations <span class=modal-keyword>shall</span> execute the following MPD refresh
logic:

1. When an MPD snapshot is downloaded, it is valid for the MPD validity duration
    as measured from the moment the download is initiated.
2. A client can expect to be able to successfully download any Media Segments that
    the MPD defines as available at any point during the MPD validity duration.
3. The client <span class=modal-keyword>may</span> refresh the MPD at any point to obtain more Segment references
    or extend the MPD validity duration.

Note: There is no requirement that clients poll for updates at
`MPD@minimumUpdatePeriod` interval. They can do so as often or as rarely as they
wish — this attribute simply defines the MPD validity duration.

Clients using HTTP to perform MPD refreshes <span class=modal-keyword>should</span> use conditional GET requests
as specified in [[!RFC7232 obsolete]] to avoid unnecessary data transfers when the
contents of the MPD do not change between refreshes.

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