"""Diagnostics for BD1–BD19. Manufactured curved states and face derivatives are not original ground-state samples."""
from pathlib import Path
import json,math
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent; rows=[]
def check(name,error,tol=3e-9):
    error=float(error);assert abs(error)<=tol,(name,error,tol)
    rows.append(dict(name=name,error=error,tolerance=tol,passed=True))
x,y,aa,bb,cc,kap=sp.symbols('x y aa bb cc kap',real=True)
tx=(1-x*x)/4;ty=(1-y*y)/4;wx=aa+cc*y;wy=bb+cc*x
def dx(f):return tx*sp.diff(f,x,2)-3*x*sp.diff(f,x)/4
def dy(f):return ty*sp.diff(f,y,2)-3*y*sp.diff(f,y)/4
Kx=-3*x*wx/4+tx*wx**2;Ky=-3*y*wy/4+ty*wy**2
V=5+kap*(Kx+Ky);Vx=kap*(-3*aa*x/4+tx*aa**2);Vy=kap*(-3*bb*y/4+ty*bb**2)
al=sp.diff(V-Vx-Vy-5,x);ca=sp.diff(kap*Kx-Vx,x);u=al-ca;v=kap*sp.diff(Kx,y)
Av=sp.diff(u,y);Bv=sp.diff(v,x);Cv=sp.diff(al,y)
J=-(tx*sp.diff(u,x)-3*x*u/4+2*tx*wx*u)
S=-3*x*wx/4+2*tx*wx**2
fullforce=-kap*(dy(S)+2*ty*wy*sp.diff(S,y))
for name,expr in [('A+B=C',Av+Bv-Cv),('two weighted divergences',J+ty*sp.diff(v,y)-3*y*v/4+2*ty*wy*v),('full force',fullforce-J+2*tx*wx*u+2*kap*tx*ty*cc**2)]:
    assert sp.expand(expr)==0,name
    check('symbolic '+name,0)
exprs=[al,ca,u,v,Av,Bv,Cv,J,fullforce,sp.diff(u,x),sp.diff(v,y)]
fn=sp.lambdify((x,y,aa,bb,cc,kap),exprs,'numpy')
n=100;angles=np.arange(1,n+1)*np.pi/(n+1)
nodes=np.cos(angles);weights=2/(n+1)*np.sin(angles)**2
xx=nodes[:,None];yy=nodes[None,:];base=weights[:,None]*weights[None,:]
txx=(1-xx**2)/4;tyy=(1-yy**2)/4
for i,(a,b,c,k) in enumerate([(a,b,c,k) for a,b,c in [(.2,.3,.07),(-.15,.21,-.04),(.33,-.2,.13),(.08,.04,.19),(-.2,-.17,.05),(.37,.1,-.11)] for k in [.7,1,1.7]]):
    rho=np.exp(2*(a*xx+b*yy+c*xx*yy));Z=np.sum(base*rho);mu=base*rho/Z
    avg=lambda f:np.sum(mu*f)
    alpha,cp,uu,vv,A,B,C,JJ,Fall,ux,vy=[np.asarray(t)+np.zeros_like(mu) for t in fn(xx,yy,a,b,c,k)]
    ww=a+c*yy;wyv=b+c*xx;T=txx*ww*uu
    Huv=txx*tyy*c*uu*vv
    check(f'curved{i}: mixed divergence identity',avg(JJ**2)-avg(txx*tyy*A*B)+2*avg(Huv))
    check(f'curved{i}: Hessian integration',avg(Huv)+avg(txx*tyy*A*vv*ww)-avg(T*JJ))
    check(f'curved{i}: complete square',avg((JJ+T)**2)+avg(txx*tyy*(A-C/2-vv*ww)**2)-avg(T**2)-avg(txx*tyy*(C/2+vv*ww)**2))
    inside_gradient=txx**2*ux**2-xx/2*txx*ux*uu+3*xx**2*uu**2/16
    inside_hessian=-xx*ww/4*txx*uu**2
    outside_gradient=tyy**2*vy**2-yy/2*tyy*vy*vv+3*yy**2*vv**2/16
    outside_hessian=-yy*wyv/4*tyy*vv**2
    check(f'curved{i}: partial inside Bochner Ricci one-half',avg(JJ**2-inside_gradient-txx*uu**2/2+2*inside_hessian))
    check(f'curved{i}: partial outside Bochner Ricci one-half',avg(JJ**2-outside_gradient-tyy*vv**2/2+2*outside_hessian))
    Amax=(abs(a)+abs(c))**2/4
    bound=2*math.sqrt(Amax*avg(txx*alpha**2))+.5*math.sqrt(avg(txx*tyy*C*C))
    check(f'curved{i}: divergence bound positive-part defect',max(0,math.sqrt(avg(JJ**2))-bound))
    ey=np.sum(mu*yy,axis=1)/np.sum(mu,axis=1)
    gb=a+c*ey[:,None];xi=c*(yy-ey[:,None])
    qg=2*txx*gb*xi;dqg=2*txx*gb*c
    F0=-2*txx*gb*uu;F1=JJ-2*txx*xi*uu-2*k*txx*tyy*c*c
    computedF0=-k*(-3*yy*dqg/4+2*tyy*wyv*dqg)
    check(f'curved{i}: marginal forcing',np.max(np.abs(F0-computedF0)))
    check(f'curved{i}: marginal first moment',avg(qg*F0)-k*avg(tyy*dqg*dqg))
    check(f'curved{i}: both force means',max(abs(avg(F0)),abs(avg(F1))))
    check(f'curved{i}: full joint force retained',np.max(np.abs(Fall-F0-F1)))
    m2=avg(F0**2)
    check(f'curved{i}: marginal second moment bound',max(0,m2-4*Amax*avg(txx*uu**2)))
    for th in [-1.3,-.4,0,.5,1,1.8]:
        check(f'curved{i}: full moment cross terms theta={th}',avg((F0+th*F1)**2)-m2-2*th*avg(F0*F1)-th*th*avg(F1**2))
    # Complete Gram and scalar optimization for a positive comparison inverse;
    # this checks the square without representing a measured Yang–Mills inverse.
    qd=(Sfn:=sp.lambdify((x,y,aa,cc),S,'numpy'))(xx,yy,a,c)
    qd=qd-np.sum(mu*qd,axis=1)[:,None]/np.sum(mu,axis=1)[:,None]-qg
    multiplier=.2/(.2+.3+xx**2+yy**2)
    Igg=avg(multiplier*qg*qg);Igd=avg(multiplier*qg*qd);Idd=avg(multiplier*qd*qd)
    Nd=avg(txx*xi**2);Ng=avg(txx*gb**2);z=.2;d=z*Nd+k*Idd
    optimum=-k*Igd/d;E0=.5+z*Ng+k*Igg
    for th in [-1,0,.7,1,optimum]:
        E=.5+z*(Ng+th*th*Nd)+k*(Igg+2*th*Igd+th*th*Idd)
        check(f'curved{i}: full scalar optimization theta={th}',E-E0+(k*Igd)**2/d-d*(th-optimum)**2)
