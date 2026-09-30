"""Independent symbolic checks of the actual radial-moment calculation.

This replay verifies finite algebra and a concrete compact-architecture
example. It does not numerically sample or assert the source endpoint.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

OUT = Path(__file__).resolve().parent
checks = []


def check(name, value):
    value = s.trigsimp(s.simplify(value))
    if value != 0:
        raise AssertionError((name, value))
    checks.append({'name': name, 'passed': True})


r, theta, z, t = s.symbols('r theta z t', real=True)
rpos = s.symbols('rpos', positive=True)
er = s.Matrix([s.cos(theta), s.sin(theta), 0])
et = s.Matrix([-s.sin(theta), s.cos(theta), 0])
ez = s.Matrix([0, 0, 1])
E = s.Matrix.hstack(er, et, ez)
Srr, Srt, Srz, Stt, Stz, Szz = [s.Function(k)(r, theta, z)
    for k in ['Srr', 'Srt', 'Srz', 'Stt', 'Stz', 'Szz']]
Scyl = s.Matrix([[Srr, Srt, Srz], [Srt, Stt, Stz], [Srz, Stz, Szz]])
Scart = E * Scyl * E.T
# Cartesian tensor differentiation in physical cylindrical directions.
div_cart = Scart.diff(r)*er + Scart.diff(theta)*et/r + Scart.diff(z)*ez
div_cyl = E.T*div_cart
expected = [
    Srr.diff(r) + (Srr-Stt)/r + Srt.diff(theta)/r + Srz.diff(z),
    Srt.diff(r) + 2*Srt/r + Stt.diff(theta)/r + Stz.diff(z),
    Srz.diff(r) + Srz/r + Stz.diff(theta)/r + Szz.diff(z)]
for k in range(3):
    check(f'Cartesian symmetric tensor divergence component {k}',
          div_cyl[k]-expected[k])

# Independently derive the vector-Laplacian basis terms in Cartesian form.
vr, vt, vz = [s.Function(k)(r, theta, z) for k in ['vr', 'vt', 'vz']]
vcart = E*s.Matrix([vr, vt, vz])
lap_cart = vcart.diff(r, 2) + vcart.diff(r)/r + vcart.diff(theta, 2)/r**2 + vcart.diff(z, 2)
lap_cyl = E.T*lap_cart


def scalar_lap(a):
    return a.diff(r, 2)+a.diff(r)/r+a.diff(theta, 2)/r**2+a.diff(z, 2)


check('azimuthal vector Laplacian retains positive radial angular coupling',
      lap_cyl[1]-(scalar_lap(vt)-vt/r**2+2*vr.diff(theta)/r**2))
check('axial vector Laplacian is scalar cylindrical Laplacian',
      lap_cyl[2]-scalar_lap(vz))

u = s.Function('u')(r)
for weight in [1, 2]:
    check(f'weighted radial divergence exact derivative e={weight}',
          r**weight*(u.diff(r)+weight*u/r)-(r**weight*u).diff(r))

Y1, Y2, d = s.symbols('Y1 Y2 d', real=True)
b = s.sqrt(2)-1
q = s.Function('q')(r, z, t, Y1, Y2)
cr = s.Matrix([d*r**(d-1), -d*r**(d-1)*b])
ct = s.Matrix([b, 1])


def Dr(a):
    return a.diff(r)+cr[0]*a.diff(Y1)+cr[1]*a.diff(Y2)


def Dt(a):
    return a.diff(t)+ct[0]*a.diff(Y1)+ct[1]*a.diff(Y2)


expanded = q.diff(r, 2)
for i, yi in enumerate([Y1, Y2]):
    expanded += 2*cr[i]*q.diff(r, yi)+cr[i].diff(r)*q.diff(yi)
    for j, yj in enumerate([Y1, Y2]):
        expanded += cr[i]*cr[j]*q.diff(yi, yj)
check('lifted radial derivative square includes differentiated chain coefficient',
      Dr(Dr(q))-expanded)
check('source lifted radial and time derivatives commute', Dr(Dt(q))-Dt(Dr(q)))
check('source lifted radial and axial derivatives commute', Dr(q.diff(z))-Dr(q).diff(z))

H = s.Function('H')(r)
g = s.Function('g')(z)
n = s.symbols('n', integer=True, nonzero=True)
f = r*H.diff(r)
Ar = f*g*s.sin(n*theta)
At = s.Integer(0)
Az = H*g*s.cos(n*theta)
v = s.Matrix([Az.diff(theta)/r-At.diff(z),
              Ar.diff(z)-Az.diff(r),
              At.diff(r)+At/r-Ar.diff(theta)/r])
expected_v = s.Matrix([-n*H*g*s.sin(n*theta)/r,
                      f*g.diff(z)*s.sin(n*theta)-H.diff(r)*g*s.cos(n*theta),
                      -n*f*g*s.cos(n*theta)/r])
for k in range(3):
    check(f'compact transverse curl example component {k}', v[k]-expected_v[k])
check('compact transverse curl example exact incompressibility',
      v[0].diff(r)+v[0]/r+v[1].diff(theta)/r+v[2].diff(z))
C = s.Matrix([-s.I*f*g, 0, H*g])
xi = s.Matrix([0, n/r, 0])
a = s.I*xi.cross(C)
for k in range(3):
    check(f'potential recovered by exact transverse triple product component {k}',
          (s.I*xi.cross(a)/(xi.dot(xi)))[k]-C[k])

# Angular integration is exact, not sampled. For any nonzero integer n,
# substituting n=1 is not needed: SymPy retains the integer assumptions.
avg_ztheta = s.integrate(v[2]*v[1], (theta, 0, 2*s.pi))/(2*s.pi)
avg_zz = s.integrate(v[2]**2, (theta, 0, 2*s.pi))/(2*s.pi)
check('example angular axial-swirl covariance factor and sign',
      avg_ztheta-n*f*H.diff(r)*g**2/(2*r))
check('example angular axial quadratic covariance factor',
      avg_zz-n**2*f**2*g**2/(2*r**2))
check('example M2 integrand with original r squared weight',
      (r**2*avg_ztheta).diff(z)-n*g*g.diff(z)*r**2*H.diff(r)**2)
check('example M1 integrand with original r weight',
      (r*avg_zz).diff(z)-n**2*g*g.diff(z)*r*H.diff(r)**2)

# Compute the axial moment directly from the full cylindrical residual of
# this example (zero pressure, stationary time coefficient), retaining nu.
nu = s.symbols('nu', real=True)
adv_t = v[0]*v[1].diff(r)+v[1]*v[1].diff(theta)/r+v[2]*v[1].diff(z)+v[0]*v[1]/r
adv_z = v[0]*v[2].diff(r)+v[1]*v[2].diff(theta)/r+v[2]*v[2].diff(z)
res_t = adv_t-nu*(scalar_lap(v[1])-v[1]/r**2+2*v[0].diff(theta)/r**2)
res_z = adv_z-nu*scalar_lap(v[2])
avg_rt = s.integrate(v[0]*v[1], (theta, 0, 2*s.pi))/(2*s.pi)
avg_rz = s.integrate(v[0]*v[2], (theta, 0, 2*s.pi))/(2*s.pi)
avg_res_t = s.integrate(s.expand_trig(s.expand(res_t)), (theta, 0, 2*s.pi))/(2*s.pi)
avg_res_z = s.integrate(s.expand_trig(s.expand(res_z)), (theta, 0, 2*s.pi))/(2*s.pi)
check('full viscous example averaged angular residual equals covariance divergence',
      avg_res_t-(avg_rt.diff(r)+2*avg_rt/r+avg_ztheta.diff(z)))
check('full viscous example averaged axial residual equals covariance divergence',
      avg_res_z-(avg_rz.diff(r)+avg_rz/r+avg_zz.diff(z)))

e, A, hh, D = s.symbols('e A h D', real=True)
for weight in [1, 2]:
    check(f'moment source chart radial measure exponent e={weight}',
          s.Rational(weight+1, 2)-2*A-s.Rational(1, 2)-(s.Rational(weight, 2)-2*A))
    check(f'axial flux chart derivative leaves epsilon e={weight}',
          (s.Rational(weight+1, 2)-2*A-D-(s.Rational(weight, 2)-2*A)-hh)
          .subs(D, s.Rational(1, 2)-hh))
    check(f'weighted norm chart exponent e={weight}',
          (s.Rational(weight+1, 2)-2*A)/2-(s.Rational(weight+1, 4)-A))

wz, wt, vz0, vt0 = s.symbols('wz wt vz0 vt0', real=True)
flux2 = wz*vt0+vz0*wt+vz0*vt0
flux1 = 2*wz*vz0+vz0**2
check('full reflection reverses swirl moment flux',
      flux2.xreplace({wt: -wt, vt0: -vt0})+flux2)
check('full reflection preserves axial moment flux',
      flux1.xreplace({wt: -wt, vt0: -vt0})-flux1)
check('added amplitude negation preserves quadratic part of swirl flux',
      flux2.xreplace({vz0: -vz0, vt0: -vt0})+flux2-2*vz0*vt0)
check('added amplitude negation preserves quadratic part of axial flux',
      flux1.xreplace({vz0: -vz0, vt0: -vt0})+flux1-2*vz0**2)

receipt = {
    'schema': 'actual-radial-moment-replay-v1',
    'all_passed': all(item['passed'] for item in checks),
    'status': 'passed',
    'check_count': len(checks),
    'checks': checks,
    'body_sha256': hashlib.sha256((OUT/'moments_body.tex').read_bytes()).hexdigest(),
    'replay_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'scope': 'Finite symbolic moment identities, original chart factors, actual full-curl structure; no endpoint or infinite source estimates asserted.'
}
(OUT/'moments_replay_receipt.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'status': 'passed', 'checks': len(checks), 'body_sha256': receipt['body_sha256']}))
