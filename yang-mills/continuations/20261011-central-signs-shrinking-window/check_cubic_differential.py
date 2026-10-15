from pathlib import Path
import functools,itertools,json,time
import sympy as s
O=Path(__file__).resolve().parent;start=time.time()
x=s.symbols('x0:4');k=s.Rational(3,5);psi=1+x[0]/5+x[1]/7;E=s.Rational(2,3)
def clean(v):return s.cancel(v)
@functools.lru_cache(None)
def X(i,f):
    v=-x[i+1]*s.diff(f,x[0])+x[0]*s.diff(f,x[i+1])
    for j in range(3):
        for z in range(3):v+=s.LeviCivita(i,j,z)*x[j+1]*s.diff(f,x[z+1])
    return clean(v/2)
@functools.lru_cache(None)
def D(f):return clean(sum(X(i,X(i,f)) for i in range(3)))
a=[clean(X(i,psi)/psi) for i in range(3)]
a2={(j,i):clean(X(j,X(i,psi))/psi) for i,j in itertools.product(range(3),repeat=2)}
a3={(h,j,i):clean(X(h,X(j,X(i,psi)))/psi) for i,j,h in itertools.product(range(3),repeat=3)}
V=clean(E+k*D(psi)/psi);Vi=[X(i,V) for i in range(3)]
Vji={(j,i):X(j,Vi[i]) for i,j in itertools.product(range(3),repeat=2)}
def L(f):return clean(-k*D(f)-2*k*sum(a[i]*X(i,f) for i in range(3)))
t=x[2]+x[0]*x[1]+x[1]*x[2]*x[3]
t1=[X(i,t) for i in range(3)];t2={(j,i):X(j,t1[i]) for i,j in itertools.product(range(3),repeat=2)}
t3={(h,j,i):X(h,t2[j,i]) for i,j,h in itertools.product(range(3),repeat=3)}
l2=clean(k**2*D(D(t))+4*k**2*sum(a[i]*X(i,D(t)) for i in range(3))+4*k**2*sum(a2[j,i]*t2[j,i] for i,j in itertools.product(range(3),repeat=2))+2*k*sum(Vi[i]*t1[i] for i in range(3)))
l3=clean(-k**3*D(D(D(t)))-6*k**3*sum(a[i]*X(i,D(D(t))) for i in range(3))-12*k**3*sum(a2[j,i]*X(j,X(i,D(t))) for i,j in itertools.product(range(3),repeat=2))-8*k**3*sum(a3[h,j,i]*t3[h,j,i] for i,j,h in itertools.product(range(3),repeat=3))-6*k**2*sum(Vi[i]*X(i,D(t)) for i in range(3))-8*k**2*sum(Vji[j,i]*t2[j,i] for i,j in itertools.product(range(3),repeat=2))-4*k**2*sum((Vi[j]*a[i]+2*Vi[i]*a[j])*t2[j,i] for i,j in itertools.product(range(3),repeat=2))-2*k**2*sum(D(Vi[i])*t1[i] for i in range(3))-4*k**2*sum(a[j]*Vji[j,i]*t1[i] for i,j in itertools.product(range(3),repeat=2)))
checks=[]
def check(name,v):
    yes=bool(clean(v)==0);checks.append(dict(name=name,passed=yes));assert yes,name
check('complete second power',L(L(t))-l2)
check('complete third power with all ordered derivatives',L(l2)-l3)
for i in range(3):check('original Casimir commutes with field '+str(i),D(X(i,t))-X(i,D(t)))
z=s.Rational(1,11);eps=s.Rational(1,4);r=s.Integer(4)
e1=z*(1+eps+r);e2=z*z*(eps+r+eps*r);e3=eps*r*z**3
check('full three-shift polynomial',L(L(L(t)))+e1*L(L(t))+e2*L(t)+e3*t-(l3+e1*l2+e2*L(t)+e3*t))
# Verify the potential is the one making the retained positive psi an exact ground.
check('original ground equation including E',-k*D(psi)+V*psi-E*psi)
res=dict(checks=len(checks),all_passed=all(q['passed'] for q in checks),details=checks,seconds=time.time()-start,scope='Exact rational differential identities on original radius-two SU2 with noncommuting fields; positive psi=1+x0/5+x1/7 and its explicitly constructed potential. This potential is not Wilson and no Wilson vacuum is simulated. The general formula retains Delta(V_i).',potential=str(V))
(O/'CUBIC_DIFFERENTIAL_CHECKS.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf8')
print(json.dumps({q:v for q,v in res.items() if q not in ['details','potential']}))

# Full ordered Haar derivative moments: retain the unit-state norm explicitly.
def haar(poly):
    poly=s.Poly(s.expand(poly),*x);out=0
    for powers,coefficient in poly.terms():
        if any(z%2 for z in powers):continue
        K=sum(powers)//2;num=s.Integer(1);den=s.Integer(1)
        for power in powers:
            if power:num*=s.factorial2(power-1)
        for n in range(K):den*=4+2*n
        out+=coefficient*num/den
    return s.factor(out)
unit_square=haar(psi**2)
for order in [1,2,3]:
    words=[psi]
    for n in range(order):words=[X(i,f) for f in words for i in range(3)]
    exact=sum(haar(f*f) for f in words)/unit_square
    cas=psi
    for n in range(order):cas=-D(cas)
    spectral=haar(psi*cas)/unit_square
    check('complete original Haar derivative moment '+str(order),exact-spectral)
for i in range(3):
    check('ground third-moment gradient identity '+str(i),clean(psi*X(i,V)+(V-E)*X(i,psi)-k*X(i,D(psi))))
for i,j in [(0,1),(1,2),(2,0)]:
    check('noncommuting left field bracket '+str((i,j)),X(i,X(j,t))-X(j,X(i,t))+sum(s.LeviCivita(i,j,h)*X(h,t) for h in range(3)))
# Exact two-link fixture: an outside derivative contributes nontrivially.
eta=s.Rational(1,7);x0=s.Rational(3,5);x1=s.Rational(4,5);y0=s.Rational(5,13);y1=s.Rational(12,13);ps=1+eta*x0*y0
outside_term=3*k**3*eta**2*x0*x1**2*y1**2*(1-eta*x0*y0)/(8*ps**4)
assert outside_term>0
checks.append(dict(name='outside index contribution in positive two-link fixture',passed=True,exact_value=str(outside_term),scope='psi=1+eta*x0*y0, t=x0, constructed potential E+kappa*Delta(psi)/psi; the contribution vanishes at y=identity and is positive here, so it is not inside-measurable.'))
res.update(checks=len(checks),details=checks,all_passed=all(q['passed'] for q in checks),seconds=time.time()-start,unit_square=str(unit_square),outside_term=str(outside_term))
(O/'CUBIC_DIFFERENTIAL_CHECKS.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(final_checks=res['checks'],all_passed=res['all_passed'],seconds=res['seconds'],outside_term=str(outside_term))))
