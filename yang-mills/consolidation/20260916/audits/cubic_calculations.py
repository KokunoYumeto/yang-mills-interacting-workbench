"""Independent rational/geometry audit; imports no delivered verification code."""
from fractions import Fraction as F
from itertools import product, combinations
from collections import defaultdict, Counter
from hashlib import sha256
from pathlib import Path
import json

root=Path(__file__).resolve().parents[3]/'continuations/20260916-cubic-linearized'
rows={}
c_pair={0:F(9,2),1:F(13,2)}
a_pair={0:F(1,27),1:-F(1,117)}
rows['path']={}
for s,t in product((0,1),repeat=2):
    c=F(6+2*(s+t))
    a=(a_pair[s]*(3+c_pair[s]-c)+a_pair[t]*(3+c_pair[t]-c))/(3*c)
    rows['path'][str((s,t))]=str(a)
rows['corner']={}
for n in range(4):
    c=F(9,2)+2*n
    rows['corner'][str(n)]=str(((3-n)*a_pair[0]*(3+c_pair[0]-c)+n*a_pair[1]*(3+c_pair[1]-c))/(3*c))
rows['common']={}
for c,b0,b1 in [(F(15,2),F(3,2),F(3,2)),(F(21,2),0,3)]:
    rows['common'][str(c)]=str((b0*a_pair[0]*(3+c_pair[0]-c)+b1*a_pair[1]*(3+c_pair[1]-c))/(3*c))
rows['repeated_K_coefficients']={'H':str(-F(1,72)-F(1,2808)-F(1,108)), 'J':str(F(5,702)+F(1,216)), 'lower_Wq':str(F(1,72)-F(1,72))}
rows['cubic_bound']=str(4*F(40,27)+84*F(66,13)+460*F(1408,351)+40*F(512,117)+24*F(3504,351))
ell=lambda x:F(128,3)*x+F(3132,13)*x*x
delta=lambda x:F(944984,351)*x**3+F(799258,39)*x**4
D=lambda x:(1-ell(x))**2-F(8,3)*delta(x)
polynomial=lambda x:(46457856*x**4+183150656*x**3+18324072*x*x-1168128*x+13689)/13689
for x in [F(0),F(1,64),F(17,1000),F(171,10000)]:
    assert D(x)==polynomial(x)
rows['D_at_1_over_64']=str(D(F(1,64)))
alpha_lo=F('0.0170787544707772675')
alpha_hi=F('0.0170787544707772677')
assert D(alpha_lo)>0>D(alpha_hi)
g2lo=F('3.825973052393385');g2hi=F('3.825973052393386')
assert 4*alpha_hi*g2lo*g2lo<1<4*alpha_lo*g2hi*g2hi
rows['alpha_bracket']=[str(alpha_lo),str(alpha_hi)]
rows['g_squared_bracket']=[str(g2lo),str(g2hi)]

# Construct each original square as four unoriented geometric edges, each edge
# represented by its sorted endpoint pair. No imported face/edge functions.
unit=[tuple(int(a==b) for a in range(3)) for b in range(3)]
plus=lambda x,y:tuple(a+b for a,b in zip(x,y))
faces={}
incidence=defaultdict(set)
for n in product(range(-3,4),repeat=3):
    for i,j in combinations(range(3),2):
        v=(n,plus(n,unit[i]),plus(plus(n,unit[i]),unit[j]),plus(n,unit[j]))
        edges=frozenset(tuple(sorted((v[k],v[(k+1)%4]))) for k in range(4))
        p=n+(i,j); faces[p]=edges
        for e in edges:incidence[e].add(p)
anchor=((0,0,0),(1,0,0))
neighbors={p:set().union(*(incidence[e] for e in es))-{p} for p,es in faces.items()}
pairs=set();triples=set()
for p in incidence[anchor]:
    for q in neighbors[p]:
        pairs.add(frozenset((p,q)))
        for r in (neighbors[p]|neighbors[q])-{p,q}:
            triples.add(frozenset((p,q,r)))
counts=Counter()
for ps in triples:
    a,b,c=tuple(ps)
    adjacent=sum(bool(faces[p]&faces[q]) for p,q in combinations(ps,2))
    if adjacent==2:typ='path'
    elif faces[a]&faces[b]&faces[c]:typ='common'
    else:typ='corner'
    counts[typ]+=1
    assert adjacent in (2,3)
    assert len(set().union(*(faces[p] for p in ps)))==({'path':10,'common':10,'corner':9}[typ])
rows['independent_incidence_census']={'anchor_faces':len(incidence[anchor]),'adjacent_pairs':len(pairs),**counts,'connected_multisets':len(incidence[anchor])+2*len(pairs)+sum(counts.values())}
assert rows['independent_incidence_census']=={'anchor_faces':4,'adjacent_pairs':42,'path':460,'common':40,'corner':24,'connected_multisets':612}
rows['source_sha256']={name:sha256((root/name).read_bytes()).hexdigest() for name in ['CUBIC_SOURCE.md','LINEARIZED_RETURN.md','coordinate_audit.py','geometry.py']}
print(json.dumps(rows,indent=2))
