# Exact plaquette coefficient and the sharper full-gap domain

15 September 2026. This sharpens, on the same original coefficients and
physical operators, the fully written construction in `RESEARCH_NOTE.md`.
It also returns the sharpened constants through every step of
`VOLUME_LIMIT.md`. The baseline estimates are preserved in those files for
comparison; the present formulas give the stronger domain and lower bound.

The actual coefficient recurrence, plaquette words, representations, product
Haar coordinates, vacuum, physical energy and observation maps are unchanged.

## O1. The original plaquette coefficient has trace norm exactly eight

Write the four independent original link variables in their word order:

    W_p=Tr(U1 U2 U3^-1 U4^-1).

The inverse entry of an SU(2) matrix is

    (U^-1)_(r,c)=(-1)^(r+c) U_(1-c,1-r), r,c in {0,1}.

It follows directly from det(U)=1, or from multiplication by the original
matrix epsilon=[[0,1],[-1,0]]. Keeping all four trace indices gives the
coefficient A in W_p=Tr(A(U1 tensor U2 tensor U3 tensor U4)):

    A_[(i1,i2,1-i2,1-i3),(i0,i1,1-i3,1-i0)]
        +=(-1)^(i0+i2),  i0,i1,i2,i3 in {0,1}.             (O1)

Every unlisted entry is zero. This formula is the complete original Fourier
coefficient, with the trace convention U6; there is no change in source mass.
For each fixed pair (i1,i3), the two possible rows (i2=0,1) and columns
(i0=0,1) form the block [[1,-1],[-1,1]]. Different pairs have disjoint row
sets and disjoint column sets. There are four such blocks and eight unused
rows and columns. These are explicitly permuted original row and column
indices, not chosen singular vectors.

Consequently A* A is positive, (A* A)^2=4A* A, and Tr(A* A)=16. The matrix
(A* A)/2 is positive and its square is A* A. Uniqueness of the positive
square root proves

    ||A||_1=Tr sqrt(A* A)=8.                              (O2)

The Haar norm check is Tr(A* A)/16=1, agreeing with the original plaquette
second moment. Any permutation into the fixed global order of edge tensor
factors conjugates A by the explicitly corresponding tensor permutation,
preserving O2. This proves the value for every original plaquette in the box.

## O2. A second auxiliary support norm, with its complete comparison

Put w=5/4. On the same labelled coefficient families in U9 define

    ||f||_w=max_e sum_(S containing e) w^|S|
                            sum_(j nontrivial)c(j)||A_(S,j)||_1. (O3)

The map between this coefficient space and U10 is the identity on each
original A_(S,j); its inverse is the same identity. On each finite original
graph their exact estimates are

    ||f||_w <= ||f||_2 <= (8/5)^|E_L| ||f||_w.             (O4)

This follows by comparing the displayed positive weights at each original
support label. The second factor retains its volume dependence. It is not
used to transfer a volume-uniform estimate. The physical L2 and energy
pairings have not been changed; O3 is an auxiliary absolute-convergence norm
for the exact same source coefficients and their assembly map.

Since w^|S union T|<=w^|S|w^|T|, the entire anchored calculation U12–14 gives,
with its original matrices and all generator components,

    ||B(f,h)||_w <= (8/3)||f||_w||h||_w.                  (O5)

O2 and the actual maximum of four incident plaquettes give the improved
source estimate

    ||v_[1] xi||_w <= B_xi,
    B_xi=4 w^4 *8 xi=(625/8)xi.                          (O6)

The factor c(j)=3 still cancels the original inverse Casimir 1/3. Every
weight and each of the four plaquette links remains explicit.

## O3. Sum the convergent majorant instead of replacing it by twice its input

Define the following actual scalars from the original coupling:

    theta_xi=(2500/3)xi,
    r_xi=(3/16)(1-sqrt(1-theta_xi)),
    0<xi<451/552960.                                    (O7)

This interval lies strictly inside theta_xi<1. Direct multiplication gives

    r_xi=B_xi+(8/3)r_xi^2,
    (16/3)r_xi=1-sqrt(1-theta_xi)<125/288<1.              (O8)

The closed r_xi ball is therefore preserved by the literal nonlinear map
f->v_[1]xi+B(f,f), and its difference bound is the strict constant in O8.
Starting at zero, the successive differences are bounded by that constant
to their iteration power times B_xi. Their sum converges in the complete
labelled norm. Passing in the bounded bilinear map proves the fixed equation;
the same difference inequality proves uniqueness in that ball.

