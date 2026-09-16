# Independent audit of the cubic source and linearized finite-box return

Date: 2026-09-16. Audit actor: an isolated subagent, supplied the raw source files and asked to derive the critical implications. The delivered numerical checker was read as evidence; it was not used as the definition of the mathematical objects. No imported source was edited, and no Lean process was started. This is a mathematical audit with exact finite calculations, not an external peer review or a formal proof-assistant certificate.

## Claim and primary verdict

**Verdict: proved as written**, for the central claim specified here: the original finite-box SU(2) operator C1 has the complete third logarithmic-vacuum coefficient C14–20, the bound C23, and the closed-interval physical spectral estimate L22 with the stated parameter transformation. The fourth energy coefficient C24 and the analytic remainder L29 follow from the same construction. The verdict does not extend to a continuum mass gap, historical priority, or the external bibliographical comparisons in L8.

The quantified objects are every integer L >= 2; the original edges and plaquettes contained in {-L,...,L}^3; the original product Haar probability; invariance under every vertex gauge transformation, including boundary vertices; a > 0; g > 0; kappa=2g^2/a; and x=xi=1/(4g^4). Let alpha be the first positive zero of

    D(x)=[46457856x^4+183150656x^3+18324072x^2
          -1168128x+13689]/13689.

Then, for 0 < x <= alpha, the bottom of the original physical spectrum above its unit positive vacuum obeys

    Delta_L >= kappa[(3/2)(1+sqrt(D(x)))+(1136/13)x^2].

In particular, 0.0170787544707772675 < alpha < 0.0170787544707772677 and

    3.825973052393385 < 1/(2sqrt(alpha)) < 3.825973052393386.

All norms on coefficients below are the auxiliary norms of C4; none is substituted for the physical vacuum pairing. The actual physical ground-state transform and its weighted form supply the return to the physical spectrum.

## Exact source identity and locators

Source directory:

    yang-mills/continuations/20260916-cubic-linearized/

SHA-256 identities at audit time:

| File | SHA-256 |
| --- | --- |
| CUBIC_SOURCE.md | d1e8fa24ce573ad1adfdaeecbb2ee6bfa1631717f9ce22b0f66d838981d5f240 |
| LINEARIZED_RETURN.md | 931d8d2824062c6435dfe324cb9145bc6d8e7a450d37aa5f86a94f1190190453 |
| coordinate_audit.py | de1d9841ebd4655194801cc053bc1f71393433e8c241d0d88cdae65fc82f7c9f |
| geometry.py | bd878efd339f05f320d051bee760bff0934ccfca10e9a2c1e6f26941a128cc1e |

Important locators: CUBIC_SOURCE.md lines 5–61 (operator, source, coefficient norms, spin budgets), 63–97 (loop norms and second coefficient), 113–172 (complete cubic table), 174–210 (cubic bound), 214–245 (fourth energy coefficient). LINEARIZED_RETURN.md lines 5–27 (evaluated spin budgets), 29–63 (exact residual), 65–123 (inverse, convergence, vacuum identification), 155–195 (entire physical spectrum), 211–235 (source quotients and physical defect), 237–249 (energy remainder), and 285–295 (explicit continuum limitation).

## Dependency graph

1. Original SU(2) product representation and invariant vertex tensors -> c(j)>=6j_e, total-spin bound, and physical nonconstant c(j)>=3.
2. Original trace-matrix multiplication, irreducible decomposition, and generator norm -> C6 -> bilinear bounds C7.
3. Original four-link characters and Haar edge integration -> C8–11 -> complete v_2.
4. The original Casimir product rule, quaternion harmonic decomposition, and three-spin singlet sum -> all five connected v_3 families C14–20.
5. Original loop norm bounds plus an exhaustive finite enumeration of original local incidences -> C21–23.
6. Evaluated v_1/v_2 spin budgets and v_3 -> ell and delta -> Neumann inverse and convergent Catalan correction, including the endpoint.
7. Finite-box coefficient convergence -> C^2 original source -> positive smooth original vacuum and exact ground-state form identity.
8. Original point-spin budget plus Peter–Weyl regularity of every finite-box eigenfunction -> blockwise eigenvalue inequality -> full physical form gap L22.
9. Center symmetry, Haar orthogonality, and the constructed analytic vacuum -> C24 and L29.

