"""Independent exact Gram checks and original-word receiving checks for PC1-PC52."""
from pathlib import Path
from fractions import Fraction as Fr
from itertools import product
from collections import Counter
from functools import lru_cache
from datetime import datetime, timezone
import ast, hashlib, json, math, random, re
import mpmath as mp

ROOT=Path(__file__).resolve().parent
mp.mp.dps=65
checks=[]

def passed(name,**metadata):
    checks.append({'name':name,'passed':True,**metadata})

def moment1(power):
    return Fr(0) if power%2 else Fr(1,power+1)

def mulpoly(a,b):
    out={}
    for p,c in a.items():
        for q,d in b.items():
            k=tuple(x+y for x,y in zip(p,q))
            out[k]=out.get(k,Fr(0))+c*d
    return {k:v for k,v in out.items() if v}

def addpoly(a,b):
    out=dict(a)
    for k,v in b.items():out[k]=out.get(k,Fr(0))+v
    return {k:v for k,v in out.items() if v}

def polynomial_value(poly,point):
    return sum(c*math.prod(x**n for x,n in zip(point,p)) for p,c in poly.items())

legendre=[
    [Fr(1)],
    [Fr(0),Fr(1)],
    [Fr(-1,2),Fr(0),Fr(3,2)],
    [Fr(0),Fr(-3,2),Fr(0),Fr(5,2)],
    [Fr(3,8),Fr(0),Fr(-30,8),Fr(0),Fr(35,8)],
]
for i,p in enumerate(legendre):
    for j,q in enumerate(legendre):
        actual=sum(c*d*moment1(a+b) for a,c in enumerate(p) for b,d in enumerate(q))
        assert actual==(Fr(1,2*i+1) if i==j else 0)
passed('PC7 exact rational orthogonality of all 25 Legendre pairs')
t=[(2*i+1)*sum(c*c for c in p) for i,p in enumerate(legendre)]
assert t==[Fr(1),Fr(3),Fr(25,2),Fr(119,2),Fr(9603,32)]
passed('PC8 all five coefficient squared norms',values=[str(x) for x in t])

indices=sorted((p for p in product(range(5),repeat=3) if sum(p)<=4),
               key=lambda p:(sum(p),p))
assert len(indices)==35
G=[[math.prod(moment1(a+b) for a,b in zip(p,q)) for q in indices] for p in indices]
aug=[list(row)+[Fr(i==j) for j in range(35)] for i,row in enumerate(G)]
for i in range(35):
    pivot=aug[i][i];assert pivot>0
    aug[i]=[x/pivot for x in aug[i]]
    for j in range(35):
        if i==j:continue
        factor=aug[j][i]
        if factor:aug[j]=[x-factor*y for x,y in zip(aug[j],aug[i])]
inverse=[row[35:] for row in aug]
trace=sum(inverse[i][i] for i in range(35))
assert trace==Fr(105041,32)
assert all(sum(G[i][k]*inverse[k][j] for k in range(35))==int(i==j)
           for i in range(35) for j in range(35))
passed('PC9-PC11 independently inverted exact 35 by 35 cube Gram',
       inverse_trace=str(trace),verified_inverse_entries=35**2)

# Exact stereographic numerator for every original ambient basis monomial.
one={(0,0,0):Fr(1)}
r2={(2,0,0):Fr(1),(0,2,0):Fr(1),(0,0,2):Fr(1)}
den=addpoly(one,r2)
num0=addpoly(one,{p:-c for p,c in r2.items()})
nums=[num0,{(1,0,0):Fr(2)},{(0,1,0):Fr(2)},{(0,0,1):Fr(2)}]
basis4=sorted((p for p in product(range(3),repeat=4) if sum(p)<=2),
              key=lambda p:(sum(p),p))
