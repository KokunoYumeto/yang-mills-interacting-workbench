**Both calculations are complete: the connected cubic vacuum source and the full linearized residual around the first two source coefficients.** Together they extend the proved coupling range from the saved bound $g^2\ge4.115616\ldots$ to
$$
\boxed{g^2\ge3.825973052393386,}
$$
with a lower bound for the **entire physical spectrum**, uniform in the original open-box size.

I published the complete proofs and checkers in **draft PR #8**, “Evaluate cubic vacuum source and full linearized Yang-Mills gap return,” at commit `91434b6962062bd80439d4cb2cae9d2479264dde`. It is stacked on PR #6; nothing has been merged. 

[Complete research package](sandbox:/mnt/data/yang_mills_cubic_linearized.zip) · [Cubic-source proof](sandbox:/mnt/data/yang_mills_cubic_source.md) · [Linearized-return proof](sandbox:/mnt/data/yang_mills_linearized_return.md)

## 1. The resulting physical lower bound

Retain the original Hamiltonian
$$
H_L=\kappa K_L+\kappa\xi(2M-S),
\qquad
S=\sum_{p\in\mathsf P_L}W_p,
$$
$$
K_L=-\sum_{e,\alpha}X_{e,\alpha}^{\,2},
\qquad
\kappa=\frac{2g^2}{a},
\qquad
\xi=\frac1{4g^4}.
$$
Here $M=|\mathsf P_L|$, and every $W_p$ is the original oriented four-link trace. The additive energy $2\kappa\xi M$ remains in $H_L$.

Define the explicit polynomial
$$
\mathscr D(x)=
\frac{
46457856x^4+183150656x^3+18324072x^2-1168128x+13689
}{13689}.
$$
Let $\alpha$ be its first positive root. Exact rational calculations give
$$
0.0170787544707772675
<
\alpha
<
0.0170787544707772677.
$$

For every original box $L\ge2$, every $a>0$, and every $0<\xi\le\alpha$, the new proof establishes
$$
\boxed{
\Delta_L\ge
\kappa\left[
\frac32\left(1+\sqrt{\mathscr D(\xi)}\right)
+\frac{1136}{13}\xi^2
\right].
}
$$
The exact coupling threshold is $g^2\ge1/(2\sqrt\alpha)$; its value lies strictly between
$$
3.825973052393385
\quad\text{and}\quad
3.825973052393386.
$$

At the closed endpoint, the coefficient of $\kappa$ is greater than $61/40$. A convenient interior consequence is
$$
\boxed{
g^2\ge4
\quad\Longrightarrow\quad
\Delta_L>1.8385\,\kappa
=3.677\,\frac{g^2}{a}.
}
$$

This result improves the **coupling domain** of the saved second-source argument. The preceding sharper small-$\xi$ excitation-band estimates retain their own scope; I have not replaced them by this bound. The complete spectral return is in equations L20-L28 of the [linearized proof](sandbox:/mnt/data/yang_mills_linearized_return.md).

## 2. First calculation: every connected cubic source term

Write the logarithmic vacuum in the original source coordinates:
$$
\psi_L=e^{v+c_L},
\qquad
c_L=-\frac12\log\int e^{2v}\,dU.
$$
With
$$
\Gamma(f,h)=\sum_{e,\alpha}(X_{e,\alpha}f)(X_{e,\alpha}h),
\qquad
B(f,h)=K_L^{-1}Q_H\Gamma(f,h),
$$
where $Q_H$ removes the original Haar constant, the exact equation is
$$
v=\xi v_1+B(v,v),
\qquad
v_1=\frac13\sum_pW_p.
$$
Every removed scalar is retained in the original ground energy
$$
E_{0,L}=2\kappa\xi M-\kappa\int\Gamma(v,v)\,dU.
$$

