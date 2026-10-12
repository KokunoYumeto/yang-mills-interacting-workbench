from pathlib import Path
import json,math
import numpy as np
from scipy.special import roots_jacobi
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

O=Path(__file__).resolve().parent
rows=[]
def check(name,ok,**data):
    rows.append(dict(name=name,passed=bool(ok),**{k:float(v) for k,v in data.items()}))
    assert ok,(name,data)
def close(name,lhs,rhs,tol=2e-10):
    check(name,abs(lhs-rhs)<=tol*max(1,abs(lhs),abs(rhs)),lhs=lhs,rhs=rhs)
def bound(name,lhs,rhs):
    check(name,lhs<=rhs+2e-10*max(1e-250,abs(lhs),abs(rhs)),lhs=lhs,rhs=rhs)

# Radius-two S^3 quadrature; these analytic densities are diagnostics,
# not samples of the original interacting Yang-Mills vacuum.
x,weights=roots_jacobi(256,.5,.5)
gamma=(1-x*x)/4
for t in [.3,1.,3.,10.,30.,60.]:
    prob=weights*np.exp(2*t*(x-1));prob/=prob.sum()
    mean=lambda y:float(prob@y)
    ka=8/t
    G=t*t*gamma
    delta=-3*t*x/4
    Hgg=-t*x*G/4
    for p in range(1,9):
        div=G**(p-1)*delta+2*G**p
        if p>1:div+=2*(p-1)*G**(p-2)*Hgg
        residual=mean(div);scale=max(1,mean(G**p))
        check(f'sphere divergence t{t} p{p}',abs(residual)<=2e-10*scale,residual=residual,comparison_scale=scale)
        bound(f'conditional moment t{t} p{p}',mean(G**p),(2*p+1)/ka*mean(G**(p-1)))
        for lam in [-3.,.5,4.]:
            u2=np.exp(2*lam*x)
            X=mean(u2*G**p);B=mean(u2*G**(p-1));Y=mean(u2*G**(p-1)*lam*lam*gamma)
            bound(f'correlated multiplier t{t} p{p} l{lam}',X,(math.sqrt(Y)+math.sqrt(Y+4*(2*p+1)/ka*B))**2/4)
    for tau in [.02,.1,.25,.4,.49]:
        bound(f'exponential t{t} tau{tau}',mean(np.exp(tau*ka*G)),(1-2*tau)**(-1.5))

# Two genuinely coupled sphere coordinates: all exterior derivatives retained.
xx=x[:,None];yy=x[None,:];gx=(1-xx*xx)/4;gy=(1-yy*yy)/4
for t1,t2,eps in [(1.,2.,.2),(3.,4.,1.),(8.,6.,2.),(15.,9.,-3.),(.5,1.,-.1)]:
    w=t1*xx+t2*yy+eps*xx*yy
    pr=weights[:,None]*weights[None,:]*np.exp(2*(w-w.max()));pr/=pr.sum()
    mu=lambda a:float(np.sum(pr*a))
    A=t1+eps*yy;B=t2+eps*xx
    G1=A*A*gx;G2=B*B*gy
    R1=3*A*A*xx*xx/16+eps*eps*gx*gy
    dG1x=-A*A*xx/2;dG1y=2*eps*A*gx
    normdG1=dG1x*dG1x*gx+dG1y*dG1y*gy
    Fx=-.75*(t1+2*eps*yy)-A*A*xx/2+2*eps*B*gy
    Fy=-.75*(t2+2*eps*xx)-B*B*yy/2+2*eps*A*gx
    exact_left=mu(normdG1+2*G1*R1+G1*G1)
    exact_right=-2*mu(G1*A*Fx*gx)
    close(f'coupled full score identity {t1}',exact_left,exact_right)
    C=(max(abs(t1),abs(t2))+2*abs(eps))/4
    ka=2/C
    bound(f'coupled sixth moment {t1}',mu(G1**3),35/ka**2*mu(G1))
    bound(f'coupled full score bound {t1}',exact_left,2*math.sqrt(35)/ka*math.sqrt(mu(G1)*mu(Fx*Fx*gx)))
    # SOM15 at kappa=1: Pi_1 dV + dG1 retains its second-link part.
    force_plus_grad=(Fx+dG1x)**2*gx+dG1y*dG1y*gy
    expanded=Fx*Fx*gx+2*Fx*dG1x*gx+normdG1
    close(f'full second matrix diagonal {t1}',mu(force_plus_grad),mu(expanded))
    check(f'exterior row nonzero {t1}',mu(dG1y*dG1y*gy)>0,exterior=mu(dG1y*dG1y*gy))

