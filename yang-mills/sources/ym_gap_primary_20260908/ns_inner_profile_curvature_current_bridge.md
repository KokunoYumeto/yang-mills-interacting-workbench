# A source-specific inner-profile bridge from Navier–Stokes to Yang–Mills curvature and current

8 September 2026.

This article calculates the curvature, conserved current, lattice links, and magnetic-energy limit obtained from the specific concentrating flow described in OpenAI's *Finite time blowup for Navier–Stokes*. It proves the displayed transfer identities and estimates in full. It does not independently prove the existence of that external Navier–Stokes flow or certify the manuscript's complete analytic or formal proof. Statements about the supplied flow are explicitly tied to the manuscript passages identified below.

The retained inner swirl gives more information than bounded fluid \(L^2\) norm and unbounded speed alone. Its circulation forces instantaneous spatial enstrophy to diverge, while the fluid energy identity makes the time integral of that enstrophy finite. A fixed-spatial-point time derivative forces a stronger electric-curvature divergence. The resulting \(SU(2)\) current is necessarily singular even though the fluid force is smooth. These are statements about the displayed sourced classical connection, not a quantum vacuum spectral-gap conclusion.

## 1. Public source identity, versions, and mathematical inputs

The primary source is OpenAI, *Finite time blowup for Navier–Stokes*, announced on 8 September 2026 in [the official release](https://openai.com/index/navier-stokes-solution/). The announcement links [the manuscript PDF](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf) and [the NavierStokesAndEuler source repository](https://github.com/openai/NavierStokesAndEuler). A precise repository revision is [commit 8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538); no correspondence between every manuscript assertion and that revision's complete dependency graph is asserted here.

The same PDF URL has supplied two distinct versions. The page locators below identify them by cryptographic hash, not merely by URL:

| Version | PDF pages | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| \(P_{165}\) | 165 | 2,955,931 | 8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81 |
| \(P_{166}\) | 166 | 2,959,204 | 0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f |

The primary derivation used \(P_{165}\). The theorem, similarity coordinates, retained derivative estimates, correction absence in the inner region, localization and full force, energy estimate, and viscosity map were also checked in \(P_{166}\). Those selected passages display the same specific mathematical inputs used here. This limited statement is not an assertion of mathematical equivalence of the complete versions. The later historical discussion on pages 2–3 concerns additional preceding work; the checked Theorem 1.1 still uses the ordinary Laplacian with every fixed positive viscosity.

| Mathematical input | Primary location in \(P_{165}\) | Checked location in \(P_{166}\) |
| --- | --- | --- |
| Positive viscosity, zero initial velocity, smooth compact force, compact support, endpoint norms | Theorem 1.1, p. 1 | [Theorem 1.1, p. 1](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=1) |
| Similarity coordinates, positive swirl, regularity at the axis | §3.1, (3.2), pp. 7–8 | [§3.1, pp. 7–8](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=7) |
| Local potential representation, full residual, terminal regularity away from the singular point | Theorem 3.1, (3.3)–(3.6), pp. 14–16 | [Theorem 3.1, pp. 15–16](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=15) |
| Summed background, differentiated retained-profile estimate, summation-cutoff contribution | Lemma 5.4 and Proposition 5.5, (5.34)–(5.46), pp. 57–61 | [Proposition 5.5 and its proof, pp. 60–61](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=60) |
| Actual local field and absence of annular corrections in the inner region | Proposition 9.9, (9.21), pp. 114–116 | [Proposition 9.9, Step 5, p. 116](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=116) |
| Potential-first localization, zero initial interval, full force and pressure-divergence term | Proposition 10.1, (10.1)–(10.5), pp. 117–118 | [Proposition 10.1 and (10.5), pp. 117–118](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=117) |
| Compatible terminal force jets and smooth compact extension | Lemmas 10.2–10.3, pp. 118–120 | [Lemma 10.2, p. 118](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=118), [Lemma 10.3, p. 120](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=120) |
| Exact energy identity and integrated dissipation | Lemma 10.4, (10.13)–(10.14), p. 121 | [Lemma 10.4, p. 121](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=121) |
| Blowup path and viscosity rescaling with unchanged terminal time | (10.20)–(10.23), p. 124 | [(10.20)–(10.23), p. 124](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=124) |

Page links resolve the live PDF URL; the two hashes specify which versions the locators describe. Source equation numbers such as (5.42) below refer to the manuscript; section-numbered equations such as (4.7) are proved in this article. The notation \(E=E_0\) denotes the same leading azimuthal profile, and \(u=u_1\) denotes the same supplied viscosity-one field. Neither identity renames a different field as the source field.

## 2. The new field, including the actual force and terminal data

For the manuscript's velocity \(u_\nu\), pressure \(p_\nu\), and force \(f_\nu\), retain the equation
\[
 \partial_tu_\nu+(u_\nu\cdot\nabla)u_\nu-\nu\Delta u_\nu
       +\nabla p_\nu=f_\nu,\qquad
 \nabla\cdot u_\nu=0,\qquad \nu>0.
 \tag{2.1}
\]
The stated whole-space data are
\[
 u_\nu(\cdot,0)=0,\quad
 f_\nu\in C_c^\infty(\mathbb R^3\times(0,\infty);\mathbb R^3),\quad
 \operatorname{supp}u_\nu(t)\cup\operatorname{supp}p_\nu(t)\subset K_\nu,
 \tag{2.2}
\]
where \(K_\nu\) is fixed and compact and \(u_\nu,p_\nu\) are smooth for \(0\le t<1\). The manuscript actually makes \(u_\nu,p_\nu\) zero on an initial time interval. Its conclusion is
\[
 \sup_{0\le t<1}\|u_\nu(t)\|_2<\infty,\qquad
 \limsup_{t\uparrow1}\|u_\nu(t)\|_\infty=\infty.
 \tag{2.3}
\]
The source's path asymptotic is stronger than the abstract limsup statement. No stronger endpoint conclusion is attributed to Theorem 1.1 merely from its wording.

The actual local field at viscosity one is the source's locally finite sum
\[
\begin{aligned}
 \mathcal A_{\rm fl}
   &=\mathcal A_0+\sum_{j\ge1}\chi(a_jq)\mathcal A_j,\\
 B_{\rm fl}
   &=B_0+\sum_{j\ge1}\chi(a_jq)B_j,\\
 p_{\rm loc}
   &=p_0+\sum_{j\ge1}\chi(a_jq)p_j,\qquad
 u_{\rm loc}=\operatorname{curl}\mathcal A_{\rm fl}+B_{\rm fl}e_\theta.
\end{aligned}
\tag{2.4}
\]
Here the identity renaming \(\mathcal A_{\rm fl}=A_{\rm source}\) avoids confusing the fluid vector potential with the gauge connection below; no value or coefficient changes. The coefficient indices \(j\) are the source's correction stages. With its cutoff \(c_{\rm cut}(x,t)=\chi_x(x)\chi_t(t)\),
\[
 u=\operatorname{curl}(c_{\rm cut}\mathcal A_{\rm fl})
                +c_{\rm cut}B_{\rm fl}e_\theta
   =c_{\rm cut}u_{\rm loc}+\nabla c_{\rm cut}\times\mathcal A_{\rm fl},
 \qquad p=c_{\rm cut}p_{\rm loc}.
 \tag{2.5}
\]
The complete preterminal force is
\[
 f=\partial_tu+(u\cdot\nabla)u-\Delta u+\nabla p.
 \tag{2.6}
\]
This includes all wave interactions, stress corrections, and cutoff derivatives. It is not the residual of the leading profile alone. Lemmas 10.2–10.3 claim compatible limits of every mixed derivative of (2.6), followed by a smooth compact-time extension. Near the origin at the terminal time, the force residual is flat to every order; its extension elsewhere retains its generally nonzero terminal jets. One cannot replace the extension by zero unless those jets vanish there.

The pressure is part of this construction. Taking the divergence of (2.1) gives exactly
\[
 -\Delta p_\nu
 =\sum_{i,j}\partial_i\partial_j(u_{\nu,i}u_{\nu,j})
                  -\nabla\cdot f_\nu.
 \tag{2.7}
\]
The source explicitly allows nonzero divergence of the force. Imposing \(\nabla\cdot f_\nu=0\), removing pressure, or replacing (2.6) by a leading stress changes the stated field.

The exact viscosity map in (10.22) is
\[
\begin{aligned}
 u_\nu(x,t)&=\sqrt\nu\,u(x/\sqrt\nu,t),&
 p_\nu(x,t)&=\nu p(x/\sqrt\nu,t),\\
 f_\nu(x,t)&=\sqrt\nu\,f(x/\sqrt\nu,t),&
 K_\nu&=\sqrt\nu K.
\end{aligned}
\tag{2.8}
\]
Its inverse is \(u(y,t)=\nu^{-1/2}u_\nu(\sqrt\nu y,t)\), with analogous pressure and force inverses. Direct differentiation verifies (2.1): each momentum term is \(\sqrt\nu\) times its viscosity-one counterpart at \(y=x/\sqrt\nu\). Time and the terminal value \(t=1\) are unchanged. In particular,
\[
\begin{aligned}
 \|u_\nu(t)\|_2^2&=\nu^{5/2}\|u(t)\|_2^2,&
 \|\partial_tu_\nu(t)\|_2^2&=\nu^{5/2}\|\partial_tu(t)\|_2^2,\\
 \|\operatorname{curl}u_\nu(t)\|_2^2
   &=\nu^{3/2}\|\operatorname{curl}u(t)\|_2^2.
\end{aligned}
\tag{2.9}
\]
Each identity follows by retaining the amplitude/derivative factors and \(dx=\nu^{3/2}dy\). The unit-viscosity source presentation is used below only with these explicit maps to every fixed positive \(\nu\).

## 3. What endpoint norms alone imply, and what they do not

The two norm assertions in (2.3) do not by themselves force spatial enstrophy to diverge. For an exact demonstration, fix any nonzero divergence-free \(v\in C_c^\infty(\mathbb R^3;\mathbb R^3)\), for example a nonzero curl of a compactly supported smooth vector potential. For \(0<\varepsilon<1\) set
\[
 v_\varepsilon(x)=\varepsilon^{-1/3}v(x/\varepsilon).
\]
Changing variables and differentiating give
\[
 \|v_\varepsilon\|_\infty=\varepsilon^{-1/3}\|v\|_\infty\to\infty,\quad
 \|v_\varepsilon\|_2^2=\varepsilon^{7/3}\|v\|_2^2\to0,\quad
 \|\operatorname{curl}v_\varepsilon\|_2^2
      =\varepsilon^{1/3}\|\operatorname{curl}v\|_2^2\to0.
 \tag{3.1}
\]
The supports remain in one compact set. These are smooth spatial fields, not a Navier–Stokes solution with the manuscript's smooth force. Formula (3.1) proves the exact failure of the proposed norm-only inference.

For the actual source field, the PDE and support give further information. Put
\[
 \mathcal F_\nu(t)=\int_0^t\|f_\nu(s)\|_2\,ds.
\]
Multiplying (2.1) by \(u_\nu\), integrating in space, using compact support, and integrating by parts yields
\[
 \frac12\frac d{dt}\|u_\nu(t)\|_2^2
       +\nu\|\nabla u_\nu(t)\|_2^2
       =\langle f_\nu(t),u_\nu(t)\rangle.
 \tag{3.2}
\]
Transport is the integral of \(\nabla\cdot(u_\nu|u_\nu|^2/2)\); pressure integrates to \(-\int p_\nu\nabla\cdot u_\nu=0\). Thus both terms have been treated, not omitted. Dividing by \((\|u_\nu\|_2^2+\delta^2)^{1/2}\), dropping the nonnegative dissipation, integrating from zero datum, and letting \(\delta\downarrow0\) gives \(\|u_\nu(t)\|_2\le\mathcal F_\nu(t)\). Integrating (3.2) once more consequently gives
\[
 \|u_\nu(t)\|_2^2
     +2\nu\int_0^t\|\nabla u_\nu(s)\|_2^2ds
       \le \mathcal F_\nu(t)^2.
 \tag{3.3}
\]
For each smooth compactly supported vector field,
\[
 \int|\operatorname{curl}u|^2
   =\sum_{i,j}\int(\partial_i u_j)^2
        -\sum_{i,j}\int\partial_i u_j\,\partial_j u_i
   =\int|\nabla u|^2-\int(\nabla\cdot u)^2.
 \tag{3.4}
\]
The second equality integrates twice by parts in the last sum. Hence the divergence-free source field has the exact equality of enstrophy and squared gradient norm. By (3.3), monotone convergence, and compact smooth \(f_\nu\),
\[
 \int_0^1\|\operatorname{curl}u_\nu(t)\|_2^2dt
 \le \frac{\mathcal F_\nu(1)^2}{2\nu}<\infty.
 \tag{3.5}
\]
This does not bound the instantaneous supremum of enstrophy.

## 4. Source-specific magnetic curvature divergence from circulation

Here one can go beyond (2.3) because the manuscript retains the inner swirl uniformly, including the summation corrections.

Keep the source constants and coordinates
\[
 \tau=1-t,\quad A=\tfrac12+h,\quad D=\tfrac12-h,\quad 0<h<1/100,
\]
\[
 \tau=q(1-\eta^2),\qquad z=q^D\eta,\qquad r^2=2qX,\qquad |\eta|<1.
 \tag{4.1}
\]
The full inner field, after the source's corrections and before a cutoff that equals one there, obeys
\[
 u_\theta(r,\theta,z,t)
       =q^{-A}\big(E(X,\eta)+R(q,X,\eta)\big),\qquad
 R=O(q^{2h}).
 \tag{4.2}
\]
The estimate and every fixed composition of \(q\partial_q,\partial_X,\partial_\eta\) are uniform on any fixed inner rectangle bounded away from \(X=0\); this is (5.42), choosing \(X_{\rm lo}\) smaller than that rectangle. All annular corrections vanish in the fixed inner similarity region by Proposition 9.9 Step 5. The local field is therefore axisymmetric on that region even though the complete field need not be axisymmetric. The compact localization equals the local field throughout each of the shrinking regions used below for all sufficiently small \(\tau\).

Choose a fixed \(X_*\) in that inner region. Its leading value satisfies \(e_0=E(X_*,0)>0\). Smoothness permits a fixed \(0<\eta_*<1\) small enough that
\[
 E(X_*,\eta)\ge e_0/2\qquad (|\eta|\le\eta_*).
\]
Uniformity in (4.2) then gives, for all sufficiently small \(\tau>0\),
\[
 u_\theta\big(\sqrt{2X_*q},\theta,q^D\eta,1-\tau\big)
       \ge e_*q^{-A},\qquad e_*:=e_0/4,\qquad
 q=\frac{\tau}{1-\eta^2}.
 \tag{4.3}
\]
At each fixed \(z\) corresponding to this \(\eta\), let \(D_z\) be the horizontal disk with radius \(r(z)=\sqrt{2X_*q}\). Stokes's formula in the original right-handed Cartesian orientation gives
\[
 \int_{D_z}(\operatorname{curl}u)_3\,dx_1dx_2
       =\oint_{\partial D_z}u\cdot d\ell
       =2\pi r(z)u_\theta(r(z),z,t).
 \tag{4.4}
\]
The field is smooth on the full disk, including the axis. Cauchy–Schwarz on that disk of area \(\pi r(z)^2\) proves
\[
 \int_{D_z}|(\operatorname{curl}u)_3|^2dx_1dx_2
 \ge 4\pi\,u_\theta(r(z),z,t)^2
 \ge4\pi e_*^2q^{-2A}.
 \tag{4.5}
\]
No derivative approximation or replacement by the leading vorticity occurs in this inequality.

The exact axial coordinate and its derivative at fixed \(\tau\) are
\[
 z(\eta)=\tau^D\eta(1-\eta^2)^{-D},\qquad
 \frac{dz}{d\eta}
   =\tau^D(1-2h\eta^2)(1-\eta^2)^{-D-1}>0.
 \tag{4.6}
\]
Integrating (4.5) over these disjoint disk slices and bounding the full enstrophy below by its axial component gives
\[
\begin{aligned}
 \|\operatorname{curl}u(1-\tau)\|_2^2
 &\ge C_\Omega\,\tau^{D-2A}
       =C_\Omega\,\tau^{-1/2-3h},\\
 C_\Omega
 &:=4\pi e_*^2\int_{-\eta_*}^{\eta_*}
       (1-2h\eta^2)(1-\eta^2)^{\,2A-D-1}d\eta>0.
\end{aligned}
\tag{4.7}
\]
The coefficient is finite and strictly positive because the integration interval is a compact subset of \((-1,1)\) and \(1-2h\eta^2>0\). Thus, for the manuscript's stated field, the instantaneous full enstrophy tends to infinity, not merely along a subsequence. Restoring the original positive viscosity gives
\[
 \|\operatorname{curl}u_\nu(1-\tau)\|_2^2
       \ge \nu^{3/2}C_\Omega\,\tau^{-1/2-3h}.
 \tag{4.8}
\]
This is compatible with (3.5): \(1/2+3h<1\), so the lower-bound power is integrable in time. No full enstrophy upper bound with this power is asserted; the annular oscillations remain present. Likewise, the source's vanishing leading-core kinetic energy does not assert that the entire fluid energy tends to zero.

## 5. The mapped electric curvature also grows

The same source estimates give a fixed-Cartesian-time derivative, as required for \(F_{0i}\). Differentiating (4.1) while holding the spatial point fixed gives, with \(L(\eta)=1-2h\eta^2\),
\[
 q_t=-L^{-1},\qquad
 \eta_t=\frac{D\eta}{qL},\qquad
 X_t=\frac{X}{qL},
\]
\[
 \partial_t=\frac1{qL}
           (-q\partial_q+X\partial_X+D\eta\partial_\eta).
 \tag{5.1}
\]
This is not the derivative along the moving growth path. Since \(e_\theta\) is independent of time at a fixed spatial point, it gives the actual azimuthal component of \(\partial_tu\).

Define the retained leading coefficient
\[
 \mathcal H(X,\eta)
  :=\frac{AE(X,\eta)+X E_X(X,\eta)+D\eta E_\eta(X,\eta)}
                {L(\eta)}.
 \tag{5.2}
\]
Equations (4.2), (5.1), and the three differentiated bounds for \(R\) give
\[
 \partial_tu_\theta
    =q^{-A-1}\big(\mathcal H(X,\eta)+O(q^{2h})\big)
 \tag{5.3}
\]
uniformly on a fixed inner rectangle. Explicitly the normalized remainder is
\[
 L^{-1}\big(AR-q\partial_qR+X\partial_XR+D\eta\partial_\eta R\big),
\]
so every term has the asserted order.

There is a point \(X_0\) in the inner interval with \(\mathcal H(X_0,0)\ne0\). If there were none, \(X E_X(X,0)+A E(X,0)=0\) on that whole interval. Differentiating \(X^A E(X,0)\) shows it is constant, whence \(E(X,0)=C X^{-A}\). But the source's smooth axis condition says \(E(X,0)=O(\sqrt X)\) at zero. Since \(A>0\), it forces \(C=0\), contradicting \(E>0\) for \(X>0\).

Choose a closed rectangle
\[
 \mathcal R=[X_0^-,X_0^+]\times[-\eta_0,\eta_0]
 \Subset (0,X_a)\times(-1,1)
\]
inside the common inner region and a constant \(h_*>0\) such that \(|\mathcal H|\ge h_*\) there. For sufficiently small \(\tau\), (5.3) gives
\[
 |\partial_tu_\theta|\ge (h_*/2)q^{-A-1}.
 \tag{5.4}
\]
At fixed \(\tau\), the full volume element is
\[
 dx=r\,dr\,d\theta\,dz
   =q\,\tau^D L(\eta)(1-\eta^2)^{-D-1}
                         dX\,d\theta\,d\eta.
 \tag{5.5}
\]
Indeed \(r\,dr=q\,dX\) on a fixed \(z\) slice and (4.6) gives the other factor; the cross term from differentiating \(r\) in \(\eta\) vanishes in the Jacobian determinant. Integrating (5.4) on \(\mathcal R\times S^1\) therefore proves
\[
\begin{aligned}
 \|\partial_tu(1-\tau)\|_2^2
   &\ge C_{\dot u}\,\tau^{D-2A-1}
        =C_{\dot u}\,\tau^{-3/2-3h},\\
 C_{\dot u}
   &:=\frac{\pi h_*^2}{2}(X_0^+-X_0^-)
        \int_{-\eta_0}^{\eta_0}
          L(\eta)(1-\eta^2)^{\,2A-D}d\eta>0.
\end{aligned}
\tag{5.6}
\]
Consequently
\[
 \|\partial_tu_\nu(1-\tau)\|_2^2
   \ge \nu^{5/2}C_{\dot u}\tau^{-3/2-3h},\qquad
 \int_0^1\|\partial_tu_\nu(t)\|_2^2dt=\infty.
 \tag{5.7}
\]
The last conclusion follows by integrating the nonintegrable lower bound. It does not contradict the fluid kinetic-energy identity, which controls \(\int|\nabla u_\nu|^2\), not \(\int|\partial_tu_\nu|^2\).

## 6. Exact SU(2) connection, curvature, and full current

Retain the fixed bridge constants \(c>0\), \(g>0\), \(\lambda\in\mathbb R\setminus\{0\}\), the source's original Cartesian space and time, and
\[
 X^0=ct,\quad X^i=x^i,\quad
 T=-i\sigma_3/2,\quad -2\operatorname{tr}(T^2)=1,\quad
 A_0=0,\quad A_i=\lambda u_{\nu,i}T.
 \tag{6.1}
\]
The inverse on this connection image is
\[
 u_{\nu,i}(x,t)=-2\operatorname{tr}(T A_i(ct,x))/\lambda.
\]
This inverse is specific to the displayed gauge representative. With \(u\) in length/time units and \(A_i\) in inverse-length units, \(\lambda\) has time/length-squared units. The new NS source's similarity time and length units stay fixed; there is no additional dilation or change of \(g\).

All commutators \([A_\mu,A_\nu]\) vanish by the common \(T\) factor, as do \([A_\mu,F_{\alpha\beta}]\). Substituting in the full curvature formula, rather than dropping terms from a general connection, yields exactly
\[
 F_{0i}=\lambda c^{-1}\partial_tu_{\nu,i}T,\qquad
 F_{ij}=\lambda(\partial_i u_{\nu,j}-\partial_j u_{\nu,i})T.
 \tag{6.2}
\]
The two nonnegative raw curvature diagnostics in the original spatial measure are therefore
\[
\begin{aligned}
 \mathcal K_B(t)
   &:=-2\int\sum_{i<j}\operatorname{tr}(F_{ij}^2)dx
        =\lambda^2\|\operatorname{curl}u_\nu(t)\|_2^2,\\
 \mathcal K_E(t)
   &:=-2\int\sum_i\operatorname{tr}(F_{0i}^2)dx
        =\lambda^2c^{-2}\|\partial_tu_\nu(t)\|_2^2.
\end{aligned}
\tag{6.3}
\]
Each is invariant under a smooth gauge transform because \(F^h=h^{-1}Fh\) and cyclicity of trace preserves every quadratic term. The curvature transformation follows by applying the product rule to \(d+A^h=h^{-1}(d+A)h\), then squaring. Equations (3.5), (4.8), and (5.7) give
\[
\begin{aligned}
 \mathcal K_B(1-\tau)
   &\ge\lambda^2\nu^{3/2}C_\Omega\tau^{-1/2-3h}\longrightarrow\infty,
 &\int_0^1\mathcal K_B(t)dt
   &\le\frac{\lambda^2}{2\nu}\mathcal F_\nu(1)^2<\infty,\\
 \mathcal K_E(1-\tau)
   &\ge\frac{\lambda^2\nu^{5/2}}{c^2}
                 C_{\dot u}\tau^{-3/2-3h}\longrightarrow\infty,
 &\int_0^1\mathcal K_E(t)dt&=\infty.
\end{aligned}
\tag{6.4}
\]
Spacetime integration in \(X^0\) multiplies these time integrals by \(c\). These are nonnegative component norms; no conclusion about cancellation in the indefinite Lorentzian action follows from them.

For the original Minkowski metric \(\operatorname{diag}(-1,1,1,1)\) and convention \(D^\mu F_{\mu\nu}=g^2j_\nu\), (6.2) gives
\[
 j_0=-\frac{\lambda}{g^2c}\partial_t(\nabla\cdot u_\nu)T=0,\qquad
 j_i=\frac{\lambda}{g^2}
             \left(\Delta u_{\nu,i}-c^{-2}\partial_t^2u_{\nu,i}\right)T.
 \tag{6.5}
\]
For example the spatial contraction is
\(\sum_k\partial_kF_{ki}
 =\lambda(\Delta u_{\nu,i}-\partial_i\nabla\cdot u_\nu)T\);
the time contraction is \(-\partial_0F_{0i}
 =-\lambda c^{-2}\partial_t^2u_{\nu,i}T\).
Thus all index signs are explicit.

Writing \(w=\partial_tu_\nu\), differentiating the full positive-viscosity equation (2.1) gives
\[
 j_i=\frac{\lambda}{g^2}\left[
 \Delta u_{\nu,i}
 -\frac1{c^2}\left(
 \nu\Delta w_i-\sum_k w_k\partial_k u_{\nu,i}
              -\sum_k u_{\nu,k}\partial_k w_i
              -\partial_i\partial_t p_\nu+\partial_t f_{\nu,i}
                       \right)\right]T.
 \tag{6.6}
\]
No smoothness of \(f_\nu\) cancels the other displayed derivatives. Conservation holds exactly:
\[
 D^\nu j_\nu=\sum_i\partial_i j_i
 =\frac{\lambda}{g^2}
       (\Delta-c^{-2}\partial_t^2)(\nabla\cdot u_\nu)T=0.
\]
This is a classical, reducible SU(2) connection satisfying a sourced equation. It does not contain the full noncommuting quantum dynamics. A different non-Abelian encoding would have to retain its own \([A,A]\) and \([A,F]\) terms; they cannot be equated with fluid transport without an additional proved identity.

## 7. The mapped current is necessarily singular despite smooth fluid forcing

Here the new source gives more than the earlier statement “the current is generally nonzero.” Write \(j_i=J_iT\) with real \(J=(J_1,J_2,J_3)\). Equation (6.5) is exactly
\[
 \partial_t^2u_\nu-c^2\Delta u_\nu
        =-\frac{g^2c^2}{\lambda}J.
 \tag{7.1}
\]
The source velocity vanishes on an initial time interval, so both wave Cauchy data \(u_\nu(0)\) and \(\partial_tu_\nu(0)\) are zero. On each fixed \([0,T]\), \(T<1\), all terms are smooth and compactly supported in space. The three-dimensional wave representation is
\[
 u_\nu(t,x)
 =-\frac{g^2c^2}{\lambda}
       \int_0^t\frac{t-s}{4\pi}
             \int_{S^2}J(s,x+c(t-s)\omega)\,d\omega\,ds.
 \tag{7.2}
\]
For verification, the spherical mean \(M_rf(x)=(4\pi)^{-1}\int_{S^2}f(x+r\omega)d\omega\) satisfies
\(\partial_r(r^2\partial_rM_rf)=r^2M_r\Delta f\):
differentiate the ball integral of \(\Delta f\), use the divergence theorem to express it as the outward normal derivative integral, and divide by \(4\pi\). Hence \(tM_{ct}f\) solves the wave equation with initial displacement zero and initial velocity \(f\). Time integration supplies the inhomogeneous equation and zero data in (7.2). The difference from \(u_\nu\) solves the homogeneous wave equation with zero data; multiplying by its time derivative and integrating proves conservation of its zero wave energy, and therefore equality. These operations are valid on each preterminal compact interval.

Since the sphere has area \(4\pi\), (7.2) implies
\[
 \|u_\nu(t)\|_\infty
 \le\frac{g^2c^2}{|\lambda|}
        \int_0^t(t-s)\|J(s)\|_\infty\,ds
 \le\frac{g^2c^2}{|\lambda|}
        \int_0^1(1-s)\|J(s)\|_\infty\,ds.
 \tag{7.3}
\]
The manuscript's unbounded speed therefore forces
\[
 \int_0^1(1-s)\|J(s)\|_\infty ds=\infty.
 \tag{7.4}
\]
In particular \(J\) is not identically zero, is not bounded through the terminal time, and cannot have a smooth extension on a compact spacetime neighborhood containing its common spatial support. Smooth gauge transformations cannot remove this norm obstruction: \(-2\sum_i\operatorname{tr}(j_i^2)=|J|^2\) is invariant. Thus this precise encoding necessarily introduces a singular gauge current, although the fluid force is smooth. It is not a source-free Yang–Mills classical solution.

## 8. Original lattice magnetic coefficient and quantum-state limits

Retain the finite-lattice coefficients
\[
 b=\frac1{2g^2a},\qquad \kappa=\frac{2g^2}{a},\qquad a>0,
\]
and \(T=-i\sigma_3/2\). Here \(a\) is the spatial edge length, \(b\) multiplies the magnetic Wilson potential, and \(\kappa\) multiplies the electric Casimir. The following transport construction fixes the signed continuum-to-link map, its path order, and both endpoint actions.

Let \(e:[0,1]\to\mathbb R^3\) be an oriented edge, with source \(s(e)=e(0)\) and target \(t(e)=e(1)\), at a fixed regular time. Put \(a_e(\rho)=A_i(e(\rho))\dot e^i(\rho)\). Ordinary parallel transport of column vectors is the solution
\[
 \frac{dP(\rho)}{d\rho}=-a_e(\rho)P(\rho),\qquad P(0)=I,
 \qquad P_e=P(1).
 \tag{8.a}
\]
Because \(a_e\) is traceless and anti-Hermitian, differentiating \(P^\dagger P\) gives zero and differentiating \(\det P\) gives
\(-\operatorname{tr}(a_e)\det P=0\). Thus \(P(\rho)\in SU(2)\) at every parameter value.

The lattice link is the inverse transport
\[
 U_e:=P_e^{-1}.
 \tag{8.b}
\]
At intermediate parameter values its inverse \(U(\rho)=P(\rho)^{-1}\) satisfies
\[
 \frac{dU(\rho)}{d\rho}=U(\rho)a_e(\rho),\qquad U(0)=I.
 \tag{8.c}
\]
This is a right-multiplication differential equation. In general it is not the ordinary left-ordered transport with a positive sign.

For a smooth \(h:\mathbb R^3\to SU(2)\), use
\[
 A^h=h^{-1}Ah+h^{-1}dh.
\]
Differentiating
\[
 \widetilde P(\rho)
   =h(e(\rho))^{-1}P(\rho)h(s(e))
\]
and using \(\partial_\rho h^{-1}=-h^{-1}(\partial_\rho h)h^{-1}\) gives
\[
 \widetilde P'=
 -\big(h^{-1}a_eh+h^{-1}\partial_\rho h\big)\widetilde P,
 \qquad \widetilde P(0)=I.
\]
Uniqueness for this matrix differential equation therefore proves the exact endpoint formulas
\[
 P_e[A^h]=h(t(e))^{-1}P_e[A]h(s(e)),\qquad
 U_e[A^h]=h(s(e))^{-1}U_e[A]h(t(e)).
 \tag{8.d}
\]
The second law is the lattice vertex-gauge action in use here; the continuum-to-link map intertwines it with the specified connection-gauge action.

If \(e_1\) is traversed first and \(e_2\) second, with \(t(e_1)=s(e_2)\), continuation of the column equation gives
\[
 P_{e_2\circ e_1}=P_{e_2}P_{e_1},\qquad
 U_{e_2\circ e_1}=U_{e_1}U_{e_2}.
 \tag{8.e}
\]
For the reversed edge \(\bar e\), reparametrization and uniqueness give \(P_{\bar e}=P_e^{-1}\), hence \(U_{\bar e}=U_e^{-1}\). Thus the lattice link product is written in traversal order, with no reordering of noncommuting factors. For the positively oriented square based at \(x\) in the \(ij\)-plane it is
\[
 U_p=
 U_i(x)\,U_j(x+a\widehat e_i)\,
 U_i(x+a\widehat e_j)^{-1}\,U_j(x)^{-1}.
 \tag{8.f}
\]
Substitution of (8.d) cancels every intermediate endpoint factor in this actual order, leaving
\[
 U_p[A^h]=h(x)^{-1}U_p[A]h(x).
\]
Its trace is therefore gauge invariant.

For the specific Cartan connection (6.1), all values \(a_e(\rho)\) commute. Equations (8.a)–(8.c) then give the exact signed formulas
\[
 P_e=\exp\!\left(-\lambda T\int_eu_\nu\cdot dx\right),
 \qquad
 U_e=\exp\!\left(+\lambda T\int_eu_\nu\cdot dx\right).
 \tag{8.g}
\]
The distinction between \(P_e\) and \(U_e\) is not only a trace convention: it fixes the matrix, the circulation sign, and the endpoint action before taking any trace.
On the Cartan image the holonomy around an oriented plaquette is
\[
 U_p=e^{\vartheta_pT},\quad
 \vartheta_p=+\lambda\oint_{\partial p}u_\nu\cdot dx,\quad
 W_p=\operatorname{tr}U_p=2\cos(\vartheta_p/2).
 \tag{8.1}
\]
For a square of side \(a\) in the \(ij\) plane, Stokes and Taylor's formula at a fixed regular time give
\[
 \vartheta_p=+\lambda a^2
                (\partial_i u_{\nu,j}-\partial_j u_{\nu,i})+O(a^3),
 \qquad
 b(2-W_p)=\frac{\lambda^2a^3}{8g^2}
                (\partial_i u_{\nu,j}-\partial_j u_{\nu,i})^2+O(a^4).
 \tag{8.2}
\]
Indeed \(2-2\cos(\vartheta/2)=\vartheta^2/4+O(\vartheta^4)\). On a fixed box containing the compact support, uniform smoothness at that regular time bounds the remainders; summing the three orientations as a Riemann sum gives the exact limiting magnetic energy in this dictionary,
\[
 \mathcal E_B^{\rm project}(t)
 :=\lim_{a\downarrow0}\frac1{2g^2a}\sum_p(2-W_p[A(t)])
 =\frac{\lambda^2}{8g^2}
                  \|\operatorname{curl}u_\nu(t)\|_2^2.
 \tag{8.3}
\]
Thus this classical magnetic energy tends to infinity by (4.8), while its time integral is bounded by \(\lambda^2\mathcal F_\nu(1)^2/(16g^2\nu)\). Any positive electric-plus-magnetic curvature energy with the same fixed coefficients is also unbounded; (6.4) gives the separate electric growth before any choice of action normalization.

The order in (8.3) matters: \(a\downarrow0\) at each fixed \(t<1\). No uniform Taylor estimate as \(t\uparrow1\), no chosen relation \(a=a(t)\), and no quantum energy expectation is implicit. At a fixed finite lattice, \(0\le2-W_p\le4\) gives the exact bound \(0\le b\sum_p(2-W_p)\le4b\,\#\{p\}\), even for a highly concentrating classical connection. A simultaneous singular-time and lattice limit must therefore be justified independently.

Gauge-invariant physical observables can still be formed. With the actual lattice vacuum \(\psi\), measure \(\mu=\psi^2d\lambda_{\rm Haar}\), and a real smooth gauge-invariant observable \(O\), the centered state
\[
 v_O=(O-\mu(O))\psi
 \tag{8.4}
\]
is physical and vacuum-orthogonal, with raw squared norm \(\operatorname{Var}_\mu(O)\). This follows by integrating \(O-\mu(O)\) and using invariance of \(O,\psi\). It is an explicit map from a real gauge-invariant configuration observable to a physical vacuum-orthogonal vector.

However \(O(U[A(u_\nu(t))])\) is a value on one classical configuration. It does not determine \(\operatorname{Var}_\mu(O)\), the excitation form \(q_{H-E_0}[v_O]\), or their quotient over the full configuration space with the actual vacuum measure. Equations (4.8), (6.4), and (8.3) prove curvature and classical energy growth. They supply no nonzero raw physical sequence satisfying
\[
 v_n\perp\psi,\qquad
 \frac{q_{H-E_0}[v_n]}{\|v_n\|^2}\longrightarrow0.
 \tag{8.5}
\]
Nor does singularity of the sourced classical image contradict existence of source-free quantum fields, which need not be smooth classical configurations.

The manuscript's retained swirl transfers to a proved magnetic-curvature divergence, its time derivatives transfer to electric-curvature divergence, and its initial rest plus velocity growth forces a singular conserved gauge current. The source-free quantum-state and continuum spectral construction remain absent from this particular map.


