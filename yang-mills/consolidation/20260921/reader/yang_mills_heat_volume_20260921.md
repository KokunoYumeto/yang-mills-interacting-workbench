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


# Original Yang–Mills heat correlations: the complete fourth-degree return

21 September 2026. This is an additive continuation of the recovered cumulative
workbench. The original open-box SU(2) operator, physical units, Haar measure,
gauge constraints and source coordinates remain. The coefficient calculation
uses the complete available fifth-source archive. The separately saved sixth-source
proofs are preserved with their recovery status; their missing catalogues are
not prerequisites for this calculation. General exponential-vacuum and character
methods retain Schütte–Zheng–Hamer (1996) as a human antecedent. The exact finite
calculations here are accompanied by analytic proofs and executable audits;
independent external analytical review and historical priority are not asserted.

## H1. The actual operator and time coordinate

For L>=2 use every vertex n in {-L,...,L}^3, every contained positive edge
(n,i), and every contained elementary face p=(n;i,j), i<j. Put

    W_p=tr(U_i(n) U_j(n+e_i) U_i(n+e_j)^(-1) U_j(n)^(-1)),
    T_alpha=-i sigma_alpha/2,
    X_e,alpha f=d/ds f(...,exp(s T_alpha)U_e,...) at s=0,
    K=-sum_(e,alpha) X_e,alpha^2,
    H(x)=kappa K+kappa sum_p x_p(2-W_p),
    kappa=2g^2/a,   x_p=xi=1/(4g^4) on the homogeneous line.       (H1)

The inner product on the original product Haar probability space is conjugate
linear in its first entry. The physical subspace is invariant under all vertex
gauge transformations, including boundary vertices. The domains are the physical
parts of H^2 and H^1. The original bounded smooth potential preserves these
domains; the compact elliptic operator has a smooth strictly positive unit
ground state psi_x with energy E0(x). These domain and vacuum facts are the
ones in the pinned original finite-box source (SOURCE_INTAKE.json, YM0).

The coefficient operator and its inverse physical return are exactly

    B_x=(H(x)-2kappa sum_p x_p I)/kappa=K-sum_p x_p W_p,
    H(x)=kappa B_x+2kappa sum_p x_p I,
    E0(x)=kappa[2sum_p x_p+e(x)].                              (H2)

Both scalar energy terms remain in the return. Let A_x=H(x)-E0(x) and
r_p=(W_p-<W_p>_rho)psi_x, rho=psi_x^2. Define

    C_pq(t;x)=<r_p,exp(-t A_x)r_q>,
    Chat_pq(tau;x)=C_pq(tau/kappa;x),
    tau=kappa t,   t=tau/kappa.                              (H3)

This is an invertible physical-time change; no link or field coordinate is
changed. The Laplace variable z below is conjugate to this stated tau:

    F_pq(z;x)=int_0^infinity exp(-z tau) Chat_pq(tau;x) dtau
             =kappa <r_p,(A_x+kappa z)^(-1)r_q>.              (H4)

All expressions are initially at real sufficiently small x and z>0. The
separate analytic proof gives their full domains and uniform time remainders.

## H2. The complete coefficient recurrence, including the ground pole

Retain the source section u=psi_x/m_x, m_x=P_H psi_x. Its inverse is
psi_x=m_x u, and its original scalar obeys m_x^2<u,u>_H=1. Thus P_H u=1
and the original norm N(x)=<u,u>_H is kept in every expectation. Expand
u(x)=sum_nu u_nu x^nu, e(x)=sum_(nu!=0)e_nu x^nu, with u_0=1,
P_H u_nu=0 for nu!=0. The exact eigen-equation gives

    e_nu=-sum_(j:nu_j>0) P_H(W_j u_(nu-e_j)),
    K u_nu=sum_j W_j u_(nu-e_j)
              +sum_(0<mu<=nu)e_mu u_(nu-mu).                 (H5)

The last term includes e_nu u_0, and its Haar scalar makes the RHS centered.
Its unique centered inverse is the original K^(-1)Q_H. The recovered coefficient
engine supplies these actual finite coefficients and all their source labels.

For a marked face q, define h_q(z;x)=(B_x-e(x)+z)^(-1)W_q u(x).
Its coefficient equation is

    (K+z)h_(q,nu)=W_q u_nu+sum_j W_j h_(q,nu-e_j)
                         +sum_(0<mu<=nu)e_mu h_(q,nu-mu).     (H6)

The source index may include repeated faces; all multiplicities remain literal
multiindex coefficients. Define

    N_nu=sum_(alpha+beta=nu)<u_alpha,u_beta>_H,
    Mp_nu=sum_(alpha+beta=nu)<u_alpha,W_p u_beta>_H,
    Hpq_nu=sum_(alpha+beta=nu)<u_alpha,W_p h_(q,beta)>_H.        (H7)

Coefficient division by N, with N_0=1, gives the original mean mu_p=Mp/N
and the uncentered resolvent Hpq/N. The complete connected answer is

    F_pq=Hpq/N-mu_p mu_q/z.                                  (H8)

The subtracted term is retained as an actual ground-state contribution. The
source shift e_mu in (H6), both norm divisions and this term are all required.
Every resulting coefficient in the catalogue has zero coefficient at each
power z^(-j), j>0. The original positive free excitation gap also proves this
cancellation analytically near (x,z)=(0,0), after the ground projection is removed.

## H3. Exact original Casimir inversion and time reconstruction

An original invariant trace monomial has a finite tensor representation on its
original edge set. For r_e occurrences on edge e, the allowed doubled spins are
r_e,r_e-2,... . At each original vertex the sum of the doubled spins is even,
and no one exceeds the sum of the others. These are the SU(2) invariant-tensor
conditions: iterated angular-momentum addition supplies every intermediate spin
in the parity-compatible interval, so zero belongs exactly on those conditions.
The resulting finite Casimir list contains all eigenvalues of that monomial.
It retains multiplicities inside every equal-eigenvalue eigenspace.

For its distinct values C, use the literal original operator projectors

    P_c=product_(d in C,d!=c)(K-dI)/(c-d),
    (K+z)^(-1)f=sum_(c in C) P_c f/(z+c).                     (H9)

The full physical operator has all spins. The finite list in (H9) is the complete
representation space reached by that Taylor coefficient and its marked word.
It does not discard a path contributing to the coefficient.

Every response coefficient is stored as exact partial fractions

    F_nu(z)=sum_(c>0,n>=1) a_(c,n)/(z+c)^n.                   (H10)

Their time functions are exactly

    Chat_nu(tau)=sum_(c,n) a_(c,n) tau^(n-1)exp(-c tau)/(n-1)!.(H11)

Indeed direct integration of each finite term gives (H10). The analytic
heat construction in the companion proof shows these are the actual Taylor
coefficients, and uniqueness of the Laplace transform identifies them.
For explicit uniqueness, weighting a vanishing transform by exp(-s0 tau)
produces a finite complex measure; x=exp(-tau) carries its integer Laplace
samples to all polynomial moments on [0,1]. Polynomial approximation forces
the measure to vanish; continuity gives equality of the time functions.

Products in the partial-fraction engine are also exact. For a!=b, the principal
part of (z+a)^(-m)(z+b)^(-n) at -a has coefficients

    (-1)^k binom(n+k-1,k)/(b-a)^(n+k),  k=0,...,m-1,          (H12)

at power (z+a)^(-(m-k)); the analogous -b principal part is retained. Their
sum has the same two principal parts and vanishes at infinity, so the rational
functions are equal. Coincident poles add their orders. This retains every
repeated pole and hence every time-polynomial factor in (H11).

The exact original source equation (H6) is audited as a complete polynomial in
all retained tree/chord quaternion coordinates, separately for every pole.
The map is Z_e=t_s U_e t_t^(-1), with its original inverse
U_e=t_s^(-1)Z_e t_t and the tree variables retained. On each chord,
Z=x0 I-i sum x_a sigma_a and sum_(a=0)^3 x_a^2=1. The remainder basis has
x0 exponent zero or one. The map and injectivity argument are the recovered
fifth-source coordinate proof, unchanged. Every residual coefficient is zero
in this full product-of-spheres algebra, not merely at sampled links.

## H4. Complete support classification and original box assembly

A change U_e -> -U_e multiplies each source or marked trace using e by -1.
Thus a nonzero coefficient has an even total multiplicity on every original
edge, counting both marked traces. At total face multiplicity 2 or 4 this
requires all face multiplicities even. At total multiplicity 6 it permits,
in addition, the six distinct faces of one elementary cube. The original
closed cubical two-chain argument is retained in the sixth-energy proof:
a nonempty closed mod-two face set has at least six faces; at six, each of
the four edges of an extreme face requires its adjacent side face, and closure
of their remaining edges forces the opposite face. The resulting set is the
boundary of that original cube.

A disconnected face source factors over disjoint original edge factors. The
original operators, positive vacua and their means factor accordingly. A source
component containing neither mark cancels between numerator and N; marks in
different components have zero connected correlation. This remains true with
shared graph vertices: the full tensor-product Hamiltonian and the actual
invariant vectors give the same physical expectation. Connectedness therefore
means sharing original edges, exactly as in the source catalogue.

The complete list is:

| heat/source degree | total face multiplicity including marks | coordinate cases | marked responses |
|---|---|---:|---:|
| 0 | 2 | 1 | 1 |
| 2 | 4 | 3 | 7 |
| 4 | 6 | 13 | 76 |

There are 84 full rational time functions. At total degree six the cases are
one single face, two geometries of an ordered 4+2 pair, seven geometries of a
three-face path, one common-edge triple, one cube corner and one cube. All marks
and all allowed diagonal marks are retained. Faces with repeated multiplicity
are never replaced by a factorial convention.

A signed coordinate permutation and translation

    y_i=epsilon_i x_(pi(i))-d_i,
    x_(pi(i))=epsilon_i(y_i+d_i)                              (H13)

transports every actual face multiset and both marked faces to its record.
Each original edge is mapped to the corresponding forward or inverse edge.
The product-Haar map is unitary, carries K to K on that support, and maps the
actual face words to the target face word or its inverse. In SU(2), tr(U^-1)=tr(U)
by the two eigenvalues lambda,lambda^-1; hence the same trace is returned.
The inverse in (H13) returns every source to its original coordinates.

The L=2 assembly retains all 240 original faces, 1,128 adjacent pairs, 6,732
paths, 576 common-edge triples, 512 corners and 64 cubes. The coefficient
matrices have respectively 240, 2,496 and 9,660 nonzero entries. Their entire
time integrals agree entry by entry with the preceding static matrices:

    int_0^infinity Chat_0(tau)dtau=I/3,
    int_0^infinity Chat_2(tau)dtau
      =-(5/36)I+(2/1053)D_degree+(4/1053)A_adj,                (H14)

and the full original Chat_4 integral is the previously calculated R4,
including every boundary row and cube. All complete matrices and all their
coordinate transports are in generated/heat_matrix_L2.json and
heat_transports_L2.json. Those files preserve the original face ordering.

## H5. Explicit time-dependent functions

For one original plaquette with only its own source parameter, the degree-two
coefficient is

    exp(-3tau)[-241/900-(7/15)tau]+(4/225)exp(-8tau).          (H15)

For two different faces sharing one original edge, the coefficient of x_p x_q is

    exp(-3tau)[-409/17199+tau/21]
       +exp(-9tau/2)/36+exp(-13tau/2)/588.                    (H16)

Its integral is 4/1053 and its value at zero is 2/351. The corresponding
diagonal, neighbour-source term replaces -409/17199 by -13/441; its integral
is 2/1053 and its time-zero value is zero. These distinct values retain the
full source and state pairings.

Now take opposite faces

    p=(0,0,0;0,1),  q=(0,0,1;0,1).                          (H17)

Their coefficients at degrees zero and two vanish. Four original three-face
paths and one original cube contribute at degree four. One path gives

    P(tau)=exp(-3tau)[75173779/67612708800
                     -(4441/3611790)tau+tau^2/882]
       -(121/108864)exp(-9tau/2)+(1/11664)exp(-6tau)
       -(197/9988160)exp(-13tau/2)+(1/163800)exp(-8tau)
       +(1/6492304)exp(-10tau).                              (H18)

