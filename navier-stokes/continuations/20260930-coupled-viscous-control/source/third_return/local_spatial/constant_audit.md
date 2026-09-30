# Independent local spatial constant audit

Scope: the actual third-steering interval of `tr:local` and the explicitly proved collar below. This audit does not assert existence of the entire third ramp, pulse, return, or hold. The original source quantities are retained: `A0 >= 1`, `nu = sqrt(A0)` is the time scale, `mu = lambda0 = ceil(nu/2)`, `Kj = mu lambda_hat_j`, physical diffusivity `d > 0`, `a = sin(s2)`, `s = s3 = L3 sigma1/sigma2`, `L = L3`, and `Gamma = sigma2 sin(s)`. In particular `q = sigma1/sigma2 = s/L` is an exact ratio, not a replacement of either physical scale by one.

Read-only sources inspected: `third_return/third_return_body.tex`, `third_transition/third_transition_body.tex`, `third_transition_spatial/third_transition_spatial_body.tex`, `finite_stage/third_growth_entry.tex`, `finite_stage/actual_viscous_entry.tex`, and the second-return bounds. Their hashes are recorded by the accompanying replay receipt. No main TeX source was edited by this audit.

## Cube geometry and actual collar

The closed cube in the proof of `tr:local` is

\[
 |U-U(t_1)|_\infty\leq1/128,
 \qquad U=(h,g,E,F,\omega,V).
\]

Its actual entry bounds imply throughout the cube

\[
 63/64<h<4,\quad11/16<g<6,\quad
 15/128<E<3,\quad7/128<F<4,
 \quad0<a\leq1/512,\quad0<s\leq a,
 \quad0<b=r_b\sin s<4\sin s\leq4a.
\]

For `D=h^2+a^2`,

\[
 D>(63/64)^2>15/16,
 \qquad D<16+1/512^2<17.
\]

For `R=(g^2+b^2)/D`, the exact bounds are

\[
 R>\frac{(11/16)^2}{17}=\frac{121}{4352}>\frac1{64},
 \qquad
 R<\frac{36+16/512^2}{15/16}<39.
\]

The coordinate formulas

\[
 x=(hg-ab)/D,\qquad y=(ag+hb)/D
\]

give `x,y>0`; the source proof gives the stronger lower bound `x>1/32`. The exact identity `x^2+y^2=R` now gives `x,y<sqrt(39)<7`.

The bound `M=32/sin(s)` on the complete older vector field is proved on this entire cube for `0 <= tau <= 1`, independently of the eventual trajectory. Consequently the identical first-exit proof extends to

\[
 \tau_*:=\frac{3\sin s}{16384}=\frac32\tau_0,
 \qquad t_*=t_1+\frac{3}{16384\sigma_2}.
\]

Indeed `tau_*<1` and displacement is strictly below

\[
 M\tau_*=\frac3{512}<\frac1{128}.
\]

This excludes a first cube exit on the enlarged interval; the smooth vector field with bounded first derivatives on a compact neighborhood then extends its unique solution through that interval. The positive-component margins used by `tr:local` are unchanged. All source trials coincide on this interval because the prescribed first ramp is independent of `m`. This is a proved collar of length `1/(16384 sigma2)` beyond the original endpoint `t1+1/(8192 sigma2)`.

## Material matrices, including both inverse bounds

The exact source formula `M2=R_(alpha-s*) [1,-(h-h0)/a;0,1]`, with `h0=cos(s2)`, gives

\[
 \|M_2\|,\|M_2^{-1}\|
 \leq1+|h-h_0|/a
 \leq1+(4-h_0)/a<2N,
 \quad N=1+(3-h_0)/a.
\]

Here `0<h0<=1`, and the cube bound `h>63/64` implies `|h-h0|<=4-h0`: the positive displacement is bounded by `4-h0`, while a negative displacement has magnitude at most `h0-63/64<1<=4-h0`. The final strict difference is exactly `1+(2-h0)/a>0`.

Set `Lmat=(zeta2 zeta3)` and `Lmat_b=Lmat(tb)`. Their determinants are both `-b`, and their exact material products are

\[
 M_3=\mathcal L^{-T}\mathcal L_b^T,
 \qquad M_3^{-1}=\mathcal L_b^{-T}\mathcal L^T.
\]

