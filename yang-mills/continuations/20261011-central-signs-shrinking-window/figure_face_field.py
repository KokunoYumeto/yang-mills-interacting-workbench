from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
O=Path(__file__).resolve().parent
fig=plt.figure(figsize=(13,7),facecolor='#f7f9fa')
fig.text(.045,.93,'Central parity isolates the physical face action',fontsize=22,weight='bold',color='#17334c')
ax=fig.add_axes([.015,.23,.45,.65],projection='3d')
p=np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0],[0,0,0]])
q=np.array([[0,0,0],[1,0,0],[1,0,1],[0,0,1],[0,0,0]])
for v in [p,q]:
    for i in range(1,4):ax.plot(*v[i:i+2].T,color='#cf681e',lw=3.5)
ax.plot([0,1],[0,0],[0,0],color='#6255a1',lw=5)
ax.text(.48,-.23,.22,'g: even',color='#6255a1',fontsize=12)
ax.text(.5,.6,0,'p',fontsize=17);ax.text(.5,0,.65,'q',fontsize=17)
for v in np.unique(np.concatenate([p,q]),axis=0):ax.scatter(*v,color='#17334c',s=20)
ax.set(xlabel='integer offset 1',ylabel='integer offset 2',zlabel='integer offset 3',xticks=[0,1],yticks=[0,1],zticks=[0,1])
ax.view_init(elev=23,azim=-57);ax.set_box_aspect((1,1,1))
fig.text(.50,.79,r'$Y_cD_q=\sum_{p\ne q,\ p\cap q=\{g\}}(c_g-\bar c_p)\,\theta_{pq,g}$',fontsize=17)
fig.text(.50,.69,'Six orange edges: odd central character\nShared purple edge: even central character',fontsize=13,linespacing=1.7)
fig.text(.50,.53,r'$\int\theta_{pq,g}^2\,dU=3/16$',fontsize=21)
fig.text(.50,.44,r'$\mathcal{F}_{\rm Haar}(c,c)=\frac{3}{16}\sum_{p,g\in p}(m_g-1)|c_g-\bar c_p|^2$',fontsize=16)
fig.text(.50,.34,'Kernel: exactly constant original coefficients.',fontsize=13,weight='bold')
fig.text(.05,.18,r'Actual state:  $\mu(\theta_{pq,g}\theta_{rq,h})=\int\theta_{pq,g}\theta_{rq,h}\,\Pi_{\partial p\triangle\partial r}(\psi^2)\,dU$',fontsize=17)
fig.text(.05,.09,r'Physical vertices: $o+a_j(z-L_j\mathbf{1})$. Diagram labels are integer offsets in $z$.',fontsize=12)
fig.text(.05,.04,'Exact geometry and identity map; no vacuum sample. Proof: FPA1–FPA8. Original words: SF1–SF5.',fontsize=11,color='#4a5c69')
for ext in ['png','svg']:fig.savefig(O/('FACE_FIELD_PARITY_MAP.'+ext),dpi=170,bbox_inches='tight')
