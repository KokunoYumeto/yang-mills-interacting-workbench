"""Check original face incidences, tail constants and full matrix identities."""
from pathlib import Path
import itertools, hashlib, json
import sympy as s
HERE=Path(__file__).resolve().parent; checks={}
def eq(name,a,b=0):
    assert s.simplify(a-b)==0,name
    checks[name]=True
def yes(name,value):
    assert value,name
    checks[name]=True
for m in [2,4,6]:
    faces=[]
    for i,j in itertools.combinations(range(3),2):
        for z in itertools.product(range(m+1),repeat=3):
            if z[i]>=m or z[j]>=m: continue
            zi=list(z);zi[i]+=1
            zj=list(z);zj[j]+=1
            faces.append(frozenset([(z,i),(tuple(zi),j),(tuple(zj),i),(z,j)]))
    incidence={}
    for k,f in enumerate(faces):
        for e in f: incidence.setdefault(e,[]).append(k)
    graph=[set() for _ in faces]
    for group in incidence.values():
        for a in group: graph[a].update(set(group)-{a})
    colours=[]
    for k,adj in enumerate(graph):
        used={colours[a] for a in adj if a<k}
        colours.append(next(c for c in range(13) if c not in used))
    eq(f"original face count m={m}",len(faces),3*m*m*(m+1))
    eq(f"all boundary incidences m={m}",sum(map(len,incidence.values())),4*len(faces))
    yes(f"thirteen disjoint-support classes m={m}",
        all(colours[a]!=colours[b] for a,adj in enumerate(graph) for b in adj))
    yes(f"degree bound twelve m={m}",max(map(len,graph))<=12)
    yes(f"at most one shared link m={m}",
        all(len(faces[a]&faces[b])==1 for a,adj in enumerate(graph) for b in adj))
q=s.symbols("q")
eq("complete one-link heat tail",
   (1+q)/(1-q)**3-1,(4*q-3*q*q+q**3)/(1-q)**3)
eq("heat-tail majorant numerator",
   8*q*(1-q)**3-(4*q-3*q*q+q**3),q*(4-21*q+23*q*q-8*q**3))
yes("heat-tail remainder positive",4-s.Rational(21,16)-s.Rational(8,16**3)>0)
eq("Haar exponential Markov exponent",-s.Rational(1,52)+s.Rational(26,52**2),-s.Rational(1,104))
eq("electric trace budget remainder",s.Rational(1,208)-s.Rational(1,256),s.Rational(3,3328))
yes("exact exponential budget integer inequality",12*2**12*3328<=3*5**12)
eq("colour Holder factor",2*13**2/s.Integer(13),26)
k,j=s.symbols("k j",positive=True)
M=3*(2*j**4)**2*(2*j**4+1);N=3*(2*j**4)*(2*j**4+1)**2
g2=k/(200*j);a=1/(100*j)
eq("unchanged original electric coefficient",2*g2/a,k)
eq("full original face boundary expansion",M,24*j**12+12*j**8)
eq("actual potential receiving fraction",6*g2*s.sqrt(N/M),3*k/(100*j)*s.sqrt((2*j**4+1)/(2*j**4)))
eq("vacuum energy lower leading coefficient",s.limit(k*M/(4096*j**12),j,s.oo),3*k/512)
eq("density oscillation on original path",32*s.pi/(4*g2**2)*M,320000*s.pi*j*j*M/k**2)
eq("retained vacuum-energy upper scalar",M/(g2*a),20000*j*j*M/k)
c=s.symbols("c",real=True)
rho=s.Matrix([[1,0],[0,0]])-s.Matrix([c,s.sqrt(1-c*c)])*s.Matrix([[c,s.sqrt(1-c*c)]])
eq("rank-two projection difference characteristic",
   rho.charpoly().as_expr(),s.Symbol("lambda")**2-(1-c*c))
x,y=s.symbols("x y")
for p in range(1,5):
    for r in range(p):
        F=x**p*y**r-x**r*y**p;n=p+r
        for i,z in enumerate([x,y]):
            cf=sum(abs(v) for v in s.Poly(s.diff(F,z),x,y).coeffs())
            yes(f"full first derivative coefficient p={p} q={r} i={i}",cf<=n)
        max2=max(sum(abs(v) for v in s.Poly(s.diff(F,z,w),x,y).coeffs())
                 for z in [x,y] for w in [x,y])
        yes(f"all four second derivative coefficients p={p} q={r}",max2<=n*(n-1))
# A non-orthonormal physical receiving map and a full complementary operator.
J=s.Matrix([[1,1],[0,2],[1,-1],[0,1]])
A=s.Matrix([[5,1,0,1],[1,6,2,0],[0,2,7,1],[1,0,1,8]])
G=J.T*J;C=J.T*A*J;Q=J.T*A*A*J;Pi=J*G.inv()*J.T
yes("original non-unit Gram positive",G.det()>0 and G[0,0]>0)
eq("exact finite physical projection",(Pi*Pi-Pi).norm(),0)
eq("entire complementary second moment",
   (Q-C*G.inv()*C-J.T*A*(s.eye(4)-Pi)*A*J).norm(),0)
Cp=s.Matrix([[2,1],[1,3]]);Gp=s.Matrix([[3,1],[1,4]])
D=C-Cp
eq("complete inverse perturbation identity",
   (G.inv()-Gp.inv()-G.inv()*(Gp-G)*Gp.inv()).norm(),0)
eq("all residual perturbation terms",
   (C*G.inv()*C-Cp*Gp.inv()*Cp
    -(D*G.inv()*D+D*G.inv()*Cp+Cp*G.inv()*D
      +Cp*(G.inv()-Gp.inv())*Cp)).norm(),0)
proof=HERE.parent/("PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md" if HERE.name=="checks"
                  else "ACTUAL_VACUUM_AND_PHASE_MATRIX_ENCLOSURES_20261009.md")
out={"all_passed":True,"check_count":len(checks),"checks":checks,
     "proof_sha256":hashlib.sha256(proof.read_bytes()).hexdigest(),
     "scope":"Finite exact algebra and original-box incidence checks. The actual-vacuum concentration, gap, cutoff convergence and spectral-weight bounds are proved in the complete written argument.",
     "actual_vacuum_numerical_sampling":False,"independent_review":False}
(HERE/"VACUUM_MATRIX_ENCLOSURE_CHECK.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps({"exact_checks":len(checks),"all_passed":True}))