For a two by two matrix the Frobenius norm of its adjugate equals its Frobenius norm. Thus, using `1<=rb<=sqrt(10)`,

\[
 \|\mathcal L\|_F^2=D+R<56,
 \quad\|\mathcal L_b\|_F^2=r_b^2+1\leq11,
\]

\[
 \|M_3\|,\|M_3^{-1}\|
 <\frac{\sqrt{616}}{b}
 \leq\frac{\sqrt{616}}{\sin s}
 <\frac{32}{\sin s}=:\mathcal M_{\rm loc}.
\]

This is a bound on the complete physical material matrix and its inverse with both older vorticities retained.

## Existing source selection absorbs the enlarged bounds

Put `Y=log(lambda_hat1)`, `Q=Q2>=202`,

\[
 p=47Q/16-3,\quad r=(31Q+1)/16,
 \quad C_M=256C_2/(15\sqrt e),
 \quad C_2=e^9\sqrt{5\sqrt{10}/4}.
\]

The original scale bounds prove

\[
 \frac{16}{\sin s}
 \leq C_M\widehat\lambda_1^{(Q-1)/16},
 \quad N\leq C_N\widehat\lambda_1^{1/16},
 \quad\ell_2=\widehat\lambda_1^{-3}/\mu,
 \quad\ell_3=\widehat\lambda_2^{-3}/\mu.
\]

The saved `Y3=1+max(...)` contains both `log(4 CN CM)/p` and `log(sqrt(11) CM/s0)/r`. Since `Y>=Y3`, their strict slack gives

\[
 4C_NC_Me^{-pY}\leq e^{-p},
 \quad \sqrt{11}C_Me^{-rY}\leq s_0e^{-r}.
\]

It follows that the support conditions with `Mloc=32/sin(s)` and the current second-matrix bound `2N` hold:

\[
 \frac{2(2N)\mathcal M_{\rm loc}\ell_3}{\ell_2}
 \leq8C_NC_Me^{-pY}\leq2e^{-p}<1,
\]

\[
 K_2\sqrt{17}\mathcal M_{\rm loc}\ell_3
 \leq2\sqrt{17}C_Me^{-rY}
 \leq 2\sqrt{17/11}\,s_0e^{-r}<s_0.
\]

These use only `p>1`, `r>2` and the elementary series inequality `exp(x)>=1+x` for positive `x`: `exp(p)>2`, while `exp(r)>3>2 sqrt(17/11)` because `9>68/11`. No new source-frequency restriction is needed.

The previously imposed `Y0` conditions also retain enough strict margin for `2N`: with `u=47/16` and `v=31/16`, their exact `+1` gives

\[
 2N\widehat\lambda_1^{-3}
 \leq\frac{s_0}{2C_\ell}e^{-u}<\frac{s_0}{2C_\ell},
 \qquad
 2N\widehat\lambda_1^{-2}\leq s_0e^{-v}<s_0.
\]

Thus the entire second support remains in the first envelope and its linear profile region; the newest support lies strictly inside the second constant-envelope and linear-profile regions. The base-cell inclusions follow from the already retained original first support and base cutoff. These estimates retain every physical factor of `mu` and `Kj`.

## Sharper newest amplitude bound on the collar

Set exactly

\[
 \bar c=c/\sigma_1^2\leq1/4,
 \quad\bar C=C/\sigma_1^2\leq a/32,
 \quad q=\sigma_1/\sigma_2=s/L,
\]

\[
 \frac{N_3}{\sigma_2^2}
 =q^2\{(E+\bar c)y+\bar Cx\}+bF.
\]

On the proved cube, positivity and `x,y<7` give

\[
 0<(E+\bar c)y+\bar Cx
 <7(13/4+1/16384)<25.
\]

The original sine bound `sin(s)>=(15/16)s` and exact identity `b=rb sin(s)` consequently give

\[
 0<\frac{N_3}{\sigma_2^2\sin s}
 <25\frac{16s}{15L^2}+r_bF
 <1+16=17.
\]

The strict bound on the first term follows from `s<=a<=1/512` and `L>=16384`:

\[
 \frac{25\cdot16}{15\cdot512\cdot16384^2}<1.
\]

