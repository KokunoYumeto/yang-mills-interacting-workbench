"""Finite, symbolic and source checks for LEM; the complete proof is separate."""
from pathlib import Path
import hashlib, json, re, math, datetime
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.integrate import quad

ROOT = Path(__file__).resolve().parent
W = ROOT
checks = []
def check(name, passed, detail):
    checks.append(dict(name=name, passed=bool(passed), detail=detail))
def close(x,y,tol=2e-10):
    return np.linalg.norm(np.asarray(x)-np.asarray(y)) < tol

s = (ROOT/'ACTUAL_LOW_ENERGY_MAPS.md').read_text(encoding='utf-8')
labels = [int(k) for k in re.findall(r'\\tag\{LEM(\d+)\}',s)]
check('complete proof labels',labels==list(range(1,56)),labels)
check('all local label references resolve',all(int(x) in labels for x in re.findall(r'LEM(\d+)',s)),sorted(set(re.findall(r'LEM\d+',s))))
check('display delimiters',s.count(r'\[')==s.count(r'\]')==56,[s.count(r'\['),s.count(r'\]')])
check('inline delimiters',s.count(r'\(')==s.count(r'\)'),[s.count(r'\('),s.count(r'\)')])
check('control character audit',not any(ord(c)<32 and c not in '\n\t' for c in s),'Only LF and tab permitted')
for a,b in [('gathered','gathered'),('split','split'),('array','array')]:
    check('environment '+a,s.count('\\begin{'+a+'}')==s.count('\\end{'+b+'}'),'Balanced')
for path,digest in [
    ('ACTUAL_SEMIGROUP_LIMIT.md','b5246f1a00b547036f9c15ebc7d4f2450bcb037bf4b307b2b1df94cc68408402'),
    ('SQUARE_ROOT_SCORE_RECEIVING_MAPS.md','51e9acd88b7030bc27545903dee4c3e8805afb182798d9a9d55e7c40363144f4')]:
    actual=hashlib.sha256((W/path).read_bytes()).hexdigest()
    check('cited public provider bytes: '+path,actual==digest,actual)

# Exact diagonal model: each approach space and the shrinking endpoint survives.
j=10000; sj=1/j; alpha=2.; beta=4.
energies=np.array([0,sj/2,sj,math.sqrt(sj),alpha-1/j,alpha,alpha+1/j,3,beta-1/j,beta,beta+1/j,j])
def diag_at(indices):
    v=np.zeros(len(energies));v[indices]=1;return np.diag(v)
V=diag_at([0]); Llt=diag_at([1]); J=diag_at([2]); L=Llt+J; D0=diag_at([3])
Z=V+L+D0; P=np.eye(len(energies));P[-1,-1]=0
check('zero-energy flag exact',close(Z,V+Llt+J+D0) and close(L@V,0),'vacuum, strict window, endpoint, missed shrinking rate')
T=np.diag(np.exp(-2*energies))
check('shrinking continuity bound',np.linalg.norm((T-np.eye(12))@L,2)<=1-math.exp(-2*sj)+1e-14,1-math.exp(-2*sj))
e=(np.eye(12)[:,1]+np.eye(12)[:,3])/math.sqrt(2)
C=V+np.outer(e,e); R=C@L@C
check('cyclic compression exact defect',close(R-R@R,C@L@(np.eye(12)-C)@L@C),float(np.linalg.norm(R-R@R,2)))
check('cyclic compression not a projection',np.linalg.norm(R-R@R,2)>.24,'One mixed zero-energy direction gives eigenvalue 1/2')
for inc_a,inc_b in [(False,False),(False,True),(True,False),(True,True)]:
    original=(energies>=alpha if inc_a else energies>alpha)&(energies<=beta if inc_b else energies<beta)
    ids=[6,7,8]+([5] if inc_a else [])+([9] if inc_b else [])
    check('endpoint interval '+str((inc_a,inc_b)),close(np.diag(original),diag_at(ids)),ids)
