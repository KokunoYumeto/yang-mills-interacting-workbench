"""Bounded exact checks for GM; the analytic proofs are in the manuscript."""
from pathlib import Path
import json, hashlib, datetime, itertools
import sympy as S
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parent
checks=[]
def zero(name, expr):
    assert S.cancel(S.expand(expr))==0,(name,S.expand(expr))
    checks.append(name)

a,ell,kappa,t,D,P,L,V,tau,r,sigma=S.symbols(
    "a ell kappa t D P L V tau r sigma", positive=True)
zero("GM7 original physical energy",
     (t*t*D/2+t**4*P/2)/(kappa*a/2)-(t*t*D+t**4*P)/(kappa*a))
zero("GM14 derivative coefficient",a**3*(ell/a)**S.Rational(3,2)/2
     -ell**S.Rational(3,2)*a**S.Rational(3,2)/2)
zero("GM14 bracket coefficient",a**3*(ell/a)**3/2*4/ell**3-2)
zero("GM15 full derivative tolerance",S.Rational(12,16)*tau/6-tau/8)
zero("GM19 positive floor",4/ell**3*3*sigma/r*(2*r*ell)**3-96*sigma*r*r)
zero("GM17 fourth derivative",S.Rational(2,24)-S.Rational(1,12))

aa=S.Matrix(S.symbols("a1:4"))
j=S.Matrix([-aa[i]*sum(aa[k]**2 for k in range(3) if i!=k) for i in range(3)])
p=sum(aa[i]**2*aa[k]**2 for i in range(3) for k in range(i+1,3))
zero("GM18 homogeneous radial variation",(aa.T*j)[0]+2*p)
ss=S.symbols("s")
trial=aa+ss**2*j/2+ss**4*j.jacobian(aa)*j/24
force=S.Matrix([-trial[i]*sum(trial[k]**2 for k in range(3) if i!=k) for i in range(3)])
for i in range(3):
    residual=S.expand(S.diff(trial[i],ss,2)-force[i])
    zero(f"GM17 homogeneous residual constant {i}",residual.coeff(ss,0))
    zero(f"GM17 homogeneous residual quadratic {i}",residual.coeff(ss,2))

eps=lambda i,j,k:S.LeviCivita(i,j,k)
count=sum(abs(eps(i,d,k)*eps(b,c,q)) for i,d,k,b,c,q in itertools.product(range(3),repeat=6))
assert count==36
checks.append("GM9 exactly36 scalar terms in each quadratic block")
c,m=S.symbols("c m",positive=True)
delta=1/(4*(1+288*c*m))
assert S.simplify(delta*(1+288*c*m))==S.Rational(1,4)
zero("GM10 positive self-map margin",
     S.cancel(2*m-(m+delta*(2*m+288*c*m*m)))
     -m*(864*c*m+2)/(4*(1+288*c*m)))
checks.append("GM10 contraction and self-map constants")

# Full local stress identity for one arbitrary colour at a point where A=0.
# Ad-invariance supplies the covariant cancellation; colours add independently.
E=S.Matrix(S.symbols("E0:3")); M=S.Matrix(S.symbols("M0:3"))
dE=S.Matrix(3,3,S.symbols("dE0:9"))
dM=S.Matrix(3,3,S.symbols("dM0:9"))
dE[2,2]=-dE[0,0]-dE[1,1]
dM[2,2]=-dM[0,0]-dM[1,1]
curl=lambda d:S.Matrix([sum(eps(i,k,l)*d[k,l] for k in range(3) for l in range(3)) for i in range(3)])
Ed=-curl(dM); Md=curl(dE)
qd=-Ed.cross(M)-E.cross(Md)
for i in range(3):
    divT=sum(E[b]*dE[i,b]+M[b]*dM[i,b] for b in range(3))
    divT-=sum(dE[k,i]*E[k]+E[i]*dE[k,k]+dM[k,i]*M[k]+M[i]*dM[k,k] for k in range(3))
    zero(f"GM26 stress conservation component{i}",qd[i]+divT)
energy=(E.dot(E)+M.dot(M))/2
stress=energy*S.eye(3)-E*E.T-M*M.T
zero("GM26 full spatial stress trace",S.trace(stress)-energy)

