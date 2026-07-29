<!--



  Part 1 clause 5: Architecture and Interfaces.
  Ported from DASH-IF IOP-1 v5.0.0 (2022-06) clause 5.
  Provenance: dashif-iop-v5-part1 (published PDF) architecture text ~offset 17231-29500.
  Figures 1 (distribution architecture) and 2 (reference client) redrawn as Mermaid
  per the DASH-IF authoring diagram convention.
-->

# Architecture and Interfaces # {#architecture}

## DASH-IF Baseline Architecture ## {#baseline-architecture}

A baseline architecture for DASH content distribution is provided in the figure
below. Content is provided in any format and then encoded and prepared following
the DASH Segment formats defined in ISO/IEC 23009-1 [[!MPEGDASH]], in particular
based on ISO BMFF (ISO/IEC 14496-12 [[!ISOBMFF]]) and CMAF (ISO/IEC 23000-19
[[!MPEGCMAF]]).

<figure class="diagram" style="max-width:100%;overflow-x:auto;">
<pre class=mermaid>
%%{init: {'theme':'neutral','themeVariables':{'fontSize':'18px','fontFamily':'system-ui, Segoe UI, Arial, sans-serif','lineColor':'#333'},'flowchart':{'curve':'linear','nodeSpacing':55,'rankSpacing':80,'padding':14,'htmlLabels':false,'useMaxWidth':true}}}%%
flowchart LR
    CP[Contribution Link] -->|Contribution| ENC[ABR Encoder]
    ENC -->|ISO BMFF / CMAF| PKG["ISO BMFF / CMAF Packager (Encryption)"]
    PKG -->|Ingest 1-IF| MPG["MPD Generator and DASH Packager (Encryption)"]
    MPG -->|Ingest 2-IF| CDN[("CDN: Segment + MPD Server")]
    CDN -->|"DASH-IOP-IF (MPD + Segments)"| AC[DASH Access Client]
    AC -->|Playback-API| RPP["Reference Playback Platform: Media Playback + Content Decryption"]
    APP[Application] -->|Application-IF| AC
    APP -->|Client-API| AC
    SC[Service Configuration] -->|Service-Config-API| MPG
    DRM[DRM System] -->|CPIX-IF| PKG
    DRM -->|CPIX| MPG
    classDef box fill:#eef3f8,stroke:#33475b,stroke-width:1.4px,color:#1a2733;
    class CP,ENC,PKG,MPG,CDN,AC,RPP,APP,SC,DRM box;
</pre>
<figcaption>DASH-based distribution architecture.</figcaption>
</figure>

The following major components are identified:

: <dfn export>ABR Encoder</dfn>
:: Adaptive Bitrate Encoder providing multiple equivalent versions of the same
    content in different qualities.
: <dfn export>ISO BMFF/CMAF Packager</dfn>
:: Encapsulation and packaging that creates segmented media content that can be
    distributed through DASH and played back on a reference platform through
    well-defined APIs. This specification assumes an ISO BMFF/CMAF Packager.
: <dfn export>DASH Packager and MPD Generator</dfn>
:: An operation that adds DASH formats and MPD signalling to create a DASH Media
    Presentation.
: <dfn export>CDN</dfn>
:: A scalable distribution network supporting the delivery and caching of DASH
    resources.
: <dfn export>DASH Access Client</dfn>
:: A client that uses the MPD and the referenced resources to create a streaming
    experience for a user by using a reference playback platform.
: <dfn export>Application</dfn>
:: An application that controls the DASH access client through a set of
    well-defined APIs.

## Interfaces ## {#interfaces}

The architecture defines a set of reference points (interfaces), explained below.

