from pathlib import Path
import json,math
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
P=Path(__file__).resolve().parent
a,t,tau,rho,lam,s,k=sp.symbols('a t tau rho lambda s k',positive=True)
checks=[]
def exact(name,x):
    assert sp.simplify(x)==0,name
    checks.append(name)
h=(1-sp.exp(-tau*a*lam))/(a*lam)
exact('Retained heat multiplier integral',sp.integrate(sp.exp(-s*a*lam),(s,0,tau))-h)
exact('Original-time heat maximizer',sp.diff(lam*sp.exp(-2*t*lam),lam).subs(lam,1/(2*t)))
exact('Original-time heat maximum', (lam*sp.exp(-2*t*lam)).subs(lam,1/(2*t))-1/(2*sp.E*t))
exact('Original-window full coefficient',(tau**2*a*lam/2).subs(lam,100*k*a)-50*tau**2*k*a**2)
F=lambda x:(1-sp.exp(-x*lam))/lam
phi=lambda x:(1-sp.exp(-x*lam))/sp.sqrt(lam)
exact('Anchored reflected Gram',F(s)+F(t)-F(s+t)-phi(s)*phi(t))
exact('Anchored covariance derivative',sp.diff(2*F(t),t)-2*sp.exp(-t*lam))
exact('Anchored covariance second derivative',sp.diff(2*F(t),t,2)+2*lam*sp.exp(-t*lam))
exact('Zero endpoint retained',sp.limit(F(t),lam,0)-t)
exact('Positive-energy transfer zero endpoint',sp.limit(phi(t),lam,0))
exact('Infinite endpoint retained',sp.limit(F(t),lam,sp.oo))
exact('Phase small-parameter second moment',sp.limit((1-sp.cos(rho*s))/rho**2,rho,0)-s**2/2)
exact('Full sixth-moment constant',(2*k*(2*3-1))**3-(10*k)**3)
exact('Full fourth-moment constant',(2*k*(2*2-1))**2-(6*k)**2)
exact('Sharper limiting fourth-moment constant',sp.factorial2(3)*(2*k)**2-12*k**2)
rr=sp.symbols('r',positive=True)
exact('Full weighted-window maximum',(lam*(1-lam/rr)).subs(lam,rr/2)-rr/4)
samples=0;max_ratio=0.0
for av in [1/200,1/400,1/1000,1/10000]:
    for tv in [.1,.7,2.0]:
        for uv in [.2,1.,3.]:
            for lv in np.geomspace(1e-6,1e5,121):
                hv=-math.expm1(-uv*av*lv)/(av*lv)
                delta=(math.sqrt(uv)-math.sqrt(hv))**2
                assert delta<=uv-hv+2e-14
                bound=uv*uv*av/(4*math.e*tv)
                value=math.exp(-2*tv*lv)*delta
                assert value<=bound*(1+1e-10)
                max_ratio=max(max_ratio,value/bound);samples+=1
for y in np.linspace(-30,30,1201):
    assert abs(y-math.sin(y))<=abs(y)**3/6+1e-12
    defect=y*y/2-(1-math.cos(y))
    assert defect>=-1e-12 and defect<=y**4/24+1e-12
    samples+=1
# A finite spectral quadrature tests identities, not the Yang–Mills state.
lv=np.array([.002,.4,1.3,7.0]);mass=np.array([.6,.8,.15,.02])
sv,tv=.3,1.1
D=lambda x:2*np.dot(mass,-np.expm1(-x*lv))
assert abs(.5*(D(sv)+D(tv)-D(sv+tv))-np.dot(mass,(-np.expm1(-sv*lv))*(-np.expm1(-tv*lv))))<1e-14
samples+=1
plt.rcParams.update({'font.size':10,'axes.titlesize':11})
fig,axs=plt.subplots(2,2,figsize=(12,8.8))
x=np.linspace(.001,8,900)
for tv in [.5,1.,2.]:
    axs[0,0].plot(x,-np.expm1(-tv*x)/np.sqrt(x),label=f't = {tv:g}')
    axs[0,1].plot(x,-np.expm1(-tv*x)/x,label=f't = {tv:g}')
