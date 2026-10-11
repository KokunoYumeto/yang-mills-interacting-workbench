"""Local-energy diagnostics: manufactured curved states, exact lattice counts and finite positive operators; no original quantum samples."""
from pathlib import Path
import json,math,itertools
from fractions import Fraction
import numpy as np
import sympy as sp
import mpmath as mp
mp.mp.dps=300
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent;rows=[]
def check(name,error,tol=4e-9):
    error=float(error);assert abs(error)<=tol,(name,error,tol)
    rows.append(dict(name=name,error=error,tolerance=tol,passed=True))
x,y,a,b,c,k=sp.symbols('x y a b c k',real=True)
tx=(1-x*x)/4;ty=(1-y*y)/4;wx=a+c*y;wy=b+c*x
Kx=-3*x*wx/4+tx*wx**2;Ky=-3*y*wy/4+ty*wy**2
Vx=k*(-3*a*x/4+tx*a*a);Vy=k*(-3*b*y/4+ty*b*b)
cross=k*(Kx+Ky)-Vx-Vy
alpha=sp.diff(cross,x);raw=Kx-Vx/k
def L(f):return -k*(tx*sp.diff(f,x,2)-3*x*sp.diff(f,x)/4+2*tx*wx*sp.diff(f,x)+ty*sp.diff(f,y,2)-3*y*sp.diff(f,y)/4+2*ty*wy*sp.diff(f,y))
diva=-(tx*sp.diff(alpha,x)-3*x*alpha/4+2*tx*wx*alpha)
assert sp.expand(L(raw)-diva)==0
check('symbolic curved full physical forcing',0)
fn=sp.lambdify((x,y,a,b,c,k),[raw,sp.diff(raw,x),sp.diff(raw,y),L(raw),alpha,Kx,sp.diff(Kx,x),Vx,sp.diff(Vx,x),L(x*x+x),sp.diff(L(x*x+x),x)],'numpy')
t=np.arange(1,101)*np.pi/101;nodes=np.cos(t);weights=2/101*np.sin(t)**2
xx=nodes[:,None];yy=nodes[None,:];base=weights[:,None]*weights[None,:]
for z,(aa,bb,cc,kap) in enumerate(itertools.product([-.19,.27],[.12,.31],[-.09,.16],[.7,1.8])):
    density=np.exp(2*(aa*xx+bb*yy+cc*xx*yy));partition=np.sum(base*density);mu=base*density/partition
    avg=lambda v:np.sum(mu*v)
    cond=lambda v:np.sum(mu*v,axis=1)[:,None]/np.sum(mu,axis=1)[:,None]
    rr,dx,dy,force,al,K,Kd,vx,vxd,LF,dLF=[np.asarray(v)+np.zeros_like(mu) for v in fn(xx,yy,aa,bb,cc,kap)]
    ups=rr-avg(rr);kq=K-cond(K);R=kap*cond(K)-vx;h=(R-avg(R))/kap
    xi=cc*(yy-cond(yy));rho=cond(kq*xi);dR=kap*(cond(Kd)+2*rho)-vxd
    check(f'curved{z}: original covariance cancellation',np.max(abs(dR-cond(al)-2*kap*rho)))
    check(f'curved{z}: whole original energy vector',np.max(abs(ups-kq-h)))
    check(f'curved{z}: complete variance',avg(ups*ups)-avg(kq*kq)-avg(h*h))
    check(f'curved{z}: vacuum orthogonality',avg(ups))
    check(f'curved{z}: complete physical energy',avg(ups*force)-kap*avg((1-xx*xx)/4*dx*dx+(1-yy*yy)/4*dy*dy))
    F=xx*xx+xx-avg(xx*xx+xx)
    check(f'curved{z}: original source covariance',avg(F*ups)-avg(F*R)/kap)
    # This comparison does not have disjoint support: retain its nonzero energy pairing.
    check(f'curved{z}: complete source energy form',avg(F*force)-avg((1-xx*xx)/4*(2*xx+1)*al))
    check(f'curved{z}: full source second moment',avg(LF*force)-avg((1-xx*xx)/4*dLF*al))
rng=np.random.default_rng(20261011070)
def lap(n):
    t=rng.uniform(.4,1.5,n-1);D=np.diff(np.eye(n),axis=0)
    return D.T@np.diag(t)@D
