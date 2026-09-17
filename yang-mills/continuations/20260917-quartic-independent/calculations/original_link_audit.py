"""Independent second-order jets through original links and the exact tree map."""
from fractions import Fraction as F
from pathlib import Path
from collections import defaultdict,deque
from itertools import product
import json
from gauge_polynomial import Cluster,endpoints
ROOT=Path(__file__).resolve().parents[1]
Z=(F(0),F(0),F(0));ONE=(F(1),F(0),F(0))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(c,a):return tuple(c*x for x in a)
def mul(a,b):return (a[0]*b[0],a[0]*b[1]+a[1]*b[0],a[0]*b[2]+a[1]*b[1]+a[2]*b[0])
def power(a,n):
 out=ONE
 for _ in range(n):out=mul(out,a)
 return out
QONE=(ONE,Z,Z,Z)
def qa(a,b):return tuple(add(x,y) for x,y in zip(a,b))
def qc(a):return (a[0],)+tuple(scale(-1,x) for x in a[1:])
def qm(a,b):
 w,x,y,z=a;v,r,s,t=b
 return (add(add(mul(w,v),scale(-1,mul(x,r))),scale(-1,add(mul(y,s),mul(z,t)))),
         add(add(mul(w,r),mul(x,v)),add(mul(y,t),scale(-1,mul(z,s)))),
         add(add(mul(w,s),scale(-1,mul(x,t))),add(mul(y,v),mul(z,r))),
         add(add(mul(w,t),mul(x,s)),add(scale(-1,mul(y,r)),mul(z,v))))
def constq(v):return tuple((x,F(0),F(0)) for x in v)
def tree_map(model,U):
 tree=[tuple(e) for e in model['original_tree']];chords=[tuple(e) for e in model['chords']]
 adj=defaultdict(list)
 for e in tree:
  a,b=endpoints(e);adj[a].append((b,e,1));adj[b].append((a,e,-1))
 root=tuple(model['root']);H={root:QONE};queue=deque([root])
 while queue:
  a=queue.popleft()
  for b,e,s in adj[a]:
   if b not in H:H[b]=qm(H[a],U[e] if s==1 else qc(U[e]));queue.append(b)
 return [qm(qm(H[endpoints(e)[0]],U[e]),qc(H[endpoints(e)[1]])) for e in chords]
def poly_jet(poly,chords):
 v=[x for q in chords for x in q];out=Z
 for a,c in poly.items():
  term=(c,F(0),F(0))
  for i,n in enumerate(a):
   if n:term=mul(term,power(v[i],n))
  out=add(out,term)
 return out
POOL=[(F(1),F(0),F(0),F(0)),(F(0),F(1),F(0),F(0)),(F(0),F(0),F(1),F(0)),(F(0),F(0),F(0),F(1))]+[tuple(F(t,2) for t in ss) for ss in product((-1,1),repeat=4)]+[(F(3,5),F(4,5),F(0),F(0))]

def check_one(index):
 d=json.loads((ROOT/f'results/quartic_coefficients/class_{index:02d}.json').read_text());model=d['model']
 f={tuple(t['powers']):F(t['coefficient']) for t in d['coefficient_polynomial']}
 c=Cluster([tuple(p) for p in model['faces']])
 if [list(e) for e in c.chords]!=model['chords']:raise ArithmeticError('tree-reconstruction')
 U={e:constq(POOL[(7*i+3)%len(POOL)]) for i,e in enumerate(c.edges)}
 ch=tree_map(model,U);expect=poly_jet(c.K(f),ch)[0];total=F(0)
 for e in c.edges:
  for alpha in range(3):
   exp=[(F(1),F(0),-F(1,8)),Z,Z,Z];exp[alpha+1]=(F(0),F(1,2),F(0))
   varied=dict(U);varied[e]=qm(tuple(exp),U[e])
   value=poly_jet(f,tree_map(model,varied));total-=2*value[2]
 if total!=expect:raise ArithmeticError(('original-kinetic-return',index,total,expect))
 H={v:constq(POOL[(5*i+2)%len(POOL)]) for i,v in enumerate(c.vertices)}
 transformed={e:qm(qm(H[endpoints(e)[0]],q),qc(H[endpoints(e)[1]])) for e,q in U.items()}
 original=poly_jet(f,ch)[0];after=poly_jet(f,tree_map(model,transformed))[0]
 if after!=original:raise ArithmeticError('gauge-return')
 return {'class_index':index,'original_link_generator_tests':3*len(c.edges),
  'K_from_original_edge_jets':str(total),'K_from_returned_polynomial_fields':str(expect),
  'original_value':str(original),'value_after_original_vertex_gauge_map':str(after)}

if __name__=='__main__':
 import time
 rows=[]
 for i in range(78):
  t=time.monotonic();row=check_one(i);rows.append(row);print(i,'PASS',time.monotonic()-t,flush=True)
 (ROOT/'results/original_link_jet_audit.json').write_text(json.dumps(rows,sort_keys=True,indent=2)+'\n')
