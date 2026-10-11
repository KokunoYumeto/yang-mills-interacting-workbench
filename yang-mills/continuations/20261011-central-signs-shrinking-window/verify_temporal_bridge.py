"""Independent exact algebra and numerical checks for AT1--AT60.

These checks do not compute the actual growing-box vacuum or the endpoint sign.
The original complete proofs, including global error constants, are in the note.
"""
from pathlib import Path
import json
import math
import hashlib
from collections import Counter
import re
import datetime
import mpmath as mp
import sympy as sp
import numpy as np
from scipy.linalg import expm
from scipy.special import ive

ROOT = Path(__file__).resolve().parent
mp.mp.dps = 65
checks = []

def check(name, condition, kind="exact"):
    if not condition:
        raise AssertionError(name)
    checks.append({"name": name, "kind": kind, "passed": True})

def close(a, b, tol=mp.mpf("1e-45")):
    return abs(a-b) <= tol*(1+abs(a)+abs(b))

# Bessel multipliers are compared to direct compact-group quadrature.
D = {k: 3*mp.e*mp.pi**2/8*mp.gamma(k+mp.mpf("1.5")) *
        (mp.pi**2/4)**(k+mp.mpf("1.5")) for k in (1, 2)}
a0 = 2*D[2]/9+D[1]/2
b0 = 2*D[2]/3
for beta in map(mp.mpf, ["1", "2", "5", "10", "100"]):
    weight = lambda t: mp.sin(t)**2*mp.exp(-2*beta*(1-mp.cos(t)))
    den = mp.quad(weight, [0, mp.pi/2, mp.pi])
    z = mp.exp(-2*beta)*mp.besseli(1, 2*beta)/beta
    check(f"Haar normalization beta={beta}", close(2*den/mp.pi, z), "numerical")
    E = lambda f: mp.quad(lambda t: f(t)*weight(t), [0, mp.pi/2, mp.pi])/den
    moments = {k:E(lambda t,k=k:t**(2*k)) for k in (1,2)}
    for k in (1,2):
        check(f"global radial moment k={k}, beta={beta}",
              moments[k] <= D[k]/beta**k, "numerical")
    check(f"radial integration by parts beta={beta}",
          close(E(lambda t:mp.sin(t)**2), 3*E(mp.cos)/(2*beta)), "numerical")
    check(f"generator moment coefficient beta={beta}",
          abs(2*moments[1]/3-1/beta) <= a0/beta**2, "numerical")
    check(f"fourth remainder constant beta={beta}",
          2*moments[2]/3 <= b0/beta**2, "numerical")
    for l in range(13):
        integral = mp.quad(
            lambda t: mp.sin(t)*mp.sin((l+1)*t) *
            mp.exp(-2*beta*(1-mp.cos(t))), [0,mp.pi/2,mp.pi])
        eig_quad = integral/((l+1)*den)
        eig = mp.besseli(l+1,2*beta)/mp.besseli(1,2*beta)
        lam = mp.mpf(l*(l+2))/4
        check(f"all-spin formula sample l={l}, beta={beta}",
              close(eig_quad,eig), "numerical")
        check(f"one-step all-spin bound l={l}, beta={beta}",
              abs(eig-1+lam/beta) <= (a0*lam+b0*lam**2)/beta**2+mp.mpf("1e-60"),
              "numerical")
        check(f"positive contraction l={l}, beta={beta}", 0<eig<=1, "numerical")

# The strengthened tensor estimate is taken pointwise before the vector norm.
for beta in map(mp.mpf, ["1", "7", "100"]):
    for spins in [(0,1),(1,2,3),(0,2,4,6),(1,1,1,1,1,1,1,1)]:
        lambdas=[mp.mpf(l*(l+2))/4 for l in spins]
        total=sum(lambdas)
        product=mp.fprod(mp.besseli(l+1,2*beta)/mp.besseli(1,2*beta) for l in spins)
        heat=mp.exp(-total/beta)
        bound=(a0*total+(b0+mp.mpf(".5"))*total**2)/beta**2
        check(f"dimension-free tensor multiplier beta={beta}, spins={spins}",
              abs(product-heat)<=bound,"numerical")
        check(f"tensor quadratic sum spins={spins}, beta={beta}",
              sum(t*t for t in lambdas)<=total**2)