The leaves in this graph are internal coordinate/representation calculations, standard compact-group Fourier and elliptic facts, and the explicit finite incidence calculation. L8 literature comparisons are not dependencies of this graph and were not independently verified in this bounded audit.

## Obligation matrix

| Obligation | Status | Evidence |
| --- | --- | --- |
| Original orientations, signs and generator scaling | Passed | C1 and the exact identity K(fh)=(Kf)h+f(Kh)-2Gamma(f,h). |
| Gauge restriction and physical free Casimir floor | Passed | Endpoint intertwiner inequalities and triangle-free cubic incidence, reconstructed below. |
| Complete spin multiplicities and coefficient product bounds | Passed | Unitary decomposition, pinching, partial trace, and trace-norm duality. |
| Repeated-pair lower-spin cancellation | Passed | Exact three-channel calculation below. |
| Common-edge multiplicity space | Passed | Singlet sum uses the full total-spin-1/2 isotypic space; no false commutativity assumption. |
| All cubic support types and incidence counts | Passed | Original face geometry and a separate exhaustive finite original-coordinate enumeration. |
| Endpoint convergence | Passed | Catalan series has summable endpoint coefficients and the displayed telescoping tail. |
| Vacuum versus coefficient majorant | Passed | Direct original-operator differentiation and the full ground-state form identity. |
| Return to every physical excitation | Passed | Smooth eigenfunctions have the required weighted Fourier summability; no trial-space lower bound is used. |
| L6 conditional-kernel terminology | Passed with definition clarification | Operators must mean the operators of the respective restricted forms; the statement does not assert invariance under the full scalar generator. |
| Quartic energy sign and extensive factors | Passed | Independent Rayleigh–Schrodinger derivation below. |
| Exact interval arithmetic in L17 | Passed | Separate Fraction calculation; source checker not imported. |
| Primary-source parameter comparisons in L8 | Out of scope | Not needed for the central theorem; do not upgrade these citations from this audit. |
| Continuum existence or finite positive continuum mass | Out of scope | Explicitly disclaimed in L9; the running weak-coupling path eventually leaves this domain. |

## Independent derivation of the critical steps

### 1. Gauge spin budgets and the bilinear operation

Fix an edge e with endpoint vertices v and w in a nonzero gauge-invariant Fourier block. At v, the tensor factor of spin j_e must couple with the other incident spins to spin zero. Thus j_e is at most their sum. The same holds at w. The set A_e of all those other incident edges has total spin at least 2j_e. Their remote endpoints are pairwise distinct: otherwise either two graph edges coincide or a triangle occurs, and neither is possible in the original cubic graph. Apply the invariant-tensor inequality at each remote endpoint. Every edge outside A_e union {e} is counted at most twice. Consequently

    sum_(f in A_e) j_f <= 2 sum_(f outside A_e union {e}) j_f.

Adding j_e, the A_e sum, and its exterior sum gives sum_f j_f >= 4j_e. Every nonzero half-integer spin satisfies j(j+1)>=3j/2. Hence c(j)>=6j_e, sum_f j_f<=2c(j)/3, and any nonconstant physical block has c(j)>=3.

For multiplication, A tensor B is transformed unitarily into the irreducible decomposition. Pinching retains the diagonal irreducible blocks, and partial trace retains all multiplicity contributions. The aggregate output trace norm is at most ||A||_1||B||_1. The partial-trace estimate holds for arbitrary matrices, not only positive ones: by trace-norm duality,

    |Tr[Z Tr_m(A)]|=|Tr[(Z tensor I_m)A]|<=||A||_1

for every ||Z||op<=1. The spin-j generator has operator norm j, so a link derivative costs j. Sum all three generator indices. For an anchor in the first input union, the derivative-pair sum costs at most 3m(f)t(h); interchanging inputs covers anchors in the second union. The output Casimir weight cancels the exact nonconstant inverse Casimir. This proves C7 and its constant 2/3 without assuming an equivalence with the physical Hilbert norm.

### 2. Original second coefficient and cubic channels

The original Leibniz rule gives

    2Gamma(f,h)=(c_f+c_h)fh-K(fh)

