# Bounded mathematical audit of the local-fibre continuation

Date: 2026-09-16. This is a read-only audit report, not a source correction,
independent mathematical certification, or a replay of the delivery's checker.
The complete research note and its README were read. The fresh derivations
below concentrate on conditional variance, the zero-shift inverse, the retained
exterior, and the nested minimum sections. No Lean process was started.

## Exact target and primary verdict

**Primary verdict: proved as written**, for the following bounded claim:
at every finite original regulator, the conditional kernel for observation
`(Omega, every exterior link)` has the form lower bound Z19 and inverse Z20;
the stated heat comparison gives the explicit inverse estimate Z22 along the
specified sequence; and the maps and response/norm identities Z51–Z53 connect
that kernel to the earlier Omega-only observation on their actual form domains.

This verdict does **not** certify all numerical constants in Z27–Z50a or the
408-check execution claim. Those have been read and their role examined, but
the absent branch checker and its full exact-arithmetic implementation were
not independently replayed in this audit. No substantive counterexample was
found to the bounded target. Two minor domain qualifications and the material
publication/continuum limitations are recorded below rather than hidden.

Authoritative artifact:

- Repository-relative path:
  `yang-mills/continuations/20260915-zero-shift-local-fibres-review/DELIVERED_RESEARCH_NOTE.md`.
- SHA-256 observed locally:
  `42aa9ab14a4b42ba9d170803fb0f9ce9f0d1d763d10139b3a15f9ba317543e55`.
- This equals the hash printed in README lines 41–42.
- Source locators below refer to the 1,031-line delivered note with this hash.
  README locators refer to its 61-line companion.

The original compact configuration manifold is
`M = SU(2)^E` for the contained positive links of `{-L,...,L}^3`, `L>=2`.
Haar measure is probability measure. All scalar spaces here are complex.
`a,g>0`, `kappa=2g^2/a`, `v=1/(2g^2 a)`, `xi=v/kappa=1/(4g^4)`.
The original derivatives use `T_alpha=-i sigma_alpha/2`, with their original
Casimir eigenvalues and original ordered Wilson words; no coefficients,
orientations, or physical spacings are changed in this audit.

Let `psi` be the smooth strictly positive unit ground state, `rho=psi^2`,
`H_rho=L^2(M,rho dU)`, and `V=H^1(M)`. The weighted and Haar Sobolev spaces
have equivalent norms at this fixed regulator because `rho` is smooth and
bounded above and below by positive numbers. The original form is

\[
 q_\rho(f,h)=\kappa\int_M\rho\sum_{e,\alpha}
                    \overline{X_{e,\alpha}f}X_{e,\alpha}h.
\]

Its multiplication map `f -> psi f` is unitary onto the original physical
configuration Hilbert space before gauge restriction, and maps this form to
the original `H-E0` form. These are the objects audited, rather than a surrogate
matrix or a Haar replacement for the interacting vacuum.

## Dependency graph and obligation matrix

The central implication graph is:

1. Positive smooth vacuum and its original closed form
   -> actual weighted conditional expectations and Sobolev form domains.
2. Original SU(2) heat identity + bounded original local potential
   -> all-configuration conditional-density ratio Z15/Z17.
3. Haar product gap `3/4` + this single density ratio + conditional Fubini
   -> Z19 -> represented self-adjoint `D_l` and bounded inverse Z20.
4. Z17 + the specified original `a_n,c_n,L_n`
   -> Z21/Z22 -> resolvent expansion and direct-sum inverse estimates.
5. Nested conditional expectations + closed coercive kernel forms
   -> minimum sections -> exact additional response Z52 and state norm Z53.

