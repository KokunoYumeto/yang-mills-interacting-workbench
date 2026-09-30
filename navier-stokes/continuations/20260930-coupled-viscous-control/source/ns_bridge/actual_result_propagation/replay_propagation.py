"""Exact polynomial replay of the proved maps; not a source-proof verifier."""
from pathlib import Path
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent
x=s.Matrix(s.symbols('x1:4'))
y=s.Matrix(s.symbols('y1:4'))
t,nu_b,rho=s.symbols('t nu_b rho',positive=True)
a=s.Matrix(s.symbols('a1:4'))
u=s.Matrix([y[0]**2+y[1]*t-y[2],-2*y[0]*y[1]+y[2]**2,t*y[0]+y[1]])
p=y[0]*y[1]*y[2]+t*y[0]**2
def lap(v,z):return v.applyfunc(lambda f:sum(s.diff(f,c,2) for c in z))
def curl(v,z):return s.Matrix([s.diff(v[2],z[1])-s.diff(v[1],z[2]),
 s.diff(v[0],z[2])-s.diff(v[2],z[0]),s.diff(v[1],z[0])-s.diff(v[0],z[1])])
def residual(v,pressure,z,visc):
 return v.diff(t)+v.jacobian(z)*v-visc*lap(v,z)+s.Matrix([s.diff(pressure,c) for c in z])
base=residual(u,p,y,nu_b)
checks=[]
def check(name,v):
 values=list(v) if isinstance(v,s.MatrixBase) else [v]
 ok=all(s.expand(s.simplify(z))==0 for z in values)
 checks.append(dict(name=name,passed=ok))
 if not ok:raise AssertionError((name,v))
check('base_polynomial_exactly_divergence_free',s.trace(u.jacobian(y)))
rot=s.Matrix([[s.Rational(3,5),-s.Rational(4,5),0],
              [s.Rational(4,5),s.Rational(3,5),0],[0,0,1]])
for label,O in [('reflection',s.diag(1,-1,1)),('rotation',rot),
                ('rotated_reflection',rot*s.diag(1,-1,1))]:
 coord=O.T*(x-a)/rho
 sub=dict(zip(y,coord))
 ev=lambda z:z.subs(sub,simultaneous=True)
 us=rho*O*ev(u);ps=rho**2*ev(p)
 check(label+'_orthogonal',O.T*O-s.eye(3))
 check(label+'_full_nonlinear_retained_viscosity_residual',
       residual(us,ps,x,rho**2*nu_b)-rho*O*ev(base))
 check(label+'_divergence',s.trace(us.jacobian(x)))
 check(label+'_vorticity_orientation',curl(us,x)-O.det()*O*ev(curl(u,y)))
 inv=dict(zip(x,a+rho*O*y))
 check(label+'_velocity_inverse',O.T*us.subs(inv,simultaneous=True)/rho-u)
 check(label+'_pressure_inverse',ps.subs(inv,simultaneous=True)/rho**2-p)
 check(label+'_absolute_jacobian_squared',s.det(coord.jacobian(x))**2-rho**(-6))
 # Third force derivative retains all three directional contractions.
 dirs=[s.Matrix([1,2,-1]),s.Matrix([3,-2,1]),s.Matrix([-1,1,2])]
 fs=rho*O*ev(base);actual=fs.diff(t);expected=base.diff(t)
 for v in dirs:
  actual=actual.jacobian(x)*v
  expected=expected.jacobian(y)*(O.T*v)
 check(label+'_third_force_derivative',actual-rho**(-2)*O*ev(expected))
check('energy_factor',rho**2*rho**3-rho**5)
check('dissipation_factor',rho**2*nu_b*rho**3-rho**5*nu_b)
Om=s.diag(1,-1,1)
check('reflection_fixes_path_direction',Om*s.Matrix([1,0,0])-s.Matrix([1,0,0]))
check('reflection_reverses_path_observable',Om*s.Matrix([0,1,0])+s.Matrix([0,1,0]))
receipt=dict(schema='exact-propagation-replay-v1',all_passed=all(c['passed'] for c in checks),
 checks=checks,check_count=len(checks),
 scope='Exact polynomial replay supports the written general chain-rule proof. No full-source theorem verification is claimed.',
 sources={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [root/'propagation_body.tex',Path(__file__)]})
(root/'propagation_replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(dict(all_passed=receipt['all_passed'],checks=len(checks))))