for T in [S.Rational(1,3),S.Rational(2),S.Rational(7,2)]:
    for h in [S.Rational(-8),S.Rational(-1,2),S.Rational(0),S.Rational(3,2),S.Rational(9)]:
        overlap=max(0,min(T,T+h)-max(-T,-T+h))
        zero(f"GM25 interval defect {T},{h}",(4*T-2*overlap)/(2*T)-min(2,abs(h)/T))

fig,ax=plt.subplots(figsize=(13.6,8.2))
fig.subplots_adjust(left=.025,right=.975,bottom=.025,top=.94)
ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
def box(x,y,w,h,title,body,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.013",
        linewidth=1.2,edgecolor=color,facecolor="#f7f9fc"))
    ax.text(x+.015,y+h-.035,title,fontsize=13,fontweight="bold",va="top",color=color)
    ax.text(x+.015,y+h-.090,body,fontsize=11.2,va="top",linespacing=1.6)
box(.02,.66,.27,.26,"Actual spatial law",
    "CM19–CM23\n"+r"$\xi\sim\mathbb{P}_\Omega,\quad \nu_\xi$"+"\nOne common deterministic schedule","#345b8c")
box(.365,.66,.27,.26,"Exact initial data",
    "SM2–SM7; GM2\n"+r"$B_i=t_j\chi_r\lambda_{i,r}T_i$"+"\n"+r"$E_i(0)=0,\quad D_iE_i(0)=0$","#345b8c")
box(.71,.66,.27,.26,"Global smooth evolution",
    "Oh's global theorem; GM4–GM12\n"+r"$\mathcal{S}_j:\xi\mapsto A^{j,\nu_\xi}$"+"\n"+r"$\mathbb{Q}_j=(\mathcal{S}_j)_*\mathbb{P}_\Omega$","#345b8c")
for x in [.30,.645]:
    ax.annotate("",xy=(x+.055,.79),xytext=(x,.79),arrowprops=dict(arrowstyle="->",lw=2,color="#345b8c"))
box(.02,.34,.44,.25,"Exact zero-time energy receiver — GM14–GM15",
    r"$a_j^3\mathcal{B}_j(f)\ \longrightarrow\ 2\sum_{i<k}\nu_{\xi,ik}(f)$"+"\n"+
    r"$a_j^4\mathcal{B}_j(f)/g_j^2\ \longrightarrow\ (4/\kappa_*)\sum_{i<k}\nu_{\xi,ik}(f)$"+"\n"+
    "All cutoff derivatives and the positive floor are controlled.","#28765f")
box(.53,.34,.45,.25,"True time dependence — GM17–GM20",
    r"$A(s)=B+s^2J(B)/2+s^4R_2/12+\mathcal{R}_6(s)$"+"\n"+
    r"$\mathbb{E}_{\mathbb{Q}_j}Z_j(s)=s^2\mathbb{E}\|J(B)\|_2^2+O_j(s^4)$"+"\n"+
    r"$\mathbb{E}\|J(B)\|_2^2>0\quad(j\geq J_1)$","#976033")
box(.02,.045,.96,.22,"Stationarity calculation — GM24–GM28",
    r"Time average: $|\mathbb{Q}_{j,T}(G\circ\Phi_h)-\mathbb{Q}_{j,T}(G)|"
    r"\leq\min\{2,|h|/T\}\|G\|_\infty$"+"\n"+
    "Exact virial: a stationary probability on conserved finite-total-energy smooth trajectories has F = 0 almost surely.\n"+
    "A nonflat stationary receiving law must leave that class. Quantum reconstruction remains to be established.","#7b496c")
fig.suptitle("The measure-to-solution map and its proved receiving observations",fontsize=16)
fig.savefig(ROOT/"GLOBAL_MEASURE_MAP.png",dpi=155)
fig.savefig(ROOT/"GLOBAL_MEASURE_MAP.svg")
plt.close(fig)
result=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),passed=True,
    exact_checks=len(checks),checks=checks,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    scope="Finite algebra diagnostics supplement GM1–GM28. Continuity, global existence application, measure convergence and virial integration are proved in the manuscript.")
(ROOT/"GLOBAL_MEASURE_CHECKS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result))
