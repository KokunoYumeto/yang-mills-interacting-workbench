from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

root = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.5),
                         gridspec_kw={"width_ratios": [1, 1.28]})
fig.patch.set_facecolor("white")
carriers = [-2, -1, 1, 2, 3]
rho = np.array([[int(n == m) + int(n == -m) for m in carriers]
                for n in carriers])
ax = axes[0]
ax.imshow(rho, cmap=ListedColormap(["#f3f0e9", "#257d87"]), vmin=0, vmax=1)
ax.set_xticks(range(5), carriers)
ax.set_yticks(range(5), carriers)
ax.set_xlabel("Second angular carrier m")
ax.set_ylabel("First angular carrier n")
ax.set_title("Angular matching", loc="left", pad=18, weight="bold")
for i in range(5):
    for j in range(5):
        ax.text(j, i, str(rho[i, j]), ha="center", va="center",
                color="white" if rho[i, j] else "#545454", fontsize=12)
ax.text(0.5, -0.25, r"$\rho_{n,m}=\mathbf{1}_{n=m}+\mathbf{1}_{n=-m}$",
        transform=ax.transAxes, ha="center", fontsize=12)
ax.text(0.5, -0.38, "1: a product can survive averaging\n0: the product averages to zero",
        transform=ax.transAxes, ha="center", fontsize=9, linespacing=1.5)
ax = axes[1]
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
ax.set_title("Auxiliary evaluation", loc="left", pad=18, weight="bold")
def box(x, y, value, color="#edf4f4"):
    ax.text(x, y, value, ha="center", va="center",
            bbox={"boxstyle": "round,pad=0.6", "fc": color, "ec": "#8ca7aa"},
            fontsize=11, linespacing=1.5)
def arrow(start, end, label, xy):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "lw": 1.3, "color": "#435a60"})
    ax.text(*xy, label, fontsize=10, ha="center", va="center")
box(.5, .86, r"$f(Y)$")
box(.21, .60, r"$\Pi_Y f$", "#f3f0e9")
box(.79, .60, r"$\mathsf{R}_Y f=f-\Pi_Y f$")
arrow((.42, .80), (.24, .67), "average", (.18, .78))
arrow((.58, .80), (.77, .67), "center", (.82, .78))
box(.5, .28, r"$\mathcal{E}f=\Pi_Y f+\mathcal{E}\mathsf{R}_Y f$")
arrow((.21, .53), (.34, .36), "constant in Y", (.17, .43))
arrow((.79, .53), (.68, .36), "evaluate", (.85, .43))
ax.text(.5, .075, r"$\mathcal{E}f=f(Y(r,t))$"+"\nY(r,t) has no axial dependence",
        ha="center", fontsize=10, linespacing=1.8)
fig.subplots_adjust(left=.07, right=.97, bottom=.22, top=.86, wspace=.37)
fig.savefig(root / "flux_maps.pdf", bbox_inches="tight", pad_inches=.15,
            metadata={"Title": "Exact angular matching and auxiliary evaluation", "Author": ""})
fig.savefig(root / "flux_maps.png", dpi=180, bbox_inches="tight", pad_inches=.15)
plt.close(fig)
print("Exact carrier matrix and evaluation diagram rendered.")
