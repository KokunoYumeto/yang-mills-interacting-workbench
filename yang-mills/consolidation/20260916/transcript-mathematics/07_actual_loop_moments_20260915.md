I have now obtained **explicit enclosures for the actual interacting-vacuum moments $N_0,N_1,N_2$, the Schur response, and the restored state norm**. The calculation also gives new all-coupling estimates with constants independent of the exterior volume.

[Full mathematical proof](sandbox:/mnt/data/yang_mills_actual_loop_moments_note.md) · [Complete research and verification package](sandbox:/mnt/data/yang_mills_actual_loop_moments.zip) · [Workbench patch](sandbox:/mnt/data/yang_mills_actual_loop_moments.patch)

The narrow numerical enclosures below are proved at
$$
\xi=\frac1{4g^4}=10^{-8},
\qquad g^2=5000,
\qquad \kappa=\frac{10000}{a},
$$
for **every $a>0$ and every exterior box $L\ge2$**. This is a large-$g$ domain. The all-coupling results are stated separately, with their actual dependence on $g,a$, and loop length retained.

## 1. The previously unevaluated response quantities now have values enclosed

Keep the full original operator
$$
H=\kappa K+V,\qquad
K=-\sum_{e,\alpha}X_{e,\alpha}^{\,2},
$$
$$
V=\frac1{2g^2a}\sum_p(2-\operatorname{tr}U_p),
\qquad
\kappa=\frac{2g^2}{a}.
$$
Let $\psi$ be its actual positive unit vacuum, $E_0$ its ground energy, and $\rho=\psi^2$. The transported excitation operator is
$$
\mathcal A=\psi^{-1}(H-E_0)\psi,
$$
with the original form
$$
q_{\mathcal A}(f,h)
=\kappa\int\rho\sum_{e,\alpha}
\overline{X_{e,\alpha}f}\,X_{e,\alpha}h\,dU.
$$
These are the workbench’s original Hamiltonian, vacuum, and physical coefficients. 

Take the elementary square based at the origin in directions $1,2$, with its complete holonomy
$$
\Omega=
U_1(0)\,U_2(\mathbf e_1)\,
U_1(\mathbf e_2)^{-1}\,U_2(0)^{-1},
\qquad F=\operatorname{tr}\Omega.
$$

Let $\mathsf E$ be conditional expectation onto this holonomy **in the actual measure $\rho\,dU$**, let $\mathsf J$ be pullback, and put
$$
Q=I-\mathsf J\mathsf E,\qquad \mathcal K=\ker\mathsf E.
$$
The operator $D$ is represented by the original closed energy form restricted to $\mathcal K$. Thus its domain retains the full conditional kernel, including exterior degrees of freedom.

The actual forcing and moments are
$$
W=-Q\mathcal AF,
$$
$$
N_0=\|W\|_\rho^2,\qquad
N_1=\langle W,DW\rangle_\rho,\qquad
N_2=\|DW\|_\rho^2.
$$

The new bounds are
$$
\boxed{
0.9994\,\kappa^2\xi^2<N_0<1.0006\,\kappa^2\xi^2,
}
$$
$$
\boxed{
4.9963\,\kappa^3\xi^2<N_1<5.0037\,\kappa^3\xi^2,
}
$$
$$
\boxed{
25.728\,\kappa^4\xi^2<N_2<25.772\,\kappa^4\xi^2.
}
$$

In particular, the forcing is quantitatively nonzero in the actual interacting vacuum.

For the actual response at the physical shift $s=\kappa$,
$$
M(\kappa)=\langle W,(D+\kappa)^{-1}W\rangle_\rho,
$$
the calculation proves
$$
\boxed{
\left|M(\kappa)-\frac{28}{165}\kappa\xi^2\right|
<0.0000075\,\kappa\xi^2.
}
$$
For the restored kernel primitive,
$$
\boxed{
\left|
\|(D+\kappa)^{-1}W\|_\rho^2
-\frac{796}{27225}\xi^2
\right|
<0.0000021\,\xi^2.
}
$$

The raw observed Gram and kinetic entry remain present:
$$
G=\langle F^2\rangle_\rho-\langle F\rangle_\rho^2,
\qquad
K_0=\kappa\bigl(4-\langle F^2\rangle_\rho\bigr).
$$
At the same coupling,
$$
|G-1|<1.1\times10^{-13},
\qquad
|K_0-3\kappa|<1.1\times10^{-13}\kappa.
$$

