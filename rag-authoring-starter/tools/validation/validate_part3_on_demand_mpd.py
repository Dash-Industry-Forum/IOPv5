#!/usr/bin/env python3
"""Validate initial DASH-IF IOP v5 Part 3 On-Demand MPD signalling."""

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


def has_segment_addressing(adaptation_set: ET.Element) -> bool:
    names = {"SegmentTemplate", "SegmentBase", "SegmentList"}
    return any(local_name(child.tag) in names for child in adaptation_set.iter())


def validate_mpd(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        return [Finding("ERROR", "MPD_XML_PARSE_ERROR", f"XML parse error: {exc}")]

    if local_name(root.tag) != "MPD":
        return [Finding("ERROR", "MPD_ROOT_NOT_MPD", "Root element is not MPD.")]

    mpd_type = root.get("type", "static")
    if mpd_type != "static":
        findings.append(Finding("ERROR", "P3_TYPE_NOT_STATIC", "On-Demand MPD@type shall be static or absent/static-compatible."))

    for live_attr in ("availabilityStartTime", "minimumUpdatePeriod", "timeShiftBufferDepth"):
        if root.get(live_attr) is not None:
            findings.append(Finding("ERROR", "P3_DYNAMIC_ATTRIBUTE_PRESENT", f"On-Demand MPD shall not use live-only @{live_attr}."))

    if not root.get("mediaPresentationDuration"):
        findings.append(Finding("ERROR", "P3_DURATION_MISSING", "On-Demand MPD should provide mediaPresentationDuration."))

    periods = children(root, "Period")
    if not periods:
        findings.append(Finding("ERROR", "P3_PERIOD_MISSING", "At least one Period shall be present."))
    for index, period in enumerate(periods, 1):
        if not period.get("duration") and not root.get("mediaPresentationDuration"):
            findings.append(Finding("ERROR", "P3_PERIOD_DURATION_MISSING", f"Period[{index}] duration is missing and MPD duration is unavailable."))

    adaptation_sets = descendants(root, "AdaptationSet")
    if not adaptation_sets:
        findings.append(Finding("ERROR", "P3_ADAPTATION_SET_MISSING", "At least one AdaptationSet shall be present."))

    for as_index, adaptation_set in enumerate(adaptation_sets, 1):
        label = f"AdaptationSet[{as_index}]"
        if not adaptation_set.get("mimeType") and not adaptation_set.get("contentType"):
            findings.append(Finding("ERROR", "P3_AS_TYPE_MISSING", f"{label} shall provide @mimeType or @contentType."))
        if not has_segment_addressing(adaptation_set):
            findings.append(Finding("ERROR", "P3_SEGMENT_ADDRESSING_MISSING", f"{label} shall provide on-demand segment addressing."))
        if not children(adaptation_set, "Representation"):
            findings.append(Finding("ERROR", "P3_REPRESENTATION_MISSING", f"{label} shall contain at least one Representation."))

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