The complete second coefficient remains
$$
v_2=
-\frac1{72}\sum_p\chi_1(\Omega_p)
+
\sum_{\{p,q\}:p\sim q}
\left[
\frac1{27}P_0(W_pW_q)
-\frac1{117}P_1(W_pW_q)
\right].
$$
Here $p\sim q$ means the original plaquettes share an edge, and $P_0,P_1$ project its two fundamental factors onto their spin-zero and spin-one components.

I evaluated
$$
v_3=2B(v_1,v_2)
$$
on **all five connected configurations**, including repeated faces.

### Complete coefficient table

For the three-distinct-face configurations, the projected function is $W_pW_qW_r$. For the repeated configuration, it is $(W_p^2-1)W_q$.

| Original configuration | Retained spin component | Original total Casimir | Coefficient in $v_3$ |
|---|---|---:|---:|
| One face repeated three times | $\chi_{1/2}=W_p$ | $3$ | $-1/81$ |
| Same | $\chi_{3/2}$ | $15$ | $1/810$ |
| Repeated adjacent pair $\{p,p,q\}$ | Shared-edge spin $1/2$ | $9$ | $-11/4212$ |
| Same | Shared-edge spin $3/2$ | $12$ | $11/11232$ |
| Three-face path | $n=0,1,2$ spin-one shared edges | $6+2n$ | $1/162,\,-11/8424,\,1/3510$ |
| Three faces sharing one edge | Total shared spin $1/2,3/2$ | $15/2,\,21/2$ | $-2/1755,\,2/2457$ |
| Three faces at a cube corner | $n=0,1,2,3$ spin-one shared edges | $9/2+2n$ | $2/81,\,34/13689,\,-38/17901,\,2/2457$ |

These projectors have explicit formulas in the original edge Casimirs:
$$
P_{e,j}
=
\prod_{\ell\in J_e,\ \ell\ne j}
\frac{E_e-\ell(\ell+1)I}{j(j+1)-\ell(\ell+1)}.
$$
The finite list $J_e$ is the actual allowed tensor-product spin list. All multiplicities remain, including the two copies of total spin $1/2$ for three fundamentals.

Three exact cancellations are important.

For the repeated adjacent pair,
$$
P_{1/2}\!\left[(W_p^2-1)W_q\right]
=
\frac43W_pP_0(W_pW_q)-\frac13W_q.
$$
The two lower-$W_q$ contributions to $Kv_3$ are $1/72$ and $-1/72$, so they cancel at their original seven-link support.

For the common-edge triple, the original eight-dimensional tensor space gives
$$
P_0^{(12)}+P_0^{(13)}+P_0^{(23)}
=
\frac32P_{\mathrm{total}\,1/2}.
$$
This retains the full multiplicity. The calculation uses the sum of those projectors, with their complete matrix products recorded.

For the cube corner, the $n=1$ projected function is exactly zero: its central vertex would carry one spin-one edge and two spin-zero edges, and the original invariant tensor space there has dimension zero. Its coefficient and original support label remain recorded. The all-spin-zero component is
$$
P_{000}(W_pW_qW_r)=\frac14W_{\partial(p,q,r)},
$$
with the original six-link boundary word.

The product identity
$$
2\Gamma(f,h)=(c_f+c_h)fh-K(fh)
$$
and these explicit recouplings prove every entry in the table. Disconnected triples contribute zero because their differentiated factors have no common original edge. Equations C13-C20 of the [cubic proof](sandbox:/mnt/data/yang_mills_cubic_source.md) give the complete calculation.

### The evaluated coefficient improves the quantitative bound

Using the original Casimir-weighted trace-coefficient norm, the per-configuration bounds and the numbers meeting an original anchor edge are
$$
\begin{array}{c|ccccc}
&\text{self}&\text{repeated}&\text{path}&\text{common edge}&\text{corner}\\
\hline
\text{bound}&40/27&66/13&1408/351&512/117&3504/351\\
\text{count}&4&84&460&40&24.
\end{array}
$$
Thus
$$
\boxed{
\|v_3\|_{\mathrm{loc}}
\le
\frac{944984}{351}
<2693.
}
$$
The previous estimate obtained before evaluating this coefficient was
$$
\frac{30208}{3}=10069\frac13.
$$

