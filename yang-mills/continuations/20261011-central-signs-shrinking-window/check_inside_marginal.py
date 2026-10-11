"""Algebra and compact positive-ground checks for IM; no original-state sampling."""
from pathlib import Path
import hashlib
import json
import numpy as np
import sympy as s

root=Path(__file__).resolve().parent
checks=[]

def exact(label,expr):
    value=s.simplify(expr)
    assert value==0,(label,value)
    checks.append({'label':label,'kind':'symbolic','error':0.0})

def close(label,left,right,tol=2e-10):
    error=float(np.max(np.abs(np.asarray(left)-np.asarray(right))))
    scale=max(1.0,float(np.max(np.abs(left))),float(np.max(np.abs(right))))
    assert error<=tol*scale,(label,error,scale)
    checks.append({'label':label,'kind':'compact-ground quadrature','error':error})

v,c,B,alpha,F=s.symbols('v c B alpha F',real=True)
cov=c-v
vara=v+B-2*c
exact('signed retained covariance',cov+vara-(B-c))
exact('complete energy variance',v+vara+2*cov-B)
k,Y,A1,gamma,e,m0,m1,m2=s.symbols('k Y A1 gamma e m0 m1 m2',positive=True)
J=6*A1-3*Y
lap_inverse=s.diff(Y**(-k),Y)*J+s.diff(Y**(-k),Y,2)*gamma
exact('inverse Laplacian',lap_inverse-(-6*k*A1*Y**(-k-1)+3*k*Y**(-k)+k*(k+1)*gamma*Y**(-k-2)))
delta=s.symbols('delta',nonnegative=True)
exact('inverse incidence coefficient',lap_inverse.subs(gamma,16*F*Y-delta)-(3*k*Y**(-k)-2*k*(3*A1-8*F*(k+1))*Y**(-k-1)-k*(k+1)*delta*Y**(-k-2)))
D,L=s.symbols('D L',nonnegative=True)
r=(s.sqrt(L)+s.sqrt(L+4*D))/2
exact('quadratic weighted receiver root',r*r-s.sqrt(L)*r-D)
M,C,W,Wx=s.symbols('M C W Wx',real=True)
exact('inside and crossing Laplacian',4*(s.Rational(3,2)*M-s.Rational(3,4)*W)+s.Rational(3,2)*C-s.Rational(3,4)*Wx-(6*M-3*W+s.Rational(3,2)*C-s.Rational(3,4)*Wx))

x,y,eps,kap,E=s.symbols('x y eps kap E',real=True)
gx=(1-x*x)/4
gy=(1-y*y)/4
V=E+kap*(-s.Rational(3,2)*eps*x*y+eps**2*(x*x+y*y-2*x*x*y*y)/4)
lapx=lambda f:gx*s.diff(f,x,2)-s.Rational(3,4)*x*s.diff(f,x)
Vx=s.lambdify((x,y,eps,kap,E),s.diff(V,x),'numpy')
lapV=s.lambdify((x,y,eps,kap,E),lapx(V),'numpy')
Vfun=s.lambdify((x,y,eps,kap,E),V,'numpy')
u=s.Function('u')(x)
zu=gx*s.diff(u,x)**2
su=lapx(u)+2*zu
uvars=s.symbols('u1 u2 u3 u4')
subjets={s.diff(u,x,i+1):uvars[i] for i in range(4)}
lap_s=s.lambdify((x,*uvars),lapx(su).subs(subjets),'numpy')
lap_veff=s.lambdify((x,*uvars),lapx(lapx(u)+zu).subs(subjets),'numpy')

