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

<figure class="diagram">
<pre class=mermaid>
%%{init: {'theme':'neutral','themeVariables':{'fontSize':'16px','fontFamily':'system-ui, Segoe UI, Arial, sans-serif','lineColor':'#333'},'flowchart':{'curve':'linear','nodeSpacing':45,'rankSpacing':70,'padding':10,'htmlLabels':false,'useMaxWidth':true}}}%%
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
        <td>The Content Protection Information Exchange (CPIX) interface, defined in a separate specification. A CPIX document carries keys and DRM information used to encrypt and protect content, and may itself be encrypted, signed, and authenticated for confidentiality, source, and integrity.
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

<figure class="diagram">
<pre class=mermaid>
%%{init: {'theme':'neutral','themeVariables':{'fontSize':'16px','fontFamily':'system-ui, Segoe UI, Arial, sans-serif','lineColor':'#333'},'flowchart':{'curve':'linear','nodeSpacing':40,'rankSpacing':60,'padding':10,'htmlLabels':false,'useMaxWidth':true}}}%%
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

- **Application**: uses the DASH/media player to play back a DASH Media
    Presentation, typically providing the MPD or its URL to the DASH client.
- **DASH Player**: a complete player, including media playback platform and
    content decryption module.
- **DASH Access Client**: accesses and downloads media from the network and uses
    the media playback platform and content decryption module for decoding and
    playback.
- **Management**: controls internal processes and communication with the
    application.
- **MPD Processing**: parses and processes the MPD and extracts relevant
    information.
- **Adaptation Set Selection**: selects Adaptation Sets based on user,
    environment, and capability information.
- **Dynamic Switching and Request Scheduling**: runs adaptive-bitrate logic and
    triggers dynamic switching across Representations.
- **Throughput Estimation**: estimates throughput from a specific
    network/application server.
- **Metrics Collection**: collects streaming metrics and offers them to the
    application for processing and potential reporting to network entities.
- **Media Playback Management**: moves downloaded information into the media
    playback platform and handles content protection and DRM information.
- **Media Playback Platform**: plays back CMAF-based media using well-defined
    playback instructions.
- **Event Processing**: processes DASH events and provides information to the
    application.

Detailed APIs and methods to communicate with a DASH reference client are
implemented in the DASH-IF reference client (see [[#part-descriptions]] and
Part 12). DASH players typically rely on CMAF-capable playback platforms and
decryption modules rather than a specific implementation; more detail on a
CMAF-capable playback platform is given in Part 2.

Content security is accomplished in a device by two functions:

- **Key management** by a digital rights management (DRM) system that
    authenticates a device and authorizes decryption and playback under specific
    conditions (e.g. output protection, rental period, hardware root of trust);
    see Part 6.
- **Decryption** of an encrypted track using a specific decryption scheme; see
    Part 6.

Received DASH events are processed for client consumption; see Part 10.

## DASH-IF IOP Parts ## {#part-descriptions}

The following summarises each part of DASH-IF IOP v5:

- **Part 1 — Overview, Architecture and Interfaces** (this document): an overview
    of the features in the DASH-IF Interoperability Guidelines, with a reference
    architecture, interfaces, and functional blocks.
- **Part 2 — Core principles and CMAF mapping**: the core principles of DASH
    including the data and timing model, and the mapping of CMAF data structures
    to DASH Media Presentations.
- **Part 3 — On-demand services**: requirements and recommendations for using
    DASH for on-demand services.
- **Part 4 — Live and low-latency services**: live service offerings, including
    low-latency services.
- **Part 5 — Ad insertion and content replacement**: guidelines for advertisement
    insertion in a CMAF-based, DASH-delivered workflow, covering conditioning,
    packaging, and signalling for both SSAI and SGAI.
- **Part 6 — Content protection and security**: guidelines for encrypted content
    in CMAF protected by MPEG CENC, key rotation, Enhanced Clear Key Content
    Protection (ECCP), and the DASH-IF content-protection XML schema.
- **Part 7 — Video**: the CMAF media profiles and DASH signalling for video
    tracks.
- **Part 8 — Audio**: audio interoperability points, coding profiles, ISO BMFF
    packaging, and MPD parameters.
- **Part 9 — Text (Subtitle)**: subtitle/caption interoperability points and
    signalling.
- **Part 10 — Events**: event signalling and processing.
- **Part 11 — Additional functionalities**: further interoperability features.
- **Part 12 — Conformance and reference tools**: the conformance validator,
    reference player, live source simulator, and test assets.

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
</table>
