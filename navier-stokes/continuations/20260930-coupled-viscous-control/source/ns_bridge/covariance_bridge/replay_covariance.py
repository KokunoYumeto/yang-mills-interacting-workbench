"""Replay finite covariance/radial/curl algebra. Analytic support is proved in TeX."""
from pathlib import Path
import hashlib,json
import sympy as S
root=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    vals=list(value) if isinstance(value,S.MatrixBase) else [value]
    residuals=[S.factor(S.cancel(S.expand(v))) for v in vals]
    ok=all(v==0 for v in residuals)
    checks.append(dict(name=name,passed=ok,residual=[str(v) for v in residuals]))
    if not ok: raise AssertionError((name,residuals))

eps=S.symbols('epsilon',positive=True)
ap,am=S.symbols('a_plus a_minus',nonzero=True)
h11,h12,h21,h22=S.symbols('H11 H12 H21 H22')
s1,s2=S.symbols('Sigma1 Sigma2')
H=S.Matrix([[h11,h12],[h21,h22]])
sg=S.Matrix([s1,s2])
d=H.inv()*sg/eps
da=S.Matrix([d[0]/(2*ap),d[1]/(2*am)])
cross=eps*H*S.Matrix([2*ap*da[0],2*am*da[1]])
quad=eps*H*S.Matrix([da[0]**2,da[1]**2])
check('signed derivative right inverse',cross-sg)
check('complete principal covariance expansion',
 eps*H*S.Matrix([(ap+da[0])**2,(am+da[1])**2])
 -eps*H*S.Matrix([ap**2,am**2])-sg-quad)
check('signed correction odd',da.xreplace({s1:-s1,s2:-s2})+da)
check('quadratic correction even',quad.xreplace({s1:-s1,s2:-s2})-quad)
for sp,sm in [(1,1),(1,-1),(-1,1),(-1,-1)]:
    dp=S.Matrix([d[0]/(2*sp*ap),d[1]/(2*sm*am)])
    check('fixed primary signs '+str((sp,sm)),
          eps*H*S.Matrix([2*sp*ap*dp[0],2*sm*am*dp[1]])-sg)

w0=S.Matrix(S.symbols('w01:4')); ew=S.Matrix(S.symbols('ew1:4'))
vp=S.Matrix(S.symbols('vp1:4')); rs=S.Matrix(S.symbols('rs1:4'))
w=w0+ew; vs=vp+rs
def BT(a,b):return a*b.T+b*a.T
check('full tensor covariance update including old wave and curl',
 (w+vs)*(w+vs).T-w*w.T-BT(w0,vp)-BT(ew,vp)-BT(w,rs)-vs*vs.T)

r,rr=S.symbols('r rr',positive=True)
F=S.Function('F'); b=S.Function('b'); Me=S.symbols('M')
for e in (1,2):
    I=S.Integral(rr**e*(F(rr)-b(rr)*Me),(rr,0,r))
    sigma=-r**(-e)*I
    check('physical radial differential e='+str(e),
          S.diff(sigma,r)+e*sigma/r+F(r)-b(r)*Me)

# Exact scaling exponents, without replacing Q,q or source h by numerical values.
A,h,e=S.symbols('A h e',real=True)
check('moment physical chart exponent',-(2*A+S.Rational(1,2))+(e+1)/2-(e/2-2*A))
Q=S.symbols('Q',positive=True)
Sf=S.Function('Sigma')
chart_r=r/S.sqrt(Q)
physical_sigma=Q**(-2*A)*Sf(chart_r)
for ev in (1,2):
    chart_derivative=S.Subs(S.diff(Sf(rr),rr),rr,chart_r)
    check('actual radial chain rule e='+str(ev),S.simplify(
       S.diff(physical_sigma,r)+ev*physical_sigma/r
       -Q**(-2*A-S.Rational(1,2))*
        (chart_derivative+ev*Sf(chart_r)/chart_r)))
check('bump and moment chart product exponent',
 (e+1)/2+(2*A-e/2)-(2*A+S.Rational(1,2)))
