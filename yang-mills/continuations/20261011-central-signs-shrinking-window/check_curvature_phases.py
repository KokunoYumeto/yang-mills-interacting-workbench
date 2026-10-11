"""Bounded checks of CP formulas. No unknown physical vacuum is simulated."""
from pathlib import Path
from fractions import Fraction
import datetime, hashlib, json, math, re
import numpy as np
import sympy as sp
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parent
W = ROOT
checks = []
def check(name, value, detail):
    checks.append(dict(name=name, passed=bool(value), detail=detail))
def close(a, b, tol=2e-10):
    return np.linalg.norm(np.asarray(a)-np.asarray(b)) < tol
source = (ROOT/'CURVATURE_PHASE_RECONSTRUCTION.md').read_text(encoding='utf-8')
labels = [int(x) for x in re.findall(r'\\tag\{CP(\d+)\}', source)]
check('CP labels complete and unique', labels == list(range(1,51)), labels)
check('CP references resolve', all(int(x) in labels for x in re.findall(r'CP(\d+)',source)), 'CP1 through CP50')
check('display delimiters',source.count(r'\[')==source.count(r'\]'),[source.count(r'\['),source.count(r'\]')])
check('inline delimiters',source.count(r'\(')==source.count(r'\)'),[source.count(r'\('),source.count(r'\)')])
check('no unexpected controls or replacement character',not any(ord(c)<32 and c not in '\n\t' for c in source) and '\ufffd' not in source,'UTF-8 source audit')
for env in ['gathered','split','array']:
    check('balanced '+env,source.count(r'\begin{'+env+'}')==source.count(r'\end{'+env+'}'),'Source environment audit')
provider_hashes = {
 'LOCAL_CURVATURE_BUDGET.md':'7e394f8c0e4a7d1cb2bfa4ed4e7b7438a17d6b864133ae51156ee022b4281a56',
 'ACTUAL_LOW_ENERGY_MAPS.md':'ca25438bb2e1abef8c06fb3266f4e7dab7db4e301347933801c8e3eafe995b12',
 'ACTUAL_SEMIGROUP_LIMIT.md':'c9fda8c47289a1dc9a5d89d190b5c64affc56454e317ca4d07e66a450a809ef1',
 'SQUARE_ROOT_SCORE_RECEIVING_MAPS.md':'5664836f2cf24e0ed6e58849e508afb9990961d5bf846626138229e88fa7f28f'}
for path, expected in provider_hashes.items():
    actual=hashlib.sha256((W/path).read_bytes()).hexdigest()
    check('accepted source unchanged: '+path,actual==expected,actual)

# Local recurrence, every factor and the full surface contribution.
L,r=sp.symbols('L r',positive=True)
U=[sp.Integer(1),L]
for k in range(1,10):
    U.append(sp.expand(L*U[-1]+r*r*k*k*U[-2]))
check('recurrence U2 and U3',U[2]==L*L+r*r and U[3]==L**3+5*L*r*r,[str(U[2]),str(U[3])])
check('recurrence homogeneity and positive coefficients',all(sp.Poly(u,L,r).total_degree()==p and all(c>0 for c in sp.Poly(u,L,r).coeffs()) for p,u in enumerate(U)), 'Orders zero through ten')
check('all recurrence leading coefficients equal one',all(sp.Poly(u,L,r).coeff_monomial(L**p)==1 for p,u in enumerate(U)),'Orders zero through ten')
check('recurrence asymptotic coefficient',all(sp.limit(u/L**p,r,0)==1 for p,u in enumerate(U)), 'Each fixed moment retains leading coefficient one')
majorant=[]
for lv in [.01,.2,1,20,1000]:
    for rv in [.001,.3,3,400]:
        for p,u in enumerate(U):
            majorant.append(float(u.subs({L:lv,r:rv})) <= (lv+p*rv)**p*(1+3e-14))
check('recurrence majorant',all(majorant),{'cases':len(majorant)})
a,kappa,R=sp.symbols('a kappa R',positive=True)
q=sp.symbols('q',positive=True)
N=3*q*(q+1)**2; M=3*q*q*(q+1); cross=12*q*(q+1); g2=kappa*a/2
Lambda=6*g2*sp.sqrt(N*M)+2*cross
check('optimized local branch full expression',sp.simplify(Lambda-(18*g2*(q*(q+1))**sp.Rational(3,2)+24*q*(q+1)))==0,str(Lambda))
check('local asymptotic includes crossing cost',sp.simplify(sp.limit(a*a*Lambda.subs(q,R/a),a,0,dir='+')-(9*kappa*R**3+24*R**2))==0,'9 kappa R^3 + 24 R^2')
check('original moment coefficient',sp.simplify(4*kappa/(1/(2*g2*a))-16*g2**2)==0,'4 kappa / b = 16 (g^2)^2, with b=1/(2 g^2 a)')
check('a squared rho vanishes',sp.limit(a*a*(4*g2),a,0)==0,'rho=4 g^2')
errors=[]
for j in [100,1000,10000]:
    av=1/(100*j); kv=.7; rv=.8; qv=math.ceil(rv/av)+3
    Lv=min(2*3*qv*qv*(qv+1),18*(kv*av/2)*(qv*(qv+1))**1.5)+24*qv*(qv+1)
    errors.append(abs(av*av*Lv-(9*kv*rv**3+24*rv**2)))
