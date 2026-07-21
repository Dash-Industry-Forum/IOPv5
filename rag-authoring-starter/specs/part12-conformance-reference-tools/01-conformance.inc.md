<!--
  Part 12: Conformance and Reference Tools.
  Migrated from DASH-IF-IOPv5.0-Part12-DRAFT.docx.
  Provenance: dashif-iop-v5-part12-draft #3,#9..#17.
  Reference-implementation facts updated (2024-2025) from:
    - dash.js:  https://github.com/Dash-Industry-Forum/dash.js
    - livesim2: https://github.com/Dash-Industry-Forum/livesim2  (2nd-gen simulator)
  Editorial: the draft's "live source simulator" (livesim1) section is updated to
  livesim2; issue-tracker guidance points at active repositories.
-->

# Scope # {#scope}

The present document provides an overview of the DASH-IF reference and conformance
tools. In particular, it introduces the conformance software used to verify
service offerings, the [=dash.js=] reference client, the [=livesim2=] live source
simulator, and the DASH-IF test assets. It also describes how conformance
keywords used across the IOP parts are interpreted by these tools.

Any identified bugs or missing features <span class=modal-keyword>may</span> be submitted through the DASH-IF
issue tracker at
[https://github.com/Dash-Industry-Forum/IOPv5/issues](https://github.com/Dash-Industry-Forum/IOPv5/issues).

# Terms and Definitions # {#terms}

: <dfn>DASH-IF Conformance Validator</dfn>
:: The DASH-IF open-source software that validates DASH Media Presentations
    (MPD, MPD updates, and Segment formats) against the requirements and
    recommendations of a DASH profile.
: <dfn>dash.js</dfn>
:: The DASH-IF JavaScript reference client for MPEG-DASH playback in browser
    environments supporting Media Source Extensions (MSE) and Encrypted Media
    Extensions (EME).
: <dfn>livesim2</dfn>
:: The second-generation DASH-IF live source simulator, which generates a
    wall-clock-synchronized, effectively infinite live stream by looping VoD DASH
    assets and rewriting timestamps.

# Conformance Interpretations # {#conformance-interpretations}

## Introduction ## {#conformance-intro}

This clause provides guidance on the contextual interpretation of the conformance
terms <span class=modal-keyword>shall</span>, <span class=modal-keyword>shall not</span>,
<span class=modal-keyword>should</span>, <span class=modal-keyword>should not</span>,
and <span class=modal-keyword>may</span>, beyond what is described in the ETSI
Drafting Rules, in terms of how the DASH-IF tools treat each keyword.

## Content Authoring ## {#conformance-authoring}

Where an IOP document associates a conformance keyword with a content-authoring
statement, the following applies:

- <span class=modal-keyword>shall</span> / <span class=modal-keyword>shall not</span>:
    the [=DASH-IF Conformance Validator=] provides a check and issues an **error**
    if the requirement is not fulfilled.
- <span class=modal-keyword>should</span> / <span class=modal-keyword>should not</span>:
    the validator provides a check and issues a **warning** if the recommendation
    is not fulfilled.
- <span class=modal-keyword>should</span> / <span class=modal-keyword>may</span>:
    where present, the validator's feature check **documents** the feature of the
    content (informational).

## Client Processing ## {#conformance-client}

Where an IOP document associates a conformance keyword with DASH client behaviour,
the following applies:

- <span class=modal-keyword>shall</span>: test content is provided for the rule
    and the reference client ([=dash.js=]) implements the feature.
- <span class=modal-keyword>shall not</span>: the reference client does not
    implement the feature.
- <span class=modal-keyword>should</span>: test content is provided and the
    reference client implements the feature unless there is a justification for
    not doing so.
- <span class=modal-keyword>should not</span>: the reference client does not
    implement the feature unless there is a justification for doing so.
- <span class=modal-keyword>may</span>: test content is provided and the reference
    client implements the feature where justified.

# Conformance and Reference Tools # {#tools}

## Overview ## {#tools-overview}

DASH-IF leads the development of testing tools that support the development and
deployment of interoperable DASH-based streaming. These tools are publicly
available for community use and contribution, and are hosted under
[https://github.com/Dash-Industry-Forum](https://github.com/Dash-Industry-Forum).

An implementor or service provider for DASH Media Presentations is encouraged to
use the [=DASH-IF Conformance Validator=] to verify that a service conforms to
the requirements indicated by the Media Presentation, and to check playback with
the [=dash.js=] reference player. An implementor of a DASH client is encouraged
to use the relevant test assets for testing. As a necessary condition, test
assets must pass DASH-IF conformance validation.

Note: The relationships between the tools are shown in Figure 1.

<figure class="diagram">
<pre class=mermaid>
%%{init: {'theme':'neutral','themeVariables':{'fontSize':'18px','fontFamily':'system-ui, Segoe UI, Arial, sans-serif','lineColor':'#333'},'flowchart':{'curve':'linear','nodeSpacing':55,'rankSpacing':80,'padding':14,'htmlLabels':false,'useMaxWidth':true}}}%%
flowchart LR
    CA["Content author / service provider"] --> V["DASH-IF Conformance Validator"]
    V -->|errors / warnings| CA
    TA[Test assets] --> V
    TA --> P[dash.js reference player]
    LS[livesim2 live source simulator] --> P
    LS --> V
    P -->|playback verification| DEV["Client / player developer"]
    classDef box fill:#eef3f8,stroke:#33475b,stroke-width:1.4px,color:#1a2733;
    class CA,V,TA,P,LS,DEV box;
</pre>
<figcaption>DASH-IF conformance and reference tools and their relationships.</figcaption>
</figure>

## Conformance Validator ## {#tools-validator}

The [=DASH-IF Conformance Validator=] validates DASH Media Presentations against
the requirements and recommendations of a DASH profile. It covers the MPD (and
MPD updates) as well as the Segment formats, reporting expected and unexpected
behaviour observed in a Media Presentation that claims conformance to one or more
profiles. It therefore provides a test and validation environment for content
providers, service providers, and player developers.

Development of the validator began after the first edition of MPEG-DASH
[[!MPEGDASH]] and has been continuously updated for new features and newer
editions of the supported standards. It is open-source software, available on
GitHub at
[https://github.com/Dash-Industry-Forum/DASH-IF-Conformance](https://github.com/Dash-Industry-Forum/DASH-IF-Conformance),
and is hosted by DASH-IF at
[https://conformance.dashif.org](https://conformance.dashif.org).

## Reference Player: dash.js ## {#tools-dashjs}

[=dash.js=] is a free, open-source MPEG-DASH player that serves as the JavaScript
reference client for implementing production-grade DASH players. It relies on
HTML5 media, Media Source Extensions (MSE) with the ISO BMFF byte-stream format,
and Encrypted Media Extensions (EME) as defined by the W3C.

It is available on GitHub at
[https://github.com/Dash-Industry-Forum/dash.js](https://github.com/Dash-Industry-Forum/dash.js)
and as an npm module (`dashjs`). Current entry points include:

- Documentation and quick-start:
    [https://dashif.org/dash.js/](https://dashif.org/dash.js/)
- Hosted reference player:
    [https://reference.dashif.org/dash.js/latest/samples/dash-if-reference-player/index.html](https://reference.dashif.org/dash.js/latest/samples/dash-if-reference-player/index.html)
- Samples:
    [https://reference.dashif.org/dash.js/latest/samples/](https://reference.dashif.org/dash.js/latest/samples/)

dash.js is released under the BSD licence, and issues are raised on GitHub.
Sample streams are included in a drop-down menu in the sample reference UI and
serve as inputs for implementing and verifying features.

## Live Source Simulator: livesim2 ## {#tools-livesim2}

[=livesim2=] is the second-generation DASH-IF live source simulator (superseding
the original `livesim`). It produces a wall-clock (UTC) synchronized, effectively
infinite linear stream of segments by looping input VoD DASH assets and rewriting
timestamps, so that an asset of duration *D* restarts every *D* relative to the
epoch. It is written in Go and compiles to a single binary that serves content
over a built-in HTTP/2 server, with optional automatic HTTPS via Let's Encrypt.

It is available on GitHub at
[https://github.com/Dash-Industry-Forum/livesim2](https://github.com/Dash-Industry-Forum/livesim2)
and hosted by DASH-IF at
[https://livesim2.dashif.org](https://livesim2.dashif.org).

Notable characteristics relevant to conformance testing:

- **Stateless, URL-parameterized generation.** Configuration is carried in the
    URL (in both MPD and segment requests), so the server can generate a large
    number of parameter variations without server-side state. Examples include
    `/segtimeline_1` (SegmentTimeline with `$Time$`), `/segtimelinenr_1`
    (SegmentTimeline with `$Number$`), and generated subtitles via
    `/timesubsstpp_en,sv` (`stpp`) or `/timesubswvtt_en,sv` (`wvtt`).
- **Deterministic time testing.** The `?nowMS=...` query parameter sets the
    reference wall-clock time for any request, enabling deterministic testing of
    time-dependent behaviour (segment availability, clock skew, early/late
    requests). A request that is too early or too late receives an HTTP 404 whose
    body reports by how much.
- **CMAF Ingest (v1.1).** livesim2 can act as a CMAF ingest source, pushing live
    segments to a destination via HTTP PUT, useful for testing ingest receivers.
- **Server-Guided Ad Insertion (SGAI).** livesim2 can signal SGAI using
    DASH 6th-edition *Alternative-MPD Replace* events.
- **Tooling.** A companion `dashfetcher` tool downloads DASH VoD assets (MPD and
    segments) for use as simulator input.

Note: Input VoD assets must be in the `isoff-live` profile (individual segment
files) using either SegmentTimeline with `$Time$` or SegmentTemplate with
`$Number$`, with additional constraints on segment-duration regularity.

## Test Assets and Test Cases ## {#tools-test-assets}

Test assets are essential to ensure large-scale interoperability. DASH-IF
maintains a Test Assets Database of test vectors covering a wide variety of
features — static and dynamic Media Presentations, on-demand and live services,
different media components and codecs, DRM protection, single- and multi-period
presentations, text tracks, captions and subtitles, and ad insertion.

The Test Assets Database is open source, split into a user-interface project and
a backend dataset:

- UI:
    [https://github.com/Dash-Industry-Forum/Test-Assets-UI-public](https://github.com/Dash-Industry-Forum/Test-Assets-UI-public)
- Dataset:
    [https://github.com/Dash-Industry-Forum/Test-Assets-Dataset-Public](https://github.com/Dash-Industry-Forum/Test-Assets-Dataset-Public)

It is hosted by DASH-IF at
[https://testassets.dashif.org](https://testassets.dashif.org). As a necessary
condition, test assets must pass DASH-IF conformance validation.

Note: CTA-WAVE test content is a common companion asset set and can be fetched
with `dashfetcher`; see [=livesim2=].

## Initial Part 9 text-track conformance mapping ## {#tools-part9-text-conformance}

The following initial mapping identifies test and validation expectations for
DASH-IF IOP v5 Part 9 text, caption, and subtitle requirements. This table is a
starting point for issue creation and test-asset planning; it does not by itself
define new Part 9 requirements.

<table class="data">
  <caption>Initial Part 9 conformance mapping.</caption>
  <thead>
    <tr><th>Part 9 feature<th>Primary validation target<th>Reference/test asset expectation
  <tbody>
    <tr>
      <td>CMAF text media profiles
      <td>The [=DASH-IF Conformance Validator=] checks MPD `@mimeType`, `@codecs`, and CMAF brand/profile consistency where the required information is available.
      <td>Test assets should include IMSC1 Text (`im1t` / `stpp.ttml.im1t`), IMSC1 Image (`im1i` / `stpp.ttml.im1i`), WebVTT (`cwvt` / `wvtt`), and CTA 608/708 carried in video.
    <tr>
      <td>Text-track Adaptation Set signalling
      <td>The validator checks `@mimeType`, `@codecs`, `@lang`, `Accessibility`, and `Role` usage for text Adaptation Sets.
      <td>Test assets should cover subtitle, caption, and easy-reader signalling, including multiple alternative text Adaptation Sets that differ by language, role, accessibility, or codec.
    <tr>
      <td>CTA 608/708 in video tracks
      <td>The validator checks the presence and syntax of the video Adaptation Set `Accessibility` descriptor used for CTA 608/708 closed-caption signalling.
      <td>Test assets should include CEA-608 channel/language signalling such as `CC1=eng;CC3=spa`, single-language shorthand, and multi-channel cases where the language-only shorthand is not used.
    <tr>
      <td>IMSC1 storage and signalling
      <td>The validator checks MPD signalling for IMSC1 text tracks and the segment/package form where applicable.
      <td>Test assets should include ISO BMFF encapsulated IMSC1 and, where retained for compatibility, stand-alone XML file delivery.
    <tr>
      <td>Chunks and gaps
      <td>The validator checks that text tracks are not chunked in conflict with Part 9 guidance and that periods without text content still provide continuous segments with empty documents where required.
      <td>Test assets should include empty-document gaps and short-duration text segments that still conform to the IMSC1 Hypothetical Render Model.
    <tr>
      <td>Client text-track selection
      <td>[=dash.js=] and other reference clients exercise language, codec, `EssentialProperty`, `Role`, `Accessibility`, and `@selectionPriority` based text-track selection.
      <td>Test assets should include multiple selectable text tracks and negative-selection cases for unsupported descriptors, codecs, or languages.
</table>

Issue: This Part 9 mapping is an initial source-level conformance inventory. It
should be reconciled with actual DASH-IF Conformance Validator coverage, dash.js
sample coverage, and the DASH-IF Test Assets Database before being treated as a
complete conformance plan.

## Initial Part 5 ad-insertion conformance mapping ## {#tools-part5-ad-insertion-conformance}

The following initial mapping identifies validator, reference-client, livesim2,
and test-asset expectations for DASH-IF IOP v5 Part 5 ad insertion. This table
is a starting point for F-0010 issue creation and does not by itself define new
Part 5 requirements.

<table class="data">
  <caption>Initial Part 5 ad-insertion conformance mapping.</caption>
  <thead>
    <tr><th>Part 5 feature<th>Primary validation target<th>Reference/test asset expectation
  <tbody>
    <tr>
      <td>IF-3 opportunity metadata and SCTE-35 MPD Events
      <td>The [=DASH-IF Conformance Validator=] checks DASH EventStream syntax, event timing, `@presentationTime`, `@duration`, duplicate-event `@id` handling where feasible, and SCTE-35 event scheme usage.
      <td>Test assets should include SCTE-35 MPD Event examples for `time_signal()` plus `segmentation_descriptor()`, legacy `splice_insert()`, early termination, expected-duration correction, and duplicate-event filtering.
    <tr>
      <td>IF-4 DASH-IF ad content storage and Table 4 requirements
      <td>The validator checks ad-content MPD constraints including one static Period, `MPD@profiles`, absent forbidden timing attributes, Period BaseURL usage, AssetIdentifier, EventStream/InbandEventStream presence, and CMAF profile compatibility.
      <td>Test assets should include DASH-IF ad content MPDs with multiple codecs/resolutions, Ad-ID and DASH-IF asset identifiers, slate content, and negative cases for forbidden attributes.
    <tr>
      <td>IF-5 MPD and segments with ad placements
      <td>The validator checks multi-Period MPD structure, Period start/duration rules, continuity/connectivity signalling, EventStream splitting/copying, UTCTiming expectations, and ad-content Period insertion constraints where mechanically testable.
      <td>Test assets should include SSAI multi-Period presentations for exact duration match, ad overrun/truncation, ad underrun/slate insertion, overlapping segment boundaries, and mixed main/ad Periods.
    <tr>
      <td>IF-6 ad metadata and DASH Callback Events
      <td>The validator checks event signalling syntax once the callback event scheme and payload rules are finalized; dash.js samples exercise event dispatch and callback timing.
      <td>Test assets should include inserted ad Periods with callback metadata aligned to Period and media timelines, including split/truncated ad cases.
    <tr>
      <td>IF-7 remote resolution and URL parameter decisioning
      <td>[=livesim2=] and [=dash.js=] exercise Server-Guided Ad Insertion and remote entity / Remote Period resolution; validator checks MPD syntax and remote-reference structure where applicable.
      <td>Test assets should include SGAI late-binding examples, URL-parameter decisioning, content-conditioning parameters, remote Period resolution, and re-decisioning after seek/rewind.
    <tr>
      <td>IF-8 ad tracking and measurement
      <td>Reference applications and dash.js samples exercise VAST tracking callbacks, Open Measurement SDK integration points, and alternative measurement metadata association.
      <td>Test assets should include VAST tracking events for impression/start/quartiles/complete and metadata mapping to inserted Periods after splitting or truncation.
    <tr>
      <td>IF-9 reference playback and decryption
      <td>dash.js validates playback behaviour across main/ad transitions using MSE and EME where encrypted assets are provided; validator checks MPD/content-protection signalling.
      <td>Test assets should include clear and encrypted multi-Period ad insertion cases, key changes at boundaries, compatible CMAF headers, and Part 6-aligned protection signalling.
</table>

Issue: This Part 5 mapping is an initial source-level conformance inventory. It
should be reconciled with actual DASH-IF Conformance Validator coverage, dash.js
SGAI/sample coverage, livesim2 SGAI support, and the DASH-IF Test Assets
Database before being treated as a complete conformance plan.

## Issue Tracking and Coordination ## {#tools-github}

DASH-IF maintains public issue trackers on GitHub for the IOP and the individual
tools; new work for IOP v5 is tracked at
[https://github.com/Dash-Industry-Forum/IOPv5/issues](https://github.com/Dash-Industry-Forum/IOPv5/issues),
and each reference tool uses the issue tracker of its own repository.

DASH-IF coordinates with other organizations and open-source projects to support
interoperable DASH deployment, including DVB, CTA WAVE, MPEG, ATSC, W3C, and
3GPP, as well as projects such as FFmpeg and GPAC.

## The Desired Approach for Interoperability ## {#tools-approach}

Effective interoperability balances good specifications, test and conformance
tools, reference implementations, open-source software, and lessons learned from
deployments. As a general model, a new feature is first added to a draft IOP
document (possibly by reference to or collaboration with the organization owning
a referenced specification, e.g. MPEG), then supported by test content, the
conformance validator, and the reference player, and finally — once all pieces
are complete — promoted to a fully supported feature. Intermediate steps <span class=modal-keyword>may</span>
involve one or more community-review rounds.

# Change History # {#change-history}

<table class="data">
  <caption>Part 12 change history.</caption>
  <thead>
    <tr><th>Version<th>Date<th>Change
  <tbody>
    <tr>
      <td>0.1
      <td>Initial
      <td>Migrated from the Part 12 draft; reference-tool sections updated to current dash.js and the second-generation livesim2 (CMAF Ingest, SGAI, stateless URL parameters).
    <tr>
      <td>0.2
      <td>Reconciliation
      <td>Added initial Part 9 text-track conformance mapping for CMAF text profiles, text/video Adaptation Set signalling, CTA 608/708, IMSC1, chunks/gaps, and client selection.
    <tr>
      <td>0.3
      <td>Reconciliation
      <td>Added initial Part 5 ad-insertion conformance mapping covering IF-3 through IF-9 validator, dash.js, livesim2, and test-asset expectations.
</table>
