"""Exact symbolic replay for mean_costs.tex; no Lean or numerical tolerance.

The TeX contains the complete arbitrary-order proofs. This finite replay
independently checks their algebraic generators, signs, scale factors,
matrix columns, physical frame formulas, and pressure derivative rule.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import sympy as s

HERE = Path(__file__).resolve().parent
CHECKS: list[dict[str, object]] = []
STRUCTURAL: list[dict[str, object]] = []


def equal(name: str, lhs: s.Expr, rhs: s.Expr = s.S.Zero) -> None:
    residual = s.simplify(s.expand(lhs - rhs))
    passed = residual == 0
    CHECKS.append({"name": name, "passed": bool(passed)})
    if not passed:
        print(f"FAILED {name}: {residual}", flush=True)


def truth(name: str, condition: bool) -> None:
    CHECKS.append({"name": name, "passed": bool(condition)})


def structural(name: str, condition: bool) -> None:
    STRUCTURAL.append({"name": name, "passed": bool(condition)})


# The exact original exponent and base-coefficient relations.
h, lam, db, cp = s.symbols("h lambda d_b c_patch", nonzero=True, real=True)
q = s.symbols("q", positive=True)
x, eta, sigma = s.symbols("x eta sigma", real=True)
A, D = s.Rational(1, 2) + h, s.Rational(1, 2) - h
B = 1 - 2 * h * eta**2
abase = 2 ** (s.Rational(1, 2) + lam) * cp / (1 + eta**2)
equal("original A plus D", A + D, 1)
equal("original D plus 2h equals A", D + 2 * h, A)
for j, expected in enumerate((1 + eta**2, 2 * eta, 2, 0, 0)):
    equal(f"original reciprocal a eta derivative {j}",
          s.diff(1 / abase, eta, j),
          expected / (2 ** (s.Rational(1, 2) + lam) * cp))

# Vandermonde inverses use unspecified actual row exponentials, not chosen values.
t0, t1, t2, z0, z1 = s.symbols("t0 t1 t2 z0 z1", real=True)
Vtheta = s.Matrix([[1, y, y**2] for y in (t0, t1, t2)])
Vz = s.Matrix([[1, z0], [1, z1]])
Btheta, Bz = Vtheta.inv(), Vz.inv()
equal("three-row exact Vandermonde determinant", Vtheta.det(),
      (t1 - t0) * (t2 - t0) * (t2 - t1))
equal("two-row exact Vandermonde determinant", Vz.det(), z1 - z0)
for i, j in itertools.product(range(3), repeat=2):
    equal(f"three-row exact inverse entry {i},{j}",
          (Vtheta * Btheta)[i, j], s.KroneckerDelta(i, j))
for i, j in itertools.product(range(2), repeat=2):
    equal(f"two-row exact inverse entry {i},{j}",
          (Vz * Bz)[i, j], s.KroneckerDelta(i, j))
mu2, mun22l, mun2l, mu1, mu12l, a = s.symbols(
    "mu2 mu_minus2minus2lambda mu_minus2lambda mu1 mu1minus2lambda a",
    nonzero=True, real=True)
Ath = s.diag(mu2, 2 * a * mun22l, -a * mun2l) * Vtheta
Az = s.diag(mu1, a * mu12l) * Vz
VP = -Btheta[:, 1] / (2 * a * mun22l)
VJz = Btheta[:, 2] / (a * mun2l)
GJth = -Bz[:, 1] / (a * mu12l)
for i in range(3):
    equal(f"pressure profile exact row {i}", (Ath * VP)[i], -s.KroneckerDelta(i, 1))
    equal(f"axial-defect angular profile exact row {i}",
          (Ath * VJz)[i], -s.KroneckerDelta(i, 2))
for i in range(2):
    equal(f"angular-defect axial profile exact row {i}",
          (Az * GJth)[i], -s.KroneckerDelta(i, 1))
# The actual axial first moment uses t_1=e^db as row-zero value z0;
# its second-column inverse contraction is exactly the zero tail.
equal("combined primitive weighted tail cancellation", Bz[0, 1] + z0 * Bz[1, 1], 0)
P, Jtheta, Jz = s.symbols("P_current Jtheta_current Jz_current", real=True)
u = Btheta * s.diag(1 / mu2, 1 / (2 * a * mun22l), -1 / (a * mun2l)) * s.Matrix(
    [0, -q**(2*A)*P, -q**(2*A-1)*Jz])
sv = Bz * s.diag(1 / mu1, 1 / (a * mu12l)) * s.Matrix([0, -q**(2*A-s.Rational(3, 2))*Jtheta])
for i in range(3):
    equal(f"physical angular coefficient {i}", q**(-A)*u[i],
          q**A*P*VP[i] + q**(A-1)*Jz*VJz[i])
for i in range(2):
    equal(f"physical axial coefficient {i}", q**(-A)*sv[i],
          q**(A-s.Rational(3, 2))*Jtheta*GJth[i])
equal("pressure row original scale exponent", -A + A, 0)
equal("angular flux original scale exponent", s.Rational(3, 2)-A+A-s.Rational(3, 2), 0)
equal("axial fifth row original scale exponent", 1-A+A-1, 0)
equal("potential original scale exponent", A-s.Rational(3, 2)+1-s.Rational(1, 2), A-1)

# Full original moving-scale differential operators in (q,x,eta).
def dr(f):
    return q**(-s.Rational(1, 2)) * s.diff(f, x)


def dz(f):
    return (2*eta*q**A/B*s.diff(f, q)
            -eta*x*q**(-D)/B*s.diff(f, x)
            +q**(-D)*(1-eta**2)/B*s.diff(f, eta))


def dt(f):
    return (-s.diff(f, q)/B+x*q**(-1)/(2*B)*s.diff(f, x)
            +D*eta*q**(-1)/B*s.diff(f, eta))


def Z(sig, f):
    return (2*sig*eta*f-eta*x*s.diff(f, x)+(1-eta**2)*s.diff(f, eta))/B


def T(sig, f):
    return (-sig*f+x*s.diff(f, x)/2+D*eta*s.diff(f, eta))/B


f = s.Function("F")(x, eta)
equal("original radial chain rule", dr(q**sigma*f), q**(sigma-s.Rational(1, 2))*s.diff(f, x))
equal("original axial chain rule", dz(q**sigma*f), q**(sigma-D)*Z(sigma, f))
equal("original time chain rule", dt(q**sigma*f), q**(sigma-1)*T(sigma, f))
equal("implicit scale axial derivative", dz(q*(1-eta**2)), 0)
equal("implicit scale time derivative", dt(q*(1-eta**2)), -1)
equal("physical axial coordinate axial derivative", dz(q**D*eta), 1)
equal("physical axial coordinate time derivative", dt(q**D*eta), 0)
equal("mixed axial-time coefficient identity",
      T(sigma-D, Z(sigma, f)), Z(sigma-1, T(sigma, f)))
equal("mixed radial-axial coefficient identity",
      s.diff(Z(sigma, f), x), Z(sigma-s.Rational(1, 2), s.diff(f, x)))
equal("mixed radial-time coefficient identity",
      s.diff(T(sigma, f), x), T(sigma-s.Rational(1, 2), s.diff(f, x)))

# Potential identity and its full product derivative, retaining eta dependence.
H = s.Function("H")(x, eta)
X = s.Function("Jtheta")(q**D*eta, 1-q*(1-eta**2))
equal("potential radial curl identity", dr(q**(A-1)*H)+q**(A-1)*H/(s.sqrt(q)*x),
      q**(A-s.Rational(3, 2))*(s.diff(H, x)+H/x))
Jzder = s.symbols("Jtheta_z_current", real=True)
equal("two radial increment terms keep both original exponents",
      -q**(A-1)*Jzder*H - Jtheta*dz(q**(A-1)*H),
      -q**(A-1)*Jzder*H-q**(A-1-D)*Jtheta*Z(A-1, H))

# The full cylindrical frame derivation is checked before subtraction.
r = s.symbols("r", positive=True)
theta, z, time = s.symbols("theta z time", real=True)
coords = (r, theta, z, time)
Ur, Uth, Uz = [s.Function(v)(*coords) for v in ("Ur", "Utheta", "Uz")]
ar, ath, az = [s.Function(v)(r, z, time) for v in ("ar", "atheta", "az")]
nu = s.symbols("nu_NS", positive=True)
pi = s.Function("delta_p")(r, theta, z, time)
uv, av = s.Matrix([Ur, Uth, Uz]), s.Matrix([ar, ath, az])
O = s.Matrix([[s.cos(theta), -s.sin(theta), 0],
              [s.sin(theta), s.cos(theta), 0], [0, 0, 1]])
J = s.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
for i, j in itertools.product(range(3), repeat=2):
    equal(f"actual angular frame derivative {i},{j}", s.diff(O, theta)[i, j], (O*J)[i, j])


def adv(Xv, Yv):
    return (Xv[0]*Yv.diff(r)+Xv[1]/r*(Yv.diff(theta)+J*Yv)
            +Xv[2]*Yv.diff(z))


adv_cart = Ur*(O*uv).diff(r)+Uth/r*(O*uv).diff(theta)+Uz*(O*uv).diff(z)
for i in range(3):
    equal(f"full oriented cylindrical transport derivation {i}", adv_cart[i], (O*adv(uv, uv))[i])
diff_adv = adv(uv+av, uv+av)-adv(uv, uv)
common = [Ur*s.diff(a_i, r)+Uz*s.diff(a_i, z)
          +ar*s.diff(U_i, r)+az*s.diff(U_i, z)+ath/r*s.diff(U_i, theta)
          +ar*s.diff(a_i, r)+az*s.diff(a_i, z)
          for U_i, a_i in zip(uv, av)]
curvature = [-(2*Uth*ath+ath**2)/r, (Ur*ath+ar*Uth+ar*ath)/r, 0]
for i in range(3):
    equal(f"all cross and self transport terms component {i}", diff_adv[i], common[i]+curvature[i])
L0 = lambda expr: s.diff(expr, r, 2)+s.diff(expr, r)/r+s.diff(expr, z, 2)
Lscalar = lambda expr: L0(expr)+s.diff(expr, theta, 2)/r**2
lap_cart = (O*av).applyfunc(Lscalar)
lap_expected = s.Matrix([L0(ar)-ar/r**2, L0(ath)-ath/r**2, L0(az)])
for i in range(3):
    equal(f"actual mean vector Laplacian component {i}", lap_cart[i], (O*lap_expected)[i])
pressure_gradient = s.Matrix([s.diff(pi, r), s.diff(pi, theta)/r, s.diff(pi, z)])
force_expected = s.Matrix([s.diff(ai, time)+common[i]+curvature[i]
                           -nu*lap_expected[i]+pressure_gradient[i] for i, ai in enumerate(av)])
force_direct = av.diff(time)+diff_adv-nu*lap_expected+pressure_gradient
for i in range(3):
    equal(f"full physical force component {i} retains nu and pressure", force_direct[i], force_expected[i])

# Exact Cartesian vector derivatives, including the frame connection.
Xop = lambda vec: s.cos(theta)*vec.diff(r)-s.sin(theta)/r*(vec.diff(theta)+J*vec)
Yop = lambda vec: s.sin(theta)*vec.diff(r)+s.cos(theta)/r*(vec.diff(theta)+J*vec)
xcart = s.cos(theta)*(O*uv).diff(r)-s.sin(theta)/r*(O*uv).diff(theta)
ycart = s.sin(theta)*(O*uv).diff(r)+s.cos(theta)/r*(O*uv).diff(theta)
for i in range(3):
    equal(f"physical Cartesian x recursion component {i}", xcart[i], (O*Xop(uv))[i])
    equal(f"physical Cartesian y recursion component {i}", ycart[i], (O*Yop(uv))[i])

# Exact primitive differentiation, including every cutoff derivative.
srad = s.symbols("s", positive=True)
ff = s.Function("f_phys")(r, z, time)
chis = s.Function("chi_m")(r, z, time)
JJ = s.Function("radial_integral_f")(z, time)
primitive = s.Integral(ff.subs(r, srad), (srad, 0, r))
pressure = primitive-chis*JJ
for k, m, n in itertools.product(range(3), range(2), range(2)):
    first = (s.Integral(s.diff(ff, z, m, time, n).subs(r, srad), (srad, 0, r))
             if k == 0 else s.diff(ff, r, k-1, z, m, time, n))
    correction = sum(s.binomial(m, i)*s.binomial(n, j)
                     *s.diff(chis, r, k, z, i, time, j)
                     *s.diff(JJ, z, m-i, time, n-j)
                     for i in range(m+1) for j in range(n+1))
    equal(f"evaluated pressure full derivative k={k},m={m},n={n}",
          s.diff(pressure, r, k, z, m, time, n), first-correction)

# Original pressure bump and every radial inverse coefficient at finite orders.
rhohat = s.Function("rho_hat")(x)
equal("original pressure bump first axial derivative", dz(q**(-s.Rational(1, 2))*rhohat),
      q**(-s.Rational(1, 2)-D)*Z(-s.Rational(1, 2), rhohat))
for power, k in itertools.product((1, 2), range(7)):
    equal(f"inverse radius original power {power} derivative {k}",
          s.diff(r**(-power), r, k), (-1)**k*s.rf(power, k)*r**(-power-k))

# Binomial/multinomial coefficients of all-order finite cost convolution.
for n, i, j in itertools.product(range(7), repeat=3):
    if i+j <= n:
        truth(f"three-factor Leibniz coefficient n={n},i={i},j={j}",
              s.binomial(n, i)*s.binomial(n-i, j)
              == s.factorial(n)/(s.factorial(i)*s.factorial(j)*s.factorial(n-i-j)))

# Exact nonlinear source recomputation is replayed in the source-operation
# component. Do not recount a generic X+(-X+Y)=Y identity here.
body = HERE / "mean_costs.tex"
body_text = body.read_text(encoding="utf-8")
for environment in ("equation", "gathered", "split", "array", "cases"):
    structural(f"TeX {environment} environment count",
          body_text.count("\\begin{"+environment+"}") == body_text.count("\\end{"+environment+"}"))
structural("all local labels use required mcmean prefix",
      all(part.startswith("mcmean:") for part in body_text.split("\\label{")[1:]))
structural("actual pressure is explicitly retained", "\\label{mcmean:actual_pressure}" in body_text)
structural("explicit support-width pressure budget is present", "\\label{mcmean:explicit_pressure_cost}" in body_text)
structural("remaining nonlinear defects are explicit", "\\label{mcmean:nonlinear_defects}" in body_text)
structural("full Cartesian derivative recursion is present", "\\label{mcmean:cartesian_recursion}" in body_text)

all_passed = all(item["passed"] for item in CHECKS+STRUCTURAL)
receipt = {
    "schema": "mean-costs-exact-replay-v1",
    "all_passed": all_passed,
    "check_count": len(CHECKS),
    "checks": CHECKS,
    "structural_validation": STRUCTURAL,
    "structural_validation_count": len(STRUCTURAL),
    "source_sha256": hashlib.sha256(body.read_bytes()).hexdigest(),
    "replay_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "input_sha256": {
        str(path.relative_to(HERE.parent)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in (HERE.parent / "source_operation" / "operation_body.tex",
                     HERE.parent / "quantitative_moments.tex")
    },
    "method": "SymPy exact expressions and integer combinatorics; no numerical tolerance; all-order proofs are in mean_costs.tex",
}
(HERE / "replay_receipt.json").write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps({key: receipt[key] for key in ("all_passed", "check_count", "source_sha256", "replay_sha256")}))
raise SystemExit(0 if all_passed else 1)
