---
title: Heat correlations and the full physical complement in SU(2) lattice Yang-Mills theory
subtitle: Fourth-order coefficients, volume-independent bounds, and original state and energy metrics
author: KokunoYumeto
date: 21 September 2026
---

# Reading the heat and volume results

The basic question of this edition is concrete. A plaquette observable probes a small square of a lattice gauge field. How does its correlation with another plaquette decay under the interacting heat flow? Can one control the error in a fourth-order calculation without that error growing with the size of the lattice? Finally, when states built from those observables are allowed to mix with every other physical state, how much can their energy change?

The five manuscripts collected here answer these questions on an explicitly specified strong-coupling domain. They give the complete fourth-order heat coefficients, a bound on their all-order error that is independent of spatial volume, and quantitative control of the entire complementary physical space. The volume-independent estimates also construct an infinite spatial lattice at **fixed lattice spacing**. They do not establish a four-dimensional continuum Yang-Mills field or its continuum mass gap.

This introduction states the objects and results and explains how the proofs fit together. Appendices A-E reproduce all five supplied proof texts, including their original equation labels, parameter restrictions, and source citations. The exact coefficient tables, proofs, replay scripts and historical records are in the [public workbench](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/tree/main/yang-mills/consolidation/20260921). This is a readable companion to those records, not a replacement for the complete calculation.

## The original lattice and its physical Hilbert space

Let $L\geq2$ be an integer. The vertices are $\{-L,\ldots,L\}^3$; all contained positive nearest-neighbour links and elementary plaquettes are retained. A link carries a matrix $U_e\in\mathrm{SU}(2)$. The Hilbert space is the subspace of the product-Haar $L^2$ space invariant under gauge transformations at every vertex, including the boundary vertices. Its inner product is conjugate-linear in the first entry.

For $p=(n;i,j)$, $i<j$, the plaquette observable is the fundamental trace

$$
W_p=\operatorname{tr}\!\left(U_i(n)U_j(n+e_i)
U_i(n+e_j)^{-1}U_j(n)^{-1}\right).
$$

With $T_\alpha=-i\sigma_\alpha/2$ and the corresponding original link derivatives $X_{e,\alpha}$, set

$$
K_L=-\sum_{e,\alpha}X_{e,\alpha}^2,\qquad
H_L=\kappa K_L+\kappa\xi\sum_{p\in\mathsf P_L}(2-W_p),
\qquad \kappa=\frac{2g^2}{a},\quad \xi=\frac1{4g^4}.
$$

Here $a>0$ is lattice spacing and $g>0$ is coupling. The operator and form domains are the physical parts of $H^2$ and $H^1$ on the finite product of link groups. The smooth positive unit ground vector is $\psi_L$, its energy is $E_{0,L}$, and

$$
A_L=H_L-E_{0,L},\qquad \rho_L=\psi_L^2,\qquad
r_p=(W_p-\langle W_p\rangle_{\rho_L})\psi_L.
$$

Thus $r_p$ is centered in the *interacting* vacuum, not just in Haar measure. On the centered physical space $\mathcal H_{0,L}=\psi_L^\perp$, the connected heat correlation is

$$
\widehat C_{L,pq}(\tau;\xi)
=\langle r_p,e^{-\tau A_L/\kappa}r_q\rangle,
\qquad \tau=\kappa t.
$$

The physical time is $t$; $\tau$ is its stated dimensionless coordinate. The number of plaquettes is $M_L=3(2L)^2(2L+1)$, so $M_2=240$.

## What the fourth-order calculation contains

The link-center symmetry makes the two-mark correlation even in the homogeneous source $\xi$. The calculation therefore has the form

$$
\widehat C_L(\tau;\xi)
=C_{0,L}(\tau)+\xi^2C_{2,L}(\tau)+\xi^4C_{4,L}(\tau)
+\mathcal R_{6,L}(\tau;\xi).
$$

Appendix A, H2-H4, computes the coefficients from the actual ground-state and resolvent recurrences. The ground-energy shift, division by the original vacuum norm, and subtraction of the ground pole are included. Each connected Laplace coefficient is a finite partial-fraction sum

$$
F_\nu(z)=\sum_{c>0,\,m\geq1}\frac{a_{c,m}}{(z+c)^m},
\qquad
C_\nu(\tau)=\sum_{c,m}
\frac{a_{c,m}}{(m-1)!}\tau^{m-1}e^{-c\tau}.
$$

There are 84 exact time functions across 17 geometric cases. Their **Laplace transforms** are rational functions; the time functions are finite polynomial-exponential sums. The phrase "rational time functions" in the preserved source should be read with that distinction. On the $L=2$ box the resulting coefficient matrices have respectively 240, 2,496 and 9,660 nonzero entries at degrees zero, two and four. Their time integrals return the earlier static response matrices.

