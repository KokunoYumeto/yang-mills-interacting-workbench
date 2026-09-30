"""Exact, independent third-steering identity audit; no shooting assertion.

The original objects are retained in `identities`.  Their complete rational
residuals, numerator/denominator and exact zero remainders are written to JSON.
Only the declared circle equation D*(Y**2+Z**2)=g**2+b**2 is used in reduction.
This replay is a finite identity verification, not an interval existence proof.
"""
from __future__ import annotations

import datetime
import hashlib
import json
from pathlib import Path
import platform

import sympy as sp


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / "third_transition" / "third_transition_body.tex"
identities = []


def exact_zero(name, original, relation=None, generator=None):
    """Keep original residual and certify its full rational numerator is zero."""
    numerator, denominator = sp.together(original).as_numer_denom()
    if relation is None:
        remainder = sp.expand(numerator)
    else:
        remainder = sp.rem(sp.expand(numerator), relation, generator)
        remainder = sp.expand(sp.together(remainder).as_numer_denom()[0])
    passed = remainder == 0
    identities.append({
        "name": name,
        "residual": str(original),
        "full_numerator": str(numerator),
        "full_denominator": str(denominator),
        "relation": None if relation is None else str(relation),
        "remainder": str(remainder),
        "passed": passed,
    })
    if not passed:
        raise AssertionError(f"{name}: nonzero exact remainder {remainder}")


h, g, a, b, Z, Y = sp.symbols("h g a b Z Y", real=True)
W1, W2, E1, E2, c, C, d, K1, K2, Q = sp.symbols(
    "Omega1 Omega2 E1 E2 c C d K1 K2 Zdot", real=True
)
D = h**2 + a**2
R = (g**2 + b**2) / D
x = (h*g-a*b)/D
y = (a*g+h*b)/D
circle = Y**2 + Z**2 - R
J = sp.Matrix([[0, -1], [1, 0]])
z3 = sp.Matrix([Z, Y])
z2 = sp.Matrix([(g*Z-b*Y)/R, (g*Y+b*Z)/R])
z1 = sp.Matrix([(x*Z-y*Y)/R, (x*Y+y*Z)/R])


def zero(name, expression):
    exact_zero(name, expression, circle, Y)


def vector_zero(name, expression):
    for index, item in enumerate(expression):
        zero(f"{name}[{index}]", item)


exact_zero("hy-ax=b", h*y-a*x-b)
exact_zero("hx+ay=g", h*x+a*y-g)
exact_zero("x^2+y^2=R", x*x+y*y-R)
zero("norm zeta1 squared = 1", z1.dot(z1)-1)
zero("norm zeta2 squared = D", z2.dot(z2)-D)
zero("norm zeta3 squared = R", z3.dot(z3)-R)
zero("zeta1 dot zeta2 = h", z1.dot(z2)-h)
zero("zeta1 dot zeta3 = x", z1.dot(z3)-x)
zero("zeta2 dot zeta3 = g", z2.dot(z3)-g)
zero("det(zeta1,zeta2)=-a", sp.Matrix.hstack(z1,z2).det()+a)
zero("det(zeta1,zeta3)=-y", sp.Matrix.hstack(z1,z3).det()+y)
zero("det(zeta2,zeta3)=-b", sp.Matrix.hstack(z2,z3).det()+b)
vector_zero("zeta2=h zeta1-a J zeta1", z2-h*z1+a*J*z1)
vector_zero("zeta3=x zeta1-y J zeta1", z3-x*z1+y*J*z1)

hdot = a*W1
gdot = W1*(2*a*h*g+(h*h-a*a)*b)/D+b*W2
xdot = sp.diff(x,h)*hdot+sp.diff(x,g)*gdot
ydot = sp.diff(y,h)*hdot+sp.diff(y,g)*gdot
Rdot = sp.diff(R,h)*hdot+sp.diff(R,g)*gdot
exact_zero("xdot=Omega1*y+bh*Omega2/D", xdot-W1*y-b*h*W2/D)
exact_zero("ydot=ba*Omega2/D", ydot-b*a*W2/D)
exact_zero("derivative hy-ax = 0", hdot*y+h*ydot-a*xdot)
exact_zero("Rdot=2 Omega1*x*y+2bg*Omega2/D", Rdot-2*W1*x*y-2*b*g*W2/D)