These intervals come from explicit analytical remainder bounds evaluated with rational arithmetic. They use no sampled vacuum, fitted density, or spin cutoff. The complete calculations are equations A37-A49 of the attached proof.

### The observation change is explicitly retained

The loop observation is connected to the preceding coarse-edge observation by
$$
\pi_C=\chi_C\circ\pi_{\mathrm{edges}},
\qquad
\mathsf E_C=\mathsf E_\chi\mathsf E_{\mathrm{edges}},
$$
where $\chi_C$ multiplies the original four coarse links with their original orientations.

The additional kernel has the exact isomorphism
$$
\boxed{
\ker\mathsf E_C/\ker\mathsf E_{\mathrm{edges}}
\longrightarrow\ker\mathsf E_\chi,
\qquad
[h]\longmapsto\mathsf E_{\mathrm{edges}}h,
}
$$
with inverse
$$
k\longmapsto[\mathsf J_{\mathrm{edges}}k].
$$
The identities $\mathsf E_{\mathrm{edges}}\mathsf J_{\mathrm{edges}}=I$ and
$h-\mathsf J_{\mathrm{edges}}\mathsf E_{\mathrm{edges}}h
\in\ker\mathsf E_{\mathrm{edges}}$ prove both inverse laws. The moments above are attached to this specified loop observation, and the additional kernel remains part of the energy calculation.

## 2. The key new estimate comes from the actual vacuum equation

Write
$$
u=\log\psi,\qquad b_{e,\alpha}=X_{e,\alpha}u,
\qquad
\mathscr L=\sum_iX_i^2+2\sum_i b_iX_i.
$$
The vacuum equation gives
$$
\sum_iX_i^2u+\sum_i b_i^2=\frac{V-E_0}{\kappa},
\qquad
\mathcal A=-\kappa\mathscr L.
$$

Commutation of the original Casimir with each $X_{e,\alpha}$, together with the antisymmetric generator coefficients, gives the exact differentiated equation
$$
\boxed{
\mathcal A b_{e,\alpha}=-X_{e,\alpha}V.
}
$$

This provides a direct equation for the vacuum derivatives entering the response.

For
$$
w_e=\sum_\alpha b_{e,\alpha}^2,
$$
the original commutators
$$
[X_{e,\alpha},X_{e,\beta}]
=-\epsilon_{\alpha\beta\gamma}X_{e,\gamma}
$$
give
$$
\sum_{i,\alpha}|X_i b_{e,\alpha}|^2\ge\frac12w_e.
$$
The term on the right is the squared norm of the antisymmetric part of the original second-derivative matrix.

At a maximum of $w_e$,
$$
0\ge\frac12\mathscr Lw_e
\ge\frac12w_e-r_e\xi\sqrt{w_e},
$$
where $r_e\le4$ is the actual number of incident plaquettes. Therefore, at **every positive coupling**,
$$
\boxed{
\|X_e\log\psi\|_\infty\le2r_e\xi\le8\xi,
\qquad
\|X_e\log\rho\|_\infty\le16\xi.
}
$$

There is also an exact derivative-energy identity:
$$
\boxed{
\int\rho\sum_{i,\alpha}|X_i b_{e,\alpha}|^2
=
\frac{3\xi}{8}
\left\langle\sum_{p\ni e}W_p\right\rangle_\rho
\le\frac{3r_e\xi}{4}.
}
$$
The index $i$ here runs over **all fine-link derivatives**.

Both results have constants independent of the number of exterior links and faces. They provide the control needed to differentiate the actual forcing and bound $N_1,N_2$.

### A controlled local term and its retained remainder

Set
$$
u_0=\frac{\xi}{3}\sum_pW_p,
\qquad
\mathfrak r_e=X_e(u-u_0).
$$
The full Hamiltonian remains unchanged. The remainder satisfies its own exact equation,
$$
\mathscr L\mathfrak r_{e,\alpha}
=-2\sum_i b_iX_i(X_{e,\alpha}u_0).
$$

For $0<\xi\le3/64$, the proof establishes
$$
\boxed{
|\mathfrak r_e|\le\frac{256}{9}\xi^2,
\qquad
\|\mathcal A\mathfrak r_e\|_\infty
\le\frac{128\kappa}{3}\xi^2,
}
$$
together with an explicit bound on the complete derivative energy of $\mathfrak r_e$.

This controls the difference between the actual vacuum derivative and the displayed local term uniformly over the exterior box. It is the remainder estimate used to return the exact local calculations to the interacting vacuum.

