# S6-reduced triality-to-profile bridge for the Yang–Mills gapless-state programme

**Date:** 30 September 2026
**Status:** complete proof of a corrected classical bundle morphism, its interaction core, and its exact source obstruction. This continuation does not construct a quantum state or settle the four-dimensional Yang–Mills mass-gap problem.

## Programme goal

The programme goal is to construct a globally smooth, interacting, gapless state within the stated four-dimensional Yang–Mills axioms and then derive the resulting contradiction of the mass-gap statement. That is the research goal. It is not a conclusion of this continuation.

The role of the present result is narrower and exact. It replaces an invalid chart-supported profile with a global fibrewise polynomial map from the retained rank-24 triality bundle. It then calculates the first interaction core and shows exactly why that core is not yet source-free.

![The retained bundle, moment maps, spatial profile and source defect](figures/S6_NS_MOMENT_MAP_BRIDGE.png)

*The retained nontrivial `Sp(1)` reduction supplies quaternionic line coordinates. Three equivariant quadratic moment maps convert those coordinates into three colour directions; three compactly supported curls convert them into spatial directions. The resulting core has nonzero commutator curvature and the displayed nonzero Yang–Mills source. The figure source is [s6_ns_moment_map_bridge_figure.py](figures/s6_ns_moment_map_bridge_figure.py).*

## Result proved here

Let \(X\cong S^6\), let \(P_H\to X\) be the retained pulled-back principal \(\operatorname{Sp}(1)\)-bundle, and write

\[
 \mathcal A_H=P_H\times_{\operatorname{Ad}}\operatorname{Im}\mathbb H,
 \qquad
 \mathcal L_H=P_H\times_L\mathbb H.
\]

The retained rank-24 bundle has the exact labelled splitting

\[
 \mathcal W_H\cong
 \mathbb R^5_{\mathrm{triv}}\oplus
 \mathcal A_H\oplus
 \mathcal L_{q,1}\oplus\mathcal L_{q,2}\oplus
 \mathcal L_{p,1}\oplus\mathcal L_{p,2}.
\]

The complete proof establishes four linked facts.

1. **The linear obstruction is exact.** Fibrewise,

   \[
   \operatorname{Hom}_{\operatorname{Sp}(1)}
   \bigl(\mathbb R^5_{\mathrm{triv}}\oplus
   \operatorname{Im}\mathbb H_{\operatorname{Ad}}\oplus
   \mathbb H_L^{\oplus4},
   \operatorname{Im}\mathbb H_{\operatorname{Ad}}\bigr)
   =\mathbb R\,\pi_{\operatorname{Ad}}.
   \]

   Every equivariant linear profile map therefore has one colour direction, so its commutator curvature vanishes.

2. **Quadratic moment maps overcome that obstruction.** For \(e\in\{\mathbf i,\mathbf j,\mathbf k\}\),

   \[
   \mu_e(a)=ae\bar a
   \]

   is \(\operatorname{Sp}(1)\)-equivariant and obeys

   \[
   |\mu_e(a)|=|a|^2,
   \qquad
   D\mu_e(a)D\mu_e(a)^{\mathsf T}=4|a|^2I_3,
   \qquad
   \det\!\bigl(D\mu_eD\mu_e^{\mathsf T}\bigr)=64|a|^6.
   \]

   Thus its differential has rank three away from the zero coordinate and rank zero at zero.

3. **The required global bundle morphism exists.** Choose the three compactly supported divergence-free curls \(w^{(1)},w^{(2)},w^{(3)}\) given in [PROOF.md](PROOF.md). With \(\zeta\) denoting every retained coordinate outside the four labelled quaternionic lines, define

   \[
   \mathcal M_H(\zeta;\alpha,\beta;\gamma,\delta)
   =\boldsymbol\mu_{\mathbf i}(\alpha)\otimes w^{(1)}
   +\boldsymbol\mu_{\mathbf j}(\beta)\otimes w^{(2)}
   +\boldsymbol\mu_{\mathbf k}(\gamma)\otimes w^{(3)}.
   \]

   This is a globally defined smooth fibrewise polynomial morphism from \(\mathcal W_H\) to compactly supported \(\mathcal A_H\)-valued divergence-free spatial profiles. Its zero set is the rank-12 subbundle retaining \(\mathcal V_{r,H}\) and the unused line \(\mathcal L_{p,2}\). Where exactly \(m\) of \(\alpha,\beta,\gamma\) are nonzero, its vertical differential has rank \(3m\).

4. **The first three-colour core is interacting and sourced.** On the constant-cutoff core at \(\alpha=\beta=\gamma=1\), the quaternionic potential components are \((\mathbf i,\mathbf j,\mathbf k)\), so

   \[
   \mathcal F_{12}=2\mathbf k,
   \qquad
   \mathcal F_{23}=2\mathbf i,
   \qquad
   \mathcal F_{31}=2\mathbf j.
   \]

   Under the exact Lie-algebra map

   \[
   \varphi(\mathbf i,\mathbf j,\mathbf k)=2(T_1,T_2,T_3),
   \qquad T_a=-\frac{i}{2}\sigma_a,
   \]

   this becomes

   \[
   F_{12}=4T_3,
   \qquad F_{23}=4T_1,
   \qquad F_{31}=4T_2,
   \]

   with magnetic density \(48\). The covariant source is

   \[
   \mathcal J=(-8\mathbf i,-8\mathbf j,-8\mathbf k),
   \qquad
   D^\mu F_{\mu j}=-16T_j.
   \]

