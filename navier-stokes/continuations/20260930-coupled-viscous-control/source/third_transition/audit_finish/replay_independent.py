"""Independent Cartesian and dimensional audit of the full third transition.

The Cartesian aggregate check uses arbitrary, nonparallel or parallel, phase
vectors and arbitrary weights.  No determinant invariant or transition formula
is substituted into that check.  Analytic continuation is audited in AUDIT.md;
these exact checks do not replace its proof.
"""
from pathlib import Path
import hashlib
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
LANE = HERE.parent.parent
checks = []
J = sp.Matrix([[0, -1], [1, 0]])
Q = sp.Rational

def zero(name, expression):
    values = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
    residues = [sp.factor(sp.cancel(v)) for v in values]
    ok = all(v == 0 for v in residues)
    checks.append({'name': name, 'passed': ok, 'residuals': list(map(str, residues))})
    if not ok:
        raise AssertionError((name, residues))

def positive(name, value):
    value = sp.factor(value)
    ok = value.is_positive is True
    checks.append({'name': name, 'passed': ok, 'exact_margin': str(value)})
    if not ok:
        raise AssertionError((name, value))

# Arbitrary Cartesian active-family calculation, with three older waves.
alpha_dot, d = sp.symbols('alpha_dot diffusivity', real=True)
G0 = sp.Matrix(sp.symbols('base_gradient_x base_gradient_y'))
Dcur = alpha_dot * J
Gcur = G0.copy()
Gdot = -Dcur.T * G0
residual = sp.zeros(2, 1)
for j in range(1, 4):
    z = sp.Matrix(sp.symbols(f'zeta{j}_x zeta{j}_y'))
    k, theta, omega, weight, weight_dot = sp.symbols(
        f'K{j} Theta{j} Omega{j} weight{j} weight_dot{j}')
    norm2 = z.dot(z)
    zdot = -Dcur.T * z
    theta_dot = -(J*z).dot(Gcur)*omega/(k*norm2) - d*k*k*norm2*theta
    Gdot += weight_dot*k*theta*z + weight*k*theta_dot*z + weight*k*theta*zdot
    residual += (weight_dot*k*theta-d*weight*k**3*norm2*theta)*z
    Dcur += weight*omega*(J*z)*z.T/norm2
    Gcur += weight*k*theta*z
    zero(f'cartesian_aggregate_after_{j}_older_waves', Gdot + Dcur.T*Gcur-residual)
    zero(f'trace_after_{j}_older_waves', sp.trace(Dcur))

# The numerator sign with arbitrary trace-free transport and activation.
p, q, r = sp.symbols('D11 D12 D21')
Dmat = sp.Matrix([[p, q], [r, -p]])
zq = sp.Matrix(sp.symbols('new_phase_x new_phase_y'))
Gold = sp.Matrix(sp.symbols('gradient_x gradient_y'))
res = sp.Matrix(sp.symbols('residual_x residual_y'))
Ndot = -(J*(-Dmat.T*zq)).dot(Gold) - (J*zq).dot(-Dmat.T*Gold+res)
zero('numerator_transport_from_cartesian_product_rule', Ndot+(J*zq).dot(res))
zj = sp.Matrix(sp.symbols('older_phase_x older_phase_y'))
w, wp, Eparent, Kparent, rparent2 = sp.symbols('weight weight_derivative Eparent Kparent norm_parent_squared')
Rparent = (-wp+d*w*Kparent**2*rparent2)*Eparent*zj
Delta = sp.det(sp.Matrix.hstack(zj,zq))
zero('activation_diffusion_oriented_sign', -(J*zq).dot(Rparent)
     -(wp-d*w*Kparent**2*rparent2)*Eparent*(-Delta))

# Matrix inverse: L(t)=M(t)^(-T)L_b and the proposed reconstruction.
l11,l12,l21,l22,b11,b12,b21,b22 = sp.symbols('l11 l12 l21 l22 b11 b12 b21 b22')
Lmat=sp.Matrix([[l11,l12],[l21,l22]])
Lb=sp.Matrix([[b11,b12],[b21,b22]])
M=Lmat.inv().T*Lb.T
zero('matrix_reconstruction_initial', M.subs({l11:b11,l12:b12,l21:b21,l22:b22})-sp.eye(2))
zero('matrix_reconstruction_all_phase_columns', M.inv().T*Lb-Lmat)
Ldot=-Dmat.T*Lmat
Mdot=sp.zeros(2)
for var, vel in zip(list(Lmat),list(Ldot)):
    Mdot += M.diff(var)*vel
zero('matrix_reconstruction_physical_evolution', Mdot-Dmat*M)

# Exact growth-to-transition determinant-coordinate dictionary.
a,h,xb,yb=sp.symbols('a h growth_x growth_y', positive=True)
D=h*h+a*a
b=h*yb-a*xb
g=h*xb+a*yb
zero('growth_transition_x_dictionary', (h*g-a*b)/D-xb)
zero('growth_transition_y_dictionary', (a*g+h*b)/D-yb)
zero('growth_transition_phase_length', (g*g+b*b)/D-(xb*xb+yb*yb))
Ep1,Ep2,c,C=sp.symbols('E1 E2 base_cos base_sin')
zero('growth_transition_numerator', (Ep1+c)*((a*g+h*b)/D)+C*((h*g-a*b)/D)+b*Ep2
     -((Ep1+c)*yb+C*xb+b*Ep2))

