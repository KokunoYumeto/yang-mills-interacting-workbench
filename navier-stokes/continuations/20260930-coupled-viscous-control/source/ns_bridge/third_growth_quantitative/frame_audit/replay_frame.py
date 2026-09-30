"""Exact algebra replay for frame_body.tex; analytic proofs are in the TeX."""
from pathlib import Path
import hashlib
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
checks = []

def check(name, expr):
    entries = list(expr) if isinstance(expr, sp.MatrixBase) else [expr]
    reduced = [sp.factor(sp.trigsimp(sp.simplify(x))) for x in entries]
    passed = all(x == 0 for x in reduced)
    checks.append({"name": name, "passed": passed})
    if not passed:
        raise AssertionError((name, reduced))

bg = sp.sqrt(2)-1
vr, vt = sp.Matrix([1,-bg]), sp.Matrix([bg,1])
Jg = sp.Matrix([[3,1],[1,5]])
Tg, Lg = 4+sp.sqrt(2), 4-sp.sqrt(2)
check("source_temporal_eigenvector", Jg*vt-Tg*vt)
check("source_radial_eigenvector", Jg*vr-Lg*vr)
check("source_dual_directions_orthogonal", vr.dot(vt))
check("source_dual_direction_length", vt.dot(vt)-(1+bg**2))
h, rho, kaps = sp.symbols("h rho kappa_s", real=True)
dr = 2*((1+h)*rho-h*kaps)
check("source_dr_retains_twice_h_kappa", dr/2-(1+h)*rho+h*kaps)
Yr, Yt = sp.symbols("Y_r Y_t", real=True)
eta = vt.dot(sp.Matrix([Yr,Yt]))/(1+bg**2)
getagrad = sp.Matrix([sp.diff(eta,Yr),sp.diff(eta,Yt)])
check("source_Li_eta_zero", getagrad.dot(vr))
check("source_Ni_eta_one", getagrad.dot(vt)-1)
Q, ti, li, rr, tt, rzero, ci = sp.symbols(
    "Q T_power L_power radius time rzero ci", positive=True)
drexact = sp.symbols("d_r", real=True)
Yeval = li*vr*rr**drexact+ti*vt*tt
veval = (vt.dot(Yeval)/(1+bg**2)+rzero)/(ti*Q**(1+h))
check("physical_clock_radial_derivative_zero", sp.diff(veval,rr))
check("physical_clock_time_derivative", sp.diff(veval,tt)-Q**(-1-h))
check("chart_clock_time_derivative_one", Q**(1+h)*sp.diff(veval,tt)-1)

sa, cc, pp, uu, angle, nt = sp.symbols("s_a c P u angle n_t", real=True)
er = sp.Matrix([1,0,0])
Ka = sp.Matrix([0,sp.cos(angle),sp.sin(angle)])
Na = sp.Matrix([0,sp.sin(angle),-sp.cos(angle)])
Un = sp.Matrix.hstack(er-sa*Ka, Na)
M = sp.Matrix([[1,1],[cc,-cc]])
Bn = Un*M
n = nt*(sa*er+Ka)
rows = sp.Matrix.vstack(er.T,Na.T)
Minv = sp.Matrix([[1,1/cc],[1,-1/cc]])/2
Bl = Minv*rows
check("actual_U_tangency", n.T*Un)
check("source_U_left_inverse", rows*Un-sp.eye(2))
check("source_M_inverse", Minv*M-sp.eye(2))
check("actual_B_tangency", n.T*Bn)
check("actual_B_left_inverse", Bl*Bn-sp.eye(2))
g2 = 1+sa**2
gram = sp.Matrix([[g2+cc**2,g2-cc**2],[g2-cc**2,g2+cc**2]])
check("actual_B_gram", Bn.T*Bn-gram)
check("actual_B_first_singular_square", gram*sp.Matrix([1,1])-2*g2*sp.Matrix([1,1]))
check("actual_B_second_singular_square", gram*sp.Matrix([1,-1])-2*cc**2*sp.Matrix([1,-1]))
check("source_ambient_left_inverse_gram", Bl*Bl.T-Minv*Minv.T)
yc = -pp*sp.Matrix([1,uu])
t = Bn*yc
expected_t = -pp*(1+uu)*er + pp*sa*(1+uu)*Ka-pp*cc*(1-uu)*Na
check("actual_direct_candidate_components", t-expected_t)
check("actual_direct_candidate_norm_square", t.dot(t)-pp**2*(g2*(1+uu)**2+cc**2*(1-uu)**2))
check("actual_direct_candidate_radial_covariance", t[0]*(t-t[0]*er)-(-pp**2*sa*(1+uu)**2*Ka+pp**2*cc*(1-uu**2)*Na))

alpha, dc, aa, bb, delta, lam, chi, chip = sp.symbols(
    "alpha d_c a_3 b_3 delta_nu lambda chi chi_prime", real=True)
