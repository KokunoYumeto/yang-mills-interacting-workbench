"""Independent finite checks for ASL; no check replaces the analytic proof."""
from pathlib import Path
import json, re, hashlib, datetime, itertools
import numpy as np
import sympy as sp
import mpmath as mp

ROOT = Path(__file__).resolve().parent
checks = []
def record(name, passed, detail):
    checks.append(dict(name=name, passed=bool(passed), detail=detail))
def close(a,b,tol=2e-11):
    return np.linalg.norm(np.asarray(a)-np.asarray(b)) < tol

s = (ROOT/'ACTUAL_SEMIGROUP_LIMIT.md').read_text(encoding='utf-8')
labels = list(map(int,re.findall(r'\\tag\{ASL(\d+)\}',s)))
record('all stable proof labels',labels==list(range(1,67)),labels)
record('control characters',not any(ord(c)<32 and c not in '\n\t' for c in s),'No nonprinting control characters except LF/tab')
record('display delimiters',s.count(r'\[')==s.count(r'\]')==66,[s.count(r'\['),s.count(r'\]')])
record('inline delimiters',s.count(r'\(')==s.count(r'\)'),[s.count(r'\('),s.count(r'\)')])
record('restored differential spacing',r'^2\,d\langle' in s,'ASL11 spectral integral differential')
refs = [int(x) for x in re.findall(r'ASL(\d+)',s)]
record('all proof references resolve',all(x in labels for x in refs),sorted(set(refs)))

# ASL56: direct complete coefficient rows, including every tree exclusion.
mp.mp.dps=70
for m in (2,4,6,8,12):
    n=m+1; h=mp.pi/(2*n)
    v0=1/mp.sqrt(n)
    v=lambda r:mp.sqrt(mp.mpf(2)/n)*mp.cos(mp.pi*(r+mp.mpf('.5'))/n)
    w=lambda r:-mp.sqrt(mp.mpf(2)/n)*mp.sin(mp.pi*(r+1)/n)
    a=mp.fsum(abs(-v(i)*w(k)*v0/mp.sqrt(2)) for i in range(1,m+1) for k in range(m) for l in range(n))
    b2=mp.fsum(abs(v0*w(k)*v(l)/mp.sqrt(2)) for i in range(1,m+1) for k in range(m) for l in range(n))
    b3=mp.fsum(abs(-v0*v(k)*w(l)/mp.sqrt(2)) for i in range(n) for k in range(n) if (i,k)!=(0,0) for l in range(m))
    C=mp.cot(h); c=mp.cos(h)
    sa=mp.sqrt(mp.mpf(2)/n)*C*(C-c)
    sb=mp.sqrt(mp.mpf(2)/n)*((2-mp.mpf(1)/n)*C*C-c*C/n)
    record(f'complete raw row sums m={m}',abs(a-sa)<mp.mpf('1e-60') and abs(b2+b3-sb)<mp.mpf('1e-60'),{'S1':str(sa),'S3':str(sb)})

# ASL49: enumerate actual faces and their edges including all boundaries.
for m in (2,4,6):
    n=m+1
    for d,e in ((0,1),(0,2),(1,2)):
        inc={}
        faces=0
        for x in itertools.product(range(n),repeat=3):
            if x[d]==m or x[e]==m: continue
            xd=list(x); xd[d]+=1
            xe=list(x); xe[e]+=1
            for edge in ((x,d),(tuple(xd),e),(tuple(xe),d),(x,e)):
                inc[edge]=inc.get(edge,0)+1
            faces+=1
        expected=4*m*n*(2*m-1)
        record(f'orientation incidence m={m}, de={d}{e}',faces==m*m*n and sum(inc.values())==4*faces and max(inc.values())==2 and sum(r*r for r in inc.values())==expected,{'faces':faces,'sum_r':sum(inc.values()),'sum_r_squared':sum(r*r for r in inc.values())})

# ASL40: exact rational SU(2) derivative sums with inverse signs retained.
I=sp.I
pauli=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-I],[I,0]]),sp.Matrix([[1,0],[0,-1]])]
T=[-I*x/2 for x in pauli]
quats=[(1,2,2,4),(2,1,4,2),(2,4,1,2),(4,2,2,1)]
U=[]
for q in quats:
    U.append(sp.Rational(q[0],5)*sp.eye(2)-I*sum((sp.Rational(q[k+1],5)*pauli[k] for k in range(3)),sp.zeros(2)))
