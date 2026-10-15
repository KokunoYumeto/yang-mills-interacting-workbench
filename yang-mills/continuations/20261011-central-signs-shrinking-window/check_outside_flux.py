from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import itertools,json,time,math
import numpy as np
import sympy as s
O=Path(__file__).resolve().parent;start=time.time();checks=[]
def ck(name,yes,**data):
    checks.append(dict(name=name,passed=bool(yes),**data))
    assert yes,(name,data)

# Exact rational functions on two original quaternion factors. A dictionary
# records every numerator coefficient and power of the one common positive
# denominator psi. No field word is commuted or truncated.
Z=(0,)*8
def padd(a,b):
    c=a.copy()
    for p,v in b.items():c[p]=c.get(p,F(0))+v
    return {p:v for p,v in c.items() if v}
def pscale(a,z):return {p:v*z for p,v in a.items() if v*z}
def pmul(a,b):
    c={}
    for p,v in a.items():
        for q,w in b.items():
            r=tuple(x+y for x,y in zip(p,q));c[r]=c.get(r,F(0))+v*w
    return {p:v for p,v in c.items() if v}
def pdiff(a,i):
    c={}
    for p,v in a.items():
        if p[i]:
            q=list(p);q[i]-=1;c[tuple(q)]=v*p[i]
    return c
def eps(i,j,k):return 0 if len({i,j,k})<3 else (1 if (i,j,k) in [(0,1,2),(1,2,0),(2,0,1)] else -1)
coords=[]
for i in range(8):
    q=list(Z);q[i]=1;coords.append({tuple(q):F(1)})
def px(i,p):
    link=i//3;col=i%3;off=link*4
    out=padd(pscale(pmul(coords[off+col+1],pdiff(p,off)),-1),pmul(coords[off],pdiff(p,off+col+1)))
    for j,k in itertools.product(range(3),repeat=2):
        if eps(col,j,k):out=padd(out,pscale(pmul(coords[off+j+1],pdiff(p,off+k+1)),eps(col,j,k)))
    return pscale(out,F(1,2))
one={Z:F(1)}
psi=padd(one,padd(pscale(pmul(coords[0],coords[4]),F(1,7)),pscale(pmul(coords[1],coords[6]),F(1,11))))
point=[F(3,5),F(4,5),F(0),F(0),F(5,13),F(12,13),F(0),F(0)]
def pval(p):return sum(v*math.prod(x**n for x,n in zip(point,q)) for q,v in p.items())
pv=pval(psi)
def ra(a,b):
    out={k:v.copy() for k,v in a.items()}
    for k,v in b.items():out[k]=padd(out.get(k,{}),v)
    return {k:v for k,v in out.items() if v}
def rs(a,z):return {k:pscale(v,z) for k,v in a.items() if z}
def rm(a,b):
    out={}
    for i,p in a.items():
        for j,q in b.items():out[i+j]=padd(out.get(i+j,{}),pmul(p,q))
    return {k:v for k,v in out.items() if v}
def rx(i,a):
    out={}
    for n,p in a.items():
        out[n]=padd(out.get(n,{}),px(i,p))
        if n:out[n+1]=padd(out.get(n+1,{}),pscale(pmul(p,px(i,psi)),-n))
    return {k:v for k,v in out.items() if v}
def rsum(xs):
    out={}
    for x in xs:out=ra(out,x)
    return out
def rv(a):return sum(pval(p)/pv**n for n,p in a.items())
def word(a,J):
    for i in reversed(J):a=rx(i,a)
    return a
@lru_cache(None)
def aa(J):
    p=psi
    for i in reversed(J):p=px(i,p)
    return {1:p}
kap=F(3,5);vac=F(7,9);e1=F(21,4)*F(2,7);e2=F(21,4)*F(2,7)**2
V=ra({0:{Z:vac}},rs(rsum(aa((i,i)) for i in range(6)),kap))
U=rs(rsum(aa((i,i)) for i in range(3,6)),kap)
@lru_cache(None)
def vj(J):return word(V,J)
@lru_cache(None)
def uj(J):return word(U,J)
def LL(f):return rs(rsum(ra(rx(o,rx(o,f)),rs(rm(aa((o,)),rx(o,f)),2)) for o in range(3,6)),-kap)
@lru_cache(None)
def DD(o,J):return ra(aa((o,)+J),rs(rm(aa((o,)),aa(J)),-1))
@lru_cache(None)
def RR(J):
    out={}
    for mask in range(1,1<<len(J)):
        A=tuple(J[i] for i in range(len(J)) if mask&(1<<i));B=tuple(J[i] for i in range(len(J)) if not mask&(1<<i))
        out=ra(out,rs(rm(uj(A),aa(B)),-1))
    return out
