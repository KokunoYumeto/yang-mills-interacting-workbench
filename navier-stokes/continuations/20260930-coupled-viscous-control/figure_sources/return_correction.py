"""Reproduce the exact return-state, dilation and compact correction diagram."""

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "corpus/artifacts/math/output/navier_stokes_research_2026-09-08/lanes/coupled_viscous_control/infinite_modified/figures/return_correction.png"
OUT.parent.mkdir(parents=True, exist_ok=True)
ink = "#17243a"
blue = "#255da8"
green = "#17795e"
gold = "#956300"
paper = "#fbfcfe"

fig = plt.figure(figsize=(16, 12), dpi=180, facecolor=paper)
canvas = fig.add_axes([0, 0, 1, 1])
canvas.set(xlim=(0, 1), ylim=(0, 1))
canvas.axis("off")
canvas.text(.5, .966, "The retained third return and its exact local correction",
            ha="center", fontsize=22, weight="bold", color=ink)
canvas.text(.5, .929, "Physical state, exact chart map, signed transition force and the full cutoff region",
            ha="center", fontsize=12.5, color="#526176")


def panel(x, y, w, h, title, color, fill):
    canvas.add_patch(FancyBboxPatch((x, y), w, h,
                     boxstyle="round,pad=0.008,rounding_size=.012",
                     facecolor=fill, edgecolor=color, linewidth=1.7))
    canvas.text(x+.022, y+h-.043, title, fontsize=15, weight="bold", color=color)


def lines(x, y, values, spacing=.035, size=12.3):
    for j, value in enumerate(values):
        canvas.text(x, y-j*spacing, value, fontsize=size, color=ink, va="center")


panel(.04, .61, .44, .26, "1  Exact physical return state", blue, "#edf4ff")
lines(.062, .788, [
    r"$\theta=G_R\cdot x,\quad u=A_Rx,\quad p=0$",
    r"$(A_R)_{21}=0,\quad (A_R)_{11}=a_R,\quad (A_R)_{22}=-a_R$",
    r"$(A_R)_{12}=-W_R,\quad W_R\geq c_W\sigma_2/4>0$",
    r"$(G_R)_1=N_3/\sqrt{R}>0$",
    "All base and three-layer gradient terms remain present.",
], spacing=.034, size=12.0)
canvas.text(.062, .628, "Proof: irc:return-G through irc:exact-return-temperature",
            fontsize=10, color="#526176")

panel(.52, .61, .44, .26, "2  Exact parabolic chart transition", blue, "#edf4ff")
lines(.542, .788, [
    r"$a=\rho'/\rho>0,\quad c'/c=a^2$",
    r"$U'=aU(\xi+ay,\tau_0+a^2s)$",
    r"$\Theta'=a^3\Theta(\xi+ay,\tau_0+a^2s)$",
    r"$D'=a^2D,\quad G'=a^4G$ at the centred core",
    r"Invariants: $G/|G|,\quad D/\sqrt{|G|}$",
], spacing=.034, size=12.0)
canvas.text(.542, .628, "Radius selection preserves every matrix shape and gradient direction.",
            fontsize=10, color="#526176")

panel(.04, .305, .92, .255, "3  Explicit affine evolution: zero total force", green, "#e8f7f1")
lines(.062, .477, [
    r"$g_1(s)=g_1e^{-a_Rs},\quad b(s)=-W_R-g_1\Phi_1(a_R,s)$",
    r"$g_2(s)=e^{a_Rs}[g_2+g_1W_R\Phi_2(a_R,s)+g_1^2\Xi(a_R,s)]$",
    r"$\Phi_k(a,s)=\int_0^s e^{-kar}\,dr,\quad \Xi(a,s)=\int_0^s e^{-2ar}\Phi_1(a,r)\,dr$",
    r"$A_{11}=a_R,\ A_{12}=b,\ A_{21}=0,\ A_{22}=-a_R$",
], spacing=.037, size=12.5)
canvas.text(.56, .366, r"$G'+A^TG=0,\quad A'+A^2+H-e_2G^T=0$",
            fontsize=12.0, color=green, va="center")
canvas.text(.062, .323, "The pressure H cancels the full momentum gradient. This affine solution has no finite-time singularity.",
            fontsize=10.5, color="#526176")

panel(.04, .06, .63, .195, "4  Flat interpolation: exact force cost", gold, "#fff6dc")
lines(.062, .173, [
    r"$r_\beta^\theta=(1-\beta)r_h^\theta+\beta'\Delta G-\beta(1-\beta)(\Delta A)^T\Delta G$",
    r"$r_\beta^u=(1-\beta)r_h^u+\beta'\Delta A-\beta(1-\beta)(\Delta A)^2$",
    r"$h=\chi\,\beta\Delta G\cdot x,\quad z=J\nabla(\chi Q),\quad Q=x^T(-J\beta\Delta A)x/2$",
], spacing=.038, size=11.2)
canvas.text(.062, .077, "Initial jets match. Every derivative of the cutoff remains in the full force.",
            fontsize=10.3, color="#526176")

local = fig.add_axes([.70, .062, .16, .19])
local.set(aspect="equal", xlim=(-1.1, 1.1), ylim=(-1.1, 1.1))
local.axis("off")
local.add_patch(Circle((0, 0), 1, color="#fff6dc", ec=gold, lw=1.7))
local.add_patch(Circle((0, 0), .5, color="#e8f7f1", ec=green, lw=1.4))
local.text(0, 0, r"$\chi=1$"+"\n"+"total force = 0"+"\n"+r"after $t_R+\ell$",
           ha="center", va="center", fontsize=9.0, color=green)
local.text(0, .77, "cutoff forces", ha="center", va="center", fontsize=9.0, color=gold)
local.text(0, -1.05, r"$|x|=r_c$", ha="center", va="center", fontsize=9.2, color=ink)
canvas.text(.865, .205, "Outside:", fontsize=11, color=ink, weight="bold")
canvas.text(.865, .175, "retained", fontsize=11, color=ink)
canvas.text(.865, .150, "parent", fontsize=11, color=ink)
canvas.text(.865, .125, "unchanged", fontsize=11, color=ink)

canvas.text(.5, .024, "Proofs: irc:full-chart, irc:orbit-classification, irc:affine-continuation, irc:compact-core-repair.  No all-stage force budget is asserted.",
            ha="center", fontsize=10.5, color="#526176")
fig.savefig(OUT, facecolor=paper)
plt.close(fig)
print(OUT)
