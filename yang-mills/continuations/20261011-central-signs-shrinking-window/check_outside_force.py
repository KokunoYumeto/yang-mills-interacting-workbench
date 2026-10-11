"""OC diagnostics: exact original combinatorics, curved comparison identities and full moment remainders.
No computed density or matrix below is an original Yang--Mills ground-state sample."""
from pathlib import Path
import json,math,itertools
import numpy as np
from numpy.polynomial import Polynomial
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent;records=[]
def check(name,value,expected,tol=4e-11,**meta):
    v=float(value);e=float(expected);err=abs(v-e);ok=err<=tol*(1+abs(e))
    records.append(dict(name=name,value=v,expected=e,error=err,tolerance=tol,passed=ok,**meta));assert ok,(name,v,e,meta)
def truth(name,ok,**meta):
    records.append(dict(name=name,passed=bool(ok),**meta));assert ok,(name,meta)
def haar(n):
    t=np.arange(1,n+1)*np.pi/(n+1);return np.cos(t),2*np.sin(t)**2/(n+1)
x,wx=haar(90);y,wy=haar(93);x=x[:,None];y=y[None,:]
nx=(1-x*x)/4;ny=(1-y*y)/4;lx=-.75*x;ly=-.75*y
for A,B,C in [(.25,.25,1/32),(.7,-.4,.2),(-.8,.2,-.6),(.1,-.3,.9),(-.2,-.7,.5),(0,0,0)]:
    for kap in [.4,1.,2.3]:
        w=A*x+B*y+C*x*y;rho=wx[:,None]*wy[None,:]*np.exp(2*w);Z=rho.sum();rho/=Z
        av=lambda f:np.sum(rho*f)
        t=B+C*x;cy=wy[None,:]*np.exp(2*t*y);cy/=cy.sum(axis=1,keepdims=True)
        ey=np.sum(cy*y,axis=1,keepdims=True);vary=np.sum(cy*(y-ey)**2,axis=1,keepdims=True)
        Ex=lambda f:np.sum(cy*f,axis=1,keepdims=True)
        Ay=A+C*y;gb=A+C*ey;d2=2*C*C*vary
        U=kap*(ly*t+ny*t*t);Ux=kap*C*(ly+2*ny*t);Uxx=2*kap*C*C*ny
        score=C*(y-ey)*np.sqrt(nx);force=Ux*np.sqrt(nx)
        direct_Lscore=-kap*C*(ly+2*t*ny)*np.sqrt(nx)
        meta=dict(A=A,B=B,C=C,kappa=kap,partition=Z)
        check('OC3-score-Poisson',np.max(np.abs(direct_Lscore+force)),0,**meta)
        check('OC3-conditional-score-mean',np.max(np.abs(Ex(score))),0,**meta)
        check('OC3-conditional-force-mean',np.max(np.abs(Ex(force))),0,**meta)
        # Complete averaged Hessian: parallel component and both perpendicular components.
        check('OC4-parallel-averaged-Hessian',np.max(np.abs(Ex(Uxx*nx-Ux*x/4)-2*kap*C*C*nx*Ex(ny))),0,**meta)
        check('OC4-perpendicular-averaged-Hessian',np.max(np.abs(Ex(-Ux*x/4))),0,**meta)
        check('OC4-complete-trace',np.max(np.abs(Ex(nx*Uxx+lx*Ux)-2*kap*C*C*nx*Ex(ny))),0,**meta)
        for h,k in [(1.,1.),(-.7,.4),(.3+.2j,-.5j)]:
            S=lx*Ay+2*nx*Ay**2;s=lx*gb+nx*d2+2*nx*gb**2;p=gb*C*(y-ey)*nx
            q=k*(S-s)+2*(h-k)*p
            qy=k*(C*lx+4*nx*C*Ay)+2*(h-k)*gb*C*nx
            qyy=4*k*nx*C*C
            direct=-kap*(ny*qyy+(ly+2*t*ny)*qy)
            forcing=-k*(nx*Uxx+lx*Ux)-nx*(4*k*Ay+2*(h-k)*gb)*Ux-2*kap*k*C*C*nx*ny
            check('OC11-complete-current-forcing',np.max(np.abs(direct-forcing)),0,**meta,h=str(h),k=str(k))
            check('OC10-current-conditional-mean',np.max(np.abs(Ex(q))),0,**meta,h=str(h),k=str(k))
            m0=float(av(abs(q)**2).real);m1=float((kap*av(ny*abs(qy)**2)).real);m2=float(av(abs(forcing)**2).real)
            check('OC13-first-moment-independent-IBP',av(np.conj(q)*direct).real,m1,**meta,h=str(h),k=str(k))
            check('OC13-first-moment-imaginary-part',av(np.conj(q)*direct).imag,0,**meta,h=str(h),k=str(k))
            truth('OC13-moment-Gram-positive',m0*m2-m1*m1>=-1e-12,**meta,h=str(h),k=str(k))
        # Original potential-to-conditional-potential equality for this manufactured curved state.
        V=kap*(lx*Ay+ly*t+nx*Ay*Ay+ny*t*t);KQ=lx*Ay+nx*Ay*Ay
        check('OC2-full-kinetic-quotient',np.max(np.abs(V-kap*KQ-U)),0,**meta)

