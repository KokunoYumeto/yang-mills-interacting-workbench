"""Reproducible numerical illustration; the certificate is separate."""

from pathlib import Path
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

HERE = Path(__file__).resolve().parent


def K(z):
    z = np.asarray(z)
    result = np.zeros_like(z)
    far = z < 0.8
    result[far] = (-(1 + z[far]) * np.log(z[far])
                   - 2 * (1 - z[far])) / (1 - z[far]) ** 3
    w = 1 - z[~far]
    for m in range(35):
        result[~far] += ((m + 1) / ((m + 2) * (m + 3))) * w ** m
    return result


fig, axes = plt.subplots(1, 3, figsize=(15.2, 5.8),
                         gridspec_kw={"width_ratios": [1.02, 1.0, 1.1]})
fig.subplots_adjust(left=.045, right=.98, bottom=.20, top=.76, wspace=.37)
fig.suptitle("The original gamma integral: domain maps and positive reduction",
             fontsize=16, y=.98)
fig.text(.5, .865,
         r"$a=-\sin x\cos y,\quad b=\cos x\sin y,\quad "
         r"C_\gamma=\dfrac{2}{\pi^2}\int_{[0,\pi]^2}"
         r"\dfrac{|ab(b-a)|}{\sqrt{a^2+b^2}}\,dx\,dy$",
         ha="center", va="center", fontsize=14)

x = np.linspace(0, np.pi, 601)
X, Y = np.meshgrid(x, x)
a = -np.sin(X) * np.cos(Y)
b = np.cos(X) * np.sin(Y)
radius = np.sqrt(a * a + b * b)
F = np.divide(np.abs(a * b * (b - a)), radius,
              out=np.zeros_like(radius), where=radius != 0)
for row, col in [(0, 0), (0, 600), (600, 0), (600, 600), (300, 300)]:
    F[row, col] = 0
heat = axes[0].imshow(F, origin="lower", extent=(0, np.pi, 0, np.pi),
                       vmin=0, vmax=1 / (2 * np.sqrt(2)), cmap="magma")
axes[0].set_title("Original integrand: numerical samples", fontsize=10.5)
axes[0].set_xticks([0, np.pi/2, np.pi], ["0", r"$\pi/2$", r"$\pi$"])
axes[0].set_yticks([0, np.pi/2, np.pi], ["0", r"$\pi/2$", r"$\pi$"])
axes[0].set_xlabel(r"original $x$")
axes[0].set_ylabel(r"original $y$")
bar = fig.colorbar(heat, ax=axes[0], fraction=.046, pad=.03)
bar.set_label(r"$F(x,y)$", fontsize=10)

ax = axes[1]
L = np.pi / 2
ax.add_patch(Polygon([(0, 0), (L, 0), (L, L)], facecolor="#9bdac5",
                     edgecolor="#23745c", linewidth=1.5))
ax.add_patch(Polygon([(0, 0), (0, L), (L, L)], facecolor="#deedf7",
                     edgecolor="#467c9d", linewidth=1.5))
ax.plot([0, L], [0, L], color="#333333", linewidth=1.1)
ax.text(.70*L, .29*L, r"$T:\ y\leq x$"+"\n"+r"$p\geq q_0$",
        ha="center", fontsize=12)
ax.text(.29*L, .70*L, r"$(x,y)\mapsto(y,x)$"+"\n"+r"$p\leftrightarrow q_0$",
        ha="center", fontsize=10.5)
ax.set_xlim(0, L); ax.set_ylim(0, L); ax.set_aspect("equal")
ax.set_xticks([0, L], ["0", r"$\pi/2$"])
ax.set_yticks([0, L], ["0", r"$\pi/2$"])
ax.set_xlabel(r"$x$ after original quadrant reflections")
ax.set_ylabel(r"$y$ after original quadrant reflections")
ax.set_title("Exact folding: all four quadrants retained", fontsize=10.5)
ax.text(.5, -.23,
        r"$C_\gamma=\dfrac{16}{\pi^2}"
        r"\int_T\frac{p^2q_0}{\sqrt{p^2+q_0^2}}\,dx\,dy$",
        transform=ax.transAxes, ha="center", fontsize=12)

t = np.linspace(0, 1, 1201)
G = np.zeros_like(t)
G[1:] = 2*t[1:]*K(t[1:]**2)/np.sqrt(1+t[1:]**2)
ax = axes[2]
ax.fill_between(t, G, color="#dbeaf7")
ax.plot(t, G, color="#1f5c92", linewidth=2)
ax.scatter([0, 1], [0, 1/(3*np.sqrt(2))], color="#1f5c92", s=22)
ax.set_xlim(0, 1); ax.set_ylim(0, .76)
ax.set_xlabel(r"$t=\tan y/\tan x$ on $T$")
ax.set_ylabel(r"$G(t)=2tK(t^2)/\sqrt{1+t^2}$")
ax.set_title("Continuous positive one-dimensional integrand", fontsize=10.5)
ax.grid(alpha=.22)
ax.text(.55, .77, r"$G(0)=0$"+"\n"+r"$G(1)=1/(3\sqrt{2})$",
        transform=ax.transAxes, fontsize=11)
ax.text(.5, -.23, r"$C_\gamma=\dfrac{4}{\pi^2}\int_0^1G(t)\,dt$",
        transform=ax.transAxes, ha="center", fontsize=12)

fig.text(.5, .025,
         "Proof locators: GAMMA_INTEGRAL.md (G10)–(G18), (G45), (G52). "
         "Plotted samples illustrate the maps; exact rational bounds are in GAMMA_INTEGRAL_CERTIFICATE.json.",
         ha="center", fontsize=9)
fig.savefig(HERE / "INTEGRAL_GEOMETRY.png", dpi=180)
fig.savefig(HERE / "INTEGRAL_GEOMETRY.svg")
plt.close(fig)