Normalize the actual negative pair without altering its original physical values:

\[
 X=-\Theta_3/P_3^*,\quad
 W=-\sigma_2\Omega_3/(K_3P_3^*),\quad
 \delta_3=dK_3^2/\Gamma,
\]

\[
 X'=\mathcal K W-\delta_3 RX,
 \quad W'=\mathcal B X-\delta_3 RW,
 \quad
 \mathcal K=\frac{N_3}{\sigma_2^2\sin s\,R}<1088,
 \quad0\leq\mathcal B=\frac Z{\sin s}<9/8.
\]

This pair is exactly the physical pair in `tr:physical_pair`, under the displayed invertible positive rescalings and `tau=Gamma(t-t1)`. Removing its common positive damping factor and applying the positive integral equations proves `X,W>0` on the collar. Its actual transition data satisfy `X(0)<=e^4`, `W(0)<=3e^4`.

For `S=X+W`, each separate coefficient is less than `1089`, hence

\[
 S'=\mathcal B X+\mathcal K W-\delta_3 RS
 \leq1089S,
 \quad S(\tau)\leq4e^4e^{1089\tau}.
\]

One must use the separate coefficient bounds in this argument; the displayed upper bounds for `K+B` sum to `1089+1/8`, not `1089`. On the enlarged collar,

\[
 1089\tau\leq\frac{3267\sin s}{16384}
 \leq\frac{3267}{16384}<\frac14.
\]

For `0<=z<1`, the series gives `exp(z)<=sum(z^n)=1/(1-z)` because `1/n!<=1` termwise. Therefore `exp(1089 tau)<4/3`, and

\[
 0<X(\tau),W(\tau)\leq S(\tau)
 <\frac{16}{3}e^4<6e^4.
\]

Returning to the original physical amplitudes gives the requested bounds

\[
 0<-\Theta_3<6e^4P_3^*,\qquad
 0<-\Omega_3<\frac{6e^4K_3P_3^*}{\sigma_2}
\]

through `t1+3/(16384 sigma2)`. These bounds do not rely on an assumed quotient continuation.

## Record of work and delegated input

The first audit request was: “Independently audit constants for local spatial addendum; do not edit main TeX. Own third_return/local_spatial/constant_audit.md and optional replay_constant_audit.py/receipt only. Verify tr:local cube implies D>15/16,D<17,R>1/64,R<39, matrix M3 norm/inverse <32/sin s and M2<=2N. Verify existing Y3=1+max source conditions absorb doubling M3 and sqrt17 replacing sqrt11 in supports. Derive normalized newest X=-Theta3/P3*, W=-sigma2 Omega3/(K3P3*) bound <=6e^4 each on tau<=sin(s)/8192 from initial X<=e4,W<=3e4, q=s/L, s<=a<=1/512,L>=16384. Current idea N3/sigma2²=q²[(E+cbar)y+Cbar x]+bF <32, K=N/(sigma2² sin s R)<2048/sin s, B=Z/sin s<=9/8; then S'=...<=2049/sin s S gives S<=4e4 exp(2049/8192)<6e4. Prove numericexp via elementary rational bound, not floating. Need exact original source quantities and no claims beyond local interval.”

The follow-up was: “Add explicit collar 3τ0/2 on same cube, displacement3/512<1/128. Sharper N/(σ2² sin s)<17 follows q²/sin s=(s/L)^2/sin s≤(16/15)s/L², bracket (E+cbar)y+Cbar x<25 with x,y<7, bF/sin=r_bF<16, and 25*(16/15)a/L²<1. Hence newest K=N/(σ2²sin s R)<1088, B=Z/sin s<9/8, S=X+W obeysS'≤1089S. Onτ≤3sin/(2*8192), exponent≤3267/16384<1/4. Thenexp<4/3 andS<16e4/3<6e4. Please independently check/include this stronger amplitude argument and collar in your audit/replay.”

The enlarged geometry, source margins, collar, and sharper amplitude argument have all been checked independently above. The only clarification needed is the separate-coefficient argument in the differential inequality for `S`. The parent was informed of that point while writing the addendum. The independent replay records exact algebra and rational inequalities; the written arguments supply the analytic existence, comparison, and support reasoning.