def prod(xs):
    ans=sp.eye(2)
    for x in xs: ans=ans*x
    return ans
for name,word in [('simple face',[(0,1),(1,1),(2,-1),(3,-1)]),('repeated commutator',[(0,1),(1,1),(0,-1),(1,-1)]),('canceling inverse pair',[(0,1),(0,-1),(2,1),(2,-1)])]:
    mats=[U[e] if sg==1 else U[e].inv() for e,sg in word]
    W=sp.simplify(sp.trace(prod(mats)))
    grad=sp.Integer(0)
    multiplicities={}
    for edge,sg in word: multiplicities[edge]=multiplicities.get(edge,0)+1
    for edge in multiplicities:
        for gen in T:
            deriv=sp.Integer(0)
            for k,(e,sg) in enumerate(word):
                if e!=edge: continue
                dm=gen*U[e] if sg==1 else -U[e].inv()*gen
                deriv+=sp.trace(prod(mats[:k])*dm*prod(mats[k+1:]))
            grad+=sp.simplify(deriv)**2
    grad=sp.simplify(grad);nu=sum(x*x for x in multiplicities.values())
    upper=sp.simplify(nu*(1-W*W/4));gap=sp.simplify(upper-grad)
    record('exact loop gradient '+name,gap>=0 and (name!='simple face' or gap==0),{'trace':str(W),'gradient_squared':str(grad),'nu':nu,'upper_minus_actual':str(gap)})

# ASL20-22: full product and commutator defects in an independent matrix model.
rng=np.random.default_rng(61011)
P=np.diag([1,1,1,0,0]).astype(complex);Q=np.eye(5)-P
z=rng.normal(size=(5,5))+1j*rng.normal(size=(5,5));Uq,_=np.linalg.qr(z)
B=Uq@np.diag([1+1j,2,-.3,.5j,-1])@Uq.conj().T
C=Uq@np.diag([-.2,1j,3,.2,-2j])@Uq.conj().T
phi=lambda x:P@x@P
record('exact compression product defect',close(phi(B@C)-phi(B)@phi(C),P@B@Q@C@P),'Commuting original matrices with generally noncommuting compressions')
record('exact compression commutator',close(phi(B)@phi(C)-phi(C)@phi(B),P@(C@Q@B-B@Q@C)@P),'Every order and sign checked')
schwarz=phi(B.conj().T@B)-phi(B).conj().T@phi(B)
record('Schwarz defect and positivity',close(schwarz,(Q@B@P).conj().T@(Q@B@P)) and np.linalg.eigvalsh(schwarz).min()>-2e-12,'Exact Gram defect')

# ASL31-32: an independent model realizes the unit defect and zero-time jump.
P3=np.diag([1,1,0]);Q3=np.eye(3)-P3
swap=np.array([[0,0,1],[0,1,0],[1,0,0]],float);omega=np.array([1,0,0])
record('unit escape product defect',close(P3@swap.T@Q3@swap@P3@omega,omega),'A_j=diag(0,2,j), B swaps vacuum and escaping component')
record('positive-time projection model',close(np.diag([1,np.exp(-1),0])@Q3,np.zeros((3,3))),'t=1/2, strong limit projection diag(1,1,0)')

# ASL59-63: tails whose amplitude and spectral cutoffs do not commute.
dim=7
z=rng.normal(size=(dim,dim));V,_=np.linalg.qr(z)
eig=np.array([0,.3,1,2,4,7,11.])
E=V@np.diag(eig<=2)@V.T
S=V@np.diag(np.exp(-.7*eig))@V.T
om=np.array([1,2,3,4,2,1,3.]);om/=np.linalg.norm(om)
F=np.array([-8,-3,-.5,1,2,5,10.]);v=F*om
u=v*(np.abs(F)<=3);r=v-u;lo=E@u;hi=u-lo
mixedlo=np.dot(lo,r);mixedhi=np.dot(hi,r)
record('full raw tail norm identity',abs(np.dot(v,v)-np.dot(lo,lo)-np.dot(hi,hi)-np.dot(r,r))<2e-12,'Low/high spectral plus amplitude remainder')
record('mixed raw norm terms cancel only together',abs(mixedlo+mixedhi)<2e-12 and abs(mixedlo)>1e-5,{'low_tail':float(mixedlo),'high_tail':float(mixedhi)})
terms=[lo@S@lo,hi@S@hi,2*lo@S@r,2*hi@S@r,r@S@r]
record('all five raw correlation terms',abs(v@S@v-sum(terms))<2e-12,[float(x) for x in terms])
record('spectral mixed correlation terms vanish',abs(lo@S@hi)<2e-12,'Spectral cutoff commutes with original semigroup')