Qmap=[]
for exponent in basis4:
    numerator=one
    for i,power in enumerate(exponent):
        for _ in range(power):numerator=mulpoly(numerator,nums[i])
    for _ in range(2-sum(exponent)):numerator=mulpoly(numerator,den)
    Qmap.append(numerator)
    for y in ((Fr(0),Fr(0),Fr(0)),(Fr(1,3),Fr(-2,5),Fr(3,7)),
              (Fr(4),Fr(-3),Fr(2))):
        d=polynomial_value(den,y)
        x=[polynomial_value(n,y)/d for n in nums]
        expected=math.prod(x[i]**exponent[i] for i in range(4))
        assert polynomial_value(numerator,y)/d**2==expected
passed('PC12 exact coordinate comparison for all 15 ambient monomials')
relation=mulpoly(den,den)
for num in nums:relation=addpoly(relation,{p:-c for p,c in mulpoly(num,num).items()})
assert not relation
passed('PC12 exact sphere relation retained in the numerator map')
for y in ((Fr(1,3),Fr(-2,5),Fr(3,7)),(Fr(4),Fr(-3),Fr(2))):
    v=sum(x*x for x in y)
    monomial_sum=sum(math.prod(x**(2*p) for x,p in zip(y,alpha)) for alpha in indices)
    assert monomial_sum<=sum(v**d for d in range(5))<=(1+v)**4
passed('PC13 exact coefficient-to-original-value comparison at rational chart points')

cap=mp.cos(mp.mpf(1)/4)**14/(1024*105041*mp.pi*mp.mpf(3)**(mp.mpf(9)/2))
cq=mp.mpf(4)/(5*mp.e**2)*(mp.mpf(23)/24)**4
assert Fr(9,16)*2**37>1024*105041*4*162
assert 64*Fr(23,24)**4>45
assert cap>mp.mpf(2)**-37 and cq>mp.mpf(1)/16
passed('PC5 and PC25 exact dyadic inequalities',
       cap_constant=str(cap),q_relative_constant=str(cq))

def rising(a,n):
    return math.prod((a+k for k in range(n)),start=Fr(1))