| Obligation | Result | Evidence/limit |
|---|---|---|
| Original heat time, sphere measure, and derivative coefficient | passed | Z6–Z8, lines 68–88; exact [HK] v2 equations inspected and translated below |
| Local/exterior tensor decomposition and semigroup comparison | passed | Z13–Z17, lines 143–200; bounded positive multiplication comparison keeps the entire exterior operator |
| Conditional-mean implication and one-ratio Poincare comparison | passed | Z18–Z19, lines 204–245; reconstructed below |
| Restricted form density, closedness, operator inverse and compactness | passed | lines 247–257; `H^1` stability follows in the displayed global coordinates |
| Sequence exponent, coefficient, and asymptotic inverse bound | passed | Z21–Z22, lines 264–292; direct substitution below |
| Zero-shift resolvent identity and energy-relative remainder | passed | Z23, lines 294–315; reconstructed below |
| Nested observation quotient, second minimizer, response and norm | passed | Z51–Z53, lines 844–893; full derivation below |
| Restriction to gauge-invariant physical vectors | passed | equivariance and uniqueness argument below |
| All individual quaternion/Hessian/support and outward-arithmetic constants | not addressed in full | source read; no independent exhaustive checker replay here |
| Claimed 408 tests, optimization replay, corruption controls | not addressed | historical execution reports, README 48–56; not executions observed by this audit |
| Physical continuum Hilbert space or complete uniform mass gap | out of scope | explicitly not established by source lines 981–988 |
| General [SZ] attribution and historical priority | out of scope | the operator quotient construction is elementary to verify; no broader attribution audit |

## Conditional variance and the actual inverse

Write `C` for the four original loop links and `Z=U_(C^c)`. The global map
Z18 is invertible by the displayed prefix formulas and sends original Haar
measure to `dOmega prod_j dg_j dZ`. Thus it is a genuine global product
coordinate map, including inversely traversed links through their
Haar-preserving inversion maps.

Let `m(Omega,Z)=int rho(Omega,g,Z) dg`. The conditional expectation is

\[
 E_lh(\Omega,Z)=\frac{\int h(\Omega,g,Z)\rho(\Omega,g,Z)\,dg}
                         {m(\Omega,Z)}.
\]

It maps `H_rho` to `H_l=L^2(m dOmega dZ)`; its adjoint is pullback `J_l`.
Fubini proves `E_l J_l=I`, hence `P_l=J_l E_l` is an orthogonal projection
and `K_l=ker E_l` is a closed Hilbert subspace. Smoothness and positivity on
the compact product make every coefficient in the first derivative of this
conditional integral bounded. Differentiating in the global coordinates
proves that `E_l,J_l,P_l,Q_l` preserve the respective `H^1` spaces and smooth
functions. Consequently `V_l=H^1(M) intersect K_l` is form closed, and
`Q_l` applied to smooth approximations proves its form density by smooth
members of `K_l`.

Conditional Fubini gives `E[h|Z]=E[E_lh|Z]=0` for `h in K_l`.
At each fixed `Z`, write `mu_Z=rho(U_C,Z)/int rho(U_C,Z)dU_C` and let
`m_Z,M_Z` be its minimum and maximum. For each complex `H^1` function `h`,

\[
\begin{aligned}
 \operatorname{Var}_{\mu_Z}(h)
 &=\inf_{b\in\mathbb C}\int|h-b|^2\mu_Z\,dU_C\\
 &\le M_Z\operatorname{Var}_{Haar}(h)\\
 &\le\frac{4M_Z}{3}\int\sum_{e\in C,\alpha}|X_{e,\alpha}h|^2\,dU_C\\
 &\le\frac{4M_Z}{3m_Z}
       \int\sum_{e\in C,\alpha}|X_{e,\alpha}h|^2\mu_Z\,dU_C.
\end{aligned}
\]

This uses exactly one density ratio `M_Z/m_Z`. Since `E[h|Z]=0`, integrate
against the unchanged exterior marginal and add the nonnegative exterior
derivative contribution to obtain

\[
 q_\rho(h)\ge\frac34\kappa e^{-H_C}\|h\|_\rho^2
 \qquad(h\in V_l).
\]

No claim that `h` is a function only of the loop was used. In particular,
its dependence on every exterior link survives this inequality.

The operator represented by this restricted form has the exact domain

\[
 \operatorname{Dom}D_l=
 \{h\in V_l:\ \exists r\in K_l\text{ such that }
       q_\rho(v,h)=\langle v,r\rangle_\rho\ \forall v\in V_l\},
 \qquad D_lh=r.
\]

It is positive self-adjoint on `K_l`, with `D_l>=delta_C I` and
`||D_l^(-1)||<=delta_C^(-1)`. Compactness of the finite-regulator embedding
`H^1(M)->L^2(M)` gives its compact resolvent. For smooth `h in K_l`,
`D_lh=Q_l A h`; the form definition is the one needed for nonsmooth vectors.

## Heat comparison, original units, and sequence