for i in range(25):
    ni=3+i%3;no=4+i%2
    A=np.kron(lap(ni),np.eye(no));B=np.kron(np.eye(ni),lap(no));M=.4+i*.01
    cv=rng.uniform(-1,1,ni*no);cv-=cv.mean();cv=M+.7*M*cv/max(abs(cv))
    es,vs=np.linalg.eigh(A+B+np.diag(cv));eps=es[0];psi=vs[:,0]
    if sum(psi)<0:psi=-psi
    assert min(psi)>0
    mu=psi*psi;ap=A@psi;bp=B@psi;aph=ap/psi;kap=.7+.013*i
    aq=(mu*aph).reshape(ni,no).sum(axis=1)/mu.reshape(ni,no).sum(axis=1);R=eps-aq
    ups=-(aph-mu@aph)/kap;kq=-(aph-np.repeat(aq,no))/kap
    h=np.repeat((R-mu.reshape(ni,no).sum(axis=1)@R)/kap,no)
    check(f'commuting{i}: complete vector decomposition',np.linalg.norm(ups-kq-h))
    n=mu@(ups*ups);rema=[(M-eps)*(M+eps-2*(mu@cv)),mu@(cv*(2*M-cv)),bp@bp,2*ap@bp,(mu@aph)**2]
    check(f'commuting{i}: whole variance with all remainders',kap*kap*n-M*M+sum(rema))
    check(f'commuting{i}: retained positive remainders',max(0,-min(rema)))
    check(f'commuting{i}: full physical first moment',ups@(np.diag(psi)@(A+B+np.diag(cv)-eps*np.eye(ni*no))@np.diag(psi))@ups-((psi*ups)@(A+B+np.diag(cv)-eps*np.eye(ni*no))@(psi*ups)))
for side in range(1,9):
    edge=lambda z,d:(tuple(z),d)
    inside=lambda ed:all(0<=ed[0][i]<=side-(ed[1]==i) for i in range(3))
    faces=[]
    for z in itertools.product(range(-1,side+1),repeat=3):
        for d,e in itertools.combinations(range(3),2):
            zd=list(z);ze=list(z);zd[d]+=1;ze[e]+=1
            es=[edge(z,d),edge(zd,e),edge(ze,d),edge(z,e)]
            flags=[inside(ed) for ed in es]
            if any(flags) and not all(flags):faces.append(es);assert sum(flags)==1
    support={ed for face in faces for ed in face if inside(ed)}
    counts={ed:sum(ed in f for f in faces) for ed in {ed for f in faces for ed in f}}
    check(f'cube{side}: original crossing count',len(faces)-12*side*(side+1))
    check(f'cube{side}: exact inside boundary support',len(support)-12*side*side)
    check(f'cube{side}: full crossing edge incidence',max(0,max(counts.values())-4))
    check(f'cube{side}: full support count upper bound',max(0,len(counts)-4*len(faces)))