check('ceil patch follows exact asymptotic',errors[2]<errors[1]<errors[0] and errors[-1]<.001,errors)

# Differentiate actual four-factor SU(2) faces on a small original cubic box.
# Haar samples are used only for pointwise identities, not as physical vacua.
rng=np.random.default_rng(112023)
sigma=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex)]
generators=[-.5j*s for s in sigma]
def shift(z,d):
    out=list(z);out[d]+=1;return tuple(out)
m=2
vertices=[(i,j,k) for i in range(m+1) for j in range(m+1) for k in range(m+1)]
links={}
for z in vertices:
    for d in range(3):
        if z[d]<m:
            v=rng.normal(size=4);v/=np.linalg.norm(v)
            links[z,d]=v[0]*np.eye(2)+1j*sum(v[b+1]*sigma[b] for b in range(3))
faces=[]
for z in vertices:
    for d,e in [(0,1),(0,2),(1,2)]:
        if z[d]<m and z[e]<m:
            faces.append(((d,e),[((z,d),1),((shift(z,d),e),1),((shift(z,e),d),-1),((z,e),-1)]))
edge_index={e:i for i,e in enumerate(links)}
def face_data(face, link_map):
    matrices=[link_map[e] if sign==1 else link_map[e].conj().T for e,sign in face]
    product=np.eye(2,dtype=complex)
    for mat in matrices:product=product@mat
    trace=float(np.trace(product).real)
    grad=np.zeros((len(links),3))
    for n,(edge,sign) in enumerate(face):
        for b,gen in enumerate(generators):
            D=gen@matrices[n] if sign==1 else -matrices[n]@gen
            product=np.eye(2,dtype=complex)
            for r,mat in enumerate(matrices):product=product@(D if r==n else mat)
            grad[edge_index[edge],b]=-np.trace(product).real
    return 2-trace,grad
data=[face_data(face,links) for orientation,face in faces]
check('actual original face count',len(faces)==3*m*m*(m+1),{'faces':len(faces),'edges':len(links)})
check('face single-edge Casimir identity',all(abs(np.sum(grad[edge_index[edge]]**2)-(D-D*D/4))<3e-14 for ((_,face),(D,grad)) in zip(faces,data) for edge,sign in face),'Every boundary occurrence, 3 generators')
check('full face gradient identity',all(abs(np.sum(grad**2)-(4*D-D*D))<1e-13 for D,grad in data),'Four differentiated factors retained')
WQ=sum(D for D,grad in data)
gradientW=sum(grad for D,grad in data)
check('all-orientation local gradient budget',np.sum(gradientW**2)<=16*WQ+1e-12,{'GammaW':float(np.sum(gradientW**2)),'bound':16*WQ})
selected=[n for n,(orientation,face) in enumerate(faces) if orientation==(0,1)]
weights=rng.uniform(-2,2,len(selected));F=max(abs(weights));av=.07
C=av*sum(c*data[n][0] for c,n in zip(weights,selected))
gradient=av*sum(c*data[n][1] for c,n in zip(weights,selected))
Gamma=float(np.sum(gradient**2))
incidence={e:sum(e in [x for x,sign in faces[n][1]] for n in selected) for e in links}
full_bound=av*av*sum(incidence[e]*sum(c*c*(data[n][0]-data[n][0]**2/4) for c,n in zip(weights,selected) if e in [x for x,sign in faces[n][1]]) for e in links)
check('one-orientation incidence including boundary',max(incidence.values())==2 and min(incidence.values())==0,sorted(set(incidence.values())))
check('full weighted gradient incidence bound',Gamma<=full_bound+1e-12 and full_bound<=8*av*av*F*F*WQ+1e-12,{'actual':Gamma,'incidence_bound':full_bound,'local_bound':8*av*av*F*F*WQ})
theta=1.7
check('exact phase gradient',abs(np.sum(abs(1j*theta*np.exp(1j*theta*C)*gradient)**2)-theta*theta*Gamma)<1e-12,'No centering contribution to link derivatives')
edge=faces[selected[0]][1][2][0];gen=generators[1];eps=1e-6
changed={}
for sign in [-1,1]:
    new=dict(links);new[edge]=expm(sign*eps*gen)@links[edge]
    changed[sign]=av*sum(c*face_data(faces[n][1],new)[0] for c,n in zip(weights,selected))
