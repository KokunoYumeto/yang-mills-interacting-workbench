**The calculation now gives a positive lower bound for the full physical SU(2) spectrum, uniformly in the box size, on the explicit range $g^2\ge15$.** I used that bound to complete the actual **zero-shift Wilson-loop response**, and then proved convergence to a **unique spatial infinite-volume vacuum and dynamics at fixed lattice spacing**.

[Complete mathematical proof](sandbox:/mnt/data/yang_mills_uniform_gap_zero_shift_note.md) · [Full sources, checker, and execution records](sandbox:/mnt/data/yang_mills_uniform_gap_zero_shift.zip) · [Tested workbench patch](sandbox:/mnt/data/yang_mills_uniform_gap_zero_shift.patch)

The lattice spacing and physical coupling remain explicit throughout. The smooth four-dimensional continuum limit is still outside the completed result.

## 1. A lower bound on the entire physical form domain

Retain the original operator
$$
H_L=\kappa K_L+v\sum_{p\in\mathsf P_L}(2-W_p),
\qquad
\kappa=\frac{2g^2}{a},\quad
v=\frac1{2g^2a},\quad
\xi=\frac{v}{\kappa}=\frac1{4g^4}.
$$
Here $K_L=-\sum_{e,\alpha}X_{e,\alpha}^2$, and every $W_p$ is the complete original oriented plaquette trace. Let $\psi_L$ be the actual positive unit vacuum, $\rho_L=\psi_L^2$, and
$$
\mathcal A_L=\psi_L^{-1}(H_L-E_{0,L})\psi_L.
$$

Define
$$
r_\xi=\frac3{16}\left(1-\sqrt{1-\frac{2500}{3}\xi}\right),
\qquad
q_\xi=\frac{65536}{9375}r_\xi,
$$
$$
d_\xi=\frac34(1-q_\xi)e^{-32\pi\xi}.
$$

For **every $L\ge2$, every $a>0$, and every $g^2\ge15$**, the proof establishes
$$
\boxed{
q_{\mathcal A_L}(f)
\ge
\kappa d_\xi
\left(
\int\rho_L|f|^2\,dU
-
\left|\int\rho_Lf\,dU\right|^2
\right)
}
$$
on the complete original scalar form domain. Restricting this inequality to the physical invariant subspace gives
$$
\boxed{\Delta_L\ge\kappa d_\xi>0.}
$$

Two convenient explicit consequences are
$$
\boxed{
\Delta_L\ge\frac{\kappa}{100}
=\frac{g^2}{50a},
\qquad g^2\ge15,
}
$$
and
$$
\boxed{
\Delta_L\ge\frac{3\kappa}{20}
=\frac{3g^2}{10a},
\qquad g\ge4.
}
$$

The constants contain **no exterior-volume factor**. The inequality covers every centered physical state, including states and observable labels that change with the regulator. The complete strongest argument is [H1-H23 in the gap proof](sandbox:/mnt/data/yang_mills_full_physical_gap.md).

### How the stronger bound was obtained

The first improvement came from calculating the original plaquette’s Fourier coefficient exactly. In the original four-link tensor coordinates,
$$
W_p(U)=\operatorname{Tr}\!\left[
A\,(U_1\otimes U_2\otimes U_3\otimes U_4)
\right],
$$
where all sixteen trace-index contributions, including inverse-link signs, remain in $A$.

Its matrix satisfies
$$
(A^*A)^2=4A^*A,\qquad \operatorname{Tr}(A^*A)=16.
$$
Consequently,
$$
|A|=\frac12A^*A,
\qquad
\boxed{\|A\|_1=8.}
$$

I then used the same coefficient families with the auxiliary support estimate
$$
\|f\|_{\mathrm{loc}}
=
\sup_e
\sum_{S\ni e}
\left(\frac54\right)^{|S|}
\sum_{\mathbf j\ne0}
c(\mathbf j)\,\|A_{S,\mathbf j}\|_1,
$$
where
$$
c(\mathbf j)=\sum_e j_e(j_e+1).
$$
The label $S$ is retained even when a product’s active Fourier support becomes smaller.

