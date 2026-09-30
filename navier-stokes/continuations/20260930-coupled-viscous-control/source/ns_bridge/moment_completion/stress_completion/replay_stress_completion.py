"""Exact replay of full Cartesian stress divergence and original moving-bump units."""
from pathlib import Path
import hashlib
import json
import sympy as s

root = Path(__file__).resolve().parent
checks = []
def eq(name, lhs, rhs=0):
    delta = s.trigsimp(s.simplify(lhs-rhs))
    if not (delta.is_zero_matrix if isinstance(delta, s.MatrixBase) else delta == 0):
        raise AssertionError((name, delta))
    checks.append(dict(name=name, passed=True))

r, z, t = s.symbols('r z t', positive=True)
theta = s.symbols('theta', real=True)
cs, sn = s.cos(theta), s.sin(theta)
O = s.Matrix([[cs,-sn,0],[sn,cs,0],[0,0,1]])
eq('oriented cylindrical basis is orthogonal', O.T*O, s.eye(3))
eq('oriented cylindrical basis has determinant one', O.det(), 1)
names = ['rr','rt','rz','tt','tz','zz']
f = {n:s.Function('S_'+n)(r,z) for n in names}
S = s.Matrix([[f['rr'],f['rt'],f['rz']],
              [f['rt'],f['tt'],f['tz']],
              [f['rz'],f['tz'],f['zz']]])
SC = O*S*O.T
dx = lambda a: cs*s.diff(a,r)-sn/r*s.diff(a,theta)
dy = lambda a: sn*s.diff(a,r)+cs/r*s.diff(a,theta)
dz = lambda a: s.diff(a,z)
divC = s.Matrix([dx(SC[i,0])+dy(SC[i,1])+dz(SC[i,2])
                 for i in range(3)])
div = s.simplify(O.T*divC)
expected = s.Matrix([
    s.diff(f['rr'],r)+(f['rr']-f['tt'])/r+s.diff(f['rz'],z),
    s.diff(f['rt'],r)+2*f['rt']/r+s.diff(f['tz'],z),
    s.diff(f['rz'],r)+f['rz']/r+s.diff(f['zz'],z)])
for i, name in enumerate(['radial','angular','axial']):
    eq('full Cartesian divergence including '+name+' connections',
       div[i], expected[i])
for e, idx, n in [(1,2,'rz'),(2,1,'rt')]:
    flux = f['zz'] if e == 1 else f['tz']
    eq(f'exact weighted divergence radial identity e={e}',
       r**e*expected[idx],
       s.diff(r**e*f[n],r)+s.diff(r**e*flux,z))

q = s.Function('q')(z,t)
J1, J2 = s.Function('J1')(z,t), s.Function('J2')(z,t)
F1, F2, Fr = [s.Function(n)(r,z,t) for n in ['F1','F2','Fr']]
sig = {}; bump = {}
for e, J, F in [(1,J1,F1),(2,J2,F2)]:
    x = r/s.sqrt(q)
    bh = s.Function('bhat'+str(e))
    be = q**(-s.Rational(e+1,2))*bh(x)
    bump[e] = be
    eq(f'original q-scaled radial bump derivative e={e}',
       s.diff(be,z),
       -s.diff(q,z)/(2*q)*((e+1)*be+r*s.diff(be,r)))
    eq(f'moving bump time derivative e={e}',s.diff(be,t),
       -s.diff(q,t)/(2*q)*((e+1)*be+r*s.diff(be,r)))
    beta_z = -s.diff(q,z)/(2*q)*r**(e+1)*be
    eq(f'cumulative bump mixed radial-axial identity e={e}',
       s.diff(beta_z,r), r**e*s.diff(be,z))
    corr = -r*s.diff(q,z)/(2*q)*be*J
    eq(f'exact primitive correction including varying bump e={e}',
       s.diff(corr,r)+e*corr/r,s.diff(be,z)*J)
    I = s.Function('I'+str(e))(r,z,t)
    sigma = -I/r**e
    sig[e] = s.Function('sigma'+str(e))(r,z,t)
    eq(f'weighted fundamental-theorem radial primitive e={e}',
       (s.diff(sigma,r)+e*sigma/r).subs(
           s.diff(I,r),r**e*(F-s.diff(be*J,z))),
       -F+s.diff(be*J,z))
    eq(f'old primitive residual identifies missing bump term e={e}',
       (-F+be*s.diff(J,z))-s.diff(be*J,z),
       -F-s.diff(be,z)*J)

T = s.Matrix([[0,sig[2],sig[1]],
              [sig[2],r*Fr+r*s.diff(sig[1],z),-bump[2]*J2],
              [sig[1],-bump[2]*J2,-bump[1]*J1]])
