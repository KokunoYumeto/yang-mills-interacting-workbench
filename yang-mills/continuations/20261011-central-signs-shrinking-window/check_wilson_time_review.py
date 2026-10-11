"""Exact and high-precision checks for INDEPENDENT_REVIEW.md.

These checks supplement the proof. They do not sample a vacuum distribution.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction
import hashlib
import json
import math
import sympy as s
import mpmath as mp

HERE = Path(__file__).resolve().parent
I = s.I
sigma = [
    s.Matrix([[0, 1], [1, 0]]),
    s.Matrix([[0, -I], [I, 0]]),
    s.Matrix([[1, 0], [0, -1]]),
]
generators = [-I * a / 2 for a in sigma]
eye = s.eye(2)
counts = Counter()

def unitary(seed):
    # Rational stereographic points of the unit quaternion sphere.
    t = [s.Rational(seed + 1, seed + 4),
         s.Rational(2 * seed + 1, 3 * seed + 7),
         s.Rational(seed + 2, 4 * seed + 9)]
    d = 1 + sum(x*x for x in t)
    q = [(1 - sum(x*x for x in t))/d] + [2*x/d for x in t]
    return q[0]*eye - I*sum((q[a+1]*sigma[a] for a in range(3)), s.zeros(2))

def product(seq):
    out = eye
    for x in seq:
        out = out*x
    return s.simplify(out)

def occurrence_gradient(word, links, edge):
    matrices = [links[e] if sign == 1 else links[e].H for e, sign in word]
    values = []
    for T in generators:
        val = 0
        for position, (e, sign) in enumerate(word):
            if e != edge:
                continue
            derivative = T*links[e] if sign == 1 else -links[e].H*T
            val += s.trace(product(matrices[:position] + [derivative] + matrices[position+1:]))
        values.append(s.simplify(val))
    return values

links = {e: unitary(e) for e in range(5)}
for e, U in links.items():
    assert s.simplify(U.H*U - eye) == s.zeros(2)
    assert s.simplify(U.det()) == 1
    x = s.trace(U)/2
    lap = sum(s.trace(T*T*U)/2 for T in generators)
    assert s.simplify(lap + 3*x/4) == 0
    counts["exact_SU2_metric_checks"] += 1

words = [
    [(0, 1), (1, 1), (2, -1), (3, -1)],
    [(2, 1), (4, -1), (1, -1), (3, 1)],
    [(0, 1), (1, 1), (0, -1), (2, 1), (3, -1)],
    [(0, 1), (1, 1), (0, 1), (1, -1), (0, -1)],
    [(0, 1), (0, -1), (1, 1), (2, 1), (1, -1)],
]
for word in words:
    G = product([links[e] if sign == 1 else links[e].H for e, sign in word])
    W = s.simplify(s.trace(G))
    one = s.simplify(1 - W*W/4)
    multiplicity = Counter(e for e, sign in word)
    gamma = 0
    for e in multiplicity:
        grad = occurrence_gradient(word, links, e)
        squared = s.simplify(sum(v*v for v in grad))
        if multiplicity[e] == 1:
            assert s.simplify(squared - one) == 0
        assert squared <= multiplicity[e]**2 * one
        gamma += squared
        counts["exact_oriented_edge_derivative_checks"] += 1
    assert s.simplify(gamma) <= sum(v*v for v in multiplicity.values())*one
    counts["full_repeated_word_bounds"] += 1

def face_edges(base, d, e):
    x = list(base)
    xd, xe = x.copy(), x.copy()
    xd[d] += 1
    xe[e] += 1
    return [(tuple(x), d), (tuple(xd), e), (tuple(xe), d), (tuple(x), e)]

for m in range(1, 10):
    n = m + 1
    all_incidence = Counter()
    for d, e in [(0, 1), (0, 2), (1, 2)]:
        incident = Counter()
        face_count = 0
        for i in range(n):
            for k in range(n):
                for l in range(n):
                    x = (i, k, l)
                    if x[d] == m or x[e] == m:
                        continue
                    for edge in face_edges(x, d, e):
                        incident[edge] += 1
                        all_incidence[edge] += 1
                    face_count += 1
        assert face_count == m*m*n
        assert sum(incident.values()) == 4*m*m*n
        assert sum(v*v for v in incident.values()) == 4*m*n*(2*m - 1)
        assert set(incident.values()).issubset({1, 2})
        counts["exact_orientation_boundary_counts"] += 1
    assert max(all_incidence.values()) <= 4
    assert sum(all_incidence.values()) == 12*m*m*n
    counts["all_face_boundary_incidence_checks"] += 1

# Distinct Laplacian and score-drift symbols are preserved under reversal.
t, T, v, r = s.symbols("t T v r", positive=True)
laplace_coefficients = s.symbols("a0:5")
score_coefficients = s.symbols("d0:5")
for degree in range(5):
    ell = sum((laplace_coefficients[k]+score_coefficients[k])*r**k
              for k in range(degree+1))
    original = s.integrate(ell, (r, 0, t))
    backward = s.integrate(ell.subs(r, T-v), (v, T-t, T))
    assert s.simplify(backward-original) == 0
    counts["full_drift_time_substitution_checks"] += 1

f, fx, fxx, psi, psix, psixx, kap, potential, energy = s.symbols(
    "f fx fxx psi psix psixx kap potential energy", nonzero=True)
expanded = (kap*(psixx*f+2*psix*fx+psi*fxx)-(potential-energy)*psi*f)/psi
vacuum_substitution = {psixx: (potential-energy)*psi/kap}
assert s.simplify(expanded.subs(vacuum_substitution)-(kap*fxx+2*kap*psix*fx/psi)) == 0
counts["full_ground_transform_jet_check"] += 1

for p in range(1, 17):
    lower = s.factorial2(2*p-3) if p > 1 else 1
    ito_coefficient = p*(2*p-1)*lower*s.Rational(1, p)
    assert ito_coefficient == s.factorial2(2*p-1)
    counts["exact_even_moment_coefficients"] += 1
assert 3*8**2 == 192
assert s.Rational(5, 2)**2 == s.Rational(25, 4)

B, rho = s.symbols("B rho", positive=True)
U = [s.Integer(1), B]
for k in range(1, 13):
    U.append(s.expand(B*U[k]+rho*rho*k*k*U[k-1]))
assert U[2] == B*B+rho*rho
assert s.expand(U[3]-(B**3+5*B*rho*rho)) == 0
assert s.expand((B+rho*s.Symbol("k"))**2
                -(B*(B+rho*s.Symbol("k"))+rho*rho*s.Symbol("k")**2)) == B*rho*s.Symbol("k")
for b in map(s.Rational, [s.Rational(1, 7), 1, 7, 100]):
    for rr in map(s.Rational, [s.Rational(1, 11), 1, 5]):
        for k in range(1, 14):
            assert U[k].subs({B: b, rho: rr}) <= (b+rr*k)**k
            counts["exact_curvature_moment_majorants"] += 1
        for factor in [4, 5, 13, 37]:
            z = factor*rr
            k = s.floor(z/(2*rr))
            assert k >= z/(4*rr)
            assert (b+rr*k)/(b+z) <= 1-z/(2*(b+z))
            counts["exact_tail_rounding_checks"] += 1

mp.mp.dps = 65
for alpha in [mp.mpf(1)/20, mp.mpf(1)/4, mp.mpf(49)/100]:
    smaller = 2**alpha*(1+2/(2**alpha-1))
    owner = 2**(alpha+1)/(1-2**(-alpha))
    assert smaller <= owner
    counts["dyadic_constant_comparisons"] += 1
for aa in [mp.log(2)+mp.mpf("0.1"), 1, 2, 5]:
    series = mp.nsum(lambda n: 2**(n+1)*mp.exp(-aa*(n+1)), [0, mp.inf])
    closed = 2*mp.exp(-aa)/(1-2*mp.exp(-aa))
    assert abs(series-closed) < mp.mpf("1e-50")
    counts["log_modulus_tail_series"] += 1

path_rows = []
for kappa in [mp.mpf("0.25"), mp.mpf("1"), mp.mpf("13")]:
    for j in [2, 5, 20, 100, 1000]:
        m = mp.mpf(2)*j**4
        n = m+1
        K = m*m*n
        N, M = 3*m*n*n, 3*K
        g2 = kappa/(200*j)
        budget = min(2*M, 6*g2*mp.sqrt(N*M))
        rr = 4*g2
        eps = budget/M
        D = 4*m*n*(2*m-1)/(K*K)
        Q = min(4*eps, (budget*budget+rr*rr)/(3*K*K))
        assert D <= 8/K
        assert mp.almosteq(4*(2*g2/(mp.mpf(1)/(100*j)))/(1/(2*g2*(mp.mpf(1)/(100*j)))), rr*rr)
        path_rows.append({
            "kappa": str(kappa), "j": j,
            "j_B_over_K": mp.nstr(j*budget/K, 25),
            "j2_Q": mp.nstr(j*j*Q, 25),
            "j12_D": mp.nstr(j**12*D, 25),
            "max_L2_bound_T1": mp.nstr((mp.sqrt(Q)+mp.mpf("2.5")*mp.sqrt(2*kappa*D))**2, 25),
        })
        counts["original_path_finite_factor_checks"] += 1
    assert abs(j*budget/K-9*kappa/100) < mp.mpf("1e-12")
    assert abs(j*j*Q-27*kappa*kappa/10000) < mp.mpf("1e-12")
    assert abs(j**12*D-1) < mp.mpf("1e-11")
    assert abs((budget*budget/(D*K*K*j**10))-81*kappa*kappa/10000) < mp.mpf("1e-11")
    counts["original_path_asymptotic_checks"] += 4

result = {
    "status": "PASS",
    "scope": "Exact algebra/incidences and high-precision constants; no vacuum sampling.",
    "counts": dict(counts),
    "total_assertion_groups": sum(counts.values()),
    "path_rows": path_rows,
}
(HERE/"WILSON_TIME_REVIEW_CHECKS.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "counts": result["counts"],
                  "total_assertion_groups": result["total_assertion_groups"]}, indent=2))
