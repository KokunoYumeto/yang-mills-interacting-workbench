# Zero-shift local Yang–Mills response: mathematical review

Read the complete [delivered mathematical proof](DELIVERED_RESEARCH_NOTE.md).
This additive review is based on the unmerged PR6 head
`e98b2c3af77f66fb1c1396143ca53daef586404f`. It changes no inherited file,
current pointer, other research branch, or main ref.

## Completed calculation

The full original finite-regulator Hamiltonian and actual vacuum give an
all-coupling local conditional-density ratio. On the explicitly selected
simultaneous path `g_n^(-2)=c0+n log(2)/(8 pi sqrt(13))`, with the original
`a_n=a0*2^(-n)` and `L_n=4*2^(2n)`, the inverse of the actual local
conditional-kernel operator is bounded by a constant times `c_n^(-7)`.
The loop has physical side `a_n`, and the observation retains its holonomy
AND every exterior link. No quantum beta-function identification is asserted.

At `xi=10^(-8)`, for every original spacing and exterior box, the actual
zero-shift response has coefficient `8/39` with error less than `2.6e-9`,
and its primitive squared norm has coefficient `196/4563` with error less
than `1.04e-8`, in their respective original `kappa*xi^2` and `xi^2` units.
The actual raw Gram and kinetic entry are evaluated through second order.
The restored physical state's Rayleigh coefficient lies in `(0.2184,0.2248)`
around `337/1521`, with the full state norm retained. The local form sector
has lower bound `0.74999*kappa`. The wider observation retains the exact
additional response `q_eff(k_star)` and its full norm cross term. A uniform
bound for that outer response and the complete physical continuum mass gap
are not established here.

## Exact publication and verification scope

This Git review contains **two files only: this guide and the complete proof**.
The proof is preserved byte-for-byte from the full tested delivery; its source
and checker descriptions refer to that complete delivery. It must be read
with this narrower publication scope. A checker-dependency upload was blocked,
so an incomplete runnable checker is deliberately not published on this branch.
The complete runnable source, all dependencies, full decoded and compressed
receipts, source intake, and tested full-workbench patch are supplied to the
owner as `yang_mills_zero_shift_local_fibres.zip`.

Proof SHA-256:
`42aa9ab14a4b42ba9d170803fb0f9ce9f0d1d763d10139b3a15f9ba317543e55`.
Proof Git blob:
`c7b1a0fb6d0da98d07e218655eb7aae6630ff6e6`.
Full decoded mathematical receipt SHA-256:
`3b68db08b411f55c39c0b3f3cd7d1401c321fded1cc0eba3250037e8dcca9e23`.

The complete local checker passed 408 named exact checks and 17 false-formula
controls normally and under Python optimization, with identical output.
A fresh standalone copied directory and a freshly applied full patch reproduced
the same receipt in both modes. Six command-line corruptions were each rejected
at their intended named error in both modes. Both unchanged predecessor
checkers also passed their original receipts. These are locally observed
executions, not GitHub CI or Lean runs. Finite exact algebra and interval
checks accompany the written analytic proofs; no external mathematical review
or historical-priority claim is made.

The next original quantity is the outer effective response in Z52 and full
restored state norm Z53 on growing physical observation families. This review
preserves that quantitative frontier without replacing it by a local-sector
mass-gap claim. No merge, paid model run, or scheduled process is performed.
