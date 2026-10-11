"""Independent exact and high-precision checks for PG1-PG70."""
from pathlib import Path
from fractions import Fraction as Fr
from itertools import product
from collections import Counter
from functools import lru_cache
from datetime import datetime, timezone
import ast, hashlib, json, math, random
import mpmath as mp
import sympy as sy

ROOT=Path(__file__).resolve().parent
mp.mp.dps=90
checks=[]

def passed(name,**data):
    checks.append(dict(name=name,passed=True,**data))

def close(a,b,tol=mp.mpf('1e-65')):
    assert abs(a-b)<=tol*max(1,abs(a),abs(b)),(a,b)

alpha=Fr(23,24)
c6=alpha**10/588
assert c6==Fr(41426511213649,37281188007641088)
assert c6>Fr(1,1024)
assert alpha**6/28>c6 and 9*alpha**4/25>c6
assert Fr(2)*(Fr(1,45)-Fr(1,49))==Fr(8,2205)
assert alpha**10/2205*15==alpha**10/147
passed('PG11-PG16 exact pair moment and all cap constants',c6=str(c6))
c6m=mp.mpf(c6.numerator)/c6.denominator
alpham=mp.mpf(23)/24

# Exact derivative check of all seven endpoint formulas.
t=sy.symbols('t',real=True)
s,c=sy.sin(t),sy.cos(t)
integrands=[s**2,s**4,s**4*c,s**4*c**2,
            s**2*(c**2+2),s**2*c*(2*c**2+1),s**2*(4*c**4-2*c**2+1)]
formulas=[t/2-sy.sin(2*t)/4,
          3*t/8-sy.sin(2*t)/4+sy.sin(4*t)/32,
          s**5/5,
          t/16-sy.sin(2*t)/64-sy.sin(4*t)/64+sy.sin(6*t)/192,
          9*t/8-sy.sin(2*t)/2-sy.sin(4*t)/32,
          s**3-sy.Rational(2,5)*s**5,
          t/2-3*sy.sin(2*t)/16-sy.sin(6*t)/48]
for i,(f,g) in enumerate(zip(formulas,integrands)):
    assert sy.trigsimp(sy.expand_trig(sy.diff(f,t)-g))==0,(i,f,g)
    assert f.subs(t,0)==0
passed('PG5-PG6 seven exact trigonometric antiderivatives')

def capvals(R):
    return [mp.quad(sy.lambdify(t,g,'mpmath'),[0,R]) for g in integrands]

for r in map(mp.mpf,('1','.5','.1','.02','.002')):
    J,I0,I1,I2,V0,V1,V2=capvals(r/2)
    scalar=16*(I2-I1**2/I0)/J
    vector=2*(V2-V1**2/V0)/J
    tensor=mp.mpf(2)/5*(4*I2+6*I0)/J
    assert scalar>=c6m*r**6
    assert vector>=alpham**6/28*r**4
    assert tensor>=9*alpham**4/25*r**2
    passed('PG7-PG15 exact cap Schur complements versus bounds',radius=str(r))

# An independent ambient-gradient calculation retains every complex coefficient.
# Six axes and eight cube vertices form an S2 rule exact through degree four.
omega=[]
for i in range(3):
    for sign in (-1,1):
        z=[mp.mpf(0)]*3;z[i]=sign
        omega.append((z,mp.mpf(1)/15))
for signs in product((-1,1),repeat=3):
    omega.append(([mp.mpf(x)/mp.sqrt(3) for x in signs],mp.mpf(3)/40))
assert sum(w for _,w in omega)==1
for i in range(3):
    close(sum(w*z[i]**2 for z,w in omega),mp.mpf(1)/3)
    close(sum(w*z[i]**4 for z,w in omega),mp.mpf(1)/5)
    for j in range(i):
        close(sum(w*z[i]**2*z[j]**2 for z,w in omega),mp.mpf(1)/15)
passed('PG8 independently verified angular cubature moments')