The improvement comes from the actual channel coefficients, shared-edge integrations, gauge constraints, and original geometry. The physical state and energy pairings remain unchanged.

## 3. Second calculation: the complete linearized residual and its infinite tail

Set
$$
q_2=\xi v_1+\xi^2v_2.
$$
The residual is exactly
$$
\boxed{
R_2=\xi v_1+B(q_2,q_2)-q_2
=\xi^3v_3+\xi^4B(v_2,v_2).
}
$$
The quartic term remains present. The proof supplies a finite original-coordinate formula for every one of its components, using the Casimir projectors above.

The derivative of the source equation at $q_2$ is
$$
\mathscr L_2=I-\mathscr J_2,
\qquad
\mathscr J_2h=2B(q_2,h).
$$

Evaluating the separate total-spin and single-edge-spin contributions of $v_2$ gives
$$
m(v_2)\le\frac{5834}{39},
\qquad
t(v_2)\le\frac{137}{6}.
$$
These improve the actual operator and residual estimates to
$$
\|\mathscr J_2\|
\le
\ell(\xi)
=
\frac{128}{3}\xi+\frac{3132}{13}\xi^2,
$$
$$
\|R_2\|_{\mathrm{loc}}
\le
\delta(\xi)
=
\frac{944984}{351}\xi^3
+\frac{799258}{39}\xi^4.
$$
Their discriminant is precisely
$$
\mathscr D(\xi)=(1-\ell(\xi))^2-\frac83\delta(\xi).
$$

Throughout $0<\xi\le\alpha$, the proof establishes $\ell(\xi)<1$. Hence the **actual** linearized inverse is
$$
\mathscr L_2^{-1}
=
\sum_{j=0}^{\infty}\mathscr J_2^j,
\qquad
\|\mathscr L_2^{-1}\|
\le\frac1{1-\ell(\xi)}.
$$

For the complete correction $w=v-q_2$,
$$
\mathscr L_2w=R_2+B(w,w).
$$
The full binary-tree expansion converges, including at the closed endpoint, and gives
$$
\boxed{
\|w\|_{\mathrm{loc}}
\le
w_*(\xi)
=
\frac34\left[1-\ell(\xi)-\sqrt{\mathscr D(\xi)}\right].
}
$$

There are explicit error bounds for both infinite operations. The linear inverse has the exact residual
$$
\mathscr L_2^{-1}R_2-\sum_{j=0}^{N}\mathscr J_2^jR_2
=
\mathscr J_2^{N+1}\mathscr L_2^{-1}R_2.
$$
For the nonlinear expansion, put
$$
\vartheta_*=\frac{8\delta}{3(1-\ell)^2}\le1.
$$
Its tail after $N$ tree orders is at most
$$
\boxed{
\frac34(1-\ell)\,
\vartheta_*^{N+1}
\frac{\binom{2N}{N}}{4^N}
\le
\frac34(1-\ell)\,
\frac{\vartheta_*^{N+1}}{\sqrt{N+1}}.
}
$$
That summable endpoint calculation supplies convergence even where the nonlinear contraction estimate reaches one.

### An explicit value inside the enlarged domain

At the original coupling $g^2=4$,
$$
\xi=\frac1{64},
\qquad
\kappa=\frac8a.
$$
The complete bounds are
$$
\|\mathscr L_2^{-1}\|
\le\frac{39936}{10963},
\qquad
\|\mathscr L_2^{-1}R_2\|_{\mathrm{loc}}
\le\frac{33836149}{808280064},
$$
$$
\boxed{
\|v-q_2\|_{\mathrm{loc}}<0.047293824576905,
}
$$
and
$$
\boxed{
\|v-q_2-\mathscr L_2^{-1}R_2\|_{\mathrm{loc}}<0.005432.
}
$$
These bounds include all further nonlinear terms.

