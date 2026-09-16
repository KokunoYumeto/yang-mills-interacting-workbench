"""Build the complete September 14-16 Yang-Mills continuation source reader.

Run from any directory with Python 3, pandoc and XeLaTeX on PATH. Raw research
files are read, hashed and never edited. Add exact repository-relative paths to
reader/extra-chapters.json to append transcript recoveries and audit reports.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "yang-mills/consolidation/20260916/reader"
STEM = "yang_mills_web_continuation"
PROOF_NAMES = (
    "RESEARCH_NOTE.md", "DELIVERED_RESEARCH_NOTE.md", "DEVELOPMENT.md",
    "HEAT_BATH_GAP.md", "VOLUME_LIMIT.md", "OPTIMIZED_DOMAIN.md",
    "SECOND_SOURCE.md", "SPATIAL_RETURN.md", "BAND_AND_CERTIFICATE.md",
    "CUBIC_SOURCE.md", "LINEARIZED_RETURN.md",
)

PREFACE = r"""\frontmatter
\begin{titlepage}
\centering
\vspace*{25mm}
{\large Research source reader\par}
\vspace{12mm}
{\Huge\bfseries Yang--Mills\par}
\vspace{8mm}
{\LARGE Complete web-session continuation\par}
\vspace{5mm}
{\Large 14--16 September 2026\par}
\vfill
{\large Complete mathematical source bodies,\par
source provenance, and accompanying review records\par}
\vspace{12mm}
{\normalsize Consolidated 16 September 2026\par}
\end{titlepage}

\chapter*{About this source reader}
\addcontentsline{toc}{chapter}{About this source reader}

This volume brings together the complete mathematical Markdown source bodies
of the Yang--Mills continuation delivered on 14--16 September 2026. It is a
documentary consolidation: it does not replace the original source files and
does not confer blanket certification on their mathematical claims. Each
chapter records its exact repository-relative source path and SHA-256 digest.
The accompanying machine-readable manifest records source sizes and ordering.

The sources retain their original hypotheses, constants, coordinates, signs,
orientations, domains, codomains, proofs, and research status. Original TeX
mathematics is typeset as mathematics. Original plain-text formulas remain in
monospaced blocks; long lines may wrap typographically without changing their
content. Original source headings and all source-body paragraphs are retained.
No new mathematical simplification or normalization is performed by the build.

These continuations primarily concern original finite-lattice SU(2) Hamiltonians,
their interacting vacua, physical excitation estimates, Wilson observables,
and specified spatial-volume or reconstruction limits. Coupling and regulator
hypotheses belong to the individual statements. A finite-lattice estimate or a
fixed-spacing spatial-volume statement is not by itself a proof of the
four-dimensional continuum Yang--Mills mass-gap problem. Source claims should
be read with their exact hypotheses and with any later review chapters in this
edition. Finite executable checks verify the fixtures they test; they are not
a formal verification of all analytic arguments.

Earlier foundational source volumes and their readable PDFs remain in the
repository under \texttt{yang-mills/sources/} and
\texttt{yang-mills/readers/}. References to those earlier sources are retained
as written. This continuation volume preserves the full new source bodies,
rather than replacing them with summaries.

Where an additional chapter is explicitly labelled as a transcript-derived
mathematical final response, it recovers only that public final response. It
does not imply that a missing attachment has been recovered. User messages
and model thinking are not included in this volume. An independent review,
when included, is identified separately from the source it reviews.

