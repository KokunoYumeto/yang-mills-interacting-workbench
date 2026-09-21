from source_engine import g
from itertools import product,permutations
from collections import Counter,defaultdict
from functools import lru_cache
import json
@lru_cache(None)
def adj(p):return g.adjacent(p)
@lru_cache(None)
def pe(p):return g.pedges(p)
@lru_cache(None)
def cubic_orbit(ps):
    # Exact signed coordinate permutations and translations, not parameter rescaling.
    best=None;bestmap=None
    for perm in permutations(range(3)):
      for signs in product((-1,1),repeat=3):
        def xform(v):return tuple(signs[i]*v[perm[i]] for i in range(3))
        polys=[]
        for p in ps:
          n,i,j=p[:3],p[3],p[4]
          vs=[xform(n),xform(g.add(n,i)),xform(g.add(n,j)),xform(g.add(g.add(n,i),j))]
          lower=tuple(min(v[i] for v in vs) for i in range(3))
          axes=tuple(i for i in range(3) if len({v[i] for v in vs})>1)
          polys.append(lower+axes)
        off=tuple(min(p[i] for p in polys) for i in range(3))
        target=tuple(sorted(tuple(p[i]-off[i] for i in range(3))+p[3:] for p in polys))
        if best is None or target<best:best=target;bestmap=(perm,signs,off)
    return best,bestmap

def anchored4():
    sets={tuple([p]) for p in g.incident((0,0,0,0))}
    stages=[sets]
    for k in (2,3,4):
      nxt=set()
      for ps in sets:
        for p in set(ps)|set().union(*(adj(q) for q in ps)):
          nxt.add(tuple(sorted(ps+(p,))))
      sets=nxt;stages.append(sets)
    return stages
