from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from itertools import product
ROOT=Path(__file__).resolve().parent
fig=plt.figure(figsize=(14,6));ax=fig.add_subplot(121,projection='3d')
for p in product([0,1],repeat=3):
 for i in range(3):
  if p[i]==0:
   q=list(p);q[i]=1;ax.plot([p[0],q[0]],[p[1],q[1]],[p[2],q[2]],color='#536570',lw=1.5)
for z,color in [(0,'#267581'),(1,'#9a6b3f')]:
 ax.add_collection3d(Poly3DCollection([[(0,0,z),(1,0,z),(1,1,z),(0,1,z)]],facecolors=color,alpha=.28,edgecolors=color,linewidths=2))
ax.text(.5,.5,0,r'$p$',fontsize=18);ax.text(.5,.5,1,r'$q$',fontsize=18)
ax.set(xlabel=r'$n_1$',ylabel=r'$n_2$',zlabel=r'$n_3$',xticks=[0,1],yticks=[0,1],zticks=[0,1]);ax.set_box_aspect([1,1,1]);ax.view_init(elev=22,azim=-55)
ax.set_title('Opposite faces of one original cube',fontsize=13,pad=18)
ax.text2D(.5,-.10,r'$S_{[4],pq}=-24h_e-3d=-90491/9856080$',transform=ax.transAxes,ha='center',fontsize=12)
ax.text2D(.5,-.18,'Four side-face paths and the full cube contribution.',transform=ax.transAxes,ha='center',fontsize=10)
ax=fig.add_subplot(122);ax.axis('off');ax.set_title('Exact finite-boundary asymmetry',fontsize=13,pad=18)
rows=[(r'$p=(-2,-2,-2;0,1)$',r'$d_p=6$'),(r'$q=(-1,-2,-2;1,2)$',r'$d_q=10$'),
 (r'$S_{[4],pq}$',r'$-976543/111702240$'),(r'$S_{[4],qp}$',r'$-2977433/335106720$'),
 (r'$S_{[4],pq}-S_{[4],qp}$',r'$703/4928040$')]
for y,(a,b) in zip([.90,.76,.57,.43,.29],rows):
 ax.text(.0,y,a,fontsize=13,va='top');ax.text(.99,y,b,fontsize=13,ha='right',va='top',color='#267581')
ax.text(.5,.09,r'$S_{[4]}-S_{[4]}^T=-\frac{703}{19712160}(D_{\rm deg}A_{\rm adj}-A_{\rm adj}D_{\rm deg})$',ha='center',fontsize=13)
fig.suptitle('The original fourth Jacobian return: cube coupling and boundary defect',fontsize=15,y=.98)
fig.text(.5,.055,r'All eight return words retained. Uniform Haar coefficient bound: $\|S_{[4]}\|\leq 4574447/33510672$.',ha='center',fontsize=11)
fig.text(.5,.018,'Exact coordinate geometry and rational entries. Proof: Q7, Q28, Q30–Q35. This is the auxiliary Jacobian coefficient.',ha='center',fontsize=10)
fig.subplots_adjust(left=.035,right=.97,top=.83,bottom=.25,wspace=.22)
for ext in ['png','svg']:
 p=ROOT/('FOURTH_SCHUR.'+ext);fig.savefig(p,dpi=180)
 if ext=='svg':p.write_text('\n'.join(x.rstrip() for x in p.read_text().splitlines())+'\n',encoding='utf-8',newline='\n')