@lru_cache(None)
def EE(J):return LL(vj(J))
for J in [(0,),(3,),(0,1),(1,0),(3,4),(0,3),(0,1,2),(2,1,0),(0,3,4)]:
    ck('full original ground-ratio outside generator '+str(J),rv(LL(aa(J)))==rv(RR(J)))
for h,i,j in [(0,1,2),(2,0,1),(1,1,0)]:
    cs=[
      rs(aa((h,)),-6*kap**3),
      ra(rs(aa((h,)),4*e1*kap**2),rs(vj((h,)),-6*kap**2)),
      rsum([rs(aa((h,)),-2*kap*e2),rs(vj((h,)),6*kap**2+2*e1*kap),
            rs(rsum(rm(aa((l,)),vj((l,h))) for l in range(6)),-4*kap**2)]),
      rs(aa((h,i)),-12*kap**3),
      rsum([rs(aa((h,i)),4*e1*kap**2),rs(vj((h,i)),-8*kap**2),
            rs(ra(rm(vj((h,)),aa((i,))),rs(rm(vj((i,)),aa((h,))),2)),-4*kap**2)]),
      rs(aa((h,j,i)),-8*kap**3)]
    es=[
      rs(RR((h,)),-6*kap**3),
      ra(rs(RR((h,)),4*e1*kap**2),rs(EE((h,)),-6*kap**2)),
      rsum([rs(RR((h,)),-2*kap*e2),rs(EE((h,)),6*kap**2+2*e1*kap),
        rs(rsum(rsum([rm(RR((l,)),vj((l,h))),rm(aa((l,)),EE((l,h))),
           rs(rsum(rm(DD(o,(l,)),vj((o,l,h))) for o in range(3,6)),-2*kap)]) for l in range(6)),-4*kap**2)]),
      rs(RR((h,i)),-12*kap**3),
      rsum([rs(RR((h,i)),4*e1*kap**2),rs(EE((h,i)),-8*kap**2),
        rs(rsum([rm(EE((h,)),aa((i,))),rm(vj((h,)),RR((i,))),
          rs(rsum(rm(vj((o,h)),DD(o,(i,))) for o in range(3,6)),-2*kap),
          rs(rm(EE((i,)),aa((h,))),2),rs(rm(vj((i,)),RR((h,))),2),
          rs(rsum(rm(vj((o,i)),DD(o,(h,))) for o in range(3,6)),-4*kap)]),-4*kap**2)]),
      rs(RR((h,j,i)),-8*kap**3)]
    for row,(c,e) in enumerate(zip(cs,es)):
        ck('six full outside generator rows '+str((h,i,j,row)),rv(LL(c))==rv(e))
    for o in [3,4,5]:
        ds=[
          rs(DD(o,(h,)),-6*kap**3),
          ra(rs(DD(o,(h,)),4*e1*kap**2),rs(vj((o,h)),-6*kap**2)),
          rsum([rs(DD(o,(h,)),-2*kap*e2),rs(vj((o,h)),6*kap**2+2*e1*kap),
            rs(rsum(ra(rm(DD(o,(l,)),vj((l,h))),rm(aa((l,)),vj((o,l,h)))) for l in range(6)),-4*kap**2)]),
          rs(DD(o,(h,i)),-12*kap**3),
          rsum([rs(DD(o,(h,i)),4*e1*kap**2),rs(vj((o,h,i)),-8*kap**2),
            rs(rsum([rm(vj((o,h)),aa((i,))),rm(vj((h,)),DD(o,(i,))),
               rs(rm(vj((o,i)),aa((h,))),2),rs(rm(vj((i,)),DD(o,(h,))),2)]),-4*kap**2)]),
          rs(DD(o,(h,j,i)),-8*kap**3)]
        for row,(c,d) in enumerate(zip(cs,ds)):
            ck('six full outside derivative rows '+str((h,i,j,o,row)),rv(rx(o,c))==rv(d))
    f=ra({0:coords[2]},aa((3,)))
    def Dh(f):return ra(rx(h,f),rs(rm(aa((h,)),f),2))
    comm=ra(LL(Dh(f)),rs(Dh(LL(f)),-1))
    expected=ra(rs(rm(uj((h,)),f),-2),rs(rsum(rm(DD(o,(h,)),rx(o,f)) for o in range(3,6)),-2*kap))
    ck('complete weighted inside/outside commutator '+str(h),rv(comm)==rv(expected))

# Exact conditional quotient identity on two original SU2 factors; x,y
# denote their scalar quaternion coordinates, with the radius-two radial
# Laplacian and the full Haar moment of y squared equal to1/4.
x,y=s.symbols('x y');eta=s.Rational(1,7);ps=1+eta*x*y
rho=1+eta**2*x*x/4;ax=(1-x*x)/4;bx=-3*x/4
g=s.diff(ps,x)/ps;bar=s.diff(rho,x)/(2*rho)
K=(ax*s.diff(ps,x,2)+bx*s.diff(ps,x))/ps
Ka=ax*(s.diff(bar,x)+bar**2)+bx*bar
qdelta=ax*(s.diff(g-bar,x)+2*g*(g-bar))+bx*(g-bar)
ck('highest row exact kinetic plus score fluctuation',s.cancel(qdelta-K+Ka-ax*(g-bar)**2)==0)