# The retained local budget and all square roots for arbitrary allowed d_Q.
rng=np.random.default_rng(2026101205)
for n in range(200):
    kap=10**rng.uniform(-1,1);a=10**rng.uniform(-4,-1);b=1/(kap*a*a)
    Lam=10**rng.uniform(0,5);d=Lam*rng.uniform(.001,.999);z=100*.7*kap*a
    sumT=b*(Lam-d)/kap;sumF=16*b*b*d
    sumdG=2*math.sqrt(35)/(kap*kap*a)*math.sqrt(sumT*sumF)
    exact=a**4*(math.sqrt(sumF)+kap*math.sqrt(sumdG))**2
    retained=(4*math.sqrt(d)+math.sqrt(8*math.sqrt(35))*(d*(Lam-d))**.25)**2/kap**2
    close(f'original trace constants {n}',exact,retained)
    bound(f'coarse trace budget {n}',retained,(4+math.sqrt(8*math.sqrt(35)))**2*Lam/kap**2)

# Actual face/edge geometry with arbitrary allowed means, not a vacuum model.
R=.02;cube=-R/2;amps={(0,1):1.,(0,2):-.3,(1,2):.8}
M=1.;Jt=(R/3)**3*((1-.3)**2+(1+.8)**2+(-.3+.8)**2)
sample=[]
def fval(coords,pair):
    return amps[pair]*np.prod(np.maximum(1-2*np.abs(coords)/R,0),axis=-1)
for j in [1,2,4,8,16,32]:
    a=1/(100*j);L=j**4;q=math.ceil(R/a)+3;v=L+math.floor(cube/a)-1
    Lam=min(6*q*q*(q+1),3*a*math.sqrt(3*q*(q+1)**2*3*q*q*(q+1)))+24*q*(q+1)
    dmean=.1*a;dQ=3*q*q*(q+1)*dmean
    bnorm2=0.;cnorm2=0.;rnorm2=0.;grid2=0.;moderr2=0.
    # Removed edge chosen outside all support faces: u=0 in this grid check.
    # Removed-star interference is checked separately below.
    for direction in range(3):
        ranges=[np.arange(v+(k!=direction),v+q+(k==direction)) for k in range(3)]
        zz=np.stack(np.meshgrid(*ranges,indexing='ij'),axis=-1).astype(float)
        coords=a*(zz-L);coords[...,direction]+=a/2
        S=np.zeros(coords.shape[:-1]);td=np.zeros_like(S)
        for k in range(3):
            if k==direction:continue
            pair=tuple(sorted((direction,k)));td+=fval(coords,pair)
            cp=coords.copy();cm=coords.copy();cp[...,k]+=a/2;cm[...,k]-=a/2
            S+=fval(cp,pair)+fval(cm,pair)
        c=-.75*a**3*S;r=.375*a**3*dmean*S;vec=c+r
        bnorm2+=float(np.sum(vec*vec));cnorm2+=float(np.sum(c*c));rnorm2+=float(np.sum(r*r))
        grid2+=float(np.sum(td*td));moderr2+=float(np.sum((c+1.5*a**3*td)**2))
    bound(f'raw source deficit error j{j}',rnorm2,9*a**6*M*M*dQ)
    # The product tent has Euclidean Lipschitz constant at most 2 sqrt(3)/R.
    omega=min(2*M,math.sqrt(3)*a/R)
    bound(f'original half-edge sampling j{j}',math.sqrt(moderr2),3*a**3*omega*math.sqrt(3*q*(q-1)**2))
    left=abs(a**(-1.5)*math.sqrt(bnorm2)-1.5*math.sqrt(a**3*grid2))
    right=3*M*math.sqrt(a**3*dQ)+3*omega*math.sqrt(a**3*3*q*(q-1)**2)
    bound(f'complete source error j{j}',left,right)
    sample.append(dict(j=j,original_a=a,original_raw_b_squared=bnorm2,a_minus3_b_squared=bnorm2/a**3,limit=2.25*Jt))
for m in [2,3,4]:
    for k in range(20):
        f=rng.uniform(-1,1,m)
        exact=float(f.sum()**2+3*(f@f))
        bound(f'removed star m{m} k{k}',exact,m*(m+3))

