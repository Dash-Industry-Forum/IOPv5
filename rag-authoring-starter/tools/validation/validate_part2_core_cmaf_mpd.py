#!/usr/bin/env python3
"""Validate DASH-IF IOP v5 Part 2 Core CMAF MPD signalling.

Covers the 10 timing-model checks defined in the Part 12 conformance mapping
(v0.4) plus the original structural checks:

  P2_PROFILES_MISSING / P2_PROFILES_UNRECOGNIZED
  P2_PERIOD_MISSING
  P2_PERIOD_ZERO_DURATION
  P2_STATIC_FIRST_PERIOD_START
  P2_STATIC_LAST_PERIOD_DURATION
  P2_ADAPTATION_SET_MISSING
  P2_AS_TYPE_MISSING
  P2_REPRESENTATION_MISSING
  P2_CODECS_MISSING
  P2_BANDWIDTH_INVALID
  P2_SEGMENT_ADDRESSING_MISSING
  P2_TIMESCALE_MISSING
  P2_TIMESCALE_EXCEEDS_JS_MAX
  P2_SEGMENT_TIMESCALE_INVALID
  P2_SEGMENT_DURATION_INVALID
  P2_SEGMENT_START_NUMBER_INVALID
  P2_SEGMENT_MEDIA_MISSING
  P2_UTCTIMING_MISSING_DYNAMIC
  P2_UTCTIMING_SCHEME_INVALID
  P2_DYNAMIC_PUBLISHTIME_MISSING
  P2_DYNAMIC_TIMESHIFT_DELAY_CONFLICT
  P2_PERIOD_CONNECTIVITY_CONFLICT
  P2_FORBIDDEN_PRESENTATION_DURATION
  P2_FORBIDDEN_AVAILABILITY_TIME_COMPLETE
  P2_STANDALONE_TEXT_PTO_PRESENT
  P2_XSDURATION_YEAR_MONTH
"""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

# ECMAScript safe integer limit (2^53 - 1)
JS_MAX_SAFE_INT = 9007199254740991

# Permitted UTCTiming schemes per Part 2 / Part 4
PERMITTED_UTC_SCHEMES = {
    "urn:mpeg:dash:utc:http-xsdate:2014",
    "urn:mpeg:dash:utc:http-iso:2014",
    "urn:mpeg:dash:utc:http-head:2014",
    "urn:mpeg:dash:utc:direct:2014",
}

# Period connectivity / continuity scheme URIs
PERIOD_CONNECTIVITY_SCHEME = "urn:mpeg:dash:period-connectivity:2015"
PERIOD_CONTINUITY_SCHEME = "urn:mpeg:dash:period-continuity:2015"

# xs:duration year/month pattern (Y or M before T)
_XS_DURATION_YEAR_MONTH_RE = re.compile(r"P(?:\d+Y|\d+M)")


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


def parse_duration_seconds(value: str | None) -> float | None:
    """Parse xs:duration to seconds (approximate, ignores Y/M)."""
    if not value:
        return None
    m = re.match(
        r"^-?P(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)D)?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:([\d.]+)S)?)?$",
        value,
    )
    if not m:
        return None
    days = int(m.group(3) or 0)
    hours = int(m.group(4) or 0)
    minutes = int(m.group(5) or 0)
    seconds = float(m.group(6) or 0)
    return days * 86400 + hours * 3600 + minutes * 60 + seconds


def has_year_or_month(duration: str | None) -> bool:
    """Return True if xs:duration uses year or month units."""
    if not duration:
        return False
    return bool(_XS_DURATION_YEAR_MONTH_RE.search(duration))


