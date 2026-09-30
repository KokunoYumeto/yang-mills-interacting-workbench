"""Exact quaternionic evolution, source, and energy checks; no PDE certificate."""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
checks = {}
def zero(label, obj):
    entries = list(obj) if isinstance(obj, s.MatrixBase) else [obj]
    checks[label] = all(s.expand(x) == 0 for x in entries)

def bracket(a, b):
    return 2*a.cross(b)

v = [s.Matrix([s.Symbol(f"v{i}_{k}") for k in range(3)]) for i in range(3)]
p = [s.Matrix([s.Symbol(f"p{i}_{k}") for k in range(3)]) for i in range(3)]
force = [sum((bracket(v[i], bracket(v[i],v[j])) for i in range(3)),
             s.zeros(3,1)) for j in range(3)]
gauss_derivative = sum((bracket(v[j],force[j]) for j in range(3)),
                       s.zeros(3,1))
zero("homogeneous_gauss_derivative", gauss_derivative)
potential = sum(bracket(v[i],v[j]).dot(bracket(v[i],v[j]))/2
                for i in range(3) for j in range(i+1,3))
for j in range(3):
    zero(f"force_is_negative_potential_gradient_{j+1}",
         force[j]+s.Matrix([s.diff(potential, z) for z in v[j]]))
energy_derivative = sum(p[j].dot(force[j]) for j in range(3))
energy_derivative += sum(s.diff(potential,v[j][k])*p[j][k]
                         for j in range(3) for k in range(3))
zero("energy_derivative", energy_derivative)

# Polynomial C has mixed spatial derivatives and all three colour directions.
# This fixture tests the differential formula, beyond the constant-core case.
x,y,z,tau,ss = s.symbols("x y z tau ss")
coords = [x,y,z]
c = [s.Matrix([x*y,z,x*x]), s.Matrix([y*y,x*z,x+y]),
     s.Matrix([y*z,x+z,z*z])]
def derivative(a,i): return a.diff(coords[i])
def cov(c,a,i): return derivative(a,i)+bracket(c[i],a)
def curvature(c,i,j):
    return derivative(c[j],i)-derivative(c[i],j)+bracket(c[i],c[j])
f = [[curvature(c,i,j) for j in range(3)] for i in range(3)]
source = [sum((cov(c,f[i][j],i) for i in range(3)),s.zeros(3,1))
          for j in range(3)]
zero("covariant_source_divergence_fixture",
     sum((cov(c,source[i],i) for i in range(3)),s.zeros(3,1)))
b = [[cov(c,source[j],i)-cov(c,source[i],j) for j in range(3)]
     for i in range(3)]
q = [[bracket(source[i],source[j]) for j in range(3)] for i in range(3)]
lin = [sum((cov(c,b[i][j],i)+bracket(source[i],f[i][j])
            for i in range(3)),s.zeros(3,1)) for j in range(3)]
quad = [sum((cov(c,q[i][j],i)+bracket(source[i],b[i][j])
             for i in range(3)),s.zeros(3,1)) for j in range(3)]
cubic = [sum((bracket(source[i],q[i][j]) for i in range(3)),s.zeros(3,1))
         for j in range(3)]
a = [c[i]+tau*source[i] for i in range(3)]
for j in range(3):
    actual = sum((cov(a,curvature(a,i,j),i) for i in range(3)),s.zeros(3,1))
    zero(f"full_spatial_source_polynomial_fixture_{j+1}",
         actual-source[j]-tau*lin[j]-tau**2*quad[j]-tau**3*cubic[j])
zero("exact_Gauss_for_C_plus_tau_S_fixture",
     sum((cov(a,source[i],i) for i in range(3)),s.zeros(3,1)))

f0, f1, f2, m, g = s.symbols("f f_s f_ss m g", nonzero=True)
e = [s.eye(3)[:,j] for j in range(3)]
vh = [f0*a for a in e]
fh = [sum((bracket(vh[i],bracket(vh[i],vh[j])) for i in range(3)),
          s.zeros(3,1)) for j in range(3)]
for j in range(3):
    zero(f"equal_colour_force_{j+1}",fh[j]+8*f0**3*e[j])
zero("core_correction_residual",8-8*(1-4*ss**2)**3
     -(96*ss**2-384*ss**4+512*ss**6))
zero("equal_colour_energy",3*f1**2/2+6*f0**4
     -s.Rational(3,2)*(f1**2+4*f0**4))
zero("fourth_order_coefficient",
     s.diff(1-4*ss**2+8*ss**4,ss,2).series(ss,0,3).removeO()
     +(8*(1-4*ss**2+8*ss**4)**3).series(ss,0,3).removeO())

I=s.I
T=[s.Matrix([[0,-I/2],[-I/2,0]]),
   s.Matrix([[0,-s.Rational(1,2)],[s.Rational(1,2),0]]),
   s.Matrix([[-I/2,0],[0,I/2]])]
electric=sum(-2*s.trace((2*f1*u)**2) for u in T)
magnetic=sum(-2*s.trace((4*f0**2*u)**2) for u in T)
zero("matrix_electric_density_12",electric-12*f1**2)
zero("matrix_magnetic_density_48",magnetic-48*f0**4)
zero("physical_energy_factor", (electric+magnetic)/(2*g*g)
     -6*(f1**2+4*f0**4)/(g*g))
phi0, phi2=s.symbols("Phi Phi_second")
zero("literature_full_scale_dictionary",
     m**3*phi2/2+8*(m*phi0/2)**3-m**3*(phi2+2*phi0**3)/2)
checks["carrier_dimensions"] = (52-3,52-28,28-3)==(49,24,25)
receipt = {
    "schema":"higher-carrier-evolution-exact-check-v1",
    "sympy_version":s.__version__,
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "checks":checks,
    "check_count":len(checks),
    "all_passed":all(checks.values()),
    "scope":"Exact homogeneous polynomial identities, trace factors, and a nonconstant polynomial differential fixture. Global bundle descent and ODE existence are proved in HIGHER_CARRIER_AND_EVOLUTION.md; no infinite-dimensional PDE or quantum reconstruction is certified.",
}
out=ROOT/"checks/HIGHER_CARRIER_EVOLUTION_CHECK.json"
out.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps(receipt,indent=2))
if not receipt["all_passed"]: raise SystemExit(1)
