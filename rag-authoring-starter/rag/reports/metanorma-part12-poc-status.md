# Metanorma Part 12 proof-of-concept status

## Goal

Evaluate whether the canonical Bikeshed/Markdown Part 12 source can be converted
to AsciiDoc and compiled through Metanorma.

## Work completed

- Added experimental converter:
  - `tools/metanorma/bikeshed_to_adoc.py`
- Generated local AsciiDoc for Part 12 under `authoring/metanorma/generated/`.
  This directory is gitignored because generated AsciiDoc is derived output.
- Tested Metanorma Generic using the locally installed winget `metanorma` binary.

## Current result

The converter can generate a readable Part 12 AsciiDoc file from the canonical
Bikeshed source. Metanorma Generic reports `Syntax Valid!` and produces semantic
XML and presentation XML locally.

However, in the current Windows/winget runtime, rendering Generic HTML/DOC fails
locally after XML generation because the packaged runtime cannot load
`sassc-embedded` during CSS generation. Generic also reports that PDF is not
supported for the Generic flavour in this installed package.

Observed outputs from local experiments:

- semantic XML: produced
- presentation XML: produced when `presentation` extension is requested
- Generic HTML/DOC: blocked locally by `sassc-embedded` runtime/package issue
- Generic PDF: unsupported by the Generic flavour

## Interpretation

The source-conversion part of the approach is viable for Part 12, but local
Metanorma rendering is not yet a complete success. This looks like a tooling/runtime
issue rather than a fundamental source-structure issue.

## Recommended next steps

1. Test the same generated AsciiDoc in a Linux CI environment or a full Ruby/gem
   environment where `sassc-embedded` is available.
2. Test the ISO flavour for PDF generation, noting that ISO may require additional
   metadata and may not match DASH-IF boilerplate without customization.
3. Decide whether generated AsciiDoc should remain CI-only or be committed as
   review artifacts. Current recommendation: keep generated AsciiDoc and outputs
   uncommitted.
4. If DOC/PDF generation becomes a requirement, scope a DASH-IF Metanorma flavour
   or a post-processing style layer.
