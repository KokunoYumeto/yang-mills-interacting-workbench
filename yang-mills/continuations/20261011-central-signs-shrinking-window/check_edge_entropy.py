from pathlib import Path
import sympy as s
import json,re,hashlib,datetime

root=Path(__file__).parent
checks=[]
def test(name,statement):
    assert statement,name
    checks.append(name)

I=s.I
sigma=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.Matrix([[1,0],[0,-1]])]
T=[-I*A/2 for A in sigma]
test("original Ito correction",sum((A*A for A in T),s.zeros(2))==-s.Rational(3,4)*s.eye(2))
for a in range(3):
    for b in range(3):
        test("original metric "+str((a,b)),s.simplify(-2*(T[a]*T[b]).trace())==int(a==b))

# A rotation about the third original Lie generator; covariance and fixed axis.
theta=s.symbols('theta',real=True)
R=s.Matrix([[s.cos(theta),-s.sin(theta),0],[s.sin(theta),s.cos(theta),0],[0,0,1]])
v=s.Matrix([0,0,1])
test("adjoint noise covariance",s.simplify(R*R.T)==s.eye(3))
test("fixed directional noise",s.simplify(R.T*v)==v)
test("determinant of adjoint rotation",s.simplify(R.det())==1)

kappa,t,eps,tau,beta,omega,M=s.symbols('kappa t eps tau beta omega M',positive=True)
shift=eps/(s.sqrt(2*kappa)*t)
test("Girsanov drift cancellation",s.simplify(s.sqrt(2*kappa)*shift-eps/t)==0)
test("quadratic variation compensator",s.simplify(shift**2*t/2-eps**2/(4*kappa*t))==0)
time=s.symbols('time',real=True)
test("potential derivative time weight",s.integrate(1-time/t,(time,0,t))==t/2)
test("conditional Gaussian mean scale",s.simplify(s.sqrt(2*t*(omega+4*kappa*beta*t))/(s.sqrt(2*kappa)*t)-s.sqrt(omega/(kappa*t)+4*beta))==0)

c=s.symbols('c',positive=True)
Phi=(2*s.pi/c+4)/(1-c/2)**2
expected=(4*c*c+3*s.pi*c-2*s.pi)/(c*c*(1-c/2)**3)
test("exact optimizing derivative",s.simplify(s.diff(Phi,c)-expected)==0)
cstar=(s.sqrt(9*s.pi**2+32*s.pi)-3*s.pi)/8
test("positive critical root equation",s.simplify(4*cstar**2+3*s.pi*cstar-2*s.pi)==0)
test("critical root in allowed interval",0<float(cstar)<2)
test("simple c=1/2 constant",s.simplify(Phi.subs(c,s.Rational(1,2))-s.Rational(64,9)*(1+s.pi))==0)
test("optimized constant improves simple constant",float(Phi.subs(c,cstar))<float(Phi.subs(c,s.Rational(1,2))))
test("proposed separate oscillation substitution",s.simplify(s.sqrt((4*s.pi*s.sqrt(beta))/(2/s.sqrt(beta))+4*beta)+(2/s.sqrt(beta))*beta/2-(1+s.sqrt(4+2*s.pi))*s.sqrt(beta))==0)

# Entropy optimization is the exact Gaussian variational calculation.
entropy,lam=s.symbols('entropy lam',positive=True)
gaussian_bound=entropy/lam+lam*t/2
test("Gaussian entropy optimizer",s.simplify(gaussian_bound.subs(lam,s.sqrt(2*entropy/t))-s.sqrt(2*t*entropy))==0)

# Every old boundary count and the new path constant remain explicit.
m=s.symbols('m',positive=True)
counts={2:12*m,3:12*m*(m-1),4:3*m*(m-1)**2}
test("face incidence receiving sum",s.expand(sum(r*n for r,n in counts.items())-12*m*m*(m+1))==0)
test("new j14 quotient coefficient",3*24*s.Rational(75,16)*40000==13500000)

doc=(root/'CONDITIONAL_EDGE_ENTROPY_AND_SCORE.md').read_text(encoding='utf-8')
tags=re.findall(r'\\tag\{(ESE\d+)\}',doc)
test("38 unique equation labels",len(tags)==len(set(tags))==38)
test("display delimiters paired",doc.count(r'\[')==doc.count(r'\]'))
test("inline delimiters paired",doc.count(r'\(')==doc.count(r'\)'))
test("banned prose word absent",not re.search(r'\bplain\b',doc,re.I))
unchanged=[
    (root/'GLOBAL_PHYSICAL_RESPONSE.md','1ea5157e2b89b82a1810f65507e771a38da47b8270e49d4f45d09c12b3336aee'),
    (root/'union_label_global'/'FULL_UNION_LABEL_INVERSE.md','f162555e2e1f348eae36705b9a8f07798e6173520a44e24ba48975d6a29ed19f'),
    (root/'PHASE_RESPONSE_AND_ENDPOINT.md','96e09c038d938125a2223c68a537696433fc1c61eecbfe2793be5a3e27ccaba0')
]
for path,sha in unchanged:test("stable "+path.name,hashlib.sha256(path.read_bytes()).hexdigest()==sha)

result={'observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks_passed':len(checks),'checks':checks,'equation_labels':tags,'inline_pairs':doc.count(r'\('),'display_pairs':doc.count(r'\['),'constants':{'c_star':str(s.N(cstar,18)),'C_psi_optimized':str(s.N(s.sqrt(Phi.subs(c,cstar)),18)),'C_rho_optimized':str(s.N(2*s.sqrt(Phi.subs(c,cstar)),18)),'C_rho_simple':str(s.N(s.Rational(16,3)*s.sqrt(1+s.pi),18)),'proposed_constant_not_used':str(s.N(2+2*s.sqrt(4+2*s.pi),18))},'source_sha256':hashlib.sha256(doc.encode()).hexdigest(),'scope':'Exact constants, signs, covariance, optimization and source-integrity checks. The stochastic law and entropy proofs are in the complete note; no stochastic simulation is used.'}
(root/'EDGE_ENTROPY_CHECKS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['checks','equation_labels']},indent=2))