The cube gives

    B(tau)=exp(-3tau)[-235/648+(10/27)tau]
       +exp(-9tau/2)[1123/2916+(23/81)tau+tau^2/18]
       +(1/648)exp(-6tau).                                  (H19)

Thus the complete actual degree-four coefficient is

    h_4(tau)=4P(tau)+B(tau),
    h_4(0)=8869/365040,
    int_0^infinity h_4(tau)dtau=641033/29568240.               (H20)

All six decay rates and both repeated-pole orders remain. The coefficient
at tau=1 is enclosed by rational exponential bounds in generated/heat_bounds.json;
its numerical size is approximately 0.00859150755. This diagnostic decimal is
not an acceptance test. The companion proof turns (H20) into intervals for the
full actual correlation, retaining every higher Taylor order.

## H6. Independent checks on the same original geometry

The single-plaquette check uses the infinite original character basis chi_(j/2),
where K chi_(j/2)=j(j+2)chi_(j/2) and
W chi_(j/2)=chi_((j-1)/2)+chi_((j+1)/2), with the negative-index term zero.
At order n every contributing insertion path has j<=n+1; the independent
recurrence retains all these indices. It reproduces all three self-source
heat coefficients, with both original norm divisions and the ground pole.
Its integrated coefficients are 1/3,-5/36,289/5184. They also follow by twice
differentiating the retained one-plaquette energy coefficients. The original
radial coordinate return e_one(xi)=b_2(-4xi)/4-1 matches the NIST DLMF 28.6.5
expansion; the map and scalar energy term are in the recovered audit report.
This comparison covers that one-plaquette coefficient convention only.

There is an additional computation for every marked cube pair. Orient the six
faces outward. Original Haar integration yields 2^8/2^12=1/16. For any proper
visited face subset S, each edge already visited twice can never occur in a
later insertion. Its surviving representation is the original spin zero; each
boundary edge carries the remaining spin one-half. Therefore its original
intermediate energy is c(S)=3|boundary S|/4.

For marks p!=q, arrange the other four faces in a permutation and split the
ordered list into right-vacuum, middle-heat and left-vacuum pieces. All 24
permutations and all 15 length triples occur. Right and left vacuum prefixes
contribute 1/c(S); the middle heat state begins at {q} union right and each
middle insertion contributes 1/[z+c(S)]. The original 1/16 remains. Summing
these 360 rational functions gives exactly the cube coefficient in (H10).
All fifteen marked cube pairs were checked: 5,400 complete original insertion
records, including every intermediate boundary energy. This calculation imports
none of the trace-differentiation or Casimir-projection engine.

The time-zero covariance, its first derivative -<Gamma(W_p,W_q)>_rho,
and its second derivative <[K,W_p]u,[K,W_q]u>_H/N are also calculated separately
from the entire original density quotient at each coefficient. All 84 rational
functions reproduce these three values. The full-polynomial source audit and
these moment identities have distinct execution records.

## H7. Sources and present mathematical scope

The original operator/domain and maximal-tree maps are the pinned finite-box
workbench source. The exponential and character/Casimir antecedent is
D. Schütte, Zheng Weihong and C. J. Hamer, arXiv:hep-lat/9603026. The residue
and minimum-section comparison imported from the current Split-Zero heat
work is specified completely in RH_HEAT_TRANSFER.md, with its exact source
revision and read equations. No arithmetic period or Gamma constant is
assigned to a physical Yang–Mills matrix.

These are actual finite-regulator heat coefficients and actual finite-volume
analytic bounds. The Cauchy radius in the companion is 1/M. It therefore
retains dependence on the original volume, and does not supply an ultraviolet
continuum construction. The earlier uniform-gap manuscripts retain their
recorded independent-audit qualification.

## H8. The complete fourth-order first-band return in its original metric

The original free energy-three space is exactly span{Wp}. To see the next
separation, an active invariant graph with four edges is a four-cycle; its
vertex intertwiners force equal edge spins, giving energy 4j(j+1)=3,8,... .
A simple bipartite active graph with five edges and minimum degree at least two
would have one cyclic component with five vertices and five edges, hence an
odd five-cycle, or at most four vertices, where bipartiteness permits at most
four edges. Both cases contradict its assumptions. Therefore any other active
assignment has at least six edges and energy >=9/2. Thus

    spec(K_phys) subset {0,3} union [9/2,infinity),
    P3H_phys=span{Wp},   dim P3=M.                           (H21)

For sufficiently small real xi let Pi_xi be the complete spectral projection
near energy 3 of B_xi-e(xi), and put

    Y_xi c=Pi_xi sum_p c_p r_p,
    Gband=Y_xi*Y_xi,
    (B_xi-e)Y_xi=Y_xi Aband.                                (H22)

The exact quantitative construction below proves invertibility of this frame
onto the actual band. At xi=0, c->sum c_p Wp is the original Haar isometry R0.
Projection of the heat resolvent onto its original energy-three poles gives

    Cband(tau)=Gband exp(-tau Aband),
    Gband=I+xi^2 G2+xi^4 G4+...,
    Aband=3I+xi^2 T2+xi^4 T4+....                            (H23)

The original center symmetry makes both matrices even. For each of the full
heat matrices let A_(n,j) be the coefficient of (z+3)^(-j). Then literal
multiplication of the two series in (H23) proves

    G2=A_(2,1),  G4=A_(4,1),  T2=-A_(2,2),
    A_(4,3)=T2^2,
    T4=-A_(4,2)-G2 T2.                                    (H24)

All matrix factors retain their order. The complete L=2 calculation gives

    T2=(7/15)I-(D_degree+A_adj)/21.                          (H25)

It gives all 9,660 nonzero entries of T4 and all 9,660 entries of G4 in
first_band_L2.json. Every entry of A_(4,3)=T2^2 is checked. Original
self-adjointness returns through the full Gram as

    Gband Aband=Aband* Gband,
    T4-T4* = T2 G2-G2 T2.                                  (H26)

The right side has 1,440 nonzero entries for this open box. For the original
faces (-2,-2,-2;0,1) and (-2,-1,-2;0,1), the displayed difference is exactly
2/7371. This is the explicit correction between the coordinate adjoint and the
original metric adjoint. Its value is retained, rather than forcing a symmetric
coefficient matrix by dropping the mixed product.

Here is a complete analytic remainder for (H23). Work on the complex
homogeneous circle |zeta|=1/(32M). The original ground/complement calculation
in A1--A2 applies with ||W||^2=eta=1/(1024M) and Re D>=47/16. On |e|=eta,
||Z(D-e)^(-1)W||<eta, so the same scalar argument principle gives |e|<=eta.
Consequently

    ||B_zeta-e-K|| <=1/16+1/(1024M)<1/15.                    (H27)

On the spectral circle |lambda-3|=1/2 the original free resolvent has norm
at most 2. Its norm-convergent resolvent series gives

    ||Pi-P3|| <=2/13,
    ||(B_zeta-e-3)Pi||<=1/13.                               (H28)

For the first inequality, integrate the difference of resolvents: the bound
is 2b/(1-2b) with b<=1/15. For the second, integrate that difference multiplied
by lambda-3, obtaining b/(1-2b). The corresponding free integral is zero
because (K-3)P3=0. The circle encloses exactly the original M-dimensional
band, by the same resolvent homotopy and finite rank at zero.

Use the exact Haar section u=1+w, where ||w||<=1/(92sqrt(M)); the denominator
in its block inverse exceeds 23/8. The column map Fu:c->sum c_p Wp u satisfies

    ||Fu-R0||<=2sqrt(M)||w||<=1/46.

Define Yhat=Pi Fu. Its original coefficient map obeys

    ||R0*Yhat-I||<=107/598,
    ||(R0*Yhat)^(-1)||<=598/491.                             (H29)

Indeed the two contributions are Pi-P3 and Pi(Fu-R0), bounded by 2/13 and
(15/13)/46. Its inverse on the band is (R0*Yhat)^(-1)R0*. The actual unit-vacuum
frame is Y=m Yhat, with psi=m u and m^2<u,u>_H=1 retained. Its scalar cancels
from the operator intertwining, not from Gband. Thus

    Aband=(R0*Yhat)^(-1)R0*(B_zeta-e)Yhat,
    ||Aband-3I|| <=(598/491)(1/13)(47/46)=47/491.             (H30)

All these maps are analytic on a neighborhood of the closed source circle.
The original center involution sends Yhat_-zeta=-C Yhat_zeta and R0*C=-R0*,
so Aband is even. Cauchy's formula and the full even tail prove

    ||Aband-3I-xi^2T2-xi^4T4||
      <=(47/491)(32M|xi|)^6/[1-(32M|xi|)^2],
                         |xi|<1/(32M).                    (H31)

Multiplication by kappa returns this to physical energy. This is an actual
finite-volume matrix remainder, with all original band coordinates, the
nonidentity Gram (H23), and the dependence on M retained. No diagonalization
of T4 or uniform-in-volume fourth-order spectral claim is inferred here.


# Full-time heat bounds and the original plaquette response metrics

21 September 2026. This proof uses the unchanged finite-box SU(2) Hamiltonian
and the complete coefficients in PHYSICAL_HEAT_COEFFICIENTS.md. Its analytic
argument is finite-volume and independent of the inherited volume-uniform
source-norm estimates. The original number M of plaquettes appears in every
Cauchy radius. Written arguments and executed finite checks have separate
records. All inner products are conjugate-linear in the first entry.

## A1. Original free spectrum and Haar blocks

Use H1--H3 of the coefficient proof. The original physical free operator K has
its constant eigenvector 1, and every other physical Fourier block has energy
at least 3. Here is the graph argument. In a nonzero invariant representation
assignment, a vertex incident to only one active edge has no invariant tensor.
Thus the finite active graph has minimum degree at least two and contains a
cycle. The original simple cubic graph has no triangles and every cycle has at
least four edges. Each active edge has spin j>=1/2 and Casimir j(j+1)>=3/4.
Hence the complete physical K on the orthogonal complement of 1 is >=3.
The elementary plaquette trace has four spin-one-half edges and energy 3.

Write P0=|1><1| and Q0=I-P0 in the original product Haar space. Integrating
one original link gives P0 Wp=0. Two distinct elementary plaquettes have an
edge occurring in just one of their two words; integration over that link
vanishes. For p=q, the product holonomy has the original Haar law and the
fundamental character has squared norm one. Therefore

    <Wp,Wq>_H=delta_pq.                                      (A1)

For the complex homogeneous coefficient zeta, x_p=zeta, put B_zeta=K-zeta S.
This complex variable retains the physical return H= kappa B_xi+2kappa M xi I
at real xi. On C1 plus Q0 H_phys the full original block operator is

    B_zeta = [[0,Z],[W,D]],
    D=Q0(K-zeta S)Q0 on Dom(K) intersect Q0 H_phys,
    W=-zeta sum_p Wp,   Z=-zeta P0 S Q0.                     (A2)

Z is the original complex-linear row, with no conjugation of its parameter
in the analytic extension. Equation (A1) proves exactly

    ||W||=||Z||=sqrt(M)|zeta|.

On |zeta|<=1/M, Re<Dh,h> >= ||h||^2 since ||zeta S||<=2.
The closed operator D is a bounded perturbation of Q0KQ0 on the same domain.
For Re e<1 its inverse D-e exists with norm <=(1-Re e)^(-1): injectivity and
closed range follow from the real part inequality; the same inequality for
its adjoint gives dense range, hence surjectivity. All finite boxes here have
M=3(2L)^2(2L+1)>=240.

## A2. A complete ground/complement decomposition on the complex disk

The scalar equation for the small eigenvalue is

    f(e)=e+Z(D-e)^(-1)W=0.                                  (A3)