# Finite Galerkin force receiver with its full density mass matrix.
# The exact score solution is a linear coordinate polynomial, already inside every trial below.
yy,ww=haar(120);nyy=(1-yy*yy)/4
for xx in [-.7,0,.6]:
    for A,B,C,kap in [(.25,.25,1/32,1.),(.7,-.4,.2,.4),(-.8,.2,-.6,2.3)]:
        t=B+C*xx;nu=ww*np.exp(2*t*yy);nu/=nu.sum()
        em=np.sum(nu*yy);nxx=(1-xx*xx)/4
        score=C*(yy-em)*math.sqrt(nxx)
        force=kap*C*(-.75*yy+2*nyy*t)*math.sqrt(nxx)
        for degree in [4,8,12]:
            polys=[Polynomial([1.]),Polynomial([0.,2.])]
            for k in range(2,degree+1):polys.append(Polynomial([0.,2.])*polys[-1]-polys[-2])
            phi=np.stack([p(yy) for p in polys[1:]]);phi-=np.sum(phi*nu,axis=1)[:,None]
            dp=np.stack([p.deriv()(yy) for p in polys[1:]])
            M=(phi*nu)@phi.T;K=kap*(dp*(nu*nyy))@dp.T
            lam,V=eigh(K,M);truth('OC6-positive-Galerkin-spectrum',np.min(lam)>0,x=xx,degree=degree)
            bf=phi@(nu*force);force_coordinates=V.T@bf
            direct_cov=np.sum(nu*score**2)
            check('OC6-full-inverse-squared-force',np.sum(force_coordinates**2/lam**2),direct_cov,tol=2e-9,x=xx,degree=degree)
            hessian=2*kap*C*C*nxx*np.sum(nu*nyy)
            check('OC6-full-inverse-force-Hessian',2*np.sum(force_coordinates**2/lam),hessian,tol=2e-9,x=xx,degree=degree)

# Original face counts, with degrees computed by enumerating the complete oriented words.
def face_words(m):
    out=[]
    for z in itertools.product(range(m+1),repeat=3):
        for d,k in itertools.combinations(range(3),2):
            if z[d]>=m or z[k]>=m:continue
            zd=list(z);zd[d]+=1;zk=list(z);zk[k]+=1
            out.append([((z,d),1),((tuple(zd),k),1),((tuple(zk),d),-1),((z,k),-1)])
    return out
for m in range(2,8):
    words=face_words(m);deg={}
    for word in words:
        for e,sign in word:deg[e]=deg.get(e,0)+1
    for r,n in [(2,12*m),(3,12*m*(m-1)),(4,3*m*(m-1)**2)]:
        check('OC8-exact-edge-degree-count',sum(v==r for v in deg.values()),n,m=m,degree=r,tol=0)
    check('OC8-total-original-face-incidence',sum(deg.values()),4*3*m*m*(m+1),m=m,tol=0)