The finite first excitation band is a related, but separate, result. If $Y_\xi$ is the actual projected plaquette frame, its state Gram $G_{\rm band}=Y_\xi^*Y_\xi$ need not be the identity. Appendix A, H8, gives

$$
A_{\rm band}=3I+\xi^2T_2+\xi^4T_4+\cdots,
\qquad T_2=\frac7{15}I-\frac{D_{\rm degree}+A_{\rm adj}}{21},
$$

$$
T_4-T_4^*=T_2G_{{\rm band},2}-G_{{\rm band},2}T_2.
$$

This last identity explains why an ordinary coordinate adjoint is not the adjoint in the computed band metric. On the open $L=2$ box its right-hand side has 1,440 nonzero entries. The band remainder is proved only for $|\xi|<1/(32M_L)$; the later volume-independent *heat* result does not silently enlarge that band domain.

## From a finite-box estimate to a volume-independent heat bound

Appendix B first proves an entrywise analytic bound on $|\xi|<1/M_L$. This controls a fixed box, but its source radius shrinks as the box grows. Appendix D addresses exactly that dependence. The proof uses a locally labelled Fourier-coefficient norm to construct the exponential source, while keeping the original Haar pairing and all scalar energy terms.

The essential estimates are as follows. The physical representation labels satisfy $c_j\geq6j_e$ at each active link and $c_j\geq3$ away from the constant block. The original plaquette coefficient has trace norm $8$. These facts give a convergent labelled source series on

$$
R_0=\frac3{256},\qquad
\chi(r)=\frac{1-\sqrt{1-256r/3}}2,\qquad
d(r)=3(1-\chi(r)).
$$

The scalar mean is solved together with the nonconstant equation. A closed generator on a stated dense coefficient domain then gives the actual heat flow, rather than replacing a semigroup estimate by an estimate on one inverse. The Poisson identity pairs that flow against an arbitrary signed sum of plaquettes. Taking the supremum over the signs controls an entire matrix row.

For $\|B\|_{\rm row}=\max_p\sum_q|B_{pq}|$, the result is

$$
\boxed{\displaystyle
\|\mathcal R_{6,L}(\tau;\xi)\|_{\rm row}
\leq512e^{-3\tau/2}\frac{\theta^6}{1-\theta^2},
\qquad \theta=\frac{|\xi|}{R_0}<1.}
$$

It holds for every $L\geq2$ and $\tau\geq0$ with the same constants (Appendix D, U29-U30). A second bound, U29b, has the smaller radius $R_1=45/4096$, prefactor $6184/25$, and decay $15/8$. Both bounds are retained with their own radii; the better of their scalar error bounds may be used where both apply.

Local Taylor coefficients agree once their original support fits inside both boxes. Combined with the complete analytic tail, this gives full-sequence convergence of local vacuum means and heat correlations. U9 constructs the limiting gauge-invariant state and symmetric Markov semigroup, with a self-adjoint generator on its physical $L^2$ space. This passage increases spatial volume with $a$ fixed. It is not an ultraviolet limit $a\to0$.

## The three Grams and why the complement matters

Let $R:\mathbb C^{M_L}\to\mathcal H_{0,L}$ be the column map $Rc=\sum_pc_pr_p$, and define its inverse-energy family

$$
\Phi=\kappa A_L^{-1}R,\qquad A_L\Phi=\kappa R.
$$

The three original Grams measure different things:

$$
G_0=R^*R,\qquad G_1=R^*\Phi,\qquad
G_2=\Phi^*\Phi,\qquad E=\Phi^*A_L\Phi=\kappa G_1.
$$

Here $G_0$ is the norm of the forcing columns, $G_2$ is the norm of the inverse-energy states, and $E$ is their energy form. More generally, $G_k=\kappa^kR^*A_L^{-k}R$ for $k\geq1$. The heat integral computes all these inverse-energy moments:

$$
G_k=\frac1{(k-1)!}\int_0^\infty
\tau^{k-1}\widehat C_L(\tau;\xi)\,d\tau\quad(k\geq1).
$$

At $g^2\geq16$, Appendix E, M10, obtains, uniformly over $L\geq2$ and $a>0$,

$$
\|G_0-I\|<\frac{124}{10^6},\qquad
\|G_1-I/3\|<\frac{66}{10^6},\qquad
\|G_2-I/9\|<\frac{36}{10^6}.
$$

The coefficient bound is valid at boundary rows because absolute values are summed *before* contributions from distinct supports can cancel. The full-space estimate is $A_L\geq(117/40)\kappa I$ on $\mathcal H_{0,L}$.

These facts alone would not justify pretending that $\operatorname{im}\Phi$ is a reducing subspace. Its coupling to the rest of the Hilbert space must be retained. Define