Equivalently, the complete order coefficients satisfy the already proved
Catalan recurrence and now obey

    ||xi^p v_[p]||_w <= C_(p-1)(8/3)^(p-1) B_xi^p,
    sum_(p>=1) C_(p-1)(8/3)^(p-1) B_xi^p=r_xi.            (O9)

The equality follows from the scalar generating equation c=1+z c^2 and the
branch with constant coefficient one, on 4z<1. For a direct justification,
the Catalan convolution proves the equation coefficient by coefficient;
C_n<=4^n gives absolute convergence, and the positive solution continuous
at z=0 is (1-sqrt(1-4z))/(2z). Its omitted tail after order P is at most

    B_xi theta_xi^P/(1-theta_xi).                         (O10)

Every coefficient is the same exact coefficient as in U26. Thus on the
common convergence interval the labelled families themselves agree, including
the assembly-kernel data. The improved radius extends that original family;
it does not select another observation or another vacuum. The C2 convergence,
elliptic bootstrap, recovered scalar c_L and ground energy E0,L are precisely
the constructions U17–18, now applied to this convergent same-source series.
Their proofs identify the actual positive unit vacuum at every g in O7.

## O4. The complete second derivative and the full physical gap

The elementary integer maximum needed in the original row estimate is

    sup_(m>=1) (m+1)/(5/4)^m=256/125, attained at m=3,4.  (O11)

The ratio of successive terms is (4/5)(m+2)/(m+1): it exceeds one at m=1,2,
equals one at m=3, and is smaller afterwards. Substitution into the full
mixed-block estimate U18, before any diagonal entry is removed, gives

    ||S_u||op <= (384/125)r_xi.                          (O12)

The same bound holds for the nonnegative full derivative row majorant used
for the drift comparison. The original group coordinate Gamma2 calculation
U20–22 is unchanged. It consequently proves on the full centered scalar
form domain, and hence on its complete physical invariant subspace,

    Delta_L >= kappa d_xi^sharp,
    d_xi^sharp=1/2-(768/125)r_xi
             =(144/125)sqrt(1-(2500/3)xi)-163/250 >0.    (O13)

This is valid for every L>=2 and a>0 on the explicit domain O7. The upper
endpoint of O7 is obtained by exact squaring:

    1-(2500/3)(451/552960)=(163/288)^2,
    r_(451/552960)=125/1536.                             (O14)

No strict estimate is asserted at that endpoint. In the original coupling
coordinate the proved positive-gap interval is

    g^4>138240/451.                                     (O15)

A useful closed subinterval with a simple physical constant is

    g>=9/2  => xi<=4/6561,
    Delta_L >= (3/20)kappa =3g^2/(10a).                 (O16)

For this explicit domain the inequality is proved, rather than inserted as
an assumption: 1-theta_xi>=9683/19683, and
9683/19683>(401/576)^2. Multiplying the latter square-root bound by 144/125
and subtracting 163/250 gives a number strictly greater than 3/20.
The weak endpoint notation in O16 is therefore safe throughout the closed
g-domain. At larger g the original formula O13 retains its stronger value.

The exact primitive relation remains

    ||p_L||^2=1/Delta_L <=1/(kappa d_xi^sharp),
    p_L((X_i f)_i)=f, int rho_L f=0.                    (O17)

Its source/target pairing is the original physical one in U25, not O3.
All physical states, including regulator-dependent choices, are included in
O13. No finite trial-space lower bound has been substituted.

## O5. Return to the actual zero-shift moments and the canonical residual

The actual D of U31 is the same original conditional-kernel form restriction.
Every element of that kernel has zero mean in rho_L. Therefore

    D>=kappa d_xi^sharp,
    ||D^-1||<=1/(kappa d_xi^sharp).                       (O18)

The actual elementary-loop constructions U33–40 retain their original
forcing W, trial Y, remainder R=W-DY, raw G, kinetic K0, and coefficients
8/39 and 196/4563. The predecessor's pointwise log-vacuum remainder is proved
on xi<=3/64, which contains the entire domain O7. Thus the same explicit
expressions delta,eta,h_z,r_z,n_z and a1,...,a6 remain applicable. In a7 and
the restored-state error, replace the inverse bound by the proved O18:

    a7=r_z^2/d_xi^sharp,
    E_M^sharp=(a1+...+a6+a7)/xi^2,
    E_Z^sharp=delta z_*+(eta Z_*)^2
          +2n_z r_z/(d_xi^sharp xi)+(r_z/(d_xi^sharp xi))^2. (O19)

These are estimates in the original physical Hilbert pairing. They give

    |M0-(8/39)kappa xi^2|<=kappa xi^2 E_M^sharp,
    |||D^-1W||^2-(196/4563)xi^2|<=xi^2 E_Z^sharp.          (O20)