def sphere_moment(power,dimension):
    if any(p%2 for p in power):return Fr(0)
    half=[p//2 for p in power]
    return math.prod((rising(Fr(1,2),p) for p in half),start=Fr(1))/rising(Fr(dimension,2),sum(half))

# A complete independent 14-dimensional cap Gram, with all affine terms.
basis14=[{(0,0,0,0):Fr(1)}]
for i in range(4):
    a=[0]*4;a[i]=1;basis14.append({tuple(a):Fr(1)})
for i in range(3):
    a=[0]*4;a[i]=2
    basis14.append({tuple(a):Fr(1),(0,0,0,0):Fr(-1,4)})
for i in range(4):
    for j in range(i+1,4):
        a=[0]*4;a[i]=a[j]=1;basis14.append({tuple(a):Fr(1)})
assert len(basis14)==14
def integrate_product(p,q,moment):
    total=0
    for x,c in p.items():
        for y,d in q.items():
            value=moment(tuple(a+b for a,b in zip(x,y)));coefficient=c*d
            total+=coefficient*value if isinstance(value,Fr) else mp.mpf(coefficient.numerator)/coefficient.denominator*value
    return total
def as_mpf(value):
    return mp.mpf(value.numerator)/value.denominator if isinstance(value,Fr) else mp.mpf(value)
H=mp.matrix([[as_mpf(integrate_product(p,q,lambda a:sphere_moment(a,4)))
              for q in basis14] for p in basis14])
for radius in (mp.mpf(1),mp.mpf('.5'),mp.mpf('.1'),mp.mpf('.02')):
    theta=radius/2
    radial_den=mp.quad(lambda z:mp.sin(z)**2,[0,theta])
    @lru_cache(None)
    def cap_moment(power):
        if any(p%2 for p in power[1:]):return mp.mpf(0)
        angular=sphere_moment(power[1:],3)
        angular=mp.mpf(angular.numerator)/angular.denominator
        radial=mp.quad(lambda z:mp.cos(z)**power[0]*mp.sin(z)**(sum(power[1:])+2),[0,theta])
        return angular*radial/radial_den
    M=mp.matrix([[integrate_product(p,q,cap_moment) for q in basis14] for p in basis14])
    eigenvalues=mp.eigsy(M-cap*radius**8*H,eigvals_only=True)
    assert eigenvalues[0]>0
    passed(f'PC16 complete 14-dimensional cap Gram at radius {radius}',
           least_eigenvalue_of_difference=str(eigenvalues[0]))

for B in (mp.mpf(0),mp.mpf('.1'),mp.mpf(1),mp.mpf(2),mp.mpf(8),
          mp.mpf(100),mp.mpf(10)**6):
    r=2/(B+2)
    assert mp.exp(-B*r)*r**8 >= (1+B)**-8*(1-mp.mpf('1e-60'))
    optimized=mp.exp(-B) if B<=8 else (8/(mp.e*B))**8
    assert optimized>=(1+B)**-8
    rq=1 if B<=2 else 2/B
    assert mp.exp(-B*rq)*rq**2>=4/mp.e**2*(1+B)**-2
passed('PC18-PC19 and PC25 radii and uniform constants across score regimes')

I2=mp.quad(lambda u:u**2*mp.exp(-mp.sqrt(1+u*u)),[0,1,8,mp.inf])
I4=mp.quad(lambda u:u**4*mp.exp(-mp.sqrt(1+u*u)),[0,1,8,mp.inf])
I10=mp.quad(lambda u:u**10*mp.exp(-mp.sqrt(1+u*u)),[0,1,8,mp.inf])
for B in (mp.mpf(1),mp.mpf(4),mp.mpf(16),mp.mpf(64)):
    top=4*B
    intervals=sorted(set([mp.mpf(0),mp.mpf(1),min(mp.mpf(8),top),min(mp.mpf(40),top),top]))
    radial=lambda u:mp.sqrt(max(mp.mpf(0),1-u*u/(16*B*B)))*mp.exp(-mp.sqrt(1+u*u))
    denB=mp.quad(lambda u:u**2*radial(u),intervals)
    moment8=mp.quad(lambda u:u**10*radial(u),intervals)/(4096*B**8*denB)
    qmoment=mp.quad(lambda u:(u**4/B**2-u**6/(16*B**4))*radial(u),intervals)/denB
    assert moment8>=cap*(1+B)**-8*mp.mpf(21)/8
    assert qmoment>=3*cq*(1+B)**-2
    passed(f'PC20-PC25 explicit smooth admissible density at B={B}',
           B8_polynomial_moment=str(B**8*moment8),
           B2_q_moment=str(B**2*qmoment))

# Reuse only the full-word function definitions from the accepted JP checks;
# no top-level test or write in that earlier file is executed.
previous=ROOT.parent/'verify_boundary_reflection.py'
tree=ast.parse(previous.read_text(encoding='utf-8'))
definitions=ast.Module(body=[node for node in tree.body if isinstance(node,ast.FunctionDef)],type_ignores=[])
ns={'mp':mp,'Counter':Counter,'rng':random.Random(20261012),
    'I':(mp.mpf(1),mp.mpf(0),mp.mpf(0),mp.mpf(0)),
    'checks':[],'ROOT':ROOT}
exec(compile(definitions,str(previous),'exec'),ns)
ns['coeff']=lru_cache(None)(ns['coeff'])
for m in (4,6,8):
    links={e:ns['I'] for e in ns['edges'](m)}
    for e in ns['chords'](m):links[e]=ns['randq']()
    L=m//2;n=m+1;h=mp.pi/(2*n)
    v=(1,L-1,0,2);b=(m,L-1,0,2);c=(m-1,L-1,0,2)
    A=ns['product'](ns['Apath'](L-1,0,m),links)
    candidate=ns['mul'](ns['mul'](ns['mul'](A,links[v]),ns['inv'](links[b])),ns['inv'](A))
    actual=ns['formula_word'](c,links,m)
    assert ns['norm']([x-y for x,y in zip(actual,candidate)])<mp.mpf('1e-55')
    av,bv=ns['coeff'](v,m)
    d=8*mp.cos(3*h)*mp.cos(h)**3/n**3
    assert abs(-4*av*bv-d)<mp.mpf('1e-55')
    maxima=max(abs(ns['coeff']((i,k,l,2),m)[0]*ns['coeff']((i,k,l,2),m)[1])
               for i in range(1,m) for k in range(m) for l in range(m+1))
    assert abs(maxima-abs(av*bv))<mp.mpf('1e-55')
    oldd=8*mp.cos(h)*mp.cos(3*h)*mp.sin(2*h)**2/n**3
    assert abs(d/oldd-1/(4*mp.sin(h)**2))<mp.mpf('1e-55')
    passed(f'PC45-PC48 full original-word conjugation, coefficients and family maximum m={m}',
           d_circle=str(d),tested_family_size=(m-1)*m*(m+1))

# Exact fourth-moment cubature verifies the entire affine remainder for
# arbitrary original boundary links at the stronger receiving chord.
m=4;L=2
links={e:ns['I'] for e in ns['edges'](m)}
for e in ns['chords'](m):links[e]=ns['randq']()
v=(1,L-1,0,2);b=(m,L-1,0,2);av,bv=ns['coeff'](v,m)
hb=links[b];d=-4*av*bv
design=[]
for i in range(4):
    for sign in (-1,1):
        p=[mp.mpf(0)]*4;p[i]=mp.mpf(sign);design.append(tuple(p))
design.extend(tuple(mp.mpf(s)/2 for s in signs) for signs in product((-1,1),repeat=4))
projection=mp.matrix(3,3);normY=mp.mpf(0);oddnorm=mp.mpf(0);cross=mp.mpf(0)
for U in design:
    links[v]=U
    V=ns['mul'](U,ns['inv'](hb));cqV=V[0]*ns['q'](V)
    for alpha in range(3):
        S,SR,Y=ns['full_data_with_derivative'](links,m,b,alpha)
        normY+=Y*Y/24
        for beta in range(3):projection[alpha,beta]+=Y*cqV[beta]/24
    odd=-av*bv*((4*U[0]**2-1)+(4*V[0]**2-1))
    oddnorm+=odd*odd/24;cross+=(S-SR-odd)*odd/24
for alpha in range(3):
    for beta in range(3):
        assert abs(projection[alpha,beta]-2*av*bv*int(alpha==beta)/6)<mp.mpf('1e-50')
assert normY>=d*d/8
assert abs(oddnorm-d*d*(1+2*hb[0]**2)/12)<mp.mpf('1e-50')
assert abs(cross)<mp.mpf('1e-50')
passed('PC49 full central-chord derivative and odd harmonic with arbitrary boundary links',
       original_derivative_norm=str(normY),harmonic_lower_bound=str(d*d/8),
       affine_cross_remainder=str(cross))

assert Fr(5000,12)==Fr(1250,3)
assert Fr(5000,6)==Fr(2500,3)
assert Fr(5000,8)==625
assert 2*3+2*12+2*8==46
assert 2*12+2*8+2*2==44
assert 2*3+2*12+2*8-1==45
passed('PC50-PC52 exact path prefactors and powers')
note=(ROOT/'POLYNOMIAL_CONDITIONAL_BOUNDS.md').read_text(encoding='utf-8')
assert set(re.findall(r'\\tag\{(PC\d+)\}',note))=={f'PC{i}' for i in range(1,53)}
assert len(re.findall(r'\\tag\{PC\d+\}',note))==52
assert '\ufffd' not in note and '\x00' not in note
receipt={
    'created_at':datetime.now(timezone.utc).isoformat(),
    'all_passed':True,'checks':checks,
    'prior_full_word_definitions_sha256':hashlib.sha256(previous.read_bytes()).hexdigest(),
    'scope':'Exact rational Gram inversion and polynomial identities; numerical complete cap Grams and 65-digit full-word harmonic checks. General proofs are in PC1-PC52.'
}
(ROOT/'POLYNOMIAL_CONDITIONAL_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'all_passed':True,'checks':len(checks)}))