$$
P=\Phi G_2^{-1}\Phi^*,\qquad Q=I-P,\qquad B=QR.
$$

Then $P$ is the actual orthogonal state projection and

$$
B^*B=G_0-G_1G_2^{-1}G_1.
$$

For every form-domain vector written as $\Phi c+h$, $h\in Q\mathcal H_{0,L}$, the full energy is

$$
q_{A_L}(\Phi c+h)
=c^*Ec+2\kappa\operatorname{Re}\langle Bc,h\rangle+q_{A_L}(h).
$$

Appendix E, M5, proves that the complementary operator $D_Q=QA_LQ$ on $\operatorname{Dom}(A_L)\cap Q\mathcal H_{0,L}$ is self-adjoint and bounded below. Minimization over its entire form domain therefore gives

$$
h_{\min}(c)=-\kappa D_Q^{-1}Bc,\qquad
E_{\rm full}=E-\kappa^2B^*D_Q^{-1}B,
$$

$$
G_{\rm restored}=G_2+\kappa^2B^*D_Q^{-2}B.
$$

At $g^2\geq16$ the sharpened bounds are

$$
\frac{999}{1000}E\prec E_{\rm full}\preceq E,
\qquad
G_2\preceq G_{\rm restored}\prec\frac{1001}{1000}G_2.
$$

Thus the original family's energy decreases by less than one part in a thousand when the entire complement is allowed to relax, while its state Gram increases by less than one part in a thousand. The inequalities are between quadratic forms in the same original coefficients; a strict inequality is evaluated on nonzero coefficients. They are not quotients of matrix entries. M8 carries the bounded maps and estimates to $\ell^2$ of the infinite plaquette family, including its full physical complement.

## Two concrete consequences

First, take opposite faces $p=(0,0,0;0,1)$ and $q=(0,0,1;0,1)$. Their degree-zero and degree-two correlations vanish; the degree-four term consists of four original three-face paths and one cube. At $\xi=10^{-10}$, so that $g^2=50000$ and $\kappa=100000/a$, Appendix E, M26, gives

$$
\frac{85910}{10^7}
<\frac{C_{pq}(1/\kappa;\xi)}{\xi^4}
<\frac{85920}{10^7}.
$$

The complete correlation is positive throughout $1/\kappa\leq t\leq3/\kappa$, in every $L\geq2$ and in the fixed-spacing spatial limit. The all-order remainder is smaller than the explicitly proved coefficient lower bound on this interval. Positivity is therefore a statement about the actual interacting correlation, not merely its truncated expansion.

Second, finite heat time gives a controlled replacement of inverse-energy states:

$$
\Phi_T=(I-e^{-TA_L})\Phi
=\kappa\int_0^Te^{-tA_L}R\,dt,\qquad
A_L\Phi_T=\kappa R-\kappa e^{-TA_L}R.
$$

The omitted forcing is explicit. If $\varepsilon=e^{-\kappa dT}$ with the full-space lower bound $A_L\geq\kappa dI$, spectral calculus gives

$$
(1-\varepsilon)^2G_2\preceq\Phi_T^*\Phi_T\preceq G_2,
\qquad
(1-\varepsilon)^2E\preceq\Phi_T^*A_L\Phi_T\preceq E.
$$

These inequalities survive restriction and minimization over the *same coefficient fibers*. In particular, a signed sum $\mathcal L=\sum_ja_j\log\det Q_j$ of such original positive quotient forms satisfies

$$
|\mathcal L_T-\mathcal L|
\leq2\mathcal B[-\log(1-\varepsilon)],\qquad
\mathcal B=\sum_j|a_j|\operatorname{rank}Q_j.
$$

For four returns with coefficients $a_j\in\{-1,+1\}$ and ranks at most 240, so that $\mathcal B\leq960$, $g^2\geq16$ and $T=10/\kappa$ give error below $4\times10^{-10}$ in every exterior volume. For a growing observation family, M25 keeps the rank explicitly and reaches tolerance $\eta>0$ at

$$
T=\frac1{\kappa d}\log\!\left(1+\frac{2\mathcal B}{\eta}\right).
$$

## Sources, mathematical lineage, and how to verify the edition

The exponential-vacuum and character framework has a human antecedent in Schütte, Zheng Weihong and Hamer [1]. The block minimization is a Feshbach-Schur construction; [2] is a modern primary reference. Appendix D proves the needed compact-group Fourier coefficient estimates and cites Eymard [3]. Its generator argument states the domain, dissipativity and range conditions used from Lumer and Phillips [4]. These are point-of-use dependencies, not generic acknowledgments.

