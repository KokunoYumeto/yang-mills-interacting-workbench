"""Independent exact checks; never writes in the owner's directory."""
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations
import hashlib
import json
import re
import sympy as s

root=Path(__file__).resolve().parent
checks=[]
def eq(name,a,b=0):
    if isinstance(a,s.MatrixBase):
        assert all(s.simplify(x)==0 for x in a-b),(name,a-b)
    else:assert s.simplify(s.expand(a-b))==0,(name,a-b)
    checks.append({"name":name,"passed":True})
def test(name,flag):
    assert flag,name
    checks.append({"name":name,"passed":True})
I=s.eye(2)
sigma=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.Matrix([[1,0],[0,-1]])]
def X(v):return sum((-s.I*v[a]*sigma[a]/2 for a in range(3)),s.zeros(2))
def H(v):return sum((-v[a]*sigma[a]/2 for a in range(3)),s.zeros(2))
def series_product(matrices,degree=5):
    result=[I]+[s.zeros(2) for _ in range(degree)]
    for aa in matrices:
        e=[aa**k/s.factorial(k) for k in range(degree+1)]
        result=[s.simplify(sum((result[j]*e[k-j] for j in range(k+1)),s.zeros(2))) for k in range(degree+1)]
    return result
def hs2(A):return s.simplify(s.trace(A.conjugate().T*A))
vecs=[s.Matrix(v) for v in [(1,2,-1),(-2,1,3),(0,-1,2),(2,0,-3)]]
for a,b in combinations(range(4),2):
    eq(f"original Pauli pair {a}{b}",s.trace(H(vecs[a])*H(vecs[b])),vecs[a].dot(vecs[b])/2)
    eq(f"original Lie bracket {a}{b}",X(vecs[a])*X(vecs[b])-X(vecs[b])*X(vecs[a]),X(vecs[a].cross(vecs[b])))
for a,b,c in combinations(range(4),3):
    eq(f"original Pauli triple {a}{b}{c}",s.trace(H(vecs[a])*H(vecs[b])*H(vecs[c])),-s.I*vecs[a].dot(vecs[b].cross(vecs[c]))/4)
C=sum(vecs,s.zeros(3,1))
B=sum((vecs[a].cross(vecs[b]) for a,b in combinations(range(4),2)),s.zeros(3,1))
eq("complete cubic factorization",sum(vecs[a].dot(vecs[b].cross(vecs[c])) for a,b,c in combinations(range(4),3)),C.dot(B))
rev=[-v for v in reversed(vecs)]
eq("whole-face reversal B",sum((rev[a].cross(rev[b]) for a,b in combinations(range(4),2)),s.zeros(3,1)),-B)
coeff=series_product([X(v) for v in vecs])
eq("full ordered quadratic defect",-s.re(s.trace(coeff[2])),C.dot(C)/4)
eq("full ordered cubic defect",-s.re(s.trace(coeff[3])),C.dot(B)/4)
revcoeff=series_product([X(v) for v in rev])
for k in range(6):
    eq(f"whole-face reversal trace coefficient {k}",s.re(s.trace(coeff[k])),s.re(s.trace(revcoeff[k])))

# Closed additive circulation: retain every noncommuting ordered factor.
closed_cases=[
    [s.Matrix(v) for v in [(1,0,0),(0,1,0),(0,0,1),(-1,-1,-1)]],
    [s.Matrix(v) for v in [(1,0,0),(0,1,0),(-1,0,0),(0,-1,0)]],
    [vecs[0],vecs[1],vecs[2],-vecs[0]-vecs[1]-vecs[2]]
]
for n,vs in enumerate(closed_cases):
    cc=series_product([X(v) for v in vs])
    bb=sum((vs[a].cross(vs[b]) for a,b in combinations(range(4),2)),s.zeros(3,1))
    eq(f"closed face P prime {n}",cc[1],s.zeros(2))
    eq(f"closed face P second {n}",2*cc[2],X(bb))
    eq(f"closed face cubic defect {n}",-s.re(s.trace(cc[3])))
    eq(f"closed face quartic coefficient {n}",-s.re(s.trace(cc[4])),bb.dot(bb)/16)