## 3. The coefficients $1,5,103/4$ were calculated from the original neighboring faces

The elementary square has twelve neighboring plaquettes other than itself. Their union with the square uses exactly 32 original links.

For a neighboring plaquette $p$, sharing edge $e$, define
$$
j_p=\sum_\alpha(X_{e,\alpha}W_p)(X_{e,\alpha}F).
$$
The original Pauli identities split $j_p$ into two explicitly constructed components. Their Haar squared norms are
$$
\frac9{64},\qquad \frac3{64},
$$
their cross term is zero, and their original electric Casimir energies are
$$
\frac92\kappa,\qquad \frac{13}{2}\kappa.
$$

The proof obtains these facts by writing the shared path product and the two remaining path products explicitly, applying the Pauli trace identity, and integrating the original Haar variables. Every cross-face pairing has an unmatched exterior link whose integral is zero; the checker constructs those link witnesses.

After retaining the forcing factor $2\kappa\xi/3$ and all twelve neighbors, the exact first local term gives
$$
1,\qquad 5,\qquad \frac{103}{4}
$$
for the three moment coefficients.

Its response is
$$
M_{\mathrm{local}}(s)
=
\kappa^2\xi^2
\left[
\frac{3/4}{s+9\kappa/2}
+
\frac{1/4}{s+13\kappa/2}
\right].
$$
At $s=\kappa$, this gives $28\kappa\xi^2/165$. The actual response differs by the certified remainder stated above.

The same calculation was completed for every square of side $b\ge2$, with original perimeter $\ell=4b$. Its coefficients are
$$
\boxed{
c_0=\frac{\ell+2}{3},\qquad
c_1=\frac{\ell(3\ell+14)}{12},\qquad
c_2=\frac{9\ell^3+66\ell^2+76\ell+104}{48}.
}
$$
The proof supplies explicit finite bounds
$$
|N_j-\kappa^{j+2}\xi^2c_j|
\le\kappa^{j+2}\xi^2\epsilon_j(\ell,\xi),
$$
retaining the loop-size dependence. It also supplies all-coupling upper bounds for the three moments.

The return to the actual vacuum uses the proved local-density comparison
$$
e^{-32\pi d\xi}\le\rho_S\le e^{32\pi d\xi},
$$
for a specified $d$-link support $S$, and the separately derived conditional-fiber comparison. For the elementary square, the two error factors are
$$
e^{1024\pi\xi}-1,
\qquad
e^{1088\pi\xi}-1.
$$
They are retained in the finite error formulas and evaluated with outward rational bounds.

## 4. There is also an all-coupling inverse estimate on the actual derivative source

Let $G_{v,\alpha}$ be the original vertex-gauge generators, and $d_v\le6$ the vertex degree. Their original link coefficients give
$$
\sum_\alpha|G_{v,\alpha}h|^2
\le d_v\sum_{e\ni v,\alpha}|X_{e,\alpha}h|^2.
$$

On the spin-one gauge sector $\mathcal E_v$,
$$
-\sum_\alpha G_{v,\alpha}^2h=2h.
$$
Gauge invariance of the actual vacuum permits integration in $\rho\,dU$, yielding
$$
\mathcal A|_{\mathcal E_v}\ge\frac{2\kappa}{d_v}\ge\frac{\kappa}{3},
$$
and hence
$$
\boxed{
\|(\mathcal A|_{\mathcal E_v}+s)^{-1}\|
\le\frac1{s+\kappa/3},\qquad s\ge0.
}
$$

The vacuum derivatives are actual members of this source:
$$
G_{s(e),\alpha}b_{e,\beta}
=-\epsilon_{\alpha\beta\gamma}b_{e,\gamma}.
$$
The estimate is therefore applied to the forcing equation above and to its remainder.

On the retained running path
$$
c_n=g_0^{-2}+\beta n\log2,\qquad
a_n=a_0\,2^{-n},\qquad g_n^2=c_n^{-1},
$$
it gives
$$
\boxed{
\sup_v\|(\mathcal A_n|_{\mathcal E_v})^{-1}\|
\le\frac{3a_0c_n}{2^{n+1}}\longrightarrow0.
}
$$

The map into the physical forcing is the original contraction
$$
(b_e,X_eF)\longmapsto
\sum_\alpha b_{e,\alpha}X_{e,\alpha}F.
$$
Both factors transform by the same adjoint matrix, so the contraction is gauge invariant. Its energy is carried through the complete product identity
$$
\mathcal A(bc)
=(\mathcal Ab)c+b(\mathcal Ac)
-2\kappa\sum_i(X_ib)(X_ic).
$$
Those last terms remain in the moment estimates. The source inverse estimate and the physical contraction are thus related by an explicit map and its complete energy defect.