check('q bump normalization exponent',-(e+1)/2+e/2+S.Rational(1,2))
check('leading covariance Q exponent',
 (-2*A+h+A+S.Rational(1,2)).subs(A,S.Rational(1,2)+h))
check('physical axial normal factor',S.Rational(1,2)-(S.Rational(1,2)-h)-h)

# A genuine witness of the unaveraged moment defect: average cos=0, tail not zero.
Y=S.symbols('Y',real=True)
check('auxiliary average of counterexample',
 S.integrate(S.cos(2*S.pi*Y),(Y,0,1)))
assert S.cos(2*S.pi*Y).subs(Y,0)==1
checks.append(dict(name='pointwise counterexample moment is nonzero at Y=0',
                   passed=True,residual=['1 (nonzero required)']))

# General exact curl leading amplitude identity; no transverse component lost.
n=S.Matrix(S.symbols('n1:4')); a=S.Matrix(S.symbols('a1:4')); km=S.symbols('km',nonzero=True)
nc=n.dot(n)
C=S.I*n.cross(a)/(km*nc)
check('curl triple product with explicit longitudinal part',
 S.I*km*n.cross(C)-a+n*n.dot(a)/nc)

# Full residual expansion for general smooth vectors in fixed Cartesian coordinates.
x,y,z,t,nu=S.symbols('x y z t nu',real=True)
X=(x,y,z)
def fv(name):return S.Matrix([S.Function(name+str(i))(x,y,z,t) for i in range(3)])
u=fv('u'); v=fv('v')
p=S.Function('p')(x,y,z,t); pp=S.Function('pi')(x,y,z,t)
def grad(f):return S.Matrix([S.diff(f,q) for q in X])
def adv(a,b):return S.Matrix([sum(a[j]*S.diff(b[i],X[j]) for j in range(3)) for i in range(3)])
def lap(a):return S.Matrix([sum(S.diff(a[i],q,2) for q in X) for i in range(3)])
def residual(a,p):return a.diff(t)+adv(a,a)-nu*lap(a)+grad(p)
check('full nonlinear residual update',residual(u+v,p+pp)-residual(u,p)
 -(v.diff(t)+adv(u,v)+adv(v,u)-nu*lap(v)+grad(pp))-adv(v,v))
# Independent exact polynomial test of all reflection terms, with nonzero time and pressure.
O=S.diag(1,-1,1)
psi=(1+t)*(x*x*y+x*y*y+z*y)
up=S.Matrix([S.diff(psi,y),-S.diff(psi,x),0]); pres=(1+t*t)*(x*y+z*z)
sub={x:x,y:-y,z:z}
usp=O*up.subs(sub, simultaneous=True); psp=pres.subs(sub, simultaneous=True)
check('reflection full viscous residual',
 residual(usp,psp)-O*residual(up,pres).subs(sub,simultaneous=True))
check('reflection divergence',sum(S.diff(usp[i],X[i]) for i in range(3)))
def curl(a):return S.Matrix([S.diff(a[2],y)-S.diff(a[1],z),S.diff(a[0],z)-S.diff(a[2],x),S.diff(a[1],x)-S.diff(a[0],y)])
check('reflection axial vector orientation',
 curl(usp)-O.det()*O*curl(up).subs(sub,simultaneous=True))

receipt=dict(schema='finite-composite-covariance-v2',all_passed=all(c['passed'] for c in checks),
check_count=len(checks),checks=checks,
scope='Exact finite algebra; compact support, all-order recurrences and coefficient-path construction proved in the TeX. No endpoint or infinite cycle certified.',
tex_sha256=hashlib.sha256((root/'covariance_bridge.tex').read_bytes()).hexdigest(),
script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
source_pdf_sha256=hashlib.sha256((root.parent/'openai_navier_stokes.pdf').read_bytes()).hexdigest())
(root/'covariance_replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(dict(all_passed=receipt['all_passed'],check_count=len(checks))))
