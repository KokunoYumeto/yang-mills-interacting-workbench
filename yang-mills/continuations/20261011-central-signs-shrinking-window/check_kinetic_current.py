"""KC diagnostics: manufactured curved states, finite positive operators and proved upper functions; no original quantum samples."""
from pathlib import Path
import json,math
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent;rows=[]
def check(name,error,tol=3e-9):
    error=float(error);assert abs(error)<=tol,(name,error,tol)
    rows.append(dict(name=name,error=error,tolerance=tol,passed=True))
x,y,aa,bb,cc,kap=sp.symbols('x y aa bb cc kap',real=True)
tx=(1-x*x)/4;ty=(1-y*y)/4;wx=aa+cc*y;wy=bb+cc*x
Kx=-3*x*wx/4+tx*wx**2;Ky=-3*y*wy/4+ty*wy**2
V=5+kap*(Kx+Ky);Vx=kap*(-3*aa*x/4+tx*aa**2);Vy=kap*(-3*bb*y/4+ty*bb**2)
alpha=sp.diff(V-Vx-Vy-5,x);cp=sp.diff(kap*Kx-Vx,x);u=alpha-cp;v=kap*sp.diff(Kx,y)
J=-(tx*sp.diff(u,x)-3*x*u/4+2*tx*wx*u)
Lk=-kap*(ty*sp.diff(Kx,y,2)-3*y*sp.diff(Kx,y)/4+2*ty*wy*sp.diff(Kx,y))
assert sp.expand(Lk-J)==0
check('symbolic full original-quotient forcing in curved comparison',0)
exprs=[Kx,sp.diff(Kx,x),sp.diff(Kx,y),cp,u,v,J]
fn=sp.lambdify((x,y,aa,bb,cc,kap),exprs,'numpy')
n=100;tgrid=np.arange(1,n+1)*np.pi/(n+1);nodes=np.cos(tgrid);weights=2/(n+1)*np.sin(tgrid)**2
xx=nodes[:,None];yy=nodes[None,:];base=weights[:,None]*weights[None,:]
txx=(1-xx**2)/4;tyy=(1-yy**2)/4
for i,(a,b,c,kappa) in enumerate([(a,b,c,k) for a,b,c in [(.2,.3,.07),(-.15,.21,-.04),(.33,-.2,.13),(.08,.04,.19),(-.2,-.17,.05),(.37,.1,-.11)] for k in [.7,1,1.7]]):
    density=np.exp(2*(a*xx+b*yy+c*xx*yy));Z=np.sum(base*density);mu=base*density/Z
    avg=lambda q:np.sum(mu*q)
    cond=lambda q:np.sum(mu*q,axis=1)[:,None]/np.sum(mu,axis=1)[:,None]
    K,Kd,Ky1,cp1,uu,vv,JJ=[np.asarray(q)+np.zeros_like(mu) for q in fn(xx,yy,a,b,c,kappa)]
    ey=cond(yy);vary=cond((yy-ey)**2);gb=a+c*ey;xi=c*(yy-ey)
    t=cond(txx*xi**2);kq=K-cond(K);rq=txx*xi**2-t;qg=2*txx*gb*xi
    Sq=K+txx*(a+c*yy)**2;qd=Sq-cond(Sq)-qg
    barK=2*txx*c*c*vary-3*xx*gb/4+txx*gb*gb
    check(f'curved{i}: complete quotient conditional mean',np.max(abs(cond(K)-barK+t)))
    check(f'curved{i}: qdelta equals kinetic plus score fluctuation',np.max(abs(qd-kq-rq)))
    check(f'curved{i}: all three conditional means',max(np.max(abs(cond(q))) for q in [kq,rq,qg]))
    rho=cond(kq*xi);kdx=Kd-cond(Kd)-2*rho;cp0=cp1-cond(cp1)
    check(f'curved{i}: exact inside derivative and conditional covariance',np.max(abs(kdx-cp0/kappa+2*rho)))
    m0k=avg(kq*kq);m1k=kappa*avg(tyy*Ky1**2)
    assert m0k>0
    check(f'curved{i}: kinetic first moment',m1k-avg(kq*JJ))
    check(f'curved{i}: original projection expression for first moment',m1k-avg(tyy*vv*vv)/kappa)
    fullenergy=kappa*avg(txx*kdx*kdx+tyy*Ky1*Ky1)
    check(f'curved{i}: complete physical energy',fullenergy-(avg(tyy*vv**2)+avg(txx*cp0**2))/kappa-4*kappa*avg(txx*rho*rho))
    check(f'curved{i}: inside-source cross form',kappa*avg(txx*(1+2*xx)*kdx)+2*kappa*avg(txx*(1+2*xx)*rho))
    rdy=2*txx*xi*c;rddy=2*txx*c*c
    Lr=-kappa*(tyy*rddy-3*yy*rdy/4+2*tyy*(b+c*xx)*rdy)
    check(f'curved{i}: full score-square forcing',np.max(abs(Lr+2*txx*xi*uu+2*kappa*txx*tyy*c*c)))
    check(f'curved{i}: retained fourth moment and mean square',avg(rq*rq)-avg((txx*xi*xi)**2)+avg(t*t))
    check(f'curved{i}: score-square first moment',avg(rq*Lr)-kappa*avg(tyy*rdy*rdy))
    # A positive multiplier checks the entire six-entry Gram algebra,
    # independently of an asserted quantum inverse.
    T=.2/(.2+.1+xx*xx+yy*yy);D=1-T
    for theta in [-1.3,0,.4,1,2.1]:
        w=qg+theta*rq;q=w+theta*kq
        exact=avg(T*w*w)+2*theta*avg(w*kq)+theta*theta*m0k-2*theta*avg(w*D*kq)-theta*theta*avg(kq*D*kq)
        check(f'curved{i}: complete six-entry inverse identity theta={theta}',avg(T*q*q)-exact)
