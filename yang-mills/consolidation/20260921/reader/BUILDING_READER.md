# Building the mathematical reader

Requirements: Python 3, Pandoc, XeLaTeX with Latin Modern fonts, and Poppler.

The complete generated `yang_mills_heat_volume_20260921.tex` is standalone:
run XeLaTeX twice on that file with `-no-shell-escape`. It embeds the full
introduction and all five proof texts and does not depend on a private path,
an external image, or an external bibliography database.

To reassemble from the original five Markdown manuscripts, put this reader
directory beside the matching `package/` directory of the public `20260921`
edition and run `python build_reader.py`. Alternatively run
`python build_reader.py --source-dir PATH --output-dir OUTPUT`, where `PATH`
is the extracted archive's `workbench/yang-mills/continuations` directory.
Both Sep21 continuation subdirectories must be present. The script assembles
each complete source text exactly once, records its SHA-256, runs Pandoc and
two XeLaTeX passes, and places the PDF in `OUTPUT` (or `output/` by default).

`reader_introduction.md` is the editable introductory exposition.
`reader_template.tex` controls the typography. The generated `.md` and `.tex`
are complete editable representations. No proof formula in the five appendices
is edited by the build. The plain-text mathematical formula blocks preserve
the source notation rather than introduce an unchecked TeX reinterpretation.
The separate `_render.md` is a mechanical writer input: literal adjoint and
multiplication asterisks and coordinate underscores outside code blocks are
escaped so Markdown cannot consume them as emphasis. Removing those writer
escapes is checked to recover each complete original manuscript exactly.

For visual review, render all pages with `pdftoppm -r 65 -png`, then inspect
the contact sheets and full-size pages containing tables and mathematical
displays. The source-preservation record is separate from visual QA and from
the workbench's finite computational verification records.
