# Complete eighth ground-energy coefficient and the original fourth-jet return

18 September 2026. The result concerns the original finite open SU(2) Hamiltonian in S1–S4 of `SIXTH_SOURCE.md`. It gives every inhomogeneous degree-eight scalar coefficient, with open-boundary counts, two independent recurrence assemblies and explicit original Haar integration. `RESPONSE_AND_REMAINDER.md` proves the finite-volume all-higher-order enclosure and the physical observable return. Earlier uniform-gap arguments are not used as premises for that enclosure.

## E1. A fourth-jet identity with the complete state norm retained

Put S(x)=sum_p x_p W_p and H(x)=kappa[K-S(x)+2 sum_p x_p]. The scalar e(x) is the analytic eigenvalue of K-S(x) issuing from zero. The original unit vacuum psi_x is strictly positive at small real x. Its original Haar coefficient m(x)=P_Hpsi_x is then positive. Retain the explicit coordinates

    u(x)=psi_x/m(x),     psi_x=m(x)u(x),
    P_Hu=1,             m(x)^2<u,u>_H=1.                    (E1)

The coordinate m is not dropped from the physical vacuum. It cancels from the following quotient by the displayed multiplication, while the original denominator is retained. Equivalently, u is the unique formal eigenvector section with original constant coefficient one and zero Haar mean in every higher coefficient.

Write u=sum_(j>=0)u_[j](x), u_[0]=1, with u_[j] homogeneous of degree j. The rank-one resolvent branch is analytic in the original graph norm near x=0: its eigen-equation gives Ku=(e+S)u, whose right side is analytic in L^2, and therefore both u and Ku are analytic. Define the actual finite polynomial vector

    phi_4=sum_(j=0)^4 u_[j],     w=u-phi_4.                  (E2)

For fixed real source direction x and scalar t near zero, w(tx)=O(t^5) in the graph norm of K. Since (K-S-e)u=0 and K-S is self-adjoint on real x, expansion of both sides gives the exact equality

    <phi_4,(K-S)phi_4>_H/<phi_4,phi_4>_H-e
       =<w,(K-S-e)w>_H/<phi_4,phi_4>_H.                    (E3)

All four cross terms cancel by the actual eigen-equation; the denominator is the original Haar state norm, tending to one. Cauchy–Schwarz in L^2 and the graph-norm bound give an O(t^10) right side. Thus the full quotient in E3 reproduces every original energy coefficient through degree nine. Repeating over real directions proves the multivariate coefficient identities; each coefficient is a polynomial in the original x_p, so equality on an open real set proves equality of all coefficients. This argument does not apply a conjugate-linear quotient as a holomorphic function away from real parameters.

The original center-link action S26 sends S(x) to -S(x) and commutes with K. The analytic eigenvalue is unique, so e(-x)=e(x). Its odd homogeneous coefficients are zero. The original coefficient recurrence for E1 is

    Ku_[n]=S(x)u_[n-1]+sum_(j=1)^n e_[j]u_[n-j],
    P_Hu_[n]=0 (n>0),
    e_[n]=-<1,S(x)u_[n-1]>_H.                               (E4)

It uses all original face variables. Only a finite Taylor coefficient is evaluated; the full operator retains every spin.

## E2. The complete eighth quotient and its exact return

Let u_j denote u_[j] in this section. Since P_Hu_j=0 for j>0, the degree-eight numerator and the denominator coefficients of E3 are

    N8=<u4,Ku4>-2<u3,S(x)u4>,
    D6=2<u2,u4>+<u3,u3>,
    D4=2<u1,u3>+<u2,u2>,
    D2=<u1,u1>.                                               (E5)

All pairings are the original Haar pairings, interpreted coefficientwise on real polynomial vectors. Dividing the full power series in E3 gives

    e8=N8-e2 D6-e4 D4-e6 D2.                                 (E6)

The original degree-four eigenvector equation is

    Ku4=S(x)u3+e2 u2+e4*1.                                  (E7)

Taking its pairing with u4, with P_Hu4=0, gives

    <u3,S(x)u4>=<u4,Ku4>-e2<u2,u4>.                         (E8)

Substitution of E8 in E5–E6 cancels the two actual e2<u2,u4> contributions. Therefore the same coefficient is

    e8=-<u4,Ku4>-e2<u3,u3>
       -e4(2<u1,u3>+<u2,u2>)-e6<u1,u1>.                    (E9)

