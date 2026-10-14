"""Exact-algebra diagnostics; none substitutes a sampled YM ground."""
from pathlib import Path
import itertools,json,math
import numpy as np
import sympy as sp
O=Path(__file__).resolve().parent;rows=[]
def ck(name,x,y,atol=3e-10):
    err=float(np.max(abs(np.asarray(x)-np.asarray(y))))
    assert err<=atol*max(1.,float(np.max(abs(y)))),(name,err)
    rows.append(dict(name=name,error=err))
# A finite central group tests all character, density and operator identities.
# Its discrete kinetic operator is explicitly a diagnostic, not the SU2 Casimir.
n=7;N=2**n;states=np.arange(N)
bits=np.array([[(k>>e)&1 for e in range(n)] for k in states])
chars=(-1.)**(bits@bits.T%2)
faces=[[0,1,2,3],[0,4,5,6]];masks=[sum(1<<e for e in p) for p in faces]
Tp=np.array([2*chars[m] for m in masks]);Dp=2-Tp;W=Dp.sum(axis=0);M=len(faces)
Delta=np.zeros((N,N));De=[]
for e in range(n):
    de=np.zeros((N,N));de[states,states^(1<<e)]=1;de-=np.eye(N);De.append(de);Delta+=de
project=lambda f:(chars@f/N)[:,None]*chars
center=(1<<1)|(1<<4)
for b in [.2,1.3,4.7]:
    kappa=1.6
    H=-kappa*Delta+np.diag(b*W);eig,U=np.linalg.eigh(H);E=eig[0];psi=U[:,0]
    if psi.sum()<0:psi=-psi
    # Probability counting measure: keep its explicit N factor.
    psi=math.sqrt(N)*psi;rho=psi**2
    assert psi.min()>0;ck('actual diagnostic ground mass',rho.mean(),1)
    pp=project(psi);rr=project(rho)
    J=sum((de@psi)**2/2 for de in De)
    for S in states:
        ck('full amplitude character equation',(-kappa*Delta+(2*b*M-E)*np.eye(N))@pp[S]-b*sum(Tp[p]*pp[S^masks[p]] for p in range(M)),np.zeros(N))
        ck('density equation with complete discrete product source',(-kappa/2*Delta+(2*b*M-E)*np.eye(N))@rr[S]-b*sum(Tp[p]*rr[S^masks[p]] for p in range(M)),-kappa*project(J)[S])
        ck('all amplitude convolution terms',rr[S],sum(pp[T]*pp[S^T] for T in states))
    # Raw complex weights, weighted product rule, mean and fluctuation.
    c=np.array([.3+.2j,-.2+.7j,1.1-.1j,.8+.6j,-1+.4j,.9-.3j,.2+.9j])
    bar=np.array([c[p].mean() for p in faces]);Dc=sum(c[e]*De[e] for e in range(n))
    Wc=bar@Dp;Hc=-kappa*Dc+np.diag(b*Wc)
    mc=np.vdot(psi,Hc@psi)/N;upsilon=-((Hc@psi)/psi-mc)/kappa
    Jc=sum(c[e]*(De[e]@psi)**2/2 for e in range(n))
    for S in states:
        left=(-kappa/2*Dc+(2*b*bar.sum()-mc)*np.eye(N))@rr[S]-b*sum(bar[p]*Tp[p]*rr[S^masks[p]] for p in range(M))
        ck('weighted full mean and fluctuation equation',left,-kappa*project(Jc+rho*upsilon)[S])
    for subset in [[],[0],[1],[0,1]]:
        raw=np.prod(Tp[subset],axis=0) if subset else np.ones(N)
        sigma=np.sign(raw);S=0
        for p in subset:S^=masks[p]
        err=np.mean(abs(rr[S]-sigma*rr[0]))
        bad=2*np.mean(rho*(raw<0))
        ck('exact L1 signed-density error',err,bad)
        d=sum(np.mean(rho*Dp[p]) for p in subset)
        assert err<=d+1e-10
        assert np.mean(abs(rr[S]))>=max(0,1-d/2)-1e-10
    for state in [0,3,57]:
        C=np.array([[rr[s^t,state] for t in states] for s in states])
        ck('positive orbit density eigenvalues',np.linalg.eigvalsh(C),np.sort(rho[states^state]))
    K=H-E*np.eye(N);minus=psi[states^center];C0=4*b*M
    ck('complete central spectral vector',(K-C0*np.eye(N))@minus,-2*b*(W*psi)[states^center])
    dall=np.mean(rho*W);m2=np.mean(rho*W**2);overlap=np.mean(psi*minus)
    ck('original first energy with cross term',np.vdot(minus,K@minus)/N,C0-2*b*dall)
    ck('original full second energy',np.vdot(K@minus,K@minus)/N,C0*C0-4*b*C0*dall+4*b*b*m2)
    assert overlap**2<=m2/(4*M*M)+1e-10
    coeff=U.T@minus/math.sqrt(N)
    for cutoff in [0,.2*C0,.6*C0]:
        mass=sum(abs(coeff[k])**2 for k in range(N) if eig[k]-E<=cutoff+1e-10)
        assert mass<=4*b*b*m2/(C0-cutoff)**2+1e-9
        rows.append(dict(name='spectral interval bound',error=0))
    weights=np.mean(pp*pp,axis=1)
    ck('central amplitude-sector overlap',sum(chars[S,center]*weights[S] for S in states),overlap)
