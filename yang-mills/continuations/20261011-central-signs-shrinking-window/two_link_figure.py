from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
m=4;n=m+1;h=np.pi/(2*n)
A=np.sqrt(2)*np.cos(3*h)*np.sin(2*h)/n**1.5
d0=-np.sqrt(2)*np.cos(h)*np.sin(2*h)/n**1.5
dstar=-4*A*d0
assert np.isclose(dstar,8*np.cos(h)*np.cos(3*h)*np.sin(2*h)**2/n**3)
theta=np.linspace(0,4*np.pi,1001)
fig,axs=plt.subplots(1,2,figsize=(13,6))
ax=axs[0]
ax.plot(theta,2*A*d0*np.sin(theta),color='#237784',lw=2.3)
ax.axhline(0,color='#aab0b5',lw=.8)
ax.set_title('Exact quadratic normal component',fontsize=13)
ax.set_xlabel(r'$V=kh_b^{-1}=\exp(\theta T_3)$; $0\leq\theta\leq4\pi$')
ax.set_ylabel(r'$2Ad_0c(V)q_3(V)=-d_*\sin\theta/2$')
ax.text(.5,1.17,r'$X_{b_*,3}D=2Ad_0c(V)q_3(V)+R_3(k)$',transform=ax.transAxes,ha='center',fontsize=11)
ax=axs[1]
rho=(1+2*np.cos(theta))/3
ax.plot(theta,2*A*A*d0*d0*(1+rho),color='#237784',lw=2.3,label=r'$\int|P_2(\mathcal{S}-\mathcal{S}_{\mathcal{R}})|^2\,dk$')
ax.plot(theta,2*A*A*d0*d0*(1-rho),color='#a85a44',lw=2.3,label=r'$\int|P_2(\mathcal{S}+\mathcal{S}_{\mathcal{R}})|^2\,dk$')
ax.axhline(dstar*dstar/12,color='#237784',ls=':',lw=1.2,label=r'Odd lower bound: $d_*^2/12$')
ax.set_title('Full two-link harmonic Gram',fontsize=13)
ax.set_xlabel(r'$h_b=\exp(\varphi T_3)$; $0\leq\varphi\leq4\pi$')
ax.set_ylabel('Single-link Haar mass; original coefficients')
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.2),fontsize=9,frameon=False)
for ax in axs:
 ax.set_xticks([0,np.pi,2*np.pi,3*np.pi,4*np.pi],['0',r'$\pi$',r'$2\pi$',r'$3\pi$',r'$4\pi$'])
 ax.ticklabel_format(axis='y',style='sci',scilimits=(-2,2))
 ax.grid(alpha=.16)
fig.suptitle('Two original links detect the global reflection correction',fontsize=16,y=.98)
fig.text(.5,.9,r'$k_*=(1,0,0;2),\quad b_*=(m,0,0;2),\quad Z_{\mathcal{R}(m-1,0,0;2)}=kh_b^{-1}$',ha='center',fontsize=12)
fig.text(.5,.055,'Exact one-parameter sections at m=4, n=5. Haar projection P₂ only; every affine remainder remains in JP40–JP47.',ha='center',fontsize=10)
fig.text(.5,.017,'Proof: JP40–JP49. The physical state has the additional full factor β₀; the plotted curves are harmonic components, not spectral measures.',ha='center',fontsize=10)
fig.subplots_adjust(left=.09,right=.97,top=.77,bottom=.32,wspace=.36)
for ext in ['png','svg']:
 p=ROOT/('TWO_LINK_HARMONICS.'+ext);fig.savefig(p,dpi=180)
 if ext=='svg':p.write_text('\n'.join(x.rstrip() for x in p.read_text().splitlines())+'\n',encoding='utf-8',newline='\n')
