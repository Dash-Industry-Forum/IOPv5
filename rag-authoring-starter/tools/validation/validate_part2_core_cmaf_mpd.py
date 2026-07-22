#!/usr/bin/env python3
"""Validate initial DASH-IF IOP v5 Part 2 Core CMAF MPD signalling."""

from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    message: str


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1] if "}" in tag else tag


def children(element: ET.Element, name: str) -> list[ET.Element]:
    return [child for child in list(element) if local_name(child.tag) == name]


def descendants(element: ET.Element, name: str) -> list[ET.Element]:
    return [child for child in element.iter() if local_name(child.tag) == name]


def validate_positive_int(value: str | None) -> bool:
    if value is None:
        return False
    try:
        return int(value) > 0
    except ValueError:
        return False


def validate_mpd(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        return [Finding("ERROR", "MPD_XML_PARSE_ERROR", f"XML parse error: {exc}")]

    if local_name(root.tag) != "MPD":
        return [Finding("ERROR", "MPD_ROOT_NOT_MPD", "Root element is not MPD.")]

    profiles = root.get("profiles")
    if not profiles:
        findings.append(Finding("ERROR", "P2_PROFILES_MISSING", "MPD@profiles shall be present for the Core CMAF baseline."))
    elif "dash" not in profiles.lower() and "cmaf" not in profiles.lower():
        findings.append(Finding("WARNING", "P2_PROFILES_UNRECOGNIZED", "MPD@profiles does not include a recognizable DASH/CMAF profile token."))

    periods = children(root, "Period")
    if not periods:
        findings.append(Finding("ERROR", "P2_PERIOD_MISSING", "At least one Period shall be present."))

    adaptation_sets = descendants(root, "AdaptationSet")
    if not adaptation_sets:
        findings.append(Finding("ERROR", "P2_ADAPTATION_SET_MISSING", "At least one AdaptationSet shall be present."))

    for as_index, adaptation_set in enumerate(adaptation_sets, 1):
        label = f"AdaptationSet[{as_index}]"
        if not adaptation_set.get("mimeType") and not adaptation_set.get("contentType"):
            findings.append(Finding("ERROR", "P2_AS_TYPE_MISSING", f"{label} shall provide @mimeType or @contentType."))

        representations = children(adaptation_set, "Representation")
        if not representations:
            findings.append(Finding("ERROR", "P2_REPRESENTATION_MISSING", f"{label} shall contain at least one Representation."))

        for rep_index, representation in enumerate(representations, 1):
            rep_label = f"{label}/Representation[{rep_index}]"
            if not representation.get("codecs") and not adaptation_set.get("codecs"):
                findings.append(Finding("ERROR", "P2_CODECS_MISSING", f"{rep_label} shall provide codec signalling."))
            if not validate_positive_int(representation.get("bandwidth")):
                findings.append(Finding("ERROR", "P2_BANDWIDTH_INVALID", f"{rep_label}@bandwidth shall be a positive integer."))

        segment_templates = children(adaptation_set, "SegmentTemplate")
        segment_bases = children(adaptation_set, "SegmentBase")
        if not segment_templates and not segment_bases:
            findings.append(Finding("WARNING", "P2_SEGMENT_ADDRESSING_MISSING", f"{label} should provide SegmentTemplate or SegmentBase in the MPD-only baseline."))

        for template_index, segment_template in enumerate(segment_templates, 1):
            template_label = f"{label}/SegmentTemplate[{template_index}]"
            if segment_template.get("timescale") is not None and not validate_positive_int(segment_template.get("timescale")):
                findings.append(Finding("ERROR", "P2_SEGMENT_TIMESCALE_INVALID", f"{template_label}@timescale shall be a positive integer."))
            if segment_template.get("duration") is not None and not validate_positive_int(segment_template.get("duration")):
                findings.append(Finding("ERROR", "P2_SEGMENT_DURATION_INVALID", f"{template_label}@duration shall be a positive integer."))
            if segment_template.get("startNumber") is not None and not validate_positive_int(segment_template.get("startNumber")):
                findings.append(Finding("ERROR", "P2_SEGMENT_START_NUMBER_INVALID", f"{template_label}@startNumber shall be a positive integer."))
            if not segment_template.get("media"):
                findings.append(Finding("WARNING", "P2_SEGMENT_MEDIA_MISSING", f"{template_label}@media should be present for template addressing."))

    return findings


def format_findings(path: Path, findings: Iterable[Finding]) -> str:
    lines = [f"{path}:"]
    lines.extend(f"  {finding.severity}: {finding.code}: {finding.message}" for finding in findings)
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mpd", nargs="+", type=Path)
    parser.add_argument("--warnings-as-errors", action="store_true")
    args = parser.parse_args(argv)

    exit_code = 0
    for mpd in args.mpd:
        findings = validate_mpd(mpd)
        if findings:
            print(format_findings(mpd, findings))
        else:
            print(f"{mpd}: OK")
        if any(f.severity == "ERROR" for f in findings) or (args.warnings_as_errors and findings):
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main())