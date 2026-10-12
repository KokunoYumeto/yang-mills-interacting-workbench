"""Reproducible diagnostics; auxiliary densities are not Yang--Mills data."""
from pathlib import Path
import json,math
import numpy as np
from scipy.special import roots_jacobi
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent
rng=np.random.default_rng(61012009);checks=[]
def eq(name,l,r):
    err=float(np.max(np.abs(np.asarray(l)-np.asarray(r))))
    scale=max(1.,float(np.max(np.abs(l))),float(np.max(np.abs(r))))
    ok=err<=3e-10*scale
    checks.append(dict(name=name,passed=bool(ok),absolute_error=err));assert ok,checks[-1]
def le(name,l,r):
    ok=bool(l<=r+3e-10*max(1.,abs(l),abs(r)))
    checks.append(dict(name=name,passed=ok,lhs=float(l),rhs=float(r)));assert ok,checks[-1]

# Coupled radius-two S3 x S3 with the exact ground psi proportional to exp(w).
# Its potential is V=kappa*(Delta w+|dw|^2); it is an auxiliary model.
x,wq=roots_jacobi(192,.5,.5)
xx=x[:,None];yy=x[None,:];gx=(1-xx*xx)/4;gy=(1-yy*yy)/4
for trial,(t1,t2,eps) in enumerate([(1,2,.2),(3,4,1),(8,6,2),(15,9,-3)]):
    w=t1*xx+t2*yy+eps*xx*yy
    prob=wq[:,None]*wq[None,:]*np.exp(2*(w-w.max()));prob/=prob.sum()
    mu=lambda f:float(np.sum(prob*f))
    A=t1+eps*yy;B=t2+eps*xx
    G1=A*A*gx;G2=B*B*gy
    G1x=-A*A*xx/2;G1y=2*eps*A*gx
    G2x=2*eps*B*gy;G2y=-B*B*yy/2
    R1=3*A*A*xx*xx/16+eps*eps*gx*gy
    R2=3*B*B*yy*yy/16+eps*eps*gx*gy
    for kappa in [.4,1.3,2.]:
        Fx=kappa*(-.75*(t1+2*eps*yy)-A*A*xx/2+2*eps*B*gy)
        Fy=kappa*(-.75*(t2+2*eps*xx)-B*B*yy/2+2*eps*A*gx)
        lap1V=kappa*gx*(-A*A/2+2*eps*eps*gy)-.75*xx*Fx
        lap2V=kappa*gy*(-B*B/2+2*eps*eps*gx)-.75*yy*Fy
        DG1=gx*(-A*A/2)-.75*xx*G1x+gy*(2*eps*eps*gx)-.75*yy*G1y+2*(A*gx*G1x+B*gy*G1y)
        DG2=gx*(2*eps*eps*gy)-.75*xx*G2x+gy*(-B*B/2)-.75*yy*G2y+2*(A*gx*G2x+B*gy*G2y)
        for e,G,R,DG,F,grad,lapV,ge,metric in [
            (1,G1,R1,DG1,Fx,(G1x,G1y),lap1V,A,gx),
            (2,G2,R2,DG2,Fy,(G2x,G2y),lap2V,B,gy)]:
            key=f'{trial}/{kappa}/{e}'
            eq('full pointwise Bochner '+key,DG,2*R+G+2*ge*F*metric/kappa)
            K=lapV-kappa*(2*R+G)
            eq('centered density mean '+key,mu(K),0)
            for u1,u2,u3 in [(1,1,0),(1,-2,.4),(-.3,.8,-.6)]:
                raw=u1*xx+u2*yy+u3*xx*yy;X=raw-mu(raw)
                Xx=u1+u3*yy;Xy=u2+u3*xx
                lapX=-.75*(u1*xx+u2*yy+2*u3*xx*yy)
                L0X=-kappa*(lapX+2*(A*gx*Xx+B*gy*Xy))
                force=mu(F*(Xx if e==1 else Xy)*metric)
                cov=mu(G*L0X)-mu(G)*mu(L0X)
                eq('self-adjoint covariance '+key+str(u1),cov,-kappa*mu(X*DG))
                eq('force plus centered density '+key+str(u1),cov,force+mu(X*K))
                for a,z in [(.01,.4),(.002,.03)]:
                    be=a*a*mu(ge*(Xx if e==1 else Xy)*metric)
                    direct=-a*a*(force+kappa*mu(grad[0]*Xx*gx+grad[1]*Xy*gy))+z*be
                    eq('doubled force source '+key+str((u1,a)),direct,-a*a*(2*force+mu(X*K))+z*be)

