"""Independent exact algebra replay for the actual third-growth derivatives.

Analytic bounds are proved in derivative_costs.tex.  These checks compare
direct differentiation of the original expressions, and an independent Lie
derivative implementation, against the displayed finite derivative rules.
No floating point evaluation, Lean invocation, or source-file parsing is used.
"""
from __future__ import annotations

from datetime import datetime, timezone
from hashlib import sha256
from itertools import product
from math import factorial
from pathlib import Path
import json
import sympy as s

BASE = Path(__file__).resolve().parent
checks: list[dict[str, str]] = []


def zero(name: str, expr: s.Expr | s.Matrix) -> None:
    values = list(expr) if isinstance(expr, s.MatrixBase) else [expr]
    residuals = [s.simplify(s.expand(value)) for value in values]
    if any(value != 0 for value in residuals):
        raise AssertionError((name, residuals))
    checks.append({"name": name, "result": "pass"})


def positive(name: str, expr: s.Expr) -> None:
    value = s.simplify(expr)
    if value.is_positive is not True:
        raise AssertionError((name, value, value.is_positive))
    checks.append({"name": name, "result": "pass"})


a, b, c, d, K1, K2, K3, Sstar, Cstar = s.symbols(
    "a b c d K1 K2 K3 Sstar Cstar", positive=True
)
h, W, A, P, g = s.symbols("h W A P g", positive=True)
chi = s.sqrt(h**2 + a**2)
R = g**2 + b**2
Nfull = b * (A + Cstar) + g * Sstar + c * K2 * P
parent_original = {
    h: a * W,
    W: a * A / chi - d * K1**2 * W,
    A: -Sstar * W - d * K1**2 * A,
    P: -d * K2**2 * chi**2 * P,
    g: b * W,
}


def original_dt(expr: s.Expr) -> s.Expr:
    return sum(s.diff(expr, variable) * rate
               for variable, rate in parent_original.items())


E = b * K1**2 * A + c * K2**3 * chi**2 * P
zero("full numerator differentiation retains both parent losses",
     original_dt(Nfull) + d * E)
zero("original phase length derivative", original_dt(R) - 2 * b * g * W)
zero("original chi derivative", original_dt(chi) - a * h * W / chi)
a3 = Nfull / (K3 * R)
b3 = K3 * c / chi
lam = d * K3**2 * R
zero("a3 logarithmic rate from original numerator and geometry",
     original_dt(a3) + a3 * (d * E / Nfull + 2 * b * g * W / R))
zero("b3 rate from original inverse phase length",
     original_dt(b3) + b3 * a * h * W / chi**2)
zero("lambda3 rate contains d K3 squared",
     original_dt(lam) - 2 * d * K3**2 * b * g * W)
zero("inverse chi derivative", original_dt(1 / chi) + a * h * W / chi**3)
zero("inverse R derivative", original_dt(1 / R) + 2 * b * g * W / R**2)

Theta, Omega, P3, u, aa, bb, ll = s.symbols(
    "Theta Omega P3 u aa bb ll", nonzero=True
)
pair_theta = aa * Omega - ll * Theta
pair_omega = bb * Theta - ll * Omega
zero("signed Theta first derivative", pair_theta.subs(
    {Theta: -P3, Omega: -P3 * u}) + P3 * (aa * u - ll))
zero("signed Omega first derivative", pair_omega.subs(
    {Theta: -P3, Omega: -P3 * u}) + P3 * (bb - ll * u))
zero("quotient diffusion cancellation in actual common-diffusion pair",
     (pair_omega * Theta - Omega * pair_theta) / Theta**2
     - (bb - aa * (Omega / Theta)**2))
gamma, ui, seed, birth_damping = s.symbols(
    "gamma ui seed birth_damping", positive=True
)
birth_matrix = s.Matrix([[-birth_damping, gamma / ui],
                        [gamma * ui, -birth_damping]])
zero("original signed birth derivative", birth_matrix * s.Matrix(
    [-seed, -seed * ui])
    + seed * (gamma - birth_damping) * s.Matrix([1, ui]))
daa, dbb, dll = s.symbols("daa dbb dll")
matrix = s.Matrix([[-ll, aa], [bb, -ll]])
matrix_dt = s.Matrix([[-dll, daa], [dbb, -dll]])
zero("full second derivative matrix including lambda derivative and square",
     matrix_dt + matrix**2 - s.Matrix([
         [ll**2 + aa * bb - dll, daa - 2 * ll * aa],
         [dbb - 2 * ll * bb, ll**2 + aa * bb - dll],
     ]))
Rbar = s.Rational(265, 256)**2
positive("retained rational R upper bound is less than two", 2 - Rbar)
positive("Theta lower derivative exceeds gamma over eight sqrt two",
         (1 / (4 * s.sqrt(2)) - Rbar / (16 * s.sqrt(2)))
         - 1 / (8 * s.sqrt(2)))
positive("Omega lower derivative exceeds gamma ui over four",
         s.Rational(1, 2) - Rbar / (8 * s.sqrt(2)) - s.Rational(1, 4))

