"""Finite matrix diagnostics for the complete inverse, not YM state samples."""
from pathlib import Path
import numpy as np,json
O=Path(__file__).resolve().parent;rng=np.random.default_rng(1041424);rows=[]
def ck(name,x,y):
    err=float(np.max(abs(np.asarray(x)-np.asarray(y))))
    assert err<3e-8*max(1.,float(np.max(abs(y)))),(name,err)
    rows.append(dict(name=name,error=err))
for j in [1,2,4,9,17,30]:
    a=1/(100*j);kappa=1.7;s=kappa/j
    for trial in range(6):
        T=rng.normal(size=(9,9))+1j*rng.normal(size=(9,9))
        T[:,0]=0 # retain an exact vacuum zero direction
        M=T.conj().T@T*(a if trial%2 else 1/a)
        Ap=M[:4,:4];B=M[4:,:4];D=M[4:,4:]
        source=rng.normal(size=9)+1j*rng.normal(size=9);source[0]=0
        x=source[:4];y=source[4:]
        eig,U=np.linalg.eigh(M)
        ck('original vacuum annihilation',M[:,0],np.zeros(9))
        assert eig.min()>-1e-8
        ws=[];spectral=[]
        for beta in [.2,1.,5.]:
            z=beta*s
            R=np.linalg.inv(D+z*np.eye(5))
            S=Ap+z*np.eye(4)-B.conj().T@R@B
            ell=x-B.conj().T@R@y
            f=np.linalg.solve(S,ell);v=R@(y-B@f)
            full=np.linalg.solve(M+z*np.eye(9),source)
            ck('full two-component inverse',np.r_[f,v],full)
            G=np.vdot(y,R@y)+np.vdot(ell,f)
            ck('full quadratic inverse and mixed source',G,np.vdot(source,full))
            assert np.linalg.eigvalsh(S).min()>=z-1e-8
            W=z*G-z*z*(np.vdot(f,f)+np.vdot(v,v))
            direct=z*np.vdot(full,M@full)
            ck('original squared-resolvent response',W,direct)
            ck('full spectral response',direct,np.sum(abs(U.conj().T@source)**2*z*eig/(eig+z)**2))
            f0=np.linalg.solve(Ap+z*np.eye(4),x)
            eta=y-B@f0
            residual=np.r_[np.zeros(4),eta]
            ck('complete central-average residual',source-(M+z*np.eye(9))@np.r_[f0,np.zeros(5)],residual)
            gain=np.vdot(residual,np.linalg.solve(M+z*np.eye(9),residual))
            ck('retained original inverse gain',G-np.vdot(x,f0),gain)
            assert gain.real>=-1e-9
            # Complex-step is unsuitable for conjugate quadratics; use analytic
            # differentiated block equations and compare the full resolvent.
            Sd=np.eye(4)+B.conj().T@R@R@B
            elld=B.conj().T@R@R@y
            fd=np.linalg.solve(S,elld-Sd@f)
            vd=-R@R@(y-B@f)-R@B@fd
            ck('full reduced-form and source derivatives',np.r_[fd,vd],-np.linalg.solve(M+z*np.eye(9),full))
            Gd=-np.vdot(y,R@R@y)+2*np.real(np.vdot(elld,f))-np.vdot(f,Sd@f)
            ck('complete quadratic inverse derivative',Gd,-np.vdot(full,full))
            ws.append(W);spectral.append(direct)
        weights=np.array([-4*.2/(1+.2)**2,1.,-4*5/(1+5)**2])
        ck('all three original signs and shifts',weights@np.array(ws),weights@np.array(spectral))
out=dict(all_passed=True,checks=len(rows),scope='Complex positive finite block matrices, exact vacuum zero direction, nonzero coupling and both source components. Original a_j=(100j)^-1 and s_j=kappa/j used in fixtures. Both low and high energy scales retained. These matrices are algebra diagnostics, not Yang–Mills vacuum spectra.',details=rows)
(O/'CENTRAL_RESOLVENT_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='details'}))
