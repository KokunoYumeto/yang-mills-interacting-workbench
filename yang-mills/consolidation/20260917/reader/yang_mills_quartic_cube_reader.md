---
title: "Fourth-order vacuum sources and sixth-order energy in cubic SU(2) lattice Yang-Mills theory"
subtitle: "A consolidated reader for two exact finite-lattice calculations"
author: "KokunoYumeto"
date: "17 September 2026"
---

# The mathematical problem

This reader brings together two calculations of the fourth coefficient of the logarithmic vacuum and the sixth coefficient of the ground energy for the same finite cubic SU(2) lattice Hamiltonian. Both calculations retain the original links, Haar measure, coupling constants, and open boundary. Their common coefficients are expressed in different coordinate systems. One calculation also supplies bounds on the complete interacting vacuum and physical spectrum, uniform in the size of the finite box. The other supplies explicit signed derivatives of the vacuum coefficients and an independently proved, volume-dependent analytic remainder for the energy.

The purpose of this introduction is to identify the mathematical objects, state the shared results, and explain precisely what each calculation adds. The six proof texts follow in full as Appendices A-F. The introduction is an expository guide to those proofs, not an additional independent analytical verification of them. The associated exact tables and executable evidence are companion material; this volume does not print thousands of polynomial entries. No claim of global historical priority or of a solution of the four-dimensional continuum Yang-Mills problem is made.

## Original lattice and Hamiltonian

Fix an integer $L\geq2$. The vertices are $\{-L,\ldots,L\}^3$; the links are the positively oriented nearest-neighbor edges contained in that box. Let $E_L$ and $P_L$ denote the sets of links and elementary plaquettes, and put $M=|P_L|$. A configuration assigns $U_e\in\mathrm{SU}(2)$ to each positive link. Integration is with respect to product Haar probability on $\mathrm{SU}(2)^{E_L}$. The physical Hilbert space consists of the functions invariant under every vertex gauge transformation, including the transformations at boundary vertices.

For $p=(n;i,j)$, $i<j$, the ordered plaquette holonomy and its fundamental trace are

$$
\begin{aligned}
\Omega_p&=U_i(n)U_j(n+e_i)U_i(n+e_j)^{-1}U_j(n)^{-1},\\
W_p&=\operatorname{tr}(\Omega_p),\qquad S=\sum_{p\in P_L}W_p.
\end{aligned}
$$

With $T_\alpha=-i\sigma_\alpha/2$ and the original left derivatives $X_{e,\alpha}$, the kinetic operator and Hamiltonian are

$$
\begin{aligned}
K&=-\sum_{e,\alpha}X_{e,\alpha}^{2},\\
H&=\kappa\bigl[K+\xi(2M-S)\bigr],\qquad
\kappa=\frac{2g^2}{a},\qquad \xi=\frac1{4g^4}.
\end{aligned}
$$

Here $a>0$ is the lattice spacing and $g>0$ the original coupling. In particular, a small value of $\xi$ corresponds to a large value of $g$. The scalar $2\kappa M\xi$ is part of the original physical energy throughout the calculations.

## The logarithmic vacuum and the coefficient equation

Let $P_H f=\int f\,dU$ and $Q_H=I-P_H$, and define

$$
\Gamma(f,h)=\sum_{e,\alpha}(X_{e,\alpha}f)(X_{e,\alpha}h),
\qquad B(f,h)=K^{-1}Q_H\Gamma(f,h).
$$

The inverse is taken on the nonconstant physical component. At finite coefficient order the papers implement it using the actual Casimir spectrum of the polynomial source. They do not impose a finite-spin approximation to the full interacting Hamiltonian.

The source is the Haar-centered logarithm $v=Q_H\log\psi$ of the positive vacuum. Its equation and formal expansion are

$$
v=\xi v_1+B(v,v),\qquad v_1=\frac S3,\qquad
v=\sum_{n\geq1}\xi^n v_n,\qquad
v_n=\sum_{i=1}^{n-1}B(v_i,v_{n-i})\quad(n\geq2).
$$

The source is a function. Its coefficient representatives carry the original multisets of plaquette labels as well; these labels record where each term came from even when an assembled function or channel vanishes. The physical normalization and energy are recovered by

$$
\begin{aligned}
c_L&=-\frac12\log\int e^{2v}\,dU,\qquad \psi_L=e^{v+c_L},\\
E_{0,L}&=\kappa\left[2M\xi-P_H\Gamma(v,v)\right].
\end{aligned}
$$

The distinction between this normalized vacuum and auxiliary polynomial representatives is essential. The second calculation also uses the formal eigenline representative $u=1+\sum_{\nu\ne0}u_\nu\lambda^\nu$, with $P_Hu_\nu=0$, for $K-\sum_p\lambda_pW_p$. Its relation to the same logarithmic source is

$$
v=Q_H\log u,\qquad u=\frac{e^v}{P_He^v}.
$$

The physical diagonal is $\lambda_p=\xi$ for every plaquette; taking it after coefficient calculations retains every directional response and multiplicity.

## Source identity and reading map

The terms *trace packet* and *quaternion packet* below identify two supplied collections dated 17 September 2026. They do not denote different physical theories. The trace packet evaluates original trace words and builds analytic bounds from their coefficient data. The quaternion packet evaluates polynomials in chord variables obtained by an explicit spanning-tree coordinate map, with the original derivatives and Haar measure transported through that map.

| Appendix and supplied proof text | Packet and principal role |
|:--|:--|
| A. `QUARTIC_SOURCE.md` | Trace: complete fourth source and coefficient bounds |
| B. `PHYSICAL_RETURN.md` | Trace: all-order vacuum correction and physical spectral estimate |
| C. `SIXTH_ENERGY.md` | Trace: sixth energy, cube term, remainder, and plaquette observable |
| D. `FOURTH_ORDER_SOURCE.md` | Quaternion: complete fourth source in exact tree and quaternion coordinates |
| E. `SIXTH_ORDER_ENERGY.md` | Quaternion: sixth energy and a separate finite-volume remainder |
| F. `SIGNED_TANGENT_CERTIFICATE.md` | Quaternion: explicit signed directional coefficients and tangent identities |

Equation labels in the supplied texts remain local to their original files. Thus “Appendix A, Q14” and “Appendix D, Q15” refer to two presentations of the same single-face component; an unqualified Q or E label inside an appendix belongs to that source or its named companion. In the sixth-energy formulas the trace packet uses $(P,T,C,B)$ for paths, common-edge triples, corners, and cubes, whereas the quaternion packet uses $(P_3,T_e,T_v,C)$. The introduction uses the latter notation to avoid that collision. Both use $J$ for unordered adjacent plaquette pairs.

