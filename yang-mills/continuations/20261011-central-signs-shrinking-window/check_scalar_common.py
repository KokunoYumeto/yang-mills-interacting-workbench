from pathlib import Path
import json,math
import numpy as np
import mpmath as mp
mp.mp.dps=80
O=Path(__file__).parent
rng=np.random.default_rng(2026101307)
rows=[]
def close(name,x,y,tol=4e-10):
    err=float(np.linalg.norm(np.asarray(x)-np.asarray(y))/max(1.,np.linalg.norm(x),np.linalg.norm(y)))
    assert err<tol,(name,err)
    rows.append(dict(name=name,relative_error=err))
def bound(name,x,y):
    excess=float(x-y)
    assert excess<=2e-9*max(1.,abs(x),abs(y)),(name,x,y)
    rows.append(dict(name=name,excess=excess))
def norm(x):return float(np.linalg.norm(x))
for kappa in [.6,1.,2.3]:
    for j in [2,3,7,19]:
        a=1/(100*j);s=100*kappa*a;b=1/(kappa*a*a);t=kappa*kappa*a**3/2
        lam=np.array([a*a/7,a*a,.02*s,.3*s,s,3*s,20*s,1.,4.,1/a,9/a,1/a**2])
        d=np.sqrt(lam/kappa)
        alpha=(rng.normal(size=12)+1j*rng.normal(size=12))/np.sqrt(12*(1+a*lam))
        ee=a*(rng.normal(size=12)+1j*rng.normal(size=12))/math.sqrt(12)
        eperp=a*(rng.normal(size=5)+1j*rng.normal(size=5))/math.sqrt(5)
        e_norm=math.sqrt(norm(ee)**2+norm(eperp)**2)
        v=(rng.normal(size=12)+1j*rng.normal(size=12))/math.sqrt(12)
        X=v/d
        B=-np.sqrt(lam)/(math.sqrt(kappa)*a*a)*alpha
        r=ee/d
        Q=t*B+r-X
        q=d*Q;G0=Q/t;Y=(B-2*G0)/(6*b)
        chi=a*np.vdot(alpha,lam*alpha).real
        key=f'k{kappa}-j{j}'
        close(key+'-full-gradient',v+q,-kappa*a/2*lam*alpha+ee)
        close(key+'-scalar-reconstruction',X+Q,t*B+r)
        close(key+'-scalar-score-norm',norm(t*B)**2,kappa**3*a*chi/4)
        close(key+'-inverse-score',norm(alpha)**2,kappa*a**4*np.vdot(B,B/lam).real)
        close(key+'-residual-energy',np.vdot(r,lam*r),kappa*norm(ee)**2)
        close(key+'-source-integration',np.vdot(B,X),-np.vdot(alpha,v)/a**2)
        close(key+'-mixed-covariance',kappa*kappa*a**5/2*np.vdot(B,G0),
              np.vdot(alpha,v)+kappa*a/2*np.vdot(alpha,lam*alpha)-np.vdot(alpha,ee))
        # The full density and squared-score terms can cancel many digits.
        # Preserve them at 80 digits; do not relax their comparison tolerance.
        mk=mp.mpf(str(kappa));ma=mp.mpf(1)/(100*j);mb=1/(mk*ma**2)
        mB=[mp.mpc(float(z.real),float(z.imag)) for z in B]
        mG=[mp.mpc(float(z.real),float(z.imag)) for z in G0]
        mY=[(x-2*y)/(6*mb) for x,y in zip(mB,mG)]
        def dot(x,y,ww=None):
            return mp.fsum(mp.conj(xx)*yy*(mp.mpf(float(ww[i])) if ww is not None else 1)
                           for i,(xx,yy) in enumerate(zip(x,y)))
        close(key+'-density-score-sum',complex(mk**2*ma**5/2*dot(mB,mG)),
              complex(3*mk*ma**3*dot(mY,mG)+mk**2*ma**5*dot(mG,mG)))
        bound(key+'-variance-floor',kappa*a*abs(np.vdot(alpha,v))**2/chi,norm(X)**2)
        for eps in [.05,.4,1.7]:
            u=eps*s;mask=lam>=u
            db=kappa**1.5/2*math.sqrt(a*chi)+math.sqrt(kappa/u)*e_norm
            bound(key+f'-highpass-{eps}',norm((X+Q)[mask]),db)
            bound(key+f'-root-mass-{eps}',abs(norm(X[mask])-norm(Q[mask])),db)
            bound(key+f'-residual-highpass-{eps}',norm(r[mask])**2,kappa/u*e_norm**2)
            sub=mask & (np.arange(12)%2==0)
            bound(key+f'-arbitrary-subset-{eps}',norm((X+Q)[sub]),db)
            mask2=mask & (lam<=7*s)
            upper=kappa**1.5*a*math.sqrt(7*s)/2*norm(alpha)
            bound(key+f'-finite-upper-{eps}',norm((t*B)[mask2]),upper)
        weights=rng.random(12)
        block=np.array([X,B,r]).T
        gram=block.conj().T@(weights[:,None]*block)
        raw=rng.normal(size=3)+1j*rng.normal(size=3)
        close(key+'-full-three-by-three-positive',np.vdot(raw,gram@raw),
              np.vdot(block@raw,weights*(block@raw)))
        cc=np.array([-1.,t,1.])
        close(key+'-nine-covariance-products',np.vdot(Q,weights*Q),np.vdot(cc,gram@cc))
        close(key+'-four-density-products',complex(dot(mB,mB,weights)),
              complex(36*mb**2*dot(mY,mY,weights)+12*mb*dot(mY,mG,weights)
              +12*mb*dot(mG,mY,weights)+4*dot(mG,mG,weights)))
        theta=.8;eps=.2;Rwin=6.;betas=[theta,eps*theta,Rwin*theta]
        WX=[];WQ=[];rho=[]
        for beta in betas:
            z=beta*s;kernel=np.sqrt(z*lam)/(lam+z)
            wx=norm(kernel*X)**2;wq=norm(kernel*Q)**2
            rr=kappa**1.5*a*math.sqrt(z)/2*norm(alpha)+math.sqrt(kappa/z)*e_norm
            WX.append(wx);WQ.append(wq);rho.append(rr)
            close(key+f'-response-polar-{beta}',wx,kappa*z*norm(v/(lam+z))**2)
            bound(key+f'-response-vector-{beta}',norm(kernel*(X+Q)),rr)
            bound(key+f'-response-root-{beta}',abs(math.sqrt(wx)-math.sqrt(wq)),rr)
        Ae=4*eps/(1+eps)**2;Ar=4*Rwin/(1+Rwin)**2
        cx=WX[0]-Ae*WX[1]-Ar*WX[2]
        ws=np.sqrt(WQ);rr=np.array(rho)
        lower=max(0.,ws[0]-rr[0])**2-Ae*(ws[1]+rr[1])**2-Ar*(ws[2]+rr[2])**2
        upper=(ws[0]+rr[0])**2-Ae*max(0.,ws[1]-rr[1])**2-Ar*max(0.,ws[2]-rr[2])**2
        bound(key+'-signed-lower',lower,cx);bound(key+'-signed-upper',cx,upper)
result=dict(checks=len(rows),all_passed=True,scope='Specified finite complex spectral arrays with both endpoint scales, full raw factors, scalar projection and mixed covariances. Universal algebra diagnostics only; these arrays are not the actual Yang–Mills ground state.',results=rows)
(O/'SCALAR_COMMON_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=len(rows),all_passed=True)))