# Four original SU(2) face-gradient norms, with arbitrary directions and weights.
for trial in range(60):
    D=4*rng.random((31,4))
    directions=rng.normal(size=(31,4,3));directions/=np.linalg.norm(directions,axis=2)[:,:,None]
    deriv=directions*np.sqrt(D-D*D/4)[:,:,None]
    weights=rng.random(31);weights/=weights.sum()
    a=10**rng.uniform(-4,-1);kappa=rng.uniform(.3,3);b=1/(kappa*a*a)
    u=rng.uniform(-2,2,4);Mf=2
    force=b*deriv.sum(axis=1);dx=a*np.einsum('p,spk->sk',u,deriv)
    we=float(weights@D.sum(axis=1))
    mf=float(weights@np.sum(force*force,axis=1))
    mx=float(weights@np.sum(dx*dx,axis=1))
    cross=float(weights@np.sum(force*dx,axis=1))
    le(f'four-face force {trial}',mf,4*b*b*we)
    le(f'original observable gradient {trial}',mx,4*a*a*Mf*Mf*we)
    le(f'force contraction {trial}',abs(cross),4*a*b*Mf*we)

# Mixture identities on a finite probability space; not a model of the vacuum.
for trial in range(30):
    mu=rng.random(20);mu/=mu.sum()
    parts=rng.random((3,20));means=parts@mu
    omega=rng.random(3);omega/=omega.sum()
    probs=parts*mu[None,:]/means[:,None]
    nu=omega@probs
    eq(f'positive mixture mass {trial}',nu.sum(),1)
    le(f'mixture total variation {trial}',.5*np.abs(nu-probs[0]).sum(),omega[1]+omega[2])
    X=rng.normal(size=20);X-=mu@X
    le(f'original observable mixture cost {trial}',abs(nu@X-probs[0]@X),2*abs(X).max()*(omega[1]+omega[2]))

# Individual-face integration under an actual curved positive comparison density.
for t in [.1,.7,2,5,11,23,40]:
    prob=wq*np.exp(2*t*(x-1));prob/=prob.sum()
    dd=2-2*x;dp=prob@dd;Te=prob@(t*t*(1-x*x)/4)
    eq(f'original single-face force score {t}',prob@(-t*(1-x*x)/2),-3*(2-dp)/8)
    lam=.8*3/Te
    ell=24*lam/(12*lam+64+math.sqrt((12*lam+64)**2-144*lam*lam))
    le(f'face floor from score ceiling {t}',ell,dp)

