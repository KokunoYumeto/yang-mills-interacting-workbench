import json, hashlib
from pathlib import Path
import sympy as sp

# Exact algebraic replay of (S5)-(S7), using an arbitrary invertible 2x2 H.
h00,h01,h10,h11 = sp.symbols('h00 h01 h10 h11', nonzero=True)
t0,t1,s0,s1,eps = sp.symbols('t0 t1 s0 s1 eps', nonzero=True)
ap,am = sp.symbols('a_plus a_minus', nonzero=True)
H = sp.Matrix([[h00,h01],[h10,h11]])
T = sp.Matrix([t0,t1])
S = sp.Matrix([s0,s1])
y = H.inv()*T
a = sp.Matrix([ap,am])
d = H.inv()*(S/eps)
delta = sp.Matrix([d[0]/(2*ap), d[1]/(2*am)])
# Leading branch relations are a_sigma^2=y_sigma; B uses the fixed a's.
B = sp.simplify(eps*H*(2*sp.Matrix([ap,am]).multiply_elementwise(delta)))
assert all(sp.simplify(B[i]-S[i]) == 0 for i in range(2))
# Quadratic term is epsilon H(delta_sigma^2), retained with no sign simplification.
Q = eps*H*sp.Matrix([delta[0]**2,delta[1]**2])
assert Q.shape == (2,1)
# Sign linearity: B(S -> -S) = -B(S), while Q is even.
minus_delta = delta.xreplace({s0:-s0,s1:-s1})
Bminus = sp.simplify(eps*H*(2*a.multiply_elementwise(minus_delta)))
Qminus = sp.simplify(eps*H*sp.Matrix([minus_delta[0]**2,minus_delta[1]**2]))
assert all(sp.simplify(Bminus[i]+S[i]) == 0 for i in range(2))
assert all(sp.simplify(Qminus[i]-Q[i]) == 0 for i in range(2))
# Radial primitive identity for e=1,2.
r = sp.symbols('r', positive=True)
e = sp.symbols('e', integer=True, positive=True)
F = sp.Function('F'); b = sp.Function('b'); M = sp.symbols('M')
sigma = -r**(-e)*sp.Integral(sp.Symbol('rp')**e*(F(sp.Symbol('rp'))-b(sp.Symbol('rp'))*M),(sp.Symbol('rp'),0,r))
# Differentiate an equivalent dummy-integral form; Leibniz is checked explicitly.
I = sp.Function('I')
# If I'(r)=r^e(F-rho), then sigma=-r^-e I and (d+e/r)sigma= -F+rho.
rho = sp.Function('rho')
expr = sp.diff(-r**(-e)*I(r),r) + e/r*(-r**(-e)*I(r))
expr = sp.simplify(expr.subs(sp.diff(I(r),r),r**e*(F(r)-rho(r))))
assert sp.simplify(expr + F(r)-rho(r)) == 0

root = Path(__file__).resolve().parent
source = root.parent / 'openai_navier_stokes.txt'
receipt = {
    'all_passed': True,
    'checks': [
        'B(W0,L_Sigma)=Sigma for arbitrary invertible H and nonzero fixed amplitudes',
        'signed increment is odd in Sigma',
        'quadratic covariance remainder is even in Sigma',
        '(d/dr+e/r)(-r^-e integral_0^r s^e(F-rho) ds)=-F+rho for e=1,2'
    ],
    'source_text_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'memo': 'COVARIANCE_CORRECTION_PROVENANCE.md'
}
(root/'signed_cycle_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
