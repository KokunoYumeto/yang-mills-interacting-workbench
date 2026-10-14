from pathlib import Path
import json
import numpy as np
from scipy.linalg import eigh,eigh_tridiagonal
from scipy.special import roots_jacobi
O=Path(__file__).resolve().parent;rows=[]
def eq(name,a,b,tol=2e-8):
    err=float(np.max(np.abs(np.asarray(a)-np.asarray(b))));scale=1+float(np.max(np.abs(a)))+float(np.max(np.abs(b)))
    rows.append(dict(name=name,passed=bool(err<=tol*scale),error=err))
def positive(name,a):rows.append(dict(name=name,passed=bool(float(np.min(a))>0),minimum=float(np.min(a))))
def polys(T,nmax):
    P=np.empty((nmax+1,len(T)));dP=np.zeros_like(P);P[0]=1;P[1]=T;dP[1]=1
    for n in range(1,nmax):
        P[n+1]=T*P[n]-P[n-1];dP[n+1]=P[n]+T*dP[n]-dP[n-1]
    return P,dP
nodes,weights=roots_jacobi(240,.5,.5);T=2*nodes;weights*=2/np.pi;G=4-T*T;P,dP=polys(T,64)
eq('original trace Haar mass',weights.sum(),1.)
eq('original complete Chebyshev Gram',P[:49]@(weights[:,None]*P[:49].T),np.eye(49))
for b in [.3,3.,30.]:
    kappa=.8;a=1/np.sqrt(kappa*b)
    grounds=[]
    for size in [32,48]:
        n=np.arange(size);diagonal=kappa*n*(n+2)+2*b;off=-b*np.ones(size-1)
        energy,vec=eigh_tridiagonal(diagonal,off,select='i',select_range=(0,0));coeff=vec[:,0];coeff*=np.sign(coeff[0]);grounds.append((energy[0],coeff))
    E,c=grounds[-1];psi=c@P[:48];psip=c@dP[:48]
    finite_residual=(kappa*np.arange(48)*(np.arange(48)+2)+2*b-E)*c
    finite_residual[:-1]-=b*c[1:];finite_residual[1:]-=b*c[:-1]
    eq(f'b{b} full finite eigenvector residual',finite_residual,np.zeros(48))
    eq(f'b{b} retained scalar coupling',b,1/(kappa*a*a));eq(f'b{b} original ground norm',np.dot(weights,psi*psi),1.)
    eq(f'b{b} two Galerkin energies',E,grounds[0][0]);eq(f'b{b} full omitted Jacobi residual',abs(b*c[-1]),0.)
    positive(f'b{b} Galerkin ground positivity',psi);positive(f'b{b} Galerkin derivative positivity',psip)
    psim=psi[::-1];psimp=psip[::-1];A2=(psi*psi+psim*psim)/2;r=(psi*psi-psim*psim)/(psi*psi+psim*psim)
    C=4*psi**2*psim**2/(psi**2+psim**2)**2
    eq(f'b{b} retain full covariance comparison',C,1-r*r)
    rp=C*(psip/psi+psimp/psim);up=(psi*psip-psim*psimp)/(psi*psi+psim*psim)
    Hchar=np.array([[(-1.)**((s&t).bit_count()) for s in range(1,16)] for t in range(16)])
    for target in [-.3,.3]:
        idx=int(np.argmin(abs(T-target)));rr=r[idx];cc=C[idx]
        probabilities=np.where(Hchar[:,-1]>0,psi[idx]**2,psim[idx]**2)/(16*A2[idx])
        moments=Hchar.T@probabilities;full=Hchar.T@(probabilities[:,None]*Hchar)-np.outer(moments,moments)
        expected=np.eye(15);inverse=np.eye(15)/cc
        expected[-1,-1]=cc
        for S in range(1,15):expected[S-1,(S^15)-1]=rr;inverse[S-1,(S^15)-1]=-rr/cc
        eq(f'b{b} T{target} all fifteen covariance blocks',full,expected)
        eq(f'b{b} T{target} full inverse character comparison',inverse,Hchar.T@((1/probabilities)[:,None]*Hchar)/256)
        eq(f'b{b} T{target} all inverse products',full@inverse,np.eye(15))
        eq(f'b{b} T{target} physical cycle block',full[:,-1],np.r_[np.zeros(14),cc])
    positive(f'b{b} actual-form covariance floor',C);positive(f'b{b} conditional moment derivative',rp)
    meanT=np.dot(weights,psi*psi*T);x=a*(meanT-T*r)/2
    eq(f'b{b} full centered source',np.dot(weights*A2,x),0.)
    even=np.arange(0,26,2);odd=np.arange(1,26,2);Pe=P[even];dPe=dP[even];Po=P[odd];dPo=dP[odd]
    MA=Pe@((weights*A2)[:,None]*Pe.T);KA=kappa*dPe@((weights*A2*G)[:,None]*dPe.T);rhs=Pe@(weights*A2*x)
    MC=Po@((weights*A2*C)[:,None]*Po.T)
    DC=kappa*(dPo@((weights*A2*C*G)[:,None]*dPo.T)+Po@((weights*A2*G*rp*rp)[:,None]*Po.T))
    ev,vec=eigh(DC,MC);positive(f'b{b} retained conditional Galerkin spectrum',ev)
    source=-a*T/2;ys=vec.T@(Po@(weights*A2*C*source))
    for z in [.1,.7,2.]:
        fcoeff=np.linalg.solve(KA+z*MA,rhs);fp=fcoeff@dPe;beta=-kappa*G*rp*fp/C
        positive(f'b{b} z{z} marginal derivative direction',-fp[T>0]);positive(f'b{b} z{z} gradient-source direction',beta[T>0])
        bs=vec.T@(Po@(weights*A2*C*beta))
        for t in [0.,.2,1.]:
            mixed=np.dot(bs,np.exp(-t*ev)*ys);positive(f'b{b} z{z} t{t} mixed sign',-mixed)
        for sig in [.2,1.3]:positive(f'b{b} z{z} sigma{sig} full Galerkin inverse sign',-np.dot(bs,ys/(ev+sig)))
out=dict(all_passed=all(r['passed'] for r in rows),checks=len(rows),scope='Finite Galerkin diagnostics for the actual one-plaquette Wilson Jacobi matrix: full original kinetic eigenvalues kappa*n*(n+2), potential constant2b, offdiagonal-b, coupling b=1/(kappa*a^2), exact Haar measure and all weighted mass matrices retained.32/48-dimensional ground comparisons and the complete omitted Jacobi residual are reported. Conditional and marginal Galerkin functions remain approximations; no finite check replaces OPC1–OPC8 or proves a full-lattice statement.',results=rows)
(O/'ONE_PLAQUETTE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='results'}));print(json.dumps([r for r in rows if not r['passed']]));assert out['all_passed']
