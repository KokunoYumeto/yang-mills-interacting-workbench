"""Reproducible mathematical diagram for OS1--OS40."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,
                     "mathtext.fontset":"dejavusans"})
fig=plt.figure(figsize=(17,12),facecolor="#fbfcfe")
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
def box(x,y,w,h,fc="#eff5fa",ec="#457093"):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.008",
                 facecolor=fc,edgecolor=ec,linewidth=1.5))
def txt(x,y,t,size=13,color="#18384e",**kw):
    ax.text(x,y,t,fontsize=size,color=color,va="top",**kw)
def arrow(p,q,color="#457093",style="-|>",lw=1.7):
    ax.add_patch(FancyArrowPatch(p,q,arrowstyle=style,mutation_scale=16,
                 linewidth=lw,color=color))
txt(.04,.964,"Actual-source curvature variance",24,weight="bold")
txt(.04,.928,r"Original path: $a_j=(100j)^{-1}$, $g_j^2=\kappa_*a_j/2$, "
    r"$L_j=j^4$, $\kappa_j=\kappa_*$, $b_j=(\kappa_*a_j^2)^{-1}$.",14)
txt(.04,.896,r"Actual vacuum $d\mu_j=\psi_j^2dU$; "
    r"$C_{f,j}=2a_j\sum_p f_p-a_j\sum_p f_pW_p$; all three face orientations.",14)

box(.04,.607,.44,.248)
txt(.056,.850,"Original oriented face and exact Hessian blocks",15,weight="bold")
coords=[(.086,.688),(.239,.688),(.239,.789),(.086,.789)]
for p,q in zip(coords,coords[1:]+coords[:1]):arrow(p,q)
for p in coords:ax.plot(*p,"o",color="#18384e",ms=5)
txt(.139,.675,r"$U_d(z)$",11)
txt(.247,.747,r"$U_e(z+e_d)$",10)
txt(.130,.811,r"$U_d(z+e_e)^{-1}$",10)
txt(.051,.757,r"$U_e(z)^{-1}$",10,rotation=90)
txt(.140,.752,r"$W_p=\mathrm{Tr}\,U_p$",12)
txt(.294,.807,r"$h^{(p)}=\nabla^2D_p$",11)
txt(.294,.781,"4 diagonal edge blocks",10)
txt(.294,.759,r"$h^{(p)}_{e\alpha,e\beta}=W_p\delta_{\alpha\beta}/4$",10)
txt(.294,.737,"12 ordered mixed blocks",11)
txt(.294,.714,r"$\|h^{(p)}_{e,e'}\|^2=1/2+W_p^2/16$",10)
txt(.057,.644,r"$\|\nabla^2C_f\|^2\leq 21a^2\sum_p f_p^2$  (OS22–OS24)",14)

box(.515,.607,.445,.248)
txt(.533,.850,"Full radius-two product geometry",15,weight="bold")
txt(.533,.811,r"$\mathrm{Ric}=\frac{1}{2}g,\quad R(v,z,v,z)\geq 0,\quad \nabla\mathrm{Ric}=0$",15)
txt(.533,.768,r"$\nabla^2V\leq 8b\,g$ with every boundary incidence",14)
txt(.533,.725,r"$\nabla^2\log\psi\geq -2\sqrt{b/\kappa}\,g$",19,weight="bold")
txt(.533,.680,"Minimum eigenvalue in the full differentiated",12)
txt(.533,.655,"ground equation; all curvature terms retained (OS18–OS21).",12)
arrow((.27,.593),(.39,.565));arrow((.735,.593),(.61,.565))

box(.09,.368,.82,.181,fc="#edf8f1",ec="#39725a")
txt(.111,.532,"Two actual energy moments at source zero",16,weight="bold")
txt(.111,.493,r"$0<e_f\leq \liminf E_{f,j},\qquad"
    r"\limsup a_jE_{2,f,j}\leq  D_f$",20)
txt(.111,.450,r"$E_f=\langle u_f,(H-\mathcal{E})u_f\rangle,\quad"
    r"E_{2,f}=\|(H-\mathcal{E})u_f\|^2,\quad u_f=(C_f-\mu C_f)\psi$",13)
txt(.111,.412,r"$e_f=81\kappa_*^3(\int|f|)^2/\mathcal{K}_R,\quad"
    r"D_f=63\kappa_*^2\int f^2+64\kappa_*\|f\|_\infty^2\mathcal{K}_R$",13)
txt(.111,.385,r"$\mathcal{K}_R=\mathfrak{d}_R^+<9\kappa_*R^3+24R^2$; sign weights remove cancellation in $f$ (OS11–OS27).",11)
arrow((.30,.355),(.27,.320));arrow((.71,.355),(.74,.320))

box(.04,.111,.445,.201,fc="#edf8f1",ec="#39725a")
txt(.057,.296,"Proved receiving bounds",15,weight="bold")
txt(.057,.261,r"$\liminf G_{f,j}/a_j\geq  e_f^2/D_f>0$",19)
txt(.057,.219,r"$\liminf\,\nu_{f,j}((0,\mathcal{R}/a_j])/a_j\geq e_f^2/D_f$",13)
txt(.057,.191,r"for $\mathcal{R}>2D_f/e_f$; the original energy window grows.",11)
txt(.057,.164,r"At original time $t=\tau a_j$: covariance loss$/a_j$",12)
txt(.057,.139,r"has lower limit $\geq \tau e_f-\tau^2D_f/2$ (OS28–OS32).",12)

box(.515,.111,.445,.201,fc="#fff7ea",ec="#b5823d")
txt(.533,.296,"Upper variance: remaining actual term",15,weight="bold")
txt(.533,.261,r"$\phi_f=(-\mathscr{L})^{-1}(C_f-\mu C_f)$",17)
txt(.533,.222,r"$G_f=\mu\|\nabla^2\phi_f\|^2+\frac{1}{2}\mu|\nabla\phi_f|^2$",13)
txt(.533,.192,r"$\qquad-2\mu\,\nabla^2\log\psi(\nabla\phi_f,\nabla\phi_f)$",13)
txt(.533,.154,"The proved lower Hessian bound gives no positive",11)
txt(.533,.132,"coercivity bound for this tensor (OS34–OS40).",11)
txt(.04,.076,"Proof: ORIGINAL_SOURCE_COVARIANCE.md, OS1–OS40. This diagram displays proved inequalities, not a simulated vacuum.",11)
txt(.04,.054,"Human source: Ascione, Castorina, Catino, Mantegazza, arXiv:2107.13846v1, Section 2; the full stationary",10)
txt(.04,.036,"curvature calculation is independently proved in OS18–OS21. Original spatial Hamiltonian: retained programme TeX, §12, (93)–(100).",10)
fig.savefig(HERE/"original_source_covariance.png",dpi=180)
fig.savefig(HERE/"original_source_covariance.svg")
print("Rendered original_source_covariance.png and .svg")
