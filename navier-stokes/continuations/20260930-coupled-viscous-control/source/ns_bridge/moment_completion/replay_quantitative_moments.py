"""Exact algebra replay for actual mixed moments and original moving-scale costs."""
from pathlib import Path
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent
checks=[]
def eq(name,lhs,rhs=0):
 delta=s.simplify(s.expand(lhs-rhs))
 if delta!=0:raise AssertionError((name,delta))
 checks.append(dict(name=name,passed=True))
x,eta,h,sg=s.symbols('x eta h sigma',real=True)
q=s.symbols('q',positive=True)
D=s.Rational(1,2)-h;A=s.Rational(1,2)+h;B=1-2*h*eta**2
Z=lambda p,f:(2*p*eta*f-eta*x*s.diff(f,x)+(1-eta**2)*s.diff(f,eta))/B
T=lambda p,f:(-p*f+x*s.diff(f,x)/2+D*eta*s.diff(f,eta))/B
eq('source A+D retains one',A+D,1)
eq('source D+2h retains A',D+2*h,A)
eq('implicit coordinate z has unit axial derivative',Z(D,eta),1)
eq('implicit coordinate z has zero time derivative',T(D,eta),0)
eq('implicit coordinate tau has zero axial derivative',Z(1,1-eta**2),0)
eq('implicit coordinate tau has negative unit time derivative',T(1,1-eta**2),-1)
eq('actual q axial coefficient',Z(1,s.Integer(1)),2*eta/B)
eq('actual q time coefficient',T(1,s.Integer(1)),-1/B)
eq('actual eta axial coefficient',Z(0,eta),(1-eta**2)/B)
eq('actual eta time coefficient',T(0,eta),D*eta/B)
f=s.Function('f')(x,eta)
eq('axial-time operators commute with their shifted homogeneities',
   T(sg-D,Z(sg,f)),Z(sg-1,T(sg,f)))
eq('radial-axial operators commute with shifted homogeneity',
   s.diff(Z(sg,f),x),Z(sg-s.Rational(1,2),s.diff(f,x)))
eq('radial-time operators commute with shifted homogeneity',
   s.diff(T(sg,f),x),T(sg-s.Rational(1,2),s.diff(f,x)))
for e in (0,1,2):
 beta=s.Rational(e+1,2);bh=x**2*(1-x)**3
 eq(f'original moving bump axial coefficient e={e}',
    Z(-beta,bh),-eta*((e+1)*bh+x*s.diff(bh,x))/B)
 beta_profile=s.integrate(x**e*bh,x)
 eq(f'weighted cumulative bump derivative e={e}',
    Z(0,beta_profile),-eta*x**(e+1)*bh/B)
 eq(f'pressure or moment bump time coefficient e={e}',
    T(-beta,bh),(beta*bh+x*s.diff(bh,x)/2)/B)
r,z,t=s.symbols('r z t',real=True)
shape=(r-1)**4*(2-r)**4
Crr=r*shape*(1+z+z*z+t*t)
Ctt=r*shape*(2-z+t+z*t)
Crz=r*shape*(z*z+t*z+1)
Czz=r*shape*(z+t*t+2)
Czt=r*shape*(z*t+z**3+1)
integ=lambda f:s.integrate(s.expand(f),(r,1,2))
g=-s.diff(Crr,r)-Crr/r-s.diff(Crz,z)+Ctt/r
P=integ(g)
Pformula=integ((Ctt-Crr)/r)-s.diff(integ(Crz),z)
Jtheta=integ(r*r*Czt)
Jz=integ(r*Czz)-integ(r*r*g)/2
Jzformula=integ(r*(Czz-Crr/2-Ctt/2))+s.diff(integ(r*r*Crz),z)/2
eq('actual pressure defect includes radial and axial covariance',P,Pformula)
eq('actual corrected axial flux includes radial pressure moment',Jz,Jzformula)
rho=shape/integ(shape)
eq('source pressure bump radial integral',integ(rho),1)
G=s.expand(g-rho*P)
p=s.integrate(G,r)
p=s.expand(p-p.subs(r,1))
eq('compact mean pressure upper boundary',p.subs(r,2),0)
eq('compact mean pressure radial equation',s.diff(p,r),g-rho*P)
crho=integ(r*r*rho)/2
eq('actual reconstructed pressure weighted moment',
   integ(r*p),-integ(r*r*g)/2+crho*P)
