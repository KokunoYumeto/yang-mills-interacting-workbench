from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json, math
HERE=Path(__file__).resolve().parent
counts={"polynomial spectral bound":0,"optimized original spectral window":0,
        "local upper and lower root":0,"root asymptotics":0}
lam=[Q(1,5),Q(1),Q(3),Q(8)]
for weights in product([Q(0),Q(1,7),Q(2,5),Q(1)],repeat=4):
    E=sum(w*l for w,l in zip(weights,lam))
    if E==0:continue
    E2=sum(w*l*l for w,l in zip(weights,lam))
    for R in [Q(1,10),Q(1,2),Q(1),Q(3),Q(8),Q(15),2*E2/E]:
        mass=sum(w for w,l in zip(weights,lam) if l<=R)
        assert mass>=4*(E-E2/R)/R
        counts["polynomial spectral bound"]+=1
    R=2*E2/E;mass=sum(w for w,l in zip(weights,lam) if l<=R)
    assert mass>=E*E/E2
    counts["optimized original spectral window"]+=1
for kappa,R in product([.3,1.,3.],[.2,.7,2.]):
    LR=9*kappa*R**3+24*R**2
    disc=LR*LR-81*kappa*kappa*R**6/4
    dm=81*kappa*kappa*R**6/(8*(LR+math.sqrt(disc)))
    dp=(LR+math.sqrt(disc))/2
    # Stable rationalized lower root: product is 81 kappa^2 R^6 / 16.
    dm=(81*kappa*kappa*R**6/16)/dp
    assert 0<dm<dp<LR
    assert abs(dm+dp-LR)<1e-12*LR
    counts["local upper and lower root"]+=1
    errors=[]
    for j in [10,100,1000,10000]:
        a=1/(100*j);q=math.ceil(R/a)+3
        N=3*q*(q+1)**2;M=3*q*q*(q+1);C=12*q*(q+1)
        Lam=min(2*M,3*kappa*a*math.sqrt(N*M))+2*C
        xi=1/(kappa*kappa*a*a);A=9+64*xi;B=36*M+64*xi*Lam
        delta=B*B-144*A*M*M
        low=72*M*M/(B+math.sqrt(delta))
        high=(B+math.sqrt(delta))/(2*A)
        err=max(abs(a*a*low-dm),abs(a*a*high-dp))/dp
        errors.append(err)
        assert low>0 and low<Lam and high>=low
        counts["local upper and lower root"]+=1
    assert errors[-1]<errors[0]/100 and errors[-1]<1e-4
    counts["root asymptotics"]+=1
result={"passed":True,"check_count":sum(counts.values()),"groups":counts}
(HERE/"ORIGINAL_SOURCE_STRENGTHENED_CHECKS.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