The pinned predecessor is the cubic calculation at Git revision `91434b6962062bd80439d4cb2cae9d2479264dde` in the [Yang-Mills interacting workbench](https://github.com/KokunoYumeto/yang-mills-interacting-workbench). The source texts identify which inherited definitions and bounds they use. Repository status is time-dependent; historical status statements in the appendices describe their source packets.

The appendix proof texts and the algorithms accompanying the edition preserve their supplied source content. Raw conversational input is omitted from the public edition for privacy. References in the original texts to an upload, a session, or a ZIP describe the original provenance; they do not imply that conversational input or every companion file is embedded in this PDF. Formatting and navigation have been added, while the supplied formulas and proofs have been retained. In particular, plain-text mathematical displays are printed in their original notation so that transcription introduces no new mathematical choices.

# The shared fourth source

## What is being completed

At the quadratic reference $q_2=\xi v_1+\xi^2v_2$, the residual is

$$
\xi v_1+B(q_2,q_2)-q_2
=\xi^3v_3+\xi^4 B(v_2,v_2).
$$

The fourth coefficient of the solution is, however,

$$
\boxed{v_4=2B(v_1,v_3)+B(v_2,v_2).}
$$

Both packets calculate this complete signed sum. The mixed term $2B(v_1,v_3)$ is indispensable; computing the degree-four part of the quadratic-reference residual alone would not calculate $v_4$.

## Completeness and two representations

A nonzero logarithmic coefficient has an edge-connected plaquette multiset. Beginning with a plaquette containing a fixed anchor link, and adding either a repeated plaquette or an edge-adjacent plaquette, gives respectively

$$4,\quad46,\quad612,\quad8621$$

anchored multisets at orders one through four. At order four, signed permutations of the three axes and translations reduce the catalogue to 78 classes:

| Partition | $4$ | $3+1$ | $2+2$ | $2+1+1$ | $1+1+1+1$ | Total |
|:--|--:|--:|--:|--:|--:|--:|
| Classes | 1 | 2 | 2 | 19 | 54 | 78 |

Both packets retain explicit maps from these representatives to all 8,621 anchored multisets. Reconstruction in a finite box includes each contained connected multiset once, with the original inverse-link convention and multiplicities.

The trace catalogue has 743 nonzero rational trace-monomial terms. The quaternion catalogue has 4,044 nonzero rational monomials after the sphere relations are used. These counts concern different presentations of the same coefficient functions, and are not a discrepancy in $v_4$. A trace monomial can expand into many quaternion monomials. In the quaternion calculation, the variables are the actual chords of the cluster graph: the four-face lateral tube of a cube has five chord variables, which the catalogue retains.

The equality of the intended coefficients is mathematical: both constructions solve the same Haar-centered coefficient equation in the original variables, and the positive Casimir makes its centered solution unique. This identifies their results once the operator maps and residual identities established in the respective proofs are applied. A separate exact reconciliation for this edition also expands all 743 trace terms into the quaternion coordinates and verifies equality of the complete polynomials in all 78 classes, together with agreement of all 8,621 signed-coordinate transports. The edition's accompanying `VALIDATION.md`, in `consolidation/20260917/`, records that reconciliation and its evidence. The two different term counts alone neither prove nor refute that identification.

For one plaquette, the shared closed expression is

$$
\boxed{
v_4^{(p^4)}=\frac{17}{10368}\chi_1(\Omega_p)
-\frac7{51840}\chi_2(\Omega_p),
}
$$

where $\chi_1=W_p^2-1$ and $\chi_2=W_p^4-3W_p^2+1$. This is one component of the full catalogue, not a substitute for its mixed-face coefficients.

## Signed tangent data in the quaternion packet

For a plaquette $p$ and a coupling multiindex $\rho$, the coefficient of the directional derivative of the logarithmic vacuum is

$$Z_{p,\rho}=(\rho_p+1)v_{\rho+e_p}.$$

Appendix F computes these signed coefficients through total degree three and verifies the differentiated source equation coefficientwise. Its evidence comprises 78 independently reconstructed logarithmic sources, 282 explicitly expanded degree-three response polynomials, and 2,156 residual identities. Of those identities, 282 are the degree-zero equations $KZ_{p,0}=W_p$ and 1,874 are homogeneous positive-degree equations. Thus every residual is zero after subtracting its prescribed forcing. This clarifies the appendix's compressed phrase “2,156 exactly zero polynomial tangent residuals.” The integer prefactor is the occurrence multiplicity of the differentiated plaquette. These are finite formal-parameter identities; the packet does not infer from them a bound on the full infinite linearized inverse.

# The shared sixth energy coefficient

## A common coefficient and complementary derivations

Write the ground eigenvalue of $K-\xi S$ near zero as

$$e(\xi)=e_2\xi^2+e_4\xi^4+e_6\xi^6+\cdots,
\qquad E_{0,L}=\kappa\bigl(2M\xi+e(\xi)\bigr).$$

A link-center involution makes the nontrivial energy branch even. The first two coefficients are

$$e_2=-\frac M3,\qquad e_4=\frac{5M}{216}-\frac{2J}{1053}.$$

The trace packet obtains $e_6$ from the logarithmic-source equation, eliminating $v_5$ with its exact equation and retaining sources through $v_4$. It checks the result against a separate eigenvector recurrence. The quaternion packet uses Haar-centered eigenline coefficients $u_1,u_2,u_3$ and proves

$$
e_6=-\langle u_3,Ku_3\rangle_H
-e_4\|u_1\|_H^2-e_2\|u_2\|_H^2.
$$

The two state-normalization terms in this identity are part of the energy calculation. Neither method drops the additive physical scalar or replaces the physical norm by a Euclidean norm of the displayed coefficients.

## Geometric contributions, including the cube

Let $P_3$ count three-plaquette paths, $T_e$ triples sharing a common edge, $T_v$ triples at a cube corner, and $C$ elementary cubes. The common result is

$$
\boxed{\begin{aligned}
e_6={}&-\frac{289}{77760}M
+\frac{22285}{23654592}J
-\frac{4909}{118272960}P_3\\
&+\frac{244}{4312035}T_e
-\frac{212}{542997}T_v
-\frac{83}{1944}C.
\end{aligned}}
$$

In the trace packet the coefficient for the labelled multiset $p^4q^2$ is $22285/47309184$. The roles $p$ and $q$ may be exchanged. Summing both roles for each unordered adjacent pair gives the coefficient $22285/23654592$ of $J$ above. This factor of two is a difference in counting convention, not a disagreement between the packets.

The last term is a three-dimensional closed-surface contribution. Link-center parity shows that the set of odd-multiplicity plaquettes in a nonzero scalar coefficient must have even boundary. At total order six the only nonempty such set is the boundary of an elementary cube. With the six faces oriented outward, Haar contraction gives

$$\left\langle\prod_{p\in\partial c}W_p\right\rangle_H=\frac{2^8}{2^{12}}=\frac1{16}.$$

For an ordering $\pi$ of the six faces let $A_k(\pi)$ be its first $k$ faces, and let $|\partial A_k|$ count the boundary links. The cube coefficient is

$$
-\frac1{16}\sum_{\pi\in S_6}\prod_{k=1}^{5}
\frac4{3|\partial A_k(\pi)|}
=-\frac1{16}\frac{166}{243}
=-\frac{83}{1944}.
$$

All 720 orders are included. The intermediate denominators are the Casimirs of the retained boundary states. Appendix E also derives the same value by pairing complementary three-face subsets.

## Open-box formula

For $m=2L\geq4$, the original boundary is included in the exact counts

$$
\begin{gathered}
M=3m^2(m+1),\qquad J=6m(3m^2-1),\qquad C=m^3,\\
T_e=12m^2(m-1),\qquad T_v=8m^3,\\
P_3=138m^3-126m^2-24m+12.
\end{gathered}
$$

They give

$$
\boxed{e_6=-\frac{211396463m^3+30959193m^2+21845782m+2336684}{4691494080}.}
$$

Consequently

$$
\frac{E_{0,L}}\kappa
=2M\xi-\frac M3\xi^2
+\left(\frac{5M}{216}-\frac{2J}{1053}\right)\xi^4
+e_6\xi^6+\text{higher even orders}.
$$

The coefficient-density limit is $\lim_{m\to\infty}e_6/M=-211396463/14074482240$. This statement concerns a coefficient. A limit of the full series requires a uniform remainder or a separate convergence argument, as supplied for a particular observable in the trace packet.

# What is controlled beyond finite order

## The trace packet: full vacuum and physical spectrum

Appendix A derives bounds for the complete fourth source in three auxiliary coefficient norms: a Casimir-weighted local norm, a total-spin budget $m(v_4)$, and a budget $t(v_4)$ at the actual anchor link. These bounds are

$$
\begin{aligned}
\|v_4\|_{\rm loc}&\leq\frac{2296826751679}{30073680},\\
m(v_4)&\leq\frac{17270702970768271}{341697152160},\\
t(v_4)&\leq\frac{110695177857394584026401}{18025447358750832000}.
\end{aligned}
$$

These are bounds on coefficient representations used to construct and estimate the vacuum; the physical state norm remains the original weighted Haar norm.

The strongest construction in Appendix B uses the full fourth-order reference $q_4=\sum_{n=1}^4\xi^n v_n$ and its entire residual. A convergent Neumann inverse and a convergent nonlinear series construct $v-q_4$, including both infinite tails. The resulting positive function is identified with the actual normalized physical ground state. Its source estimate is then returned to the complete physical excitation problem.

Let $\Delta_L$ be the lowest positive excitation energy above that ground state. The result in Appendix B, R30 is

$$\Delta_L\geq\kappa d_{[4]}(\xi),
\qquad L\geq2,\quad a>0,\quad0<\xi\leq\alpha_{[4]}.$$

Here $d_{[4]}$ is the explicit expression in R29, and $\alpha_{[4]}$ is the first positive root of the rational polynomial in R25. The stated enclosure is

$$0.018104972231644127075<\alpha_{[4]}<0.018104972231644127076.$$

The bound has $d_{[4]}(\xi)>3/2$ on that whole closed positive interval. In the original coupling, a sufficient rounded condition is $g^2\geq3.715960362535435237$. A concrete consequence is

$$\Delta_L>1.6584\,\kappa=3.3168\,g^2/a,
\qquad g^2\geq15/4.$$

This statement is uniform in the finite box size and concerns every physical excitation. Appendix B also preserves an earlier, weaker construction based on $q_3$; its endpoint $\alpha_4$ must not be confused with the stronger $q_4$ endpoint $\alpha_{[4]}$ used here.

## Two energy remainders with different domains

The trace packet gives the physical energy remainder after order six as

$$
|R_{\geq8}|\leq\frac{49\kappa|E_L|}{1200}
\frac{(60|\xi|)^8}{1-(60|\xi|)^2},\qquad0<|\xi|<\frac1{60}.
$$

Its analytic input is the inherited uniform logarithmic-source construction on the complex circle $|\xi|=1/60$. After division by $M$, the geometric factor $|E_L|/M=(m+1)/m$ is uniformly bounded. The $1/60$ domain of this Cauchy remainder is stated separately from the larger real-coupling interval of the fourth-reference spectral result.

The quaternion packet supplies a separate proof using bounded perturbation of the isolated free vacuum. With

$$R=\frac3{8M},$$

its dimensionless energy remainder satisfies

$$|R_8(\xi)|\leq\frac34
\frac{(|\xi|/R)^8}{1-(|\xi|/R)^2},\qquad |\xi|<R.$$

The physical remainder is $\kappa R_8$. This radius depends on the volume; for $L=2$ it is $1/640$. The second estimate is independently derived within its packet and does not replace the uniform analytic argument of the first.

## The plaquette observable and the continuum boundary

For the trace packet, differentiating the normalized ground-state eigenvalue yields the mean half-trace

$$P_L(\xi)=\frac1{2M}\sum_p\langle W_p\rangle_{\rho_L},
\qquad \rho_L=\psi_L^2,$$

and a uniform remainder permits the spatial-volume limit at fixed lattice spacing. Appendix C, E12 gives

$$P_\infty(\xi)=\frac\xi3-\frac{11}{468}\xi^3
+\frac{211396463}{4691494080}\xi^5+R_{P,\infty},$$

with

$$|R_{P,\infty}|\leq\frac{49}{40}
\frac{(60\xi)^7[8-6(60\xi)^2]}{[1-(60\xi)^2]^2},
\qquad0<\xi<1/60.$$

This is a fixed-lattice-spacing observable. Along the separately specified path $a_n=a_0 2^{-n}$ and $g_n^{-2}=g_0^{-2}+\beta n\log2$, the spectral domain is $g_n^{-2}\leq2\sqrt{\alpha_{[4]}}$. For $\beta>0$ the path eventually leaves that domain. The finite-regulator estimates therefore do not supply a continuum field or a finite positive continuum mass.

# Literature and evidentiary scope

The exponential-vacuum and gauge-invariant character/Casimir framework has established antecedents. The supplied trace packet explicitly transports the coupling, energy, derivative, and observable conventions of its comparison sources. The quaternion packet checks the one-plaquette coefficient against the Mathieu characteristic value in NIST DLMF. These comparisons support attribution and stated convention checks; they do not provide an independent published verification of the full fourth catalogue or sixth open-box coefficient.

The claims in the appendices combine written arguments with exact finite computation. A finite evaluation at rational link assignments is distinguished there from a polynomial identity, and a coefficient calculation is distinguished from a convergence or spectral theorem. Neither packet claims independent external analytical review or a new Lean certificate. This reader preserves those distinctions.

## References

The identities and versions below were checked against primary records on 17 September 2026. This bibliographic check does not constitute a new audit of the mathematical implications drawn from them; the scope of each use is stated in the supplied proofs.

1. D. Schütte, Zheng Weihong, and C. J. Hamer, *The Coupled Cluster Method in Hamiltonian Lattice Field Theory*. [arXiv:hep-lat/9603026v1](https://arxiv.org/abs/hep-lat/9603026v1), 30 March 1996; *Physical Review D* **55** (1997), 2974-2986, [doi:10.1103/PhysRevD.55.2974](https://doi.org/10.1103/PhysRevD.55.2974). Exponential-vacuum and character/Casimir framework; convention map in Appendix B, R23.
2. C. H. Llewellyn Smith and N. J. Watson, *The Shifted Coupled Cluster Method: A New Approach to Hamiltonian Lattice Gauge Theories*. [arXiv:hep-lat/9212025v1](https://arxiv.org/abs/hep-lat/9212025v1), 18 December 1992; *Physics Letters B* **302** (1993), 463-471, [doi:10.1016/0370-2693(93)90428-K](https://doi.org/10.1016/0370-2693(93)90428-K). Shifted coupled-cluster framework; scope discussed in Appendix C, E7.
3. Thomas Spriggs, Eliska Greplova, Juan Carrasquilla, and Jannes Nys, *Accurate ground states of SU(2) lattice gauge theory in 2+1D and 3+1D*. [arXiv:2509.12323v1](https://arxiv.org/abs/2509.12323v1), 15 September 2025. Explicit coupling, energy, observable, and boundary comparison in Appendix C, E13-E14; the cited version is v1.
4. NIST Digital Library of Mathematical Functions, Chapter 28, *Mathieu Functions and Hill's Equation* (chapter author: Gerhard Wolf), §28.6, *Expansions for Small q*, [equation (28.6.5)](https://dlmf.nist.gov/28.6.E5). Release 1.2.8 of 15 September 2026; [official citation information](https://dlmf.nist.gov/help/cite). One-plaquette Mathieu coefficient comparison in Appendix E, E17.
5. Timo Jakobs, Marco Garofalo, Tobias Hartung, Karl Jansen, Johann Ostmeyer, Simone Romiti, and Carsten Urbach, *Dynamics in hamiltonian lattice gauge theory: approaching the continuum limit with partitionings of SU(2)*. *The European Physical Journal C* **85** (2025), article 1418, published 13 December 2025, [doi:10.1140/epjc/s10052-025-15120-x](https://link.springer.com/article/10.1140/epjc/s10052-025-15120-x). Single-plaquette Mathieu representation cited in Appendix E, E17.


\clearpage
\appendix


# The complete connected fourth source in the original cubic SU(2) Hamiltonian

17 September 2026. Parent: `91434b6962062bd80439d4cb2cae9d2479264dde`, the unmerged PR8 contribution. This file, `PHYSICAL_RETURN.md`, and `SIXTH_ENERGY.md` form one continuation. The exact original-coordinate tables are generated by `verify.py`; every entry and every original anchored multiset is retained. This is a written proof with finite exact computation, not a Lean certificate or an independent external analytical review. No claim of historical priority is made.

## Q1. Original operator and labelled coefficient source

Vertices are `{-L,...,L}^3`, L>=2. Edges are every contained positively oriented nearest-neighbor link e=(n,i). Faces p=(n;i,j), i<j, carry the original word

    W_p=tr(U_i(n) U_j(n+e_i) U_i(n+e_j)^(-1) U_j(n)^(-1)).

With T_alpha=-i sigma_alpha/2 and X_e,alpha the original left derivative, retain

    K=-sum_(e,alpha) X_e,alpha^2,
    H=kappa K+kappa xi(2M-S),
    S=sum_p W_p, M=|P_L|, kappa=2g^2/a, xi=1/(4g^4).       (Q1)

The scalar 2kappa xi M remains. The Hilbert measure is the original product Haar probability. All vertex gauge transformations, including boundary vertices, are imposed in the physical space. The physical H^2 and H^1 domains and positive ground-state identity are as in the pinned original `finite_box_weak_coupling_physical_gap.md`, blob `dfee77c0ca0d6ed897c4172fcbfe23cd9d10d313`.

Let P_H be original Haar integration and Q_H=I-P_H. On nonconstant physical Fourier blocks define

    Gamma(f,h)=sum_(e,alpha)(X_e,alpha f)(X_e,alpha h),
    B(f,h)=K^(-1) Q_H Gamma(f,h),
    v_1=S/3, v_n=sum_(i=1)^(n-1)B(v_i,v_(n-i)).           (Q2)

Every occurrence keeps its multiset of original face labels. The support is their original union; cancellation of a coefficient does not delete that support record. At the function level, assembly is the map

    A: direct_sum_multisets V_multiset -> functions,
       (f_multiset) -> sum f_multiset.                   (Q3)

Its kernel is the set of coefficient families with zero assembled Fourier matrix at every original spin label. Neither a zero matrix nor a trace identity is assigned an inverse outside the stated quotient. Scalars removed by Q_H are returned to the ground energy in R9 of the companion file.

## Q2. A finite trace presentation with an explicit evaluation map

An oriented edge word is a tuple (s_1 e_1,...,s_r e_r), s_i=+1 or -1. Its evaluation is tr(product_i U_ei^si), in that order. A monomial is a product of these original trace evaluations. The coefficient algebra is rational. The retained map `ev` sends a formal rational sum of such monomials to its actual smooth cylinder function.

The program chooses representatives only using the following proved relations in ker(ev):

* adjacent U_e U_e^(-1)=I, with tr(I)=2 kept as the scalar 2;
* cyclic trace rotation;
* reversal of the entire word with every sign reversed, since tr(V^(-1))=tr(V) for V in SU(2);
* tr(V^r)=P_r(tr V), where P_0=2, P_1=x, P_r=x P_(r-1)-P_(r-2).

The last identity follows by multiplying V^2-tr(V)V+I=0 by V^(r-2) and taking the trace. Thus `ev` factors through the displayed trace relations. It is this factorization, with the original multiset still attached, that relates the coefficient representatives. No faithfulness of an unrestricted trace-word algebra is presumed, and no physical parameter, vector norm, or Haar factor is changed.

Here are the exact derivative formulas used by `trace_algebra.py`. An occurrence of U_e has sign +1 and a cut immediately before that occurrence. An occurrence of U_e^(-1) has sign -1 and a cut immediately after it. If w_i is the cyclic word starting at that cut, then

    X_e,alpha tr(w)=sum_occ s_occ tr(T_alpha w_occ).       (Q4)

For two trace factors A,B, the original Pauli matrices give

    sum_alpha tr(T_alpha A)tr(T_alpha B)
       =-(1/2)tr(AB)+(1/4)tr(A)tr(B),
    sum_alpha tr(T_alpha A T_alpha B)
       =-(1/2)tr(A)tr(B)+(1/4)tr(AB).                    (Q5)

These follow by substituting
`sum_alpha (T_alpha)_ij(T_alpha)_kl=-(1/2)delta_il delta_jk+(1/4)delta_ij delta_kl`.

For one word w and edge e, each occurrence contributes (3/4)tr(w) to E_e tr(w). Two different occurrences, with cut segments A,B and signs s,t, contribute

    st tr(A)tr(B) - (st/2)tr(w).                         (Q6)

For a product of trace factors, retain the entire product rule

    K product f_i = sum_i(Kf_i) product_(j!=i)f_j
                 -2 sum_(i<j) Gamma(f_i,f_j) product_(k!=i,j)f_k.   (Q7)

Equations Q4-Q7 prove that the rational word operators intertwine evaluation with the original K and Gamma, on every original link assignment. They also retain the nonzero cross terms. The separately implemented `differential_audit.py` differentiates quaternion matrix products by explicit generator insertions and never calls these Fierz contractions.

## Q3. Original finite Casimir inverse, with its scalar fibre

For a multiset C of n faces, an edge occurring r_e times has the full spin list

    j_e=r_e/2,r_e/2-1,...,r_e mod 2 /2.                 (Q8)

At each original vertex, a contributing invariant tensor has integral summed spin and max j_e <= sum of the other j_e. The necessity follows from the maximum weight of their tensor product. The sufficiency follows by successively adjoining a spin: the attainable spins fill the interval from the excess of the largest spin over the others (or the parity minimum) to their total, in unit steps. This inductively gives spin zero exactly for the two stated tests. For the computation only their necessary direction is needed; retaining extra channels would still give a valid inverse interpolation.

Enumerate all assignments in Q8 satisfying those vertex tests and retain their original Casimirs c=sum_e j_e(j_e+1). Call the resulting finite set C_C. Every actual representation of the coefficient source lies in that list. Define

    q_C(t)=product_(c in C_C, c>0)(1-t/c),
    f_C(t)=(1-q_C(t))/t-q_C(t) sum_(c in C_C,c>0)1/c.    (Q9)

The quotient by t in Q9 is a polynomial because its numerator has zero constant term. Direct substitution gives f_C(0)=0 and f_C(c)=1/c for every positive listed c. The original product-group spectral decomposition therefore proves

    K f_C(K) f=Q_H f                                   (Q10)

on this whole finite coefficient space, with every repeated spin multiplicity retained. This is a polynomial in the original derivatives, not an inverse on an independently chosen matrix. The constant removed by Q10 is recorded explicitly by original Haar integration.

For a face multiset C, let C=A+B range over ordered nonempty proper submultisets, with their original multiplicities. The complete coefficient is

    v_C=f_C(K) sum_(A+B=C) Gamma(v_A,v_B),
    v_{ {p} }=W_p/3.                                  (Q11)

For repeated labels each distinct submultiset is counted once. For distinct labels both ordered complementary choices occur. This agrees exactly with Q2 on expansion of the original sums. It proves each computed entry without introducing an eigenfunction cutoff for H: n bounds only the degree of the one Taylor coefficient being calculated.

## Q4. Exhaustive fourth coefficient and inverse coordinate transports

Start at the four original faces incident on the anchor edge (0,0,0;1). Grow a multiset by adjoining a face already present or a face sharing an original edge with a present face. Retain all results as multisets. The cardinalities at orders one through four are

    4, 46, 612, 8621.                                  (Q12)

This exhausts connected anchored multisets: choose a face containing the anchor, take a spanning tree of the adjacency graph of the distinct faces, grow along that tree, and insert each remaining repeated occurrence. This gives a growth order of every such multiset. A disconnected term is zero in Q11 because either an input source is already zero or the two differentiated active supports are disjoint.

The fourth multiset counts and representative counts are respectively

| Multiplicity | Original anchored multisets | Cubic representatives |
|---|---:|---:|
| 4 | 4 | 1 |
| 3+1 | 84 | 2 |
| 2+2 | 42 | 2 |
| 2+1+1 | 1572 | 19 |
| 1+1+1+1 | 6919 | 54 |
| Total | 8621 | 78 |

The representative map retains an actual permutation pi of the three axes, signs epsilon_i, and an integer translation d:

    y_i=epsilon_i x_(pi(i))-d_i,
    x_(pi(i))=epsilon_i(y_i+d_i).                       (Q13)

A positive original edge maps to the corresponding signed edge under Q13. The link-variable map uses that same U or U^(-1). A face maps to the original face word or its whole inverse, which have equal fundamental traces. Haar integration and each link Casimir are preserved by this map. Applying Q4-Q7 proves that Q13 transports every coefficient in Q11. The full inverse is retained for every one of the 8621 original multisets in `quartic_transports.json`.

No invariance of the auxiliary trace-coefficient norm under separate link inversion is asserted. The estimates in Q6-Q8 below use bounds valid in every original orientation.

`quartic_coefficients.json` contains all 78 polynomials: 743 nonzero rational trace-monomial terms, their original edge dictionaries, face words, multiplicities and complete allowed Casimir lists. The exact self contribution is

    v_{ {p,p,p,p} } = (17/10368) chi_1(Omega_p)
                        -(7/51840) chi_2(Omega_p).      (Q14)

Here chi_1=W_p^2-1 and chi_2=W_p^4-3W_p^2+1. All other contributions are exposed in the table in the same original words. The producer regenerates the entire table; it does not merely test a few displayed examples. Its differential audit checks the original equation for every representative at two declared rational quaternion assignments. Those finite evaluations accompany, rather than replace, the general intertwining proof Q4-Q11.

## Q5. The auxiliary norm and its original physical gauge inequality

For an original nonempty union label S and spin tuple j, write the coefficient as Tr(A_(S,j) pi_j(U)). Define

    ||f||loc=max_a sum_(S contains a,j!=0)c(j)||A_(S,j)||_1,
    m(f)=max_a sum_(S contains a,j!=0)(sum_e j_e)||A_(S,j)||_1,
    t(f)=max_e sum_(S contains e,j!=0)j_e||A_(S,j)||_1.    (Q15)

All these sums concern the explicitly retained coefficient source. The physical norm stays int rho |f|^2 and physical energy stays kappa int rho sum|Xf|^2.

For any active edge e, the endpoint invariant-tensor inequalities force at least 2j_e total spin on the other edges at its endpoints. Their remote endpoints are distinct on the triangle-free original cubic graph. Applying the same inequality there and counting every further edge at most twice forces at least j_e further total spin. Thus sum_f j_f>=4j_e. Since j(j+1)>=3j/2 on nonzero half-integers,

    c(j)>=6j_e, m(f)<=2||f||loc/3, t(f)<=||f||loc/6.     (Q16)

A nonconstant physical block has c>=3. Products of coefficient matrices have trace-norm bound ||A tensor B||_1=||A||_1||B||_1. Decomposing the actual tensor representation, pinching to its isotypic blocks and tracing the multiplicity factors gives the complete actual product coefficients with total trace norm at most that product. The last assertion follows by trace duality against block-diagonal contractions; all multiplicities remain. Each original spin generator has operator norm j_e. Summing its three indices and retaining both possible anchored inputs proves

    ||B(f,h)||loc<=3[m(f)t(h)+m(h)t(f)]
                 <=(2/3)||f||loc||h||loc.              (Q17)

The first source has (||v1||loc,m(v1),t(v1))<=(32,64/3,16/3). The full second source retains (236,5834/39,137/6), from the parent Q2 expansion.

## Q6. Exact cubic channel capacities, including all mixed channels

This stage further evaluates the original cubic table; it changes no coefficient. The per-cluster nuclear masses x are constrained as follows. Every coordinate is nonnegative.

* Pair: x_0+x_1<=64, x_0<=16.
* Repeated cubic: x_(1/2)+x_(3/2)<=216, x_(1/2)<=520/3.
* Path cubic: x_00+x_01+x_10+x_11<=512; x_00<=32; x_00+x_01<=128; x_00+x_10<=128.
* Common-edge cubic: x_(1/2)+x_(3/2)<=512; x_(1/2)<=256.
* Corner cubic: retain 000,011,101,110,111, with total at most512, x_000<=8, and x_000+x_b<=128 for each b in {011,101,110}. Each one-spin channel is exactly zero by the original central-vertex invariant condition.

The pair and path bounds are original single-link Haar contractions. For the repeated cubic, H=(4/3)W_p P_0(W_p W_q)-(1/3)W_q gives ||H||_1<=(4/3)*8*16+8/3=520/3, and the full product chi_1(Omega_p)W_q has norm at most27*8=216. For the common-edge cubic, its entire half-isotypic projection is (2/3)sum W_r P_0(W_pW_q), with norm at most(2/3)*3*8*16=256; this keeps both half-spin copies. The corner single-zero projections have norm at most8*16=128; its triple-zero projection is one quarter of the original six-edge boundary trace, giving8. These bounds follow from literal original Haar contractions and Q17, not from independent assignment of channel masses.

A self cubic has the two fixed bounds 8,64 on its half- and three-half character terms. Maximizing each actual weighted coefficient over these finite polytopes, then summing over the 612 anchored multisets with their actual anchor spins, gives

    ||v3||loc <= 918680/351,
    m(v3) <= 336572872/208845,
    t(v3) <= 225985217/1253070.                         (Q18)

The weights are respectively c(j)|a_j|, (sum j_e)|a_j|, and j_anchor|a_j| for the complete parent cubic coefficients a_j. `channel_bounds.py` records every rational facet and vertex. The exact vertex calculation solves every candidate set of active facets, retains feasible vertices and evaluates those displayed weights. Since each polytope is bounded, a linear functional has a maximum on that list. This is a finite complete certificate of all three sums. The original v3 coefficients, signs and physical state norm remain unchanged.

## Q7. Three independently valid fourth-source estimates

For each original fourth multiset C, the table bounds its full c-weighted norm by the smallest of the following separately proved scalar upper bounds.

**Input-channel bound.** For each ordered split A+B=C in Q11, use the actual eigencomponents (a_mu,F_mu) and (a_nu,F_nu) of the lower sources. The c-weighted inverse cancels the output c. Thus the bound is

    3 sum_(mu,nu)|a_mu a_nu| (sum_e j_mu,e j_nu,e) x_mu x_nu.    (Q19)

Maximize it over the two actual mass polytopes of Q6. A bilinear functional on two compact polytopes reaches a maximum at a pair of vertices: fix one variable, maximize the other linearly, then maximize the retained first coordinate linearly. The producer evaluates every such pair, including equal lower multisets without presuming independence of their actual masses. This is a bound; treating their equal masses as independent merely enlarges the admitted domain. Sum every ordered split.

**Complete trace expression.** Compute Kv_C by Q6-Q7 from the exact table. A nonempty reduced closed word of length l has a tensor trace coefficient of nuclear norm at most2^(l-1). To verify it before identifying repeated edge variables, use independent fundamental factors for its occurrences. At a maximum and minimum of the original coordinate height along the closed walk, the alternating two-index contractions each have Euclidean norm sqrt(2); the other contractions are two-dimensional identities. Separate row/column permutations give norm2^(l-t), with at least one maximum t>=1. Identifying repeated original links is the actual tensor-representation restriction, followed by the trace-norm-contractive isotypic decomposition used in Q17. Thus the bound2^(l-1) is valid in every orientation, also for repeated original edges. Products of words multiply these bounds. Applying this to every rational term of Kv_C gives a whole-source bound on ||v_C||loc; constants cause no difficulty because the nonconstant Fourier sum is at most the full sum. No rotational invariance of this auxiliary norm is used.

**Joint output-channel bound.** For a four-distinct-face multiset with no edge in more than two faces, choose s_e=0,1 on each shared edge. Single-occurrence edges have spin1/2. Keep every assignment admitted by the original vertex conditions. Let c_A(s) be the original Casimir of a submultiset A in that assignment. For singleton A set a_A=1/3; otherwise define

    a_A(s)=sum_(empty!=B proper subset A)
       [(c_B(s)+c_(A\B)(s)-c_A(s))/(2c_A(s))]
        a_B(s)a_(A\B)(s).                              (Q20)

A zero c_A is assigned zero by the original Q_H. At every shared edge a subset has either zero factors, one fundamental factor with scalar Casimir3/4, or the full pair with the total edge Casimir. Hence these lifted subset Casimirs commute with the final edge projectors. Q10 and the product rule prove Q20 on the full product of the original four traces. A forbidden intermediate component can have a formally displayed coefficient, but its projected function is literally zero; it is not assigned a new vector.

For each set Z of shared edges, integrate precisely those original edge variables. The projection P_(0,Z) is product_(e in Z)(I-E_e/2) on this four-face product. Its trace expression, produced by Q6-Q7, supplies the orientation-independent norm bound b_Z just proved. Therefore its final channel masses satisfy

    sum_(s with s_e=0 for all e in Z) x_s <= b_Z.         (Q21)

Maximize sum_s c(s)|a_C(s)|x_s over x_s>=0 and every constraint Q21. The file `quartic_bounds.json` retains the entire constraint list, all coefficient weights, a rational primal vector and a rational dual vector y. The checker verifies y>=0, A^T y>=the weights and equality of primal and dual objectives. Consequently b^T y is a proved upper bound independent of any numerical optimization. `exact_lp.py` obtains it by exact rational elimination with Bland's rule; all certification inequalities are checked again. Forty-four of the 78 representatives admit this particular commuting-channel calculation; the others retain Q19 and the complete trace bound.

## Q8. Complete summed bound and physical scope

Sum the selected per-cluster bounds over every original anchored multiset using Q13 and the orientation-independent inequalities above. The complete rational sum is

    ||v4||loc <= A4 := 2296826751679/30073680
                       < 76374.                        (Q22)

The complete table includes the 78 exact source polynomials and their 8621 transports. The bound itself includes every ordered input split, every admitted joint output channel and every original scalar return. It is stronger than the preceding unevaluated estimate
`(128/3)*(944984/351)+799258/39`.

The three quantities in Q18 and the full fourth coefficient Q22 are the inputs used in `PHYSICAL_RETURN.md`. That argument controls every remaining order. The finite fourth-coefficient calculation is never substituted for the full interacting Hamiltonian.

## Q9. The fourth source's total-spin and actual-anchor-spin bounds

The complete fourth coefficient also gives more information than its c-weighted norm. Retain each original coefficient family and the actual list of allowed spins from Q8. For a representative C with a proved whole c-weighted bound b_C, two immediate estimates are

    m_C <= b_C max_(j in C_C,j!=0) (sum_e j_e)/c(j),
    t_C,e <= b_C max_(j in C_C,j!=0) j_e/c(j).           (Q23)

These follow term by term on the original Fourier coefficients. The maximum is over the complete displayed assignments, not just their distinct Casimir values. It is finite and rational. Every extra admitted spin enlarges these upper bounds.

There is also an estimate directly from the complete v_C trace polynomial. For a monomial m let r_e(m) be its full occurrence count on edge e. Tensor decomposition places every actual output spin at most r_e(m)/2. With b_m=2^(sum_words(length(word)-1)), the orientation-independent bound from Q7 gives

    m_C <= sum_m |a_m| b_m (sum_e r_e(m))/2,
    t_C,e <= sum_m |a_m| b_m r_e(m)/2.                  (Q24)

Every term and its original occurrences remain. These are bounds on the same canonical Fourier coefficient quantities as Q23; taking the smaller of the two scalar upper bounds does not change a coefficient or physical metric.

For the 44 commuting-channel cases in Q20-Q21, retain the identical mass constraints A x<=b and x>=0. Use instead the two complete objective rows

    weight_m(s)=(sum_e j_e(s)) |a_C(s)|,
    weight_e(s)=j_e(s) |a_C(s)|.                        (Q25)

Exact rational dual vectors y>=0 with A^T y>=weight bound these quantities by b^T y. The producer computes and verifies the primal and dual equations as for Q21. The table `quartic_spin_budgets.json` keeps every dual, the selected scalar bounds and the original edge multiplicities.

For the point-spin sum the anchor must be transported as well. In each actual map Q13 its endpoints 0 and e_1 go to -d and (epsilon_i delta_(pi(i),1)-d_i)_i. The code locates that exact original edge in the representative dictionary and adds its own t_C,e bound. The total-spin bound is added once for every original anchored multiset. Thus every original orientation and anchor are retained. In particular this computation uses universal orientation bounds, not a claimed nuclear-norm invariance under a partial transpose.

The resulting complete rational sums are

    m(v4) <= m4 := 17270702970768271/341697152160,
    t(v4) <= t4 := 110695177857394584026401/18025447358750832000. (Q26)

Their approximate sizes are 50543.88912 and 6141.050242. The exact fractions in Q26, rather than those renderings, are used in every subsequent bound. The point-spin result is strictly smaller than A4/6. These are proved bounds for the entire original fourth source, not selected channels or a sampled cluster. `PHYSICAL_RETURN.md` R24-R34 uses them to complete the full correction at q4; R1-R23 retain the earlier cubic-reference calculation as an intermediate result.

## Sources and attribution

The pinned parent provides the complete second and third coordinate calculations, original support reconstruction, and auxiliary coefficient norms; its cubic producer was replayed unchanged. Classical exponential-vacuum and gauge-invariant character/Casimir approaches are described by Schuette, Zheng Weihong and Hamer, arXiv:hep-lat/9603026v1, especially equations17,21-26,30,38; the actual physical parameter/energy dictionary is retained in the companion return file. No new general coupled-cluster method or worldwide-priority claim is asserted. Source scopes and the latest peer README discovery are in SOURCE_INTAKE.json.


# Full corrections at the cubic and fourth sources in the original physical energy

17 September 2026. All operators, parameters, coefficient spaces and source maps are those of `QUARTIC_SOURCE.md` (Q1-Q26). R24-R34 give the strongest result, using the complete fourth source; R1-R23 preserve the cubic-reference calculation and its explicit maps. This argument constructs the full correction rather than truncating the Hamiltonian. The final estimate is for the original finite-regulator physical spectrum, uniformly in L. The smooth four-dimensional continuum mass is not determined by this contribution.

## R1. The actual cubic reference and its whole residual

Write x=xi without changing its physical value, and set

    q3=x v1+x^2 v2+x^3 v3,
    R3=x v1+B(q3,q3)-q3
      =x^4 v4+2x^5 B(v2,v3)+x^6 B(v3,v3),
    J3 h=2B(q3,h), L3=I-J3.                              (R1)

Every term is an original function. Q11 evaluates all of v4. The fifth and sixth terms remain as the displayed complete bilinear functions, with the independent bounds below. The Frechet factor two follows by expansion of B(q3+h,q3+h) using symmetry of the original Gamma.

Put

    A4=2296826751679/30073680,
    m3=336572872/208845, t3=225985217/1253070,
    m2=5834/39, t2=137/6,
    l3=m3+4t3=292337810/125307,
    b23=3(m2*t3+m3*t2)=222621900791/1163565,
    b33=6m3*t3=76060493515233224/43616234025.              (R2)

The exact Q17 source estimate and the three evaluated lower coefficients give

    ||J3|| <= ell(x)=(128/3)x+(3132/13)x^2+l3*x^3,
    ||R3||loc <= delta(x)=A4*x^4+2b23*x^5+b33*x^6.        (R3)

For the cubic part of J3, Q17 and Q16 give
`2*3[m3/6+(2/3)t3]=m3+4t3`; this retains the two different spin budgets. The fifth residual coefficient is twice b23, not b23. All sixth-order residual terms are included in b33.

Define the explicitly specified rational polynomial

    D4(x)=(1-ell(x))^2-(8/3)delta(x).                    (R4)

Let alpha4 be its unique root between 178/10000 and 179/10000. Exact rational evaluation proves opposite signs at these endpoints and ell(179/10000)<1. On [0,179/10000], ell and delta are increasing, and

    D4'(x)=-2(1-ell(x))*ell'(x)-(8/3)delta'(x)<0.

Thus alpha4 is also the first positive root; D4>=0 and ell<1 on [0,alpha4]. The full constants in R2-R4 define the polynomial without rounded coefficients.

## R2. Both infinite constructions and their actual residuals

The actual source operator L3 has the norm-convergent inverse

    L3^(-1)=sum_(j>=0)J3^j,
    ||L3^(-1)||<=1/(1-ell(x)).                           (R5)

Let z=L3^(-1)R3 and C=L3^(-1)B. Define w_1=z and
`w_n=sum_(i=1)^(n-1) C(w_i,w_(n-i))`. From R3 and Q17,

    ||w_n||loc <= Cat_(n-1) c_*^(n-1) z_*^n,
    z_*=delta/(1-ell), c_*=(2/3)/(1-ell),
    theta=4 c_* z_*<=1.

The complete series w=sum_n w_n is absolutely convergent, including x=alpha4, and satisfies L3w=R3+B(w,w). Its bound is

    ||w||loc<=w_*(x)=(3/4)(1-ell(x)-sqrt(D4(x))).         (R6)

At theta=1 the convergence comes from the Catalan series itself. With b_N=binom(2N,N)/4^N, the exact identity Cat_N/4^N=2(b_N-b_(N+1)) gives the full nonlinear tail

    ||sum_(n>N)w_n||loc
       <=(3/4)(1-ell)theta^(N+1)b_N
       <=(3/4)(1-ell)theta^(N+1)/sqrt(N+1).              (R7)

The final inequality follows from b_N^2<=1/(N+1), proved by induction from the displayed ratio b_(N+1)/b_N=(2N+1)/(2N+2). Independently, the finite linear sum has the exact original residual

    L3^(-1)R3-sum_(j=0)^N J3^j R3
       =J3^(N+1)L3^(-1)R3.                             (R8)

Its norm is at most ell^(N+1)delta/(1-ell). Each J3 operation adjoins at most three original faces to the union label, and R3 has at most six; the finite linear sums therefore retain supports of at most6+3N faces. R7 retains every subsequent nonlinear union.

## R3. Identification with the original positive vacuum and its scalar

At each finite L the labelled normed coefficient source is complete, and its global c-weighted sum is at most |E_L| times its local norm. The original spin-generator bounds control every first and second derivative by that global sum. Thus the convergent v=q3+w is C^2 on the original compact product group. The source equation can be summed with its full derivatives. Retain

    C(v)=int_H Gamma(v,v),
    c_L=-(1/2)log int_H exp(2v),
    psi_L=exp(v+c_L),
    E0,L=2kappa x M-kappa C(v).                         (R9)

The original product rule gives H psi_L=E0,L psi_L. Elliptic regularity makes psi_L smooth and strictly positive. Multiplication and division by psi_L preserve the original finite-volume H^1 domain. Integration by parts gives, for every smooth f,

    q_(H-E0,L)(psi_L f)=kappa int psi_L^2 sum_i|X_i f|^2. (R10)

This proves E0,L is the actual ground energy. A second ground state divided by psi_L has every original derivative zero and is constant. The source construction is gauge invariant, so this is the actual physical vacuum. The argument does not assume an excitation gap.

The approximate exponential has a separate exact identity, which retains its multiplication defect:

    exp(-q3) H exp(q3)
      =kappa[K-2Gamma(q3,.)]
       +kappa[2Mx-C(q3)]I-kappa M_(K R3).                (R11)

Here M_(K R3) means multiplication by the full original polynomial K R3. Q1-Q2 and a direct differentiation prove R11. Its scalar C(q3) and the multiplication operator remain; they are not replaced by the actual E0,L before R9 is proved.

The same absolute coefficient arguments give analyticity for complex |x|<alpha4. At every original power the unique coefficient recurrence is Q2. Consequently this solution agrees, by its actual coefficients and the ground-state identification, with the preceding constructions on their common domain. No competing vacuum or comparison measure is substituted.

## R4. Return to the complete physical spectral problem

The original transported operator is

    A=psi_L^(-1)(H-E0,L)psi_L=kappa[K-2Gamma(v,.)].      (R12)

The complete actual point-spin budget is

    t(v)<= (16/3)x+(137/6)x^2+t3*x^3+w_*/6.

For a physical Fourier function h, the three original generator indices and sum_e j_e<=2c(j)/3 give

    ||2Gamma(v,h)||_X<=chi(x)||Kh||_X,
    chi(x)=4[(16/3)x+(137/6)x^2+t3*x^3+w_*/6].           (R13)

The norm X is the sum of the original trace norms of Fourier coefficients. The scalar output is included in this bound. Substitution of R6 gives the exact identity

    3(1-chi(x))=d4(x)
      =(3/2)(1+sqrt(D4(x)))+(1136/13)x^2+p3*x^3,
    p3=(3/2)m3-6t3=278874091/208845>0.                 (R14)

In particular chi<1 throughout the entire closed domain. At alpha4, d4 exceeds3/2.

Let lambda>0 be an actual physical excitation eigenvalue, and h the zero-Haar-mean part of its eigenfunction after division by the actual vacuum. A constant transported eigenfunction has eigenvalue zero, so h is nonzero. The original eigen-equation gives

    (K-lambda/kappa)h=Q_H 2Gamma(v,h).                  (R15)

Smoothness on this fixed finite product implies absolute summability of its c-weighted Fourier trace coefficients: applying arbitrarily high powers of the elliptic K gives rapid decay, while the number and dimensions of product-spin representations grow polynomially in c at this fixed L. Cauchy-Schwarz then gives the required trace-norm summability. Hence R13 applies to the actual eigenfunction. Q16 gives c>=3 on every nonconstant physical block. For 0<lambda/kappa<3,

    ||(K-lambda/kappa)h||_X
       >=(1-lambda/(3kappa))||Kh||_X.

Combining this with R13 proves lambda>=kappa d4(x). Excitations with lambda/kappa>=3 obey the same bound because d4(x)=3(1-chi(x))<=3. The compact physical spectral resolution returns this to the full original physical form domain:

    Delta_L>=kappa d4(x),
    q_A(f)>=kappa d4(x) Var_(rho_L)(f),
    L>=2, a>0, 0<x<=alpha4.                             (R16)

Thus the result includes states whose original labels depend on L. It is a lower bound on all physical excitations, not a lower bound only on a chosen finite trace family.

## R5. Exact numerical enclosures in original physical units

Rational bisection and integer-square comparisons give

    0.01781868048538520630 < alpha4 < 0.01781868048538520631,
    3.745693472404566975 < 1/(2sqrt(alpha4))
                        < 3.745693472404566976.          (R17)

The exact condition on the original coupling is g^2>=1/(2sqrt(alpha4)). A sufficient rounded condition is g^2>=3.745693472404566976. The parent threshold was about3.825973052393386; the comparison retains that stronger saved value, not an earlier weaker summary.

At g^2=15/4, x=4/225, the bound is

    d4(4/225)>1.5794.

The same rational bound holds for all g^2>=15/4. To verify the required monotonicity, for 0<=x<=4/225 use D4<=1, ell'>=128/3 and R4 to bound

    d4'(x)<=-(3/2)(1-ell(4/225))(128/3)
             +2(1136/13)(4/225)+3p3(4/225)^2<0.

Every number in this final test is rational. Therefore

    Delta_L>1.5794*kappa=3.1588*g^2/a,
    g^2>=15/4.                                        (R18)

At g^2=4, x=1/64,

    d4(1/64)>1.88578,
    ||v-q3||loc<0.019533267617373.                      (R19)

The unchanged physical scale is kappa=8/a there. These bounds include the complete linear and nonlinear tails in R7-R8. The generated verification record contains exact rational brackets, not only these decimal renderings.

## R6. Retained source kernels, complete operator defect, and physical primitive

For the actual finite windows

    V_N=span{R3,J3R3,...,J3^N R3},
    V_N --L3--> V --0--> 0,

the inclusion in degree zero and the identity in degree one give the commuting support transitions. R5 supplies the explicit isomorphism

    V_(N+1)/V_N -> ker[V/L3 V_N -> V/L3 V_(N+1)],
    [h] -> [L3h],   inverse [L3h] -> [h].               (R20)

Changing a representative by L3 V_N changes the inverse by exactly V_N, proving both inverse laws. Subtraction of the actual finite primitive sum leaves J3^(N+1)R3 as the representative. The source label remains attached at a receiving zero. This is the actual Split Zero support-indexed complex and its retained primitive, with the same original coefficient domain throughout.

The map from this source to the physical equation has the exact identities

    K L3 h=Q_H[K-2Gamma(q3,.)]h,
    Q_H A h-kappa K L3h=-2kappa Q_H Gamma(w,h).           (R21)

The right side has X norm at most(2kappa/3)w_*||Kh||_X by the original spin bounds. R11 separately retains the entire multiplication residual and scalar of the reference exponential. Thus no identity between the linearized source and the full physical operator is asserted without its displayed defect.

On centered original physical functions let d_X f=(X_i f)_i, with squared derivative norm kappa int rho_L sum_i |X_i f|^2. The inverse on its actual range is p_X(d_X f)=f. Its uniqueness follows from the derivative-zero functions being constants and the centering condition. The original ground-state map f->psi_L f and its inverse h->h/psi_L preserve the specified pairings. The variational characterization and R16 give

    ||p_X||^2=1/Delta_L<=1/(kappa d4(x)).                 (R22)

An actual gauge-invariant conditional-expectation kernel is a centered subspace. Restriction of R16 to its original closed form consequently gives the same lower bound for its physical restricted operator. This returns the stronger inverse estimate to the previously computed zero-shift response without changing its forcing or Gram matrix.

## R7. Continuum scope and literature correspondence

The standing path is a_n=a0*2^(-n), g_n^2=1/c_n, c_n=g0^(-2)+beta*n*log2. Its inclusion in R16 is exactly c_n<=2sqrt(alpha4). For beta>0 the path eventually leaves this proved domain. This finite-regulator, volume-uniform result does not assign a finite continuum mass or a nontrivial ultraviolet field to that path.

The exponential vacuum and linear excitation equations have established antecedents. In Schuette, Zheng Weihong and Hamer, arXiv:hep-lat/9603026v1, the coefficient x_C=2/g_C^4 and physical operator H_C=g_C^2[K-x_C S]/(2a) have the exact original-coordinate return

    g_C=2^(3/4)g,
    H_original=sqrt(2)H_C(a,g_C)+2kappa xi M I.           (R23)

Substitution verifies both coefficients and the additive energy. Their Hermitian-generator commutator derivative corresponds to iX here, giving the original signs K v-Gamma(v,v)-xi S. The exact physical Haar/energy pairings and complete source residuals in R1-R22 are kept after this comparison. The general method and existence of higher-order calculations are not claimed as new. No global priority or best-known-threshold statement follows from this scoped literature reading.


## R8. Execute the full correction at the calculated fourth source

The fourth table is now used as an actual reference, rather than left as a remainder estimate. Put

    q4=x v1+x^2 v2+x^3 v3+x^4 v4,
    J_[4]h=2B(q4,h), L_[4]=I-J_[4].

Expansion of the unchanged source equation Q2 gives the entire residual, with all ordered contributions:

    R_[4]=x v1+B(q4,q4)-q4
      =x^5[2B(v1,v4)+2B(v2,v3)]
       +x^6[2B(v2,v4)+B(v3,v3)]
       +2x^7 B(v3,v4)+x^8 B(v4,v4).                   (R24)

Each displayed B is the original function with its full union support. The fifth source is not claimed to have been separately expanded into its final channel table. R24 is an exact expression for every part of the reference residual, including the sixth, seventh and eighth degrees.

Use the exact m4,t4 from Q26, together with the earlier m_i,t_i. Define

    l4=m4+4t4,
    b14=3(m1*t4+m4*t1), b24=3(m2*t4+m4*t2),
    b34=3(m3*t4+m4*t3), b44=6m4*t4,
    ell_[4](x)=ell(x)+l4*x^4,
    delta_[4](x)=(2b14+2b23)x^5+(2b24+b33)x^6
                       +2b34*x^7+b44*x^8,
    D_[4](x)=(1-ell_[4](x))^2-(8/3)delta_[4](x).        (R25)

All of these constants are rational and positive. The underlying estimates are exactly Q17:

    ||J_[4]||<=ell_[4], ||R_[4]||loc<=delta_[4].

In particular the fourth contribution to the derivative is
`2*3[m4/6+(2/3)t4]=m4+4t4`, and the factor two in each unequal reference pair is retained.

Let alpha_[4] be the first positive root of the polynomial D_[4]. On [0,182/10000], ell_[4]<1, ell_[4] and delta_[4] are increasing, and

    D_[4]'=-2(1-ell_[4])ell_[4]'-(8/3)delta_[4]'<0.

Exact signs at 181/10000 and 182/10000 therefore prove existence and uniqueness of this root in that interval, and its first-positive-root status. Integer-square comparisons and rational bisection give

    0.018104972231644127075 < alpha_[4]
                           < 0.018104972231644127076,
    3.715960362535435236 < 1/(2sqrt(alpha_[4]))
                        < 3.715960362535435237.         (R26)

For every 0<x<=alpha_[4], L_[4] has its actual norm-convergent Neumann inverse and the complete correction w^[4]=v-q4 is constructed by the same explicit binary-tree series as R5-R7, with the R25 data. Thus

    ||L_[4]^(-1)||<=1/(1-ell_[4]),
    ||w^[4]||loc <= w_[4]*(x)
       =(3/4)(1-ell_[4](x)-sqrt(D_[4](x))).             (R27)

For clarity, set z=L_[4]^(-1)R_[4], C=L_[4]^(-1)B, w_1=z and
`w_n=sum_(i=1)^(n-1) C(w_i,w_(n-i))`. Its scalar majorants are
`z_*=delta_[4]/(1-ell_[4])` and `c_*=(2/3)/(1-ell_[4])`.
The parameter theta_[4]=4c_*z_* lies in [0,1]. The exact complete tail is bounded by

    ||sum_(n>N)w_n||loc
       <=(3/4)(1-ell_[4]) theta_[4]^(N+1)
                          binom(2N,N)/4^N
       <=(3/4)(1-ell_[4]) theta_[4]^(N+1)/sqrt(N+1).    (R28)

At alpha_[4] this converges to zero by the central-binomial bound. The inverse truncation separately has residual
`J_[4]^(N+1)L_[4]^(-1)R_[4]` and norm at most
`ell_[4]^(N+1)delta_[4]/(1-ell_[4])`. These equations control both infinities without replacing their actual coefficient sources. A finite inverse term has original support in at most8+4N faces, and every nonlinear union remains recorded.

The resulting v=q4+w^[4] is C^2 in the original finite-volume coordinates by the same global c-summability proof in R3. Its full equation proves R9-R10 with this v, hence identifies the same actual positive physical vacuum and its scalar. The exact approximate exponential formula is R11 with q3,R3 replaced by q4,R_[4]; the full multiplication defect K R_[4] and the scalar C(q4) remain.

## R9. Strongest full physical lower bound and retained inverse

The actual point-spin bound is now

    t(v)<=t1*x+t2*x^2+t3*x^3+t4*x^4+w_[4]*/6.

The complete physical excitation argument R12-R16 applies to this actual v. Its returned margin is exactly

    d_[4](x)=(3/2)(1+sqrt(D_[4](x)))
             +(1136/13)x^2+p3*x^3+p4*x^4,
    p4=(3/2)m4-6t4
       =32092619324045301088/823531037954625>0.          (R29)

Indeed expanding `3[1-4(t1*x+t2*x^2+t3*x^3+t4*x^4+w_[4]*/6)]` using R27 proves R29 term by term. In particular d_[4]>3/2 on the full closed positive-coupling interval. The exact original theorem is

    Delta_L>=kappa d_[4](xi),
    q_A(f)>=kappa d_[4](xi) Var_(rho_L)(f),
    L>=2, a>0, 0<xi<=alpha_[4].                        (R30)

The proof includes every physical form-domain vector through the complete compact spectral resolution as in R15-R16. No preassigned missing excitation gap is used in the source construction. A sufficient rounded original coupling condition is
`g^2>=3.715960362535435237`; the exact condition is `g^2>=1/(2sqrt(alpha_[4]))`.

At the concrete original parameters,

    g^2=15/4, xi=4/225: d_[4](xi)>1.6584,
    g^2=4, xi=1/64:     d_[4](xi)>1.89811.              (R31)

The first bound holds throughout g^2>=15/4. For x0=4/225 the exact rational inequality

    -(3/2)(1-ell_[4](x0))(128/3)
       +2(1136/13)x0+3p3*x0^2+4p4*x0^3<0

bounds d_[4]' from above for 0<x<=x0, because sqrt(D_[4])<=1 and ell_[4]' >=128/3. Thus d_[4] decreases on that interval. It follows in original physical units that

    Delta_L>1.6584*kappa=3.3168*g^2/a,
    g^2>=15/4.                                        (R32)

At g^2=4 the complete reference error obeys
`||v-q4||loc<0.011169768000312`. The generated receipt retains full rational brackets for the correction, discriminant, and original energy factors.

For the actual source windows `V_N=span{R_[4],J_[4]R_[4],...,J_[4]^N R_[4]}`, the two degree maps and inverse in R20 are now the explicit maps

    [h] -> [L_[4]h], inverse [L_[4]h] -> [h].

They are well-defined on `V_(N+1)/V_N` and the corresponding transported cohomology kernel because L_[4] is injective and its inverse is R27. Both inverse compositions remain literal. The receiving scalar, support and full physical defect are

    K L_[4]h=Q_H[K-2Gamma(q4,.)]h,
    Q_H A h-kappa K L_[4]h=-2kappa Q_H Gamma(w^[4],h),
    ||p_X||^2=1/Delta_L<=1/(kappa d_[4](xi)).             (R33)

The defect norm is at most `(2kappa/3)w_[4]*||Kh||_X`. The physical derivative norm and ground-state multiplication/division maps are exactly those in R22. Thus the stronger inverse also restricts to the original physical conditional kernel, without changing a forcing vector or its raw Gram matrix.

The standing simultaneous path has the exact domain

    a_n=a0*2^(-n), g_n^2=1/c_n,
    c_n=g0^(-2)+beta*n*log2 <= 2sqrt(alpha_[4]).          (R34)

For beta>0 it eventually leaves the certified interval. The root in R26 is the endpoint of this particular proved majorant, not an assigned singularity of the actual theory. This contribution gives no ultraviolet continuum field or finite positive continuum mass. The complete fourth table and its q4 correction are now finished inputs; the next unevaluated coefficient is the original channel-resolved v5.


# The complete sixth-order ground energy and its original cube contribution

17 September 2026. This calculation uses the actual fourth source evaluated in `QUARTIC_SOURCE.md`, not a finite Hamiltonian approximation. The original scalar energy and all extensive and boundary factors are retained. The coefficient is reproduced by an independent eigenvector recurrence, and the cube contribution is additionally computed by all720 original face orderings.

## E1. Eliminate the fifth source through its exact equation

Retain the original real Haar pairing and source recurrence. Since

    C(v)=int_H Gamma(v,v), E0=2kappa xi M-kappa C(v),

its sixth energy coefficient is

    e6:= [xi^6](E0/kappa)
       =-2 int Gamma(v1,v5)-2 int Gamma(v2,v4)-int Gamma(v3,v3).

The original fifth equation is Kv5=2Q_H Gamma(v1,v4)+2Q_H Gamma(v2,v3). Integrating against the zero-Haar-mean v1, and using int Gamma(f,h)=int f Kh, gives

    e6=-4 int v1 Gamma(v1,v4)-4 int v1 Gamma(v2,v3)
        -2 int Gamma(v2,v4)-int Gamma(v3,v3).             (E1)

This identity includes all fifth-source contributions; none is estimated or discarded. For a specified original multiset of six faces, expand every product in E1 over ordered allocations of that multiset to the displayed sources. A repeated label is allocated by its actual multiplicity, as in Q11. The resulting coefficients depend only on sources through degree four, all evaluated in the adjoining tables.

## E2. Exact original Haar integration

Each word is evaluated in its original SU(2) edge variables. For an edge of even total occurrence r, its full spin-zero projector on that polynomial is

    P_e,0=product_(j=1,...,r/2)[I-E_e/(j(j+1))].         (E2)

Odd occurrence has zero Haar integral, proved by U_e->-U_e. Formula E2 follows by its values1 on Casimir0 and0 on each original positive spin Casimir in that edge's complete occurrence range. Its output is independent of U_e. Thus replacing U_e by I after E2 is the actual original-edge integration, not a substitution for an unevaluated integral. Repeat over every edge. Q4-Q7 make each step a rational original trace calculation. The code retains the resulting constants, including tr(I)=2.

The integration algorithm is independently checked on the fundamental character moments1,2,5 at powers2,4,6. For every sixth-order coefficient below, the same final number is obtained from the separate Rayleigh-Schrodinger recurrence for the original K-xi S. Its overall vacuum amplitude remains a separate scalar factor; the energy coefficients are independent of that factor because the original eigen-equation is homogeneous in it. The numerical polynomial entries in that recurrence are coefficient multipliers, not an assigned physical vacuum norm. The actual amplitude and original unit Haar norm are returned by R9.

Explicitly, with multivariate face couplings, write those coefficient multipliers as u_C, u_empty=1, int u_C=0 for C nonempty, and keep the overall scalar amplitude a as a separate factor a u_C. The energy coefficients satisfy

    e_C=-sum_(p distinct in C) int W_p u_(C-{p}),
    u_C=K^(-1)Q_H[sum_(p distinct in C)W_p u_(C-{p})
                   +sum_(empty!=A proper submultiset C)e_A u_(C-A)].    (E3)

Both equations follow by comparing each original face-coupling monomial in K(a sum u_C x^C)-sum_p x_p W_p(a sum u_C x^C)=e(x)(a sum u_C x^C). The same scalar a appears on both sides; no energy or coupling is rescaled. E3 and E1 give the same six local coefficients. The first calculation uses the logarithmic-vacuum equation, while E3 uses the original linear eigen-equation.

## E3. Exhaustion of the sixth-order connected supports

For each face p, changing U_e to -U_e on one original edge multiplies a source coefficient by the parity of that edge's total original occurrences. Differentiation and all Casimir inverses commute with this center action. A nonzero Haar scalar therefore requires the set of odd-multiplicity faces to have even boundary over F2.

A nonempty finite even-boundary set of elementary cubic faces has at least six faces. Equality is the six-face boundary of one original cube. Here is an explicit finite filling argument. Let c12,c13,c23 be its binary face arrays. Set the binary cube array

    b(n1,n2,n3)=sum_(k>n3)c12(n1,n2,k) mod2.

The edge-boundary equations imply that the sum over k of c12 is constant in n1 and n2; finite support makes that constant zero. Thus b is finite also toward negative n3. Its upper-minus-lower cube boundary has the required c12 array. The remaining face difference is a finite2-cycle with c12=0. The boundary equations on directions1 and2 force its c13,c23 arrays to be constant in direction3; finite support makes them zero. This proves the finite filling and its exact boundary map.

For a nonempty finite cube array b, each nonempty column along an axis has at least two boundary faces normal to that axis. Therefore its boundary has at least twice the sum of the cardinalities of its three coordinate projections, hence at least six. Equality forces each projection to be a singleton, so b is exactly one cube. This proves the stated six-face classification without deleting nonreduced or repeated face labels.

At total order six, all-even multiplicities are6,4+2,2+2+2. Their connected distinct-face supports are respectively a single face, an adjacent pair, or a path/common-edge/corner triple. The only all-odd surviving support is one complete cube. Disconnected supports have zero logarithmic energy coefficient by Q11 and E1; equivalently the original operator on disjoint active link supports is the sum of its commuting tensor-factor operators, so their scalar eigen-energy has no mixed coefficient. The original scalar and all variables remain in that tensor comparison.

## E4. Complete local coefficient table

The coefficient for each indicated original multiset is

| Original multiset | e_C |
|---|---:|
| {p,p,p,p,p,p} | -289/77760 |
| {p,p,p,p,q,q}, p~q | 22285/47309184 |
| {p,p,q,q,r,r}, distinct path | -4909/118272960 |
| Same multiplicities, common-edge triple | 244/4312035 |
| Same multiplicities, cube corner | -212/542997 |
| Six distinct faces bounding one cube | -83/1944 |

The first pair row has the separate original role exchange p<->q; a sum over unordered adjacent pairs counts both roles. The complete finite evidence includes both pair embeddings (coplanar and perpendicular), all nine original cubic-orbit embeddings of distinct triples, and the exact coefficients computed from both E1 and E3.

For clarity, the four terms in E1 for the cube are

    -43/1458, -7/972, -13/2916, -1/648.

For the single face they are

    -17/5832, -1/1458, 17/46656, -7/14580.

Their sums give the corresponding rows. `sixth_energy.json` retains all four terms for every row, together with their original face words and multiplicities.

## E5. A second, path-resolved cube proof

Orient the six cube faces outward. Reversing a whole SU(2) loop preserves its trace, so this is the exact original trace product. Each of the twelve edges now occurs once as U and once as U^(-1). The original integral

    int U_ij conjugate(U_kl)=delta_ik delta_jl/2

supplies twelve factors1/2. Its delta identifications leave one free fundamental color at each of the eight vertices. Hence

    int product_(six cube faces) W_p=2^8/2^12=1/16.     (E4)

In the independent six-distinct-face perturbation coefficient, each proper subset has zero scalar energy coefficient by E3 and the even-boundary argument. In any original ordering, edges occurring twice in an intermediate subset occur in no later face. Integration of those edges projects them onto spin zero. Every edge occurring once carries spin1/2. The original intermediate Casimir is consequently exactly (3/4)|boundary(subset)|. These projections commute with later independent edge variables and with the original total K. Therefore the full cube coefficient is

    -(1/16) sum_(pi in S6) product_(j=1)^5
                        4/[3 |boundary(first j faces of pi)|].       (E5)

No intermediate denominator is replaced by the plaquette denominator3. The complete path count is

| Five successive boundary lengths | Multiplicity |
|---|---:|
| (4,8,8,8,4) | 48 |
| (4,8,8,6,4) | 96 |
| (4,6,8,8,4) | 96 |
| (4,6,8,6,4) | 192 |
| (4,6,6,6,4) | 288 |

There are720 paths. Their rational sum before the1/16 factor is166/243. Equation E5 therefore gives exactly -83/1944, matching the complete coefficient recurrence. This retains all original intermediate boundaries, their denominators, and the terminal Haar contraction. It is the first closed-surface scalar term on six distinct original faces.

## E6. All original finite-box factors and the complete higher-order remainder

Let m=2L. Denote by M,J,P,T,C,B the numbers of original faces, unordered adjacent pairs, three-face paths, common-edge triples, corners and cubes. Their exact values are

    M=3m^2(m+1), J=6m(3m^2-1),
    P=138m^3-126m^2-24m+12,
    T=12m^2(m-1), C=8m^3, B=m^3.                       (E6)

For T sum binom(r_e,3) over the original edge degrees r_e in {2,3,4}. There are3m(m-1)^2 degree-four edges and12m(m-1) degree-three edges, giving the stated T. Each cube has eight three-face corners. To obtain P, count centered face-adjacency wedges and subtract three for each triangular triple. A face degree is s_i+s_j+4r_k-4, where s_i,s_j are3 at one of the two cell-end positions and4 otherwise, and r_k is1 at either normal boundary and2 internally. The direct count is

    sum_p binom(deg p,2)=198m^3-162m^2-24m+12.

Subtract3(T+C), proving P. These formulas preserve every original open boundary. The verifier independently enumerates the actual boxes L=2,3,4.

Summing all rows in E4 gives

    e6= -289M/77760 +22285J/23654592 -4909P/118272960
                       +244T/4312035 -212C/542997 -83B/1944
       =-(211396463m^3+30959193m^2+21845782m+2336684)/4691494080.   (E7)

Thus the original full ground energy is

    E0,L=2kappa M xi-kappa M xi^2/3
       +kappa(5M/216-2J/1053)xi^4+kappa e6 xi^6+R_ge8.  (E8)

The parent analyticity proof on the complex circle |xi|=1/60 bounds the complete scalar C(v) by49|E_L|/1200 there. The new source agrees coefficientwise with that proved construction. The exact center involution makes E0-2kappa Mxi even. Cauchy's estimate and the full geometric tail therefore give

    |R_ge8| <= (49kappa |E_L|/1200)
                 (60|xi|)^8/[1-(60|xi|)^2],
    0<|xi|<1/60.                                       (E9)

The finite coefficient polynomial is accompanied by all higher orders through this bound. Its validity range remains stated; it is not silently extended past the Cauchy circle.

At L=2, e6=-3528610133/1172873520. Along the original spatial-volume limit m->infinity, the coefficient per face is

    lim e6/M=-211396463/14074482240.                     (E10)

This is a limit of the specified Taylor coefficient with its complete original counts. It does not by itself exchange a spatial or ultraviolet limit with a coupling series beyond the proved domain.

## E7. Literature and scope

Schuette-Zheng-Hamer's coupled-cluster/character method and Llewellyn Smith-Watson's shifted linked-cluster formulation are primary antecedents, arXiv:hep-lat/9603026v1 and hep-lat/9212025v1. The former's operator dictionary to Q1 is R23. The latter explicitly describes its truncation and cluster-shift prescriptions; this calculation keeps the original products and uses the full residual bounds R3-R8 and E9. This establishes the method correspondence and the actual all-order error returned here; it is not a claim that the general expansion method or every displayed coefficient is historically new. The scoped search did not establish an independent published match or global priority for the full spatial sixth coefficient E7.


## E8. Return to an actual measured plaquette observable

For real 0<xi<1/60 at fixed original kappa, the constructed simple vacuum is differentiable in xi. Its original mass is one, hence `2 Re<psi,partial_xi psi>=0`. Differentiating `H psi=E0 psi` and testing with the same psi therefore proves the exact Hellmann-Feynman identity

    dE0/dxi = kappa(2M-sum_p <W_p>_rho).

No derivative of the vacuum is omitted: its two terms cancel through the displayed mass derivative and the actual eigen-equation. Define the original mean half-trace as an explicit observation map

    P_L(xi)=(1/(2M))sum_p <W_p>_rho.

Keeping M and the complete coefficients e4,e6 from E8 gives

    P_L(xi)=xi/3-(2e4/M)xi^3-(3e6/M)xi^5+R_P,L,
    |R_P,L| <= (49|E_L|/(40M))
         (60xi)^7 [8-6(60xi)^2]/[1-(60xi)^2]^2.         (E11)

To prove the tail, the same original Cauchy bound used in E9 gives
`|e_(2n)|<=(49|E_L|/1200)60^(2n)` for every n>=4. Differentiate its absolutely convergent series on |xi|<1/60. The exact scalar sum

    sum_(n>=4)2n r^(2n-1)=r^7(8-6r^2)/(1-r^2)^2

follows by differentiating r^8/(1-r^2). Its factor60 and the factor1/(2M) in the actual observation give precisely E11. The ratio |E_L|/M=(m+1)/m is retained and is at most5/4 for L>=2; consequently the entire error is independent of exterior volume after this explicitly defined spatial average.

For each fixed coefficient, all connected source supports have a finite number of original faces. Their interior translates contribute the same coefficient, and the boundary embeddings have vanishing proportion as m->infinity. The bounds just used are uniform after division by M. Dominated power-series summation therefore proves the full mean-observable limit on |xi|<1/60, as well as differentiation of its energy-density series. Its first terms are

    P_infinity(xi)=xi/3-(11/468)xi^3
                       +(211396463/4691494080)xi^5+R_P,infinity,
    |R_P,infinity| <= (49/40)
         (60xi)^7 [8-6(60xi)^2]/[1-(60xi)^2]^2.         (E12)

This is a fixed-lattice-spacing observable return. No continuum scaling limit is used in the coefficientwise or dominated-series argument.

## E9. Explicit correspondence to a current variational benchmark convention

Spriggs, Greplova, Carrasquilla and Nys, arXiv:2509.12323v1, equation1, use the physical convention

    H_N(g_N,a)=g_N^2/a [K/2+(4/g_N^4)sum_p(1-W_p/2)].

Specialize this formula to the same original edge and face sets as Q1. Then the literal coefficient substitution is

    g_N=2g, lambda_N=4/g_N^4=xi,
    H_N(2g,a)=H_original(g,a),
    (a/g_N^2)H_N=H_original/(2kappa).                   (E13)

The generator commutators and E^2=-Delta_(S3)/4 in their equations1-3 agree with the original T_alpha=-i sigma_alpha/2 coordinates through their Hermitian derivative iX. Direct substitution in E13 gives exactly kappa and kappa xi for the two original coefficients. The trace map in their equation4 is W_p->W_p/2, precisely the measured observation in E11. All energy and trace factors are exhibited.

Their reported finite numerical lattices have their own boundary choice. To retain the comparison on a periodic extension of our same vertex set, let J be pullback from the old edge variables, with inverse adjoint the Haar integral over the additional wrapping links. For side2L+1>=5 its actual operator defect is

    H_periodic J-J H_open
       =kappa xi sum_(p in P_periodic\P_open)(2-W_p)J.  (E14)

The electric terms on the added links annihilate the pullback, and all old terms agree; expansion proves E14. Thus E13 is a convention correspondence on matched index sets, and E14 keeps the added interactions needed for the other boundary choice. No numerical data from that paper are presented as an evaluation or independent verification of E7 or E12. The earlier 1985 perturbative source cited in that paper was identified bibliographically but its full text was not retrieved here. The new coefficients and remainder are offered as explicit original-convention benchmark data, with their written derivation and exact replay.


# Completed fourth-order source in the original lattice coordinates

Audit and continuation, 17 September 2026. The requested basis is the supplied
`Pasted markdown(6).md`. Its original bytes are preserved in `input/`. The
published cubic predecessor was read at Git revision
`91434b6962062bd80439d4cb2cae9d2479264dde`; source recovery and its limits are in
`sources/`. This note gives a complete, executable fourth-order source catalogue.
It makes no new claim about a uniform gap or the four-dimensional continuum.

## 1. Operator, source, and the distinction that needs to be retained

Use the original finite open cubic graph and positive edges, generators
`T_a=-i sigma_a/2`, derivatives `X_e,a`, and Haar probability. Write

\[
 K=-\sum_{e,a}X_{e,a}^{2},\qquad
 H=\kappa[K+\xi(2M-S)],\quad S=\sum_pW_p,
 \quad\kappa=2g^2/a,\quad\xi=1/(4g^4).
\tag{Q1}
\]
The original ordered face is
`W_(n;i,j)=tr(U_i(n)U_j(n+e_i)U_i(n+e_j)^-1 U_j(n)^-1)`.
Let `P_H` be Haar expectation and `Q_H=I-P_H`. The original physical source
is the zero-Haar-mean logarithmic vacuum `v=Q_H log psi`, with scalar return

\[
 \psi=\exp(v+c),\quad c=-\tfrac12\log\int e^{2v}dU,\qquad
 E_0=\kappa[2M\xi-P_H\Gamma(v,v)],
 \quad\Gamma(f,h)=\sum_{e,a}(X_{e,a}f)(X_{e,a}h).
\tag{Q2}
\]
The scalar `c` and the additive original energy have not been discarded.
The coefficient equation is

\[
 v=\xi v_1+B(v,v),\qquad v_1=S/3,\quad
 B(f,h)=K^{-1}Q_H\Gamma(f,h).
\tag{Q3}
\]
The inverse in Q3 is on its actual nonconstant physical polynomial image.
On a fixed finite graph its uniqueness follows from the positive Casimir and
Haar centering.

Consequently, at `q2=xi*v1+xi^2*v2`, the exact residual and full fourth
coefficient are different specified expressions:

\[
 R_2=\xi^3v_3+\xi^4b_{22},\quad b_{22}=B(v_2,v_2),\qquad
 \boxed{v_4=2B(v_1,v_3)+b_{22}.}
\tag{Q4}
\]
The uploaded L5–L7 give `b22`. Equation Q4 retains the additional incoming
source and its unique `K^{-1}Q_H` primitive. This package computes their
signed sum before any norm bound.

## 2. The exact tree-coordinate map and its inverse

For the original edge union E of a connected face cluster, choose the stored
spanning tree T, root o, and original oriented chords `c_1,...,c_r`, where
`r=|E|-|V|+1`. For a vertex v let `h_v(U)` be the original ordered product
along the tree path from o to v, using inverse links on reverse traversals.
Define

\[
 Z_j=h_{s(c_j)}(U)\,U_{c_j}\,h_{t(c_j)}(U)^{-1},
 \qquad
 \Phi:SU(2)^E\longrightarrow SU(2)^T\times SU(2)^r,
 \quad U\longmapsto(U_T,Z).
\tag{Q5}
\]
Its inverse keeps `U_T` and sets
`U_c=h_s(U_T)^-1 Z_c h_t(U_T)`. Both compositions are literal identities.
Successive left and right Haar translations in the chord variables prove
`dU=dU_T dZ`. A gauge-invariant function pulls back from a function of Z
invariant under simultaneous conjugation; its original Haar norm is exactly
its product-Haar norm in these variables. The remaining root gauge action
is retained, rather than treated as an extra independent observable.

At the slice `U_T=I`, an original chord derivative is `L_(j,a)`, the original
left generator of Z_j. For a tree edge e, let `s_e(c),t_e(c)` be the zero-one
indicators that the original paths to the two chord endpoints cross e.
Up to the common path-orientation sign for that one e, its field is

\[
 V_{e,a}=\sum_c[s_e(c)L_{c,a}-t_e(c)R_{c,a}].
\tag{Q6}
\]
The common sign cancels in the original squared generator and in Gamma.
The reduced kinetic operator is the exact original operator

\[
 K_T=-\sum_{e\in E,a}V_{e,a}^{2}.
\tag{Q7}
\]
To prove Q6–Q7, vary one original tree link as `exp(tT_a)U_e`, and then apply
Q5. Each affected chord becomes `exp(epsilon*s_e*tT_a) Z_c
exp(-epsilon*t_e*tT_a)`. Its first and second derivatives are precisely the
stated fields. Gauge covariance returns this identity from the tree slice
to every original configuration. The checker additionally verifies it by
independent second-order quaternion jets through every original edge of
all 78 representatives. Those are supplementary coordinate tests; Q5–Q7
are the analytic identification of the operator.

## 3. Complete polynomial coordinates with exact relations

Each stored chord has quaternion coordinates
`Z=q0 I-i(q1 sigma1+q2 sigma2+q3 sigma3)`, with
`q0^2+q1^2+q2^2+q3^2=1`. The algebra is the rational polynomial quotient by
these original sphere relations, one per chord. In the stored representative
monomials each q0 exponent is zero or one. The relation maps are explicit:
`q0^2 -> 1-q1^2-q2^2-q3^2`; their inverse interpretation is evaluation on the
original sphere. The ideal generators have relatively prime leading
monomials in different chord groups, so this representation is unique.
No state or energy metric is replaced by a Euclidean coefficient norm.

The generator matrices are the original quaternion multiplications by
`(0,e_a/2)` on the left or right. Thus all their entries are rational halves.
The original moments are

\[
 \int q_0^{d_0}q_1^{d_1}q_2^{d_2}q_3^{d_3}\,dq=0
 \quad\hbox{if any }d_i\hbox{ is odd},
\]
\[
 \int\prod_iq_i^{d_i}dq
 =\frac{\prod_i(d_i-1)!!}{4\cdot6\cdots(2+\sum_i d_i)}
 \quad\hbox{when all }d_i\hbox{ are even}.
\tag{Q8}
\]
The empty denominator and `(-1)!!` are one. Products over distinct chords
use independent original Haar factors. Q8 supplies every mean and full
polynomial Gram used in the package.

## 4. The exact finite inverse and coefficient recurrence

Introduce formal face source coordinates `lambda_p`, with the original
physical diagonal map `lambda_p=xi` after all coefficients have been
computed. The exact physical operator on that diagonal is Q1.
For a multiindex nu, its original edge multiplicity is
`m_e(nu)=sum_(p containing e) nu_p`. Its allowed edge spins are
`j_e=m_e/2,m_e/2-1,...` down to zero or one half. Therefore the finite list
of possible positive Casimirs on that source is

\[
 \mathcal C_\nu=
 \left\{\sum_ej_e(j_e+1)>0:
 j_e\in\{m_e/2,m_e/2-1,\ldots\}\right\}.
\tag{Q9}
\]
Extra allowed values are harmless. The implementation proves that its
returned inverse solves the original equation, not just a matrix fit.
For a centered forcing f, start `r0=f`, `y0=0`, and for each `c in C_nu` set

\[
 y_{j+1}=y_j+r_j/c,\qquad r_{j+1}=r_j-K_Tr_j/c.
\tag{Q10}
\]
The exact identity is `K_T y_j=f-r_j` at every stage. The final polynomial
`r_j` is checked to be zero in the original sphere quotient. This gives a
unique centered inverse because K_T is a sum of nonnegative squares and
its chord fields alone force a zero-derivative function to be constant.
All these operations have finite degree because this is a coefficient
calculation at a stated order; no finite-spin approximation to the full
Hamiltonian or its spectrum is used.

For explicit arithmetic it is convenient to use a formal eigenline
representative `u(lambda)=1+sum_(nu!=0)u_nu lambda^nu`, `P_H u_nu=0`, of
`K-sum_p lambda_p W_p`, with eigenvalue `e(lambda)`. This is an explicitly
recorded choice of the scalar coordinate of the eigenline. Its exact return
is `v=Q_H log u`, followed by Q2 for the physical unit vacuum. The inverse
coordinate relation is `u=e^v/(P_H e^v)`, whose denominator has constant
coefficient one. The original physical normalization is not dropped.
The recurrences used are

\[
 F_\nu=\sum_{p:\nu_p>0}W_pu_{\nu-e_p},\qquad
 e_\nu=-P_HF_\nu,
\]
\[
 K_Tu_\nu=Q_HF_\nu+
   \sum_{0<\mu<\nu}e_\mu u_{\nu-\mu},\quad P_Hu_\nu=0.
\tag{Q11}
\]
Terms are interpreted coefficientwise, with `mu<=nu`. Writing
`l=log u`, differentiation of the formal series gives the complete
coefficient relation

\[
 l_\nu=u_\nu-\frac1{|\nu|}
     \sum_{0<\mu<\nu}|\mu|\,l_\mu u_{\nu-\mu},
 \qquad v_\nu=Q_Hl_\nu.
\tag{Q12}
\]
As an independent polynomial check for each coefficient the program verifies

\[
 K_Tv_\nu=
 Q_H\!\sum_{0<\mu<\nu}
 \Gamma_T(v_\mu,v_{\nu-\mu}),\qquad |\nu|>1,
\tag{Q13}
\]
with `K_Tv_(e_p)=W_p` and
`2 Gamma_T(f,h)=(K_T f)h+f(K_T h)-K_T(fh)`.
These are identities of complete rational polynomials, not agreements only
at finitely many sampled configurations.

## 5. All connected fourth-order supports are included

The source operation Gamma differentiates a common original link. Its
inverse Casimir creates no new link. Consequently every nonzero logarithmic
coefficient has an edge-connected face multiset. Starting from the four
faces incident on the original anchor edge `(0,0,0;direction0)`, the
following exhaustive recursion suffices: add a repeated present face or a
face sharing an original edge with a present face, and retain the sorted
multiset. Any connected multiset containing that anchor can be recovered
in this way by removing a leaf of a rooted spanning tree of its adjacency
graph, or one repeated occurrence. Counts by order are

\[
 4,\quad46,\quad612,\quad8621.
\tag{Q14}
\]
The 48 signed coordinate permutations and translations act on the original
faces and links. A reversed edge maps to its inverse; this is a Haar- and
Casimir-preserving coordinate map. A reversed complete SU(2) face word has
the same trace. Each orbit is represented by its explicitly stored minimum
corner coordinates and ordered axes. The fourth-order orbit counts are

| Face-multiplicity partition | Orbits |
|---|---:|
| 4 | 1 |
| 3+1 | 2 |
| 2+2 | 2 |
| 2+1+1 | 19 |
| 1+1+1+1 | 54 |
| Total | 78 |

`results/quartic_coefficients/class_00.json` through `class_77.json` contain
all 4,044 nonzero rational monomials of these 78 fully calculated source
coefficients. They also give original faces, tree links, chords, root,
original derivative fields, coupling multiindex, Haar mean and full Haar
state/energy norms. These auxiliary Haar norms are not asserted to be the
interacting physical norms.

One class (index25) has four distinct faces but five chord variables: the
four-sided tube formed by the cube's lateral faces. Its original graph has
an extra independent cycle. The implementation retains it. Replacing the
chord count by the number of faces would change this original source.

The source for any original finite box is reconstructed by summing each
contained connected multiset once, pulling its representative polynomial
back through the stored lattice symmetry and Q5, and setting every formal
face coordinate to xi. Q11–13 already include the correct multiplicities;
no additional division by 4! is applied. `results/anchored_quartic_transports.json`
also records all 8,621 original face multisets, their class numbers, and an
explicit signed coordinate permutation plus translation for each. The original
edge orientation and inverse-link rule are implemented by `transform_edge` in
`calculations/reconstruct.py`. This is a complete finite, coordinate-level
specification of v4, rather than an unevaluated B term.

## 6. A readable closed component and the signed derivative

For a single face the fully evaluated contribution is

\[
 \boxed{v_4^{(p^4)}=
   \frac{17}{10368}\chi_1(\Omega_p)
   -\frac7{51840}\chi_2(\Omega_p).}
\tag{Q15}
\]
The own-face part of the already available b22 is
`chi1/10368-chi2/31104`. The other incoming term in Q4 has coefficients
`chi1/648-chi2/9720`. Adding them gives Q15 exactly.
The signs remain in the catalogue before any norms are taken.

The catalogue also determines every formal plaquette-direction response
through degree three by the exact derivative

\[
 Z_p^{[3]}=\partial_{\lambda_p}
       \sum_{1\le|\nu|\le4}\lambda^\nu v_\nu.
\tag{Q16}
\]
Differentiating Q13 coefficientwise proves that the terms through total
degree three in
`[K-2Q_H Gamma(q3,.)] Z_p^[3] - W_p` vanish, with
`q3=sum_(1<=|nu|<=3) lambda^nu v_nu`.
The remaining degree4–6 polynomial is exactly the corresponding sum of
those unremoved higher products. This records the signed tangent data; it
is not being promoted to a uniform bound on the full linearized inverse.

The previous numerical coupling threshold requires a coefficient trace-norm
bound and a full infinite-tail argument. This session does not replace
those with the catalogue's Haar norms or assert a new threshold.

## 7. Evidence scope

Every returned coefficient has zero Haar mean, an exact inverse residual,
and an independently expanded exact logarithmic-source residual. The sum
over all 78 coefficient downsets executes 1,053 inverse/source steps. The
additional second-order-jet audit differentiates original unfixed links and
verifies the tree return and original vertex-gauge invariance at retained
rational assignments for every representative. Those assignments are an
independent regression; the polynomial equalities and operator maps above
are the identity argument. No independent external or Lean review is
claimed. The full raw input, recovered code, calculations and receipts are
included in this session's ZIP.


# Completed sixth-order ground-energy calculation, including the cube surface

Audit and continuation, 17 September 2026. This result is derived in this
session. The uploaded status line about sixth-order coefficients contained
no such coefficient table, proof, or execution record. The formulas below
retain the original Hamiltonian and open-box geometry. They are finite-order
coefficients with a separately proved finite-volume remainder, not a new
uniform-coupling or continuum mass-gap theorem.

## 1. Original parameters and exact coefficient convention

Use Q1 of `FOURTH_ORDER_SOURCE.md`:

\[
 H=\kappa\{K+\xi(2M-S)\},\qquad S=\sum_p W_p,
 \quad\kappa=2g^2/a,\quad\xi=1/(4g^4).
\tag{E1}
\]
Write the ground eigenvalue of `K-xi S` as
`e(xi)=e2 xi^2+e4 xi^4+e6 xi^6+...`. Then the original physical energy is
`E0=kappa(2M xi+e(xi))`. The additive original scalar stays in this equation.
A link-center transformation
`U_(n,i) -> (-1)^(sum_(j<i)n_j) U_(n,i)` preserves Haar and K and changes
every W_p to -W_p. It intertwines `K-xi S` with `K+xi S`; the ground
branch near zero is simple, so e is even.

Use the formal eigenline representative
`u=1+xi u1+xi^2 u2+...`, `P_H un=0`. The exact scalar return to the
original unit vacuum is Q2 and Q12 of the companion. The low-order equations
are

\[
 u_1=K^{-1}S=S/3,\qquad
 u_2=K^{-1}Q_H(Su_1),\qquad
 u_3=K^{-1}Q_H(Su_2+e_2u_1),
\]
\[
 e_2=-\langle S,u_1\rangle_H=-M/3,\qquad
 e_4=-\langle S,u_3\rangle_H=5M/216-2J/1053.
\tag{E2}
\]
Here J counts original unordered pairs of plaquettes sharing an edge.
All pairings are original Haar pairings.

The complete sixth coefficient depends only on these three actual
wavefunction coefficients:

\[
 \boxed{e_6=-\langle u_3,Ku_3\rangle_H
             -e_4\|u_1\|_H^2-e_2\|u_2\|_H^2.}
\tag{E3}
\]
For an explicit proof, use `e6=-<S,u5>=-<u1,Ku5>`.
The order-five equation is `Ku5=Q_H S u4+e2 u3+e4 u1`.
Move K through `<S u1,u4>` by `Ku2=Su1+e2`, and then use
`Ku4=Q_H S u3+e2 u2+e4`. Finally substitute
`Su2=Ku3-e2 u1`. The two cross terms `e2<u1,u3>` cancel; the remaining
terms are precisely E3. This also shows why the two state-denominator
corrections in E3 must be retained.

## 2. Complete third-vector spectral data

For one face the spin-3/2 character component of u3 is
`chi_(3/2)(Omega_p)/360`. Its kinetic norm contribution is 1/8640.
The coefficient of the original W_p in the assembled u3 is

\[
 a_p=-5/216+d_p/1053,
\tag{E4}
\]
where d_p is its original plaquette adjacency degree. This is obtained by
multiplying the self and adjacent components of u2 by each possible outer
face in `S u2+e2 u1`. It is also the coefficient required by
`e4=-sum_p a_p` and `sum_p d_p=2J`.

For the repeated multiset p,p,q on adjacent faces, put
`F=(W_p^2-1)W_q`. The two actual shared-edge spins are 1/2 and 3/2,
with Casimirs 9 and 12. The coefficients in u3 are

\[
 r_{1/2}=\frac{1/24+1/9+1/39}{9}=\frac{167}{8424},
 \qquad
 r_{3/2}=\frac{1/24+4/39}{12}=\frac5{416}.
\tag{E5}
\]
Their Haar squared masses are 1/3 and 2/3. To verify the lower mass,
write the original shared unit quaternion u and complementary unit
quaternions v,w. The harmonic projection is
`H=(8/3)(u dot v)(v dot w)-(2/3)(u dot w)`.
Using `int u_i u_j=delta_ij/4` and independent Haar in v,w gives
`<H^2>=4/9+1/9-2/9=1/3`. The full `<F^2>=1`, giving the other mass.
Thus each oriented repeated-adjacent contribution to `<u3,Ku3>` is

\[
 R_{\mathrm{adj}}=3r_{1/2}^{2}+8r_{3/2}^{2}
                 =110453/47309184.
\]
A repeated nonadjacent pair has coefficient `1/72`, Casimir 11, Haar
squared norm one, hence contribution `R_dis=11/5184`.

For a distinct pair in u2 the adjacent coefficients are
`u_0=4/27`, `u_1=4/39`, with shared-edge masses 1/4 and 3/4.
The adjacent-pair squared norm in u2 is therefore

\[
 P_2=\tfrac14(4/27)^2+\tfrac34(4/39)^2=1648/123201.
\tag{E6}
\]
The nonadjacent-pair value is 1/81, and the self value is 1/576.

For three distinct faces the original projection masses and Casimirs are
as follows. Each coefficient is the sum of its three possible outer-face
sources from E2, divided by that actual Casimir.

* No adjacency: coefficient 1/27, Casimir 9, squared mass one.
* One adjacent pair: `u_s/3`, Casimir `15/2+2s`, masses 1/4,3/4.
* Two-edge path: coefficient `(1/9+u_s+u_t)/(6+2s+2t)`, with masses
  `(1,3,3,9)/16` for shared-edge spins `(0,0),(0,1),(1,0),(1,1)`.
* Common-edge triple: coefficients
  `(3/2)(u_0+u_1)/(15/2)` and `3u_1/(21/2)`; squared masses 1/2,1/2.
* Cube corner: coefficient `[(3-n)u_0+n u_1]/(9/2+2n)`;
  the n=0,2,3 squared masses, with n=2 aggregated, are `1/16,9/16,3/8`.
  The n=1 subspace is killed by the original vertex invariant projection.

Here is a derivation of all nontrivial masses. For a path, one shared-edge
Haar projection is one half of the original two-face boundary times the
third trace, with squared norm 1/4. Both such projections give one quarter
of the eight-link boundary trace, with squared norm 1/16. Orthogonality of
the commuting original edge projections gives the remaining three masses.
For a common edge, expose three independent complementary unit quaternions
and the shared original unit quaternion. Each pair singlet term has squared
norm 1/4, and each distinct cross pairing is 1/16. The identity
`P_(1/2)F=(2/3)sum W_r P_0(W_p W_q)` gives mass
`(4/9)(3/4+6/16)=1/2`; its complement has the other half.
For a corner, the triple-singlet projection is one quarter of the six-link
boundary, of squared mass 1/16. Each single-edge-singlet projection has
squared mass 1/4. Its only additional component is one of the three n=2
channels, of mass 3/16. The full mass is one, so the n=3 remainder is 3/8.
All simple-loop Haar squared norms here equal one by integrating one of
its original links. Unique exterior links justify the stated product masses.

These give the following exact kinetic contributions for each distinct
triple in u3:

| Adjacency type | Contribution to `<u3,K u3>` |
|---|---:|
| none | 1/81 |
| one pair | 4768/369603 |
| path | 1595629/118272960 |
| common edge | 20032/1437345 |
| cube corner | 210880/14660919 |

The direct original-generator calculation in `gauge_polynomial.py` constructs
u1,u2,u3 without this table, using the exact K fields and inverse residuals.
It agrees with E3 and the table for every geometric orbit of a connected
one-, two-, or three-face set. That calculation also verifies the complete
Rayleigh numerator and denominator identity, preserving all cross terms.

## 3. Linked contributions and why six distinct cube faces occur

With independent formal face couplings, an energy coefficient with support
split into edge-disjoint components is additive in those components. The
full Haar space, electric operator and potential factor over the disjoint
edge sets; their positive vacuum product is already gauge invariant at any
shared vertices. Thus mixed connected-energy coefficients vanish on an
edge-disconnected set. Subtracting proper subcluster energies gives the
following linked sixth-order weights:

| Support | Weight |
|---|---:|
| One plaquette | `-289/77760` |
| Adjacent pair, with all sixth-order powers on that support | `22285/23654592` |
| Distinct path of three plaquettes | `-4909/118272960` |
| Three plaquettes sharing an edge | `244/4312035` |
| Three faces at a cube corner | `-212/542997` |
| All six faces of an elementary cube, each once | `-83/1944` |

For example, the original two-adjacent-face energy has
`e6=-767713/118272960`. Subtracting twice the one-face value gives the
pair weight. The original path/common/corner three-face e6 values are
`-183461/19712160`, `-5281/638820`, and `-2555051/293218380` respectively.
Subtracting the three one-face values and the actual number of adjacent
pair weights gives the table. These are rational identities, executed both
from E3 and from the independently constructed polynomial states.

The last row needs an explicit additional calculation. Let Z_e multiply
one original link by -I. It commutes with K and preserves Haar. The operator

\[
 \Pi_{\mathrm{even}}=\prod_e(I+Z_e)/2
\tag{E7}
\]
projects the original polynomial source onto the edge-even subspace. A
monomial in face couplings can contribute to the scalar energy only if its
set of odd-multiplicity faces is a mod-two closed cubical surface. For total
order six, either every face has even multiplicity (supports of at most
three faces), or the six distinct faces form an elementary cube surface.

For completeness, every finite cubical two-cycle in this open cubic box
bounds a finite mod-two set of cubes. This can be constructed by assigning
cube membership from the exterior along one coordinate: the cycle condition
ensures the assignments obtained from the other faces agree. For a nonempty
cube set, each occupied coordinate line has two boundary faces. Two distinct
cubes give at least five occupied two-dimensional projection cells in the
three directions, hence at least ten boundary faces. A boundary with at most
six faces therefore comes from exactly one cube. This proves the stated
exhaustion at order six.

### Exact cube calculation

Orient the six original face words outward. Complete face reversal leaves
an SU(2) fundamental trace unchanged. Each of the twelve original edges is
then traversed once in each direction. The identity
`int U_ab conjugate(U_cd)dU=delta_ac delta_bd/2` supplies one factor 1/2
per edge. The remaining trace-index identifications have eight independent
vertex-color loops, each of dimension two. Consequently

\[
 \left\langle\prod_{p\in\partial c}W_p\right\rangle_H
 =2^8/2^{12}=1/16.
\tag{E8}
\]
The coordinate union-find audit retains all twelve edge gluings and verifies
the eight color classes.

For an order of the six distinct face insertions, let A_k be its first k
faces. Every edge internal to A_k has both its insertions already present.
Any nontrivial spin on that edge is killed by final Haar expectation,
because no later face contains it. Its singlet projector commutes with the
remaining insertions and the Casimir. Each boundary edge carries its
original spin 1/2, so the retained intermediate energy is
`(3/4)|partial A_k|`. No proper A_k is a closed surface, so no intermediate
vacuum subtraction occurs. Therefore the full linked coefficient is

\[
 -\frac1{16}\sum_{\pi\in S_6}
   \prod_{k=1}^{5}\frac4{3|\partial A_k(\pi)|}
 =-\frac1{16}\frac{166}{243}
 =\boxed{-83/1944}.
\tag{E9}
\]
All 720 original orders and their five boundary counts are in
`results/cube_sixth_paths.json`.

There is also an independent three-plus-three calculation. Of the twenty
three-face cube subsets, twelve are paths and eight are corners. Their
all-internal-singlet u3 coefficients are 11/162 and 8/81, with boundary
energies 6 and 9/2. The cross pairing with the complementary triple is E8.
Thus the contribution to E3 is

\[
 -\frac1{16}\left[12\cdot6(11/162)^2
                   +8\cdot(9/2)(8/81)^2\right]=-83/1944.
\tag{E10}
\]
The cube term is a required original three-dimensional contribution. It
cannot be assigned a planar value by deleting the extra faces.

## 4. The complete finite-box coefficient

Let M count original plaquettes, J adjacent pairs, P3 three-face paths,
T_e common-edge triples, T_v cube-corner triples, and C cubes. The result is

\[
 \boxed{\begin{aligned}
 e_6={}&-\frac{289}{77760}M
 +\frac{22285}{23654592}J
 -\frac{4909}{118272960}P_3\\
 &+\frac{244}{4312035}T_e
 -\frac{212}{542997}T_v
 -\frac{83}{1944}C.
 \end{aligned}}
\tag{E11}
\]
This formula can also be verified before linked subtraction. The full
`||u2||^2` is
`M/576+(choose(M,2)-J)/81+J*(1648/123201)`.
The full `<u3,Ku3>` has: `3 sum_p a_p^2+M/8640`; the repeated contributions
`[M(M-1)-2J]*(11/5184)+2J*(110453/47309184)`; the distinct-triple table
in section2; and the positive norm cross term `(83/1944)C`.
Inserting these into E3 cancels every disconnected term and gives E11.

For `m=2L>=4`, the original open-box counts are

\[
 \begin{gathered}
 M=3m^2(m+1),\quad J=6m(3m^2-1),\quad C=m^3,\\
 T_e=12m^2(m-1),\quad T_v=8m^3,\\
 P_3=138m^3-126m^2-24m+12.
 \end{gathered}
\tag{E12}
\]
Here `T_e=sum_e choose(r_e,3)` for the original incidence r_e; each cube
has eight different corner triples. For paths, count the wedges centered
at an original face, then subtract three per adjacency triangle:
`P3=sum_p choose(d_p,2)-3(T_e+T_v)`.
In one orientation, faces in each boundary coordinate plane have degrees
`8-b_x-b_y`, and those in an interior plane have `12-b_x-b_y`, where
`b_x,b_y` indicate whether the face interval touches its corresponding
boundary. The numbers for `b_x+b_y=0,1,2` are `(m-2)^2,4(m-2),4`.
There are two boundary and m-1 interior planes and three orientations.
Their exact sum is `198m^3-162m^2-24m+12`, giving E12. The executable also
enumerates all original faces and triples directly for L=2,3,4.

Substitution yields the closed finite-box coefficient

\[
 \boxed{e_6=
 -\frac{211396463m^3+30959193m^2+21845782m+2336684}
        {4691494080}.}
\tag{E13}
\]
In particular, at L=2,

\[
 \boxed{\frac{E_0}{\kappa}
 =480\xi-80\xi^2+\frac{1198}{351}\xi^4
 -\frac{3528610133}{1172873520}\xi^6+R_8(\xi).}
\tag{E14}
\]
The limit of this exact coefficient divided by M is
`-211396463/14074482240`. This is a limit of a finite-order coefficient;
no interchange with an infinite-volume perturbative sum is asserted.

## 5. An independently proved finite-volume remainder

The original physical free Casimir has lowest nonconstant eigenvalue 3.
A physical nonconstant spin support has no degree-one active vertex;
a finite graph of minimum active degree two contains a cycle, and the
original cubic graph has no cycle shorter than four. Each active spin has
Casimir at least 3/4. Four spin-one-half edges around one original face
attain 3. This proves the free value used here.

On the physical space, `||S||<=2M`. On the contour `|z|=3/2`, the free
resolvent `(K-z)^-1` has norm at most 2/3. Set

\[
 R=\frac3{8M}.
\tag{E15}
\]
For `|xi|<=R`, the bounded perturbation `-xi S` has norm at most 3/4.
The contour resolvent Neumann series is thus bounded by a ratio at most
1/2, and its isolated spectral projection has the same rank one as at zero.
This gives an analytic ground branch e(xi). The elementary resolvent
inclusion `dist(z,spec K)>||xi S|| => z in resolvent(K-xi S)` puts its
single enclosed eigenvalue in `|e(xi)|<=3/4`; the other free eigenvalues
are at least 3 away from zero. On the real interval this branch is the
original ground energy after subtracting the explicit scalar 2Mxi.

Cauchy's estimate on the displayed radius and the exact parity in E1 give

\[
 \boxed{|R_8(\xi)|\le\frac34
 \frac{(|\xi|/R)^8}{1-(|\xi|/R)^2},\qquad |\xi|<R.}
\tag{E16}
\]
The physical remainder is kappa times E16. For L=2, `R=1/640`.
This complete remainder is volume dependent. It uses no unverified
uniform logarithmic-source bound and does not extend an earlier coupling
threshold or prove a continuum mass gap.

## 6. Primary-literature check with explicit conventions

For one original plaquette, K acts on class functions of
`Omega=cos(theta)I-i sin(theta)n.sigma` as
`-(partial_theta^2+2cot(theta)partial_theta)`.
Put `u(theta)=sin(theta)f(theta)` and `theta=2z`. The equation for
`K-xi W` becomes the Mathieu equation with
`a=4(e+1)` and `q=-4xi`, with zero boundary values at z=0,pi/2.
Thus the original ground branch is

\[
 e_{\mathrm{one}}(\xi)=\tfrac14b_2(-4\xi)-1.
\tag{E17}
\]
NIST DLMF 28.6.5 gives
`b2(q)=4-q^2/12+5q^4/13824-289q^6/79626240+...`.
The exact return in E17 is

\[
 e_{\mathrm{one}}=-\xi^2/3+5\xi^4/216
                         -289\xi^6/77760+\cdots,
\]
matching the independent original character recurrence and the single-face
row above. A modern original-source treatment of the single-plaquette
Mathieu spectrum is Jakobs et al., EPJC85 (2025)1418, equation39; its
Hamiltonian convention must be transported before numerical comparison.
This literature check verifies the one-plaquette convention and coefficient.
It does not claim that the full cubic-box E13 or the catalogue is new to
the literature, nor supply an independent review of those results.

Sources: https://dlmf.nist.gov/28.6.E5 ;
https://link.springer.com/article/10.1140/epjc/s10052-025-15120-x .
For the established exponential-vacuum and linked-source framework see
Schütte, Zheng Weihong and Hamer, arXiv:hep-lat/9603026, section3.


# Explicit signed tangent certificate

This accompanies Q16 in `FOURTH_ORDER_SOURCE.md`. The source convention is the
same original family of independent plaquette couplings, with `lambda_p=xi`
only after the exact coefficients and their directional responses are retained.

The main coefficient producer solves the original eigenvector coefficient
equation and then computes `Q_H log u`. The independent program
`checks/verify_signed_tangent.py` instead solves the logarithmic-source equation
directly on every coefficient downset:

    K v_nu = Q_H sum_(0<mu<nu) Gamma(v_mu,v_(nu-mu)),
    K v_(e_p)=W_p.

Its returned order-four coefficient equals the entire stored catalogue polynomial
for each of the 78 classes. The same polynomial ring, original link vector
fields, and exact inverse residual are specified in Q5–Q13. The two coefficient
constructions are distinct recurrences on those fixed objects.

For the original face p and each retained source multiindex rho of total degree
at most three, define

    Z_(p,rho)=(rho_p+1) v_(rho+e_p).

The program evaluates the complete signed residual

    K Z_(p,rho) - 2 Q_H sum_(0<mu<=rho)
                  Gamma(v_mu,Z_(p,rho-mu))

and proves it is the zero quotient polynomial for positive degree rho. At
rho=0 its value is exactly the original W_p. This is a finite formal-parameter
coefficient identity, with every sign and multiplicity retained. It follows
analytically by differentiating the logarithmic-source equation; the checker
also executes all coefficient products explicitly.

The full receipt `results/signed_tangent.json` contains:

* 78 independent reconstructed logarithmic sources;
* 2,156 exactly zero polynomial tangent residuals;
* 282 explicitly expanded degree-three response polynomials, with the original
  differentiated face, remaining coupling multiindex, support multiset and chord
  coordinates for every one.

The original symmetry transports in `anchored_quartic_transports.json` return
these representative polynomials to any original four-face cluster. The
source-prefactor is the actual integer occurrence of that differentiated face;
there is no extra factorial or loss of its original union label.

These are the signed finite coefficients through degree three in the derivative
of the vacuum source. No new bound on the norm of an infinite linearized inverse,
uniform gap or continuum limit is inferred from this finite coefficient data.
