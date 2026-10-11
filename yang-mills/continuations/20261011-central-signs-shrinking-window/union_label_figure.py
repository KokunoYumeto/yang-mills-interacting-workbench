from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'mathtext.fontset':'dejavusans','svg.hashsalt':'union-label-20261011'})
fig=plt.figure(figsize=(14,9),facecolor='#f8fafc')
ax=fig.add_axes([.03,.52,.94,.43]);ax.set_xlim(0,14);ax.set_ylim(0,4);ax.axis('off')
fig.suptitle('The full labelled inverse and its exact connected vacuum terms',fontsize=19,y=.987)
def box(x,y,w,h,title,body,color):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',facecolor=color,edgecolor='#334155',lw=1.2))
 ax.text(x+w/2,y+h-.3,title,ha='center',va='center',fontsize=14,fontweight='bold')
 ax.text(x+w/2,y+.64,body,ha='center',va='center',fontsize=12,linespacing=1.6)
box(.25,1.4,3.7,1.65,'Original labels',r'$F_S\in Y_1(S)$'+'\nEvery nonempty '+r'$S\subseteq E$','#e0f2fe')
box(5.05,1.4,3.8,1.65,'Cumulative coordinates',r'$G_A=\sum_{S\subseteq A}F_S$'+'\n'+r'$G_A\in Y_1(A)$','#dcfce7')
box(10.0,1.4,3.7,1.65,'Physical inverses',r'$G_A\longmapsto\mathscr{L}_A^{-1}G_A$'+'\nOne exact inverse for every '+r'$A$','#fef3c7')
for a,b,label in [(4.1,4.87,r'$\zeta$'),(9.0,9.81,r'$\operatorname{diag}(\mathscr{L}_A^{-1})$')]:
 ax.add_patch(FancyArrowPatch((a,2.15),(b,2.15),arrowstyle='-|>',mutation_scale=18,lw=1.8,color='#334155'))
 ax.text((a+b)/2,3.3,label,ha='center',fontsize=13)
ax.text(7,.78,r'$\mathfrak{L}_x^{-1}=\mathfrak{m}\,\operatorname{diag}(\mathscr{L}_A^{-1})\,\zeta$',ha='center',fontsize=20)
ax.text(7,.23,r'All relation directions remain:  $\zeta(\ker\mathsf{a})=\{G:G_E=0\}$   (UL34–UL39)',ha='center',fontsize=12)
geo=fig.add_axes([.07,.115,.4,.35]);geo.set_aspect('equal');geo.set_xlim(-.5,2.5);geo.set_ylim(-.5,1.5);geo.axis('off')
geo.fill([0,1,1,0],[0,0,1,1],color='#dbeafe');geo.fill([1,2,2,1],[0,0,1,1],color='#fef3c7')
edges={'a':((0,0),(1,0)),'b':((1,0),(1,1)),'c':((0,1),(1,1)),'d':((0,0),(0,1)),'e':((1,0),(2,0)),'f':((2,0),(2,1)),'g':((1,1),(2,1))}
offset={'a':(0,-.16),'b':(.14,0),'c':(0,.16),'d':(-.14,0),'e':(0,-.16),'f':(.14,0),'g':(0,.16)}
for label,(start,end) in edges.items():
 color='#be123c' if label=='b' else '#334155'
 geo.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=16,lw=2,color=color))
 dx,dy=offset[label];geo.text((start[0]+end[0])/2+dx,(start[1]+end[1])/2+dy,label,ha='center',va='center',color=color,fontsize=14)
geo.text(.5,.5,r'$p$',ha='center',fontsize=22);geo.text(1.5,.5,r'$q$',ha='center',fontsize=22)
for x in range(3):
 for y in range(2):geo.plot(x,y,'o',color='#0f172a',ms=4)
geo.text(1,1.42,'Two actual adjacent faces, with positive edge orientations',ha='center',fontsize=12)
geo.text(1,-.43,r'$p=(0;1,2),\quad q=(e_1;1,2)$',ha='center',fontsize=13)
txt=fig.add_axes([.52,.105,.45,.38]);txt.axis('off')
txt.text(0,.94,'Every other face source is zero; the full kinetic operator remains.',fontsize=12)
txt.text(0,.73,r'$P=\{a,b,c,d\},\quad Q=\{b,e,f,g\},\quad U=P\cup Q$',fontsize=14)
txt.text(0,.52,r'$V_P=v_P,\qquad V_Q=v_Q$',fontsize=17)
txt.text(0,.29,r'$V_U=v_U-v_P-v_Q$',fontsize=20,color='#9f1239')
txt.text(0,.075,'The shared-edge interaction stays in its complete union label.\nThe same identity retains energy and normalization scalars (UF10–UF13).',fontsize=12,linespacing=1.6)
fig.text(.5,.035,'Disconnected face unions have zero connected coefficient by exact product factorization (UF1–UF9).\nThese are finite-volume identities; quantitative bounds for the limit remain to be calculated.',ha='center',fontsize=11,color='#475569')
for ext in ['png','svg']:
 fig.savefig(ROOT/f'FULL_UNION_LABEL_INVERSE.{ext}',dpi=180,facecolor=fig.get_facecolor(),metadata={'Creator':'Matplotlib'})
plt.close(fig)
