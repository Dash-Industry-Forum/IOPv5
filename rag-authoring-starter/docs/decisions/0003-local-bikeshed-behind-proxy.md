# ADR 0003: Local Bikeshed build behind a TLS-intercepting proxy

- Status: accepted
- Date: 2025

## Context

Bikeshed is the canonical authoring tool (ADR 0002), built locally without Docker
(Option B). Two blockers prevented a local build:

1. **Corporate TLS interception.** A proxy re-signs TLS, so Python `requests`
   (used by Bikeshed) failed with `self-signed certificate in certificate chain`.
   This blocked `bikeshed update` and any data fetch — and was a root cause of the
   original "the agent does not act" symptom.
2. **`Group: dashif` is not a built-in Bikeshed group.** It is provided by the
   DASH-IF-IOP repo's boilerplate/container, absent from a plain pip install.

## Decision

Solve both locally, reproducibly, without weakening TLS security:

1. **`tools/env/build_ca_bundle.py`** exports the OS trust store (via
   `wincertstore` on Windows), which already contains the proxy's root CA, and
   merges it with certifi into `build-tools/corp-ca-bundle.pem`. Tools point at it
   via `REQUESTS_CA_BUNDLE` / `SSL_CERT_FILE`. Verification stays **on**; we never
   set `verify=False`. The bundle is machine-specific and gitignored.

2. **`tools/env/install_dashif_boilerplate.py`** fetches the DASH-IF `dashif`
   boilerplate includes (`defaults`, `header`, `logo`) into Bikeshed's
   `spec-data/boilerplate/org-dashif/` and registers a `dashif` org + group in
   `doctypes.kdl` (matching Bikeshed's KDL schema). This reuses the DASH-IF
   authoring assets rather than replicating document content.

3. **`build.ps1`** wraps the local build: it sets the CA env vars and runs
   `bikeshed spec` per `specs/<part>/<part>.bs`, with a `-Watch` mode.

The Part 4 `.bs` metadata was corrected to the Bikeshed-required
`<pre class=metadata> ... </pre>` block (the bare-key form only works inside the
DASH-IF container's preprocessing) and given `Abstract` / `Editor` keys that the
`dashif` header expects.

## Consequences

- `./build.ps1 part04-live-low-latency` produces a ~100 KB styled HTML spec
  locally, offline-capable after the one-time `bikeshed update`.
- The CA-bundle approach generalises to pip, git, and any `requests`-based tool
  behind the same proxy.
- If DASH-IF later updates its boilerplate, re-run
  `install_dashif_boilerplate.py` to refresh `org-dashif`.
- A Docker-based build (DASH-IF's exact container) remains a future option for
  publish-time parity; not required for authoring.