On |e|=2/M the second term has modulus at most 1/(M-2)<2/M. The finite scalar
argument principle, or Rouche's theorem applied to e, gives one simple zero
inside that circle, with multiplicity counted. The contour construction
makes e(zeta) analytic on a neighborhood of the closed |zeta|<=1/M disk and
|e|<=2/M. Define the actual right and left graph coordinates

    w=-(D-e)^(-1)W,
    ell=-Z(D-e)^(-1),
    P=(1,w)(1,ell)/(1+ell w).                               (A4)

They satisfy B(1,w)=e(1,w), (1,ell)B=e(1,ell), ell W=e, and
Z+ell D=e ell. Their norms obey

    ||w||,||ell|| <= sqrt(M)/(M-2),
    M/(M-2)^2 <= 240/238^2 < 1/225.

The last bound decreases with M>=240 by differentiating M/(M-2)^2.
Consequently 1+ell w is nonzero, P^2=P, and

    ||P||_trace <= (1+1/225)/(1-1/225)=113/112.               (A5)

The original complement is ker(1,ell). Its exact coordinate map and inverse are

    J:Q0H -> ker(1,ell),   Jh=(-ell h,h),
    J^(-1)=Q0 restricted to ker(1,ell).                     (A6)

On the unchanged operator domain direct multiplication gives

    (B-e)J=J Bc,   Bc=D-e-Well.                             (A7)

Every factor in the feedback Well is retained. For its real part,

    Re<Bc h,h> >= [1-2/M-1/(M-2)]||h||^2
                 >=[1-1/120-1/238]||h||^2
                 > (49/50)||h||^2.                         (A8)

Bc is again the same self-adjoint free operator plus a bounded perturbation.
The norm-convergent Duhamel series constructs its strongly continuous semigroup;
its derivative on Dom(K), followed by the real-part energy inequality (A8),
proves ||exp(-tau Bc)||<=exp(-49tau/50). Density extends this estimate to all
vectors. Holomorphy in zeta follows locally from the uniformly convergent bounded
perturbation series and the analytic coefficients in (A4).

The exact excited semigroup is therefore

    exp[-tau(B-e)](I-P)=J exp(-tau Bc)Q0(I-P).               (A9)

The bounds on the original graph maps are

    ||J||<=226/225,
    ||Q0P||<=113/1680,
    ||Q0(I-P)||<=1793/1680.                                 (A10)

For example Q0P=w(1,ell)/(1+ell w), and using ||w||<=1/15 and
sqrt(1+1/225)<=226/225 gives 113/1680. No product-space Gram is replaced.

For real xi, B_xi is the full self-adjoint physical operator less its displayed
scalar. Its lowest eigenvalue is <=0 by the original constant trial state.
Equation (A8) leaves the entire remaining spectrum positive after subtracting
e. Thus e is its actual ground eigenvalue. P is its actual orthogonal ground
projection, obtained above on the same domain. This also identifies the analytic
branch without choosing a surrogate vacuum.

## A3. The complete all-time analytic bound

Define the analytic connected heat observable by the literal trace

    Chat_pq(tau;zeta)
      =Tr[P Wp exp[-tau(B-e)](I-P)Wq].                       (A11)

At real xi this equals the original C_pq(tau/kappa;xi), with its actual
vacuum-mean subtraction. The complex trace is its holomorphic continuation;
no conjugation of zeta is inserted. Each original multiplication Wp has norm
at most 2. Equations (A5), (A9), (A10) give

    |Chat_pq(tau;zeta)|
      <=4(113/112)(226/225)(1793/1680)exp(-49tau/50)
      <5 exp(-49tau/50),    |zeta|<=1/M, tau>=0.             (A12)

The original link-center substitution U_(n,i) ->
(-1)^(sum_(j<i)n_j) U_(n,i) sends every plaquette trace to -Wp, preserves Haar,
K and all gauge spaces, and is its own inverse. It carries B_zeta to B_-zeta.
Both marked traces change sign, so (A11) is even in zeta. Cauchy's coefficient
formula on the original circle |zeta|=1/M and summation of the full even tail
now prove

    |Chat_pq(tau;xi)-C0_pq(tau)-xi^2 C2_pq(tau)-xi^4 C4_pq(tau)|
      <=5 exp(-49tau/50)(M|xi|)^6/[1-(M|xi|)^2],
                    |xi|<1/M, tau>=0.                     (A13)

All constants and all higher orders remain. The bound is uniform in positive
time, with its original volume dependence. It also justifies differentiation
in the source before Laplace integration. The finite rational functions in the
coefficient proof are therefore precisely the Taylor coefficients of (A11).
The Laplace uniqueness argument H3 returns their actual time functions.

## A4. A positive original opposite-face correlation on an entire time interval

For the two faces H17, C0=C2=0 and C4=h4=4P+B with H18--H20. Exact rational
Taylor remainder estimates enclose exp(-x) for each x in [0,50]: the even
Taylor sum of degree 240 is an upper bound, and subtracting x^241/241! is a
lower bound. Taylor's Lagrange remainder has the required negative sign and
magnitude <=x^241/241!. The code checks positive lower endpoints. This is
an interval calculation with rational endpoints, including at all cited times.

At L=2, M=240, xi=10^(-10), tau=1, evaluation of H18--H20 and (A13) gives

    85879/10^7 < Chat_pq(1;xi)/xi^4 < 85951/10^7.             (A14)

The complete rational inner endpoints are in generated/heat_bounds.json.
The physical parameters are g^2=50000, kappa=100000/a, and t=1/kappa.

The positivity on 1<=tau<=3 has a continuous proof. In the first bracket of
H18, let a=1/882, b=-4441/3611790, c=75173779/67612708800. Its quadratic
minimum is c-b^2/(4a). Exact rational comparison gives

    c-b^2/(4a) > (121/108864)/4+(197/9988160)/16.              (A15)

Since exp(-3/2)<1/4 and exp(-7/2)<1/16, the two negative exponentials in H18
are bounded by this quantity times exp(-3tau) for tau>=1. Its other terms are
positive. Thus P(tau)>0 throughout tau>=1. In H19 the first bracket is at
least 5/648 at tau=1 and increases, and both other terms are positive. Hence

    h4(tau) >= (5/648)exp(-3tau),    tau>=1.                 (A16)

For tau in [1,3], the ratio of the complete error (A13) to xi^4 times (A16)
is at most

    648 M^6 xi^2 exp(303/50)/[1-(Mxi)^2] < 0.531 < 1         (A17)

at the actual M and xi above. Consequently the full interacting-vacuum
correlation, not just its leading coefficient, is strictly positive on
1/kappa<=t<=3/kappa. Its original integrated value has all physical factors
retained by H4.

## A5. Full inverse-power metrics, including the original state norm

Let R:C^M->H_phys,0 have the original centered columns r_p. For integer k>=1,

    G^(k)=kappa^k R* A^(-k) R
         =int_0^infinity tau^(k-1) Chat(tau)d tau/(k-1)!.     (A18)

The actual finite-regulator spectral theorem and the positive centered gap
established in A2 justify the integral. Equation (A12) gives a uniform
integrable majorant for the analytic Taylor coefficients and their remainder.
For a partial fraction a/(z+c)^n, its exact contribution is

    a (k+n-2)!/[(k-1)!(n-1)! c^(k+n-1)].                    (A19)

Every original pole and multiplicity is used. Integrating (A13) proves the
entrywise bound

    |G^(k)_pq - sum_(j=0)^2 xi^(2j) G^(k)_(2j),pq|
      <=5(50/49)^k (M|xi|)^6/[1-(M|xi|)^2].                 (A20)

The physical energy response is G^(1). For the actual derivative primitive

    Phi=kappa A^(-1)R,
    A Phi=kappa R,    Phi*Phi=G^(2),
    Phi*A Phi=kappa G^(1),                                 (A21)

the original state and energy metrics remain separately specified.

All coefficients for k=1,2 on the original 240-face L=2 box are calculated
entry by entry in generated/native_inverse_metrics_L2.json. Let L_(k,j) be the
maximum absolute row sum of the exact degree-2j coefficient matrix. A real
symmetric M by M error whose entries have magnitude at most e has operator
norm at most M e: apply the row and column bounds and Cauchy--Schwarz. Therefore
(A20), with the complete off-diagonal rows, gives

    [3^(-k)-w_k]I <= G^(k) <= [3^(-k)+w_k]I,
    w_k=xi^2 L_(k,1)+xi^4 L_(k,2)
          +5M(50/49)^k(Mxi)^6/[1-(Mxi)^2].                  (A22)

For 0<xi<=1/1600, all the scalar terms on the right increase with xi, so its
endpoint evaluation bounds the whole interval. Exact rational evaluation gives

    (3/10)I_240 < G^(1) < (11/30)I_240,
    (9/100)I_240 < G^(2) < (13/100)I_240.                    (A23)

This is the original L=2 box, every a>0, and every g^2>=20. The identities use
the original coefficient pairing on C^240; the actual state Gram is the
calculated G^(2), not the identity. The complete original energy form on these
primitive columns is kappa G^(1). The tighter rational endpoints and each
original row-sum certificate are retained in generated/heat_bounds.json.

## A6. Scope and comparison with the preceding analysis

The finite-volume Cauchy circle in (A13) has radius 1/M. Equation (A23) has been
evaluated on the original L=2 family, with all 240 columns. Every dependence on
M, a, g and time is displayed. These statements establish neither a nontrivial
four-dimensional continuum field nor a uniform-in-volume positive mass bound.
They do not independently recertify the earlier uniform-source/gap argument.

The method uses classical bounded perturbation, block resolvents, the scalar
argument principle and the original spectral theorem. A relevant primary
Feshbach--Schur antecedent is Dusson--Sigal--Stamm, arXiv:2105.02058. The present
proof gives all blocks, graph inverses and finite constants on the actual
Hamiltonian instead of supplying a desired spectral gap as an input. The new
Split-Zero heat transfer to the resulting actual Grams is in RH_HEAT_TRANSFER.md.

## A7. The original forcing Gram for the same observation family

The time-zero matrix is the original forcing Gram G^(0)=R*R=Chat(0). It is
computed from exactly the same complete pole coefficients by

    G^(0)_(2j),pq=sum_(c>0) a_(c,1),                        (A24)

because higher pole orders vanish at tau=0. Equation (A13) at zero supplies its
complete entry error 5(Mxi)^6/[1-(Mxi)^2]. The identical full row-sum argument
on the actual L=2 box and 0<xi<=1/1600 proves

    (49/50)I_240 < G^(0) < (51/50)I_240.                    (A25)

No division by a chosen source norm is involved. The tighter rational
interval is retained with G^(1),G^(2) in generated/heat_bounds.json. Thus all
three original Grams R*R, Phi*A Phi/kappa and Phi*Phi are quantitatively
controlled together. Their use in the actual inverse-power observation is
proved in T7 of the source-transfer note.

## A8. The full original kinetic Gram, retaining its local zero entries

The forcing columns have original energy Gram R*A R=kappa Kobs, where

    Kobs_pq=<Gamma(Wp,Wq)>_rho=-Chat'_pq(0).                 (A26)

The ground-state form identity proves the first equality; differentiation of
the original semigroup proves the second. In the coefficient file each simple
pole contributes its energy times its coefficient and each double pole
contributes minus its coefficient. Higher poles contribute zero. This gives
all entries through degree four in native_inverse_metrics_L2.json.

Every off-diagonal entry outside the original face adjacency is zero exactly:
Gamma differentiates a common original edge. On a diagonal,
Gamma(Wp,Wp)=4-Wp^2 has absolute value at most4. On adjacent distinct faces,
their single shared-edge derivative vectors each have Euclidean length at most
one; writing the original SU(2) product as q0I-iq.sigma gives the length
sqrt(1-q0^2). Their scalar product has absolute value at most1. Each face has
at most12 original neighbours. All assertions concern the unchanged original
link derivatives, with their generator factor1/2 retained.

The complex ground projection from (A4)--(A5) therefore bounds the diagonal
expectation by4*113/112 and each adjacent expectation by113/112. Original
center symmetry makes these analytic expectations even. Cauchy's formula on
|zeta|=1/M bounds the entire row of the omitted tail by

    (113/112)*16*(M|xi|)^6/[1-(M|xi|)^2].                   (A27)

