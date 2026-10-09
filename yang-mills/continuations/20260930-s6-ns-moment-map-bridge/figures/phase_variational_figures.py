"""Exact original face filling and phase/Hamiltonian maps, PK177a–PK206."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
ROOT=Path(__file__).resolve().parent
plt.rcParams.update({"font.size":12,"mathtext.fontset":"dejavusans"})
fig=plt.figure(figsize=(14,7.8))
ax=fig.add_axes([.025,.18,.46,.68],projection="3d")
faces13=[[(a,2,1),(a+1,2,1),(a+1,2,2),(a,2,2)] for a in range(3)]
faces23=[[(0,b,1),(0,b+1,1),(0,b+1,2),(0,b,2)] for b in range(2)]
ax.add_collection3d(Poly3DCollection(faces13,facecolors="#8acbd0",edgecolors="#185e63",alpha=.65))
ax.add_collection3d(Poly3DCollection(faces23,facecolors="#f2c28a",edgecolors="#9c5814",alpha=.7))
path=[(0,0,1),(0,2,1),(3,2,1),(3,2,2),(0,2,2),(0,0,2),(0,0,1)]
ax.plot(*zip(*path),color="#9b253c",lw=3)
for start,end in zip(path,path[1:]):
    delta=[end[i]-start[i] for i in range(3)]
    mid=[start[i]+.40*delta[i] for i in range(3)]
    ax.quiver(*mid,*[.22*x for x in delta],color="#9b253c",
              linewidth=1.8,arrow_length_ratio=.45)
ax.plot([0,0],[0,0],[0,1],color="#475569",ls="--",lw=2)
ax.scatter([0],[0],[0],color="#475569",s=32)
ax.text(.08,-.2,0,"root",fontsize=11)
ax.text(3.05,2.05,1.48,"chord",fontsize=11,color="#9b253c")
ax.set(xlim=(-.2,3.5),ylim=(-.4,2.7),zlim=(-.1,2.7),
       xlabel=r"$l_1$",ylabel=r"$l_2$",zlabel=r"$l_3$")
ax.set_xticks(range(4));ax.set_yticks(range(3));ax.set_zticks(range(3))
ax.view_init(elev=24,azim=-57);ax.set_box_aspect((3.5,2.7,2.8))
fig.suptitle("Every face in the original rooted chord",fontsize=19,y=.96)
fig.text(.50,.83,"Shown exactly: direction-three chord at (3, 2, 1)",fontsize=14,weight="bold")
fig.text(.50,.755,r"$\mathcal{F}(c_3)=\{(a,2,1;13):a=0,1,2\}$",fontsize=14)
fig.text(.50,.695,r"$\qquad\qquad\cup\ \{(0,b,1;23):b=0,1\}$",fontsize=14)
fig.text(.50,.60,"Three cyan faces + two orange faces = 5 faces.\n"
         "The dashed root segment stays in the conjugating word.\n"
         "Face attachment fixes the factor order and orientations.",fontsize=12,linespacing=1.7)
fig.text(.50,.44,r"$W_{\mu p}=\sum_{c:\,p\in\mathcal{F}(c)}|\mathsf{M}_{\mu c}|$",fontsize=16)
fig.text(.50,.35,r"$|u_\mu|^2\leq4T_\mu\sum_p W_{\mu p}(2-W_p)$",fontsize=16)
fig.text(.50,.255,r"$T_1=\frac{mC^2}{\sqrt{2n}},\quad T_3=3T_1,\quad C=\cot\frac{\pi}{2n}$",fontsize=16)
fig.text(.055,.115,r"$m=4,\ L=2,\ n=5$ in the drawing. Original physical coordinates: $o+a(l_1-L,l_2-L,l_3-L)$.",fontsize=12)
fig.text(.055,.055,"PK177a–PK177f prove the ordered non-Abelian filling, all face weights and the actual-vacuum bound.\n"
         "The bound retains every face and boundary term; it does not settle the original-path fourth-moment growth.",fontsize=11,color="#334155")
for ext in ["png","svg"]:fig.savefig(ROOT/("ORIGINAL_CHORD_FACE_FILLING."+ext),dpi=170)
plt.close(fig)

fig=plt.figure(figsize=(14,10))
fig.suptitle("Full reflection, amplitude limits and the next variational space",fontsize=18,y=.975)
ax=fig.add_axes([.04,.52,.43,.38]);ax.axis("off")
ax.set(xlim=(0,1),ylim=(0,1))
ax.text(.03,.97,"Exact two-link configuration (all other links I)",fontsize=13,weight="bold")
for row,labels,title in [(.68,["I","-I",r"$h=2T_1$"],r"$U$"),
                         (.33,[r"$h=2T_1$","-I","I"],r"$\mathcal{R}U$")]:
    ax.text(.01,row+.05,title,fontsize=16)
    for x,label,index in zip([.2,.5,.8],labels,["0","L","m"]):
        ax.annotate("",(x,row+.16),(x,row-.02),arrowprops={"arrowstyle":"->","lw":2,"color":"#185e93"})
        ax.text(x,row+.2,label,ha="center",fontsize=14)
        ax.text(x,row-.1,r"$l_1="+index+"$",ha="center",fontsize=11)
ax.text(.1,.105,r"Direction-two links $(l_1,0,0;2)$; $m=2L$.",fontsize=11)
ax.text(.1,.005,r"$p(U)=4\beta_0d_0^2,\quad r(U)=-12\beta_0d_0^2$",fontsize=14)
bx=fig.add_axes([.53,.52,.43,.38]);bx.axis("off")
bx.text(0,.97,"The iterated limits differ (fixed L and a)",fontsize=13,weight="bold")
bx.text(.08,.72,r"$\Gamma_g(A)$",fontsize=22)
bx.annotate("",(.75,.74),(.37,.74),arrowprops={"arrowstyle":"->","lw":1.7})
bx.text(.45,.81,r"$A\to\infty$",fontsize=14)
bx.text(.80,.70,r"$1/4$",fontsize=22,color="#185e93")
bx.annotate("",(.20,.22),(.20,.59),arrowprops={"arrowstyle":"->","lw":1.7})
bx.text(.01,.4,r"$g\downarrow0$",fontsize=13)
bx.text(.04,.10,r"$\frac{1}{2}[1-(1+4A^2)^{-3/2}]$",fontsize=18)
bx.annotate("",(.90,.20),(.69,.20),arrowprops={"arrowstyle":"->","lw":1.7})
bx.text(.70,.27,r"$A\to\infty$",fontsize=11)
bx.text(.87,.12,r"$1/2$",fontsize=19,color="#9b253c")
cx=fig.add_axes([.055,.16,.9,.29]);cx.axis("off")
cx.text(0,.94,"Actual phase space and the full Hamiltonian action",fontsize=14,weight="bold")
cx.text(.01,.66,r"$(\mathcal{Q}_L,\mu=\psi_g^2dU)$",fontsize=18)
cx.annotate("",(.50,.69),(.33,.69),arrowprops={"arrowstyle":"->","lw":1.7})
cx.text(.345,.80,r"$\Theta=(p,r)$",fontsize=14)
cx.text(.54,.66,r"$(K,\rho=\Theta_*\mu)$",fontsize=18)
cx.text(.01,.37,r"$Jf=\psi_g f(p,r)$",fontsize=18)
cx.text(.36,.37,r"$\mathcal{A}Jf=J(B_{\rm ph}f)+\psi_g R_f$",fontsize=18)
cx.text(.01,.08,r"$m_0=\int|f|^2d\rho,\qquad"
         r"m_1=\kappa\int\sum_{i,j=1}^{2}a_{ij}\overline{f_i}f_j\,d\rho$",fontsize=17)
fig.text(.065,.107,r"$m_2=\int|B_{\rm ph}f|^2d\rho+\int|R_f|^2d\mu,\qquad"
         r"\mathbb{E}_\mu[R_f\mid\Theta]=0$",fontsize=17)
fig.text(.065,.037,"PK178–PK206 contain the complete proofs. High-amplitude raw mass survives but escapes every bounded energy interval.\n"
         "The phase form and finite polynomial matrices retain the actual vacuum and the entire residual interaction.",fontsize=11,color="#334155")
for ext in ["png","svg"]:fig.savefig(ROOT/("ACTUAL_PHASE_VARIATIONAL_MAP."+ext),dpi=170)
plt.close(fig)

import numpy as np
fig,axes=plt.subplots(1,2,figsize=(14,8))
fig.subplots_adjust(left=.075,right=.965,top=.78,bottom=.32,wspace=.30)
fig.suptitle("An exact rank-two section of the actual phase image",fontsize=19,y=.96)
fig.text(.5,.88,r"Displayed original regulator: $L=2,\ a=1,\ g=1,\ n=5$; no phase coordinate rescaling.",ha="center",fontsize=12)
n=5;beta=np.sqrt(8)*np.sin(np.pi/10)/2
d2=2*np.cos(np.pi/10)**2*np.sin(np.pi/5)**2/5**3
tt=np.linspace(np.pi/2-.25,np.pi/2+.25,121)
ss=np.linspace(np.pi-.25,np.pi+.25,121)
def mapping(t,s):
    u=2*np.sin(t/2);v=2*np.sin(s/2);w=2*np.sin((s-t)/2)
    return beta*d2*u*(u+v),-beta*d2*u*(2*u+w)
for t in np.linspace(tt[0],tt[-1],9):
    axes[0].plot(np.full_like(ss,t),ss,color="#185e93",lw=1)
    axes[1].plot(*mapping(t,ss),color="#185e93",lw=1)
for s0 in np.linspace(ss[0],ss[-1],9):
    axes[0].plot(tt,np.full_like(tt,s0),color="#9b253c",lw=1)
    axes[1].plot(*mapping(tt,s0),color="#9b253c",lw=1)
axes[0].scatter([np.pi/2],[np.pi],color="black",s=26,zorder=5)
axes[1].scatter(*mapping(np.pi/2,np.pi),color="black",s=26,zorder=5)
axes[0].set(xlabel=r"$t$ in $h(t)=\exp(tT_1)$",ylabel=r"$s$ in $k(s)=\exp(sT_1)$",title="A patch of the two original group circles")
axes[1].set(xlabel=r"$p=\beta_0d_0^2 u(u+v)$",ylabel=r"$r=-\beta_0d_0^2 u(2u+w)$",title="Its exact phase image")
for ax in axes:ax.spines[["top","right"]].set_visible(False)
fig.text(.075,.23,r"$u=2\sin(t/2),\quad v=2\sin(s/2),\quad w=2\sin((s-t)/2),\qquad"
         r"\det D_{(t,s)}(p,r)|_{(\pi/2,\pi)}=-(2+\sqrt{2})\beta_0^2d_0^4\neq0$",fontsize=13)
fig.text(.075,.14,r"$d\rho=\varpi\,dx\,dy,\qquad a>0\ \ \rho\mathrm{-a.e.},\qquad"
         r"\varpi B_{\rm ph}f=-\kappa\sum_{i,j=1}^{2}\partial_j(\varpi a_{ij}f_i)"
         r"\ \ \mathrm{in}\ \mathcal{D}'(\mathbb{R}^2)$",fontsize=15)
fig.text(.075,.05,"PK203–PK206 prove full rank, actual density, positive finite Gram matrices and the distributional identity.\n"
         "The grids evaluate the exact two-link map. They do not depict a computed vacuum density; all phase-boundary terms remain.",fontsize=11,color="#334155")
for ext in ["png","svg"]:fig.savefig(ROOT/("ACTUAL_PHASE_RANK_AND_BOUNDARY."+ext),dpi=170)