<table class="data">
  <caption>Reference points of the DASH-based distribution architecture.</caption>
  <thead>
    <tr><th>Reference Point<th>Explanation
    <tbody>
      <tr>
        <td>Ingest 1-IF
        <td>The first interface of the DASH-IF Live Media Ingest Specification: CMAF ingest, based on fragmented MPEG-4 (CMAF). It uses the HTTP POST method to transmit media objects from the ingest source to the receiving entity, and supports carriage of timed metadata and timed text, with guidelines for redundancy and failover.
      <tr>
        <td>Ingest 2-IF
        <td>The second interface of the DASH-IF Live Media Ingest Specification, based on MPEG DASH and HLS. It uses the HTTP POST method to transmit media objects, and supports timed metadata and timed text with redundancy and failover guidelines.
      <tr>
        <td>CPIX-IF
        <td>The Content Protection Information Exchange (CPIX) interface, defined in a separate specification. A CPIX document carries keys and DRM information used to encrypt and protect content, and <span class=modal-keyword>may</span> itself be encrypted, signed, and authenticated for confidentiality, source, and integrity.
      <tr>
        <td>DASH-IOP-IF
        <td>The main interface defined in the DASH-IF IOP guidelines, providing interoperability between a content provider offering DASH-based services on a CDN and a DASH client.
      <tr>
        <td>Application-IF
        <td>An interface, typically in an application, that provides the entry point to the DASH service by supplying a URL to an MPD.
      <tr>
        <td>Playback-IF
        <td>A reference interface between a DASH access client and a playback and decryption platform, modelled on the HTML5 video element and Media Source Extensions, with the restrictions of the CTA WAVE device playback API.
      <tr>
        <td>Service-Config-API
        <td>A network-side API that allows an application provider to configure parameters of a DASH-based streaming service, used to statically and dynamically create MPDs and manage segment data generation and distribution.
      <tr>
        <td>Client-API
        <td>An API between the application and the DASH client (both access client and playback platform) to configure, control, and monitor the service.
  </table>

## DASH Reference Client ## {#reference-client}

To develop the interoperability guidelines, a reference client for playback is
assumed, as shown below. The reference client is not a mandatory implementation
but serves as a reference for developing the IOP guidelines and for service
offerings. The following basic workflow is assumed:

- The DASH reference client downloads, processes, and presents a DASH Media
    Presentation under the instruction of an application.
- The application can additionally configure the media presentation, receive
    event notifications, and query the internal status of the DASH player and
    access client.
- Several functions in the DASH access client are typically necessary to process
    a DASH Media Presentation, including MPD processing, Adaptation Set selection,
    and download functions.
- A media playback platform and content decryption module are used for secure
    decoding and presentation of the streamed media.

<figure class="diagram" style="max-width:100%;overflow-x:auto;">
<pre class=mermaid>
%%{init: {'theme':'neutral','themeVariables':{'fontSize':'18px','fontFamily':'system-ui, Segoe UI, Arial, sans-serif','lineColor':'#333'},'flowchart':{'curve':'linear','nodeSpacing':50,'rankSpacing':75,'padding':14,'htmlLabels':false,'useMaxWidth':true}}}%%
flowchart TB
    APP[Application] -->|"Client-API (config / notifications / status)"| MGMT
    subgraph Player [DASH Player]
      direction TB
      subgraph AC [DASH Access Client]
        direction TB
        MGMT[Management] --- MPD[MPD Processing]
        MPD --- ASS[Adaptation Set Selection]
        ASS --- ABR[ABR Controller and Dynamic Switching]
        ABR --- TP[Download / Throughput Estimation]
        MGMT --- EV[Event Processing]
        MGMT --- MET[Metrics]
        MGMT --- MPM[Media Playback Management and Protection Controller]
      end
      MPM -->|Playback-API| MPP["Media Playback Platform and Content Decryption Module"]
    end
    SRV[("Segment Server / MPD Server")] -->|"DASH-Interface (request scheduling)"| TP
    classDef box fill:#eef3f8,stroke:#33475b,stroke-width:1.4px,color:#1a2733;
    class APP,MGMT,MPD,ASS,ABR,TP,EV,MET,MPM,MPP,SRV box;