rng=np.random.default_rng(20261011)
def lap(n):
    w=rng.uniform(.4,1.6,n-1);M=np.zeros((n,n))
    for j,t in enumerate(w):
        M[j,j]+=t;M[j+1,j+1]+=t;M[j,j+1]-=t;M[j+1,j]-=t
    return M
for i in range(35):
    ni=3+i%3;no=4+i%2;A=np.kron(lap(ni),np.eye(no));B=np.kron(np.eye(ni),lap(no))
    # Original comparison roles: nonnegative commuting sector energies;
    # crossing multiplication in [0,2M] with product-ground mean M.
    M=.3+.02*i;cv=rng.uniform(-1,1,ni*no);cv-=cv.mean();cv=M+.7*M*cv/max(abs(cv))
    H=A+B+np.diag(cv);es,vecs=np.linalg.eigh(H);eps=es[0];psi=vecs[:,0]
    if psi.sum()<0:psi=-psi
    assert min(psi)>0
    mu=psi*psi;cmu=mu@cv;ap=A@psi;bp=B@psi;aph=ap/psi
    m=mu.reshape(ni,no).sum(axis=1)
    aq=(mu*aph).reshape(ni,no).sum(axis=1)/m
    kq=aph-np.repeat(aq,no)
    var=mu@(kq*kq)
    remainders=[(M-eps)*(M+eps-2*cmu),mu@(cv*(2*M-cv)),bp@bp,2*(ap@bp),m@(aq*aq)]
    for j,t in enumerate(remainders):check(f'positive product{i}: remainder{j} nonnegative',max(0,-t))
    check(f'positive product{i}: exact full variance identity',var-M*M+sum(remainders))
    check(f'positive product{i}: full ground equation',np.linalg.norm((A+B)@psi-(eps-cv)*psi))
    check(f'positive product{i}: product crossing mean',np.mean(cv)-M)
    check(f'positive product{i}: energy comparison',max(0,cmu-eps,eps-M))
