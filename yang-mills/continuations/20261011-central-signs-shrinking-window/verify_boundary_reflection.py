"""Independent full-word, incidence and harmonic checks for JP1-JP49."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import random, json
import mpmath as mp

ROOT=Path(__file__).resolve().parent
mp.mp.dps=60
rng=random.Random(20261011)
checks=[]
I=(mp.mpf(1),mp.mpf(0),mp.mpf(0),mp.mpf(0))

def mul(a,b):
    aw,ax,ay,az=a;bw,bx,by,bz=b
    return (aw*bw-ax*bx-ay*by-az*bz,
            aw*bx+bw*ax+ay*bz-az*by,
            aw*by+bw*ay+az*bx-ax*bz,
            aw*bz+bw*az+ax*by-ay*bx)

def inv(a):return (a[0],-a[1],-a[2],-a[3])
def q(a):return mp.matrix([2*x for x in a[1:]])
def cross(a,b):return mp.matrix([a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def norm(a):return mp.sqrt(sum(x*x for x in a))
def randq():
    x=[mp.mpf(rng.randint(-20,20)) for _ in range(4)]
    r=norm(x);return tuple(y/r for y in x)
def expgen(t,alpha):
    z=[mp.cos(t/2),mp.mpf(0),mp.mpf(0),mp.mpf(0)]
    z[alpha+1]=mp.sin(t/2)
    return tuple(z)

def edges(m):
    n=m+1
    for i in range(n):
      for k in range(n):
       for l in range(n):
        if i<m:yield(i,k,l,1)
        if k<m:yield(i,k,l,2)
        if l<m:yield(i,k,l,3)
def path(i,k,l):
    return [(0,0,z,3) for z in range(l)]+[(0,y,l,2) for y in range(k)]+[(x,k,l,1) for x in range(i)]
def chords(m):
    return [e for e in edges(m) if (e[3]==2 and e[0]>0) or (e[3]==3 and e[:2]!=(0,0))]
def boundary(m):
    return [(m,k,l,2) for k in range(m) for l in range(m+1)]+[(m,0,l,3) for l in range(m)]
def endpoint(e):
    v=list(e[:3]);v[e[3]-1]+=1;return tuple(v)
def product(seq,links):
    a=I
    for e in seq:a=mul(a,links[e])
    return a
def rooted(e,links):
    return mul(mul(product(path(*e[:3]),links),links[e]),inv(product(path(*endpoint(e)),links)))
def reflected(links,m):
    out={}
    for e in edges(m):
        i,k,l,d=e
        out[e]=inv(links[(m-1-i,k,l,1)]) if d==1 else links[(m-i,k,l,d)]
    return out
def coeff(e,m):
    i,k,l,d=e;n=m+1
    v=lambda x:mp.sqrt(mp.mpf(2)/n)*mp.cos(mp.pi*(x+mp.mpf('.5'))/n)
    w=lambda x:-mp.sqrt(mp.mpf(2)/n)*mp.sin(mp.pi*(x+1)/n)
    v0=1/mp.sqrt(n)
    if d==2:return(-v(i)*w(k)*v0/mp.sqrt(2),v0*w(k)*v(l)/mp.sqrt(2))
    return(mp.mpf(0),-v0*v(k)*w(l)/mp.sqrt(2))
def Apath(k,l,m):
    return [(m,0,r,3) for r in range(l)]+[(m,b,l,2) for b in range(k)]
def formula_word(e,links,m):
    i,k,l,d=e;s=(k,l);t=(k+1,l) if d==2 else(k,l+1)
    A=product(Apath(*s,m),links);B=product(Apath(*t,m),links)
    return mul(mul(A,links[(m-i,k,l,d)]),inv(B))
def vectors(links,m,use_reflection=False):
    vals=[mp.matrix([0,0,0]),mp.matrix([0,0,0])]
    for e in chords(m):
        qq=q(formula_word(e,links,m) if use_reflection else rooted(e,links))
        a,b=coeff(e,m);vals[0]+=a*qq;vals[1]+=b*qq
    return vals
def defect(links,m):
    u=vectors(links,m);r=vectors(links,m,True)
    return dot(u[0],u[1])+dot(r[0],r[1])
def close(name,a,b,tol=mp.mpf('1e-45')):
    error=norm([x-y for x,y in zip(a,b)]) if not isinstance(a,(int,float,mp.mpf)) else abs(a-b)
    assert error<tol,(name,error)
    checks.append({'name':name,'passed':True,'absolute_error':str(error)})

m=4
links={e:I for e in edges(m)}
for e in chords(m):links[e]=randq()
rlinks=reflected(links,m)
maxerr=mp.mpf(0)
for e in chords(m):
    actual=rooted(e,rlinks);pred=formula_word(e,links,m)
    maxerr=max(maxerr,norm([x-y for x,y in zip(actual,pred)]))
assert maxerr<mp.mpf('1e-50')
checks.append({'name':'JP4 all original reflected rooted words, m=4 random SU(2)','passed':True,'max_error':str(maxerr),'word_count':len(chords(m))})

# JP6 includes the scalar term and the noncommuting cross product.
maxerr=mp.mpf(0)
for e in chords(m):
    i,k,l,d=e;t=(k+1,l) if d==2 else(k,l+1)
    aa=product(Apath(k,l,m),links);bb=product(Apath(*t,m),links)
    U=links[(m-i,k,l,d)];V=mul(aa,inv(bb));rqu=q(mul(mul(aa,U),inv(aa)));vv=q(V)
    pred=V[0]*rqu+U[0]*vv+cross(rqu,vv)/2
    maxerr=max(maxerr,norm(pred-q(formula_word(e,links,m))))
assert maxerr<mp.mpf('1e-50')
checks.append({'name':'JP6 full affine quaternion identity, all chords m=4','passed':True,'max_error':str(maxerr)})

# Boundary-identity fibre with arbitrary remaining bulk holonomies.
for b in boundary(m):links[b]=I
u1,u3=vectors(links,m);r1,r3=vectors(links,m,True)
close('JP7 first vector on exact boundary fibre',r1,-u1)
close('JP7 third vector on exact boundary fibre',r3,u3)
close('JP8 full defect on boundary fibre',defect(links,m),mp.mpf(0))

# Compare JP10 with finite differences of the entire reflected word calculation.
for b in [(m,0,0,2),(m,2,3,2),(m,0,1,3)]:
    avec=[mp.mpf(0),mp.mpf(0)];vv=[mp.matrix([0,0,0]),mp.matrix([0,0,0])]
    for e in chords(m):
        i,k,l,d=e;t=(k+1,l) if d==2 else(k,l+1)
        epss=int(b in Apath(k,l,m));epst=int(b in Apath(*t,m))
        U=links[(m-i,k,l,d)]
        for z,coef in enumerate(coeff(e,m)):
            avec[z]+=coef*(epss-epst)*U[0]
            vv[z]+=coef*(epss+epst)*q(U)/2
    a,bcoef=coeff(b,m)
    predicted=(a+avec[0])*u3+(bcoef-avec[1])*u1+cross(vv[0],u3)-cross(vv[1],u1)
    step=mp.mpf('1e-22')
    for alpha in range(3):
        links[b]=expgen(step,alpha);plus=defect(links,m)
        links[b]=expgen(-step,alpha);minus=defect(links,m)
        links[b]=I
        close(f'JP10 original derivative b={b}, colour={alpha}',(plus-minus)/(2*step),predicted[alpha],mp.mpf('1e-35'))

for m in (4,6,8):
    B=boundary(m);rows=[];wall=[]
    for b in B:
        rr=Counter(path(*b[:3]));rr[b]+=1
        for e in path(*endpoint(b)):rr[e]-=1
        rows.append({e:k for e,k in rr.items() if k})
        _,k,l,d=b;t=(k+1,l) if d==2 else(k,l+1)
        wall.append({(k,l):-1,t:1})
    for i,r in enumerate(rows):
        for j,s in enumerate(rows):
            actual=sum(value*s.get(e,0) for e,value in r.items())
            predicted=2*int(i==j)+m*sum(value*wall[j].get(v,0) for v,value in wall[i].items())
            assert actual==predicted,(m,i,j,actual,predicted)
    checks.append({'name':f'JP12 all integer original-word metric entries, m={m}','passed':True,'dimension':len(B),'entries':len(B)**2})

for m in (4,6,8):
    links={e:I for e in edges(m)};links[(1,0,0,2)]=expgen(mp.pi,0)
    n=m+1;h=mp.pi/(2*n)
    expected=8*mp.cos(h)*mp.cos(3*h)*mp.sin(2*h)**2/n**3
    step=mp.mpf('1e-22');be=(m,0,0,2)
    links[be]=expgen(step,0);plus=defect(links,m)
    links[be]=expgen(-step,0);minus=defect(links,m)
    links[be]=I
    close(f'JP15 zero-fibre value, m={m}',defect(links,m),mp.mpf(0))
    close(f'JP15 positive original normal derivative, m={m}',(plus-minus)/(2*step),expected,mp.mpf('1e-35'))

def normal_data(links,m,b):
    u1,u3=vectors(links,m)
    avec=[mp.mpf(0),mp.mpf(0)]
    vv=[mp.matrix([0,0,0]),mp.matrix([0,0,0])]
    for e in chords(m):
        i,k,l,d=e;t=(k+1,l) if d==2 else(k,l+1)
        epss=int(b in Apath(k,l,m));epst=int(b in Apath(*t,m))
        U=links[(m-i,k,l,d)]
        for z,coef in enumerate(coeff(e,m)):
            avec[z]+=coef*(epss-epst)*U[0]
            vv[z]+=coef*(epss+epst)*q(U)/2
    a,bcoef=coeff(b,m)
    return (a+avec[0])*u3+(bcoef-avec[1])*u1+cross(vv[0],u3)-cross(vv[1],u1)

# Extract the exact quadratic term while all other bulk links are arbitrary.
m=4
links={e:I for e in edges(m)}
for e in chords(m):
    if e not in boundary(m):links[e]=randq()
be=(m,0,0,2);ke=(1,0,0,2);A,d0=coeff(ke,m)
links[ke]=I;at_plus=normal_data(links,m,be)
links[ke]=(-1,0,0,0);at_minus=normal_data(links,m,be)
vzero=(at_plus+at_minus)/2;hzero=(at_plus-at_minus)/2
Mzero=mp.matrix(3,3)
for alpha in range(3):
    basis=[0,0,0,0];basis[alpha+1]=1
    links[ke]=tuple(basis);value_plus=normal_data(links,m,be)
    links[ke]=tuple(-x for x in basis);value_minus=normal_data(links,m,be)
    for beta in range(3):Mzero[beta,alpha]=(value_plus[beta]-value_minus[beta])/4
for trial in range(5):
    U=randq();links[ke]=U
    predicted=2*A*d0*U[0]*q(U)+U[0]*hzero+Mzero*q(U)+vzero
    close(f'JP31 full quadratic harmonic identity, arbitrary bulk, trial={trial}',
          normal_data(links,m,be),predicted,mp.mpf('1e-45'))

# The 24 unit-quaternion points below integrate all degrees through four.
from fractions import Fraction as Fr
from itertools import product as cartesian_product
from math import comb
design=[]
for alpha in range(4):
    for sign in (-1,1):
        e=[Fr(0)]*4;e[alpha]=Fr(sign);design.append(tuple(e))
design.extend(tuple(Fr(sign,2) for sign in signs)
              for signs in cartesian_product((-1,1),repeat=4))
def rising(a,k):
    out=Fr(1)
    for i in range(k):out*=a+i
    return out
for powers in cartesian_product(range(5),repeat=4):
    if sum(powers)>4:continue
    observed=sum(__import__('functools').reduce(lambda x,y:x*y,
                 (point[i]**powers[i] for i in range(4)),Fr(1))
                 for point in design)/24
    expected=Fr(0)
    if all(power%2==0 for power in powers):
        expected=__import__('functools').reduce(lambda x,y:x*y,
                     (rising(Fr(1,2),power//2) for power in powers),Fr(1))
        expected/=rising(Fr(2),sum(powers)//2)
    assert observed==expected,(powers,observed,expected)
checks.append({'name':'JP32 exact 24-point Haar cubature for every quaternion monomial through degree four',
               'passed':True,'monomials':comb(8,4)})
projection=mp.matrix(3,3);totalnorm=mp.mpf(0)
for point in design:
    U=tuple(mp.mpf(p.numerator)/p.denominator for p in point)
    links[ke]=U;nb=normal_data(links,m,be);cq=U[0]*q(U)
    totalnorm+=dot(nb,nb)/24
    for alpha in range(3):
        for beta in range(3):projection[alpha,beta]+=nb[alpha]*cq[beta]/24
for alpha in range(3):
    for beta in range(3):
        close(f'JP33 projected component alpha={alpha}, beta={beta}',
              projection[alpha,beta],2*A*d0*int(alpha==beta)/6)
assert totalnorm>=2*A*A*d0*d0
checks.append({'name':'JP33 complete Haar normal norm exceeds exact d_star squared / 8',
               'passed':True,'integral':str(totalnorm),'proved_lower_bound':str(2*A*A*d0*d0)})

for m in (4,6,8):
    B=boundary(m);faces=[]
    for i,k,l in cartesian_product(range(m+1),repeat=3):
        v=(i,k,l)
        for d in (1,2,3):
            for f in range(d+1,4):
                if v[d-1]>=m or v[f-1]>=m:continue
                vd=list(v);vd[d-1]+=1
                vf=list(v);vf[f-1]+=1
                faces.append({v+(d,),tuple(vd)+(f,),tuple(vf)+(d,),v+(f,)})
    incidences={edge:sum(edge in face for face in faces) for edge in B}
    assert sum(incidences.values())==3*m*(m+1)
    assert sum((1,0,0,2) in face for face in faces)==3
    checks.append({'name':f'JP25 and JP34 all original face incidences, m={m}',
                   'passed':True,'boundary_incidence_total':sum(incidences.values())})
    for e in chords(m):
        i,k,l,d=e;t=(k+1,l) if d==2 else(k,l+1)
        counts=Counter(Apath(k,l,m)+Apath(*t,m))
        assert sum(counts.values())<=4*m-1 and max(counts.values(),default=0)<=2
        assert (m-i,k,l,d) not in B
    K=8*m-2;dimension_coeff=[1]+[0]*K
    for _ in B:
        dimension_coeff=[sum((power+1)**2*dimension_coeff[z-power]
                              for power in range(min(4,z)+1)) for z in range(K+1)]
    dim=sum(dimension_coeff)
    assert dim<=55**len(B) and dim<=comb(4*len(B)+K,K)
    if len(B)>=K:assert dim>=4**K*comb(len(B),K)
    checks.append({'name':f'JP26-JP29 full endpoint degrees and exact band dimension, m={m}',
                   'passed':True,'A_m':str(dim),'K_m':K,'boundary_count':len(B)})

# Global arbitrary-boundary calculation, independently differentiating each
# occurrence in the full reflected product.
def product_and_derivative(word,links,b,alpha):
    value=I;derivative=(mp.mpf(0),)*4
    generator=[mp.mpf(0)]*4;generator[alpha+1]=mp.mpf('.5')
    for edge,sign in word:
        factor=links[edge] if sign==1 else inv(links[edge])
        df=(mp.mpf(0),)*4
        if edge==b:
            df=mul(generator,factor) if sign==1 else tuple(-x for x in mul(factor,generator))
        derivative=tuple(x+y for x,y in zip(mul(derivative,factor),mul(value,df)))
        value=mul(value,factor)
    return value,derivative

def full_data_with_derivative(links,m,b,alpha):
    u=[mp.matrix([0,0,0]),mp.matrix([0,0,0])]
    r=[mp.matrix([0,0,0]),mp.matrix([0,0,0])]
    du=[mp.matrix([0,0,0]),mp.matrix([0,0,0])]
    dr=[mp.matrix([0,0,0]),mp.matrix([0,0,0])]
    generator=[mp.mpf(0)]*4;generator[alpha+1]=mp.mpf('.5')
    for e in chords(m):
        i,k,l,d=e;t=(k+1,l) if d==2 else(k,l+1)
        word=[(f,1) for f in Apath(k,l,m)]+[((m-i,k,l,d),1)]+[(f,-1) for f in reversed(Apath(*t,m))]
        rvalue,rd=product_and_derivative(word,links,b,alpha)
        ud=mul(generator,links[e]) if e==b else (mp.mpf(0),)*4
        for z,coef in enumerate(coeff(e,m)):
            u[z]+=coef*q(links[e]);r[z]+=coef*q(rvalue)
            du[z]+=coef*q(ud);dr[z]+=coef*q(rd)
    S=dot(u[0],u[1]);SR=dot(r[0],r[1])
    derivative=dot(du[0],u[1])+dot(u[0],du[1])+dot(dr[0],r[1])+dot(r[0],dr[1])
    return S,SR,derivative

m=4;links={e:I for e in edges(m)}
for e in chords(m):links[e]=randq()
be=(m,0,0,2);ke=(1,0,0,2);A,d0=coeff(ke,m)
hb=links[be];saved_k=links[ke];step=mp.mpf('1e-22')
for alpha in range(3):
    _,_,analytic=full_data_with_derivative(links,m,be,alpha)
    links[be]=mul(expgen(step,alpha),hb);plus=defect(links,m)
    links[be]=mul(expgen(-step,alpha),hb);minus=defect(links,m)
    links[be]=hb
    close(f'JP42 full nonidentity-boundary product derivative, colour={alpha}',
          analytic,(plus-minus)/(2*step),mp.mpf('1e-35'))

derivative_projection=mp.matrix(3,3);derivative_norm=mp.mpf(0)
raw_mass=mp.mpf(0);projected_mass=mp.mpf(0);cross_remainder=mp.mpf(0)
gram=mp.matrix(2,2);even_projected_mass=mp.mpf(0)
for point in design:
    U=tuple(mp.mpf(p.numerator)/p.denominator for p in point);links[ke]=U
    V=mul(U,inv(hb));cq=V[0]*q(V)
    chi=4*U[0]**2-1;chiv=4*V[0]**2-1
    pq=[-A*d0*chi,A*d0*chiv]
    for alpha in range(3):
        S,SR,Y=full_data_with_derivative(links,m,be,alpha)
        derivative_norm+=Y*Y/24
        for beta in range(3):derivative_projection[alpha,beta]+=Y*cq[beta]/24
    raw=S-SR;quadratic=pq[0]-pq[1]
    raw_mass+=raw*raw/24;projected_mass+=quadratic*quadratic/24
    cross_remainder+=(raw-quadratic)*quadratic/24
    even_projected_mass+=(pq[0]+pq[1])**2/24
    for alpha in range(2):
        for beta in range(2):gram[alpha,beta]+=pq[alpha]*pq[beta]/24
for alpha in range(3):
    for beta in range(3):
        close(f'JP42 global derivative harmonic alpha={alpha}, beta={beta}',
              derivative_projection[alpha,beta],2*A*d0*int(alpha==beta)/6,
              mp.mpf('1e-43'))
assert derivative_norm>=2*A*A*d0*d0
checks.append({'name':'JP43 arbitrary-boundary full derivative Haar energy lower bound',
               'passed':True,'integral':str(derivative_norm),'lower_bound':str(2*A*A*d0*d0)})
rho=(4*hb[0]**2-1)/3
for alpha in range(2):
    for beta in range(2):
        expected=A*A*d0*d0*(1 if alpha==beta else -rho)
        close(f'JP46 complete harmonic mass Gram alpha={alpha}, beta={beta}',gram[alpha,beta],expected)
close('JP47 original odd projection norm',projected_mass,(4*A*A*d0*d0/3)*(1+2*hb[0]**2))
close('JP47 full affine remainder orthogonal to odd harmonic',cross_remainder,mp.mpf(0))
assert raw_mass>=projected_mass
checks.append({'name':'JP47 full original odd Haar mass exceeds harmonic mass',
               'passed':True,'raw_mass':str(raw_mass),'harmonic_mass':str(projected_mass)})
close('JP48 original even harmonic norm',even_projected_mass,(16*A*A*d0*d0/24)*dot(q(hb),q(hb)))

note=(ROOT/'BOUNDARY_REFLECTION_AND_RAW_ENDPOINT.md').read_text(encoding='utf-8')
import re
assert set(re.findall(r'\\tag\{(JP\d+)\}',note))=={f'JP{i}' for i in range(1,50)}
assert '\x00' not in note
assert '\ufffd' not in note
receipt={'created_at':datetime.now(timezone.utc).isoformat(),'scope':'Exact integer incidence and quaternion cubature tests, plus high-precision full-word and normal-harmonic evaluations with arbitrary boundary links; general mathematical proofs are in JP1-JP49.','checks':checks,'all_passed':True}
(ROOT/'BOUNDARY_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'all_passed':True,'checks':len(checks)}))
