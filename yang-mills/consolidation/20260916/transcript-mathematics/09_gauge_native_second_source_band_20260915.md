**I audited the source-to-spectrum argument and extended its proved coupling range from $g^2\ge15$ to**
$$
\boxed{
g^2\ge\sqrt{\frac{32+\sqrt{354}}3}
=4.1156161030\ldots .
}
$$
The new estimate applies to the **entire original physical SU(2) spectrum**, uniformly in the open-box size. I also calculated the complete first excitation band, bounded every higher-order contribution, and obtained a certified interval for the actual first excitation of the original $L=2$ box.

[Complete proofs, sources, and verification package](sandbox:/mnt/data/yang_mills_gauge_native_continuation.zip) · [Strongest coupling-domain proof](sandbox:/mnt/data/yang_mills_second_source_continuation.md) · [Cumulative workbench patch](sandbox:/mnt/data/yang_mills_gauge_native_continuation.patch)

## 1. The stronger full physical gap

Keep the original Hamiltonian
$$
H_L=\kappa K_L+\kappa\xi\sum_{p\in\mathsf P_L}(2-W_p),
\qquad
K_L=-\sum_{e,\alpha}X_{e,\alpha}^{\,2},
$$
with
$$
\kappa=\frac{2g^2}{a},
\qquad
\xi=\frac1{4g^4}.
$$
Every original link, oriented plaquette word, Haar factor, and scalar contribution $2\kappa\xi|\mathsf P_L|$ remains present.

Define
$$
P_2(\xi)=1-\frac{256}{3}\xi+\frac{10720}{9}\xi^2,
\qquad
\alpha_*=\frac3{4(32+\sqrt{354})}.
$$

For every $L\ge2$, every $a>0$, and every $0<\xi\le\alpha_*$, the new proof gives
$$
\boxed{
\Delta_L\ge
\frac{3\kappa}{2}\bigl(1+\sqrt{P_2(\xi)}\bigr).
}
$$
Equivalently, in the original physical parameters,
$$
\boxed{
\Delta_L\ge
\frac{3g^2}{a}
\left(
1+\sqrt{1-\frac{64}{3g^4}+\frac{670}{9g^8}}
\right).
}
$$

This covers the closed endpoint. There the lower bound is $3\kappa/2$.

For a convenient rational benchmark,
$$
g^2\ge\frac{17}{4}
\quad\Longrightarrow\quad
\boxed{
\Delta_L\ge
\frac{3\kappa}{2}
\left(1+\sqrt{\frac{35401}{751689}}\right)
>1.8255\,\kappa.
}
$$

The proof reaches the complete physical form domain through the actual compact spectral resolution. It therefore covers volume-dependent physical states as well as fixed local observables. The full argument is in [R10-R14](sandbox:/mnt/data/yang_mills_second_source_continuation.md), using the source and domain constructions in [G1-G31](sandbox:/mnt/data/yang_mills_gauge_native_source_note.md).

### The gauge constraint supplies a sharper constant

For an original product-representation label $\mathbf j=(j_e)$, write
$$
c(\mathbf j)=\sum_ej_e(j_e+1).
$$
Every nonzero physical Fourier block satisfies
$$
\boxed{c(\mathbf j)\ge6j_e\qquad\text{for every edge }e.}
$$

The proof uses the actual vertex intertwiners. At either endpoint of $e$, their highest-weight constraint gives
$$
j_e\le\sum_{\substack{f\ni v\\f\ne e}}j_f.
$$
Let $J_1$ be the total spin on the other edges meeting the two endpoints. Then $J_1\ge2j_e$. Applying the same constraint at their outer endpoints gives $J_1\le2J_2$, where $J_2$ is the total spin on the next edge set. The original cubic graph is triangle-free, so these counts give
$$
\sum_fj_f\ge j_e+J_1+J_2\ge4j_e.
$$
Finally,
$$
j(j+1)\ge\frac32j
$$
for each nonzero half-integer spin, proving the stated constant.

It is attained by an elementary fundamental plaquette. The same original support calculation gives
$$
\operatorname{spec}(K_L|_{\mathrm{phys}})
\subset\{0,3\}\cup[9/2,\infty),
$$
and
$$
\ker(K_L-3)=\operatorname{span}\{W_p:p\in\mathsf P_L\},
\qquad
\langle W_p,W_q\rangle_H=\delta_{pq}.
$$