for i in range(40):
    p=4;q=7;dim=p+q
    Y=rng.normal(size=(dim+3,dim));Y[:,0]=0;L=Y.T@Y
    z=.01+.013*i;inside=L[:p,:p]+z*np.eye(p)
    kv=np.zeros(dim);kv[p:]=rng.normal(size=q);m0=kv@kv
    omega=(L@kv)[:p];d=kv@(L+z*np.eye(dim))@kv
    Aw=np.linalg.solve(inside,omega);delta=d-omega@Aw
    F=np.zeros(dim);F[1:p]=rng.normal(size=p-1);Af=np.linalg.solve(inside,F[:p]);e=omega@Af
    trial=np.zeros(dim);trial[:p]=Af+e/delta*Aw;trial-=e/delta*kv
    beta=np.linalg.solve(L+z*np.eye(dim),F);res=beta-trial
    check(f'physical scalar{i}: exact Green gain and residual',F@beta-F[:p]@Af-e*e/delta-res@(L+z*np.eye(dim))@res)
    check(f'physical scalar{i}: Schur lower remainder',max(0,z*(m0+Aw@Aw)-delta))
    check(f'physical scalar{i}: both optimizing equations',np.linalg.norm(((L+z*np.eye(dim))@trial-F)[:p])+abs(kv@((L+z*np.eye(dim))@trial-F)))
    check(f'physical scalar{i}: vacuum orthogonality',abs(trial[0]))
    check(f'physical scalar{i}: response sign',F@np.linalg.solve(L+z*np.eye(dim),L@F)-(F@F-z*(F@beta)))
for i in range(30):
    lam=10**rng.uniform(-8,4,17);q=rng.normal(size=(3,17));z=10**rng.uniform(-5,1);T=z/(lam+z);D=1-T
    m0=np.sum(q*q,axis=1);m1k=np.sum(lam*q[1]**2);Dkk=np.sum(D*q[1]**2)
    check(f'spectral{i}: kinetic defect inequality',max(0,Dkk-m1k/z))
    for f in [0,2]:
        Dfk=np.sum(D*q[f]*q[1])
        check(f'spectral{i}: complete cross defect inequality',max(0,Dfk*Dfk-m0[f]*m1k/z),1e-6)
Cheat=2+2*math.sqrt(4+2*math.pi)
def bounds(j,kind):
    a=1/(100*j);R=1.;k=1.;ell=math.log(math.e+R/a)
    K=max(1,math.floor(math.sqrt(R/a) if kind=='sqrt' else R/(a*ell)))
    n=math.ceil(R/a)+3+2*K;N=3*n*(n+1)**2;M=3*n*n*(n+1);C=12*n*(n+1)
    Lam=min(2*M,3*k*a*math.sqrt(N*M))+2*C
    A=N*min(8/(k*k*a*a),Cheat/(k*a))**2
    m0=4*C*C/(k**4*a**4)
    defect=Lam/(200*k**4*a**5*K)
    cross=math.sqrt(A*Lam*Lam/(50*k**6*a**7*K))
    return a,K,m0,defect,cross
for kind in ['sqrt','log']:
    a,K,m0,d,c=bounds(10**12,kind);tol=.5 if kind=='log' else 1e-5
    check(kind+': retained variance coefficient',a**8*m0/576-1,tol)
    check(kind+': original s=100 kappa a diagonal defect coefficient',a**7*K*d/(33/200)-1,tol)
    check(kind+': original-window cross defect coefficient',a**8*math.sqrt(K)*c/(Cheat*33*math.sqrt(3/50))-1,tol)