Ydot = (Rdot-2*Z*Q)/(2*Y)
alphadot = (W1*y*z1[0]+b*W2*z2[0]/D-Q)/Y
rates = {h: hdot, g: gdot, Z: Q, Y: Ydot}


def total_derivative(expression):
    return sum(sp.diff(expression, variable)*rate for variable,rate in rates.items())


z1dot = z1.applyfunc(total_derivative)
z2dot = z2.applyfunc(total_derivative)
z3dot = z3.applyfunc(total_derivative)
T1 = alphadot*J
T2 = T1+W1*(J*z1)*z1.T
T3 = T2+W2*(J*z2)*z2.T/D
vector_zero("first physical phase equation", z1dot+T1.T*z1)
vector_zero("second physical phase equation", z2dot+T2.T*z2)
vector_zero("third physical phase equation", z3dot+T3.T*z3)
zero("horizontal steering reproduces prescribed Zdot", (-T3.T*z3)[0]-Q)
zero("trace third parent matrix is zero", sp.trace(T3))

# This is the full derivative of the specified principal-arcsine alpha lift.
alpha_lift_derivative = (
    -Q/Y+Z*Rdot/(2*R*Y)-b*gdot/(g*g+b*b)-a*hdot/D
)
zero("alpha lift derivative equals physical steering control", alpha_lift_derivative-alphadot)

N2 = a*(E1+c)+C*h
N3 = (E1+c)*y+C*x+b*E2
E1dot = -C*W1-d*K1*K1*E1
E2dot = -N2*W2/D-d*K2*K2*D*E2
N2dot = a*E1dot+C*hdot
N3dot = E1dot*y+(E1+c)*ydot+C*xdot+b*E2dot
exact_zero("N2 derivative exact diffusion loss", N2dot+a*d*K1*K1*E1)
exact_zero("N3 derivative exact diffusion loss", N3dot+d*(K1*K1*E1*y+b*K2*K2*D*E2))
G2 = -(E1+c)*z1-C*(J*z1)
G3 = G2-E2*z2
zero("second temperature numerator pairing", -(J*z2).dot(G2)-N2)
zero("third temperature numerator pairing", -(J*z3).dot(G3)-N3)

# The following identity multiplies the actual A2 derivative by sqrt(D),
# retaining A2=sqrt(D)*E2 and the complete changing-length term.
actual_A2_derivative_times_rootD = a*h*W1*E2+D*E2dot
claimed_A2_derivative_times_rootD = (a*h*W1/D-d*K2*K2*D)*D*E2-N2*W2
exact_zero("actual A2=sqrt(D)E2 derivative", actual_A2_derivative_times_rootD-claimed_A2_derivative_times_rootD)

# Recover M2 with the original cos(s2) datum retained as c2.
cb, sb, c2, A = sp.symbols("cos_beta sin_beta cos_s2 alphadot", real=True)
B = sp.Matrix([[cb,-sb],[sb,cb]])
S = sp.Matrix([[1,-(h-c2)/a],[0,1]])
Sdot = sp.Matrix([[0,-hdot/a],[0,0]])
M2 = B*S
u1 = B*sp.Matrix([0,1])
u2 = B*sp.Matrix([a,h])
Bdot = A*J*B
M2dot = Bdot*S+B*Sdot
parent2 = A*J+W1*(J*u1)*u1.T
unit_rotation = sb**2+cb**2-1
for index,item in enumerate(M2dot-parent2*M2):
    exact_zero(f"M2 full matrix evolution[{index}]", item, unit_rotation, sb)
for index,item in enumerate(M2.T*u2-sp.Matrix([a,c2])):
    exact_zero(f"M2 transpose inverse recovers activation vector[{index}]", item, unit_rotation, sb)
exact_zero("M2 determinant is one", M2.det()-1, unit_rotation, sb)

# Recover M3 without suppressing either initial column.  Lb has its actual
# two columns; its determinant is -b and newest column is e(s).
p0, q0, Z0, Y0 = sp.symbols("zeta2b_1 zeta2b_2 zeta3b_1 zeta3b_2", real=True)
Lb = sp.Matrix([[p0,Z0],[q0,Y0]])
L = sp.Matrix.hstack(z2,z3)
LinvT = sp.Matrix([[Y,-z2[1]],[-Z,z2[0]]])/(-b)
M3 = LinvT*Lb.T
for index,item in enumerate(L.T*M3-Lb.T):
    zero(f"M3 exact inverse relation[{index}]",item)