# Independent finite-order check: direct Lie derivatives of the closed
# polynomial vector field versus the ordinary multinomial recurrences.
q, nn, j = s.symbols("q nn j", positive=True)
states = (h, W, A, P, q, g, nn, j)
rates = {
    h: a * W,
    W: a * A * q - d * K1**2 * W,
    A: -Sstar * W - d * K1**2 * A,
    P: -d * K2**2 * (h**2 + a**2) * P,
    q: -a * h * W * q**3,
    g: b * W,
    nn: -d * b * K1**2 * A - d * c * K2**3 * (h**2 + a**2) * P,
    j: -2 * b * g * W * j**2,
}


def lie(expr: s.Expr, field: dict[s.Symbol, s.Expr] = rates) -> s.Expr:
    return s.expand(sum(s.diff(expr, variable) * rate
                        for variable, rate in field.items()))


def muljet(n: int, *arrays: list[s.Expr]) -> s.Expr:
    total = s.S.Zero
    for indices in product(range(n + 1), repeat=len(arrays)):
        if sum(indices) != n:
            continue
        coefficient = factorial(n)
        term = s.S.One
        for array, index in zip(arrays, indices):
            term *= array[index]
        denominator = 1
        for index in indices:
            denominator *= factorial(index)
        total += s.Integer(coefficient // denominator) * term
    return s.expand(total)


invchi_defect = q**2 * (h**2 + a**2) - 1
zero("inverse chi invariant has exact multiplicative defect evolution",
     lie(invchi_defect) + 2 * a * h * W * q**2 * invchi_defect)
invR_defect = j * (g**2 + b**2) - 1
zero("inverse R invariant has exact multiplicative defect evolution",
     lie(invR_defect) + 2 * b * g * W * j * invR_defect)
zero("independent numerator equals full parent sum along its exact ODE",
     lie(nn - Nfull))
zero("oriented determinant invariant remains constant", lie(b * h - a * g))

jets: dict[s.Symbol, list[s.Expr]] = {variable: [variable] for variable in states}
direct: dict[s.Symbol, s.Expr] = {variable: variable for variable in states}
Xjets: list[s.Expr] = []
for n in range(3):
    Xjets.append(muljet(n, jets[h], jets[h]) + (a**2 if n == 0 else 0))
    next_jets = {
        h: a * jets[W][n],
        W: a * muljet(n, jets[A], jets[q]) - d * K1**2 * jets[W][n],
        A: -Sstar * jets[W][n] - d * K1**2 * jets[A][n],
        P: -d * K2**2 * muljet(n, Xjets, jets[P]),
        q: -a * muljet(n, jets[h], jets[W], jets[q], jets[q], jets[q]),
        g: b * jets[W][n],
        nn: -d * b * K1**2 * jets[A][n]
            - d * c * K2**3 * muljet(n, Xjets, jets[P]),
        j: -2 * b * muljet(n, jets[g], jets[W], jets[j], jets[j]),
    }
    for variable in states:
        direct[variable] = lie(direct[variable])
        zero(f"parent ordinary derivative recurrence {variable}, order {n + 1}",
             next_jets[variable] - direct[variable])
    for variable in states:
        jets[variable].append(s.expand(next_jets[variable]))

y1, y2 = s.symbols("y1 y2")
coefficient_matrix = s.Matrix([
    [-d * K3**2 * (g**2 + b**2), nn * j / K3],
    [K3 * c * q, -d * K3**2 * (g**2 + b**2)],
])
full_field = dict(rates)
raw_pair = coefficient_matrix * s.Matrix([y1, y2])
full_field.update({y1: raw_pair[0], y2: raw_pair[1]})
matrix_jets = [coefficient_matrix]
for _ in range(3):
    matrix_jets.append(matrix_jets[-1].applyfunc(lie))
amplitude_jets = [s.Matrix([y1, y2])]
raw_amplitude = s.Matrix([y1, y2])
for n in range(4):
    candidate = s.zeros(2, 1)
    for k in range(n + 1):
        candidate += s.binomial(n, k) * matrix_jets[k] * amplitude_jets[n - k]
    raw_amplitude = raw_amplitude.applyfunc(lambda expr: lie(expr, full_field))
    for component in range(2):
        zero(f"actual amplitude Lie derivative, order {n + 1}, component {component + 1}",
             candidate[component] - raw_amplitude[component])
    amplitude_jets.append(candidate.applyfunc(s.expand))

v, tbase, alpha_clock, Qlabel, hsrc = s.symbols(
    "v tbase alpha_clock Qlabel hsrc", positive=True
)
f = s.Function("f")
for n in range(1, 4):
    x = s.Symbol("x")
    zero(f"constant source-clock derivative factor, order {n}",
         s.diff(f(tbase + alpha_clock * v), v, n)
         - alpha_clock**n * s.Subs(s.diff(f(x), x, n), x, tbase + alpha_clock * v))

receipt = {
    "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    "check_count": len(checks),
    "checks": checks,
    "scope": "Exact algebra and finite-order independent derivative replay; analytic all-orders bounds are proved in derivative_costs.tex.",
    "sources": {
        path.name: sha256(path.read_bytes()).hexdigest()
        for path in (BASE / "derivative_costs.tex", Path(__file__).resolve())
    },
}
(BASE / "replay_receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": "pass", "check_count": len(checks), "receipt": str(BASE / "replay_receipt.json")}))
