from fractions import Fraction as F
from functools import lru_cache
import math
import mpmath as mp
mp.mp.dps=80

def mpf(x):return mp.mpf(x.numerator)/x.denominator if isinstance(x,F) else mp.mpf(x)
class Growth:
    def __init__(self,value,degree=0,leading=None):
        self.value=mpf(value);self.degree=F(degree);self.leading=mpf(value if leading is None else leading)
    def __add__(self,o):
        o=cast(o)
        if not self.value:return o
        if not o.value:return self
        d=max(self.degree,o.degree)
        return Growth(self.value+o.value,d,(self.leading if self.degree==d else 0)+(o.leading if o.degree==d else 0))
    __radd__=__add__
    def __mul__(self,o):
        o=cast(o);return Growth(self.value*o.value,self.degree+o.degree,self.leading*o.leading)
    __rmul__=__mul__
    def __truediv__(self,o):return self*cast(o)**F(-1)
    def __rtruediv__(self,o):return cast(o)*self**F(-1)
    def __pow__(self,p):
        p=F(p);q=mpf(p);return Growth(self.value**q,self.degree*p,self.leading**q)
def cast(x):return x if isinstance(x,Growth) else Growth(x)
def product(xs):
    out=Growth(1)
    for x in xs:out=out*x
    return out
def minus_one(x):return Growth(x.value-1,x.degree,x.leading)
def minimum(x,y):
    d=min(x.degree,y.degree)
    lead=min(x.leading,y.leading) if x.degree==y.degree else (x.leading if x.degree==d else y.leading)
    return Growth(min(x.value,y.value),d,lead)
@lru_cache(None)
def partitions(n):
    if n==0:return ((),)
    out=[]
    for p in partitions(n-1):
        out.append(p+((n-1,),))
        for k in range(len(p)):out.append(p[:k]+(p[k]+(n-1,),)+p[k+1:])
    return tuple(out)
def fall(z,n):return math.prod(z-i for i in range(n))
def triples(r):
    for a in range(r+1):
        for b in range(r-a+1):
            c=r-a-b;yield a,b,c,math.factorial(r)*2**c//(math.factorial(a)*math.factorial(b)*math.factorial(c))
def block_types(partition,m,r):
    return [(len(block)-2*sum(2*a in block and 2*a+1 in block for a in range(r)),sum(2*a in block and 2*a+1 in block for a in range(r))) for block in partition]
def polynomial(m,r,I):
    out={}
    for a,b,c,fac in triples(r):
        for s in range(m+1):
            l=m-s+c+2*b;term=fac*math.comb(m,s)*I[s+c,a]
            out[l]=out.get(l,0)+term
    return out

