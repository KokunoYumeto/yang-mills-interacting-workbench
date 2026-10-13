from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import re
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
fig=plt.figure(figsize=(15,12),facecolor='white');ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(.04,.958,'Original gauge covariance, physical norm and dynamic curl',fontsize=22,weight='bold')
ax.text(.04,.928,'Exact maps from GCM1–GCM16; all original edges, transports and gauge zero modes remain.',fontsize=12,color='#34495e')
def box(x,y,w,h,title,lines,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',facecolor=color,edgecolor='#64748b',linewidth=1.2))
    ax.text(x+.014,y+h-.026,title,fontsize=14,weight='bold',va='top')
    yy=y+h-.072
    for text,size in lines:
        text=re.sub(r'\\(mathcal|mathscr|mathbb|mathbf)\s*([A-Za-z0-9])',r'\\\1{\2}',text)
        ax.text(x+.014,yy,text,fontsize=size,va='top');yy-=.041
box(.04,.66,.44,.22,'Actual vertex cross covariance · GCM1–GCM4',[
    (r'$B_Uc=K_U^*D_cg,\quad A_0=\mu B_U^*B_U$',15),
    (r'$A_1=\mu B_U^*(K_U^*K_U)B_U$',15),
    (r'$V_g\ \geq\ a_j^4 A_0A_1^\dagger A_0\ \geq\ a_j^4A_0/12$',15)],'#edf3ff')
box(.52,.66,.44,.22,'Full physical receiver · GCM7–GCM9',[
    (r'$C^*PC+V_g\leq N$',17),
    (r'$\mathcal N_h=M_{\mathbf1_{\mathcal Q}\tau}-\mathcal V_g$',17),
    (r'$\mathcal M([0,\infty])\leq\mathcal N_h$',17)],'#e7f3eb')
box(.04,.38,.44,.22,'Common smooth spatial weight · GCM10–GCM12',[
    (r'$(B_Uc)_v=\sum_{e\ni v}(\varphi(x_e)-\varphi(x_v))j_{ve}$',13),
    (r'$c_e=\varphi(x_e),\quad r_{\rm graph}=\lambda/a_j^2$',15),
    (r'$\zeta_\varphi(\{\infty\})=0$',16)],'#fcf1de')
box(.52,.38,.44,.22,'Individual columns and collective mode · GCM5',[
    (r'$(V_g)_{ee}\geq \frac{2}{7}N_{ee}$',17),
    (r'$V_g\mathbf1=0,\quad PC\mathbf1=C\mathbf1$',17),
    ('The constant identity uses the full original edge list.',11)],'#f4ebf7')
box(.04,.095,.92,.23,'Exact dynamic map · GCM13–GCM16',[
    (r'$\mathscr T L_1-L_0^{\mathbb V}\mathscr T=\kappa_*\mathscr R\,d,\qquad \mathscr R\,dCc=0$',17),
    (r'$\mathscr T(L_1+z)^{-1}Cc=(L_0^{\mathbb V}+z)^{-1}[a_j^2B_Uc-\kappa_*\mathscr R(L_2+z)^{-1}dCc]$',16),
    ('The two-form resolvent can contribute diagonal curl; the full signed combination is retained.',12)],'#e9eef1')
ax.annotate('',(.51,.77),(.493,.77),arrowprops={'arrowstyle':'->','lw':2,'color':'#334155'})
ax.text(.04,.043,r'Physical relative energy remains $\lambda/s_j$, with $s_j=100\kappa_*a_j$. The graph and physical measures are linked by the proved norm and curl maps.',fontsize=11)
ax.text(.04,.018,'The physical window and smooth interacting continuum no-gap construction remain under investigation.',fontsize=11,color='#34495e')
for ext in ['png','svg']:fig.savefig(O/('GAUGE_CURRENT_AND_DYNAMIC_MAP.'+ext),dpi=150)