The source decomposition `H=kappa K_C+H_ext,C+V_C` has
`0<=V_C<=4v m_C`; `H_ext,C` retains every other derivative and every face
not touching `C`. Positivity of the product heat semigroup and its bounded
potential Trotter factors gives the pointwise comparison Z14. At fixed `Z`
its exterior kernel is common to both loop configurations. Its ratio is
therefore bounded by the product of four original link-kernel ratios, and
the common ground energy factor cancels. Squaring for `rho=psi^2` gives

\[
 \operatorname{osc}_{C\mid C^c}\log\rho
 \le 8m_C\xi\theta+8\pi^2/\theta.
\]

Here `m_C=13`, and the optimized physical time is
`t_*=theta_*/kappa=(pi a/2)sqrt(4/13)`, using the unchanged identity
`kappa v=1/a^2`. Thus the statement retains the original energy and time
scales. Keeping the Z12 heat prefactor yields exactly

\[
 \frac{\sup_{U_C}\rho(U_C,Z)}{\inf_{U_C}\rho(U_C,Z)}
 \le (8c)^{-8}e^{Bc},\quad c=g^{-2}\ge2,
 \quad B=8\pi\sqrt{13}.
\]

For `a_n=a0 2^(-n)`, `c_n=c0+beta n log 2`,
`kappa_n=2^(n+1)/(a0 c_n)`, direct substitution into the preceding
Poincare inequality gives

\[
 \delta_n\ge\frac34\frac{2^{n+1}}{a_0c_n}
                  (8c_n)^8e^{-Bc_n}
 =\frac{3\,8^8}{2a_0}e^{-Bc_0}c_n^7 2^{(1-B\beta)n}.
\]

At exactly `beta=1/B` and `n>=n0` this proves Z22, including its coefficient
and its power seven. The loops have physical side `a_n`; the estimate says
neither that their physical size stays fixed nor that these Hilbert spaces
have already been identified with a continuum field Hilbert space.

For a finite family of smooth retained observations, put
`T=D_l^(-1/2)W`. The original nonnegative coupled form implies
`T^*T=W^*D_l^(-1)W<=K0`: minimize its kernel variable at `D_l^(-1)W x`.
Spectral calculus gives, for `|z|<delta`,

\[
 W^*(D_l-z)^{-1}W=T^*(I-zD_l^{-1})^{-1}T.
\]

Subtract the finite geometric sum inside this formula. The remaining
multiplier has operator norm at most
`(|z|/delta)^(d+1)/(1-|z|/delta)`. Cauchy–Schwarz and `T^*T<=K0` give
exactly Z23. This proves the stated continuation through zero shift; it
does not supply a limit of the individual moments or a physical resolvent
pole. For the elementary trace `K0<=4kappa_n`; at `d=n`, the bound has
logarithm at most `-7(n+1)log c_n+O(n)` on a fixed complex disk. It tends
to minus infinity even while the raw kinetic scale grows.

## Exact exterior map and minimum sections

Let `nu(Omega)=int m(Omega,Z)dZ`, let `E_o:H_l->L^2(nu dOmega)` be
conditional expectation in the exterior variables, and let `J_o` be its
pullback. The Omega-only expectation is `E_C=E_o E_l` and its pullback is
`J_C=J_l J_o`. For every `h in K_C=ker E_C`,

\[
 h=Q_lh+J_lE_lh,\qquad E_lh\in\ker E_o.
\]

Conversely `J_lk in K_C` for `k in ker E_o`. These are orthogonal summands,
so

\[
 K_C=K_l\mathbin{\oplus_{H_\rho}}J_l(\ker E_o).
\]

This proves both inverse laws in Z51; it also proves that the induced map
from the Hilbert quotient `K_C/K_l` is isometric. The same maps preserve
the form domains by the compact smooth-density derivative argument above.

For `g in H_l` with `J_lg in V`, Z19 and closedness make `q_rho` a complete
inner product on `V_l`. Riesz gives the unique `h_l(g) in V_l` satisfying

\[
 q_\rho(v,h_l(g))=-q_\rho(v,J_lg)\quad(v\in V_l).
\]

Thus `S_lg=J_lg+h_l(g)` is form orthogonal to `V_l`, the section is linear,
and it minimizes the energy of the original affine fibre. If `J_lg` is
in `Dom A`, this identity is exactly
`h_l(g)=D_l^(-1)(-Q_l A J_lg)`, including the minus sign.

