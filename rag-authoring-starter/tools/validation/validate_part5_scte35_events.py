#!/usr/bin/env python3
"""Validate DASH-IF IOP v5 Part 5 IF-3 SCTE-35 MPD EventStreams.

Initial F-0010-A1 validator. It performs MPD-level checks only:
allowed SCTE-35 EventStream schemes, Event timing syntax, duplicate Event IDs,
xml+bin Binary presence, Base64 validity, and basic Period bounds.
"""

from __future__ import annotations

import argparse
import base64
import binascii
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

SCTE35_2013_XML = "urn:scte:scte35:2013:xml"
SCTE35_2014_XML_BIN = "urn:scte:scte35:2014:xml+bin"
ALLOWED_SCTE35_SCHEMES = {SCTE35_2013_XML, SCTE35_2014_XML_BIN}


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    message: str


def local_name(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[1]
    return tag


def attr(element: ET.Element, name: str) -> str | None:
    return element.get(name)


def children(element: ET.Element, name: str) -> list[ET.Element]:
    return [child for child in list(element) if local_name(child.tag) == name]


def descendants(element: ET.Element, name: str) -> list[ET.Element]:
    return [child for child in element.iter() if local_name(child.tag) == name]


def parse_non_negative_number(value: str | None) -> float | None:
    if value is None:
        return None
    try:
        parsed = float(value)
    except ValueError:
        return None
    if parsed < 0:
        return None
    return parsed


def event_payload_text(event: ET.Element) -> str:
    return "".join(event.itertext()).strip()


def find_binary(event: ET.Element) -> ET.Element | None:
    for element in descendants(event, "Binary"):
        return element
    return None


def decode_binary_payload(binary_text: str) -> bytes | None:
    normalized = "".join(binary_text.split())
    if not normalized:
        return None
    try:
        return base64.b64decode(normalized, validate=True)
    except (binascii.Error, ValueError):
        return None


def validate_binary_base64(binary_text: str) -> bool:
    return decode_binary_payload(binary_text) is not None


@dataclass(frozen=True)
class Scte35PayloadInfo:
    command_type: int
    command_name: str
    command_length: int | None
    has_splice_time: bool = False
    has_break_duration: bool = False
    out_of_network_indicator: bool | None = None
    segmentation_descriptor_count: int = 0


def bits_from_bytes(data: bytes) -> str:
    return "".join(f"{byte:08b}" for byte in data)


def bits_to_int(bits: str, start: int, length: int) -> int | None:
    end = start + length
    if end > len(bits):
        return None
    return int(bits[start:end], 2)


def parse_scte35_payload_info(payload: bytes) -> Scte35PayloadInfo | None:
    """Parse a minimal SCTE-35 splice_info_section payload summary.

    The parser intentionally extracts only deterministic fields needed by the
    Part 5 F-0010-A2 validator-start work: command type, command length,
    splice_insert out_of_network/break_duration hints, time_signal splice_time
    presence, and segmentation_descriptor count in the descriptor loop.
    """
    if len(payload) < 14 or payload[0] != 0xFC:
        return None

    command_length = payload[12] & 0x0F
    command_type = payload[13]

    command_start_byte = 14
    command_end_byte = command_start_byte + command_length
    command_bits = bits_from_bytes(payload[command_start_byte:command_end_byte]) if command_end_byte <= len(payload) else ""

    has_splice_time = False
    has_break_duration = False
    out_of_network_indicator: bool | None = None

    if command_type == 0x06 and len(command_bits) >= 1:
        time_specified_flag = bits_to_int(command_bits, 0, 1)
        has_splice_time = time_specified_flag == 1
    elif command_type == 0x05 and len(command_bits) >= 40:
        out_of_network_indicator = bits_to_int(command_bits, 32, 1) == 1
        duration_flag = bits_to_int(command_bits, 38, 1)
        has_break_duration = duration_flag == 1

    descriptor_count = 0
    descriptor_loop_length_offset = command_end_byte + 2
    descriptor_bytes = payload[descriptor_loop_length_offset:] if descriptor_loop_length_offset < len(payload) else b""
    descriptor_bits = bits_from_bytes(descriptor_bytes)
    descriptor_loop_length = bits_to_int(descriptor_bits, 0, 16)
    descriptor_start = 16
    descriptor_end = descriptor_start + ((descriptor_loop_length or 0) * 8)
    cursor = descriptor_start
    while descriptor_loop_length is not None and cursor + 16 <= min(descriptor_end, len(descriptor_bits)):
        descriptor_tag = bits_to_int(descriptor_bits, cursor, 8)
        descriptor_length = bits_to_int(descriptor_bits, cursor + 8, 8)
        if descriptor_tag is None or descriptor_length is None:
            break
        descriptor_payload_start = cursor + 16
        if descriptor_payload_start + descriptor_length * 8 > len(descriptor_bits):
            break
        if descriptor_tag == 0x02:
            descriptor_count += 1
        cursor = descriptor_payload_start + descriptor_length * 8

    return Scte35PayloadInfo(
        command_type=command_type,
        command_name=scte35_command_name(command_type),
        command_length=command_length,
        has_splice_time=has_splice_time,
        has_break_duration=has_break_duration,
        out_of_network_indicator=out_of_network_indicator,
        segmentation_descriptor_count=descriptor_count,
    )


def parse_scte35_command_type(payload: bytes) -> int | None:
    info = parse_scte35_payload_info(payload)
    return info.command_type if info else None


def scte35_command_name(command_type: int) -> str:
    return {
        0x00: "splice_null",
        0x04: "splice_schedule",
        0x05: "splice_insert",
        0x06: "time_signal",
        0x07: "bandwidth_reservation",
        0xFF: "private_command",
    }.get(command_type, f"unknown_{command_type}")


def is_scte35_like_scheme(scheme: str | None) -> bool:
    if not scheme:
        return False
    return "scte35" in scheme.lower() or "scte-35" in scheme.lower() or scheme.startswith("urn:scte:")


def period_bounds(period: ET.Element) -> tuple[float | None, float | None]:
    start = parse_non_negative_number(attr(period, "start"))
    duration = parse_non_negative_number(attr(period, "duration"))
    if start is None:
        start = 0
    end = start + duration if duration is not None else None
    return start, end


def validate_mpd(path: Path) -> list[Finding]:
    findings: list[Finding] = []

    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        return [Finding("ERROR", "MPD_XML_PARSE_ERROR", f"XML parse error: {exc}")]

    if local_name(root.tag) != "MPD":
        return [Finding("ERROR", "MPD_ROOT_NOT_MPD", "Root element is not MPD.")]

    scte35_stream_count = 0

    for period_index, period in enumerate(children(root, "Period"), 1):
        period_start, period_end = period_bounds(period)

        for stream_index, event_stream in enumerate(children(period, "EventStream"), 1):
            scheme = attr(event_stream, "schemeIdUri")
            if not is_scte35_like_scheme(scheme):
                continue

            scte35_stream_count += 1
            stream_label = f"Period[{period_index}]/EventStream[{stream_index}]"

            if scheme not in ALLOWED_SCTE35_SCHEMES:
                findings.append(
                    Finding(
                        "ERROR",
                        "SCTE35_SCHEME_UNSUPPORTED",
                        f"{stream_label}@schemeIdUri uses unsupported SCTE-35 scheme {scheme!r}.",
                    )
                )

            timescale = parse_non_negative_number(attr(event_stream, "timescale")) or 1
            presentation_time_offset = parse_non_negative_number(attr(event_stream, "presentationTimeOffset")) or 0

            seen_ids: dict[str, str] = {}

            for event_index, event in enumerate(children(event_stream, "Event"), 1):
                event_label = f"{stream_label}/Event[{event_index}]"
                event_id = attr(event, "id")
                presentation_time = parse_non_negative_number(attr(event, "presentationTime"))

                if event_id:
                    payload = event_payload_text(event)
                    if event_id in seen_ids and seen_ids[event_id] != payload:
                        findings.append(
                            Finding(
                                "WARNING",
                                "SCTE35_EVENT_ID_DUPLICATE_CONFLICTING_PAYLOAD",
                                f"{event_label}@id {event_id!r} duplicates another Event id with different payload.",
                            )
                        )
                    seen_ids.setdefault(event_id, payload)

                if attr(event, "presentationTime") is None:
                    findings.append(
                        Finding("ERROR", "SCTE35_EVENT_PRESENTATION_TIME_MISSING", f"{event_label}@presentationTime shall be present.")
                    )
                elif presentation_time is None:
                    findings.append(
                        Finding("ERROR", "SCTE35_EVENT_PRESENTATION_TIME_INVALID", f"{event_label}@presentationTime shall be non-negative numeric.")
                    )
                elif period_end is not None:
                    event_time_seconds = (presentation_time - presentation_time_offset) / timescale
                    if period_start is not None and event_time_seconds < period_start:
                        findings.append(
                            Finding("WARNING", "SCTE35_EVENT_TIME_BEFORE_PERIOD", f"{event_label}@presentationTime appears before Period start.")
                        )
                    if event_time_seconds > period_end:
                        findings.append(
                            Finding("WARNING", "SCTE35_EVENT_TIME_AFTER_PERIOD", f"{event_label}@presentationTime appears after Period end.")
                        )

                duration_attr = attr(event, "duration")
                if duration_attr is not None and parse_non_negative_number(duration_attr) is None:
                    findings.append(
                        Finding("ERROR", "SCTE35_EVENT_DURATION_INVALID", f"{event_label}@duration shall be non-negative numeric when present.")
                    )

                if scheme == SCTE35_2014_XML_BIN:
                    binary = find_binary(event)
                    if binary is None:
                        findings.append(
                            Finding(
                                "ERROR",
                                "SCTE35_XML_BIN_BINARY_MISSING",
                                f"{event_label} shall contain scte35:Signal/scte35:Binary for xml+bin.",
                            )
                        )
                    else:
                        payload = decode_binary_payload(binary.text or "")
                        if payload is None:
                            findings.append(
                                Finding("ERROR", "SCTE35_XML_BIN_BINARY_INVALID_BASE64", f"{event_label} Binary payload is not valid Base64.")
                            )
                        else:
                            command_type = parse_scte35_command_type(payload)
                            if command_type is None:
                                findings.append(
                                    Finding(
                                        "ERROR",
                                        "SCTE35_PAYLOAD_COMMAND_TYPE_UNPARSEABLE",
                                        f"{event_label} Binary payload does not expose a parseable SCTE-35 command type.",
                                    )
                                )
                            else:
                                payload_info = parse_scte35_payload_info(payload)
                                command_name = scte35_command_name(command_type)
                                if command_type not in {0x05, 0x06}:
                                    findings.append(
                                        Finding(
                                            "WARNING",
                                            "SCTE35_PAYLOAD_COMMAND_TYPE_NOT_OPPORTUNITY_SIGNAL",
                                            f"{event_label} SCTE-35 command type is {command_name}; expected splice_insert or time_signal for opportunity signalling.",
                                        )
                                    )
                                elif payload_info and command_type == 0x06 and not payload_info.has_splice_time:
                                    findings.append(
                                        Finding(
                                            "WARNING",
                                            "SCTE35_TIME_SIGNAL_SPLICE_TIME_MISSING",
                                            f"{event_label} time_signal() does not set splice_time().",
                                        )
                                    )
                                if payload_info and command_type == 0x06 and payload_info.segmentation_descriptor_count == 0:
                                    findings.append(
                                        Finding(
                                            "WARNING",
                                            "SCTE35_SEGMENTATION_DESCRIPTOR_MISSING",
                                            f"{event_label} SCTE-35 descriptor loop contains no segmentation_descriptor().",
                                        )
                                    )

    if scte35_stream_count == 0:
        findings.append(
            Finding(
                "WARNING",
                "SCTE35_EVENTSTREAM_MISSING",
                "No SCTE-35 MPD EventStream found; IF-3 opportunity metadata shall be carried through MPD Events when the feature is claimed.",
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