"""Reproduce exact-map and operator diagrams for PK13--PK54."""
from pathlib import Path
import hashlib
import json
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

ROOT=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,"svg.fonttype":"none"})
blue="#123b5d"; teal="#12635c"; red="#9a332b"; ink="#192d3c"
fig=plt.figure(figsize=(12,14),facecolor="white")
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
ax.text(.05,.965,"Actual fields, physical states, and the complete interaction",size=21,weight="bold",color=blue)
ax.text(.05,.938,"Exact formulas from PK13–PK54 • diagrams are schematics, not numerical samples",size=12,color=ink)

def panel(y,height,title):
    ax.add_patch(FancyBboxPatch((.04,y),.92,height,boxstyle="round,pad=0.008",
                              facecolor="#f6f8fa",edgecolor="#bdcbd6"))
    ax.text(.06,y+height-.029,title,size=16,weight="bold",color=blue)

panel(.699,.205,"1. The geometric parameter reaches a physical vector")
steps=[(.07,r"$\mathcal W_M=c_M^*\mathcal W_H$",r"$[p,v]$"),
       (.37,r"$A(v;s,x)$",r"$h_e=H_e(A)^{-1}$"),
       (.69,r"$\Phi_{h,t}=\Pi\prod_e p_t(U_eh_e^{-1})$",r"$\eta_{h,t}=\Phi_{h,t}-\Phi_{\mathcal Rh,t}$")]
for xpos,top,bottom in steps:
    ax.text(xpos,.839,top,size=15,color=teal)
    ax.text(xpos,.804,bottom,size=15,color=ink)
for left,right in [(.275,.35),(.59,.66)]:
    ax.annotate("",xy=(right,.824),xytext=(left,.824),arrowprops={"arrowstyle":"->","color":blue,"lw":2})
ax.text(.07,.766,"Bundle equivariance gives simultaneous colour conjugation; the vertex Haar projection removes it.",size=12)
ax.text(.07,.736,r"$\langle\psi,\eta_{h,t}\rangle=0$  by reflection parity;  $\|\eta_{h,t}\|^2=\Gamma(h)>0$  by an actual core face.",size=14)

panel(.426,.244,"2. Keep both reflected core cubes and every face coefficient")
ax.plot([.11,.91],[.589,.589],color=ink,lw=1.4)
ax.annotate("",xy=(.92,.589),xytext=(.9,.589),arrowprops={"arrowstyle":"->","color":ink})
ax.text(.925,.585,r"$x^1$",size=13)
ax.add_patch(Rectangle((.13,.561),.28,.06,facecolor="#d4e4ef",edgecolor=blue,lw=1.6))
ax.add_patch(Rectangle((.205,.569),.13,.045,facecolor="#8dbfbd",edgecolor=teal,lw=1.6))
ax.add_patch(Rectangle((.72,.569),.13,.045,facecolor="#ead2cf",edgecolor=red,lw=1.6))
ax.text(.27,.545,r"$0$",ha="center")
ax.text(.785,.545,r"$2aK$",ha="center")
ax.text(.27,.627,r"source support projection: $[-\lambda R,\lambda R]$",ha="center",size=12)
ax.text(.785,.627,"reflected core cube",ha="center",size=12)
ax.text(.27,.517,r"$[-am,am]^3$",ha="center",size=14,color=teal)
ax.text(.785,.517,r"$2aKe_1+[-am,am]^3$",ha="center",size=14,color=red)
ax.text(.07,.482,r"$m=\lfloor\lambda r/(2\sqrt{3}a)\rfloor,\quad M_m=3(2m)^2(2m+1),\quad 2aK-am>\lambda R$",size=14)
ax.text(.07,.448,r"$\Gamma=e^{-6t}\sum_p|W_p(h)-W_p(\mathcal Rh)|^2+\|\eta-P_{\mathcal F}\eta\|^2"
                  r"\ \geq\ 32M_me^{-6t}\sin^8(a/\lambda)$",size=14)

panel(.157,.235,"3. The first electric layer and its full interacting return")
ax.text(.07,.326,r"$P=P_{\mathcal F}|_{\mathcal H_-},\quad Q=I-P,\quad M=M_L,\quad"
                 r"C=Q\mathcal WP,\quad \mathcal W=\sum_pW_p$",size=15)
ax.text(.07,.291,r"$PH_0P=3P,\qquad QH_0Q\geq(9/2)Q,\qquad C^*C=(M-1)P$",size=15)
ax.text(.07,.256,r"$H-E_0\ :\quad P\ \longrightarrow Q\ \ (-bC),\qquad"
                 r"P(H-E_0)P=dP,\quad Q(H-E_0)Q=B_-\geq0$",size=15)
ax.text(.07,.217,r"$P(H-E_0+s)^{-1}P=\left[(d+s)P-b^2C^*(B_-+s)^{-1}C\right]^{-1},\quad s>0$",size=15,color=teal)
ax.text(.07,.182,r"$d=2bM+3\kappa-E_0\ \geq\ (3\kappa+\sqrt{9\kappa^2+4b^2M})/2$",size=15)

ax.text(.05,.121,"Same-coupling path (PK43):",weight="bold",size=14,color=blue)
ax.text(.05,.092,r"$T_j=j^6,\ M_{{\rm cov},j}=j^4,\ a_j=(100j)^{-1},\ L_j=j^4,\ "
                 r"g_j^2=\kappa_*/(200j),\ \lambda_j=j^2$",size=15)
ax.text(.05,.064,r"$\mathscr E_{g_j}^{[\lambda_j]}=(400/(\kappa_*j))\,[\mathrm{full\ CE22\ energy\ bracket}],\quad"
                 r"b_j=10000j^2/\kappa_*$",size=14)
ax.text(.05,.032,"Proof: PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md, PK13–PK54. The continuum spectral limit remains open.",size=11,color=ink)
# Matplotlib's math font uses text, while the source proof retains all formulas.
for text in ax.texts:
    text.set_text(re.sub(r"\\(mathcal|mathscr)\s*([A-Za-z])",r"\\\1{\2}",text.get_text()))
fig.canvas.draw()
renderer=fig.canvas.get_renderer()
overflow=[text.get_text() for text in ax.texts
          if not fig.bbox.contains(*text.get_window_extent(renderer).get_points()[0])
          or not fig.bbox.contains(*text.get_window_extent(renderer).get_points()[1])]
assert not overflow, overflow
outputs=[]
for ext in ("png","svg"):
    out=ROOT/("PERIOD_PHYSICAL_KERNELS."+ext)
    fig.savefig(out,dpi=160,facecolor="white")
    outputs.append({"file":out.name,"sha256":hashlib.sha256(out.read_bytes()).hexdigest(),"bytes":out.stat().st_size})
plt.close(fig)
(ROOT/"PERIOD_PHYSICAL_FIGURE_CHECK.json").write_text(json.dumps({
    "schema":"period-physical-figure-v1","files":outputs,
    "proof_locators":["PK13-PK17","PK23-PK30","PK38-PK49","PK50-PK54"],
    "diagram_kind":"Exact maps and a labelled coordinate projection; not to scale",
    "rendered":True,"visual_inspection":"pending"
},indent=2)+"\n",encoding="utf-8")
print(json.dumps({"rendered":True,"files":[r["file"] for r in outputs]}))
