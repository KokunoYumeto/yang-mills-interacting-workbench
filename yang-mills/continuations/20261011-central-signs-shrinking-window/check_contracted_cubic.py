from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import itertools,json,math,time
import numpy as np
import sympy as s
from contracted_constants import constants,report,partitions,triples,block_types,mp,leading_coefficient
O=Path(__file__).resolve().parent;start=time.time();checks=[]
def ck(name,yes,**data):
    checks.append(dict(name=name,passed=bool(yes),**data));assert yes,(name,data)

# Exact rational ambient jets on the original unit quaternion coordinates.
# The vector fields carry the original factor 1/2, hence the radius-two metric.
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
h=add(one,add(scale(coords[0],F(1,5)),scale(coords[1],F(1,7))))
alpha=inv(h);rho=mul(alpha,alpha)
v=add(coords[2],add(mul(coords[0],coords[1]),mul(mul(coords[1],coords[2]),coords[3])))
jets={'h':h,'rho':rho,'v':v,'hv':mul(h,v)}
@lru_cache(None)
def derivative(name,word):
    return jets[name] if not word else X(word[-1],derivative(name,word[:-1]))
@lru_cache(None)
def contracted(name,word,r):
    out=F(0)
    for ii in itertools.product(range(3),repeat=r):
        pairs=tuple(z for i in ii for z in (i,i));out+=val(derivative(name,pairs+word))
    return out
def subs(n):
    for mask in range(1<<n):yield tuple(i for i in range(n) if mask&(1<<i))
for i,j in [(0,1),(1,2),(2,0)]:
    z=val(add(X(i,X(j,v)),scale(X(j,X(i,v)),-1)))
    ck(f'original noncommuting field bracket {i}/{j}',z==-sum(eps(i,j,k)*val(X(k,v)) for k in range(3)))
for r in range(4):
    for m in range(min(2,6-2*r)+1):
        for J in itertools.product(range(3),repeat=m):
            rhs=F(0)
            for aa,bb,cc,fac in triples(r):
                for K in itertools.product(range(3),repeat=cc):
                    for S in subs(m):
                        Sc=tuple(i for i in range(m) if i not in S)
                        JS=tuple(J[i] for i in S);JC=tuple(J[i] for i in Sc)
                        rhs+=fac*val(alpha)*contracted('h',K+JS,aa)*contracted('v',K+JC,bb)
            ck(f'full contracted product m{m} r{r} word{J}',val(alpha)*contracted('hv',J,r)==rhs)