# Original finite budgets, asymptotic constants and complementary Gram identity.
for kappa in [.2,1,3]:
    for R in [.1,1,20,100]:
        LR=9*kappa*R**3+24*R**2
        KR=(LR+math.sqrt(LR*LR-81*kappa*kappa*R**6/4))/2
        r=9*kappa*R**3/16
        Kkin=min(KR,LR-r)
        eq(f'kinetic threshold expansion {kappa}/{R}',r*(LR-r)-81*kappa*kappa*R**6/16,
            81*kappa*R**5/256*(128/3-kappa*R))
        assert (Kkin<KR)==(kappa*R<128/3)
        checks.append(dict(name=f'strict kinetic improvement {kappa}/{R}',passed=True))
        for j in [1,10,1000]:
            a=1/(100*j);b=1/(kappa*a*a);q=math.ceil(R/a)+3
            N=3*q*(q+1)**2;M=3*q*q*(q+1);cross=12*q*(q+1)
            Lam=min(2*M,3*kappa*a*math.sqrt(N*M))+2*cross
            AA=9+64*b/kappa;BB=36*M+64*(b/kappa)*Lam
            discr=BB*BB-144*AA*M*M
            lower=72*M*M/(BB+math.sqrt(discr))
            upper=(BB+math.sqrt(discr))/(2*AA)
            ell=24*kappa*a/(12*kappa*a+64+math.sqrt((12*kappa*a+64)**2-144*kappa*kappa*a*a))
            sharp=max(lower,M*ell)
            le(f'consistent finite sharp root {kappa}/{R}/{j}',sharp,upper)
            le(f'positive finite kinetic remainder {kappa}/{R}/{j}',sharp,Lam)
for trial in range(40):
    C=rng.normal(size=(24,8));D=np.diag(np.geomspace(.2,30,24))
    A=D@C;Z=A.T@A;v=rng.normal(size=24);k=A.T@v
    n=3;ZA=Z[:n,:n];ZB=Z[:n,n:];ZD=Z[n:,n:]
    S=ZD-ZB.T@np.linalg.solve(ZA,ZB)
    corrected=k[n:]-ZB.T@np.linalg.solve(ZA,k[:n])
    eq(f'complete source Schur receiver {trial}',k@np.linalg.solve(Z,k),
       k[:n]@np.linalg.solve(ZA,k[:n])+corrected@np.linalg.solve(S,corrected))
    le(f'positive omitted block {trial}',0,np.linalg.eigvalsh(S)[0])

out=dict(checks=len(checks),all_passed=True,scope='Exact curved positive comparison densities check full Bochner, covariance and doubled-force identities. Finite group-gradient arrays check the original four-face constants. Positive mixtures, complete Gram matrices and the original finite budget constants check the stated maps and estimates. Auxiliary data are not original Yang-Mills vacuum or spectral values.',results=checks)
(O/'CENTERED_CURRENT_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')