Both E6 and E9, with every contributing term, are stored separately in every row. No product of means or quotient denominator is omitted. The first producer checks that their complete original multiindex sums agree.

For a specified original multiplicity nu, the product <u_a,u_b>_nu in these formulas means precisely

    sum_(mu<=nu,|mu|=a) <u_mu,u_(nu-mu)>_H,
    |nu|=a+b.                                                (E10)

The multiplication by S adds one distinguished original face with its actual multiplicity index. This specifies every ordered input of the calculation.

## E3. Complete classification of the degree-eight scalar supports

Multiplication of one original edge variable U_e by the central element -I preserves K, the original Haar measure and the physical subspace. It changes the sign of precisely the face terms incident on that edge. Uniqueness of the analytic ground branch therefore forces an energy coefficient e_nu to vanish unless

    sum_(p containing e)nu_p is even for every original edge e. (E11)

The faces whose multiplicities are odd form a finite cubical two-cycle over F_2. Its finite filling by cubes has an explicit construction. At each cube, assign the parity of the horizontal marked faces above it on the positive third-coordinate ray. Finite support gives zero outside a bounded region. The horizontal boundary differences reproduce those horizontal faces; the two-cycle identities at horizontal edges force the vertical boundary differences to reproduce the other faces. Hence the boundary of this finite cube chain is exactly the specified marked face set. The filling is unique: a nonzero finite cube chain has a highest exposed horizontal face.

For any finite nonempty cube set, each nonempty coordinate column has at least two boundary faces perpendicular to that coordinate. With at least two distinct cubes, their three coordinate-plane projections have total cardinality at least five: two distinct cube positions have distinct images in at least two of the three projections. Thus the boundary contains at least ten faces. A boundary of at most eight faces consequently is either empty or consists of the six faces of one original cube.

At total degree eight, E11 therefore permits exactly these cases:

1. Every multiplicity is even. Dividing each displayed integer multiplicity by two gives an original degree-four face multiset; multiplying it back by two is the inverse map. This yields the 78 complete connected fourth-source representatives.
2. Six cube faces have odd multiplicity, and two additional occurrences are put on one original face. This face is either a face of the cube (one multiplicity becomes three), or an external face occurring twice.

The scalar coefficient is connected in original face-edge adjacency. One way to prove this is the source recurrence S7: all nonzero lower logarithmic sources are connected, and Gamma requires a common differentiated edge. Its Haar scalar has the same property. For an external doubled face in case 2, it must therefore share an original edge with the cube. There are exactly 24 such external faces, and the original signed cubic coordinate group acts transitively on them. The six choices of a marked cube face are also one orbit. The proof retains their actual placements; it does not divide their coefficients by these counts.

Thus the full degree-eight scalar catalogue consists of exactly 80 coordinate representatives: 78 doubled fourth-source representatives, one marked cube, and one cube with an adjacent external doubled face. `generated/energy8_patterns.json` records every source multiset and inverse coordinate witness. `generated/energy8/000.json` through `079.json` contain all coefficients and all terms of E6 and E9.

## E4. Explicit coefficients, including both cube families

A few readable components of the complete catalogue are

    e_(8e_p)=21391/27993600,
    e_(6e_p+2e_q)=-684413851/5147712311040  (p adjacent q),
    e_(4e_p+4e_q)=-322564213/2789727962112  (p adjacent q).     (E12)

For six faces C=boundary(cube) and a marked p in C,

    e_(sum_(q in C)e_q+2e_p)
       =366249151389169/58572365289984000.                    (E13)

For an original external face p adjacent to C,

    e_(sum_(q in C)e_q+2e_p)
       =-336785779/647189637120.                             (E14)

Equations E13–E14 retain the distinct original multiplicities and complete shared-edge recouplings. They include all original scalar returns, rather than only a boundary-length approximation to an intermediate representation.

For four distinct faces in an original straight face-adjacency path, with each face occurring twice, the coefficient is

    c_path4=-41237423/40314521145600.                          (E15)

The full list includes all other four-face shapes and their original words, rather than assigning E15 to an unspecified path geometry. Its use for the two-separated-face response is checked on exactly the four shapes returned in `RESPONSE_AND_REMAINDER.md`.

