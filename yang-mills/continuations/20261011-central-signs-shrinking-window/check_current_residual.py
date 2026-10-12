from pathlib import Path
import json,math
import numpy as np
from scipy.special import roots_jacobi
O=Path(__file__).resolve().parent
rng=np.random.default_rng(61012008);checks=[]
def eq(name,l,r):
    ok=abs(l-r)<=5e-10*max(1,abs(l),abs(r))
    checks.append(dict(name=name,passed=bool(ok),lhs=float(l),rhs=float(r)));assert ok,checks[-1]
def le(name,l,r):
    ok=l<=r+5e-10*max(1,abs(l),abs(r))
    checks.append(dict(name=name,passed=bool(ok),lhs=float(l),rhs=float(r)));assert ok,checks[-1]

# Fixed-regulator Hilbert-space diagnostics. Matrices are not Yang-Mills data.
for trial in range(24):
    kappa=rng.uniform(.2,3);z=10**rng.uniform(-2,1)
    Q=np.linalg.qr(rng.normal(size=(24,24)))[0]
    eigen=np.geomspace(.002,100,24);L=Q@np.diag(eigen)@Q.T
    D=L+z*np.eye(24);C=rng.normal(size=(24,7));A=D@C
    v=rng.normal(size=24);beta=np.linalg.solve(D,v)
    N=C.T@C;Z=A.T@A;k=A.T@v;coeff=np.linalg.solve(Z,k)
    residual=v-A@coeff
    eq(f'complete residual square {trial}',np.dot(residual,residual),np.dot(v,v)-np.dot(k,coeff))
    eq(f'full inverse residual identity {trial}',np.linalg.norm(beta-C@coeff-np.linalg.solve(D,residual)),0)
    le(f'full inverse residual bound {trial}',np.linalg.norm(beta-C@coeff),np.linalg.norm(residual)/z)
    W=z*kappa*np.dot(beta,beta);P=z*kappa*np.dot(coeff,N@coeff)
    Delta=math.sqrt(kappa/z)*np.linalg.norm(residual)
    le(f'uncut lower response {trial}',max(math.sqrt(P)-Delta,0)**2,W)
    le(f'uncut upper response {trial}',W,(math.sqrt(P)+Delta)**2)
    # Entry masks are independent column cutoffs on a finite probability space.
    cutoff=np.ones_like(A);cutoff[rng.random(A.shape)<.06]=0
    Ac=A*cutoff;err=np.linalg.norm(A-Ac);Zc=Ac.T@Ac;kc=Ac.T@v
    cc=np.linalg.solve(Zc,kc);rc=v-Ac@cc
    le(f'cutoff pairing error {trial}',np.linalg.norm(k-kc),err*np.linalg.norm(v))
    le(f'cutoff Gram error {trial}',np.linalg.norm(Z-Zc,2),(2*math.sqrt(np.trace(Z))+err)*err)
    eq(f'cutoff least-squares defect {trial}',np.dot(rc,rc),np.dot(v,v)-np.dot(kc,cc))
    le(f'complete cutoff residual {trial}',np.linalg.norm(v-A@cc),np.linalg.norm(rc)+err*np.linalg.norm(cc))
    Pc=z*kappa*np.dot(cc,N@cc);Dc=math.sqrt(kappa/z)*(np.linalg.norm(rc)+err*np.linalg.norm(cc))
    le(f'cutoff lower physical response {trial}',max(math.sqrt(Pc)-Dc,0)**2,W)
    le(f'cutoff upper physical response {trial}',W,(math.sqrt(Pc)+Dc)**2)
    # Original three shifts share L and v; no independent spectrum substituted.
    lo=.1;hi=20.;weights=[1.,-4*lo/(1+lo)**2,-4*hi/(1+hi)**2]
    truth=[];lower=[];upper=[]
    for zz in [z,lo*z,hi*z]:
        DD=L+zz*np.eye(24);AA=DD@C;ZZ=AA.T@AA;kk=AA.T@v;cc=np.linalg.solve(ZZ,kk)
        rr=v-AA@cc;PP=zz*kappa*np.dot(cc,N@cc);dd=math.sqrt(kappa/zz)*np.linalg.norm(rr)
        bv=np.linalg.solve(DD,v);truth.append(zz*kappa*np.dot(bv,bv))
        lower.append(max(math.sqrt(PP)-dd,0)**2);upper.append((math.sqrt(PP)+dd)**2)
    signed=float(np.dot(weights,truth))
    below=lower[0]+weights[1]*upper[1]+weights[2]*upper[2]
    above=upper[0]+weights[1]*lower[1]+weights[2]*lower[2]
    le(f'signed lower response uses upper subtractions {trial}',below,signed)
    le(f'signed upper response uses lower subtractions {trial}',signed,above)
    eta_coeff=np.sqrt(kappa/eigen)*(Q.T@v)
    rawmass=np.sum(eta_coeff[(eigen>=lo*z)&(eigen<=hi*z)]**2)
    le(f'full original-window lower receiver {trial}',4*max(below,0),rawmass)