This uses the exact local support, rather than a dense-M multiplier on this
particular Gram. The exact degree-two and degree-four row sums and (A27) give,
on the original L=2 box with g^2>=20,

    (29/10)I_240 < Kobs < (31/10)I_240.                     (A28)

The sharper rational endpoints and every nonzero coefficient are retained in
the same records. This is the further original energy input used in T8 to
bound the correction between the actual state-minimum and energy-minimum
sections of the inverse-power family.


# The Split-Zero heat comparison transferred to the original Yang–Mills Grams

21 September 2026. This is a source-specific transfer, accompanied by a new
calculation of actual Yang–Mills heat correlations. The inspected Riemann
workbench revision is 128aa308dd2a70ba6e073816a957d1ee6414ba2c. The exact read
ranges and source blobs are in SOURCE_INTAKE.json. Its arithmetic quantities
remain attached to their own source; the Yang–Mills quantities below are
computed from the original Hamiltonian and its physical vacuum.

## T1. What was read and what is transferred

The complete argument used from the Riemann workbench is HM6--HM14 and
HM19--HM24 of HEAT_TO_ORIGINAL_QUOTIENT_METRICS.tex (19 September). It constructs
its original coefficient column map Rcal and a finite heat replacement
Rcal_J=Rcal-T_s Pcal. The physical arithmetic source pairing is unchanged and
T_s* T_s=s^(-1)I. From the complete original Gram, including both relation
cross blocks, HM13 proves the relative column error. Triangle inequalities
give (1-delta)^2 G <= G_J <=(1+delta)^2 G. Completing the square on the same
coefficient fibers carries these bounds through their actual restrictions and
quotient minima. HM22--HM24 retain every determinant rank and give the finite
heat depth for a prescribed return error.

HG6--HG10 of ORIGINAL_HEAT_AND_SOURCE_ENDPOINT.tex were also read. They expand
actual observation/kernel currents with both mixed products and give their
error under a relative change of the same original Gram. The fixed-divisor
subexponential estimate HG1--HG5 is retained as an inspected arithmetic result;
no value of its divisor-dependent constants is assigned to a Yang–Mills bound.

The common column-map calculation is instantiated below, on actual Yang–Mills
spaces. Its input error is supplied by the original physical semigroup rather
than by the arithmetic dilation. A source-specific map between arithmetic
zeta packets and physical gauge fields is not asserted. The explicit shared
interface and each new map are the displayed linear maps below.

## T2. The original physical heat columns and their entire forcing defect

Fix the original L=2 open box, M=240, a>0, and g^2>=20. Let A=H-E0 on the
centered physical Hilbert space H0, with its unchanged inner product. The
source columns R have entries rp=(Wp-<Wp>_rho)psi. From A23,

    Phi=kappa A^(-1)R,
    G2=Phi*Phi,   E=Phi*A Phi=kappa G1,
    (9/100)I<G2<(13/100)I,
    (3kappa/10)I<E<(11kappa/30)I.                           (T1)

All original coefficient axes p are retained. In particular Phi is injective.
The finite-regulator inverse and the original source identity A Phi=kappa R
are established in the analytic proof, not assumed as an observation metric.

The physical gap needed here has an independent short derivation. In the
original Haar space, minmax applied to B_xi=K-xi S gives its second physical
eigenvalue >=3-2Mxi. Its ground eigenvalue is <=0 by the original constant
trial vector. Therefore, for the actual centered A,

    A >=kappa(3-2Mxi)I >=(27kappa/10)I                       (T2)

because xi<=1/1600. This is a bound for this original box and coupling domain.
Every volume factor in its derivation is explicit.

For T>0 define the actual map and its convergent inverse on H0

    C_T=I-exp(-TA),
    C_T^(-1)=sum_(j>=0)exp(-jTA),
    ||C_T^(-1)|| <=[1-exp(-27kappa T/10)]^(-1).              (T3)

They commute with A on Dom(A); convergence in the graph norm follows by
commuting A through each term and applying the same geometric bound. Put

    Phi_T=C_T Phi=kappa int_0^T exp(-tA)R dt,
    E_T=Phi_T*A Phi_T,  G2_T=Phi_T*Phi_T.                   (T4)

Both state and energy errors retain their complete mixed products. Specifically,

    E_T-E =-Phi*A exp(-TA)Phi
            -Phi*exp(-TA)A Phi
            +Phi*exp(-TA)A exp(-TA)Phi,                     (T5)

with the analogous identity omitting A for G2. The two cross products are
equal here because the original A and its heat semigroup commute; their
origin in the expansion remains explicit. The source equation is

    A Phi_T=kappa R-kappa exp(-TA)R.                        (T6)

Thus the original forcing defect and its primitive are exactly
-kappa exp(-TA)R and -exp(-TA)Phi, respectively.

For epsilon=exp(-27kappa T/10), spectral calculus applied on the complete
centered physical space gives

    (1-epsilon)^2 G2 <= G2_T <= G2,
    (1-epsilon)^2 E <= E_T <= E.                            (T7)

For the energy inequality one applies C_T to A^(1/2)Phi; for the state
inequality one applies it to Phi. These are the actual column-map instances
of HM11, with a sharper one-sided upper bound supplied by the semigroup.
The norm of the omitted column is bounded relatively in its own original
state/energy pairing. All constants are independent of a after the exact
physical time T is inserted; T itself retains its factor 1/kappa.

## T3. Original support quotients and the corrected minimum

For an original face subset F, put V_F=Phi(C^F), U_F=A V_F=kappa R(C^F).
The complex is

    V_F --A--> H0 --0--> 0.                                 (T8)

Its support transition F subset G is the actual inclusion in degree zero and
identity on H0. The differential square commutes by the same original A.
For J=G\F, the transported cohomology kernel is exactly

    V_G/V_F -> ker[H0/U_F -> H0/U_G],
    [h] -> [Ah].                                           (T9)

Surjectivity follows by writing a killed class as Ah with h in V_G.
Changing h by V_F changes Ah by U_F, and conversely the injectivity of A on
H0 implies that a change by U_F has exactly a change by V_F. The inverse is
[Ah] -> [h]. The heat complexes use V_F^T=C_TV_F with the same target H0
and differential A. The actual pair (C_T,C_T) intertwines their differentials
and is invertible by (T3). It commutes with every support inclusion. Applying
the Split-Zero support reconstruction therefore retains F and its receiving
zero, together with the original killed representative and its primitive.

The energy-minimum representative of [Phi_J y] in V_G/V_F has the old-support
coordinate

    x_F=-E_FF^(-1)E_FJ y.

All blocks are taken in the fixed original face coordinates. Its exact quotient
Gram is

    Q_E(F,G)=E_JJ-E_JF E_FF^(-1)E_FJ.                       (T10)

Completing the square in x_F proves this formula and both inverse coordinate
maps to the quotient. The removed primitive Phi_F x_F remains. The state
minimum has the separately calculated formula with G2; it is not substituted
for the energy minimum.

Equation (T7) holds at every vector (x_F,y) in the same original coefficient
fiber. Taking the infimum in x_F on both sides proves

    (1-epsilon)^2 Q_E(F,G)<=Q_(E_T)(F,G)<=Q_E(F,G),           (T11)

and the state counterpart. The same proof applies successively to every finite
chain of fixed restrictions and quotient maps, retaining the same two bounds,
not multiplying an error factor at each stage. This is the actual HM19--HM21
minimum-fiber argument in the physical metric. A rank-zero quotient retains
its unique zero vector and determinant one.

To retain the surrounding physical space, put P_Phi=Phi G2^(-1)Phi*. Its
multiplication identities give P_Phi^2=P_Phi=P_Phi*. For any original form-domain
h perpendicular to im(Phi), the full energy is

    q_A(Phi c+h)=kappa c*G1 c
                +2kappa Re<Rc,h>+q_A(h).                  (T12)

This is the complete original coupling to the remaining physical functions.
No reducing-subspace property of the finite observation family is used.

## T4. A finite heat horizon for every four-return determinant

For a rank-r positive form G and its same-coordinate heat comparison satisfying
(T7), its relative eigenvalues belong to [(1-epsilon)^2,1]. The determinant
ratio is invariant under the displayed congruence with G^(-1/2), including its
inverse G^(1/2). Hence

    |log det G_T-log det G| <=2r[-log(1-epsilon)].           (T13)

The difference uses the same original frame and, for energy Grams, the same
kappa^r factor, which cancels exactly in the ratio. For any four prescribed
restriction/quotient returns with coefficients +1,+1,-1,-1 and ranks r_j<=240,

    |L_T-L| <=2 sum_j r_j [-log(1-epsilon)]
              <=1920 epsilon/(1-epsilon).                 (T14)

The final inequality follows by integrating 1/(1-x) from zero to epsilon.
Take the actual physical horizon

    T=10/kappa=5a/g^2.                                     (T15)

Then epsilon=exp(-27). The exact rational exponential enclosure gives

    epsilon<19/10^13,
    1920 epsilon/(1-epsilon)<4/10^9.                        (T16)

The calculated inner upper bound is approximately 3.608695327762*10^(-9).
The complete rational fraction is in generated/heat_bounds.json. This is one
common finite heat horizon for all four original returns and all original
support choices in this 240-column family. It requires no estimate of a newly
selected arithmetic comparison constant or observation angle.

## T5. Every signed observation current retains its mixed terms

Fix a surjection Lambda from the original C^240 onto its actual chosen
observation image; for example its rows can read a fixed subset of original
face coordinates. From the energy Gram E define

    Q=(Lambda E^(-1)Lambda*)^(-1),
    Omega=Lambda*Q Lambda,
    L=E-Omega.                                             (T17)

The minimum representative S=E^(-1)Lambda*Q satisfies Lambda S=I and
E S=Lambda*Q. Direct expansion proves that y*L y is the squared E-norm of
(1-S Lambda)y. Thus both the kernel residual and boundary Gram are the original
canonical ones, with every rectangular mixed entry preserved. Define the heat
versions using E_T and the identical Lambda.

Put eta=2epsilon-epsilon^2. Equation (T7) gives
(1-eta)E<=E_T<=E. Minimize on the identical Lambda fibers to get the same bounds
for Q. For fixed original columns a1,a2,v and omega>0 let

    K_i=a_i*L v, B_i=a_i*Omega v,
    d_i=a_i*E a_i, E_v=v*E v,
    Phi_K=2Re(conj(K1)K2)/omega,
    Phi_B=2Re(conj(B1)B2)/omega,
    Phi_cross=2Re(conj(K1)B2+conj(B1)K2)/omega.              (T18)

The same-fiber bounds and Cauchy--Schwarz give
|Delta K_i|<=2eta sqrt(d_i E_v), |Delta B_i|<=eta sqrt(d_i E_v), while each
original |K_i| and |B_i| is at most sqrt(d_i E_v). Expanding every linear and
quadratic product in (T18) proves the HG8 receiving inequalities

    |Delta Phi_K|<=2sqrt(d1 d2)E_v(4eta+4eta^2)/omega,
    |Delta Phi_B|<=2sqrt(d1 d2)E_v(2eta+eta^2)/omega,
    |Delta Phi_cross|<=2sqrt(d1 d2)E_v(6eta+4eta^2)/omega.    (T19)

These estimates contain the original phases and both cross products. The
actual source/target numerical values in this application are the calculated
Yang–Mills Grams, and their relative error is (T16). No sign of a current is
inferred from its norm alone.

## T6. Source and execution scope

This contribution reads the original HM/HG heat and metric proofs and proves
the displayed Yang–Mills instances in full. The arithmetic dilation T_s, its
Mellin variables, zeta-zero jets, original source masses and period-dependent
constants remain in the cited RH construction. Here exp(-TA) is the physical
ground-relative semigroup, with T (T15) in the original time units.

