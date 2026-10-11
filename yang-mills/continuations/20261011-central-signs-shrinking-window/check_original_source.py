"""Exact diagnostics for OS; these do not replace the analytic proof."""
from pathlib import Path
from collections import defaultdict
from itertools import product, combinations
from fractions import Fraction
import json, hashlib, datetime
import sympy as s

HERE=Path(__file__).resolve().parent
checks=defaultdict(int)
def require(ok, group):
    assert bool(ok), group
    checks[group]+=1

I=s.I
sigma=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),
       s.Matrix([[1,0],[0,-1]])]
T=[-I*A/2 for A in sigma]
eye=s.eye(2)
def quat(r):
    d=1+sum(t*t for t in r)
    return s.simplify((1-sum(t*t for t in r))*eye/d
         -I*sum((2*r[k]*sigma[k]/d for k in range(3)),s.zeros(2)))
def trword(factors):
    a=eye
    for b in factors:a=a*b
    return s.simplify(s.trace(a))

for trial in range(8):
    U=[quat([s.Rational(((trial+2)*(e+1)*(k+3))%7-3,4)
             for k in range(3)]) for e in range(4)]
    for A in U:require(s.simplify(A.H*A)==eye,"SU2 probability-metric inputs")
    for flags in [(1,1,-1,-1),(-1,1,1,-1),(1,-1,1,-1),(-1,-1,1,1)]:
        fac=[U[e] if flags[e]>0 else U[e].H for e in range(4)]
        W=trword(fac)
        def d(e,k):return T[k]*U[e] if flags[e]>0 else -U[e].H*T[k]
        for e in range(4):
            for alpha,beta in product(range(3),repeat=2):
                anti=(T[alpha]*T[beta]+T[beta]*T[alpha])/2
                dd=anti*U[e] if flags[e]>0 else U[e].H*anti
                ff=fac.copy();ff[e]=dd
                require(s.simplify(-trword(ff)-W*s.KroneckerDelta(alpha,beta)/4)==0,
                        "Exact diagonal Hessian blocks with inverse orientations")
        for e,ee in product(range(4),repeat=2):
            if e==ee:continue
            block=[]
            for alpha,beta in product(range(3),repeat=2):
                ff=fac.copy();ff[e]=d(e,alpha);ff[ee]=d(ee,beta)
                block.append(-trword(ff))
            require(s.simplify(sum(x*x for x in block)-s.Rational(1,2)-W*W/16)==0,
                    "Exact transported distinct-edge Hessian norm")

def lattice(m):
    E=[(z,d) for z in product(range(m+1),repeat=3) for d in range(3) if z[d]<m]
    P=[]
    for z in product(range(m+1),repeat=3):
        for d,e in combinations(range(3),2):
            if z[d]>=m or z[e]>=m:continue
            zd=list(z);zd[d]+=1
            ze=list(z);ze[e]+=1
            P.append(((z,d),(tuple(zd),e),(tuple(ze),d),(z,e)))
    return E,P
for m in range(1,8):
    E,P=lattice(m);inc=defaultdict(int);pair=defaultdict(int)
    require(len(E)==3*m*(m+1)**2,"Original edge counts")
    require(len(P)==3*m*m*(m+1),"Original face counts")
    for face in P:
        require(len(set(face))==4,"Four distinct original face edges")
        for e in face:inc[e]+=1
        for e,ee in combinations(face,2):pair[tuple(sorted((e,ee)))]+=1
    for n in inc.values():require(n<=4,"All boundary incidence counts")
    for n in pair.values():require(n==1,"No pair of edges shared by distinct faces")
    for q in range(1,m+1):
        for v in product(range(m-q+1),repeat=3):
            inside=set()
            for z,d in E:
                zz=list(z);zz[d]+=1
                if all(v[k]<=z[k]<=v[k]+q and v[k]<=zz[k]<=v[k]+q for k in range(3)):
                    inside.add((z,d))
            cls=[sum(e in inside for e in p) for p in P]
            require(set(cls)<={0,1,4},"Every original boundary face class")
            eta=sum(int(v[k]>0)+int(v[k]+q<m) for k in range(3))
            require(cls.count(1)==2*q*(q+1)*eta,"Exact crossing count for local Hessian")
            require(sum(cls)==4*3*q*q*(q+1)+2*q*(q+1)*eta,
                    "Exact local Laplacian face multiplicities")

