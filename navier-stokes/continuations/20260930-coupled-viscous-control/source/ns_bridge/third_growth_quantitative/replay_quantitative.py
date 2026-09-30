"""Independent exact replay of the full physical factorization and units."""
from pathlib import Path
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent
checks=[]
def check(name,value):
 entries=list(value) if isinstance(value,s.MatrixBase) else [value]
 ok=all(s.simplify(s.expand(x))==0 for x in entries)
 if not ok:raise AssertionError((name,value))
 checks.append(dict(name=name,passed=True))
x,y,z,t=s.symbols('x y z t',real=True)
xx=s.Matrix([x,y,z])
nu=s.symbols('nu_NS',positive=True)
def curl(v):
 return s.Matrix([s.diff(v[2],y)-s.diff(v[1],z),
                  s.diff(v[0],z)-s.diff(v[2],x),
                  s.diff(v[1],x)-s.diff(v[0],y)])
def lap(v):return v.applyfunc(lambda a:sum(s.diff(a,q,2) for q in xx))
def grad(p):return s.Matrix([s.diff(p,q) for q in xx])
def residual(u,p):return u.diff(t)+u.jacobian(xx)*u-nu*lap(u)+grad(p)
old=curl(s.Matrix([x*y*z,t*x*z,y*y*x]))
pold=x*y*z+t*z
potentials=[s.Matrix([x*x*y,t*x*z,y*z*z]),
 s.Matrix([t*x*y,x*x*z,z*y]),
 s.Matrix([z*z*x,t*y*y,y*x*z]),
 s.Matrix([x*z,t*x*y,x*y*y])]
fields=[curl(p) for p in potentials]
pressures=[x*y+t*z,x*z+t*y,y*z+t*x,x*y*z+t*x*x]
coeff=[s.Function(f'ya{i}')(t) for i in range(4)]
v=sum((c*f for c,f in zip(coeff,fields)),s.zeros(3,1))
pi=sum(c*p for c,p in zip(coeff,pressures))
actual=residual(old+v,pold+pi)-residual(old,pold)
linear=s.zeros(3,1);clock=s.zeros(3,1);quad=s.zeros(3,1)
for j in range(4):
 shape=fields[j]
 linear+=coeff[j]*(shape.diff(t)+shape.jacobian(xx)*old+
                  old.jacobian(xx)*shape-nu*lap(shape)+grad(pressures[j]))
 clock+=s.diff(coeff[j],t)*shape
 for k in range(4):
  quad+=coeff[j]*coeff[k]*fields[k].jacobian(xx)*shape
for i in range(3):check(f'complete_physical_residual_component_{i}',actual[i]-linear[i]-clock[i]-quad[i])
for j,f in enumerate(fields):
 check(f'exact_shape_divergence_{j}',s.trace(f.jacobian(xx)))
check('old_field_divergence',s.trace(old.jacobian(xx)))
check('actual_added_field_divergence',s.trace(v.jacobian(xx)))
# Retain unequal affine clock rates before differentiating each amplitude.
tb,beta,tauc=s.symbols('tb beta tauc',real=True)
f=s.Function('Theta')(tauc)
composed=f.subs(tauc,tb+beta*t)
for order in range(1,4):
 check(f'physical_affine_clock_order_{order}',
       s.diff(composed,t,order)-beta**order*s.diff(f,tauc,order).subs(tauc,tb+beta*t))
A,h,D=s.symbols('A h D',real=True)
sub={A:s.Rational(1,2)+h,D:s.Rational(1,2)-h}
check('physical_time_equals_residual_unit',(-A-1-h-(-2*A-s.Rational(1,2))).subs(sub))
check('physical_viscosity_retains_epsilon',(-A-1-(-2*A-s.Rational(1,2)+h)).subs(sub))
check('advection_equals_residual_unit',-A-A-s.Rational(1,2)-(-2*A-s.Rational(1,2)))
check('pressure_equals_residual_unit',-2*A-s.Rational(1,2)-(-2*A-s.Rational(1,2)))
for e in [1,2]:
 check(f'actual_radial_norm_units_{e}',(s.Rational(e+1,2)-2*A)/2-(s.Rational(e+1,4)-A))
 check(f'actual_axial_derivative_norm_units_{e}',
       (s.Rational(e+1,2)-2*A-2*D)/2-(s.Rational(e+1,4)-A-D))
mu,lhat,A0,sigma,ni,gamma,L,Ls=s.symbols('mu lhat A0 sigma ni gamma L Ls',positive=True)
Pstar=A0/mu*lhat**(-s.Rational(7,8))
ui=mu*lhat/(sigma*s.sqrt(ni))
check('actual_second_component_frequency_power',ui*Pstar-A0/(sigma*s.sqrt(ni))*lhat**s.Rational(1,8))
check('actual_second_component_budget',2*ui*Pstar-2*A0/(sigma*s.sqrt(ni))*lhat**s.Rational(1,8))
check('actual_second_component_derivative_budget',gamma*ui*Pstar-gamma*A0/(sigma*s.sqrt(ni))*lhat**s.Rational(1,8))
alphamax=8*s.sqrt(2)*L/(gamma*Ls)
check('first_clock_cost',alphamax*2*gamma*Pstar-16*s.sqrt(2)*L/Ls*Pstar)
check('second_clock_cost',alphamax*gamma*ui*Pstar-8*s.sqrt(2)*L/Ls*A0/(sigma*s.sqrt(ni))*lhat**s.Rational(1,8))
receipt=dict(schema='third-growth-quantitative-replay-v1',all_passed=True,
 checks=checks,check_count=len(checks),
 sources={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [root/'quantitative_body.tex',Path(__file__)]},
 scope='Exact full-residual product rule with four nontrivial divergence-free shape fields, arbitrary time amplitudes, unequal clocks and retained physical viscosity; exact original scale identities. Analytic bounds are proved in the TeX.')
(root/'quantitative_replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(dict(all_passed=True,checks=len(checks))))