# Matrix tests retain complex noncommuting inside/outside generators,
# a vacuum, dependent source columns and every matrix remainder.
def pinv(A):
    lam,U=np.linalg.eigh((A+A.conj().T)/2);cut=1e-11*max(1,float(lam.max()))
    inv=np.zeros_like(lam);np.divide(1,lam,out=inv,where=lam>cut)
    return (U*inv)@U.conj().T
for n in [5,8,11]:
    for rep in range(6):
        rng=np.random.default_rng(20261015+n*41+rep);k=.8;z=.19
        di=(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))/n
        do=(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))/n
        di[:,0]=0;do[:,0]=0
        L=k*(di.conj().T@di+do.conj().T@do);T=k*do.conj().T@do
        Gi=rng.normal(size=n)+1j*rng.normal(size=n)
        Go=rng.normal(size=n)+1j*rng.normal(size=n)
        S=rng.normal(size=n)+1j*rng.normal(size=n)
        q=S+do.conj().T@Go;eta0=np.linalg.solve(T+z*np.eye(n),q)
        Pop=(Gi,k*do@eta0,z*eta0)
        Wv=-di.conj().T@Gi-do.conj().T@Go-S;xi=np.linalg.solve(L+z*np.eye(n),Wv)
        Min=(-k*di@xi,-k*do@xi,-z*xi)
        norm=lambda P:(np.vdot(P[0],P[0]).real+np.vdot(P[1],P[1]).real)/k+np.vdot(P[2],P[2]).real/z
        sub=lambda A,B:tuple(a-b for a,b in zip(A,B))
        P0=(Gi,Go,S);b=np.vdot(Wv,xi).real
        ck('exact two kernel components '+str((n,rep)),abs(norm(P0)-b-norm(sub(Pop,Min))-norm(sub(P0,Pop)))<1e-9)
        ck('outside projection preserves full forcing '+str((n,rep)),np.linalg.norm(-di.conj().T@Pop[0]-do.conj().T@Pop[1]-Pop[2]-Wv)<1e-10)
        Q=rng.normal(size=(n,3))+1j*rng.normal(size=(n,3));Q[0,:]=0
        Q=np.column_stack([Q,Q[:,0]+2j*Q[:,1]])
        lam,U0=np.linalg.eigh(T);lam=np.maximum(lam,0)
        fn=lambda f:(U0*f(lam))@U0.conj().T
        M0=Q.conj().T@Q;M1=Q.conj().T@T@Q;M2=Q.conj().T@T@T@Q
        H=M2+z*M1;K=M1+z*M0;Hp=pinv(H);Kp=pinv(K)
        I=Q.conj().T@np.linalg.solve(T+z*np.eye(n),Q)
        A=fn(lambda l:np.sqrt(l/(l+z)))@Q;Bv=fn(lambda l:np.sqrt(l*(l+z)))@Q
        C=fn(lambda l:1/np.sqrt(l+z))@Q;D=fn(lambda l:np.sqrt(l+z))@Q
        R1=A-Bv@Hp@M1;R0=C-D@Kp@M0
        ck('complete noncommuting matrix upper residual '+str((n,rep)),np.linalg.norm(M0-z*I-M1@Hp@M1-R1.conj().T@R1)<1e-8)
        ck('complete noncommuting matrix lower residual '+str((n,rep)),np.linalg.norm(I-M0@Kp@M0-R0.conj().T@R0)<1e-8)
        raw=rng.normal(size=4)+1j*rng.normal(size=4)
        line=np.vdot(raw,M1@raw).real**2/np.vdot(raw,H@raw).real
        matrix=np.vdot(raw,M1@Hp@M1@raw).real
        ck('full matrix improvement retains source direction '+str((n,rep)),matrix>=line-1e-9)
for j in [4,5,16,100]:
    m=2*j**4;N=3*m*(m+1)**2;Nq=300*j*(100*j+1)**2
    ns=[12*m,12*m*(m-1),3*m*(m-1)**2-Nq]
    ck('complete original outside counts '+str(j),sum(ns)==N-Nq and min(ns)>=0)
result=dict(checks=len(checks),all_passed=True,seconds=time.time()-start,details=checks,
 scope='Exact rational two-factor original SU2 fields with all six coefficient tables and noncommuting ordered ratios, on a constructed positive ground and its own potential; exact conditional leading-row identity; complex matrix projection and full moment residual identities retaining vacuum and singular source columns; original outside counts. No Wilson spectral moment is sampled or inferred.')
(O/'OUTSIDE_FLUX_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='details'}))
