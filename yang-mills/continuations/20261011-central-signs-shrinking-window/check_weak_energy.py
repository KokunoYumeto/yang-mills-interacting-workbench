from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import itertools,json,math,time
import numpy as np
import sympy as s
from weak_energy_constants import constants,report,leading_energy,mp,partitions,fall,triples
O=Path(__file__).resolve().parent;start=time.time();checks=[]
def ck(name,yes,**data):
    checks.append(dict(name=name,passed=bool(yes),**data));assert yes,(name,data)
ORDER=6;zero=(0,0,0,0);one={zero:F(1)}
def add(a,b):
    c=a.copy()
    for p,v in b.items():c[p]=c.get(p,F(0))+v
    return {p:v for p,v in c.items() if v}
def scale(a,k):return {p:v*k for p,v in a.items() if v*k}
def mul(a,b):
    out={}
    for p,v in a.items():
        for q,w in b.items():
            k=tuple(p[i]+q[i] for i in range(4))
            if sum(k)<=ORDER:out[k]=out.get(k,F(0))+v*w
    return {p:v for p,v in out.items() if v}
def diff(a,i):
    out={}
    for p,v in a.items():
        if p[i]:q=list(p);q[i]-=1;out[tuple(q)]=v*p[i]
    return out
def val(a):return a.get(zero,F(0))
coords=[]
for i,p0 in enumerate([F(3,5),F(4,5),F(0),F(0)]):
    p=list(zero);p[i]=1;coords.append({zero:p0,tuple(p):F(1)} if p0 else {tuple(p):F(1)})
def eps(i,j,k):return 0 if len({i,j,k})<3 else (1 if (i,j,k) in [(0,1,2),(1,2,0),(2,0,1)] else -1)
def X(i,f):
    out=add(scale(mul(coords[i+1],diff(f,0)),-1),mul(coords[0],diff(f,i+1)))
    for j,k in itertools.product(range(3),repeat=2):
        e=eps(i,j,k)
        if e:out=add(out,scale(mul(coords[j+1],diff(f,k+1)),e))
    return scale(out,F(1,2))
def inv(f):
    f0=val(f);u=scale(add(f,{zero:-f0}),-1/f0);out=one;term=one
    for n in range(1,ORDER+1):term=mul(term,u);out=add(out,term)
    return scale(out,1/f0)

def sub(a,b):return add(a,scale(b,-1))
def psum(v):return sum_poly(list(v))
def sum_poly(v):
    out={}
    for x in v:out=add(out,x)
    return out
def lap(f):return psum(X(i,X(i,f)) for i in range(3))
def pw(f,n):
    out=one
    for _ in range(n):out=mul(out,f)
    return out
def word(f,seq):
    for i in reversed(seq):f=X(i,f)
    return f
psi=add(one,add(scale(coords[0],F(1,7)),scale(mul(coords[1],coords[2]),F(1,11))))
ip=inv(psi);kap=F(3,5);vac=F(7,9)
V=add({zero:vac},scale(mul(lap(psi),ip),kap))
a=[mul(X(i,psi),ip) for i in range(3)]
def aj(seq):return mul(word(psi,seq),ip)
def DD(i,f):return add(X(i,f),scale(mul(a[i],f),2))
def div(cs):return psum(DD(i,cs[i]) for i in range(3))
def dot(v,w):return psum(mul(x,y) for x,y in zip(v,w))
v1=[X(i,V) for i in range(3)]
v2=[[X(i,v1[j]) for j in range(3)] for i in range(3)]
v=add(coords[2],mul(mul(coords[0],coords[1]),coords[3]))
for j in range(3):
    ck('exact ordered Casimir contraction '+str(j),
       val(psum(X(h,X(j,X(h,v))) for h in range(3)))==val(add(X(j,lap(v)),X(j,v))))
    for delta in range(3):
        ck('original epsilon double contraction '+str((j,delta)),
           sum(eps(h,j,c)*eps(c,h,delta) for h,c in itertools.product(range(3),repeat=2))==2*(j==delta))
for n in range(3):
    for J in itertools.product(range(3),repeat=n):
        lhs=div([aj((h,)+J) for h in range(3)])
        rhs=add(scale(mul(ip,word(mul(sub(V,{zero:vac}),psi),J)),1/kap),
                dot(a,[aj((h,)+J) for h in range(3)]))
        ck('complete ground divergence length '+str(J),val(lhs)==val(rhs))
A0=add(scale(sub(V,{zero:vac}),1/kap),dot(a,a))
for i in range(3):
    c=[add(mul(v1[h],a[i]),scale(mul(v1[i],a[h]),2)) for h in range(3)]
    rhs=psum([mul(a[i],lap(V)),dot(v1,[aj((h,i)) for h in range(3)]),
              mul(a[i],dot(a,v1)),scale(dot(a,[v2[h][i] for h in range(3)]),2),
              scale(mul(v1[i],A0),2)])
    ck('full product divergence coefficient '+str(i),val(div(c))==val(rhs))
