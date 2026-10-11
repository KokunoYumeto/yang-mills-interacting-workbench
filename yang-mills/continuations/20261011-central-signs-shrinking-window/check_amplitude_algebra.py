from pathlib import Path
import datetime
import hashlib
import json
import sympy as S

root = Path(__file__).resolve().parent
x = S.symbols('x1:4', real=True)
t, ell = S.symbols('t ell', positive=True)
I = S.I
T = [S.Matrix([[0, -I/2], [-I/2, 0]]),
     S.Matrix([[0, -S.Rational(1, 2)], [S.Rational(1, 2), 0]]),
     S.Matrix([[-I/2, 0], [0, I/2]])]
zero = S.zeros(2)
def comm(A, B):
    return A * B - B * A

checks = []
def check(name, expression):
    entries = list(expression) if isinstance(expression, S.MatrixBase) else [expression]
    values = [S.simplify(S.expand(e)) for e in entries]
    assert all(v == 0 for v in values), (name, values)
    checks.append(name)

rho = [S.Function('rho12', positive=True)(*x),
       S.Function('rho13', positive=True)(*x),
       S.Function('rho23', positive=True)(*x)]
signs = [(1, 1, -1), (1, -1, 1), (-1, 1, 1)]
lam = [S.sqrt(2) * ell**(-S.Rational(3, 4)) *
       S.prod(rho[e]**(S.Rational(signs[i][e], 4)) for e in range(3)) for i in range(3)]
for e, (i, k) in enumerate(((0, 1), (0, 2), (1, 2))):
    check(f'AA2 density {i+1}{k+1}', ell**3 / 4 * lam[i]**2 * lam[k]**2 - rho[e])
for i in range(3):
    for r in range(3):
        Qr = sum(signs[i][e] * S.diff(rho[e], x[r]) / rho[e] for e in range(3))
        check(f'AA4 gradient {i+1},{r+1}', S.diff(lam[i], x[r]) - lam[i]*Qr/4)
        for s in range(3):
            Qs = sum(signs[i][e] * S.diff(rho[e], x[s]) / rho[e] for e in range(3))
            Hrs = sum(signs[i][e] * (S.diff(rho[e], x[r], x[s])/rho[e]
                       - S.diff(rho[e], x[r])*S.diff(rho[e], x[s])/rho[e]**2) for e in range(3))
            check(f'AA4 Hessian {i+1},{r+1},{s+1}',
                  S.diff(lam[i], x[r], x[s])-lam[i]*(Qr*Qs/16+Hrs/4))
check('AA5 Hessian constant', S.Rational(9,16)+S.Rational(3,4)-S.Rational(21,16))

b = [S.Function(f'b{i+1}', real=True)(*x) for i in range(3)]
B = [t*b[i]*T[i] for i in range(3)]
F = [[S.diff(B[i], x[k])-S.diff(B[k], x[i])+comm(B[k], B[i])
      for i in range(3)] for k in range(3)]
J = [sum((S.diff(F[k][i], x[k])+comm(B[k], F[k][i]) for k in range(3)), zero)
     for i in range(3)]
for i in range(3):
    expected = sum((t*(S.diff(b[i], x[k], x[k])*T[i]-S.diff(b[k], x[k], x[i])*T[k])
                    +t**2*(b[i]*S.diff(b[k], x[k])+2*b[k]*S.diff(b[i], x[k]))*comm(T[k], T[i])
                    -t**3*b[i]*b[k]**2*T[i] for k in range(3) if k != i), zero)
    check(f'AA12 complete matrix source {i+1}', J[i]-expected)
for k, i in ((0,1),(0,2),(1,2)):
    square = -2*S.trace(F[k][i]*F[k][i])
    expected = t**2*(S.diff(b[i],x[k])**2+S.diff(b[k],x[i])**2)+t**4*b[k]**2*b[i]**2
    check(f'AA10 full curvature square {k+1}{i+1}', square-expected)
check('AA19 covariant divergence of full source',
      sum((S.diff(J[i],x[i])+comm(B[i],J[i]) for i in range(3)),zero))

chi = S.Function('chi', real=True)(*x)
v = [S.Function(f'lambda{i+1}', real=True)(*x) for i in range(3)]
for i in range(3):
    for r in range(3):
        check(f'AA6 cutoff gradient {i+1},{r+1}',
              S.diff(chi*v[i],x[r])-S.diff(chi,x[r])*v[i]-chi*S.diff(v[i],x[r]))
        for s in range(3):
            check(f'AA6 cutoff Hessian {i+1},{r+1},{s+1}',
                  S.diff(chi*v[i],x[r],x[s])-S.diff(chi,x[r],x[s])*v[i]
                  -S.diff(chi,x[r])*S.diff(v[i],x[s])-S.diff(chi,x[s])*S.diff(v[i],x[r])
                  -chi*S.diff(v[i],x[r],x[s]))
    for k in range(3):
        if k == i:
            continue
        full = chi*v[i]*S.diff(chi*v[k],x[k])+2*chi*v[k]*S.diff(chi*v[i],x[k])
        expanded = 3*chi*S.diff(chi,x[k])*v[i]*v[k]+chi**2*(v[i]*S.diff(v[k],x[k])+2*v[k]*S.diff(v[i],x[k]))
        check(f'AA13 quadratic cutoff coefficient {k+1},{i+1}',full-expanded)

report = dict(time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              status='passed', exact_symbolic_checks=len(checks), checks=checks,
              sympy_version=S.__version__, script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              limitation='Finite symbolic checks supplement the full proofs; no PDE existence or measure-limit claim is tested here.')
(root/'AMPLITUDE_ALGEBRA_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status=report['status'], exact_symbolic_checks=len(checks))))
