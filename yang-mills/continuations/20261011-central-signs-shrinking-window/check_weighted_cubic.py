from pathlib import Path
import itertools,json,math,time
from fractions import Fraction as F
import sympy as s
from evaluate_weighted_cubic import constants
from contracted_constants import mp,mpf
O=Path(__file__).resolve().parent
start=time.time()
checks=[]
def ck(name,value):
    checks.append(dict(name=name,passed=bool(value)))
    assert value,name

# Reuse only the original rational field definitions, not earlier test runs.
provider=O/'check_outside_flux.py'
ns={'__file__':str(provider)}
code=provider.read_text(encoding='utf8')
exec(code[:code.index('for J in [(0,),')],ns)
aa,rx,rm,rs,ra,rsum=[ns[n] for n in ['aa','rx','rm','rs','ra','rsum']]
px,padd,pmul,pscale=[ns[n] for n in ['px','padd','pmul','pscale']]
psi,coords,one,kap,eps=[ns[n] for n in ['psi','coords','one','kap','eps']]
def fullL(f):
    return rs(rsum(ra(rx(i,rx(i,f)),rs(rm(aa((i,)),rx(i,f)),2)) for i in range(6)),-kap)
def rational_zero(f):
    if not f:return True
    n=max(f)
    out={}
    for k,p in f.items():
        term=p
        for _ in range(n-k):term=pmul(term,psi)
        out=padd(out,term)
    return not out
def structure(i,h,l):
    return -eps(i%3,h%3,l%3) if i//3==h//3==l//3 else 0
def hess(i,h):
    return ra(rx(i,aa((h,))),rs(rsum(rs(aa((l,)),structure(i,h,l)) for l in range(6)),F(-1,2)))
samples=[{0:coords[0]},{0:pmul(coords[1],coords[2])},{0:padd(pmul(coords[0],coords[0]),pscale(coords[3],F(2,7)))}]
for n,t in enumerate(samples):
    for i in range(3):
        actual=ra(fullL(rx(i,t)),rs(rx(i,fullL(t)),-1))
        expected=ra(rs(rsum(rm(hess(i,h),rx(h,t)) for h in range(3)),2*kap),
                    rs(rsum(rs(rm(aa((h,)),rx(l,t)),structure(i,h,l)) for h,l in itertools.product(range(3),repeat=2)),kap))
        ck(f'original SU2 ordered commutator polynomial {n} {i}',rational_zero(ra(actual,rs(expected,-1))))
    ck(f'original product Casimir commutes with inside field {n}',
       all(rational_zero(ra(rsum(rx(h,rx(h,rx(i,t))) for h in range(6)),
           rs(rx(i,rsum(rx(h,rx(h,t)) for h in range(6))),-1))) for i in range(3)))

def rising(x,n):
    out=F(1)
    for i in range(n):out*=x+i
    return out