M3dot = M3.applyfunc(total_derivative)
for index,item in enumerate(M3dot-T3*M3):
    zero(f"M3 full matrix evolution[{index}]",item)
zero("M3 determinant equals det(Lb)/(-b)", M3.det()+Lb.det()/b)

# Newest signed pair: chi is the constant entry norm chi1, never r3(t).
sigma, chi, ss, K3, N, P, v, theta, W3, delta3 = sp.symbols(
    "sigma2 chi1 sin_s K3 N3 P3 v Theta3 Omega3 delta3", nonzero=True, real=True
)
Gamma = sigma*ss
theta_dot = N*W3/(K3*R)-d*K3*K3*R*theta
W3dot = K3*Z*theta-d*K3*K3*R*W3
k = chi*N/(sigma*sigma*ss*R)
quotient_prime = sigma*(W3dot*theta-W3*theta_dot)/(K3*chi*theta*theta*Gamma)
quotient_prime = quotient_prime.subs(W3,K3*chi*theta*v/sigma)
exact_zero("physical quotient Riccati equation", quotient_prime-Z/(chi*ss)+k*v*v)
logP_prime = (theta_dot/(theta*Gamma)).subs(W3,K3*chi*theta*v/sigma)
exact_zero("physical amplitude logarithmic derivative", logP_prime-k*v+d*K3*K3*R/Gamma)
vprime = Z/(chi*ss)-k*v*v
Pprime = (k*v-d*K3*K3*R/Gamma)*P
reconstructed_theta = -P
reconstructed_W3 = -K3*chi*P*v/sigma
reconstructed_theta_dot = -Gamma*Pprime
reconstructed_W3dot = -K3*chi*Gamma*(Pprime*v+P*vprime)/sigma
exact_zero("Riccati-to-physical temperature reconstruction", reconstructed_theta_dot-theta_dot.subs({theta:reconstructed_theta,W3:reconstructed_W3}))
exact_zero("Riccati-to-physical vorticity reconstruction", reconstructed_W3dot-W3dot.subs({theta:reconstructed_theta,W3:reconstructed_W3}))

# Retain the original pulsed horizontal prescription and its complete derivative.
tau, Z1, m, pulse_L = sp.symbols("tau Z1 m L", real=True)
eta = sp.Function("eta")
eta2 = sp.Function("eta2")
pulse = Z1*(1-eta(tau))-m*pulse_L*ss*chi*eta2(pulse_L*(tau-1))
pulse_prime = sp.diff(pulse,tau)
claimed_pulse_prime = -Z1*sp.diff(eta(tau),tau)-m*pulse_L**2*ss*chi*sp.Subs(sp.Derivative(eta2(sp.Symbol("u")),sp.Symbol("u")),sp.Symbol("u"),pulse_L*(tau-1))
exact_zero("source pulse full time derivative", pulse_prime-claimed_pulse_prime)
exact_zero("source pulse scaled Riccati forcing", pulse/(chi*ss)-(Z1*(1-eta(tau))/(chi*ss)-m*pulse_L*eta2(pulse_L*(tau-1))))

receipt = {
    "audit": "Independent exact third-steering algebra replay",
    "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "python": platform.python_version(),
    "sympy": sp.__version__,
    "source": str(SOURCE),
    "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "assumptions": [
        "a>0,b>0,h>0,g>0; D=h^2+a^2; R=(g^2+b^2)/D",
        "Y=sqrt(R-Z^2)>0; original determinant orientation is retained",
        "The prescribed Z and existing state are differentiable on the audited interval",
        "sigma2>0,chi1=|zeta3(t1)|>0,K3>0,sin(s)>0; chi1 is constant",
        "All older activation weights equal one; physical d,K1,K2,K3 are retained",
        "M3 uses the actual L(tb), det L(tb)=-b and zeta3(tb)=e(s)",
    ],
    "identity_count": len(identities),
    "all_passed": all(item["passed"] for item in identities),
    "scope_limit": "Exact algebra and local inverse only; no interval enclosure, third shooting root, or cascade is asserted.",
    "identities": identities,
}
(HERE/"symbolic_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({key:receipt[key] for key in ("audit","identity_count","all_passed","source_sha256","script_sha256","scope_limit")},indent=2))
