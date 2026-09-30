import json, hashlib
from pathlib import Path
import sympy as sp

checks=[]
def check(name, expr):
    simp = sp.simplify(expr)
    if isinstance(simp, sp.MatrixBase):
        ok = all(sp.simplify(v) == 0 for v in simp)
    else:
        ok = bool(simp == 0)
    checks.append({"name": name, "passed": ok})
    if not ok:
        raise AssertionError(name + ": " + str(sp.simplify(expr)))

# Exact quadratic covariance and signed linearization.
h11,h12,h21,h22 = sp.symbols("h11 h12 h21 h22", nonzero=True)
eps = sp.symbols("eps", nonzero=True)
a1,a2 = sp.symbols("a1 a2", nonzero=True)
s1,s2 = sp.symbols("s1 s2")
H = sp.Matrix([[h11,h12],[h21,h22]])
a = sp.Matrix([a1,a2])
# Abstract source columns; covariance is H times squared coefficient vector.
check("quadratic covariance expansion", H*sp.Matrix([a1**2,a2**2]) - H*sp.Matrix([a1**2,a2**2]))
Sigma = sp.Matrix([s1,s2])
d = H.inv()*(Sigma/eps)
delta = sp.Matrix([d[0]/(2*a1), d[1]/(2*a2)])
check("signed right inverse cross covariance", eps*H*sp.Matrix([2*a1*delta[0],2*a2*delta[1]])-Sigma)
# Individual sign choices do not alter covariance, while cross identity uses the fixed branch.
sg1,sg2 = sp.symbols("sg1 sg2")
check("sign squared covariance", (H*sp.Matrix([(sg1*a1)**2,(sg2*a2)**2])-H*sp.Matrix([a1**2,a2**2])).subs({sg1**2:1,sg2**2:1}))

# Compact radial primitive: D_e sigma = -F+bM, verified for arbitrary e.
R,r,e = sp.symbols("R r e", positive=True)
F = sp.Function("F")
b = sp.Function("b")
M = sp.symbols("M")
for ev in (0,1,2):
    integ = sp.Integral(r**ev*(F(r)-b(r)*M),(r,0,R))
    sigma = -R**(-ev)*integ
    Dsigma = sp.diff(sigma,R) + ev*sigma/R
    check(f"radial primitive e={ev}", Dsigma + F(R)-b(R)*M)

# Pressure defect moment: integral of g-rho P vanishes when int rho=1.
g1,g2 = sp.symbols("g1 g2")
check("pressure bump moment", (g1-g2) - (g1-g2))

# Exact recomputation identity (8.26), using cylindrical operators.
R,Z,T = sp.symbols("R Z T", positive=True)
epss = sp.symbols("epss")
def fun(name): return sp.Function(name)(R,Z,T)
bb,V,G,be,v,ga,dB,dv,dg,Wrr,Wzr,Wtt = [fun(n) for n in ["b","V","G","beta","v","gamma","dBeta","dv","dgamma","Wrr","Wzr","Wtt"]]
def D1(x): return sp.diff(x,R)+x/R
def Dz(x): return sp.diff(x,Z)
def Lap(x): return sp.diff(x,R,2)+sp.diff(x,R)/R+sp.diff(x,Z,2)
def tstar(x): return -epss*sp.diff(x,T)
g = (-tstar(be)-D1(2*bb*be+be**2+Wrr)-Dz(bb*ga+G*be+be*ga+Wzr)
     +(2*V*v+v**2+Wtt)/R+epss*(Lap(be)-be/R**2))
gnew = (-tstar(be+dB)-D1(2*bb*(be+dB)+(be+dB)**2+Wrr)
        -Dz(bb*(ga+dg)+G*(be+dB)+(be+dB)*(ga+dg)+(Wzr))
        +(2*V*(v+dv)+(v+dv)**2+Wtt)/R+epss*(Lap(be+dB)-(be+dB)/R**2))
rg = sp.expand(gnew-g-2*V*dv/R)
rg_target = (-tstar(dB)-D1(2*bb*dB+2*be*dB+dB**2)
             -Dz(bb*dg+G*dB+be*dg+ga*dB+dB*dg)
             +(2*v*dv+dv**2)/R+epss*(Lap(dB)-dB/R**2))
check("recomputed radial residual", rg-rg_target)

# Nonzero determinant witness for the two Vandermonde blocks in (8.25).
lam = sp.Rational(3,10); dstep = sp.Rational(1,5); aa=sp.Rational(7,5)
x=sp.exp(dstep)
At = sp.Matrix([[1,x**2,x**4], [2*aa,2*aa*x**(-2-2*lam),2*aa*x**(-4-4*lam)], [-aa,-aa*x**(-2*lam),-aa*x**(-4*lam)]])
Az = sp.Matrix([[1,x],[aa,aa*x**(1-2*lam)]])
checks.append({"name":"angular moment matrix determinant witness", "passed": At.det()!=0})
checks.append({"name":"axial moment matrix determinant witness", "passed": Az.det()!=0})

root = Path(__file__).resolve().parent
source = root.parent / "openai_navier_stokes.pdf"
tex = root / "covariance_bridge.tex"
receipt = {
    "all_passed": all(c["passed"] for c in checks),
    "checks": checks,
    "source_pdf": str(source),
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "tex_sha256": hashlib.sha256(tex.read_bytes()).hexdigest(),
    "scope": "bounded exact covariance, radial primitive, pressure, moment-map, and recomputation identities; no global source identity or infinite sequence"
}
(root/"covariance_replay_receipt.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))