# Coupled radius-two sphere densities test the full force/score source identity.
x,wq=roots_jacobi(192,.5,.5)
xx=x[:,None];yy=x[None,:];gx=(1-xx*xx)/4;gy=(1-yy*yy)/4
for t1,t2,eps in [(1.,2.,.2),(3.,4.,1.),(8.,6.,2.),(15.,9.,-3.)]:
    w=t1*xx+t2*yy+eps*xx*yy
    prob=wq[:,None]*wq[None,:]*np.exp(2*(w-w.max()));prob/=prob.sum()
    mu=lambda q:float(np.sum(prob*q))
    A=t1+eps*yy;B=t2+eps*xx;G1=A*A*gx;G2=B*B*gy
    G1x=-A*A*xx/2;G1y=2*eps*A*gx
    G2x=2*eps*B*gy;G2y=-B*B*yy/2
    Fx=-.75*(t1+2*eps*yy)-A*A*xx/2+2*eps*B*gy
    Fy=-.75*(t2+2*eps*xx)-B*B*yy/2+2*eps*A*gx
    for z in [.01,.2,3.]:
        for u1,u2 in [(1.,1.),(1.,-2.),(-.3,.8)]:
            lap=-.75*(u1*xx+u2*yy);J=A*u1*gx+B*u2*gy
            k1=mu((-Fx-G1x+z*A)*u1*gx-G1y*u2*gy)
            k2=mu(-G2x*u1*gx+(-Fy-G2y+z*B)*u2*gy)
            rhs1=-mu(Fx*u1*gx)+mu(G1*(lap+2*J))+z*mu(A*u1*gx)
            rhs2=-mu(Fy*u2*gy)+mu(G2*(lap+2*J))+z*mu(B*u2*gy)
            eq(f'full force-score source1 {t1} {z} {u1}',k1,rhs1)
            eq(f'full force-score source2 {t1} {z} {u1}',k2,rhs2)
            c1=(-Fx-G1x+z*A,-G1y)
            c2=(-G2x,-Fy-G2y+z*B)
            dot=lambda p,q:mu(p[0]*q[0]*gx+p[1]*q[1]*gy)
            ZZ=np.array([[dot(c1,c1),dot(c1,c2)],[dot(c2,c1),dot(c2,c2)]])
            kv=np.array([k1,k2]);cc=np.linalg.solve(ZZ,kv)
            rr=(u1-cc[0]*c1[0]-cc[1]*c2[0],u2-cc[0]*c1[1]-cc[1]*c2[1])
            eq(f'actual diagnostic residual source {t1} {z} {u1}',dot(rr,rr),mu(u1*u1*gx+u2*u2*gy)-np.dot(kv,cc))

# Exact finite tolerance choices in high precision prevent underflow.
import mpmath as mp
mp.mp.dps=70
for j in [1,10,1000]:
    a=1/(mp.mpf(100)*j);k=mp.mpf('1.3');z=100*k*a
    gamma=z*z*a**4*9*(8-a*mp.log(1/a))**2/(256*a*mp.log(1/a))
    uz=mp.mpf(13)/a**2;vnorm=mp.mpf('2.1');bt=mp.mpf(5)/a**mp.mpf('1.5')
    t=mp.mpf('.125');target=a**2
    estar=min(1,gamma/(2*(2*mp.sqrt(uz)+1)),target*gamma*mp.sqrt(z)/(2*mp.sqrt(k)*vnorm*(mp.sqrt(uz)+1)))
    cutoff=2/t*mp.log(max(1,bt/estar));er=bt*mp.exp(-t*cutoff/2)
    eta=(2*mp.sqrt(uz)+er)*er
    amp=2*mp.sqrt(k/z)*er*(mp.sqrt(uz)+er)*vnorm/gamma
    assert eta<=gamma/2*(1+mp.mpf('1e-60'))
    assert amp<=target*(1+mp.mpf('1e-60'))
    checks.extend([dict(name=f'finite inverse threshold {j}',passed=True),dict(name=f'finite amplitude tolerance {j}',passed=True)])
    improved=min(1,(1-1/mp.sqrt(2))*mp.sqrt(gamma),target*mp.sqrt(z*gamma/(2*k))/vnorm)
    rproj=2/t*mp.log(max(1,bt/improved));err=bt*mp.exp(-t*rproj/2)
    assert (mp.sqrt(gamma)-err)**2>=gamma/2*(1-mp.mpf('1e-60'))
    assert err*mp.sqrt(2*k/(z*gamma))*vnorm<=target*(1+mp.mpf('1e-60'))
    checks.extend([dict(name=f'projection singular-value threshold {j}',passed=True),dict(name=f'projection amplitude tolerance {j}',passed=True)])
out=dict(checks=len(checks),all_passed=True,scope='Finite positive operators verify full residual, two-sided response and signed window bounds; coupled radius-two sphere densities independently verify the complete force/score source identity and least-squares defect. High-precision constants check the explicit cutoff tolerance. These models are not original Yang-Mills spectral or vacuum values.',results=checks)
(O/'CURRENT_RESIDUAL_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=len(checks),all_passed=True,status='TCR1–TCR21 checked; original interacting residual unevaluated.')))
