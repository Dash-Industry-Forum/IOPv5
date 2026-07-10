<!--
  Part 11: Additional Functionalities.
  Initial Bikeshed/Markdown shell following the IOPv5 authoring convention.
  Source grounding / migration target: iop-docs-overview / legacy v4.3 feature clauses.
-->

# Scope # {#scope}

This document specifies DASH-IF IOP v5 Part 11: **Additional Functionalities**.
The part collects DASH-IF interoperability features that are not primarily core
DASH/CMAF mapping, service-type, media-profile, content-protection, ad-insertion,
or event-processing topics.

Part 11 has not yet been substantively drafted. The initial work items are:

- migrate **trick mode** material, including v4.3 clause 3.2.9 and live trick-mode
    material, into this part where it is not specific to Part 4;
- migrate **thumbnail tracks** from v4.3;
- define treatment of **specific metadata tracks**, in coordination with Part 10
    because timed metadata <span class=modal-keyword>may</span> also be event-related;
- define a **registration and documentation process** for additional DASH-IF
    technologies and extension points; and
- identify examples and conformance/test-asset expectations for each technology.

Normative content <span class=modal-keyword>shall</span> be migrated from the identified source material and
reconciled with Part 2 core principles, Part 10 events/metadata processing, Part
12 conformance interpretation, and the current editions of MPEG-DASH and CMAF.

# References # {#doc-references}

The following referenced documents are necessary for the application of this
part:

- ISO/IEC 23009-1 [[!MPEGDASH]].
- ISO/IEC 23000-19 [[!MPEGCMAF]].
- DASH-IF IOP v5 Part 2, *Core Principles and CMAF Mapping*.
- DASH-IF IOP v5 Part 12, *Conformance and Reference Tools*.

# Terms and Definitions # {#terms}

Terms and definitions are inherited from ISO/IEC 23009-1, ISO/IEC 23000-19, and
Part 2 unless defined in this part.

# Additional Technologies # {#additional-technologies}

## Trick Mode ## {#trick-mode}

Issue: Migrate trick-mode requirements and recommendations from DASH-IF IOP v4.3,
including clause 3.2.9 and live trick-mode text, into Part 11. Separate generic
trick-mode signalling/client behaviour from live-service-specific constraints
that <span class=modal-keyword>may</span> remain in Part 4. [GROUNDED_BY=dashif-iop-v4-3#168..#170]

## Thumbnail Tracks ## {#thumbnail-tracks}

Issue: Migrate thumbnail-track requirements and recommendations from v4.3. Define
how thumbnail tracks are signalled in the MPD, how they map to CMAF/ISO BMFF
tracks where applicable, and what clients can assume for seeking and preview
experiences. [GROUNDED_BY=dashif-iop-v4-3 / uploaded source material]

## Specific Metadata Tracks ## {#specific-metadata-tracks}

Issue: Define the scope of specific metadata tracks in Part 11 and coordinate
with Part 10. If metadata is time-synchronized and event-like, Part 10 <span class=modal-keyword>may</span> own the
processing model; Part 11 <span class=modal-keyword>may</span> own registration, carriage, and deployment
conventions. [GROUNDED_BY=dashif-iop-v4-3 / iop-docs-overview]

## Registration and Documentation Process ## {#registration-process}

Issue: Define a registration and documentation process for additional DASH-IF
technologies. The process <span class=modal-keyword>should</span> identify: required specification text, signalling
scheme ownership, examples/test assets, validator expectations, reference-player
expectations, and where maintained registries are published.


# Open Issues and Work Items # {#open-issues}

<table class="data">
  <caption>Part 11 open issues and topics to progress.</caption>
  <thead><tr><th>Topic<th>Status<th>Next action
  <tbody>
        <tr><td>Trick mode migration<td>Open<td>Move v4.3 clause 3.2.9 and related live trick-mode material into Part 11 or cross-reference Part 4 where live-specific.
    <tr><td>Thumbnail tracks<td>Open<td>Migrate thumbnail-track text from v4.3 and define signalling, packaging, and client behaviour.
    <tr><td>Specific metadata tracks<td>Open<td>Decide split between Part 10 and Part 11; define carriage and processing expectations.
    <tr><td>Registration process<td>Open<td>Define documentation and registration workflow for additional DASH-IF technologies.
    <tr><td>Examples<td>Open<td>Create examples/test assets for each additional technology.
    <tr><td>Cross-part alignment<td>Open<td>Align terminology and references with Parts 1, 2, 10, and 12.
    <tr><td>Conformance mapping<td>Open<td>Identify validator/test-asset/reference-player expectations and link them to Part 12.
</table>

# Change History # {#change-history}

<table class="data">
  <caption>Part 11 change history.</caption>
  <thead><tr><th>Version<th>Date<th>Change
  <tbody>
    <tr><td>0.1<td>Initial<td>Created initial Bikeshed/Markdown shell for Part 11.
</table>
