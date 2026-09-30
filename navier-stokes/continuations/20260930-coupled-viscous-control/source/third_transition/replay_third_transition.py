"""Exact identities and rational margins for the full third transition.

The analytic existence and comparison proofs are in third_transition_body.tex.
No sampled trajectory or inviscid bound is used to infer analytic continuation.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
checks = []
J = s.Matrix([[0, -1], [1, 0]])
a, b, h, g, r, C, c, E1, E2, O1, O2, d, K1, K2 = s.symbols(
    'a b h g r C c E1 E2 Omega1 Omega2 d K1 K2', positive=True)
S, T, alphadot = s.symbols('sin_theta cos_theta alpha_dot', real=True)
D = h*h+a*a
x = (h*g-a*b)/D
y = (a*g+h*b)/D
relation = [r*r-D, T*T+S*S-1]


def reduce_expr(expr):
    num, den = s.fraction(s.cancel(expr))
    num = s.rem(s.Poly(num, r), s.Poly(relation[0], r)).as_expr()
    num = s.rem(s.Poly(num, T), s.Poly(relation[1], T)).as_expr()
    return s.cancel(num/den)


def zero(name, expression, geometric=False):
    entries = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
    residues = [reduce_expr(v) if geometric else s.factor(v) for v in entries]
    ok = all(v == 0 for v in residues)
    checks.append(dict(name=name, passed=ok, residuals=[str(v) for v in residues]))
    if not ok:
        raise AssertionError((name, residues))


def positive(name, expression):
    expression = s.factor(expression)
    ok = expression.is_positive is True
    checks.append(dict(name=name, passed=ok, margin=str(expression)))
    if not ok:
        raise AssertionError((name, expression))


z1 = s.Matrix([(h*S-a*T)/r, (h*T+a*S)/r])
z2 = s.Matrix([r*S, r*T])
z3 = s.Matrix([(g*S+b*T)/r, (g*T-b*S)/r])
zero('first_phase_unit_length', z1.dot(z1)-1, True)
zero('second_phase_length', z2.dot(z2)-D, True)
zero('third_phase_length', z3.dot(z3)-(g*g+b*b)/D, True)
zero('adjacent_determinant_12', s.det(s.Matrix.hstack(z1,z2))+a, True)
zero('adjacent_determinant_23', s.det(s.Matrix.hstack(z2,z3))+b, True)
zero('nonadjacent_determinant_13', s.det(s.Matrix.hstack(z1,z3))+y, True)
zero('inverse_first_basis_zeta2', z2-h*z1+a*J*z1, True)
zero('inverse_first_basis_zeta3', z3-x*z1+y*J*z1, True)
zero('scalar_coordinate_inverse_1', h*y-a*x-b)
zero('scalar_coordinate_inverse_2', h*x+a*y-g)

hp = a*O1
gp = O1*(2*a*h*g+(h*h-a*a)*b)/D+b*O2
xp = O1*y+b*h*O2/D
yp = b*a*O2/D
zero('x_evolution', s.diff(x,h)*hp+s.diff(x,g)*gp-xp)
zero('y_evolution', s.diff(y,h)*hp+s.diff(y,g)*gp-yp)
zero('adjacent_determinant_derivative', hp*y+h*yp-a*xp)
zero('dot_product_evolution', hp*x+h*xp+a*yp-gp)

N2 = a*(E1+c)+C*h
N3 = (E1+c)*y+C*x+b*E2
G2 = -(E1+c)*z1-C*J*z1
G3 = G2-E2*z2
zero('second_gradient_numerator', -(J*z2).dot(G2)-N2, True)
zero('third_gradient_numerator', -(J*z3).dot(G3)-N3, True)
E1p = -C*O1-d*K1*K1*E1
E2p = -N2*O2/D-d*K2*K2*D*E2
zero('second_numerator_derivative', a*E1p+C*hp+a*d*K1*K1*E1)
zero('third_numerator_derivative', E1p*y+(E1+c)*yp+C*xp+b*E2p
     +d*(K1*K1*E1*y+b*K2*K2*D*E2))

F2 = a*O1*(h*S-a*T)/(D*T)
F3 = (O1*y*(h*S-a*T)+b*O2*S)/(g*T-b*S)
F2_source = -O1*z1[0]*(J*z1).dot(z2)/z2[1]
F3_source = -(O1*z1[0]*(J*z1).dot(z3)
              +O2*z2[0]*(J*z2).dot(z3)/D)/z3[1]
zero('feedback_2_source_map', F2_source-F2, True)
zero('feedback_3_source_map', F3_source-F3, True)
factored = b*O1*(h*S-a*T)*(h*T+a*S)/(D*T*(g*T-b*S)) + b*O2*S/(g*T-b*S)
zero('feedback_difference_factorization', F3-F2-factored)
zero('initial_feedback_difference', (F3-F2).subs({S:0,T:1,O2:0})+a*b*h*O1/(D*g))

theta_p = -alphadot-a*a*O1/D
rp = h*hp/r
derivatives = {h:hp,g:gp,r:rp,S:T*theta_p,T:-S*theta_p}
def total(expr):
    return sum(expr.diff(var)*value for var,value in derivatives.items())

D1 = alphadot*J
D2 = D1+O1*(J*z1)*z1.T
D3 = D2+O2*(J*z2)*z2.T/D
zero('phase1_transport', z1.applyfunc(total)+D1.T*z1, True)
zero('phase2_transport', z2.applyfunc(total)+D2.T*z2, True)
zero('phase3_transport', z3.applyfunc(total)+D3.T*z3, True)
zero('second_phase_is_transported_by_third_parent', (D3-D2).T*z2, True)
zero('third_parent_trace', s.trace(D3), True)

P,Q,Rm = s.symbols('matrix_p matrix_q matrix_r')
Mat = s.Matrix([[P,Q],[Rm,-P]])
zero('trace_free_bilinear_identity', J*Mat.T+Mat*J)
v1,v2,G1,G2c,R1,R2 = s.symbols('phase_x phase_y G_x G_y residual_x residual_y')
z = s.Matrix([v1,v2]); G = s.Matrix([G1,G2c]); residual = s.Matrix([R1,R2])
zp = -Mat.T*z; Gp = -Mat.T*G+residual
zero('general_numerator_derivative_sign', -(J*zp).dot(G)-(J*z).dot(Gp)+(J*z).dot(residual))
wj,wjp,Ej,Kj,rj,Z1,Z2 = s.symbols('weight weight_prime E_j K_j r_j zeta_j1 zeta_j2')
zj = s.Matrix([Z1,Z2]); Bj=-wj*Ej*zj
Rj=(-wjp+d*wj*Kj*Kj*rj*rj)*Ej*zj
zero('activation_and_diffusion_determinant_sign', -(J*z).dot(Rj)
     -(wjp-d*wj*Kj*Kj*rj*rj)*Ej*(-s.det(s.Matrix.hstack(zj,z))))
zero('diffusion_Bj_sign', d*Kj*Kj*rj*rj*(J*z).dot(Bj)
     +d*wj*Kj*Kj*rj*rj*Ej*(-s.det(s.Matrix.hstack(zj,z))))

sigma,K3,Gamma,N,Rphase,zz,Ptemp,v,delta3 = s.symbols(
    'sigma2 K3 Gamma3 N3 phase_square phase_first P3 ratio delta3', positive=True)
sins = s.symbols('sin_s3', positive=True)
calK=N/(sigma*sigma*sins*Rphase); calB=zz/sins
Pp=Ptemp*(calK*v-delta3*Rphase)
vp=calB-calK*v*v
theta=-Ptemp; omega=-K3*Ptemp*v/sigma
zero('newest_temperature_inverse', (-Gamma*Pp-N*omega/(K3*Rphase)+Gamma*delta3*Rphase*theta).subs(Gamma,sigma*sins))
zero('newest_vorticity_inverse', (-Gamma*K3*(Pp*v+Ptemp*vp)/sigma-K3*zz*theta+Gamma*delta3*Rphase*omega).subs(Gamma,sigma*sins))

q=s.Rational
A=q(1,512); L=q(16384)
positive('converted_second_temperature_lower', q(2,5)**2/10-q(1,8)**2)
positive('denominator_margin', q(3,4)*q(15,16)-4*A*A/1024-q(2,3))
positive('first_phase_negative_horizontal', q(15,16)-q(13,4)/1024)
positive('first_vorticity_upper_margin', 10-9-6*A/L)
positive('first_temperature_lower_margin', q(1,4)-20*A/(32*L)-q(3,128)-q(1,8))
positive('h_upper_margin', q(13,4)-3-20*A/L)
positive('g_lower_margin_using_sqrt10_less4', q(15,16)-q(4,32)-q(3,4))
positive('g_upper_margin_using_sqrt20_less4_5', 5-q(9,2)-300*A/L)
zero('angular_forcing_arithmetic', 2*4*10*q(7,2)*q(16,15)*q(3,2)-448)
positive('angular_forcing_margin', 512-448)
positive('angular_exponential_margin', q(5,4)-1/(1-q(3,16)))
positive('revival_angle_first_exit_margin', q(1,1024)-640*A/L)
positive('revival_vorticity_first_exit_margin', q(1,32)-7040*A/L)
positive('vorticity_integrand_margin_squared', 11**2-(3*q(16,15))**2*11)
zero('log_length_arithmetic', 140+q(32,5)*7040-45196)
positive('log_length_strict_margin', q(1,128)-46000*A/L)
positive('second_length_log_margin', q(1,64)-22*A/L)
positive('newest_numerator_lower_margin', q(1,5)*(1-q(13,128))-q(1,6))
positive('newest_numerator_upper_margin', q(9,8)-q(16,15)*q(64,63))
positive('newest_buoyancy_lower_margin', q(1,2)*q(63,64)**2-q(15,32))
positive('newest_buoyancy_upper_margin', q(9,8)-1-3840*A/L)
zero('newest_ratio_lower_inward_margin', q(15,32)-q(9,8)*q(1,4)-q(3,16))
zero('newest_ratio_upper_inward_margin', q(9,8)-q(1,6)*9+q(3,8))
zero('full_transition_gain_lower_margin', q(1,6)*q(1,2)-3*q(1,108)-q(1,18))
positive('full_transition_gain_upper_margin', 4-q(9,8)*3)

sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
receipt=dict(schema='third-transition-exact-replay-v1', all_passed=True,
             checks=checks,total_checks=len(checks),
             files_sha256={p.name:sha(p) for p in [HERE/'third_transition_body.tex',Path(__file__)]},
             analytic_claims_proved_in='third_transition_body.tex',
             numerical_trajectory_used=False,lean_used=False,
             third_shooting_return_proved=False,
             infinite_modified_viscous_sequence_proved=False)
(HERE/'replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(all_passed=True,checks=len(checks),receipt='third_transition/replay_receipt.json')))