The actual logarithmic-vacuum equation gives the source and nonlinear bounds
$$
\|f^{(1)}\|_{\mathrm{loc}}\le\frac{625}{8}\xi,
\qquad
\|\mathcal B(f,h)\|_{\mathrm{loc}}
\le\frac83\|f\|_{\mathrm{loc}}\|h\|_{\mathrm{loc}},
$$
with
$$
\mathcal B(f,h)=K_L^{-1}Q_H\sum_{e,\alpha}
(X_{e,\alpha}f)(X_{e,\alpha}h).
$$
The Haar-constant terms removed by $Q_H$ are separately recorded and returned to $E_{0,L}$.

The complete support series converges on the stated domain. Its summed coefficient bound is exactly $r_\xi$. The reconstructed function is identified with the **actual** vacuum through
$$
\psi_L=e^{v_L+c_L},
\qquad
c_L=-\frac12\log\int e^{2v_L}\,dU,
$$
and the original eigen-equation and ground-state form identity. Its scalar coordinate and original Haar mass remain present.

The final improvement uses the actual single-link conditional expectations
$$
(\mathsf P_e f)(U_{e^c})
=
\frac{\int \rho_L(U_e,U_{e^c})f(U_e,U_{e^c})\,dU_e}
{\int \rho_L(U_e,U_{e^c})\,dU_e}.
$$
The convergent support series bounds their complete influence matrix by $q_\xi<1$. A bounded-operator spectral calculation then proves
$$
(1-q_\xi)\operatorname{Var}_{\rho_L}(f)
\le
\sum_e\|f-\mathsf P_e f\|_{\rho_L}^2.
$$

The original pointwise vacuum-derivative estimate supplies the second comparison:
$$
\sum_e\|f-\mathsf P_e f\|_{\rho_L}^2
\le
\frac{4e^{32\pi\xi}}{3\kappa}\,
q_{\mathcal A_L}(f).
$$
Combining these two inequalities gives the full physical gap above, with the original $\kappa$ and the single-link Casimir factor $3/4$ retained.

The general Fourier-algebra and conditional-comparison methods have established antecedents. The new proof supplies their explicit coefficient, support, domain, and energy return for this original Hamiltonian. 

## 2. The actual zero-shift response is now enclosed

For the elementary square at the origin, retain its ordered holonomy $\Omega$, the trace $F=\operatorname{tr}\Omega$, and conditional expectation $\mathsf E_C$ onto $\Omega$ in the actual vacuum measure. Put
$$
Q_C=I-\mathsf J_C\mathsf E_C,\qquad
\mathcal K_C=\ker\mathsf E_C,
$$
and let $D$ be the operator represented by the original energy form restricted to $\mathcal K_C$.

Every vector in this kernel has zero vacuum mean. The full-domain estimate therefore proves
$$
\boxed{
D\ge\kappa d_\xi I,
\qquad
\|D^{-1}\|\le\frac1{\kappa d_\xi}.
}
$$
This includes the complete conditional kernel, with its exterior degrees of freedom.

For the original forcing
$$
W=-Q_C\mathcal A_LF,
$$
the zero-shift response is
$$
M_0=\langle W,D^{-1}W\rangle_{\rho_L}.
$$

At the actual coupling
$$
\xi=10^{-8},\qquad g^2=5000,\qquad \kappa=\frac{10000}{a},
$$
the new certificate proves, for every exterior box,
$$
\boxed{
\left|M_0-\frac8{39}\kappa\xi^2\right|
<
0.0000094\,\kappa\xi^2,
}
$$
and
$$
\boxed{
\left|
\|D^{-1}W\|_{\rho_L}^2-\frac{196}{4563}\xi^2
\right|
<
0.00000319\,\xi^2.
}
$$

The centers are calculated from the original twelve neighboring plaquettes. Their two retained components have electric energies $9\kappa/2$ and $13\kappa/2$, giving
$$
\frac{3/4}{9/2}+\frac{1/4}{13/2}=\frac8{39},
$$
$$
\frac{3/4}{(9/2)^2}+\frac{1/4}{(13/2)^2}
=\frac{196}{4563}.
$$
The full analytic remainder returns these local Haar calculations to the actual interacting-vacuum pairing.

