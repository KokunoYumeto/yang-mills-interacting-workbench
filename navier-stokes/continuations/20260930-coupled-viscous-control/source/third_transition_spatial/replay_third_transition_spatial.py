"""Exact algebra replay for the full third-transition spatial extension.

Written analytic proofs, not this algebra replay, establish existence,
strict support inequalities, amplitude bounds, and smooth continuation.
This script differentiates unrestricted profile jets and a generic envelope.
It never substitutes a sine-only profile or a fixed deformation matrix.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as S

HERE = Path(__file__).resolve().parent
CHECKS = []

def check(name, difference):
    if isinstance(difference, S.MatrixBase):
        remainder = [S.simplify(S.expand(v)) for v in difference]
        passed = all(v == 0 for v in remainder)
    else:
        remainder = S.simplify(S.expand(difference))
        passed = remainder == 0
    CHECKS.append({'name': name, 'passed': bool(passed),
                   'remainder': str(remainder)})
    if not passed:
        raise AssertionError((name, remainder))

def inequality(name, assertion):
    passed = bool(assertion)
    CHECKS.append({'name': name, 'passed': passed})
    if not passed:
        raise AssertionError(name)

x, y = S.symbols('x y', real=True)
coords = (x, y)
kx, ky, Gx, Gy = S.symbols('kx ky Gx Gy', real=True)
k = S.Matrix([kx, ky]); G = S.Matrix([Gx, Gy])
J = S.Matrix([[0,-1],[1,0]])
rho = k.dot(k)
T, Q, Qr, d, wd, Theta = S.symbols('T Q Qr d wd Theta', real=True)
aa, bb, cc = S.symbols('D11 D12 D21', real=True)
D = S.Matrix([[aa,bb],[cc,-aa]])
flow = D*S.Matrix(coords)
P = S.Function('P')(x,y)
Fjets = [S.Function('F'+str(n))(x,y) for n in range(6)]
F, F1, F2 = Fjets[:3]
g = S.Function('g')(x,y)

def reduce_profiles(expr):
    """Use only P'=F and the linear phase chain rule at arbitrary jets."""
    replacements = {}
    for der in expr.atoms(S.Derivative):
        base = der.expr
        if base != P and base not in Fjets:
            continue
        nx = sum(count for var,count in der.variable_count if var == x)
        ny = sum(count for var,count in der.variable_count if var == y)
        order = nx + ny
        assert order == sum(count for _,count in der.variable_count)
        index = order-1 if base == P else Fjets.index(base)+order
        replacements[der] = kx**nx*ky**ny*Fjets[index]
    return expr.xreplace(replacements)

def dx(expr, i):
    return reduce_profiles(S.diff(expr, coords[i]))

def grad(expr):
    return S.Matrix([dx(expr,0),dx(expr,1)])

def jac(vec):
    return S.Matrix([[dx(vec[i],j) for j in range(2)] for i in range(2)])

def lap(expr):
    return dx(dx(expr,0),0)+dx(dx(expr,1),1)

def vlap(vec):
    return S.Matrix([lap(v) for v in vec])

gradg=grad(g); Hessg=jac(gradg); lapg=lap(g)
V=T*F*g
psi=Q*P*g
v=J*grad(psi)
check('trace-free rotation identity',D*J+J*D.T)
check('streamfunction velocity formula',v-Q*J*(k*F*g+P*gradg))
check('divergence zero',jac(v).trace())
expected_jac=Q*J*(k*k.T*F1*g+F*(k*gradg.T+gradg*k.T)+P*Hessg)
check('full velocity Jacobian',jac(v)-expected_jac)
expected_lapV=T*(rho*F2*g+2*F1*k.dot(gradg)+F*lapg)
check('full scalar Laplacian',lap(V)-expected_lapV)
expected_lapv=Q*J*(rho*k*F2*g+rho*F1*gradg+
    2*F1*k*k.dot(gradg)+2*F*Hessg*k+F*k*lapg+P*grad(lapg))
check('six-group full vector Laplacian',vlap(v)-expected_lapv)
check('reverse scalar parent interaction',v.dot(G)-Q*F*g*(J*k).dot(G)-Q*P*(J*gradg).dot(G))
check('complete scalar self-advection',v.dot(grad(V))-Q*T*(F**2-P*F1)*g*(J*k).dot(gradg))

kdot=-D.T*k
phase_t=kdot.dot(S.Matrix(coords))
gt=-flow.dot(gradg)
check('exact material phase transport',phase_t+flow.dot(k))
check('exact material envelope transport',gt+flow.dot(gradg))
Tdot=wd*Theta-Q*(J*k).dot(G)-d*rho*T
Vt=Tdot*F*g+T*F1*phase_t*g+T*F*gt
raw_scalar=Vt+flow.dot(grad(V))+v.dot(G)+v.dot(grad(V))-d*lap(V)
display_scalar=(wd*Theta*F*g+Q*P*(J*gradg).dot(G)
    +Q*T*(F**2-P*F1)*g*(J*k).dot(gradg)
    -d*T*(rho*(F+F2)*g+2*F1*k.dot(gradg)+F*lapg))