# Radius-two continuous one-face product rule, with residual explicitly retained.
x,t,k,b,E=sp.symbols('x t k b E',real=True)
lap=lambda f:(1-x*x)*sp.diff(f,x,2)-3*x*sp.diff(f,x)
psi=sp.exp(t*x);rho=psi**2;V=b*(2-2*x)
res=(-k*lap(psi)+(V-E)*psi)/psi
J=t*t*(1-x*x)*rho
assert sp.expand((-k*lap(rho)/2+(V-E)*rho+k*J-res*rho)/rho)==0
rows.append(dict(name='original radius-two one-face density source and residual',error=0))
# Exact original inside-edge and ordered neighbor counts, including all boundaries.
for q in range(1,8):
    inc={}
    for z in itertools.product(range(q+1),repeat=3):
        for d,h in itertools.combinations(range(3),2):
            if z[d]>=q or z[h]>=q:continue
            zd=list(z);zh=list(z);zd[d]+=1;zh[h]+=1
            es=[(z,d),(tuple(zd),h),(tuple(zh),d),(z,h)]
            for e in es:inc[e]=inc.get(e,0)+1
    count=sum(m*(m-1) for m in inc.values())
    ck('complete inside ordered face-pair count',count,24*q+72*q*(q-1)+36*q*(q-1)**2)
    ck('exact count polynomial identity',count,12*q*(3*q*q-1))
# Original a_j and full cell averages of one fixed C2 compact test.
r=1/40
anti=lambda u:u-u**3+3*u**5/5-u**7/7
def avg(y,a):
    lo=np.clip((y-a/2)/r,-1,1);hi=np.clip((y+a/2)/r,-1,1)
    return r*(anti(hi)-anti(lo))/a
u=sp.symbols('u');f=(1-u*u)**3
I0=float(sp.integrate(f*f,(u,-1,1)))*r
I1=float(sp.integrate(sp.diff(f,u)**2,(u,-1,1)))/r
target=9/16*3*I1*I0*I0
limits=[]
for j in [2,4,8,16]:
    a=1/(100*j);L=j**4;maxz=math.ceil(r/a)+2
    assert maxz<L
    z=np.arange(-maxz,maxz+1)*a
    base=np.meshgrid(z,z,z,indexing='ij')
    total=0.
    for d,h in itertools.combinations(range(3),2):
        corners=[]
        for direction,shift in [(d,(0,0,0)),(h,tuple(int(i==d) for i in range(3))),(d,tuple(int(i==h) for i in range(3))),(h,(0,0,0))]:
            vals=np.ones_like(base[0])
            for axis in range(3):vals*=avg(base[axis]+a*(shift[axis]+.5*(axis==direction)),a)
            corners.append(vals)
        bar=sum(corners)/4
        total+=sum(np.sum((v-bar)**2) for v in corners)
    original=9/16*total
    limits.append(dict(j=j,a=a,original_Haar_form=float(original),a_times_form=float(a*original),target=target,error=float(abs(a*original-target))))
assert all(limits[i+1]['error']<limits[i]['error'] for i in range(len(limits)-1))
assert limits[-1]['error']<.006*target
rows.append(dict(name='original cell-average coefficient9/16 with all orientations',error=limits[-1]['error']))
out=dict(all_passed=True,checks=len(rows),scope='Finite central-group operators check complete character algebra with an explicitly different discrete kinetic operator. The radius-two differential test retains its non-ground residual. Cubic incidence and cell integrals use the original coordinates and spacing. No YM ground sample or numerical continuum claim.',cell_limit=limits,details=rows)
(O/'DENSITY_CHARACTER_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='details'}))