Two distinct contributions associated with **Levent Alpöge** enter the earlier workbench and deserve separate attribution. The $S^6$ branch starts from the claimed complex-threefold construction he circulated with AI assistance [5], also credited to him in Engel's exposition [6]. A different branch starts from his Jacobian counterexample: global noninjectivity despite a constant nonzero Jacobian. His original announcement [7] credits Akhil's question and Fable's work; Tao's later exposition is credited separately [8]. These constructions are not interchangeable. Their subsequent coordinate maps and conductor calculations belong to their respective continuations. The five heat manuscripts collected here do not directly use either originating construction as a lemma: their actual transferred inputs are the heat, Gram, quotient-minimum and inverse-power maps specified next. This distinction records the programme's mathematical origins without attributing the present heat bounds to Alpöge or claiming an unproved spectral equivalence.

The workbench's [attribution and mathematical lineage record](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/ATTRIBUTION.md) gives the primary sources and exact historical points of use.

The direct transfer used in the present proofs is the heat/Gram and minimum-fiber argument from the Riemann workbench, not a spectral identification of its arithmetic objects with Yang-Mills fields. Appendix C identifies the receiving maps explicitly. Its pinned source revision is `128aa308dd2a70ba6e073816a957d1ee6414ba2c` in [the Riemann workbench](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/128aa308dd2a70ba6e073816a957d1ee6414ba2c): HM6-HM14 and HM19-HM24 of `HEAT_TO_ORIGINAL_QUOTIENT_METRICS.tex`, HG6-HG10 of `ORIGINAL_HEAT_AND_SOURCE_ENDPOINT.tex`, and IK9-IK12 of `INVERSE_POWER_CONDUCTOR_OBSERVABILITY.tex`. The source intake records retain their full paths and blob identities. Original conductor coefficients, zeta-zero data and arithmetic constants remain attached to their source constructions.

The workbench was developed with AI assistance from ChatGPT 5.6 Sol in Ultra mode in Codex and GPT-6 Astra; the collection preserves the individual mathematical and source records. The supplied mathematical arguments are presented for scrutiny. Fresh integration checks repeated 2,425 exact volume checks with 16 false-formula controls, 879 heat checks with 21 controls, and 52 route calculations, in both ordinary and optimized Python. The cumulative manifest passed before and after these runs. These executions verify their declared finite algebra and endpoints. They are not Lean proofs, independent external peer review, or a formal verification of every infinite-dimensional analytical step.

The source texts remain complete below, so the numerical statements can be followed through their constructions rather than accepted from this introduction. The original cumulative volume archive contains 2,015 files and retains all files of the preceding heat edition, including the five earlier control documents in its history directory. A non-mutating integrity check from the extracted archive root is `python -B verify_cumulative.py`. Full producer replays should use a new disposable copy; their scripts generate files and are not read-only checks.

The mathematical advance described here is the passage from finite-box heat coefficients to a volume-independent heat error and to a quantitative full-complement return in original physical metrics. The next, different issue is extension beyond the stated strong-coupling domain. The simultaneous shrinking-spacing path discussed in the source eventually leaves that domain. Neither the existing local source certificate nor its elementary restart establishes the ultraviolet continuum limit.

## References

1. D. Schütte, Zheng Weihong and C. J. Hamer, *The Coupled Cluster Method in Hamiltonian Lattice Field Theory*, 1996, [arXiv:hep-lat/9603026](https://arxiv.org/abs/hep-lat/9603026).
2. G. Dusson, I. M. Sigal and B. Stamm, *The Feshbach-Schur map and perturbation theory*, 2021, [arXiv:2105.02058](https://arxiv.org/abs/2105.02058).
3. P. Eymard, *L'algèbre de Fourier d'un groupe localement compact*, Bulletin de la Société Mathématique de France 92 (1964), 181-236. [Original article](https://www.numdam.org/item/BSMF_1964__92__181_0/).
4. G. Lumer and R. S. Phillips, *Dissipative operators in a Banach space*, Pacific Journal of Mathematics 11 (1961), 679-698, Theorem 3.1, pp. 686-687. [Original article](https://msp.org/pjm/1961/11-2/pjm-v11-n2-p19-s.pdf).

5. Levent Alpöge, $S^6$ construction circulated with AI assistance, [original 108-page manuscript](https://alpo.ge/s6.pdf), especially p. 2, Setup, for the coordinate matrix $\Pi$.
6. Philip Engel, *Complex structures on $S^6$*, 13 September 2026, [expository manuscript](https://philip-engel.github.io/S6.pdf), abstract and Section 1.3.
7. Levent Alpöge, [original announcement of the Jacobian counterexample](https://x.com/__alpoge__/status/2079028340955197566), 20 July 2026. The announcement credits Akhil and Fable.
8. Terence Tao, *A digestion of the Jacobian conjecture counterexample*, 21 July 2026, [exposition](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/).

```{=latex}
\clearpage
\appendix
```
