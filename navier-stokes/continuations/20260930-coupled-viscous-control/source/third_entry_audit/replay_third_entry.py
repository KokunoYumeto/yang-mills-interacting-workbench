"""Independent exact audit of the actual third-growth entry calculation.

The analytic existence/comparison proof is written in audit.md. This replay
derives the phase transport from the physical parent matrix, the coupled
numerator from the full gradient, and exact parameter/constant margins.
It uses no floating point sampling and no Lean.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
LANE = HERE.parent
checks = []


def exact(name, expression):
    residual = sp.factor(sp.cancel(sp.expand(expression)))
    passed = residual == 0
    checks.append(dict(name=name, passed=passed, residual=str(residual)))
    if not passed:
        raise AssertionError((name, residual))


def margin(name, expression):
    residual = sp.simplify(expression)
    passed = residual.is_positive is True
    checks.append(dict(name=name, passed=passed, positive_margin=str(residual)))
    if not passed:
        raise AssertionError((name, residual))


def matrix_exact(name, expression):
    for i in range(expression.rows):
        for j in range(expression.cols):
            exact(f'{name}_{i+1}{j+1}', expression[i, j])


# Source exponents retain all original dimensional factors.
A0, nu, mu, lam1, Q2, Q3, L3, sigma1, sigma2 = sp.symbols(
    'A0 nu_AB mu lambda_hat_1 Q2 Q3 L3 sigma1 sigma2', positive=True)
k3 = sp.symbols('k3', nonnegative=True)
exact('original_seed_to_target_power',
      -(k3+6)+(k3+sp.Rational(41,8))+sp.Rational(7,8))
exact('physical_target_to_gradient_amplitude',
      mu*lam1*(A0/mu)*lam1**(-sp.Rational(7,8))
      - A0*lam1**sp.Rational(1,8))
exact('third_logarithmic_gain_recursion',
      (k3+sp.Rational(41,8))*sp.log((lam1**Q2)**Q3)
      -(k3+sp.Rational(41,8))*Q2*Q3*sp.log(lam1))
margin('source_minimum_Q2_envelope_denominator', 3*202-sp.Rational(49,16))
margin('source_minimum_Q2_angle_denominator', 202-2)
margin('angle_bound_stronger_than_transition_512', sp.Rational(1,512)-sp.Rational(1,12288))
margin('growth_horizon_inside_existing_second_hold', sp.Rational(1,32)-sp.Rational(16,12288))
margin('birth_rotation_vertical_sign_margin',
       sp.Rational(1,4)-sp.Rational(1,8)-sp.Rational(16,15*12288))
margin('sum_of_insertion_angles_branch_margin', sp.Rational(1,8)-sp.Rational(3,12288))
exact('birth_scale_dominance_ratio', 1+sp.Rational(3,12)-sp.Rational(5,4))
exact('birth_scale_relative_lower_ratio', 1/sp.Rational(5,4)-sp.Rational(4,5))
exact('third_angle_ratio_frequency_exponent',
      sp.Rational(2,16)-Q2/16+(Q2-2)/16)
margin('exact_sine_lower_bound_margin_at_one_eighth',
       1-sp.Rational(1,8)**2/6-sp.Rational(15,16))

# Derive phase transport using the original laboratory J and full older D.
a,h,hb,b,g,gb,Om,A1,Cbase,Sbase,P2,K1,K2,K3,d = sp.symbols(
    'a h h_birth b g g_birth Omega1 A1 A0_cos_sstar A0_sin_sstar P2 K1 K2 K3 d',
    positive=True)
D = h*h+a*a
chi = sp.sqrt(D)
chib = sp.sqrt(hb*hb+a*a)
J = sp.Matrix([[0,-1],[1,0]])
z1 = sp.Matrix([-a,h])/chi
z2 = sp.Matrix([0,chi])
c = b*h-a*g
z3 = sp.Matrix([c,h*g+a*b])/chi
R = g*g+b*b
alpha_dot = -a*a*Om/D
Dparent = alpha_dot*J+Om*(J*z1)*z1.T


def material_derivative(expr):
    return expr.diff(h)*(a*Om)+expr.diff(g)*(b*Om)


exact('older_parent_matrix_trace', sp.trace(Dparent))
exact('first_phase_norm', (z1.T*z1)[0]-1)
exact('second_phase_squared_length', (z2.T*z2)[0]-D)
exact('third_phase_squared_length', (z3.T*z3)[0]-R)
exact('adjacent_signed_determinant', sp.det(sp.Matrix.hstack(z2,z3))+c)
exact('first_third_signed_determinant', sp.det(sp.Matrix.hstack(z1,z3))+b)
exact('invariant_adjacent_determinant_derivative', material_derivative(c))
matrix_exact('first_original_phase_equation', material_derivative(z1)-alpha_dot*J*z1)
matrix_exact('second_original_phase_equation', material_derivative(z2)+Dparent.T*z2)
matrix_exact('third_original_phase_equation', material_derivative(z3)+Dparent.T*z3)

# Full material map and its inverse, independent of the scalar phase formula.
Rtheta=sp.Matrix([[h,-a],[a,h]])/chi
Rminus_birth=sp.Matrix([[hb,a],[-a,hb]])/chib
shear=sp.Matrix([[1,-(h-hb)/a],[0,1]])
M=Rtheta*shear*Rminus_birth
Minv=Rminus_birth.T*sp.Matrix([[1,(h-hb)/a],[0,1]])*Rtheta.T
exact('material_map_determinant', sp.det(M)-1)
matrix_exact('material_inverse_left', Minv*M-sp.eye(2))
matrix_exact('material_inverse_right', M*Minv-sp.eye(2))
matrix_exact('material_initial_identity', M.subs(h,hb)-sp.eye(2))
matrix_exact('material_original_ODE', M.diff(h)*(a*Om)-Dparent*M)
ps,pc=sp.symbols('sin_s3 cos_s3',real=True)
b_birth=(hb*ps+a*pc)/chib
g_birth=(hb*pc-a*ps)/chib
g_from_birth=g_birth+b_birth*(h-hb)/a
z3_from_birth=z3.subs({b:b_birth,g:g_from_birth}, simultaneous=True)
matrix_exact('third_original_initial_phase_pullback', M.T*z3_from_birth-sp.Matrix([ps,pc]))
exact('adjacent_birth_determinant', (b_birth*hb-a*g_birth)-chib*ps)

# Obtain the coupling from all older temperature terms, before differentiating.
G=-(A1+Cbase)*z1-Sbase*J*z1-K2*P2*z2
N=b*(A1+Cbase)+g*Sbase+c*K2*P2
exact('full_inherited_gradient_numerator', -(J*z3).dot(G)-N)
Adot=-Sbase*Om-d*K1*K1*A1
Pdot=-d*K2*K2*D*P2
Ndot=material_derivative(N)+sp.diff(N,A1)*Adot+sp.diff(N,P2)*Pdot
Eparent=b*K1*K1*A1+c*K2**3*D*P2
exact('both_parent_losses_and_shear_cancellation',Ndot+d*Eparent)
exact('inviscid_numerator_cancellation',Ndot.subs(d,0))
exact('third_phase_length_rate',material_derivative(R)-2*b*g*Om)
acoeff=N/(K3*R)
bcoeff=K3*c/chi
adot=material_derivative(acoeff)+sp.diff(acoeff,A1)*Adot+sp.diff(acoeff,P2)*Pdot
exact('temperature_coefficient_logarithmic_rate',
      adot/acoeff+d*Eparent/N+2*b*g*Om/R)
exact('vorticity_coefficient_logarithmic_rate',
      material_derivative(bcoeff)/bcoeff+a*h*Om/D)
F2=-a*a*Om/D
F3=-a*b*Om/(h*g+a*b)
exact('feedback_difference_sign_and_factors',F3-F2+a*c*h*Om/(D*(h*g+a*b)))

# Exact coefficient interval certificates and quotient map.
Ni,Nactual,Ractual,ai,bi,Arel,Brel,u = sp.symbols(
    'Ni Nactual Ractual ai bi Arelative Brelative u',positive=True)
exact('lower_temperature_coefficient_certificate',
      Nactual/(K3*Ractual)-Ni/(4*K3)
      -(2*Nactual-Ni)/(2*K3*Ractual)-Ni*(2-Ractual)/(4*K3*Ractual))
exact('upper_temperature_coefficient_certificate',
      Ni/K3-Nactual/(K3*Ractual)
      -(Ni-Nactual)/K3-Nactual*(Ractual-1)/(K3*Ractual))
exact('riccati_lower_barrier_certificate',
      bi*Brel-ai*Arel*(bi/ai)/2
      -bi*((Brel-sp.Rational(1,2))+(1-Arel)/2))
exact('riccati_upper_barrier_certificate',
      -(bi*Brel-ai*Arel*4*(bi/ai))
      -bi*((1-Brel)+4*(Arel-sp.Rational(1,4))))
r=sp.symbols('r',real=True)
aa=sp.Function('a3')(r)
bb=sp.Function('b3')(r)
lam=sp.Function('lambda3')(r)
X=sp.Function('X')(r)
Y=sp.Function('Y')(r)
integrating=sp.Function('E')(r)
Theta=-X/integrating
Omega=-Y/integrating
sub={sp.diff(X,r):aa*Y,sp.diff(Y,r):bb*X,sp.diff(integrating,r):lam*integrating}
exact('cooperative_temperature_map',(sp.diff(Theta,r)-aa*Omega+lam*Theta).subs(sub))
exact('cooperative_vorticity_map',(sp.diff(Omega,r)-bb*Theta+lam*Omega).subs(sub))
exact('ratio_ODE_with_changing_equal_damping',
      sp.diff(Y/X,r).subs(sub)-(bb-aa*(Y/X)**2))
exact('actual_temperature_logarithmic_rate',
      (sp.diff(Theta,r)/Theta).subs(sub)-(aa*Y/X-lam))
sin3=sp.symbols('sin_s3',positive=True)
ni=Ni/(sigma2**2*sin3)
exact('initial_ratio_original_physical_normalization',
      sigma2**2/K3**2*(K3*sin3)/(Ni/K3)-1/ni)
exact('normalized_riccati_original_gravity_coefficient',
      sigma2/(K3*(sigma2*sin3))*K3*chib*sin3/chi-chib/chi)
exact('normalized_riccati_temperature_coefficient',
      (N/(K3*R))*K3/(sigma2*(sigma2*sin3))-N/(sigma2**2*sin3*R))

# Closed algebraic margins controlling the horizon and exact threshold.
exact('phase_length_rational_constant', 1+sp.Rational(432,12288)-sp.Rational(265,256))
exact('parent_phase_length_rational_constant', 1+sp.Rational(144,12288)-sp.Rational(259,256))
margin('new_phase_length_squared_below_two',2-sp.Rational(265,256)**2)
margin('parent_phase_length_ratio_below_two',2-sp.Rational(259,256))
exact('parent_numerator_half_loss_exponent',10*(sigma1*sp.log(2)/(160*K2**2))*K2**2*(16/sigma1)-sp.log(2))
exact('initial_ni_upper_margin_constant',1+sp.Rational(64,15*64)-sp.Rational(16,15))
margin('initial_rate_lower_square_margin',sp.Rational(4,5)-sp.Rational(7,8)**2)
exact('physical_rate_lower_constant',sp.Rational(7,8)*sp.Rational(15,16)-sp.Rational(105,128))
exact('normalized_ratio_lower_squared',1/(2*sp.Rational(16,15))-sp.Rational(15,32))
exact('normalized_ratio_upper_squared',4/sp.Rational(4,5)-5)
margin('normalized_ratio_upper_below_three',9-5)
margin('temperature_rate_upper_below_three_gamma_squared',9-4*sp.Rational(16,15))
margin('diffusion_to_growth_margin_using_weaker_64_bound',
       sp.Rational(105,128)/(16*sp.sqrt(2))-sp.Rational(1,64))
exact('physical_lower_logarithmic_gain_constant',1/(4*sp.sqrt(2))-2/(16*sp.sqrt(2))-1/(8*sp.sqrt(2)))
exact('threshold_time_upper_constant',8*sp.sqrt(2)/sp.Rational(105,128)-1024*sp.sqrt(2)/105)
margin('threshold_before_fourteen_over_sigma1',14-1024*sp.sqrt(2)/105)
margin('activation_complete_before_actual_crossing',sp.Rational(64,3)-1)
exact('tighter_d3_implies_transition_delta3_bound',
      (L3*sigma1/(128*K3**2))*K3**2/(sp.Rational(15,16)*L3*sigma1)-sp.Rational(1,120))
exact('parent_loss_d3_implies_transition_delta2_bound',
      (sigma1*sp.log(2)/(160*K2**2))*K2**2/(sp.Rational(15,16)*L3*sigma1)-sp.log(2)/(150*L3))
margin('delta3_transition_margin',sp.Rational(1,108)-sp.Rational(1,120))
margin('delta2_transition_margin_using_L3_one',sp.Rational(1,128)-sp.log(2)/150)

# Both exact support conditions, including every mu factor.
exact('third_envelope_nesting_frequency_exponent',
      sp.Rational(1,16)-3*Q2+3+(3*Q2-sp.Rational(49,16)))
exact('third_profile_nesting_frequency_exponent',-2*Q2+2*Q2)
exact('third_envelope_physical_mu_cancellation',
      (lam1**(-3*Q2)/mu)/(lam1**-3/mu)-lam1**(3-3*Q2))
exact('third_profile_physical_mu_cancellation',
      (mu*lam1**Q2)*(lam1**(-3*Q2)/mu)-lam1**(-2*Q2))
exact('growth_material_deformation_bound',1+sp.Integer(144)-145)

# Newly added explicit full-transition nesting constants. The third-transition
# spatial proof establishes its matrix bounds; these are the independent
# source-parameter consequences of the already proved birth amplitude bound.
C2=sp.exp(9)*sp.sqrt(5*sp.sqrt(10)/4)
CM=256*C2/(15*sp.sqrt(sp.E))
exact('birth_scale_C2_square_from_original_amplitude_bound',
      C2**2-sp.Rational(5,4)*sp.sqrt(10)*sp.exp(18))
exact('transition_material_CM_from_exact_sine_lower_bound',
      16*sp.Rational(16,15)*C2/sp.sqrt(sp.E)-CM)
margin('transition_material_frobenius_constant_margin_squared',16**2-14*11)
exact('transition_envelope_source_exponent',
      (Q2-1)/16+sp.Rational(1,16)-3*Q2+3+(47*Q2/16-3))
exact('transition_profile_source_exponent',
      (Q2-1)/16-2*Q2+(31*Q2+1)/16)
margin('transition_envelope_Y3_denominator_positive',sp.Rational(47*202,16)-3)
margin('transition_profile_Y3_denominator_positive',sp.Rational(31*202+1,16))
exact('transition_envelope_constant_includes_both_factors_two',2*2-4)

source_names = ['finite_stage/third_growth_entry.tex',
                'finite_stage/actual_viscous_entry.tex',
                'second_return/second_return_body.tex',
                'modified_spatial/modified_spatial_body.tex',
                'sources/alpoge_buckmaster_boussinesq.pdf']
receipt = dict(schema='third-growth-entry-independent-audit-v1',
               all_passed=True,count=len(checks),checks=checks,
               scope='Exact phase/material transport, full inherited-gradient coupling, changing damping/ratio maps, frequency powers and closed constant margins. The analytic construction is independently audited in audit.md.',
               no_numerical_sampling=True,no_lean=True,
               files_sha256={name:hashlib.sha256((LANE/name).read_bytes()).hexdigest()
                             for name in source_names})
(HERE/'replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(all_passed=True,count=len(checks),receipt='third_entry_audit/replay_receipt.json')))
