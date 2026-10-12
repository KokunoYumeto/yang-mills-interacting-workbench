from pathlib import Path
import json,math
import numpy as np
O=Path(__file__).resolve().parent
rng=np.random.default_rng(13012026)
rows=[]
def check(name,err,scale=1,tol=3e-9):
    err=float(err);scale=max(1,float(scale))
    rows.append(dict(name=name,error=err,scale=scale,passed=bool(err<=tol*scale)))
    assert rows[-1]['passed'],rows[-1]
def close(name,x,y,tol=3e-9):check(name,np.linalg.norm(x-y),max(np.linalg.norm(x),np.linalg.norm(y)),tol)
def positive(name,x,tol=3e-9):check(name,max(0,-np.linalg.eigvalsh((x+x.conj().T)/2).min()),np.linalg.norm(x),tol)
def rand(n,m):return rng.normal(size=(n,m))+1j*rng.normal(size=(n,m))
for case in range(18):
    m=2+case%3;k=4+case%4;n=m+k
    F=np.diag(1+np.arange(m)/3)+.08*np.triu(rand(m,m),1);invF=np.linalg.inv(F)
    C=np.vstack([F,np.zeros((k,m))]);N=C.conj().T@C
    vals=np.geomspace(.04,5,k)
    if case%3==0:vals[0]=0
    R=.1*rand(k,m)
    if vals[0]==0:R[0]=0
    Ai=np.diag([1/x if x else 0 for x in vals]);A=np.diag(vals)
    h=rand(m,m);K=.04*(h.conj().T@h)
    Q=K+R.conj().T@Ai@R
    L=np.block([[invF.conj().T@Q@invF,invF.conj().T@R.conj().T],[R@invF,A]])
    v=rand(n,1)[:,0];vp=v[m:];b=C.conj().T@v
    Pi=C@np.linalg.solve(N,C.conj().T)
    Rfull=(np.eye(n)-Pi)@L@C
    close(f'{case}: raw complement',Rfull,np.vstack([np.zeros((m,m)),R]))
    close(f'{case}: full raw Q',C.conj().T@L@C,Q)
    close(f'{case}: KP13',C.conj().T@L@L@C,Q@np.linalg.solve(N,Q)+R.conj().T@R)
    positive(f'{case}: full nonnegative operator',L)
    for z in [.001,.04,.3,2,9]:
        Di=np.diag(1/(vals+z));Sigma=R.conj().T@Di@R
        S=Q+z*N-Sigma;d=b-R.conj().T@Di@vp;c=np.linalg.solve(S,d)
        y=Di@(vp-R@c);beta=C@c+np.r_[np.zeros(m),y]
        direct=np.linalg.solve(L+z*np.eye(n),v)
        close(f'{case},{z}: full solution',beta,direct,tol=2e-8)
        response=np.vdot(v,direct).real
        received=(np.vdot(d,c)+np.vdot(vp,Di@vp)).real
        close(f'{case},{z}: complete response',np.array([response]),np.array([received]),tol=2e-8)
        close(f'{case},{z}: complete norm',np.array([np.vdot(beta,beta).real]),np.array([(c.conj()@N@c+np.vdot(y,y)).real]))
        positive(f'{case},{z}: Schur lower',S-z*N)
        positive(f'{case},{z}: energy measure upper',Q-Sigma)
        Spr=N+R.conj().T@Di@Di@R
        dp=R.conj().T@Di@Di@vp
        derivative=2*np.vdot(dp,c).real-np.vdot(c,Spr@c).real-np.vdot(Di@vp,Di@vp).real
        close(f'{case},{z}: all source derivatives',np.array([derivative]),np.array([-np.vdot(beta,beta).real]),tol=2e-8)
        T=C-np.vstack([np.zeros((m,m)),Di@R])
        close(f'{case},{z}: lift norm',T.conj().T@T,Spr)
        close(f'{case},{z}: lift energy',T.conj().T@L@T,S-z*Spr)
        close(f'{case},{z}: lift overlap',T.conj().T@v,d)
        invenergy=Q-K
        weights=np.diag([z/(x+z)/x if x else 0 for x in vals])
        close(f'{case},{z}: static full formula',S,K+z*N+R.conj().T@weights@R)
        J=R.conj().T@Di@vp;e=np.vdot(vp,Di@vp).real
        close(f'{case},{z}: corrected source',d,b-J)
        for cut in [.02,.06,.5,2,6]:
            proj=np.diag((vals<=cut).astype(float));M=R.conj().T@proj@R
            positive(f'{case},{z},{cut}: sharp low coupling',cut*Q-M)
            cross=R.conj().T@proj@vp
            raw=rand(m,1)[:,0]
            rhs=np.vdot(raw,M@raw).real*np.vdot(vp,proj@vp).real
            check(f'{case},{z},{cut}: cross measure Cauchy',max(0,abs(np.vdot(raw,cross))**2-rhs),rhs)
    z1=.03;z2=.71;D1=np.diag(1/(vals+z1));D2=np.diag(1/(vals+z2))
    S1=Q+z1*N-R.conj().T@D1@R;S2=Q+z2*N-R.conj().T@D2@R
    close(f'{case}: joint Schur shifts',S2-S1,(z2-z1)*(N+R.conj().T@D2@D1@R))
    close(f'{case}: joint source shifts',(-R.conj().T@D2@vp)-(-R.conj().T@D1@vp),(z2-z1)*R.conj().T@D2@D1@vp)
