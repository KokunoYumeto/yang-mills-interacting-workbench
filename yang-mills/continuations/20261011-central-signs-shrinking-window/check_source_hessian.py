from pathlib import Path
import json,math
import numpy as np
O=Path(__file__).resolve().parent
rng=np.random.default_rng(61012007);checks=[]
def eq(name,x,y):
    ok=abs(x-y)<=2e-10*max(1,abs(x),abs(y))
    checks.append(dict(name=name,passed=bool(ok),lhs=float(x),rhs=float(y)));assert ok,checks[-1]
def le(name,x,y):
    ok=x<=y+2e-10*max(1,abs(x),abs(y))
    checks.append(dict(name=name,passed=bool(ok),lhs=float(x),rhs=float(y)));assert ok,checks[-1]
# Exact actual cubical incidence. Samples are arbitrary face deficits, not vacuum data.
vertices=range(4);edges=[];faces=[]
for z in np.ndindex(4,4,4):
    for d in range(3):
        if z[d]<3:edges.append((z,d))
ei={v:i for i,v in enumerate(edges)}
for z in np.ndindex(4,4,4):
    for d in range(3):
        for k in range(d+1,3):
            if z[d]<3 and z[k]<3:
                zd=list(z);zd[d]+=1;zk=list(z);zk[k]+=1
                faces.append([ei[(z,d)],ei[(tuple(zd),k)],ei[(tuple(zk),d)],ei[(z,k)]])
inc=np.zeros((len(edges),len(faces)))
for p,ee in enumerate(faces):inc[ee,p]=1
assert np.max(inc.sum(axis=1))==4 and np.all(inc.sum(axis=0)==4)
for trial in range(48):
    a=10**rng.uniform(-4,-1);u=rng.normal(size=len(faces));d=rng.uniform(0,4,len(faces))
    # Retain an explicit removed star.
    e0=int(rng.integers(len(edges)));u[inc[e0]>0]=0
    M=np.max(abs(u));A=inc@u;B=inc@(u*d);S=inc@(u*(2-d))
    exact=a*a*(3/16*np.dot(S,S)+np.dot(u*u,6+.75*(2-d)**2))
    full=a*a*(.75*np.dot(A,A)+9*np.dot(u,u)-.75*np.dot(A,B)+3/16*np.dot(B,B)-3*np.dot(u*u,d)+.75*np.dot(u*u,d*d))
    eq(f'complete source Hessian expansion {trial}',exact,full)
    leading=a*a*(.75*np.dot(A,A)+9*np.dot(u,u))
    le(f'full finite Hessian error {trial}',abs(a*(exact-leading)),15*a**3*M*M*np.sum(d))
    v=rng.normal(size=len(faces));v[inc[e0]>0]=0
    Av=inc@v;Sv=inc@(v*(2-d));Mv=np.max(abs(v))
    cross=a*a*(3/16*np.dot(S,Sv)+np.dot(u*v,6+.75*(2-d)**2))
    crossleading=a*a*(.75*np.dot(A,Av)+9*np.dot(u,v))
    le(f'full bilinear Hessian error {trial}',abs(a*(cross-crossleading)),15*a**3*M*Mv*np.sum(d))
    c=rng.uniform(0,10);dd=rng.uniform(.1,10);E=rng.uniform(.1,10)
    delta=1e-5
    fd=((E+delta)**3/(c+dd*(E+delta))**2-(E-delta)**3/(c+dd*(E-delta))**2)/(2*delta)
    deriv=E*E*(3*c+dd*E)/(c+dd*E)**3
    eq(f'full energy denominator derivative {trial}',fd,deriv)
for k in [.3,1.,2.]:
    for R in [.25,1.,4.]:
        Jt=4*R**3/9;J2=R**3/9;e=k*k*R**3/3
        for theta in [.25,1.,4.]:
            coeff=100*theta*k*e**3/(k*k*(3*Jt+9*J2)+4*e)**2
            eq(f'full original tent filter constant {k} {R} {theta}',coeff,100*theta*k**3*R**3/363)

# Independent SU(2) mixed-block calculation in the original radius-two metric.
sigmas=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)]
generators=[-1j*v/2 for v in sigmas]
def product(mm):
    out=np.eye(2,dtype=complex)
    for m in mm:out=out@m
    return out
for trial in range(20):
    links=[]
    for _ in range(4):
        q=rng.normal(size=4);q=q/np.linalg.norm(q)
        links.append(q[0]*np.eye(2)-1j*sum(q[k+1]*sigmas[k] for k in range(3)))
    factors=[links[0],links[1],links[2].conj().T,links[3].conj().T]
    Wtrace=np.trace(product(factors)).real
    total=4*3*Wtrace*Wtrace/16
    for i in range(4):
        for j in range(4):
            if i==j:continue
            block=0.
            for Ta in generators:
                for Tb in generators:
                    mm=list(factors)
                    mm[i]=Ta@factors[i] if i<2 else -factors[i]@Ta
                    mm[j]=Tb@factors[j] if j<2 else -factors[j]@Tb
                    val=-np.trace(product(mm))
                    le(f'original mixed block real {trial} {i} {j}',abs(val.imag),1e-12)
                    block+=val.real**2
            eq(f'original mixed block norm {trial} {i} {j}',block,.5+Wtrace*Wtrace/16)
            total+=block
    eq(f'original one-face full Hessian {trial}',total,6+1.5*Wtrace*Wtrace)

