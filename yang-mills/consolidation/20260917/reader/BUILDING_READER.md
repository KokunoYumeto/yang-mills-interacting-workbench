# Rebuilding the reader PDF

`yang_mills_quartic_cube_reader.tex` is standalone: it contains the complete introduction, bibliography, and six proof appendices. No external images, bibliography databases, scripts, or source-packet paths are needed to compile it.

With a current TeX distribution providing XeLaTeX and the packages named in the preamble, run these two commands in the directory containing the TeX file:

```text
xelatex -interaction=nonstopmode -halt-on-error -no-shell-escape yang_mills_quartic_cube_reader.tex
xelatex -interaction=nonstopmode -halt-on-error -no-shell-escape yang_mills_quartic_cube_reader.tex
```

The second pass resolves the contents and page references. The document uses the Latin Modern Roman, Sans, Mono, and Math fonts. The distributed PDF was built using Pandoc 3.9.0.2 and MiKTeX-XeTeX 4.18; Pandoc is not needed when compiling the distributed standalone TeX.

The companion Markdown preserves all six supplied proof texts with only line-ending and UTF-8 BOM normalization. `source_integrity.json` records their original byte hashes and normalized-text hashes. The explanatory introduction is separate editorial material. The finished PDF has 49 pages.