check('moving zero endpoint triple',close(Z,(V+Llt)+J+D0),'Moving threshold s_j includes vacuum in its approach-from-below space')

# Gram pseudoinverse formula including an actual null relation.
words=np.array([[1,0,1],[0,1,1],[0,0,0]],float); v=np.array([2,3,4.])
G=words.T@words; d=words.T@v
check('Gram detection with null rank',abs(d@np.linalg.pinv(G)@d-13)<1e-10,{'rank':int(np.linalg.matrix_rank(G)),'visible_norm_squared':13})

# Product form and form/Sylvester commutator estimates in a weighted two-point model.
# This is a check of algebraic receiving operations, not a replacement lattice model.
A=np.diag([0.,.2,2.,4.]); b=np.array([[1,.2,.1,.3],[.2,2,.4,.1],[.1,.4,-1,.2],[.3,.1,.2,.5]])
t=.7; T=expm(-t*A); Ehi=np.diag([0,0,1,1]); Elo=np.diag([1,1,0,0])
X=Ehi@b@Elo; Y=Ehi@(T@b-b@T)@Elo
check('separated Sylvester inequality',np.linalg.norm(X,2)<=np.linalg.norm(Y,2)/(math.exp(-t*.2)-math.exp(-t*2))+1e-12,{'left':float(np.linalg.norm(X,2))})

# Exact original face gradient and weighted one-orientation incidence calculation.
rng=np.random.default_rng(1729)
sigma=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex)]
gen=[-.5j*x for x in sigma]
m=2
vertices=[(i,k,l) for i in range(m+1) for k in range(m+1) for l in range(m+1)]
def shift(z,d):
    q=list(z);q[d]+=1;return tuple(q)
links={}
for z in vertices:
    for d in range(3):
        if z[d]<m:
            q=rng.normal(size=4);q/=np.linalg.norm(q)
            links[(z,d)]=q[0]*np.eye(2)+1j*sum(q[a+1]*sigma[a] for a in range(3))
faces=[]
for z in vertices:
    if z[0]<m and z[1]<m:
        faces.append([((z,0),1),((shift(z,0),1),1),((shift(z,1),0),-1),((z,1),-1)])
coeff=rng.normal(size=len(faces))+1j*rng.normal(size=len(faces))
gradient={e:np.zeros(3,complex) for e in links}
all_face_checks=[]
for c,face in zip(coeff,faces):
    matrices=[links[e] if sign==1 else links[e].conj().T for e,sign in face]
    hol=np.eye(2,dtype=complex)
    for U in matrices:hol=hol@U
    trace=np.trace(hol).real
    own=np.zeros((4,3),complex)
    for occurrence,(edge,sign) in enumerate(face):
        for a in range(3):
            D=gen[a]@matrices[occurrence] if sign==1 else -matrices[occurrence]@gen[a]
            prod=np.eye(2,dtype=complex)
            for r,U in enumerate(matrices):prod=prod@(D if r==occurrence else U)
            own[occurrence,a]=np.trace(prod)
        gradient[edge]+=c*own[occurrence]
    all_face_checks.append(abs(np.sum(abs(own)**2)-(4-trace**2))<2e-12)
qvalue=sum(np.sum(abs(g)**2) for g in gradient.values())
Rcoeff=np.sum(abs(coeff)**2)
check('original four-edge face identity',all(all_face_checks),len(all_face_checks))
check('weighted one-orientation gradient bound',qvalue<=8*Rcoeff+1e-12,{'gradient_squared':float(qvalue),'eight_R':float(8*Rcoeff),'faces':len(faces)})
inc={e:sum(e==f for face in faces for f,sgn in face) for e in links}
check('all orientation boundary incidences',sum(r*r for r in inc.values())==4*m*(m+1)*(2*m-1),sum(r*r for r in inc.values()))