cross=[dot(a,[v2[j][h] for j in range(3)]) for h in range(3)]
rhs=psum(mul(add(aj((h,j)),mul(a[h],a[j])),v2[j][h])
         for h,j in itertools.product(range(3),repeat=2))
rhs=add(rhs,dot(a,[add(X(j,lap(V)),v1[j]) for j in range(3)]))
ck('full ordered potential divergence with complete general potential',val(div(cross))==val(rhs))

# The positive-half ordered chain rule is checked on the actual square alpha^2,
# retaining noncommuting fields, internal pairs and split shared indices.
alpha=psi;rho=mul(alpha,alpha)
jets={'alpha':alpha,'rho':rho}
@lru_cache(None)
def derivative(name,J):return jets[name] if not J else X(J[-1],derivative(name,J[:-1]))
@lru_cache(None)
def contract(name,J,r):
    return sum(val(derivative(name,tuple(z for i in ii for z in (i,i))+J))
               for ii in itertools.product(range(3),repeat=r))
for r,m in [(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1)]:
    for J in itertools.product(range(3),repeat=m):
        rhs=F(0)
        for pi in partitions(m+2*r):
            owners={p:k for k,B in enumerate(pi) for p in B}
            split=[a for a in range(r) if owners[2*a]!=owners[2*a+1]]
            internal={a for a in range(r) if a not in split}
            factor=fall(F(1,2),len(pi))
            for assignment in itertools.product(range(3),repeat=len(split)):
                labels={p:i for a,i in zip(split,assignment) for p in [2*a,2*a+1]}
                labels.update({2*r+k:i for k,i in enumerate(J)})
                term=factor
                for B in pi:
                    rb=sum(2*a in B and 2*a+1 in B for a in internal)
                    term*=contract('rho',tuple(labels[p] for p in B if p in labels),rb)/val(rho)
                rhs+=term
        ck('complete positive-half partition '+str((m,r,J)),rhs==contract('alpha',J,r)/val(alpha))

# Haar integration on the radius-two SU2 sphere in its original quaternion
# coordinates. Its probability measure is unchanged. All factors stay explicit.
ORDER=24
coords=[]
for i in range(4):
    p=[0]*4;p[i]=1;coords.append({tuple(p):F(1)})
