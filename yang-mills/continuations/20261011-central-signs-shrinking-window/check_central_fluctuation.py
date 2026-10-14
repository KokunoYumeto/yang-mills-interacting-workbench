from pathlib import Path
import json,mpmath as mp,numpy as np
O=Path(__file__).resolve().parent;mp.mp.dps=40;rows=[]
def ck(name,x,y,tol=mp.mpf('1e-28')):
    err=abs(x-y);assert err<tol*max(1,abs(y)),(name,str(err))
    rows.append(dict(name=name,error=str(err)))
weight=lambda x:2/mp.pi*mp.sqrt(1-x*x)
integ=lambda f:mp.quad(lambda x:weight(x)*f(x),[-1,0,1])
for t in map(mp.mpf,['.3','.8','1.4']):
    k=mp.mpf('1.7');E=12;mass=integ(lambda x:mp.exp(2*t*x))
    A=lambda x:mp.sqrt(mp.cosh(2*t*x)/mass)
    h=[lambda x,sg=sg:mp.exp(sg*t*x)/mp.sqrt(2*mp.cosh(2*t*x)) for sg in [1,-1]]
    V=lambda x:E+k*(t*t*(1-x*x)-3*t*x)
    gamma=lambda f,g,x:(1-x*x)*mp.diff(f,x)*mp.diff(g,x)
    lap=lambda f,x:(1-x*x)*mp.diff(f,x,2)-3*x*mp.diff(f,x)
    LA=lambda f,x:-k*(lap(f,x)+2*(1-x*x)*mp.diff(A,x)/A(x)*mp.diff(f,x))
    F=lambda x:sum(gamma(v,v,x) for v in h)
    Vbar=lambda x:sum(h[i](x)**2*V(sg*x) for i,sg in enumerate([1,-1]))
    MM=lambda i,f,x:LA(f,x)+(V([1,-1][i]*x)-Vbar(x)-k*F(x))*f(x)
    Z=lambda x:(mp.mpc('1.2','.4')*x+mp.mpc('.3','-.2')*x*x+mp.mpc('.1','.7')*x**3)
    zt=[lambda x,sg=sg:Z(sg*x) for sg in [1,-1]]
    bar=lambda x:sum(h[i](x)**2*zt[i](x) for i in range(2))
    y=[lambda x,i=i:h[i](x)*(zt[i](x)-bar(x)) for i in range(2)]
    mean_gradient=lambda x:sum(h[i](x)**2*mp.diff(zt[i],x) for i in range(2))
    defect=lambda x:mp.diff(bar,x)-mean_gradient(x)
    f=lambda x:mp.mpc('.4','.3')*(x*x+mp.mpf('.2')*x**4)
    for x in map(mp.mpf,['-.9','-.4','.15','.6']):
        moment=lambda v:h[0](v)**2-h[1](v)**2
        FS=gamma(h[0],h[0],x)-gamma(h[1],h[1],x)
        covV=sum(sg*h[i](x)**2*V(sg*x) for i,sg in enumerate([1,-1]))-moment(x)*Vbar(x)
        ck('full conditional moment source with constructed potential',LA(moment,x),-2*covV+2*k*(moment(x)*F(x)-FS))
        ck('complete conditional derivative defect',defect(x),2*sum(y[i](x)*mp.diff(h[i],x) for i in range(2)))
        # delta_A on a covector t(x)dx for the radial one-face measure:
        # -(1-x²)t' +3x t -2(1-x²)(A'/A)t .
        adj=-((1-x*x)*mp.diff(defect,x)-3*x*defect(x)+2*(1-x*x)*mp.diff(A,x)/A(x)*defect(x))
        actual=sum(h[i](x)*MM(i,y[i],x) for i in range(2))
        ck('complete original adjoint coupling',actual,-k*adj)
        bf=[-2*k*gamma(h[i],f,x) for i in range(2)]
        exact=sum(abs(y[i](x)-bf[i])**2 for i in range(2))
        expanded=sum(abs(v(x))**2 for v in y)+sum(abs(v)**2 for v in bf)+2*k*mp.re((1-x*x)*mp.conj(defect(x))*mp.diff(f,x))
        ck('full residual norm including signed cross term',exact,expanded)
    energy=integ(lambda x:A(x)**2*sum(mp.conj(y[i](x))*MM(i,y[i],x) for i in range(2)))
    decomposition=k*integ(lambda x:A(x)**2*(1-x*x)*(sum(h[i](x)**2*abs(mp.diff(zt[i],x)-mean_gradient(x))**2 for i in range(2))+abs(defect(x))**2))
    ck('full fluctuation energy positive decomposition',energy,decomposition)
    mixed=integ(lambda x:A(x)**2*sum(mp.conj(h[i](x)*f(x))*MM(i,y[i],x) for i in range(2)))
    ck('actual mixed first energy and full drift',mixed,-k*integ(lambda x:A(x)**2*(1-x*x)*mp.conj(mp.diff(f,x))*defect(x)))
