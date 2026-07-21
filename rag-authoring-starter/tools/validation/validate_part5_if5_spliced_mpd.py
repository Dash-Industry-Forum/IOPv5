#!/usr/bin/env python3
"""Validate DASH-IF IOP v5 Part 5 Table 5 IF-5 spliced-output MPDs.

Initial F-0010-C1 structural validator for final IF-5 output after ad insertion.
It focuses on deterministic MPD structure checks from the restructured Table 5
matrix and intentionally leaves business-rule, playback, and segment-level
checks for later implementation.
"""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

CMAF_PROFILE = "urn:mpeg:dash:profile:cmaf:2019"
CMAF_EXTENDED_PROFILE = "urn:mpeg:dash:profile:cmaf-extended:2019"


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


def split_profiles(value: str | None) -> set[str]:
    if not value:
        return set()
    return {part.strip() for part in value.replace(",", " ").split() if part.strip()}


def parse_duration_seconds(value: str | None) -> float | None:
    """Parse a small useful subset of xs:duration used in fixtures."""
    if value is None:
        return None
    match = re.fullmatch(
        r"P(?:(?P<days>\d+(?:\.\d+)?)D)?(?:T(?:(?P<hours>\d+(?:\.\d+)?)H)?(?:(?P<minutes>\d+(?:\.\d+)?)M)?(?:(?P<seconds>\d+(?:\.\d+)?)S)?)?",
        value,
    )
    if not match:
        return None
    days = float(match.group("days") or 0)
    hours = float(match.group("hours") or 0)
    minutes = float(match.group("minutes") or 0)
    seconds = float(match.group("seconds") or 0)
    return days * 86400 + hours * 3600 + minutes * 60 + seconds


def period_role(period: ET.Element) -> str:
    role = attr(period, "data-if5-role")
    if role:
        return role.strip().lower()
    period_id = (attr(period, "id") or "").lower()
    if "slate" in period_id:
        return "slate"
    if "ad" in period_id:
        return "ad"
    return "main"


