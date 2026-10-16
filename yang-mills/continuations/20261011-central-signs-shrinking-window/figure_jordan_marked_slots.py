"""Reproducible diagram of the maps proved in JMO1--JMO12."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

out=Path(__file__).resolve().parent
fig=plt.figure(figsize=(13,11),facecolor="white")
fig.text(.055,.96,"Three marked octonion slots and their profile maps",
         fontsize=20,weight="bold",color="#142d43")
fig.text(.055,.925,"Original coordinates, exact products, retained complements",
         fontsize=12,color="#42596b")
def box(x,y,w,h,title,lines,color):
    fig.patches.append(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.012",
                       transform=fig.transFigure,facecolor=color,edgecolor="#7490a3"))
    fig.text(x+.012,y+h-.035,title,fontsize=13,weight="bold",color="#142d43")
    for k,line in enumerate(lines):
        fig.text(x+.012,y+h-.075-k*.039,line,fontsize=12,color="#142d43")
box(.055,.675,.415,.195,"Marked domain — JMO1–JMO2",[
    r"Upper slots: $(r,q,p)\in\mathbb{O}_r\oplus\mathbb{O}_q\oplus\mathbb{O}_p$",
    r"Cyclic slots: $(r,\bar q,p)\in V_1\oplus V_2\oplus V_3$",
    r"$G(J_0,J_0)=2[N(r)+N(q)+N(p)]$"],"#eaf3f9")
box(.53,.675,.415,.195,"Tangent receiver — JMO6",[
    r"$F_4\times_K W\ \longrightarrow\ \pi^*T(F_4/\mathrm{Spin}(8))$",
    r"$D_i(a)d_\lambda=\Delta_iE_i(a)$",
    r"$G_\lambda(K_i(a),K_i(a))=2\Delta_i^2N(a)$"],"#eaf3f9")
box(.055,.405,.89,.205,"Full Jordan square — JMO7",[
    r"$J_0^2=\mathrm{diag}(N(p)+N(q),\,N(p)+N(r),\,N(q)+N(r))+J_0(\mathcal{P}(w))$",
    r"$\mathcal{P}(r,q,p)=(\bar p q,\;pr,\;q\bar r)$",
    r"All three diagonal entries and all three marked output slots are retained."],"#edf5ee")
box(.055,.16,.415,.175,"Profile composition — JMO8–JMO9",[
    r"$\mathcal{N}=\mathcal{M}\circ\mathcal{P}$",
    r"Smooth, degree four, original cutoff curls",
    r"Retained graph starts with the whole input $w$"],"#f7f0df")
box(.53,.16,.415,.175,"Specified fibre curve — JMO10–JMO12",[
    r"$(r,q,p)=(t,1,1):\ \mathcal{I}=t,\ \mathcal{P}=(1,t,t)$",
    r"$\mathcal{N}=t^2(\mathbf{i}w^{(1)}+\mathbf{k}w^{(3)})$",
    r"Core: $F_{13}=-4t^4T_2$, magnetic density $16t^8$"],"#f7f0df")
for y in [.64,.37]:
    fig.text(.495,y,"↓",fontsize=24,color="#42596b",ha="center")
fig.text(.055,.08,
         "The diagram records classical bundle and curvature maps.\n"
         "Quantum spectral mass requires its own calculation. Full proofs and source citations: JMO1–JMO12.",
         fontsize=11,color="#42596b",linespacing=1.5)
fig.savefig(out/"JORDAN_MARKED_SLOTS.png",dpi=170)
fig.savefig(out/"JORDAN_MARKED_SLOTS.svg")
plt.close(fig)
