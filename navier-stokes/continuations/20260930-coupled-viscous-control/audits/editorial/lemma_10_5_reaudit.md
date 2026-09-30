# Re-audit and strengthening of the whole-space comparison lemma

## Source identity and scope

The source statement is Lemma 10.5 of *Finite Time Blowup for Navier–Stokes*, pp. 121–123 of the 166-page capture, SHA-256

\[
0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f.
\]

The line-by-line reading copy is the source-faithful independent transcription frozen at workbench commit

\[
e672c8021820af39df19eb0bb1fdfa5ceb990751,
\]

file “reconstruction/sections/pp121-126.tex,” lines 61–284. This note checks the argument as written, retains its pressure convention and all cutoff powers, and then proves a stronger comparison result. It does not alter the source or establish the earlier profile, correction, summation, localization, or force-extension constructions on which the source’s global singular solution depends.

The source proof cites the \(L^p\) boundedness of the Riesz transforms; the relevant human source is Elias M. Stein, *Singular Integrals and Differentiability Properties of Functions*, Princeton University Press, 1970. No novelty claim is made here.

## Statement proved

Let \(u,p\) and \(v,P\) be smooth solutions on \(\mathbb R^3\times[0,T]\) of the incompressible viscosity-one equation with the same force and the same initial velocity. Assume

\[
u,v\in L^\infty(0,T;L^2(\mathbb R^3)),\qquad
u\in L^\infty(0,T;L^6(\mathbb R^3)),\qquad
\|\nabla u(\,\cdot\,,t)\|_\infty\in L^1(0,T).
\tag{1}
\]

Then \(u=v\) on \(\mathbb R^3\times[0,T]\). In particular, the compact spatial support assumed for the reference field in the source lemma is not needed for the comparison step.

For the compactly supported reference field of the source, the expanding-cutoff error can be bounded by \(C_TR^{-4/3}\), which strengthens the displayed source bound \(C_TR^{-1}\).

## 1. Pressure-gradient recovery

Set

\[
w=v-u,\qquad \pi=P-p,\qquad
g_{ij}=v_iv_j-u_iu_j=w_iw_j+w_iu_j+u_iw_j,
\tag{2}
\]

and keep the convention

\[
(\operatorname{div}g)_i=\sum_{j=1}^3\partial_jg_{ij}.
\tag{3}
\]

If

\[
M=\sup_{0\le t\le T}\|w(t)\|_2,\qquad
U_2=\sup_{0\le t\le T}\|u(t)\|_2,
\tag{4}
\]

then Cauchy–Schwarz, component by component, gives

\[
\|g_{ij}(t)\|_1
\le \|w_i(t)\|_2\|w_j(t)\|_2
 \|w_i(t)\|_2\|u_j(t)\|_2
 \|u_i(t)\|_2\|w_j(t)\|_2.
\tag{5}
\]

Thus

\[
G:=\sup_{0\le t\le T}\sum_{i,j=1}^3\|g_{ij}(t)\|_1<\infty.
\tag{6}
\]

The exact difference equation is

\[
\partial_tw+\operatorname{div}g=\Delta w-\nabla\pi,
\qquad \operatorname{div}w=0.
\tag{7}
\]

Use the unitary Fourier transform with derivative multiplier \(i\xi_i\), and let \(R_i\) have multiplier \(i\xi_i/|\xi|\). Define

\[
\pi_*=\sum_{i,j=1}^3R_iR_jg_{ij}.
\tag{8}
\]

For every \(s>3/2\),

\[
\|\pi_*(t)\|_{H^{-s}}^2
\le (2\pi)^{-3}G^2
\int_{\mathbb R^3}(1+|\xi|^2)^{-s}\,d\xi<\infty.
\tag{9}
\]

The integral is finite at the origin and has radial exponent \(2-2s<-1\) at infinity. The multiplier in (8) is \(-\xi_i\xi_j/|\xi|^2\), so

\[
\Delta\pi_*=-\sum_{i,j=1}^3\partial_i\partial_jg_{ij}.
\tag{10}
\]

Taking divergence in (7) gives the same equation for \(\pi\), locally in distributions.

For \(a\in C_c^\infty(0,T)\), integration by parts in time in (7) yields the exact signs

