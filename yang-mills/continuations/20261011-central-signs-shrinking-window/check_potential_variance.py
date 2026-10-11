"""Exact finite checks for PVI; analytic proofs are in the mathematical note."""
import json
from pathlib import Path
import sympy as s

out = Path(__file__).resolve().parent
y = s.symbols('y')
v = 5*(7*y-8)*(1-y)
z = 25*y*(1-y)
euclidean_mean = lambda f: s.integrate(4*y**3*s.expand(f), (y, 0, 1))
cov = lambda mean, f, g: s.factor(mean(f*g)-mean(f)*mean(g))
varv = cov(euclidean_mean, v, v)
covvz = cov(euclidean_mean, v, z)
assert varv == s.Rational(325, 18)
assert covvz == -s.Rational(775, 126)
assert varv+covvz == s.Rational(250, 21)

def beta_mean(f):
    return s.factor(sum(c*s.rf(s.Rational(9, 2), p[0])/s.rf(6, p[0])
                        for p, c in s.Poly(s.expand(f), y).terms()))

aa = 6*(8*y-9)*(1-y)
bb = 36*y*(1-y)
compact_cov = cov(beta_mean, aa, bb)
assert compact_cov == -s.Rational(8721, 784)
explicit_upper = compact_cov+s.Rational(7935, 10000)
assert explicit_upper < 0
assert 12+108*s.Rational(900, 391) < 261
assert 9+18*s.Rational(900, 391) < 51
assert 594+972*s.Rational(900, 391) < 2832
assert 2832+9*261+54*51 == 7935

alpha, M, Lambda, d, second, grad = s.symbols(
    'alpha M Lambda d second grad', real=True)
J2 = 36*M*M-36*M*d+9*second
c = 1+9*alpha/64
B = Lambda+9*alpha*M/16
D = 9*alpha*M*M/16
original = second+alpha*(J2/64-3*grad/32)-Lambda*d-alpha*(3*M-3*d/2)
rearranged = c*second-B*d+D-3*alpha*M+3*alpha*(16*d-grad)/32
assert s.expand(original-rearranged) == 0

result = {
    'euclidean_variance': str(varv),
    'euclidean_potential_score_covariance': str(covvz),
    'euclidean_half_laplacian_mean': str(varv+covvz),
    'compact_reference_covariance': str(compact_cov),
    'compact_epsilon_1_over_100_scaled_covariance_upper': str(explicit_upper),
    'compact_error_constants_checked': True,
    'parent_square_rearrangement_checked': True,
    'limitations': 'Polynomial checks supplement the full analytic proofs; no original-potential covariance sign is asserted.'
}
(out/'POTENTIAL_VARIANCE_CHECKS.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, indent=2))
