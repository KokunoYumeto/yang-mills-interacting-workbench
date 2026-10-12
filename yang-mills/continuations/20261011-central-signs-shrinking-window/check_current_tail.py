from pathlib import Path
import math,json
import numpy as np
from scipy.special import roots_jacobi
O=Path(__file__).resolve().parent
x,wq=roots_jacobi(256,.5,.5)
xx=x[:,None];yy=x[None,:];gx=(1-xx*xx)/4;gy=(1-yy*yy)/4
checks=[]
def eq(name,lhs,rhs,scale=None):
    scale=max(1,abs(lhs),abs(rhs)) if scale is None else scale
    ok=abs(lhs-rhs)<=5e-10*scale
    checks.append(dict(name=name,passed=bool(ok),lhs=float(lhs),rhs=float(rhs),scale=float(scale)))
    assert ok,checks[-1]
def le(name,lhs,rhs):
    ok=lhs<=rhs+5e-10*max(abs(lhs),abs(rhs),1e-200)
    checks.append(dict(name=name,passed=bool(ok),lhs=float(lhs),rhs=float(rhs)))
    assert ok,checks[-1]
for t1,t2,eps in [(1.,2.,.2),(3.,4.,1.),(8.,6.,2.),(15.,9.,-3.),(.5,1.,-.1)]:
    w=t1*xx+t2*yy+eps*xx*yy
    pr=wq[:,None]*wq[None,:]*np.exp(2*(w-w.max()));pr/=pr.sum()
    mu=lambda v:float(np.sum(pr*v))
    A=t1+eps*yy;B=t2+eps*xx
    G1=A*A*gx;G2=B*B*gy
    G1x=-A*A*xx/2;G1y=2*eps*A*gx
    G2x=2*eps*B*gy;G2y=-B*B*yy/2
    R1=3*A*A*xx*xx/16+eps*eps*gx*gy
    R2=3*B*B*yy*yy/16+eps*eps*gx*gy
    Fx=-.75*(t1+2*eps*yy)-A*A*xx/2+2*eps*B*gy
    Fy=-.75*(t2+2*eps*xx)-B*B*yy/2+2*eps*A*gx
    Fxx=-A*A/2+2*eps*eps*gy;Fyy=-B*B/2+2*eps*eps*gx
    C=(max(abs(t1),abs(t2))+2*abs(eps))/4;a=2/C
    normdG1=G1x*G1x*gx+G1y*G1y*gy;force2=mu(Fx*Fx*gx)
    for t in [.03,.08,.13,.18,.23]:
        r=t*a;exp=np.exp(r*G1)
        lhs=mu(exp*(r*normdG1+2*R1+G1))
        rhs=-2*mu(exp*A*Fx*gx)
        eq(f'exponential full identity {t1} {t}',lhs,rhs)
        upper=2*math.sqrt(3)/math.sqrt(a)*(1-4*t)**(-1.25)*math.sqrt(force2)
        le(f'exponential full bound {t1} {t}',lhs,upper)
        le(f'exponential derivative bound {t1} {t}',mu(exp*normdG1),upper/r)
        le(f'weighted moment comparison {t1} {t}',mu(G1*np.exp(2*r*G1)),3/a*(1-4*t)**(-2.5))
        refined=2*(1-4*t)**(-1.25)*math.sqrt(mu(G1)*force2)
        le(f'refined exponential full bound {t1} {t}',lhs,refined)
        le(f'refined exponential derivative bound {t1} {t}',mu(exp*normdG1),refined/r)
        le(f'refined weighted first moment {t1} {t}',mu(G1*np.exp(2*r*G1)),mu(G1)*(1-4*t)**(-2.5))
        le(f'refined exponential moment {t1} {t}',mu(exp),1+a*mu(G1)/3*((1-2*t)**(-1.5)-1))
        for threshold in [1.,4.,12.]:
            mask=G1>threshold/a
            le(f'actual score tail {t1} {t} {threshold}',mu(mask*G1),math.exp(-t*threshold)*mu(G1)*(1-2*t)**(-2.5))
            le(f'full derivative tail {t1} {t} {threshold}',mu(mask*normdG1),math.exp(-t*threshold)*refined/r)
    for h1,h2 in [(1.,1.),(1.,-2.),(-.3,.8)]:
        Gh=h1*G1+h2*G2;Rh=h1*R1+h2*R2
        Jh=h1*A*Fx*gx+h2*B*Fy*gy
        Ghx=h1*G1x+h2*G2x;Ghy=h1*G1y+h2*G2y
        DeltaV=h1*(gx*Fxx-.75*xx*Fx)+h2*(gy*Fyy-.75*yy*Fy)
        lhs=mu(Ghx*Ghx*gx+Ghy*Ghy*gy)
        terms=[-2*mu(Gh*Rh),-mu(Gh*Gh),-2*mu(Gh*Jh)]
        eq(f'signed derivative identity {t1} {h1} {h2}',lhs,sum(terms),max(1,abs(lhs),sum(abs(v) for v in terms)))
        exact=mu((h1*Fx+Ghx)**2*gx+(h2*Fy+Ghy)**2*gy)
        terms=[mu(h1*h1*Fx*Fx*gx+h2*h2*Fy*Fy*gy),-2*mu(Gh*DeltaV),-6*mu(Gh*Jh),-2*mu(Gh*Rh),-mu(Gh*Gh)]
        eq(f'full directional second energy {t1} {h1} {h2}',exact,sum(terms),max(1,abs(exact),sum(abs(v) for v in terms)))

