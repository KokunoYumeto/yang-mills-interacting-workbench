from pathlib import Path
import json
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent;mp.mp.dps=45
def integral(k,B=None):
 f=lambda u:u**k*mp.exp(-mp.sqrt(1+u*u))*(mp.sqrt(max(mp.mpf(0),1-u*u/(16*B*B))) if B is not None else 1)
 end=4*B if B is not None else mp.inf
 points=[mp.mpf(0)]+[mp.mpf(x) for x in [1,4,16,64,256] if x<end]+[end]
 return mp.quad(f,points)
constant=integral(10)/(4096*integral(2))
bs=[2,4,8,16,32,64];values=[integral(10,mp.mpf(b))/(4096*b**8*integral(2,mp.mpf(b))) for b in bs]
fig,axs=plt.subplots(1,2,figsize=(13.8,6.1))
ax=axs[0];ax.loglog(bs,[float(x) for x in values],'o-',color='#247984',lw=2,label=r'Actual $\int|P_*|^2\rho_B\,dU$')
dense=np.geomspace(2,64,200);ax.loglog(dense,float(constant)*dense**-8,'--',color='#a45a44',lw=1.8,label=r'Proved asymptote $(I_{10}/4096I_2)B^{-8}$')
ax.set(xlabel='Score parameter B in the original radius-two metric',ylabel='Weighted squared norm; full unit-density factor retained',title='The universal exponent eight is attained')
ax.grid(which='both',alpha=.14);ax.legend(fontsize=9,loc='lower left')
ax=axs[1];n=9;m=n-1;h=np.pi/(2*n);k=np.arange(m)
d=8*np.cos(3*h)*np.cos(h)*np.sin(np.pi*(k+1)/n)**2/n**3
ax.bar(k,d,color=['#a45a44' if x in [m//2-1,m//2] else '#247984' for x in k],width=.62)
ax.set(xticks=k,xlabel=r'Original second-coordinate index $k$, with $i=1,l=0$',ylabel=r'$-4a_{(1,k,0;2)}b_{(1,k,0;2)}$',title='A larger coefficient in the unchanged phase')
ax.text(.5,1.15,r'$d^\circ=8\cos(3h)\cos^3h/n^3$',ha='center',transform=ax.transAxes,fontsize=11)
ax.text(.5,-.21,r'$m=8,\ n=9,\ h=\pi/(2n)$; all k rows in this section.',ha='center',transform=ax.transAxes,fontsize=11)
ax.grid(axis='y',alpha=.14)
fig.suptitle('Polynomial density control and the exact receiving-link optimization',fontsize=16,y=.98)
fig.text(.5,.86,r'$P_*=(1-c)^2,\quad\rho_B=Z_B^{-1}\exp[-B\sqrt{B^{-2}+8(1-c)}],\quad |\nabla\log\rho_B|\leq B$',ha='center',fontsize=12)
fig.text(.5,.055,'Left: numerical quadrature of the explicit sharpness family in PC20–PC22, not a Yang–Mills vacuum sample. Right: exact original coefficients, PC45–PC52.',ha='center',fontsize=10)
fig.text(.5,.018,'Every affine remainder is retained in the proofs. These lower bounds do not determine the spectral mass inside the shrinking window.',ha='center',fontsize=10)
fig.subplots_adjust(left=.065,right=.98,top=.72,bottom=.27,wspace=.34)
for ext in ['png','svg']:
 p=ROOT/('POLYNOMIAL_CONDITIONAL_BOUNDS.'+ext);fig.savefig(p,dpi=180)
 if ext=='svg':p.write_text('\n'.join(x.rstrip() for x in p.read_text().splitlines())+'\n',encoding='utf-8',newline='\n')
(ROOT/'POLYNOMIAL_FIGURE_VALUES.json').write_text(json.dumps({'precision_digits':45,'B':bs,'weighted_squared_norms':[str(x) for x in values],'asymptotic_coefficient':str(constant),'right_panel':{'m':m,'n':n,'original_d_values':d.tolist()},'scope':'Reproducible numerical illustration of exact proved formulas; not a numerical proof or a physical vacuum sample.'},indent=2)+'\n',encoding='utf-8',newline='\n')
