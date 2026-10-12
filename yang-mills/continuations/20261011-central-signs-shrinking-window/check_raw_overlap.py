"""Exact original-coordinate integral checks and one-edge character-compression comparisons. No full-vacuum samples and no computed value of the variational overlap constant."""
from pathlib import Path
import json,math
import numpy as np
from scipy.special import roots_legendre,beta
from scipy.linalg import eigh_tridiagonal
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent;rows=[];profiles=[]
def check(name,error,tol=3e-8):
    error=float(error);assert abs(error)<=tol,(name,error,tol)
    rows.append(dict(name=name,error=error,tolerance=tol,passed=True))
xx,ww=roots_legendre(900);r=np.pi*(xx+1);dr=np.pi*ww
J=(np.sin(r/2)/(r/2))**2;logJr=1/np.tan(r/2)-2/r
haar=r*r*J/(4*np.pi)
check('radius-two probability Haar integral',np.dot(dr,haar)-1)
check('radius-two Haar trace second moment',np.dot(dr,haar*(2*np.cos(r/2))**2)-1)
for kap in [.3,1.,1.7]:
    for m,rho in [(2,1.2),(3,2.1),(4,4.)]:
        for j in [4,19,80]:
            a=1/(100*j);b=1/(kap*a*a);y=r/np.sqrt(a);dy=dr/np.sqrt(a)
            for n in [0,3,10,30]:
                norm=math.sqrt(4.**(2*n)*8/np.pi*beta(2*n+1.5,1.5))
                base=2+2*np.cos(r/2);chi=base**n/norm
                chir=np.zeros_like(r) if n==0 else -n*base**(n-1)*np.sin(r/2)/norm
                w=a**.75/(4*np.pi)*np.sqrt(J)*chi
                wy=a**.75/(4*np.pi)*np.sqrt(J)*np.sqrt(a)*(chir+.5*logJr*chi)
                cov=wy-.5*np.sqrt(a)*logJr*w
                kinetic=kap*np.dot(dy,4*np.pi*y*y*cov*cov)
                potential=np.dot(dy,4*np.pi*y*y*rho/(2*kap*a)*(1-np.cos(np.sqrt(a)*y/2))*w*w)
                originalK=3*n*n/(4*(4*n+1));originalD=6/(2*n+3)
                check(f'coords{kap},{m},{rho},{j},{n}: exact full norm',np.dot(dy,4*np.pi*y*y*w*w)-1)
                check(f'coords{kap},{m},{rho},{j},{n}: original kinetic and Jacobian derivative',kinetic-a*kap*originalK)
                full=(m-rho)/(2*kap*a)+kinetic+potential
                expected=a*(kap*originalK+b*(m-rho)/2+b*rho*originalD/4)
                check(f'coords{kap},{m},{rho},{j},{n}: full scalar and potential',(full-expected)/max(1.,abs(expected)))
                lower=rho*y*y/(4*kap*np.pi*np.pi)
                actual=rho/(2*kap*a)*(1-np.cos(np.sqrt(a)*y/2))
                check(f'coords{kap},{m},{rho},{j},{n}: original global tail potential',max(0.,np.max(lower-actual))/max(1.,np.max(actual)))
# The complete original central character operator, compressed to 1024 characters.
N=1024;nn=np.arange(N);cas=nn*(nn+2)/4
def evaluate(c,chi):
    p0=np.ones_like(chi);out=c[0]*p0
    if len(c)==1:return out
    p1=chi.copy();out+=c[1]*p1
    for k in range(2,len(c)):
        p2=chi*p1-p0;out+=c[k]*p2;p0,p1=p1,p2
    return out
for rho in [2.,4.]:
    olderror=None
    for j in [4,16,64]:
        kap=1.;a=1/(100*j);b=1/a**2
        E,V=eigh_tridiagonal(kap*cas,np.full(N-1,-b*rho/4),select='i',select_range=(0,0))
        c=V[:,0]
        if c[0]<0:c=-c
        phi=evaluate(c,2*np.cos(r/2));y=r/np.sqrt(a);dy=dr/np.sqrt(a)
        w=a**.75/(4*np.pi)*np.sqrt(J)*phi
        gamma=np.sqrt(rho)/(4*kap);g=(gamma/np.pi)**.75*np.exp(-gamma*y*y/2)
        norm=np.dot(dy,4*np.pi*y*y*w*w);overlap=np.dot(dy,4*np.pi*y*y*w*g)
        check(f'compressed ground{rho},{j}: original transformed norm',norm-1,2e-7)
        err=np.dot(dy,4*np.pi*y*y*(w-g)**2)
        if olderror is not None:check(f'compressed ground{rho},{j}: decreasing comparison error',max(0.,err-olderror),1e-12)
        olderror=err
        check(f'compressed ground{rho},{j}: exact retained upper bound',max(0.,a*(E[0]+b*rho/2)-3*np.sqrt(rho)/4-3*a/16),2e-7)
        scaled_kinetic=a*kap*np.dot(cas,c*c)
        deficit=2-2*np.dot(c[:-1],c[1:])
        scaled_potential=rho*deficit/(4*kap*a)
        check(f'compressed ground{rho},{j}: separate original energy contributions',scaled_kinetic+scaled_potential-a*(E[0]+b*rho/2),2e-7)
        profiles.append(dict(rho=rho,j=j,a=a,characters=N,transformed_norm=norm,gaussian_overlap=overlap,squared_L2_difference=err,shifted_scaled_rayleigh=a*(E[0]+b*rho/2),scaled_original_kinetic=scaled_kinetic,scaled_original_potential=scaled_potential,oscillator_energy=3*np.sqrt(rho)/4,separate_limit=3*np.sqrt(rho)/8))
