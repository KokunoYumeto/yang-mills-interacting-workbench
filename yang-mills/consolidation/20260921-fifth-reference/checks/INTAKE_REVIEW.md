# Fifth-reference edition: source and publication review

21 September 2026. This is a bounded publication intake and verification record for the supplied cumulative fifth-reference edition. It is not a new research contribution, a full audit of the inherited analytical chain, an external analytical certification, or a formal-assistant proof.

## Source preservation

The supplied archive `yang_mills_cumulative_20260921_fifth_reference.zip` has SHA-256 `3c5e2603f0a8700c8372bdad45a2c961d8c1e07c3ad9a98b0555d2874142f5d9`. It contains 2,768 UTF-8 text files, totaling 119,687,221 uncompressed bytes. Manifest verification counts 2,767 entries because the manifest itself is excluded from its file list.

Its predecessor `yang_mills_cumulative_20260921_volume.zip` has SHA-256 `f16f29aa8326e2e312376165595a30d760c63ed0775c7a95e26263d4cdd2282d` and 2,015 files. Of these, 2,010 remain byte-identical at their original paths. Five controls changed: `CUMULATIVE_RESEARCH.md`, `CURRENT_STATE.json`, `MANIFEST.json`, `START_HERE.md`, and `workbench/yang-mills/research-control/CURRENT.md`. Their exact predecessor bytes are retained under `history/20260921-volume-controls/`. No predecessor path is missing. There are 753 additional paths.

Fresh comparisons also checked all 2,015 preservation records against both archives. The old cumulative manuscript is an exact prefix of the new one, and both new proof manuscripts appear verbatim in the appended material. Extraction rejected unsafe paths and duplicate/case-colliding members and verified every extracted file against its ZIP-member digest. No source bytes were edited during intake or checking.

## Complete new proof texts

The source directory is `package/workbench/yang-mills/continuations/20260921-fifth-reference-return/`.

| Manuscript | Scope and locators | SHA-256 |
| --- | --- | --- |
| `FIFTH_REFERENCE.md` | Sections F1–F8; equations F1–F42; 23,367 bytes | `67e3b0220ce7173e0223b7f00fbf67ed5adef5fd0c83bf85c79015f84cb660d2` |
| `HEAT_AND_COMPLEMENT.md` | Sections H1–H8; equations H1–H34; 19,505 bytes | `250e567605d2d1e508aad21c4942a7c028a5d82b468c089d4e2c9a9b6e78dd2c` |

Both manuscripts were read in full, together with the new fast checker, its imported exact arithmetic/tensor/assembly code, the producer and polynomial-auditor source, and the supplied execution metadata. The finite checks verify their stated algebraic and numerical scope; the analytical arguments remain the written arguments in the manuscripts.

The unchanged original setting is the open cubic lattice box with integer `L >= 2`, all contained links and faces, all vertex gauge constraints including the boundary, original product Haar probability, `a,g > 0`, `kappa = 2g^2/a`, and `xi = 1/(4g^4)` (F1–F3).

The source argument preserves 662 fifth-source representatives and 124,864 original anchored multisets. Equations F11–F13 prove the orientation-resolved coefficient estimate and explicitly retain all eight axis reflections. F15–F21 give the distinct-face final-spin recurrence, original partial projections, and rational primal/dual objectives. F22–F25 cover the remaining configurations and return every original marked edge. The resulting upward bounds are `||v5||loc < 2476866`, `m(v5) < 1638684`, and `t(v5) < 190128` (F25).

The complete residual has degrees six through ten (F27). With the exact input table F26, `ell(x)`, `delta(x)` and `D(x) = (1-ell(x))^2 - 8 delta(x)/3` are defined in F28. The first positive root satisfies `0.018424953576117616681 < alpha5 < 0.018424953576117616682`. Its corresponding sufficient original coupling endpoint satisfies `3.683551983985727304439 < 1/(2 sqrt(alpha5)) < 3.683551983985727304440` (F29). Thus `g^2 >= 3.683551983985727304440` is an outward-rounded sufficient threshold, not an exact decimal identity for the endpoint.