</pre>
<figcaption>DASH reference client.</figcaption>
</figure>

The following functions are part of the reference client:

- <b>Application</b>: uses the DASH/media player to play back a DASH Media
    Presentation, typically providing the MPD or its URL to the DASH client.
- <b>DASH Player</b>: a complete player, including media playback platform and
    content decryption module.
- <b>DASH Access Client</b>: accesses and downloads media from the network and uses
    the media playback platform and content decryption module for decoding and
    playback.
- <b>Management</b>: controls internal processes and communication with the
    application.
- <b>MPD Processing</b>: parses and processes the MPD and extracts relevant
    information.
- <b>Adaptation Set Selection</b>: selects Adaptation Sets based on user,
    environment, and capability information.
- <b>Dynamic Switching and Request Scheduling</b>: runs adaptive-bitrate logic and
    triggers dynamic switching across Representations.
- <b>Throughput Estimation</b>: estimates throughput from a specific
    network/application server.
- <b>Metrics Collection</b>: collects streaming metrics and offers them to the
    application for processing and potential reporting to network entities.
- <b>Media Playback Management</b>: moves downloaded information into the media
    playback platform and handles content protection and DRM information.
- <b>Media Playback Platform</b>: plays back CMAF-based media using well-defined
    playback instructions.
- <b>Event Processing</b>: processes DASH events and provides information to the
    application.

