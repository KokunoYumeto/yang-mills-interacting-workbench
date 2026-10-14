from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(12,9));fig.patch.set_facecolor('#f6f8fb');ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.04,.955,'Both original sources, with the entire mixed tail',fontsize=21,weight='bold',color='#16334a')
ax.text(.04,.91,'Original metric, potential, raw face coefficients and projections retained',fontsize=13,color='#42586b')
def box(y,h,title):
    ax.add_patch(FancyBboxPatch((.04,y),.92,h,boxstyle='round,pad=.012',fc='white',ec='#9bb1c5',lw=1.3))
    ax.text(.06,y+h-.035,title,fontsize=16,weight='bold',color='#16334a',va='top')
box(.59,.26,'Exact gradient-source action  [MSA1]')
ax.text(.06,.75,r'$DBf=B(L_Af)-2\kappa_*b_j\sum_p\xi_{\partial p}\langle dT_p,df\rangle$',fontsize=17)
ax.text(.12,.69,r'$+\;4\kappa_*^2Q\left(\nabla^2h_\tau:\nabla^2f+(\frac{1}{2}g-2\nabla^2u)(dh_\tau,df)\right)_\tau$',fontsize=16)
ax.text(.06,.625,r'For the actual resolvent: $B(L_Af_z^0)=Bx-zBf_z^0$.',fontsize=14)
box(.335,.20,'Both full source norms evaluated  [MSA2–MSA3]')
ax.text(.06,.435,r'$b_z=Bf_z^0,\quad \|Db_z\|\leq\mathcal{B}_{j,z},\quad \|Dy\|\leq\mathcal{Y}_j$',fontsize=18)
ax.text(.06,.375,r'All constants use the original $N_j,M_j,a_j,\kappa_*,z$ and face samples.',fontsize=14)
box(.04,.24,'The complete resolvent cross term  [MSA5–MSA6]')
ax.text(.06,.18,r'$\langle b_z,(D+\sigma)^{-1}y\rangle=\frac{\langle b_z,y\rangle}{\sigma}-\frac{\langle b_z,Dy\rangle}{\sigma^2}$',fontsize=18)
ax.text(.18,.115,r'$+\;\frac{\langle Db_z,(D+\sigma)^{-1}Dy\rangle}{\sigma^2},\qquad |\mathrm{tail}|\leq\frac{\mathcal{B}_{j,z}\mathcal{Y}_j}{\sigma^2(\sigma+\delta_j)}$',fontsize=18)
ax.text(.04,.012,'The tail is retained exactly; its magnitude bound does not determine the mixed sign or the continuum limit.',fontsize=11,color='#42586b')
fig.subplots_adjust(left=.01,right=.99,top=.99,bottom=.01)
for ext in ['png','svg']:fig.savefig(O/f'MIXED_SOURCES_AND_ENTIRE_TAIL.{ext}',dpi=180,facecolor=fig.get_facecolor())
plt.close(fig)