# A specified scalar block model retains a, s, N and all endpoint contributions.
# It tests receiving formulas; it is not Yang--Mills vacuum data.
model=[]
kappa=1.7;tau=1.2;Kc=.4;weights=np.array([.3,.5,.7]);rho=1.6
for j in [1,4,16,64,256,1024]:
    a=1/(100*j);s=100*kappa*a;lam=s*np.array([a,rho,1/a])
    M=a*a*weights*lam;Q=a*a*(Kc+weights.sum());N=a**3*tau;R=np.sqrt(M)
    # One original-volume coefficient is chosen to test all powers exactly.
    b=-1.5*a**3
    for theta in [.2,1,3]:
        z=theta*s;Sigma=np.sum(M/(lam+z));S=Q+z*N-Sigma
        Spr=N+np.sum(M/(lam+z)**2)
        rat=lam/s
        Sscaled=Kc+np.sum(weights*theta/(rat+theta))+100*kappa*theta*a*a*tau
        close(f'path {j},{theta}: full S powers',np.array([S/a**2]),np.array([Sscaled]))
        derivative=np.sum(weights*rat/(rat+theta)**2)+100*kappa*a*a*tau
        close(f'path {j},{theta}: full norm powers',np.array([s*Spr/a**2]),np.array([derivative]))
        # N is the unchanged metric; the explicit block C=(sqrt(N),0,0,0).
        C=np.r_[np.sqrt(N),np.zeros(3)];L=np.zeros((4,4))
        L[0,0]=Q/N;L[0,1:]=R/np.sqrt(N);L[1:,0]=R/np.sqrt(N);L[1:,1:]=np.diag(lam)
        T=C-np.r_[0,R/(lam+z)]
        close(f'path {j},{theta}: exact lift energy',np.array([T@L@T]),np.array([S-z*Spr]))
        close(f'path {j},{theta}: original-volume matrix receiver',np.array([a**-3*b*b*S/a**5]),np.array([2.25*S/a**2]))
        normreceived=a**-3*b*b*Spr/a**4
        close(f'path {j},{theta}: original-volume norm receiver',np.array([normreceived]),np.array([9/(400*kappa)*derivative]))
        limit=Kc+weights[0]+weights[1]*theta/(rho+theta)
        derivlim=weights[1]*rho/(rho+theta)**2
        model.append(dict(j=j,a=a,theta=theta,schur=S/a**2,limit=limit,derivative=derivative,derivative_limit=derivlim,norm_receiver=normreceived,norm_limit=9/(400*kappa)*derivlim))
# Exact kernel relation with a nonzero infinity-only component.
K=np.diag([1,0,0,0]);V0=np.diag([0,1,0,0]);Vfinite=np.diag([0,0,2,0]);Vinf=np.diag([0,0,0,3])
Q=K+V0+Vfinite+Vinf
for theta in [.01,.4,1,10]:
    S=K+V0+theta/(2+theta)*Vfinite
    close(f'kernel {theta}: infinity cancellation',S@np.array([0,0,0,1.]),np.zeros(4))
    positive(f'kernel {theta}: effective order',Q-S)
    close(f'kernel {theta}: exact dimension',np.array([(np.linalg.eigvalsh(S)<1e-12).sum()]),np.array([1]))
# Original three-shift pointwise spectral inequality including zero.
eps=.17;rw=4.3;z=.7
for lam in [0,*np.geomspace(1e-6,1e4,80)]:
    h=lambda zz:zz*lam/(lam+zz)**2
    signed=h(z)-4*eps/(1+eps)**2*h(eps*z)-4*rw/(1+rw)**2*h(rw*z)
    upper=.25 if eps*z<=lam<=rw*z else 0
    check(f'window lambda {lam}: unchanged pointwise inequality',max(0,signed-upper))
out=dict(checks=len(rows),all_passed=all(x['passed'] for x in rows),scope='Finite complex positive block operators, complete source and lift identities, original-scale scalar diagnostics with endpoint escape, exact kernel and original three-shift inequality. No Yang–Mills vacuum samples.',checks_detail=rows,model=model)
(O/'CURRENT_SCHUR_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:out[k] for k in ['checks','all_passed','scope']}))