# Algebraic finite-dimensional diagnostics do not supply Yang-Mills matrix values.
rng=np.random.default_rng(621006)
for trial in range(16):
    columns=rng.normal(size=(40,8))+1j*rng.normal(size=(40,8))
    masks=rng.random((40,8))>.2
    cut=columns*masks;error=columns-cut;Z=columns.conj().T@columns
    Zcut=cut.conj().T@cut
    explicit=columns.conj().T@error+error.conj().T@columns-error.conj().T@error
    eq(f'full noncommuting Gram identity {trial}',np.linalg.norm(Z-Zcut-explicit),0)
    eh=np.linalg.norm(error);gram_error=np.linalg.norm(Z-Zcut,2)
    le(f'raw coefficient Gram norm bound {trial}',gram_error,(2*math.sqrt(np.trace(Z).real)+eh)*eh)
    src=rng.normal(size=8)+1j*rng.normal(size=8)
    A=Z[:5,:5];B=Z[:5,5:];D=Z[5:,5:];p=src[:5];q=src[5:]
    S=D-B.conj().T@np.linalg.solve(A,B);qcorrect=q-B.conj().T@np.linalg.solve(A,p)
    exact=np.vdot(src,np.linalg.solve(Z,src)).real
    retained=np.vdot(p,np.linalg.solve(A,p)).real
    schur=np.vdot(qcorrect,np.linalg.solve(S,qcorrect)).real
    eq(f'complete finite Schur source {trial}',exact,retained+schur)
    le(f'positive Schur matrix {trial}',0,float(np.linalg.eigvalsh(S)[0]))
    beta=rng.normal(size=40)+1j*rng.normal(size=40)
    paired=columns.conj().T@beta
    residual=beta-columns@np.linalg.solve(Z,paired)
    eq(f'complete projection residual {trial}',np.vdot(beta,beta).real,np.vdot(paired,np.linalg.solve(Z,paired)).real+np.vdot(residual,residual).real)
    # Actual positive energy Gram and its exact Bessel residual.
    basis=np.linalg.qr(rng.normal(size=(40,8)))[0]
    norm=np.exp(rng.uniform(-5,1,8))
    alpha=basis*np.sqrt(norm);v=rng.normal(size=(40,3))
    Bsrc=alpha.T@v;energy=v.T@v
    res=v-basis@(basis.T@v)
    eq(f'energy matrix Bessel identity {trial}',np.linalg.norm(energy-Bsrc.T@np.diag(1/norm)@Bsrc-res.T@res),0)
    le(f'energy matrix lower order {trial}',-1e-11,float(np.linalg.eigvalsh(energy-Bsrc.T@Bsrc/norm.max())[0]))
    # A genuinely close masked-column example is unnecessary for the inverse identity.
    perturb=rng.normal(size=(5,5))+1j*rng.normal(size=(5,5));perturb=(perturb+perturb.conj().T)/2
    gamma=float(np.linalg.eigvalsh(A)[0]);perturb*=gamma/(4*np.linalg.norm(perturb,2))
    Acut=A+perturb;eta=np.linalg.norm(perturb,2)
    le(f'quantitative inverse bound {trial}',abs(np.vdot(p,np.linalg.solve(A,p)-np.linalg.solve(Acut,p))),np.vdot(p,p).real*eta/(gamma*(gamma-eta)))
