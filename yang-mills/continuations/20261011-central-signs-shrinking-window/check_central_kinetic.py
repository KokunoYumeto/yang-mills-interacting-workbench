"""Diagnostics for exact density/kinetic algebra; no sampled YM ground."""
from pathlib import Path
import json
import mpmath as mp
import numpy as np
O=Path(__file__).resolve().parent
mp.mp.dps=45
checks=[]
def ck(name,x,y,tol=mp.mpf('1e-32')):
    err=abs(x-y)
    assert err<=tol*max(1,abs(y)),(name,str(err))
    checks.append(dict(name=name,error=str(err)))
# One-face radius-two differential operator, with an explicitly constructed
# smooth potential V=E+kappa Delta(psi)/psi, NOT the YM Wilson potential.
# Keep the exact Haar probability factor and full normalization integral.
weight=lambda x:2/mp.pi*mp.sqrt(1-x*x)
integ=lambda f:mp.quad(lambda x:weight(x)*f(x),[-1,0,1])
for t in map(mp.mpf,['0.2','0.7','1.3']):
    k=mp.mpf('1.7');E=mp.mpf(12)
    Z=integ(lambda x:mp.exp(2*t*x))
    ck('complete Haar integral',Z,mp.besseli(1,2*t)/t)
    psi=lambda x:mp.exp(t*x)/mp.sqrt(Z)
    A=lambda x:mp.sqrt(mp.cosh(2*t*x)/Z)
    h=[lambda x,sg=sg:mp.exp(sg*t*x)/mp.sqrt(2*mp.cosh(2*t*x)) for sg in [1,-1]]
    V=lambda x:E+k*(t*t*(1-x*x)-3*t*x)
    lap=lambda f,x:(1-x*x)*mp.diff(f,x,2)-3*x*mp.diff(f,x)
    gam=lambda f,g,x:(1-x*x)*mp.diff(f,x)*mp.diff(g,x)
    F=lambda x:sum(gam(v,v,x) for v in h)
    Vbar=lambda x:sum(h[i](x)**2*V(sg*x) for i,sg in enumerate([1,-1]))
    LA=lambda f,x:-k*(lap(f,x)+2*(1-x*x)*mp.diff(A,x)/A(x)*mp.diff(f,x))
    MM=lambda i,f,x:LA(f,x)+(V(([1,-1][i])*x)-Vbar(x)-k*F(x))*f(x)
    f=lambda x:x*x+mp.mpf('.2')*x**4
    c=mp.mpc('.4','.7')
    for x in map(mp.mpf,['-.93','-.54','-.11','.17','.61','.88']):
        ck('full conditional unit mass',sum(v(x)**2 for v in h),1)
        ck('constructed full ground equation',-k*lap(psi,x)+V(x)*psi(x),E*psi(x))
        for S in [0,1]:
            chars=[1,(-1)**S]
            r=lambda y:sum(chars[i]*h[i](y)**2 for i in range(2))
            left=sum(chars[i]*c*gam(lambda y,sg=sg:psi(sg*y),lambda y,sg=sg:psi(sg*y),x)/2 for i,sg in enumerate([1,-1]))
            right=c*(r(x)*gam(A,A,x)+mp.mpf('.5')*gam(lambda y:A(y)**2,r,x)+A(x)**2*sum(chars[i]*gam(h[i],h[i],x) for i in range(2)))
            ck('all character kinetic cross terms with complex coefficient',left,right)
        ck('averaged equation with full conditional kinetic',-k*lap(A,x)+(Vbar(x)+k*F(x))*A(x),E*A(x))
        for i,sg in enumerate([1,-1]):
            ck('complete conditional amplitude equation',MM(i,h[i],x),0)
            p=lambda y:h[i](y)**2
            ck('complete conditional probability equation',LA(p,x),2*(Vbar(x)+k*F(x)-V(sg*x))*p(x)-2*k*gam(h[i],h[i],x))
            vec=lambda y:h[i](y)*f(y)
            ck('original off-diagonal coupling',MM(i,vec,x),h[i](x)*LA(f,x)-2*k*gam(h[i],f,x))
            test=lambda y:(1+mp.mpc('.3','.2')*y+y*y)
            full=(-k*lap(lambda y:A(y)*test(y),x)+(V(sg*x)-E)*A(x)*test(x))/A(x)
            ck('full original operator conjugation including E',MM(i,test,x),full)
        off=[-2*k*gam(h[i],f,x) for i in range(2)]
        ck('conditional coupling orthogonal to ground channel',sum(h[i](x)*off[i] for i in range(2)),0)
        ck('full second energy square with coupling',sum(abs(MM(i,lambda y,i=i:h[i](y)*f(y),x))**2 for i in range(2)),abs(LA(f,x))**2+sum(abs(v)**2 for v in off))
    T=integ(lambda x:gam(psi,psi,x))
    TA=integ(lambda x:gam(A,A,x))
    IF=integ(lambda x:A(x)**2*F(x))
    assert IF>0
    ck('integrated kinetic decomposition',T,TA+IF)
    ck('original ground energy with all three terms',E,k*TA+k*IF+integ(lambda x:A(x)**2*Vbar(x)))
    ck('projected first physical energy',integ(lambda x:A(x)**2*f(x)*LA(f,x)),k*integ(lambda x:A(x)**2*gam(f,f,x)))
# Every finite character and all cross-covariances for raw complex coefficients.
rng=np.random.default_rng(10414)
n=8;bits=np.array([[(k>>e)&1 for e in range(3)] for k in range(n)])
chars=(-1.)**((bits@bits.T)%2)
for trial in range(50):
    raw=np.exp(rng.normal(size=n));p=raw/raw.sum();rr=chars@p
    assert np.max(abs(chars@rr/n-p))<1e-12
    masks=[3,5,6];traces=np.array([1.2,-.7,1.8]);a=.01
    coefficients=rng.normal(size=3)+1j*rng.normal(size=3)
    values=-a/2*np.sum(coefficients[:,None]*traces[:,None]*chars[masks],axis=0)
    mean=p@values
    direct=p@abs(values-mean)**2
    full=a*a/4*sum(np.conj(coefficients[i])*coefficients[j]*traces[i]*traces[j]*(rr[masks[i]^masks[j]]-rr[masks[i]]*rr[masks[j]]) for i in range(3) for j in range(3))
    assert abs(direct-full)<1e-16
    checks.append(dict(name='complete finite-character scalar covariance with original coefficients',error=float(abs(direct-full))))
out=dict(all_passed=True,checks=len(checks),scope='Continuous radius-two one-face diagnostic with its explicitly constructed potential V=E+kappa Delta(psi)/psi, retained Haar constant and integral. This potential is not the Wilson potential. Independent finite-character diagnostics retain all original covariance factors and complex coefficients. No numerical YM vacuum or gap conclusion.',details=checks)
(O/'CENTRAL_KINETIC_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='details'}))
