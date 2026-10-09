"""Reproduce the PK63--PK78 operator and error diagram."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import math
OUT=Path(__file__).resolve().parent
if OUT.name!="figures":
    OUT=OUT/"full_packet_figure_20261009"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
                    "svg.hashsalt":"YM-full-packet-20261009"})
fig=plt.figure(figsize=(15,10),facecolor="#f7f9fc")
fig.text(.055,.951,"The original packet, the complete complement, and a proved error",
         fontsize=20,weight="bold",color="#183149")
fig.text(.055,.914,r"$H=\kappa H_0+2bM-b\mathcal{W}$  |  "
         r"$F(s)=\langle\eta,(H-E_0+s)^{-1}\eta\rangle$  |  no packet rescaling",
         fontsize=13,color="#29475d")
ax=fig.add_axes([.055,.365,.43,.495]);ax.axis("off")
ax.text(0,1,"Every packet component remains",fontsize=15,weight="bold")
for y,color,title,body in [
 (.72,"#dfeefa",r"$p=P\eta$",r"First electric faces: eigenvalue $3$"),
 (.43,"#e7e2f4",r"$Cw=\Pi Q\eta$",r"$C^*C=mP$,  $w=m^{-1}C^*Q\eta$"),
 (.14,"#dff0e9",r"$z=Q_2Q\eta$",r"Entire remaining odd physical space")]:
    ax.add_patch(FancyBboxPatch((0,y),.97,.21,boxstyle="round,pad=.013",
                 edgecolor="#90a4b7",facecolor=color))
    ax.text(.035,y+.135,title,fontsize=18,color="#183149")
    ax.text(.035,y+.047,body,fontsize=12,color="#29475d")
ax.text(.03,.042,r"$\eta=p+Cw+z$    (PK63–PK64)",fontsize=15,color="#183149")
ar=fig.add_axes([.54,.365,.405,.495]);ar.axis("off")
ar.text(0,1,"Complete cutoff error: three contributions",fontsize=15,weight="bold")
for y,title,formula,explain in [
 (.75,"1  Omitted operator space",
  r"$\Gamma_\Lambda\ell^2/(\beta_\Lambda(s)s^2)$",
  r"$\ell=2bM,\quad \beta_\Lambda(s)=\kappa\Lambda-e_\Lambda+s$"),
 (.45,"2  Omitted packet and its cross terms",
  r"$(2\sqrt{\Gamma_\Lambda\tau_\Lambda}+\tau_\Lambda)/s$",
  r"$\tau_\Lambda\leq4e^{-t\Lambda}Z_t^{N_L}$"),
 (.15,"3  Actual vacuum-energy uncertainty",
  r"$\Gamma(u_\Lambda-e_\Lambda)/s^2$",
  r"$e_\Lambda\leq E_0\leq u_\Lambda$")]:
    ar.text(0,y+.13,title,fontsize=12,weight="bold",color="#183149")
    ar.text(0,y+.04,formula,fontsize=18,color="#245f80")
    ar.text(0,y-.045,explain,fontsize=11,color="#29475d")
ar.text(0,.01,r"Sum bounds $|F(s)-f_\Lambda(s)|$  (PK71)",fontsize=13)
ab=fig.add_axes([.06,.13,.88,.15])
ab.set_xlim(0,35);ab.set_ylim(-.9,1.7)
ab.set_yticks([]);ab.spines[["left","right","top"]].set_visible(False)
ab.spines["bottom"].set_position(("data",0))
ab.set_xticks([0,5,10,15,20,25,30,33])
ab.tick_params(axis="x",labelsize=10)
u=21-3*math.sqrt(257)/4
e=(u+24-math.sqrt((24-u)**2+324))/2
ab.plot([e,u],[.40,.40],lw=12,color="#4c9a85",solid_capstyle="butt")
ab.plot([e,e],[.2,.6],lw=2,color="#23463e")
ab.plot([u,u],[.2,.6],lw=2,color="#23463e")
ab.text((e+u)/2,1.03,r"$e_\Lambda\leq E_0\leq u_\Lambda$",ha="center",fontsize=13)
ab.text((e+u)/2,-.75,f"{e:.6f} to {u:.6f}",ha="center",fontsize=11)
ab.plot([33,33],[0,.78],color="#7a60a5",lw=3)
ab.text(32.5,1.1,r"$H_\Lambda|_{\rm odd}=33I_{16}$",ha="right",fontsize=13)
ab.text(0,1.64,"Original box L = 1,  a = 1,  g = 2,  electric cutoff Λ = 3",
        fontsize=14,weight="bold",color="#183149")
fig.text(.06,.062,"The full cutoff has dimension 37. The interval bounds the actual vacuum; "
         "33 is the odd cutoff eigenvalue, not an asserted full-spectrum value.",fontsize=11)
fig.text(.06,.028,"Proof: PK63–PK78, especially (PK69), (PK71), (PK77) and (PK78). "
         "Displayed decimals illustrate the exact radical endpoints. No continuum mass is plotted.",
         fontsize=10,color="#455c70")
for ext in ("png","svg"):
    fig.savefig(OUT/("FULL_PACKET_RESOLVENT."+ext),dpi=150,
                metadata={"Date":None} if ext=="svg" else None)
print(OUT/"FULL_PACKET_RESOLVENT.png")