summaries=[]
for n in [96,160]:
    nodes=np.cos(np.arange(1,n+1)*np.pi/(n+1))
    weights=2*np.sin(np.arange(1,n+1)*np.pi/(n+1))**2/(n+1)
    X=nodes[:,None]; YY=nodes[None,:]
    GX=(1-X*X)/4; GY=(1-YY*YY)/4
    for ep in [0.2,1.0,-2.0]:
        kapp=1.7; energy=12.0
        tilt=np.exp(2*ep*X*YY)
        den=tilt@weights
        total=weights@den
        conditional=tilt*weights[None,:]/den[:,None]
        px=weights*den/total
        prob=px[:,None]*conditional
        avg=lambda f:float(np.sum(prob*f))
        avx=lambda f:float(px@np.asarray(f).reshape(n))
        moments=[conditional@(nodes**i) for i in range(1,5)]
        m1v,m2v,m3v,m4v=moments
        u1=ep*m1v
        u2=2*ep**2*(m2v-m1v*m1v)
        u3=4*ep**3*(m3v-3*m2v*m1v+2*m1v**3)
        u4=8*ep**4*(m4v-4*m3v*m1v-3*m2v*m2v+12*m2v*m1v*m1v-6*m1v**4)
        gxx=(1-nodes*nodes)/4
        z=u1*u1*gxx
        sm=gxx*u2-0.75*nodes*u1+2*z
        Z=ep*ep*YY*YY*GX
        SS=-0.75*ep*X*YY+2*Z
        Hq2=3*ep*ep*X*X*YY*YY/16
        Hmix2=ep*ep*GX*GY
        Hgg=-ep*X*YY*Z/4
        lamparallel=u2*gxx-nodes*u1/4
        lamtrans=-nodes*u1/4
        Hm2=lamparallel**2+2*lamtrans**2
        Hmgg=lamparallel*z
        cv=(conditional*(SS-sm[:,None])**2).sum(axis=1)
        lowerK=abs(ep)/2
        key=f'n={n},eps={ep}'
        close('conditional score '+key,(conditional*SS).sum(axis=1),sm)
        close('zero marginal score '+key,avx(sm),0.0)
        close('full partial Bochner '+key,avg(SS*SS),avg(Hq2+0.5*Z-2*Hgg))
        close('marginal Bochner '+key,avx(sm*sm),avx(Hm2+0.5*z-2*Hmgg))
        close('original Hessian contraction '+key,avg(Hq2+Hmix2+0.5*Z),avg(lapV(X,YY,ep,kapp,energy))/(2*kapp))
        close('positive remainder equality '+key,avx(sm*sm)+avg(Hmix2)+2*avg(Hgg+lowerK*Z)+avx(cv),avg(lapV(X,YY,ep,kapp,energy))/(2*kapp)+2*lowerK*avg(Z))
        assert np.min(cv)>-1e-13
        close('marginal effective-potential derivative '+key,avx(lap_veff(nodes,u1,u2,u3,u4)),2*avx(Hm2)+avx(z))
        close('marginal score derivative '+key,avx(lap_s(nodes,u1,u2,u3,u4)),2*avx(sm*sm))
        # Positive smooth weights test the full weighted identity without a singular endpoint.
        Yval=2.4-2*X
        for exponent in [0.5,1.0,2.0,3.0]:
            phi=Yval**(-exponent)
            phi_x=2*exponent*Yval**(-exponent-1)
            lhs=avg(phi*(SS*SS+Hmix2+2*Hgg+2*lowerK*Z))
            rhs=avg(phi*lapV(X,YY,ep,kapp,energy)+phi_x*Vx(X,YY,ep,kapp,energy)*GX)/(2*kapp)+2*lowerK*avg(phi*Z)-avg(SS*phi_x*ep*YY*GX)
            close('weighted complete Bochner '+key+f',p={exponent}',lhs,rhs,tol=2e-9)
        # The actual conditional-vector kinetic decomposition is pointwise in x.
        T=ep**2*(m2v-m1v*m1v)*gxx
        close('conditional kinetic split '+key,z+T,(conditional*Z).sum(axis=1))
        summaries.append({'nodes_per_factor':n,'epsilon':ep,'marginal_score_second_moment':avx(sm*sm),'full_score_second_moment':avg(SS*SS),'conditional_score_variance':avx(cv)})

# The exact sign counterexample IM41-IM42, with its own complete potential.
n=160
nodes=np.cos(np.arange(1,n+1)*np.pi/(n+1)); weights=2*np.sin(np.arange(1,n+1)*np.pi/(n+1))**2/(n+1)
X=nodes[:,None]; YY=nodes[None,:]; GX=(1-X*X)/4; GY=(1-YY*YY)/4
tilt=np.exp(2*X*YY); den=tilt@weights; total=weights@den
conditional=tilt*weights[None,:]/den[:,None]; px=weights*den/total
mean_y=conditional@nodes; second_y=conditional@(nodes*nodes)
u1=mean_y; u2=2*(second_y-mean_y*mean_y); gxv=(1-nodes*nodes)/4
z=u1*u1*gxv; T=(second_y-mean_y*mean_y)*gxv
sm=gxv*u2-0.75*nodes*u1+2*z
Yv=2-2*nodes
cross=Vfun(X,YY,1.0,1.0,6.0)-(2-2*X)
RQ=(conditional*(X*X*GY+cross)).sum(axis=1)
A=6+sm-Yv
close('counterexample exact marginal equation',-(gxv*u2-0.75*nodes*u1+z)+Yv+RQ+T,6.0)
close('counterexample retained energy',A,(conditional*(YY*YY*GX)).sum(axis=1)+RQ)
close('counterexample mean Y',float(px@Yv),2.0)
variance=float(px@(Yv-2)**2)
covariance=float(px@((Yv-2)*(A-float(px@A))))
close('counterexample negative covariance',covariance,-variance)
assert float(np.min(cross))>=0.5-1e-12 and float(np.min(A))>0

result={'status':'passed','check_count':len(checks),'checks':checks,'compact_test_families':summaries,
        'counterexample':{'variance_Y':variance,'covariance_Y_A':covariance,'minimum_sampled_crossing_potential':float(np.min(cross)),'minimum_sampled_retained_energy':float(np.min(A))},
        'scope':'Symbolic algebra and actual compact positive-ground differential identities; not sampling the original Wilson state.'}
(root/'INSIDE_MARGINAL_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','check_count':len(checks),'largest_numerical_error':max(c['error'] for c in checks),'covariance_counterexample':covariance}))
