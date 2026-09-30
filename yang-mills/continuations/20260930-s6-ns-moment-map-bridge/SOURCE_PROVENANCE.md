# Source identity, authorship, and reading coverage

## Distinct source roles

The originating S6 construction was circulated by **Levent Alpöge and produced with Claude**. Its public source is linked in the repository's [attribution record](../../../ATTRIBUTION.md#the-s6-construction-and-the-period-dependent-magnetic-branch). The retained higher-rung TeX in this continuation is an exact source snapshot used for the bundle data below. The proofs in [PROOF.md](PROOF.md), [SP1_BUNDLE_BRIDGE.md](SP1_BUNDLE_BRIDGE.md), and the two programme documents are later workbench derivations and audits; they are not attributed to the originating source.

Claude's three retained TeX notes have a different role. They record the assessment of the Yang–Mills source and the suggestion that “locally gapped, globally gapless sequences” form a well-posed direction once a limit satisfying reconstruction axioms is supplied. This continuation audits that assessment, retains the well-posed direction, and sharpens its spectral target.

The Navier–Stokes bridge and the spatial Yang–Mills manuscript supply profile, current, regulator, and spectral-limit data. Their inclusion records the exact mathematical inputs used; it does not transfer any unverified global conclusion from one programme to another.

## Files actually read and used

| Source | SHA-256 | Reading coverage and use |
| --- | --- | --- |
| [s6_higher_rung_24d_preprint.tex](sources/higher_rung/s6_higher_rung_24d_preprint.tex) | `8c526746de9b56a4fcd0a274df0c470092cc82a16e49857df539a1c9d033956f` | Lines 5205–5283 for \(H:X\cong S^6\to S^4\) and \(P_H\); 5285–5398 for the clutching class and \(\mathcal A_H\); 5400–5511 for \(\rho\) and the three actions; 5576–5614 for the associated-bundle convention, \(\mathcal L_H\), and \(\mathcal W_H\); 5645–5792 for the trivial extension and retained nontrivial reduction. |
| [y6_side.tex](sources/claude/y6_side.tex) | `ce00398f45e2a1d2ac25c06c29389c448a0de86bb12c41f73e890af9f914ad22` | Retained comparison note; checked against the source state before deciding which statements were theorem claims and which were research suggestions. |
| [y9_open.tex](sources/claude/y9_open.tex) | `a21350081133a66ea6e0c0720848c50831a893a29f2777dc0ec66dfba46985c0` | Line 12 for the exact closing-gap, escaping-weight, reconstruction question. |
| [y9a_directions.tex](sources/claude/y9a_directions.tex) | `2a1a53ad2245a2ead619b038efd55eca7de1b7a8e48eb08d22ad0df6737fc8eb` | Lines 5–7 for the well-posed-direction assessment. |
| [GAUGE_AND_NAVIER_STOKES_BRIDGE.md](sources/navier_stokes/GAUGE_AND_NAVIER_STOKES_BRIDGE.md) | `c674559b58bc8fc6d519d9484fa6c8752fdb21cb716468b4ecaf0359e279e002` | Lines 69–143 for the Cartan-valued map, curvature/current equations, finite local energy, and the limits of that map. |
| [29_s6_cusp_gauge_spectral_chain.tex](sources/s6_cusp/tex/satellites/29_s6_cusp_gauge_spectral_chain.tex) | `1c09f1847ed5e2c907a02c13f1b63df2174f10afc51749ecfdd8299e5abec47b` | Exact cusp-period, vertical-operator, gauge-quotient, and spectral-chain input used by the higher-domain programme. |
| [29a_native_magnetic_upgrade.tex](sources/s6_cusp/tex/satellites/29a_native_magnetic_upgrade.tex) | `44c773aa483d9b23a5fbce54fb2c82c54d8682007f51b102e78f89c753f853fe` | Native magnetic upgrade and its retained parameter factors. |
| [spatial_continuum.tex](sources/spatial/spatial_continuum.tex) | `e035407b59854b77307ad1bb0021a4f834aa13231ca6028f2b8de5409ab5aba4` | Sections 20–21 and equations 251–256 for the escaping-weight and second-zero-mode obstructions; regulator and physical-space definitions used in the spectral programme. |

The higher-rung source recursively includes the TeX files under [sources/higher_rung/supporting_materials/workbench/research/](sources/higher_rung/supporting_materials/workbench/research/). They are retained byte-for-byte so the source closure remains inspectable.

The external target was checked against the [official Clay Mathematics Institute Yang–Mills problem page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/) on 30 September 2026. That page identifies the problem as unsolved and links the official description by Arthur Jaffe and Edward Witten. No author TeX source is supplied there, so the accessible official page and linked description are recorded as the primary statement rather than represented as part of the retained TeX corpus.

## New derivations and exact receiving calculations

The following claims are derived in this continuation rather than imported from the retained sources:

1. the complete real equivariant Hom-space calculation;
2. the three quadratic maps \(\mu_e(a)=ae\bar a\), their norm identity, differential Gram matrices, determinants, and rank strata;
3. the global associated-bundle morphism \(\mathcal M_H\), its zero subbundle, and its vertical rank stratification;
4. the core curvatures, magnetic density \(48\), quaternionic source \((-8\mathbf i,-8\mathbf j,-8\mathbf k)\), and \(SU(2)\) source \(-16T_j\);
5. the correction space determined by that source obstruction;
6. the precise reconstructed spectral target that distinguishes continuous support at zero from vacuum degeneracy and high-energy escape.

Their complete proofs and exact limitations are in [PROOF.md](PROOF.md) and [SPECTRAL_PROGRAM.md](SPECTRAL_PROGRAM.md). The machine checks establish the displayed polynomial and matrix identities only; the global bundle arguments remain mathematical proofs in the text.
