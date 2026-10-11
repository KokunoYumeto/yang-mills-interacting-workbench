from pathlib import Path
import json, math, re
import numpy as np
import sympy as s

root=Path(__file__).resolve().parent
checks=[]
def exact(name, expr):
    assert s.simplify(expr)==0, (name,s.simplify(expr))
    checks.append(name)
def numeric(name, good):
    assert bool(good), name
    checks.append(name)

y,e,F,alpha,J,A,gamma=s.symbols('y e F alpha J A gamma',positive=True)
face=s.symbols('A_1',positive=True)
phi=y/(e+y)
exact('first derivative',s.diff(phi,y)-e/(e+y)**2)
exact('second derivative',s.diff(phi,y,2)+2*e/(e+y)**3)
D=J+2*A
L=s.diff(phi,y)*D+s.diff(phi,y,2)*gamma
exact('second-energy mixed term',L**2-e**2*(D**2/(e+y)**4-4*D*gamma/(e+y)**5+4*gamma**2/(e+y)**6))
exact('gradient maximum critical point',s.diff(y/(e+y)**4,y).subs(y,e/3))
exact('gradient maximum value',(16*F*e**2*y/(e+y)**4).subs(y,e/3)-27*F/(16*e))
exact('Hessian maximum critical point',s.diff(y/(e+y)**3,y).subs(y,e/2))
exact('Hessian composition value',(32*F*e*y/(e+y)**3).subs(y,e/2)-128*F/(27*e))
exact('negative Laplacian maximum',(3*e*y/(e+y)**2).subs(y,e)-s.Rational(3,4))
u,v,w=s.symbols('Sigma_11 Sigma_12 Sigma_22',real=True)
res=s.Matrix([-2*e/(e+y)**3,2*e/(e+y)**2])
sigma=s.Matrix([[u,v],[v,w]])
exact('conditional residual covariance',(res.T*sigma*res)[0]-4*e**2*(u/(e+y)**6-2*v/(e+y)**5+w/(e+y)**4))

for n in range(1,9):
    exact(f'moment algebra {n}',y*phi**n-(y-e*sum(phi**k for k in range(1,n+1))))
    expected=n*phi**(n-1)*s.diff(phi,y,2)
    if n>1:expected+=n*(n-1)*phi**(n-2)*s.diff(phi,y)**2
    exact(f'power second derivative {n}',s.diff(phi**n,y,2)-expected)
    r=(e+y)**(-n)
    actual=s.diff(r,y)*(6*face-3*y)+s.diff(r,y,2)*gamma
    expected=-n*(6*face+3*e)*(e+y)**(-n-1)+3*n*(e+y)**(-n)+n*(n+1)*gamma*(e+y)**(-n-2)
    exact(f'resolvent Laplacian {n}',actual-expected)
    R0,Rn,Rnext,An,Hn=s.symbols('Rprevious Rn Rnext An Hn')
    residual=R0-2*e*Rn+An-alpha*F*s.Rational(1,2)*(-n*(6*face+3*e)*Rnext+3*n*Rn+n*(n+1)*Hn)
    recurrence=R0+An-alpha*F*n*(n+1)*Hn/2+alpha*F*n*(6*face+3*e)*Rnext/2-(2*e+3*n*alpha*F/2)*Rn
    exact(f'resolvent recurrence {n}',residual-recurrence)

ell,P,Q=s.symbols('l P Q',positive=True)
R=2*(Q+P/ell); q=ell**2/(P+Q*ell)
exact('spectral minorant at lower energy',4*ell/R-4*(P+Q*ell)/R**2-q)
numeric('spectral bound monotonic derivative',s.simplify(s.diff(ell**2/(P+Q*ell),ell))==ell*(2*P+Q*ell)/(P+Q*ell)**2)
r,p=s.symbols('r p',positive=True)
delta=s.symbols('delta',nonnegative=True)
exact('lower tail layer cake',s.integrate(2*y*s.exp(-p*y*y/(2*r*r)),(y,0,r))-2*r*r/p*(1-s.exp(-p/2)))
T,V=s.symbols('T V',positive=True)
gaussian=s.integrate(2*y*s.exp(-y*y/(4*V)),(y,0,2*V*T))
tail=s.integrate(2*y*s.exp(-T*y+V*T*T),(y,2*V*T,s.oo))
exact('joined upper root excess',gaussian+tail-(4*V+2/T**2*s.exp(-V*T*T)))
beta,d=s.symbols('beta d',real=True)
cov=d-(e+d)*beta
exact('covariance complement',(e+d)*beta-d+cov)
x,xp=s.symbols('x xp',nonnegative=True)
bp=x/(1+x); bpp=xp/(1+xp)
exact('variance comparison exact difference',bp-bpp-(x-xp)/((1+x)*(1+xp)))