for i in range(35):
    dim=12;pdim=5;Y=rng.normal(size=(16,dim));Y[:,0]=0;L=Y.T@Y
    F=np.zeros(dim);F[1:pdim]=rng.normal(size=pdim-1);kv=np.zeros(dim);kv[pdim:]=rng.normal(size=dim-pdim)
    h=-(F@L@kv)/(F@L@F)*F;ups=kv+h
    z=.03+i*.018;m=F@F;n=ups@ups;p=F@ups;df=F@L@F;e=ups@L@ups
    G=np.array([[m,p],[p,n]]);E=np.diag([df,e]);Q=np.array([[F@L@L@F,F@L@L@ups],[ups@L@L@F,ups@L@L@ups]])
    az=df+z*m;tz=e+z*n-z*z*p*p/az;be=p*df/(az*tz);ga=(m-z*p*be)/az
    X=ga*F+be*ups;T=L+z*np.eye(dim);true=np.linalg.solve(T,F);err=true-X
    check(f'physical{i}: disjoint energy algebra',F@L@ups,2e-7)
    check(f'physical{i}: source Gram strict determinant',max(0,m*(kv@kv)-(m*n-p*p)))
    check(f'physical{i}: two-vector Green gain and full residual',F@true-m*m/az-p*p*df*df/(az*az*tz)-err@T@err,2e-7)
    coef=np.array([ga,be]);res=F-T@X
    re=m-2*coef@np.array([df+z*m,z*p])+coef@(Q+2*z*E+z*z*G)@coef
    check(f'physical{i}: full second-moment residual',res@res-re,3e-7)
    Az=T[:pdim,:pdim];om=(L@kv)[:pdim];ell=(T@ups)[:pdim];delta=kv@T@kv-om@np.linalg.solve(Az,om)
    check(f'physical{i}: explicit whole-space Schur map',ups@T@ups-ell@np.linalg.solve(Az,ell)-delta,2e-7)
    ez=om@np.linalg.solve(Az,F[:pdim])
    check(f'physical{i}: same whole-space source remainder',p-ell@np.linalg.solve(Az,F[:pdim])+ez)
    lam,U=np.linalg.eigh(L);assert lam[0]>-1e-10;lam[0]=0
    v=U.T@ups;f=U.T@F;s=np.quantile(lam[1:],.4);low=(lam>1e-9)&(lam<=s);high=lam>s
    check(f'physical{i}: actual spectral tail bound',max(0,sum(v[high]**2)-e/s))
    check(f'physical{i}: full physical inverse defect',max(0,np.sum(v*v*lam/(lam+s))-e/s))
    overlap=np.sum(f[low]*v[low])
    check(f'physical{i}: high-energy source remainder',max(0,abs(p-overlap)-math.sqrt(m*e/s)))
    check(f'physical{i}: source window lower function',max(0,max(0,abs(p)-math.sqrt(m*e/s))**2/n-sum(f[low]**2)))