The second minimizer exists at fixed regulator without assuming any
uniform estimate. Indeed, on the compact original product let
`rho_min=min rho>0`, `rho_max=max rho`. The same single-ratio comparison
with the full product Haar gap proves

\[
 q_\rho(u)\ge\lambda\|u\|_\rho^2,
 \qquad\lambda=\frac{3\kappa}{4}\frac{\rho_{\min}}{\rho_{\max}}>0,
 \qquad\int\rho u=0.
\]

Every `u in K_C` is centered. Riesz on `V intersect K_C` therefore gives
the unique full correction `h_C` minimizing `q_rho(J_Cf+h)` for the
centered loop trace `f`. Define `k_*=E_lh_C`. The orthogonal decomposition
and the first minimum section give

\[
 h_C=J_lk_*+h_l(J_of+k_*).
\]

Hence `k_*` is precisely the minimizing exterior form vector in the note.
For `k in ker E_o` in that coarse form domain,
`q_eff(k)=q_rho(S_lk)>=lambda ||S_lk||^2>=lambda ||k||_m^2`, which also
proves its uniqueness. This argument supplies the full domain/coercivity
justification behind the concise existence assertion at lines 865–868.

Set `x=J_of`. Stationarity gives
`q_eff(x+k_*,k_*)=0`. Expansion, with its complex conjugate, therefore gives

\[
 q_{\rm eff}(x+k_*)=q_{\rm eff}(x)-q_{\rm eff}(k_*).
\]

Subtract from the unchanged `K0=q_rho(J_Cf)` to prove

\[
 M_C(0)=M_l(0)+q_{\rm eff}(k_*),\qquad
 h_C=h_l(J_of)+J_lk_*+h_l(k_*).
\]

For the norm, the vector `a=h_l(J_of)+h_l(k_*)` lies in `K_l`, whereas
`J_Cf` and `J_lk_*` lie in its orthogonal complement. Moreover
`<J_Cf,J_lk_*>_rho=<f,E_ok_*>_nu=0`. Therefore

\[
 \|J_Cf+h_C\|_\rho^2
 =G+\|k_*\|_m^2+
       \|h_l(J_of)+h_l(k_*)\|_\rho^2.
\]

This is Z53 with the source's pullback convention made explicit. The last
term includes its actual cross pairing. The identities prove
`M_l(0)<=M_C(0)<=K0`, but do not imply a monotonicity statement for the
restored state norm.

Gauge transformations act on the observation by conjugating `Omega` at
its base vertex and applying the original endpoint actions to `Z`. On
prefixes they act by `g_j -> h_base g_j h_vertex_j^(-1)`.
These formulas show equivariance of the exact coordinate map. Haar
invariance and gauge invariance of the unique positive vacuum imply that
the conditional expectations intertwine the gauge actions. The original
form is invariant as well, so uniqueness makes both minimum sections
intertwine them. Consequently the entire derivation restricts to the
physical invariant subspaces, and the restored trace state is physical.

## Locatable qualifications and limitations

1. **Form-domain qualification, note lines 782–788, Z48.** The sentence says
   “arbitrary ... h in K_l” before writing two form values. If these are
   finite form values, the domain is `h in H^1 intersect K_l`, as explicitly
   stated for Z49 immediately below. Otherwise both sides require the
   extended-value closed-form convention. This is a local wording omission,
   not a failure of the subsequent bound: `h0 in Dom D_l` and the translation
   `k=h-h0 x` preserve the required form domain.

2. **Nonzero trial qualification, note lines 913–926, Z55.** The formula
   `alpha_Y=<Y,W>/q(Y)` requires a nonzero trial `Y` in the stated smooth
   kernel trial domain. Z19 then gives `q(Y)>0`. The note explicitly checks
   this for its actual `Y0` at lines 924–926, so this does not invalidate
   that application. The general sentence is not meaningful at `Y=0`.

3. **Finite-sector lower bound, note lines 793–819.** Z49 concerns
   `span{f}+(H^1 intersect K_l)`, not the entire physical centered form
   domain. Z50 gives a variational *upper* bound on the complete finite-box
   physical gap. Its direction is correct in the source. The omitted coarse
   directions are explicitly represented by `ker E_o` through Z51; they
   are not proved irrelevant by retaining the exterior.

