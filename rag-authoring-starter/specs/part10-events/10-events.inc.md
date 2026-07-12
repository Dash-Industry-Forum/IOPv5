<!--
  Part 10: Events.
  Initial Bikeshed/Markdown shell following the IOPv5 authoring convention.
  Source grounding / migration target: iop-docs-overview / Part 2 content annotation placeholders.
  Normative content in this revision is migrated from:
  - Dash-Industry-Forum/DASH-IF-IOP branch v5-old-draft, 40-Features.inc.md
    (update signaling via in-band events / MPD validity events)
  - Dash-Industry-Forum/DASH-IF-IOP branch v5-old-draft, 65-AdInsertion.inc.md
    (general DASH events model, MPD events, DASH Callback events)
-->

# Scope # {#scope}

This document specifies DASH-IF IOP v5 Part 10: **Events**. Event signalling and processing, including MPD events, inband events, and timed metadata tracks.

# References # {#doc-references}

The following referenced documents are necessary for the application of this
part:

- ISO/IEC 23009-1 [[!MPEGDASH]].
- ISO/IEC 23000-19 [[!MPEGCMAF]].
- DASH-IF IOP v5 Part 2, *Core Principles and CMAF Mapping*.
- DASH-IF IOP v5 Part 5, *Ad Insertion and Content Replacement*.
- DASH-IF IOP v5 Part 12, *Conformance and Reference Tools*.

# Terms and Definitions # {#terms}

Terms and definitions are inherited from ISO/IEC 23009-1, ISO/IEC 23000-19, and
Part 2 unless defined in this part.

# DASH Events Overview # {#events-overview}

DASH events are messages having type, timing and optional payload. They can appear either in the MPD (as a Period-level `EventStream` element) or inband, as ISO BMFF boxes of type `emsg`. The `emsg` boxes <span class=modal-keyword>shall</span> be placed at the very beginning of the Segment, i.e. prior to any media data, so that a DASH client needs a minimal amount of parsing to detect them.

DASH defines events that are processed directly by a DASH client: MPD Validity Expiration, MPD Patch, and MPD Update. These signal to the client that the MPD needs to be updated, either by providing the publish time of the MPD that should be used, by providing an XML patch that can be applied to the client's in-memory representation of the MPD, or by providing a complete new MPD.

User-defined events are also possible. The DASH client does not process these directly — they are passed to an application, or discarded if there is no application willing or registered to process these events. A possible client API would allow an application to register callbacks for specific event types, triggered when the DASH client parses the `emsg` box in a Segment or the `Event` element in the MPD. User-defined events can, for example, be used to signal cue messages such as SCTE-35 in an ad-insertion context (see Part 5).

If several `emsg` boxes are present in a Segment and one of them is the MPD Validity Expiration event, the `emsg` carrying it <span class=modal-keyword>shall</span> always appear first.

# Update Signaling via In-Band Events # {#inband}

Services <span class=modal-keyword>may</span> signal the MPD validity duration by embedding in-band messages into Representations instead of specifying a fixed validity duration in the MPD. This allows services to trigger MPD refreshes at exactly the desired time and to avoid needless MPD refreshes.

This clause only applies to services and clients that use in-band MPD validity signaling.

Services <span class=modal-keyword>shall</span> define `MPD@minimumUpdatePeriod=0` and add an in-band event stream to every audio Representation or, if no audio Representations are present, to every video Representation. The in-band event stream <span class=modal-keyword>may</span> also be added to other Representations. The in-band event stream <span class=modal-keyword>shall</span> be identical in every Representation where it is present.

The in-band event stream <span class=modal-keyword>shall</span> be signaled on the adaptation set level by an `InbandEventStream` element with `@scheme_id_uri="urn:mpeg:dash:event:2012"` and a `@value` of 1 or 3, where:

* A value of `1` indicates that in-band events only extend the MPD validity duration.
* A value of `3` indicates that in-band events also contain the updated MPD snapshot when updates occur.

Services <span class=modal-keyword>shall</span> update `MPD@publishTime` to a unique value after every MPD update.

Note: `MPD@publishTime` is merely a version label. The value is not used in timing calculations.

<div class="example">
Using in-band signaling and `MPD@minimumUpdatePeriod=0`, each Media Segment increases the validity period of the MPD by the duration of the Media Segment by default. When a validity event arrives, it carries the validity end timestamp of the MPD, enabling the client to determine when a new MPD refresh is needed.
</div>