Cheat=2+2*math.sqrt(4+2*math.pi)
def bounds(j,kind,R=1.,kap=1.):
    ratio=Fraction(str(R))*100*int(j)
    R=mp.mpf(R);kap=mp.mpf(kap);a=mp.mpf(1)/(100*int(j))
    K=max(1,math.isqrt(ratio.numerator//ratio.denominator) if kind=='sqrt' else int(mp.floor(R/(a*mp.log(mp.e+R/a)))))
    q=math.ceil(ratio)+3;side=q+2*K;N=3*side*(side+1)**2;M=3*side*side*(side+1);C=12*side*(side+1)
    Lam=min(2*M,3*kap*a*mp.sqrt(N*M))+2*C;g=min(8/(kap*kap*a*a),Cheat/(kap*a))
    Ab=12*side*side*g*g;Ac=4*C*g*g
    # Lower crossing count and upper score count give a bound uniform in the selected side.
    Cbase=12*q*(q+1)
    Bstar=9/(64*Ab)*max(0,2*Cbase-Lam/K)**2
    nu=4*C*C/(kap**4*a**4);eu=2*Lam/(kap**3*a**4*K)
    qu=(1/(kap*kap*a**4))*(mp.mpf('1.5')*C+2*mp.sqrt(2*Ab*Lam/K))**2
    el=K*Bstar**2/(16*kap**3*a**4*Lam)
    nl=Bstar**2/(kap**4*a**4*(6*C+8*mp.sqrt(Ac*Lam/K))**2)
    return a,K,nu,eu,qu,Bstar,el,nl,eu/(100*kap*a)
for kind in ['sqrt','log']:
    a,K,nu,eu,qu,bs,el,nl,defect=bounds(10**200,kind);LR=33;BR=27/(4*Cheat**2);tol=.05 if kind=='log' else 1e-12
    for name,ratio in [('variance upper',a**8*nu/576),('energy upper',a**6*K*eu/(2*LR)),('second moment upper',a**10*K*qu/(96*Cheat**2*LR)),('boundary lower',bs/BR),('energy lower',a*a/K*el/(729/(256*Cheat**4*LR))),('norm lower',nl/(a*a*K)/(243/(16384*Cheat**6*LR))),('physical window',a**7*K*defect/(LR/50))]:
        check(kind+': complete '+name+' coefficient',ratio-1,tol)
fig,ax=plt.subplots(figsize=(13,7));ax.set_xlim(0,13);ax.set_ylim(0,7);ax.axis('off')
def box(x,y,w,h,t,col):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',facecolor=col,edgecolor='#52667c'))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=11)
def arrow(p,q):ax.add_patch(FancyArrowPatch(p,q,arrowstyle='->',mutation_scale=17,color='#33465c'))
ax.text(6.5,6.65,'The whole original local-energy fluctuation',ha='center',fontsize=17,weight='bold')
box(.4,4.1,3.7,1.7,r'$\upsilon_Q=k_Q+(R_Q-\mu R_Q)/\kappa$'+'\n'+r'$2\kappa\rho_Q=dR_Q-b\,\mathbb{E}_x\alpha$'+'\nExact covariance cancellation\nLE4–LE5','#e6eef6')
box(4.7,4.1,3.5,1.7,r'$d\upsilon_Q=(b/\kappa)P\alpha$'+'\n'+r'$\mathscr{L}_0\upsilon_Q=b\delta_Q\alpha$'+'\nFull physical Hamiltonian\nLE6–LE7','#e6f2ed')
box(8.9,4.1,3.65,1.7,r'$\|\Pi_{s_j}^{>}\upsilon_Q\|^2\leq e/s_j$'+'\n'+r'$a_j^8\|\Pi_{s_j}^{>}\upsilon_Q\|^2\to0$'+'\nOriginal physical window\nLE21–LE22','#fff2da')
arrow((4.25,4.95),(4.55,4.95));arrow((8.35,4.95),(8.75,4.95))
box(.5,1.45,5.5,1.8,r'$p=\operatorname{Cov}(C,R_Q)/\kappa$'+'\n'+r'$\langle F,\mathscr{L}_0\upsilon_Q\rangle=0$'+'\nDisjoint edge supports give energy orthogonality.\nOrdinary covariance is retained; LE15–LE18.','#e6eef6')
box(6.95,1.45,5.5,1.8,r'$f+\tau\upsilon_Q=(f+\tau h_Q)+\tau k_Q$'+'\nThe complete scalar trial space is the same.\nIts full Schur complement and source remainder\nare unchanged; LE19–LE20.','#e6f2ed')
arrow((2.25,3.95),(2.9,3.4));arrow((6.5,3.95),(9.4,3.4))
ax.text(6.5,.45,'No limiting norm or observable overlap is assigned. All original energies, covariance terms and physical residuals remain.',ha='center',fontsize=10)
fig.savefig(O/'LOCAL_ENERGY_PHYSICAL_MAP.png',dpi=170,bbox_inches='tight');fig.savefig(O/'LOCAL_ENERGY_PHYSICAL_MAP.svg',bbox_inches='tight');plt.close(fig)
js=np.unique(np.rint(np.logspace(1,9,150)).astype(np.int64));fig,axs=plt.subplots(1,3,figsize=(14,5.2))
for kind,label,col in [('sqrt','Square-root collar','#316ca0'),('log','Logarithmic collar','#ba753a')]:
    vv=[tuple(float(t) for t in bounds(j,kind)) for j in js]
    axs[0].loglog(js,[r[0]**8*r[2] for r in vv],label=label+' upper',color=col)
    axs[0].loglog(js,[r[0]**8*r[7] for r in vv],ls='--',label=label+' lower',color=col)
    axs[1].loglog(js,[r[0]**8*r[8] for r in vv],label=label,color=col)
    axs[2].semilogx(js,[r[5] for r in vv],label=label,color=col)
for ax in axs:ax.grid(alpha=.2);ax.set_xlabel('Original regulator j');ax.legend(fontsize=8)
axs[0].set_ylabel(r'Bounds for $a_j^8\|\upsilon_Q\|^2$')
axs[1].set_ylabel(r'Upper function for $a_j^8e/s_j$')
axs[2].set_ylabel(r'Lower function for $\|\alpha\|^2$')
fig.suptitle('Physical norm, removed spectral weight and actual boundary force',weight='bold')
fig.text(.5,.015,r'LE9–LE14 and LE22; $R=\kappa_*=1$. Exact integer counts; lower functions use the inner crossing count and outer score count.'+'\nThese are proved bounds uniform in the selected cube, not measured vacuum data or spectral gaps.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.10,1,.94))
fig.savefig(O/'LOCAL_ENERGY_WINDOW_BOUNDS.png',dpi=170,bbox_inches='tight');fig.savefig(O/'LOCAL_ENERGY_WINDOW_BOUNDS.svg',bbox_inches='tight');plt.close(fig)
(O/'LOCAL_ENERGY_CHECKS.json').write_text(json.dumps(dict(description=__doc__,checks=len(rows),all_passed=True,results=rows),indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=len(rows),all_passed=True)))