rng=np.random.default_rng(1041408)
for j in [1,3,10,27]:
    a=1/(100*j);s=1.7/j
    for case in range(7):
        T=rng.normal(size=(8,8))+1j*rng.normal(size=(8,8));T[:,0]=0
        M=T.conj().T@T*(a if case%2 else 1/a);Ap=M[:3,:3];B=M[3:,:3]
        src=rng.normal(size=8)+1j*rng.normal(size=8);src[0]=0
        x=src[:3];y=src[3:];actual=[];upper=[];lower=[]
        for beta in [.2,1.,5.]:
            z=beta*s;f0=np.linalg.solve(Ap+z*np.eye(3),x);eta=y-B@f0
            full=np.linalg.solve(M+z*np.eye(8),src)
            w=float((z*np.vdot(full,M@full)).real)
            w0=float((z*np.vdot(f0,Ap@f0)).real)
            u=np.sqrt(max(0,w0));delta=.5*np.linalg.norm(eta)
            assert abs(np.sqrt(max(0,w))-u)<=delta+1e-9
            lower.append(max(0,u-delta)**2);upper.append((u+delta)**2);actual.append(w)
            rows.append(dict(name='original root response with complete residual',error=0))
        ee=4*.2/(1+.2)**2;rr=4*5/(1+5)**2
        value=actual[1]-ee*actual[0]-rr*actual[2]
        lo=lower[1]-ee*upper[0]-rr*upper[2];hi=upper[1]-ee*lower[0]-rr*lower[2]
        assert lo-1e-8<=value<=hi+1e-8
        rows.append(dict(name='all original three-shift coefficients and error signs',error=0))
n=8;bits=np.array([[(k>>e)&1 for e in range(3)] for k in range(n)])
chars=(-1.)**((bits@bits.T)%2)
for trial in range(40):
    logits=rng.normal(size=n);p=np.exp(logits);p/=p.sum()
    dp=rng.normal(size=(n,5));dp-=dp.mean(axis=0)
    rr=chars@p;dr=chars@dp
    C=np.array([[rr[S^T]-rr[S]*rr[T] for T in range(1,n)] for S in range(1,n)])
    inverse=(chars[1:]/p)@chars[1:].T/(n*n)
    err=np.max(abs(C@inverse-np.eye(n-1)));assert err<1e-10
    rows.append(dict(name='complete inverse character covariance with n^-2',error=float(err)))
    Xi=dp.T@(dp/p[:,None])/4
    full=dr[1:].T@inverse@dr[1:]/4
    err=np.max(abs(Xi-full));assert err<1e-8
    rows.append(dict(name='entire kinetic tensor in character coordinates',error=float(err)))
    for S in range(1,n):
        assert dr[S]@dr[S]<=4*(1-rr[S]**2)*np.trace(Xi)+1e-8
    rows.append(dict(name='retained conditional derivative bounds',error=0))
    centered=chars[1:].T-rr[1:]
    score=dp/p[:,None]
    score_from_chars=centered@inverse@dr[1:]
    err=np.max(abs(score-score_from_chars));assert err<1e-8
    rows.append(dict(name='entire logarithmic probability derivative',error=float(err)))
    zz=rng.normal(size=n)+1j*rng.normal(size=n)
    zhat=(chars@zz/n)[1:]
    df=rng.normal(size=5)+1j*rng.normal(size=5);kappa=1.7
    qq=dr[1:]@df;cc=zhat+kappa*inverse@qq
    residual=zz-p@zz+kappa*score@df
    err=np.max(abs(residual-centered@cc));assert err<1e-8
    rows.append(dict(name='complete residual in all character coordinates',error=float(err)))
    exact=np.sum(p*abs(residual)**2)
    gram=np.vdot(cc,C@cc).real
    expanded=(np.vdot(zhat,C@zhat)+2*kappa*np.vdot(zhat,qq).real+kappa*kappa*np.vdot(qq,inverse@qq)).real
    err=max(abs(exact-gram),abs(exact-expanded));assert err<1e-7
    rows.append(dict(name='complete residual Gram square and retained cross term',error=float(err)))
out=dict(all_passed=True,checks=len(rows),scope='Continuous radius-two diagnostics with an explicitly constructed potential V=E+kappa Delta(psi)/psi and complex observables; not the Wilson potential. Finite positive matrix diagnostics retain original a_j,s_j, vacuum zero direction and both full source components. Full finite-character inverse and kinetic tensors retain all probabilities and n^-2. No sampled YM vacuum or assigned continuum response.',details=rows)
(O/'CENTRAL_FLUCTUATION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='details'}))