for original Casimir eigenfunctions. A plaquette has c=3. Its square is 1+chi_1 with nonconstant c=8. For an adjacent pair the two shared-edge channels have c=9/2,13/2. Applying K^(-1)Q_H to Gamma(S/3,S/3), retaining the two ordered appearances of distinct plaquettes, gives exactly

    v_2=-(1/72)sum_p chi_1(Omega_p)
         +sum_{unordered adjacent {p,q}}[(1/27)P_0(W_pW_q)
                                         -(1/117)P_1(W_pW_q)].

For a self triple, W chi_1=chi_(3/2)+W. The multiplier in 2B(W/3,-chi_1/72) on an output Casimir c is -(11-c)/(216c). At c=3 and c=15 this is -1/81 and 1/810, respectively.

For a repeated adjacent triple, write F=(W_p^2-1)W_q and z=P_0(W_pW_q). In an original shared-edge quaternion u, write W_p=2u dot v and W_q=2u dot w, with v,w unit. The degree-one harmonic projection of (u dot v)^2(u dot w) is [u dot w+2(v dot w)(u dot v)]/6. Therefore

    H=P_(1/2)F=(4/3)W_p z-(1/3)W_q,
    J=P_(3/2)F=F-H,
    W_p z=(3H+W_q)/4,
    W_p P_1(W_pW_q)=H/4+J+3W_q/4.

The K v_3 coefficients are

    H: -1/72-1/2808-1/108=-11/468,
    J: 5/702+1/216=11/936,
    W_q: 1/72-1/72=0.

Dividing the nonzero channels by their original Casimirs 9 and 12 gives C15. The zero lower component is an actual cancellation, not an omitted support.

For a distinct path, the two inner-pair possibilities give, on channel (s,t),

    [a_s(3+c_s-c)+a_t(3+c_t-c)]/(3c),
    (c_0,a_0)=(9/2,1/27), (c_1,a_1)=(13/2,-1/117),
    c=6+2(s+t).

This produces 1/162, -11/8424, -11/8424, 1/3510 on (0,0),(0,1),(1,0),(1,1).

For a common edge, the three original spin-1/2 pair-singlet projectors satisfy

    sum_(i<j) P_0^(ij)=3/4-sum_(i<j)J_i dot J_j
                       =9/8-(1/2)J_total^2.

It therefore has eigenvalues 3/2 and 0 on the complete total-spin-1/2 and total-spin-3/2 spaces. The complementary pair-triplet sum has eigenvalues 3/2 and 3. Substitution in the same Casimir multiplier gives -2/1755 at c=15/2 and 2/2457 at c=21/2. This preserves both spin-1/2 copies and does not multiply noncommuting pair projectors.

For a cube corner, the three independent shared-edge channels give c=9/2+2n. There are 3-n pair-singlet contributions and n pair-triplet contributions. The coefficient is

    [(3-n)a_0(3+c_0-c)+n a_1(3+c_1-c)]/(3c),

which yields 2/81,34/13689,-38/17901,2/2457. At n=1 the central vertex would carry spins (1,0,0), so the gauge-invariant projection is identically zero. For n=0, integrate the original shared-edge words successively: two integrations give factors 1/2 and the last trace is conjugation invariant. The surviving boundary loop therefore has coefficient 1/4.

Disconnected triples contribute zero because their outer and inner active derivative supports do not meet, or their inner second coefficient is zero. The connected three-face adjacency graph is a path or a triangle. Original cubic geometry gives only common-edge triangles and three-face cube corners. Together with repeated faces, these are precisely the five displayed families.

### 3. Norm bounds and exhaustive original incidences

For a simple loop with ell edges and t extrema pairs relative to n_1+n_2+n_3, row/column index permutations expose ell-2t identity contractions and 2t alternating contractions. The identities each contribute trace norm 2, while each alternating contraction has its single nonzero singular value sqrt(2). Thus the trace norm is 2^(ell-t). For spin j plaquettes the same calculation gives (2j+1)^3. The particular values 8,27,64 and the six/eight-link bounds in C8–9 follow with the original edge orientations retained.

For path projections x_st, aggregate pinching gives sum x_st<=512; one shared-edge integration gives x_00+x_01<=128 and x_00+x_10<=128; two give x_00<=32. The channel-weighted absolute sum equals

    [3 sum x_st+8(x_00+x_01)+8(x_00+x_10)+20x_00]/1053
    <=1408/351.