## 4. Returning that correction to the physical spectrum

The returned operator is the original ground-state transform
$$
\mathcal A
=
\psi^{-1}(H-E_0)\psi
=
\kappa\bigl(K-2\Gamma(v,\cdot)\bigr).
$$

The evaluated spin contributions give
$$
t(v)\le
\frac{16}{3}\xi+\frac{137}{6}\xi^2+\frac{w_*}{6}.
$$
Consequently, on the original Fourier coefficients,
$$
\|2\Gamma(v,h)\|_X
\le
\chi(\xi)\|Kh\|_X,
$$
where
$$
\chi(\xi)
=
\frac12\left(1-\sqrt{\mathscr D(\xi)}\right)
-\frac{1136}{39}\xi^2.
$$

For an actual positive-energy physical eigenfunction, subtraction of its Haar scalar gives
$$
(K-\lambda/\kappa)h=Q_H\,2\Gamma(v,h).
$$
Every nonconstant physical Fourier component has $c(\mathbf j)\ge3$. The coefficient estimate therefore gives
$$
\lambda\ge3\kappa(1-\chi(\xi)).
$$
The complete compact physical spectral resolution returns this to the full form-domain inequality stated at the beginning.

The approximation’s full operator defect remains explicit:
$$
\boxed{
Q_H\mathcal Ah-\kappa K\mathscr L_2h
=
-2\kappa Q_H\Gamma(w,h).
}
$$
It has bound
$$
\frac{2\kappa}{3}w_*\|Kh\|_X.
$$
Thus the approximate source, its correction, and the actual physical operator are connected by an exact equation with a quantified remainder.

The corresponding Split Zero source windows are
$$
V_N\xrightarrow{\mathscr L_2}V\xrightarrow0 0,
\qquad
V_N=\operatorname{span}\{R_2,\mathscr J_2R_2,\ldots,\mathscr J_2^NR_2\}.
$$
Their transported kernel has the explicit isomorphism
$$
V_{N+1}/V_N
\longrightarrow
\ker\!\left(V/\mathscr L_2V_N\to V/\mathscr L_2V_{N+1}\right),
\qquad
[h]\longmapsto[\mathscr L_2h],
$$
with inverse supplied by $\mathscr L_2^{-1}$. The original residual, primitive, and support label all remain.

For the physical derivative primitive, with its original energy pairing,
$$
\boxed{
\|p_X\|^2=\frac1{\Delta_L}
\le
\frac1{\kappa d(\xi)},
\qquad
d(\xi)=3(1-\chi(\xi)).
}
$$

## 5. An additional completed calculation: the fourth vacuum-energy coefficient

The two source calculations also determine
$$
\boxed{
E_{0,L}
=
2\kappa M\xi-\frac{\kappa M}{3}\xi^2
+
\kappa\left(\frac{5M}{216}-\frac{2J}{1053}\right)\xi^4
+\mathcal E_{\ge6},
}
$$
where $J$ is the **actual number of unordered adjacent plaquette pairs**.

For the original box, writing $m=2L$,
$$
M=3m^2(m+1),
\qquad
J=6m(3m^2-1).
$$
At $L=2$, the fourth coefficient divided by $\kappa$ is
$$
\frac{1198}{351}.
$$

I checked this through an independent Rayleigh-Schrödinger coefficient calculation:
$$
\frac{E_{[4]}}{\kappa}
=
\frac{M^2}{27}
-
\frac19\left\langle Q_HS^2,K^{-1}Q_HS^2\right\rangle_H,
$$
$$
\left\langle Q_HS^2,K^{-1}Q_HS^2\right\rangle_H
=
\frac M8+\frac23\binom M2+\frac2{117}J.
$$
Substitution reproduces the same coefficient, including the boundary-dependent $J$.