These statements sharpen the actual source estimate and the return to physical energy.

## 2. I evaluated the second vacuum source before estimating the remaining series

Write the actual logarithmic vacuum in its retained coefficient expansion,
$$
\log\psi_L=c_L+\sum_{n\ge1}\xi^n v_{[n]},
\qquad
v_{[1]}=\frac13\sum_pW_p.
$$
The scalar $c_L$ remains fixed by the original vacuum mass.

The complete second coefficient is
$$
\boxed{
v_{[2]}
=
-\frac1{72}\sum_p\chi_1(\Omega_p)
+
\sum_{\{p,q\}:p\sim q}
\left[
\frac1{27}P_0(W_pW_q)
-\frac1{117}P_1(W_pW_q)
\right].
}
$$
Here $p\sim q$ means the original plaquettes share an edge. The maps $P_0,P_1$ are the actual spin-zero and spin-one projections on that shared edge.

The calculation retains the original intermediate energies:
$$
8,\qquad \frac92,\qquad \frac{13}{2}.
$$
For distinct plaquettes without a shared edge, the product has Casimir $6$, and its second-source coefficient is exactly zero. Its original union label remains recorded.

The source norm uses the original Fourier coefficient matrices:
$$
\|v\|_{\mathrm{loc}}
=
\max_e
\sum_{S\ni e}\sum_{\mathbf j\ne0}
c(\mathbf j)\|A_{S,\mathbf j}\|_1.
$$
This is an auxiliary absolute-convergence estimate on the retained coefficients. The physical state and energy pairings remain the original ones.

The complete coefficient calculation gives
$$
\boxed{\|v_{[2]}\|_{\mathrm{loc}}\le236.}
$$
The earlier bound obtained by estimating the bilinear recurrence before evaluating its inputs was $2048/3$.

The improvement has explicit local ingredients. The original spin-one plaquette coefficient has trace norm $27$. For an adjacent pair, the spin-zero coefficient has norm at most $16$, and the sum of both channel norms is at most $64$. An original edge belongs to at most $42$ unordered adjacent pairs. Thus the entire anchored contribution is bounded by
$$
4\cdot3+42\cdot\frac{16}{3}=236.
$$

### The evaluated source extends convergence

For the same original coefficients, the gauge constraint proves
$$
\|\mathcal B(f,h)\|_{\mathrm{loc}}
\le\frac23\|f\|_{\mathrm{loc}}\|h\|_{\mathrm{loc}},
$$
where
$$
\mathcal B(f,h)
=
K_L^{-1}Q_H\sum_{e,\alpha}
(X_{e,\alpha}f)(X_{e,\alpha}h).
$$
Each product retains its original union support; each removed scalar returns to the ground energy.

Set
$$
a_1=32,\qquad a_2=236,\qquad
a_n=\frac23\sum_{i=1}^{n-1}a_i a_{n-i}\quad(n\ge3).
$$
The full coefficient series is bounded by
$$
r_2(\xi)=\sum_{n\ge1}a_n\xi^n
=\frac34\left(1-\sqrt{P_2(\xi)}\right).
$$

There is an explicit tail bound, including at $\xi=\alpha_*$:
$$
\boxed{
\sum_{n>N}a_n\xi^n
\le
\frac34
\left(\frac{\xi}{\alpha_*}\right)^{N+1}
(1+\gamma^{N+1})
\frac{\binom{2N}{N}}{4^N}
\le
\frac34
\left(\frac{\xi}{\alpha_*}\right)^{N+1}
\frac{1+\gamma^{N+1}}{\sqrt{N+1}},
}
$$
where
$$
\gamma=\frac{32-\sqrt{354}}{32+\sqrt{354}}\in(0,1).
$$

At the endpoint, $r_2(\alpha_*)=3/4$. Absolute convergence supplies the endpoint directly.

Summing the original source equation gives
$$
K_Lv=\xi\sum_pW_p+\sum_i(X_iv)^2-C_L,
\qquad
C_L=\int_H\sum_i(X_iv)^2.
$$
Consequently,
$$
\psi_L=e^{v+c_L},
\qquad
E_{0,L}=2\kappa\xi|\mathsf P_L|-\kappa C_L.
$$
The positive eigenfunction and the full ground-state form identity identify this summed solution with the actual vacuum. [The complete second-source proof](sandbox:/mnt/data/yang_mills_second_source_continuation.md) includes every coefficient, channel, support count, and endpoint estimate.