check('inverse occurrence derivative finite difference',abs((changed[1]-changed[-1])/(2*eps)-gradient[edge_index[edge],1])<2e-9,'Includes derivative -U inverse T of the third factor')

# Exact complex Leibniz cross term and the form-root triangle inequality.
x=np.linspace(0,2*np.pi,20001,endpoint=False)
b=np.exp(1j*(.4*np.cos(x)+.1*np.sin(3*x)))
bp=1j*(-.4*np.sin(x)+.3*np.cos(3*x))*b
h=(1+.2*np.cos(2*x))*np.exp(.3j*np.sin(x))
hp=(-.4*np.sin(2*x)+.3j*np.cos(x)*(1+.2*np.cos(2*x)))*np.exp(.3j*np.sin(x))
lhs=abs(bp*h+b*hp)**2
rhs=abs(b)**2*abs(hp)**2+abs(h)**2*abs(bp)**2+2*np.real(np.conj(b)*h*bp*np.conj(hp))
check('full complex product cross term',np.max(abs(lhs-rhs))<1e-13,float(np.max(abs(lhs-rhs))))
check('form-root bound',math.sqrt(np.mean(lhs))<=max(abs(b))*math.sqrt(np.mean(abs(hp)**2))+max(abs(h))*math.sqrt(np.mean(abs(bp)**2))+1e-13,'Circle quadrature tests the exact differentiated algebra')
phase=np.exp(1j*theta*C);eta=-.8;center=123.4
check('phase multiplication and adjoint',abs(phase*np.exp(1j*eta*C)-np.exp(1j*(theta+eta)*C))<1e-12 and abs(np.conj(phase)-np.exp(-1j*theta*C))<1e-12,'Original curvature coefficient unchanged')
check('centering cancels only in relative phase',abs(np.exp(-1j*theta*center)*np.exp(1j*theta*(C+.3))*np.conj(np.exp(-1j*theta*center)*phase)-np.exp(1j*theta*.3))<1e-12,'Both scalar factors retained before cancellation')

# Finite reversible example checks semigroup and word receiving operations only.
weights_state=np.array([.2,.3,.5]);conduct=np.array([[0,.4,.2],[.4,0,.1],[.2,.1,0.]])
Lgen=conduct/weights_state[:,None];np.fill_diagonal(Lgen,-Lgen.sum(axis=1))
t=.37;S=expm(t*Lgen);psi=np.sqrt(weights_state)
A=-np.diag(psi)@Lgen@np.diag(1/psi);T=expm(-t*A)
check('ground transform exact',close(T,np.diag(psi)@S@np.diag(1/psi)),'Three-state reversible identity only')
check('Markov invariance and positivity',close(S@np.ones(3),np.ones(3)) and close(weights_state@S,weights_state) and np.min(S)>=0,'Actual-state proof remains CP12-CP13')
check('detailed balance and vacuum',close(A,A.T) and close(A@psi,0) and close(np.diag(weights_state)@S,S.T@np.diag(weights_state)),{'min_eigenvalue':float(np.linalg.eigvalsh(A)[0])})
bs=[np.exp(1j*np.array([.1,1,2])),np.exp(1j*np.array([.7,-.2,.6])),np.array([.7,-.4,.5])]
hv=np.ones(3,complex);Hv=1.;Ev=0.
def energy(hv):return float(np.vdot(psi*hv,A@(psi*hv)).real)
word_checks=[]
for bj in reversed(bs):
    oldH=Hv;Mv=float(max(abs(bj)))
    hv=bj*hv;Hv=oldH*Mv;Ev=Mv*Ev+oldH*math.sqrt(max(0,energy(bj)))
    word_checks.append(max(abs(hv))<=Hv+1e-13 and energy(hv)<=Ev*Ev+1e-12)
    hv=S@hv
    word_checks.append(max(abs(hv))<=Hv+1e-13 and energy(hv)<=Ev*Ev+1e-12)
check('bounded word recursion and contractivity',all(word_checks),{'steps':len(word_checks),'ratio_bound':Hv,'form_root_bound':Ev})
v=psi*hv
check('zero-time collision spectral estimate',np.linalg.norm((np.eye(3)-T)@v)**2<=t*float(np.vdot(v,A@v).real)+1e-13,'(1-exp(-t lambda)) squared <= t lambda')
Bmat=np.diag(bs[0]);hj=np.array([.5+.2j,-.3j,.8])
comm=Bmat@S@hj-S@Bmat@hj
conditional=np.sum(S*(bs[0][:,None]-bs[0][None,:])*hj[None,:],axis=1)
check('conditional commutator identity',close(comm,conditional),'All signs and time endpoints retained')
g=[S@bs[0],S@(bs[1]*(S@bs[2]))]
gram=np.array([[np.vdot(psi*gi,psi*gj) for gj in g] for gi in g])
check('reflection Gram positivity',np.linalg.eigvalsh(gram).min()>-1e-12,'Bounded cylinder quotient identity')