def validate_mpd(path: Path) -> list[Finding]:
    findings: list[Finding] = []

    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        return [Finding("ERROR", "MPD_XML_PARSE_ERROR", f"XML parse error: {exc}")]

    if local_name(root.tag) != "MPD":
        return [Finding("ERROR", "MPD_ROOT_NOT_MPD", "Root element is not MPD.")]

    profiles = split_profiles(attr(root, "profiles"))
    if CMAF_PROFILE not in profiles and CMAF_EXTENDED_PROFILE not in profiles:
        findings.append(
            Finding(
                "ERROR",
                "MPD_PROFILE_CMAF_OR_EXTENDED_MISSING",
                f"MPD@profiles shall include {CMAF_PROFILE} or {CMAF_EXTENDED_PROFILE}.",
            )
        )

    mpd_type = attr(root, "type")
    is_live_or_dynamic = mpd_type == "dynamic"

    minimum_update_period = attr(root, "minimumUpdatePeriod")
    if minimum_update_period is not None and parse_duration_seconds(minimum_update_period) is None:
        findings.append(
            Finding("ERROR", "MPD_MINIMUM_UPDATE_PERIOD_INVALID", "MPD@minimumUpdatePeriod shall be a valid duration.")
        )

    periods = children(root, "Period")
    if not periods:
        findings.append(Finding("ERROR", "MPD_PERIOD_MISSING", "At least one Period shall be present."))
        return findings

    ids: set[str] = set()
    starts: list[tuple[int, float | None]] = []
    roles = [period_role(period) for period in periods]

    for index, period in enumerate(periods, 1):
        role = roles[index - 1]
        period_id = attr(period, "id")
        start = attr(period, "start")
        duration = attr(period, "duration")
        start_seconds = parse_duration_seconds(start)
        starts.append((index, start_seconds))

        if start is None:
            findings.append(Finding("ERROR", "PERIOD_START_MISSING", f"Period[{index}]@start shall be present."))
        elif start_seconds is None:
            findings.append(Finding("ERROR", "PERIOD_START_INVALID", f"Period[{index}]@start shall be a valid duration."))

        if period_id is not None:
            if period_id in ids:
                findings.append(Finding("ERROR", "PERIOD_ID_DUPLICATE", f'Period[{index}]@id "{period_id}" is not unique.'))
            ids.add(period_id)

        if role in {"ad", "slate"}:
            if period_id is None:
                findings.append(Finding("ERROR", f"PERIOD_{role.upper()}_ID_MISSING", f"Inserted {role} Period[{index}]@id shall be present."))
            if not children(period, "BaseURL"):
                findings.append(Finding("ERROR", f"PERIOD_{role.upper()}_BASEURL_MISSING", f"Inserted {role} Period[{index}] shall contain BaseURL."))
            if is_live_or_dynamic and attr(period, "availabilityTimeOffset") is None:
                findings.append(
                    Finding(
                        "ERROR",
                        f"PERIOD_{role.upper()}_ATO_MISSING",
                        f"Inserted {role} Period[{index}]@availabilityTimeOffset shall be present for live/dynamic IF-5 output.",
                    )
                )
            if not children(period, "AdaptationSet"):
                findings.append(
                    Finding("ERROR", f"PERIOD_{role.upper()}_ADAPTATION_SET_MISSING", f"Inserted {role} Period[{index}] shall contain AdaptationSet.")
                )
            if duration is not None:
                findings.append(
                    Finding(
                        "WARNING",
                        f"PERIOD_{role.upper()}_DURATION_PRESENT",
                        f"Inserted {role} Period[{index}]@duration is typically removed.",
                    )
                )

        if role == "slate" and children(period, "EventStream"):
            findings.append(
                Finding("WARNING", "PERIOD_SLATE_EVENTSTREAM_PRESENT", f"Slate Period[{index}] is not expected to carry EventStream.")
            )

        if role == "main" and children(period, "AdaptationSet") == []:
            findings.append(Finding("ERROR", "PERIOD_MAIN_ADAPTATION_SET_MISSING", f"Main Period[{index}] shall contain AdaptationSet."))

    for previous, current in zip(starts, starts[1:]):
        previous_index, previous_start = previous
        current_index, current_start = current
        if previous_start is not None and current_start is not None and current_start < previous_start:
            findings.append(
                Finding(
                    "ERROR",
                    "PERIOD_START_NON_MONOTONIC",
                    f"Period[{current_index}]@start shall not be earlier than Period[{previous_index}]@start.",
                )
            )

    for index, role in enumerate(roles):
        if role in {"ad", "slate"}:
            if index > 0 and roles[index - 1] == "main" and attr(periods[index - 1], "duration") is not None:
                findings.append(
                    Finding(
                        "ERROR",
                        "PERIOD_MAIN_BEFORE_INSERTION_DURATION_PRESENT",
                        f"Main Period[{index}] before inserted {role} Period shall not carry @duration.",
                    )
                )
            if index + 1 < len(periods) and roles[index + 1] == "main" and attr(periods[index + 1], "duration") is not None:
                findings.append(
                    Finding(
                        "ERROR",
                        "PERIOD_MAIN_RETURN_DURATION_PRESENT",
                        f"Return main Period[{index + 2}] shall not carry @duration.",
                    )
                )

    for initialization_set in children(root, "InitializationSet"):
        if attr(initialization_set, "inAllPeriods") == "true":
            findings.append(
                Finding(
                    "WARNING",
                    "INITIALIZATION_SET_IN_ALL_PERIODS_REQUIRES_COMPATIBILITY_REVIEW",
                    "InitializationSet@inAllPeriods=true requires compatibility review across inserted ad/slate Periods.",
                )
            )

    return findings


def format_findings(path: Path, findings: Iterable[Finding]) -> str:
    lines = [f"{path}:"]
    for finding in findings:
        lines.append(f"  {finding.severity}: {finding.code}: {finding.message}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mpd", nargs="+", type=Path, help="IF-5 MPD file(s) to validate")
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