The nonzero source is a proved obstruction, and it defines the next object rather than ending the programme:

\[
 \mathfrak C_{\mathcal M_H}
 =\left\{\alpha:\
 D_{\mathcal M_H+\alpha}^{\mu}
 F_{\mu\nu}(\mathcal M_H+\alpha)=0,
 \quad
 [\mathcal M_H+\alpha,\mathcal M_H+\alpha]\not\equiv0,
 \quad
 \text{Gauss, support, boundary, and regularity conditions hold}
 \right\}.
\]

The next calculation is to construct and classify elements of this correction space while retaining the exact bundle transition law, all four quaternionic-line labels, the interaction term, and the stated boundary conditions.

## Corrections to the earlier route

The audit found several scope errors and repaired each affected statement.

- The earlier chart-supported bump profile showed that the receiving profile space was nonempty. It was independent of the rank-24 bundle point and therefore was not the required domain-to-profile map. The map \(\mathcal M_H\) above is the replacement.
- The proved \(\operatorname{Sp}(1)\) reduction is a bundle over \(X\cong S^6\). No reduction of the tangent frame bundle of \(F_4/\operatorname{Spin}(8)\) has been proved.
- The displayed spatial coefficients form a partial connection along the \(\mathbb R^3\) fibres. Components in the \(X\)-directions are still required for a full connection over \(X\times\mathbb R^3\).
- A smooth classical profile is not a physical quantum state. Link holonomy, gauge projection, a nonzero Hilbert-space vector, Hamiltonian dynamics, continuum reconstruction, uniqueness of the vacuum, interaction in the reconstructed theory, and spectral support at arbitrarily small positive energy remain to be constructed.
- The retained Navier–Stokes material supplies regular divergence-free profiles and exact curvature/current formulae. It does not identify fluid time with Yang–Mills Hamiltonian time, and its singular endpoint is excluded from the smooth target.

The complete finding-by-finding record is [CLAIM_LEDGER.md](CLAIM_LEDGER.md), with a compact machine-readable companion in [CURRENT_CLAIM_DISPOSITIONS.json](CURRENT_CLAIM_DISPOSITIONS.json).

## Research programme

The [higher-domain programme](HIGHER_DOMAIN_PROGRAM.md) formalizes the proposed route: identify a domain functionally analogous to the retained \(S^6\) construction, preserve the soft-period and gauge data that matter, map the domain into interacting Yang–Mills profiles, solve the source equations, construct physical states, and test the reconstructed spectrum. The retained 24-dimensional triality carrier is a candidate source of structure; it is not already the desired domain.

The [spectral programme](SPECTRAL_PROGRAM.md) sharpens the “locally gapped, globally gapless” direction found in Claude's assessment. A viable limit must have nonzero continuum spectral weight in every \((0,\varepsilon)\), no second zero-energy vector, a unique vacuum, strong continuity, gauge-invariant local observables, reconstruction axioms, nontrivial interaction, and an exact identification with the theory selected by the original Yang–Mills action. High-energy escape by itself fails to create a nonzero continuum vector.

## Reading order

| Step | File | Purpose |
| --- | --- | --- |
| 1 | [PROOF.md](PROOF.md) | Complete corrected theorem, all maps, ranks, curvature, source calculation, and next correction space. |
| 2 | [SP1_BUNDLE_BRIDGE.md](SP1_BUNDLE_BRIDGE.md) | Retained cusp class, subgroup injection, colour bundle, metric factors, and corrected partial-connection statement. |
| 3 | [HIGHER_DOMAIN_PROGRAM.md](HIGHER_DOMAIN_PROGRAM.md) | Full domain-to-state-to-spectrum programme and the exact role of S6, triality, and regular Navier–Stokes profiles. |
| 4 | [SPECTRAL_PROGRAM.md](SPECTRAL_PROGRAM.md) | Reconstruction requirements and the exact distinction among low-energy weight, a second vacuum, and spectral escape. |
| 5 | [CLAIM_LEDGER.md](CLAIM_LEDGER.md) | Overclaims, underclaims, corrected statements, proof locators, and unresolved consequences. |
| 6 | [SOURCE_PROVENANCE.md](SOURCE_PROVENANCE.md) | Source identity, authorship, hashes, reading coverage, and exact uses. |

## Reproduction

The three symbolic calculations are independent checks of stated coordinate identities. They accompany, and do not replace, the written proofs.

```bash
python checks/verify_sp1_bundle_bridge.py
python checks/verify_sp1_moment_map_bridge.py
python checks/verify_three_colour_curvature.py
python verify_public_package.py
```

The published receipts are:

- [SP1_BUNDLE_BRIDGE_CHECK.json](checks/SP1_BUNDLE_BRIDGE_CHECK.json)
- [SP1_MOMENT_MAP_BRIDGE_CHECK.json](checks/SP1_MOMENT_MAP_BRIDGE_CHECK.json)
- [THREE_COLOUR_CURVATURE_CHECK.json](checks/THREE_COLOUR_CURVATURE_CHECK.json)
- [PUBLIC_VALIDATION.json](PUBLIC_VALIDATION.json)
- [PUBLIC_MANIFEST.json](PUBLIC_MANIFEST.json)

The first three require Python and SymPy. The package verifier uses only Python's standard library. All retained source files used by this continuation are under [sources/](sources/).