The heat coefficients, original box matrices, graph constants and rational
bounds are independently exercised by the executable tests described in
VERIFICATION.md. Their complete analytic proofs are supplied as written
arguments for review. The tests do not give a Lean proof, independently audit
every older source estimate, or establish the four-dimensional continuum gap.
The standing continuum path and the growing-volume problem still require
bounds beyond the explicitly finite M-dependent domain proved here.

## T7. The latest inverse-power observation has a concrete receiving instance

After the heat-source intake, the complete 21 September source
INVERSE_POWER_CONDUCTOR_OBSERVABILITY.tex was read at the same pinned commit.
Its IK9--IK10 construct a literal left inverse of selected original conductor
rows on their inverse-power space. IK12 returns that inverse through the
original source and observation Grams, retaining their eigenvalue factors.
IK13 explicitly permits its lower bound to tend to zero with its cutoff.
Those coefficients, root differences and guards remain in that construction.

In the present Yang–Mills family the actual inverse-power source is

    Phi=kappa A^(-1)R:C^240->H0,
    O=R*:H0->C^240,
    O Phi=G^(1).                                           (T20)

The independent computed bound (A23) makes this original response matrix
invertible, so its exact coefficient left inverse is

    W=(G^(1))^(-1) R*,
    W Phi=I_240,   ||(G^(1))^(-1)||<=10/3.                  (T21)

This is a proved inverse on these specific columns, not an assumed observation
angle. The original quotient metric for the observation O is (G^(0))^(-1):
minimizing the physical Hilbert norm over R*h=z has the representative
R(G^(0))^(-1)z. Its full residual is perpendicular to im(R), as multiplication
by R* verifies. Thus P_R=R(G^(0))^(-1)R* is the actual orthogonal projection,
and every nonzero coefficient vector c satisfies

    ||P_R Phi c||^2=c*G^(1)(G^(0))^(-1)G^(1)c,
    ||Phi c||^2=c*G^(2)c.                                  (T22)

Returning the three computed original metrics (A23),(A25) gives

    G^(1)(G^(0))^(-1)G^(1) >= (3/34)I,
    ||P_R Phi c||^2 / ||Phi c||^2 > 150/221.                 (T23)

Indeed the first coefficient is (3/10)^2/(51/50)=3/34, and dividing by the
upper state coefficient 13/100 gives 150/221. Every source metric and its
inverse has been retained. This is the IK12 left-inverse/minimum argument
applied to the original physical inverse-power family, with the needed Gram
bounds actually calculated here. It detects all 240 columns simultaneously
at L=2, every a>0 and g^2>=20. It does not supply an infinite-volume fraction or
an independence assertion for an uncomputed concatenation of higher powers.

The portion outside this observation is the exact vector
(I-P_R)Phi c. Its squared norm is

    c*[G^(2)-G^(1)(G^(0))^(-1)G^(1)]c,                       (T24)

and is positive semidefinite by the original orthogonal decomposition. No
component is removed from the energy formula (T12). The maps (T20)--(T24)
state the entire receiving construction; they make no identification of
arithmetic zeta zeros with physical spectral points.

## T8. The actual residual between the state and energy sections is bounded

Retain the original orthogonal state projection P_R from T7 and define

    h=(I-P_R)Phi,
    B0=(G^(0))^(-1)G^(1),   P_R Phi=R B0.                  (T25)

All columns of h satisfy R*h=0. Since A Phi=kappa R, the mixed energy
q_A(Phi c,h d) vanishes for every coefficient pair c,d, by the original
Hilbert adjoint identity. Thus Phi is the actual minimum-energy section
of the affine fibers R*f=G^(1)c. The state-minimum section of that same
fiber is R B0 c. They have the exact comparison

    h*Ah=kappa[G^(1)(G^(0))^(-1)Kobs(G^(0))^(-1)G^(1)-G^(1)],
    (P_R Phi)*A(P_R Phi)=Phi*A Phi+h*Ah.                    (T26)

To verify the first identity, expand the whole expression
(Phi-RB0)*A(Phi-RB0). Both cross products are kappa G^(1), while the last
term is kappa B0* Kobs B0; their signed sum is (T26). This also proves
nonnegativity of the right side. The state residual remains the matrix (T24).

The three raw bounds (A23),(A25),(A28) give the strict original energy bound

    0<=h*Ah < (1322/7203) Phi*A Phi.                        (T27)

Indeed congruence by (G^(1))^(-1/2), with its explicitly inverse square root,
puts the bracket in (T26) below

    [(31/10)(50/49)^2(11/30)-1]I = (1322/7203)I.

Returning that congruence proves (T27) in the original coefficient coordinates.
Thus the state-section correction has at most this fraction (less than0.184)
of the original primitive's energy, and (T23) retains more than150/221 of its
state norm in the actual observed force span. The difference itself remains
an element of ker(R*) with its complete state and energy Grams, rather than
being dropped. Both conclusions hold simultaneously for all240 original
columns on the specified finite box and coupling domain.

For a prescribed observation z, the two exact sections are
Phi(G^(1))^(-1)z and R(G^(0))^(-1)z, and their difference is
h(G^(1))^(-1)z. Their source-to-observation compositions are both the identity.
This supplies the explicit section-correction morphism and its quantitative
energy return in the original metric. It is the same minimum-section mechanism
read in the Split-Zero source, now with all physical Grams evaluated and the
entire correction bounded on its stated domain.


# Original Yang–Mills heat: a box-independent analytic radius and row-sum remainder

21 September 2026. This continuation addresses the two quantities left by the heat edition: its radius 1/M and the coupling of its observed states to the full physical complement. All operator coefficients, Haar masses, original link and plaquette coordinates, and state and energy pairings are retained. This note proves the local-source-to-heat argument used here in full. It does not certify every earlier stronger-coupling assertion. Its coefficient tables are the inherited, separately replayed heat tables; new constant and matrix calculations have their own records. No continuum mass-gap conclusion, historical-priority determination, or external analytical review is asserted.

## U1. Original operator, physical time, and coefficient maps

For each L>=2 take vertices {-L,...,L}^3, all contained positive nearest-neighbor links e=(n,i), and all elementary faces p=(n;i,j), i<j. Retain

    Wp=tr(U_i(n) U_j(n+e_i) U_i(n+e_j)^(-1) U_j(n)^(-1)),
    T_a=-i sigma_a/2,  X_e,a f=d/dt f(...,exp(t T_a)U_e,...)|0,
    K=-sum_(e,a) X_e,a^2,
    H(x)=kappa K+kappa sum_p x_p(2-Wp),
    kappa=2g^2/a,   x_p=xi=1/(4g^4),   a,g>0.                 (U1)

The physical Hilbert space is the invariant subspace of original product Haar probability L2(dU), with every vertex including boundary vertices averaged. H has physical H2 domain and H1 form domain, since the original potential is smooth bounded on this finite compact group. Its smooth positive unit ground vector psi and simple bottom energy E0 follow from the modulus form inequality, elliptic regularity, the maximum principle, and the identity

    q_(H-E0)(psi f)=kappa int psi^2 sum_i |X_i f|^2.         (U2)

The multiplication map f -> psi f and inverse division by psi are unitary between L2(rho dU) and original L2(dU), rho=psi^2. The time coordinates are tau=kappa t and t=tau/kappa. No field variable is rescaled.

For a product-spin label j=(j_e), define pi_j(U)=tensor_e pi_(j_e)(U_e), d_j=product_e(2j_e+1), c_j=sum_e j_e(j_e+1), and the actual coefficient

    A_j=d_j int f(U) pi_j(U)^* dU,
    f(U)=sum_j Tr(A_j pi_j(U)).                             (U3)

This Fourier map and its inverse follow from the original Haar matrix-coefficient orthogonality. The trace-coefficient norm is ||f||_X=sum_j ||A_j||_1. Let X0 be its zero-Haar physical part, and Y0 its dense domain sum_(j!=0)c_j||A_j||_1<infinity. The actual K maps Y0 bijectively onto X0 by multiplying each coefficient by c_j; its inverse divides it by that same c_j. These are auxiliary convergence estimates on the original coefficients, not replacements for (U2).

The compact-group Fourier algebra and its product norm are classical (Eymard, 1964). Here their required inequalities are proved directly. In a product of two coefficient functions, decompose pi_j tensor pi_k into its full irreducible and multiplicity spaces by a unitary intertwiner. Pinching to all its diagonal representation blocks and tracing each multiplicity space returns the exact output coefficients. Pinching is an average of unitary conjugations. For a partial trace, trace-norm duality gives |Tr[(Z tensor I)C]|<=||C||_1 when ||Z||<=1. Hence

    ||fh||_X<=||f||_X||h||_X,
    ||A(X_e,a f_j)||_1<=j_e||A_j||_1.                      (U4)

Every representation dimension and every multiplicity is included in this argument.

## U2. The graph bound that enters the source estimate

A nonzero gauge-invariant coefficient has an invariant tensor on the original incident indices at every vertex. Grouping the factors gives an intertwiner from the dual spin-j_e factor into the tensor product of the others. The maximum target weight is their summed spin, so

    j_e<=sum_(f incident v, f!=e) j_f.                      (U5)

Fix e={u,v}, and let E1 be the other edges at its endpoints. Because the graph is simple and triangle-free, their outer endpoints are distinct. Put J1=sum_(f in E1)j_f. The two endpoint inequalities give J1>=2j_e. Sum the outer-endpoint inequalities: every edge outside E1 and {e} is counted at most twice, so J1<=2J2, where J2 counts these outer edges once. Therefore sum_f j_f>=j_e+J1+J2>=4j_e. The original half-integer spectrum obeys j(j+1)>=(3/2)j, and consequently

    c_j>=6j_e on every physical block;
    sum_e j_e<=(2/3)c_j on every product block.             (U6)

In particular c_j>=3 on each nonconstant physical block. The fundamental elementary plaquette has c_j=3. This argument includes active bridges and boundary vertices; no cycle decomposition of every active edge is presumed.

## U3. Local labelled source and its exact assembly kernel

For every nonempty finite edge label S retain a zero-Haar physical coefficient family A_(S,j), with supp(j) contained in S; the label may exceed the active support. Put

    ||v||loc=sup_e sum_(S containing e,j!=0)c_j||A_(S,j)||_1. (U7)

On a finite graph this is a complete space, and its total c-weighted coefficient sum is at most |E_L| ||v||loc. Assembly sends A_(S,j) to sum_(S containing supp(j)) A_(S,j). Its kernel is exactly the family equations that all those sums vanish. For each S strictly containing supp(j), the relation with coefficient A at (S,j) and -A at (supp(j),j) has zero assembly. The actual coefficients at all enlarged S give a unique decomposition of every assembly-kernel element into these relations. Its inverse reads those same enlarged-label coefficients. This supplies the support-preserving quotient map and both inverse laws.

Define, retaining the original union label,

    B(v,h)_S=K^(-1) Q_H sum_(S1 union S2=S) Gamma(v_S1,h_S2),
    Gamma(f,h)=sum_(e,a)(X_e,a f)(X_e,a h),  Q_H=I-P_H.     (U8)

Each Haar scalar removed by Q_H is recorded separately. For an anchor in S1, (U4) and (U6) bound the output before K inversion by

    3 sum_(S1 containing anchor,j) ||A_(S1,j)||_1
        sum_e j_e sum_(S2 containing e,k) k_e||B_(S2,k)||_1
      <=(1/3)||v||loc||h||loc.

The anchor-in-S2 contribution gives the other 1/3. The original output Casimir cancels precisely against its nonzero inverse Casimir in (U8). Thus

    ||B(v,h)||loc<=(2/3)||v||loc||h||loc.                   (U9)

## U4. Exact elementary coefficient and convergent complex source

For the original four-link word, the coefficient matrix on (C2)^tensor4 has entries

    A_(i1,i2,1-i2,1-i3 ; i0,i1,1-i3,1-i0) += (-1)^(i0+i2),
    i0,i1,i2,i3 in {0,1}.                                  (U10)