The remaining orders have a complete bound:
$$
\boxed{
|\mathcal E_{\ge6}|
\le
\frac{49\kappa|\mathsf E_L|}{1200}
\frac{(60|\xi|)^6}{1-(60|\xi|)^2},
\qquad
0<|\xi|<\frac1{60}.
}
$$
Every extensive factor remains. This comes from the analytic source construction and the exact link-center involution that makes $E_0-2\kappa M\xi$ even.

## 6. What the literature comparison actually establishes

The exponential-vacuum equation, connected loop expansion, and linear excitation equation have established Hamiltonian lattice-gauge antecedents. Schütte, Zheng Weihong, and Hamer explicitly formulate these equations and their gauge-invariant loop/Casimir construction. Their work is credited in the proof. ([arXiv](https://arxiv.org/html/hep-lat/9603026v1))

The comparison retains the exact parameter and energy map:
$$
g_C=2^{3/4}g,
\qquad
\boxed{
H_{\mathrm{original}}(a,g)
=
\sqrt2\,H_C(a,2^{3/4}g)+2\kappa\xi M I.
}
$$
Their original commutator derivative is $iX$ in our generator coordinates, which returns their vacuum equation to the signs in $K v-\Gamma(v,v)-\xi S$. ([arXiv](https://arxiv.org/html/hep-lat/9603026v1))

The proof also compares Dahmen’s planar strong-coupling calculation and Hui-Fang-Shi’s higher-order vacuum construction using their respective parameter maps. The latter paper explicitly states its later finite-order and random-phase approximations; this contribution instead retains the complete residual and bounds the ensuing infinite correction. ([arXiv](https://arxiv.org/abs/hep-lat/9412080))

The planar-to-spatial comparison has its own exact original-link inclusion $J_\pi$:
$$
K_3J_\pi=J_\pi K_2,
$$
$$
\boxed{
H_3J_\pi-J_\pi H_2
=
\kappa\xi
\left[
2(M_3-M_2)-\sum_{p\text{ outside the plane}}W_p
\right]J_\pi.
}
$$
All perpendicular plaquettes remain in that defect.

**The specific contribution submitted here is the complete spatial cubic coefficient calculation, its evaluated source bounds, and the full linearized infinite-tail return to an explicit physical gap domain.** The literature reading establishes the displayed correspondences and antecedents. It does not establish a global priority claim or an independently confirmed best coupling threshold.

## Verification and present scope

The checker passed **2,246 named exact checks and 15 false-formula controls**. It evaluates all **612 anchored cubic multisets at two exact rational quaternion assignments**, comparing direct differentiation of the original link products with the separately constructed projected formulas.

The full replay includes the unchanged saved predecessor, ordinary and optimized Python, copied sources, intended corruption rejections, and restored sources. Fresh patch application reproduced every target file and the complete verification output. The publication source-identity check also caught and corrected a transcription error before the final commit. 

[Complete verification record](sandbox:/mnt/data/yang_mills_cubic_linearized_verification.json) · [Execution record](sandbox:/mnt/data/yang_mills_cubic_linearized_execution.json) · [Patch-validation record](sandbox:/mnt/data/yang_mills_cubic_patch_validation.json) · [Workbench patch](sandbox:/mnt/data/yang_mills_cubic_linearized.patch)

The analytical proofs are written in full and submitted for review. The finite tests verify their specified coordinate identities and numerical certificates; no new Lean formalization or independent external analytical review has been performed.

The standing continuum path remains
$$
a_n=a_02^{-n},
\qquad
g_n^2=\frac1{c_n},
\qquad
c_n=g_0^{-2}+\beta n\log2.
$$
Its exact inclusion in the enlarged domain is
$$
\boxed{c_n\le2\sqrt\alpha.}
$$
For $\beta>0$, it eventually leaves that domain. **A nontrivial four-dimensional continuum field and a finite positive continuum mass remain unestablished.**

The two requested calculations are now completed inputs in the workbench. The active checkpoint records the next original coefficient
$$
v_4=2B(v_1,v_3)+B(v_2,v_2),
$$
together with the signed action of the linearized operator on those same connected four-face supports.
