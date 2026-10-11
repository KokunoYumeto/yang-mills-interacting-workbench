from pathlib import Path
import sympy as s
import itertools,json,re,hashlib,datetime

root=Path(__file__).parent
checks=[]
def test(name,statement):
    assert statement,name
    checks.append(name)

# The complete degree-four numerator Gram matrix, including all even terms.
G=s.Matrix(5,5,lambda i,j: s.Rational(2,i+j+1) if (i+j)%2==0 else 0)
test("coefficient functional 75/8",G.inv()[1,1]==s.Rational(75,8))
for k in range(1,6):
    test("positive Gram principal minor "+str(k),G[:k,:k].det()>0)
y=s.symbols('y')
test("Legendre derivative sum",sum(s.Rational(2*l+1,2)*s.diff(s.legendre(l,y),y).subs(y,0)**2 for l in range(5))==s.Rational(75,8))

# Every frequency allowed by physical degree two, including affine terms.
z=s.symbols('z',real=True)
a=s.symbols('a0:5')
trig_rational=a[0]+a[1]*(1-z*z)/(1+z*z)+a[2]*2*z/(1+z*z)+a[3]*(1-6*z*z+z**4)/(1+z*z)**2+a[4]*4*z*(1-z*z)/(1+z*z)**2
P=s.cancel(trig_rational*(1+z*z)**2)
test("complete stereographic numerator degree",s.Poly(P,z).degree()<=4)
test("derivative factor four",s.diff(P,z).subs(z,0)==2*a[2]+4*a[4])

# Exact noncommuting SU(2) matrices verify every subtree endpoint pattern.
I=s.I
sigma=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.Matrix([[1,0],[0,-1]])]
def quaternion(c,v):
    return c*s.eye(2)-I*sum((v[i]*sigma[i] for i in range(3)),s.zeros(2))
U=quaternion(s.Rational(1,3),[s.Rational(2,3),s.Rational(2,3),0])
V=quaternion(s.Rational(2,3),[s.Rational(1,3),0,s.Rational(2,3)])
C=quaternion(s.Rational(3,5),[0,s.Rational(4,5),0])
for label,M in [('U',U),('V',V),('C',C)]:
    test(label+" unit determinant",s.simplify(M.det())==1)
    test(label+" unitary",s.simplify(M*M.conjugate().T)==s.eye(2))
for orientation in [1,-1]:
    Q=C**orientation
    for es,et,eu,ew in itertools.product([0,1],repeat=4):
        Uvar=Q**es*U*Q**(-et); Vvar=Q**eu*V*Q**(-ew)
        plus=(Uvar*Vvar).trace()
        minus=(Uvar*Vvar.inv()).trace()
        rhsplus=(U*Q**(eu-et)*V*Q**(es-ew)).trace()
        rhsminus=(U*Q**(ew-et)*V.inv()*Q**(es-eu)).trace()
        test("full trace plus "+str((orientation,es,et,eu,ew)),s.simplify(plus-rhsplus)==0)
        test("full trace minus "+str((orientation,es,et,eu,ew)),s.simplify(minus-rhsminus)==0)

# Face multiplicities include every boundary edge.
m,xi=s.symbols('m xi',positive=True)
counts={2:12*m,3:12*m*(m-1),4:3*m*(m-1)**2}
N=3*m*(m+1)**2; M=3*m*m*(m+1)
test("all edges counted",s.expand(sum(counts.values())-N)==0)
test("all face incidences counted",s.expand(sum(r*c for r,c in counts.items())-4*M)==0)
test("squared incidences",s.expand(sum(r*r*c for r,c in counts.items())-12*m*(4*m*m+m-1))==0)
test("polynomial quotient bound",s.expand(sum(c*(1+4*r*xi)**2 for r,c in counts.items())-(N+32*xi*M+192*xi*xi*m*(4*m*m+m-1)))==0)

# Coefficients retain the factor three for colour and all path factors.
test("path coefficient",3*24*s.Rational(75,16)*160000**2==8640000000000)
test("older occurrence constant",(12*(64*s.sqrt(5)+96*s.sqrt(2))**2).expand()==(12288*(38+12*s.sqrt(10))).expand())

# Response-square algebra, with no exchange of inequality directions.
mass,T,energy,t=s.symbols('mass T energy t',nonzero=True)
def energy_square(alpha): return energy-2*alpha*mass+alpha**2*T
test("response Schur defect",s.simplify(energy_square(mass/T)-(energy-mass**2/T))==0)
test("endpoint square",s.simplify(T/(4*t)-t*energy_square(1/(2*t))-(mass-t*energy))==0)
for l1,l2,lk in [(1,3,10),(2,5,100),(3,4,1000)]:
    t0=s.Rational(l2-l1,2*l2)
    ak=t0*(s.Rational(1,l2)-s.Rational(1,lk))/(s.Rational(1,l1)-s.Rational(1,l2))
    test("fibre coefficients "+str(lk),1+ak>0 and 1-t0-ak>=s.Rational(1,2))
    test("fibre mass "+str(lk),s.simplify(1+ak+1-t0-ak+t0)==2)
    test("fibre response "+str(lk),s.simplify((1+ak)/l1+(1-t0-ak)/l2+t0/lk-s.Rational(1,l1)-s.Rational(1,l2))==0)

doc=(root/'PHASE_RESPONSE_AND_ENDPOINT.md').read_text(encoding='utf-8')
tags=re.findall(r'\\tag\{(PRE\d+)\}',doc)
test("55 unique equation labels",len(tags)==len(set(tags))==55)
test("display math paired",doc.count(r'\[')==doc.count(r'\]'))
test("inline math paired",doc.count(r'\(')==doc.count(r'\)'))
test("author prose banned word absent",not re.search(r'\bplain\b',doc,re.I))
for name,path,expected in [
    ('completed physical source',root/'GLOBAL_PHYSICAL_RESPONSE.md','1ea5157e2b89b82a1810f65507e771a38da47b8270e49d4f45d09c12b3336aee'),
    ('completed union source',root/'union_label_global'/'FULL_UNION_LABEL_INVERSE.md','f162555e2e1f348eae36705b9a8f07798e6173520a44e24ba48975d6a29ed19f')
]:
    test(name+" unchanged",hashlib.sha256(path.read_bytes()).hexdigest()==expected)

result={'observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks_passed':len(checks),'checks':checks,'labels':tags,'inline_pairs':doc.count(r'\('),'display_pairs':doc.count(r'\['),'C2_decimal':str(s.N(s.Rational(75,4)*s.E*(s.Rational(17,16))**5,16)),'source_sha256':hashlib.sha256(doc.encode()).hexdigest(),'scope':'Exact algebra and source integrity checks; no numerical vacuum or spectral approximation is claimed.'}
(root/'PHASE_RESPONSE_CHECKS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['checks','labels']},indent=2))
