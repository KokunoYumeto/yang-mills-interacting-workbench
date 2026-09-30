"""Exact algebra replay for first_stage_audit.tex; no numerical proof claims.

Run: python replay_first_stage.py
Only the adjacent JSON receipt is written. Integral comparison, positivity,
root existence, and convergence proofs are written in the TeX artifact.
"""
from pathlib import Path
import hashlib
import json
import sympy as S

ROOT = Path(__file__).resolve().parent
# audit -> finite_stage -> coupled_viscous_control -> lanes -> notebook
SOURCE = ROOT.parents[3] / "research" / "alpoge_buckmaster_boussinesq.pdf"
CHECKS = []


def check(name, expressions):
    if not isinstance(expressions, (list, tuple, S.MatrixBase)):
        expressions = [expressions]
    residues = [S.cancel(S.trigsimp(S.expand(expr))) for expr in expressions]
    if any(residue != 0 for residue in residues):
        raise AssertionError((name, residues))
    CHECKS.append({"name": name, "residuals": [str(r) for r in residues], "passed": True})


t, s, A0, lam, sigma, mu = S.symbols("t s A0 Lambda sigma0 mu_sp", positive=True)
alpha = S.Function("alpha")(t)
ad = S.diff(alpha, t)
J = S.Matrix([[0, -1], [1, 0]])
R = S.Matrix([[S.cos(alpha), -S.sin(alpha)], [S.sin(alpha), S.cos(alpha)]])
e2 = S.Matrix([0, 1])
p = S.Matrix([S.sin(s), S.cos(s)])
zeta = R*p
G = -A0*R*e2
D = ad*J
check("rotation_transport_zeta", S.diff(zeta, t)+D.T*zeta)
check("rotation_transport_base_G", S.diff(G, t)+D.T*G)
check("rotation_matrix_transport", S.diff(R,t)-D*R)
check("determinant_one", R.det()-1)
check("unit_length_original_zeta", zeta.dot(zeta)-1)
check("a_coefficient_original_dot_product", (J*zeta).dot(G)+A0*S.sin(s))

x1,x2=S.symbols("x1 x2",real=True)
x=S.Matrix([x1,x2])
phase=lam*zeta.dot(x)
check("physical_phase_transport",S.diff(phase,t)+(D*x).dot(S.Matrix([S.diff(phase,x1),S.diff(phase,x2)])))
pb=ad**2*x.dot(x)/2+G.dot(x)*x2/2
fpb=S.Matrix([S.diff(pb,x1),S.diff(pb,x2)])
fb=(S.diff(alpha,t,2)-G[0]/2)*J*x
check("affine_momentum_force_and_pressure",(S.diff(D,t)+D*D)*x+fpb-G.dot(x)*e2-fb)
check("affine_scalar_transport",S.diff(G.dot(x),t)+(D*x).dot(G))

tau=S.symbols("tau",real=True)
Pent=S.symbols("P_ent",positive=True)
P=S.Function("P")(tau)
z=S.Function("z")(tau)
Gamma=sigma*S.sin(s)
theta=-Pent*P
omega=-lam*Pent*S.diff(P,tau)/sigma
a=sigma**2*S.sin(s)/lam
b=lam*S.sin(s)*z
check("physical_temperature_amplitude",Gamma*S.diff(theta,tau)-a*omega)
check("physical_vorticity_amplitude",(Gamma*S.diff(omega,tau)-b*theta).subs(S.diff(P,tau,2),z*P))
check("physical_ratio",sigma*omega/(lam*theta)-S.diff(P,tau)/P)

compression,mass,y=S.symbols("C m y",positive=True)
chi=S.Function("chi")(y)
h=S.Function("h")(y)
V=compression*S.diff(chi,y)/chi
check("compressed_Riccati_equation",(S.diff(V,y)+mass*h+V**2/compression).subs(S.diff(chi,y,2),-mass*h*chi/compression))

Pf=S.symbols("P_f",positive=True)
Gnew=S.Matrix([A0*S.sin(s),-A0*S.cos(s)-lam*Pf])
check("terminal_gradient_norm",Gnew.dot(Gnew)-(A0**2+lam**2*Pf**2+2*A0*lam*Pf*S.cos(s)))

