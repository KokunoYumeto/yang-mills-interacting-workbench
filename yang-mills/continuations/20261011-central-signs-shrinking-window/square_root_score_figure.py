"""Reproduce exact proved bounds, not samples of the unknown vacuum."""
from pathlib import Path
import json, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
beta=np.geomspace(1e-3,1e4,500)
C=2+2*math.sqrt(4+2*math.pi)
c=(math.sqrt(9*math.pi**2+32*math.pi)-3*math.pi)/8
Crho=2*math.sqrt((2*math.pi/c+4)/(1-c/2)**2)
fig,ax=plt.subplots(1,2,figsize=(14,5.8))
fig.suptitle('Actual-vacuum bounds with the original one-link metric',fontsize=17)
ax[0].loglog(beta,4*beta,'--',label=r'Original bound $4\beta$',color='#888888')
ax[0].loglog(beta,np.minimum(4*beta,Crho*np.sqrt(beta)),label=r'Entropy closure (ESE29)',color='#dd842c')
ax[0].loglog(beta,np.minimum(4*beta,C*np.sqrt(beta)),label=r'Heat ratio + entropy (LS32)',color='#1874a9',lw=2.5)
ax[0].set(xlabel=r'Actual local source $\beta=r_e\xi=r_e/(4g^4)$',ylabel=r'Proved upper bound for $\|\nabla_e\log\psi^2\|_\infty$',title=r'$C_*=2+2\sqrt{4+2\pi}$; every exterior link retained')
ax[0].legend(loc='upper left',fontsize=9);ax[0].grid(alpha=.2,which='both')
ax[1].axis('off')
texts=[
 (0.87,r'$H\psi=E_0\psi,\quad H=\kappa K+\kappa\xi\sum_p(2-W_p)$'+'\nFull physical vacuum and scalar terms (LS2)', '#e7f2f7'),
 (0.64,r'$\operatorname{osc}_e\log\psi\leq4\pi\min\{\beta,\sqrt{\beta}\}$'+'\nExact outside-path Feynman–Kac map (HR18–HR21)', '#e7f2f7'),
 (0.41,r'$\|\nabla_e\log\psi^2\|_\infty\leq\min\{4\beta,C_*\sqrt{\beta}\}$'+'\nConditional edge entropy; terminal point retained (LS20–LS32)', '#e7f2f7'),
 (0.17,r'$\mathcal{E}(s)=4\beta_0^2[\mathcal{Q}_4-(\kappa/s)\mathcal{K}_1]$'+'\n'+r'$-\beta_0^2\mu(D^2)+(\kappa\beta_0^2/s)\mu|\nabla D|^2$'+'\nEvery signed term remains in the endpoint (LS47)', '#fff1df')]
for y,t,color in texts:
    ax[1].text(.5,y,t,ha='center',va='center',fontsize=10.5,transform=ax[1].transAxes,bbox=dict(boxstyle='round,pad=.65',facecolor=color,edgecolor='#9ba9b2'))
for y1,y2 in [(.79,.73),(.55,.50),(.32,.28)]:
    ax[1].annotate('',xy=(.5,y2),xytext=(.5,y1),xycoords='axes fraction',arrowprops=dict(arrowstyle='->',lw=1.4,color='#566978'))
fig.text(.5,.015,'Curves show explicit upper bounds. They are not measurements of the vacuum, spectral mass, or a continuum gap.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.06,1,.93))
for ext in ('png','svg'):fig.savefig(ROOT/f'SQUARE_ROOT_SCORE.{ext}',dpi=170)
(ROOT/'SQUARE_ROOT_SCORE_FIGURE_VALUES.json').write_text(json.dumps({'C_star':C,'C_rho_entropy':Crho,'beta_range':[float(beta[0]),float(beta[-1])],'samples':len(beta),'scope':'Exact explicit upper-bound functions; no numerical vacuum or spectral approximation.'},indent=2)+'\n')