4. **Different coupling regimes, note lines 319–321 and 981–988.** The
   coefficient enclosures at `xi=10^(-8)` occur at the original
   `g=50 sqrt(2)` and `c=1/5000`. Along the weak-coupling path Z22,
   `c_n -> infinity` and `xi_n=c_n^2/4 -> infinity`. The small-xi
   numerical coefficients therefore do not hold eventually along that
   path by the argument given. The note already separates the two domains;
   consolidation must preserve that separation and the exact dictionaries.

5. **Uncontrolled outer quantity, note lines 860–893 and 996–999.** The
   exact additional response is `q_eff(k_*)>=0`. Its uniform control and
   the corresponding complete restored-state norm on growing physical
   observation families are absent. The calculation above establishes
   an exact relationship, not the desired uniform estimate. No continuum
   physical Hilbert-space or complete positive mass lower bound is claimed.

6. **Publication scope, README 32–39 versus note 3–5 and 1015–1018.** The
   note's inherited description says its Git contribution/checker is
   self-contained, but the companion README expressly limits this branch
   to the proof and guide and says the runnable dependency set is absent.
   Read literally in isolation, the note's checker statement is not true
   of this two-file publication. The README discloses the distinction.
   Checker availability and historical execution success must remain
   distinct from the mathematical derivations in a consolidated reader.

## Source and computation checks

The vacuum/domain dependency was checked in the local original source
`yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md`,
section 1. Its compact elliptic ground-state argument, positivity, gauge
invariance, and multiplication-form identity apply with exactly the Z1
operator and coefficients.

The external heat-kernel leaf was checked against the exact cited primary
version: A. Nowak, P. Sjogren, T. Z. Szarek,
[*Sharp estimates of the spherical heat kernel*, arXiv:1802.09385v2](https://arxiv.org/pdf/1802.09385v2),
dated 2 September 2018, page 2 equations (1)–(2), with the unit-sphere area
measure convention on page 1. The dimension recurrence and periodized
one-dimensional Gaussian translate using `t=theta/4`,
`p_theta=2 pi^2 K^3_(theta/4)`, and
`q_theta^5=pi^3 K^5_(theta/4)`. They give the exact derivative coefficient
`-4 exp(-3 theta/4) sin(r)` in Z7 and the prefactor in Z8. Thus this source
leaf and its measure/time translation pass; no wider novelty claim was
investigated. No third-party source file was added or changed.

Simple rational arithmetic in the response formulas was also recomputed:

\[
 \frac{3/4}{9/2}+\frac{1/4}{13/2}=\frac8{39},\qquad
 \frac{3/4}{(9/2)^2}+\frac{1/4}{(13/2)^2}
 =\frac1{27}+\frac1{169}=\frac{196}{4563},
\]
\[
 \frac34-\frac7{36}-\frac8{39}-3\frac{196}{4563}
 =\frac{337}{1521}.
\]

The Cauchy derivative step Z45 -> Z46 preserves the original disk radius
`kappa/4`, so multiplying the Z43 supremum by `4/kappa` gives the displayed
`104,000,000 xi^4` bound. This confirms the implication between the
displayed enclosures, not an independent derivation of every input to their
constant `C(xi)`.

Commands used for audit were bounded `Get-Content` line reads, `rg --files`
and `rg -n` discovery, and `Get-FileHash -Algorithm SHA256` on the note.
The primary paper was opened through the web tool at the exact version URL.
No original checker, numerical solver, source mutation, or Lean run was
performed. A separate subagent freshly derived Z51–Z53 from the raw source
definitions and form domains; its agreement is supporting review work, not
a mathematical certification by an independent institution.

## Strongest safe statement and next check

The preserved finite-regulator calculation provides an exterior-uniform
local conditional-kernel inverse, an explicit shrinking-loop weak-coupling
sequence on which that inverse tends to zero, and exact response/norm maps
to the larger Omega-only kernel. The numerical response certificate belongs
to its separately stated small-xi regime and to the historical delivery's
own proof/checker evidence record.

For consolidation, the cheapest additional verification is to locate the
complete named local-fibres archive, authenticate its source/checker and
receipt identities against the preserved note, and replay its exact checks
without relabeling that replay as independent analytic proof. The next
mathematical estimate required beyond this branch remains uniform control
of `q_eff(k_*)` and the full Z53 norm on the growing observation families;
the exact operators and maps involved have been exhibited above.
