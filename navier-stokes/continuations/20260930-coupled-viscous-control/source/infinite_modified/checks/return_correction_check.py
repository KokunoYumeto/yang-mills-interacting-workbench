"""Exact replay of signed residuals and the compact return-core correction."""

from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import json
import math
import re

import sympy as s

HERE = Path(__file__).resolve().parent
PROOF = HERE.parent / "return_correction_body.tex"
OUT = HERE / "return_correction_receipt.json"
x, y, t = s.symbols("x y t", real=True)
coords = (x, y, t)
X = s.Matrix([x, y])
J = s.Matrix([[0, -1], [1, 0]])
e2 = s.Matrix([0, 1])
delta = s.Rational(3, 7)
checks = {}


def zero(value):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    assert all(s.simplify(s.expand(entry)) == 0 for entry in entries), value


def grad(f):
    return s.Matrix([s.diff(f, x), s.diff(f, y)])


def lap(f):
    if isinstance(f, s.MatrixBase):
        return f.applyfunc(lap)
    return s.diff(f, x, 2) + s.diff(f, y, 2)


def residual(theta, u, p):
    scalar = s.diff(theta, t) + u.dot(grad(theta)) - delta * lap(theta)
    vector = u.diff(t) + u.jacobian(X) * u + grad(p) - delta * lap(u) - theta * e2
    return s.expand(scalar), vector.applyfunc(s.expand)


def multiindices(order):
    return [a for a in product(range(order + 1), repeat=3) if sum(a) <= order]


@lru_cache(None)
def jet(f, alpha):
    return s.diff(f, *[(coords[j], alpha[j]) for j in range(3)])


def plus(a, index, amount=1):
    b = list(a)
    b[index] += amount
    return tuple(b)


point = {x: s.Rational(2, 3), y: s.Rational(-3, 5), t: s.Rational(5, 7)}


def value(f, alpha):
    return jet(f, alpha).subs(point)


def leibniz_at(left, right, alpha, shift=None):
    result = 0
    for beta in product(*(range(n + 1) for n in alpha)):
        complement = tuple(alpha[j] - beta[j] for j in range(3))
        if shift is not None:
            complement = plus(complement, shift)
        result += math.prod(math.comb(alpha[j], beta[j]) for j in range(3)) * value(left, beta) * value(right, complement)
    return result


# Independently expand the PDE first, then compare every signed Leibniz jet.
parent_theta = 2 * x**2 * y + t * y**3 - 3 * x * t**2
parent_psi = x**3 * y**2 + 2 * t * x * y**3 - y * t**3
parent_u = J * grad(parent_psi)
parent_p = x**2 + 3 * t * x * y - 2 * y**3
inc_theta = x**2 * t**2 - 2 * y**3 * t + 7 * x * y
inc_psi = x**2 * y**3 + 3 * x * t**2 - y**2 * t
inc_u = J * grad(inc_psi)
inc_p = x * y * t**2 + x**3 - 3 * y
old_theta_force, old_u_force = residual(parent_theta, parent_u, parent_p)
total_theta_force, total_u_force = residual(
    parent_theta + inc_theta, parent_u + inc_u, parent_p + inc_p
)
actual_scalar = s.expand(total_theta_force - old_theta_force)
actual_vector = (total_u_force - old_u_force).applyfunc(s.expand)
D = parent_u.jacobian(X)
G = grad(parent_theta)
signed_cases = 0
for alpha in multiindices(4):
    scalar = value(inc_theta, plus(alpha, 2))
    for i in range(2):
        scalar += leibniz_at(parent_u[i] + inc_u[i], inc_theta, alpha, i)
        scalar += leibniz_at(inc_u[i], G[i], alpha)
        scalar -= delta * value(inc_theta, plus(alpha, i, 2))
    assert scalar == value(actual_scalar, alpha)
    signed_cases += 1
    for k in range(2):
        vector = value(inc_u[k], plus(alpha, 2)) + value(inc_p, plus(alpha, k))
        for i in range(2):
            vector += leibniz_at(parent_u[i] + inc_u[i], inc_u[k], alpha, i)
            vector += leibniz_at(D[k, i], inc_u[i], alpha)
            vector -= delta * value(inc_u[k], plus(alpha, i, 2))
        if k == 1:
            vector -= value(inc_theta, alpha)
        assert vector == value(actual_vector[k], alpha)
        signed_cases += 1
checks["signed_space_time_jet_cases"] = signed_cases

