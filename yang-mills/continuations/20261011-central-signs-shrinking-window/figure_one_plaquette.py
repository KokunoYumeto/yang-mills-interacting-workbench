from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(12,10));fig.patch.set_facecolor('#f6f8fb');ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.04,.958,'An exact mixed sign in the one-plaquette Wilson model',fontsize=20,weight='bold',color='#16334a')
ax.text(.04,.92,'Four radius-two links • all 16 signs • actual Wilson potential • complete physical domain',fontsize=12,color='#42586b')
def box(x,y,w,h,title,lines):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',fc='white',ec='#9bb1c5',lw=1.3))
    ax.text(x+.018,y+h-.03,title,fontsize=15,weight='bold',color='#16334a',va='top')
    for i,line in enumerate(lines):ax.text(x+.018,y+h-.09-.05*i,line,fontsize=15,color='#172c3c',va='top')
box(.04,.65,.92,.23,'Original ground equation and differentiated receiving map  [OPC1–OPC3]',[
    r'$H_{□}\psi=-\kappa_*[(4-T^2)\psi^{\prime\prime}-3T\psi^\prime]+(2b-bT)\psi=E_{□}\psi$',
    r'$T=2x_6:\ S^5\to[-2,2],\qquad \Delta_{S^5}(F\circ T)=[(4-T^2)F^{\prime\prime}-5TF^\prime]\circ T$',
    r'Positive source $b\psi$ in the differentiated equation gives $\psi^\prime>0$.'])
box(.04,.36,.44,.23,'Conditional geometry  [OPC4, OPC8]',[
    r'$r=\tanh(w(T)-w(-T)),\quad r^\prime>0$',
    r'$C=1-r^2>0,\quad w=\log\psi$',
    'All 15 covariance directions retained.'])
box(.53,.36,.43,.23,'Physical hemisphere  [OPC5–OPC6]',[
    r'$c(-T)=-c(T),\qquad c(0)=0$',
    r'$0<T<2:\quad (f_{z,1}^0)^\prime<0$',
    r'$e^{-tD_C}$ preserves strict signs.'])
ax.annotate('',xy=(.525,.475),xytext=(.49,.475),arrowprops=dict(arrowstyle='->',lw=2,color='#1b6b83'))
box(.04,.06,.92,.24,'The complete original mixed correlation  [OPC7]',[
    r'$\beta_{z,1}=-\kappa_*C^{-1}(4-T^2)r^\prime(f_{z,1}^0)^\prime>0,\qquad d_1^X=-aT/2<0$',
    r'$\langle Bf_{z,\varphi}^0,e^{-tD}y_\varphi\rangle=2|\varphi|^2\int_0^2 A^2C\,\beta_{z,1}(e^{-tD_C}d_1^X)\frac{\sqrt{4-T^2}}{2\pi}\,dT<0$',
    r'Every $z>0$, $t\geq0$, $\varphi\neq0$; the same sign holds after Laplace integration.'])
ax.text(.04,.018,'The sphere is an exact receiving map for the derivative equation. Full-lattice and continuum extension remains a separate calculation.',fontsize=10.6,color='#42586b')
fig.subplots_adjust(left=.01,right=.99,top=.99,bottom=.01)
for ext in ['png','svg']:fig.savefig(O/f'ACTUAL_ONE_PLAQUETTE_SIGN.{ext}',dpi=180,facecolor=fig.get_facecolor())
plt.close(fig)