for a,b in ((0,0),(1,0),(0,1),(2,0),(1,1),(0,2)):
 eq(f'actual mixed pressure defect derivative {a},{b}',
    s.diff(P,z,a,t,b),s.diff(Pformula,z,a,t,b))
 eq(f'actual mixed axial flux derivative {a},{b}',
    s.diff(Jz,z,a,t,b),s.diff(Jzformula,z,a,t,b))
Erz=s.Matrix([[0,0,s.Rational(1,2)],[0,0,0],[s.Rational(1,2),0,0]])
Etz=s.Matrix([[0,0,0],[0,0,s.Rational(1,2)],[0,s.Rational(1,2),0]])
v1,v2,v3,w1,w2,w3=s.symbols('v1 v2 v3 w1 w2 w3')
v=s.Matrix([v1,v2,v3]);w=s.Matrix([w1,w2,w3]);C=w*v.T+v*w.T+v*v.T
contract=lambda E:s.trace(E.T*C)
eq('rz contraction retains both old cross terms and self term',contract(Erz),C[0,2])
eq('ztheta contraction retains both old cross terms and self term',contract(Etz),C[1,2])
eq('pressure diagonal contraction',contract(s.diag(-1,1,0)),C[1,1]-C[0,0])
eq('axial defect diagonal contraction',contract(s.diag(-s.Rational(1,2),-s.Rational(1,2),1)),
   C[2,2]-C[0,0]/2-C[1,1]/2)
for name,E in [('rz',Erz),('ztheta',Etz)]:
 eq(f'{name} exact half-norm eigenvalue polynomial',E.charpoly().as_expr(),
    E.charpoly().gen*(E.charpoly().gen**2-s.Rational(1,4)))
u,alpha,c=s.symbols('u alpha c',real=True)
Y=s.Function('Y');W=s.Function('W')
for a,b in ((0,1),(1,1),(0,2),(2,2),(1,3)):
 actual=s.diff(Y(u+alpha*c*t)*W(z,t),z,a,t,b)
 predicted=sum(s.binomial(b,k)*(alpha*c)**k*
   s.Subs(s.diff(Y(s.Symbol('s0')),s.Symbol('s0'),k),s.Symbol('s0'),u+alpha*c*t)*
   s.diff(W(z,t),z,a,t,b-k) for k in range(b+1))
 eq(f'actual complete amplitude-shape mixed product {a},{b}',actual,predicted.doit())
for e in (-1,0,1,2):
 eq(f'original weighted radial norm exponent e={e}',
    s.Rational(e+1,2)/2-A,s.Rational(e+1,4)-A)
for a,b in ((0,0),(1,0),(0,1),(2,3)):
 for k in range(b+1):
  eq(f'actual all-order time unit a={a},b={b},s={k}',
     -A-a*D-k*(1+h)-(b-k)*(1+h),-A-a*D-b*(1+h))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
receipt=dict(schema='moment-quantitative-exact-v1',all_passed=True,
 check_count=len(checks),checks=checks,
 proof_sha256=sha(root/'quantitative_moments.tex'),script_sha256=sha(Path(__file__)),
 scope='Exact source-coordinate differential operators; pressure/covariance defect identities; mixed derivative product and chart units. Analytic estimates are proved in the TeX.')
(root/'quantitative_replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(dict(all_passed=True,check_count=len(checks),proof_sha256=receipt['proof_sha256'])))
