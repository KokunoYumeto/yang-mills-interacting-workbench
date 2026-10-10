"""Reproduce exact two-dimensional sections of the three-dimensional sign map."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

ROOT=Path(__file__).resolve().parent
fig,axs=plt.subplots(1,3,figsize=(16,5.7),gridspec_kw={'width_ratios':[1,1,1.14]})
fig.suptitle('Central link signs: the open construction and the periodic defect',fontsize=17,y=.97)
ax=axs[0]
for y in range(4):
    for x in range(3):
        ax.plot([x,x+1],[y,y],color='#267581',lw=2)
for x in range(4):
    for y in range(3):
        ax.plot([x,x],[y,y+1],color='#af3a42' if x%2 else '#267581',
                linestyle='--' if x%2 else '-',lw=2)
for x in range(3):
    for y in range(3):ax.text(x+.5,y+.5,'−1',ha='center',va='center',fontsize=15)
ax.scatter(*zip(*[(x,y) for x in range(4) for y in range(4)]),s=17,color='#17252b',zorder=3)
ax.set(xlim=(-.25,3.25),ylim=(-.25,3.25),aspect='equal')
ax.set_xticks(range(4));ax.set_yticks(range(4))
ax.set_xlabel(r'$n_1$');ax.set_ylabel(r'$n_2$')
ax.set_title(r'Open slice: $z_1=1,\ z_2=(-1)^{n_1}$',fontsize=12,pad=15)
ax.legend(handles=[Line2D([0],[0],color='#267581',lw=2,label='+1 link'),
                   Line2D([0],[0],color='#af3a42',lw=2,ls='--',label='−1 link')],
          loc='lower center',bbox_to_anchor=(.5,-.27),ncol=2,frameon=False)
ax=axs[1]
for n in range(4):
    ax.plot([0,3],[n,n],color='#6d7981',lw=1.3)
    ax.plot([n,n],[0,3],color='#6d7981',lw=1.3)
for x in range(3):
    for y in range(3):ax.text(x+.5,y+.5,'−1',ha='center',va='center',fontsize=15,color='#af3a42')
ax.annotate('',xy=(2.7,-.18),xytext=(.3,-.18),arrowprops={'arrowstyle':'->','color':'#267581'})
ax.annotate('',xy=(2.7,3.18),xytext=(.3,3.18),arrowprops={'arrowstyle':'->','color':'#267581'})
ax.annotate('',xy=(-.18,2.7),xytext=(-.18,.3),arrowprops={'arrowstyle':'->','color':'#267581'})
ax.annotate('',xy=(3.18,2.7),xytext=(3.18,.3),arrowprops={'arrowstyle':'->','color':'#267581'})
ax.set(xlim=(-.35,3.35),ylim=(-.35,3.35),aspect='equal')
ax.axis('off')
ax.set_title('Periodic 3 × 3 coordinate torus',fontsize=12,pad=15)
ax.text(.5,-.06,'Opposite edges are identified.\nEvery link occurs twice in the face product.',
        transform=ax.transAxes,ha='center',va='top',fontsize=10)
ax.text(.5,-.23,r'Required: $(-1)^9=-1$; actual: $+1$.',
        transform=ax.transAxes,ha='center',va='top',fontsize=11,color='#af3a42')
ax=axs[2];ax.axis('off')
ax.text(.02,.98,'Exact three-dimensional conclusions',fontsize=13,weight='bold',va='top')
rows=[
('Open box','Every side length allowed.\nOne physical sign map.'),
('Periodic box',r'Exists iff each $N_iN_j$ is even.'+'\nAt most one odd side length.'),
('When it exists','Eight physical maps, labelled by\n'+r'$(\omega_1,\omega_2,\omega_3)\in\{+1,-1\}^3$.'),
('Full operator',r'$\mathcal{T}_z H(\xi)\mathcal{T}_z$'+'\n'+r'$=H(-\xi)+4\kappa M\xi I$.'),
]
for y,(title,body) in zip([.84,.64,.42,.20],rows):
    ax.text(.02,y,title,fontsize=11,weight='bold',va='top',color='#267581')
    ax.text(.02,y-.052,body,fontsize=11,va='top',linespacing=1.45)
fig.text(.5,.018,'Exact signs and boundary identifications; no sampled fields. Proof: CS1–CS19 in CENTRAL_SIGNS_AND_BOUNDARIES.md.',
         ha='center',fontsize=10)
fig.subplots_adjust(left=.045,right=.99,top=.84,bottom=.25,wspace=.32)
for ext in ['png','svg']:fig.savefig(ROOT/('CENTRAL_SIGNS_AND_BOUNDARIES.'+ext),dpi=180)
