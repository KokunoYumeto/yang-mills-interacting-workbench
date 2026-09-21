"""Original anchored face multisets and exact signed-coordinate orbit maps."""
import sys,json
from pathlib import Path
from functools import lru_cache
from itertools import product,permutations
from collections import Counter
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'20260916-cubic-linearized'))
import geometry as g
OPS=tuple((p,s) for p in permutations(range(3)) for s in product((-1,1),repeat=3))
@lru_cache(None)
def moved_face(p,j):
 perm,sg=OPS[j];n=p[:3];aa=p[3:]
 target=[sg[i]*n[perm[i]] for i in range(3)]
 axes=tuple(i for i in range(3) if perm[i] in aa)
 for i in axes:
  if sg[i]<0:target[i]-=1
 return tuple(target)+axes
@lru_cache(None)
def canonical(ps):
 best=None;witness=None
 for j in range(48):
  fs=[moved_face(p,j) for p in ps];off=tuple(min(p[i] for p in fs) for i in range(3))
  z=tuple(sorted(tuple(p[i]-off[i] for i in range(3))+p[3:] for p in fs))
  if best is None or z<best:best=z;witness=(j,off)
 return best,witness
@lru_cache(None)
def neighbors(p):return g.adjacent(p)
def run():
 root=(0,0,0,0);stage={tuple([p]) for p in g.incident(root)};counts=[]
 for n in range(2,6):
  nxt=set()
  for ps in stage:
   for p in set(ps)|set().union(*(neighbors(q) for q in ps)):
    nxt.add(tuple(sorted(ps+(p,))))
  stage=nxt;counts.append([n,len(stage)]);print('stage',n,len(stage),flush=True)
 reps={};trans=[]
 for i,ps in enumerate(sorted(stage)):
  rep,w=canonical(ps);reps[rep]=reps.get(rep,0)+1;trans.append((ps,rep,w))
  if (i+1)%20000==0:print('classified',i+1,'classes',len(reps),flush=True)
 ordered=sorted(reps);ids={r:i for i,r in enumerate(ordered)}
 out={'schema':'ym-original-fifth-geometry-v1','anchor':root,'stages':counts,'classes':[
  {'index':i,'faces':r,'anchored_count':reps[r],'pattern':sorted(Counter(r).values(),reverse=True)} for i,r in enumerate(ordered)],
 'signed_operations':OPS,'transports':[
  {'faces':p,'class':ids[r],'operation':w[0],'translation':w[1]} for p,r,w in trans]}
 (ROOT/'generated').mkdir(exist_ok=True);(ROOT/'generated/geometry_fifth.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
 print('FINISHED',len(stage),len(ordered),dict(Counter(tuple(sorted(Counter(r).values(),reverse=True)) for r in ordered)),flush=True)
if __name__=='__main__':run()