Services <span class=modal-keyword>shall</span> emit in-band events as `emsg` boxes to signal the MPD validity duration using the following logic:

* Lack of an in-band MPD validity event in a Media Segment indicates that an MPD that was valid at the start of the Media Segment remains valid up to the end of the Media Segment.
* The presence of an in-band MPD validity event in a Media Segment indicates that the MPD with `MPD@publishTime` equal to the event's `publish_time` field remains valid up to the event start time.

The in-band events used for signaling MPD validity duration <span class=modal-keyword>shall</span> have `scheme_id_uri` and `value` matching the `InbandEventStream` element. Clients <span class=modal-keyword>shall not</span> use in-band events for MPD validity update signaling if these fields on the events do not match the `InbandEventStream` element or if the `InbandEventStream` element is not present in the MPD.

In-band events with `value=3` <span class=modal-keyword>shall</span> provide an updated MPD in the event's `mpd` field as UTF-8 encoded text without a byte order mark.

Clients <span class=modal-keyword>may</span> perform MPD refreshes or process an event-embedded MPD immediately upon reading the event, without waiting for the moment signaled by the event timestamp. Services <span class=modal-keyword>shall</span> ensure that an updated MPD is available and valid starting from the moment a validity event is signaled.

Multiple Media Segments <span class=modal-keyword>may</span> signal the same validity update event (identified by a matching `id` field on the event), enabling the signal to be delivered several segments in advance of the MPD expiration.

In-band MPD validity events <span class=modal-keyword>shall not</span> be signaled in a static MPD but <span class=modal-keyword>may</span> be present in the Media Segments referenced by a static MPD, in which case they <span class=modal-keyword>shall</span> be ignored by clients.

Note: The above may happen when a live service is converted to an on-demand service for catchup/recording purposes.

# MPD Events # {#mpd-events}

In addition to tracking events (e.g. ad starts, quartile tracking), a server may also need to signal additional metadata to the application. There is no need for a generic DASH client to implement this functionality directly — it is enough to provide opaque information that the client passes to an external module. The `Event@schemeIdUri` provides the addressing mechanism, while MPD events allow opaque payloads to be embedded in the MPD.

# DASH Callback Events # {#callback-events}

DASH Callback events, defined in ISO/IEC 23009-1 Amendment 3, are a simple native implementation of time-based impression reporting (e.g. quartiles). A callback event is a promise by the DASH client to issue an HTTP GET request to a provided URL at a given offset from `PeriodStart`. The body of the HTTP response is ignored. Callback events <span class=modal-keyword>may</span> be signaled as either MPD events or inband events.

# Requirements and Recommendations # {#requirements}

Issue: The above clauses migrate the general DASH events model, in-band MPD
validity/update signaling, MPD events, and DASH Callback events from
Dash-Industry-Forum/DASH-IF-IOP branch v5-old-draft, 40-Features.inc.md and
65-AdInsertion.inc.md. Remaining migration work: reconciling event-stream
constraints with Part 5 (ad insertion cue messages, e.g. SCTE-35) and Part 4
(low-latency MPD-update timing), and defining the ownership boundary for
timed-metadata tracks with Part 11.
[GROUNDED_BY=Dash-Industry-Forum/DASH-IF-IOP@v5-old-draft:40-Features.inc.md;65-AdInsertion.inc.md]
# Open Issues and Work Items # {#open-issues}

<table class="data">
  <caption>Part 10 open issues and topics to progress.</caption>
  <thead><tr><th>Topic<th>Status<th>Next action
  <tbody>
    <tr><td>Source migration<td>In progress<td>General events model and in-band MPD validity/update signaling migrated from DASH-IF-IOP v5-old-draft. Timed metadata track ownership boundary with Part 11 still needs to be defined.
    <tr><td>Cross-part alignment<td>Open<td>Align terminology and references with Parts 1, 2, 4, 5, and 12.
    <tr><td>Conformance mapping<td>Open<td>Identify validator/test-asset/reference-player expectations and link them to Part 12.
</table>

# Change History # {#change-history}

<table class="data">
  <caption>Part 10 change history.</caption>
  <thead><tr><th>Version<th>Date<th>Change
  <tbody>
    <tr><td>0.1<td>Initial<td>Created initial Bikeshed/Markdown shell for Part 10.
    <tr><td>0.2<td>Migration<td>Migrated general DASH events model and in-band MPD validity/update signaling from DASH-IF-IOP v5-old-draft.
</table>

