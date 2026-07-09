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

Any identified bugs or missing features may be submitted through the DASH-IF
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
terms *shall*, *shall not*, *should*, *should not*, and *may*, beyond what is
described in the ETSI Drafting Rules, in terms of how the DASH-IF tools treat
each keyword.

## Content Authoring ## {#conformance-authoring}

Where an IOP document associates a conformance keyword with a content-authoring
statement, the following applies:

- **shall / shall not**: the [=DASH-IF Conformance Validator=] provides a check
    and issues an **error** if the requirement is not fulfilled.
- **should / should not**: the validator provides a check and issues a
    **warning** if the recommendation is not fulfilled.
- **should / may**: where present, the validator's feature check **documents**
    the feature of the content (informational).

## Client Processing ## {#conformance-client}

Where an IOP document associates a conformance keyword with DASH client behaviour,
the following applies:

- **shall**: test content is provided for the rule and the reference client
    ([=dash.js=]) implements the feature.
- **shall not**: the reference client does not implement the feature.
- **should**: test content is provided and the reference client implements the
    feature unless there is a justification for not doing so.
- **should not**: the reference client does not implement the feature unless
    there is a justification for doing so.
- **may**: test content is provided and the reference client implements the
    feature where justified.

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

Issue: Redraw the source "Figure 1 — DASH-IF conformance and reference tools" as
a Mermaid diagram; see below.

<figure>
<pre class=mermaid>
flowchart LR
    CA[Content author / service provider] --> V[DASH-IF Conformance Validator]
    V -->|errors / warnings| CA
    TA[Test assets] --> V
    TA --> P[dash.js reference player]
    LS[livesim2 live source simulator] --> P
    LS --> V
    P -->|playback verification| DEV[Client / player developer]
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
presentations, and ad insertion.

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
are complete — promoted to a fully supported feature. Intermediate steps may
involve one or more community-review rounds.

# Change History # {#change-history}

<figure>
  <table class="data">
    <thead>
      <tr><th>Version<th>Date<th>Change
    <tbody>
      <tr>
        <td>0.1
        <td>Initial
        <td>Migrated from the Part 12 draft; reference-tool sections updated to current dash.js and the second-generation livesim2 (CMAF Ingest, SGAI, stateless URL parameters).
  </table>
  <figcaption>Part 12 change history.</figcaption>
</figure>
