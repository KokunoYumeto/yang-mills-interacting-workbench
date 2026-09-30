"""Exact finite algebra and rational-constant replay for the second return.

Run with Python and SymPy. Every physical scale remains an independent
symbol until its displayed source relation is substituted. Polynomial
remainders only impose Y**2=h**2+a**2-a**2*z**2; they do not replace the
written analytic existence, shooting or gain proof with numerical tests.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
checks = []
J = s.Matrix([[0, -1], [1, 0]])
a, h, z, Y, W, B, C0, C1, delta1, delta2 = s.symbols(
    'a h z Y W B C0 C1 delta1 delta2', real=True)
zp = s.symbols('z_prime', real=True)
Dstar = h*h+a*a
relation = Y*Y-Dstar+a*a*z*z

def reduce_exact(expr):
    num, den = s.fraction(s.cancel(expr))
    return s.cancel(s.rem(num, relation, Y)/den)

def zero(name, expr, geometric=False):
    entries = list(expr) if isinstance(expr, s.MatrixBase) else [expr]
    residues = [reduce_exact(v) if geometric else s.trigsimp(s.cancel(v))
                for v in entries]
    ok = all(v == 0 for v in residues)
    checks.append(dict(name=name, passed=ok,
                       residuals=[str(v) for v in residues]))
    if not ok:
        raise AssertionError((name, residues))

def positive(name, expr):
    value = s.cancel(expr)
    ok = bool(value > 0)
    checks.append(dict(name=name, passed=ok, exact_positive_margin=str(value)))
    if not ok:
        raise AssertionError((name, value))

z2 = s.Matrix([a*z,Y])
z1 = s.Matrix([(h*a*z-a*Y)/Dstar, (h*Y+a*a*z)/Dstar])
zero('inverse_first_phase_unit_length', z1.dot(z1)-1, True)
zero('inverse_second_phase_squared_length', z2.dot(z2)-Dstar, True)
zero('inverse_phase_dot_product', z1.dot(z2)-h, True)
zero('inverse_phase_signed_determinant', s.det(s.Matrix.hstack(z1,z2))+a, True)
zero('signed_determinant_representation', z2-h*z1+a*J*z1, True)
zero('source_cone_bracket_square', Y*Y-h*h*z*z-Dstar*(1-z*z), True)

# Inverse material deformation, with the original datum (a,h0).
h0 = s.symbols('h0', positive=True)
Rot = s.Matrix([[z1[1], z1[0]],[-z1[0],z1[1]]])
Shear = s.Matrix([[1,-(h-h0)/a],[0,1]])
M = Rot*Shear
Minverse = Shear.inv()*Rot.T
zero('inverse_rotation_maps_original_parent', Rot*s.Matrix([0,1])-z1, True)
zero('material_matrix_inverse', Minverse*M-s.eye(2), True)
zero('material_matrix_determinant', M.det()-1, True)
zero('original_phase_material_pullback', Minverse.T*s.Matrix([a,h0])-z2, True)

# Exact differential map in source steering time; Gamma=sigma*a.
Yp = (h*W-a*a*z*zp)/Y
def tau_derivative(expr):
    return expr.diff(h)*W+expr.diff(z)*zp+expr.diff(Y)*Yp
alphap = (W*z1[0]-a*zp)/Y
Dscaled = alphap*J+(W/a)*(J*z1)*z1.T
zero('first_phase_angular_equation', z1.applyfunc(tau_derivative)-alphap*J*z1, True)
zero('second_phase_full_parent_equation', z2.applyfunc(tau_derivative)+Dscaled.T*z2, True)
zero('material_deformation_full_parent_equation', M.applyfunc(tau_derivative)-Dscaled*M, True)
zero('source_control_enforces_first_component', (-Dscaled.T*z2)[0]-a*zp, True)
zero('inner_product_derivative',
     (alphap*J*z1).dot(z2)+z1.dot(-Dscaled.T*z2)-W, True)

# All physical factors in the amplitude coordinate transformation.
sigma,K1,K2,d,A0,ss = s.symbols('sigma K1 K2 d A0 s_star', positive=True)
Gamma = sigma*a
Bp = -C1*W-delta1*B
Wp = B*(Y-h*z)/Dstar-delta1*W
n = B+C0+C1*h
k = n/Dstar
zero('coupling_numerator_exact_cancellation', Bp+C1*W+delta1*B)
subs = {C1:A0*s.sin(ss)/(sigma*sigma*a),
        C0:A0*s.cos(ss)/(sigma*sigma),
        delta1:d*K1*K1/Gamma, delta2:d*K2*K2/Gamma}
zero('first_temperature_equation_physical',
     ((-sigma*sigma/K1)*Gamma*Bp -
      (A0*s.sin(ss)/K1*sigma*W-d*K1*K1*(-sigma*sigma*B/K1))).subs(subs))
zero('first_vorticity_equation_physical',
     (sigma*Gamma*Wp -
      (K1*z1[0]*(-sigma*sigma*B/K1)-d*K1*K1*sigma*W)).subs(subs))
zero('second_coefficient_retains_base_and_parent',
     (sigma*sigma*a*n/(K2*Dstar) -
      (a*sigma*sigma*B+A0*(a*s.cos(ss)+h*s.sin(ss)))/(K2*Dstar)).subs(subs))

P,v = s.symbols('P v', real=True)
vp = z-k*v*v
Pp = P*(k*v-delta2*Dstar)
theta = -P
omega = -K2*P*v/sigma
a2 = sigma*sigma*a*k/K2
b2 = K2*a*z
zero('second_temperature_exponential_inverse',
     (Gamma*(-Pp)-(a2*omega-d*K2*K2*Dstar*theta)).subs(subs))
zero('second_vorticity_product_inverse',
     (Gamma*(-K2/sigma)*(Pp*v+P*vp)-
      (b2*theta-d*K2*K2*Dstar*omega)).subs(subs))
zero('common_diffusion_quotient_cancellation',
     (sigma/K2/Gamma)*((b2*theta-d*K2*K2*Dstar*omega)*theta-
      omega*(a2*omega-d*K2*K2*Dstar*theta))/(theta*theta)-vp)
zero('selected_hold_vorticity_stationarity', vp.subs({z:0,v:0}))
zero('selected_hold_geometry_equation',
     (Wp.subs({z:0,Y:s.sqrt(Dstar)})-
      (B/s.sqrt(Dstar)-delta1*W)))
zero('selected_hold_exact_angular_velocity',
     (Gamma*alphap).subs({z:0,zp:0,Y:s.sqrt(Dstar)})+
     a*a*sigma*W/Dstar)
zero('selected_hold_origin_vorticity',
     (2*Gamma*alphap+sigma*W).subs({z:0,zp:0,Y:s.sqrt(Dstar)})-
     sigma*W*(1-2*a*a/Dstar))

# Direct laboratory-coordinate affine scalar and full momentum residuals.
alpha,ad,add,A1,Omega = s.symbols('alpha alpha_dot alpha_ddot A1 Omega1', real=True)
R = s.Matrix([[s.cos(alpha),-s.sin(alpha)],[s.sin(alpha),s.cos(alpha)]])
e2 = s.Matrix([0,1])
e1 = R*s.Matrix([s.sin(ss),s.cos(ss)])
D = ad*J+Omega*(J*e1)*e1.T
Bvec = -A1*e1
G = -A0*R*e2+Bvec
A1dot = -A0*s.sin(ss)*Omega-d*K1*K1*A1
Odot = -A1*e1[0]-d*K1*K1*Omega
Gdot = G.diff(alpha)*ad+G.diff(A1)*A1dot
Ddot = D.diff(alpha)*ad+D.diff(ad)*add+D.diff(Omega)*Odot
zero('affine_parent_gradient_diffusion_identity', Gdot+D.T*G+d*K1*K1*Bvec)
zero('affine_parent_incompressibility', s.trace(D))
zero('affine_tracefree_square', D*D+D.det()*s.eye(2))
curl = D[1,0]-D[0,1]
zero('affine_curl_includes_parent_vorticity', curl-2*ad-Omega)
curl_dot = curl.diff(alpha)*ad+curl.diff(ad)*add+curl.diff(Omega)*Odot
forcecurl = 2*add-A0*s.sin(alpha)-d*K1*K1*Omega
zero('pressure_independent_affine_curl_residual', curl_dot-G[0]-forcecurl)
A = Ddot+D*D-e2*G.T
x1,x2 = s.symbols('x1 x2', real=True)
x = s.Matrix([x1,x2])
pressure = -(x.T*((A+A.T)/2)*x)[0]/2
pressure_gradient = s.Matrix([s.diff(pressure,xi) for xi in x])
zero('full_vector_force_with_exact_pressure', A*x+pressure_gradient-forcecurl*J*x/2)
zero('affine_velocity_physical_laplacian',
     (D*x).applyfunc(lambda f:s.diff(f,x1,2)+s.diff(f,x2,2)))
zero('affine_temperature_physical_laplacian',
     s.diff(G.dot(x),x1,2)+s.diff(G.dot(x),x2,2))

# Exact rational margins appearing in the written continuation argument.
q = s.Rational
zero('bound_total_holding_duration', 1+q(1,64)+q(1,32)-q(67,64))
positive('duration_strictly_below_17_over_16', q(17,16)-q(67,64))
zero('older_vorticity_bound', 2/q(15,16)*(q(17,16)+3)-q(26,3))
positive('older_vorticity_strict_margin', 9-q(26,3))
zero('geometry_upper_bound_arithmetic', 1+q(16,15)+q(13,32)-q(1187,480))
positive('geometry_strict_margin', 3-q(1187,480))
zero('temperature_lower_bound_arithmetic', q(1,2)*(1-q(17,256))-q(3,32)-q(191,512))
positive('temperature_strict_margin', q(191,512)-q(1,4))
positive('coupling_numerator_upper_margin', 3-q(73,32))
zero('first_phase_cone_arithmetic', ((q(15,16)*q(7,8)-q(1,32))/10)-q(101,1280))
positive('first_phase_cone_margin', q(101,1280)-q(1,16))
zero('ramp_riccati_integral_margin', q(1,2)**2/(40*(1+4*q(1,2)))-q(1,480))
positive('trial_riccati_first_exit_margin', 6-3-q(144,64))
positive('zero_pulse_endpoint_margin', 1/(6+q(4,64))-q(1,7))
zero('selected_pulse_lower_bound', q(1,6)*(1-q(12,64))-q(13,96))
zero('selected_parent_vorticity_coefficient', q(1,40)*q(13,96)-q(13,3840))
positive('net_gain_margin_in_units_log3', q(1,160)-10*q(17,16)/6400-q(1,320))
zero('origin_vorticity_lower_bound_factor', 1-2*q(1,64)-q(31,32))

sha = lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
receipt = dict(schema='second-return-exact-replay-v1', all_passed=True,
    checks=checks, total_checks=len(checks),
    files_sha256={p.name:sha(p) for p in [HERE/'second_return_body.tex',Path(__file__)]},
    analytic_claims_proved_in='second_return_body.tex',
    analytic_existence_inferred_from_computation=False,
    numerical_trajectory_used=False, lean_used=False,
    infinite_modified_viscous_sequence_proved=False)
(HERE/'replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(all_passed=True,checks=len(checks),receipt='replay_receipt.json')))