For a corner, the all-zero channel has norm at most 8; the n=1 channel is zero; and the n=2,3 weighted absolute coefficients are at most 19/1053. This gives (19*512+98*8)/1053=3504/351. The remaining family bounds are directly 40/27,66/13,512/117.

The separate calculation file constructs each original plaquette from four endpoint pairs. It does not import geometry.py. A connected triple whose edge union contains the anchor contains an anchor plaquette p, an adjacent q, and a third plaquette adjacent to p or q. Conversely that generation produces a connected triple. Every such face lies within two face-adjacency steps of an anchor face; coordinate bases in [-3,3]^3 include every possibility. Exact set enumeration therefore exhausts the infinite-grid local problem, and finite-box clusters inject into it. The resulting counts are four anchor self triples, 42 adjacent pairs and their two repeated choices, 460 paths, 40 common-edge triples, and 24 corners. It follows that

    ||v_3||loc <=4*(40/27)+84*(66/13)+460*(1408/351)
                 +40*(512/117)+24*(3504/351)=944984/351.

### 4. Nonlinear source at the closed endpoint

The second-source budgets follow directly from the same channels: m(v_2)<=5834/39 and t(v_2)<=137/6. In particular the shared-edge spin-zero channel contributes zero to the anchor's point-spin budget. The resulting constants are

    ell=(128/3)x+(3132/13)x^2,
    delta=(944984/351)x^3+(799258/39)x^4.

These are bounds on the actual J_2=2B(q_2,.) and R_2=x^3v_3+x^4B(v_2,v_2). Expanding (1-ell)^2-(8/3)delta gives the displayed D exactly. D'' is positive for x>=0, D'(171/10000)<0, and D has opposite signs at 17/1000 and 171/10000; hence its first zero is unique in that interval, D>=0 before it, and ell<1 there.

The Neumann series of the actual J_2 is therefore absolutely convergent. After applying its inverse, the equation is w=z+C(w,w), with ||z||<=delta/(1-ell) and bilinear norm at most c_*=(2/3)/(1-ell). The binary-tree series has term bound Catalan_(n-1)c_*^(n-1)z_*^n. With theta=4c_*z_*<=1, its total equals the stated w_* bound. At theta=1, Catalan_n/4^n=2(b_n-b_(n+1)), where b_n=binom(2n,n)/4^n. The tail after N terms is bounded by

    [3(1-ell)/4]theta^(N+1)b_N.

This proves endpoint convergence directly. No strict-contraction assertion at the endpoint is needed.

At fixed finite L, the coefficient space is a finite collection of support-labelled weighted trace-matrix l1 spaces; the physical subspace is closed. Its global c-weighted sum is bounded by |E_L| times its local norm. First derivatives cost j_e<=c and second derivatives cost j_e j_f<=c, including both derivatives on one edge. Thus the source sum is C^2 on the original compact product. Direct differentiation proves H exp(v+c_L)=E_0 exp(v+c_L). Real source coefficients give a real v and hence a positive exponential. Elliptic regularity makes it smooth. The exact identity

    q_(H-E_0)(psi h)=kappa integral psi^2 sum_i |X_i h|^2

extends from smooth functions to the original form domain because multiplication and division by positive smooth psi preserve H^1. It proves that E_0 is the lowest energy and that its eigenspace is one-dimensional: equality forces all derivatives of h to vanish on the connected compact product. No gap was presumed to construct the vacuum.

### 5. Return to every physical spectral block

For the original drift D_v=2Gamma(v,.), the complete trace-norm product inequality gives

    ||D_v h||_X <=6t(v) sum_j(sum_e j_e)||A_j(h)||_1
                 <=4t(v)||Kh||_X.

The evaluated v_1/v_2 budgets and w_* give exactly

    4t(v)<=chi(x)=(1/2)(1-sqrt(D(x)))-(1136/39)x^2.

Let A f=lambda f be any actual physical eigenfunction with lambda>0, where A=psi^(-1)(H-E_0)psi. It has rho-mean zero. Then h=Q_Hf is nonzero and f=h-<h>rho. These maps are literal inverse maps on the stated centered spaces. They give

    (K-lambda/kappa)h=Q_H D_vh.

