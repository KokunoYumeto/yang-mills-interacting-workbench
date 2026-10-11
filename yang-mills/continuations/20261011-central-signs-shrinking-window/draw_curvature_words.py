from pathlib import Path
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

ROOT=Path(__file__).resolve().parent
mp.mp.dps=70
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig=plt.figure(figsize=(18,5.2),layout='constrained')
ax=fig.add_subplot(1,3,1,projection='3d')
faces=[];colours=[]
for b in range(2):
    faces.append([(0,b,1),(0,b+1,1),(0,b+1,2),(0,b,2)]);colours.append('#f4bb68')
    ax.text(0,b+.5,1.45,rf'$23,{b}$',ha='center',fontsize=9)
for a in range(3):
    faces.append([(a,2,1),(a+1,2,1),(a+1,2,2),(a,2,2)]);colours.append('#70b2d9')
    ax.text(a+.5,2,1.45,rf'$13,{a}$',ha='center',fontsize=9)
ax.add_collection3d(Poly3DCollection(faces,facecolors=colours,edgecolors='#374151',alpha=.65))
path=np.array([(0,0,0),(0,0,1),(0,2,1),(3,2,1),(3,2,2),(0,2,2),(0,0,2),(0,0,0)])
ax.plot(*path.T,color='#152c52',lw=2)
ax.plot([3,3],[2,2],[1,2],color='#b32626',lw=4)
ax.scatter([0],[0],[0],s=30,color='black')
ax.text(.12,0,.25,r'rooted stem $C_1$',fontsize=9)
ax.text(3,2,2.1,r'$Z_3(3,2,1)$',fontsize=9)
ax.set(xlabel=r'Index $i$',ylabel=r'Index $k$',zlabel=r'Index $l$',xlim=(-.3,3.4),ylim=(-.3,2.5),zlim=(0,2.5),title='Exact bent strip and rooted stem (CW8–CW13)')
ax.set_xticks([0,1,2,3]);ax.set_yticks([0,1,2]);ax.set_zticks([0,1,2]);ax.view_init(elev=23,azim=-55)
ax.text2D(.01,-.06,r'Factor order: $Q_{13,2}Q_{13,1}Q_{13,0}Q_{23,1}Q_{23,0}$',transform=ax.transAxes,fontsize=10)

js=list(range(2,129))
def values(j0):
    # Every sampled point uses an allowed integer on the original path.
    j=mp.mpf(j0);m=2*j**4;n=m+1;h=mp.pi/(2*n);s=mp.sin(h);c=mp.cos(h);C=mp.cot(h)
    alpha=mp.pi/(2*m);bb=mp.pi/n;g2=1/(200*j)
    S1=mp.sqrt(2/n)*C*(C-c);S3=mp.sqrt(2/n)*((2-1/n)*C*C-c*C/n)
    A=mp.cos(n*alpha/2)/mp.sqrt(n)*(mp.csc((alpha+bb)/2)+mp.csc((alpha-bb)/2))
    beta=mp.sqrt(8)*s/(2*g2)
    return [float(4*(1-mp.cos(alpha))/3),float(min(2,6*g2*mp.sqrt(n/m))),float(4*beta*beta*A**4*C**4),float(64*beta*beta*S1*S1*S3*S3)]
vals=np.array([values(j) for j in js])
ax2=fig.add_subplot(1,3,2)
ax2.loglog(js,vals[:,0],lw=2,label=r'Exact configuration $W/M$')
ax2.loglog(js,vals[:,1],'--',label=r'Vacuum mean upper bound in CW14')
ax2.set(xlabel=r'Original path parameter $j$',ylabel='Mean face defect',title=r'Family CW42: small curvature, $\kappa_*=1$')
ax2.legend(fontsize=9);ax2.grid(alpha=.2)
ax3=fig.add_subplot(1,3,3)
ax3.loglog(js,vals[:,2],lw=2,label=r'Exact configuration $F^2$')
ax3.loglog(js,vals[:,3],'--',label=r'Pointwise envelope $4\beta_0^2 U_{\rm point}$')
ax3.set(xlabel=r'Original path parameter $j$',ylabel=r'Original squared phase $F^2$',title=r'The same configurations retain a large odd phase')
ax3.legend(fontsize=9);ax3.grid(alpha=.2)
fig.suptitle('Full rooted transport, signed coefficients, and the curvature-to-phase comparison',fontsize=14)
fig.savefig(ROOT/'CURVATURE_ROOTED_WORDS_FIGURE.png',dpi=160,bbox_inches='tight')
plt.close(fig)
print(ROOT/'CURVATURE_ROOTED_WORDS_FIGURE.png')
