from fractions import Fraction as F
import math
from contracted_constants import constants as prior_constants,Growth,minimum,partitions,fall,product,triples,block_types,mp,mpf,minus_one

def constants(j,k='0.8',theta=1):
    old=prior_constants(j,k=k,theta=theta,eps='0.25',Rwin=4)
    jj=Growth(j,1,1);kap=Growth(k);th=Growth(theta);a=1/(100*jj)
    b=1/(kap*a*a);z=th*kap/jj;e1=F(21,4)*z;e2=F(21,4)*z*z;e3=z**3
    N,M,A,G,AQ=[old['original'][n] for n in ['N','M','A','G','AQ']]
    cc=2/(kap*a);K=A+minus_one(3*N)*cc
    U=old['Ug'];v1=4*b*M**F(1,2);v2=12*b*M**F(1,2)
    RR=old['RR'];II=old['II'];TH=old['TH']
    HH={(0,0):Growth(1)}
    for n in range(1,7):
        for rr in range(n//2+1):
            mm=n-2*rr
            HH[mm,rr]=sum(abs(fall(F(1,2),len(pi)))*product(RR[typ] for typ in block_types(pi,mm,rr)) for pi in partitions(n))
    def upot(m,r):
        return kap*sum(fac*math.comb(m,ss)*II[ss+c,aa]*HH[m-ss+c,bb+1]
                       for aa,bb,c,fac in triples(r) for ss in range(m+1))
    VV={mr:upot(*mr) for mr in [(1,0),(2,0),(1,1)]}
    DD={mr:sum(v*TH[l] for l,v in p.items()) for mr,p in old['PP'].items()}
    E0=1/e3;E1=1/(2*(kap*e2*e3)**F(1,2))
    EL=1/(2*(e1*e3)**F(1,2));E32=1/(2*e3**F(1,2))
    B01=EL/kap+2*AQ*E1
    B20=(EL*EL/(kap*kap)+2*K*E1*E1)**F(1,2)
    B11=E32/(kap**F(3,2))+2*K*E1+2*AQ*B20
    M32=E32+2*kap**F(1,2)*AQ*EL
    M3=(kap**3*DD[0,3]+6*kap**3*HH[1,0]*DD[1,2]
        +12*kap**3*HH[2,0]*DD[2,1]+8*kap**3*HH[3,0]*DD[3,0]
        +6*kap*kap*VV[1,0]*DD[1,1]+8*kap*kap*VV[2,0]*DD[2,0]
        +12*kap*kap*VV[1,0]*HH[1,0]*DD[2,0]
        +2*kap*kap*VV[1,1]*DD[1,0]+4*kap*kap*HH[1,0]*VV[2,0]*DD[1,0])
    M2=M32**F(2,3)*M3**F(1,3)
    B02=M2/(kap*kap)+4*AQ*B11+4*HH[2,0]*B20+2*VV[1,0]*E1/kap
    trial={(0,0):E0,(1,0):minimum(DD[1,0],E1),(0,1):minimum(DD[0,1],B01),
           (2,0):minimum(DD[2,0],B20),(1,1):minimum(DD[1,1],B11),(0,2):minimum(DD[0,2],B02)}
    AA0=A+U[1]*U[1];AA1=A*U[1]+v1/kap+U[1]*U[2]
    AA2=A*U[2]+(v2+2*v1*U[1])/kap+U[1]*U[3]
    DV=6*b*M+2*U[1]*v1;DVi=3*v1+2*U[1]*v2
    EE=6*b*M*U[1]+v1*U[2]+U[1]*U[1]*v1+2*U[1]*v2+2*v1*AA0
    DX=(U[2]+U[1]*U[1])*v2+2*U[1]*v1
    C={(0,2):6*kap**3*U[1],(0,1):4*e1*kap*kap*U[1]+6*kap*kap*v1,
       (0,0):2*kap*e2*U[1]+(6*kap*kap+2*e1*kap)*v1+4*kap*kap*U[1]*v2,
       (1,1):12*kap**3*U[2],(1,0):4*e1*kap*kap*U[2]+8*kap*kap*v2+12*kap*kap*v1*U[1],
       (2,0):8*kap**3*U[3]}
    T={(0,2):6*kap**3*AA0,(0,1):4*e1*kap*kap*AA0+6*kap*kap*DV,
       (0,0):2*kap*e2*AA0+(6*kap*kap+2*e1*kap)*DV+4*kap*kap*DX,
       (1,1):12*kap**3*AA1,(1,0):4*e1*kap*kap*AA1+8*kap*kap*DVi+4*kap*kap*EE,
       (2,0):8*kap**3*AA2}
    fterms={mr:C[mr]*trial[mr] for mr in C}
    sterms={mr:(T[mr]+2*U[1]*C[mr])*trial[mr] for mr in C}
    Fsum=sum(fterms.values());Ssum=sum(sterms.values())
    energy=Fsum*Fsum/kap+Ssum*Ssum/z
    oldenergy=old['beta']**2/z;best=minimum(energy,oldenergy)
    return dict(j=str(j),k=str(k),theta=str(theta),old=old,HH=HH,VV=VV,DD=DD,K=K,E0=E0,E1=E1,EL=EL,E32=E32,
                B01=B01,B20=B20,B11=B11,B02=B02,M32=M32,M3=M3,M2=M2,
                trial=trial,C=C,T=T,fterms=fterms,sterms=sterms,Fsum=Fsum,Ssum=Ssum,
                energy=energy,oldenergy=oldenergy,best=best)

def leading_energy(k='0.8',theta=1):
    k=mpf(k);theta=mpf(theta)
    aa=mp.mpf(960000)/k**2;gg=mp.mpf(3840000)*mp.pi**2/k**2
    u1=mp.sqrt(gg);u2=aa+gg;gam=mp.sqrt(2*mp.pi*(2*aa+gg));u3=u2*gam
    d=1/(mp.sqrt(21)*theta**mp.mpf('2.5')*k**3)
    d02=4*(aa*mp.sqrt(2*aa)+u1*(2*aa+gg))*d
    d11=2*aa*d;d20=mp.sqrt(2*aa)*d
    S=k**3*(6*(aa+3*gg)*d02+12*u1*(4*aa+3*gg)*d11+8*(aa*u2+3*u1*u3)*d20)
    return S*S/(theta*k)

def report(d):
    return dict(j=d['j'],log10_energy=mp.nstr(mp.log10(d['energy'].value),30),
                degree=str(d['energy'].degree),log10_old_energy=mp.nstr(mp.log10(d['oldenergy'].value),30),
                ratio_to_leading=mp.nstr(d['energy'].value/(d['energy'].leading*mp.mpf(d['j'])**mpf(d['energy'].degree)),30),
                leading_ratio=mp.nstr(d['energy'].leading/leading_energy(d['k'],d['theta']),30),
                degrees={n:({str(k):str(v.degree) for k,v in d[n].items()} if isinstance(d[n],dict) else str(d[n].degree))
                         for n in ['HH','VV','trial','C','T','Fsum','Ssum','M32','M3','M2','B02','fterms','sterms']})

if __name__=='__main__':
    import json
    for j in [4,16,10**8,10**32]:print(json.dumps(report(constants(j))))
