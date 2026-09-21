# Separate return through the original vacuum density

This supplementary calculation recomputes the susceptibility coefficients through the original source derivative and the full unit-vacuum density. It does not obtain them by differentiating the stored energy polynomial. It shares the explicitly retained original trace/Haar engine with the coefficient producer.

Let D(x)=exp(2v(x))=sum D_nu x^nu, with D_0=1. The exact Euler derivative gives

    |nu| D_nu=sum_(0<mu<=nu) 2|mu| v_mu D_(nu-mu).

This determines the full required density coefficient, including every ordered product. Its actual mass is Z_nu=P_H D_nu. For a numerator N(x), the coefficients of its original vacuum expectation A=N/Z obey

    A_nu=N_nu-sum_(0<mu<=nu) Z_mu A_(nu-mu),   Z_0=1.

For z_q=partial_xq v, its coefficient is (alpha_q+1)v_(alpha+e_q). Thus the direct original response is

    R_pq=[<W_p z_q>_rho-<W_p>_rho<z_q>_rho].

`source_expectation_check.py` executes these three finite coefficient equations on the actual source indices. No source-mass term is discarded. The required degree-four response uses the fifth source but no higher unknown source coefficient.

For one of the four paths connecting opposite cube faces, the two terms are

    density moment =186029/59136480,
    product of means=1132/369603,
    their difference=4909/59136480.

For the six-face cube source, the two terms are 83/3888 and 0. The complete opposite-face coefficient is therefore

    4*(4909/59136480)+83/3888=641033/29568240.

The file `source_expectation_receipt.json` retains all nine checked original source cases, their faces, multiindices, marked derivatives, both original expectation terms and the resulting connected entry. Cases include the one-face result, both diagonal adjacent-pair multiplicities, an off-diagonal adjacent pair, path/common-edge/corner triples, and the cube. Every value agrees with the independently differentiated sixth-energy polynomial.

The source equations and their coefficient expansions are exact. The full response at positive coupling receives the separately proved finite-volume analytic tail in P13-P22 of the main response proof; this supplementary calculation does not claim that its finite polynomial equals the entire response.

Replay from the cumulative root:

```sh
python -B supplementary_audits/source_expectation_check.py --verify-receipt supplementary_audits/source_expectation_receipt.json
python -O -B supplementary_audits/source_expectation_check.py --verify-receipt supplementary_audits/source_expectation_receipt.json
```
