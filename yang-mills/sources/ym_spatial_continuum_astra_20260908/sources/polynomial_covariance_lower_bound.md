# Centered spin remainder advance

## Polynomial covariance lower bound for the actual finite-box vacuum

This subsection records an exact centered scalar expansion and the strongest finite-box covariance estimate obtained without replacing the actual positive vacuum. It is a fixed-box result, with the remaining volume-uniform centered-remainder estimate stated explicitly below.

## Exact joint-spin fourth coefficient

On a joint spin block, with `gamma=sum_e n_2^2 lambda_e`, `lambda_e=s_e(s_e+1)`, and independent uniform magnetic weights as in (138)--(140), write

`r_theta(gamma,lambda)=k(theta)-1+(2/3)theta^2 gamma`.

The exact fourth term from the cosine expansion is

`r_theta = (2/9) theta^4 gamma^2 -(4/45)theta^4 sum_e n_2^4 lambda_e^2 -(2/45)theta^4 sum_e n_2^4 lambda_e + rem_6`.

Here `rem_6` is the finite block remainder obtained by replacing `cos x` by its sixth-order Taylor polynomial; the displayed coefficient follows directly from (140), without suppressing any diagonal spin term. After centering, the deterministic part of `(2/9)theta^4 gamma^2` is removed by `P_psi^perp`, leaving the exact covariance contribution `(2/9)theta^4 P_psi^perp((Gamma^2-<Gamma^2>)psi)` plus the two diagonal terms and the sixth remainder. This identifies precisely what a variance-sensitive estimate must control; the old bound `(2/9)theta^4||Gamma^2 psi||` is valid but does not exploit this cancellation.

No bound that replaces `||Gamma^2 psi||` by a variance has been asserted: the joint spin blocks carry arbitrary actual-vacuum coefficients, and a scalar variance inequality alone is false without an additional moment/concentration input.

## Polynomial covariance lower bound from the exact vacuum

Let `W=sum_p(2-tr U_p)`, and let `u=log psi`. The exact operator identity is

`Gamma W = (3/4) sum_p S_p (w_p-2)`,

where `S_p=sum_{e in p, direction 1} n_2(e)^2`, and `A_L=sum_p S_p=sum_{e direction 1} n_2(e)^2 r_e`. In particular `A_L` is of order `L^5`, with all boundary incidence factors retained. The actual energy bound gives

`A_L = (4 L^2(2L+1)/3)(4L^2+2L+1)`.

`<W> <= E/b <= 6 g^2 sqrt(N M) = 6 g^2 sqrt(r) M`, `r=N/M<=5/4`.

Since `S_p <= 2 L^2`,

`sum_p S_p <w_p> <= 2 L^2 <W>` and therefore

`<Gamma W> <= -(3/2)A_L + (3/2)L^2 <W>`.

Using the displayed energy estimate, the explicit condition
`6 g^2 sqrt(r) L^2 M <= A_L/2` implies `<Gamma W> <= -3A_L/4`; hence
`|<Gamma W>| >= 3A_L/4` on that domain. This is an ordinary inequality, with no lower bound on individual plaquette expectations assumed.

Integration by parts gives `<Gamma W>=2 Re int (Gamma-gradient W) dot (Gamma-gradient u) psi^2`. Therefore

`|<Gamma W>|^2 <= 4 S_Gamma <Gamma>`, `S_Gamma=<sum_{e dir1} n_2^2 |grad_e W|^2>`, while `<Gamma> <= L^2 <H_0> <= 3 L^2 sqrt(NM) sqrt(xi) = 3 L^2 M sqrt(r xi)`.

Consequently, whenever the preceding small-coupling inequality holds,

`S_Gamma >= (A_L^2)/(12 L^2 M sqrt(r xi))`.

This is a polynomial, volume-explicit replacement for the previous local-density bound `S_Gamma >= (3/4)e^{-32 pi xi} mathscr S_L`. For an explicit denominator, use the retained exact identity
`[H_0,W]psi=(3W-6M)psi-2 grad W dot grad psi`. The actual-vacuum graph estimate gives
`||[H_0,W]psi|| <= 6M+3 sqrt(M_2)+8 sqrt(I)`,
where `I=int W |grad log psi|^2 psi^2 <= a^2 K^2+3M = 9rM^2+3M` and `M_2<=B_2(K)g^4`. Since `M>=240`, `r<=5/4`, and `g<=1`, one has `B_2(K)g^4 <= 36rM^2+16`, so this denominator is `<60M` (retaining this coarse integer only for a transparent bound). Therefore the preceding inequalities imply the fully explicit covariance estimate

`|| (Gamma-<Gamma>)psi || >= sqrt(xi) A_L^2 /(720 L^2 M^2 sqrt(r))`,

whenever `6g^2 sqrt(r)L^2M <= A_L/2`. This is polynomial in `L` and `xi` and applies to the actual interacting vacuum; it replaces the former exponential-in-`xi` lower bound. It still does not control the centered fourth remainder, whose diagonal and sixth-order terms require a separate weighted fourth-moment estimate, so no prescribed-path spectral conclusion is claimed here.

## Consequence and non-claim

The centered expansion is an exact morphism on each finite joint-spin block and the all-block graph domain. The polynomial covariance lower bound holds for the actual interacting ground state on its displayed small-coupling condition. It does not establish nonzero native low-energy weight in the prescribed continuum paths, nor does it prove an interacting four-dimensional continuum; those remain open.
