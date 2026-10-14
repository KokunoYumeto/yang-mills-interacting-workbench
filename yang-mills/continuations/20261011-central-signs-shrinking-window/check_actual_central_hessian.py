from pathlib import Path
import json,mpmath as mp,numpy as np
O=Path(__file__).resolve().parent;mp.mp.dps=40;rows=[]
def ck(name,a,b,tol=mp.mpf('1e-26')):
    if isinstance(a,mp.matrix) or isinstance(b,mp.matrix):err=mp.norm(a-b);scale=max(1,mp.norm(b))
    else:err=abs(a-b);scale=max(1,abs(b))
    assert err<=tol*scale,(name,str(err))
    rows.append(dict(name=name,error=str(err)))
c=mp.matrix([1,1,-1,-1]);HT=-c*c.T/2
sgn=[(-1)**k.bit_count() for k in range(16)];T=mp.mpf(2)
weight=lambda x:2/mp.pi*mp.sqrt(1-x*x)
for t in map(mp.mpf,['.2','.7','1.3']):
    mass=mp.quad(lambda x:weight(x)*mp.exp(4*t*x),[-1,0,1])
    muT=mp.quad(lambda x:weight(x)*2*x*mp.exp(4*t*x),[-1,0,1])/mass
    p=[lambda x,sg=sg:mp.exp(2*t*sg*x)/(16*mp.cosh(2*t*x)) for sg in sgn]
    h=[lambda x,i=i:mp.sqrt(p[i](x)) for i in range(16)]
    w=[lambda x,sg=sg:t*sg*x-mp.log(mass)/2 for sg in sgn]
    u=lambda x:(mp.log(mp.cosh(2*t*x))-mp.log(mass))/2
    rr=lambda x:mp.tanh(2*t*x)
    FF=lambda x:(4-x*x)*sum(mp.diff(v,x)**2 for v in h)
    FFchar=lambda x:(4-x*x)*sum(sg*mp.diff(h[i],x)**2 for i,sg in enumerate(sgn))
    KK=lambda fn:mp.diff(fn,T)*HT
    lap=lambda fn,x:(4-x*x)*mp.diff(fn,x,2)-3*x*mp.diff(fn,x)
    Ks=[KK(v) for v in w];pu=[v(T) for v in p]
    U=sum((pu[i]*Ks[i] for i in range(16)),mp.zeros(4))
    diff=[v-U for v in Ks];VK=sum((pu[i]*diff[i]**2 for i in range(16)),mp.zeros(4))
    VKchar=sum((sgn[i]*pu[i]*diff[i]**2 for i in range(16)),mp.zeros(4))
    ck('actual marginal Hessian mean in explicit state fixture',KK(u),U)
    for i in [0,1,5]:
        ck('complete conditional probability Hessian',KK(p[i]),2*pu[i]*diff[i])
        ck('complete conditional square-root Hessian',KK(h[i]),h[i](T)*diff[i])
    ck('complete conditional kinetic Hessian variance',KK(FF),2*VK)
    ck('complete signed kinetic Hessian variance',KK(FFchar),2*VKchar)
    for k in map(mp.mpf,['.8','1.7']):
        E=mp.mpf(12)
        vv=[lambda x,i=i:E+k*(lap(w[i],x)+(4-x*x)*mp.diff(w[i],x)**2) for i in range(16)]
        vb=lambda x:sum(p[i](x)*vv[i](x) for i in range(16))
        cov=lambda x:sum(sgn[i]*p[i](x)*vv[i](x) for i in range(16))-rr(x)*vb(x)
        for i in [0,1]:
            ck('complete original logarithmic equation Hessian',KK(lambda x,i=i:lap(w[i],x)),KK(vv[i])/k-2*Ks[i]**2)
        kvb=sum((pu[i]*KK(vv[i])+2*pu[i]*(vv[i](T)-vb(T))*diff[i] for i in range(16)),mp.zeros(4))
        ck('full marginal potential Hessian and covariance',KK(vb),kvb)
        ck('full marginal fourth derivative matrix',KK(lambda x:lap(u,x)),kvb/k+2*VK-2*U**2)
        kr=KK(rr)
        left=-k*KK(lambda x:lap(rr,x))-2*k*(U*kr+kr*U)
        right=-2*KK(cov)+4*k*(rr(T)*VK-VKchar)
        ck('full character fourth derivative with signed variance',left,right)
        variance=sum(pu[i]*(vv[i](T)-vb(T))**2 for i in range(16))
        curvature=3*sum(KK(FF)[i,i] for i in range(4))
        ck('full trace variance bound in one-cycle fixture',curvature,2*variance/(3*k*k))
        for j in [1,3,7]:
            a=mp.mpf(1)/(100*j);phi=mp.mpc('.4','.7');z=k/j
            xphi=lambda x:a*phi*(muT-x*rr(x))/2
            ck('entire original face-test source Hessian',KK(xphi),a*phi*rr(T)*(c*c.T)/4-a*phi*KK(rr))
            f=lambda x:mp.mpc('.3','-.2')*x*x
            LA=lambda fn,x:-k*(lap(fn,x)+2*(4-x*x)*mp.diff(u,x)*mp.diff(fn,x))
            source=lambda x:LA(f,x)+z*f(x)
            kf=KK(f)
            ck('both orders in full marginal resolvent Hessian',KK(lambda x:lap(f,x)),z*kf/k-2*(U*kf+kf*U)-KK(source)/k)
rng=np.random.default_rng(141441)
n=8;bits=np.array([[(k>>e)&1 for e in range(3)] for k in range(n)])
chars=(-1.)**((bits@bits.T)%2)
for trial in range(30):
    p0=np.exp(rng.normal(size=n));p0/=p0.sum()
    raw=rng.normal(size=(n,5,5));raw=(raw+raw.transpose(0,2,1))/2
    mean=np.einsum('t,tij->ij',p0,raw);dif=raw-mean
    var=np.einsum('t,tik,tkj->ij',p0,dif,dif)
    moments=chars@p0
    cov=np.array([[moments[S^T]-moments[S]*moments[T] for T in range(1,n)] for S in range(1,n)])
    inv=(chars[1:]/p0)@chars[1:].T/(n*n)
    kr=2*np.einsum('st,t,tij->sij',chars[1:],p0,dif)
    full=np.einsum('st,sik,tkj->ij',inv,kr,kr)/4
    err=float(np.max(abs(full-var)));assert err<1e-10
    rows.append(dict(name='noncommuting full character Hessian variance',error=err))
    restored=np.einsum('ts,su,uij->tij',chars[1:].T-moments[1:],inv,kr)/2
    err=float(np.max(abs(restored-dif)));assert err<1e-10
    rows.append(dict(name='all original centered matrix components reconstructed',error=err))
    tr=np.trace(var);bound=sum(p0[t]*np.trace(dif[t])**2 for t in range(n))/5
    assert tr+1e-10>=bound
    rows.append(dict(name='full dimensional matrix variance trace bound',error=0))
out=dict(all_passed=True,checks=len(rows),scope='Continuous original radius-two four-link loop formulas with explicitly constructed V=E+kappa Delta(psi)/psi, complete sixteen central signs and retained probability mass. Marginal resolvent identity uses a specified f with its computed source. Original a_j,s_j retained in those diagnostics; no Wilson vacuum or its resolvent is sampled. Finite matrix diagnostics retain noncommuting products and every covariance component.',details=rows)
(O/'ACTUAL_CENTRAL_HESSIAN_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='details'}))
