"""Check source-preserving publication and prepare contact sheets for review."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess

import pdfplumber
from PIL import Image, ImageDraw
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
STEM = "yang_mills_fifth_reference_20260921"
PDF = ROOT / (STEM + ".pdf")
TMP = ROOT / "tmp/pdfs"

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--render", action="store_true")
    args = parser.parse_args()
    TMP.mkdir(parents=True, exist_ok=True)
    if args.render:
        subprocess.run(["pdftoppm", "-r", "90", "-png", str(PDF), str(TMP / "page")],
                       check=True, timeout=240)
    reader = PdfReader(PDF)
    texts = [p.extract_text() or "" for p in reader.pages]
    text = "\n".join(texts)
    leaks = [s for s in ["C:\\Users\\", "C:/Users/", "private_review",
                           "<INSTRUCTIONS>", "<environment_context>"] if s in text]
    outliers = []
    with pdfplumber.open(PDF) as pdf:
        for index, page in enumerate(pdf.pages, 1):
            for char in page.chars:
                if not char.get("text", "").strip():
                    continue
                if 68 <= char["top"] <= 775 and (char["x0"] < 65 or char["x1"] > 532):
                    outliers.append({"page": index, "text": char["text"],
                                     "x0": char["x0"], "x1": char["x1"],
                                     "top": char["top"]})
    pages = sorted(TMP.glob("page-*.png"))
    contacts = []
    for start in range(0, len(pages), 12):
        sheet = Image.new("RGB", (4*300, 3*445), "#e6e8eb")
        draw = ImageDraw.Draw(sheet)
        for offset, path in enumerate(pages[start:start+12]):
            picture = Image.open(path).convert("RGB")
            picture.thumbnail((280, 405))
            x, y = (offset % 4)*300+10, (offset // 4)*445+25
            sheet.paste(picture, (x, y))
            draw.text((x, y-18), f"PDF page {start+offset+1}", fill="black")
        target = TMP / f"contact-{start//12+1}.png"
        sheet.save(target)
        contacts.append(target.name)
    log = (ROOT / (STEM + ".log")).read_text(encoding="utf-8", errors="replace")
    issues = [line for line in log.splitlines()
              if re.search(r"Overfull|Missing character|undefined|^!", line)]
    labels = [f"(F{n})" for n in range(1, 43)] + [f"(H{n})" for n in range(1, 35)]
    missing = [s for s in ["Levent Alpöge", "Fable", "Lumer", "Eymard"] + labels if s not in text]
    integrity = json.loads((ROOT / "source_integrity.json").read_text())
    assembled = (ROOT / (STEM + ".md")).read_text(encoding="utf-8")
    source_checks = []
    for source in integrity["sources"]:
        data = (ROOT / "sources" / source["filename"]).read_bytes()
        normalized = data.decode("utf-8-sig").replace("\r\n", "\n")
        ok = hashlib.sha256(data).hexdigest() == source["sha256"] and assembled.count(normalized) == 1
        source_checks.append({"filename": source["filename"], "bytes_sha256_and_complete_assembly": ok})
    # A section heading at a proof's first page starts at the beginning of that
    # page after the standard running head; find its unique numbered heading.
    first = next(i for i, value in enumerate(texts)
                 if re.search(r"A\s+The complete fifth reference", value) and "(F1)" in value)
    appendix_text = "\n".join(texts[first:])
    literal_counts = {symbol: {
        "source_prose": sum(s["protected_prose_symbols"][symbol] for s in integrity["sources"]),
        "pdf_appendices": appendix_text.count(symbol)} for symbol in ["*", "_"]}
    literal_ok = all(v["source_prose"] == v["pdf_appendices"] for v in literal_counts.values())
    standalone_pdf = ROOT / "standalone_check" / (STEM + ".pdf")
    standalone_ok = None
    if standalone_pdf.exists():
        standalone_ok = texts == [p.extract_text() or "" for p in PdfReader(standalone_pdf).pages]
    visual_path = ROOT / "VISUAL_REVIEW.json"
    visual = json.loads(visual_path.read_text()) if visual_path.exists() else None
    digest = hashlib.sha256(PDF.read_bytes()).hexdigest()
    if visual and visual.get("pdf_sha256") != digest:
        raise RuntimeError("Visual review refers to an older PDF")
    qa = {
        "schema": "ym-fifth-reference-reader-qa-v1", "pdf_pages": len(texts),
        "rendered_pages": len(pages), "latex_material_errors": issues,
        "body_text_outliers": outliers, "private_markers": leaks,
        "required_text_missing": missing, "contact_sheets": contacts,
        "source_preservation": source_checks,
        "literal_mathematical_character_counts": literal_counts,
        "literal_prose_characters_preserved": literal_ok,
        "standalone_tex_text_identical": standalone_ok,
        "pdf_metadata": {str(k): str(v) for k, v in reader.metadata.items()},
        "artifacts": {name: {"bytes": (ROOT/name).stat().st_size,
                              "sha256": hashlib.sha256((ROOT/name).read_bytes()).hexdigest()}
                      for name in [STEM+".pdf", STEM+".md", STEM+".tex",
                                   "source_integrity.json", "reader_introduction.md",
                                   "build_reader.py", "reader_template.tex", "reader_filter.lua"]},
        "visual_review": visual,
        "proof_start_pdf_page": first+1,
        "table_and_formula_pages": [i+1 for i, value in enumerate(texts) if
                                    any(label in value for label in ["(F11)", "(F25)", "(F29)", "(F38)", "(H13)", "(H18)", "(H26)", "(H30)"])]
    }
    (ROOT / "reader_qa.json").write_text(json.dumps(qa, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k: qa[k] for k in ["pdf_pages", "rendered_pages", "latex_material_errors",
                      "private_markers", "required_text_missing", "literal_mathematical_character_counts",
                      "standalone_tex_text_identical", "proof_start_pdf_page", "table_and_formula_pages"]}))
    print(json.dumps({"outliers": len(outliers), "pdf_sha256": digest}))
    if leaks or issues or missing or outliers or not literal_ok or not all(s["bytes_sha256_and_complete_assembly"] for s in source_checks):
        raise SystemExit(1)
    if pages and len(pages) != len(texts):
        raise SystemExit(1)
    if standalone_ok is False:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
