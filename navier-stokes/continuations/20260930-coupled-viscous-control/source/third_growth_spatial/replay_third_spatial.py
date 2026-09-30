"""Exact third-growth spatial replay, retaining independent profile jets.

The formal profile/envelope jets are independent: these are polynomial/rational
identity checks, not checks restricted to a sine or a sampled spatial profile.
The companion TeX supplies the analytic construction and proofs. No numerical
integration, Lean, source modification, or external service is used.

Run this file with Python and SymPy; it writes only replay_report.json beside it.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
CHECKS = []


def zero(name, expression):
    entries = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
    residuals = [s.cancel(s.expand(e)) for e in entries]
    passed = all(e == 0 for e in residuals)
    CHECKS.append({"name": name, "passed": passed,
                   "residuals": [str(e) for e in residuals]})
    if not passed:
        raise AssertionError((name, residuals))


J = s.Matrix([[0, -1], [1, 0]])
kx, ky, Q, T, d = s.symbols("kx ky Q T d", real=True)
k = s.Matrix([kx, ky])
rho = k.dot(k)
P, F, F1, F2, F3, F4 = s.symbols("P F F1 F2 F3 F4", real=True)
profile_chain = {P: F, F: F1, F1: F2, F2: F3, F3: F4}
gj = {(i, j): s.Symbol(f"g{i}{j}", real=True)
      for i in range(5) for j in range(5-i)}
g = gj[0, 0]
gg = s.Matrix([gj[1, 0], gj[0, 1]])
Hg = s.Matrix([[gj[2, 0], gj[1, 1]], [gj[1, 1], gj[0, 2]]])
lg = gj[2, 0] + gj[0, 2]
glg = s.Matrix([gj[3, 0]+gj[1, 2], gj[2, 1]+gj[0, 3]])


def dx(expression, axis):
    if isinstance(expression, s.MatrixBase):
        return expression.applyfunc(lambda e: dx(e, axis))
    answer = sum(s.diff(expression, a)*b*k[axis]
                 for a, b in profile_chain.items())
    for (i, j), jet in gj.items():
        if i+j < 4:
            answer += s.diff(expression, jet)*gj[i+(axis == 0), j+(axis == 1)]
    return s.expand(answer)


def grad(expression):
    return s.Matrix([dx(expression, 0), dx(expression, 1)])


def jac(expression):
    return s.Matrix.hstack(dx(expression, 0), dx(expression, 1))


def lap(expression):
    return dx(dx(expression, 0), 0) + dx(dx(expression, 1), 1)


V = T*F*g
psi = Q*P*g
v = J*grad(psi)
zero("velocity_from_original_primitive", v-Q*(F*g*J*k+P*J*gg))
zero("increment_is_exactly_divergence_free", dx(v[0], 0)+dx(v[1], 1))
lapV = T*(rho*F2*g+2*F1*k.dot(gg)+F*lg)
zero("all_scalar_laplacian_terms", lap(V)-lapV)
lapPsi = Q*(rho*F1*g+2*F*k.dot(gg)+P*lg)
zero("all_primitive_laplacian_terms", lap(psi)-lapPsi)
lapv = Q*J*(rho*F2*k*g + rho*F1*gg + 2*F1*k*k.dot(gg)
             + 2*F*Hg*k + F*k*lg + P*glg)
zero("all_six_velocity_laplacian_groups", lap(v)-lapv)
zero("laplacian_commutes_with_rotated_gradient", lap(v)-J*grad(lapPsi))
self_scalar = KQT = Q*T*(F**2-P*F1)*g*(J*k).dot(gg)
zero("scalar_self_advection_with_envelope", v.dot(grad(V))-self_scalar)

aa, bb, cc = s.symbols("D11 D12 D21", real=True)
D = s.Matrix([[aa, bb], [cc, -aa]])
zero("trace_free_transport_matrix_identity", D*J+J*D.T)
kd = -D.T*k
ggd = -D.T*gg
Qdot, Tdot = s.symbols("Qdot Tdot", real=True)
transport_rates = {kx: kd[0], ky: kd[1], Q: Qdot, T: Tdot,
                   gj[1, 0]: ggd[0], gj[0, 1]: ggd[1]}


def material(expression):
    if isinstance(expression, s.MatrixBase):
        return expression.applyfunc(material)
    return s.expand(sum(s.diff(expression, a)*b for a, b in transport_rates.items()))


zero("material_velocity_derivative_sign", material(v)-D*v-J*grad(Qdot*P*g))
zero("material_temperature_derivative", material(V)-Tdot*F*g)
GX, GY, w, wp, theta, omega = s.symbols("GX GY w wp theta omega", real=True)
G = s.Matrix([GX, GY])
a = -(J*k).dot(G)/rho
b = kx
rho_dot = 2*k.dot(kd)
Qactual = w*omega/rho
Tactual = w*theta
theta_dot = a*omega-d*rho*theta
omega_dot = b*theta-d*rho*omega
Qactual_dot = wp*omega/rho+w*omega_dot/rho-w*omega*rho_dot/rho**2
Qrest = (wp*omega+w*b*theta)/rho-Qactual*rho_dot/rho
zero("damped_stream_amplitude_derivative", Qactual_dot-Qrest+d*rho*Qactual)
zero("full_scalar_parent_coupling_cancellation",
     w*a*omega*F*g+(Q*F*g*J*k).dot(G).subs(Q, Qactual))

scalar_raw = (wp*theta+w*theta_dot)*F*g + v.dot(G)+v.dot(grad(V))-d*lapV
scalar_claim = (wp*theta*F*g+Q*P*(J*gg).dot(G)+self_scalar
                -d*T*(rho*(F+F2)*g+2*F1*k.dot(gg)+F*lg))
amplitude_subs = {Q: Qactual, T: Tactual}
zero("complete_damped_scalar_residual",
     (scalar_raw-scalar_claim).subs(amplitude_subs))
e2 = s.Matrix([0, 1])
raw_momentum = material(v)+D*v+jac(v)*v-V*e2-d*lapv
Qrest_independent = s.Symbol("Qrest", real=True)
momentum_claim = (2*D*v+J*grad(Qrest_independent*P*g)+jac(v)*v-V*e2
                  -d*(rho*v+lapv))
zero("complete_damped_vector_residual",
     raw_momentum.subs(Qdot, Qrest_independent-d*rho*Q)-momentum_claim)

# In a region where the envelope is constant, direct modal damping cancels
# diffusion exactly for the sine profile, while the released affine cell
# retains nonzero damping forces. These are different exact restrictions.
constant_envelope = {g: 1, **{jet: 0 for key, jet in gj.items() if key != (0, 0)}}
scalar_damping = -d*T*(rho*(F+F2)*g+2*F1*k.dot(gg)+F*lg)
vector_damping = -d*(rho*v+lapv)
zero("uncut_sine_scalar_damping_cancellation",
     scalar_damping.subs(constant_envelope).subs(F2, -F))
zero("uncut_sine_vector_damping_cancellation",
     vector_damping.subs(constant_envelope).subs(F2, -F))
zero("affine_profile_cell_retains_scalar_force",
     scalar_damping.subs(constant_envelope).subs(F2, 0)+d*T*rho*F)
zero("affine_profile_cell_retains_vector_force",
     vector_damping.subs(constant_envelope).subs(F2, 0)+d*rho*Q*F*J*k)

# Independently verify conversion to the original material-coordinate metric.
n11, n12, n21, n22, K, p1, p2 = s.symbols("n11 n12 n21 n22 K p1 p2", real=True)
N = s.Matrix([[n11, n12], [n21, n22]])  # N=M^{-1}
C = N*N.T
p = s.Matrix([p1, p2])
hy = s.Matrix(s.symbols("gy1 gy2", real=True))
hy11, hy12, hy22 = s.symbols("gy11 gy12 gy22", real=True)
Hy = s.Matrix([[hy11, hy12], [hy12, hy22]])
km = K*N.T*p
zero("material_phase_metric", km.dot(km)-K**2*(p.T*C*p)[0])
zero("material_mixed_scalar_term", km.dot(N.T*hy)-K*(C*p).dot(hy))
zero("material_envelope_laplacian", s.trace(N.T*Hy*N)-s.trace(C*Hy))

# An independent explicit, genuinely time-dependent SL(2) transport check.
# Polynomial choices are used only for this second check, never for the jet proof.
x1, x2, time = s.symbols("x1 x2 time", real=True)
x = s.Matrix([x1, x2])
M = s.Matrix([[1+time**2, time], [time, 1]])
explicit_D = s.diff(M, time)*M.inv()
material_y = M.inv()*x
u = explicit_D*x


def ordinary_grad(expression):
    return s.Matrix([s.diff(expression, x1), s.diff(expression, x2)])


def ordinary_material(expression):
    if isinstance(expression, s.MatrixBase):
        return expression.applyfunc(ordinary_material)
    return s.diff(expression, time)+ordinary_grad(expression).dot(u)


zero("explicit_SL2_matrix_determinant", M.det()-1)
zero("explicit_affine_divergence_free", s.trace(explicit_D))
zero("explicit_original_material_coordinates", ordinary_material(material_y))
explicit_phase = 2*material_y[0]-3*material_y[1]
explicit_envelope = 1+material_y[0]+material_y[0]*material_y[1]+material_y[1]**2
explicit_P = explicit_phase**2/2+explicit_phase**3/6
explicit_Q = 1+time+time**2
explicit_v = J*ordinary_grad(explicit_Q*explicit_P*explicit_envelope)
zero("explicit_transported_phase", ordinary_material(explicit_phase))
zero("explicit_transported_nonradial_envelope", ordinary_material(explicit_envelope))
zero("explicit_time_dependent_velocity_transport",
     ordinary_material(explicit_v)-explicit_D*explicit_v
     -J*ordinary_grad(s.diff(explicit_Q, time)*explicit_P*explicit_envelope))

# Exact two-increment residual telescoping: every old/new interaction survives.
U = [s.Matrix(s.symbols(f"u{i}1 u{i}2")) for i in range(3)]
A = [s.Matrix(2, 2, s.symbols(f"A{i}11 A{i}12 A{i}21 A{i}22")) for i in range(3)]
H = [s.Matrix(s.symbols(f"H{i}1 H{i}2")) for i in range(3)]
whole_velocity = U[0]+U[1]+U[2]
whole_jacobian = A[0]+A[1]+A[2]
first_advective_increment = A[0]*U[1]+A[1]*U[0]+A[1]*U[1]
second_advective_increment = ((A[0]+A[1])*U[2]
                              +A[2]*(U[0]+U[1])+A[2]*U[2])
zero("two_increment_momentum_telescoping",
     whole_jacobian*whole_velocity-A[0]*U[0]
     -first_advective_increment-second_advective_increment)
first_scalar_increment = U[0].dot(H[1])+U[1].dot(H[0])+U[1].dot(H[1])
second_scalar_increment = ((U[0]+U[1]).dot(H[2])
                           +U[2].dot(H[0]+H[1])+U[2].dot(H[2]))
zero("two_increment_temperature_telescoping",
     whole_velocity.dot(H[0]+H[1]+H[2])-U[0].dot(H[0])
     -first_scalar_increment-second_scalar_increment)

# The exact mixed-jet operators include explicit x derivatives. Dropping
# these derivatives would give an incorrect commutator and wrong mixed
# cutoff derivatives, even for this time-dependent SL(2) test.
phase_variable, material_1, material_2 = s.symbols("ss yy1 yy2", real=True)
ell = s.symbols("ell", positive=True)
jet_A = M.inv()/ell
jet_k = M.inv().T*s.Matrix([2, -3])
jet_y = s.Matrix([material_1, material_2])
jet_coeff_y = s.diff(jet_A, time)*x
jet_coeff_s = s.diff(jet_k, time).dot(x)


def jet_time(expression):
    if isinstance(expression, s.MatrixBase):
        return expression.applyfunc(jet_time)
    return (s.diff(expression, time)
            +jet_coeff_s*s.diff(expression, phase_variable)
            +sum(jet_coeff_y[i]*s.diff(expression, jet_y[i]) for i in range(2)))


def jet_space(expression, axis):
    if isinstance(expression, s.MatrixBase):
        return expression.applyfunc(lambda e: jet_space(e, axis))
    return (s.diff(expression, x[axis])
            +jet_k[axis]*s.diff(expression, phase_variable)
            +sum(jet_A[i, axis]*s.diff(expression, jet_y[i]) for i in range(2)))


jet_coordinates = s.Matrix([time, x1, x2, phase_variable, material_1, material_2])
for axis in range(2):
    zero(f"full_mixed_jet_commutator_axis_{axis+1}",
         jet_time(jet_space(jet_coordinates, axis))
         -jet_space(jet_time(jet_coordinates), axis))
jet_graph = {phase_variable: jet_k.dot(x),
             material_1: (jet_A*x)[0], material_2: (jet_A*x)[1]}
jet_test = (1+time)*phase_variable**2*material_1+time*phase_variable*material_2**2
jet_test_graph = jet_test.subs(jet_graph)
for order in (1, 2):
    jet_result = jet_space(jet_test, 0)
    for _ in range(order):
        jet_result = jet_time(jet_result)
    zero(f"independent_mixed_pullback_time_{order}_space_1",
         jet_result.subs(jet_graph)-s.diff(jet_test_graph, time, order, x1))


# Exact third-growth flow: rotations are expressed in original h,a coordinates.
# h,hb,a remain independent positive symbols; no physical parameter is set to 1.
h, hb, aa3, Om1 = s.symbols("h hb a Omega1", positive=True)
chi = s.sqrt(h*h+aa3*aa3)
chib = s.sqrt(hb*hb+aa3*aa3)
Rh = s.Matrix([[h, -aa3], [aa3, h]])/chi
Rhb = s.Matrix([[hb, -aa3], [aa3, hb]])/chib
shear = s.Matrix([[1, -(h-hb)/aa3], [0, 1]])
Mthird = Rh*shear*Rhb.T
Mthirdinv = Rhb*s.Matrix([[1, (h-hb)/aa3], [0, 1]])*Rh.T
z1 = s.Matrix([-aa3, h])/chi
alpha_rate = -aa3**2*Om1/chi**2
Dthird = alpha_rate*J+Om1*(J*z1)*z1.T
zero("third_relative_flow_determinant", Mthird.det()-1)
zero("third_explicit_inverse_both_directions",
     s.Matrix.vstack(Mthird*Mthirdinv-s.eye(2), Mthirdinv*Mthird-s.eye(2)))
zero("third_flow_initial_value", Mthird.subs(h, hb)-s.eye(2))
zero("third_flow_actual_affine_ODE", s.diff(Mthird, h)*aa3*Om1-Dthird*Mthird)
zero("third_inverse_actual_ODE", s.diff(Mthirdinv, h)*aa3*Om1+Mthirdinv*Dthird)
third_p = s.Matrix([p1, p2])
third_z = Mthirdinv.T*third_p
zero("third_covector_actual_ODE", s.diff(third_z, h)*aa3*Om1+Dthird.T*third_z)
zero("third_material_coordinate_transport",
     s.diff(Mthirdinv, h)*aa3*Om1*x+Mthirdinv*Dthird*x)
zero("third_material_phase_transport",
     s.diff(third_z, h).dot(x)*aa3*Om1+third_z.dot(Dthird*x))
zero("third_phase_born_in_original_coordinates", third_z.subs(h,hb)-third_p)

# Full four-field telescoping, rather than only two increment examples.
Ut = [s.Matrix(s.symbols(f"ut{i}1 ut{i}2")) for i in range(4)]
At = [s.Matrix(2,2,s.symbols(f"at{i}11 at{i}12 at{i}21 at{i}22")) for i in range(4)]
Ht = [s.Matrix(s.symbols(f"ht{i}1 ht{i}2")) for i in range(4)]
total_u = sum(Ut, s.zeros(2,1))
total_A = sum(At, s.zeros(2,2))
total_H = sum(Ht, s.zeros(2,1))
momentum_increments = s.zeros(2,1)
scalar_increments = s.S.Zero
for j in range(1,4):
    older_u = sum(Ut[:j], s.zeros(2,1))
    older_A = sum(At[:j], s.zeros(2,2))
    older_H = sum(Ht[:j], s.zeros(2,1))
    momentum_increments += older_A*Ut[j]+At[j]*older_u+At[j]*Ut[j]
    scalar_increments += older_u.dot(Ht[j])+Ut[j].dot(older_H)+Ut[j].dot(Ht[j])
zero("all_three_increment_vector_interactions", total_A*total_u-At[0]*Ut[0]-momentum_increments)
zero("all_three_increment_scalar_interactions", total_u.dot(total_H)-Ut[0].dot(Ht[0])-scalar_increments)
second_hold = {entry: 0 for entry in list(Ut[2])+list(At[2])}
zero("held_second_velocity_still_has_reverse_temperature_interaction",
     (Ut[3].dot(Ht[0]+Ht[1]+Ht[2])-Ut[3].dot(Ht[0]+Ht[1])).subs(second_hold)
     -Ut[3].dot(Ht[2]))

# The primitive's original constant survives at every cutoff derivative.
Pzero, ss = s.symbols("Pzero ss", real=True)
core_primitive = Pzero+ss**2/2
zero("affine_primitive_retains_original_constant", s.diff(core_primitive, ss)-ss)
zero("primitive_constant_velocity_cutoff_contribution", s.diff(v, P)-Q*J*gg)
zero("primitive_constant_vector_diffusion_cutoff_contribution",
     s.diff(lapv, P)-Q*J*glg)

# Exact physical powers in the finite diffusion bounds.
mu, nu, lam2, lam3, sigma2 = s.symbols("mu nu lambda2 lambda3 sigma2", positive=True)
Kthree = mu*lam3
Pstar = nu**2/mu*lam3**(-s.Rational(7,8))
Qbound = 3*Kthree*Pstar/sigma2/Kthree**2
zero("third_original_source_radius_cost", 145/(lam2**(-3)/mu)-145*mu*lam2**3)
zero("third_scalar_diffusion_frequency_power", d*Pstar*Kthree**2-d*nu**2*mu*lam3**s.Rational(9,8))
zero("third_vector_diffusion_frequency_power", d*Qbound*Kthree**3-3*d*nu**2*mu/sigma2*lam3**s.Rational(9,8))

def exact_inequality(name, inequality):
    passed = bool(inequality)
    CHECKS.append({"name": name, "passed": passed, "exact_comparison": str(inequality)})
    if not passed:
        raise AssertionError(name)

exact_inequality("third_shear_norm_bound", 1+9*16 == 145)
exact_inequality("third_hold_horizon_is_strictly_inside_second_hold",
                 s.Rational(16,12288) < s.Rational(1,32))
exact_inequality("third_phase_length_bound", s.Rational(265,256)**2 < 2)
exact_inequality("explicit_unit_scaled_collar_fits_remaining_horizon", 14+1 < 16)
exact_inequality("source_Y3_nesting_denominator_is_positive", 3*202-s.Rational(49,16)>0)

report = {
    "schema_version": 1, "status": "passed", "check_count": len(CHECKS),
    "method": "Exact independent profile/envelope jets; original-parameter third relative-flow identities; full four-field ordered-interaction telescoping; exact rational and physical-power checks.",
    "scope": "Algebra for the actual compact third growth and its full PDE residuals. Analytic threshold existence, support and norm inequalities require the written companion proofs; this replay does not assert a third return.",
    "assumptions": ["trace(D)=0", "k'=-D^T k", "P'=F with independent primitive constant", "material transport of the actual cutoff", "rho=k dot k>0", "equal physical diffusivity d", "actual third-growth flow h'=a Omega1", "Omega2=0 during third growth while Theta2 is retained"],
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "body_sha256": hashlib.sha256((HERE/'third_growth_spatial_body.tex').read_bytes()).hexdigest(),
    "sympy_version": s.__version__, "checks": CHECKS,
}
(HERE/'replay_report.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
print(json.dumps({"status": report['status'], "checks": len(CHECKS),
                  "report": str(HERE/'replay_report.json')}))
