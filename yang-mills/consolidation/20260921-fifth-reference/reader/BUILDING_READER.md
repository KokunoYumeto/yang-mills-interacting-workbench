# Building the fifth-reference mathematical reader

Requirements: Python 3, Pandoc, XeLaTeX with Latin Modern fonts, and Poppler.
The reader contains a new explanatory introduction and both complete proof
manuscripts, without extending or rewriting their mathematics.

The generated `yang_mills_fifth_reference_20260921.tex` is standalone. Copy
that file to an otherwise empty directory and run:

```sh
xelatex -interaction=nonstopmode -halt-on-error -no-shell-escape yang_mills_fifth_reference_20260921.tex
xelatex -interaction=nonstopmode -halt-on-error -no-shell-escape yang_mills_fifth_reference_20260921.tex
```

No external images, bibliography database, private paths or source files are
needed by that TeX build. Its header comments retain the source SHA-256 identities.

To reassemble from the byte-preserved manuscripts in `sources/`, run:

```sh
python build_reader.py --output-dir output
```

Alternatively pass `--source-dir PATH`, where PATH contains the two original
manuscripts `FIFTH_REFERENCE.md` and `HEAT_AND_COMPLEMENT.md`. Their fixed
SHA-256 values are checked before assembly. The script never runs mathematical
producer or audit scripts. The new introduction is `reader_introduction.md`;
the typography is in `reader_template.tex` and `reader_filter.lua`.

`source_integrity.json` records byte counts and hashes of the two original
files, canonical Markdown assembly, display counts, and reversible writer
escapes. Original TeX display contents and equation labels are retained. Literal
asterisks and underscores in prose are protected from Markdown emphasis. For
oversized formula boxes only, the filter scales down to the text width and
substitutes the equivalent `aligned` environment for `split` inside the box.
The filter also supplies the missing array-header row terminator before
`\hline` in F38; all values, labels and original manuscript bytes are preserved.

Render every page for review, then prepare contact sheets and machine checks:

```sh
pdftoppm -r 90 -png yang_mills_fifth_reference_20260921.pdf tmp/pdfs/page
python verify_reader.py
```

The verifier needs `pypdf`, `pdfplumber` and Pillow. It checks display labels,
source preservation, prose adjoints/underscores, margins and private markers,
and compares the standalone rebuild page text when `standalone_check/` exists.
Contact sheets and full-page equation/table checks are recorded in
`VISUAL_REVIEW.json`; `reader_qa.json` binds the review to the final PDF hash.
This publication QA is distinct from the source's finite mathematical checks.