def validate_mpd(path: Path) -> list[Finding]:  # noqa: C901
    findings: list[Finding] = []
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        return [Finding("ERROR", "MPD_XML_PARSE_ERROR", f"XML parse error: {exc}")]

    if local_name(root.tag) != "MPD":
        return [Finding("ERROR", "MPD_ROOT_NOT_MPD", "Root element is not MPD.")]

    mpd_type = root.get("type", "static")
    is_dynamic = mpd_type == "dynamic"

    # ── Forbidden attributes ──────────────────────────────────────────────────
    if root.get("presentationDuration") is not None:
        findings.append(Finding(
            "ERROR", "P2_FORBIDDEN_PRESENTATION_DURATION",
            "MPD@presentationDuration shall not be used (forbidden technique)."))

    for elem in root.iter():
        if elem.get("availabilityTimeComplete") is not None:
            findings.append(Finding(
                "ERROR", "P2_FORBIDDEN_AVAILABILITY_TIME_COMPLETE",
                f"{local_name(elem.tag)}: @availabilityTimeComplete shall not be used (forbidden technique)."))
            break

    # ── xs:duration year/month check ─────────────────────────────────────────
    duration_attrs = [
        "mediaPresentationDuration", "minimumUpdatePeriod",
        "timeShiftBufferDepth", "suggestedPresentationDelay",
        "maxSegmentDuration", "maxSubsegmentDuration",
    ]
    for attr in duration_attrs:
        val = root.get(attr)
        if has_year_or_month(val):
            findings.append(Finding(
                "ERROR", "P2_XSDURATION_YEAR_MONTH",
                f"MPD@{attr}='{val}' uses year or month units; xs:duration fields shall use seconds."))

    # ── Profiles ──────────────────────────────────────────────────────────────
    profiles = root.get("profiles")
    if not profiles:
        findings.append(Finding(
            "ERROR", "P2_PROFILES_MISSING",
            "MPD@profiles shall be present for the Core CMAF baseline."))
    elif "dash" not in profiles.lower() and "cmaf" not in profiles.lower():
        findings.append(Finding(
            "WARNING", "P2_PROFILES_UNRECOGNIZED",
            "MPD@profiles does not include a recognizable DASH/CMAF profile token."))

    # ── Dynamic-only checks ───────────────────────────────────────────────────
    if is_dynamic:
        # publishTime
        if not root.get("publishTime"):
            findings.append(Finding(
                "ERROR", "P2_DYNAMIC_PUBLISHTIME_MISSING",
                "MPD@publishTime shall be present in dynamic presentations."))

        # UTCTiming
        utc_timings = children(root, "UTCTiming")
        if not utc_timings:
            findings.append(Finding(
                "ERROR", "P2_UTCTIMING_MISSING_DYNAMIC",
                "Dynamic presentations shall include at least one UTCTiming element."))
        else:
            for utc in utc_timings:
                scheme = utc.get("schemeIdUri", "")
                if scheme and scheme not in PERMITTED_UTC_SCHEMES:
                    findings.append(Finding(
                        "ERROR", "P2_UTCTIMING_SCHEME_INVALID",
                        f"UTCTiming@schemeIdUri='{scheme}' is not a permitted scheme. "
                        f"Permitted: {sorted(PERMITTED_UTC_SCHEMES)}."))

        # suggestedPresentationDelay vs timeShiftBufferDepth
        spd = parse_duration_seconds(root.get("suggestedPresentationDelay"))
        tsb = parse_duration_seconds(root.get("timeShiftBufferDepth"))
        if spd is not None and tsb is not None and spd >= tsb:
            findings.append(Finding(
                "WARNING", "P2_DYNAMIC_TIMESHIFT_DELAY_CONFLICT",
                f"MPD@suggestedPresentationDelay ({spd}s) >= MPD@timeShiftBufferDepth ({tsb}s); "
                "this results in a zero or negative effective time shift buffer."))

    # ── Periods ───────────────────────────────────────────────────────────────
    periods = children(root, "Period")
    if not periods:
        findings.append(Finding("ERROR", "P2_PERIOD_MISSING", "At least one Period shall be present."))
        return findings

    for p_idx, period in enumerate(periods, 1):
        p_label = f"Period[{p_idx}]"
        dur = period.get("duration")
        if dur is not None:
            secs = parse_duration_seconds(dur)
            if secs is not None and secs == 0:
                findings.append(Finding(
                    "ERROR", "P2_PERIOD_ZERO_DURATION",
                    f"{p_label}@duration is zero; Periods shall not have zero duration."))
            if has_year_or_month(dur):
                findings.append(Finding(
                    "ERROR", "P2_XSDURATION_YEAR_MONTH",
                    f"{p_label}@duration='{dur}' uses year or month units."))

    # Static: first period start=0, last period has duration
    if not is_dynamic:
        first_start = periods[0].get("start", "PT0S")
        first_secs = parse_duration_seconds(first_start)
        if first_secs is not None and first_secs != 0:
            findings.append(Finding(
                "ERROR", "P2_STATIC_FIRST_PERIOD_START",
                f"In a static presentation, the first Period shall start at 0 "
                f"(Period[1]@start='{first_start}')."))
        if not periods[-1].get("duration"):
            findings.append(Finding(
                "ERROR", "P2_STATIC_LAST_PERIOD_DURATION",
                "In a static presentation, the last Period shall have @duration."))

    # ── Period connectivity / continuity conflict ─────────────────────────────
    for p_idx, period in enumerate(periods, 1):
        p_label = f"Period[{p_idx}]"
        for as_elem in descendants(period, "AdaptationSet"):
            as_id = as_elem.get("id", "?")
            as_label = f"{p_label}/AdaptationSet[@id='{as_id}']"
            sup_props = descendants(as_elem, "SupplementalProperty")
            schemes_here = {sp.get("schemeIdUri", "") for sp in sup_props}
            if PERIOD_CONNECTIVITY_SCHEME in schemes_here and PERIOD_CONTINUITY_SCHEME in schemes_here:
                findings.append(Finding(
                    "ERROR", "P2_PERIOD_CONNECTIVITY_CONFLICT",
                    f"{as_label}: period-connectivity and period-continuity descriptors "
                    "shall not both be present on the same AdaptationSet."))

    # ── AdaptationSets ────────────────────────────────────────────────────────
    adaptation_sets = descendants(root, "AdaptationSet")
    if not adaptation_sets:
        findings.append(Finding("ERROR", "P2_ADAPTATION_SET_MISSING", "At least one AdaptationSet shall be present."))

    for as_index, adaptation_set in enumerate(adaptation_sets, 1):
        label = f"AdaptationSet[{as_index}]"
        mime = adaptation_set.get("mimeType", "")
        if not mime and not adaptation_set.get("contentType"):
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

        # Stand-alone text track: @presentationTimeOffset shall not be present
        is_text = "ttml" in mime or "webvtt" in mime or "vtt" in mime or "wvtt" in mime
        if is_text:
            seg_bases = descendants(adaptation_set, "SegmentBase")
            seg_templates = descendants(adaptation_set, "SegmentTemplate")
            all_seg = seg_bases + seg_templates
            # If no segmentation (stand-alone file), check for PTO
            if not all_seg:
                for rep in representations:
                    if rep.get("presentationTimeOffset") is not None:
                        findings.append(Finding(
                            "ERROR", "P2_STANDALONE_TEXT_PTO_PRESENT",
                            f"{label}/Representation[@id='{rep.get('id', '?')}']: "
                            "@presentationTimeOffset shall not be present on stand-alone text Representations."))

        segment_templates = children(adaptation_set, "SegmentTemplate")
        segment_bases = children(adaptation_set, "SegmentBase")
        if not segment_templates and not segment_bases:
            findings.append(Finding(
                "WARNING", "P2_SEGMENT_ADDRESSING_MISSING",
                f"{label} should provide SegmentTemplate or SegmentBase."))

        for template_index, segment_template in enumerate(segment_templates, 1):
            template_label = f"{label}/SegmentTemplate[{template_index}]"

            # @timescale shall be present
            timescale_str = segment_template.get("timescale")
            if timescale_str is None:
                findings.append(Finding(
                    "ERROR", "P2_TIMESCALE_MISSING",
                    f"{template_label}@timescale shall be present (default of 1 is not interoperable)."))
            else:
                if not validate_positive_int(timescale_str):
                    findings.append(Finding(
                        "ERROR", "P2_SEGMENT_TIMESCALE_INVALID",
                        f"{template_label}@timescale shall be a positive integer."))
                else:
                    ts_val = int(timescale_str)
                    if ts_val > JS_MAX_SAFE_INT:
                        findings.append(Finding(
                            "ERROR", "P2_TIMESCALE_EXCEEDS_JS_MAX",
                            f"{template_label}@timescale={ts_val} exceeds 2^53-1 ({JS_MAX_SAFE_INT}); "
                            "ECMAScript cannot represent this accurately."))

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