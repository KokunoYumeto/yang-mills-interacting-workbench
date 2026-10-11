"""Reproducible diagram of actual maps and retained mathematical terms."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(15,9))
ax.set_xlim(0,15);ax.set_ylim(0,9);ax.axis('off')
def box(x,y,w,h,title,body,color='#eaf1f8'):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.10',
                            ec='#38546a',fc=color,lw=1.4))
 ax.text(x+w/2,y+h-0.23,title,ha='center',va='top',fontsize=10,weight='bold')
 ax.text(x+w/2,y+h/2-0.12,body,ha='center',va='center',fontsize=10.5,linespacing=1.5)
def arrow(a,b):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=16,
                             lw=1.4,color='#38546a'))
ax.text(7.5,8.75,'Actual weighted-potential law: exact maps, squares, and variance reception',
        ha='center',va='center',fontsize=17,weight='bold')
box(.25,6.5,4.2,1.65,'Original physical ground state',
    r'$d\mu=\psi^2dU$'+'\n'+r'$Y=\sum_p |f_p|(2-W_p)$'+'\n'+r'$0\leq Y\leq\ell=4A_1$')
box(5.4,6.5,4.2,1.65,'Actual coarea law — PF2–PF4',
    r'$Y_*\mu=p(y)\,dy$'+'\n'+r'$h=\mathbb{E}[\gamma\mid Y],\quad \eta=\mathbb{E}[A\mid Y]$'+'\n'+r'$z=\mathbb{E}[Z_Q\mid Y]$')
box(10.55,6.5,4.2,1.65,'Two continuous fluxes — PF6–PF16',
    r'$s=hp,\quad t=\eta p$'+'\n'+r'$s^{\prime}=Jp+2t$'+'\n'+r'$s(0)=s(\ell)=t(0)=t(\ell)=0$')
arrow((4.55,7.32),(5.3,7.32));arrow((9.7,7.32),(10.45,7.32))
box(.25,3.55,4.2,1.8,'All-function optimizer — PF20–PF24',
    r'$B_*(y)=-yt(y)/s(y)$'+'\n'+r'$I=\int_0^\ell y t^2/s\,dy$'+'\n'+r'$\mu(YZ_Q)=I+Q_*$')
box(5.4,3.55,4.2,1.8,'Exact remaining square',
    r'$Q_*=\int_0^\ell y\tau(y)p(y)\,dy$'+'\nTangential score energy\n+ normal-score variation within each fiber',
    '#fff0d9')
box(10.55,3.55,4.2,1.8,'Derived scalar ground equation — PF29',
    r'$-\kappa(h\chi^{\prime\prime}+J\chi^{\prime})$'+'\n'+
    r'$+(bu+o+\delta_Q+\kappa\tau)\chi$'+'\n'+r'$=b\Lambda_Q\chi,\qquad p=\chi^2m$')
arrow((2.35,6.4),(2.35,5.45));arrow((4.55,4.45),(5.3,4.45));arrow((9.7,4.45),(10.45,4.45))
box(.25,.60,4.2,1.8,'Actual upper excess — PF43–PF45',
    r'$e=F(E_0-E_{\rm out})/b\geq d$'+'\n'+
    r'$\mu[(Y-e)_+^2]\leq4V+2T^{-2}e^{-VT^2}$'+'\nScaled upper excess is '+r'$O(a)$')
box(5.4,.60,4.2,1.8,'Endpoint contribution removed — PF52',
    r'$a^2\int_{2\Lambda_f}^{\ell}\mathfrak{R}hp$'+'\n'+
    r'$\leq a^2\ell^2\exp(-c_0a^{-3})$'+'\nSmaller than every fixed power of '+r'$a$',
    '#e4f3e8')
box(10.55,.60,4.2,1.8,'Central variance receiver — PF53',
    r'$a^2\int_0^{\min(2\Lambda_f,\ell)}\mathfrak{R}hp$'+'\n'+
    r'$\mathfrak{R}=-\int_0^y(v-d)p(v)dv\,/\,(hp)$'+'\nOriginal mean '+r'$d$'+' retained; full exponent open',
    '#fff0d9')
arrow((2.35,3.45),(2.35,2.5));arrow((4.55,1.5),(5.3,1.5));arrow((9.7,1.5),(10.45,1.5))
ax.text(7.5,.16,'Exact identities PF2–PF53. Every conditional quantity comes from the original state; no shape for its unknown density is assumed.',
        ha='center',fontsize=10,color='#38546a')
fig.savefig(out/'pushforward_form_maps.png',dpi=165,bbox_inches='tight')
fig.savefig(out/'pushforward_form_maps.svg',bbox_inches='tight')