rng=np.random.default_rng(20261011)
sigma=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex)]
generators=[-.5j*s for s in sigma]
def su2():
    q=rng.normal(size=4);q/=np.linalg.norm(q)
    return q[0]*np.eye(2)-1j*sum(q[i+1]*sigma[i] for i in range(3))
def prod(arr):
    out=np.eye(2,dtype=complex)
    for m in arr:out=out@m
    return out
for i in range(25):
    us=[su2() for _ in range(4)]
    factors=[us[0],us[1],us[2].conj().T,us[3].conj().T]
    tr=np.trace(prod(factors)).real;D=2-tr
    for e in range(4):
        for r in range(e+1,4):
            hs=[]
            for gen in generators:
                for ge2 in generators:
                    fs=list(factors)
                    fs[e]=gen@us[e] if e<2 else -us[e].conj().T@gen
                    fs[r]=ge2@us[r] if r<2 else -us[r].conj().T@ge2
                    hs.append(-np.trace(prod(fs)).real)
            check(f'face{i}: ordered distinct pair {e},{r}',sum(t*t for t in hs)-(.5+tr*tr/16))
    check(f'face{i}: full scalar and deficit terms',3*(.5+tr*tr/16)-(9/4-3*D/4+3*D*D/16))
Cheat=2+2*math.sqrt(4+2*math.pi)
def bounds(j,kind):
    a=1/(100*j);R=1.;k=1.;ell=math.log(math.e+R/a)
    K=max(1,math.floor(math.sqrt(R/a) if kind=='sqrt' else R/(a*ell)))
    q=math.ceil(R/a)+3;n=q+2*K
    N=3*n*(n+1)**2;M=3*n*n*(n+1);cross=12*n*(n+1)
    Lam=min(2*M,3*k*a*math.sqrt(N*M))+2*cross
    A=N*min(8/(k*k*a*a),Cheat/(k*a))**2
    J=(2*math.sqrt(2*A*Lam/K)+.75*math.sqrt(cross))**2
    m2=8*A*Lam/(k*k*a**4*K)
    return a,K,Lam,J,m2