The same calculation now supplies a two-sided enclosure for the **full physical gap**:
$$
\boxed{
0.74999514999\,\kappa
\le
\Delta_L
<
\left(3+\frac5{10^{13}}\right)\kappa.
}
$$
The lower bound is the full-domain estimate. The upper bound follows from the explicit inclusion of the restored physical trial state into the complete centered form domain.

### The retained cohomology has a quantified zero-shift primitive

For the actual trial $Y\in\mathcal K_C$, retain
$$
R=W-DY,
\qquad
a_Y=q_D(Y)>0,
\qquad
c_Y=\langle Y,W\rangle_{\rho_L},
\qquad
\alpha_Y=\frac{c_Y}{a_Y}.
$$
The canonical representative is
$$
R_{\mathrm{can}}=W-D(\alpha_YY).
$$

In the original pairing $\langle r,D^{-1}t\rangle_{\rho_L}$,
$$
\boxed{
\|[W]\|_{\mathcal K_C/D\operatorname{span}\{Y\}}^2
=
M_0-\frac{|c_Y|^2}{a_Y},
}
$$
and
$$
\boxed{
\langle R,D^{-1}R\rangle_{\rho_L}
=
\|[W]\|^2+a_Y|\alpha_Y-1|^2.
}
$$
The second term retains the actual boundary primitive $(\alpha_Y-1)Y$. The calculated bound on their complete nonnegative sum is
$$
\boxed{
\|[W]\|^2+a_Y|\alpha_Y-1|^2
<
0.0000000000142\,\kappa\xi^2.
}
$$

There is also a full-domain primitive factorization. On the original smooth physical source, define
$$
d_Xf=(X_if)_i,
\qquad
d_Bf=(f-\mathsf P_ef)_e,
$$
$$
T(d_Xf)=d_Bf,\qquad
p_B(d_Bf)=f-\langle f\rangle_{\rho_L}.
$$
The inverse of $T$ on its actual image is $z\mapsto d_Xp_Bz$, and
$$
\boxed{p_X=p_BT.}
$$
With the derivative range carrying its original energy pairing,
$$
\boxed{
\|p_X\|^2=\frac1{\Delta_L}
\le
\frac1{\kappa d_\xi}.
}
$$
Thus the support construction is now connected to a bounded primitive for the complete physical energy problem.

## 3. The spatial-volume limit is unique, including its dynamics

The support calculation gives more than a uniform estimate: each labelled coefficient is **exactly the same in every box containing its original support**. Its convergent series therefore defines a fixed summable interaction family.

I used those coefficients to prove convergence of the entire sequence of finite-box vacuum measures to a unique measure $\nu$. The proof retains the original conditional densities and the complete influence matrix; it does not choose a subsequence and then assign uniqueness to it.

The same coefficients control the original drift $b_e^L=X_e\log\psi_L$. Their full mixed derivative matrix has a summable row bound, which permits a direct comparison of the finite-volume ground-relative dynamics. With common original link Brownian motions, the pathwise comparison retains every matrix power:
$$
z_e(t)
\le
\sum_{r\ge0}
\frac{(2\kappa t)^{r+1}}{(r+1)!}
\left(B^r\bigl(t(L)+t(M)\bigr)\right)_e.
$$
Here $B$ is the actual drift-derivative majorant and $t_e(L)$ the actual omitted-support drift error. The row bound, pointwise vanishing of $t_e(L)$, and factorial tail prove convergence of the dynamics on every finite set of original links.

This gives a unique limiting semigroup and a self-adjoint generator on the constructed vacuum space, with
$$
\boxed{
A_\infty\big|_{1^\perp}\ge\kappa d_\xi.
}
$$

It also proves convergence of **all local time-ordered vacuum correlations**:
$$
\begin{aligned}
&\langle\psi_L,
O_0e^{-t_1(H_L-E_{0,L})}O_1
\cdots
e^{-t_m(H_L-E_{0,L})}O_m\psi_L\rangle\\
&\qquad\longrightarrow
\int O_0T(t_1)\!\left(O_1T(t_2)(\cdots O_m)\right)\,d\nu .
\end{aligned}
$$
Every observable, time interval, and ground-energy subtraction in this expression is retained.