\[
\int_0^T a\nabla\pi\,dt
=\Delta\int_0^T aw\,dt
+\int_0^T a'w\,dt
-\operatorname{div}\int_0^T ag\,dt.
\tag{11}
\]

The three terms on the right belong to \(H^{-2}\), \(L^2\), and \(H^{-3}\), respectively. The last inclusion follows from \(L^1\subset H^{-2}\) in three dimensions and one spatial derivative. Equation (9), with \(s=2\), also gives

\[
H_a:=\int_0^T a(\nabla\pi-\nabla\pi_*)\,dt\in H^{-3}(\mathbb R^3),
\qquad \Delta H_a=0.
\tag{12}
\]

The Fourier transform of each component of \(H_a\) is a weighted \(L^2\) function. The harmonic equation makes it vanish away from \(\{0\}\); a function supported on that measure-zero set is zero almost everywhere. Therefore \(H_a=0\). Testing against every time test function and every compact spatial test function proves

\[
\nabla\pi=\nabla\pi_*
\quad\text{on }\mathbb R^3\times(0,T).
\tag{13}
\]

This proves equality of pressure gradients. It neither identifies the scalar pressure gauges nor imposes a growth condition on \(P\).

## 2. The exact commutator and pressure-flux estimate

Choose \(\varphi\in C_c^\infty(\mathbb R^3)\) with \(0\le\varphi\le1\) and \(\varphi=1\) on the unit ball. For \(R\ge1\), retain the source definitions

\[
\varphi_R(x)=\varphi(x/R),\qquad
\chi_R=\varphi_R^8,
\tag{14}
\]

\[
E_R=\int_{\mathbb R^3}\chi_R|w|^2,\qquad
A_R=\left(\int_{\mathbb R^3}\chi_R|\nabla w|^2\right)^{1/2},\qquad
B_R=\|\varphi_R^4w\|_6.
\tag{15}
\]

The homogeneous Sobolev inequality and the product rule give

\[
B_R\le C_S\|\nabla(\varphi_R^4w)\|_2
\le C_S\left(A_R+4\|\nabla\varphi\|_\infty R^{-1}M\right).
\tag{16}
\]

The full distributional kernel of \(R_iR_j\) is

\[
\operatorname{pv}\frac{3y_iy_j-\delta_{ij}|y|^2}{4\pi|y|^5}
-\frac{\delta_{ij}}3\delta_0.
\tag{17}
\]

The local term cancels in a commutator. With \(a_R=\varphi_R^4\),

\[
a_R\pi_*=
\sum_{i,j}R_iR_j(a_Rg_{ij})
+\sum_{i,j}[a_R,R_iR_j]g_{ij}.
\tag{18}
\]

The nonlocal kernel in (17) is bounded by \(\pi^{-1}|y|^{-3}\), while

\[
|a_R(x)-a_R(y)|
\le \min\left\{4\|\nabla\varphi\|_\infty\frac{|x-y|}{R},1\right\}.
\tag{19}
\]

Consequently each commutator is majorized by convolution with

\[
K_R(y)=C|y|^{-3}\min\{|y|/R,1\}.
\tag{20}
\]

The complete radial calculation is

\[
\begin{aligned}
\|K_R\|_{4/3}^{4/3}
&=4\pi C^{4/3}\left[
R^{-4/3}\int_0^Rr^{-2/3}\,dr
+\int_R^\infty r^{-2}\,dr\right]\\
&=16\pi C^{4/3}R^{-1}.
\end{aligned}
\tag{21}
\]

Young’s convolution inequality therefore gives

\[
\left\|\sum_{i,j}[a_R,R_iR_j]g_{ij}\right\|_{4/3}
\le C G R^{-3/4}.
\tag{22}
\]

Let

\[
U_6=\sup_{0\le t\le T}\|u(t)\|_6.
\tag{23}
\]

The first sum in (18) satisfies

\[
\|\varphi_R^4w_iw_j\|_{3/2}\le B_RM,
\tag{24}
\]

\[
\|\varphi_R^4w_iu_j\|_{3/2}\le MU_6,\qquad
\|\varphi_R^4u_iw_j\|_{3/2}\le U_6M.
\tag{25}
\]

The \(L^{3/2}\) boundedness of the Riesz transforms then yields

\[
\left\|\sum_{i,j}R_iR_j(a_Rg_{ij})\right\|_{3/2}
\le C M(B_R+2U_6).
\tag{26}
\]