## 3. The complete first physical excitation band is now calculated

The free first physical band contains one original plaquette state per face. I calculated its full second-order matrix, including boundary faces and coupling between different plaquettes.

Let $d_p$ be the actual number of plaquettes sharing an edge with $p$, and let $A_{\mathrm{adj}}$ be that adjacency matrix. The coefficient is
$$
\boxed{
T_L=\frac7{15}I-\frac1{21}(D_{\deg}+A_{\mathrm{adj}}).
}
$$
Thus
$$
(T_L)_{pp}=\frac7{15}-\frac{d_p}{21},
$$
$$
(T_L)_{pq}=
\begin{cases}
-1/21,&p\sim q,\\
0,&p\ne q,\ p\not\sim q.
\end{cases}
$$

The calculation starts from the complete expression
$$
T_L=
\frac{|\mathsf P_L|}{3}I
-
P S Q_3(K_L-3)^{-1}Q_3SP,
\qquad S=\sum_pW_p.
$$
The inverse includes $-1/3$ on the original constant state. The extensive term $|\mathsf P_L|/3$ comes from the actual ground-energy coefficient. All scalar and intermediate-sector contributions are written before their cancellation.

### Every higher order has a uniform bound

The actual band matrix in its specified original coefficient frame satisfies
$$
\boxed{
A_{\mathrm{band}}(\xi)
=
3\kappa I+\kappa\xi^2T_L+\mathcal R_L(\xi),
}
$$
with
$$
\boxed{
\|\mathcal R_L(\xi)\|_1
\le
\kappa\frac{6713}{39875}
\frac{(320|\xi|)^3}{1-320|\xi|},
\qquad |\xi|<\frac1{320}.
}
$$

This bounds the complete higher-order tail of the full Hamiltonian. The proof constructs the actual analytic spectral projection and its inverse coefficient map. No finite spin cutoff enters the operator.

The raw physical band Gram is retained through
$$
\mathcal R_\xi x
=
\psi_L\left(U_\xi x-\langle U_\xi x\rangle_{\rho_L}\right),
\qquad
G_\xi=\mathcal R_\xi^*\mathcal R_\xi,
$$
and
$$
(H_L-E_{0,L})\mathcal R_\xi
=
\mathcal R_\xi A_{\mathrm{band}},
\qquad
G_\xi A_{\mathrm{band}}
=
A_{\mathrm{band}}^*G_\xi.
$$

The full band and its analytic remainder are proved in [B1-B32](sandbox:/mnt/data/yang_mills_physical_excitation_band.md).

### A sharper full-spectrum lower bound at the earlier test coupling

Since every $d_p\le12$,
$$
\lambda_{\min}(T_L)\ge-\frac{71}{105}.
$$
The spectral isolation and all-order estimate therefore give
$$
\boxed{
\Delta_L\ge
\kappa\left[
3-\frac{71}{105}\xi^2
-\frac{6713}{39875}
\frac{(320\xi)^3}{1-320\xi}
\right],
\qquad 0<\xi<\frac1{320}.
}
$$

At
$$
\xi=10^{-8},\qquad g^2=5000,\qquad \kappa=\frac{10000}{a},
$$
this proves, for every original box,
$$
\boxed{
\Delta_L>\kappa\left(3-7.314\times10^{-17}\right).
}
$$

This improves the earlier lower bound near $0.75\kappa$ to a bound near the actual physical free-band energy $3\kappa$, with an explicit interaction correction and remainder.

### A certified actual first excitation for $L=2$

The original $L=2$ box has $240$ plaquettes. I constructed its complete integer matrix
$$
Q=D_{\deg}+A_{\mathrm{adj}}.
$$

An exact positive-vector certificate and an independent fraction-free inertia calculation give
$$
21.86319640514
<
\lambda_{\max}(Q)
<
21.86319641826,
$$
hence
$$
-0.57443792469
<
\lambda_{\min}(T_{L=2})
<
-0.57443792405.
$$