The identity (U^(-1))_(r,c)=(-1)^(r+c) U_(1-c,1-r) proves its trace formula. Its four nonzero 2-by-2 blocks, up to row/column order, are [[1,-1],[-1,1]]. Direct multiplication gives (A* A)^2=4A* A and Tr(A* A)=16. Thus |A|=A* A/2 and ||Wp||_X=8. At most four original plaquettes meet an edge.

Allow independent complex x_p with max_p|x_p|<=r. The source equation is

    v=(1/3)sum_p x_p Wp+B(v,v).                            (U11)

Its homogeneous order-n coefficient obeys the original binary recurrence, giving

    a_n(r)=Cat_(n-1)(2/3)^(n-1)(32r)^n,
    sum_(n>=1) a_n(r)=r_v(r)=(3/4)(1-sqrt(1-256r/3)).       (U12)

The radius used throughout the new bound is exactly

    R0=3/256.                                              (U13)

For r<R0 the series is norm-analytic. It converges absolutely also at r=R0, where its tail is (3/4)binom(2N,N)/4^N<=3/(4sqrt(N+1)). The finite coefficient proof is Cat_N/4^N=2(b_N-b_(N+1)), b_N=binom(2N,N)/4^N. No strict contraction at the boundary is used.

Each order-n label is an edge-connected union of at most n plaquettes. The coefficients agree literally in every original box containing that union. This follows inductively from (U8): derivatives require a shared original edge, and K inversion acts on the same coefficients.

On a finite graph the norm convergence controls every first and second coordinate derivative, since j_e j_f<=c_j. Thus the actual assembled function solves

    Kv=sum_p x_pWp+Gamma(v,v)-C(x),
    C(x)=P_H Gamma(v,v).                                   (U14)

For real x, psi=exp(v)/sqrt(int exp(2v)) is positive and solves the original eigen-equation with

    E0=kappa[2sum_p x_p-C(x)].                              (U15)

Equation (U2) then proves it is the actual ground vector and fixes every scalar. Elliptic bootstrapping makes it smooth. For complex x the nonzero function exp(v) is still a smooth solution of that eigen-equation. Its squared integral is addressed below, rather than presumed nonzero.

## U5. The full drift, including its scalar row

Set D_v f=2 Gamma(v,f). Equations (U4),(U6) give, on the original coefficient spaces,

    ||D_v h||_X<=chi(r)||Kh||_X,
    chi(r)=(2/3)r_v(r)=(1-sqrt(1-256r/3))/2<=1/2.           (U16)

Both the constant and nonconstant outputs are included. Indeed the sum over generators is at most 6 sum_j ||A_j(h)||_1 sum_e j_e [r_v/6], and sum_ej_e<=(2/3)c_j. Define

    T=Q_H D_v K^(-1):X0->X0,
    p=P_H D_v K^(-1):X0->C,
    S=(I-T)^(-1)=sum_(n>=0)T^n.                            (U17)

The stacked bound is |py|+||Ty||_X<=chi||y||_X; in particular ||S||<=1/(1-chi). Define the actual mean functional by

    mu_x(F)=P_HF+p S Q_HF.                                 (U18)

For chi<=1/2, |mu_x(F)|<=||F||_X and |mu_x(Q_HF)|<=chi||Q_HF||_X/(1-chi). The associated source inverse is h=K^(-1)S Q_HF in Y0, with

    (K-D_v)h=F-mu_x(F).                                    (U19)

All maps are analytic for r<R0.

Here (U18) equals the actual complex density functional as well. Put Z_x=int exp(2v). Integration by parts gives int exp(2v)(K-D_v)h=0 for h in Y0, since its first and second derivatives converge. Equation (U19) therefore gives

    int exp(2v)F=mu_x(F) Z_x.                               (U20)

If Z_x vanished, the left side would vanish for every physical Fourier polynomial. Their uniform closure contains the conjugate of the nonzero smooth gauge-invariant exp(2v). Its squared modulus would then have zero integral, a contradiction. Hence Z_x is nonzero, and mu_x(F)=int exp(2v)F/Z_x. For real x it is precisely expectation in rho. The exact bilinear integration identity is

    mu_x((K-D_v)h . G)=mu_x(Gamma(h,G)).                    (U21)

Complex x uses the bilinear analytic continuation; the physical real-coupling Hilbert pairing retains conjugation in its first entry.

## U6. Closed generator and heat flow in the same coefficients

Let L_x=K-Q_H D_v on X0, Dom(L_x)=Y0. The graph norms of K and L_x are equivalent because ||Q_H D_vh||<=chi||Kh||, chi<1. Thus L_x is closed and densely defined. For h>0,

    I+hL_x=[I-hQ_H D_v(I+hK)^(-1)](I+hK),                 (U22)

and the square bracket is invertible by a Neumann series of norm ratio at most chi. The original sum of trace norms also gives

    ||(I+hL_x)f||_X
      >=||f||_X+h(1-chi)||Kf||_X
      >=[1+3h(1-chi)]||f||_X.                              (U23)

All powers of the actual resolvent obey the corresponding product bound. The Hille–Yosida/Lumer–Phillips generation theorem applies to this explicitly closed dense domain and the proved surjectivity (U22). It gives

    E_x(tau)=exp(-tau L_x),
    ||E_x(tau)||<=exp[-d(r)tau],  d(r)=3(1-chi(r))>=3/2.    (U24)

For completeness, the shifted operator L_x-d(r) is dissipative with the negative-generator convention: the directional norm derivative of -Kf is -||Kf||, and its perturbation is at most chi||Kf||. Its sufficiently large positive resolvent is obtained by (U22) and the resolvent identity. This proves the decay constant, rather than using a norm for one inverse as a substitute for a semigroup estimate. Lumer–Phillips (1961), Theorem3.1, pp686–687, is the primary generation reference.

Each resolvent in (U22) is analytic in x. Its exponential Euler powers are uniformly bounded on compact complex source polydisks and converge strongly to (U24). Here the latter assertion has a direct integral proof: (I+hL)^(-1)f=int_0^infinity exp(-u)E_x(hu)f du, by integration on the original generator domain and density. The m-fold product at h=tau/m is the average of E_x(tau Y_m/m)f, where Y_m has the convolution density exp(-u)u^(m-1)/(m-1)!, mean m and variance m. The nonnegative scalar density has mass one. Chebyshev's inequality outside a fixed neighborhood of tau, strong continuity inside it, and the contraction bound give the stated strong convergence. No spectral diagonalization of the perturbed coefficient generator is presumed. Applying scalar Vitali convergence to every bounded functional and then the locally bounded weak-to-strong holomorphy principle proves analytic dependence of E_x(tau). Equivalently the sectorial resolvent obtained from (U16) gives the same contour construction. This concerns source analyticity, not a holomorphic continuation of physical time across arbitrary rays.

For real x the full physical heat return is

    T_x(tau)F=E_x(tau)Q_HF+mu_x(F)-mu_x(E_x(tau)Q_HF).      (U25)

On the dense smooth domain it solves the actual equation with generator K-D_v, preserves its original mean, and agrees with the physical Hilbert semigroup by uniqueness. Its positive physical time is tau/kappa. The same formula defines the analytic continuation for complex x. In particular

    ||T_x(tau)F-mu_x(F)||_X
      <=exp[-d(r)tau]||Q_HF||_X/(1-chi).                   (U26)

Every physical eigenfunction in a finite box is smooth and belongs to Y0 after subtracting its Haar constant. This last membership follows from Plancherel and Cauchy–Schwarz with a sufficiently high original Casimir power: sum_j d_j^2(1+c_j)^(-s)<infinity for s>3|E_L|/2. Thus (U24) applied to the exact eigen-equation proves A=H-E0>=kappa d(r) on the complete centered physical Hilbert space. Compact spectral resolution gives the full form-domain statement. This is a rederivation of the elementary strong-coupling lower bound on this explicit domain, not of every stronger historical source estimate.

## U7. The row-sum estimate that removes the volume factor

For fixed original p put q_tau=E_x(tau)Wp and h_tau=K^(-1)S q_tau. The exact mean equation gives

    (K-D_v)h_tau=T_x(tau)Wp-mu_x(Wp).                      (U27)

For arbitrary complex coefficients z_q with max_q|z_q|<=1, set G_z=sum_q z_qWq. The original edge incidences and trace coefficient 8 give

    sup_e sum_(q containing e) (1/2)||z_q Wq||_X<=16.

Consequently, with every generator retained,

    ||Gamma(h,G_z)||_X
      <=3*16 sum_j sum_e j_e||A_j(h)||_1
      <=32||Kh||_X.                                       (U28)

Use (U21), ||mu_x||<=1, ||S||<=1/(1-chi), and ||Wp||_X=8. The connected analytic heat matrix satisfies

    Chat_pq(tau;x)=mu_x[(T_x(tau)Wp-mu_xWp)Wq],
    sum_q |Chat_pq(tau;x)|
      <=[256/(1-chi(r))] exp[-d(r)tau]
      <=512 exp(-3tau/2).                                  (U29)

The sum equality to a supremum over phases z_q is exact in every original finite face set. At real x this is precisely <r_p,exp(-tau A/kappa)r_q>. Its transpose symmetry extends to complex x by analyticity from the real multivariate polydisk. Thus the same bound holds for columns and for the coefficient-space operator norm. No M is introduced.


There is a useful sharper bound that uses the original Haar projection before estimating the returned mean. The physical Fourier block with spin one-half on the four edges of a specified elementary plaquette and zero on all other edges is one-dimensional: at each two-edge vertex the invariant contraction is unique, and following the original indices gives Wp. Consequently, for physical h in Y0,

    |P_H Gamma(h,G_z)| <= (1/8)||Kh||_X.

Indeed the contributing block is a_p Wp, has norm8|a_p| and Casimir3, and its Haar pairing with Wp is a_p. All other product-spin labels integrate to zero. On the nonconstant output, (U18) gives |(mu-P_H)QF|<=chi||QF||_X/(1-chi). Retaining both terms in this mean decomposition and using (U28) yields the additional full-row bound

    ||Chat(tau;x)||row
       <=[(1+255chi)/(1-chi)^2] exp[-3(1-chi)tau].        (U29a)

The original bound(U29) remains available. Take the exact original source radius and its derived constants

    R1=45/4096,  chi(R1)=3/8,
    C1=6184/25,  d1=15/8.

Then (U29a) supplies

    ||Chat-C0-xi^2 C2-xi^4 C4||row
      <=(6184/25) exp(-15tau/8)
             (|xi|/R1)^6/[1-(|xi|/R1)^2], |xi|<R1.        (U29b)

This second circle has its stated smaller radius and sharper prefactor and decay. A scalar minimum of the two error bounds is permitted; no minimum of noncommuting matrices is introduced. For the kth inverse moment its prefactor is (6184/25)(8/15)^k. These are used in the strengthened numerical return M10.

## U8. Uniform analytic remainder and all inverse-energy moments

Now restrict x_p=zeta homogeneously. The original central link map U_(n,i) -> (-1)^(sum_(j<i)n_j)U_(n,i) preserves Haar, K and every gauge constraint and sends all Wp to -Wp. Both marked traces change sign, so Chat(tau;zeta) is even. Let theta=|xi|/R0. Cauchy's formula using (U29), first at radius r<R0 and then letting r increase to R0, proves in maximum absolute row-sum norm

    ||Chat(tau;xi)-C0(tau)-xi^2 C2(tau)-xi^4 C4(tau)||row
       <=512 exp(-3tau/2) theta^6/(1-theta^2),
       |xi|<R0, tau>=0.                                    (U30)

The original coefficients C0,C2,C4 are exactly the inherited full heat tables: uniqueness of the local analytic eigen/heat equation at x=0 gives the identical recurrence and ground-pole subtraction. Their source and original time coordinates are unchanged.

For the original centered columns R and A=H-E0 put

    G0=R*R,  Gk=kappa^k R*A^(-k)R (k>=1),
    Phi=kappa A^(-1)R,  Phi*Phi=G2,  Phi*A Phi=kappa G1.