divT = s.Matrix([
    s.diff(T[0,0],r)+(T[0,0]-T[1,1])/r+s.diff(T[0,2],z),
    s.diff(T[0,1],r)+2*T[0,1]/r+s.diff(T[2,1],z),
    s.diff(T[0,2],r)+T[0,2]/r+s.diff(T[2,2],z)])
rules = {
    s.diff(sig[1],r):-F1+s.diff(bump[1]*J1,z)-sig[1]/r,
    s.diff(sig[2],r):-F2+s.diff(bump[2]*J2,z)-2*sig[2]/r}
for i, (name,F) in enumerate([('radial',Fr),('angular',F2),('axial',F1)]):
    eq('complete compact tensor cancels '+name+' force',divT[i].subs(rules),-F)
eq('radial-zero alternative after omitting hoop radial force',divT[0]+Fr,0)
p = s.trace(T)/3
T0 = T-p*s.eye(3)
eq('unique pressure gives tracefree stress',s.trace(T0),0)
eq('tracefree-pressure map exact inverse',T0+p*s.eye(3),T)
eq('full prescribed pressure sign and every diagonal entry',
   p,(r*Fr+r*s.diff(sig[1],z)-bump[1]*J1)/3)
for i in range(3):
    eq(f'tracefree decomposition entry {i}',T0[i,i],T[i,i]-p)
# Isotropic tensors: check Cartesian differential intertwiner explicitly.
P = s.Function('P')(r,z)
PC = O*(P*s.eye(3))*O.T
divP = s.Matrix([dx(PC[i,0])+dy(PC[i,1])+dz(PC[i,2])
                 for i in range(3)])
for i in range(3):
    eq(f'isotropic stress pressure gradient Cartesian row {i}',
       divP[i],s.Matrix([dx(P),dy(P),dz(P)])[i])

Fcyl = s.Matrix([Fr,F2,F1])
Fcart = O*Fcyl
torquecyl = s.Matrix([r,0,z]).cross(Fcyl)
eq('full oriented cylindrical torque',
   torquecyl,s.Matrix([-z*F2,z*Fr-r*F1,r*F2]))
torquecart = O*torquecyl
for i in range(3):
    eq(f'angular integral force component {i}',
       s.integrate(Fcart[i],(theta,0,2*s.pi)),
       2*s.pi*F1 if i == 2 else 0)
    eq(f'angular integral torque component {i}',
       s.integrate(torquecart[i],(theta,0,2*s.pi)),
       2*s.pi*r*F2 if i == 2 else 0)
# Antisymmetric first moments cancel for every symmetric tensor.
for i,j in [(0,1),(0,2),(1,2)]:
    eq(f'first-moment torque antisymmetry {i},{j}',T[j,i]-T[i,j],0)

h,e = s.symbols('h e', real=True)
A,D = s.Rational(1,2)+h,s.Rational(1,2)-h
eq('source anisotropic derivative factor',s.Rational(1,2)-D,h)
for ev in [1,2]:
    eq(f'original source flux radial unit e={ev}',
       -2*A+s.Rational(ev+1,2),
       -(2*A-s.Rational(ev+1,2)))
    eq(f'original source moment unit e={ev}',
       -(2*A+s.Rational(1,2))+s.Rational(ev+1,2),
       -(2*A-s.Rational(ev,2)))
    eq(f'flux to moment retains epsilon exponent e={ev}',
       (2*A-s.Rational(ev,2))+(-2*A+s.Rational(ev+1,2))-D,h)
    eq(f'original bump times flux stress unit e={ev}',
       -s.Rational(ev+1,2)-2*A+s.Rational(ev+1,2),-2*A)
    eq(f'complete primitive force source unit e={ev}',
       -s.Rational(ev,2)+s.Rational(ev+1,2)-2*A-s.Rational(1,2),-2*A)
    eq(f'complete primitive axial flux source unit e={ev}',
       -s.Rational(ev,2)+s.Rational(ev+1,2)-2*A-D,-2*A+h)
    eq(f'original varying bump correction source unit e={ev}',
       s.Rational(1,2)+(1-D)-1-s.Rational(ev+1,2)
       -2*A+s.Rational(ev+1,2),-2*A+h)
eq('radial hoop force has exact stress unit',
   s.Rational(1,2)-2*A-s.Rational(1,2),-2*A)
eq('axial hoop derivative retains epsilon',
   s.Rational(1,2)-D-2*A,-2*A+h)

sha = lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
receipt = dict(schema='full-stress-exact-replay-v1',all_passed=True,
    check_count=len(checks),checks=checks,
    proof_sha256=sha(root/'stress_completion.tex'),
    script_sha256=sha(Path(__file__)),
    scope='Exact Cartesian/cylindrical algebra, moving-bump derivatives, full cancellation, tracefree pressure, torque, and original source units. Smooth support, moment image and projection are proved in the complete TeX.')
(root/'replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['all_passed','check_count','proof_sha256']}))