m=6;words=face_words(m);low=(2,2,2);side=2
inside=lambda e:all(low[d]<=e[0][d]<=low[d]+side-(1 if d==e[1] else 0) for d in range(3))
cross=[w for w in words if sum(inside(e) for e,s in w)==1]
sigma=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex)]
T=[-.5j*s for s in sigma]
for word in cross:
    e,se=next((e,s) for e,s in word if inside(e))
    er=next((r,sr) for r,sr in word if not inside(r) and r[1]!=e[1])
    r,sr=er
    both=[w for w in words if e in dict(w) and r in dict(w)]
    truth('OC19-unique-original-crossing-face',len(both)==1)
    for alpha in range(3):
        value=-se*sr*np.trace(T[alpha]@T[alpha]).real
        check('OC19-exact-mixed-potential-coefficient',value,se*sr/2,tol=0)
# Actual comparison bound: original path and both minimum branches.
def Bout(j,kap=1.,R=1.):
    m=2*j**4;a=1/(100*j);q=math.ceil(R/a)+3
    NQ=3*q*(q+1)**2
    counts={2:12*m,3:12*m*(m-1),4:3*m*(m-1)**2-NQ}
    assert counts[4]>0
    value=sum(n*min(r/(kap*kap*a*a),math.sqrt(r)/(kap*a)) for r,n in counts.items())
    return value
for kap in [.4,1.,2.3]:
    check('OC9-original-j13-coefficient',Bout(10000,kap)/10000**13,4800/kap,tol=1e-10,kappa=kap)

# Full finite-matrix resolvents checked independently of the moment fractions.
rng=np.random.default_rng(61011)
for case in range(32):
    n=3+case%6;Q,_=np.linalg.qr(rng.normal(size=(n,n)))
    lam=np.geomspace(.007,13,n)*(1+case/7)
    L=(Q*lam)@Q.T
    q=(rng.normal(size=n)+1j*rng.normal(size=n))*10**((case%5)-2)
    m0=np.vdot(q,q).real;m1=np.vdot(q,L@q).real;m2=np.vdot(L@q,L@q).real
    for z in [.001,.2,3.]:
        I=(z*np.vdot(q,np.linalg.solve(L+z*np.eye(n),q))).real;D=m0-I
        qc=Q.T@q
        r1=np.sqrt(lam/(lam+z))*qc-m1/(m2+z*m1)*np.sqrt(lam*(lam+z))*qc
        r2=qc/np.sqrt(lam+z)-m0/(m1+z*m0)*np.sqrt(lam+z)*qc
        check('OC14-full-gain-remainder',D,m1*m1/(m2+z*m1)+np.vdot(r1,r1).real,tol=3e-9,case=case,z=z)
        check('OC14-full-filter-remainder',I,z*m0*m0/(m1+z*m0)+z*np.vdot(r2,r2).real,tol=3e-9,case=case,z=z)
        truth('OC14-complete-moment-bounds',z*m0*m0/(m1+z*m0)<=I+2e-8*(1+m0) and I<=m0-m1*m1/(m2+z*m1)+2e-8*(1+m0),case=case,z=z)
