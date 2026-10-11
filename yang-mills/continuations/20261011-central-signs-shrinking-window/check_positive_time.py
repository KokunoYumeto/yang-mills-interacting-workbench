from pathlib import Path
import json,hashlib
import numpy as np
import sympy as s
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
O=Path(__file__).resolve().parent
a,k,K,B,Bp,z,E,E2,r,m=s.symbols('a k K B Bp z E E2 r m',positive=True)
mixed=3*K/(2*a)-B/(2*a*k)
last=9*K/(4*a*a)-3*B/(2*a*a*k)-Bp/(4*a*a*k*k)
exact=[]
def eq(name,expr):
    assert s.simplify(expr)==0,name
    exact.append(name)
eq('PT5 complete two-time cancellation',k*k*(9*K-12*a*mixed+4*a*a*last)+Bp)
q=s.symbols('q')
for n in [0,1,2,7,19]:
    eq('PT24 full geometric remainder '+str(n),sum(q**i for i in range(n+1))+q**(n+1)/(1-q)-1/(1-q))
R=s.symbols('R')
eq('PT29 exact window threshold',s.solve(s.Eq(R,m/z+(E-m)/(z+r)),m)[0]-z*(z+r)/r*(R-E/(z+r)))
H=s.symbols('H')
eq('PT26 all kappa factors',k*(E/k)**2/(k*H+(k/2+4/a+z)*E/k)-E**2/(k*k*H+(k/2+4/a+z)*E))
eq('PT23 contraction identity',1/(1+m/z)-z/(z+m))
rng=np.random.default_rng(11061735);count=0;worst=0.
def chk(name,x,y,tol=2e-8):
    global count,worst
    err=float(np.max(np.abs(np.asarray(x)-np.asarray(y))))
    scale=1+float(np.max(np.abs(np.asarray(y))))
    assert err<=tol*scale,(name,err,scale)
    worst=max(worst,err/scale);count+=1
def positive(name,A,tol=2e-8):
    global count
    assert np.linalg.eigvalsh((A+A.T)/2).min()>=-tol*(1+np.linalg.norm(A,2)),name
    count+=1
def power(A,p):
    w,v=np.linalg.eigh(A);assert w.min()>0
    return (v*w**p)@v.T
for j in range(32):
    n=7;kap=.7+j/20;aa=1/(100*(j+1))
    X=rng.normal(size=(n,n));L=X.T@X+.03*np.eye(n)
    Y=rng.normal(size=(n,n))
    T=(kap/2+4/aa)*np.eye(n)+Y.T@Y
    S=(T-L)/(2*kap);positive('S actual algebra prerequisites',S)
    g=rng.normal(size=n);g[3:]=0
    for zz in [.1,1.,7.]:
        I=np.eye(n);Tz=T+zz*I;Dz=L+zz*I
        half=power(Tz,-.5);Q=2*kap*half@S@half
        mq=2*kap*np.linalg.eigvalsh(S).max()
        positive('PT23 explicit contraction',mq/(zz+mq)*I-Q)
        v=half@g;xi=np.sqrt(kap)*power(I-Q,-.5)@v
        Rfull=kap*g@np.linalg.solve(Dz,g)
        chk('PT23 inverse',half@np.linalg.solve(I-Q,half),np.linalg.inv(Dz))
        chk('PT35 norm',xi@xi,Rfull)
        J=power(Dz,.5)@half@power(I-Q,-.5)
        chk('PT36 left unitary',J.T@J,I)
        chk('PT36 right unitary',J@J.T,I)
        chk('PT36 vector receiver',J@xi,np.sqrt(kap)*power(Dz,-.5)@g)
        Sch=Dz[:3,:3]-Dz[:3,3:]@np.linalg.solve(Dz[3:,3:],Dz[3:,:3])
        chk('PT20 full exterior inverse',kap*g[:3]@np.linalg.solve(Sch,g[:3]),Rfull)
        positive('PT19 Schur lower bound',Sch-zz*np.eye(3))
        for N in [0,1,4,30]:
            trunc=kap*sum(v@np.linalg.matrix_power(Q,i)@v for i in range(N+1))
            tail=kap*v@np.linalg.matrix_power(Q,N+1)@np.linalg.solve(I-Q,v)
            chk('PT24 exact all-order remainder',trunc+tail,Rfull)
            assert tail>=-1e-10;count+=1
            assert trunc<=(N+1)*kap*(g@g)/(kap/2+4/aa+zz)+1e-9;count+=1
        lam,U=np.linalg.eigh(Q)
        for delta in [.02,.1,np.sqrt(aa)]:
            outside=U[:,lam<=1-delta]
            mass=np.linalg.norm(outside.T@xi)**2
            assert mass<=kap*(g@g)/((kap/2+4/aa+zz)*delta)+1e-8;count+=1
        ev,V=np.linalg.eigh(L);weight=kap*(V.T@g)**2;ener=float(sum(weight))
        chk('PT20 spectral resolvent',sum(weight/(zz+ev)),Rfull)
        for cutoff in [.1,1.,5.,10.]:
            mass=sum(weight[ev<=cutoff])
            lower=max(0,zz*(zz+cutoff)/cutoff*(Rfull-ener/(zz+cutoff)))
            assert mass>=lower-1e-8;count+=1