def haar_monomial(p):
    if any(n%2 for n in p):return F(0)
    out=F(1)
    for off in [0,4]:
        ns0=[n//2 for n in p[off:off+4]]
        out*=math.prod(rising(F(1,2),n) for n in ns0)/rising(F(2),sum(ns0))
    return out
def integral(p):
    return sum(v*haar_monomial(q) for q,v in p.items())
def psum(xs):
    out={}
    for x in xs:out=padd(out,x)
    return out
Bpsi=pscale(psum(px(o,px(o,psi)) for o in range(3,6)),-kap)
for i in range(3):
    derivative_numerator=padd(pmul(psi,pscale(psum(px(o,px(o,px(i,psi))) for o in range(3,6)),-kap)),pscale(pmul(Bpsi,px(i,psi)),-1))
    partial={}
    for power,value in derivative_numerator.items():
        outside=(0,)*4+power[4:]
        inside=power[:4]+(0,)*4
        partial[inside]=partial.get(inside,F(0))+value*haar_monomial(outside)
    ck('exact conditional outside energy derivative cancellation '+str(i),all(v==0 for v in partial.values()))
for n,t in enumerate(samples):
    f=t[0]
    grad=[px(i,f) for i in range(3)]
    lap=psum(px(i,px(i,f)) for i in range(3))
    comm=pscale(padd(pmul(psi,lap),pscale(psum(pmul(px(i,psi),grad[i]) for i in range(3)),2)),-kap)
    left=integral(pmul(pmul(comm,f),Bpsi))
    right=kap*integral(pmul(pmul(psi,Bpsi),psum(pmul(x,x) for x in grad)))
    ck('exact Haar first-derivative weighted cost '+str(n),left==right)
    d2=integral(pmul(pmul(psi,psi),psum(pmul(px(h,grad[i]),px(h,grad[i])) for h,i in itertools.product(range(3),repeat=2))))
    hh=F(0)
    for h,i in itertools.product(range(3),repeat=2):
        hnum=padd(pmul(psi,px(h,px(i,psi))),pscale(pmul(px(h,psi),px(i,psi)),-1))
        hnum=padd(hnum,pscale(pmul(psi,psum(pscale(px(l,psi),structure(h,i,l)) for l in range(3))),F(-1,2)))
        hh+=integral(pmul(hnum,pmul(grad[h],grad[i])))
    ck('exact original weighted Hessian energy identity '+str(n),d2==integral(pmul(comm,comm))/kap**2+2*hh)

# Independent finite tensor fixture for the weighted energy identity:
# a positive exact ground, actual conditional averages, complex dependent
# source columns and original nonzero multiplication/kinetic commutators.
# This fixture is not an evaluation of the Wilson vacuum.
A=s.kronecker_product(s.Matrix([[1,-1],[-1,1]]),s.eye(2))
B=s.kronecker_product(s.eye(2),s.Matrix([[1,-1],[-1,1]]))
D=A+B
psi_v=s.Matrix([1,1,1,2])/s.sqrt(7)
V=s.diag(1,2,2,0)
epsilon=s.Integer(1)
Mx=s.Integer(1)
ck('tensor fixture actual ground equation',(D+V)*psi_v==epsilon*psi_v)
ck('tensor fixture positive commuting sectors',A*B==B*A and min(A.eigenvals())==0 and min(B.eigenvals())==0)
rho=[s.Rational(2,7),s.Rational(5,7)]
fs=[s.Matrix([1+2*s.I,1+2*s.I,3-s.I,3-s.I]),
    s.Matrix([2,2,-1+3*s.I,-1+3*s.I])]
fs.append(2*fs[0]-s.I*fs[1])
Mu=s.diag(*[x*x for x in psi_v])
energy=s.diag(*[1/x for x in psi_v])*A*psi_v
means=s.Matrix([sum(Mu[i,i]*energy[i] for i in pair)/rho[n] for n,pair in enumerate([(0,1),(2,3)])])
meanvec=s.Matrix([means[0],means[0],means[1],means[1]])
kvec=-(energy-meanvec)
mul=lambda f:s.diag(*list(f))
cols=lambda xs:s.Matrix.hstack(*xs)
U=cols([mul(f)*psi_v for f in fs])
C=cols([(A*mul(f)-mul(f)*A)*psi_v for f in fs])
Sf=cols(fs).conjugate().T*Mu*cols(fs)
Kf=cols([mul(f)*kvec for f in fs]).conjugate().T*Mu*cols([mul(f)*kvec for f in fs])
R1=U.conjugate().T*(2*Mx*s.eye(4)-2*epsilon*s.eye(4)+V)*(2*Mx*s.eye(4)-V)*U
R2=(B*U-C).conjugate().T*(B*U-C)
R3=2*U.conjugate().T*A*B*U
R4=cols([mul(f)*meanvec for f in fs]).conjugate().T*Mu*cols([mul(f)*meanvec for f in fs])
delta=Kf-((2*Mx-epsilon)**2*Sf+C.conjugate().T*C-R1-R2-R3-R4)
ck('complete complex weighted variance matrix with all cross entries',all(s.expand(x)==0 for x in delta))
for n,R in enumerate([R1,R2,R3,R4]):
    ck('weighted remainder Hermitian '+str(n),all(s.expand(x)==0 for x in R-R.conjugate().T))
    ck('weighted remainder positive '+str(n),all(float(s.re(x))>=-1e-12 for x in R.evalf().eigenvals()))
ck('dependent raw source retained',Sf.det().expand()==0)

# Score variance identity for actual nonconstant conditional distributions.
for weights,values in [
    ([F(1,3),F(2,3)],[(F(1),F(0)),(F(-1),F(0))]),
    ([F(1,4),F(1,4),F(1,2)],[(F(1),F(0)),(F(0),F(1)),(F(0),F(0))]),
    ([F(2,5),F(3,5)],[(F(3,5),F(4,5)),(F(-5,13),F(12,13))])]:
    mean=[sum(p*x[i] for p,x in zip(weights,values)) for i in range(2)]
    Y=[sum((x[i]-mean[i])**2 for i in range(2)) for x in values]
    m=sum(p*y for p,y in zip(weights,Y))
    variance=sum(p*(y-m)**2 for p,y in zip(weights,Y))
    ck('full score variance remainder '+str(values),
       3-variance==(1-m)*(3-m)+sum(p*y*(4-y) for p,y in zip(weights,Y)))
    ck('score variance pointwise constraints '+str(values),0<=m<=1 and all(0<=y<=4 for y in Y))

# Full finite functions are evaluated independently of the asymptotic table.
for kval,theta in [('0.8',1),('1.3','0.6')]:
    for j in [4,16,10**8]:
        d=constants(j,kval,theta)
        for name,degree in [('d30',F(33,2)),('d21',F(47,2)),('d12',F(61,2)),('d03',F(75,2)),('direct_energy',F(76))]:
            ck(f'complete finite degree {j} {kval} {theta} {name}',d[name].degree==degree)
        ck(f'full six residual rows {j} {kval}',len(d['direct_terms'])==6)
        expected=[F(33),F(75,2),F(75,2),F(39,2),F(45,2),F(17,2)]
        ck(f'every original residual row degree {j} {kval}',[x.degree for x in d['direct_terms'].values()]==expected)
        ck(f'best original bound retained {j} {kval}',d['best'].value<=d['old']['best'].value)
        k=mpf(kval);th=mpf(theta)
        a=mpf(960000)/k**2;g=mpf(3840000)*mp.pi**2/k**2
        u1=mp.sqrt(g);gamma=mp.sqrt(2*mp.pi*(2*a+g))
        e=1/(mp.sqrt(21)*th**mp.mpf('2.5')*k**3)
        l11=2*a*e;l02=4*(a*mp.sqrt(2*a)+u1*(2*a+g))*e
        v30=2*mp.sqrt(2)*a*e;v21=mp.sqrt(l02*l02+2*a*l11*l11)
        r6=12*a*v21+8*a*gamma*v30
        leading=k**5*r6*r6/th
        ck(f'independent exact leading formula {j} {kval}',abs(d['direct_energy'].leading/leading-1)<mp.mpf('1e-65'))
result=dict(checks=len(checks),all_passed=all(x['passed'] for x in checks),
    seconds=time.time()-start,scope='Original two-factor SU2 polynomial commutators and exact Haar Hessian/first-derivative identities; independent finite tensor weighted-variance matrix retaining complex cross entries and dependent sources; exact score variance fixtures; complete six-row finite constants and independently computed leading coefficient. No Wilson-state moment is numerically inferred.',items=checks)
(O/'WEIGHTED_CUBIC_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8',newline='\n')
print(json.dumps({k:v for k,v in result.items() if k!='items'}))
