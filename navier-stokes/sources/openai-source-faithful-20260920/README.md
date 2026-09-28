# Finite Time Blowup for Navier–Stokes — complete editable source

[Read the 166-page PDF](upstream/output/pdf/source-faithful-reconstruction.pdf) · [Browse the LaTeX](upstream/reconstruction/) · [Download the complete source ZIP](full-source-release.zip) · [Zenodo archive](https://doi.org/10.5281/zenodo.22852310)

This is the corrected independent, source-faithful LaTeX reconstruction of OpenAI's *Finite Time Blowup for Navier–Stokes*, based on [release `5e162f34`](https://github.com/KokunoYumeto/openai-navier-stokes-latex/tree/5e162f34cd2d3581f890660e81fbf063509085d0). The editable text, six figures, style file, checked PDF and transcription records are available directly in this workbench. The source, PDF and ZIP include the [D1 transcription correction](upstream/evidence/errata/D1.md) to equation (10.20), applied on 28 September 2026. The ZIP and the extracted source contain the same corrected files.

The source-faithful edition preserves the paper's wording, mathematical notation and numbering. It is not an official OpenAI LaTeX release. It is also distinct from this workbench's [208-page analytical reader](../../navier_stokes_workbench_208p.pdf) and later research continuations.

The earlier source edition is archived at [10.5281/zenodo.22852310](https://doi.org/10.5281/zenodo.22852310). That published record predates D1; the corrected reading copy and editable source are the GitHub files linked above. Its [publication family](https://doi.org/10.5281/zenodo.22852309) links versions of this source edition, separately from the analytical reader.

## Build the paper

Open [main.tex](upstream/reconstruction/main.tex) in the `upstream/reconstruction/` directory. The section files, style and figures needed by that master document are included. With the TeX packages listed in the [upstream build instructions](upstream/README.md#build), run:

```text
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

The result is `main.pdf`. The already checked release PDF is linked above. A fresh build can differ in bytes with TeX-engine, package or font versions.

## Sources and verification

The mathematical source is the [official OpenAI paper](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf), frozen by the reconstruction at SHA-256 `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`. The reconstructed PDF has SHA-256 `41fd1d62501d4776efbfd3e55cda0e97d46e9f443e0a157e30c75eb98bcd4d2a`.

The publisher's [transcription audit](upstream/evidence/transcription/TRANSCRIPTION_AUDIT.json), [page correspondence](upstream/evidence/transcription/PDF_TEX_CORRESPONDENCE.json), [formula inventory](upstream/evidence/transcription/FORMULA_INVENTORY.json) and [page-level visual records](upstream/evidence/build/visual_qa.jsonl) accompany the complete source. They record 166 pages and 6,175 mathematical occurrences. These are transcription and presentation checks, not a new mathematical proof certificate. The [manifest](upstream/MANIFEST.sha256) identifies the corrected files, and the [D1 verification record](upstream/evidence/errata/D1-verification.json) records the new build and checks. Run `python verify_mirror.py` to check every recorded file, the archive and equality between the archive and extracted snapshot.

Attribution and the original [rights notice](upstream/LICENSE-NOTICE.md) are preserved without assigning a new licence. The [source reading record](../../SOURCE_READING_20260920.json) connects this edition to the workbench's historical source versions.
