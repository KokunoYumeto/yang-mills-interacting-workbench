# Explicit signed tangent certificate

This accompanies Q16 in `FOURTH_ORDER_SOURCE.md`. The source convention is the
same original family of independent plaquette couplings, with `lambda_p=xi`
only after the exact coefficients and their directional responses are retained.

The main coefficient producer solves the original eigenvector coefficient
equation and then computes `Q_H log u`. The independent program
`checks/verify_signed_tangent.py` instead solves the logarithmic-source equation
directly on every coefficient downset:

    K v_nu = Q_H sum_(0<mu<nu) Gamma(v_mu,v_(nu-mu)),
    K v_(e_p)=W_p.

Its returned order-four coefficient equals the entire stored catalogue polynomial
for each of the 78 classes. The same polynomial ring, original link vector
fields, and exact inverse residual are specified in Q5–Q13. The two coefficient
constructions are distinct recurrences on those fixed objects.

For the original face p and each retained source multiindex rho of total degree
at most three, define

    Z_(p,rho)=(rho_p+1) v_(rho+e_p).

The program evaluates the complete signed residual

    K Z_(p,rho) - 2 Q_H sum_(0<mu<=rho)
                  Gamma(v_mu,Z_(p,rho-mu))

and proves it is the zero quotient polynomial for positive degree rho. At
rho=0 its value is exactly the original W_p. This is a finite formal-parameter
coefficient identity, with every sign and multiplicity retained. It follows
analytically by differentiating the logarithmic-source equation; the checker
also executes all coefficient products explicitly.

The full receipt `results/signed_tangent.json` contains:

* 78 independent reconstructed logarithmic sources;
* 2,156 exactly zero polynomial tangent residuals;
* 282 explicitly expanded degree-three response polynomials, with the original
  differentiated face, remaining coupling multiindex, support multiset and chord
  coordinates for every one.

The original symmetry transports in `anchored_quartic_transports.json` return
these representative polynomials to any original four-face cluster. The
source-prefactor is the actual integer occurrence of that differentiated face;
there is no extra factorial or loss of its original union label.

These are the signed finite coefficients through degree three in the derivative
of the vacuum source. No new bound on the norm of an infinite linearized inverse,
uniform gap or continuum limit is inferred from this finite coefficient data.