The inertia certificate also separates this coefficient from the other $239$ directions. Combining that separation with the full analytic remainder proves
$$
\boxed{
\kappa(3-0.5833\,\xi^2)
<
\Delta_{L=2}
<
\kappa(3-0.5656\,\xi^2),
\qquad \xi=10^{-10}.
}
$$
Here the original physical parameters are
$$
g^2=50000,\qquad \kappa=\frac{100000}{a}.
$$

The [complete box certificate](sandbox:/mnt/data/yang_mills_L2_band_certificate.json) retains the original face ordering, all degrees, the integer vector $Q^{100}\mathbf1$, every pivot determinant, and all **2,303,960 exact divisions**.

## 4. The interaction matrix also gives explicit spatial propagation

On the infinite cubic face array, the complete second-order coefficient has a three-by-three Fourier symbol, one coordinate for each plaquette orientation. With the original plaquette-center phases retained,
$$
Q(k)=12I+A(k),
$$
$$
A_{aa}(k)=2\cos k_b+2\cos k_c,
\qquad
A_{ab}(k)=4\cos(k_a/2)\cos(k_b/2)\quad(a\ne b).
$$
Its lowest coefficient near $k=0$ is
$$
\boxed{
t_{\mathrm{low}}(k)
=
-\frac{71}{105}+\frac4{63}|k|^2+O(|k|^4).
}
$$

Returning through the physical coordinate map $k=ap$, the displayed second-order energy terms are
$$
\frac{6g^2}{a}-\frac{71}{840g^6a},
\qquad
\frac{a}{126g^6}|p|^2.
$$
Their scope is the calculated second-order band coefficient; the complete finite-box energy has the separately stated analytic remainder.