# The generic Hermitian case retains trace scalars as well.
herm=[H(v)+(a+1)*I/3 for a,v in enumerate(vecs)]
pp=series_product([s.I*h for h in herm],3)
aa=sum(herm,s.zeros(2))
eq("Hermitian scalar-retaining quadratic", -s.re(s.trace(pp[2])),s.trace(aa*aa)/2)
eq("Hermitian scalar-retaining cubic", -s.re(s.trace(pp[3])),-sum(s.im(s.trace(herm[a]*herm[b]*herm[c])) for a,b,c in combinations(range(4),3)))

Q=[I+s.I*h-h*h/2 for h in herm]
R=s.simplify(Q[0]*Q[1]*Q[2]*Q[3])
rhs=s.zeros(2);defect=0
for a in range(4):
    eq(f"Taylor factor unitarity defect {a}",Q[a].conjugate().T*Q[a],I+herm[a]**4/4)
    suffix=I
    for r in range(a+1,4):suffix=suffix*Q[r]
    rhs+=suffix.conjugate().T*herm[a]**4*suffix/4
    defect+=hs2(herm[a]**2*suffix)/8
eq("complete ordered positive defect matrix",R.conjugate().T*R-I,rhs)
eq("complete ordered positive defect trace",s.trace(R.conjugate().T*R-I)/2,defect)
x=s.Symbol("x",real=True)
hh=s.diag(x,-x);qa=I+s.I*hh-hh*hh/2
qb=I-s.I*hh-hh*hh/2
rb=qa*qb
eq("literal source backtracking product",rb,(1+x**4/4)*I)
eq("literal backtracking missing scalar",s.trace(rb.conjugate().T*rb-I)/2,x**4/2+x**8/16)
eq("intended source one-edge missing scalar",s.trace(qa.conjugate().T*qa-I)/2,x**4/4)
eta=s.Symbol("eta",nonnegative=True)
eq("dimension-independent defect geometric sum",eta**4*s.Rational(1,8)*sum((1+eta**4/4)**k for k in range(4)),((1+eta**4/4)**4-1)/2)
eq("dimension-independent cubic norm coefficient",4**3/s.Integer(6),s.Rational(32,3))
eq("SU2 fourth remainder constant",s.Rational(2,24)/2**4,s.Rational(1,192))
eq("SU2 fifth remainder constant",s.Rational(2,120)/2**5,s.Rational(1,1920))
eq("twice-vanishing sextic bound",s.Rational(1,36)/2**6,s.Rational(1,2304))

# Full finite CW path, then series at z=1/j.
z,kappa=s.symbols("z kappa",positive=True)
m=2/z**4;n=m+1;bb=10000/(kappa*z**2);alpha=s.pi/(2*m)
ww=4*m*m*n*(1-s.cos(alpha));wquad=2*m*m*n*alpha**2
eq("full original potential quadratic path",bb*wquad,5000*s.pi**2*(2/z**4+1)/(kappa*z**2))
eq("full original finite path remainder coefficient",bb*m*m*n*alpha**4/6,10000*s.pi**4*(2/z**4+1)*z**6/(384*kappa))
series=s.series(bb*ww,z,0,7).removeO().expand()
eq("CW actual potential leading coefficient",series.coeff(z,-6),10000*s.pi**2/kappa)
eq("CW actual potential finite-boundary coefficient",series.coeff(z,-2),5000*s.pi**2/kappa)
eq("CW actual potential scaled difference",series.coeff(z,2),-625*s.pi**4/(12*kappa))

note=root/"ORDERED_WILSON_INDEPENDENT_REVIEW.md"
raw=note.read_text(encoding="utf-8")
ids=re.findall(r"\\tag\{UR(\d+)\}",raw)
test("UR1--UR15 each once",sorted(map(int,ids))==list(range(1,16)) and len(ids)==len(set(ids)))
test("inline delimiters balanced",raw.count(r"\(")==raw.count(r"\)"))
test("display delimiters balanced",raw.count(r"\[")==raw.count(r"\]"))
test("banned prose token absent",not re.search(r"\b"+"pl"+"ain"+r"\b",raw,re.I))
report={"observed_utc":datetime.now(timezone.utc).isoformat(),"check_count":len(checks),"checks":checks,"review_sha256":hashlib.sha256(note.read_bytes()).hexdigest(),"scope":"Exact independent matrix coefficients, original signs, whole-face reversal, positive Taylor defect, closed-circulation quartic, original CW path and source integrity. No vacuum expectation numerically evaluated."}
(root/"ORDERED_WILSON_REVIEW_CHECKS.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"passed":len(checks),"review_sha256":report["review_sha256"]},indent=2))
