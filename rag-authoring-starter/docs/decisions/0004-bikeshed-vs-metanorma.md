# ADR 0004: Authoring toolchain — Bikeshed vs Metanorma

- Status: accepted
- Date: 2025
- Supersedes: the "Bikeshed vs Metanorma" section of ADR 0002 (which parked the
  evaluation); this ADR is the deeper evaluation requested afterwards.

## Context

DASH-IF IOP v5 is authored in this workspace and must ultimately be publishable
in a form consistent with the existing DASH-IF-IOP repository and the
dashif.org guidelines. Two candidate toolchains were considered:

- **Bikeshed** — the tool the current DASH-IF-IOP repo already uses. Input is
  Bikeshed-flavoured Markdown (`.bs` + `.inc.md`), output is a single HTML spec.
  DASH-IF has a custom `dashif` Bikeshed *group* (boilerplate + `doctypes.kdl`).
- **Metanorma** — an AsciiDoc-based standards toolchain that emits HTML **and**
  Word (`.doc`) **and** PDF from one source, validates document structure against
  a semantic XML model, and ships organization "flavours" (ISO, IEC, IEEE, IETF,
  ITU, …).

The published DASH-IF deliverables are **Word/PDF** documents that follow
**ETSI/ISO drafting conventions** (the very "shall/should/may" and clause
structure our Part 1/Part 12 text mirrors). That makes Metanorma's ISO/IEC
fidelity and DOC/PDF output genuinely attractive, so the option deserved a real
test rather than a hand-wave.

## What was actually verified in this environment

Facts established by running tools here (not assumptions):

1. **Bikeshed works today.** Local `bikeshed` builds all three current parts
   cleanly behind the corporate TLS proxy (ADR 0003), with the `dashif` group
   boilerplate installed and shared includes staged by `build.ps1`/`build_all.py`.
   Round-trip edit→build→check is a few seconds.
2. **Metanorma is present and runs standalone.** The winget package
   (`Metanorma.Metanorma`) bundles its own Ruby: `metanorma help`,
   `metanorma list-doctypes` run **without** a separate Ruby/gem/Docker install
   (none of which are on this machine). This removes the main objection recorded
   in ADR 0002 ("larger investment: Ruby toolchain, gem or Docker").
3. **Metanorma ships the relevant flavours.** `list-doctypes` shows
   `iso`, `iec`, `ieee`, `ietf`, `itu`, `generic` — each producing
   `html, doc, pdf` (ISO also `sts`/`isosts`). There is **no `dashif` flavour**;
   DASH-IF would use `generic` or `iso`/`itu` until/unless a DASH-IF flavour is
   built.

## Comparison

| Dimension | Bikeshed | Metanorma |
|---|---|---|
| Alignment with existing DASH-IF-IOP repo | Exact (same `.bs`/`.inc.md`, `dashif` group, CI) | Divergent (AsciiDoc, different CI, no `dashif` flavour) |
| Input format | Bikeshed Markdown | AsciiDoc |
| Output | HTML (single file) | HTML + **DOC** + **PDF** from one source |
| Standards fidelity (ISO/ETSI clause model, ToC, refs) | Good, but org-specific styling is manual | Strong; ISO/IEC/ITU flavours model this natively |
| Structure validation | Link/ref checks; our `check_links.py` | Semantic XML model + schema validation |
| Cross-refs / bibliography | SpecRef + local `biblio.json` | Built-in bibliographic database, relaton |
| Diagrams | Mermaid/PlantUML inline (works today) | AsciiDoc + Mermaid/PlantUML |
| Toolchain footprint here | pip `bikeshed` (works, proxy solved) | self-contained binary (works) |
| Migration cost from current state | Zero (already in use) | Re-port all `.inc.md` → AsciiDoc; rebuild CI; author/boilerplate mapping |
| DOC/PDF for members & IPR review | Not native (HTML → external convert) | Native, high-fidelity |

## Decision

**Keep Bikeshed as the canonical authoring path**, and **adopt Metanorma as a
tracked, opt-in secondary path for DOC/PDF rendering**, not (yet) as the source
of truth.

Rationale:

- The overriding near-term goal is to **align with the existing DASH-IF-IOP
  repository and workflow** (issue #3): same `specs/<part>/<part>.bs` +
  `.inc.md`, same `dashif` group, same Pages-based CI. Switching the *source
  format* to AsciiDoc now would fork us away from that alignment and throw away
  the migrated Part 1/4/12 content.
- Metanorma's decisive advantage is **native DOC/PDF at ISO/ETSI fidelity**,
  which matters for **member circulation and IPR review**, not for the HTML
  guidelines. That is a *rendering/output* need, addressable later without moving
  the source of truth.
- The earlier blocker (Ruby/Docker footprint) is **no longer real** here — the
  bundled binary runs standalone — so the door is genuinely open, but the
  content-migration and CI cost is not justified while Bikeshed meets the
  publish-to-dashif.org requirement.

## Consequences

- No change to the current source format, CI, or contributor workflow.
- A proof-of-concept Metanorma path may live under
  `authoring/dashif-metanorma-template/` and be built with the standalone
  `metanorma` binary (`generic` or `iso` flavour) to evaluate DOC/PDF fidelity on
  one real part (e.g. Part 12). It must not become a second source of truth.
- **Revisit and potentially promote Metanorma** if any of these become hard
  requirements: (a) native Word/PDF deliverables at ISO/ETSI fidelity for every
  part; (b) schema-level structure validation; (c) a bespoke **DASH-IF Metanorma
  flavour** is funded. At that point, the `.inc.md` → AsciiDoc migration and a
  parallel CI job would be scoped as their own work item.
- If promoted, prefer a **one-way generation** (Bikeshed Markdown remains
  authored source; a converter emits AsciiDoc for Metanorma) over dual authoring,
  to avoid divergence.

## Follow-ups (tracked, not blocking)

- Optional: build one part with `metanorma compile --agree-to-terms` using the
  `generic` flavour and compare the DOC/PDF against a published DASH-IF Part.
- Optional: assess effort for a `dashif` Metanorma flavour (styles, boilerplate,
  ToC, IPR page) vs. maintaining the Bikeshed `dashif` group.
