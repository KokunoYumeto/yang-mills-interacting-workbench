from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = Path(__file__).resolve().parent
fig = plt.figure(figsize=(13, 9.6), facecolor="#f7f8fa")
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
ax.text(.045, .954, "Actual Wilson time estimates: independent review",
        fontsize=21, fontweight="bold", color="#152c48")
ax.text(.045, .916, "Radius-two SU(2) · original vacuum · unchanged lattice path",
        fontsize=13, color="#4d5a68")

def panel(x, y, w, h, heading, lines, color="#eaf1f9"):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.012",
                               linewidth=1,edgecolor="#b6c4d2",facecolor=color))
    ax.text(x+.018,y+h-.037,heading,fontsize=14,fontweight="bold",color="#173757")
    cursor = y+h-.085
    for text, size in lines:
        ax.text(x+.018,cursor,text,fontsize=size,color="#172635",va="top")
        cursor -= .054

panel(.045,.613,.91,.247,"The original drift cancels only after exact time reversal  [R2–R6]",[
    (r"$\mathcal{L}=\kappa_*\sum X^2+2\kappa_*\sum(X\log\psi)X,\qquad d\mu=\psi^2\,dU$",17),
    (r"$b(U_t)-b(U_0)=\frac{1}{2} M_t-\frac{1}{2}(N_T-N_{T-t})$",19),
    ("M is forward; N is forward in reversed time. Their dependence is retained.",12),
])
panel(.045,.300,.438,.275,"Fixed finite Wilson words  [R7–R18]",[
    (r"$c=2\kappa_*\,\sup\sum|Xb|^2$",16),
    (r"$\mathbb{E}|\Delta b|^{2p}\leq(2p-1)!!\,c^p h^p$",15),
    (r"$\mathbb{P}(|\Delta b|\geq r)\leq2e^{-r^2/(2ch)}$",15),
    (r"Continuous paths: modulus $\sqrt{h\log(1/h)}$",12),
])
panel(.517,.300,.438,.275,"Original orientation averages  [R22–R29]",[
    (r"$Y_{de,j}=2-\overline{W}_{de,j}\geq0$",16),
    (r"$\limsup_j\,j^2\,\mathbb{E}\sup_{t\leq T}Y_{de,j}(t)^2$",15),
    (r"$\leq27\kappa_*^2/10000$",17),
    ("Actual curvature moments supply the stronger rate.",11.8),
], "#eef5ed")
panel(.045,.090,.91,.166,"Full-sequence consequence with specified marginal path laws  [R29]",[
    (r"$\limsup_j\,j\,\sup_{0\leq t\leq T}Y_{de,j}(t)\leq9\kappa_*/100"
     r"\quad\mathrm{almost\ surely}$",18),
    ("Summable tails; no independent-face hypothesis or bound on the vacuum drift.",12),
], "#eef5ed")
ax.text(.045,.065,"Proof: INDEPENDENT_REVIEW.md, R1–R29. Original human source: "
        "Takeda–Trutnau, arXiv:1007.3900v1, §2, (1), Remark (i).",
        fontsize=10.5,color="#45515d")
ax.text(.045,.038,"This diagram shows proved estimates, not simulated trajectories. "
        "Growing loops and the raw phase retain their original gradient constants.",
        fontsize=10.5,color="#45515d")
fig.savefig(HERE/"REVIEW_FINDINGS.png",dpi=170)
fig.savefig(HERE/"REVIEW_FINDINGS.svg")
plt.close(fig)