# Exact drift cancellation and all martingale constants.
Ct,C0,I=sp.symbols('Ct C0 I',real=True)
forward=Ct-C0-I;reverse=C0-Ct-I
check('forward-reverse drift cancellation',sp.expand((forward-reverse)/2-(Ct-C0))==0,'Each martingale carries the same negative drift integral')
for p in range(1,9):
    h,c=sp.symbols('h c',positive=True)
    candidate=((2*p-1)*c*h)**p
    check('moment ODE coefficient p='+str(p),sp.simplify(sp.diff(candidate,h)-p*(2*p-1)*candidate**sp.Rational(p-1,p)*c)==0,'Random bracket Holder bound, not deterministic gradient')
    prev=sp.factorial2(2*p-3) if p>1 else sp.Integer(1)
    check('limiting Gaussian-bound recurrence p='+str(p),sp.simplify(p*(2*p-1)*prev/p-sp.factorial2(2*p-1))==0,'Integrating h^(p-1) retains division by p')
check('even-moment cosh coefficients',all(sp.factorial2(2*p-1)/sp.factorial(2*p)==1/(2**p*sp.factorial(p)) for p in range(1,15)),'No Gaussian law is asserted')
check('dyadic tightness exponent',all(p-1-2*p*((p-1)/(2*p)-.001)>0 for p in range(2,30)),'Every selected gamma is strictly below (p-1)/(2p)')
seriesB=1+2*sum(math.sqrt(r+1)*2**(-r/2) for r in range(1,2000))
upperB=2/(1-2**(-.5))**2-1
check('logarithmic chaining constant',seriesB<upperB,{'series':seriesB,'upper_bound':upperB})
z=.1
check('dyadic logarithmic union bound',abs(sum(2*(2**n)*z**(n+1) for n in range(60))-2*z/(1-2*z))<1e-14,'Requires 2z<1')

# Parameter winding and the explicitly proved unitary generator map.
check('rational winding retains all chosen fixed denominators',all((Fraction(math.factorial(j)*m,n)).denominator==1 for n in range(1,13) for m in [-5,1,7] for j in [12,13,20]),'2 pi j! diverges but every tested rational character equals one')
X=np.diag([-2.,0.,.7,4.]);Id=np.eye(4);resolvent=np.linalg.inv(Id-1j*X)
check('Stone resolvent identity',close(resolvent+resolvent.conj().T,2*resolvent.conj().T@resolvent),'R + R* = 2 R* R')
check('Stone Cayley factor is unitary',close((Id-2*resolvent).conj().T@(Id-2*resolvent),Id),'I - 2 R')
check('Stone generator sign and factors',close(1j*(np.linalg.inv(resolvent)-Id),X),'X = i (R inverse - I), V(t)=exp(i t X)')

# First-energy escape is distinct from Hilbert mass escape.
values=[]
for j in [10,100,1000,10000]:
    K=lambda t:1-1/j+math.exp(-t*j)/j
    values.append(1-K(1))
    check('unit mass and first energy at j='+str(j),abs((1-1/j)+1/j-1)<1e-15 and abs(j/j-1)<1e-15,'Illustrative spectral measures only')
    detector=K(2)-2*K(3)+K(4)
    check('heat detector identity at j='+str(j),abs(detector-(math.exp(-j)-math.exp(-2*j))**2/j)<4e-16,'Keeps the full heat difference')
check('first-energy counterexample heat convergence',values[-1]<values[-2]<values[-3]<values[-4],values)
tail=[(j-7)/j for j in [10,100,1000,10000]]
check('full weighted escape tail approaches one',tail[-1]>tail[-2]>tail[-3]>tail[-4] and tail[-1]>.999,'At each fixed R=7, (lambda-R)+ mass tends to one')

report={'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'proof_sha256':hashlib.sha256((ROOT/'CURVATURE_PHASE_RECONSTRUCTION.md').read_bytes()).hexdigest(),
        'scope':'Bounded pointwise, algebraic, symbolic and source checks. No unknown vacuum distribution or limiting energy weight is assumed.',
        'total':len(checks),'passed':sum(c['passed'] for c in checks),'checks':checks}
(ROOT/'CURVATURE_PHASE_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ['total','passed','proof_sha256']}))
for failure in checks:
    if not failure['passed']: print('FAIL',failure)
raise SystemExit(0 if report['passed']==report['total'] else 1)
