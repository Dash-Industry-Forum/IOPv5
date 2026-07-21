#!/usr/bin/env python3
"""Validate DASH-IF IOP v5 Part 5 Table 4 DASH-IF ad content MPDs.

This is the initial F-0010-B1 structural validator. It intentionally focuses on
deterministic MPD-level checks from Part 5 Table 4 and does not attempt media
segment validation.
"""

from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

DASH_NS = "urn:mpeg:dash:schema:mpd:2011"
XLINK_NS = "http://www.w3.org/1999/xlink"

CMAF_PROFILE = "urn:mpeg:dash:profile:cmaf:2019"
DASHIF_AD_CONTENT_PROFILE = "http://dashif.org/guidelines/dashif-ad-content"


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    message: str


def local_name(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[1]
    return tag


def attr(element: ET.Element, name: str, namespace: str | None = None) -> str | None:
    if namespace:
        return element.get(f"{{{namespace}}}{name}")
    return element.get(name)


def children(element: ET.Element, name: str) -> list[ET.Element]:
    return [child for child in list(element) if local_name(child.tag) == name]


def descendants(element: ET.Element, name: str) -> list[ET.Element]:
    return [child for child in element.iter() if local_name(child.tag) == name]


def split_profiles(value: str | None) -> set[str]:
    if not value:
        return set()
    return {part.strip() for part in value.replace(",", " ").split() if part.strip()}


def has_segment_base_attr(adaptation_set: ET.Element, attribute_name: str) -> bool:
    for segment_base_name in ("SegmentBase", "SegmentTemplate", "SegmentList"):
        for segment_element in children(adaptation_set, segment_base_name):
            if attr(segment_element, attribute_name) is not None:
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

    profiles = split_profiles(attr(root, "profiles"))
    if CMAF_PROFILE not in profiles:
        findings.append(
            Finding("ERROR", "MPD_PROFILE_CMAF_MISSING", f"MPD@profiles shall include {CMAF_PROFILE}.")
        )
    if DASHIF_AD_CONTENT_PROFILE not in profiles:
        findings.append(
            Finding(
                "WARNING",
                "MPD_PROFILE_DASHIF_AD_CONTENT_MISSING",
                f"MPD@profiles should include {DASHIF_AD_CONTENT_PROFILE}.",
            )
        )

    if attr(root, "type") != "static":
        findings.append(Finding("ERROR", "MPD_TYPE_NOT_STATIC", 'MPD@type shall be set to "static".'))

    for forbidden in (
        "mediaPresentationDuration",
        "minimumUpdatePeriod",
        "timeShiftBufferDepth",
        "suggestedPresentationDelay",
        "maxSegmentDuration",
        "maxSubsegmentDuration",
    ):
        if attr(root, forbidden) is not None:
            findings.append(Finding("ERROR", f"MPD_{forbidden}_PRESENT", f"MPD@{forbidden} shall not be present."))

    if attr(root, "minBufferTime") is None:
        findings.append(Finding("ERROR", "MPD_MIN_BUFFER_TIME_MISSING", "MPD@minBufferTime shall be present."))

    if children(root, "BaseURL"):
        findings.append(Finding("ERROR", "MPD_BASEURL_PRESENT", "MPD-level BaseURL shall not be present."))

    periods = children(root, "Period")
    if len(periods) != 1:
        findings.append(Finding("ERROR", "MPD_PERIOD_COUNT", "Exactly one Period shall be present."))
        return findings

    period = periods[0]
    if attr(period, "href", XLINK_NS) is not None:
        findings.append(Finding("ERROR", "PERIOD_XLINK_HREF_PRESENT", "Period@xlink:href shall be absent."))
    if attr(period, "actuate", XLINK_NS) is not None:
        findings.append(Finding("ERROR", "PERIOD_XLINK_ACTUATE_PRESENT", "Period@xlink:actuate shall be absent."))
    if attr(period, "start") is not None:
        findings.append(Finding("ERROR", "PERIOD_START_PRESENT", "Period@start shall be absent."))
    if attr(period, "duration") is None:
        findings.append(Finding("ERROR", "PERIOD_DURATION_MISSING", "Period@duration shall be present."))

    if not children(period, "BaseURL"):
        findings.append(Finding("ERROR", "PERIOD_BASEURL_MISSING", "At least one Period-level BaseURL shall be present."))

    asset_identifiers = children(period, "AssetIdentifier")
    if len(asset_identifiers) == 0:
        findings.append(Finding("WARNING", "PERIOD_ASSET_IDENTIFIER_MISSING", "Period AssetIdentifier should be present."))
    elif len(asset_identifiers) > 1:
        findings.append(Finding("ERROR", "PERIOD_ASSET_IDENTIFIER_MULTIPLE", "At most one Period AssetIdentifier is allowed."))

    adaptation_sets = children(period, "AdaptationSet")
    if not adaptation_sets:
        findings.append(Finding("ERROR", "PERIOD_ADAPTATION_SET_MISSING", "At least one AdaptationSet shall be present."))

    if children(period, "EmptyAdaptationSet"):
        findings.append(Finding("ERROR", "PERIOD_EMPTY_ADAPTATION_SET_PRESENT", "EmptyAdaptationSet shall be absent."))

    for index, adaptation_set in enumerate(adaptation_sets, 1):
        prefix = f"AdaptationSet[{index}]"

        if attr(adaptation_set, "href", XLINK_NS) is not None:
            findings.append(Finding("ERROR", "ADAPTATION_SET_XLINK_HREF_PRESENT", f"{prefix}@xlink:href shall be absent."))
        if attr(adaptation_set, "actuate", XLINK_NS) is not None:
            findings.append(
                Finding("ERROR", "ADAPTATION_SET_XLINK_ACTUATE_PRESENT", f"{prefix}@xlink:actuate shall be absent.")
            )

        if has_segment_base_attr(adaptation_set, "presentationTimeOffset"):
            findings.append(
                Finding(
                    "ERROR",
                    "ADAPTATION_SET_PTO_PRESENT",
                    f"{prefix} SegmentBase@presentationTimeOffset shall be absent.",
                )
            )
        if has_segment_base_attr(adaptation_set, "eptDelta"):
            findings.append(
                Finding("ERROR", "ADAPTATION_SET_EPT_DELTA_PRESENT", f"{prefix} SegmentBase@eptDelta shall be absent.")
            )

        for segment_base_name in ("SegmentBase", "SegmentTemplate", "SegmentList"):
            for segment_element in children(adaptation_set, segment_base_name):
                pd_delta = attr(segment_element, "pdDelta")
                if pd_delta is not None:
                    try:
                        if float(pd_delta) < 0:
                            findings.append(
                                Finding(
                                    "ERROR",
                                    "ADAPTATION_SET_PD_DELTA_NEGATIVE",
                                    f"{prefix} SegmentBase@pdDelta shall be non-negative.",
                                )
                            )
                    except ValueError:
                        findings.append(
                            Finding(
                                "ERROR",
                                "ADAPTATION_SET_PD_DELTA_INVALID",
                                f"{prefix} SegmentBase@pdDelta shall be numeric when present.",
                            )
                        )

        if attr(adaptation_set, "contentType") is None:
            findings.append(Finding("ERROR", "ADAPTATION_SET_CONTENT_TYPE_MISSING", f"{prefix}@contentType shall be present."))

        if children(adaptation_set, "SegmentList"):
            findings.append(Finding("ERROR", "ADAPTATION_SET_SEGMENT_LIST_PRESENT", f"{prefix} SegmentList shall be absent."))

        if not children(adaptation_set, "Representation"):
            findings.append(
                Finding("ERROR", "ADAPTATION_SET_REPRESENTATION_MISSING", f"{prefix} shall contain at least one Representation.")
            )

    if children(root, "UTCTiming"):
        findings.append(Finding("ERROR", "MPD_UTC_TIMING_PRESENT", "UTCTiming shall not be present."))

    if children(root, "LeapSecondInformation"):
        findings.append(Finding("ERROR", "MPD_LEAP_SECOND_INFORMATION_PRESENT", "LeapSecondInformation shall not be present."))

    return findings


def format_findings(path: Path, findings: Iterable[Finding]) -> str:
    lines = [f"{path}:"]
    for finding in findings:
        lines.append(f"  {finding.severity}: {finding.code}: {finding.message}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mpd", nargs="+", type=Path, help="MPD file(s) to validate")
    parser.add_argument("--warnings-as-errors", action="store_true", help="Return non-zero on warnings")
    args = parser.parse_args(argv)

    exit_code = 0
    for mpd_path in args.mpd:
        findings = validate_mpd(mpd_path)
        errors = [finding for finding in findings if finding.severity == "ERROR"]
        warnings = [finding for finding in findings if finding.severity == "WARNING"]

        if findings:
            print(format_findings(mpd_path, findings))
        else:
            print(f"{mpd_path}: OK")

        if errors or (args.warnings_as_errors and warnings):
            exit_code = 1

    return exit_code


if __name__ == "__main__":
    sys.exit(main())