"""Exact map schematic for one original face and one adjacent unordered pair."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root = Path(__file__).resolve().parent
fig,ax = plt.subplots(figsize=(12.5,6.1))
ax.set_xlim(0,12); ax.set_ylim(0,6); ax.axis('off')
ax.text(6,5.7,'The original first Jacobian map and its complete face return',
        ha='center',fontsize=16)
ax.text(6,5.3,r'$J_{[1]}=\frac{2}{3}K^{-1}Q_H\Gamma(S,\cdot)$,   $P=\mathbf{1}_{\{3\}}(K)$',
        ha='center',fontsize=14)
def box(x,y,w,h,label,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.04',
                  linewidth=1.3,facecolor=color,edgecolor='#263b4f'))
    ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=12)
def arrow(start,end,label,offset=(0,0.17),color='#274d73'):
    ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','lw':1.7,'color':color})
    ax.text((start[0]+end[0])/2+offset[0],(start[1]+end[1])/2+offset[1],
            label,ha='center',va='center',fontsize=12,color=color,
            bbox={'facecolor':'white','edgecolor':'none','pad':2})

box(.45,2.52,1.3,.85,r'$W_p$'+'\n'+r'$c=3$','#e7f0f7')
box(4.15,3.95,2.2,.72,r'$D_p=\chi_1(U_p),\ c=8$','#f7e9e5')
box(4.15,2.58,2.2,.82,r'$C_{0,pq},\ c=9/2$'+'\n'+r'$\|C_0\|_H^2=1/4$','#e8f3ef')
box(4.15,1.13,2.2,.82,r'$C_{1,pq},\ c=13/2$'+'\n'+r'$\|C_1\|_H^2=3/4$','#e8f3ef')
box(9.42,3.95,1.85,.72,r'$W_p$','#f7e9e5')
box(9.42,2.15,1.85,.82,r'$W_p+W_q$','#e8f3ef')
arrow((1.75,3.18),(4.15,4.25),r'$-1/12$')
arrow((1.75,2.95),(4.15,2.99),r'$1/9$')
arrow((1.75,2.68),(4.15,1.54),r'$-1/39$',offset=(0,-.18))
arrow((6.35,4.31),(9.42,4.31),r'$8/9$',color='#9a3f29')
arrow((6.35,2.99),(9.42,2.73),r'$1/8$')
arrow((6.35,1.54),(9.42,2.39),r'$13/24$',offset=(0,-.19))
ax.text(7.85,3.62,r'Self return: $-2W_p/27$',ha='center',fontsize=12,color='#9a3f29')
ax.text(7.9,.96,r'Pair return: $(1/72-1/72)(W_p+W_q)=0$',
        ha='center',fontsize=12)
ax.text(6,.57,r'$PJ_{[1]}P=0,\qquad PJ_{[1]}^2P=-2P/27,\qquad PJ_{[2]}P=-P/27$',
        ha='center',fontsize=14)
ax.text(6,.12,'Every original adjacent pair is included; both channels keep its seven-edge union label.',
        ha='center',fontsize=11)
fig.tight_layout(pad=.4)
fig.savefig(root/'JACOBIAN_RETURN.png',dpi=180,facecolor='white')
fig.savefig(root/'JACOBIAN_RETURN.svg',facecolor='white')
plt.close(fig)
print('Saved the original Jacobian return PNG and SVG.')