def constants(j,k='0.8',theta=1,eps='0.25',Rwin=4):
    j0=mpf(j);j=Growth(j0,1,1);k=Growth(k);theta=Growth(theta);eps=Growth(eps);Rwin=Growth(Rwin)
    q=100*j;N=3*(2*j**4)*(2*j**4+1)**2;M=3*(2*j**4)**2*(2*j**4+1)
    Nq=3*q*(q+1)**2;Mq=3*q*q*(q+1);Cq=12*q*(q+1);dall=3*N
    a=1/(100*j);b=1/(k*a*a);c=2/(k*a);A=4*b*M/k;G=4*mp.pi**2*N*c*c
    H=(A*A+2*minus_one(dall)*c*A+dall*minus_one(dall)*c*c)**F(1,2)
    AQ=2*mp.pi*c*Nq**F(1,2);Ap=2*mp.pi*c*(Nq+3*Cq)**F(1,2)
    p1=2*b*(4*Mq+Cq)**F(1,2);p2=3*b*(16*Mq+Cq)**F(1,2)
    px=2*b*Cq**F(1,2);p2x=3*b*Cq**F(1,2);p2p=6*b*(4*Mq+Cq)**F(1,2)
    vg={1:4*b*M**F(1,2),2:12*b*M**F(1,2),**{r:2*b*M*mp.mpf(3)**(mp.mpf(r)/2) for r in range(3,6)}}
    vl={1:p1,2:p2,**{r:2*b*(Mq+Cq)*mp.mpf(3)**(mp.mpf(r)/2) for r in range(3,6)}}
    Ug={0:Growth(1),1:G**F(1,2),2:H+G+(G/2)**F(1,2)}
    Ul={0:Growth(1),1:AQ,2:H+AQ*AQ+AQ/mp.sqrt(2)}
    for U,V in [(Ug,vg),(Ul,vl)]:
        for m in range(3,7):
            BB=sum(math.comb(m-1,r)*V[r]*U[m-1-r] for r in range(1,m))/k
            U[m]=(2*mp.pi*U[m-1]*((2*A+G)*U[m-1]+BB))**F(1,2)
    def ff(kk,aa):
        if kk:return 3**aa*vg[kk]/k
        return A if aa==0 else (6*b*M/k)*3**(aa-1)
    E={(m,0):Ug[m] for m in range(7)}
    for r in range(1,4):
        for m in range(7-2*r):
            E[m,r]=sum(fac*math.comb(m,s)*ff(s+cc,aa)*E[m-s+cc,bb] for aa,bb,cc,fac in triples(r-1) for s in range(m+1))
    RR={(m,0):sum(math.comb(m,s)*Ul[s]*Ul[m-s] for s in range(m+1)) for m in range(7)}
    for r in range(1,4):
        for m in range(7-2*r):
            RR[m,r]=sum(fac*math.comb(m,s)*E[s+cc,aa]*E[m-s+cc,bb] for aa,bb,cc,fac in triples(r) for s in range(m+1))
    II={(0,0):Growth(1)}
    for n in range(1,7):
        for r in range(n//2+1):
            m=n-2*r
            II[m,r]=sum(abs(fall(F(-1,2),len(pi)))*product(RR[typ] for typ in block_types(pi,m,r)) for pi in partitions(n))
    PP={(m,r):polynomial(m,r,II) for r in range(4) for m in range(7-2*r)}
    z=theta*k/j;e1=z*(1+eps+Rwin);e2=z*z*(eps+Rwin+eps*Rwin);e3=eps*Rwin*z**3
    def coef(pf,p2f):return {(1,2):6*k**3*Ul[1],(2,1):12*k**3*Ul[2],(3,0):8*k**3*Ul[3],
        (1,1):6*k*k*pf+4*e1*k*k*Ul[1],(2,0):8*k*k*p2f+12*k*k*p1*AQ+4*e1*k*k*Ul[2],
        (1,0):6*k*k*pf+4*k*k*p2p*Ap+2*e1*k*pf+2*e2*k*Ul[1]}
    dc=coef(p1,p2);rc=coef(px,p2x)
    D={}
    for mr,coef0 in [((0,3),k**3),((0,2),e1*k*k),((0,1),e2*k),((0,0),e3),*dc.items()]:
        for l,v in PP[mr].items():
            if l<6:D[l]=D.get(l,0)+coef0*v
    dh={l:D[l] for l in range(4)}
    d4direct=e1*k*k+3*k**3*(A+G)+12*k**3*AQ*AQ
    dh[4]=minimum(D[4],d4direct)
    et={l:k**3/(8*dh[l]) for l in range(1,5)}
    bt={l:F(6-l,6)*(F(l,6)/et[l])**F(l,6-l) for l in range(1,5)}
    KK=2/k**3*(dh[0]+sum(dh[l]*bt[l] for l in range(1,5)))
    LL=2/k**3+KK/e3;TH={l:LL**F(l,6)*e3**F(l-6,6) for l in range(7)}
    pvalues={mr:sum(v*TH[l] for l,v in p.items()) for mr,p in PP.items()}
    energy=1/(2*(k*e2*e3)**F(1,2))
    terms={mr:cc*(minimum(pvalues[mr],energy) if mr==(1,0) else pvalues[mr]) for mr,cc in rc.items()}
    beta=sum(terms.values())
    return dict(j=str(j0),H=H,Ug=Ug,Ul=Ul,E=E,RR=RR,II=II,PP=PP,D=D,dh=dh,KK=KK,LL=LL,TH=TH,terms=terms,beta=beta,energy=energy,d4direct=d4direct,
        original=dict(N=N,M=M,Nq=Nq,Mq=Mq,Cq=Cq,A=A,G=G,AQ=AQ))

def report(x):
    return dict(j=x['j'],log10_beta=mp.nstr(mp.log10(x['beta'].value),25),beta_degree=str(x['beta'].degree),log10_leading=mp.nstr(mp.log10(x['beta'].leading),25),
        ratio_to_leading=mp.nstr(x['beta'].value/(x['beta'].leading*mp.mpf(x['j'])**mpf(x['beta'].degree)),25),
        degrees={name:{str(k):str(v.degree) for k,v in x[name].items()} for name in ['Ug','Ul','E','RR','II','dh','TH','terms']},
        K_degree=str(x['KK'].degree),L_degree=str(x['LL'].degree),H_degree=str(x['H'].degree),first_derivative_degree=str(x['energy'].degree))

def leading_coefficient(k='0.8',theta=1,eps='0.25',Rwin=4):
    k=mpf(k);theta=mpf(theta);eps=mpf(eps);Rwin=mpf(Rwin)
    aa=mp.mpf(960000)/k**2;gg=mp.mpf(3840000)*mp.pi**2/k**2
    gam=mp.sqrt(2*mp.pi*(2*aa+gg));ee=eps*Rwin*theta**3*k**3
    u={0:mp.mpf(1),1:mp.sqrt(gg),**{m:(aa+gg)*gam**(m-2) for m in range(2,7)}}
    uq={0:mp.mpf(1),1:mp.mpf(0),**{m:aa*gam**(m-2) for m in range(2,7)}}
    RR={(m,0):sum(math.comb(m,s)*uq[s]*uq[m-s] for s in range(m+1)) for m in range(7)}
    for r in range(1,4):
        for m in range(7-2*r):RR[m,r]=sum(fac*math.comb(m,s)*aa**(a+b)*u[s+c]*u[m-s+c] for a,b,c,fac in triples(r) for s in range(m+1))
    II={(0,0):mp.mpf(1)}
    for n in range(1,7):
        for r in range(n//2+1):
            m=n-2*r
            II[m,r]=sum(mpf(abs(fall(F(-1,2),len(pi))))*math.prod(RR[t] for t in block_types(pi,m,r)) for pi in partitions(n))
    pp={mr:polynomial(*mr,II) for mr in [(0,3),(2,1),(3,0)]}
    dd={l:k**3*(pp[0,3].get(l,0)+12*aa*pp[2,1].get(l,0)+8*aa*gam*pp[3,0].get(l,0)) for l in range(4)}
    dd[4]=3*k**3*(aa+gg)
    KK=2/k**3*(dd[0]+sum((1-mp.mpf(l)/6)*(8*mp.mpf(l)/(6*k**3))**(mp.mpf(l)/(6-l))*dd[l]**(mp.mpf(6)/(6-l)) for l in range(1,5)))
    evaluate=lambda p:sum(v*KK**(mp.mpf(l)/6) for l,v in p.items())
    return k**3/ee*(12*aa*evaluate(pp[2,1])+8*aa*gam*evaluate(pp[3,0]))
