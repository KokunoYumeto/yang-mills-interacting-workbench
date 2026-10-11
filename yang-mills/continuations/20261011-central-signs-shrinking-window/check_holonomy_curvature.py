"""Bounded checks and reproducible scientific figure for HC1--HC21.

Matrix samples and classical holonomies are not vacuum samples.
All mathematical proofs, including the actual probability bound, are in
HOLONOMY_CURVATURE_RECEIVING.md.
"""
from pathlib import Path
import json, math
import numpy as np
from scipy.linalg import expm
import sympy as sp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
T = np.array([
    [[0, -1j/2], [-1j/2, 0]],
    [[0, -1/2], [1/2, 0]],
    [[-1j/2, 0], [0, 1j/2]]
])
I = np.eye(2)
rng = np.random.default_rng(61011)
checks = 0
residuals = {}

def check(name, value, tolerance=1e-10):
    global checks
    checks += 1
    residuals[name] = max(residuals.get(name, 0.0), float(abs(value)))
    assert abs(value) <= tolerance, (name, value)

for d in range(3):
    for k in range(3):
        check("original_metric", -2*np.trace(T[d]@T[k])-(d==k))
        comm = T[d]@T[k]-T[k]@T[d]
        target = sum(float(sp.LeviCivita(d,k,r))*T[r] for r in range(3))
        check("Lie_bracket", np.linalg.norm(comm-target))

for _ in range(120):
    X = np.einsum("i,ijk->jk", rng.normal(size=3), T)
    Y = np.einsum("i,ijk->jk", rng.normal(size=3), T)
    delta = float(rng.uniform(.003,.5))
    C = X@Y-Y@X
    P = expm(delta*X)@expm(delta*Y)@expm(-delta*X)@expm(-delta*Y)
    R = P-I-delta**2*C
    M = max(np.linalg.norm(X,2),np.linalg.norm(Y,2))
    bound = (32/3)*M**3*delta**3
    assert np.linalg.norm(R,2) <= bound+1e-14
    checks += 1
    D = float((2-np.trace(P)).real)
    full = delta**4*np.linalg.norm(C,"fro")**2/2
    full += delta**2*np.trace(C.conj().T@R).real
    full += np.linalg.norm(R,"fro")**2/2
    check("full_deficit_square",D-full)
    check("radius_two_deficit",D-np.linalg.norm(I-P,"fro")**2/2)
    check("original_norms",np.linalg.norm(X,"fro")**2+np.trace(X@X))
    lam = rng.uniform(.1,2,size=3)
    for d,k in [(0,1),(0,2),(1,2)]:
        P = expm(delta*lam[d]*T[d])@expm(delta*lam[k]*T[k])
        P = P@expm(-delta*lam[d]*T[d])@expm(-delta*lam[k]*T[k])
        exact = 4*math.sin(delta*lam[d]/2)**2*math.sin(delta*lam[k]/2)**2
        check("orthogonal_exact_commutator",2-np.trace(P)-exact)

q = sp.symbols("q1:4", real=True)
v = sp.symbols("v1:4", real=True)
energy = sum(x*x for x in v)/2 + sum(q[d]**2*q[k]**2 for d,k in [(0,1),(0,2),(1,2)])/2
acc = [-q[d]*sum(q[k]**2 for k in range(3) if k != d) for d in range(3)]
derivative = sum(sp.diff(energy,q[d])*v[d]+sp.diff(energy,v[d])*acc[d] for d in range(3))
assert sp.expand(derivative) == 0
checks += 1
for d in range(3):
    for k in range(3):
        if d != k:
            C = T[k]@T[d]-T[d]@T[k]
            check("static_source_sign",np.linalg.norm(T[k]@C-C@T[k]+T[d]))

# Exact mesh test: f(x)=product_d max(1-2|x_d|,0), origin o=0.
# Each integer or half-integer mesh sum equals 50j, with endpoints retained.
for j in [4,5,8,16]:
    a = 1/(100*j)
    for shift in [0,.5]:
        z = np.arange(-50*j-2,50*j+3)+shift
        mesh_sum = np.maximum(1-2*np.abs(a*z),0).sum()
        check("exact_triangle_mesh",mesh_sum-50*j,1e-10)
    qpatch = 100*j+3
    lower = j**4-50*j-1
    assert lower > 0 and lower+qpatch < 2*j**4
    checks += 1

