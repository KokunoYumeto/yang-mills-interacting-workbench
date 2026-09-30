"""Independent polynomial subtraction, annulus expansion and jet-scaling replay."""
from pathlib import Path
import json
import sympy as s

x, y, t, r, d = s.symbols('x y t r d', real=True, nonzero=True)
X = s.Matrix([x, y])
J = s.Matrix([[0, -1], [1, 0]])
e2 = s.Matrix([0, 1])
psi = (1-x*x-y*y)**3
A = s.Matrix([[1+t, 2-t], [t*t, -1-t]])
L = s.Matrix([[t+t*t, 1+2*t], [2-t*t, -t-t*t]])
G = s.Matrix([1+t*t, 2-t])
g = s.Matrix([t+2, t*t-1])
K = s.Matrix([[1-t, t*t], [t*t, 2+t]])
B = -J*L
assert B == B.T
grad = lambda f: s.Matrix([s.diff(f, x), s.diff(f, y)])
lap = lambda f: s.diff(f, x, 2)+s.diff(f, y, 2)
Q = (X.T*B*X)[0]/2
H = psi*g.dot(X)
Z = J*grad(psi*Q)
P = psi*(X.T*K*X)[0]/2
assert s.expand(Z[0]-psi*(L*X)[0]-Q*(J*grad(psi))[0]) == 0
assert s.expand(Z[1]-psi*(L*X)[1]-Q*(J*grad(psi))[1]) == 0
assert s.expand(s.diff(Z[0], x)+s.diff(Z[1], y)) == 0

# Compute the residual directly from total fields and subtract the old field.
oldT = G.dot(X)
oldV = A*X
oldP = (x*x+2*x*y+3*y*y)*(t+1)/2
Rtheta = lambda T,V: s.diff(T,t)+V.dot(grad(T))-d*lap(T)
Ru = lambda T,V,P: V.diff(t)+V.jacobian(X)*V+grad(P)-d*V.applyfunc(lap)-T*e2
directS = s.expand(Rtheta(oldT+H,oldV+Z)-Rtheta(oldT,oldV))
directV = (Ru(oldT+H,oldV+Z,oldP+P)-Ru(oldT,oldV,oldP)).applyfunc(s.expand)
transportS = s.diff(H,t)+(A*X).dot(grad(H))+Z.dot(G)+Z.dot(grad(H))
transportV = Z.diff(t)+A*Z+Z.jacobian(X)*A*X+Z.jacobian(X)*Z+grad(P)-H*e2
assert s.expand(directS-transportS+d*lap(H)) == 0
assert all(s.expand(v)==0 for v in directV-transportV+d*Z.applyfunc(lap))

n=grad(psi)
S=s.hessian(psi,(x,y))
k=(X.T*K*X)[0]/2
expandS = (psi*(g.diff(t)+A.T*g+L.T*G).dot(X)
           +psi**2*g.dot(L*X)+g.dot(X)*n.dot(A*X)
           +Q*G.dot(J*n)+psi*Q*g.dot(J*n)
           +psi*g.dot(X)*n.dot(L*X))
expandV = (psi*(L.diff(t)+A*L+L*A+K-e2*g.T)*X+psi**2*L*L*X
           +s.diff(Q,t)*J*n+Q*A*J*n
           +(L*X)*n.dot(A*X)+(J*n)*(B*X).dot(A*X)+Q*J*S*A*X
           +psi*Q*L*J*n+psi*(L*X)*n.dot(L*X)
           -Q*n.dot(L*X)*J*n+psi*Q*J*S*L*X+Q**2*J*S*J*n+k*n)
assert s.expand(transportS-expandS)==0
assert all(s.expand(v)==0 for v in transportV-expandV)
expandLapZ = lap(psi)*L*X+2*L*n+s.trace(B)*J*n+2*J*S*B*X+Q*J*grad(lap(psi))
assert all(s.expand(v)==0 for v in Z.applyfunc(lap)-expandLapZ)

# Verify each physical coordinate jet against its chart factor with r=3/7.
transportS=s.expand(transportS)
transportV=transportV.applyfunc(s.expand)
H=s.expand(H)
Z=Z.applyfunc(s.expand)
rr=s.Rational(3,7)
subs={x:x/rr,y:y/rr}
physicalS = s.expand(rr*transportS.subs(subs, simultaneous=True)-d/rr*lap(H).subs(subs,simultaneous=True))
physicalV = (rr*transportV.subs(subs, simultaneous=True)-d/rr*Z.applyfunc(lap).subs(subs,simultaneous=True)).applyfunc(s.expand)
cases=0
for a in range(4):
    for b in range(4-a):
        for time_order in range(3):
            jet=lambda f:s.diff(f,x,a,y,b,t,time_order)
            expectedS = (rr**(1-a-b)*jet(transportS)-d*rr**(-1-a-b)*jet(lap(H))).subs(subs,simultaneous=True)
            assert s.expand(jet(physicalS)-expectedS)==0
            for j in range(2):
                expectedV=(rr**(1-a-b)*jet(transportV[j])-d*rr**(-1-a-b)*jet(lap(Z[j]))).subs(subs,simultaneous=True)
                assert s.expand(jet(physicalV[j])-expectedV)==0
            cases+=3
M=s.symbols('M',nonnegative=True)
assert lap(M*(1-x*x-y*y)/4)==-M
out={'all_passed':True,'independent_full_pde_subtraction':True,
     'full_cutoff_expansions':True,'physical_signed_jet_cases':cases,
     'barrier_constant': '1/4 in dimension 2',
     'analytical_lower_bound': 'Maximum-principle argument in ifs:cutoff-diffusion-lower-bound; not inferred from sampled polynomial',
     'infinite_sequence_proved':False}
target=Path(__file__).with_name('full_support_force_receipt.json')
target.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