# Actual correction identity compared with full PDE subtraction.
h = x * y**2 * t - x**3
z = J * grad(x**3 * t + x * y**2 * t**2)
kappa = x**2 * y * t + y**2 * t**3
theta_total = parent_theta + inc_theta
u_total = parent_u + inc_u
new_scalar, new_vector = residual(theta_total + h, u_total + z, parent_p + inc_p + kappa)
delta_scalar = s.diff(h, t) + u_total.dot(grad(h)) + z.dot(grad(theta_total)) + z.dot(grad(h)) - delta * lap(h)
delta_vector = z.diff(t) + z.jacobian(X) * u_total + u_total.jacobian(X) * z + z.jacobian(X) * z + grad(kappa) - delta * lap(z) - h * e2
zero(new_scalar - total_theta_force - delta_scalar)
zero(new_vector - total_u_force - delta_vector)
zero(z.jacobian(X).trace())
checks["full_correction_PDE_subtraction"] = True

# Exact local pressure--buoyancy cancellation; unsigned row remains 2.
f_theta, f_u = residual(y, s.zeros(2, 1), y**2 / 2)
zero(f_theta)
zero(f_u)
checks["zero_force_unsigned_majorant_counterexample"] = {"actual_residual": 0, "unsigned_second_row": 2}

# Full shifted chart, inverse and force weights with nonzero pressure.
chart_cases = 0
for a in (s.Rational(2, 3), s.Rational(3, 2)):
    xi = (s.Rational(-1, 4), s.Rational(2, 7))
    tau0 = s.Rational(3, 5)
    subs = {x: xi[0] + a * x, y: xi[1] + a * y, t: tau0 + a**2 * t}
    theta_new = a**3 * parent_theta.subs(subs, simultaneous=True)
    u_new = a * parent_u.subs(subs, simultaneous=True)
    p_new = a**2 * parent_p.subs(subs, simultaneous=True)
    force_theta, force_u = residual(theta_new, u_new, p_new)
    zero(force_theta - a**5 * old_theta_force.subs(subs, simultaneous=True))
    zero(force_u - a**3 * old_u_force.subs(subs, simultaneous=True))
    inv = {x: (x - xi[0]) / a, y: (y - xi[1]) / a, t: (t - tau0) / a**2}
    zero(a**-3 * theta_new.subs(inv, simultaneous=True) - parent_theta)
    zero(a**-1 * u_new.subs(inv, simultaneous=True) - parent_u)
    zero(a**-2 * p_new.subs(inv, simultaneous=True) - parent_p)
    for alpha in multiindices(3):
        exponent = alpha[0] + alpha[1] + 2 * alpha[2]
        zero(jet(theta_new, alpha) - a**(3 + exponent) * jet(parent_theta, alpha).subs(subs, simultaneous=True))
        zero(jet(force_theta, alpha) - a**(5 + exponent) * jet(old_theta_force, alpha).subs(subs, simultaneous=True))
        for j in range(2):
            zero(jet(u_new[j], alpha) - a**(1 + exponent) * jet(parent_u[j], alpha).subs(subs, simultaneous=True))
            zero(jet(force_u[j], alpha) - a**(3 + exponent) * jet(old_u_force[j], alpha).subs(subs, simultaneous=True))
        chart_cases += 6
checks["shifted_chart_and_force_jet_cases"] = chart_cases
checks["chart_inverse_exact"] = True

# Return matrix and G_1, from the original unsuppressed control sums.
xx, yy, gg, bb, om1, om2 = s.symbols("xx yy gg bb om1 om2", real=True)
RR = xx**2 + yy**2
DP = (gg**2 + bb**2) / RR
z1 = s.Matrix([-yy, xx]) / s.sqrt(RR)
z2 = s.Matrix([-bb, gg]) / s.sqrt(RR)
alpha_dot = -om1 * yy**2 / RR - om2 * bb**2 / (DP * RR)
A_return = alpha_dot * J + om1 * (J*z1) * z1.T + om2 * (J*z2) * z2.T / DP
W = 2*alpha_dot + om1 + om2
a_return = om1*xx*yy/RR + om2*bb*gg/(DP*RR)
zero(A_return - s.Matrix([[a_return, -W], [0, -a_return]]))
EE1, EE2, cc, CC = s.symbols("E1 E2 c C", real=True)
G1_sum = (cc*yy + CC*xx + EE1*yy + EE2*bb) / s.sqrt(RR)
N3 = (EE1+cc)*yy + CC*xx + bb*EE2
zero(G1_sum - N3 / s.sqrt(RR))
checks["original_return_matrix_and_horizontal_gradient"] = True