for m0,m1,m2 in [(2.,3.,8.),(.4,1.7,9.),(7.,.2,3.)]:
    for f in [1e-5,.03,.4,.9]:
        eps=f*m1/m0;den=m2-2*eps*m1+eps*eps*m0;la=(m2-eps*m1)/(m1-eps*m0)
        aa=(m0*m2-m1*m1)/den;bb=(m1-eps*m0)**2/den
        check('OC15-zeroth-moment',aa+bb,m0)
        check('OC15-first-moment',aa*eps+bb*la,m1)
        check('OC15-second-moment',aa*eps*eps+bb*la*la,m2)
        truth('OC15-no-zero-spectral-atom',min(eps,la,aa,bb)>0)
        z=.2;I=aa*z/(eps+z)+bb*z/(la+z)
        truth('OC15-upper-bound-with-unchanged-moments',I<=m0-m1*m1/(m2+z*m1)+1e-12)
        u,v=.3+.4j,-.2+.7j
        lhs=abs(u)**2*m0+2*np.real(np.conj(u)*v)*m1+abs(v)**2*m2
        rhs=aa*abs(u+v*eps)**2+bb*abs(u+v*la)**2
        check('OC16-exact-moment-span-isometry',lhs,rhs)

for case in range(24):
    n=7;d=5;rank=1+case%5
    left=rng.normal(size=(n,rank));right=rng.normal(size=(rank,d));X=left@right
    Qrot,_=np.linalg.qr(rng.normal(size=(n,n)))
    eigen=np.linspace(.2,4,n);L=(Qrot*eigen)@Qrot.T
    Force=-L@X;G=X.T@X;HH=2*X.T@L@X;QQ=Force.T@Force
    Gplus=np.linalg.pinv(G,rcond=1e-11);residual=Force+.5*X@Gplus@HH
    target=QQ-.25*HH@Gplus@HH
    check('OC24-full-force-projection-remainder',np.linalg.norm(target-residual.T@residual),0,tol=2e-8,case=case,rank=rank)
    check('OC24-complete-score-orthogonality',np.linalg.norm(X.T@residual),0,tol=2e-8,case=case,rank=rank)
    truth('OC23-common-kernels',np.linalg.matrix_rank(G,tol=1e-8)==np.linalg.matrix_rank(HH,tol=1e-8)==np.linalg.matrix_rank(QQ,tol=1e-8)==rank,case=case)
    truth('OC23-positive-operator-comparison',np.linalg.eigvalsh(HH-2*eigen[0]*G)[0]>=-1e-8,case=case)