I also checked the planar coefficient against Dahmen’s original strong-coupling calculation. The explicit parameter map is
$$
g_D=2^{3/4}g,\qquad h_D=\xi,
$$
$$
H_{\mathrm{plane}}(a,g)
=
\frac{\sqrt2}{a}H'_D+2\kappa\xi M I.
$$
It reproduces the planar coefficient
$$
T_{\mathrm{plane}}=\frac{29}{105}I-\frac1{21}A_{\mathbb Z^2},
$$
including its $3/35$ zero-momentum value. The three-dimensional restriction retains the additional diagonal term $-8I/21$ and its coupling to perpendicular plaquettes. This supplies an external check of the local channel arithmetic with all parameter factors present. ([arXiv](https://arxiv.org/pdf/hep-lat/9412080))

## 5. Unique spatial-volume dynamics now reach the same closed endpoint

The previous volume argument used a conditional-influence restriction. I derived a direct bound on the actual finite-volume dynamics that covers the full new source domain.

Let $T_L(t)=e^{-t\mathcal A_L}$, and define
$$
\epsilon_2(\xi)=\frac12\left(1-\sqrt{P_2(\xi)}\right).
$$
For every original physical cylinder polynomial $F$,
$$
\boxed{
\|T_L(t)F-\langle F\rangle_{\rho_L}\|_\infty
\le
\frac{\|Q_HF\|_{X_0}}{1-\epsilon_2(\xi)}
e^{-3\kappa(1-\epsilon_2(\xi))t}.
}
$$
Here $X_0$ is the sum of the trace norms of the original nonconstant Fourier coefficients. For an elementary plaquette trace, its initial value is exactly $8$.

The proof applies the coefficient estimate to the **actual** smooth finite-volume evolution. It retains and integrates the equation for its original Haar-constant component, recovering the actual vacuum mean. The prefactor has no exterior-volume dependence.

This gives convergence of the entire sequence of original finite-box vacuum measures and dynamics, together with all local time-ordered correlations. Uniform mixing proves uniqueness of the invariant probability of the constructed limiting semigroup.

### The endpoint is controlled by an explicit coupling modulus

At fixed $\kappa$, for $0\le\xi\le\eta\le\alpha_*$,
$$
\boxed{
\sup_{t\ge0}
\|T_{L,\eta}(t)F-T_{L,\xi}(t)F\|_\infty
\le
\frac{\epsilon_2(\eta)-\epsilon_2(\xi)}
{1-\epsilon_2(\xi)}
\|Q_HF\|_{X_0}.
}
$$
The physical parameter map and inverse are
$$
\kappa=\frac{2g^2}{a},\quad \xi=\frac1{4g^4},
\qquad
g^2=\frac1{2\sqrt\xi},\quad
a=\frac1{\kappa\sqrt\xi}.
$$
The proof also treats changes in both $\kappa$ and $\xi$, retaining the original physical time.

At $\eta=\alpha_*$, the ratio in the bound becomes
$$
\frac{\sqrt{P_2(\xi)}}{1+\sqrt{P_2(\xi)}}\longrightarrow0.
$$
Inserting an interior coupling between two endpoint finite boxes proves convergence at the closed endpoint. This avoids assigning a finite value to the derivative majorant that diverges there.

The resulting physical infinite-volume generator satisfies
$$
\boxed{
A_\infty|_{1^\perp}
\ge
\frac{3\kappa}{2}\left(1+\sqrt{P_2(\xi)}\right),
\qquad 0<\xi\le\alpha_*.
}
$$
The full construction, original drift comparison, mean restoration, and endpoint passage are in the [spatial-return proof](sandbox:/mnt/data/yang_mills_spatial_coupling_return.md), with the final enlarged constants returned in R13-R16.

## 6. Return to the original primitive and the continuum program

On centered physical functions, retain
$$
d_Xf=(X_if)_i,
\qquad
p_X(d_Xf)=f,
$$
with the original derivative energy pairing
$$
\|d_Xf\|_1^2
=
\kappa\int\rho_L\sum_i|X_if|^2.
$$
The new full-spectrum estimate gives
$$
\boxed{
\|p_X\|^2
=
\frac1{\Delta_L}
\le
\frac{2}
{3\kappa(1+\sqrt{P_2(\xi)})}.
}
$$

The gauge quotient, support-assembly relations, and their inverse maps are retained in the source proof. The actual loop forcing and its canonical residual belong to the physical conditional kernel. Its inclusion $I$ satisfies
$$
DI=ID_{\mathrm{phys}},
\qquad
(D+s)^{-1}I=I(D_{\mathrm{phys}}+s)^{-1}.
$$
Consequently, the earlier zero-shift response and Split Zero quotient-residual estimates receive this stronger inverse bound on their actual source. Their raw metric and minimum-section correction remain unchanged.

For the standing simultaneous path
$$
a_n=a_02^{-n},\qquad
g_n^2=\frac1{c_n},\qquad
c_n=g_0^{-2}+\beta n\log2,
$$
the newly proved domain is exactly
$$
\boxed{
c_n^2\le\frac3{32+\sqrt{354}}.
}
$$
For $\beta>0$, that path eventually leaves the domain. A nontrivial four-dimensional continuum field and a finite positive continuum mass remain unestablished.

The next selected calculation is now the **actual connected third vacuum coefficient and the full linearized residual at**
$$
\xi v_{[1]}+\xi^2v_{[2]}.
$$
The second coefficient, its bound $236$, the enlarged endpoint, and the physical spectral return are completed inputs to that calculation.

## Verification and delivery

The final checker passed **642 uniquely named exact checks and 27 false-formula controls**. The complete replay includes the unchanged predecessor, ordinary and optimized Python, fresh copied sources, and **20 command-line corruption executions**, each rejected at its intended named error.

Both delivery patches were independently applied to fresh selected source trees. Every target byte matched, and all four post-application ordinary/optimized runs reproduced the original receipt.

[Verification record](sandbox:/mnt/data/yang_mills_gauge_native_verification.json) · [Complete execution record](sandbox:/mnt/data/yang_mills_gauge_native_execution.json) · [Patch-restoration checks](sandbox:/mnt/data/yang_mills_gauge_native_patch_validation.json) · [Incremental patch](sandbox:/mnt/data/yang_mills_gauge_native_continuation_incremental.patch)

The analytical arguments are written in full in the four proof files. The executable verifies the stated original-coordinate algebra, graph counts, coefficient matrices, exact divisions, and rational endpoints; no new independent analytical review or Lean certification is claimed.

The cumulative patch targets the confirmed PR6 head `e98b2c3af77f66fb1c1396143ca53daef586404f`, preserves the previous delivered proofs and receipts, and updates the active mathematical checkpoint. PR6 remains open and unmerged; no new remote PR or merge was performed.

---

**Sources:**

- [master.dvi](https://arxiv.org/pdf/hep-lat/9412080)