For \(g\in L^1\), identity (18) follows by first cutting \(g\) off smoothly, applying the identity to the compact smooth approximants, and passing to the limit in \(H^{-s}\) for the Riesz terms and in \(L^{4/3}\) for the commutators. The compact factor \(a_Rg\) is also locally in every finite \(L^p\), since the solutions are smooth. Hence \(\pi_*\) is locally integrable.

Testing (13) against \(a(t)\chi_Rw\) gives, for almost every \(t\),

\[
\int_{\mathbb R^3}\pi w\cdot\nabla\chi_R
=\int_{\mathbb R^3}\pi_*w\cdot\nabla\chi_R.
\tag{27}
\]

There is no scalar-gauge term because

\[
\operatorname{div}(\chi_Rw)=w\cdot\nabla\chi_R.
\tag{28}
\]

The exact derivative

\[
\nabla\chi_R
=8R^{-1}\varphi_R^7(\nabla\varphi)(x/R)
\tag{29}
\]

pairs (18) with \(CR^{-1}\varphi_R^3w\). The required interpolations retain the cutoff powers:

\[
\|\varphi_R^3w\|_3
\le\|\varphi_R^2w\|_3
\le B_R^{1/2}M^{1/2},
\tag{30}
\]

\[
\|\varphi_R^3w\|_4
\le B_R^{3/4}M^{1/4}.
\tag{31}
\]

Indeed,

\[
\varphi_R^2|w|=(\varphi_R^4|w|)^{1/2}|w|^{1/2},
\qquad
\varphi_R^3|w|=(\varphi_R^4|w|)^{3/4}|w|^{1/4},
\tag{32}
\]

and Hölder gives (30)–(31). Combining (22), (26), and (29)–(31) gives the complete pressure-flux estimate

\[
\left|\int_{\mathbb R^3}\pi w\cdot\nabla\chi_R\right|
\le C R^{-1}M(B_R+2U_6)B_R^{1/2}M^{1/2}
+C G R^{-7/4}B_R^{3/4}M^{1/4}.
\tag{33}
\]

After uniform \(L^2\) and \(L^6\) bounds are placed in \(C_T\), this is exactly the source estimate (10.19).

## 3. Difference energy and the stronger remainder

Pairing (7) with \(\chi_Rw\), with all integrals over \(\mathbb R^3\), gives

\[
\begin{aligned}
\frac12E_R'+A_R^2
={}&-\int\chi_R(w\cdot\nabla)u\cdot w
+\frac12\int|w|^2\Delta\chi_R\\
&+\frac12\int|w|^2v\cdot\nabla\chi_R
+\int\pi w\cdot\nabla\chi_R.
\end{aligned}
\tag{34}
\]

Let

\[
K(t)=\|\nabla u(t)\|_{\mathrm{op},\infty}.
\tag{35}
\]

The first term on the right of (34) is bounded by \(K(t)E_R\). Since

\[
\Delta\varphi_R^8
=56\varphi_R^6|\nabla\varphi_R|^2
+8\varphi_R^7\Delta\varphi_R,
\tag{36}
\]

the Laplacian term is bounded by \(CR^{-2}M^2\).

If \(u\) is compactly supported and \(R\) is large enough that \(\chi_R=1\) near its support, then \(v=w\) on \(\operatorname{supp}\nabla\chi_R\). The transport flux is bounded by

\[
CR^{-1}\int\varphi_R^6|w|^3
\le CR^{-1}B_R^{3/2}M^{3/2}.
\tag{37}
\]

The exponent \(6\) is an inequality consequence of the actual exponent \(7\), since \(0\le\varphi_R\le1\).

For the stronger theorem, keep \(v=w+u\). The additional term obeys

\[
\begin{aligned}
CR^{-1}\int\varphi_R^7|w|^2|u|
&\le CR^{-1}U_6\|\varphi_R^{7/2}w\|_{12/5}^2\\
&\le CR^{-1}U_6B_R^{1/2}M^{3/2}.
\end{aligned}
\tag{38}
\]

The last step uses \(\varphi_R^{7/2}\le\varphi_R\) and the exact interpolation