eq('different masks need not preserve Gram order',np.linalg.det(np.array([[0.,1.],[1.,1.]])),-1)

import mpmath as mp
mp.mp.dps=70
for k in [mp.mpf('0.3'),mp.mpf('1'),mp.mpf('2')]:
    for j in [1,10,1000]:
        a=1/(mp.mpf(100)*j);sel=a*mp.log(1/a)
        tau=9*(8-sel)**2/(256*sel)
        m=mp.mpf(4)
        root=24*k*a*m/(12*k*a+64+mp.sqrt((12*k*a+64)**2-144*k*k*a*a))
        eq(f'exact incident-deficit lower root {k} {j}',float(3*k*a*(2*m-root)**2),float(64*m*root))
        q=mp.ceil(1/a)+3;n=3*q*(q-1)**2;N=3*q*(q+1)**2;M=3*q*q*(q+1);C=12*q*(q+1)
        budget=min(2*M,3*k*a*mp.sqrt(N*M))+2*C;d=mp.mpf('.4')*budget
        b=1/(k*a*a);T=min(3*n/(k*a),b*(budget-d)/k);t=mp.mpf('.125')
        ft=16*b*b*(n+k*a*T/3*((1-2*t)**(-mp.mpf('1.5'))-1))
        gt=T*(1-2*t)**(-mp.mpf('2.5'))
        ht=8*b/(t*k*k*a)*(1-4*t)**(-mp.mpf('1.25'))*mp.sqrt(T*d)
        for theta in [mp.mpf('.25'),mp.mpf(1),mp.mpf(4)]:
            z=theta*100*k*a;gamma=z*z*a**4*tau
            uz=(4*mp.sqrt(d)+mp.sqrt(8*mp.sqrt(35))*(d*(budget-d))**mp.mpf('.25'))**2/(k*k)
            uz+=2*z*(3*a*a*n/k+4*a*(budget-d)/(k*k))+z*z*a*a*(budget-d)/(k*k)
            bt=a*a*(mp.sqrt(ft)+k*mp.sqrt(ht)+z*mp.sqrt(gt))
            bb=9*a**6*n;tol=mp.mpf('.001')
            eta_star=min(gamma/2,tol*gamma*gamma/(2*z*k*bb))
            e_star=min(1,eta_star/(2*mp.sqrt(uz)+1))
            Rstar=2/t*mp.log(max(1,bt/e_star))
            er=bt*mp.exp(-t*Rstar/2);eta=(2*mp.sqrt(uz)+er)*er
            le(f'finite cutoff yields requested Gram error {k} {j} {theta}',float(eta),float(eta_star))
            le(f'finite cutoff yields inverse tolerance {k} {j} {theta}',float(z*k*bb*eta/(gamma*(gamma-eta))),float(tol))
            le(f'finite retained Gram invertibility {k} {j} {theta}',float(eta),float(gamma/2))

for k in [.3,1.,2.]:
    for R in [.25,1.,4.,16.,64.]:
        L=9*k*R**3+24*R**2;K=(L+math.sqrt(L*L-81*k*k*R**6/4))/2
        old=81*k**3*R**6/(64*K);new=k*k*R**3/3
        eq(f'tent exact ratio {k} {R}',new/old,64*K/(243*k*R**3))
        le(f'tent strict improvement {k} {R}',(32+16*math.sqrt(3))/27,new/old)
        # Integrals directly from the original piecewise linear factors.
        xx,ww=np.polynomial.legendre.leggauss(16)
        i1=R/2*float(np.dot(ww,1-(xx+1)/2))
        i2=R/2*float(np.dot(ww,(1-(xx+1)/2)**2))
        eq(f'original tent first integral {k} {R}',i1**3,R**3/8)
        eq(f'original tent second integral {k} {R}',i2**3,R**3/27)
for trial in range(12):
    fs=rng.normal(size=(3,50));ts=np.stack([fs[0]+fs[1],fs[0]+fs[2],fs[1]+fs[2]])
    eq(f'orientation cross terms retained {trial}',float(np.sum(ts*ts)),float(np.sum(fs*fs)+np.sum(np.sum(fs,axis=0)**2)))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.size':11,'svg.fonttype':'none'})