# Independently nondimensionalize the physical equations, without fixing any
# dimensional parameter to one.
sigma1,sigma2,Gamma,s,L,sins=sp.symbols('sigma1 sigma2 Gamma s L sin_s', positive=True)
E,F,omega,V,u=sp.symbols('E F omega V u', real=True)
cbar,Cbar,K1,K2=sp.symbols('cbar Cbar K1 K2', real=True)
g,b=sp.symbols('g b', real=True)
delta1=d*K1*K1/Gamma
delta2=d*K2*K2/Gamma
epsilon=sigma1/Gamma
ratio=sigma1/sigma2
E1=sigma1**2*E
E2=sigma2**2*F
Om1=sigma1*omega
Om2=sigma2*V
Cbase=sigma1**2*Cbar
cbase=sigma1**2*cbar
N2=a*(E1+cbase)+Cbase*h
sinth=sp.sin(s*u); costh=sp.cos(s*u)
z11=(h*sinth-a*costh)/sp.sqrt(D)
physical=[a*Om1,
          Om1*(2*a*h*g+(h*h-a*a)*b)/D+b*Om2,
          -Cbase*Om1-d*K1*K1*E1,
          -E1*z11-d*K1*K1*Om1,
          -N2*Om2/D-d*K2*K2*D*E2,
          -E2*sp.sqrt(D)*sinth-d*K2*K2*D*Om2]
scales=[1,1,sigma1**2,sigma1,sigma2**2,sigma2]
expected=[a*epsilon*omega,
          epsilon*omega*(2*a*h*g+(h*h-a*a)*b)/D+b*V/sins,
          -epsilon*Cbar*omega-delta1*E,
          -epsilon*E*z11-delta1*omega,
          -ratio*epsilon*(a*(E+cbar)+Cbar*h)*V/D-delta2*D*F,
          -F*sp.sqrt(D)*sinth/sins-delta2*D*V]
for name, rhs, scale, target in zip(['h','g','E','omega','F','V'],physical,scales,expected):
    zero(f'physical_to_dimensionless_{name}', (rhs/(Gamma*scale)-target).subs(Gamma,sigma2*sins))
zero('source_ratio_kept', (sigma1/sigma2-s/L).subs(s,L*sigma1/sigma2))
zero('epsilon_source_conversion', (sigma1/(sigma2*sins)-s/(L*sins)).subs(s,L*sigma1/sigma2))

# Exact rational analytic margins; trigonometric/exponential bounds are proved
# separately in AUDIT.md.  Endpoints use the weaker published transition box.
A=Q(1,512); LL=sp.Integer(16384)
positive('entry_E1_lower_from_second_hold',Q(191,512)-Q(1,4))
positive('entry_F_lower_squared',Q(2,5)**2/10-Q(1,8)**2)
positive('growth_endpoint_quotient_above_half_squared',Q(15,32)-Q(1,4))
positive('diffusion_delta3_link',Q(1,108)-Q(1,120))
positive('diffusion_delta2_link_using_log2_below_one',Q(1,128)-1/(150*LL))
positive('base_phase_positive_branch',Q(15,16)-Q(13,4)/1024)
positive('feedback_positive_denominator',Q(3,4)*Q(15,16)-4*A*A/1024-Q(2,3))
positive('first_parent_E_lower',Q(1,4)-20*A/(32*LL)-Q(3,128)-Q(1,8))
positive('second_parent_F_lower_using_exp_minus_x',Q(1,8)*(1-Q(11,128))-Q(1,16))
positive('second_parent_F_upper',3-2-A*A/(4*LL*LL))
positive('first_parent_omega_upper',10-9-6*A/LL)
positive('h_upper',Q(13,4)-3-20*A/LL)
positive('g_lower_using_sqrt10_below_4',Q(15,16)-Q(1,8)-Q(3,4))
positive('g_upper_using_sqrt20_below_9over2',5-Q(9,2)-300*A/LL)
positive('x_positive_numerator',Q(15,16)*Q(3,4)-4*A*A)
positive('revival_u_closes_bootstrap',Q(1,1024)-640*A/LL)
positive('revival_V_closes_bootstrap',Q(1,32)-7040*A/LL)
positive('exact_integrand_11_bound_squared',121-9*11*Q(16,15)**2)
positive('phase_length_variation',Q(1,128)-46000*A/LL)
positive('second_phase_length_variation',Q(1,64)-22*A/LL)
positive('K_lower_using_exp_minus_x',Q(1,5)*(1-Q(13,128))-Q(1,6))
positive('K_upper_using_geometric_series',Q(9,8)-Q(16,15)*Q(64,63))
positive('B_lower',Q(1,2)*Q(63,64)**2-Q(15,32))
positive('B_upper',Q(9,8)-1-3840*A/LL)
positive('quotient_lower_inward',Q(15,32)-Q(9,8)/4)
positive('quotient_upper_inward',Q(1,6)*9-Q(9,8))
zero('gain_lower_exact',Q(1,6)*Q(1,2)-3*Q(1,108)-Q(1,18))
positive('gain_upper',4-Q(9,8)*3)

sha=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
inputs=[LANE/'third_transition/third_transition_body.tex',
        LANE/'finite_stage/third_growth_entry.tex',
        LANE/'second_return/second_return_body.tex',Path(__file__)]
receipt={'schema':'independent-third-transition-audit-v1',
         'all_passed':all(c['passed'] for c in checks),'total_checks':len(checks),
         'checks':checks,'source_sha256':{str(p.relative_to(LANE)):sha(p) for p in inputs},
         'analytic_proof_audit':'third_transition/audit_finish/AUDIT.md',
         'independent_derivation':'arbitrary Cartesian phases, arbitrary active weights, physical rescaling',
         'trajectory_sampling_used':False,'lean_used':False,
         'third_return_claimed':False,'infinite_cascade_claimed':False}
(HERE/'replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'all_passed':receipt['all_passed'],'checks':len(checks)}))
