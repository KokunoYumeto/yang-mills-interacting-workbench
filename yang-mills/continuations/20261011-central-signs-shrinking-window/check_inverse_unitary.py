from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import itertools, json, math
import mpmath as mp

O=Path(__file__).resolve().parent
mp.mp.dps=80
checks=[]
def ck(name,condition,**data):
    checks.append(dict(name=name,passed=bool(condition),**data))
    assert condition,(name,data)

# Exact rational jets at x=1/3,y=2/5. The two derivations do not commute.
# All words have length <=6; retaining Taylor order six suffices for their value.
ORDER=6
def add(a,b):
    c=a.copy()
    for p,v in b.items(): c[p]=c.get(p,F(0))+v
    return {p:v for p,v in c.items() if v}
def scale(a,s):return {p:v*s for p,v in a.items() if v*s}
def mul(a,b):
    c={}
    for p,v in a.items():
        for q,w in b.items():
            r=(p[0]+q[0],p[1]+q[1])
            if sum(r)<=ORDER:c[r]=c.get(r,F(0))+v*w
    return {p:v for p,v in c.items() if v}
def diff(a,i):
    c={}
    for p,v in a.items():
        if p[i]:
            q=list(p);q[i]-=1;c[tuple(q)]=v*p[i]
    return c
one={(0,0):F(1)}
x={(0,0):F(1,3),(1,0):F(1)}
y={(0,0):F(2,5),(0,1):F(1)}
def X(i,a):return add(diff(a,0),mul(y,diff(a,1))) if i==0 else mul(x,diff(a,1))
def value(a):return a.get((0,0),F(0))
def word(a,J):
    for i in J:a=X(i,a)
    return a
def inv(a):
    a0=value(a);u=scale(add(a,{(0,0):-a0}),-1/a0);term=one;out=one
    for k in range(1,ORDER+1):term=mul(term,u);out=add(out,term)
    return scale(out,1/a0)
h=add(add(scale(one,F(2)),x),add(mul(x,y),mul(y,y)))
rho=mul(h,h);hinv=inv(h)
v=add(add(mul(x,x),mul(x,y)),mul(mul(y,y),y))
potential=add(mul(x,mul(y,y)),mul(mul(x,x),x))
ck('fixture derivations are noncommuting',value(add(X(0,X(1,y)),scale(X(1,X(0,y)),-1)))!=0)
ck('exact inverse multiplier jet',mul(h,hinv)==one)

@lru_cache(None)
def partitions(n):
    if n==0:return ((),)
    out=[]
    for p in partitions(n-1):
        out.append(p+((n-1,),))
        for k in range(len(p)):out.append(p[:k]+(p[k]+(n-1,),)+p[k+1:])
    return tuple(out)
def fall(z,n):
    out=F(1)
    for i in range(n):out*=z-i
    return out
def subsets(n):
    for mask in range(1<<n):yield tuple(i for i in range(n) if mask&(1<<i))
