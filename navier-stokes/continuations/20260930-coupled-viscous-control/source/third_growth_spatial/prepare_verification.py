"""Prepare a standalone replay and an in-lane cumulative verification reader.

All writes stay beside this file; the earlier proof and replay are read-only.
The generated replay is self-contained and does not invoke earlier scripts.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
LANE = HERE.parent
earlier = (LANE / 'modified_spatial/replay_spatial.py').read_text(encoding='utf-8')
generic = earlier.split('\nreport = {"schema_version"', 1)[0]
generic = generic.replace('"""Exact spatial-jet replay of the modified, damped compact profiles.',
                          '"""Exact third-growth spatial replay, retaining independent profile jets.')
additional = r'''

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
'''
(HERE / 'replay_third_spatial.py').write_text(generic + additional, encoding='utf-8')
master = (LANE / 'coupled_viscous_control.tex').read_text(encoding='utf-8')
preamble = master.split('\\begin{document}', 1)[0]
components = [
    'physical_realization.tex', 'finite_stage/first_stage_section.tex',
    'finite_stage/evolving_diffusive_parent_section.tex',
    'finite_stage/actual_viscous_entry.tex', 'second_return/second_return_body.tex',
    'modified_spatial/modified_spatial_body.tex', 'coupled_feedback.tex',
    'infinite_status.tex', 'paper_coupling/coupled_background_body.tex',
    'paper_coupling/profile_diffusion/profile_diffusion_body.tex',
    'finite_stage/third_growth_entry.tex',
    'third_growth_spatial/third_growth_spatial_body.tex',
]
reader = preamble + '\\begin{document}\n'
reader += '\n'.join('\\input{' + name + '}' for name in components)
reader += '\n\\end{document}\n'
(HERE/'audit/preview_build').mkdir(exist_ok=True)
(HERE/'audit/preview.tex').write_text(reader, encoding='utf-8')
print('Prepared self-contained replay and cumulative verification reader inside the owned directory.')
