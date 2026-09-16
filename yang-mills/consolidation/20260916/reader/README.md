# Complete Yang-Mills continuation reader

The PDF and editable TeX preserve the complete mathematical sources of the
14-16 September continuation, followed by the full historical mathematical
final responses recovered from the web-session export and the bounded audit
reports. The source chapters are complete bodies, not mathematical summaries.

- `yang_mills_web_continuation.pdf`: readable cumulative continuation volume.
- `yang_mills_web_continuation.tex`: editable standalone LaTeX source.
- `yang_mills_web_continuation.md`: assembled Markdown, retaining source text.
- `CHAPTER_MANIFEST.json`: exact source paths, SHA-256 hashes, sizes, ordering,
  and provenance classification for every chapter.
- `extra-chapters.json`: additional historical-response and review chapters.
- `RENDERING_ERRATA.md`: the explicit B32 TeX repair and typographic policy.
- `BUILD_CHECKS.json`: compilation, source-integrity and layout checks.
- `LAYOUT_REVIEW.md`: representative-page visual review record.

The three final-response chapters whose original linked attachments remain
unavailable say so prominently. A transcript-derived final response is not
presented as recovery of its missing attachment. The audit chapters state
their own bounded scope and qualifications.

From the repository root, rebuild with:

```sh
python tools/build_ym_continuation_reader.py
```

The build requires Python 3 with PyMuPDF, Pandoc 3, XeLaTeX, DejaVu Serif/Sans/Sans Mono,
Latin Modern Math, and the TeX packages listed in the generated preamble. It
runs three TeX passes for the table of contents and page labels. Original
source files are hashed before building and rechecked afterward. The builder
does not edit them. Intermediate TeX files, logs and local raster review
images stay in the ignored `.build/` directory.

To append a newly available source, add its repository-relative path and
provenance classification to `extra-chapters.json`, then rebuild. No absolute
machine path is needed in the publication artifacts.