lam = np.array([1.,.8,.6])
J1 = 1/8
Emax = 33.0
C0 = 81*J1**2/16
Rbar = 2*C0/(Emax+math.sqrt(Emax**2-4*C0))
Klimit = math.sqrt(2*Rbar/(3*J1))
receiver_limit = sum(lam[d]**2*lam[k]**2 for d,k in [(0,1),(0,2),(1,2)])/32
samples = []
for j in np.unique(np.logspace(math.log10(4),5,130).astype(int)):
    j = int(j); a = 1/(100*j); g2 = a/2; qpatch = 100*j+3
    N = 3*qpatch*(qpatch+1)**2
    Mfaces = 3*qpatch**2*(qpatch+1)
    crossing = 12*qpatch*(qpatch+1)
    ebar = min(2*Mfaces,6*g2*math.sqrt(N*Mfaces))+2*crossing
    A1 = 3*(50*j)**3
    c = 9*a*a/64
    Ce = 4*c*A1*A1
    Be = ebar+4*c*A1
    disc = Be*Be-4*(1+c)*Ce
    assert disc > 0
    rbar = 2*Ce/(Be+math.sqrt(disc))
    cutoff = math.sqrt(2*rbar/(a**4*A1))
    delta = a**.25
    deficits = [4*math.sin(delta*lam[d]/2)**2*math.sin(delta*lam[k]/2)**2
                for d,k in [(0,1),(0,2),(1,2)]]
    receiver = sum(deficits)/(8*a)
    log_probability_bound = (3*A1/8)*(1-.5+math.log(.5))
    samples.append(dict(j=j,a=a,scaled_cutoff=a**1.5*cutoff,
                        classical_receiver=receiver,
                        scaled_log_probability_bound=a**3*log_probability_bound))
    checks += 1
assert abs(samples[-1]["scaled_cutoff"]-Klimit) < 1e-6
assert abs(samples[-1]["classical_receiver"]-receiver_limit) < 1e-5
checks += 2

report = dict(check_count=checks,all_assertions_passed=True,residuals=residuals,
              exact_symbolic_energy_derivative=str(sp.expand(derivative)),
              test_function="product_d max(1-2|x_d|,0); F=1; integral=1/8; R=1",
              constants=dict(kappa=1,ell=1,u=.5,lambda_values=lam.tolist(),
                             scaled_curvature_cutoff_limit=Klimit,
                             original_classical_receiver_limit=receiver_limit),
              samples=samples,
              scope="Exact formulas sampled and algebra checked; these are not vacuum samples.")
(HERE/"HOLONOMY_CURVATURE_CHECKS.json").write_text(json.dumps(report,indent=2)+"\n")

plt.rcParams.update({"font.size":11,"axes.titlesize":12,"mathtext.fontset":"dejavusans"})
fig,axs=plt.subplots(1,3,figsize=(15.5,5.3))
js=np.array([s["j"] for s in samples])
axs[0].semilogx(js,[s["scaled_cutoff"] for s in samples],lw=2,label="Exact finite cutoff")
axs[0].axhline(Klimit,color="black",ls="--",label="Proved limiting cutoff")
axs[0].set(xlabel="Original regulator j",ylabel=r"$a_j^{3/2}K^{\rm cut}_{j,1/2}$",
           title="Actual vacuum: curvature constraint\nHC9–HC12; all patch boundaries retained")
axs[0].legend(fontsize=9)
axs[1].semilogx(js,[s["classical_receiver"] for s in samples],lw=2,color="#ad462b",label="Exact four-link holonomy")
axs[1].axhline(receiver_limit,color="black",ls="--",label="Proved classical receiver")
axs[1].set(xlabel="Original regulator j",ylabel=r"$a_j C_{f,j}(\mathrm{Hol}_j(t_jA))$",
           title="Explicit smooth non-Abelian core\nHC13–HC17; no vacuum law assigned")
axs[1].legend(fontsize=9)
axs[2].axis("off")
axs[2].text(.01,.95,"Exact maps and retained dynamics",weight="bold",fontsize=12,va="top")
lines=[
 r"$\mathrm{Hol}_j:\ A\ \mapsto\ (U_e)_{e\in E_j}\in SU(2)^{E_j}$",
 "Every finite configuration has a smooth preimage.",
 r"$D_p\leq a_j^4\,\sup_p |F_{dk}|^2/4$",
 r"$F_{dk}(t_jA)=t_j(\partial_dA_k-\partial_kA_d)$",
 r"$\qquad{}+t_j^2[A_d,A_k],\quad t_j=(\ell/a_j)^{3/4}$",
 r"$q_i''=-q_i\sum_{k\ne i}q_k^2$",
 "The homogeneous solution is globally smooth.",
 "Its positive density has infinite spatial energy.",
 "Matching its receiver to the actual state",
 "remains a separate calculation.",
]
for y,line in zip([.82,.72,.61,.51,.43,.32,.23,.16,.08,.01],lines):
    axs[2].text(.01,y,line,va="center",fontsize=10)
for ax in axs[:2]:ax.grid(alpha=.23)
fig.suptitle("Original smooth-connection map: the vacuum curvature bound and an explicit classical receiver",fontsize=15,y=.99)
fig.text(.5,.015,"Numerical samples of proved formulas.  κ*=ℓ=R=1; u=1/2; f=∏(1−2|x_d|)₊; λ=(1,0.8,0.6).  Complete proofs: HC1–HC24.",ha="center",fontsize=10)
fig.tight_layout(rect=[.015,.065,.99,.91],w_pad=2.5)
fig.savefig(HERE/"HOLONOMY_CURVATURE.png",dpi=160)
fig.savefig(HERE/"HOLONOMY_CURVATURE.svg")
plt.close(fig)
print(json.dumps({k:v for k,v in report.items() if k!="samples"},indent=2))