## 5. Split Zero now controls an actual response error, including the section correction

For the calculated local trial $Y\in\mathcal K$, retain
$$
R=W-(D+\kappa)Y.
$$
The response identity is
$$
M(\kappa)
=
2\operatorname{Re}\langle W,Y\rangle
-q_{\mathcal A+\kappa}(Y)
+\langle R,(D+\kappa)^{-1}R\rangle.
$$

The final proof audit caught an important point: the chosen trial requires a correction to reach the canonical minimum section. I computed that correction explicitly.

Put
$$
a_Y=q_{\mathcal A+\kappa}(Y),\qquad
c_Y=\langle Y,W\rangle,\qquad
\alpha_Y=c_Y/a_Y.
$$
The proof establishes $a_Y>0$. In the actual complex
$$
\operatorname{span}\{Y\}
\xrightarrow{D+\kappa}\mathcal K
\xrightarrow0 0,
$$
the canonical representative is
$$
R_{\mathrm{can}}
=W-(D+\kappa)(\alpha_YY).
$$

In the original resolvent pairing,
$$
\boxed{
\begin{aligned}
\|[W]\|_{\mathcal K/(D+\kappa)\operatorname{span}\{Y\}}^2
&=M(\kappa)-\frac{|c_Y|^2}{a_Y},\\
R&=R_{\mathrm{can}}+(\alpha_Y-1)(D+\kappa)Y,\\
\langle R,(D+\kappa)^{-1}R\rangle
&=\|[W]\|^2+a_Y|\alpha_Y-1|^2.
\end{aligned}}
$$

The final term retains the exact primitive $(\alpha_Y-1)Y$ and its energy. Both nonnegative terms receive the proved residual bound. This is the quantitative cohomological calculation underlying the response certificate, with the full minimum-section correction retained.

### Return to the original physical state

Let
$$
h_\kappa=(D+\kappa)^{-1}W,
\qquad
\Phi=\psi\bigl(\mathsf J(F-\langle F\rangle_\rho)+h_\kappa\bigr).
$$
This is a nonzero physical form-domain vector perpendicular to the actual vacuum. Its original norm and energy are exactly
$$
\|\Phi\|^2=G+\|h_\kappa\|_\rho^2,
$$
$$
q_{H-E_0}(\Phi,\Phi)
=K_0-M(\kappa)-\kappa\|h_\kappa\|_\rho^2.
$$
Both mixed energy entries are included in this equality.

The verified intervals give
$$
\boxed{
(3-5\cdot10^{-13})\kappa
<
\frac{q_{H-E_0}(\Phi,\Phi)}{\|\Phi\|^2}
<
(3+5\cdot10^{-13})\kappa.
}
$$
The inclusion of $\operatorname{span}\{\Phi\}$ into the full centered physical form domain gives
$$
\Delta_L\le
\frac{q_{H-E_0}(\Phi,\Phi)}{\|\Phi\|^2}
$$
by the exact variational infimum. The lower endpoint displayed for this particular state is retained at that scope.

## Verification and workbench delivery

The final verifier passes **134 exact checks and 12 false-formula controls**, including the corrected section identity and the variational direction. Ordinary Python, optimized Python, fresh copied-source runs, and fresh patch application produced matching results. The unchanged parent checker also passed against its original receipt. The executable checks cover the quaternion identities, Haar integrals, original graph counts, and rational evaluation of the error bounds; the analytical arguments are supplied as written proofs for independent review.

[Complete verification record](sandbox:/mnt/data/yang_mills_actual_loop_moments_verification.json)

The patch adds the proof, verifier, receipt, execution record, and mathematical checkpoint, and updates `CURRENT.md` against the verified PR6 head `e98b2c3af77f66fb1c1396143ca53daef586404f`. PR6 remains open at that revision.  No new remote PR was opened: this session’s exposed GitHub actions provide reads and searches but no write action. The attached package includes the tested patch and its proposed PR description.

**The completed advance is actual interacting-vacuum moment and response control, together with all-coupling control of the derivative source.** The physical zero-shift response and a uniform positive continuum mass lower bound remain unevaluated. The narrow certificate stays on its specified large-$g$ domain; the all-coupling estimates retain the full growth factors along the existing continuum path.