# Exact Riemann sums for f(x)=product max(1-|x_i|,0), centers shifted in d,e.
integral=8/27
riemann=[]
for j in [2,4,8,16,32]:
    a=1/(100*j)
    def one(shifted):
        k=np.arange(-100*j-1,100*j+2)
        vals=np.maximum(1-abs(a*(k+shifted)),0)**2
        return a*sum(vals)
    val=one(.5)**2*one(0)
    bound=8*a**3*val
    riemann.append([j,float(val),float(j**3*bound)])
check('spatial full path constant',abs(riemann[-1][2]-(1/125000)*integral)<1e-12,riemann)
check('spatial Riemann convergence',abs(riemann[-1][1]-integral)<abs(riemann[0][1]-integral),integral)
theta=2
j=100
K=(2*j**4)**2*(2*j**4+1)
scaled=j**5.5*8*math.sqrt(j/(math.e*K))/(math.exp(-1)-math.exp(-theta))
check('relative-window orientation constant',abs(scaled-2*math.sqrt(2)/(math.sqrt(math.e)*(math.exp(-1)-math.exp(-theta))))<1e-7,scaled)

# Spectral projection and amplitude truncation fail to preserve orthogonality.
u=np.array([1.,0.]); r=np.array([0.,3.]); E=np.ones((2,2))/2
left=np.linalg.norm(E@(u+r))**2
right=np.linalg.norm(E@u)**2+2*np.vdot(E@u,E@r).real+np.linalg.norm(E@r)**2
check('raw amplitude-window full mixed term',abs(left-right)<1e-12 and abs(np.vdot(E@u,E@r))>0,{'mass':left,'mixed_contribution':float(2*np.vdot(E@u,E@r).real)})

# Exact physical heat-moment polynomial with both endpoint coefficients zero.
xvals=[sp.Rational(1),sp.Rational(3,4),sp.Rational(1,2),sp.Rational(1,4),sp.Rational(0)]
weights=[sp.Rational(1),sp.Rational(2),sp.Rational(3),sp.Rational(4),sp.Rational(5)]
h=lambda x:x-x*x
norm=sum(w*h(x)**2 for w,x in zip(weights,xvals))
Kmoment=lambda k:sum(w*x**k for w,x in zip(weights,xvals))
check('three-correlation detector identity',sp.simplify(norm-(Kmoment(2)-2*Kmoment(3)+Kmoment(4)))==0,str(norm))
check('detector exact peak and endpoint kills',h(sp.Rational(1,2))**2==sp.Rational(1,16) and h(0)==h(1)==0,'Physical h_t, no time rescaling')
def eta(x):
    return max(sp.Rational(0),min(sp.Rational(1),(x-sp.Rational(1,4))*8,(sp.Rational(3,4)-x)*8))
n=8
poly=lambda x:sum(eta(sp.Rational(k,n))*sp.binomial(n,k)*x**k*(1-x)**(n-k) for k in range(n+1))
direct=sum(w*poly(x) for w,x in zip(weights,xvals))
expanded=sum(eta(sp.Rational(k,n))*sp.binomial(n,k)*sp.binomial(n-k,r)*(-1)**r*Kmoment(k+r) for k in range(n+1) for r in range(n-k+1))
check('complete Bernstein correlation expansion',sp.simplify(direct-expanded)==0,str(direct))
check('Bernstein endpoint zeros',poly(0)==poly(1)==0,[str(poly(0)),str(poly(1))])
for n in [16,64,256]:
    xs=np.linspace(0,1,301)
    values=np.array([float(eta(sp.Rational(k,n))) for k in range(n+1)])
    maxerr=0.
    for x in xs:
        p=sum(values[k]*math.comb(n,k)*x**k*(1-x)**(n-k) for k in range(n+1))
        target=max(0,min(1,(x-.25)*8,(.75-x)*8))
        maxerr=max(maxerr,abs(p-target))
    check('Bernstein uniform error n='+str(n),maxerr<=4/math.sqrt(n)+1e-12,{'max_grid_error':maxerr,'proved_bound':4/math.sqrt(n)})