fig,ax=plt.subplots(figsize=(13,7));ax.set_xlim(0,13);ax.set_ylim(0,7);ax.axis('off')
def box(x,y,w,h,t,col):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',facecolor=col,edgecolor='#50687e'))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=11)
def arrow(a,b):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='->',mutation_scale=16,color='#33465c'))
ax.text(6.5,6.6,'The same original kinetic vector in both operators',ha='center',fontsize=17,weight='bold')
box(.4,4.2,3.5,1.6,r'$K_Q=\Delta_Q\psi/\psi$'+'\n'+r'$k_Q=K_Q-\mathbb{E}_xK_Q$'+'\nOriginal quotient and\nconditional mean retained', '#e5eef6')
box(4.65,4.2,3.65,1.6,r'$\mathscr{L}_{\rm out}k_Q=bJ$'+'\n'+r'$m_1^k=(b^2/\kappa)\|v\|^2$'+'\n'+r'$m_2^k=b^2\|J\|^2$', '#e6f2ed')
box(9.05,4.2,3.5,1.6,r'$\mathcal{T}_{s_j}=s_j(\mathscr{L}_{\rm out}+s_j)^{-1}$'+'\n'+r'$a_j^8(m_0^k-I_{kk})\to0$'+'\nComplete inverse column\nKC17–KC21', '#fff2da')
arrow((4.05,5),(4.5,5));arrow((8.45,5),(8.9,5))
box(.5,1.55,5.5,1.8,r'$d_Qk_Q=(b/\kappa)c_0-2\rho_Q$'+'\n'+r'$\rho_Q=\mathbb{E}_x(k_Q\xi)$'+'\nFull physical energy retains '+r'$4\kappa\|\rho_Q\|^2$', '#e5eef6')
box(6.9,1.55,5.5,1.8,r'$\omega_Q=-2\kappa\delta_m\rho_Q$'+'\nInside functions plus the same kinetic vector\nExact scalar Green gain '+r'$e_z^2/\Delta_z$'+'\nwith the full physical residual; KC25–KC28', '#e6f2ed')
arrow((2.2,4.05),(2.6,3.5));arrow((6.15,2.45),(6.75,2.45))
ax.text(6.5,.5,'The conditional estimate alone does not set the physical energy. Both are calculated in the original state.\nThe covariance and source gain have explicit formulas; no limiting value is assigned.',ha='center',fontsize=10)
fig.savefig(O/'KINETIC_PHYSICAL_MAP.png',dpi=170,bbox_inches='tight');fig.savefig(O/'KINETIC_PHYSICAL_MAP.svg',bbox_inches='tight');plt.close(fig)
js=np.unique(np.rint(np.logspace(1,9,180)).astype(np.int64));fig,axs=plt.subplots(1,3,figsize=(14,5.3))
for kind,label,col in [('sqrt','Square-root collar','#316ca0'),('log','Logarithmic collar','#c37838')]:
    vals=[bounds(j,kind) for j in js]
    for ax,index in zip(axs,[2,3,4]):
        ax.loglog(js,[row[0]**8*row[index] for row in vals],label=label,color=col)
for ax in axs:
    ax.set_xlabel(r'Original regulator $j$');ax.grid(alpha=.2);ax.legend(fontsize=8)
axs[0].set_ylabel(r'Upper function for $a_j^8m_{0,j}^k$')
axs[1].set_ylabel(r'Upper function for $a_j^8D_{kk}(s_j)$')
axs[2].set_ylabel(r'Upper function for $a_j^8|D_{\gamma k}(s_j)|$')
fig.suptitle('Variance and removed inverse mass at the original energy',weight='bold')
fig.text(.5,.02,r'KC12–KC20; $R=\kappa_*=1$, $a_j=(100j)^{-1}$, $s_j=100\kappa_*a_j$; all integer counts retained.'+'\nProved upper functions only: these curves are not measured quantum variances or spectral gaps.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.09,1,.93))
fig.savefig(O/'KINETIC_INVERSE_RATES.png',dpi=170,bbox_inches='tight');fig.savefig(O/'KINETIC_INVERSE_RATES.svg',bbox_inches='tight');plt.close(fig)
(O/'KINETIC_CURRENT_CHECKS.json').write_text(json.dumps(dict(description=__doc__,checks=len(rows),all_passed=True,results=rows),indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=len(rows),all_passed=True)))
