from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

root=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(17,10),facecolor='#f7f8fb')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,17);ax.set_ylim(0,10);ax.axis('off')
def box(x,y,w,h,color='#ffffff',edge='#cbd5e1',radius=.12):
    p=FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0.02,rounding_size={radius}',facecolor=color,edgecolor=edge,linewidth=1.5)
    ax.add_patch(p);return p
def txt(x,y,text,size=12,color='#17243a',ha='left',va='center',weight='normal'):
    text=re.sub(r'\\(mathcal|mathscr|mathsf|mathbf) ([A-Za-z0-9])',r'\\\1{\2}',text)
    return ax.text(x,y,text,fontsize=size,color=color,ha=ha,va=va,fontweight=weight,linespacing=1.5)
def arrow(x1,y1,x2,y2,color='#3465a4'):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=16,color=color,lw=1.8))

txt(.65,9.48,'The actual bounded potential multiplier',24,weight='bold')
txt(.65,9.01,r'$b_Y=Y/(e+Y),\quad e=F(E_0-E_{\rm out})/b,\quad d\mu=\psi^2\,dU$',16)
txt(16.35,9.08,'Original state · original time · unchanged vectors',11,ha='right',color='#526278')

box(.6,3.35,5.15,5.05)
txt(.88,8.04,'1  Actual spaces and the shrinking window',14,weight='bold')
box(.88,3.73,4.58,3.88,'#edf3fc','#8da7cc')
txt(1.1,7.30,r'$\mathcal H_c=P\mathcal H_{\mathcal U}$',16)
box(1.12,4.1,4.10,2.67,'#eaf5ef','#82b296')
txt(1.35,6.47,r'$\mathcal H_+$: augmented cyclic space',14)
box(1.38,4.39,3.57,1.32,'#fff','#94b8a3')
txt(1.65,5.32,r'$\mathcal H_{\rm rec}\subseteq\mathcal H_+$',15)
txt(1.65,4.82,'Existing Wilson cyclic space',11)
txt(1.12,3.98,'B is central on the augmented algebra.',10.5)
txt(.9,6.97,'B reduces P; its full spectrum is not restricted here.',10,color='#526278')
txt(.9,3.54,'IB18–IB26, IB31–IB32. Inclusion need not be strict.',10,color='#526278')

box(5.98,3.35,5.05,5.05)
txt(6.24,8.04,'2  The exact visible / hidden split',14,weight='bold')
txt(8.50,7.30,r'$v=(B-\beta)\Omega\in\operatorname{ran}L$',17,ha='center')
txt(8.50,6.86,r'$L=[\mathbf 1_{(0,s_j]}(\mathscr H_j)],\quad s_j=100\kappa_*a_j$',12,ha='center')
txt(8.50,6.48,r'$Av=0,\qquad \Vert v\Vert^2=g$',15,ha='center')
arrow(8.25,6.12,7.23,5.56);arrow(8.75,6.12,9.80,5.56)
box(6.23,4.73,2.05,.78,'#eaf2ff','#789fca')
box(8.74,4.73,2.03,.78,'#fff1e9','#c99875')
txt(7.25,5.13,r'$Rv$',17,ha='center');txt(9.76,5.13,r'$(I-R)v$',17,ha='center')
txt(7.25,4.38,'Visible to original words',10,ha='center');txt(9.76,4.38,'Orthogonal to their span',10,ha='center')
txt(8.50,3.92,r'$g=g_{\rm vis}+g_{\rm hid}$',16,ha='center')
txt(6.25,3.54,'R is the existing cyclic projection; g remains unknown.',10,color='#526278')

box(11.26,3.35,5.14,5.05)
txt(11.54,8.04,'3  The complementary energy receiver',14,weight='bold')
txt(13.82,7.28,r'$X=B(I-B)^{-1}$ on $\mathcal H_+$',17,ha='center')
txt(13.82,6.75,r'$\rho_- I\leq X\leq\rho_+ I,\quad\rho_-+\rho_+=1$',14,ha='center')
txt(11.61,6.16,r'$Y_j/e_j$',17);arrow(12.88,6.14,14.25,6.14);txt(14.57,6.16,r'$X$',18)
txt(11.61,5.52,r'$\mathcal A_j/e_j$',17);arrow(13.04,5.50,14.25,5.50);txt(14.57,5.52,r'$I-X$',18)
txt(13.82,4.78,'Each map acts on the actual bounded heat words.',11,ha='center')
txt(13.82,4.31,r'Error $\leq N_j\sqrt{B^*_{Q,j}}/e_j=O(a_j^{3/2})$',13,ha='center')
txt(11.53,3.54,'IB36–IB43. No unbounded-operator commutation is used.',10,color='#526278')

box(.6,.72,15.8,2.26,'#ffffff','#cbd5e1')
txt(.91,2.59,'Exact receiving data retained',14,weight='bold')
txt(.94,2.12,r'$\nu_j((s_j,\infty))\leq 27F/(1600a_je_j)=O(a_j)$',14)
txt(.94,1.59,r'$g_{\rm vis}=\sup k^*\mathsf G^+ k$',14)
txt(6.2,2.12,r'$RB^2R-(RBR)^2=K^*K,\quad K=(I-R)B|_{\mathcal H_{\rm rec}}$',14)
txt(6.2,1.58,r'$\lim_{\mathcal U}\operatorname{Cov}(b_Y,\mathcal A/e)=-\operatorname{Cov}_{\Omega}(B,X)$',14)
txt(.94,1.08,'The lower spectral weight is positive at each regulator; no positive limiting variance is assigned.',11,color='#526278')
txt(.62,.32,'Proof: IB17, IB22–IB26, IB36–IB46 in BOUNDED_MULTIPLIER_RECEIVING.md.  Diagram of proved maps; no simulated vacuum law.',10,color='#526278')
fig.savefig(root/'bounded_multiplier_receiving.png',dpi=160)
fig.savefig(root/'bounded_multiplier_receiving.svg')
plt.close(fig)
print('bounded_multiplier_receiving.png and bounded_multiplier_receiving.svg written')