# Explicit solution, including the exceptional zero-strain branch.
solution_cases = 0
g10, g20, b0 = s.symbols("g10 g20 b0", real=True)
for aa in (-2, 0, 3):
    phi = {k: t if aa == 0 else (1-s.exp(-k*aa*t))/(k*aa) for k in (1,2,3)}
    Xi = t**2/2 if aa == 0 else (phi[2]-phi[3])/aa
    g1 = g10*s.exp(-aa*t)
    b = b0-g10*phi[1]
    g2 = s.exp(aa*t)*(g20-g10*b0*phi[2]+g10**2*Xi)
    A = s.Matrix([[aa,b],[0,-aa]])
    G_exp = s.Matrix([g1,g2])
    H = s.Matrix([[-aa**2,g1],[g1,g2-aa**2]])
    zero(G_exp.diff(t) + A.T*G_exp)
    zero(A.diff(t) + A*A + H - e2*G_exp.T)
    ff_theta, ff_u = residual(G_exp.dot(X), A*X, (X.T*H*X)[0]/2)
    zero(ff_theta)
    zero(ff_u)
    zero(A.subs(t,0) - s.Matrix([[aa,b0],[0,-aa]]))
    zero(G_exp.subs(t,0) - s.Matrix([g10,g20]))
    solution_cases += 1
checks["explicit_unforced_affine_branches"] = solution_cases

# Exact interpolation errors, with both quadratic cross products retained.
Ah = s.Matrix([[t,1-t],[2*t,-t]])
Aa = s.Matrix([[1+t**2,3-t],[1+t,-1-t**2]])
Gh = s.Matrix([1+t,2-t**2])
Ga = s.Matrix([3-t,t**3])
Hh = s.Matrix([[t,1],[1,2*t]])
Ha = s.Matrix([[1-t,t],[t,t**2]])
beta = t**3-2*t+1
Ad = Aa-Ah
Gd = Ga-Gh
Ab = Ah+beta*Ad
Gb = Gh+beta*Gd
Hb = Hh+beta*(Ha-Hh)
rth = Gh.diff(t)+Ah.T*Gh
rta = Ga.diff(t)+Aa.T*Ga
ruh = Ah.diff(t)+Ah*Ah+Hh-e2*Gh.T
rua = Aa.diff(t)+Aa*Aa+Ha-e2*Ga.T
zero(Gb.diff(t)+Ab.T*Gb - ((1-beta)*rth+beta*rta+s.diff(beta,t)*Gd-beta*(1-beta)*Ad.T*Gd))
zero(Ab.diff(t)+Ab*Ab+Hb-e2*Gb.T - ((1-beta)*ruh+beta*rua+s.diff(beta,t)*Ad-beta*(1-beta)*Ad*Ad))
checks["all_transition_cross_terms"] = True

# Cutoff product identities with a generic differentiable chi.
chi = s.Function("chi")(x,y)
L = s.Matrix([[1+t,2-t],[3*t,-1-t]])
B = -J*L
zero(B-B.T)
Q = (X.T*B*X)[0]/2
zc = J*grad(chi*Q)
zc_written = chi*L*X+Q*J*grad(chi)
zc_grad = chi*L+(L*X)*grad(chi).T+(J*grad(chi))*(B*X).T+Q*J*s.hessian(chi,X)
zc_lap = lap(chi)*L*X+2*L*grad(chi)+s.trace(B)*J*grad(chi)+2*J*s.hessian(chi,X)*B*X+Q*J*grad(lap(chi))
zero(zc-zc_written)
zero(zc.jacobian(X)-zc_grad)
zero(lap(zc)-zc_lap)
zero(zc.jacobian(X).trace())
g = s.Matrix([t**2,2-t])
K = s.Matrix([[1+t,t**2],[t**2,3-t]])
hc = chi*g.dot(X)
kc = chi*(X.T*K*X)[0]/2
zero(grad(hc)-(chi*g+g.dot(X)*grad(chi)))
zero(lap(hc)-(g.dot(X)*lap(chi)+2*g.dot(grad(chi))))
zero(grad(kc)-(chi*K*X+(X.T*K*X)[0]*grad(chi)/2))
zero(hc.diff(t)-chi*g.diff(t).dot(X))
zero(zc.diff(t)-(chi*L.diff(t)*X+(X.T*B.diff(t)*X)[0]*J*grad(chi)/2))
checks["generic_cutoff_derivatives_and_divergence"] = True

proof_text = PROOF.read_text(encoding="utf-8")
labels = re.findall(r"\\label\{([^}]+)\}", proof_text)
assert len(labels) == len(set(labels))
assert ",qquad" not in proof_text
assert all(not line.rstrip().endswith("\\") or line.rstrip().endswith("\\\\")
           for line in proof_text.splitlines())
checks["tex_structure"] = True
receipt = {
    "schema": "return-correction-check-v1",
    "status": "pass",
    "checks": checks,
    "proof": "infinite_modified/return_correction_body.tex",
    "proof_sha256": hashlib.sha256(PROOF.read_bytes()).hexdigest(),
    "scope": "Exact finite/local identities; no all-stage budget or infinite blowup certified.",
}
OUT.write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
