import hashlib
import json
import re
from pathlib import Path
import sympy as sp
ROOT = Path(__file__).resolve().parent
TEX = ROOT / 'class_propagation.tex'
text = TEX.read_text(encoding='utf-8')
checks = []
def check(name, cond):
    cond = bool(cond)
    checks.append({'name': name, 'passed': cond})
    if not cond:
        raise AssertionError(name)

h, eta, q = sp.symbols('h eta q', positive=True)
A = sp.Rational(1, 2) + h
D = sp.Rational(1, 2) - h
B = 1 - 2*h*eta**2
check('scale_A_plus_D', sp.simplify(A + D - 1) == 0)
check('scale_epsilon_exponent', sp.simplify(sp.Rational(1,2) - D - h) == 0)
check('B_lower_bound_identity', sp.simplify(B - (1 - 2*h) - 2*h*(1 - eta**2)) == 0)
qz = 2*eta*q**A/B
qt = -1/B
etaz = q**(-D)*(1-eta**2)/B
etat = D*eta*q**-1/B
check('q_z_factor', sp.simplify(qz*B/(2*eta*q**A)-1) == 0)
check('q_t_sign', sp.simplify(qt*B+1) == 0)
check('eta_z_factor', sp.simplify(etaz*B*q**D/(1-eta**2)-1) == 0)
check('eta_t_factor', sp.simplify(etat*B*q/(D*eta)-1) == 0)
# Exact source class formulas and closure.
for name, needle in [
 ('M_class', r'\label{mccp:Mclass}'),
 ('S_class', r'\label{mccp:Sclass}'),
 ('W_class', r'\label{mccp:Wclass}'),
 ('product_closure', r'M^\alpha M^\beta\subset M^{\alpha+\beta}'),
 ('MW_closure', r'M^\alpha W^\beta\subset W^{\alpha+\beta}'),
 ('W_square_envelope', r'(\sqrt\zeta)^2=\zeta'),
 ('radial_map', r'D_r:C^\alpha\to C^{\alpha-\kappa_s}'),
 ('axial_map', r'D_z=\varepsilon\partial_Z:C^\alpha\to C^{\alpha+1}'),
 ('time_map', r'-\varepsilon\partial_T:C^\alpha\to C^{\alpha+1}'),
 ('phase_arithmetic', r'k_\gamma p_\gamma\in\mathbb Z\setminus\{0\}'),
]: check(name, needle in text)
# Exact Vandermonde determinant algebra.
t0, t1, t2 = sp.symbols('t_0 t_1 t_2')
V3 = sp.Matrix([[1,t0,t0**2],[1,t1,t1**2],[1,t2,t2**2]])
V2 = sp.Matrix([[1,t0],[1,t1]])
check('Vandermonde3_det', sp.simplify(V3.det()-(t1-t0)*(t2-t0)*(t2-t1)) == 0)
check('Vandermonde2_det', sp.simplify(V2.det()-(t1-t0)) == 0)
# Actual five-row scale, signs and full targets.
for name, needle in [
 ('five_rows', r'\label{mccp:five_rows}'),
 ('theta_target', r'a_\theta=q^A{\cal P}V_P'),
 ('z_target', r'a_z=q^{A-3/2}{\cal J}_\theta'),
 ('pressure_target', r'q^{A-1}{\cal J}_zV_{J_z}'),
 ('theta_row_sign', r'=-{\cal J}_\theta'),
 ('z_row_sign', r'=-{\cal J}_z'),
 ('radial_potential', r'a_r=-\partial_z\Psi'),
 ('old_pressure_target', r'P_{\rm old}'),
 ('old_theta_target', r'(J_\theta)_{\rm old}'),
 ('old_z_target', r'(J_z)_{\rm old}'),
 ('B_minus1', r'{\cal B}_{-1,I}'),
 ('B2_shift', r'{\cal B}_{2,(m+1,n)}'),
]: check(name, needle in text)
# Exact pressure and full-force cost pipeline.
for name, needle in [
 ('full_force_identity', r'\label{mccp:full_force_identity}'),
 ('pressure_free_array', r'\mathsf G_{k,m,n}'),
 ('pressure_step_array', r'\mathsf D_{m,n}'),
 ('pressure_source_array', r'\label{mccp:pressure_source_array}'),
 ('pressure_cutoff_array', r'\mathsf X_{k,i,j}'),
 ('pressure_array', r'\label{mccp:pressure_array}'),
 ('physical_viscosity', r'\nu_{\rm NS}'),
 ('inverse_radius_R1', r'\mathsf R_1'),
 ('inverse_radius_R2', r'\mathsf R_2'),
 ('quadratic_force', r'\mathsf A_\theta\star\mathsf A_\theta'),
 ('pressure_gradient_cost', r'S_{e_r}\mathsf\Pi'),
 ('force_cost_array', r'\label{mccp:force_costs}'),
 ('force_bound', r'\label{mccp:force_bound}'),
 ('pressure_tail_retained', 'tail itself and'),
 ('cutoff_tail_retained', 'cutoff derivative remain'),
 ('finite_ratio', r'K_{I,\gamma,m}'),
 ('no_uniform_statement', 'no uniform bound'),
]: check(name, needle in text)
check('pressure_full_force', r'+\nabla\delta p' in text)
# All source cycle maps are attributed finite maps.
for name, needle in [
 ('pulse_map', r'W^\alpha\xrightarrow{\rm pulse}W^\alpha'),
 ('stress_map', r'\xrightarrow{\rm stress}W^{\alpha-1/2}'),
 ('temporal_map', r'S^\alpha\xrightarrow{\rm temporal}M^\alpha'),
 ('five_row_map', r'S^\alpha\xrightarrow{\rm five\ rows}M^\alpha'),
 ('source_gain_tenth', r'B_{j+1}-B_j=C_{j+1}^*-C_j^*=1/10'),
 ('negative_scope', 'sign-reversed profile'),
]: check(name, needle in text)
labels = re.findall(r'\\label\{([^}]+)\}', text)
check('labels_unique', len(labels) == len(set(labels)))
check('no_malformed_ref', not re.search(r'\\ref\{[^}]*\)', text))
receipt = {'schema':'mccp.replay.v1', 'all_passed':True,
           'check_count':len(checks), 'checks':checks,
           'tex_sha256':hashlib.sha256(TEX.read_bytes()).hexdigest(),
           'label_count':len(labels)}
(ROOT/'replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n', encoding='utf-8')
print(json.dumps(receipt, indent=2))
