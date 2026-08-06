<!--
  Part 10: Events.
  Reconciled 2026-07-28:
  - Added cross-references to Part 4 (MPD update timing, inband events)
  - Added cross-references to Part 5 (SCTE-35 cue messages, ad insertion events)
  - Added timed metadata tracks section
  - Updated open issues
  - Fixed cross-document [[#...]] references (not valid across documents)
  Source grounding:
  - Dash-Industry-Forum/DASH-IF-IOP branch v5-old-draft, 40-Features.inc.md
  - Dash-Industry-Forum/DASH-IF-IOP branch v5-old-draft, 65-AdInsertion.inc.md
-->

# Scope # {#scope}

This document specifies DASH-IF IOP v5 Part 10: <b>Events</b>. Event signalling
and processing, including MPD events, inband events, timed metadata tracks, and
DASH Callback events.

This part defines the general event model and the requirements for event
signalling that are common across service types. Service-type-specific event
requirements are defined in:

- <b>Part 4</b> (Live and Low-Latency Services) — MPD validity expiry events and
    inband MPD update signalling for live services.
- <b>Part 5</b> (Ad Insertion and Content Replacement) — SCTE-35 cue message
    events, DASH Callback events for ad tracking, and ad-insertion event
    stream constraints.

Note: ETSI TS 103 285 [[DVBDASH]] (the "DVB-DASH" profile) defines its own
constraints on event signalling, including mandatory support for the
`urn:mpeg:dash:event:2012` MPD validity expiry event and DVB-specific
application-signalling event streams (e.g. programme metadata and SCTE-35 cue
messages carried per DVB conventions). Alignment notes with DVB-DASH are
provided in the relevant clauses below.

# References # {#doc-references}

The following referenced documents are necessary for the application of this
part:

- ISO/IEC 23009-1 [[!MPEGDASH]].
- ISO/IEC 23000-19 [[!MPEGCMAF]].
- DASH-IF IOP v5 Part 2, *Core Principles and CMAF Mapping*.
- DASH-IF IOP v5 Part 4, *Live and Low-Latency Services*.
- DASH-IF IOP v5 Part 5, *Ad Insertion and Content Replacement*.
- DASH-IF IOP v5 Part 12, *Conformance and Reference Tools*.

# Terms and Definitions # {#terms}

Terms and definitions are inherited from ISO/IEC 23009-1, ISO/IEC 23000-19, and
Part 2 unless defined in this part.

: <dfn export>MPD event</dfn>
:: An event carried in the MPD as an <b>Event</b> element within an <b>EventStream</b>
    element at Period level.

: <dfn export>inband event</dfn>
:: An event carried in a Media Segment as an ISO BMFF `emsg` box.

: <dfn export>timed metadata track</dfn>
:: A CMAF track carrying timed metadata samples, delivered as a DASH
    Representation with `@mimeType="application/mp4"`.

# DASH Events Overview # {#events-overview}

DASH events are messages having type, timing and optional payload. They can
appear either in the MPD (as a Period-level <b>EventStream</b> element) or inband,
as ISO BMFF boxes of type `emsg`. The `emsg` boxes <span class=modal-keyword>shall</span> be placed at the very
beginning of the Segment, i.e. prior to any media data, so that a DASH client
needs a minimal amount of parsing to detect them.

DASH defines events that are processed directly by a DASH client:

- <b>MPD Validity Expiration</b> — signals that the current MPD snapshot is no
    longer valid and a new MPD must be fetched. See [[#inband]] and Part 4
    (Section "MPD- and Segment-based Live Service Offering").
- <b>MPD Patch</b> — provides an XML patch that can be applied to the client's
    in-memory representation of the MPD.
- <b>MPD Update</b> — provides a complete new MPD snapshot.

User-defined events are also possible. The DASH client does not process these
directly — they are passed to an application, or discarded if there is no
application willing or registered to process these events. A possible client API
would allow an application to register callbacks for specific event types,
triggered when the DASH client parses the `emsg` box in a Segment or the
<b>Event</b> element in the MPD. User-defined events can, for example, be used to
signal cue messages such as SCTE-35 in an ad-insertion context (see Part 5,
Section "IF-3 Opportunity Metadata and SCTE-35 MPD Events").

If several `emsg` boxes are present in a Segment and one of them is the MPD
Validity Expiration event, the `emsg` carrying it <span class=modal-keyword>shall</span> always appear first.

# Update Signaling via In-Band Events # {#inband}

Services <span class=modal-keyword>may</span> signal the MPD validity duration by embedding in-band messages
into Representations instead of specifying a fixed validity duration in the MPD.
This allows services to trigger MPD refreshes at exactly the desired time and to
avoid needless MPD refreshes.

This clause only applies to services and clients that use in-band MPD validity
signaling. For the complete requirements on MPD updates and snapshot validity in
live services, see Part 4 (Section "Live Service Offering including MPD Updates").

Services <span class=modal-keyword>shall</span> define `MPD@minimumUpdatePeriod=0` and add an in-band event
stream to every audio Representation or, if no audio Representations are
present, to every video Representation. The in-band event stream <span class=modal-keyword>may</span> also be
added to other Representations. The in-band event stream <span class=modal-keyword>shall</span> be identical in
every Representation where it is present.

The in-band event stream <span class=modal-keyword>shall</span> be signaled on the adaptation set level by an
<b>InbandEventStream</b> element with `@schemeIdUri="urn:mpeg:dash:event:2012"` and
a `@value` of 1 or 3, where:

* A value of `1` indicates that in-band events only extend the MPD validity
    duration.
* A value of `3` indicates that in-band events also contain the updated MPD
    snapshot when updates occur.

Services <span class=modal-keyword>shall</span> update <code><b>MPD</b>@publishTime</code> to a unique value after every MPD
update.

Note: <code><b>MPD</b>@publishTime</code> is merely a version label. The value is not used in
timing calculations.

<div class="example">
Using in-band signaling and `MPD@minimumUpdatePeriod=0`, each Media Segment
increases the validity period of the MPD by the duration of the Media Segment
by default. When a validity event arrives, it carries the validity end timestamp
of the MPD, enabling the client to determine when a new MPD refresh is needed.
</div>

Services <span class=modal-keyword>shall</span> emit in-band events as `emsg` boxes to signal the MPD validity
duration using the following logic:

* Lack of an in-band MPD validity event in a Media Segment indicates that an
    MPD that was valid at the start of the Media Segment remains valid up to the
    end of the Media Segment.
* The presence of an in-band MPD validity event in a Media Segment indicates
    that the MPD with <code><b>MPD</b>@publishTime</code> equal to the event's `publish_time`
    field remains valid up to the event start time.

The in-band events used for signaling MPD validity duration <span class=modal-keyword>shall</span> have
`schemeIdUri` and `value` matching the <b>InbandEventStream</b> element. Clients
<span class=modal-keyword>shall not</span> use in-band events for MPD validity update signaling if these fields
on the events do not match the <b>InbandEventStream</b> element or if the
<b>InbandEventStream</b> element is not present in the MPD.

In-band events with `value=3` <span class=modal-keyword>shall</span> provide an updated MPD in the event's `mpd`
field as UTF-8 encoded text without a byte order mark.

Clients <span class=modal-keyword>may</span> perform MPD refreshes or process an event-embedded MPD immediately
upon reading the event, without waiting for the moment signaled by the event
timestamp. Services <span class=modal-keyword>shall</span> ensure that an updated MPD is available and valid
starting from the moment a validity event is signaled.

Multiple Media Segments <span class=modal-keyword>may</span> signal the same validity update event (identified
by a matching `id` field on the event), enabling the signal to be delivered
several segments in advance of the MPD expiration.

In-band MPD validity events <span class=modal-keyword>shall not</span> be signaled in a static MPD but <span class=modal-keyword>may</span> be
present in the Media Segments referenced by a static MPD, in which case they
<span class=modal-keyword>shall</span> be ignored by clients.

Note: The above may happen when a live service is converted to an on-demand
service for catchup/recording purposes.

Note: DVB-DASH [[DVBDASH]] mandates support for the
`urn:mpeg:dash:event:2012` in-band MPD validity expiry event, consistent with
the signalling defined in this clause, and requires DVB-DASH Live players to
react by fetching an updated MPD. Services should confirm they set
`MPD@minimumUpdatePeriod=0` and populate the <b>InbandEventStream</b> element
exactly as required by this clause to remain compatible with DVB-DASH players.

# MPD Events # {#mpd-events}

In addition to tracking events (e.g. ad starts, quartile tracking), a server
may also need to signal additional metadata to the application. There is no need
for a generic DASH client to implement this functionality directly — it is enough
to provide opaque information that the client passes to an external module. The
<code><b>Event</b>@schemeIdUri</code> provides the addressing mechanism, while MPD events allow
opaque payloads to be embedded in the MPD.

MPD events <span class=modal-keyword>shall</span> be carried in <b>EventStream</b> elements at Period level. Each
<b>EventStream</b> element <span class=modal-keyword>shall</span> carry a `@schemeIdUri` that identifies the event
type. The `@timescale` attribute <span class=modal-keyword>shall</span> be present if <code><b>Event</b>@presentationTime</code> or
<code><b>Event</b>@duration</code> are used.

For ad-insertion cue messages (e.g. SCTE-35), see Part 5 (Section "IF-3
Opportunity Metadata and SCTE-35 MPD Events") for the specific requirements on
MPD event stream signalling.

Note: DVB-DASH [[DVBDASH]] defines its own application-signalling and
programme-metadata event streams (using DVB-specific `@schemeIdUri` values
distinct from the SCTE-35 signalling referenced above) for carrying DVB SI-like
metadata within the MPD. Services offering DVB-DASH-compatible programme
metadata or ad-cue signalling should consult ETSI TS 103 285 clause 9 for the
complete set of required event stream descriptors, in addition to the SCTE-35
requirements in Part 5.

# DASH Callback Events # {#callback-events}

DASH Callback events, defined in ISO/IEC 23009-1, are a simple native
implementation of time-based impression reporting (e.g. quartiles). A callback
event is a promise by the DASH client to issue an HTTP GET request to a provided
URL at a given offset from `PeriodStart`. The body of the HTTP response is
ignored. Callback events <span class=modal-keyword>may</span> be signaled as either MPD events or inband events.

For ad tracking and measurement using DASH Callback events in an ad-insertion
context, see Part 5 (Section "IF-8 Ad Tracking and Measurement").

# Timed Metadata Tracks # {#timed-metadata}

## General ## {#timed-metadata-general}

Timed metadata tracks carry time-aligned metadata samples as CMAF tracks
delivered as DASH Representations. They are used for metadata that must be
precisely synchronized with media playback, such as:

- Subtitle and caption data (see Part 9 for text-specific requirements).
- Dynamic metadata for HDR/WCG content.
- Application-specific metadata (e.g. chapter markers, interactive overlays).
- Accessibility metadata.

## Signalling ## {#timed-metadata-signalling}

A timed metadata Representation <span class=modal-keyword>shall</span> use `@mimeType="application/mp4"` and
<span class=modal-keyword>shall</span> carry a `@codecs` string identifying the metadata format.

The <b>AdaptationSet</b> containing timed metadata Representations <span class=modal-keyword>shall</span> carry a
`@mimeType="application/mp4"` and <span class=modal-keyword>should</span> carry a <b>Role</b> descriptor indicating
the purpose of the metadata (e.g. `urn:mpeg:dash:role:2011` with value
`supplementary`, `caption`, `subtitle`, or `description`).

## Timing ## {#timed-metadata-timing}

Timed metadata tracks <span class=modal-keyword>shall</span> follow the same timing model as media tracks in
the same Period. The `@presentationTimeOffset` and `@timescale` attributes
<span class=modal-keyword>shall</span> be consistent with the Period timing as defined in Part 2.

Timed metadata samples <span class=modal-keyword>shall</span> be aligned with the Period boundaries. Metadata
that spans a Period boundary <span class=modal-keyword>shall</span> be split at the boundary, with each part
carried in the respective Period.

Note: The ownership boundary between timed metadata tracks (Part 10) and
text/subtitle tracks (Part 9) is defined by the `@mimeType`: text tracks use
`application/mp4` with IMSC1 or WebVTT codecs and are governed by Part 9;
other timed metadata tracks are governed by this part.

# Open Issues and Work Items # {#open-issues}

<table class="data">
  <caption>Part 10 open issues and topics to progress.</caption>
  <thead><tr><th>Topic<th>Status<th>Next action
  <tbody>
    <tr><td>Cross-part alignment<td>Partial<td>Cross-references to Part 4 (MPD update timing) and Part 5 (SCTE-35, ad tracking) added as plain-text section references. Verify section names once Part 4 and Part 5 are finalized.
    <tr><td>Timed metadata track ownership<td>Partial<td>Ownership boundary with Part 9 (text tracks) defined by @mimeType. Ownership boundary with Part 11 (additional technologies) still needs to be defined.
    <tr><td>Conformance mapping<td>Open<td>Add Part 12 conformance mapping for Part 10 (event stream signalling, inband events, timed metadata).
    <tr><td>Validator-start tool<td>Open<td>Create `tools/validation/validate_part10_events_mpd.py` covering EventStream signalling, InbandEventStream presence, and timed metadata track constraints.
    <tr><td>MPD Patch events<td>Open<td>Add normative requirements for MPD Patch events (ISO/IEC 23009-1 Amendment 3) once the amendment is finalized.
</table>

# Change History # {#change-history}

<table class="data">
  <caption>Part 10 change history.</caption>
  <thead><tr><th>Version<th>Date<th>Change
  <tbody>
    <tr><td>0.1<td>Initial<td>Created initial Bikeshed/Markdown shell for Part 10.
    <tr><td>0.2<td>Migration<td>Migrated general DASH events model and in-band MPD validity/update signaling from DASH-IF-IOP v5-old-draft.
    <tr><td>0.3<td>Reconciliation<td>Added cross-references to Part 4 (MPD update timing) and Part 5 (SCTE-35, ad tracking). Added timed metadata tracks section. Added terms and definitions. Updated scope to reference Parts 4 and 5 for service-type-specific event requirements.
    <tr><td>0.4<td>Fix<td>Replaced cross-document `[[#section-id]]` anchors with plain-text section references to fix Bikeshed build errors.
</table>