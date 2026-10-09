"""Exact chart-mass bound and the global SU(2) coordinate receiving map."""
from pathlib import Path
import math
import numpy as np
from scipy.special import gammaln
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"svg.hashsalt":"joint-path-global-observable-20261009"})
fig=plt.figure(figsize=(14,10),facecolor="#f7f9fc")
fig.text(.06,.95,"The original joint path: cutoff mass and a global replacement",fontsize=20,weight="bold")
fig.text(.06,.9,r"$L_j=j^4,\quad a_j=1/(100j),\quad g_j^2=\kappa_*/(200j),\quad b_j=10000j^2/\kappa_*$",fontsize=17)
ax=fig.add_axes([.065,.39,.405,.40])
logs=np.linspace(math.log(600),36,400);jj=np.exp(logs);m=2*jj**4
N=3*m*(m+1)**2;M=3*m*m*(m+1);d=2*m**3+3*m*m
kappa=1.;R=math.pi/2
ss=kappa/(300*jj)*np.sqrt(1+1/(2*jj**4))
C0=math.exp(.25)*(3*math.sqrt(math.pi)+4)
Dperd=(N/d)*(1+math.log(C0)-1.5*np.log(ss))+3*math.log(R)-math.log(16)-.5*math.log(math.pi)-gammaln(1.5*d+1)/d
ax.plot(logs,Dperd,lw=2.5,color="#a44632")
ax.set_title(r"Actual vacuum mass: $\log\Gamma_j^{\rm odd}/d_j\leq D_j(\pi/2)/d_j$",fontsize=13,pad=20)
ax.set_xlabel(r"$\log j$ (envelope of the integer sequence)")
ax.set_ylabel(r"Exact upper bound $D_j(\pi/2)/d_j$")
ax.grid(alpha=.23)
ax.text(0,-.25,r"Displayed member: $\kappa_*=1$; full formula PK140."
        "\nThe proof holds for every fixed "+r"$\kappa_*>0$."
        "\nThis curve bounds mass; it does not sample eigenvalues.",transform=ax.transAxes,fontsize=11)
ax=fig.add_axes([.58,.39,.36,.40])
theta=np.linspace(-2*np.pi,2*np.pi,700)
ax.plot(theta,2*np.sin(theta/2),lw=2.5,color="#225d87")
ax.scatter([-2*np.pi,0,2*np.pi],[0,0,0],color="#225d87",zorder=3)
ax.set_xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],[r"$-2\pi$",r"$-\pi$","0",r"$\pi$",r"$2\pi$"])
ax.set_ylim(-2.4,2.4);ax.set_yticks([-2,-1,0,1,2]);ax.grid(alpha=.23)
ax.set_xlabel(r"Original group parameter $\theta$; period $4\pi$")
ax.set_ylabel(r"$q^1(\exp(\theta T_1))=2\sin(\theta/2)$")
ax.set_title(r"Global coordinate: $q^\alpha(Z)=-2\,\mathrm{tr}(T_\alpha Z)$",fontsize=13,pad=20)
ax.text(0,-.25,r"$T_1=-i\sigma_1/2$; the endpoints are the same group point $-I$."
        "\nThe value and all derivatives match there."
        "\nExact map and receiving coefficients: PK143–PK144.",transform=ax.transAxes,fontsize=10)
fig.text(.065,.225,r"$\limsup D_j(R)/(d_j\log j)\leq-63/4$ for fixed $R$: the cutoff's raw measure tends to zero.",fontsize=14,color="#a44632")
fig.text(.065,.17,r"$\widehat\upsilon_g^A=\frac{1}{2}\{\sin[(A\sigma_*/2g^2)\,u_1\!\cdot u_3]-"
         r"\mathscr{S}_{\mathcal{R}}\sin[(A\sigma_*/2g^2)\,u_1\!\cdot u_3]\}\psi_g$",fontsize=17,color="#225d87")
fig.text(.065,.1,"The global replacement is smooth and nonzero for every A > 0 at each finite regulator."
         "\nIts joint-path mass and energy still require estimates. Complete proofs: PK132–PK157.",fontsize=12)
fig.text(.065,.035,"All heat, Haar, boundary-count, trace and derivative factors are derived in the accompanying proof."
         "\nThe actual ground-state transform retains its earlier programme source: local_energy_current_true_vacuum.md, equation (1.3).",fontsize=10,color="#425564")
fig.savefig(HERE/"JOINT_PATH_GLOBAL_OBSERVABLE.png",dpi=165)
fig.savefig(HERE/"JOINT_PATH_GLOBAL_OBSERVABLE.svg",metadata={"Date":None})
plt.close(fig);print("Rendered the complete original-path bound and global group-coordinate map.")