# Contract every partition, retaining internal Laplacians and split shared indices.
for r in range(1,4):
    for m in range(7-2*r):
        words=list(itertools.product(range(3),repeat=m))
        if len(words)>12:words=words[::max(1,len(words)//9)]
        for J in words:
            rhs=F(0)
            for pi in partitions(m+2*r):
                owners={pos:k for k,B in enumerate(pi) for pos in B}
                split=[a for a in range(r) if owners[2*a]!=owners[2*a+1]]
                internal={a for a in range(r) if a not in split}
                factor=math.prod(F(-1,2)-n for n in range(len(pi)))
                for assignment in itertools.product(range(3),repeat=len(split)):
                    labels={p:i for a,i in zip(split,assignment) for p in [2*a,2*a+1]}
                    labels.update({2*r+k:i for k,i in enumerate(J)})
                    term=factor
                    for B in pi:
                        rb=sum(2*a in B and 2*a+1 in B for a in internal)
                        remain=tuple(labels[p] for p in B if p in labels)
                        term*=contracted('rho',remain,rb)/val(rho)
                    rhs+=term
            ck(f'all contracted inverse partitions m{m} r{r} word{J}',rhs==val(alpha)*contracted('h',J,r))

# Exact high-order compressed coefficients on two original quaternion factors.
# psi=1+eta*x0*y0 is positive; its potential is constructed from its ground equation.
x,y=s.symbols('x y');eta=s.Rational(1,7);kap=s.Rational(3,5);psi=1+eta*x*y
ax=(1-x*x)/4;ay=(1-y*y)/4;bx=-3*x/4;by=-3*y/4
drx=bx+2*ax*s.diff(psi,x)/psi;dry=by+2*ay*s.diff(psi,y)/psi
clean=s.cancel
def apply_L(rows,minimum):
    out={}
    for n,f in rows.items():
        pieces={n:-kap*(ax*s.diff(f,x,2)+drx*s.diff(f,x)+ay*s.diff(f,y,2)+dry*s.diff(f,y)),n+1:-kap*(2*ax*s.diff(f,x)+drx*f),n+2:-kap*ax*f}
        for k,z in pieces.items():
            if k>=minimum:out[k]=out.get(k,0)+z
    return {k:clean(z) for k,z in out.items()}
L1=apply_L({0:s.Integer(1)},0);L2=apply_L(L1,2);L3=apply_L(L2,4)
def haar_y(poly):
    poly=s.Poly(s.cancel(poly),y);out=0
    for (n,),c in poly.terms():
        if n%2:continue
        k=n//2;num=s.factorial2(n-1) if n else 1;den=math.prod(4+2*i for i in range(k));out+=c*num/den
    return clean(out)
rh=1+eta**2*x*x/4
bc={k:clean(haar_y(psi**2*z)/rh) for k,z in L3.items()}
h1=-eta**2*x/(4*rh)
h2=clean(-eta**2/(4*rh)+3*eta**4*x*x/(16*rh**2))
tilde5=clean(bc[5]+6*bc[6]*h1);tilde4=clean(bc[4]+5*bc[5]*h1+15*bc[6]*h2)
def apply_delta(rows):
    out={}
    for n,f in rows.items():
        for k,z in {n:ax*s.diff(f,x,2)+bx*s.diff(f,x),n+1:2*ax*s.diff(f,x)+bx*f,n+2:ax*f}.items():out[k]=out.get(k,0)+z
    return {k:clean(z) for k,z in out.items()}
dd=apply_delta(apply_delta(apply_delta({0:s.Integer(1)})))
alpha1=eta**2*x/(4*rh);alpha2=clean(eta**2/(4*rh)-eta**4*x*x/(16*rh**2))
U=kap*(ax*alpha2+bx*alpha1);variance=eta**2/(4*rh**2)
ck('exact original two-link fifth-order cancellation',clean(tilde5+kap**3*dd[5])==0)
ck('exact original fourth-order marginal potential and covariance',clean(tilde4+kap**3*dd[4]-3*kap**2*U*ax**2-12*kap**3*variance*ax**3)==0)
ck('exact conditional density contraction in two-link fixture',clean(ax*s.diff(rh,x,2)+bx*s.diff(rh,x)-eta**2*(1-4*x*x)/8)==0)

# Matrix trace estimate, including its exact rank-one equality case.
for dimension in [3,5,12,40]:
    for rep in range(16):
        rng=np.random.default_rng(20261015+dimension*31+rep)
        c=float(np.exp(rng.uniform(-2,2)));A=float(np.exp(rng.uniform(-2,4)))
        lam=rng.random(dimension);lam*=rng.random()*(A+dimension*c)/lam.sum();hess=lam-c
        H2=A*A+2*(dimension-1)*c*A+dimension*(dimension-1)*c*c
        ck(f'full Hessian trace ceiling {dimension}/{rep}',np.sum(hess*hess)<=H2*(1+1e-12))
    c=F(2,3);A=F(7,5);eigs=[A+(dimension-1)*c]+[-c]*(dimension-1)
    ck(f'exact trace-ceiling equality case {dimension}',sum(z*z for z in eigs)==A*A+2*(dimension-1)*c*A+dimension*(dimension-1)*c*c)
for n in [4,7,12]:
    for rep in range(10):
        rng=np.random.default_rng(20261015+n*101+rep);kcols=n-2
        J=np.linalg.qr(rng.normal(size=(n,kcols))+1j*rng.normal(size=(n,kcols)))[0]
        lam=np.r_[0,np.exp(rng.uniform(-3,3,n-1))];z=.3;eps=.25;rw=4
        e1=z*(1+eps+rw);e2=z*z*(eps+rw+eps*rw);e3=eps*rw*z**3
        q=(lam+z)*(lam+eps*z)*(lam+rw*z);B=J.conj().T@(q[:,None]*J)
        Fv=rng.normal(size=kcols)+1j*rng.normal(size=kcols);t=np.linalg.solve(B,Fv);u=J@t
        budget=np.vdot(Fv,Fv).real/(4*e3)
        terms=[np.sum(lam**3*abs(u)**2),e1*np.sum(lam**2*abs(u)**2),e2*np.sum(lam*abs(u)**2)]
        ck(f'complete compressed energy bounds {n}/{rep}',all(x<=budget*(1+1e-10) for x in terms) and abs(np.vdot(t,Fv).real-sum(terms)-e3*np.vdot(t,t).real)<1e-7)

path=[]
for j in [4,5,8,16,64,1024,10**8,10**16]:
    data=constants(j);row=report(data);path.append(row)
    ck(f'complete contracted original-path powers {j}',data['beta'].degree==45 and data['KK'].degree==42 and data['LL'].degree==45 and all(data['dh'][l].degree==42-7*l for l in range(5)))
    ck(f'all mixed ground orders {j}',all(z.degree==7*(m+2*r) for (m,r),z in data['E'].items()))
ck('full finite upper function convergence to its proved leading coefficient',abs(mp.mpf(path[-1]['ratio_to_leading'])-1)<mp.mpf('1e-10'))
for k,th,ep,rw in [('0.8','1','0.25','4'),('2','0.7','0.125','5'),('0.1','2','0.3','3')]:
    full=constants(4,k=k,theta=th,eps=ep,Rwin=rw)
    exact=leading_coefficient(k,th,ep,rw)
    ck('independent explicit leading coefficient '+str((k,th,ep,rw)),abs(full['beta'].leading/exact-1)<mp.mpf('1e-65'))
result=dict(checks=len(checks),all_passed=all(c['passed'] for c in checks),seconds=time.time()-start,details=checks,path=path,
    scope='Exact rational original SU2 product and contracted inverse-partition identities; exact two-link compressed fifth/fourth coefficients in a constructed positive-ground potential, not Wilson; full Hessian trace matrix bound and equality case; complete noncommuting compression energy fixtures;80-digit evaluation and exact rational growth exponents for the original parameter path. These checks do not evaluate the Wilson spectral measure.')
(O/'CONTRACTED_CUBIC_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=result['checks'],all_passed=result['all_passed'],seconds=result['seconds'],log10_j4=path[0]['log10_beta'],degree=path[0]['beta_degree'],last_ratio=path[-1]['ratio_to_leading'])))
