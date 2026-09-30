"""Exact replay for source-operation bridge; analytic proofs remain in TeX."""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
checks = []
def check(name,expr):
    entries=list(expr) if isinstance(expr,s.MatrixBase) else [expr]
    reduced=[s.simplify(s.expand(x)) for x in entries]
    ok=all(x==0 for x in reduced)
    checks.append({"name":name,"passed":ok})
    if not ok:
        raise AssertionError((name,reduced))

r,z,t,Y=s.symbols("r z t Y",real=True,positive=True)
Crr=s.Function("Crr")(r,z,t)
Ctt=s.Function("Ctheta_theta")(r,z,t)
Crz=s.Function("Crz")(r,z,t)
g=-s.diff(Crr,r)-Crr/r-s.diff(Crz,z)+Ctt/r
check("actual_pressure_defect_boundary_identity",
      g-((Ctt-Crr)/r-s.diff(Crz,z))+s.diff(Crr,r))
check("actual_second_radial_source_moment_boundary_identity",
      r*r*g-(r*(Crr+Ctt)-s.diff(r*r*Crz,z))+s.diff(r*r*Crr,r))
p=s.Function("pressure")(r,z,t)
rho=s.Function("rho")(r,z,t)
P=s.Function("pressure_defect")(z,t)
check("compact_pressure_weighted_identity",
      (s.diff(r*r*p,r)/2-r*p-r*r*(g-rho*P)/2).subs(s.diff(p,r),g-rho*P))
q=s.Function("q")(z,t)
x=r/s.sqrt(q)
e=s.symbols("e",real=True)
bhat=s.Function("bhat")
b=q**(-(e+1)/2)*bhat(x)
check("moving_bump_full_axial_derivative",
      s.diff(b,z)+s.diff(q,z)/(2*q)*((e+1)*b+r*s.diff(b,r)))
c0=s.symbols("c0",real=True)
crho=c0*q
check("moving_pressure_bump_second_moment_derivative",
      s.diff(crho,z)-s.diff(q,z)/q*crho)
Jraw=s.Function("raw_J1")(z,t)
K=s.Function("radial_pressure_moment")(z,t)
check("axial_pressure_coupling_keeps_c_rho_derivative",
      s.diff(Jraw+K+crho*P,z)
      -(s.diff(Jraw,z)+s.diff(K,z)+crho*s.diff(P,z)+c0*s.diff(q,z)*P))

Q,h,A=s.symbols("Q h A",positive=True)
D=s.Rational(1,2)-h
check("source_theta_moment_normalization_exponent",
      h+D+(2*A-s.Rational(3,2))-(2*A-1))
check("source_axial_moment_normalization_exponent",
      h+D+(2*A-1)-(2*A-s.Rational(1,2)))
check("source_c_rho_P_normalization_exponent",-1+2*A-(2*A-1))
A_source=s.Rational(1,2)+h
Tg,ii=s.symbols("T_g i_0",positive=True)
ci=Tg**ii*Q**(1+h)
check("temporal_update_physical_inverse_keeps_all_Q_powers",
      Q**(-A_source)*ci**(-1)*Q**(2*A_source+s.Rational(1,2))-Tg**(-ii))
check("temporal_update_physical_time_unit_equals_residual_unit",
      -A_source-(1+h)-(-2*A_source-s.Rational(1,2)))
check("temporal_update_physical_fast_direction_factor",
      Q**(-1-h)*ci-Tg**ii)
check("temporal_radial_potential_axial_factor_is_epsilon",
      s.Rational(1,2)-D-h)

qq,xx,amp,lam=s.symbols("qscale x a lambda",positive=True)
phi,psi=s.symbols("phi psi",real=True)
rr=s.sqrt(qq)*xx
V=qq**(-A)*amp*xx**(-1-2*lam)
dv=qq**(-A)*phi
dgamma=qq**(-A)*psi
jac=s.sqrt(qq)
check("five_row_angular_velocity_scale",rr**2*dv*jac-qq**(s.Rational(3,2)-A)*xx**2*phi)
check("five_row_axial_velocity_scale",rr*dgamma*jac-qq**(1-A)*xx*psi)
check("five_row_pressure_scale",2*V/rr*dv*jac-qq**(-2*A)*2*amp*xx**(-2-2*lam)*phi)
check("five_row_theta_flux_scale",rr**2*V*dgamma*jac-qq**(s.Rational(3,2)-2*A)*amp*xx**(1-2*lam)*psi)
check("five_row_axial_flux_scale",-rr*V*dv*jac+qq**(1-2*A)*amp*xx**(-2*lam)*phi)
check("fifth_row_single_radius_from_radial_pressure",
      -s.Rational(1,2)*rr**2*(2*V/rr)*dv+rr*V*dv)
R=s.symbols("R",positive=True)
Vfixed=Q**A*qq**(-A)*amp*(s.sqrt(Q)*R/s.sqrt(qq))**(-1-2*lam)
Vexpected=(Q/qq)**A*amp*(s.sqrt(Q/qq)*R)**(-1-2*lam)
check("reserved_patch_chart_factor_Q_over_q_to_A",Vfixed-Vexpected)
t1,t2,t3=s.symbols("t1 t2 t3",real=True)
Vm=s.Matrix([[1,t1,t1*t1],[1,t2,t2*t2],[1,t3,t3*t3]])
check("three_bump_Vandermonde_determinant",
      Vm.det()-(t2-t1)*(t3-t1)*(t3-t2))