The map from the correlation construction to the physical Hilbert space is explicit:
$$
\boxed{
[O,t]\longmapsto T(t)(O-\nu O).
}
$$
Its pairing is exactly the limiting correlation kernel. The time-zero physical cylinder functions are dense, giving the full unitary rather than an identification based on a finite loop frame.

### The limiting theory is quantitatively nonzero

For the original elementary-loop observable,
$$
\operatorname{Var}_{\nu}(F)\ge e^{-128\pi\xi},
\qquad
q_\infty(F-\nu F)\le4\kappa.
$$
Its limiting correlation consequently obeys
$$
\boxed{
e^{-128\pi\xi}-4\kappa t
\le C_F(t)
\le C_F(0)e^{-\kappa d_\xi t}.
}
$$
The lower bound is positive on an explicitly nonempty time interval.

At fixed $a,g$ in this domain, the first-moment estimate prevents spectral mass from escaping to infinite energy, while the full gap excludes a zero-energy atom in the centered sector. Both endpoint terms from the earlier reconstruction are therefore controlled in this spatial-volume limit.

The complete argument is in the [unique-volume-limit proof, V1-V25](sandbox:/mnt/data/yang_mills_unique_volume_limit.md), with its final coupling constants returned in H23.

### The extensive vacuum energy is retained too

The original finite-volume energy satisfies
$$
\boxed{
\begin{aligned}
\left|
E_{0,L}
-\kappa|\mathsf P_L|
\left(2\xi-\frac{\xi^2}{3}\right)
\right|
\le\kappa\left[
\frac{2048}{27}|\mathsf P_L|\xi^3
+
\frac{65536}{81}|\mathsf E_L|\xi^4
\right].
\end{aligned}}
$$
The energy per plaquette has a unique limit, with that finite remainder. The scalar contribution $2v|\mathsf P_L|$ has remained in the calculation throughout.

## 4. Exact relation to the continuum objective

This completes spatial infinite-volume control on the stated strong-coupling domain, with $a>0$ fixed.

The earlier simultaneous path remains
$$
a_n=a_02^{-n},\qquad
g_n^2=\frac1{g_0^{-2}+\beta n\log2}.
$$
Writing $c_n=g_0^{-2}+\beta n\log2$, the new theorem applies exactly on
$$
\boxed{c_n\le\frac1{15}.}
$$
For $\beta>0$, that is only a finite initial portion of the path.

The other limit order is now explicit too. At any fixed admissible $g$,
$$
\Delta_n\ge\frac{2g^2d_\xi}{a_n}\longrightarrow\infty
\qquad(a_n\to0).
$$
Bounded centered positive-time correlations then tend to zero, and retained zero-time spectral mass moves to the energy-infinity endpoint. This calculation stays attached to its fixed-$g$ path.

**A nontrivial smooth four-dimensional continuum field and a positive finite continuum mass have not been established here.** The completed result supplies a full physical lower bound, a quantified zero-shift primitive, and unique spatial vacuum/dynamics limits from which to continue the original coupling-dependent analysis.

## Verification and delivery

The final checker passed **273 named exact checks and 35 false-formula controls**. The complete replay records ordinary and optimized execution, the unchanged predecessor in both modes, copied-source execution, and restoration after deliberate corruption. All **18 additional command-line corruption cases** failed at their intended named errors.

Both the combined and incremental patches were applied independently to fresh selected source trees. Their complete target bytes matched, and their ordinary/optimized verification outputs reproduced the final receipt.

[Verification record](sandbox:/mnt/data/yang_mills_uniform_gap_zero_shift_verification.json) · [Complete execution record](sandbox:/mnt/data/yang_mills_uniform_gap_zero_shift_execution.json) · [Incremental patch after the previous delivery](sandbox:/mnt/data/yang_mills_uniform_gap_zero_shift_incremental.patch)

The analytical arguments are supplied as complete written proofs. The executable checks their stated finite algebra, original coordinate identities, and rational endpoints; no independent analytical review, Lean certificate, sampled vacuum, or spin-cutoff approximation is claimed.

The combined patch targets the exact PR6 revision `e98b2c3af77f66fb1c1396143ca53daef586404f`, includes the previously unpublished actual-loop-moment contribution, and updates the active mathematical checkpoint. **No new remote PR or merge was performed.** The package contains the proposed PR description, complete sources, and a single-command replay.
