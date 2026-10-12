from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent
v=json.loads((O/'KINETIC_PROFILE_CHECKS.json').read_text())
plt.rcParams.update({'font.size':11,'axes.titlesize':12,'svg.fonttype':'none','figure.facecolor':'white'})
fig,ax=plt.subplots(figsize=(12,7));ax.set_xlim(0,12);ax.set_ylim(0,7);ax.axis('off')
def box(x,y,w,h,title,text,color='#edf3f7'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.08',facecolor=color,edgecolor='#4e6879'))
    ax.text(x+w/2,y+h-.25,title,ha='center',va='center',fontsize=12,weight='bold')
    ax.text(x+w/2,y+h/2-.15,text,ha='center',va='center',fontsize=11)
box(.2,4.5,3.3,1.5,'Actual kinetic means',r'$\tau_{j,d}=a_jT_e$'+'\n'+r'$0<\tau_{j,d}\leq3/\kappa_*$')
box(4.2,4.5,3.3,1.5,'Constructed profiles',r'$0<\tau_d\leq3/\kappa_*$'+'\n'+r'$\sum_d\int\tau_d^{-1}\leq16K_R/9$')
box(8.2,4.5,3.5,1.5,'Full first energy matrix',r'$0\leq Q_j\leq15a_j^2/\kappa_*$'+'\n'+'positive Hessian remainder retained')
ax.annotate('',xy=(4.05,5.25),xytext=(3.55,5.25),arrowprops={'arrowstyle':'->','lw':1.6})
box(.2,1.6,5.3,1.9,'Actual source images',r'$Y_1=2Q_jb_j,\quad Y_2=N_jb_j$'+'\n'+r'$a_j^{-5}Y_1\rightharpoonup-3\mathcal{Q}t$'+'\n'+r'$a_j^{-6}Y_2\rightharpoonup-3\tau t/2$')
box(6.5,1.6,5.2,1.9,'Joint Green moments',r'$H^{11}:a_j^5,\quad H^{12},H^{21}:a_j^6$'+'\n'+r'$H^{22}:a_j^7$'+'\n'+'KP11: every mixed coefficient retained')
ax.annotate('',xy=(6.35,2.55),xytext=(5.6,2.55),arrowprops={'arrowstyle':'->','lw':1.6})
ax.text(6,3.95,'One actual subsequence carries the entire finite test family',ha='center',fontsize=11)
ax.text(6,.65,r'$Z^{(0)}=Q_jN_j^{-1}Q_j+R_j^*R_j$'+'\n'+'KP13: all five remaining Green moments retain the full complementary residual',ha='center',fontsize=12)
fig.suptitle('Original kinetic profiles, first energy and full shift receiver',fontsize=16)
fig.text(.5,.025,'KP1–KP17. Weak arrows denote the specified original-cell fields; all finite powers remain explicit.\nThese are exact maps and proved bounds, not a reconstructed continuum Yang–Mills state.',ha='center',fontsize=10)
fig.subplots_adjust(bottom=.13,top=.92)
for ext in ['png','svg']:fig.savefig(O/('KINETIC_PROFILE_AND_MOMENT_MAP.'+ext),dpi=180)
plt.close(fig)
rows=v['original_path_diagnostics'];fig,axes=plt.subplots(1,2,figsize=(12,5.4),layout='constrained')
for k,label,m in [('H11',r'$a^{-5}Y_1^*G^{-1}Y_1$','o'),('H12',r'$a^{-6}Y_1^*G^{-1}Y_2$','s'),('H22',r'$a^{-7}Y_2^*G^{-1}Y_2$','^')]:
    axes[0].plot([r['j'] for r in rows],[r['ratios'][k] for r in rows],marker=m,label=label)
for k,label,m in [('N',r'$a^{-6}b^*Nb$','o'),('Q',r'$a^{-5}b^*Qb$','s')]:
    axes[1].plot([r['j'] for r in rows],[r['ratios'][k] for r in rows],marker=m,label=label)
for ax,title in zip(axes,['Full mixed Green forms','Original source norm and first energy']):
    ax.axhline(1,color='black',ls='--',label='explicit diagnostic limit')
    ax.set(title=title,xlabel='original regulator index j',ylabel='value / its displayed reference limit')
    ax.legend(fontsize=10);ax.grid(alpha=.2)
fig.suptitle('Original-grid checks of four Green moments and source matrices',fontsize=15)
fig.supxlabel('Specified diagnostic face means 2 − a and nonlocal Q; not sampled Yang–Mills vacuum data.\nR = 1/25, a = 1/(100j), q = ceil(R/a) + 3. Full matrix, fields and reference constants are stated in the proof.',fontsize=10)
for ext in ['png','svg']:fig.savefig(O/('KINETIC_MOMENTS_ORIGINAL_GRID.'+ext),dpi=180)
plt.close(fig)
print(json.dumps({'figures':['KINETIC_PROFILE_AND_MOMENT_MAP','KINETIC_MOMENTS_ORIGINAL_GRID']}))