Every such eigenfunction is smooth by compact elliptic regularity. For completeness, if f_j=Tr(A_j pi_j) and d_j=dim(pi_j), Peter–Weyl gives the weighted square sum sum_j (1+c(j))^s||A_j||HS^2/d_j<infinity for every s. Since ||A_j||_1<=sqrt(d_j)||A_j||HS, Cauchy–Schwarz bounds sum c(j)||A_j||_1 by that square sum times the square root of sum c(j)^2d_j^2(1+c(j))^(-s). The latter is finite for sufficiently large s on this fixed finite product. Thus the X-norm inequalities apply to every actual eigenfunction.

For 0<lambda/kappa<3, each nonconstant physical block has c>=3, and therefore

    ||(K-lambda/kappa)h||_X
      >=[1-lambda/(3kappa)]||Kh||_X.

The drift bound forces lambda>=3kappa(1-chi). Eigenvalues already at least 3kappa satisfy that inequality automatically. Compact spectral resolution then gives the same lower bound on the entire centered physical form domain, which is exactly L22. The equality ||p_X||^2=1/Delta_L in L28 follows from the variational characterization of that first positive eigenvalue, with the original weighted gradient norm.

### 6. Fourth energy coefficient and all higher terms

In an intermediate-normalized wavefunction u=1+xu_1+x^2u_2+..., the original K-xS eigen-equation gives u_1=S/3, e_2=-M/3, and u_2=K^(-1)Q_HS^2/3. The order-three equation is K u_3-Su_2=e_2u_1; test it against S, using KS=3S. The constant order-four equation is e_4=-<S,u_3>. Together these give

    e_4=M^2/27-(1/9)<Q_H S^2,K^(-1)Q_H S^2>.

The self term contributes M/8. A distinct nonadjacent unordered pair contributes 4/6=2/3. An adjacent pair contributes

    4[(1/4)/(9/2)+(3/4)/(13/2)]=80/117=2/3+2/117.

Cross terms vanish by an odd-occurrence original edge, or by distinct spin sectors. Hence the inner product is M/8+(2/3)binom(M,2)+(2/117)J, and substitution yields e_4=5M/216-2J/1053 with its original sign and extensive factors.

The original link-center sign changes every plaquette trace, commutes with K, and preserves Haar. It sends v_n to (-1)^nv_n, so the nontrivial vacuum energy part is even. On |x|=1/60, the majorant gives ||v||loc<7/10 and |X_(e,alpha)v|<=||v||loc/6. Consequently |C_L(x)|<49|E_L|/1200. Cauchy bounds on the even coefficients and a geometric sum from order six give exactly L29. This is a bound on every omitted order, not an identification of a truncated polynomial with the exact energy.

## Conditional-kernel clarification in L6

LINEARIZED_RETURN.md:235 should be interpreted with its own phrase “closed restricted form.” For P the original vacuum conditional expectation and G gauge averaging, let K_0=ker P. The scalar operator is the operator D associated with the restriction of the weighted Dirichlet form to K_0; the physical operator is the corresponding restriction to K_0 intersect Ran G. If PG=GP and the conditional coordinate algebra is gauge stable, gauge invariance of the form makes G a reducing projection for this restricted form, so the inclusion I obeys DI=ID_phys and intertwines the corresponding resolvents. This is the exact relation that supports the text. It does not claim that K_0 is invariant under the unrestricted scalar generator A. Gauge covariance of the original conditional integrals supplies PG=GP for the original loop-observation setting; an arbitrary unspecified conditional expectation would not automatically have that property. This clarification is ancillary to, and does not weaken, the full physical spectral bound L22.

Here is the full original-coordinate proof, independently checked in a subsidiary audit. For the original loop edges V_1,...,V_ell, use the global smooth coordinates

    Omega=V_1...V_ell, g_j=V_1...V_j (1<=j<ell), Z=U_(C^c).

Their inverse is V_1=g_1, V_j=g_(j-1)^(-1)g_j for 2<=j<ell, and V_ell=g_(ell-1)^(-1)Omega, retaining the actual traversed-link inversions in V_j. Successive Haar changes of variables give product measure dOmega product_j dg_j dZ. For the observation (Omega,Z), the actual conditional integral is

    Ef(Omega,Z)= [integral f(Omega,g,Z)rho(Omega,g,Z) product_j dg_j]
                 /[integral rho(Omega,g,Z) product_j dg_j].

