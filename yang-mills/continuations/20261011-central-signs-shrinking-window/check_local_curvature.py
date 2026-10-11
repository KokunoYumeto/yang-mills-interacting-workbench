"""Exact combinatorial/algebraic and high-precision receiving checks."""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction as F
import json
import math
import sympy as s
import mpmath as mp

HERE=Path(__file__).resolve().parent
counts=Counter()

def edge_face(x,d,e):
    xd=list(x); xd[d]+=1
    xe=list(x); xe[e]+=1
    return [(x,d),(tuple(xd),e),(tuple(xe),d),(x,e)]

for m in range(1,7):
    vertices=list(product(range(m+1),repeat=3))
    edges=[(x,d) for x in vertices for d in range(3) if x[d]<m]
    faces=[(d,e,edge_face(x,d,e)) for x in vertices
           for d,e in [(0,1),(0,2),(1,2)] if x[d]<m and x[e]<m]
    for q in range(1,m+1):
        for v in product(range(m-q+1),repeat=3):
            def inside_vertex(x):
                return all(v[d]<=x[d]<=v[d]+q for d in range(3))
            inside=set()
            for x,d in edges:
                y=list(x); y[d]+=1
                if inside_vertex(x) and inside_vertex(y): inside.add((x,d))
            incidence=Counter()
            classes=Counter()
            cross_orientation=Counter()
            for d,e,es in faces:
                number=sum(edge in inside for edge in es)
                assert number in (0,1,4)
                classes[number]+=1
                if number==1:
                    cross_orientation[d,e]+=1
                    counts["crossing_one_inside_three_outside"]+=1
                if number==4:
                    incidence.update(es)
            side=[int(v[d]>0)+int(v[d]+q<m) for d in range(3)]
            assert len(inside)==3*q*(q+1)**2
            assert classes[4]==3*q*q*(q+1)
            assert classes[1]==2*q*(q+1)*sum(side)
            assert classes[0]==3*m*m*(m+1)-classes[4]-classes[1]
            assert max(incidence.values())<=4
            assert sum(incidence.values())==12*q*q*(q+1)
            for d,e in [(0,1),(0,2),(1,2)]:
                assert cross_orientation[d,e]==q*(q+1)*(side[d]+side[e])
            counts["all_patch_positions_and_boundaries"]+=1

# Exact oriented gauge action on every possible inside position of a face.
I=s.I
sigmas=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.Matrix([[1,0],[0,-1]])]
generators=[-I*x/2 for x in sigmas]
assert sum((T*T for T in generators),s.zeros(2)) == -s.Rational(3,4)*s.eye(2)
counts["radius_two_Casimir"]+=1
points=[(s.Rational(3,5),s.Rational(4,5),0,0),
        (0,s.Rational(3,5),s.Rational(4,5),0),
        (s.Rational(5,13),0,0,s.Rational(12,13)),
        (s.Rational(1,2),s.Rational(1,2),s.Rational(1,2),s.Rational(1,2))]
Us=[x[0]*s.eye(2)-I*sum((x[i+1]*sigmas[i] for i in range(3)),s.zeros(2)) for x in points]
path=[Us[0],Us[1],Us[2].H,Us[3].H]
def prod(mats):
    out=s.eye(2)
    for mat in mats: out=out*mat
    return s.simplify(out)
for k in range(4):
    cyclic=path[k:]+path[:k]
    outside=cyclic[1:]
    P=prod(outside)
    # Gauge -I at the final endpoint of the outside path changes only
    # the final path traversal among its three traversals.
    signed=outside[:-1]+[-outside[-1]]
    assert s.simplify(prod(signed)+P)==s.zeros(2)
    assert s.simplify(s.trace(prod(cyclic))-s.trace(prod(path)))==0
    counts["exact_oriented_crossing_gauge_signs"]+=1
W=s.trace(prod(path))
lap_total=sum(s.trace(prod(path[:k]+[generators[a]*generators[a]*path[k]]+path[k+1:]))
              for k in range(4) for a in range(3))
assert s.simplify(lap_total+3*W)==0
counts["full_face_Casimir_eigenvalue"]+=1

kap,b,N,M=s.symbols("kap b N M",positive=True)
t=4*s.sqrt(b*M/(kap*N))
trial=3*kap*N*t/8+6*b*M/t
assert s.simplify(trial-3*s.sqrt(kap*b*N*M))==0
g2,a=s.symbols("g2 a",positive=True)
assert s.simplify((4*kap/b).subs({kap:2*g2/a,b:1/(2*g2*a)})-16*g2*g2)==0
assert s.simplify((b/kap).subs({kap:2*g2/a,b:1/(2*g2*a)})-1/(4*g2*g2))==0
q,eta=s.symbols("q eta",positive=True)
assert s.simplify(2*(2*q*(q+1)*eta)/(3*q*q*(q+1))-4*eta/(3*q))==0
counts["exact_energy_and_surface_factors"]+=4

