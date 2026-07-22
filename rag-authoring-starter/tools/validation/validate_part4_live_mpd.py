#!/usr/bin/env python3
"""Validate initial DASH-IF IOP v5 Part 4 Live/Low-Latency MPD signalling."""

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


def validate_number(value: str | None) -> bool:
    if value is None:
        return False
    try:
        return float(value) >= 0
    except ValueError:
        return False


def has_segment_timing(adaptation_set: ET.Element) -> bool:
    for template in descendants(adaptation_set, "SegmentTemplate"):
        if template.get("duration") or children(template, "SegmentTimeline"):
            return True
    return False


def validate_mpd(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        return [Finding("ERROR", "MPD_XML_PARSE_ERROR", f"XML parse error: {exc}")]

    if local_name(root.tag) != "MPD":
        return [Finding("ERROR", "MPD_ROOT_NOT_MPD", "Root element is not MPD.")]

    if root.get("type") != "dynamic":
        findings.append(Finding("ERROR", "P4_TYPE_NOT_DYNAMIC", "Live MPD@type shall be dynamic."))

    for required_attr in ("availabilityStartTime", "minimumUpdatePeriod", "timeShiftBufferDepth"):
        if not root.get(required_attr):
            findings.append(Finding("ERROR", "P4_LIVE_ATTRIBUTE_MISSING", f"Live MPD should provide @{required_attr}."))

    if not children(root, "UTCTiming"):
        findings.append(Finding("WARNING", "P4_UTC_TIMING_MISSING", "Live MPD should include UTCTiming or document an explicit waiver."))

    periods = children(root, "Period")
    if not periods:
        findings.append(Finding("ERROR", "P4_PERIOD_MISSING", "At least one Period shall be present."))

    adaptation_sets = descendants(root, "AdaptationSet")
    if not adaptation_sets:
        findings.append(Finding("ERROR", "P4_ADAPTATION_SET_MISSING", "At least one AdaptationSet shall be present."))

    for as_index, adaptation_set in enumerate(adaptation_sets, 1):
        label = f"AdaptationSet[{as_index}]"
        if not adaptation_set.get("mimeType") and not adaptation_set.get("contentType"):
            findings.append(Finding("ERROR", "P4_AS_TYPE_MISSING", f"{label} shall provide @mimeType or @contentType."))
        if not has_segment_timing(adaptation_set):
            findings.append(Finding("ERROR", "P4_SEGMENT_TIMING_MISSING", f"{label} shall provide live segment timing via SegmentTemplate duration or SegmentTimeline."))

        for template_index, template in enumerate(descendants(adaptation_set, "SegmentTemplate"), 1):
            template_label = f"{label}/SegmentTemplate[{template_index}]"
            ato = template.get("availabilityTimeOffset")
            if ato is not None and ato != "INF" and not validate_number(ato):
                findings.append(Finding("ERROR", "P4_AVAILABILITY_TIME_OFFSET_INVALID", f"{template_label}@availabilityTimeOffset shall be numeric or INF."))

    for service_description in children(root, "ServiceDescription"):
        latency = children(service_description, "Latency")
        if latency:
            target = latency[0].get("target")
            if target is not None and not validate_number(target):
                findings.append(Finding("ERROR", "P4_LATENCY_TARGET_INVALID", "ServiceDescription/Latency@target shall be numeric when present."))

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