Avec=mp.mpc(3,2);B=mp.mpc(2,-1);C=mp.mpc(-3,4)
b=mp.matrix([mp.mpc(1,2),mp.mpc(-3,1),mp.mpc(2,-4)])
d=mp.matrix([mp.mpc(2,-3),mp.mpc(4,1),mp.mpc(-1,2)])
T=mp.matrix([[mp.mpc(1,2),mp.mpc(2,-1),mp.mpc(3,1)],
             [mp.mpc(2,-1),mp.mpc(-4,1),mp.mpc(1,-2)],
             [mp.mpc(3,1),mp.mpc(1,-2),mp.mpc(3,-3)]])
normT=sum(abs(x)**2 for x in T)
for r in (mp.mpf(1),mp.mpf('.3')):
    R=r/2;J,I0,I1,I2,V0,V1,V2=capvals(R)
    exact=(I0*abs(B)**2+4*I1*mp.re(mp.conj(B)*C)+4*I2*abs(C)**2)/(4*J)
    exact+=sum(V0*abs(b[i])**2+2*V1*mp.re(mp.conj(b[i])*d[i])+V2*abs(d[i])**2 for i in range(3))/(12*J)
    exact+=normT*(4*I2+6*I0)/(30*J)
    def ambient(theta):
        co,si=mp.cos(theta),mp.sin(theta)
        ans=mp.mpf(0)
        for wgtvec,weight in omega:
            x=mp.matrix([si*w for w in wgtvec])
            partial0=B+2*C*co+sum(d[i]*x[i] for i in range(3))
            partial=b+co*d+2*T*x
            radial=co*partial0+sum(x[i]*partial[i] for i in range(3))
            ans+=weight*(abs(partial0)**2+sum(abs(v)**2 for v in partial)-abs(radial)**2)/4
        return ans*si**2
    direct=mp.quad(ambient,[0,R])/J
    close(exact,direct)
    passed('PG7 full complex polynomial ambient gradient versus every cap block',radius=str(r))

# Pointwise two-channel determinant, including the affine coefficient.
cc=sy.symbols('c',real=True)
avec=sy.Matrix([cc,sy.sqrt(2)])
dvec=sy.Matrix([2*cc**2-1,sy.sqrt(2)*cc])
assert sy.expand(avec.dot(avec)*dvec.dot(dvec)-avec.dot(dvec)**2-2*(1-cc**2)**2)==0
passed('PG13 exact vector-channel determinant')

for Bscore in map(mp.mpf,('0','.1','1','2','6','100','1000000')):
    r=2/(Bscore+2)
    assert mp.exp(-Bscore*r)*r**6>= (1+Bscore)**-6*(1-mp.mpf('1e-85'))
    opt_r=1 if Bscore<=6 else 6/Bscore
    opt=mp.exp(-Bscore*opt_r)*opt_r**6
    assert opt>=mp.exp(-Bscore*r)*r**6*(1-mp.mpf('1e-85'))
passed('PG18-PG20 cap averaging radius and optimized bound')

