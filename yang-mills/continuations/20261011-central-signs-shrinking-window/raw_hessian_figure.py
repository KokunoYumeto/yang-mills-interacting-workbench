from pathlib import Path
import importlib.util, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root=Path(__file__).resolve().parent
# The check module also replays the finite verification before rendering.
spec=importlib.util.spec_from_file_location('checked',root/'check_raw_hessian.py')
checked=importlib.util.module_from_spec(spec);spec.loader.exec_module(checked)
xs=np.unique(np.geomspace(2,1000,180).astype(int));old=[];new=[]
for jf in xs:
    j=checked.mp.mpf(str(jf));n=2*j**4+1;m=n-1;k=checked.constants(n)
    a=1/(100*j);b=10000*j*j;N=3*m*n*n;M=3*m*m*n
    e0=min(2*b*M,3*checked.mp.sqrt(N*M)/a)
    old.append(float(4*k['S1']**2*e0))
    new.append(float(400*j*k['S1']**2+k['S1']*k['R2c']/2))
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(15.5,7.5),layout='constrained')
gs=fig.add_gridspec(1,2,width_ratios=[1,1.18])
ax=fig.add_subplot(gs[0,0]);ax.loglog(xs,old,color='#b65245',lw=2.5,label=r'CV43: $4S_1^2\mathcal{E}_0/\kappa_*$')
ax.loglog(xs,new,color='#147d92',lw=2.5,label=r'RH41: $4\sqrt{\xi}S_1^2+S_1R_{2,c}/2$')
ax.set(xlabel=r'Original path index $j$; $\kappa_*=1$',ylabel=r'Proved upper function for $V_B=\mu(B\log\psi)^2$',title='A smaller bound for the same physical field')
ax.grid(True,which='major',alpha=.2);ax.legend(loc='upper left',fontsize=10)
ax.text(.05,.53,r'Old: $j^{25}$'+'\n'+r'New: $j^{13}$'+'\n\n'+r'$j^{12}\,U_{\rm new}/U_{\rm old}\ \longrightarrow\ 1/72$',transform=ax.transAxes,bbox=dict(boxstyle='round,pad=.5',fc='#f5f6f7',ec='none'),fontsize=12)
ax.text(.97,.03,'Curves join integer-path bound values.\nThey do not measure the vacuum variance.',transform=ax.transAxes,fontsize=10,ha='right')
bx=fig.add_subplot(gs[0,1]);bx.axis('off');bx.set_title('Exact raw receiving quantities',pad=16)
boxes=[
 (.81,'Original physical conjugate  (RH32–RH36)',r'$B=Y_{V_3,u_1},\quad \nabla_BB=Y_{V_3,(u_1\times u^{[1]})/2}$'),
 (.57,'All same-chord terms cancel  (RH37, RH47)',r'$V_B=-\frac{1}{2}\mu[\nabla^2w(B,B)]+\frac{1}{8}(C_{02}-C_{11})$'+'\n'+r'$C_{02}-C_{11}=\frac{1}{2}\sum_{c,d}a_ca_d(r_c-r_d)^2\mu(q_c\cdot q_d)$'),
 (.31,'Unchanged raw phase and covariance  (RH43–RH44)',r'$F=\beta_0(S-S_R),\quad 4G_FV_B\geq\beta_0^2(2x+\mu\Xi)^2$'),
 (.095,'Shrinking window remains undecided  (RH49–RH51)',r'$\nu_F((0,s_j])\geq\max\{0,G_F-E_F/s_j\},\quad s_j=\kappa_*/j$')]
for y,title,body in boxes:
    height=.15 if y<.1 else (.18 if y!=.57 else .21)
    bx.add_patch(FancyBboxPatch((.02,y-height/2),.96,height,boxstyle='round,pad=.008',transform=bx.transAxes,facecolor='#edf5f6' if y>.1 else '#f9f1e9',edgecolor='#b7c9ce'))
    bx.text(.5,y+height*.30,title,ha='center',va='center',transform=bx.transAxes,fontsize=10.5)
    bx.text(.5,y-height*.11,body,ha='center',va='center',transform=bx.transAxes,fontsize=10.5)
for y0,y1 in [(.73,.685),(.46,.39),(.235,.165)]:
    bx.annotate('',xy=(.5,y1),xytext=(.5,y0),xycoords='axes fraction',arrowprops=dict(arrowstyle='-|>',lw=1.5,color='#455a64'))
fig.suptitle('The new vacuum Hessian bound applied to the original raw S6 phase',fontsize=17)
fig.savefig(root/'RAW_S6_HESSIAN_RECEIVING.png',dpi=190)
fig.savefig(root/'RAW_S6_HESSIAN_RECEIVING.svg')
(root/'FIGURE_VALUES.json').write_text(json.dumps({'kappa_star':1,'j':xs.tolist(),'old_bound':old,'new_bound':new,'source_equations':['RH36','RH37','RH41','RH42','RH43','RH47','RH49']},indent=2),encoding='utf-8')
print('Figure written.')