for kind in ['sqrt','log']:
    a,K,lam,J,m2=bounds(10**12,kind);constant=24*Cheat**2*33
    check(kind+': divergence upper coefficient',a**7*K*J/constant-1,.5 if kind=='log' else 1e-5)
    check(kind+': marginal second moment upper coefficient',a**11*K*m2/constant-1,.5 if kind=='log' else 1e-5)
fig,ax=plt.subplots(figsize=(13,7));ax.set_xlim(0,13);ax.set_ylim(0,7);ax.axis('off')
def box(x,y,w,h,t,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',facecolor=color,edgecolor='#50687e'))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=11)
def arrow(a,b):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='->',mutation_scale=16,color='#33465c'))
ax.text(6.5,6.55,'Boundary divergence and the original joint trial family',ha='center',fontsize=17,weight='bold')
box(.4,4.3,3.1,1.45,r'$\zeta=u-v,\quad\delta_\mu\zeta=0$'+'\n'+r'$A+B=C,\quad J=\delta_Q u$', '#e5eef6')
box(4.2,4.3,4.2,1.45,r'$\|J+T\|^2+\|A-C/2-W\|^2$'+'\n'+r'$=\|T\|^2+\|C/2+W\|^2$', '#e6f2ed')
box(9.1,4.3,3.4,1.45,r'$\|J\|\leq2\sqrt{\mathcal{A} B_Q}$'+'\n'+r'$+\ \|C\|/2$'+'\nBD3–BD12', '#fff2da')
arrow((3.65,5),(4.05,5));arrow((8.55,5),(8.95,5))
box(.5,1.65,4.9,1.75,r'$\eta_\theta=a^2(\bar g+\theta\xi)$'+'\n'+r'$\mathscr{L}_{\rm out}q_\theta=\mathscr{F}_0+\theta\mathscr{F}_1$'+'\nComplete original scalar line; BD16–BD19', '#e5eef6')
box(6.25,1.65,6.05,1.75,r'$\mathscr{F}_0=-2b\,\bar g\cdot u$'+'\n'+r'$\mathscr{F}_1=bJ-2b\,\xi\cdot u-2\kappa X$'+'\n'+r'$m_2(\theta)=\|\mathscr{F}_0+\theta\mathscr{F}_1\|^2$', '#e6f2ed')
arrow((5.55,2.55),(6.1,2.55))
ax.text(6.5,.55,'All norms use the original ground-state measure. The marginal block has a proved second-moment bound.\nThe full-gradient direction retains the fluctuation of X and the complete signed cross term.',ha='center',fontsize=10)
fig.savefig(O/'BOUNDARY_DIVERGENCE_MAP.png',dpi=170,bbox_inches='tight');fig.savefig(O/'BOUNDARY_DIVERGENCE_MAP.svg',bbox_inches='tight');plt.close(fig)
js=np.unique(np.rint(np.logspace(1,9,180)).astype(np.int64))
fig,axs=plt.subplots(1,2,figsize=(12,5.3))
for kind,label,col in [('sqrt','Square-root collar','#316ca0'),('log','Logarithmic collar','#c37838')]:
    vals=[bounds(j,kind) for j in js]
    axs[0].loglog(js,[a**7*J for a,K,L,J,m in vals],label=label,color=col)
    axs[1].loglog(js,[a**11*m for a,K,L,J,m in vals],label=label,color=col)
for ax in axs:
    ax.set_xlabel(r'Original regulator $j$');ax.grid(alpha=.2);ax.legend(fontsize=9)
axs[0].set_ylabel(r'Upper function for $a_j^7\|J_j\|_{\mu_j}^2$')
axs[1].set_ylabel(r'Upper function for $a_j^{11}m_{2,j}^{\gamma}$')
fig.suptitle('Original boundary and marginal-moment estimates',weight='bold')
fig.text(.5,.02,r'BD10–BD15; $R=\kappa_*=1$, $a_j=(100j)^{-1}$. Every floor, ceiling and minimum branch retained.'+'\nThese are proved upper functions, not ground-state measurements or spectral gaps.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.09,1,.93))
fig.savefig(O/'BOUNDARY_DIVERGENCE_RATES.png',dpi=170,bbox_inches='tight');fig.savefig(O/'BOUNDARY_DIVERGENCE_RATES.svg',bbox_inches='tight');plt.close(fig)
(O/'BOUNDARY_DIVERGENCE_CHECKS.json').write_text(json.dumps(dict(description=__doc__,checks=len(rows),all_passed=True,results=rows),indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=len(rows),all_passed=True)))