R=np.geomspace(.25,64,250);k=1.
L=9*k*R**3+24*R**2;K=(L+np.sqrt(L*L-81*k*k*R**6/4))/2
old=81*k**3*R**6/(64*K);new=k*k*R**3/3
fig,axes=plt.subplots(1,2,figsize=(12,4.7),layout='constrained')
axes[0].loglog(R,old,label='Earlier lower bound')
axes[0].loglog(R,new,label='CTI21–CTI26 lower bound',lw=2)
axes[0].set(xlabel='Original tent side R',ylabel='Lower bound on source energy',title=r'Original tent, all three orientations; $\kappa_*=1$')
axes[0].legend();axes[0].grid(alpha=.2)
axes[1].semilogx(R,new/old,lw=2,label='Ratio of proved lower bounds')
axes[1].axhline((32+16*math.sqrt(3))/27,color='#777777',ls='--',label=r'$(32+16\sqrt{3})/27$')
axes[1].set(xlabel='Original tent side R',ylabel='Ratio',title='The original energy and filter scales remain')
axes[1].legend();axes[1].grid(alpha=.2)
fig.suptitle('Stronger energy estimate for the unchanged Wilson source',fontsize=15)
for ext in ['png','svg']:fig.savefig(O/f'RETAINED_SOURCE_ENERGY.{ext}',dpi=180)
plt.close(fig)
fig,ax=plt.subplots(figsize=(12,7));ax.set(xlim=(0,12),ylim=(0,7));ax.axis('off')
def box(x,y,width,height,text,color):
    ax.add_patch(FancyBboxPatch((x,y),width,height,boxstyle='round,pad=0.08',facecolor=color,edgecolor='#345065',lw=1.2))
    ax.text(x+width/2,y+height/2,text,ha='center',va='center',fontsize=11)
box(.3,5.25,11.4,1.15,r'Original full filter: $\mathcal{W}(z)=z\kappa\|(\mathscr{L}_1+z)^{-1}dh\|_\mu^2$'+'\nSame state, shift, source and metric throughout · CTI7, CTI33','#e0eef6')
for x in [2.,6.,10.]:
    ax.annotate('',xy=(x,4.5),xytext=(6,5.15),arrowprops=dict(arrowstyle='->',color='#345065'))
box(.2,2.7,3.55,1.75,'Retained trial term\n'+r'$z\kappa\,p^*A^{-1}p$'+'\nProved lower matrix bound\nExplicit inverse tolerance\nCTI27–CTI31, CTI34–CTI37','#e1f2e5')
box(4.2,2.7,3.55,1.75,'Omitted finite directions\n'+r'$z\kappa\,q_{\rm corr}^*S^{-1}q_{\rm corr}$'+'\n'+r'$q_{\rm corr}=q-B^*A^{-1}p$'+'\nComplete Schur contribution\nCTI32','#fff0d4')
box(8.2,2.7,3.55,1.75,'Full physical residual\n'+r'$z\kappa\|\beta-A_{z,I}Z_I^{-1}b\|_\mu^2$'+'\nExact + nonexact components\nBoth retained\nCTI33, FTC31','#f4e7f3')
box(.3,.35,11.4,1.35,'The three nonnegative terms add exactly at each shift.\nThe shrinking-window expression subtracts contributions at two other shifts.\nIt requires the signed values of all three terms; inverse accuracy alone does not evaluate them.\nExact source formulas: CTI39 · Three-shift window: PLF25–PLF26','#f1f3f5')
ax.set_title('How the retained matrix maps to the original physical filter',fontsize=16,pad=12)
fig.tight_layout()
for ext in ['png','svg']:fig.savefig(O/f'RETAINED_SOURCE_FULL_FILTER.{ext}',dpi=180)
plt.close(fig)
out=dict(checks=len(checks),all_passed=True,scope='Coupled radius-two sphere densities verify exponential and signed derivative identities, including refined first-moment bounds. Finite-dimensional matrices check Gram, Bessel, Schur, inverse and full residual formulas. Original regulator constants and tent integrals are evaluated independently. These diagnostics do not supply original Yang-Mills vacuum or spectral values.',results=checks)
(O/'CURRENT_TAIL_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=len(checks),all_passed=True,figures=2)))