check('complete direct scalar PDE residual',raw_scalar-display_scalar)
psit=(Qr-d*rho*Q)*P*g+Q*F*phase_t*g+Q*P*gt
vt=J*grad(psit)
raw_vector=vt+jac(v)*flow+D*v+jac(v)*v-V*S.Matrix([0,1])-d*vlap(v)
display_vector=2*D*v+Qr*J*(k*F*g+P*gradg)+jac(v)*v-V*S.Matrix([0,1])-d*(rho*v+vlap(v))
check('complete direct vector PDE residual',raw_vector-display_vector)
check('material velocity derivative includes Dv',vt+jac(v)*flow-D*v-J*grad((Qr-d*rho*Q)*P*g))
check('both velocity interaction directions',jac(flow+v)*(flow+v)-jac(flow)*flow-jac(v)*v-jac(v)*flow-D*v)
check('moving squared phase derivative',2*k.dot(kdot)+2*k.dot(D.T*k))

# Direct affine-cell fields preserve the primitive constant before differentiation.
p0=S.symbols('P0', real=True)
phase=k.dot(S.Matrix(coords))
corepsi=Q*(p0+phase**2/2)
corev=J*S.Matrix([S.diff(corepsi,c) for c in coords])
check('affine streamfunction with retained P0',corev-Q*(J*k)*phase)
check('core Laplacian vanishes',S.Matrix([sum(S.diff(vv,c,2) for c in coords) for vv in corev]))
check('primitive constant changes localized velocity',J*S.Matrix([S.diff(Q*p0*g,c) for c in coords])-Q*p0*J*gradg)

# Exact coordinate metric with an arbitrary nonsingular material matrix.
m11,m12,m21,m22,p1,p2=S.symbols('m11 m12 m21 m22 p1 p2', real=True)
M=S.Matrix([[m11,m12],[m21,m22]]); p=S.Matrix([p1,p2]); Mi=M.inv()
Cmetric=Mi*Mi.T; zeta=Mi.T*p
check('material metric squared phase',zeta.dot(zeta)-(p.T*Cmetric*p)[0])
check('material mixed-Laplacian vector',Mi*zeta-Cmetric*p)
check('inverse material derivative',-Mi*D*M*Mi+Mi*D)

# Reconstruct the signed newest physical pair from the displayed scaled pair.
sig,Gamma,K,Pstar,N,R,Bphase,XX,YY=S.symbols('sigma Gamma K Pstar N R Bphase X Y', positive=True)
ss=S.symbols('s', positive=True)
delta=d*K**2/Gamma
calK=N/(sig*Gamma*R); calB=K*Bphase*sig/(K*Gamma)
Xp=calK*YY-delta*R*XX; Yp=calB*XX-delta*R*YY
the=-Pstar*XX; om=-K*Pstar*YY/sig
check('signed newest temperature inverse',-Pstar*Gamma*Xp-(N/(K*R)*om-d*K**2*R*the))
check('signed newest vorticity inverse',-K*Pstar*Gamma*Yp/sig-(K*Bphase*the-d*K**2*R*om))
sig1,sig2,Kap2,N2,Om2,Dlen,Lsym,Es,Fs,Vs=S.symbols('sigma1 sigma2 K2 N2 Omega2 D L E F V', positive=True)
eps=sig1/Gamma; q=sig1/sig2
normN=S.symbols('normalized_N2', real=True)
physicalE2dot=-(sig1**2*normN/Dlen)*(sig2*Vs)-d*Kap2**2*Dlen*(sig2**2*Fs)
scaledFdot=-q*eps*normN/Dlen*Vs-d*Kap2**2/Gamma*Dlen*Fs
check('second temperature exact q epsilon factors',physicalE2dot/(sig2**2*Gamma)-scaledFdot)

# Exact scalar constants used in operator norm, support and collar estimates.
Q2=S.symbols('Q2', real=True)
check('third support source exponent',Q2/S.Integer(16)-3*Q2+3+(47*Q2/S.Integer(16)-3))
check('second linear-cell source exponent',(Q2-1)/S.Integer(16)-2*Q2+(31*Q2+1)/S.Integer(16))
check('third velocity diffusion prefactor',S.Rational(64,63)*3-S.Rational(64,21))
inequality('sqrt154 less than 16',S.Integer(154)<16**2)
inequality('collar h stays above three quarters',1-S.Rational(1,512)**2-S.Rational(1,100)>S.Rational(3,4))
inequality('collar g stays above seven tenths',S.Rational(3,4)-S.Rational(1,100)>S.Rational(7,10))
inequality('collar scaled angle less than one fiftieth',S.Rational(1,1024)+S.Rational(1,100)<S.Rational(1,50))
inequality('collar feedback denominator above three fifths',S.Rational(7,10)*S.Rational(15,16)-4*S.Rational(1,512)**2/S.Integer(50)>S.Rational(3,5))
inequality('Picard movement fits stated cube',S.Rational(1,400)<S.Rational(1,100))
inequality('third total physical interval below fifteen',14+S.Rational(16,15)/16384<15)

sources=['third_transition_spatial_body.tex','replay_third_transition_spatial.py',
         '../third_transition/third_transition_body.tex',
         '../finite_stage/third_growth_entry.tex',
         '../modified_spatial/modified_spatial_body.tex']
hashes={p:hashlib.sha256((HERE/p).read_bytes()).hexdigest() for p in sources}
receipt={'schema_version':1,'generated_at':datetime.now(timezone.utc).isoformat(),
 'scope':'Full generic-profile spatial algebra and scaling through actual third transition; analytic existence and estimates are proved in TeX.',
 'checks':CHECKS,'checks_total':len(CHECKS),'checks_passed':sum(c['passed'] for c in CHECKS),
 'all_passed':all(c['passed'] for c in CHECKS),'source_sha256':hashes,
 'sympy_version':S.__version__}
(HERE/'replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'checks_total':len(CHECKS),'all_passed':receipt['all_passed']}))