e11,e12,e21,e22 = sp.symbols("E11 E12 E21 E22", real=True)
Ec = sp.Matrix([[e11,e12],[e21,e22]])
Cc = sp.Matrix([[-dc,aa],[bb,-dc]])
H = sp.diag(lam,-lam)+Ec
mismatch = chi*(alpha*Cc-H+delta*sp.eye(2))*yc+chip*yc
Delta = delta-alpha*dc
expected_mismatch = -pp*(chi*sp.Matrix([
    Delta-lam-e11+(alpha*aa-e12)*uu,
    alpha*bb-e21+(Delta+lam-e22)*uu])+chip*sp.Matrix([1,uu]))
check("exact_cutoff_principal_residual_entries", mismatch-expected_mismatch)
check("signed_diffusion_mismatch_first_coordinate", sp.diff(mismatch[0],dc)-alpha*chi*pp)
check("signed_diffusion_mismatch_second_coordinate", sp.diff(mismatch[1],dc)-alpha*chi*pp*uu)
nuNS, mm, eps, kk, nsq = sp.symbols("nu_NS m epsilon k normal_square", positive=True)
physical_delta = nuNS*mm**2*eps*kk**2*nsq
check("physical_viscosity_multiplier_retained", sp.diff(physical_delta,nuNS)-mm**2*eps*kk**2*nsq)

S, ui, zz1, zz2, env0 = sp.symbols("S_3 u_i z_1 z_2 envelope0", real=True)
z = sp.Matrix([zz1,zz2])
Z = sp.Matrix([[zz1,-zz2],[zz2,zz1]])
W = sp.Matrix([[1,ui],[-ui,1]])
L0 = -Z*W/(S*(1+ui**2))
L0inv = -S*sp.Matrix([[1,-ui],[ui,1]])*Z.T/(zz1**2+zz2**2)
seed = -S*sp.Matrix([1,ui])
check("actual_unscaled_seed_to_general_target", L0*seed-z)
check("L0_explicit_right_inverse", L0*L0inv-sp.eye(2))
check("L0_explicit_left_inverse", L0inv*L0-sp.eye(2))
check("L0_exact_determinant", L0.det()-(zz1**2+zz2**2)/(S**2*(1+ui**2)))
check("L0_exact_conformal_gram", L0.T*L0-(zz1**2+zz2**2)/(S**2*(1+ui**2))*sp.eye(2))
check("L0_inverse_exact_conformal_gram", L0inv.T*L0inv-S**2*(1+ui**2)/(zz1**2+zz2**2)*sp.eye(2))
sourceL0 = L0.subs({zz1:env0,zz2:0})
check("actual_seed_to_source_Lemma_7_4_initial_vector", sourceL0*seed-sp.Matrix([env0,0]))

A0, mu, freq, sig2, ni = sp.symbols("A0 mu lambda_hat_3 sigma_2 n_i", positive=True)
Pstar = A0/mu*freq**(-sp.Rational(7,8))
uibirth = mu*freq/(sig2*sp.sqrt(ni))
check("original_endpoint_vorticity_scale", Pstar*uibirth-A0/(sig2*sp.sqrt(ni))*freq**sp.Rational(1,8))

Di = sp.diag(1,ui)
balanced = Di.inv()*Cc*Di
check("coupled_balance_with_actual_initial_ratio", balanced-sp.Matrix([[-dc,aa*ui],[bb/ui,-dc]]))
beta = (aa*ui+bb/ui)/2
symbalanced = (balanced+balanced.T)/2
check("balanced_upper_energy_eigenvalue", symbalanced*sp.Matrix([1,1])-(-dc+beta)*sp.Matrix([1,1]))
check("balanced_lower_energy_eigenvalue", symbalanced*sp.Matrix([1,-1])-(-dc-beta)*sp.Matrix([1,-1]))
check("exact_intertwiner_determinant_rate", sp.trace(H-delta*sp.eye(2))-alpha*sp.trace(Cc)-(e11+e22-2*delta+2*alpha*dc))

# Check differentiation of the concrete two-by-two inverse, rather than
# treating inverse differentiation as a formal rewrite rule.
x11,x12,x21,x22 = sp.symbols("x11 x12 x21 x22", real=True)
d11,d12,d21,d22 = sp.symbols("d11 d12 d21 d22", real=True)
X = sp.Matrix([[x11,x12],[x21,x22]])
D = sp.Matrix([[d11,d12],[d21,d22]])
Xp = D*X
varsx = list(X)
valsxp = list(Xp)
Xinvprime = X.inv().applyfunc(lambda f:sum(sp.diff(f,x)*v for x,v in zip(varsx,valsxp)))
check("actual_two_by_two_inverse_derivative", Xinvprime+X.inv()*D)
detprime = sum(sp.diff(X.det(),x)*v for x,v in zip(varsx,valsxp))
check("actual_two_by_two_Liouville_identity", detprime-sp.trace(D)*X.det())

receipt = {
    "scope":"Exact source clock, actual frame, signed principal residual and actual-seed source-pulse finite intertwiner",
    "analytic_proofs":"frame_body.tex; not inferred from the algebra replay",
    "source_pdf_sha256":"0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f",
    "tex_sha256":hashlib.sha256((HERE/"frame_body.tex").read_bytes()).hexdigest(),
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "check_count":len(checks),
    "passed":all(c["passed"] for c in checks),
    "checks":checks,
}
(HERE/"replay_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"check_count":len(checks),"passed":receipt["passed"],"tex_sha256":receipt["tex_sha256"]}))
