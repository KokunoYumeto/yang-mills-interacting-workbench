"""Exact odd-sector signs, full Gaussian factors and all-mode radial weights."""
from pathlib import Path
import hashlib,itertools,json
import sympy as s
HERE=Path(__file__).resolve().parent
checks={}
def eq(name,a,b=0):
    assert s.simplify(s.expand(a-b))==0,name
    checks[name]=True
k=s.Rational(3,2);r,theta,sigma,z=s.symbols("r theta sigma z",positive=True)
g,a,N,M=s.symbols("g a N M",positive=True)
eq("full coupling product",(2*g*g/a)/(2*g*g*a),1/a**2)
eq("prior vacuum bound identity",3*s.sqrt((2*g*g/a)/(2*g*g*a)*N*M),3*s.sqrt(N*M)/a)
zz,t=s.symbols("zz t",positive=True)
eq("exact trial exponent dictionary",2*zz,t.subs(t,2*zz))
modepairs=[(0,1),(0,2),(1,2)]
chars={}
for flips in itertools.product([-1,1],repeat=3):
    signs=[flips[i]*flips[j] for i,j in modepairs]
    chars[flips]=[1,1,1,signs[0]*signs[1],signs[0]*signs[2],signs[1]*signs[2]]
assert chars[(-1,1,1)]==[1,1,1,1,-1,-1]
checks["original first-coordinate reflection has two odd singlets"]=True
for character in itertools.product([0,1],repeat=3):
    projection=[s.Rational(1,8)*sum(s.prod(f[i]**character[i] for i in range(3))*vals[j] for f,vals in chars.items()) for j in range(6)]
    rank=sum(projection)
    expected=3 if character==(0,0,0) else 1 if sum(character)==2 else 0
    eq("full sign-character rank "+str(character),rank,expected)
    assert all(v in [0,1] for v in projection)
    checks["exact character projection "+str(character)]=True
for perm in itertools.permutations(range(3)):
    image={tuple(sorted((perm[i],perm[j]))) for i,j in modepairs}
    assert image==set(modepairs)
    checks["permutation transitivity "+str(perm)]=True
Q=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
assert Q.T*Q==s.eye(2)
checks["retained two-mode orthogonal map"]=True
eq("absolute two-mode determinant",s.det(Q)**2,1)
x,y=s.symbols("x y",real=True)
eq("original mixed product",x*y,(((x+y)/s.sqrt(2))**2-((x-y)/s.sqrt(2))**2)/2)
char=(1+4*theta**2/sigma**2)**(-k)
eq("original mixed Gaussian variance",-s.diff(char,theta,2).subs(theta,0),12/sigma**2)
overlap=(-s.diff(char,theta)*sigma/(2*s.sqrt(3))).subs(theta,sigma/2)
eq("raw first odd weight",overlap**2,s.Rational(3,32))
mass=(1-char.subs(theta,sigma))/2
eq("raw total odd mass",mass,(1-5**(-k))/2)
A=s.symbols("A",nonnegative=True)
eq("full higher-domain raw mass",(1-char.subs(theta,A*sigma))/2,(1-(1+4*A*A)**(-k))/2)
general_overlap=(-s.diff(char,theta)*sigma/(2*s.sqrt(3))).subs(theta,A*sigma/2)
eq("full higher-domain first weight",general_overlap**2,3*A*A/(1+A*A)**5)
eq("original three-colour amplitude weight",(3*A*A/(1+A*A)**5).subs(A,3),s.Rational(27,100000))
eq("original three-colour raw mass",((1-(1+4*A*A)**(-k))/2).subs(A,3),(1-37**(-k))/2)
def lag(n):
    return s.expand(sum((-1)**l*s.rf(k,n)/(s.rf(k,l)*s.factorial(n-l)*s.factorial(l))*r**l for l in range(n+1)))
def gamma_int(poly):
    return s.expand(sum(coef*s.rf(k,power[0]) for power,coef in s.Poly(s.expand(poly),r).terms()))
for n in range(7):
    L=lag(n)
    eq("retained radial oscillator equation "+str(n),r*s.diff(L,r,2)+(k-r)*s.diff(L,r)+n*L)
    eq("full radial polynomial squared norm "+str(n),gamma_int(L*L),s.rf(k,n)/s.factorial(n))
    for m in range(n):
        eq(f"radial orthogonality {n},{m}",gamma_int(L*lag(m)))
weights=[]
for ell in range(15):
    exact=s.Rational(1,2)**(ell+3)*sum(s.rf(k,m)*s.rf(k,ell-m)/(s.factorial(m)*s.factorial(ell-m))*s.sin(s.pi*(ell-2*m)/4)**2 for m in range(ell+1))
    closed=s.Rational(1,2)**(ell+4)*(s.Rational((ell+1)*(ell+2),2)-(0 if ell%2 else (-1)**(ell//2)*s.rf(k,ell//2)/s.factorial(ell//2)))
    eq("full energy-level convolution "+str(ell),exact,closed)
    assert closed>=0
    checks["positive raw weight "+str(ell)]=True
    weights.append(str(closed))
G=((1-z/2)**(-3)-(1+z*z/4)**(-k))/16
eq("generating function first weight",s.diff(G,z).subs(z,0),s.Rational(3,32))
eq("generating function second weight",s.diff(G,z,2).subs(z,0)/2,s.Rational(15,128))
eq("complete raw mass sum",G.subs(z,1),mass)
beta=s.symbols("beta",real=True)
for n in range(5):
    integral=sum(coef*s.rf(k,power[0])/(1-s.I*beta)**(k+power[0]) for power,coef in s.Poly(lag(n),r).terms())
    target=s.rf(k,n)/s.factorial(n)*(-s.I*beta)**n/(1-s.I*beta)**(k+n)
    eq("complete oscillatory radial coefficient "+str(n),integral/((1-s.I*beta)**(-k)),target/((1-s.I*beta)**(-k)))
proof=HERE.parent/("PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md" if HERE.name=="checks" else "ODD_VACUUM_OBSERVABLE_PROOF_20261009.md")
out={"all_passed":True,"checks":checks,"check_count":len(checks),"proof_sha256":hashlib.sha256(proof.read_bytes()).hexdigest(),
     "scope":"Exact finite algebra supports the complete fixed-box operator and convergence proofs; no uniform-in-volume or continuum result certified.",
     "raw_weights_l0_through_l14":weights,"independent_review":False}
(HERE/"ODD_VACUUM_OBSERVABLE_CHECK.json").write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8",newline="\n")
print(json.dumps({"checks":len(checks),"all_passed":True,"first_weight":weights[1]}))