\tableofcontents
\mainmatter
"""

HEADER = r"""\documentclass[11pt,a4paper,oneside,openany]{book}
\usepackage[margin=23mm,headheight=16pt,headsep=8mm]{geometry}
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont[Scale=0.84]{DejaVu Sans Mono}
\usepackage{amsmath,amssymb,mathtools,mathrsfs}
\usepackage{unicode-math}
\setmathfont{Latin Modern Math}
\usepackage{microtype}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{adjustbox}
\usepackage{longtable,booktabs,array}
\newcounter{none}
\usepackage{calc}
\usepackage{etoolbox}
\usepackage{fvextra}
\DefineVerbatimEnvironment{verbatim}{Verbatim}{breaklines=true,breakanywhere=true,fontsize=\small,breaksymbolleft={\tiny\ensuremath{\hookrightarrow}},breaksymbolright={}}
\usepackage{xurl}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=black,urlcolor=blue!55!black,pdftitle={Yang-Mills: complete web-session continuation (14-16 September 2026)},pdfauthor={},pdfsubject={Complete mathematical continuation sources and provenance},pdfcreator={Pandoc and XeLaTeX}}
\usepackage{bookmark}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small Yang--Mills continuation, 14--16 September 2026}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.3pt}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\thepage}\renewcommand{\headrulewidth}{0pt}}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt plus 1pt minus 1pt}
\setlength{\emergencystretch}{3em}
\setcounter{tocdepth}{1}
\setcounter{secnumdepth}{-1}
\makeatletter
\renewcommand{\@pnumwidth}{2.5em}
\renewcommand{\@tocrmarg}{3.5em}
\makeatother
\allowdisplaybreaks[2]
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\passthrough}[1]{#1}
\newcommand{\pandocbounded}[1]{#1}
\begin{document}
"""


def tex_escape(text: str) -> str:
    return "".join({"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%",
                    "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{",
                    "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}.get(c, c) for c in text)


def collect() -> list[dict]:
    paths = ["yang-mills/research-control/RESEARCH_NOTE.md"]
    for folder in sorted((ROOT / "yang-mills/continuations").iterdir()):
        if folder.is_dir() and folder.name[:8] in {"20260914", "20260915", "20260916"}:
            paths += [(folder / name).relative_to(ROOT).as_posix()
                      for name in PROOF_NAMES if (folder / name).is_file()]
    extras_path = OUT / "extra-chapters.json"
    entries = [{"path": p, "kind": "complete delivered mathematical source"} for p in paths]
    if extras_path.exists():
        entries += json.loads(extras_path.read_text(encoding="utf-8"))
    seen = set()
    for i, item in enumerate(entries, 1):
        rel = item["path"]
        path = (ROOT / rel).resolve()
        if not path.is_relative_to(ROOT) or path.suffix.lower() != ".md":
            raise ValueError(f"Invalid source path: {rel}")
        if rel in seen:
            raise ValueError(f"Repeated source path: {rel}")
        seen.add(rel)
        raw = path.read_bytes()
        body = raw.decode("utf-8-sig")
        first = re.search(r"^#\s+(.+)$", body, re.M)
        item.update(chapter=i, title=item.get("title", first.group(1) if first else path.stem),
                    sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw), body=body)
    return entries


def wrap_literal(text: str) -> str:
    """Give long paths/code legal typographic breaks without changing characters."""
    chars = [r"\ " if c == " " else tex_escape(c) for c in text]
    return r"\texorpdfstring{{\ttfamily\small " + r"\allowbreak{}".join(chars) + "}}{" + tex_escape(text) + "}"


def presentation_ast(value):
    if isinstance(value, list):
        return [presentation_ast(x) for x in value]
    if not isinstance(value, dict):
        return value
    if value.get("t") == "Code":
        return {"t": "RawInline", "c": ["latex", wrap_literal(value["c"][1])]}
    if value.get("t") == "Str" and len(value.get("c", "")) > 12:
        text = value["c"]
        if any(c in text for c in "/_=<>") or re.search(r"[0-9a-f]{32}", text) or (len(text) > 24 and "," in text and any(c.isdigit() for c in text)):
            return {"t": "RawInline", "c": ["latex", wrap_literal(text)]}
    if value.get("t") == "Math" and value["c"][0]["t"] == "DisplayMath":
        math = value["c"][1]
        math = math.replace("p\\ {\nm in\\ plane}\\p\\sim q", r"p\ {\rm in\ plane}\\p\sim q")
        tags = re.findall(r"\\tag\*?\{[^{}]*\}", math)
        if len(tags) <= 1:
            for tag in tags:
                math = math.replace(tag, "")
            math = re.sub(r"\n\s*\n", "\n", math).strip()
            displayed = r"\[\adjustbox{max width=0.92\linewidth}{$\displaystyle " + math + "$}" + "".join(tags) + r"\]"
            return {"t": "RawInline", "c": ["latex", displayed]}
    if value.get("t") == "Math" and value["c"][0]["t"] == "InlineMath":
        # Permit coefficient lists to wrap inside narrow table columns.
        return {"t": "Math", "c": [value["c"][0], value["c"][1].replace(",", r",\allowbreak ")]}
    return {k: presentation_ast(v) for k, v in value.items()}


def verify_pdf(sources: list[dict]) -> dict:
    import fitz
    pdf_path = OUT / (STEM + ".pdf")
    doc = fitz.open(pdf_path)
    log = (OUT / ".build" / (STEM + ".log")).read_text(encoding="utf-8", errors="replace")
    outside = []
    texts = []
    for index, page in enumerate(doc):
        texts.append(page.get_text())
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    rect = fitz.Rect(span["bbox"])
                    if (rect.x0 < -0.5 or rect.y0 < -0.5 or
                            rect.x1 > page.rect.width + 0.5 or rect.y1 > page.rect.height + 0.5):
                        outside.append({"page": index + 1, "text": span["text"]})
    checks = {
        "page_count": len(doc), "source_chapters": len(sources),
        "source_bytes": sum(s["bytes"] for s in sources),
        "source_hashes_verified": all(hashlib.sha256((ROOT / s["path"]).read_bytes()).hexdigest() == s["sha256"] for s in sources),
        "overfull_box_count": log.count("Overfull"),
        "missing_character_count": log.count("Missing character"),
        "out_of_page_text_span_count": len(outside),
        "pdf_bookmark_count": len(doc.get_toc()),
        "metadata_author": doc.metadata.get("author", ""),
        "local_path_scan_clean": not bool(re.search(r"[A-Z]:[/\\]Users|AppData", "\n".join(texts), re.I)),
        "xelatex_passes": 3,
        "pdf_sha256": hashlib.sha256(pdf_path.read_bytes()).hexdigest(),
        "tex_sha256": hashlib.sha256((OUT / (STEM + ".tex")).read_bytes()).hexdigest(),
        "rendering_record": "RENDERING_ERRATA.md",
        "visual_review_record": "LAYOUT_REVIEW.md",
    }
    (OUT / "BUILD_CHECKS.json").write_text(json.dumps(checks, indent=2) + "\n", encoding="utf-8")
    if (not checks["source_hashes_verified"] or checks["overfull_box_count"] or
            checks["missing_character_count"] or outside or not checks["local_path_scan_clean"]):
        raise RuntimeError("Reader build checks failed; inspect BUILD_CHECKS.json")
    return checks


def build(no_pdf: bool = False) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    sources = collect()
    scratch = OUT / ".build"
    scratch.mkdir(exist_ok=True)
    parts = [PREFACE]
    previous_part = None
    for item in sources:
        body = item["body"]
        if item.get("part") and item["part"] != previous_part:
            parts.append(r"\part{" + tex_escape(item["part"]) + "}")
        previous_part = item.get("part")
        provenance = "\n\n" + r"\begin{quote}\footnotesize" + "\n"
        provenance += r"\textbf{Source classification:} " + tex_escape(item["kind"]) + "\n\n"
        provenance += r"\textbf{Repository source:} \path{" + item["path"] + "}\n\n"
        provenance += r"\textbf{SHA-256:} \path{" + item["sha256"] + "}\n"
        if item.get("notice"):
            provenance += "\n\\textbf{Editorial provenance notice:} " + tex_escape(item["notice"]) + "\n"
        provenance += r"\end{quote}" + "\n\n"
        if re.match(r"\s*#\s+", body):
            first, _, remainder = body.partition("\n")
            parts.append(first + provenance + remainder)
        else:
            parts.append("# " + item["title"] + provenance + body)
    assembled = "\n\n".join(parts) + "\n"
    md_path = OUT / (STEM + ".md")
    md_path.write_text(assembled, encoding="utf-8", newline="\n")
    parsed = subprocess.run(
        ["pandoc", str(md_path), "--from=markdown+tex_math_single_backslash-smart",
         "--to=json"], capture_output=True, text=True, encoding="utf-8", check=True)
    ast = presentation_ast(json.loads(parsed.stdout))
    converted = subprocess.run(
        ["pandoc", "--from=json", "--to=latex", "--top-level-division=chapter", "--syntax-highlighting=none",
         "--wrap=preserve"], input=json.dumps(ast), capture_output=True, text=True, encoding="utf-8", check=True)
    (scratch / "pandoc.log").write_text(converted.stderr, encoding="utf-8")
    latex = HEADER + converted.stdout + "\n\\end{document}\n"
    tex_path = OUT / (STEM + ".tex")
    tex_path.write_text(latex, encoding="utf-8", newline="\n")
    manifest = {"title": "Yang-Mills: complete web-session continuation (14-16 September 2026)",
                "source_policy": "Complete source bodies; raw sources unchanged; presentation-only wrapping.",
                "chapters": [{k: v for k, v in s.items() if k != "body"} for s in sources]}
    (OUT / "CHAPTER_MANIFEST.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    if not no_pdf:
        for pass_no in range(1, 4):
            proc = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error",
                                   "-file-line-error", "-output-directory=.build", tex_path.name],
                                  cwd=OUT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                  text=True, encoding="utf-8", errors="replace")
            (scratch / f"xelatex-pass-{pass_no}.txt").write_text(proc.stdout, encoding="utf-8")
            if proc.returncode:
                print(proc.stdout[-14000:])
                raise SystemExit(proc.returncode)
        shutil.copy2(scratch / (STEM + ".pdf"), OUT / (STEM + ".pdf"))
    for item in sources:
        if hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest() != item["sha256"]:
            raise RuntimeError(f"Source changed during build: {item['path']}")
    if not no_pdf:
        verify_pdf(sources)
    print(json.dumps({"chapters": len(sources), "source_bytes": sum(s["bytes"] for s in sources),
                      "output": (OUT / (STEM + (".tex" if no_pdf else ".pdf"))).relative_to(ROOT).as_posix()}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-pdf", action="store_true", help="Generate Markdown, TeX and manifest only")
    build(parser.parse_args().no_pdf)
