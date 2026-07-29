# Enhanced Clear Key Content Protection (ECCP) # {#CPS-ECCP}

## General ## {#CPS-ECCP-general}

Enhanced Clear Key Content Protection (ECCP) is a constrained use of Clear Key,
HTTPS delivery, and access-control mechanisms intended to provide stronger
practical protection than any of those mechanisms used individually.

Issue: This section migrates published IOP v5.1.0 Part 6 clause 11 into the
Bikeshed source. It preserves the published ECCP requirements as a
`Draft/reconciliation` baseline. Final editorial review is still needed for
cross-references, examples, and interaction with the newer DASH-IF interoperable
license request model.

## Background ## {#CPS-ECCP-background}

TLS protects content while it is transferred between client and server, but media
content is stored and processed in the clear after delivery. Token authentication
schemes authenticate or authorize a client, but do not by themselves protect the
media once delivered. Clear Key protects encrypted content at rest and while it
is processed in an inaccessible media pipeline, but by itself provides no
authentication because a key can be provided to any client that requests it.

ECCP combines HTTPS delivery, access control, token authentication or equivalent
authorization, and Clear Key content protection so that authorization decisions
are cryptographically enforced through encrypted media delivery and key access.

ECCP is therefore a collective set of restrictions on:

- content preparation,
- manifest preparation,
- license-server behavior,
- segment access control and authentication.

## Constraints on DASH content generation ## {#CPS-ECCP-content-generation}

Media segments used with ECCP ***shall*** be packaged in CMAF containers
according to the applicable DASH-IF IOP Part 1 and Part 2 constraints. Additional
constraints for encryption are defined in the content-protection constraints for
CMAF, and content-protection constraints for the MPD are defined in the MPD
content-protection signaling sections of this part.

## Constraints on content protection ## {#CPS-ECCP-content-protection}

Implementations of W3C Clear Key content protection used with ECCP ***shall***
follow the Clear Key requirements defined in this part.

Note: ECCP support is not announced in the MPD using an additional
**ContentProtection** descriptor or a separate ECCP system identifier. A
**ContentProtection** descriptor using the Clear Key system identifier is
sufficient. The additional ECCP restrictions are enforced through the
interactions with media servers and content-key servers.

## Constraints on transport ## {#CPS-ECCP-transport}

All URLs referencing manifests, media objects, and license servers used with
ECCP ***shall*** use the `https` URI scheme. The TLS version used for those
resources ***shall*** be TLS 1.2 or higher.

## Constraints on access control ## {#CPS-ECCP-access-control}

Access control to the manifest, the license-key URL, and all media segments
containing encrypted content ***shall*** be present. No object described by the
manifest, including the manifest itself, ***shall*** be openly available to an
unauthenticated or unauthorized client.

Access control may invoke authorization, authentication, or both. Enforcement
mechanisms include, for example:

- tokens, including token formats such as CTA WAVE Common Access Token (CAT),
- client certificates,
- proxy solutions, such as a license proxy that performs authorization checks
  before forwarding license requests to the actual license server.

If tokens are used, they ***shall*** be transmitted either as part of the URL
path or as a query argument, so that native implementations transfer the token
information automatically when making the relevant `GET` or `POST` request.

## Client requirements ## {#CPS-ECCP-client-requirements}

To support ECCP, a client ***shall*** support:

- Clear Key as constrained in this part, and
- HTTPS as constrained by the ECCP transport requirements.

## Examples ## {#CPS-ECCP-examples}

The following example illustrates the structure of an MPD for content protected
by ECCP. It is adapted from the published IOP v5.1.0 Part 6 clause 11 example
and should be reviewed against the final schema-casing decision for
`dashif:laurl` / `dashif:Laurl`.

```xml
<MPD xmlns:dashif="https://dashif.org/"
     xmlns="urn:mpeg:dash:schema:mpd:2011"
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xmlns:cenc="urn:mpeg:cenc:2013"
     profiles="urn:mpeg:dash:profile:isoff-live:2011"
     minBufferTime="PT2S"
     type="static"
     mediaPresentationDuration="PT32.08333206176758S">
  <Period id="0">
    <AdaptationSet id="0"
                   contentType="video"
                   maxWidth="1920"
                   maxHeight="1080"
                   frameRate="12288/512"
                   segmentAlignment="true"
                   par="16:9">
      <ContentProtection value="cbcs"
                         schemeIdUri="urn:mpeg:dash:mp4protection:2011"
                         cenc:default_KID="9eb4050d-e44b-4802-932e-27d75083e266"/>
      <ContentProtection value="ClearKey1.0"
                         schemeIdUri="urn:uuid:e2719d58-a985-b3c9-781a-b030af78d30e">
        <dashif:laurl>https://example-license-server.com/license</dashif:laurl>
      </ContentProtection>
      <Representation id="0"
                      bandwidth="1350152"
                      codecs="avc1.64081f"
                      mimeType="video/mp4"
                      sar="1:1"
                      width="768"
                      height="432">
        <SegmentTemplate timescale="12288"
                         initialization="768x432/init.mp4"
                         media="768x432/$Number%04d$.m4s"
                         startNumber="1">
          <SegmentTimeline>
            <S t="0" d="49152" r="7"/>
            <S t="393216" d="1024"/>
          </SegmentTimeline>
        </SegmentTemplate>
      </Representation>
    </AdaptationSet>
  </Period>
</MPD>
```

For Clear Key, the client derives the key identifier used in the license request
from the `cenc:default_KID` value according to the Clear Key request format. For
example, the license request body can contain a `kids` array and request type:

```json
{"kids":["nrQFDeRLSAKTLifXUIPiZg"],"type":"temporary"}
```

The license server response can contain one or more keys:

```json
{"keys":[{"kty":"oct","k":"FmY0xnWCPCNaSpRG-tUuTQ","kid":"nrQFDeRLSAKTLifXUIPiZg"}],"type":"temporary"}
```

The player uses the returned key material to decrypt the protected samples
through the CENC-capable media pipeline.