Under an original vertex gauge transformation a, the coordinates transform as

    Omega -> a_(v_0) Omega a_(v_0)^(-1),
    g_j -> a_(v_0)g_j a_(v_j)^(-1),

and Z transforms by its unchanged original edge action. Every fiber map preserves product Haar measure. Since rho is invariant, changing those variables proves E T_a=T_a^base E. For cylinder inclusion J, direct composition gives J T_a^base=T_a J. Consequently P=JE commutes with T_a and therefore with G. The same proof applies when the observation is Omega alone, by including Z in the integrated variables.

The coordinate transformation and rho are smooth, rho is strictly positive, and all manifolds here are compact. Differentiating numerator and denominator under the compact fiber integral, followed by Cauchy–Schwarz and finite upper/lower smooth coefficient bounds, proves that P preserves smooth functions and is bounded on H^1. Thus (I-P)C^infinity is dense in H^1 intersect K_0; G(I-P)C^infinity is dense in its physical part. The corresponding restricted forms are densely defined and closed. This resolves the domain point needed for their self-adjoint associated operators.

Let q denote the original weighted Dirichlet form. Gauge invariance implies q(Gu,v)=q(u,Gv). For u in Dom(D_phys) and v in H^1 intersect K_0, the defining form identity gives

    q(Iu,v)=q(u,Gv)=<D_phys u,Gv>rho=<I D_phys u,v>rho.

The characterization of the operator associated with q restricted to K_0 proves Iu in Dom(D) and DIu=I D_phys u. Conversely, testing the defining identity for D only against physical vectors proves

    Dom(D_phys)=Dom(D) intersect K_phys.

It follows that the physical part reduces D and

    (D+s)^(-1)I=I(D_phys+s)^(-1)

whenever those inverses exist. At zero shift, every h in K_0 has rho-mean zero, and the original compact scalar Poincare inequality with smooth positive rho ensures the scalar inverse exists. For the physical part, L22 gives D_phys>=kappa d(x), so

    ||D_phys^(-1)r||rho <=||r||rho/[kappa d(x)],
    q(D_phys^(-1)r,D_phys^(-1)r)<=||r||rho^2/[kappa d(x)].

The corresponding gradient primitive norm is bounded by 1/sqrt(kappa d(x)); its square is the inverse-gap bound in L28. Thus the distinction between the primitive norm and its square is retained.

The exact relation to the unrestricted original transformed generator is instead

    u in Dom(A) intersect K_0 => u in Dom(D), D u=(I-P)A u.

There is no assertion here that P commutes with A. The antecedent definition explicitly uses this form compression: yang-mills/continuations/20260915-gauge-native-band/RESEARCH_NOTE.md:306–314. This subsidiary check did not change imported source files.

## Computation and verification scope

Separate calculation:

    python yang-mills/consolidation/20260916/audits/cubic_calculations.py

The script imports no supplied code. It uses exact Fraction arithmetic for channel coefficients, the cubic norm sum, D(1/64), endpoint signs, and rational squared comparisons for the g^2 bracket. It reconstructs plaquettes as endpoint-pair edges and exhaustively counts local connected triples. Its output is saved as cubic_calculations.json.

The supplied coordinate_audit.py itself samples selected motifs in its direct entry point; verify.py is the separate driver responsible for the claimed 612-multiset exhaustive finite geometry regression. Even two exact assignments per support are not a polynomial-identity proof. The universal identities above follow from the full Casimir, Haar, and spin arguments; the finite source-checker assignments are additional regressions. Fresh replay of the full supplied checker is recorded separately in ../VALIDATION.md.

## Strongest supported content and remaining scope

No counterexample or failed implication was found in the central finite-box cubic/linearized proof, and the critical implications have been reconstructed above. The supported statement is the explicit strong-coupling finite-box theorem, uniform in L through its original kappa=2g^2/a factor, with the analytic vacuum and energy estimates. It does not construct a nontrivial continuum field or a finite positive continuum mass. The asserted running path with positive beta eventually violates x<=alpha exactly as L9 records.

For consolidation, retain the raw files and their hashes, include the exact finite-check outputs as computational evidence, and keep the literature-comparison and continuum labels separate from the proved finite-box result. The cheapest useful additional verification is the already-assigned full supplied-checker replay; this audit does not require a new mathematical assumption or a human approval gate.
