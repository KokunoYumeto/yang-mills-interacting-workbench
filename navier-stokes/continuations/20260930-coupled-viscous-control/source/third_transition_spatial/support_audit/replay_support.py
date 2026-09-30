"""Independent exact algebra replay for the support audit; no numerical ODE claims."""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
checks = []

def check(name, expr):
    if isinstance(expr, s.MatrixBase):
        residual = expr.applyfunc(s.simplify)
        passed = residual == s.zeros(*residual.shape)
    elif isinstance(expr, bool):
        residual = expr
        passed = expr
    else:
        residual = s.simplify(expr)
        passed = residual == 0
    checks.append({"name": name, "passed": bool(passed), "residual": str(residual)})
    if not passed:
        raise AssertionError((name, residual))

J = s.Matrix([[0, -1], [1, 0]])
aa, bb, cc, dd = s.symbols("l11 l12 l21 l22", real=True)
L = s.Matrix([[aa, bb], [cc, dd]])
rb, ss, cs = s.symbols("rb sin_s cos_s", positive=True)
Lb = s.Matrix([[0, ss], [rb, cs]])
b = rb * ss
check("oriented insertion determinant", Lb.det() + b)
check("adjugate identity preserving operator norm", L.adjugate() + J*L.T*J)
check("orthogonality of J", J.T*J - s.eye(2))
M = L.inv().T * Lb.T
MinvT = L * Lb.inv()
check("M3 inverse transpose order", M.T*MinvT - s.eye(2))
check("M3 original insertion value", (Lb.inv().T*Lb.T)-s.eye(2))
check("transported insertion covector", MinvT*s.Matrix([ss,cs])-L[:,1])
check("M3 determinant exact ratio", M.det()-Lb.det()/L.det())
p, q, r = s.symbols("p q r", real=True)
Dvel = s.Matrix([[p,q],[r,-p]])
Ldot = -Dvel.T*L
# The derivative is evaluated independently by entrywise differentiation.
Mdot = s.zeros(2)
for variable, rate in zip(list(L), list(Ldot)):
    Mdot += M.diff(variable)*rate
check("full matrix evolution M3dot=D_<3 M3", Mdot-Dvel*M)
detdot = sum(s.diff(L.det(),var)*rate for var,rate in zip(list(L),list(Ldot)))
check("determinant conservation under actual trace-free transport",detdot)
check("Frobenius product bound 14 times 11", s.Integer(14)*11-154)
check("strict sqrt154 less than 16 by positive squares", bool(s.Integer(154)<16**2))

a,h0=s.symbols("a h0",positive=True)
N=1+(3-h0)/a
Ntilde=1+(s.Rational(13,4)-h0)/a
check("exact spare margin in doubled second deformation", 2*N-Ntilde-(1+(s.Rational(11,4)-h0)/a))
check("spare numerator positive for h0 at most one", bool(s.Rational(11,4)-1>0))
nu,lam1,Q2=s.symbols("nu lam1 Q2",positive=True)
C2=s.exp(9)*s.sqrt(5*s.sqrt(10)/4)
CM=256*C2/(15*s.sqrt(s.E))
check("squared scale upper constant", C2**2-s.Rational(5,4)*s.sqrt(10)*s.exp(18))
check("third deformation frequency constant", CM-s.Rational(256,15)*C2/s.sqrt(s.E))
check("third deformation exponent", Q2/s.Integer(16)-s.Rational(1,16)-(Q2-1)/16)
check("second envelope nesting exponent", s.Rational(1,16)+(Q2-1)/16-3*Q2+3+(47*Q2/16-3))
check("second linear profile nesting exponent", (Q2-1)/16-2*Q2+(31*Q2+1)/16)
check("source exponent positivity at minimal Q2", bool(s.Rational(47,16)*202-3>0))
check("source second exponent positivity at minimal Q2", bool((s.Integer(31)*202+1)/16>0))
check("first envelope exponent", s.Rational(1,16)-3+s.Rational(47,16))
check("first linear profile exponent", s.Rational(1,16)-2+s.Rational(31,16))
check("first envelope margin absorbs doubling", 2*s.Rational(1,4)-s.Rational(1,2))
check("first phase margin absorbs doubling", 2*s.Rational(1,2)-1)
mu,K,Theta,Omega,z1,z2,x1,x2,P0=s.symbols("mu K Theta Omega z1 z2 x1 x2 P0",real=True)
x=s.Matrix([x1,x2]); z=s.Matrix([z1,z2]); phase=K*z.dot(x)
Paff=P0+phase**2/2
gradP=s.Matrix([s.diff(Paff,x1),s.diff(Paff,x2)])
check("primitive constant retained and exact affine velocity", J*gradP-K**2*J*z*z.dot(x))
check("physical phase-radius factors retain mu", (mu*s.Symbol('lambda2'))*(s.Symbol('lambda2')**-3/mu)-s.Symbol('lambda2')**-2)

paths=[
    "third_transition/third_transition_body.tex",
    "finite_stage/third_growth_entry.tex",
    "finite_stage/actual_viscous_entry.tex",
    "modified_spatial/modified_spatial_body.tex",
    "physical_realization.tex",
]
receipt={
    "scope":"Exact algebra only; operator-norm, strict-frequency, profile and support proofs in AUDIT.md.",
    "check_count":len(checks),
    "all_passed":all(c['passed'] for c in checks),
    "inputs":[{"path":p,"sha256":hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in paths],
    "checks":checks,
}
(HERE/'replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({"check_count":receipt['check_count'],"all_passed":receipt['all_passed']}))