# Exact original radius-two vector fields on quaternion polynomials.
x = sp.symbols("x0:4", real=True)
kappa,b,h = sp.symbols("kappa b h", positive=True)
vec = sp.Matrix(x[1:])
fields = []
for a in range(3):
    unit = sp.eye(3)[:,a]
    fields.append(sp.Matrix([-x[a+1]/2, *((x[0]*unit+unit.cross(vec))/2)]))
def X(a,f):
    return sp.expand(sum(fields[a][i]*sp.diff(f,x[i]) for i in range(4)))
def K(f):
    return sp.expand(-sum(X(a,X(a,f)) for a in range(3)))
def gam(f,g):
    return sp.expand(sum(X(a,f)*X(a,g) for a in range(3)))
def zero_sphere(f):
    # The vector fields are tangential; reduce only the exact unit-sphere relation.
    return sp.rem(sp.Poly(sp.expand(f),x[3]),sp.Poly(sum(t*t for t in x)-1,x[3])).as_expr()==0
for l in range(9):
    chi=sp.chebyshevu(l,x[0])
    check(f"radius-two Casimir l={l}",zero_sphere(K(chi)-sp.Rational(l*(l+2),4)*chi))
V=b*(2-2*x[0])
f=1+x[0]*x[1]+2*x[2]*x[3]+x[1]**2*x[2]
H=lambda f:kappa*K(f)+V*f
check("full potential product rule",sp.expand(K(V*f)-V*K(f)-K(V)*f+2*gam(V,f))==0)
forward=kappa**2*K(K(f))+2*kappa*V*K(f)+kappa*K(V)*f-2*kappa*gam(V,f)+V**2*f
check("H squared full scalar and cross terms",sp.expand(H(H(f))-forward)==0)
reverse=H(H(f))-V*H(f)-kappa*V*K(f)-kappa*K(V)*f+2*kappa*gam(V,f)
check("reverse H graph identity",sp.expand(kappa**2*K(K(f))-reverse)==0)
A=sp.exp(-h*V/2)
lhs=A*K(A*f)-K(f)
rhs=(A*A-1)*K(f)-h*A*A*K(V)*f/2-h*h*A*A*gam(V,V)*f/4+h*A*A*gam(V,f)
check("exponential product identity signs AT28",sp.simplify(lhs-rhs)==0)
check("four-derivative coefficient",sum(math.comb(4,r)*2**r for r in range(5))==81)
check("Bell and Leibniz constants",15*2**2==60 and 15*2**4==240)

# Exact noncommuting plaquette, gauge change, trace and quaternion identities.
I=sp.I
pauli=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-I],[I,0]]),sp.diag(1,-1)]
Ts=[-I*s/2 for s in pauli]
def unitq(p,q,r):
    den=sp.Integer(1+p*p+q*q+r*r)
    vals=[(1-p*p-q*q-r*r)/den,2*sp.Integer(p)/den,2*sp.Integer(q)/den,2*sp.Integer(r)/den]
    return vals[0]*sp.eye(2)-I*sum((vals[i+1]*pauli[i] for i in range(3)),sp.zeros(2))
U,Up,qs,qt,hs,ht,hsp,htp=[unitq(*v) for v in
    [(1,2,0),(0,1,2),(2,1,1),(1,-1,2),(2,0,1),(0,-2,1),(1,1,-1),(-1,2,1)]]
pla=U*qt*Up.inv()*qs.inv()
alpha=qs*Up*qt.inv()
check("temporal orientation inverse",
      sp.simplify(pla.inv()-alpha*U.inv())==sp.zeros(2))
Ug=hs.inv()*U*ht
Upg=hsp.inv()*Up*htp
qsg=hs.inv()*qs*hsp
qtg=ht.inv()*qt*htp
check("original temporal gauge law",
      sp.simplify(Ug*qtg*Upg.inv()*qsg.inv()-hs.inv()*pla*hs)==sp.zeros(2))
qfun=lambda A:sp.Matrix([-2*sp.trace(T*A) for T in Ts])
check("original two-word phase trace identity",
      sp.simplify(qfun(U).dot(qfun(Up))-sp.trace(U*Up.inv())+sp.trace(U*Up))==0)
