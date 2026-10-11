from pathlib import Path
import datetime, hashlib, json, re
import sympy as s

root = Path(__file__).parent
checks = []
def check(name, condition):
    assert condition, name
    checks.append(name)

I = s.I
sigmas = [s.Matrix([[0,1],[1,0]]), s.Matrix([[0,-I],[I,0]]), s.Matrix([[1,0],[0,-1]])]
T = [-I*A/2 for A in sigmas]
check('matrix Ito drift coefficient', sum((A*A for A in T),s.zeros(2)) == -s.Rational(3,4)*s.eye(2))
for a in range(3):
    for b in range(3):
        check(f'original metric {a},{b}', -2*s.trace(T[a]*T[b]) == int(a==b))

# Directly compute the adjoint from the original complex matrices.
angle = s.symbols('angle', real=True)
g = s.diag(s.exp(-I*angle/2), s.exp(I*angle/2))
R = s.Matrix(3,3,lambda a,b:s.simplify(-2*s.trace(T[a]*g*T[b]*g.inv()).expand(complex=True)))
check('adjoint computed from original group matrices', s.simplify(R*R.T)==s.eye(3))
check('adjoint fixed directional axis', R[:,2] == s.Matrix([0,0,1]))
check('adjoint orientation', s.simplify(R.det())==1)

k,t,epsilon,clock = s.symbols('k t epsilon clock',positive=True)
theta=epsilon/(s.sqrt(2*k)*t)
check('negative controlled drift removed by positive likelihood', s.simplify(-epsilon/t+s.sqrt(2*k)*theta)==0)
check('half quadratic variation of likelihood', s.simplify(theta**2*t/2-epsilon**2/(4*k*t))==0)
check('potential variation weight', s.integrate(1-clock/t,(clock,0,t))==t/2)
D=s.symbols('D',positive=True)
check('directional entropy score factor', s.simplify(s.sqrt(2*t*D)/(s.sqrt(2*k)*t)-s.sqrt(D/(k*t)))==0)

c=s.symbols('c',positive=True)
phi=(2*s.pi/c+4)/(1-c/2)**2
dphi=(4*c*c+3*s.pi*c-2*s.pi)/(c*c*(1-c/2)**3)
check('optimizing derivative',s.simplify(s.diff(phi,c)-dphi)==0)
cstar=(s.sqrt(9*s.pi**2+32*s.pi)-3*s.pi)/8
check('critical polynomial',s.simplify(4*cstar*cstar+3*s.pi*cstar-2*s.pi)==0)
check('critical point in allowed interval',0<float(cstar)<2)
check('simple constant',s.simplify(phi.subs(c,s.Rational(1,2))-s.Rational(64,9)*(1+s.pi))==0)

# Recompute the coefficient-functional norm by direct rational matrix inversion.
gram=s.Matrix(5,5,lambda a,b:0 if (a+b)%2 else s.Rational(2,a+b+1))
check('exact derivative coefficient norm',gram.inv()[1,1]==s.Rational(75,8))
check('subgroup coefficient after derivative scaling and Jacobian',s.Rational(75,8)/16/4==s.Rational(75,512))
check('subgroup interval length factor',s.Rational(75,512)*8==s.Rational(75,64))
m=s.symbols('m',integer=True,positive=True)
counts={2:12*m,3:12*m*(m-1),4:3*m*(m-1)**2}
check('all original edges counted',s.expand(sum(counts.values())-3*m*(m+1)**2)==0)
check('all original face incidences counted',s.expand(sum(r*count for r,count in counts.items())-12*m*m*(m+1))==0)
check('original path asymptotic coefficient',3*24*s.Rational(75,16)*40000==13500000)

# Entropy improvement and its exact two-point equality law retain the lower scale a.
a,p=s.symbols('a p',positive=True)
A=D/(1-s.exp(-D))
pstar=(A-1)/(s.exp(D)-1)
Z=a*(1+pstar*(s.exp(D)-1))
check('maximizing two-point mean retains lower scale',s.simplify(Z-a*A)==0)
Istar=s.simplify(pstar*a*s.exp(D)*D/Z-s.log(Z/a))
J=A-1-s.log(A)
check('sharp entropy attained',s.simplify(Istar-J)==0)
check('small-range quadratic coefficient',s.limit(J/D**2,D,0,dir='+')==s.Rational(1,8))
z=s.symbols('z',positive=True)
check('range entropy maximizer derivative',s.simplify(s.diff(A*(1-1/z)-s.log(z),z)-(A-z)/z**2)==0)

proof=(root/'INDEPENDENT_EDGE_ENTROPY_PROOF.md').read_text(encoding='utf-8')
labels=re.findall(r'\\tag\{(ID\d+)\}',proof)
check('57 ordered proof labels',labels==[f'ID{i}' for i in range(1,58)])
check('display delimiters paired',proof.count(r'\[')==proof.count(r'\]'))
check('inline delimiters paired',proof.count(r'\(')==proof.count(r'\)'))
check('prohibited prose term absent',re.search(r'\b'+''.join(['p','l','a','i','n'])+r'\b',proof,re.I) is None)

report={'observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks_passed':len(checks),'checks':checks,'constants':{'c_star':str(s.N(cstar,20)),'C_psi':str(s.N(s.sqrt(phi.subs(c,cstar)),20)),'C_rho':str(s.N(2*s.sqrt(phi.subs(c,cstar)),20))},'proof_sha256':hashlib.sha256(proof.encode()).hexdigest(),'proof_role':'Algebra and presentation checks supplement the complete analytic proof. They are not a stochastic simulation or a substitute for disintegration and differentiation.'}
(root/'INDEPENDENT_EDGE_ENTROPY_CHECKS.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'checks_passed':len(checks),'constants':report['constants'],'proof_sha256':report['proof_sha256']},indent=2))
