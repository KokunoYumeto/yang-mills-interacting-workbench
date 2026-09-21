# Evaluate actual interacting loop moments and response with finite uniform-volume errors

Proposed base: `research/20260914-coupled-response`, inspected head
`e98b2c3af77f66fb1c1396143ca53daef586404f`. Proposed branch:
`research/20260915-actual-loop-moments`. No remote branch or PR has been created.

## Mathematical continuation

This evaluates the response inputs named by PR6 on an original Wilson-loop
observation, retaining its exact map from the preceding coarse-edge observation
and its additional kernel. A differentiated-vacuum Ward identity proves
all-coupling pointwise log-gradient and integrated derivative bounds without
an exterior-volume factor. The exact spin-one gauge source has inverse bound
3/kappa; its physical contraction and all cross derivatives are retained.

The actual local drift has a uniform remainder. Exact SU(2) neighboring-face
integrals give the first three moment coefficients 1, 5, 103/4 for an elementary
square and explicit polynomial coefficients for every larger square. Complete
finite error formulas return these to the actual interacting vacuum. At
xi=10^-8 (g^2=5000, kappa=10000/a), N0,N1,N2 are enclosed respectively by
[0.9994,1.0006] kappa^2 xi^2, [4.9963,5.0037] kappa^3 xi^2, and
[25.728,25.772] kappa^4 xi^2, for every exterior box L>=2.

The actual positive-shift response is within 0.0000075 kappa xi^2 of
(28/165) kappa xi^2. The restored kernel norm squared is within 0.0000021 xi^2
of (796/27225) xi^2, and the raw observed Gram is retained. The canonical
cohomological quotient norm is related to the chosen trial's residual by the
explicit positive section-correction term A45a.

## Verification and scope

134 uniquely named exact checks and 12 false-formula controls passed normally,
under Python -O, and from a fresh copied-source directory. Three CLI corruption
tests failed at their intended errors in both modes. The original PR6 checker
also passed unchanged in both modes. Analytical proofs are written in full;
no numerical vacuum integration, spin cutoff, new Lean certificate or external
proof audit is claimed.

The narrow interval is on its stated large-g domain. The all-coupling bounds
apply to the retained running path with their full growth factors. A physical
continuum gap, a nontrivial four-dimensional field and the physical zero-shift
response remain unestablished by this contribution. No priority claim or
automatic merge is requested. All inherited proofs and receipts remain unchanged.
