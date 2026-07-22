#!/usr/bin/env python3
"""Validate initial DASH-IF IOP v5 Part 9 text-track MPD signalling.

Initial F-0009-T1/T2 validator-start script. It focuses on deterministic
MPD-level checks for text Adaptation Sets and video-carried caption signalling.
"""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

DASH_NS = "urn:mpeg:dash:schema:mpd:2011"

TEXT_MIME_TYPES = {
    "application/mp4",
    "application/ttml+xml",
    "text/vtt",
}

TEXT_CODEC_HINTS = {
    "stpp",
    "wvtt",
    "im1t",
    "im1i",
    "cwvt",
}

VALID_TEXT_ROLES = {
    "subtitle",
    "caption",
    "easyreader",
    "alternate",
    "main",
}

DASH_ROLE_SCHEME = "urn:mpeg:dash:role:2011"
DASH_ACCESSIBILITY_SCHEME = "urn:mpeg:dash:role:2011"
CEA608_SCHEME = "urn:scte:dash:cc:cea-608:2015"
CEA708_SCHEME = "urn:scte:dash:cc:cea-708:2015"


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


def split_tokens(value: str | None) -> set[str]:
    if not value:
        return set()
    return {part.strip() for part in value.replace(",", " ").split() if part.strip()}


def is_text_adaptation_set(adaptation_set: ET.Element) -> bool:
    content_type = (attr(adaptation_set, "contentType") or "").lower()
    mime_type = (attr(adaptation_set, "mimeType") or "").lower()
    codecs = " ".join(
        filter(
            None,
            [attr(adaptation_set, "codecs")]
            + [attr(representation, "codecs") for representation in children(adaptation_set, "Representation")],
        )
    ).lower()
    if content_type == "text":
        return True
    if mime_type in TEXT_MIME_TYPES:
        return True
    return any(hint in codecs for hint in TEXT_CODEC_HINTS)


def is_video_adaptation_set(adaptation_set: ET.Element) -> bool:
    return (attr(adaptation_set, "contentType") or "").lower() == "video" or (
        attr(adaptation_set, "mimeType") or ""
    ).lower().startswith("video/")


def descriptor_values(adaptation_set: ET.Element, descriptor_name: str) -> list[tuple[str | None, str | None]]:
    return [
        (attr(descriptor, "schemeIdUri"), attr(descriptor, "value"))
        for descriptor in children(adaptation_set, descriptor_name)
    ]


def validate_lang(value: str | None) -> bool:
    if value is None:
        return False
    if value in {"und", "mul"}:
        return True
    return re.fullmatch(r"[A-Za-z]{2,3}(-[A-Za-z0-9]{2,8})*", value) is not None


def validate_cea608_value(value: str | None) -> bool:
    if not value:
        return False
    # Accept CC1=eng;CC3=spa style values and language-only shorthand.
    if re.fullmatch(r"[A-Za-z]{2,3}", value):
        return True
    entry = r"CC[1-4]=[A-Za-z]{2,3}"
    return re.fullmatch(entry + r"(;" + entry + r")*", value) is not None


def validate_mpd(path: Path) -> list[Finding]:
    findings: list[Finding] = []

    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        return [Finding("ERROR", "MPD_XML_PARSE_ERROR", f"XML parse error: {exc}")]

    if local_name(root.tag) != "MPD":
        return [Finding("ERROR", "MPD_ROOT_NOT_MPD", "Root element is not MPD.")]

    text_count = 0
    caption_signalling_count = 0

    for as_index, adaptation_set in enumerate(descendants(root, "AdaptationSet"), 1):
        label = f"AdaptationSet[{as_index}]"
        mime_type = attr(adaptation_set, "mimeType")
        content_type = attr(adaptation_set, "contentType")
        selection_priority = attr(adaptation_set, "selectionPriority")

        if selection_priority is not None:
            try:
                if int(selection_priority) < 0:
                    findings.append(
                        Finding("ERROR", "TEXT_SELECTION_PRIORITY_INVALID", f"{label}@selectionPriority shall be a non-negative integer.")
                    )
            except ValueError:
                findings.append(
                    Finding("ERROR", "TEXT_SELECTION_PRIORITY_INVALID", f"{label}@selectionPriority shall be a non-negative integer.")
                )

        role_values = descriptor_values(adaptation_set, "Role")
        for scheme, value in role_values:
            if scheme == DASH_ROLE_SCHEME and value and value not in VALID_TEXT_ROLES:
                findings.append(
                    Finding("WARNING", "TEXT_ROLE_VALUE_UNRECOGNIZED", f"{label} Role@value {value!r} is not in the initial Part 9 text role set.")
                )

        if is_text_adaptation_set(adaptation_set):
            text_count += 1

            if content_type and content_type.lower() != "text":
                findings.append(
                    Finding("WARNING", "TEXT_CONTENT_TYPE_NOT_TEXT", f"{label}@contentType should be 'text' for text Adaptation Sets.")
                )

            if mime_type is None:
                findings.append(Finding("ERROR", "TEXT_MIME_TYPE_MISSING", f"{label}@mimeType shall be present."))
            elif mime_type not in TEXT_MIME_TYPES:
                findings.append(
                    Finding("ERROR", "TEXT_MIME_TYPE_UNSUPPORTED", f"{label}@mimeType {mime_type!r} is not in the initial Part 9 text MIME set.")
                )

            codecs = split_tokens(attr(adaptation_set, "codecs"))
            for representation in children(adaptation_set, "Representation"):
                codecs |= split_tokens(attr(representation, "codecs"))
            if not codecs:
                findings.append(Finding("ERROR", "TEXT_CODECS_MISSING", f"{label} shall provide text codec signalling."))
            elif not any(any(hint in codec.lower() for hint in TEXT_CODEC_HINTS) for codec in codecs):
                findings.append(
                    Finding("WARNING", "TEXT_CODECS_UNRECOGNIZED", f"{label} codecs {sorted(codecs)!r} are not recognized by the initial Part 9 text set.")
                )

            if not validate_lang(attr(adaptation_set, "lang")):
                findings.append(
                    Finding("WARNING", "TEXT_LANG_MISSING_OR_INVALID", f"{label}@lang should be present and BCP-47-like for text tracks.")
                )

            role_values_only = {value for scheme, value in role_values if scheme == DASH_ROLE_SCHEME and value}
            if not role_values_only:
                findings.append(Finding("WARNING", "TEXT_ROLE_MISSING", f"{label} should include a DASH Role descriptor."))
            if "caption" in role_values_only and not children(adaptation_set, "Accessibility"):
                findings.append(
                    Finding("WARNING", "TEXT_CAPTION_ACCESSIBILITY_MISSING", f"{label} caption text track should include Accessibility signalling.")
                )

        if is_video_adaptation_set(adaptation_set):
            for scheme, value in descriptor_values(adaptation_set, "Accessibility"):
                if scheme in {CEA608_SCHEME, CEA708_SCHEME}:
                    caption_signalling_count += 1
                    if scheme == CEA608_SCHEME and not validate_cea608_value(value):
                        findings.append(
                            Finding(
                                "ERROR",
                                "CEA608_ACCESSIBILITY_VALUE_INVALID",
                                f"{label} CEA-608 Accessibility@value should use language shorthand or CCn=lang entries.",
                            )
                        )

    if text_count == 0 and caption_signalling_count == 0:
        findings.append(
            Finding(
                "WARNING",
                "TEXT_TRACK_SIGNALLING_MISSING",
                "No text AdaptationSet or video-carried CTA caption signalling found.",
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