# Validation of the 14â€“16 September consolidation

## Fresh computation

All eleven top-level delivery-replay commands completed with exit code zero in the existing local Ubuntu 22.04 WSL2 environment, using Python 3.10.12 and SymPy 1.9 where required. Across their direct checks and replay drivers there were 77 checker invocations: 31 successful reproductions and 46 deliberately corrupted cases rejected with their expected exit/error. All eleven computation manifests validated, and an independent post-run scan found all 125 original intake files unchanged.

| Checker family | Named positive checks | False-formula controls | Fresh comparison |
| --- | ---: | ---: | --- |
| Research-control | 56 | 17 | Ordinary and optimized output match the original complete receipt. |
| Vacuum refinement | 181 | â€” | Ordinary and optimized output match each other; the six comparable fields agree with the historical summary. |
| Coupled response | 189 | 12 | Ordinary and optimized output match the original complete receipt. |
| Actual loop moments | 134 | 12 | Ordinary and optimized output match the original complete receipt. |
| Uniform gap / zero shift | 273 | 35 | Full replay, including predecessor and 18 intended CLI rejections, passed. |
| Gauge-native source and band | 642 | 27 | Full replay, original integer box certificate and 20 intended CLI rejections passed. |
| Cubic / linearized | 2,246 | 15 | Full replay, gauge-native predecessor and eight intended CLI rejections passed. |

The vacuum file is a summary, not a full output receipt. Its separate `prior_checker_replay` metadata is historical and was not falsely counted as a fresh execution. The original complete receipts in the source folders retain their original bytes. Fresh records are in [verification/fresh-summary.json](verification/fresh-summary.json), the [full replay report](verification/REPLAY_REPORT.md), and the individual result directories.

The original spectral-reconstruction fixture was additionally run with ordinary Python, retaining its active assertions: [spectral_fixture.json](verification/spectral_fixture.json). It checks a specified two-atom rational matrix moment identity and raw-frame inverse congruence. The separate [cubic arithmetic/geometry implementation](audits/cubic_calculations.py), which imports no delivered checker code, reproduces the recorded rational coefficients and original local incidence census.

These programs check the finite assertions actually implemented. In particular, the cubic source checker exhausts 612 support multisets but evaluates each at two exact quaternion assignments; this is not a polynomial-identity proof for all configurations. The [full checker-scope report](audits/checker_scope.md) records the ranges, arithmetic, norm fixtures and exclusions. No Lean, Lake, Elan, remote CI or paid model execution was performed.

## Bounded mathematical reviews

Four separate reviews read their selected full sources and reconstructed the important mathematical implications: [early/middle maps](audits/early_mid.md), [gauge-native gap and fixed-spacing volume return](audits/gauge_native.md), [local conditional fibres](audits/local_fibres.md), and [cubic/linearized finite-box return](audits/cubic_linearized.md). Each report states a precise bounded claim, dependencies, verdict, complete supporting derivations and exclusions. These are review passes within the same AI-assisted workflow, not external institutional or formal certification.

The selected central arguments passed those bounded reviews. The local-fibre review records the form-domain requirement `h in H^1 intersect K_l` at Z48 and the nonzero-trial requirement at Z55. The cubic review proves the conditional-kernel statement using restricted-form operators; it does not assert kernel invariance under the unrestricted generator. The earlier escaping-state and canonical-residual corrections are already explicit in the integrated source sequence. Minor cross-reference and mathematical typography defects are documented without changing hash-bound original sources.

The reviews do not establish the unresolved four-dimensional continuum construction or a finite positive continuum mass. The enlarged cubic finite-lattice gap range is not silently assigned to the earlier volume-uniqueness theorem.

## Source identity, reader and portability

`python -B tools/verify_ym_consolidation.py` checks all 81 imported source destinations against their exact origin hashes and all eleven complete response extractions against the transcript map. The independent source inventory also checked every provided archive manifest. The original source blobs and all baseline foundation files remain available.

The [reader chapter manifest](reader/CHAPTER_MANIFEST.json), [reader build checks](reader/BUILD_CHECKS.json) and [visual validation](reader/LAYOUT_REVIEW.md) and [rendering errata](reader/RENDERING_ERRATA.md) identify the complete reading edition and its presentation-only repairs. Editable Markdown and TeX accompany the PDF. Reader generation rechecks every included source hash after the build.

The provided replay drivers expect POSIX path and LF output serialization. The fresh run used that environment to preserve exact receipt comparison; no input pins were edited to hide a mismatch. Run the original checker commands on Linux/WSL, or compare native-platform differences explicitly. The source manifest and reader builder are portable Python; the reader additionally requires Pandoc and XeLaTeX with the fonts/packages documented by its build record.

Individual computation manifests retain the exact original intake-relative command paths. [INPUT_PATH_MAP.json](verification/INPUT_PATH_MAP.json) maps their mathematical source hashes to identical files in the integrated tree. Intake-only delivery metadata and historical workflow files are identified as such. Host-path-only wrapper logs are excluded from publication; the actual checker stdout/stderr, execution records and hashes are preserved.

Missing attachment bodies and the absent PR7 checker package are listed in [SOURCE_COVERAGE.md](SOURCE_COVERAGE.md). They were not counted as integrated source or as fresh executions. A [ready-to-paste follow-up prompt](FOLLOWUP_PROMPT.md) requests those exact remaining files and identifies the unfinished fourth vacuum-source calculation.