\[
\|\varphi_Rw\|_{12/5}
\le B_R^{1/4}M^{3/4},
\qquad
\frac5{12}=\frac{1/4}{6}+\frac{3/4}{2}.
\tag{39}
\]

For \(0<\beta<2\), \(a>0\), and \(\delta>0\), direct maximization of \(ax^\beta-\delta x^2\) over \(x\ge0\) gives

\[
ax^\beta\le\delta x^2
+\left(1-\frac\beta2\right)
\left(\frac\beta2\right)^{\beta/(2-\beta)}
\delta^{-\beta/(2-\beta)}
a^{2/(2-\beta)}.
\tag{40}
\]

Substituting (16) into (33), (37), and (38) leaves only these positive powers of \(A_R\):

\[
CR^{-1}A_R^{3/2},\qquad
CR^{-1}A_R^{1/2},\qquad
CR^{-7/4}A_R^{3/4}.
\tag{41}
\]

Their remainders under (40) have powers

\[
R^{-4},\qquad R^{-4/3},\qquad R^{-14/5},
\tag{42}
\]

respectively. The terms obtained from the \(R^{-1}M\) part of (16), together with (36), have powers

\[
R^{-5/2},\qquad R^{-3/2},\qquad R^{-5/2},\qquad R^{-2}.
\tag{43}
\]

Choose the finitely many \(\delta\)’s in (40) so that their sum is at most \(1/2\). For \(R\ge1\), equations (34)–(43) yield

\[
\frac12E_R'+\frac12A_R^2
\le K(t)E_R+C_TR^{-4/3}.
\tag{44}
\]

The source’s \(C_TR^{-1}\) bound is therefore valid and non-sharp; (44) is the stronger bound.

If the initial velocities agree, then \(E_R(0)=0\). Gronwall’s inequality and \(K\in L^1(0,T)\) give

\[
E_R(t)\le
2C_TR^{-4/3}\int_0^t
\exp\left(2\int_s^tK(a)\,da\right)\,ds.
\tag{45}
\]

Every fixed spatial ball lies in the region where \(\chi_R=1\) once \(R\) is large. Letting \(R\to\infty\) in (45) shows that the \(L^2\) mass of \(w(t)\) on every fixed ball is zero. Smoothness gives \(w=0\) pointwise, including the time endpoints.

## 4. The \(L^6\) input follows from the source’s stronger regularity

If \(u(t)\in L^2\) and \(L=\|\nabla u(t)\|_{\mathrm{op},\infty}>0\), let \(a=|u(x,t)|\). On the ball of radius \(a/(2L)\) centered at \(x\),

\[
|u(y,t)|\ge a/2.
\tag{46}
\]

Therefore

\[
\|u(t)\|_2^2
\ge\frac{a^2}{4}\frac{4\pi}{3}\left(\frac{a}{2L}\right)^3
=\frac{\pi a^5}{24L^3}.
\tag{47}
\]

Taking the supremum over \(x\) gives

\[
\|u(t)\|_\infty
\le\left(\frac{24}{\pi}\right)^{1/5}
\|u(t)\|_2^{2/5}L^{3/5}.
\tag{48}
\]

Also,

\[
\|u(t)\|_6
\le\|u(t)\|_\infty^{2/3}\|u(t)\|_2^{1/3}.
\tag{49}
\]

If \(L=0\), the field is spatially constant and its \(L^2\) membership makes it zero. Thus the source’s smooth compactly supported reference field has the required uniform \(L^6\) bound on every interval \([0,T]\), \(T<1\).

## Audit disposition

![Cutoff geometry and exact remainder powers](../figures/lemma_10_5_cutoff_flux.png)

The figure records the exact proof flow from the transition annulus through the Riesz and commutator terms to the three Young remainders. Its reproducible source is `figures/lemma_10_5_cutoff_flux.py`; the proof locators are equations (14)–(45) above.

The written proof of Lemma 10.5 is mathematically sound under the constructed-field inputs stated there. The pressure-gradient argument does not require a hidden pressure-growth hypothesis. The calculation above proves two underclaims:

1. the source cutoff remainder \(C_TR^{-1}\) improves to \(C_TR^{-4/3}\);
2. compact support of the reference velocity can be replaced by the three conditions in (1).

These strengthen the comparison step only. They do not certify the profile existence theorem, annular correction sequence, infinite summation, localization, force extension, or the claimed singular solution.