The independent program `audit_energy_eight.py` reconstructs E4 through degree seven and then takes the original Haar scalar at degree eight, without using E6, E9 or supplied sixth-energy coefficients. It reproduces all 80 entries. The linear recurrence and the fourth-jet producer share the declared exact trace, Casimir and Haar implementation. The separately recorded chord-sphere integration tests use the original product-S^3 moments as an additional scalar-return check. Their scope is given by their exact execution record.

## E5. Exact open-boundary embedding counts

For every representative apply all 48 original signed coordinate operations and translate the minimum coordinate to zero. Equality of the complete oriented face multisets identifies duplicate images, leaving a list of distinct original oriented shapes. For one such shape, let w_i be the extent of its original vertices in direction i. In the box with side m=2L, the original translation coordinates lie in

    -L<=n_i<=L-w_i,

so there are exactly product_i(m+1-w_i) placements. All displayed shapes have w_i<=4, and L>=2 covers the complete list. Planar supports retain the factor m+1 in their unused direction. The inverse map reads the original minimum vertex and its unique translated shape.

Each original face multiset has exactly one such shape and translation, so the count introduces no orbit-size or factorial correction. Multiplying these integer count polynomials by the coefficients in E12–E14 and all remaining rows yields

    e8,L=A3 m^3+A2 m^2+A1 m+A0,       m=2L,                  (E16)

where

    A3=1703320005700992315276593/68235298203010622261760000,
    A2=421994013280213546390961/31615192631460259261440000,
    A1=14702805516554176523/16975106412310126080000,
    A0=404673359378191/1312237663289280000.                    (E17)

`energy8_response.json` retains each shape's widths, integer embedding polynomial and independently enumerated L=2 placement count and digest. Every finite placement is verified against the actual contained face set before differentiation.

In particular the L=2 box has M=240 and

    e8,L=9876448280610811115073772847/
          5441765031690097125375360000.                       (E18)

The coefficient per original plaquette has the exact spatial limit

    e8,bulk/face=A3/3
      =1703320005700992315276593/
         204705894609031866785280000.                         (E19)

This is the limit of the coefficient of xi^8. The complete finite-volume analytic remainder is stated separately and retains its actual dependence on M.

## E6. Complete original energy and external single-face check

The lower coefficients retained from the independently checked predecessor are

    e2,L=-M/3,
    e4,L=5M/216-2J/1053,
    M=3m^2(m+1),   J=6m(3m^2-1),
    e6,L=-(211396463m^3+30959193m^2+21845782m+2336684)/4691494080.
                                                                    (E20)

The original physical energy therefore has the complete displayed series

    E0,L=kappa[2Mxi+e2,L xi^2+e4,L xi^4+e6,L xi^6+e8,L xi^8]
          + original higher-order remainder.                 (E21)

The independent one-face character recurrence reproduces E12 and every lower one-face coefficient. For the original class angle theta, W=2cos(theta) and

    K=-(d_theta^2+2cot(theta)d_theta).

The exact coordinate map t=theta/2, y(t)=sin(2t)F(2t), with inverse F(theta)=y(theta/2)/sin(theta) on the induced domain, has the norm return

    (2/pi)int_0^pi sin^2(theta)|F(theta)|^2dtheta
      =(4/pi)int_0^(pi/2)|y(t)|^2dt.                          (E22)

The original eigen-equation becomes y''+[4(e+1)+8xi cos(2t)]y=0. Thus its branch is

    q_Mathieu=-4xi,   e_one=b_2(q_Mathieu)/4-1,
    E_one=kappa(2xi+e_one).                                  (E23)

NIST DLMF 28.6.5 gives the coefficient 21391/27993600 after exactly this substitution. This checks the single-face convention and coefficient. The full spatial catalogue, its two cube families and its boundary return have the separate original-coordinate calculations above.

## E7. Scope and source credit

The complete tables are finite exact Taylor calculations with full original representation lists. E3 supplies the all-state variational identity underlying the new fourth-jet evaluation. A separate finite-volume contour proof encloses the uncomputed orders; it does not invoke the historical volume-uniform source norm estimates. No new continuum gap, volume-independent analytic radius, external analytical review, Lean certificate or global priority claim is made.

The original Hamiltonian exponential-vacuum/linked-cluster and character methods retain their attribution to Schütte–Zheng–Hamer and the predecessor workbench sources. NIST's authored Mathieu chapter is cited for E23 only. The complete used local dependency identities and original publication URLs are in `SOURCE_INTAKE.json`.