The physical spectral theorem and (U30) justify all integrals, including their complete tails:

    Gk=int_0^infinity tau^(k-1) Chat(tau)d tau/(k-1)!,
    ||Gk-sum_(j=0)^2 xi^(2j) Gk_(2j)||row
       <=512(2/3)^k theta^6/(1-theta^2), k>=1.              (U31)

For G0, (U30) at tau=0 supplies the same formula with k=0. A pole a/(z+c)^n contributes a(k+n-2)!/[(k-1)!(n-1)!c^(k+n-1)]. These maps use the original kappa in both the heat-time integral and every inverse energy.

## U9. Spatial tails and the actual volume limit

The preceding estimates also specify their spatial return. Set all couplings outside a given finite list to zero. The scalar Hilbert tensor factors on disjoint active link components factorize, as do the positive vacuum and semigroup. Their restrictions to the original invariant observables agree with that scalar calculation. A connected marked correlation therefore has zero multivariate coefficient unless its original marks and source faces lie in one edge-connected component. In particular, if the original face-adjacency distance is d(p,q), a degree-n coefficient connecting distinct marks needs n>=d(p,q)-1. Both marks retain their original links.

At degree n, the same coefficient depends only on the n-neighborhood of the union of marked links, where two links are adjacent when they share an original plaquette. This follows either from the tensor factorization or directly from (U8),(U17),(U25): every source insertion attaches its original connected plaquette union through a differentiated edge, K and its resolvent preserve link support, and all orders add to n. The constant and disconnected products are retained until the connected subtraction.

For two boxes containing the N-neighborhood of the same marks, every homogeneous coefficient through N is identical. Equation(U30)'s coefficient bound gives

    |Chat_L-Chat_L'|
       <=1024 exp(-3tau/2) theta^(2(floor(N/2)+1))/(1-theta^2). (U32)

The identical reasoning gives a row tail outside face-distance D by omitting every coefficient with n<D-1; n is even. These are explicit spatial bounds, with the physical link length a unaltered.

For clarity the limiting state and dynamics are also constructed. The coefficient mean (U18) is analytic and bounded by ||F||X, and its Taylor coefficients depend on finite original neighborhoods. Cauchy tails prove full-sequence convergence mu_L(F)->mu(F) for every cylinder Fourier polynomial on |xi|<R0. Real-coupling positivity and mass one pass from the original vacua. For an arbitrary cylinder function use the actual finite vertex Haar average P_G on its incident vertices; the equality mu_L(F)=mu_L(P_G F) extends the limiting physical functional consistently to all cylinder functions. Uniform cylinder approximation then gives its gauge-invariant probability lift on the product of original link groups. Both positivity and this gauge extension are the original finite-volume ones.

Equation(U25) has norm at most3||F||X and localized Taylor coefficients. Hence T_L(tau)F converges uniformly, first on cylinder Fourier polynomials and then on their continuous uniform completion by the real Markov contraction. The resulting T is positive, unital, strongly continuous, and preserves mu. Its semigroup and symmetry laws pass by approximating the intermediate continuous function uniformly with cylinder polynomials. Equations(U24)–(U26) prove uniqueness of its invariant probability on the gauge-invariant observable algebra: integrate the uniform mixing bound and use density. This claim concerns physical observables; it does not assign a unique gauge-variant probability from those observations alone.

The symmetric Markov semigroup has its self-adjoint generator A_infty on L2(mu)_phys. The finite real bounds pass on cylinder functions by the uniform convergence and then by L2 density, giving

    A_infty|_(1 perp)>=kappa d(|xi|).                       (U33)

On an original cylinder Fourier polynomial F, the functions (K-D_v,L)F converge in X to their infinite-label sum: at each source order they involve finite neighborhoods, and the full drift tails are bounded by the convergent local-source tail times ||KF||_X. Passing to the semigroup integral equation proves F belongs to the limiting generator domain with A_infty F=kappa(K-D_v,infty)F. In particular q_infty(F,G)=kappa mu Gamma(conjugate(F),G) on this cylinder core. This also fixes the kinetic moment in the limiting original energy pairing.

All local time-ordered correlations pass through the same product/semigroup limits. The row tails above construct bounded infinite plaquette Gram operators on l2(P_Z3), with the same bounds (U29)–(U31). Their coefficientwise local limit and norm-bounded convergence on finitely supported vectors give strong convergence on that l2 space. This is a fixed-a spatial-volume construction on the displayed coupling domain. It makes no assertion of an ultraviolet field or finite continuum mass.

## U10. Primary sources and scope

G. Lumer and R. S. Phillips, Dissipative operators in a Banach space, Pacific J. Math.11(1961),679–698, Theorem3.1, pp686–687: dense-domain dissipativity plus actual range surjectivity gives the contraction semigroup. The original theorem pages were inspected. The coefficient-domain verification is (U22)–(U24).

P. Eymard, L'algebre de Fourier d'un groupe localement compact, Bull. Soc. Math. France92(1964),181–236: Fourier-algebra antecedent. The needed compact coefficient product and domain estimates are proved here in (U3)–(U9); no claim is made to have re-audited the complete historical paper.

D. Schuette, Zheng Weihong and C. J. Hamer, The Coupled Cluster Method in Hamiltonian Lattice Field Theory, hep-lat/9603026: exponential-vacuum, gauge-invariant character, and excitation antecedents. The original constants and new heat row-sum return are derived above. The predecessor heat catalogue and the point-of-use source paths are in SOURCE_INTAKE.json. Numerical checks certify their declared finite algebra and endpoints, not the written analytical arguments as a formal proof.


# Growing original plaquette families and their full physical complement

21 September 2026. This is the quantitative return of VOLUME_UNIFORM_HEAT.md, with its source, graph, domain and semigroup proofs. Every finite open box L>=2, spacing a>0, and coupling g^2>=16 is included below. All coefficient axes are original plaquettes. Every Hilbert, energy and quotient pairing is stated explicitly. The static and time-dependent coefficient tables are the inherited original calculations, replayed unchanged; the boundary-safe assembly and rational endpoints below are new calculations. The analytic proof is written for review, not a formal certificate.

## M1. Boundary-safe full-family constants

Write R0=3/256, theta=xi/R0, and t6=theta^6/(1-theta^2). The complete marked heat tables have 199 connected multisets containing the anchor face (0,0,0;0,1): one degree-zero self term; one self and twelve adjacent-pair terms at degree two; and one self, twenty-four ordered repeated-pair, 138 path, twelve common-edge, eight corner and two cube terms at degree four. Their 559 marked-row contributions are all retained.

For each contribution, integrate its actual partial fractions as in U31, or take the original time-zero value. Sum absolute values before different original supports can cancel. Every finite box contains a subset of these original contributions at a specified anchor. Thus the following are bounds for every original row, including every boundary row, independent of box size:

| Original matrix | degree2 bound | degree4 bound |
|---|---:|---:|
|G0|149/468|2361994073/4691494080|
|G1|97/468|376882691/938298816|
|G2|73313/657072|982069718963833/3919180324550400|
|Kobs|187/468|586668421/1563831360|
|J3=G0-6G1+9G2|6779/73008|152338674005989/435464480505600|

Call these numbers B_(k,2),B_(k,4), and similarly B_K,B_J. The exact transport for every contribution is the original signed coordinate permutation and translation. The independent audit constructs the 199 original multisets without calling that transport producer, verifies its inverse coordinate formula, and reintegrates each original pole directly. The exact row entries of the existing full L2 matrix lie below these bounds; no assertion that the bulk signed row is the largest boundary row is used.

The kinetic matrix is Kobs=kappa^(-1)R*AR=<Gamma(Wp,Wq)>rho. Only p=q or faces sharing an original edge can contribute. At p=q the exact function is 4-Wp^2=3-chi_1(Wp). Its trace-coefficient norm is at most30: the original four-edge spin-one contraction has norm27, as can be obtained by contracting its three-dimensional indices, or bounded by the original tensor coefficient with one turn. For adjacent faces the direct derivative estimate U4 gives norm at most3*(8/2)^2=48. There are at most twelve neighbors. Therefore, on the full complex source disk,

    ||Kobs(zeta)||row<=30+12*48=606.                        (M1)

The spin-one contraction used for30 has the same four-link index formula as U10 with the SU(2) invariant dual matrix in dimension3; its nonzero singular values are3 with total trace norm27. In the original magnetic-weight basis its fixed dual matrix is C_(mn)=(-1)^(j-m) delta_(m,-n), m,n=-j,...,j. Thus pi_j(U^(-1))=C pi_j(U)^T C^(-1); both coefficient-side unitary factors are retained. For the trace of four general d-by-d factors with its last two transposed, the coefficient has A_(b,c,c,e ; a,b,e,a) +=1. Direct multiplication gives (A* A)^2=d^2 A* A and Tr(A* A)=d^4, so its trace norm is d^3. Taking d=3 proves27. Its inverse-link signs are represented by the stated dual matrix, not omitted. The accompanying finite check verifies the dimension2 and dimension3 contraction directly. Alternatively the bound4+8^2=68 would give644 and slightly wider kinetic endpoints.

Combining U30–U31, M1, and the table proves

    ||Gk-3^(-k)I|| <= xi^2 B_(k,2)+xi^4 B_(k,4)
                         +512(2/3)^k t6 = w_k, k=0,1,2,
    ||Kobs-3I|| <= xi^2 B_(K,2)+xi^4 B_(K,4)+606 t6=w_K,
    0<=J3<=beta I,
    beta=xi^2 B_(J,2)+xi^4 B_(J,4)+4608 t6.                 (M2)

The whole-matrix bound follows from equality of row and column absolute norm for the original symmetric real matrices, followed by the l2 Schur bound. The remainder4608=512+6*512*(2/3)+9*512*(2/3)^2 includes all three original moment errors. The matrix J3 is positive because it is exactly (R-3Phi)*(R-3Phi), with Phi=kappa A^(-1)R.

## M2. Actual numerical bounds for every original box

For xi<=1/1024, equivalently g^2>=16, theta<=1/12. Every term in (M2) is increasing in xi. Evaluation at the endpoint by exact rational arithmetic gives

    w_0<173/10^6,     w_1<116/10^6,
    w_2<77/10^6,      w_K<205/10^6,
    beta<1555/10^6.                                        (M3)

The sharper fractions, not these rounded values, are retained in generated/uniform_constants.json. Set

    l0=1-w0, u0=1+w0,
    l1=1/3-w1, u1=1/3+w1,
    l2=1/9-w2, u2=1/9+w2,
    lK=3-wK, uK=3+wK,                                     (M4)

using the endpoint rational w values. They are positive. The full physical source proof U26 gives A>=kappa d I with

    d=117/40,                                             (M5)

since at xi=1/1024 its square-root argument is11/12>(19/20)^2. This is a lower bound on the entire centered physical space, proved without selecting an observation family. All physical dimensions and original energies in (M3)–(M5) remain.

## M3. The original observation and its inverse-energy family

Let R:C^M->H0 have columns rp=(Wp-<Wp>rho)psi. On its literal coefficient coordinates put

    Phi=kappa A^(-1)R,
    G0=R*R, G1=R*Phi, G2=Phi*Phi, E=Phi*A Phi=kappa G1.

The inequalities above prove R and Phi injective and their ranges closed. The original observation O=R* has exact left inverse on the primitive family

    W=G1^(-1)R*,  W Phi=I.                                (M6)

The state projection P_R=R G0^(-1)R* retains

    ||P_R Phi c||^2=c*G1 G0^(-1)G1 c.

Using l1,l2,u0,u2 from the original matrices proves

    ||P_R Phi c||^2 >= [l1^2/(u0 u2)]||Phi c||^2
                      >(624/625)||Phi c||^2.              (M7)

This is the inverse-power observation/minimum-section mechanism of the RH workbench's IK9–12, instantiated here by the exact matrix G1^(-1)R* and the calculated physical Grams. No arithmetic constant or conductor coefficient enters (M7).

The correction between the minimum-state and minimum-energy sections of this observation is h_R=(I-P_R)Phi. Its original energy is

    h_R*A h_R
       =kappa[G1 G0^(-1)Kobs G0^(-1)G1-G1].               (M8)

