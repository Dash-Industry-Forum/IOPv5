import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

DOCX = Path(__file__).resolve().parents[2] / "rag" / "corpus" / "published" / "DASH-IF-IOP-Part5-v5.0.0.docx"
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

with zipfile.ZipFile(DOCX) as archive:
    root = ET.fromstring(archive.read("word/document.xml"))

tables = root.findall(".//w:tbl", NS)
print(f"tables {len(tables)}")

patterns = re.compile(
    r"DASH-IF Ad content|Ad Content spliced|DASH-IF ad content|Ad content|MPD Requirements",
    re.IGNORECASE,
)

for index, table in enumerate(tables, 1):
    rows = []
    for tr in table.findall(".//w:tr", NS):
        cells = []
        for tc in tr.findall("./w:tc", NS):
            parts = []
            for para in tc.findall(".//w:p", NS):
                text = "".join(node.text or "" for node in para.findall(".//w:t", NS))
                if text.strip():
                    parts.append(text.strip())
            value = " / ".join(parts)
            value = re.sub(r"\s+", " ", value).strip()
            cells.append(value)
        rows.append(cells)

    flat = " | ".join(" | ".join(row) for row in rows)
    if patterns.search(flat):
        print(f"\nTABLE {index} rows {len(rows)}")
        for row in rows[:100]:
            print(" | ".join(row)[:1000])