plt.rcParams.update({'font.size':11,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(14,8));ax.set_xlim(0,14);ax.set_ylim(0,8);ax.axis('off')
def box(x,y,w,h,title,body,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',facecolor=color,edgecolor='#334155'))
    ax.text(x+.15,y+h-.28,title,weight='bold',va='top',fontsize=13)
    ax.text(x+.15,y+h-.76,body,va='top',linespacing=1.55,fontsize=11)
box(.2,4.7,4.1,2.6,'Original finite regulator',
    r'$\mu=\psi^2dU,\quad R_e=\sum_r\|H_{er}\|_{\rm HS}^2$'+'\n'+
    r'$G_e=|d_ew|^2,\quad W_e=\sum_{p\ni e}D_p$'+'\n'+
    r'$\mathcal{A}_e=\kappa(2R_e+G_e)+3bW_e/4$'+'\n'+r'$\mu\mathcal{A}_e=6b$  [CFC6–9]','#e0f2fe')
box(5.,4.7,8.4,2.6,'Exact positive mixture [CFC9–12]',
    r'$d\nu_e=(\mathcal{A}_e/6b)d\mu=\omega_e^R d\nu_e^R+\omega_e^G d\nu_e^G+\omega_e^D d\nu_e^D$'+'\n'+
    r'$\omega_e^R=\kappa\mu R_e/(3b),\quad\omega_e^G=\kappa T_e/(6b),\quad\omega_e^D=w_e/8$'+'\n'+
    r'$\omega_e^R+\omega_e^G+\omega_e^D=1,\qquad \omega_e^R,\omega_e^G,\omega_e^D>0$'+'\n'+
    'Finite configuration measures; no continuum vacuum identification.','#dcfce7')
box(.2,.9,6.25,2.8,'Source-carrying links [CFC14–20]',
    r'$I(C)=\{e:w_e\leq Ca\},\quad C=\max\{\kappa,64M_f^2K_R/J_t\}$'+'\n'+
    r'$\liminf a^{-3}\|\mathsf{b}_{I(C)}\|^2\geq27J_t/16$'+'\n'+
    r'$a^2\mu R_e\longrightarrow3/\kappa^2$ uniformly on this set'+'\n'+
    'Exponential score tails hold under both '+r'$\nu_e$ and $\nu_e^R$.'+'\n'+
    'Every omitted source and Gram block remains.','#fef3c7')
box(7.05,.9,6.35,2.8,'Exact physical receiver [CFC12, CFC21]',
    r'$k_e=(6/\kappa)(\nu_eX-\mu X)-2a^2\mu(F_e\cdot d_eX)+z\mathsf{b}_e$'+'\n'+
    'The force term appears twice.'+'\n'+
    r'$\|r\|^2=E_X/\kappa-k^*\mathsf{Z}^{-1}k$'+'\n'+
    'The full source, Gram matrix and residual are still required.'+'\n'+
    'Total variation alone does not control the growing original X.','#ffe4e6')
ax.annotate('',xy=(4.9,6),xytext=(4.45,6),arrowprops=dict(arrowstyle='->',lw=2))
ax.text(.25,7.75,'Positive current measures with the complete original source',fontsize=18,weight='bold')
ax.text(.25,.25,'Exact maps and proved bounds. Every Hessian row and original coupling is retained; this is not a numerical vacuum sample.',fontsize=10)
fig.savefig(O/'CENTERED_CURRENT_MAP.png',dpi=160,bbox_inches='tight');fig.savefig(O/'CENTERED_CURRENT_MAP.svg',bbox_inches='tight');plt.close(fig)

fig,axes=plt.subplots(1,2,figsize=(13,5.5))
av=np.geomspace(1e-5,.1,250);kap=1
ell=24*kap*av/(12*kap*av+64+np.sqrt((12*kap*av+64)**2-144*kap*kap*av*av))
axes[0].semilogx(av,ell/av,label=r'Exact $\ell(a)/a$')
axes[0].axhline(3/16,color='#be123c',ls='--',label=r'Limit $3\kappa_*/16$')
axes[0].set(xlabel='Original lattice spacing a',ylabel='Proved individual-face lower coefficient',title=r'CFC22: every face, $\kappa_*=1$')
axes[0].legend()
rv=np.geomspace(.05,100,300);LR=9*rv**3+24*rv**2;KR=(LR+np.sqrt(LR*LR-81*rv**6/4))/2
kin=np.minimum(KR,LR-9*rv**3/16)
axes[1].semilogx(rv,1-kin/KR,color='#047857')
axes[1].axvline(128/3,color='#be123c',ls='--',label=r'Threshold $\kappa_*R=128/3$')
axes[1].set(xlabel='Support cube side R',ylabel=r'Relative improvement $1-K_R^{\rm kin}/K_R$',title=r'CFC23–26: kinetic ceiling, $\kappa_*=1$')
axes[1].legend()
for ax in axes:ax.grid(alpha=.2)
fig.suptitle('Individual plaquette means strengthen the original spatial and kinetic bounds',fontsize=15)
fig.text(.5,.015,'Plots of proved bounds at an explicitly illustrative parameter; no sampled vacuum values or change of units.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.04,1,.94))
fig.savefig(O/'PLAQUETTE_FLOOR_AND_KINETIC.png',dpi=160);fig.savefig(O/'PLAQUETTE_FLOOR_AND_KINETIC.svg');plt.close(fig)
print(json.dumps(dict(checks=len(checks),all_passed=True,figures=2)))