# All finite factors of the raw-measure receiving bracket, without substituting c_{2,T}.
for kap in [.3,1.7]:
    for R in [.23,2.1]:
        Tval=2*(3+8/(kap*R));a=1e-9;b=1/(kap*a*a);q=np.ceil(R/a)+3
        nq=3*q*(q+1)**2;mp=3*q*q*(q+1);cq=12*q*(q+1);count=3*q*(q-1)**2
        lam=min(2*mp,3*kap*a*np.sqrt(nq*mp))+2*cq
        bracket=a**3*(count-lam-a*b*lam/Tval)
        target=3*R**3-(9*R**3+24*R*R/kap)/Tval
        check(f'raw bound{kap},{R}: original-path bracket',bracket/target-1,2e-5)
plt.rcParams.update({'font.size':10,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(12,7.2));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
def box(x,y,w,h,txt,col):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',facecolor=col,edgecolor='#6c7d8c'))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',fontsize=11)
box(.05,.71,.40,.20,'Original radius-two SU(2) coordinate\n'+r'$r=\sqrt{a}\,y,\quad dV=J(r)\,d^3r/(16\pi^2)$'+'\n'+r'$w_a=a^{3/4}J(\sqrt{a}\,y)^{1/2}\chi/(4\pi)$','#e8f0fa')
box(.55,.71,.40,.20,'Full transformed form retained\nJacobian derivative + original metric\n'+r'$(m-\rho)/(2\kappa_*a)+\mathfrak{q}_{a,\rho}[w]$','#e8f0fa')
box(.05,.39,.40,.21,'Ground comparison and compactness\n'+r'$g_\rho=(\sqrt{\rho}/(4\pi\kappa_*))^{3/4}$'+'\n'+r'$\times\exp[-\sqrt{\rho}|y|^2/(8\kappa_*)]$'+'\nExact original-coordinate proof: RO1–RO8','#eaf3e7')
box(.55,.39,.40,.21,'Actual raw overlap\n'+r'$c_{2,T}>0,\quad k_e^2\geq c_{2,T}^2/4$'+'\n'+r'$d\nu_e=m_{\mathrm{out},e}k_e^2\,dx$'+'\nProved on the controlled region: RO9–RO14','#faefdc')
for x in [.25,.75]:ax.add_patch(FancyArrowPatch((x,.70),(x,.60),arrowstyle='->',mutation_scale=15,color='#526675'))
ax.add_patch(FancyArrowPatch((.45,.50),(.55,.50),arrowstyle='->',mutation_scale=15,color='#526675'))
ax.text(.5,.235,r'$\liminf_j\,a_j^4\sum_{e\in E_Q^\circ}\int\mathcal{G}_e\,d\nu_e'
+r'\ \geq\ \frac{9\sqrt{2}\,c_{2,T}^2}{128}\left(3R^3-\frac{9R^3+24R^2/\kappa_*}{T}\right)>0$',
ha='center',fontsize=14)
ax.text(.5,.135,r'$T>3+8/(\kappa_*R)$'+'. The positive variational constant is retained; no numerical value assigned.',ha='center',fontsize=11)
ax.text(.5,.065,'RO17 controls the original raw measure. The full complementary inverse and the physical spectral window remain.',ha='center',fontsize=10)
ax.set_title('From the original one-edge geometry to actual raw overlap',fontsize=15,pad=12)
fig.tight_layout();fig.savefig(O/'RAW_OVERLAP_COORDINATE_MAP.png',dpi=170);fig.savefig(O/'RAW_OVERLAP_COORDINATE_MAP.svg');plt.close(fig)
result=dict(all_passed=True,checks=len(rows),scope=__doc__,diagnostics=rows,character_comparisons=profiles)
(O/'RAW_OVERLAP_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(all_passed=True,checks=len(rows),character_comparisons=profiles)))