def haar(f):
    out=F(0)
    for p,v in f.items():
        if any(n%2 for n in p):continue
        k=[n//2 for n in p];num=math.prod(math.prod(range(1,2*n,2)) for n in k)
        den=math.prod(4+2*i for i in range(sum(k)))
        out+=v*F(num,den)
    return out
def hess(f,i,j):
    return add(X(i,X(j,f)),scale(psum(scale(X(k,f),eps(i,j,k)) for k in range(3)),F(1,2)))
psi=add(one,add(scale(coords[0],F(1,7)),scale(mul(coords[1],coords[2]),F(1,11))))
mass=haar(mul(psi,psi))
for idx,t in enumerate([coords[0],mul(coords[1],coords[2]),add(coords[3],mul(coords[0],mul(coords[1],coords[2])))]):
    grad=[X(i,t) for i in range(3)];dpsi=[X(i,psi) for i in range(3)]
    psiLu=scale(add(mul(psi,lap(t)),scale(dot(dpsi,grad),2)),-kap)
    ordered=psum(pw(X(i,X(j,t)),2) for i,j in itertools.product(range(3),repeat=2))
    hessint=psum(mul(sub(mul(psi,hess(psi,i,j)),mul(dpsi[i],dpsi[j])),mul(grad[i],grad[j]))
                for i,j in itertools.product(range(3),repeat=2))
    ck('exact weighted ordered-Hessian energy '+str(idx),
       haar(mul(pw(psi,2),ordered))/mass==haar(pw(psiLu,2))/(mass*kap**2)+2*haar(hessint)/mass)
    rhs=add(psum(pw(hess(t,i,j),2) for i,j in itertools.product(range(3),repeat=2)),scale(dot(grad,grad),F(1,2)))
    ck('exact radius-two Hessian connection identity '+str(idx),sub(ordered,rhs)=={})

# Conditional integration on two SU2 factors: integrate every polynomial
# in the outside coordinate against its exact Haar moments.
x,y=s.symbols('x y');eta=s.Rational(1,7);ps=1+eta*x*y
def haary(expr):
    out=0
    for (n,),v in s.Poly(s.cancel(expr),y).terms():
        if n%2:continue
        out+=v*s.Rational(math.prod(range(1,n,2)),math.prod(4+2*i for i in range(n//2)))
    return s.cancel(out)
rh=haary(ps**2);a=s.diff(ps,x)/ps
def cond(f):return s.cancel(haary(ps**2*f)/rh)
for c in [x+y,x*y+y**2,1+x**2*y**3]:
    bar=cond(c);ab=cond(a)
    ck('conditional derivative retains covariance '+str(c),
       s.cancel(s.diff(bar,x)-cond(s.diff(c,x))-2*(cond(a*c)-ab*bar))==0)
    Dc=s.diff(c-bar,x)+2*a*(c-bar)
    ck('weighted centered derivative conditional mean '+str(c),cond(Dc)==0)

# Full noncommuting block compression and the exact variational kernel norm.
# These finite Hermitian fixtures are algebra diagnostics, not Wilson states.
for n in [5,8,12]:
    for rep in range(8):
        rng=np.random.default_rng(20261015+n*100+rep)
        mat=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        U=np.linalg.qr(mat)[0];lam=np.r_[0,np.exp(rng.uniform(-2,2,n-1))]
        L=(U*lam)@U.conj().T;k=.8;z=.3
        m=n//2;J=np.eye(n,dtype=complex)[:,:m];Q=np.eye(n,dtype=complex)[:,m:]
        A=J.conj().T@L@J;K=Q.conj().T@L@J;D=Q.conj().T@L@Q
        e1=21*z/4;e2=21*z*z/4;e3=z**3
        cubic=L@L@L+e1*L@L+e2*L+e3*np.eye(n)
        full=A@A@A+A@K.conj().T@K+K.conj().T@K@A+K.conj().T@D@K+e1*(A@A+K.conj().T@K)+e2*A+e3*np.eye(m)
        ck('complete cubic block with complementary coupling '+str((n,rep)),np.linalg.norm(J.conj().T@cubic@J-full)<1e-9)
        # d satisfies k d* d=L; no invertibility of L or removal of its vacuum.
        d=np.diag(np.sqrt(lam/k))@U.conj().T
        G=rng.normal(size=n)+1j*rng.normal(size=n);S=rng.normal(size=n)+1j*rng.normal(size=n)
        Wv=-d.conj().T@G-S;xi=np.linalg.solve(L+z*np.eye(n),Wv)
        G0=-k*d@xi;S0=-z*xi;GK=G-G0;SK=S-S0
        b=np.vdot(Wv,xi).real
        pair=np.vdot(G,G).real/k+np.vdot(S,S).real/z
        knorm=np.vdot(GK,GK).real/k+np.vdot(SK,SK).real/z
        ck('full divergence right inverse and kernel component '+str((n,rep)),
           np.linalg.norm(-d.conj().T@GK-SK)<1e-10 and abs(pair-b-knorm)<1e-9 and
           abs(np.vdot(G0,GK)/k+np.vdot(S0,SK)/z)<1e-10)

path=[]
for j in [4,5,8,16,64,1024,10**8,10**24]:
    data=constants(j);row=report(data);path.append(row)
    ck('full finite energy exponent '+str(j),data['energy'].degree==76 and data['oldenergy'].degree==91)
    ck('six complete flux exponents '+str(j),[data['fterms'][p].degree for p in data['C']]==[F(61,2),13,18,F(61,2),F(35,2),F(61,2)])
    ck('six complete scalar exponents '+str(j),[data['sterms'][p].degree for p in data['C']]==[F(75,2),20,25,F(75,2),F(49,2),F(75,2)])
    ck('best bound keeps both finite estimates '+str(j),data['best'].value<=data['energy'].value and data['best'].value<=data['oldenergy'].value)
for k,theta in [('0.8','1'),('2','0.7'),('0.1','2')]:
    data=constants(7,k,theta)
    ck('independent exact leading coefficient '+str((k,theta)),
       abs(data['energy'].leading/leading_energy(k,theta)-1)<mp.mpf('1e-65'))
ck('complete upper function leading convergence',abs(mp.mpf(path[-1]['ratio_to_leading'])-1)<mp.mpf('1e-20'))
result=dict(checks=len(checks),all_passed=all(c['passed'] for c in checks),seconds=time.time()-start,details=checks,path=path,
 scope='Exact rational original SU2 noncommuting field, ground divergence, positive-half partition and weighted Hessian identities; conditional integration with its covariance; full noncommuting Hermitian block and variational kernel fixtures with vacuum; complete80-digit original-path upper functions and independent leading coefficients. Constructed positive-ground fixtures are not Wilson states. No actual spectral survival or vanishing residual is measured.')
(O/'WEAK_ENERGY_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=result['checks'],all_passed=result['all_passed'],seconds=result['seconds'],log10_j4=path[0]['log10_energy'],degree=path[0]['degree'])))