# Exact fourth moments establish the complete quadratic harmonic norm.
def rising(a,k):return math.prod((a+i for i in range(k)),start=Fr(1))
def moment(p):
    if any(i%2 for i in p):return Fr(0)
    return math.prod((rising(Fr(1,2),i//2) for i in p),start=Fr(1))/rising(Fr(2),sum(p)//2)
assert moment((4,0,0,0))-Fr(1,2)*moment((2,0,0,0))+Fr(1,16)==Fr(1,16)
assert moment((2,2,0,0))==Fr(1,24)
assert 2*(moment((0,4,0,0))-moment((0,2,2,0)))==Fr(1,6)
passed('PG3 exact scalar vector and trace-free tensor Haar moments')

# The sharpness example: exact gradient and smooth score square.
tt=sy.symbols('t',nonnegative=True)
assert sy.expand((tt**2/8)**2*(tt**2/4-tt**4/64))==tt**6/256-tt**8/4096
I2=mp.quad(lambda u:u**2*mp.exp(-mp.sqrt(1+u*u)),[0,1,mp.inf])
I8=mp.quad(lambda u:u**8*mp.exp(-mp.sqrt(1+u*u)),[0,1,mp.inf])
limit=I8/(256*I2)
for BB in (8,32,128):
    den=mp.quad(lambda u:u**2*mp.sqrt(1-u*u/(16*BB*BB))*mp.exp(-mp.sqrt(1+u*u)),[0,1,8,4*BB])
    num=mp.quad(lambda u:u**8/256*(1-u*u/(16*BB*BB))**mp.mpf('1.5')*mp.exp(-mp.sqrt(1+u*u)),[0,1,8,4*BB])
    actual=num/den
    assert abs(actual-limit)<limit*80/(BB*BB)
passed('PG21-PG24 full gradient sharpness family',limit=str(limit))

# Load only previously audited original-word function definitions, never top-level code.
previous=ROOT/'verify_boundary_reflection.py'
tree=ast.parse(previous.read_text(encoding='utf-8'))
definitions=ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[])
ns={'mp':mp,'Counter':Counter,'rng':random.Random(311),'I':(mp.mpf(1),mp.mpf(0),mp.mpf(0),mp.mpf(0)),
    'checks':[],'ROOT':ROOT}
exec(compile(definitions,str(previous),'exec'),ns)
ns['coeff']=lru_cache(None)(ns['coeff'])
for m in (4,6,8,10):
    n=m+1;hh=mp.pi/(2*n)
    Jn=n/2-2*mp.cos(hh)**2
    close(sum(mp.cos(mp.pi*(i+mp.mpf('.5'))/n)**2 for i in range(1,m)),Jn)
    close(sum(mp.sin(mp.pi*(k+1)/n)**4 for k in range(m)),3*mp.mpf(n)/8)
    sums=Counter()
    incidences=Counter()
    for vert in product(range(m+1),repeat=3):
        for d1 in range(3):
            for d2 in range(d1+1,3):
                if vert[d1]==m or vert[d2]==m:continue
                v1=list(vert);v1[d1]+=1
                v2=list(vert);v2[d2]+=1
                for edge in (tuple(vert)+(d1+1,),tuple(v1)+(d2+1,),tuple(v2)+(d1+1,),tuple(vert)+(d2+1,)):
                    incidences[edge]+=1
    counts=Counter()
    for i,k,l in product(range(1,m),range(m),range(m+1)):
        edge=(i,k,l,2);bd=(m,k,l,2)
        rr=2+int(l>0)+int(l<m)
        assert incidences[edge]==rr and incidences[bd]==rr-1
        counts[rr]+=1
        aa,bb=ns['coeff'](edge,m)
        predicted=4/mp.mpf(n)**6*mp.cos(mp.pi*(i+mp.mpf('.5'))/n)**2*mp.cos(mp.pi*(l+mp.mpf('.5'))/n)**2*mp.sin(mp.pi*(k+1)/n)**4
        close(aa**2*bb**2,predicted)
        sums[rr]+=aa**2*bb**2
    assert counts=={3:2*m*(m-1),4:m*(m-1)**2}
    close(sums[3],3*Jn*mp.cos(hh)**2/n**5)
    close(sums[4],3*Jn**2/(2*n**5))
    passed('PG33-PG36 exhaustive physical-face counts and full coefficient sums',m=m,counts=dict(counts))

# Recover H2 from full reflected original words, retaining all affine terms.
m=4
links={e:(ns['randq']() if e in set(ns['chords'](m)) else ns['I']) for e in ns['edges'](m)}
def fullF(K,edge,reflected_sign=-1):
    changed=dict(links);changed[edge]=K
    vv=ns['vectors'](changed,m)
    ww=ns['vectors'](ns['reflected'](changed,m),m)
    return ns['dot'](vv[0],vv[1])+reflected_sign*ns['dot'](ww[0],ww[1])

for edge in ((1,0,0,2),(3,2,2,2),(1,3,4,2)):
    diag=[]
    for i in range(4):
        e=[mp.mpf(0)]*4;e[i]=1
        diag.append((fullF(tuple(e),edge)+fullF(tuple(-x for x in e),edge))/2)
    scalar=sum(diag)/4
    M=mp.matrix(4)
    for i in range(4):M[i,i]=diag[i]-scalar
    for i in range(4):
        for k in range(i):
            e=[mp.mpf(0)]*4;e[i]=e[k]=1/mp.sqrt(2)
            value=(fullF(tuple(e),edge)+fullF(tuple(-x for x in e),edge))/2
            M[i,k]=M[k,i]=value-scalar-(M[i,i]+M[k,k])/2
    actual=sum(v*v for v in M)/12
    aa,bb=ns['coeff'](edge,m)
    HH=links[(m,edge[1],edge[2],2)]
    expected=mp.mpf(4)/3*aa*aa*bb*bb*(1+2*HH[0]**2)
    close(actual,expected)
    passed('PG29-PG32 H2 recovered from complete original physical words',edge=edge,beta0=1)

# Exact rational path prefactors: beta0^2 j^6 -> 5000 pi^2/kappa^2.
assert Fr(2)*5000*Fr(1,4)*Fr(1,8)==Fr(625,2)
assert Fr(4)*5000*Fr(1,2)*Fr(1,16)==625
for j in (4,10,40):
    jj=mp.mpf(j);kap=mp.mpf('1.7');n=2*j**4+1;hh=mp.pi/(2*n)
    beta=mp.sqrt(8)*mp.sin(hh)*100*jj/kap
    xi=10000*jj**2/kap**2;Jn=n/2-2*mp.cos(hh)**2
    eta=lambda B:c6m/(1+B)**6
    cq=4/(5*mp.e**2)*alpham**4
    etaq=lambda B:cq/(1+B)**2
    bd=2*kap*beta**2*Jn/n**5*2*mp.cos(hh)**2*eta(12*xi)*(1+etaq(8*xi)/2)
    inside=2*kap*beta**2*Jn**2/n**5*eta(16*xi)*(1+etaq(12*xi)/2)
    limitbd=625*mp.pi**2/kap*c6m*(kap**2/120000)**6
    limitin=625*mp.pi**2/(2*kap)*c6m*(kap**2/160000)**6
    assert abs(jj**34*bd/limitbd-1)<20/jj**4
    assert abs(jj**30*inside/limitin-1)<20/jj**4
passed('PG42-PG46 original-path powers and both leading constants')

# Complete extension: density floor, pure linear factor and disjoint boundary sum.
C1=Fr(705,4096)
Cvec=Fr(75,784)*Fr(47,384)**3
assert C1==Fr(4,3)*Fr(15,8)*Fr(9,16)*Fr(47,384)
assert C1>=alpha**4/5
assert Fr(1,3)-Fr(3,7)**2/Fr(3,5)==Fr(4,147)
assert Fr(15,16)*Fr(5,8)*Fr(4,147)==Fr(25,1568)
assert 3*Fr(25,1568)*Fr(47,384)**3==Cvec/2
passed('PG50-PG59 exact marginal and vector-cap constants and Schur complement')
C1m=mp.mpf(C1.numerator)/C1.denominator
Cvecm=mp.mpf(Cvec.numerator)/Cvec.denominator
def optimized(B,k):
    r=1 if B<=k else k/B
    return mp.exp(-B*r)*r**k
def psi6(B):return max(2*mp.exp(-2*mp.pi*B),c6m*optimized(B,6))
def theta1(B):return max(mp.exp(-2*mp.pi*B),C1m*optimized(B,2))
def theta6(B):return max(mp.exp(-2*mp.pi*B),Cvecm*optimized(B,6))
assert psi6(0)==2 and theta1(0)==theta6(0)==1
for Bscore in map(mp.mpf,('0','.1','1','2','6','100','1000000')):
    assert psi6(Bscore)>=c6m/(1+Bscore)**6
    assert theta1(Bscore)>=4/(5*mp.e**2)*alpham**4/(1+Bscore)**2
passed('PG47-PG52 retained Casimir factor and all stronger receiving comparisons')

def h2norm(callback):
    dd=[]
    for i in range(4):
        e=[mp.mpf(0)]*4;e[i]=1
        dd.append((callback(tuple(e))+callback(tuple(-x for x in e)))/2)
    mean=sum(dd)/4
    mat=mp.matrix(4)
    for i in range(4):mat[i,i]=dd[i]-mean
    for i in range(4):
        for k in range(i):
            e=[mp.mpf(0)]*4;e[i]=e[k]=1/mp.sqrt(2)
            value=(callback(tuple(e))+callback(tuple(-x for x in e)))/2
            mat[i,k]=mat[k,i]=value-mean-(mat[i,i]+mat[k,k])/2
    return sum(v*v for v in mat)/12

for edge in ((1,0,0,2),(3,2,2,2)):
    actual=h2norm(lambda K:fullF(K,edge,1))
    aa,bb=ns['coeff'](edge,m);HH=links[(m,edge[1],edge[2],2)]
    expected=mp.mpf(2)/3*aa*aa*bb*bb*ns['dot'](ns['q'](HH),ns['q'](HH))
    close(actual,expected)
    passed('PG53 complete original even polynomial H2 norm',edge=edge)

# Differentiate all full ordered words, including derivative of every remainder.
edge=(1,1,0,2);bdedge=(m,1,0,2)
aa,bb=ns['coeff'](edge,m);qnorms={'D':mp.mpf(0),'F':mp.mpf(0)}
dercache={}
def boundary_data(K,al):
    key=tuple(K)+(al,)
    if key not in dercache:
        changed=dict(links);changed[edge]=K
        SS,RR,derD=ns['full_data_with_derivative'](changed,m,bdedge,al)
        vv=ns['vectors'](changed,m)
        gen=[mp.mpf(0)]*4;gen[al+1]=mp.mpf('.5')
        dq=ns['q'](ns['mul'](gen,changed[bdedge]))
        ca,cb=ns['coeff'](bdedge,m)
        derS=ca*ns['dot'](dq,vv[1])+cb*ns['dot'](vv[0],dq)
        dercache[key]=(derD,2*derS-derD)
    return dercache[key]
for al in range(3):
    for z,label in enumerate(('D','F')):
        qnorms[label]+=h2norm(lambda K:boundary_data(K,al)[z])
close(qnorms['D'],2*aa**2*bb**2)
close(qnorms['F'],2*aa**2*bb**2)
passed('PG60-PG62 quadratic vector norm from full original boundary derivatives',
       edge=edge,boundary=bdedge,beta0=1)

for mm in (4,6,8):
    nn=mm+1;hh=mp.pi/(2*nn);Jn=nn/2-2*mp.cos(hh)**2;xi=mp.mpf('.07')
    actualBD=mp.mpf(0);actualBF=mp.mpf(0);actualW=mp.mpf(0)
    bulkset=set()
    for i,k,l in product(range(1,mm),range(mm),range(mm+1)):
        e=(i,k,l,2);bulkset.add(e)
        av,bv=ns['coeff'](e,mm)
        BK=12*xi if l in (0,mm) else 16*xi
        BH=8*xi if l in (0,mm) else 12*xi
        actualBD+=2*av**2*bv**2*psi6(BK)*theta1(BH)
        actualBF+=mp.mpf(4)/3*av**2*bv**2*psi6(BK)*(1+theta1(BH)/2)
    bdset=set()
    for k,l in product(range(mm),range(mm+1)):
        bdset.add((mm,k,l,2))
        av,bv=ns['coeff']((1,k,l,2),mm)
        BK=12*xi if l in (0,mm) else 16*xi
        actualW+=2*av**2*bv**2*theta6(BK)
    assert not (bulkset&bdset)
    expectedBD=3*Jn/nn**5*(2*mp.cos(hh)**2*psi6(12*xi)*theta1(8*xi)+Jn*psi6(16*xi)*theta1(12*xi))
    expectedBF=2*Jn/nn**5*(2*mp.cos(hh)**2*psi6(12*xi)*(1+theta1(8*xi)/2)+Jn*psi6(16*xi)*(1+theta1(12*xi)/2))
    expectedW=3*mp.cos(3*hh)**2/nn**5*(2*mp.cos(hh)**2*theta6(12*xi)+Jn*theta6(16*xi))
    close(actualBD,expectedBD);close(actualBF,expectedBF);close(actualW,expectedW)
    passed('PG55-PG63 exhaustive even odd and disjoint boundary sums',m=mm)

kap=mp.mpf('1.7')
P3=c6m*(kap**2/(20000*mp.e))**6
P4=c6m*(3*kap**2/(80000*mp.e))**6
T12=C1m*(kap**2/(40000*mp.e))**2
T13=C1m*(kap**2/(60000*mp.e))**2
T63=Cvecm*(kap**2/(20000*mp.e))**6
T64=Cvecm*(3*kap**2/(80000*mp.e))**6
limits=[(32,mp.mpf(3)/16*T63),(28,mp.mpf(3)/32*T64),
        (32,mp.mpf(3)/16*P3*T12),(28,mp.mpf(3)/32*P4*T13),
        (28,P3/8),(32,P3*T12/16),(24,P4/16),(28,P4*T13/32)]
for j in (4,10,40):
    jj=mp.mpf(j);nn=2*j**4+1;hh=mp.pi/(2*nn);Jn=nn/2-2*mp.cos(hh)**2
    xi=10000*jj**2/kap**2;cc=mp.cos(hh)**2
    summands=[3*mp.cos(3*hh)**2/nn**5*2*cc*theta6(12*xi),
              3*mp.cos(3*hh)**2/nn**5*Jn*theta6(16*xi),
              3*Jn/nn**5*2*cc*psi6(12*xi)*theta1(8*xi),
              3*Jn/nn**5*Jn*psi6(16*xi)*theta1(12*xi),
              2*Jn/nn**5*2*cc*psi6(12*xi),
              2*Jn/nn**5*cc*psi6(12*xi)*theta1(8*xi),
              2*Jn/nn**5*Jn*psi6(16*xi),
              Jn/nn**5*Jn*psi6(16*xi)*theta1(12*xi)]
    for value,(p,limitval) in zip(summands,limits):
        assert abs(jj**p*value/limitval-1)<20/jj**4
    beta=100*jj*mp.sqrt(8)*mp.sin(hh)/kap
    even=sum(summands[:4])
    odd=sum(summands[:2])+sum(summands[4:])
    evenlimit=mp.mpf(1875)*mp.pi**2/(4*kap**2)*(T64+P4*T13)
    oddlimit=mp.mpf(625)*mp.pi**2/(2*kap**2)*P4
    assert abs(jj**33*(jj*beta**2*even)/evenlimit-1)<20/jj**4
    assert abs(jj**29*(jj*beta**2*odd)/oddlimit-1)<20/jj**4
passed('PG64-PG70 all eight original-path contributions and both endpoint constants')

receipt={'created_at':datetime.now(timezone.utc).isoformat(),
         'all_passed':all(c['passed'] for c in checks),'checks':checks,
         'precision_decimal_digits':mp.mp.dps,
         'proof_file':'POLYNOMIAL_GRADIENT_BOUNDS.md',
         'original_word_helper_sha256':hashlib.sha256(previous.read_bytes()).hexdigest(),
         'test_scope':'Exact algebra and exhaustive finite-face counts; finite high-precision checks support, and do not replace, the complete proof.'}
(ROOT/'POLYNOMIAL_GRADIENT_CHECKS.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'all_passed':receipt['all_passed'],'checks':len(checks),'output':str(ROOT/'POLYNOMIAL_GRADIENT_CHECKS.json')}))