axs[0,0].set(title='EF15: anchored vector transfer',xlabel='Original spectral energy λ',ylabel='φₜ(λ) = (1 − exp(−tλ)) / √λ')
axs[0,1].set(title='EF19–EF20: anchored variance transfer',xlabel='Original spectral energy λ',ylabel='Fₜ(λ) = (1 − exp(−tλ)) / λ')
for ax in axs[0]:
    ax.legend(frameon=False);ax.grid(alpha=.2)
axs[0,0].text(.97,.94,'φₜ(0) = 0\nφₜ(∞) = 0',ha='right',va='top',transform=axs[0,0].transAxes)
axs[0,1].text(.97,.94,'Fₜ(0) = t\nFₜ(∞) = 0',ha='right',va='top',transform=axs[0,1].transAxes)
ax=axs[1,0];ax.axis('off');ax.set_title('EF6, EF16–EF18: exact receiving spaces')
boxes=[
(.02,.72,.94,.20,'Heat fluctuation ητ:  Pητ = √τ Pζ'),
(.02,.41,.45,.20,'Positive energy ζ⁺\nVisible in phase space K*'),
(.51,.41,.45,.20,'Zero energy Zζ\nVisibility still retained'),
(.02,.04,.94,.23,'Escape Qητ is killed by every positive heat time.\nThe original shrinking window lies at zero energy;\nits cyclic-compression defect is still present.')]
for xx,yy,ww,hh,txt in boxes:
    ax.add_patch(FancyBboxPatch((xx,yy),ww,hh,boxstyle='round,pad=0.012',facecolor='#edf3fa',edgecolor='#325a79',transform=ax.transAxes))
    ax.text(xx+ww/2,yy+hh/2,txt,ha='center',va='center',fontsize=9.5,transform=ax.transAxes)
for xx in [.24,.75]:
    ax.annotate('',xy=(xx,.62),xytext=(.49,.70),arrowprops={'arrowstyle':'->','color':'#325a79'},xycoords='axes fraction')
ax=axs[1,1];ax.axis('off');ax.set_title('EF21–EF27: actual history and window maps')
ax.text(.02,.88,'D(t) / (2t) → ‖Zζ‖²  as t → ∞',fontsize=12,transform=ax.transAxes)
ax.text(.02,.64,'Reflected linear increments retain\n½[D(s) + D(t) − D(s+t)].\nThe zero-energy linear term cancels.',fontsize=11,linespacing=1.5,transform=ax.transAxes)
ax.text(.02,.21,'Phase weight in (0,r), divided by θ²,\nhas lower limit at least\n'+r'$(4/r)\langle\zeta^c,(I-A/r)_+\zeta^c\rangle$'+'\nThe zero-energy contribution is retained.',fontsize=11,linespacing=1.5,transform=ax.transAxes)
fig.suptitle('Actual energy-root vectors and bounded phase histories',fontsize=15)
fig.text(.5,.035,'Top panels plot the exact transfer functions at the stated times; they are not spectral samples of the quantum vacuum.\nBottom panels retain the continuous, zero-energy, cyclic and escaped components separately.',ha='center',fontsize=9)
fig.subplots_adjust(top=.90,bottom=.12,hspace=.42,wspace=.32)
fig.savefig(P/'ENERGY_ROOT_MAP.png',dpi=170)
fig.savefig(P/'ENERGY_ROOT_MAP.svg')
plt.close(fig)
receipt=dict(exact_checks=checks,exact_check_count=len(checks),numerical_samples=samples,max_heat_error_to_bound=max_ratio,finite_spectral_quadrature='Four selected positive energies test an algebraic identity only; no actual quantum coefficients inferred.',figure='ENERGY_ROOT_MAP.png',proof_status='Diagnostics supplement the complete EF1–EF27 derivation.')
(P/'ENERGY_ROOT_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8',newline='\n')
print(json.dumps(receipt))