for trial in range(20):
    k=rng.uniform(.2,3);z=10**rng.uniform(-4,1)
    lam=np.geomspace(1e-6,1e6,24)
    eta_h=rng.normal(size=24)+1j*rng.normal(size=24)
    eta_q=rng.normal(size=24)+1j*rng.normal(size=24)
    eta_F=eta_h+eta_q
    beta=lambda eta,z:np.sqrt(lam/k)*eta/(lam+z)
    Wfun=lambda eta,z:float(np.sum(z*lam*abs(eta)**2/(lam+z)**2))
    bh,bq=beta(eta_h,z),beta(eta_q,z)
    exact=Wfun(eta_F,z)
    rhs=Wfun(eta_h,z)+2*z*k*np.vdot(bh,bq).real+z*k*np.vdot(bq,bq).real
    eq(f'full original source correction {trial}',exact,rhs)
    v=np.sqrt(lam/k)*eta_F;E=k*np.vdot(v,v).real
    # An additional nonnegative form term checks inverse order and both Cauchy factors.
    tdiag=lam+z+rng.uniform(0,5,24)
    denom=k*np.sum(tdiag*abs(v)**2)
    le(f'full filtered lower inequality {trial}',z*E**3/denom**2,exact)
    lo=.1;hi=20.;clo=4*lo/(1+lo)**2;chi=4*hi/(1+hi)**2
    C=exact-clo*Wfun(eta_F,lo*z)-chi*Wfun(eta_F,hi*z)
    mass=np.sum(abs(eta_F[(lam>=lo*z)&(lam<=hi*z)])**2)
    le(f'direct full-source physical window {trial}',4*max(C,0),mass)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.size':11,'svg.fonttype':'none'})
R=np.geomspace(.25,64,300);k=1.;theta=1.
L=9*k*R**3+24*R**2;K=(L+np.sqrt(L*L-81*k*k*R**6/4))/2
eold=81*k**3*R**6/(64*K);enew=k*k*R**3/3
U=16*k*K;D=7*k*k*R**3/3+4*U
co=100*theta*k*eold**3/D**2
cc=100*theta*k*enew**3/D**2
cn=100*theta*k**3*R**3/363
fig,ax=plt.subplots(figsize=(10.5,5.8),layout='constrained')
ax.loglog(R,co,label='FTC12 coefficient')
ax.loglog(R,cc,label='CTI23 coefficient')
ax.loglog(R,cn,label='HSF9 / HSF13 coefficient',lw=2.4)
ax.set(xlabel='Original tent side R',ylabel=r'Proved lower coefficient of $\mathcal{W}(\theta s_j)/a_j^3$',
       title=r'Original three-orientation tent; $\kappa_*=1$, $\theta=1$')
ax.legend();ax.grid(alpha=.2)
fig.suptitle('The complete energy-dependent denominator strengthens the estimate',fontsize=14)
for ext in ['png','svg']:fig.savefig(O/f'SOURCE_HESSIAN_FILTER_BOUNDS.{ext}',dpi=180)
plt.close(fig)

fig,ax=plt.subplots(figsize=(12,7.4));ax.set(xlim=(0,12),ylim=(0,7.4));ax.axis('off')
def box(x,y,w,h,t,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.08',facecolor=color,edgecolor='#35536a'))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=11)
box(.25,5.8,11.5,1.05,'Unchanged original observables: full F and outside h\nSame actual ground state, radius-two metric, coupling and face centres · HSF1, HSF11–HSF13','#e4edf7')
box(.25,3.8,5.45,1.15,r'Same-link Hessian limit: $3J_t$'+'\nAll orientation cross terms retained\nHSF1–HSF5','#e6f3e5')
box(6.3,3.8,5.45,1.15,r'Distinct-link Hessian limit: $9J_2^\Sigma$'+'\nExact full block calculation\nHSF1–HSF5','#e6f3e5')
for x in [3,9]:ax.annotate('',xy=(x,5.03),xytext=(6,5.7),arrowprops=dict(arrowstyle='->'))
box(.25,1.65,11.5,1.25,'Complete finite denominator:\n'+r'$\kappa_*^2 C_j+(4+\kappa_*a_j/2+100\theta\kappa_*a_j^2)E_j$'+'\n'+r'$C_j=a_j\mu_j\|\nabla^2X_j\|^2,\quad E_j=\kappa_*\mu_j|dX_j|^2$'+'\nEnergy dependence is retained before taking the limit · HSF7–HSF9','#fff0d8')
for x in [3,9]:ax.annotate('',xy=(6,2.98),xytext=(x,3.7),arrowprops=dict(arrowstyle='->'))
box(.25,.1,11.5,.9,'Direct full-source response bound → original physical window receiver\nThe signed three-shift value remains unevaluated; all source corrections remain · HSF14–HSF15','#f2e8f4')
ax.annotate('',xy=(6,1.08),xytext=(6,1.55),arrowprops=dict(arrowstyle='->'))
ax.set_title('From the exact source Hessian to the full physical response',fontsize=16)
fig.tight_layout()
for ext in ['png','svg']:fig.savefig(O/f'SOURCE_HESSIAN_FULL_SOURCE_MAP.{ext}',dpi=180)
plt.close(fig)
out=dict(checks=len(checks),all_passed=True,scope='Exact cubical incidence checks the full signed Hessian expansion, bilinear error and finite deficit bound. Independent radius-two SU(2) matrix derivatives check every original one-face Hessian block. Spectral diagnostics check the full-source correction, inverse/Cauchy inequality and direct physical-window receiver. The original tent constants and denominator derivative are checked independently. These are algebraic diagnostics, not original Yang-Mills vacuum values.',results=checks)
(O/'SOURCE_HESSIAN_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=len(checks),all_passed=True,figures=2)))