# Reproducible illustrations of proved bounds and the full receiving map.
plt.rcParams.update({'font.size':11,'svg.fonttype':'none'})
r=np.linspace(0,35,600);tail=np.ones_like(r);mask=r>3
tail[mask]=(r[mask]/3)**1.5*np.exp(-(r[mask]-3)/2)
fig,ax=plt.subplots(figsize=(9,5.8));ax.semilogy(r,tail,color='#126782',lw=2)
ax.set(xlabel=r'Original threshold $R$ in $G_e\geq R/(\kappa_*a_j)$',ylabel='Proved conditional probability upper bound',title='Actual conditional score tail: every outside link configuration')
ax.axvline(3,color='#777777',ls=':',lw=1);ax.grid(alpha=.2)
ax.text(.43,.70,r'$G_e=|\nabla_e\log\psi_j|^2$'+'\n\n'+r'$(R/3)^{3/2}\exp[-(R-3)/2]$ for $R>3$',transform=ax.transAxes,bbox=dict(facecolor='white',edgecolor='#a0bac7',pad=10))
fig.text(.5,.015,'SOM3–SOM7. An upper bound for the actual conditional measure; no sampled vacuum or Gaussian identification.',ha='center',fontsize=8)
fig.tight_layout(rect=[0,.045,1,1])
for ext in ['png','svg']:fig.savefig(O/('ACTUAL_SCORE_TAIL.'+ext),dpi=170)
plt.close(fig)
fig,ax=plt.subplots(figsize=(11,7.5));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
def box(x,y,w,h,text):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',fc='#edf4f7',ec='#507b96'))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=10)
def arrow(xy1,xy2):ax.annotate('',xy=xy2,xytext=xy1,arrowprops=dict(arrowstyle='->',color='#315873',lw=1.5))
box(.05,.73,.40,.20,'Actual conditional score moments\n'+r'$\mu_e^xG_e^3\leq35(\kappa_*a_j)^{-2}\mu_e^xG_e$'+'\nAll outside configurations retained')
box(.55,.73,.40,.20,'Original local force and energy\n'+r'$\sum\mu|F_e|^2\leq16b_j^2d_Q$'+'\n'+r'$\sum T_e\leq b_j(\Lambda_Q-d_Q)/\kappa_*$')
box(.15,.40,.70,.21,r'$\mathscr{L}_1\alpha_e=-a_j^2(\Pi_e\,dV+\kappa_*\,dG_e)$'+'\n\n'+r'$(\mathsf{K}_2)_{er}=\langle\mathscr{L}_1\alpha_e,\mathscr{L}_1\alpha_r\rangle_\mu$'+'\nEvery Hessian row, force cross term and exterior derivative remains')
box(.10,.09,.80,.20,'Complete original finite matrix and source\n'+r'$\mathsf{Z}(z)=\mathsf{K}_2+2z\mathsf{K}+z^2\mathsf{N},\quad a_j^{-3}\|\mathsf{b}_j\|^2\to(9/4)J_t$'+'\n'+r'$\mathcal{W}(z)=z\kappa_*\mathsf{b}^*\mathsf{Z}(z)^{-1}\mathsf{b}+z\kappa_*\|\beta-D_z\alpha_*\|_\mu^2$')
arrow((.25,.72),(.40,.62));arrow((.75,.72),(.60,.62));arrow((.5,.39),(.5,.31))
ax.text(.5,.028,r'$e,r\in I=E_Q^\circ,\quad G_e=|\nabla_e\log\psi|^2,\quad\alpha_e=a_j^2\Pi_e\,d\log\psi$',ha='center',fontsize=9)
ax.set_title('From actual score moments to the second-energy matrix',fontsize=14,pad=12)
fig.text(.5,.04,r'$D_z=\mathscr{L}_1+zI,\quad\beta=D_z^{-1}dh_{e_0},\quad\alpha_*=\sum_e(\mathsf{Z}^{-1}\mathsf{b})_e\alpha_e$. SOM9–SOM23.',ha='center',fontsize=9)
fig.text(.5,.008,'The trace bound is proved; the directional inverse and physical residual still require evaluation.',ha='center',fontsize=9)
fig.tight_layout(rect=[0,.075,1,1])
for ext in ['png','svg']:fig.savefig(O/('SCORE_SECOND_ENERGY_MAP.'+ext),dpi=170)
plt.close(fig)
out=dict(checks=len(rows),all_passed=all(r['passed'] for r in rows),scope='Radius-two analytic one- and two-sphere diagnostics, correlated multiplier inequalities, original trace constants, exact face/edge sampling and removed-star bounds. Analytic diagnostic densities and arbitrary bounded face means are not the original Yang-Mills vacuum.',source_grid_diagnostics=sample,results=rows)
(O/'SCORE_MOMENTS_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=len(rows),all_passed=out['all_passed'],source_grid_diagnostics=sample)))