# Full covariant tensor diagnostics, including mixed blocks of a product.
# At the origin in dimensionless stereographic coordinates for radius-two
# S^3, g_ij=16 delta_ij. Off-origin metric derivatives are retained before
# evaluating; a product uses one separate conformal factor per sphere.
for blocks in (1,2):
    n=3*blocks;x=s.symbols("x:"+str(n));zero=dict.fromkeys(x,0)
    w=sum(s.Rational(k+1,k+2)*x[k]+s.Rational(k+2,3)*x[k]**2
          +s.Rational(k+1,5)*x[k]**3+s.Rational(k+3,7)*x[k]**4 for k in range(n))
    w+=sum(s.Rational(i+j+1,7)*x[i]*x[j]+s.Rational(i+j+2,11)*x[i]*x[j]**2
           for i in range(n) for j in range(i+1,n))
    r2=[sum(x[k]**2 for k in range(3*b,3*b+3)) for b in range(blocks)]
    inv=[(1+r2[k//3])**2/16 for k in range(n)]
    def gam(k,i,j):
        if not(k//3==i//3==j//3):return s.S.Zero
        return -2*((int(k==i)*x[j])+(int(k==j)*x[i])-(int(i==j)*x[k]))/(1+r2[k//3])
    dw=[s.diff(w,t) for t in x]
    hh=[[s.diff(w,x[i],x[j])-sum(gam(k,i,j)*dw[k] for k in range(n))
         for j in range(n)] for i in range(n)]
    delta=sum(inv[k]*hh[k][k] for k in range(n))
    score=sum(inv[k]*dw[k]**2 for k in range(n))
    val=lambda p:s.simplify(p.subs(zero))
    h0=s.Matrix([[val(hh[i][j]) for j in range(n)] for i in range(n)])
    dw0=s.Matrix([val(z) for z in dw])
    for i,j in product(range(n),repeat=2):
        rough=0
        for k in range(n):
            rough+=val(s.diff(hh[i][j],x[k],2)-sum(
                s.diff(gam(l,k,i),x[k])*hh[l][j]+s.diff(gam(l,k,j),x[k])*hh[i][l]
                for l in range(n)))/16
        drift=sum(dw0[k]*val(s.diff(hh[i][j],x[k])) for k in range(n))/8
        r_h=r_ww=s.S.Zero
        if i//3==j//3:
            ids=range(3*(i//3),3*(i//3)+3)
            r_h=(int(i==j)*sum(h0[k,k] for k in ids)-h0[i,j])/2
            r_ww=(int(i==j)*sum(dw0[k]**2 for k in ids)-dw0[i]*dw0[j])/2
        rhs=rough+drift+(h0*h0)[i,j]/8+r_h-h0[i,j]+r_ww
        lhs=val(s.diff(delta+score,x[i],x[j]))
        require(s.simplify(lhs-rhs)==0,"Full covariant OS18 including product mixed blocks")

# Exact algebra of the limiting constants; all three orientations retained.
a,R,k=s.symbols("a R k",positive=True)
q=s.symbols("q",positive=True)
N=3*q*(q+1)**2;M=3*q*q*(q+1);cross=12*q*(q+1)
budget=3*k*a*s.sqrt(N*M)+2*cross
require(s.simplify(s.limit(a*a*budget.subs(q,R/a),a,0,dir="+")-(9*k*R**3+24*R**2))==0,
        "Original path patch limit")
J=s.symbols("J",positive=True);LR=9*k*R**3+24*R**2
require(s.simplify(k*k*(18*J/a**2)**2/(4*(1/(k*a*a))*(LR/a**2))
                   -81*k**3*J**2/LR)==0,"Sign-weighted first-energy constant")
E,G,S,AA=s.symbols("E G S AA")
require(s.expand(9*G+4*AA-12*(3*G-S)/2-(6*S-9*G+4*AA))==0,
        "Exact centered drift identity")
for fp,fe in product([Fraction(k,7) for k in range(-15,16)],repeat=2):
    sign=int(fe>0)-int(fe<0)
    require(abs(fp*sign-abs(fp))<=2*abs(fp-fe),"Sign weights at zeros and sign changes")

report={"passed":True,"groups":dict(checks),"check_count":sum(checks.values()),
        "observed_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "scope":"Exact diagnostic calculations, not substitutes for analytic proofs."}
(HERE/"ORIGINAL_SOURCE_CHECKS.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps(report,indent=2))
