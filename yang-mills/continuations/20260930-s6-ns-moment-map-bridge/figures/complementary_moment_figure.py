"""Reproducible original-lattice cube and exact return diagram, PK55–PK62."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,FancyBboxPatch
from itertools import product
ROOT=Path(__file__).resolve().parent
OUT=ROOT if ROOT.name=="figures" else ROOT/"complement_figure_20261009"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"svg.hashsalt":"ym-complement-20261009"})
fig=plt.figure(figsize=(14,10),facecolor="#fbfaf5")
ax=fig.add_axes([.03,.05,.94,.89]);ax.set(xlim=(0,14),ylim=(0,10));ax.axis("off")
fig.suptitle("The cube contribution and the complete next return",fontsize=21,y=.98,color="#173d4a")
def text(x,y,s,**kw):ax.text(x,y,s,color="#173d4a",**kw)
def proj(v):
    x,y,z=v
    return (1.2+2.1*x+.8*y,6.35+.65*y+2.1*z)
for v in product((0,1),repeat=3):
    p=proj(v)
    for k in range(3):
        if v[k]==0:
            w=list(v);w[k]=1;q=proj(w)
            ax.plot([p[0],q[0]],[p[1],q[1]],color="#327c78",lw=2.3)
    ax.plot(*p,"o",color="#173d4a",ms=4)
text(.6,9.65,"Six faces · twelve links · eight vertices",fontsize=14,fontweight="bold")
text(.5,6.0,r"$(0,0,0)$",fontsize=13)
text(3.4,9.2,r"$(a,a,a)$",fontsize=13)
text(.5,5.5,r"Each link integral: $\frac{1}{2}\delta_{il}\delta_{jk}$",fontsize=15)
text(.5,4.9,r"Cube integral: $2^8/2^{12}=1/16$",fontsize=16)
text(.5,4.4,"Coordinate projection; edge length is the original a.",fontsize=10)
text(6.1,9.65,"One shared link, two electric sectors",fontsize=14,fontweight="bold")
text(6.1,8.8,r"$W_pW_q=F_0+F_1,\quad F_0\perp F_1$",fontsize=16)
text(6.1,8.1,r"$\|F_0\|^2=1/4,\quad H_0F_0=(9/2)F_0$",fontsize=16)
text(6.1,7.4,r"$\|F_1\|^2=3/4,\quad H_0F_1=(13/2)F_1$",fontsize=16)
text(6.1,6.65,r"First moment: $(1/4)(9/2)+(3/4)(13/2)=6$",fontsize=14)
text(6.1,5.9,r"Second: $(1/4)(9/2)^2+(3/4)(13/2)^2=147/4$",fontsize=14)
text(6.1,5.15,r"Magnetic cube coefficient: $4!/16=3/2$",fontsize=15)
text(6.1,4.55,"Full matrices, all faces and boundary counts: PK56–PK57.",fontsize=11)
ax.plot([.4,13.7],[4.0,4.0],color="#9caaa9",lw=1)
for x,w,label,sub in [
(.5,2.6,r"$P\mathcal{H}_-$","Original odd face space"),
(5.0,3.0,r"$\operatorname{ran}C\subset Q\mathcal{H}_-$",r"$C^*C=(M-1)P$"),
(10.3,3.2,r"$Q_2\mathcal{H}_-$",r"$Q_2=Q-CC^*/(M-1)$")]:
    ax.add_patch(FancyBboxPatch((x,2.5),w,1.0,boxstyle="round,pad=.1",facecolor="#e4efeb",edgecolor="#327c78"))
    text(x+w/2,3.12,label,ha="center",fontsize=16)
    text(x+w/2,2.73,sub,ha="center",fontsize=10)
for left,right,label in [(3.2,4.85,r"$C$"),(8.15,10.15,r"$Q_2B$")]:
    ax.add_patch(FancyArrowPatch((left,3),(right,3),arrowstyle="-|>",mutation_scale=16,color="#327c78",lw=2))
    text((left+right)/2,3.35,label,ha="center",fontsize=16)
text(.5,1.82,r"$T=Q_2BC,\qquad T^*T=K_2-\mu^2P/(M-1)>0$",fontsize=17)
text(.5,1.05,r"$C^*(B+s)^{-1}C=(M-1)^2[(\mu+s(M-1))P-T^*(B_2+s)^{-1}T]^{-1}$",fontsize=16)
text(.5,.37,r"$B=Q(H-E_0)Q,\quad B_2=Q_2BQ_2,\quad \mu=\kappa(6M-4)+(2bM-E_0)(M-1)$",fontsize=13)
fig.text(.065,.023,"Exact original Hamiltonian: H = κH₀ + 2bM − bW, κ = 2g²/a, b = 1/(2g²a). Proofs: PK55–PK62.",fontsize=12,color="#173d4a")
fig.savefig(OUT/"COMPLEMENTARY_SECOND_MOMENT.png",dpi=160)
fig.savefig(OUT/"COMPLEMENTARY_SECOND_MOMENT.svg",metadata={"Date":None})
plt.close(fig)
print(str(OUT/"COMPLEMENTARY_SECOND_MOMENT.png"))