# Unconditional full residual interval lower bound.
H=np.array([[1.1,.2,0],[.2,2.,.3],[0,.3,4.]])
ev,U=np.linalg.eigh(H); psi=U[:,0]; E0=ev[0]; A=H-E0*np.eye(3)
Hcut=H[:2,:2]; evalcut,Ucut=np.linalg.eigh(Hcut); u0=evalcut[0]
phi=np.r_[Ucut[:,0],0.];phi*=np.sign(phi@psi)
w=u0-E0+1e-12; eps=np.linalg.norm(phi-psi); B=np.diag([1,2,-1]);M=2.;f=B@phi
c=1.2;d=.8;r=(H-u0*np.eye(3)-c*np.eye(3))@f
lower=max(0,math.sqrt(max(0,np.linalg.norm(f)**2-(np.linalg.norm(r)+w*np.linalg.norm(f))**2/d**2))-M*eps)**2
mask=(ev-E0>=c-d)&(ev-E0<=c+d)
actual=np.linalg.norm(U[:,mask].T@B@psi)**2
check('full residual original interval enclosure',actual>=lower-1e-12,{'actual_mass':float(actual),'lower_bound':float(lower)})
t=.5
f2=f[:2]; SR=lambda r:expm(-r*(Hcut-u0*np.eye(2)))@f2
rho=lambda r:abs(H[2,:2]@SR(r))
Kexact=(B@psi)@expm(-t*A)@(B@psi)
Kcut=f2@SR(t)
error=2*M*M*eps+M*M*(math.exp(t*w)-1)+M*quad(lambda r:math.exp((t-r)*w)*rho(r),0,t)[0]
check('physical heat accuracy full residual',abs(Kexact-Kcut)<=error+1e-12,{'difference':float(abs(Kexact-Kcut)),'bound':float(error)})
embedded=np.r_[SR(t),0.]
full=expm(-t*(H-u0*np.eye(3)))@f
integralvec=np.array([quad(lambda r,k=k:(expm(-(t-r)*(H-u0*np.eye(3)))@np.array([0.,0.,H[2,:2]@SR(r)]))[k],0,t)[0] for k in range(3)])
check('Duhamel exact sign and complementary block',close(full-embedded,-integralvec),'Full original Hamiltonian scalar and shift retained')

# Constants checked symbolically instead of floating huge path quantities.
kappa,C=sp.symbols('kappa C',positive=True)
check('raw orientation overlap asymptotic constant',
sp.simplify(2*(204800*sp.sqrt(2)/(kappa*sp.pi**3))*sp.sqrt(3*kappa/100)-40960*sp.sqrt(6)/(sp.sqrt(kappa)*sp.pi**3))==0,'All beta, row and curvature factors')
check('bulk variance coefficient',4*sp.sqrt(3)*(2*200*C/kappa)==1600*sp.sqrt(3)*C/kappa,'Pair of incidence-four edges')
check('heat global boundary count identity',sum([12*m,12*m*(m-1),3*m*(m-1)**2])==3*m*(m+1)**2,'All edge classes including boundaries')

result=dict(recorded_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),proof_sha256=hashlib.sha256((ROOT/'ACTUAL_LOW_ENERGY_MAPS.md').read_bytes()).hexdigest(),checks=checks,all_passed=all(x['passed'] for x in checks),count=len(checks),scope='Finite checks support the written derivation; no unknown vacuum expectation has been numerically supplied.')
(ROOT/'LOW_ENERGY_MAP_CHECKS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'count':len(checks),'all_passed':result['all_passed'],'failed':[c for c in checks if not c['passed']]},indent=2))
raise SystemExit(0 if result['all_passed'] else 1)
