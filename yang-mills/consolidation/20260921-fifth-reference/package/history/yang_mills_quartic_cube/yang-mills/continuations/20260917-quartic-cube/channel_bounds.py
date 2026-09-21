from source_engine import *
from itertools import combinations,product
from functools import lru_cache
from math import factorial
# small nonnegative channel polytopes; full original trace-norm mass is retained.

def vertices(A,b):
    from exact_lp import solve_square
    n=len(A[0]);aa=[list(map(F,r)) for r in A]+[[-F(i==j) for i in range(n)] for j in range(n)];bb=list(map(F,b))+[F(0)]*n
    out=set()
    for active in combinations(range(len(aa)),n):
      v=solve_square([aa[i] for i in active],[bb[i] for i in active])
      if v is None:continue
      if all(sum(x*y for x,y in zip(r,v))<=t for r,t in zip(aa,bb)):out.add(tuple(v))
    return tuple(sorted(out))
VERTS={
 'self1':((F(8),),),
 'self2':((F(27),),),
 'pair':vertices([[1,1],[1,0]],[64,16]),
 'self3':((F(8),F(64)),),
 'repeat':vertices([[1,1],[1,0]],[216,F(520,3)]),
 'path':vertices([[1,1,1,1],[1,0,0,0],[1,1,0,0],[1,0,1,0]],[512,32,128,128]),
 # full half-isotypic component carries BOTH spin-one-half copies.
 'common':vertices([[1,1],[1,0]],[512,256]),
 # active channels 000,011,101,110,111; one-spin channels are identically zero.
 'corner':vertices([[1,1,1,1,1],[1,0,0,0,0],[1,1,0,0,0],[1,0,1,0,0],[1,0,0,1,0]],[512,8,128,128,128])
}
@lru_cache(None)
def channels(ps):
  n=len(ps);es=sorted(g.union(ps));counts=Counter(e for p in ps for e in g.pedges(p))
  def js(sp):return {e:sp.get(e,F(counts[e],2)) for e in es}
  if n==1:return 'self1',[(F(1,3),js({}))]
  if n==2:
    if ps[0]==ps[1]:return 'self2',[(-F(1,72),js({}))]
    common=g.pedges(ps[0])&g.pedges(ps[1])
    if not common:return None,[]
    e=next(iter(common));return 'pair',[(F(1,27),js({e:F(0)})),(-F(1,117),js({e:F(1)}))]
  typ=g.type3(ps)
  if typ=='disconnected':return None,[]
  if typ=='self':return 'self3',[(-F(1,81),{e:F(1,2) for e in es}),(F(1,810),{e:F(3,2) for e in es})]
  shared=[e for e in es if counts[e]>1]
  if typ=='repeat':
    p=next(p for p in ps if ps.count(p)==2);q=next(p for p in ps if ps.count(p)==1)
    e=next(iter(g.pedges(p)&g.pedges(q)))
    base={f:(F(1) if f in g.pedges(p) else F(1,2)) for f in es}
    return 'repeat',[(-F(11,4212),dict(base,**{})|{e:F(1,2)}),(F(11,11232),base|{e:F(3,2)})]
  if typ=='common':
    e=next(e for e in es if counts[e]==3);base={f:F(1,2) for f in es}
    return 'common',[(-F(2,1755),base|{e:F(1,2)}),(F(2,2457),base|{e:F(3,2)})]
  coefs=({0:F(1,162),1:-F(11,8424),2:F(1,3510)} if typ=='path' else {0:F(2,81),1:F(34,13689),2:-F(38,17901),3:F(2,2457)})
  bitslist=list(product((0,1),repeat=len(shared)))
  if typ=='corner':bitslist=[b for b in bitslist if sum(b)!=1]
  return typ,[(coefs[sum(bits)],js(dict(zip(shared,map(F,bits))))) for bits in bitslist]

def maxlin(kind,weights):return max(sum(a*b for a,b in zip(weights,v)) for v in VERTS[kind])

def norm_budget(ps,selector):
    k,chs=channels(tuple(sorted(ps)))
    if not chs:return F(0)
    ws=[abs(c)*selector(j) for c,j in chs]
    return maxlin(k,ws)

@lru_cache(None)
def Bbound(a,b):
    ka,as_=channels(a);kb,bs=channels(b)
    if not as_ or not bs:return F(0)
    mat=[[3*abs(c*d)*sum(j.get(e,0)*k.get(e,0) for e in set(j)&set(k)) for d,k in bs] for c,j in as_]
    return max(sum(x*y*m for i,row in enumerate(mat) for y,m in zip(vb,row) for x in [va[i]]) for va in VERTS[ka] for vb in VERTS[kb])

def submultisets(ps):
    items=sorted(Counter(ps).items())
    for cs in product(*(range(n+1) for p,n in items)):
        a=tuple(p for (p,n),k in zip(items,cs) for _ in range(k))
        if not a or len(a)==len(ps):continue
        b=tuple(p for (p,n),k in zip(items,cs) for _ in range(n-k))
        yield a,b

