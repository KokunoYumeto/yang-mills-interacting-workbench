# Exact collapse of the finite-box weak-coupling disk at fixed coupling

**Date:** 9 September 2026.  This is a bounded result for the original
finite open-box \(SU(2)\) Hamiltonian.  It does not replace the interacting
continuum theory by a free oscillator and it does not assert either a mass
gap or its absence.  It identifies, with the original coupling and all
plaquettes retained, the precise point at which the available analytic
small-\(g\) argument cannot be continued along a growing-box sequence with
fixed \(g_{\rm YM}>0\).

## 1. The exact finite-box operator

Let \(L\geq2\), \(m=2L\), and let \(E_L\) and \(P_L\) be respectively the
positive nearest-neighbour edges and elementary oriented faces in the open
box with vertices \(\{-L,\ldots,L\}^{3}\).  Their face count is

\[
 M_L:=|P_L|=3m^{2}(m+1)=12L^{2}(2L+1).
\tag{1}
\]

On \(\mathcal H_L=L^{2}(SU(2)^{E_L},d\lambda)\), with product Haar
probability, retain

\[
 H_{L,g,a}=\frac{2g^{2}}{a}H_{0,L}
 +\frac{1}{2g^{2}a}\sum_{p\in P_L}(2-W_p),
 \qquad
 H_{0,L}:=\sum_{e\in E_L}E_e,
\tag{2}
\]

where \(g=g_{\rm YM}>0\), \(a>0\), \(E_e=-\sum_{\alpha=1}^{3}X_{e,\alpha}^{2}\), and
\(W_p=\operatorname{tr}(U_p)\) is the fundamental trace of the original
four-link face word.  Define the multiplication operator

\[
 W_L:=\sum_{p\in P_L}W_p,
 \qquad
 \xi:=\frac{1}{4g^{4}}.
\tag{3}
\]

Then, as an exact operator identity on the common form domain,

\[
 H_{L,g,a}=\frac{2g^{2}}a\bigl(H_{0,L}-\xi W_L\bigr)
       +\frac{M_L}{g^{2}a}I .
\tag{4}
\]

The last term is the complete scalar \(2bM_L\), with
\(b=(2g^{2}a)^{-1}\).  It is retained in (4); it shifts every eigenvalue
by the same amount and therefore does not enter excitation differences.

## 2. Exact interaction norm

Every \(W_p\) is real and satisfies \(|W_p|\leq2\), hence

\[
 \|W_L\|_{\infty}\leq2M_L.
\tag{5}
\]

At the identity configuration \(U_e=I\) for every edge, every face word is
the identity and \(W_p=2\).  The continuous function \(W_L\) therefore
takes the value \(2M_L\), so the upper bound in (5) is attained:

\[
\boxed{\|W_L\|_{\mathcal B(\mathcal H_L)}=2M_L.}
\tag{6}
\]

This uses the original words and all faces; no face or link is dropped.

With \(T_\alpha=-i\sigma_\alpha/2\), the one-link Casimir has first
nonzero eigenvalue \(3/4\).  Consequently the constant function is the
simple ground vector of \(H_{0,L}\), and

\[
\operatorname{dist}\bigl(0,\operatorname{spec}(H_{0,L})\setminus\{0\}\bigr)=\frac34.
\tag{7}
\]

The dimensionless perturbation in (4) has exact norm

\[
\|\xi W_L\|=2\xi M_L=\frac{M_L}{2g^{4}},
\tag{8}
\]

and its ratio to the unperturbed gap is

\[
\frac{\|\xi W_L\|}{3/4}=\frac{2M_L}{3g^{4}}
 =\frac{8L^{2}(2L+1)}{g^{4}}.
\tag{9}
\]

For every fixed finite \(g>0\), (9) tends to \(+\infty\) as \(L\to\infty\).

## 3. The exact Riesz-disk bound and its collapse

Let \(\Gamma\) be the circle \(|z|=3/8\).  By (7),

\[
\|(H_{0,L}-z)^{-1}\|\leq\frac{8}{3},
 \qquad z\in\Gamma.
\tag{10}
\]

The resolvent identity factors as

\[
H_{0,L}-\xi W_L-z
 =(I-\xi W_L(H_{0,L}-z)^{-1})(H_{0,L}-z).
\tag{11}
\]

Using (6) and (10), the Neumann-series proof of invertibility on
\(\Gamma\) is valid whenever

\[
\sup_{z\in\Gamma}
\|\xi W_L(H_{0,L}-z)^{-1}\|
\leq 2\xi M_L\frac83<1,
\]

that is,

\[
\boxed{ |\xi|<\frac{3}{16M_L}. }
\tag{12}
\]

This is a sufficient analytic disk for the rank-one Riesz projection at the
constant ground state.  It is not claimed to be a sharp radius of
analyticity; (12) is the exact radius delivered by the displayed global
operator-norm argument.

Substituting (1) and (3), the disk becomes

\[
\frac{3}{16M_L}=\frac{1}{64L^{2}(2L+1)}.
\tag{13}
\]

Along \(L=j^{2}\),

\[
\frac{3}{16M_{j^{2}}}
 =\frac{1}{64j^{4}(2j^{2}+1)}
 \sim\frac{1}{128j^{6}}.
\tag{14}
\]

At fixed \(g_{\rm YM}=g>0\), \(\xi=1/(4g^{4})\) is independent of \(j\).
For all sufficiently large \(j\),

\[
\frac{1}{4g^{4}}
 \geq \frac{1}{64j^{4}(2j^{2}+1)},
\tag{15}
\]

so the fixed-coupling sequence eventually leaves the sufficient Riesz disk.
Equivalently, the condition for staying inside the disk would be

\[
16j^{4}(2j^{2}+1)<g^{4},
\tag{16}
\]

which cannot hold for an unbounded sequence \(j\) at any fixed finite \(g\).

## 4. What this proves, and what it does not prove

Equations (8)--(16) prove an exact regulator-level obstruction: the
global operator-norm perturbation argument around \(H_{0,L}\) has no
volume-uniform fixed-coupling domain.  The obstruction is driven by the
retained sum of all \(M_L\) Wilson traces, whose norm grows exactly as
\(2M_L\); it is not caused by deleting the scalar term, changing the metric,
or replacing the Wilson action by a quadratic potential.

This result does **not** prove that the interacting eigenvalues fail to
have a continuum limit, nor that the fixed-coupling theory has or lacks a
mass gap.  It proves only that the existing small-\(g\) Riesz/Taylor route
cannot certify such a limit along \(L\to\infty\) at fixed \(g\).  A valid
fixed-coupling continuum argument must therefore supply a different
volume-uniform construction (for example, a nonperturbative spectral,
renormalization, or measure estimate) while retaining (2), the full
plaquette words, and the physical gauge-invariant subspace.