mu1,mu2,muang,muz,muax=s.symbols("mu1 mu2 muang muz muax",positive=True)
Atheta=s.diag(mu2,2*amp*muang,-amp*muz)*Vm
check("angular_moment_matrix_full_determinant",
      Atheta.det()+2*amp**2*mu2*muang*muz*(t2-t1)*(t3-t1)*(t3-t2))
Az=s.Matrix([[mu1,mu1*t1],[amp*muax,amp*muax*t2]])
check("axial_moment_matrix_full_determinant",Az.det()-amp*mu1*muax*(t2-t1))

# Verify the complete nonlinear radial source update with an actual
# auxiliary derivative operator; no auxiliary-independent old mean
# assumption is inserted.
nu=s.symbols("nu_NS",positive=True)
ar=s.Function("radial_auxiliary_coefficient")(r)
at=s.symbols("temporal_auxiliary_coefficient",real=True)
Dr=lambda f:s.diff(f,r)+ar*s.diff(f,Y)
Dt=lambda f:s.diff(f,t)+at*s.diff(f,Y)
Lapl=lambda f:Dr(Dr(f))+Dr(f)/r+s.diff(f,z,2)
baseb=s.Function("base_radial")(r,z,t)
baseV=s.Function("base_swirl")(r,z,t)
baseG=s.Function("base_axial")(r,z,t)
beta=s.Function("old_beta")(r,z,t,Y)
vv=s.Function("old_v")(r,z,t,Y)
gg=s.Function("old_gamma")(r,z,t,Y)
dbeta=s.Function("delta_beta")(r,z,t)
dvv=s.Function("delta_v")(r,z,t)
dgg=s.Function("delta_gamma")(r,z,t)
wrr=s.Function("Wrr")(r,z,t,Y)
wrz=s.Function("Wrz")(r,z,t,Y)
wtt=s.Function("Wtt")(r,z,t,Y)
def radial_source(be,ve,ga):
    return (-Dt(be)-Dr(2*baseb*be+be*be+wrr)
            -(2*baseb*be+be*be+wrr)/r
            -s.diff(baseb*ga+baseG*be+be*ga+wrz,z)
            +(2*baseV*ve+ve*ve+wtt)/r
            +nu*(Lapl(be)-be/r**2))
gold=radial_source(beta,vv,gg)
gnew=radial_source(beta+dbeta,vv+dvv,gg+dgg)
Rg=(-Dt(dbeta)-Dr(2*baseb*dbeta+2*beta*dbeta+dbeta**2)
    -(2*baseb*dbeta+2*beta*dbeta+dbeta**2)/r
    -s.diff(baseb*dgg+baseG*dbeta+beta*dgg+gg*dbeta+dbeta*dgg,z)
    +(2*vv*dvv+dvv**2)/r+nu*(Lapl(dbeta)-dbeta/r**2))
check("complete_nonlinear_radial_source_remainder",gnew-gold-2*baseV*dvv/r-Rg)
Jth_old=baseG*vv+baseV*gg+gg*vv
Jth_new=baseG*(vv+dvv)+baseV*(gg+dgg)+(gg+dgg)*(vv+dvv)
check("theta_flux_defect_exact_nonlinear_remainder",
      Jth_new-Jth_old-baseG*dvv-baseV*dgg-(gg*dvv+vv*dgg+dgg*dvv))
Jz_old=2*baseG*gg+gg**2-r*gold/2
Jz_new=2*baseG*(gg+dgg)+(gg+dgg)**2-r*gnew/2
check("axial_flux_defect_exact_nonlinear_remainder",
      Jz_new-Jz_old-(2*baseG*dgg-baseV*dvv)-(2*gg*dgg+dgg**2-r*Rg/2))

# Actual radial-potential scaling and all axial coefficient derivatives.
sj=s.Function("s_j")(z,t)
phifun=s.Function("Psi_j")
Psipot=q**(s.Rational(1,2)-A)*sj*phifun(x)
betexp=-q**(s.Rational(1,2)-A)*(s.diff(sj,z)*phifun(x)+s.diff(q,z)/q*sj*
              ((s.Rational(1,2)-A)*phifun(x)-x*s.Subs(s.Derivative(phifun(s.Symbol("xx")),s.Symbol("xx")),s.Symbol("xx"),x)/2))
check("induced_radial_velocity_full_q_and_target_derivatives",-s.diff(Psipot,z)-betexp)
potential=s.Function("Psi")(r,z,t)
check("azimuthal_potential_exact_divergence",
      s.diff(-s.diff(potential,z),r)-s.diff(potential,z)/r
      +s.diff(s.diff(potential,r)+potential/r,z))
data={
    "scope":"Actual candidate pressure-defect bridge, source five-row map, nonlinear recomputation",
    "analytic_scope":"Written proofs and attributed source estimates in operation_body.tex; algebra checks are not terminal iteration estimates",
    "source_pdf_sha256":"0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f",
    "tex_sha256":hashlib.sha256((HERE/"operation_body.tex").read_bytes()).hexdigest(),
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "check_count":len(checks),
    "passed":all(c["passed"] for c in checks),
    "checks":checks,
}
(HERE/"replay_receipt.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:data[k] for k in ("check_count","passed","tex_sha256")}))
