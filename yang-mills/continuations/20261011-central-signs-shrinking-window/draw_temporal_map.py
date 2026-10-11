"""Reproducible mathematical receiving-map figure for the local AT derivation."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

root=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"mathtext.fontset":"dejavusans"})
fig,ax=plt.subplots(figsize=(14,11))
ax.set(xlim=(0,14),ylim=(0,11));ax.axis("off")
fig.patch.set_facecolor("#f7f8fa")
ax.text(.4,10.65,"The exact temporal receiving map",fontsize=23,weight="bold",color="#122b47")
ax.text(.4,10.18,"Original open SU(2) box, every face, radius-two electric metric and raw phase",fontsize=12.5,color="#435365")

def box(x,y,w,h,title,body,color="#dceaf7"):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.16",linewidth=1.2,
                               edgecolor="#49657d",facecolor=color))
    ax.text(x+.13,y+h-.18,title,va="top",fontsize=11.1,weight="bold",color="#122b47")
    ax.text(x+.13,y+h-.62,body,va="top",fontsize=10.7,linespacing=1.65,color="#1e3449")
def arrow(a,b,label=None,xy=None):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=17,linewidth=1.7,color="#3d5f7d"))
    if label:ax.text(*xy,label,ha="center",fontsize=10.5,color="#3d5f7d")

box(.45,7.35,5.55,2.3,"Finite anisotropic Wilson integral  |  AT7, AT17–19",
    r"$\beta_t=1/(\kappa\epsilon),\quad\beta_s=\epsilon b$"+"\n"+
    "All temporal vertex Haar integrals; all spatial faces.\n"+
    "Open time: half spatial weight at both endpoints.\n"+
    r"$P_e=U_eq_t(U'_e)^{-1}q_s^{-1}$")
box(7.6,7.35,5.9,2.3,"Exact physical transfer  |  AT8–11, AT16–20",
    r"$\mathcal{T}_\epsilon^{raw}=z(\beta_t)^N T_\epsilon P_G$"+"\n"+
    r"$T_\epsilon=e^{-\epsilon V/2}\mathcal{W}_\epsilon e^{-\epsilon V/2}$"+"\n"+
    r"$z=e^{-2\beta_t}I_1(2\beta_t)/\beta_t$"+"\n"+
    r"$r_l=I_{l+1}(2\beta_t)/I_1(2\beta_t),\quad l=0,1,\ldots$")
arrow((6.2,8.5),(7.35,8.5),"exact", (6.77,8.76))
box(.45,4.6,5.55,1.85,"Original Hamiltonian and state  |  AT2–6, AT38–39",
    r"$H=\kappa K+b\sum_p(2-\mathrm{Tr}\,U_p)$"+"\n"+
    r"$H\psi=E_0\psi,\quad\|\psi\|=1,\quad\psi>0$"+"\n"+
    r"$F=\beta_0(S-S_{\mathcal{R}}),\quad G=\|F\psi\|^2$")
box(7.6,4.6,5.9,1.85,"Quantified product limit  |  AT30–32",
    r"$\|(T_\epsilon^q-e^{-q\epsilon H})f\|$"+"\n"+
    r"$\qquad\leq(q\epsilon)\epsilon C_{\mathrm{tr}}$"+
    r"$\,(\|f\|+\|H^2f\|)$"+"\n"+
    "Explicit constants keep the full original box.")
arrow((10.5,7.15),(10.5,6.66),"compact-kernel moments + full graph bounds",(10.5,6.93))
arrow((7.35,5.5),(6.2,5.5))
box(.45,1.72,5.55,1.95,"Constant boundary vacuum filter  |  AT41–53",
    r"$R_{\epsilon,B}(t)=$ finite Wilson expectation"+"\n"+
    r"of $F(U_r)F(U_{r+q})$,  $B=r\epsilon,\ t=q\epsilon$."+"\n"+
    r"$|R_{\epsilon_j,B_j}(t)-\langle F_j\psi_j,$"+"\n"+
    r"$e^{-t(H_j-E_{0,j})}F_j\psi_j\rangle|\leq\zeta_j$"+
    "  (grid times)")
box(7.6,1.72,5.9,1.95,"Original shrinking-window certificate  |  AT54–60",
    r"$|\mathcal{E}_j^{lat}-(G_j-C_{F,j}/s_j)|\leq3/(4j)$"+"\n"+
    r"$\nu_{F_j\psi_j}((0,s_j])\geq$"+"\n"+
    r"$\qquad\max\{0,\mathcal{E}_j^{lat}-3/(4j)\}$"+"\n"+
    "The actual endpoint sign remains unevaluated.",color="#e1f0e8")
arrow((3.2,4.39),(3.2,3.9),"explicit heat filter: positive finite-box gap",(3.2,4.15))
arrow((10.5,4.39),(10.5,3.9),"unchanged path + explicit temporal sequence",(10.5,4.15))
arrow((6.2,2.7),(7.35,2.7),"probe", (6.77,2.96))
ax.text(.45,.99,r"Unchanged: $L_j=j^4,\ a_j=(100j)^{-1},\ g_j^2=\kappa_*/(200j),\ s_j=\kappa_*/j$.",
        fontsize=12,color="#122b47")
ax.text(.45,.51,"Proof: ANISOTROPIC_TEMPORAL_BRIDGE.md, AT1–60. Arrows show proved maps and bounds, not sampled data.",
        fontsize=10.6,color="#435365")
ax.text(.45,.12,"Existing source: Exact SU(2) Wilson transfer operator and the finite-spatial-lattice time limit (8 September 2026).",
        fontsize=10.3,color="#435365")
fig.savefig(root/"TEMPORAL_RECEIVING_MAP.png",dpi=160,bbox_inches="tight",facecolor=fig.get_facecolor())
fig.savefig(root/"TEMPORAL_RECEIVING_MAP.svg",bbox_inches="tight",facecolor=fig.get_facecolor())
print(root/"TEMPORAL_RECEIVING_MAP.png")