check("radius-two electric versus original c metric",
      all(sp.simplify(-2*sp.trace(Ts[a]*Ts[c]))==int(a==c) and
          sp.simplify(-sp.trace(Ts[a]*Ts[c])/2)==sp.Rational(int(a==c),4)
          for a in range(3) for c in range(3)))

# Complete finite coefficient sums, including the excluded direction-three corner.
for L in (2,3,5,8):
    m=2*L;n=m+1;theta=mp.pi/(2*n)
    v0=1/mp.sqrt(n)
    vv=lambda z:mp.sqrt(mp.mpf(2)/n)*mp.cos(mp.pi*(z+mp.mpf(".5"))/n)
    ww=lambda z:-mp.sqrt(mp.mpf(2)/n)*mp.sin(mp.pi*(z+1)/n)
    a_sum=mp.mpf(0);b_sum=mp.mpf(0)
    for i in range(1,m+1):
        for k in range(m):
            for z in range(m+1):
                a_sum+=abs(-vv(i)*ww(k)*v0/mp.sqrt(2))
                b_sum+=abs(v0*ww(k)*vv(z)/mp.sqrt(2))
    for i in range(m+1):
        for k in range(m+1):
            if (i,k)==(0,0):continue
            for z in range(m):
                b_sum+=abs(-v0*vv(k)*ww(z)/mp.sqrt(2))
    cot=mp.cot(theta);cos=mp.cos(theta)
    check(f"full row one sum L={L}",close(a_sum,mp.sqrt(mp.mpf(2)/n)*cot*(cot-cos)), "numerical")
    check(f"full row three sum L={L}",close(b_sum,mp.sqrt(mp.mpf(2)/n)*((2-mp.mpf(1)/n)*cot*cot-cos*cot/n)), "numerical")

# Complete root-word occurrences on the smallest original open box L=2.
m=4
def rootword(i,k,z):
    return [(0,0,r,3) for r in range(z)]+[(0,s,z,2) for s in range(k)]+[(v,k,z,1) for v in range(i)]
chords=[(i,k,z,2) for i in range(1,m+1) for k in range(m) for z in range(m+1)]
chords += [(i,k,z,3) for i in range(m+1) for k in range(m+1) if (i,k)!=(0,0) for z in range(m)]
wordcounts=[]
for i,k,z,direction in chords:
    target=(i,k+1,z) if direction==2 else (i,k,z+1)
    wordcounts.append(Counter(rootword(i,k,z)+[(i,k,z,direction)]+rootword(*target)))
check("all complete chord occurrences are at most two",max(max(c.values()) for c in wordcounts)==2)
check("all two-chord full words have at most four occurrences",max(max((c+d).values()) for c in wordcounts for d in wordcounts)==4)

# Noncommuting transfer calculation in a finite character compression.
# This checks the estimate algebra on a computable representation; it is not
# identified with the original many-edge vacuum or its actual endpoint.
size=18
Kmat=np.diag([l*(l+2)/4 for l in range(size)])
kap=.7;bb=.31
Vmat=bb*(2*np.eye(size)-np.eye(size,k=1)-np.eye(size,k=-1))
Hmat=kap*Kmat+Vmat
d=3;N=1;M=1
V0=4*bb;V1=math.sqrt(d)*bb;V2=d*bb/2
h2=kap**2+2*kap*V0+kap*V2+2*kap*V1+V0**2
k1=(1+V0)/kap
k2=((1+V0)**2+kap*V2+2*kap*V1*math.sqrt(k1))/kap**2
dl=V0**2/2+kap*(V0+V2/2+V1**2/4+V1)+kap**2*(60*d*float(a0)+240*d*d*(float(b0)+1))+h2/2
ctr=dl*(1+k2)
rng=np.random.default_rng(20261011)
fv=rng.normal(size=size);fv/=np.linalg.norm(fv)
qh=np.linalg.norm(fv)+np.linalg.norm(Hmat@Hmat@fv)
for step in (.001,.002,.005):
    beta=1/(kap*step)
    wm=np.diag([ive(l+1,2*beta)/ive(1,2*beta) for l in range(size)])
    am=expm(-step*Vmat/2)
    tm=am@wm@am
    check(f"noncommuting compressed transfer local step={step}",
          np.linalg.norm((tm-expm(-step*Hmat))@fv) <= step*step*ctr*qh,"numerical")
    for power in (2,7,20):
        check(f"noncommuting telescoping power={power}, step={step}",
          np.linalg.norm((np.linalg.matrix_power(tm,power)-expm(-power*step*Hmat))@fv)
          <=power*step*step*ctr*qh,"numerical")