out=dict(description=__doc__,checks=len(records),all_passed=all(r['passed'] for r in records),records=records)
(O/'OUTSIDE_FORCE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,ax=plt.subplots(figsize=(12,6.4));ax.set_xlim(0,12);ax.set_ylim(0,6);ax.axis('off')
def box(x,y,w,h,title,lines,color='#e5eef6'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.09',fc=color,ec='#365776',lw=1.2))
    ax.text(x+w/2,y+h-.25,title,ha='center',va='center',fontsize=12,weight='bold',color='#203c59')
    for i,t in enumerate(lines):ax.text(x+w/2,y+h-.7-i*.4,t,ha='center',va='center',fontsize=12)
box(.15,3.2,3.4,1.6,'Original conditional potential',
    [r'$\mathcal{U}_{\rm out}=V-E_0-\kappa K_Q$',r'$K_Q=\Delta_Q\psi/\psi$'])
box(4.2,3.2,3.3,1.6,'Score and exact forcing',
    [r'$\mathscr{L}_{\rm out}\xi_e=-F_e$',r'$F_e=\nabla_e\mathcal{U}_{\rm out}$'])
box(8.15,3.2,3.5,1.6,'Positive averaged Hessian',
    [r'$\mathbb{E}_x\nabla_Q^2\mathcal{U}_{\rm out}$',r'$=2\kappa\,\mathbb{E}_x(d_{\rm out}\xi)^*(d_{\rm out}\xi)$'])
for x0,x1 in [(3.57,4.08),(7.52,8.03)]:ax.annotate('',xy=(x1,4),xytext=(x0,4),arrowprops={'arrowstyle':'->','lw':1.5})
box(.5,.7,4.8,1.75,'Actual outside-current moments',
    [r'$m_0=\|q\|_\mu^2,\quad m_1=\kappa\|d_{\rm out}q\|_\mu^2$',r'$m_2=\|\mathscr{F}_{h,k}\|_\mu^2$',r'$\mathscr{F}_{h,k}=\mathscr{L}_{\rm out}q_{h,k}$'],'#e5f2ec')
box(6,.7,5.4,1.75,'Quantified removed energy',
    [r'$D_z\geq m_1^2/(m_2+zm_1)$',r'$d_z=\kappa a^4m_1^2/(m_2+zm_1)>0$',r'$h=k>0$ on $Q$; OC17–OC21'],'#e5f2ec')
ax.annotate('',xy=(5.9,1.55),xytext=(5.4,1.55),arrowprops={'arrowstyle':'->','lw':1.5})
ax.text(6,2.82,'OC10–OC12 retain every mixed Hessian, potential scalar and inside kinetic derivative.',ha='center',fontsize=10.5)
fig.suptitle('Outside score forcing keeps the full original kinetic quotient',fontsize=16,weight='bold',y=.96)
fig.text(.5,.035,'OC1–OC6 and OC10–OC21. Exact identities for the original ground state and conditional operator.\nThe finite positive improvement retains both physical residuals; its limiting value is not assigned.',ha='center',fontsize=10.5)
fig.subplots_adjust(left=.02,right=.98,top=.87,bottom=.11)
for ext in ['png','svg']:fig.savefig(O/f'OUTSIDE_FORCE_MAP.{ext}',dpi=175)
plt.close(fig)
m0,m1,m2=2.,3.,8.
def comp(eps,z):
    den=m2-2*eps*m1+eps*eps*m0;la=(m2-eps*m1)/(m1-eps*m0)
    aa=(m0*m2-m1*m1)/den;bb=(m1-eps*m0)**2/den
    return aa*z/(eps+z)+bb*z/(la+z)
fig,axs=plt.subplots(1,2,figsize=(12,5.5))
eps=np.geomspace(.0001,1.4,230);z=.2
axs[0].semilogx(eps,[comp(e,z) for e in eps],color='#1f657d',lw=2,label='Exact positive two-eigenvalue comparison')
axs[0].axhline(m0-m1*m1/(m2+z*m1),color='#b55132',ls='--',label='Moment upper bound')
axs[0].axhline(z*m0*m0/(m1+z*m0),color='#6f747c',ls=':',label='Moment lower bound')
axs[0].set_xlabel(r'Lower positive eigenvalue $\epsilon$');axs[0].set_ylabel(r'$I_z=\langle v_\epsilon,z(A_\epsilon+z)^{-1}v_\epsilon\rangle$')
axs[0].set_title(r'All three moments retained; $z=0.2$')
zs=np.geomspace(.001,10,230);eps=.15
axs[1].semilogx(zs,[m0-comp(eps,z) for z in zs],color='#1f657d',lw=2,label='Exact comparison gain')
axs[1].semilogx(zs,[m1*m1/(m2+z*m1) for z in zs],color='#b55132',ls='--',label='Proved moment lower bound')
axs[1].set_xlabel(r'Positive resolvent parameter $z$');axs[1].set_ylabel(r'$D_z=m_0-I_z$');axs[1].set_title(r'Complete gain bound; $\epsilon=0.15$')
for ax in axs:ax.grid(alpha=.18);ax.legend(fontsize=8.5);ax.spines[['top','right']].set_visible(False)
fig.suptitle('Exact moment information and its positive-spectrum limit',fontsize=16,weight='bold',y=.96)
fig.subplots_adjust(left=.08,right=.98,top=.83,bottom=.22,wspace=.27)
fig.text(.5,.055,r'OC14–OC16: $m_0=2$, $m_1=3$, $m_2=8$. Every finite comparison has two strictly positive eigenvalues.'+'\nThese are exact comparison operators with the proved moment-span isometry, not Yang–Mills spectra.',ha='center',fontsize=10.5)
for ext in ['png','svg']:fig.savefig(O/f'OUTSIDE_MOMENT_MAP.{ext}',dpi=175)
plt.close(fig)
print(json.dumps(dict(checks=out['checks'],all_passed=out['all_passed'])))