# ASL35-36: complex reflected word Gram matrix, all time sums and adjoints.
A=np.diag([0,.2,.8,1.7]);omega=np.array([1,0,0,0],complex)
Tfun=lambda t:np.diag(np.exp(-t*np.diag(A)))
words=[];vec=[]
for k in (1,2,3,2):
    ts=np.sort(rng.uniform(0,1,k));obs=[]
    for _ in range(k): obs.append(np.diag(rng.normal(size=4)+1j*rng.normal(size=4)))
    # Mix the common commuting multiplication basis with the energy basis.
    zz=rng.normal(size=(4,4));rot,_=np.linalg.qr(zz)
    obs=[rot@x@rot.T for x in obs]
    v=omega.copy()
    for a in reversed(range(k)):
        gap=ts[a]-(ts[a-1] if a else 0)
        v=Tfun(gap)@obs[a]@v
    words.append((ts,obs));vec.append(v)
Gram=np.array([[np.vdot(v,w) for w in vec] for v in vec])
record('reflection-positive word Gram',np.linalg.eigvalsh(Gram).min()>-2e-12,{'least_eigenvalue':float(np.linalg.eigvalsh(Gram).min())})
ts,bs=words[1];us,cs=words[2]
right=omega.copy()
for a in reversed(range(len(cs))):
    right=cs[a]@right
    if a: right=Tfun(us[a]-us[a-1])@right
right=Tfun(ts[0]+us[0])@right
for a in range(len(bs)):
    right=bs[a].conj().T@right
    if a+1<len(bs): right=Tfun(ts[a+1]-ts[a])@right
record('reflected time-sum and adjoint identity',abs(np.vdot(omega,right)-Gram[1,2])<2e-12,'Complete ASL35 factor order')

# Exact asymptotic constants are proved analytically; this checks their path substitution.
j=mp.mpf(1000);kappa=mp.mpf(3)/2;n=2*j**4+1;m=n-1;h=mp.pi/(2*n)
S1=mp.sqrt(2/n)*mp.cot(h)*(mp.cot(h)-mp.cos(h))
S3=mp.sqrt(2/n)*((2-1/n)*mp.cot(h)**2-mp.cos(h)*mp.cot(h)/n)
beta=100*j*mp.sqrt(8)*mp.sin(h)
MF=8*beta*S1*S3/kappa;target=204800*mp.sqrt(2)/(kappa*mp.pi**3)
record('raw full-factor j9 constant',abs(MF/j**9/target-1)<mp.mpf('1e-10'),{'ratio':str(MF/j**9/target)})
N=3*m*n*n;M=3*m*m*n;B=min(2*M,6*kappa/(200*j)*mp.sqrt(N*M))
record('orientation budget path constant',abs((j*B/M)/(3*kappa/100)-1)<mp.mpf('1e-10'),str(j*B/M))
j=mp.mpf(100000);m=2*j**4;n=m+1;r=mp.mpf('.03');s=mp.mpf('.05');rr=mp.ceil(100*j*r);ss=mp.ceil(100*j*s)
K=(m-rr+1)*(m-ss+1)*n;N=3*m*n*n;M=3*m*m*n;B=6*kappa/(200*j)*mp.sqrt(N*M)
val=(rr*ss)**2*B/(3*K*j**3);target=3000000*kappa*r*r*s*s
record('physical rectangle averaged budget j3 constant',abs(val/target-1)<mp.mpf('1e-10'),{'computed':str(val),'target':str(target)})

out={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'proof_sha256':hashlib.sha256(s.encode()).hexdigest() if isinstance(s,str) else hashlib.sha256((ROOT/'ACTUAL_SEMIGROUP_LIMIT.md').read_bytes()).hexdigest(),'count':len(checks),'passed':sum(x['passed'] for x in checks),'checks':checks,'scope':'Finite exact and numerical checks supplement ASL1-ASL66; no actual vacuum samples or unproved numerical spectral limit are claimed.'}
(ROOT/'ACTUAL_LIMIT_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'count':len(checks),'passed':out['passed'],'failed':[x for x in checks if not x['passed']]},indent=2))
if out['passed']!=len(checks): raise SystemExit(1)