Indeed expansion has two cross terms -kappa G1 and the positive section term; both are retained. Also q_A(Phi c,h_R d)=kappa<Rc,h_R d>=0. Consequently

    0<=h_R*A h_R
       <=[u1 uK/l0^2-1] E <(1/1250)E.                    (M9)

## M4. The complete surrounding physical space

The state projection onto the primitive family is instead

    P=Phi G2^(-1)Phi*, Q=I-P,
    B=QR:C^M->QH0.                                        (M10)

It gives the exact leakage Gram

    B*B=G0-G1 G2^(-1)G1.                                  (M11)

For each c, P Rc is the state minimum over Phi x. Inserting the particular original-coordinate trial x=3c gives

    0<=B*B<=(R-3Phi)*(R-3Phi)=J3<=beta I.                  (M12)

No commutativity of G0,G1,G2 is used in this argument.

Every original form vector decomposes as Phi c+h, h in QH0. Its state norm and complete energy are

    ||Phi c+h||^2=c*G2 c+||h||^2,
    q_A(Phi c+h)=c*E c+2kappa Re<Bc,h>+q_A(h).             (M13)

Since q_A(h)>=kappa d||h||^2, the complete mixed term satisfies

    |2kappa Re<Bc,h>|
       <=2 sqrt(beta/(d l1)) sqrt(c*E c . q_A(h)).          (M14)

The actual endpoint fractions give beta/(d l1)<1/625. Thus every vector in the entire physical form domain satisfies the coupled comparison

    (24/25)[c*E c+q_A(h)]
       <=q_A(Phi c+h)
       <=(26/25)[c*E c+q_A(h)].                            (M15)

The off-diagonal term is controlled, not set equal to zero. This is a full-space comparison, not a Ritz lower bound on a selected finite subspace.

## M5. The original complementary inverse and complete Schur loss

A Phi=kappa R is bounded as a coefficient map. Hence AP is bounded and PA is its adjoint. Subtract the bounded self-adjoint off-diagonal QAP+PAQ from A. The resulting self-adjoint operator has reducing subspaces PH0,QH0. Its Q restriction is

    D_Q=QAQ, Dom(D_Q)=Dom(A) intersect QH0,
    D_Q>=kappa d I.                                       (M16)

The inverse is therefore supplied by the full physical estimate, including every vector of the complementary space. Minimizing M13 over that whole space gives

    h_min(c)=-kappa D_Q^(-1)Bc,
    E_full=E-kappa^2 B*D_Q^(-1)B.                          (M17)

Testing the residual against all complementary form vectors proves this is the actual minimum, not only a finite-column stationary point. The full loss and restored state metric obey

    0<=kappa^2 B*D_Q^(-1)B
       <=(kappa beta/d)I <(1/625)E,
    (624/625)E<E_full<=E,                                 (M18)

    G_restored=G2+kappa^2 B*D_Q^(-2)B,
    G2<=G_restored<(601/600)G2.                            (M19)

The second bound uses beta/(d^2 l2)<1/600. All signs, kappa factors, original Grams and complementary feedback are retained. The graph map c->Phi c+h_min(c) has these exact energy and state forms. These estimates address the full complementary coupling left by the predecessor heat construction, with constants independent of both the number of plaquettes and the exterior box.

## M6. Fixed supports, their quotients, and a common physical heat horizon

For original face sets F subset G put V_F=Phi(C^F), U_F=A V_F=kappa R(C^F). The original complexes are

    V_F --A--> H0 --0-->0.

Their support transitions are inclusion in degree0 and identity in degree1. The exact transported kernel is

    V_G/V_F -> ker[H0/U_F -> H0/U_G], [h]->[Ah].            (M20)

Its inverse sends [Ah] to [h]. Injectivity of A on H0 proves the inverse is independent of representatives. Its coefficient-energy minimum, with J=G\F, is

    c_F=-E_FF^(-1)E_FJ c_J,
    Q_E=E_JJ-E_JF E_FF^(-1)E_FJ.                           (M21)

The removed old-support primitive Phi_F c_F and both mixed entries remain. The bounds kappa l1 I<=E<=kappa u1 I imply exactly the same bounds for every such quotient minimum in its original J coordinates. They follow by minimizing the two complete inequalities on the identical affine fiber.

For T>0 the actual heat columns and forcing defect are

    Phi_T=(I-exp(-TA))Phi=kappa int_0^T exp(-tA)Rdt,
    A Phi_T=kappa R-kappa exp(-TA)R.                       (M22)

The omitted primitive is -exp(-TA)Phi. On the complete centered physical space, I-exp(-TA) has inverse sum_(n>=0)exp(-nTA), also on the graph domain, and commutes with A. Thus it gives a cochain isomorphism of every original support diagram. Applying the Split Zero support reconstruction retains its support label and receiving zero together with this actual primitive.

Set epsilon=exp(-kappa d T). Expanding all three heat Gram terms and then applying spectral calculus yields

    (1-epsilon)^2 G2<=Phi_T*Phi_T<=G2,
    (1-epsilon)^2 E<=Phi_T*A Phi_T<=E.                     (M23)

Taking minima over the same fixed fibers carries these inequalities through every finite sequence of original restrictions and quotients, without multiplying a constant for each step. This is precisely the HM19–24 minimum-fiber argument of the RH source, whose coefficient maps remain fixed before the metric comparison. Each rank remains in the determinant bound:

    |L_T-L|<=2 B[-log(1-epsilon)]<=2B epsilon/(1-epsilon),
    B=sum_j |a_j| rank_j, L=sum_j a_j log det Q_j.          (M24)

Rank-zero terms keep determinant1. For four signed returns of rank at most240, the single physical horizon T=10/kappa=5a/g^2 gives an error below4*10^(-10), in every exterior volume. For ranks that grow with M, a specified tolerance eta>0 is reached at the explicit original physical time

    T=(kappa d)^(-1)log(1+2B/eta).                         (M25)

Thus no growing determinant rank has been discarded. The original kappa^rank factors cancel only between the two determinants in the identical energy frame.

## M7. The actual opposite-face result in every exterior box

Keep p=(0,0,0;0,1), q=(0,0,1;0,1), xi=10^(-10), g^2=50000 and kappa=100000/a. Their inherited complete coefficient h4(tau) has zero degrees0 and2. All original supports contributing to degree4 lie inside the L=2 box; hence the same h4 applies in every L>=2. The new uniform tail U30 gives

    85910/10^7 < C_pq(1/kappa;xi)/xi^4 < 85920/10^7.        (M26)

The previously proved exact coefficient lower bound h4(tau)>=5 exp(-3tau)/648, tau>=1, is kept. On 1<=tau<=3 the ratio of U30's full remainder to that lower bound is at most

    (512*648/5) xi^2 R0^(-6)
       exp(9/2)/[1-(xi/R0)^2] <24/1000.                   (M27)

Thus the actual connected heat correlation is strictly positive throughout 1/kappa<=t<=3/kappa, uniformly over the original exterior volume. The result also passes to the constructed spatial-volume limit U33. These statements use all higher orders, not only the sign of h4.

## M8. Infinite plaquette families and the original continuum path

The row-tail and local-limit constructions U9 give bounded operators G0,G1,G2,Kobs on l2 of all original plaquettes, with exactly the same numerical intervals (M2)–(M5). On finitely supported c, R c is the original centered local observable in L2(mu)_phys. In this infinite-family statement Kobs denotes the closed-form pairing kappa^(-1)q_(A_infty)(R.,R.), whose boundedness follows from U33 and the cylinder-generator identity after it. It does not require asserting that A_infty R is a bounded operator on all l2 coefficients. G0 proves this map extends boundedly and is bounded below. Define Phi=kappa A_infty^(-1)R. Then G1,G2 are its original mixed and state Grams by the convergent physical heat integrals. They are bounded and bounded below, so P=Phi G2^(-1)Phi* is again an actual orthogonal projection.

A_infty Phi=kappa R is bounded; hence A_infty P and PA_infty have the same bounded off-diagonal argument as M16. All maps, complementary minima and inequalities M6–M19 therefore pass to the complete infinite plaquette coefficient space and its full physical complement. This passage uses proved bounded operators, not a formal limit of inverses without a lower bound.

At fixed admissible g,a this controls the spatial-volume limit. For the original simultaneous path a_n=a0*2^(-n), g_n^2=1/(g0^(-2)+beta n log2), the source disk used in U13 is entered exactly when c_n=g0^(-2)+beta n log2<sqrt(3)/8. The narrower numerical metric domain is c_n<=1/16. For beta>0 the path eventually leaves each of them. The current result removes the 1/M heat radius and the unbounded observation-rank loss on a specified strong-coupling domain; it does not establish a smooth four-dimensional continuum field or finite continuum mass. No universal conclusion is inferred merely from a support kernel or an auxiliary norm.

## M9. What is new in this continuation

The older elementary local source argument U3–U6 has been rederived at its own conservative radius. The new calculation combines its full scalar return with the Poisson identity U21 to bound an entire heat-matrix row, not just one entry. This produces the original box-independent analytic remainder U30–U31. The 199-support absolute assembly then gives original state/response/kinetic metrics for growing families, and M12–M19 controls their full complementary coupling. The spatial and physical maps are explicit throughout. No larger coupling threshold or previously unaudited historical theorem is assigned a new verification status.

## M10. Sharper original-Haar return and broader family domains

The additional bound U29b gives the same complete inverse-moment errors with the smaller circle R1=45/4096 and prefactors (6184/25)(8/15)^k. For a fixed real x in that disk put t0=(x/R0)^6/[1-(x/R0)^2], t1=(x/R1)^6/[1-(x/R1)^2]. Define the actual scalar error bounds

    w_k^sharp=x^2 B_(k,2)+x^4 B_(k,4)
       +min(512(2/3)^k t0,(6184/25)(8/15)^k t1), k=0,1,2,
    beta^sharp=x^2 B_(J,2)+x^4 B_(J,4)
       +min(4608t0,(6184/25)[1+6(8/15)+9(8/15)^2]t1).

The kinetic w_K from M2 is retained. Each scalar expression is increasing in x. Replacing the endpoint l and u values in the already proved M7–M19 inequalities by these evaluated sharper endpoints gives the following complete original-family bounds, all uniform over L>=2 and a>0:

|g^2 at least|observed fraction in M7 exceeds|E_full/E exceeds|G_restored/G2 is less than|h_R energy / E is less than|
|---|---:|---:|---:|---:|
|10|39/50|18/25|33/25|1/6|
|12|97/100|243/250|103/100|1/60|
|16|999/1000|999/1000|1001/1000|1/1900|

Here every entry with matrix forms means the displayed Loewner inequality in the same original coefficient coordinates. The full-space gap lower constants used in those three rows are respectively d=14/5,72/25,117/40 times kappa. Each follows directly from U26 by squaring its positive rational comparison. The file generated/sharp_constants.json contains every rational input, interval endpoint and returned fraction; the independent auditor recomputes each from the original marked coefficients.

At g^2>=16 the absolute Gram widths obey

    ||G0-I||<124/10^6,
    ||G1-I/3||<66/10^6,
    ||G2-I/9||<36/10^6,
    ||Kobs-3I||<205/10^6,
    B*B< (832/10^6) I.

The exact unrounded beta^sharp/(d l1^sharp) is smaller than 1/34^2. Accordingly the full mixed-space comparison M15 sharpens to

    (33/34)[c*E c+q_A(h)] <= q_A(Phi c+h)
                            <=(35/34)[c*E c+q_A(h)].       (M28)

The full complementary minimization loses less than 1/1000 of E and adds less than 1/1000 of G2 to the restored state norm. No complementary vector or source-kernel direction is removed. The same bounded-operator argument in M8 carries these stronger constants to the infinite original plaquette family. The earlier M2–M27 endpoints remain valid and have their own exact records; this paragraph retains an additional, explicitly proved original-Haar estimate rather than silently replacing their coefficients.