@lru_cache(None)
def dr(J):return value(word(rho,J))/value(rho)
@lru_cache(None)
def ah(J):return value(h)*value(word(hinv,J))
for n in range(1,7):
    ck(f'Bell count order {n}',len(partitions(n))==[1,2,5,15,52,203][n-1])
    size_counts={}
    for p in partitions(n):
        sizes=tuple(sum(len(b)==r for b in p) for r in range(1,n+1))
        size_counts[sizes]=size_counts.get(sizes,0)+1
    for sizes,count in size_counts.items():
        den=math.prod(math.factorial(r)**sizes[r-1]*math.factorial(sizes[r-1]) for r in range(1,n+1))
        ck(f'partition multiplicity {n}/{sizes}',count==math.factorial(n)//den)
    for J in itertools.product(range(2),repeat=n):
        chain=sum(fall(F(-1,2),len(p))*math.prod(dr(tuple(J[i] for i in b)) for b in p) for p in partitions(n))
        ck(f'ordered inverse chain {J}',ah(J)==chain)
        rhs=F(0);comm=F(0);rhod=F(0)
        for S in subsets(n):
            Sc=tuple(i for i in range(n) if i not in S)
            JS=tuple(J[i] for i in S);JC=tuple(J[i] for i in Sc)
            rhs+=ah(JS)*value(word(v,JC))
            rhod+=value(word(h,JS))*value(word(h,JC))
            if S:comm-=value(word(potential,JS))*value(word(h,JC))
        ck(f'all inverse product subsets {J}',value(h)*value(word(mul(hinv,v),J))==rhs)
        ck(f'all density product subsets {J}',value(word(rho,J))==rhod)
        ck(f'ordered commutator subsets {J}',value(potential)*value(word(h,J))-value(word(mul(potential,h),J))==comm)

# Track each complete positive expression and its exact rational growth exponent.
class Growth:
    def __init__(self,value,degree=0,leading=None):
        self.value=mp.mpf(value);self.degree=F(degree);self.leading=mp.mpf(value if leading is None else leading)
    def __add__(self,other):
        other=cast(other);d=max(self.degree,other.degree)
        lead=(self.leading if self.degree==d else 0)+(other.leading if other.degree==d else 0)
        return Growth(self.value+other.value,d,lead)
    __radd__=__add__
    def __mul__(self,other):
        other=cast(other);return Growth(self.value*other.value,self.degree+other.degree,self.leading*other.leading)
    __rmul__=__mul__
    def __truediv__(self,other):return self*cast(other)**F(-1)
    def __rtruediv__(self,other):return cast(other)*self**F(-1)
    def __pow__(self,p):
        p=F(p);v=mp.mpf(p.numerator)/p.denominator
        return Growth(self.value**v,self.degree*p,self.leading**v)
def cast(x):return x if isinstance(x,Growth) else Growth(x)
def total(seq):
    seq=list(seq);out=seq[0]
    for x in seq[1:]:out=out+x
    return out

def constants(j,k='0.8',theta=1,eps='0.25',Rwin=4):
    j0=mp.mpf(j);j=Growth(j0,1,1);k=Growth(k);theta=Growth(theta);eps=Growth(eps);Rwin=Growth(Rwin)
    q=100*j;N=3*(2*j**4)*(2*j**4+1)**2;M=3*(2*j**4)**2*(2*j**4+1)
    Nq=3*q*(q+1)**2;Mq=3*q*q*(q+1);Cq=12*q*(q+1);a=1/(100*j);b=1/(k*a*a);c=2/(k*a)
    z=theta*k/j;e1=z*(1+eps+Rwin);e2=z*z*(eps+Rwin+eps*Rwin);e3=eps*Rwin*z**3
    A=4*b*M/k;G=4*mp.pi**2*N*c*c
    N3minus1=Growth(3*N.value-1,N.degree,3*N.leading)
    Wp=A+N3minus1*c;AQ=2*mp.pi*c*Nq**F(1,2);Ap=2*mp.pi*c*(Nq+3*Cq)**F(1,2)
    p1=2*b*(4*Mq+Cq)**F(1,2);px=2*b*Cq**F(1,2)
    p2=3*b*(16*Mq+Cq)**F(1,2);p2x=3*b*Cq**F(1,2);p2p=6*b*(4*Mq+Cq)**F(1,2)
    U={0:Growth(1),1:AQ,2:(3*Nq)**F(1,2)*Wp+AQ**2+AQ/mp.sqrt(2)}
    V={1:p1,2:p2,**{r:2*b*(Mq+Cq)*mp.mpf(3)**(mp.mpf(r)/2) for r in range(3,6)}}
    for m in range(3,7):
        B=total(math.comb(m-1,r)*V[r]*U[m-1-r] for r in range(1,m))/k
        U[m]=(2*mp.pi*U[m-1]*((2*A+G)*U[m-1]+B))**F(1,2)
    RR={m:total(math.comb(m,r)*U[r]*U[m-r] for r in range(m+1)) for m in range(1,7)}
    AM={0:Growth(1)}
    for m in range(1,7):
        AM[m]=total(abs(fall(F(-1,2),len(p)).numerator)/Growth(abs(fall(F(-1,2),len(p)).denominator))*total_product(RR[len(block)] for block in p) for p in partitions(m))
    d=3*Nq
    ccoef={6:k**3*d**F(3,2),5:6*k**3*U[1]*d,4:12*k**3*U[2]*d**F(1,2)+e1*k*k*d,
        3:8*k**3*U[3]+(6*k*k*p1+4*e1*k*k*U[1])*d**F(1,2),
        2:8*k*k*p2+12*k*k*p1*AQ+4*e1*k*k*U[2]+e2*k*d**F(1,2),
        1:6*k*k*p1+4*k*k*p2p*Ap+2*k*e1*p1+2*k*e2*U[1],0:e3}
    DT={l:total(math.comb(m,l)*ccoef[m]*AM[m-l] for m in range(l,7)) for l in range(6)}
    BT={l:(1-mp.mpf(l)/6)*((mp.mpf(l)/6)/(k**3/(10*DT[l])))**F(l,6-l) for l in range(1,6)}
    K=2/k**3*(DT[0]+total(DT[l]*BT[l] for l in range(1,6)))
    LL=2/k**3+K/e3;TH={l:LL**F(l,6)*e3**F(l-6,6) for l in range(7)}
    wc={5:6*k**3*U[1]*d,4:12*k**3*U[2]*d**F(1,2),
        3:8*k**3*U[3]+(6*k*k*px+4*e1*k*k*U[1])*d**F(1,2),
        2:8*k*k*p2x+12*k*k*p1*AQ+4*e1*k*k*U[2],
        1:6*k*k*px+4*k*k*p2p*Ap+2*k*e1*px+2*k*e2*U[1]}
    summands={m:wc[m]*total(math.comb(m,r)*AM[r]*TH[m-r] for r in range(m+1)) for m in range(1,6)}
    beta=total(summands.values())
    lead=2700*(mp.mpf(800)/27)**(mp.mpf(2)/3)*mp.mpf(9000000)**5*mp.mpf(960000)**3/(eps.value*Rwin.value*theta.value**3*k.value**6)
    ck(f'full original recurrence degree j{j0}',beta.degree==60 and abs(beta.leading/lead-1)<mp.mpf('1e-65'))
    return dict(j=str(j0),log10_beta=mp.nstr(mp.log10(beta.value),25),log10_leading_coefficient=mp.nstr(mp.log10(lead),25),
        ratio_to_leading=mp.nstr(beta.value/(lead*j0**60),25),
        degrees={name:{str(i):str(z.degree) for i,z in vals.items()} for name,vals in [('U',U),('R',RR),('inverse_multiplier',AM),('coefficients',ccoef),('transformed',DT),('theta',TH),('residual_coefficients',wc),('residual_summands',summands)]},
        K_degree=str(K.degree),L_degree=str(LL.degree),beta_degree=str(beta.degree))
def total_product(seq):
    out=Growth(1)
    for z in seq:out=out*z
    return out

path=[constants(j) for j in [4,5,8,16,64,1024,10**8,10**16]]
ck('asymptotic leading coefficient check',abs(mp.mpf(path[-1]['ratio_to_leading'])-1)<mp.mpf('1e-6'))
result=dict(checks=len(checks),all_passed=all(c['passed'] for c in checks),details=checks,path=path,
    scope='Exact rational noncommuting differential-jet identities through order six, every ordered subset and set partition; exact rational growth exponents with 80-digit evaluation of complete original-path bounds. Constructed algebraic fixtures are not Wilson ground samples and do not evaluate actual spectral mass.')
(O/'INVERSE_UNITARY_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=result['checks'],all_passed=result['all_passed'],j4=path[0],large_j=path[-1]['ratio_to_leading'])))