fig=plt.figure(figsize=(13,7.8),layout='constrained')
gs=fig.add_gridspec(2,2,width_ratios=[1.25,1])
ax=fig.add_subplot(gs[:,0]);ax.axis('off')
ax.set_title('Exact maps for the original energy vector',loc='left',fontweight='bold',fontsize=14)
boxes=[
(.88,r'$\zeta_j=A_j^{1/2}u_j$',r'Original time, state norm and gauge constraints'),
(.68,r'$\sqrt{\kappa_*}\,dC_j$',r'Unitary $VU_0^{-1}$ on the exact physical subspace (PT14–17)'),
(.46,r'$\xi_{z,j}=\sqrt{\kappa_*}(I-Q_{z,j})^{-1/2}v_{z,j}$',r'$v_{z,j}=(\mathcal{T}_j+z)^{-1/2}dC_j$; $\|\xi_{z,j}\|^2=\mathcal{R}_j(z)$'),
(.22,r'$\mathcal{J}_{z,j}\xi_{z,j}=\sqrt{\kappa_*}(\mathscr{L}_{1,j}+z)^{-1/2}dC_j$',r'Exact unitary receiver (PT36); no spectrum identification')]
for y,label,sub in boxes:
    ax.text(.5,y,label,ha='center',va='center',fontsize=13,bbox=dict(boxstyle='round,pad=.65',fc='#eef4fb',ec='#426a8f'),transform=ax.transAxes)
    ax.text(.5,y-.074,sub,ha='center',va='center',fontsize=9.2,transform=ax.transAxes)
for top,bottom in [( .782,.735),(.58,.515),(.35,.275)]:
    ax.annotate('',xy=(.5,bottom),xytext=(.5,top),xycoords='axes fraction',arrowprops=dict(arrowstyle='->',lw=1.8,color='#426a8f'))
ax.text(.5,.055,'The exterior Hessian retains the complete complement inverse.\nPT18–21 eliminate edge components on the full configuration space.',ha='center',fontsize=10,transform=ax.transAxes)
bx=fig.add_subplot(gs[0,1])
delta=np.geomspace(1e-5,1,800);x=1-delta
for N in [0,4,40,400]:bx.semilogx(delta,x**(N+1),label=f'N = {N}')
bx.set(xlabel=r'$\delta=1-x$ for a spectral value $x$ of $Q_z$',ylabel=r'Exact tail fraction $x^{N+1}$',ylim=(-.02,1.02))
bx.set_title('Geometric tail transfer functions (PT24)',loc='left',fontsize=12)
bx.legend(fontsize=9);bx.grid(alpha=.22)
cx=fig.add_subplot(gs[1,1]);cx.axis('off')
cx.text(0,.95,'Actual regulator bounds',fontweight='bold',fontsize=13,va='top')
cx.text(0,.76,r'$0\leq R_{0,j}(z)\leq E_j/(\kappa_*/2+4/a_j+z)$',fontsize=13)
cx.text(0,.54,r'$a_j(N_j+1)\to0\ \Longrightarrow\ \mathcal{E}_{N_j,j}(z)\to\mathcal{R}^c(z)$',fontsize=12)
cx.text(0,.32,r'$\|(I-P_{\sqrt{a_j},j})\xi_{z,j}\|^2\leq E_j/[c_j(z)\sqrt{a_j}]$',fontsize=12)
cx.text(0,.05,'The plot shows exact scalar transfer functions, not lattice data.\nThe bounds locate any surviving response; they do not assign\nits limiting value. Complete proofs: PT33–36.',fontsize=10)
fig.savefig(O/'POSITIVE_TIME_MAP.png',dpi=180)
fig.savefig(O/'POSITIVE_TIME_MAP.svg')
plt.close(fig)
result=dict(exact_algebra_checks=len(exact),exact_labels=exact,numerical_checks=count,worst_relative_residual=worst,
    scope='Noncommuting finite matrices test the exact operator identities and bounds. They are not sampled Yang–Mills states; complete proofs are in PT1–PT36.',
    figure='Exact maps and geometric transfer functions; no physical data or assigned limiting coefficient.')
(O/'POSITIVE_TIME_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(result))
