"""Build a reader containing both complete fifth-reference proof manuscripts.

Requires Python 3, Pandoc and XeLaTeX. No source calculation is rerun.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent
STEM = "yang_mills_fifth_reference_20260921"
SOURCES = [
    ("A", "FIFTH_REFERENCE.md", "67e3b0220ce7173e0223b7f00fbf67ed5adef5fd0c83bf85c79015f84cb660d2"),
    ("B", "HEAT_AND_COMPLEMENT.md", "250e567605d2d1e508aad21c4942a7c028a5d82b468c089d4e2c9a9b6e78dd2c"),
]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def protect(source):
    """Protect prose notation, leaving all display-math contents untouched."""
    lines, recovery, in_math, protected_counts = [], [], False, {"*": 0, "_": 0}
    for line in source.splitlines(keepends=True):
        if line.strip() == r"\[":
            in_math = True
        if in_math or line.startswith("    "):
            out, back = line, line
        else:
            out = line.replace("*", r"\*").replace("_", r"\_")
            back = out.replace(r"\*", "*").replace(r"\_", "_")
            for symbol in protected_counts:
                protected_counts[symbol] += line.count(symbol)
        lines.append(out)
        recovery.append(back)
        if line.strip() == r"\]":
            in_math = False
    if in_math or "".join(recovery) != source:
        raise ValueError("Non-reversible source escaping or unterminated formula")
    return "".join(lines), protected_counts

def run(command, logfile):
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                            encoding="utf-8", errors="replace", timeout=240)
    (ROOT / logfile).write_text(result.stdout + result.stderr, encoding="utf-8")
    if result.returncode:
        raise RuntimeError(f"Build command failed; inspect {logfile}")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, default=ROOT / "sources",
                        help="Folder containing FIFTH_REFERENCE.md and HEAT_AND_COMPLEMENT.md")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "output")
    args = parser.parse_args()
    introduction = (ROOT / "reader_introduction.md").read_text(encoding="utf-8")
    pieces, render_pieces, records = [introduction], [introduction], []
    original_dir = ROOT / "sources"
    original_dir.mkdir(exist_ok=True)
    for appendix, filename, expected_hash in SOURCES:
        data = (args.source_dir / filename).read_bytes()
        if sha(data) != expected_hash:
            raise ValueError("Original source hash mismatch: " + filename)
        destination = original_dir / filename
        if not destination.exists():
            destination.write_bytes(data)
        if destination.read_bytes() != data:
            raise ValueError("Existing preserved source differs: " + filename)
        source = data.decode("utf-8-sig").replace("\r\n", "\n")
        rendered, counts = protect(source)
        # Verify every original display, including tags, remains byte-identical
        # in the Markdown writer input before its typographic boxing filter.
        formulas = re.findall(r"\\\[\s*\n(.*?)\\\]", source, flags=re.S)
        if formulas != re.findall(r"\\\[\s*\n(.*?)\\\]", rendered, flags=re.S):
            raise ValueError("A source display changed")
        pieces.append(source)
        render_pieces.append(rendered)
        records.append({"appendix": appendix, "filename": filename,
                        "bytes": len(data), "sha256": sha(data),
                        "normalized_text_sha256": sha(source.encode()),
                        "display_math_blocks": len(formulas),
                        "protected_prose_symbols": counts,
                        "complete_source_preserved": True,
                        "formula_or_proof_edits": False})
    full = "\n\n".join(pieces)
    for _, filename, _ in SOURCES:
        expected = (original_dir / filename).read_text(encoding="utf-8-sig").replace("\r\n", "\n")
        if full.count(expected) != 1:
            raise ValueError("Complete source not included exactly once: " + filename)
    md = ROOT / (STEM + ".md")
    md.write_text(full, encoding="utf-8", newline="\n")
    render_md = ROOT / (STEM + "_render.md")
    render_md.write_text("\n\n".join(render_pieces), encoding="utf-8", newline="\n")
    (ROOT / "source_integrity.json").write_text(json.dumps({
        "schema": "ym-fifth-reference-reader-source-integrity-v1",
        "integrity": "Two complete original source texts included exactly once, with UTF-8 BOM and line-ending handling only in the canonical assembly; exact original bytes retained in sources/.",
        "sources": records, "assembled_markdown_sha256": sha(md.read_bytes()),
        "render_input_sha256": sha(render_md.read_bytes()),
        "render_protection": "Only literal asterisks and underscores outside display math are Markdown-escaped. Recovery to complete source text and equality of all display-math content are checked. The typesetting filter boxes wide formulas, uses aligned instead of split inside the box, and supplies the omitted array-header row terminator before hline in F38. Every mathematical value and source tag is retained.",
    }, indent=2) + "\n", encoding="utf-8")
    run(["pandoc", str(render_md),
         "--from=markdown+tex_math_single_backslash-superscript-subscript-raw_tex-raw_html-smart",
         "--to=latex", "--standalone", "--number-sections", "--toc", "--toc-depth=2",
         "--template=" + str(ROOT / "reader_template.tex"),
         "--lua-filter=" + str(ROOT / "reader_filter.lua"),
         "--output=" + str(ROOT / (STEM + ".tex"))], "pandoc.log")
    tex = ROOT / (STEM + ".tex")
    generated = tex.read_text(encoding="utf-8")
    identities = "\n".join(f"% Source {a}: {name}; SHA-256 {digest}" for a, name, digest in SOURCES)
    tex.write_text(identities + "\n" + generated, encoding="utf-8", newline="\n")
    for number in range(1, 3):
        run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "-no-shell-escape",
             "-recorder", STEM + ".tex"], f"xelatex-pass-{number}.log")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    target = args.output_dir / (STEM + ".pdf")
    shutil.copy2(ROOT / (STEM + ".pdf"), target)
    print(json.dumps({"sources": len(records), "source_integrity": "pass",
                      "pdf": str(target), "bytes": target.stat().st_size,
                      "sha256": sha(target.read_bytes())}))

if __name__ == "__main__":
    main()
