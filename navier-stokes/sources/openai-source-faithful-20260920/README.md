# Finite Time Blowup for Navier–Stokes — complete editable source

[Read the 166-page PDF](upstream/output/pdf/source-faithful-reconstruction.pdf) · [Browse the LaTeX](upstream/reconstruction/) · [Download the complete source ZIP](full-source-release.zip) · [Zenodo archive](https://doi.org/10.5281/zenodo.22852310)

This is a complete copy of the independent, source-faithful LaTeX reconstruction of OpenAI's *Finite Time Blowup for Navier–Stokes*, preserved from [release `5e162f34`](https://github.com/KokunoYumeto/openai-navier-stokes-latex/tree/5e162f34cd2d3581f890660e81fbf063509085d0). The editable text, six figures, style file, checked PDF and transcription records are available directly in this workbench. The original release's files are unchanged in `upstream/`; the ZIP contains the same committed snapshot.

The source-faithful edition preserves the paper's wording, mathematical notation and numbering. It is not an official OpenAI LaTeX release. It is also distinct from this workbench's [208-page analytical reader](../../navier_stokes_workbench_208p.pdf) and later research continuations.

For a permanent citation to this source edition, use [10.5281/zenodo.22852310](https://doi.org/10.5281/zenodo.22852310). The record provides the PDF for reading and an editable-source archive for reuse. Its [publication family](https://doi.org/10.5281/zenodo.22852309) links versions of this source edition, separately from the analytical reader.

## Build the paper

Open [main.tex](upstream/reconstruction/main.tex) in the `upstream/reconstruction/` directory. The section files, style and figures needed by that master document are included. With the TeX packages listed in the [upstream build instructions](upstream/README.md#build), run:

```text
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

The result is `main.pdf`. The already checked release PDF is linked above. A fresh build can differ in bytes with TeX-engine, package or font versions.

## Sources and verification

The mathematical source is the [official OpenAI paper](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf), frozen by the reconstruction at SHA-256 `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`. The reconstructed PDF has SHA-256 `67bca97d638868c2fcb34b0ef1acdc4918cfcbb1a210afe98f0019a3c93fe8d9`.

The publisher's [transcription audit](upstream/evidence/transcription/TRANSCRIPTION_AUDIT.json), [page correspondence](upstream/evidence/transcription/PDF_TEX_CORRESPONDENCE.json), [formula inventory](upstream/evidence/transcription/FORMULA_INVENTORY.json) and [page-level visual records](upstream/evidence/build/visual_qa.jsonl) accompany the complete source. They record 166 pages and 6,175 mathematical occurrences. These are transcription and presentation checks, not a new mathematical proof certificate. The upstream [manifest](upstream/MANIFEST.sha256) identifies the preserved files. Run `python verify_mirror.py` to check every recorded file, the archive and equality between the archive and extracted snapshot.

Attribution and the original [rights notice](upstream/LICENSE-NOTICE.md) are preserved without assigning a new licence. The [source reading record](../../SOURCE_READING_20260920.json) connects this edition to the workbench's historical source versions.
