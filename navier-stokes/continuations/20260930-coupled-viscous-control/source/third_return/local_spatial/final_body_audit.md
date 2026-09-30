# Final bounded audit of the local spatial addendum

The complete `third_return/local_spatial_body.tex` was read, together with the equations it cites in `third_return/third_return_body.tex` and `third_transition_spatial/third_transition_spatial_body.tex`. The review covers the actual local interval and its explicit right collar only. No main TeX was edited. No further mathematical extension was undertaken.

The preceding `constant_audit.md` proves the numerical geometry, amplitude, material and source-nesting estimates used in the completed addendum. The completed body incorporates those estimates correctly, including the separate-coefficient argument for `(X+W)' <= 1089(X+W)`. The closed rectangle used for derivative maxima also satisfies all the same denominator bounds. The body is accepted on its stated finite scope.

## Exact angular control and its upper bound

The prescribed local ramp is `Z=Z1(1-eta(tau))`, with `tau=Gamma(t-t1)`, so `dot(Z)=-Gamma Z1 eta'(tau)`. Substitution in the exact control gives

\[
 \dot\alpha=
 \frac{\Omega_1y\zeta_{1,1}+(b\Omega_2/D)\zeta_{2,1}
          +\Gamma Z_1\eta'(\tau)}Y.
\]

Every sign and physical factor is therefore the one in `trls:controlfunction`. The cube implies `Y>1/9`, `y<7`, `|zeta1,1|<=1`, `|zeta2,1|<sqrt(17)<5`, `|Omega1|<11 sigma1`, `|Omega2|<sigma2/16`, and `b/D<(64/15)sin(s)`. Thus

\[
 |\mathcal F_3|
 <9\left(77\sigma_1+\frac{64}{15}\sin s
                        \frac{\sigma_2}{16}\,5\right)
 =693\sigma_1+12\Gamma.
\]

The remaining ramp term is at most `(81/8) Gamma sin(s) [eta']0` because `Z1<(9/8)sin(s)`. This proves the entire displayed `A_*` with no hidden coefficient or omitted second-parent term.

## Exact full PDE substitutions

All three activation weights equal one on the local interval and its collar, so `Tj=Thetaj`, `Qj=Omegaj/rhoj`, and every positive-order activation derivative vanishes there. For each layer write `D_*=D_<j`, `G_*=G_<j`, `k=Kj zetaj`, `rho=|k|^2`, `g=f(Mj^-1 x/ellj)`, `V=T F(k dot x)g`, `Psi=Q P(k dot x)g`, and `v=J grad(Psi)`. The support calculation proves that the actual sum of older fields equals `G_* dot x` and `D_* x` on a neighborhood of the entire layer support.

The exact material equations give

\[
 \mathcal D=\partial_t+D_*x\cdot\nabla,
 \quad\mathcal D(k\cdot x)=0,\quad\mathcal Dg=0,
 \quad\dot\rho=-2k\cdot D_*^Tk,
\]

\[
 Q_{\rm r}=\frac{k_1\Theta}{\rho}-Q\frac{\dot\rho}{\rho},
 \quad\dot Q=Q_{\rm r}-d\rho Q.
\]

The temperature coupling is `dot(Theta)=-Omega(J zeta dot G_*)/(Kj |zeta|^2)-d rho Theta`, whose first term cancels the `Q F g (J k dot G_*)` contribution from `v dot G_*`. The remaining cross term is `Q P(J grad(g) dot G_*)`. The exact self-advection calculation uses `P'=F`, `Jk dot k=0`, `J grad(g) dot grad(g)=0`, and `J grad(g) dot k=-Jk dot grad(g)` to give

\[
 v\cdot\nabla V=QT(F^2-PF')g(Jk\cdot\nabla g).
\]

Subtracting `d Delta(V)` and retaining `-d rho V` yields exactly the cited scalar residual. For the vector equation, trace zero gives `D_*J+JD_*^T=0`; commuting the material derivative past the spatial gradient yields

\[
 \mathcal Dv=D_*v+Q_{\rm r}J(kFg+P\nabla g)-d\rho v.
\]

The reverse interaction `(v dot grad)(D_*x)=D_*v` supplies the other copy of `D_*v`. The remaining terms are precisely `(grad v)v`, `-V e2`, and `-d Delta(v)`. This verifies the full vector residual, including its factor two, its gravity sign, and the changing phase-length term. Differentiating `Delta(Psi)=Q(rho F'g+2F k dot grad(g)+P Delta(g))` produces all six groups in the cited vector Laplacian; no derivative group is missing.

Adding layers in their actual order counts the two directions of every distinct pair once, since each layer interacts with the entire older sum. The self-interaction is included in that layer's residual. Outside a layer's closed support, its spatial and temporal derivatives vanish. The identities consequently hold globally, not only near the origin.

The base scalar phase and radial cutoff are materially transported by `dot(alpha)Jx` on their support; the initial interpolation is already complete on the local interval. Its scalar residual is therefore `-d Delta(theta_b)` there. Direct differentiation of `u_b=dot(alpha)J grad(H0)` gives the four base vector terms cited by the addendum: angular acceleration, quadratic velocity advection, negative buoyancy and velocity diffusion. All formulas match the earlier original sine initial interpolation. Flat source switching and the proved matching angular, state and material jets at `t1` make their concatenation smooth. No frozen endpoint is used.

In the core, `g=1` and `F(xi)=xi`, while `P(xi)=P(0)+xi^2/2`. Hence both fields are affine, their Laplacians vanish, and the modal terms `-d rho V` and `-d rho v` remain. The constant `P(0)` is retained in the full cutoff field. The phase-coordinate mixed Laplacian is the exact chain-rule expression with `Mj^-1 Mj^-T`; the body never substitutes an eigenprofile or stationary metric.

## Complete spatial force costs

The tuples of lower and upper phase lengths, amplitude bounds and matrix bounds in `trls:normdata` and `trls:matrixbounds` are exactly the enlarged local bounds proved by the constant audit. `||J zeta tensor zeta/|zeta|^2||=1` proves `||D_<j||<=D_j`; the triangle inequality proves the stated bound `|G_<j|<=G_j`. Since `|dot(rho)/rho|<=2D_j`, the formula for `Q_r` gives exactly

\[
 |Q_{\rm r}|\leq
 \frac{\kappa_j U_{\Theta,j}+2D_jU_{\Omega,j}}
      {K_j^2r_{-,j}^2}.
\]

No activation derivative belongs in this local numerator. Product differentiation of `W(k dot x)g` allocates `q` of its `m` derivatives to the linear phase, with bound `kappa^q[W]q`, and the remaining derivatives to the material envelope, with bound `(Nj/ellj)^(m-q) f_(m-q)`. The exact count is `binomial(m,q)`, giving `B_j,m(W)`. Leaving one additional derivative on the envelope gives `C_j,m(P)`. These estimates hold in the stated Euclidean multilinear norm, not only for coordinate derivatives.

The two coordinate traces in each spatial Laplacian give the factor two in both complete damping-plus-diffusion estimates. The scalar nonlinear sum bounds `v dot grad(V)` by allocating `q` derivatives to `v=Q J grad(Pg)` and the other `m-q` to `grad(V)`. This gives derivative indices `q+1` and `m-q+1`. The vector sum applies the same allocation to `(grad v)v`, giving indices `q+1` and `m-q+2`; reversing the allocation yields the identical sum after reindexing. The remaining linear terms give exactly the displayed coefficients of `B(P)`, `C(P)`, and `B(F)` in `trls:forcecost`.

The global norms add the entire base residual and all three layer residuals. The base quadratic term allocates `q` derivatives to the velocity gradient and `m-q` to velocity, yielding `H_(q+1) H_(m-q)` with the stated binomial factor. Its acceleration coefficient is the separately defined exact `A_2`. The base temperature phase has norm `mu`, so its product bound is `B_0,m(F)` exactly. These bounds hold on all physical space; integrating a constant bound over the local interval or collar supplies respectively `1/(8192 sigma2)` or `3/(16384 sigma2)`.

For the displayed frequency costs, `P3*=(A0/mu) lambda_hat3^(-7/8)` and `K3=mu lambda_hat3` imply `K3^2 P3*=A0 mu lambda_hat3^(9/8)`. Consequently the temperature coefficient is `6 e^4 d A0 mu lambda_hat3^(9/8)`. The inverse phase-length lower bound contributes `64` to `Q3`, so `d Q3 K3^3=384 e^4 d A0 mu lambda_hat3^(9/8)/sigma2`. The localization factors retain each `mu`, source radius and sine exactly. The three modal exponents are the original physical integrals `d Kj^2 integral |zetaj|^2 dt`; their upper and lower estimates use precisely the proved intervals for `D` and `R`. The body separately retains the two numerator-loss terms.

## Eight-state jet derivation and mixed derivatives

With `z=(h,g,E,Fa,omega,V,X,W)`, the field components are associated to these named coordinates. The first six coordinate equations are the six named equations in `tr:scaled`; their typeset order places the omega equation before Fa, whereas the state lists Fa before omega. The parent has clarified the final text to specify the coordinate right-hand sides ordered exactly as `(h,g,E,Fa,omega,V)`, followed by `(X,W)`. That final wording was inspected and resolves the display-order ambiguity. No mathematical correction is required.

The first six named equations and the last two amplitude equations depend on the prescribed switch value `lambda^[0]` through `Z` and the exact inverse phases. They do not depend on switch derivatives. The angular function depends on both `lambda^[0]` and `lambda^[1]`, with the latter appearing exactly as `+Gamma Z1 lambda^[1]/Y`. Every denominator is positive on a neighborhood of the whole closed rectangle: `D>15/16`, `R>1/64`, and `Y>1/9`, including the rectangle's weak boundaries. The fixed positive constants `a`, `sin(s)`, the physical frequencies and scales are never allowed to vanish. Thus the vector field and angular function, and every finite derivative of them, are smooth on the stated finite jet rectangles.

Along the actual trajectory, the chain rule gives

\[
 \frac{d}{d\tau}H(z,\lambda^{[0]},\ldots,\lambda^{[m]})
 =\sum_{l=1}^8\mathcal V_l^{\rm loc}\partial_{z_l}H
  +\sum_{j=0}^m\lambda^{[j+1]}\partial_{\lambda^{[j]}}H
 =\mathcal C_{\rm loc}H.
\]

At every iteration the highest switch jet increases by at most one. Since `Phi` already uses the first jet, `C_loc^n Phi` uses at most jet `n+1`, exactly as in the maximum defining `A_(n+1)`. Physical differentiation adds a factor `Gamma` at each iteration; since `Phi=dot(alpha)`, this proves `alpha^(n+1)=Gamma^n C_loc^n Phi`. The maxima are over explicit compact sets on which their expressions are smooth and finite. The actual state and switch jets belong to those sets by the proved bounds. This verifies the control-derivative estimates, including the `n=0` and `n=1` cases and the definition of `A_2`.

For mixed derivatives the cited pullback operators are the actual chain rule on `H(t,x,k(t) dot x,Aj(t)x)`, with `Aj=Mj^-1/ellj`. Their time/spatial commutators vanish by cancellation of the derivative of each coefficient with the derivative of its explicit `x` factor. Differentiating `dot(Aj)=-Aj D_<j` yields the displayed ordered product recursion. The matrix and phase recursions retain their correct multiplication order and transposes. Jets of the parent sums use the state and angular derivation just proved. The periodic factors and material cutoffs remain their original functions. Bounding the finitely many coefficient products on their support by `(Nj ellj)^|beta|`, the original profile derivative bounds and the recursive coefficient bounds therefore gives every requested mixed norm. Positive-order activation jets vanish on this local interval, while the base uses the original fixed support radius and its angular derivative bounds. No time derivative of the diffusion metric or damping coefficient has been suppressed.

## Compact force extension and parity

The right collar is the actual nonconstant first-ramp continuation already proved on the same cube. It has physical length `epsilon_R=1/(16384 sigma2)` beyond `t*`. The left collar is the original sine initial state held constant at negative time with zero velocity. At zero, flatness of the original initial interpolation matches all these left jets. At `t1`, the source control and all state/material jets match the preceding transition; the local construction therefore defines a smooth field throughout the full enlarged slab.

The raw residuals of these fields equal the proved PDE forces on the entire nonnegative slab. The cutoff

\[
 \beta_*(t)=\eta(1+t/\epsilon_L)
            \eta(1+(t_*-t)/\epsilon_R)
\]

equals one on `[0,t*]` because each argument is at least one there. At `-epsilon_L` and `t*+epsilon_R` its relevant factor is zero with every derivative. The zero extension of the product with the smooth raw residuals is therefore smooth. The spatial supports are uniformly compact on this finite interval; on the proved slab they stay within the original base support ball by the strict nesting already verified. The product rule gives the stated cutoff derivative sum; absolute values remove the sign from the derivative of the right factor. The raw mixed norms are covered by the local recursion, preceding slab bounds and fixed left initial state. Their maximum covers the entire interval used by the cutoff.

The final PDE claim is confined to `[0,t*]`, where multiplication has not altered the forces. Odd scalar profile, even primitive and even cutoffs make the scalar fields odd, the streamfunctions even, the velocities odd, and vorticities even. Each full residual preserves the claimed odd parity. Compact smooth streamfunctions have square-integrable velocities, and the cited distributional identity `(Delta N0)*psi=psi`, with `N0=(2pi)^-1 log|x|`, gives the exact Biot--Savart formula for their compact smooth curls. The local addendum correctly preserves this complete spatial realization without making a third-return or infinite-iteration claim.

## Final audit record

The final bounded request was: “Final bounded verification: complete third_return/local_spatial_body.tex is now written. Read it fully and check every claim outside constants especially local control A*=693sigma1+12Gamma+(81/8)Gamma sin(s)[eta']0, all spatial force substitutions, amplitude pair, jetbox derivatives (8state and eta^[j]), compact force collar. Record any findings in your existing constant_audit.md or separate final_body_audit.md under owned local_spatial directory; no TeX edits. Re-run35 replay after audit torefreshsourcehash including local_spatial_body.tex ifappropriate. Then freeze; no additional math expansion.”

That bounded review is complete. The independent 35-check replay was refreshed to hash the completed local body and this final audit in addition to its existing sources. Its analytic scope remains as declared; written proofs above supply the PDE, differentiation and collar checks that are not substitutes for algebraic test counts. The final named-coordinate wording clarification was verified. The audit is frozen after that replay with no outstanding mathematical finding.