The exact canonical quotient/primitive energy identity U45 is unchanged,
and its full nonnegative error is at most kappa r_z^2/d_xi^sharp.

At the already specified actual coupling xi=10^-8, g^2=5000, kappa=10000/a,
outward rational square-root bounds prove

    d_xi^sharp>0.49999519998,
    E_M^sharp<0.0000094,
    E_Z^sharp<0.0000041,
    r_z^2/(d_xi^sharp xi^2)<0.000000000022.               (O21)

Thus all zero-shift intervals U41–50 remain valid with this sharper full-gap
lower endpoint. In particular the actual complete physical gap satisfies

    0.49999519998 kappa <= Delta_L < (3+5/10^13)kappa.    (O22)

The upper bound is still the actual one-state variational upper bound U49;
its direction and scope have not changed. The lower bound is from the full-
domain argument O13. The polynomial coefficients and actual-vacuum remainder
estimates have been retained separately in O19–20.

## O6. Complete return through the spatial-volume construction

The proof in `VOLUME_LIMIT.md` uses the actual coefficient recurrence,
absolute support bounds, a summed conditional influence below one, and a
summable drift derivative row bound. Each input is now evaluated explicitly
on O7; the following formulas replace only the auxiliary bounds in that
proof, on the exact same finite-volume vacua.

First, labelled coefficients are cutoff-compatible by V1, independently of
the auxiliary norm. Their complete w-weighted bound is r_xi. Thus

    sup_e sum_(S containing e)||v_S||infinity<=(16/15)r_xi. (O23)

Here c(j)>=3/4 and w^|S|>=5/4 were used directly. The original conditional
densities V5 consequently have the same uniformly absolutely convergent
meaning. Their original influence majorant V6 now obeys

    sup_e sum_f c_ef<=(65536/9375)r_xi<128/225<1.         (O24)

Indeed sup_(m>=1)(m-1)/(5/4)^m=4096/3125, attained at m=5,6, and multiplying
by 16/3 gives the first coefficient. Its endpoint value at r=125/1536 is
128/225. The finite heat-bath comparison V8–9 is therefore the same actual
comparison, with q=128/225 and its complete Neumann powers. The proof gives
uniqueness and full-sequence convergence of the original vacuum measure on
the entire sharper interval O7.

The full mixed drift matrix in V10 has row sum at most

    B_*=(384/125)r_xi<1/4.                               (O25)

Its long-distance rows are bounded by
(3/2)r_xi (m_d+1)/(5/4)^m_d, with m_d=max(3,d+1), by O11 and the original
connected-support argument. The drift approximation is supplied by the
complete coefficient tail O10. All original variables, vector fields and
Brownian coefficients in V12–18 remain fixed. Hence the direct dynamics,
its invariant measure, and every local time-ordered correlation converge
along the full box sequence just as proved there. In V20 substitute the
proved full-domain lower value kappa d_xi^sharp. This constructs the same
physical vacuum representation and gives its self-adjoint generator that
positive lower edge. Both compactified spectral endpoint atoms are zero at
fixed a,g, using the same local first-moment bound U51.

The scalar vacuum energy identity V23–25 is also unchanged: its pointwise
input xi<=3/64 contains O7, and its local drift convergence now uses O10.
Thus the original energy-per-plaquette limit and its finite explicit error
remain established on this larger domain.

Finally, the original simultaneous path keeps

    a_n=a0 2^-n, c_n=g0^-2+beta n log2, g_n^2=1/c_n,
    xi_n=c_n^2/4.

The exact new validity interval on that path is

    c_n < sqrt(451/138240).                              (O26)

For beta>0 only a finite initial part of that unbounded c_n path lies in this
proved domain. With fixed admissible g and a->0, the original physical lower
bound kappa d_xi^sharp diverges as 1/a; the positive-time collapse and the
retained infinite-energy endpoint in U57 follow with this same exact value.
No finite continuum mass or smooth four-dimensional field construction is
assigned to these parameter maps.

## Scope of verification

The checker constructs the complete original 16 by 16 Fourier coefficient,
checks its positive-square-root identity, and verifies the trace convention
against literal four-link SU(2) words using exact rational quaternions. It
checks the finite support norm comparisons, all extremal weight constants,
the exact quadratic majorant, domain endpoints, original physical factors,
and O21 with integer-square outward bounds. The general analytic arguments
and infinite-limit proofs are the written proofs U1–57 and V1–25 with the
explicit substitutions O1–26 above. Exact finite checks do not constitute a
new Lean build or an independent mathematical audit. No general-priority
claim is made for the Fourier, contraction, curvature or Gibbs methods.