Detailed APIs and methods to communicate with a DASH reference client are
implemented in the DASH-IF reference client (see [[#part-descriptions]] and
Part 12). DASH players typically rely on CMAF-capable playback platforms and
decryption modules rather than a specific implementation; more detail on a
CMAF-capable playback platform is given in Part 2.

Content security is accomplished in a device by two functions:

- <b>Key management</b> by a digital rights management (DRM) system that
    authenticates a device and authorizes decryption and playback under specific
    conditions (e.g. output protection, rental period, hardware root of trust);
    see Part 6.
- <b>Decryption</b> of an encrypted track using a specific decryption scheme; see
    Part 6.

Received DASH events are processed for client consumption; see Part 10.

## DASH-IF IOP Parts ## {#part-descriptions}

The following summarises each part of DASH-IF IOP v5. Each part is published
as a separate document; links point to the current published version.

- <b>[Part 1 — Overview, Architecture and Interfaces](https://dashif.org/Guidelines/iop-v5/part01-overview.html)</b>
    (this document): an overview of the features in the DASH-IF Interoperability
    Guidelines, with a reference architecture, interfaces, and functional blocks.
- <b>[Part 2 — Core principles and CMAF mapping](https://dashif.org/Guidelines/iop-v5/part02-core-cmaf.html)</b>:
    the core principles of DASH including the data and timing model, and the
    mapping of CMAF data structures to DASH Media Presentations.
- <b>[Part 3 — On-demand services](https://dashif.org/Guidelines/iop-v5/part03-on-demand.html)</b>:
    requirements and recommendations for using DASH for on-demand services.
- <b>[Part 4 — Live and low-latency services](https://dashif.org/Guidelines/iop-v5/part04-live-low-latency.html)</b>:
    live service offerings, including low-latency services.
- <b>[Part 5 — Ad insertion and content replacement](https://dashif.org/Guidelines/iop-v5/part05-ad-insertion.html)</b>:
    guidelines for advertisement insertion in a CMAF-based, DASH-delivered
    workflow, covering conditioning, packaging, and signalling for both SSAI
    and SGAI.
- <b>[Part 6 — Content protection and security](https://dashif.org/Guidelines/iop-v5/part06-content-protection.html)</b>:
    guidelines for encrypted content in CMAF protected by MPEG CENC, key
    rotation, Enhanced Clear Key Content Protection (ECCP), and the DASH-IF
    content-protection XML schema.
- <b>[Part 7 — Video](https://dashif.org/Guidelines/iop-v5/part07-video.html)</b>:
    the CMAF media profiles and DASH signalling for video tracks, with reference
    to the [DASH-IF Codec Registry](https://dashif.org/codecs/).
- <b>[Part 8 — Audio](https://dashif.org/Guidelines/iop-v5/part08-audio.html)</b>:
    audio interoperability points, coding profiles, ISO BMFF packaging, and MPD
    parameters, with reference to the [DASH-IF Codec Registry](https://dashif.org/codecs/).
- <b>[Part 9 — Text (Subtitle)](https://dashif.org/Guidelines/iop-v5/part09-text.html)</b>:
    subtitle/caption interoperability points and signalling.
- <b>[Part 10 — Events](https://dashif.org/Guidelines/iop-v5/part10-events.html)</b>:
    event signalling and processing, including MPD events, inband events, and
    timed metadata tracks.
- <b>[Part 11 — Additional functionalities](https://dashif.org/Guidelines/iop-v5/part11-additional-technologies.html)</b>:
    further interoperability features.
- <b>[Part 12 — Conformance and reference tools](https://dashif.org/Guidelines/iop-v5/part12-conformance-reference-tools.html)</b>:
    the conformance validator, reference player ([dash.js](https://github.com/Dash-Industry-Forum/dash.js)),
    live source simulator ([livesim2](https://github.com/Dash-Industry-Forum/livesim2)),
    and test assets.

Note: Issues for any part <span class=modal-keyword>should</span> be filed at the single IOPv5 issue tracker:
[https://github.com/Dash-Industry-Forum/IOPv5/issues](https://github.com/Dash-Industry-Forum/IOPv5/issues).
Use the label `Part N` or the title prefix `[Part N]:` to identify the relevant
part (e.g. `[Part 2]: Clarify @timescale requirement`).

# DASH-IF Registries # {#registries}

## Overview ## {#registries-overview}

DASH-IF maintains two publicly accessible registries that serve as authoritative
references for identifiers and codecs used in DASH-IF compliant services. These
registries are living documents, continuously updated as new values are registered
and existing entries are refined.

- <b>[DASH-IF Identifier Registry](https://dashif.org/identifiers/introduction/)</b>
    [[DASHIF-IDENTIFIERS]] — the authoritative registry of `@schemeIdUri` values,
    profile URIs, and other string identifiers used in DASH MPDs and media.
- <b>[DASH-IF Codec Registry](https://dashif.org/codecs/introduction/)</b>
    [[DASHIF-CODECS]] — the authoritative registry of `@codecs` strings and CMAF
    profiles for video and audio codecs supported in DASH-IF compliant services.

Services and clients <span class=modal-keyword>shall</span> use only identifiers and codec strings that are
registered in the respective DASH-IF registry or explicitly defined in the
applicable IOP v5 part.

## DASH-IF Identifier Registry ## {#identifier-registry}

### General ### {#identifier-registry-general}

The DASH-IF Identifier Registry at
[https://dashif.org/identifiers/introduction/](https://dashif.org/identifiers/introduction/)
provides the canonical `@schemeIdUri` values and other string identifiers used
across DASH MPD elements. The registry covers:

- <code><b>AudioChannelConfiguration</b>@schemeIdUri</code> — schemes for signalling audio
    channel layout (e.g. MPEG channel configuration, Dolby, DTS).
- <code><b>Role</b>@schemeIdUri</code> — schemes for Adaptation Set role descriptors
    (e.g. `urn:mpeg:dash:role:2011` for main, alternate, subtitle, etc.).
- <code><b>Accessibility</b>@schemeIdUri</code> — schemes for accessibility descriptors
    (e.g. closed captions, audio description, sign language).
- <code><b>EventStream</b>@schemeIdUri</code> — schemes for MPD and inband event streams
    (e.g. `urn:mpeg:dash:event:2012` for MPD validity expiry).
- <code><b>ContentProtection</b>@schemeIdUri</code> — DRM system identifiers
    (e.g. Common Encryption, Widevine, PlayReady, FairPlay).
- <b>Profile URIs</b> — URIs identifying DASH profiles and interoperability points
    (e.g. `http://dashif.org/guidelines/dash-if-ondemand`).
- <b>Supplemental and Essential Property descriptors</b> — `@schemeIdUri` values
    for MPD property descriptors.

The registry source data is maintained at
[https://github.com/Dash-Industry-Forum/Identifiers](https://github.com/Dash-Industry-Forum/Identifiers).

### Identifier Types in ISO/IEC 23009-1 ### {#identifier-types-23009}

ISO/IEC 23009-1 [[!MPEGDASH]] defines several mechanisms for extensible
identification in DASH MPDs. The following identifier types are used throughout
the IOP v5 document set:

<table class="data">
  <caption>Key identifier types in ISO/IEC 23009-1 and their use in IOP v5.</caption>
  <thead>
    <tr><th>Identifier type<th>MPD attribute/element<th>Purpose<th>IOP v5 part(s)
  <tbody>
    <tr>
      <td>`@schemeIdUri` + `@value`
      <td><b>Role</b>, <b>Accessibility</b>, <b>AudioChannelConfiguration</b>, <b>EventStream</b>, <b>ContentProtection</b>, <b>SupplementalProperty</b>, <b>EssentialProperty</b>
      <td>Extensible scheme identification for descriptors and event streams
      <td>Parts 2, 6, 7, 8, 9, 10
    <tr>
      <td>`@codecs`
      <td><b>Representation</b>, <b>AdaptationSet</b>
      <td>Codec and profile identification string (RFC 6381 format)
      <td>Parts 7, 8, 9
    <tr>
      <td>`@mimeType`
      <td><b>Representation</b>, <b>AdaptationSet</b>
      <td>MIME type of the media container
      <td>Parts 7, 8, 9, 10
    <tr>
      <td>Profile URI
      <td><code><b>MPD</b>@profiles</code>, <code><b>AdaptationSet</b>@profiles</code>, <code><b>Representation</b>@profiles</code>
      <td>URI identifying a DASH profile or interoperability point
      <td>Parts 2, 3, 4
    <tr>
      <td>`@id`
      <td><b>Period</b>, <b>AdaptationSet</b>, <b>Representation</b>, <b>Event</b>
      <td>Local identifier within the MPD for cross-referencing
      <td>Parts 2, 4, 5
</table>

### Using Identifiers in IOP v5 ### {#identifier-usage}

When an IOP v5 part requires a specific `@schemeIdUri` value, it <span class=modal-keyword>shall</span> reference
the DASH-IF Identifier Registry as the authoritative source. Services <span class=modal-keyword>shall</span> use
only registered `@schemeIdUri` values for the applicable scheme. Clients <span class=modal-keyword>shall</span>
ignore descriptors with unrecognised `@schemeIdUri` values unless the descriptor
is marked as `EssentialProperty`.

Note: The DASH-IF Identifier Registry is a living document. Services and clients
<span class=modal-keyword>should</span> consult the current version of the registry rather than relying solely
on the static tables in individual IOP v5 parts.

## DASH-IF Codec Registry ## {#codec-registry}

### General ### {#codec-registry-general}

The DASH-IF Codec Registry at
[https://dashif.org/codecs/introduction/](https://dashif.org/codecs/introduction/)
provides the canonical `@codecs` strings and CMAF profiles for video and audio
codecs supported in DASH-IF compliant services. The registry source data is
maintained at
[https://github.com/Dash-Industry-Forum/Codecs](https://github.com/Dash-Industry-Forum/Codecs).

Detailed codec requirements are defined in:

- <b>[Part 7 — Video](https://dashif.org/Guidelines/iop-v5/part07-video.html)</b>:
    H.264/AVC, H.265/HEVC, and other video codecs.
- <b>[Part 8 — Audio](https://dashif.org/Guidelines/iop-v5/part08-audio.html)</b>:
    HE-AACv2, E-AC-3, AC-4, MPEG-H 3D Audio, and other audio codecs.
- <b>[Part 9 — Text](https://dashif.org/Guidelines/iop-v5/part09-text.html)</b>:
    IMSC1, WebVTT, and other text/subtitle codecs.

## Registering New Identifiers and Codecs ## {#registry-registration}

### General ### {#registry-registration-general}

DASH-IF welcomes proposals for new identifiers and codec registrations from the
community. The registration process ensures that new values are reviewed for
technical correctness, uniqueness, and alignment with the DASH-IF IOP v5
framework.

### Registering a New Identifier ### {#register-identifier}

To propose a new `@schemeIdUri` value or other identifier for the DASH-IF
Identifier Registry:

1. <b>Submit a registration request</b> using the DASH-IF Identifier Registration
    Form at
    [https://docs.google.com/forms/d/e/1FAIpQLSfoMH4BL-1VwEpnVrYSnlvzwdO_7VAFeP1OfifxKW7nXVeWjg/viewform](https://docs.google.com/forms/d/e/1FAIpQLSfoMH4BL-1VwEpnVrYSnlvzwdO_7VAFeP1OfifxKW7nXVeWjg/viewform).
2. <b>Alternatively</b>, file an issue at the Identifiers repository:
    [https://github.com/Dash-Industry-Forum/Identifiers/issues](https://github.com/Dash-Industry-Forum/Identifiers/issues).
3. The DASH-IF Technical Working Group reviews the proposal and, if approved,
    adds the identifier to the registry.

Note: The Google Forms submission workflow is the current recommended entry
point. A more streamlined GitHub-based workflow is planned for a future update.

### Registering a New Codec ### {#register-codec}

To propose a new codec for the DASH-IF Codec Registry:

1. File an issue or pull request at the Codecs repository:
    [https://github.com/Dash-Industry-Forum/Codecs](https://github.com/Dash-Industry-Forum/Codecs).
2. The registration requires: a defined `@codecs` string, a CMAF media profile
    or equivalent container format specification, demonstrated interoperability
    with at least one DASH client and one DASH packager, and alignment with the
    DASH-IF IOP v5 framework.

# Change History # {#change-history}

<table class="data">
  <caption>Part 1 change history.</caption>
  <thead>
    <tr><th>Version<th>Date<th>Change
  <tbody>
    <tr>
      <td>0.1
      <td>Initial
      <td>Migrated from DASH-IF IOP-1 v5.0.0 (2022-06); references modernised (HTTP RFC 9110/9111/9112, TLS 1.3 RFC 8446); issue-tracker URL updated to the IOPv5 repository.
    <tr>
      <td>0.2
      <td>Initial
      <td>Ported clause 5 (Architecture and Interfaces: baseline architecture, interfaces, reference client, part descriptions); added editors, contributors, and shared IPR boilerplate.
    <tr>
      <td>0.3
      <td>Enhancement
      <td>Added Document Status section explaining Living Document status, Working Draft versioning, publication workflow (Working Draft → WG Review → Community Review → Approved), and issue reporting guidance (single IOPv5 tracker with Part N labels). Added hyperlinks to all part descriptions. Added Codec Registry links for Parts 7 and 8.
    <tr>
      <td>0.4
      <td>Enhancement
      <td>Added DASH-IF Registries section covering the Identifier Registry (schemeIdUri values, profile URIs, ISO/IEC 23009-1 identifier types) and Codec Registry, with registration workflow (Google Forms, GitHub issues). Added DASHIF-IDENTIFIERS and DASHIF-CODECS biblio entries. Updated all 12 .bs files: replaced Repository: with !Repository:, added !Issue Tracking: and !Document Status: custom metadata entries.
</table>

<h2 class="appendix no-num" id="document-status">Annex A: Document Status</h2>

<h3 id="living-document">Living Document</h3>

This document is published as a <b>Living Document</b> (LD). A Living Document is
continuously updated as new content is added, issues are resolved, and the
technical community provides feedback. It does not represent a final, approved
specification.

The current status of each part is indicated by its version number in the Change
History table:

- <b>Working Draft (0.x)</b>: Content is being drafted and reviewed by the DASH-IF
    Technical Working Group. The document is open for community feedback but has
    not yet been formally approved.
- <b>WG Review (0.8.x-wgr)</b>: The Working Group has completed its internal review
    and the document is open for broader community review.
- <b>Community Review (0.9.x-pr)</b>: The document is open for public comment before
    final approval (public review).
- <b>Approved (1.x)</b>: The document has been formally approved by DASH-IF and
    represents a stable, normative specification. Only approved versions use
    version numbers 1.0 and above.


<h3 id="document-workflow">Document Workflow</h3>

The DASH-IF IOP v5 document set follows this publication workflow:

1. <b>Working Draft</b>: Editors draft content in the `main` development branch.
    Issues and pull requests are tracked at
    [https://github.com/Dash-Industry-Forum/IOPv5/issues](https://github.com/Dash-Industry-Forum/IOPv5/issues).
    Use the label or title prefix `[Part N]` (e.g. `[Part 2]`) to associate an
    issue with a specific part.
2. <b>WG Review</b>: The Working Group reviews the draft and resolves open issues.
    A release candidate is tagged on the `main` branch.
3. <b>Community Review</b>: The release candidate is published for public comment.
    A `stable` branch is created to maintain the approved version independently
    of ongoing development.
4. <b>Approved</b>: After community review, the document is formally approved and
    published as a stable release. The `stable` branch is updated; the `main`
    branch continues development of the next version.

<h3 id="stable-dev-branches">Stable and Development Versions</h3>

DASH-IF IOP v5 uses a <b>two-branch model</b> to allow simultaneous maintenance of
a stable approved version and ongoing development of the next version:

- <b>`main` branch</b> — the development branch. All Working Draft content is
    authored here. The preview publication at
    [https://dashif.org/IOPv5/previews/](https://dashif.org/IOPv5/previews/)
    is built from `main`. Version numbers are `0.x` (Working Draft).
- <b>`stable` branch</b> — the approved/stable branch. When a version is formally
    approved, it is tagged (e.g. `v1.0`) and the `stable` branch is updated to
    that tag. The official publication at
    [https://dashif.org/Guidelines/iop-v5/](https://dashif.org/Guidelines/iop-v5/)
    is built from `stable`. Version numbers are `1.x` or higher.

<b>Typical workflow for a new version:</b>

1. Development continues on `main` (Working Draft, version `0.x`).
2. When ready for WG Review, a release candidate is tagged on `main`
    (e.g. `v1.0-rc1`).
3. After WG and Community Review, the approved version is tagged (e.g. `v1.0`)
    and the `stable` branch is fast-forwarded to that tag.
4. The official publication is updated from `stable`.
5. Development of the next version (`0.x` → `2.0-wip`) continues on `main`.

<b>Working on a new major version while maintaining a stable one:</b>

If a new major version (e.g. v2) needs to be developed while v1 remains stable:

1. Create a `v2-dev` branch from `main` for the new major version.
2. The `stable` branch continues to track the approved v1 content.
3. When v2 is approved, `stable` is updated to the v2 tag.

This model ensures that the official publication always reflects the latest
approved content, while editors can freely develop the next version without
affecting the stable publication.

<h3 id="issue-reporting">Issue Reporting</h3>

All issues, bugs, and feature requests for DASH-IF IOP v5 <span class=modal-keyword>shall</span> be submitted
through the single DASH-IF IOPv5 issue tracker at
[https://github.com/Dash-Industry-Forum/IOPv5/issues](https://github.com/Dash-Industry-Forum/IOPv5/issues).

To associate an issue with a specific part, use one of the following conventions:

- <b>Label</b>: Apply the GitHub label `Part 1`, `Part 2`, etc. to the issue.
- <b>Title prefix</b>: Begin the issue title with `[Part N]:`, for example
    `[Part 2]: Clarify @timescale requirement for SegmentTemplate`.

<h3 id="contributing">Contributing and Reviewing</h3>

<h4 id="contributing-general">General</h4>

DASH-IF IOP v5 is developed openly on GitHub. Contributions and reviews are
welcome at all stages of the publication workflow. The primary mechanisms are
GitHub issues (for feedback and discussion) and pull requests (for editorial
contributions).

<h4 id="contributing-wd">During the Working Draft Phase</h4>

While a part is at Working Draft status:

- <b>File an issue</b> at
    [https://github.com/Dash-Industry-Forum/IOPv5/issues](https://github.com/Dash-Industry-Forum/IOPv5/issues)
    to report errors, raise technical questions, or propose new content. Use the
    title prefix `[Part N]:` to identify the relevant part.
- <b>Assign the issue</b> to the appropriate per-part GitHub Project under the
    [Dash-Industry-Forum organization](https://github.com/orgs/Dash-Industry-Forum/projects)
    (e.g. `Part 2: Core Principles and CMAF Mapping`). Each part has a dedicated
    project for tracking its open issues and work items.
- <b>Submit a pull request</b> against the `main` branch to propose editorial
    corrections, add missing content, or improve existing text. Pull requests
    <span class=modal-keyword>should</span> reference the issue they address.
- <b>Discuss</b> open issues in the GitHub issue tracker. The DASH-IF Technical
    Working Group reviews issues and pull requests on a regular basis.

<h4 id="contributing-wg-review">During WG Review</h4>

When a part reaches WG Review status (release candidate tagged on `main`):

- <b>WG members</b> review the release candidate and file issues or pull requests
    for any remaining technical or editorial concerns.
- <b>Substantive changes</b> require a new release candidate; editorial corrections
    <span class=modal-keyword>may</span> be applied directly.
- The WG chair coordinates the review schedule and announces the review period
    via the DASH-IF mailing list and GitHub.

<h4 id="contributing-community-review">During Community Review</h4>

When a part reaches Community Review status:

- <b>Anyone</b> <span class=modal-keyword>may</span> submit feedback by filing a GitHub issue at
    [https://github.com/Dash-Industry-Forum/IOPv5/issues](https://github.com/Dash-Industry-Forum/IOPv5/issues).
    Use the label `Community Review` or the title prefix `[CR]:` to identify
    community review comments.
- <b>Pull requests</b> for editorial corrections are also welcome during this phase.
- The review period is announced on the DASH-IF website and mailing list. At the
    end of the review period, the WG resolves all open issues and, if no
    substantive changes are required, approves the document.

<h4 id="contributing-pr">How to Submit a Pull Request</h4>

1. <b>Fork</b> the IOPv5 repository at
    [https://github.com/Dash-Industry-Forum/IOPv5](https://github.com/Dash-Industry-Forum/IOPv5).
2. <b>Create a branch</b> from `main` with a descriptive name (e.g.
    `fix-part2-timescale-clarification`).
3. <b>Make your changes</b> to the relevant `.inc.md` or `.bs` files in the
    `rag-authoring-starter/specs/` directory.
4. <b>Build locally</b> (optional but recommended) using
    `python tools/publication/build_all.py --out ../dist` to verify the changes
    compile without errors.
5. <b>Submit a pull request</b> against the `main` branch of the IOPv5 repository.
    Reference the issue(s) the PR addresses in the PR description.
6. <b>Assign the related issue(s)</b> to the appropriate per-part GitHub Project
    under the [Dash-Industry-Forum organization](https://github.com/orgs/Dash-Industry-Forum/projects).
7. The DASH-IF Technical Working Group reviews and merges approved pull requests.
