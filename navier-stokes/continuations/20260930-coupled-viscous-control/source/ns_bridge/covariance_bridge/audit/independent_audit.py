"""Independent finite algebra and counterexample audit; writes only in audit/."""
import json
from pathlib import Path
import sympy as s

checks = []
def zero(name, expression):
    values = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
    assert all(s.simplify(v) == 0 for v in values), (name, expression)
    checks.append({"name": name, "passed": True})

eps, Q, q, r, R = s.symbols("eps Q q r R", positive=True)
A, h, e = s.symbols("A h e", real=True)
H = s.Matrix(2, 2, s.symbols("h11 h12 h21 h22"))
a1, a2 = s.symbols("a1 a2", nonzero=True)
sig = s.Matrix(s.symbols("s1 s2"))
d = H.inv()*sig/eps
da = s.Matrix([d[0]/(2*a1), d[1]/(2*a2)])
def C(a):
    return eps*H*s.Matrix([a[0]**2, a[1]**2])
a = s.Matrix([a1, a2])
zero("signed covariance differential right inverse", eps*H*s.Matrix([2*a1*da[0], 2*a2*da[1]])-sig)
zero("full principal quadratic covariance remainder", C(a+da)-C(a)-sig-C(da))
zero("correction sign reverses cross, preserves square", C(a-da)-C(a)+sig-C(da))

# A complete scalar-component covariance expansion for arbitrary actual fields.
ur, ut, pr, pt, lr, lt, rr, rt = s.symbols("ur ut pr pt lr lt rr rt")
zero("old-wave and curl terms in exact covariance change",
     (ur+lr+rr)*(ut+lt+rt)-ur*ut
     -(pr*lt+lr*pt)
     -((ur-pr)*lt+lr*(ut-pt))
     -(ur*rt+rr*ut)
     -(lr+rr)*(lt+rt))

f = s.Function("S")
physical_stress = Q**(-2*A)*f(r/s.sqrt(Q))
lhs = s.diff(physical_stress, r)+e*physical_stress/r
rhs = Q**(-2*A-s.Rational(1,2))*(s.diff(f(R), R)+e*f(R)/R)
zero("physical radial stress derivative scaling", lhs.subs(r,s.sqrt(Q)*R)-rhs)
zero("weighted residual moment scale", (e+1)/2-2*A-s.Rational(1,2)-(e/2-2*A))
zero("normalized bump times moment scaling", 2*A+s.Rational(1,2)-(e+1)/2+e/2-2*A)
zero("q-dependent bump weighted normalization exponent", -(e+1)/2+e/2+s.Rational(1,2))
zero("leading stress physical Q exponent cancels", (-2*A+h+A+s.Rational(1,2)).subs(A,s.Rational(1,2)+h))

# Determinant polynomial factors valid at every distinct exponential node.
x1,x2,x3,y1,y2 = s.symbols("x1 x2 x3 y1 y2")
V = s.Matrix([[1,x1,x1**2],[1,x2,x2**2],[1,x3,x3**2]])
zero("three-row Vandermonde determinant exact", V.det()-(x2-x1)*(x3-x1)*(x3-x2))
zero("two-row Vandermonde determinant exact", s.Matrix([[1,y1],[1,y2]]).det()-(y2-y1))

# The draft's normalized Dz omitted eps; display its exact loss for Z^2.
Z = s.symbols("Z")
zero("omitted axial derivative diffusion discrepancy", s.diff(Z**2,Z,2)-eps**2*s.diff(Z**2,Z,2)-2*(1-eps**2))

receipt = {
    "all_passed": True,
    "checks": checks,
    "scope": "independent finite covariance, full curl remainder, physical/chart scaling and general determinant identities; no endpoint or source convergence verification",
    "defects_are_in_original_draft": True,
}
Path(__file__).with_name("independent_audit_receipt.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))