d,r,L2,s2=S.symbols("d r Lambda2 s2",positive=True)
Th=S.Function("Theta0")(r)
Om=S.Function("Omega0")(r)
ar=S.Function("a")(r)
br=S.Function("b")(r)
decay=S.exp(-d*lam**2*r)
check("common_diffusion_temperature",(S.diff(decay*Th,r)-ar*decay*Om+d*lam**2*decay*Th).subs(S.diff(Th,r),ar*Om))
check("common_diffusion_vorticity",(S.diff(decay*Om,r)-br*decay*Th+d*lam**2*decay*Om).subs(S.diff(Om,r),br*Th))

a2=(lam*Pf*S.exp(-d*lam**2*r)*S.sin(s2)+A0*S.sin(s+s2))/L2
b2=L2*S.sin(s2)
check("evolving_parent_feedback_derivative",S.diff(a2,r)+d*lam**3*Pf*S.exp(-d*lam**2*r)*S.sin(s2)/L2)
c0=A0*S.sin(s+s2)*S.sin(s2)
c1=lam*Pf*S.sin(s2)**2
check("evolving_parent_feedback_potential",a2*b2-c0-c1*S.exp(-d*lam**2*r))

W=S.Function("W")(r)
delta=S.symbols("delta2",nonnegative=True)
theta2=S.exp(-delta*r)*S.diff(W,r)/b2
omega2=S.exp(-delta*r)*W
check("feedback_scalar_to_pair_vorticity",S.diff(omega2,r)+delta*omega2-b2*theta2)
check("feedback_scalar_to_pair_temperature",(S.diff(theta2,r)+delta*theta2-a2*omega2).subs(S.diff(W,r,2),a2*b2*W))

xx,q,c0s,c1s=S.symbols("x q c0 c1",positive=True)
f=S.Function("f")(xx)
dr_operator=(q**2/4)*(xx**2*S.diff(f,xx,2)+xx*S.diff(f,xx))
potential=(c0s+q**2*xx**2/4)*f
transformed=(q**2/4)*(xx**2*S.diff(f,xx,2)+xx*S.diff(f,xx)-(xx**2+4*c0s/q**2)*f)
check("exact_feedback_coordinate_operator",dr_operator-potential-transformed)

n,vartheta,anprev=S.symbols("n vartheta a_prev",positive=True)
an=anprev/(4*n*(n+vartheta))
check("fundamental_series_recurrence",((vartheta+2*n)**2-vartheta**2)*an-anprev)

I=S.Function("I")(xx)
g=f*I
Iprime=1/(xx*f**2)
g_residue=S.diff(g,xx,2)+S.diff(g,xx)/xx-(1+vartheta**2/xx**2)*g
g_residue=g_residue.subs(S.diff(I,xx,2),S.diff(Iprime,xx)).subs(S.diff(I,xx),Iprime)
g_residue=g_residue.subs(S.diff(f,xx,2),(1+vartheta**2/xx**2)*f-S.diff(f,xx)/xx)
check("fundamental_pair_reduction_of_order",g_residue)
check("fundamental_pair_nonzero_Wronskian",(f*S.diff(g,xx)-S.diff(f,xx)*g).subs(S.diff(I,xx),Iprime)-1/xx)

nu_t,kappa,tilde_lam,tilde_kappa=S.symbols("nu_time kappa_phys lambda1 kappa_tilde",positive=True)
check("diffusive_scaling_exponent",(kappa*mu**2/nu_t)*tilde_lam**2*(nu_t*r)-kappa*(mu*tilde_lam)**2*r)
check("seed_threshold_exponent",-(S.symbols("k1")+6)+(S.symbols("k1")+S.Rational(41,8))+S.Rational(7,8))

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

receipt={
 "status":"all exact symbolic identities passed",
 "check_count":len(CHECKS),
 "checks":CHECKS,
 "sympy_version":S.__version__,
 "proof_file":"first_stage_audit.tex",
 "proof_sha256":digest(ROOT/"first_stage_audit.tex"),
 "script_sha256":digest(Path(__file__)),
 "source_file":"research/alpoge_buckmaster_boussinesq.pdf",
 "source_sha256":digest(SOURCE),
 "analytical_proof_location":"first_stage_audit.tex: all-trial positivity, unique root, gain estimates, holding, exact feedback solution and series convergence",
 "limitations":["The affine-wave proof does not assert compact spatial support.","The equal-diffusion continuation uses the sine profile.","No infinite viscous iteration is claimed.","No Lean process was started."]
}
(ROOT/"replay_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":receipt["status"],"check_count":len(CHECKS),"receipt":"replay_receipt.json"}))