# Exact scalar coefficients underlying filtering and the receiving sequence.
j,us,zeta,af2,s=sp.symbols("j us zeta af2 s",positive=True)
check("correlation error budget AT57",
      sp.simplify((1+2/us)/(4*j*(1+2/us))-1/(4*j))==0)
check("probe budget with positive slack",
      sp.simplify(1/(2*j)-af2/(2*j*(1+af2)))==1/(2*j*(af2+1)))
check("total endpoint error",sp.Rational(1,4)+sp.Rational(1,2)==sp.Rational(3,4))
for xval in [mp.mpf(t) for t in ("0","0.0001",".03",".5","1","3","100")]:
    check(f"spectral defect sign x={xval}",
          0<=xval+mp.expm1(-xval)<=xval*xval/2,"numerical")
    integral=mp.quad(lambda r:(1-r)*xval*xval*mp.exp(-r*xval),[0,1])
    check(f"exact next defect integral x={xval}",
          close(integral,xval+mp.expm1(-xval)),"numerical")

# Positive finite matrix vacuum-filter ratio, with full energy shift.
energies=np.array([.4,1.1,2.3])
psi=np.array([1.,0.,0.])
boundary=np.array([.6,.64,.48])
check("filter test unit boundary",abs(np.linalg.norm(boundary)-1)<1e-14,"numerical")
fm=np.array([[.2,1.,-.3],[1.,-.4,.6],[-.3,.6,.1]])
fbound=np.linalg.norm(fm,2)
for B in (2.,4.,7.):
    eta=boundary[1:]/boundary[0]*np.exp(-B*(energies[1:]-energies[0]))
    r=np.linalg.norm(eta)
    for t in (0.,.5,2.):
        y=np.exp(-B*energies)*boundary
        num=y@fm@np.diag(np.exp(-t*energies))@fm@y
        den=np.dot(boundary*boundary,np.exp(-(2*B+t)*energies))
        true=(fm@psi)@np.diag(np.exp(-t*(energies-energies[0])))@(fm@psi)
        check(f"vacuum-filter cross terms B={B}, t={t}",
              abs(num/den-true)<=fbound*fbound*(2*r+2*r*r)+1e-14,"numerical")

text=(ROOT/"ANISOTROPIC_TEMPORAL_BRIDGE.md").read_text(encoding="utf-8")
labels=re.findall(r"\\tag\{AT(\d+)\}",text)
check("all AT1--AT60 labels exactly once",Counter(labels)==Counter(map(str,range(1,61))),"structure")
check("inline delimiters balanced",text.count(r"\(")==text.count(r"\)"),"structure")
check("display delimiters balanced",text.count(r"\[")==text.count(r"\]"),"structure")
check("no damaged TeX controls",not re.search(r"(?<!\\)\b(?:qquad|quad|tag\{AT)\b",text),"structure")
report={
    "observed_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "total":len(checks),"counts_by_kind":dict(Counter(c["kind"] for c in checks)),
    "all_passed":True,
    "proof_sha256":hashlib.sha256((ROOT/"ANISOTROPIC_TEMPORAL_BRIDGE.md").read_bytes()).hexdigest(),
    "scope":"Exact algebra, orientation, original coefficient/occurrence checks, independent compact-group quadrature, numerical representation checks, and source integrity. No actual growing-box endpoint value is computed.",
    "constants":{"D1":str(D[1]),"D2":str(D[2]),"a0":str(a0),"b0":str(b0)},
    "checks":checks
}
(ROOT/"TEMPORAL_BRIDGE_CHECKS.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:report[k] for k in ("total","counts_by_kind","all_passed","proof_sha256")},indent=2))