# Preserve the full potential scalar and outside energy in the jet identity.
f,fx,fxx,ps,px,pxx,V,E,Eout=s.symbols("f fx fxx ps px pxx V E Eout",nonzero=True)
expanded=kap*(pxx*f+2*px*fx+ps*fxx)/ps-(V-E)*f
assert s.simplify(expanded.subs(pxx,(V-E)*ps/kap)-(kap*fxx+2*kap*px*fx/ps))==0
counts["ground_equation_scalar_cancellation"]+=1

for qq in [1,2,4,17]:
    for coupling in [F(1,1000),F(1,5),F(3,2)]:
        # q(q+1) chosen square in none is unnecessary: use a rational
        # overestimate parameter independently to check the moment algebra.
        Lambda=F(24*qq*(qq+1))+F(18)*coupling*(qq+1)**3
        rho=4*coupling
        U=[F(1),Lambda]
        for k in range(1,13): U.append(Lambda*U[k]+rho*rho*k*k*U[k-1])
        assert U[2]==Lambda*Lambda+rho*rho
        assert U[3]==Lambda**3+5*Lambda*rho*rho
        for k in range(1,14):
            assert U[k]<=(Lambda+rho*k)**k
            counts["exact_local_moment_majorants"]+=1
        for zz in [4*rho,7*rho,33*rho,Lambda+4*rho]:
            kk=math.floor(zz/(2*rho))
            assert kk>=zz/(4*rho)
            assert (Lambda+rho*kk)/(Lambda+zz)<=1-zz/(2*(Lambda+zz))
            counts["exact_local_tail_rounding"]+=1

for j in [2,3,5,11]:
    aa=F(1,100*j); LL=j**4
    for R in [F(1,100),F(13,100),F(7,3)]:
        qq=math.ceil(R/aa)+3
        for cd in [F(-7,10),F(0),F(2,7)]:
            vv=LL+math.floor(cd/aa)-1
            lower=aa*(vv-LL)
            upper=lower+aa*qq
            assert cd-2*aa<lower<=cd-aa
            assert upper>=cd+R+aa
            counts["physical_patch_floor_ceiling_checks"]+=1

eps,Fmax,aa,Lambda,kappa,T,Rc=s.symbols("eps Fmax aa Lambda kappa T Rc",positive=True)
r=eps*Fmax*aa**3*Lambda/2
c=16*kappa*Rc
assert s.simplify(2*r*r/(9*c*T)-eps**2*Fmax**2*aa**6*Lambda**2/(288*kappa*T*Rc))==0
counts["full_time_tail_constant"]+=1

mp.mp.dps=65
rows=[]
for kappa in [mp.mpf("0.4"),mp.mpf(1),mp.mpf(7)]:
    for R in [mp.mpf("0.1"),mp.mpf(1),mp.sqrt(2)]:
        for j in [10,1000,1000000]:
            aa=mp.mpf(1)/(100*j)
            qq=mp.ceil(R/aa)+3
            NN=3*qq*(qq+1)**2; MM=3*qq**2*(qq+1)
            CC=12*qq*(qq+1); g2=kappa/(200*j); rho=4*g2
            L=min(2*MM,6*g2*mp.sqrt(NN*MM))+2*CC
            CR=9*kappa*R**3/100+6*R**2/25
            target_average=3*kappa/100+2/(25*R)
            rows.append({"kappa":str(kappa),"R":str(R),"j":j,
                         "j_a3_Lambda":mp.nstr(j*aa**3*L,24),
                         "C_R":mp.nstr(CR,24),
                         "j_Lambda_over_M":mp.nstr(j*L/MM,24),
                         "target_average":mp.nstr(target_average,24)})
            counts["finite_original_patch_path_checks"]+=1
        assert abs(j*aa**3*L/CR-1)<mp.mpf("1e-6")
        assert abs((j*L/MM)/target_average-1)<mp.mpf("1e-6")
        assert abs((j*aa**3*mp.sqrt(L*L+rho*rho))/CR-1)<mp.mpf("1e-6")
        assert abs((10000*L/(kappa*kappa*j*j))/(mp.mpf(10)**10*CR/(kappa*kappa))-1)<mp.mpf("1e-6")
        counts["patch_path_limit_comparisons"]+=4

result={"status":"PASS","counts":dict(counts),"total_groups":sum(counts.values()),
        "path_rows":rows,"scope":"Exact finite geometry and algebra; no sampled or substituted vacuum."}
(HERE/"LOCAL_CURVATURE_CHECKS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:result[k] for k in ["status","counts","total_groups"]},indent=2))