F30–F32 retain the full inverse and convergent nonlinear correction, including the endpoint tail. F33–F34 return the normalized physical vacuum and scalar ground energy. The actual physical gap obeys `Delta_L >= kappa d5(xi)` on `0 < xi <= alpha5`, with `d5` defined in F35; this acts on the complete physical form domain (F36–F37). The derivative primitive has exact norm identity `||p_X||^2 = 1/Delta_L` in its stated original pairing (F42).

The heat result uses the open circle `|xi| < 1/55`, all original boxes and every dimensionless time `tau >= 0`, with `tau = kappa t`. Its matrix row-norm remainder beyond the unchanged coefficients of degrees zero, two and four is bounded by `(67896/169) exp(-13 tau/8) (55|xi|)^6 / (1-(55|xi|)^2)` (H12–H13). The signed leakage integral retains its cross term and has rational prefactor `5156090136/3570125` (H15–H18).

The full complementary operator has domain `Dom(A) intersect Q H0` and a bounded inverse justified in H25. H26 preserves both the full energy reduction and restored state metric. At `g^2 >= 13`, every original box has complementary energy loss and state-metric increase strictly below `1/2000`, and observed state fraction strictly above `999/1000`; at `g^2 >= 16`, both complementary corrections are below `1/25000` (H5, H27–H30). H31–H34 retain support quotients, their mixed Schur blocks, the physical heat horizon, and the fixed-spacing spatial limit.

## Supplied evidence and fresh checks

The supplied execution record reports 30 runs, including both producer modes, 321 complete channel-polynomial identities per mode, 5,726 primal/dual certificates per mode, and 14 intended corruption rejections. Fresh provenance checking matched all 60 supplied stdout/stderr hashes and the declared rejection diagnostics. This validates consistency of the supplied records; those 30 executions were not repeated during publication intake.

Fresh local execution ran the manifest check before and after the two fast replay modes:

| Fresh check | Result | Scope |
| --- | --- | --- |
| Manifest before and after | Pass, 2,767 listed files each | All listed lengths and SHA-256 hashes, UTF-8 decoding, complete file membership |
| Ordinary fast replay | Pass, 51 named checks and 11 false-formula controls | Pinned inputs, 662 bound rows through 124,864 anchors, 316 integer tensor calculations, endpoint/heat/complement rational arithmetic, saved-receipt equality |
| Optimized fast replay (`-O`) | Same pass and byte-identical fresh stdout | Acceptance does not depend on Python `assert` statements |

The fresh processes ran serially, with single-CPU affinity requested and no child process observed. The largest sampled process-tree resident set was 224,387,072 bytes, below 512 MiB. A 480 MiB sampled stop threshold and a 180-second per-process timeout were used. Full producer regeneration, the full channel-polynomial/dual-audit replay, the inherited quartic replay, and Lean were not run. The fast replay seals the supplied full-audit records by source hashes; it does not independently recompute their polynomial identities or all primal/dual certificates.

No concrete mathematical or source-preservation discrepancy was identified by this bounded intake. This statement is limited to the manuscript reading, byte comparisons and executed finite checks described here.

## Public-package screening and scope

A read-only filename and content scan found no concrete credentials, private keys, personal home paths, email addresses, credential-bearing URLs, or private identifiers requiring exclusion or redaction. The package includes historical research workflow documents, six preserved `AGENTS.md` copies, an earlier assistant report, local `/mnt/data` and `/tmp` paths, and sandbox download links. These are archived provenance; they were not adopted as current instructions and do not contain an identified secret. Pattern screening cannot certify the absence of every possible sensitive string.

Human attribution remains to Schuette, Zheng Weihong and Hamer for the exponential-vacuum/character/Casimir antecedents, Eymard for the Fourier-algebra antecedent, and Lumer–Phillips for the semigroup theorem used after the stated domain/range checks. No historical-priority or independent external-validation claim is added.

The continuum restriction is explicit in H7. On `a_n = a0 2^(-n)`, `g_n^2 = 1/c_n`, `c_n = g0^(-2) + beta n log 2`, the source domain requires `c_n <= 2 sqrt(alpha5)` and the heat circle requires `c_n < 2/sqrt(55)`. For `beta > 0` the path eventually leaves both. A nontrivial four-dimensional continuum field and finite positive continuum mass remain unestablished. The missing sixth-source catalogue is not declared recovered.
