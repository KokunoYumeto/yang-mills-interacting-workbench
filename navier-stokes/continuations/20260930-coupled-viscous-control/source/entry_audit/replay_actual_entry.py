"""Independent exact algebra and rational-margin audit of actual_viscous_entry.tex.

No floating point or parameter sampling is used. The analytic comparisons,
continuation arguments and frequency proof are audited in AUDIT.md; these
checks verify their algebraic transformations and numerical margins.
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
    residual = sp.cancel(sp.trigsimp(sp.expand(expression)))
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


A0, nu, mu, lam1, lam2, K1, K2, L1, L, Gamma1, Gamma, sigma = sp.symbols(
    'A0 nu_AB mu lambda_hat_1 lambda_hat_2 K1 K2 L1 L2 Gamma1 Gamma2 sigma',
    positive=True)
d, q, r, S1, Pstar, Lam1 = sp.symbols('d q r S1 Pstar Lambda1', positive=True)
k1, k2, Q2 = sp.symbols('k1 k2 Q2', nonnegative=True)
sstar, s = sp.symbols('s_star s2', real=True)
a = sp.sin(s)
Ad = sp.symbols('A_d', positive=True)

# The original physical seed and target, with the exact derivative-order cost.
exact('seed_to_original_target_exponent', -(k1 + 6) + (k1 + sp.Rational(41,8)) + sp.Rational(7,8))
exact('physical_target_to_parent_gain_power', 1 - sp.Rational(7,8) - sp.Rational(1,8))
exact('source_second_logarithmic_gain', (k2 + sp.Rational(41,8))*Q2*sp.log(lam1)
      - (k2 + sp.Rational(41,8))*sp.log(lam1**Q2))

# The actual first threshold is not the old inviscid threshold time.
theta = -S1 * sp.exp((Gamma1-q)*r)
omega = K1/nu*theta
a1 = nu**2*sp.sin(sstar)/K1
b1 = K1*sp.sin(sstar)
exact('first_damped_temperature_equation',
      (sp.diff(theta,r) - a1*omega + q*theta).subs(Gamma1,nu*sp.sin(sstar)))
exact('first_damped_vorticity_equation',
      (sp.diff(omega,r) - b1*theta + q*omega).subs(Gamma1,nu*sp.sin(sstar)))
exact('first_actual_threshold_log_gain', (Gamma1-q)*(L1/(Gamma1-q))-L1)
exact('first_growth_gain_minus_diffusion', Gamma1*L1/(Gamma1-q)-q*L1/(Gamma1-q)-L1)
exact('first_post_threshold_diffusion_duration',
      q/Gamma1 + q*(1+1/Lam1)/Gamma1 - q*(2+1/Lam1)/Gamma1)
T = sp.Function('Theta_E')(r)
O = sp.Function('Omega_E')(r)
aa, bb = sp.symbols('a1 b1', real=True)
Td = sp.exp(-q*r)*T
Od = sp.exp(-q*r)*O
exact('translated_first_steering_temperature_map',
      (sp.diff(Td,r)-aa*Od+q*Td).subs(sp.diff(T,r),aa*O))
exact('translated_first_steering_vorticity_map',
      (sp.diff(Od,r)-bb*Td+q*Od).subs(sp.diff(O,r),bb*T))
exact('translated_first_steering_inverse_temperature',
      sp.diff(sp.exp(q*r)*Td,r)-sp.diff(T,r))

# Retain the base contribution in the changing inherited gradient.
Gx = A0*sp.sin(sstar)
Gy = -A0*sp.cos(sstar)-Ad
exact('inherited_gradient_norm_squared', Gx**2+Gy**2
      -(A0**2+Ad**2+2*A0*Ad*sp.cos(sstar)))
exact('inherited_parallel_perpendicular_decomposition',
      A0**2+Ad**2+2*A0*Ad*sp.cos(sstar)
      -((Ad+A0*sp.cos(sstar))**2+(A0*sp.sin(sstar))**2))
ai = (Ad*a + A0*sp.sin(sstar+s))/K2
b2 = K2*a
C0 = A0*sp.cos(sstar)/sigma**2
C1 = A0*sp.sin(sstar)/(sigma**2*a)
ni = Ad/sigma**2 + C0 + C1*sp.cos(s)
exact('actual_second_initial_rate_ratio', ai*b2/(sigma*a)**2-ni)
exact('second_normalized_initial_ratio_squared',
      (sigma/K2)**2*(b2/ai)-1/ni)

# The evolving coefficient is exponential in physical time, rather than frozen.
ar = (Ad*sp.exp(-q*r)*a+A0*sp.sin(sstar+s))/K2
exact('evolving_parent_second_coefficient_derivative', sp.diff(ar,r)
      +q*Ad*sp.exp(-q*r)*a/K2)
X = sp.Function('X')(r)
Y = sp.Function('Y')(r)
dphys = d*K2**2
th = -sp.exp(-dphys*r)*X
om = -sp.exp(-dphys*r)*Y
exact('second_cooperative_temperature_map',
      (sp.diff(th,r)-ar*om+dphys*th).subs(sp.diff(X,r),ar*Y))
exact('second_cooperative_vorticity_map',
      (sp.diff(om,r)-b2*th+dphys*om).subs(sp.diff(Y,r),b2*X))
exact('second_ratio_riccati_equation',
      sp.diff(Y/X,r).subs({sp.diff(Y,r):b2*X,sp.diff(X,r):ar*Y})
      -(b2-ar*(Y/X)**2))
exact('second_actual_temperature_log_derivative',
      (sp.diff(th,r)/th).subs(sp.diff(X,r),ar*Y)-(ar*Y/X-dphys))

# Explicit Y0 and nesting exponents: every original physical mu cancels only
# through the displayed dimensional maps.
H, CL, y, CN, Csig = sp.symbols('H C_L y C_N C_sigma', positive=True)
exact('Y0_cubic_series_constant',
      (72*16**3*H*CL**2/sp.sqrt(sp.E))/(6*16**3)
      -12*H*CL**2/sp.sqrt(sp.E))
exact('second_shear_constant_at_L64', 6*Csig/64 - 3*Csig/32)
exact('envelope_nesting_exponent', sp.Rational(1,16)-3+sp.Rational(47,16))
exact('profile_nesting_exponent', sp.Rational(1,16)-2+sp.Rational(31,16))
exact('physical_first_profile_nesting_mu', mu*lam1*(lam1**-3/mu)-lam1**-2)
exact('physical_envelope_nesting_mu', (lam1**-3/mu)/(1/mu)-lam1**-3)

# Rational and algebraic margins used by the analytic proof.
margin('ni_lower_implies_v_above_half', 2-sp.Rational(33,32))
margin('ni_lower_implies_v_below_two_squared', 4-2/sp.Rational(4,5))
margin('growth_diffusion_lower_scale_margin', 1/(8*sp.sqrt(2))-sp.Rational(1,16))
margin('growth_plus_transition_inside_horizon', 16-8*sp.sqrt(2)-sp.Rational(1,32))
margin('Bentry_above_half', sp.Rational(4,5)*sp.Rational(2,3)-sp.Rational(1,2))
exact('Bentry_stated_lower_bound', sp.Rational(4,5)*sp.Rational(2,3)-sp.Rational(8,15))
exact('dmax_to_delta2_factor', (L*nu*sp.log(3)/(12800*K2**2))*K2**2/(L*nu/2)
      -sp.log(3)/6400)
margin('delta2_below_delta1_allowed_ceiling', sp.Rational(1,16)-sp.log(3)/6400)
margin('selected_gain_after_entire_hold', sp.log(3)/160
      -10*(sp.log(3)/6400)*(1+sp.Rational(1,64)+sp.Rational(1,32))
      -sp.log(3)/320)
margin('second_amplitude_exponent_eighteen', 18-4-12*(1+sp.Rational(1,64)))
exact('range_limit_exponential_series_bound',
      y/((2*Q2*y)**2/2)-1/(2*Q2**2*y))

# Original datum constraint: mu=ceil(nu/2), nu=sqrt(A0)>=1.
# For 1<=nu<=2, mu=1; for nu>2, mu>=nu/2. These elementary
# ceiling facts are proved in the source and audited in AUDIT.md.
exact('original_scaling_first_branch_margin',
      1/nu-sp.Rational(1,2)-(2-nu)/(2*nu))
nu_excess = sp.symbols('nu_minus_two', positive=True)
margin('original_scaling_second_branch_strict_margin',
       (2+nu_excess)/4-sp.Rational(1,2))
exact('original_scaling_equality_case', sp.ceiling(sp.Integer(2)/2)**2/sp.Integer(2)-sp.Rational(1,2))
exact('transformed_diffusion_exact_coefficient', d*(mu*lam1)**2/nu-(d*mu**2/nu)*lam1**2)
exact('necessary_first_growth_in_source_time',
      (nu*sp.sin(sstar)-d*(mu*lam1)**2)/nu
      -(sp.sin(sstar)-(d*mu**2/nu)*lam1**2))
exact('necessary_first_growth_equality_case',
      (d*mu**2/nu).subs({mu:1,nu:2})-d/2)

source_names = ['finite_stage/actual_viscous_entry.tex',
                'second_return/second_return_body.tex',
                'finite_stage/first_stage_section.tex',
                'finite_stage/evolving_diffusive_parent_section.tex',
                'sources/alpoge_buckmaster_boussinesq.pdf']
receipt = dict(schema='actual-viscous-entry-independent-audit-v1',
               all_passed=True, count=len(checks), checks=checks,
               scope='Exact entry transformations and constant margins; analytic proof independently audited in AUDIT.md.',
               no_numerical_sampling=True, no_lean=True,
               files_sha256={rel:hashlib.sha256((LANE/rel).read_bytes()).hexdigest()
                             for rel in source_names})
(HERE/'replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(all_passed=True,count=len(checks),receipt='entry_audit/replay_receipt.json')))