# These bounded numerical fixtures test algebra and inequalities only.
# They are not samples or replacement laws for the Yang--Mills vacuum.
rng=np.random.default_rng(20261011)
max_error=0.0
for case in range(120):
    ev=float(10**rng.uniform(-1,3)); fv=float(rng.uniform(.01,3))
    yy=np.linspace(0,10*ev,301)
    numeric(f'gradient bound grid {case}',np.max(16*fv*ev**2*yy/(ev+yy)**4)<=27*fv/(16*ev)*(1+1e-12))
    xv=rng.uniform(0,3,128); rv=rng.uniform(0,2,128); err=np.abs(xv+rv-1)
    numeric(f'potential clipping receiver {case}',np.all(np.maximum(xv-1,0)<=err+1e-14))
    numeric(f'retained clipping receiver {case}',np.all(np.abs(rv-(1-np.minimum(xv,1)))<=err+1e-14))
    # Singular original-word Gram fixture: last word is a linear combination.
    words=rng.normal(size=(8,3))+1j*rng.normal(size=(8,3))
    words=np.column_stack((words,words[:,0]+2*words[:,1]))
    vv=rng.normal(size=8)+1j*rng.normal(size=8)
    gram=words.conj().T@words; k=words.conj().T@vv
    projection=words@np.linalg.pinv(gram)@words.conj().T
    lhs=float(np.real(k.conj()@np.linalg.pinv(gram)@k)); rhs=float(np.linalg.norm(projection@vv)**2)
    max_error=max(max_error,abs(lhs-rhs))
    numeric(f'singular Gram visibility {case}',abs(lhs-rhs)<2e-10)
    # Exact finite-dimensional compression-defect identity.
    vals=rng.uniform(.2,.45,8); B=np.diag(vals)
    C=projection@B@projection; K=(np.eye(8)-projection)@B@projection
    defect=projection@B@B@projection-C@C
    dif=float(np.linalg.norm(defect-K.conj().T@K));max_error=max(max_error,dif)
    numeric(f'positive compression defect {case}',dif<1e-10 and np.linalg.eigvalsh((defect+defect.conj().T)/2).min()>-1e-10)
    rho=float(rng.uniform(.05,.49)); samples=rng.uniform(rho,1-rho,37)
    weights=rng.uniform(.1,1,37);weights/=weights.sum(); bs=samples/(1+samples)
    varx=float(weights@samples**2-(weights@samples)**2)
    varb=float(weights@bs**2-(weights@bs)**2)
    covbx=float(weights@(bs*samples)-(weights@bs)*(weights@samples))
    numeric(f'refined variance interval {case}',varx/(2-rho)**4-1e-13<=varb<=varx/(1+rho)**4+1e-13)
    numeric(f'retained covariance interval {case}',(1+rho)**2*varb-1e-13<=covbx<=(2-rho)**2*varb+1e-13)

proof=(root/'BOUNDED_MULTIPLIER_RECEIVING.md').read_text(encoding='utf-8')
from bounded_receiving_reference_check import rename_numbered_references
numeric('prefix preserves actual multiplication',rename_numbered_references(r'\Phi(BM), BM20, \tag{BM20}')==r'\Phi(BM), IB20, \tag{IB20}')
numeric('actual compressed product serialization',r'\Phi(BM)=B|' in proof and r'\Phi(IB)' not in proof)
numeric('mixed residual density serialization',r'\int d_r^*\Sigma d_s\,p\,dy' in proof and 'd_s,p' not in proof)
numeric('original energy coefficient serialization',r'\mathfrak e\,XW\Omega' in proof and r'\mathfrak e,XW' not in proof)
numeric('equation sequence',re.findall(r'\\tag\{(IB\d+)\}',proof)==[f'IB{i}' for i in range(1,47)])
numeric('display delimiters',proof.count('\\[')==proof.count('\\]'))
numeric('inline delimiters',proof.count('\\(')==proof.count('\\)'))
numeric('no control characters',not any(ord(c)<32 and c not in '\r\n\t' for c in proof))
numeric('word restriction',re.search(r'\bplain\b',proof,re.I) is None)
result={'status':'passed','check_count':len(checks),'max_numerical_identity_error':max_error,'checks':checks,'scope':'Symbolic original coefficients and bounded algebra fixtures, not a numerical ground-state simulation'}
(root/'BOUNDED_RECEIVING_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
