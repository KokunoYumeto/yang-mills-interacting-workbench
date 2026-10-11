"""Reproducible mathematical map for AC8, AC17, AC20 and AC33."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

root=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(14,8))
fig.patch.set_facecolor("#f7f9fc")
ax.set(xlim=(0,14),ylim=(0,8));ax.axis("off")
def box(x,y,w,h,text,color="#e4edf8",size=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.15",facecolor=color,edgecolor="#263c57",linewidth=1.4))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",fontsize=size,color="#112d49",linespacing=1.6)
def arrow(x1,y1,x2,y2):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",mutation_scale=17,color="#35567b",linewidth=1.8))
ax.text(.25,7.65,"The original signed endpoint: keep the joint covariance",fontsize=19,weight="bold",color="#112d49")
box(.35,5.65,5.7,1.35,r"$h_0=(S^2+S_{\mathcal{R}}^2)/2-\tau[\Gamma(S,S)+\Gamma(S_{\mathcal{R}},S_{\mathcal{R}})]/2$"+"\n"+r"$h_D=D^2-\tau\Gamma(D,D),\qquad D=S+S_{\mathcal{R}}$",size=12)
box(7.15,5.65,6.1,1.35,r"$F=\beta_0(S-S_{\mathcal{R}}),\qquad \tau=\kappa/s$"+"\n"+r"$h_F=F^2-\tau\Gamma(F,F)=\beta_0^2(4h_0-h_D)$")
arrow(6.23,6.32,6.97,6.32)
box(.35,3.15,5.7,1.7,"One full cutoff vacuum"+ "\n"+r"$\mu_\Lambda=|\phi_\Lambda|^2dU,\quad m^\Lambda_a=\mu_\Lambda h_a$"+"\n"+r"$\Sigma^\Lambda_{ab}=\mu_\Lambda(h_ah_b)-m^\Lambda_a m^\Lambda_b$"+ "\n"+r"$1-|\langle\phi_\Lambda,\psi\rangle|^2\leq\eta_\Lambda\leq 1/2$",color="#e7f3ee")
box(7.15,3.15,6.1,1.7,"The same receiving direction in mean and variance"+ "\n"+r"$m^\Lambda_F=\beta_0^2(4m^\Lambda_0-m^\Lambda_D)$"+"\n"+r"$\sigma_F^2=\beta_0^4(16\Sigma^\Lambda_{00}+\Sigma^\Lambda_{DD}-8\Sigma^\Lambda_{0D})$",color="#e7f3ee")
arrow(3.2,5.45,3.2,5.02);arrow(10.15,5.45,10.15,5.02);arrow(6.23,4.0,6.97,4.0)
box(.35,.65,12.9,1.65,"Actual vacuum endpoint: "+r"$\mathcal{E}(s)=\mu h_F$"+"\n"+r"$m^\Lambda_F-2\sqrt{\eta_\Lambda(1-\eta_\Lambda)}\,\sigma_F-\eta_\Lambda(m^\Lambda_F-l_F)$"+"\n"+r"$\leq\ \mathcal{E}(s)\ \leq$"+"\n"+r"$m^\Lambda_F+2\sqrt{\eta_\Lambda(1-\eta_\Lambda)}\,\sigma_F+\eta_\Lambda(u_F-m^\Lambda_F)$",color="#fff1d9",size=13)
arrow(10.15,2.98,10.15,2.48)
ax.text(.35,.16,"Exact map: AC8, AC15–AC23, AC33. Original path: τ = j. Finite-cutoff means have not been numerically evaluated; no endpoint sign is inferred.",fontsize=10,color="#344c68")
fig.savefig(root/"COUPLED_ENDPOINT_MAP.png",dpi=170,bbox_inches="tight")
plt.close(fig)
