"""Return every marked heat coefficient to the original open-box face ordering."""
from pathlib import Path
import sys,json
from fractions import Fraction as F
from collections import defaultdict,Counter
from functools import lru_cache
from itertools import combinations
from exact_rational import PF
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'20260917-quartic-cube'))
sys.path.insert(0,str(ROOT.parent/'20260917-fifth-source'))
from clusters import cubic_orbit
from plaquette_response import faces_box,adj,triples_containing,cubes_containing
import geometry as g

def transform_face(p,per,sgn,off):
    n,i,j=p[:3],p[3],p[4]
    vv=[n,g.add(n,i),g.add(n,j),g.add(g.add(n,i),j)]
    tv=[tuple(sgn[k]*v[per[k]]-off[k] for k in range(3)) for v in vv]
    lo=tuple(min(v[k] for v in tv) for k in range(3))
    axes=tuple(k for k in range(3) if len({v[k] for v in tv})>1)
    return lo+axes

class HeatCatalogue:
 def __init__(self):
    self.rows=json.loads((ROOT/'generated/heat_coefficients.json').read_text())['cases'];self.bykey={}
    for row in self.rows:
      ps=tuple(map(tuple,row['faces']));key=tuple(p for p,n in zip(ps,row['multiplicities']) for _ in range(n))
      self.bykey[key]=row
 @lru_cache(None)
 def transport(self,multiset):
    key,(per,sgn,off)=cubic_orbit(multiset);row=self.bykey[key];ps=tuple(map(tuple,row['faces']))
    mapping={p:ps.index(transform_face(p,per,sgn,off)) for p in set(multiset)}
    back={j:p for p,j in mapping.items()}
    return row,back,{'permutation':per,'signs':sgn,'translation':off,'target':key}

def original_clusters(ps):
    ps=tuple(ps);ss=set(ps)
    for p in ps:
      for n in (2,4,6):yield (p,)*n
    pairs=sorted({tuple(sorted((p,q))) for p in ps for q in adj(p) if q in ss})
    for p,q in pairs:
      yield tuple(sorted((p,p,q,q)))
      yield tuple(sorted((p,p,p,p,q,q)));yield tuple(sorted((p,p,q,q,q,q)))
    triples=sorted({t for p in ps for t in triples_containing(p) if set(t)<=ss})
    for t in triples:yield tuple(p for p in t for _ in range(2))
    cubes=sorted({c for p in ps for c in cubes_containing(p) if set(c)<=ss})
    for c in cubes:yield c

def run_box(L):
    H=HeatCatalogue();ps=faces_box(L);ids={p:i for i,p in enumerate(ps)};mats={k:{} for k in (0,2,4)};counts=Counter();transports=[]
    for cluster in original_clusters(ps):
      row,back,mp=H.transport(cluster);degree=row['degree'];counts[(degree,row['type'])]+=1
      transports.append({'source':cluster,'case':row['id'],**{k:v for k,v in mp.items() if k!='target'}})
      for r in row['responses']:
        i,j=ids[back[r['p']]],ids[back[r['q']]];v=PF.from_json(r['resolvent']);mat=mats[degree]
        mat[i,j]=mat.get((i,j),PF())+v
        if i!=j:mat[j,i]=mat.get((j,i),PF())+v
    inherited=json.loads((ROOT.parent/f'20260917-fifth-source/generated/response_L{L}.json').read_text())
    if tuple(map(tuple,inherited['faces']))!=ps:raise RuntimeError('changed original face ordering')
    checked=[]
    for j in inherited['matrices']:
      d=j['degree'];expected={(a,b):F(c) for a,b,c in j['entries']};actual={k:v.at_zero() for k,v in mats[d].items() if v.at_zero()}
      if actual!=expected:raise RuntimeError('full time integral differs from original static matrix:'+str(d))
      for (a,b),v in mats[d].items():
       if v!=mats[d][b,a]:raise RuntimeError('raw matrix transpose')
      checked.append({'degree':d,'full_matrix_integral_matches':True,'nonzero_static_entries':len(expected),'nonzero_heat_entries':sum(bool(v) for v in mats[d].values())})
    rows=[{'degree':d,'entries':[[i,j,v.to_json()] for (i,j),v in sorted(mat.items()) if v]} for d,mat in sorted(mats.items())]
    result={'schema':'ym-original-full-heat-matrix-v1','L':L,'faces':ps,'counts':[{'degree':d,'type':t,'count':n} for (d,t),n in sorted(counts.items())],'checks':checked,'matrices':rows}
    (ROOT/f'generated/heat_matrix_L{L}.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
    (ROOT/f'generated/heat_transports_L{L}.json').write_text(json.dumps(transports,separators=(',',':'))+'\n')
    print('BOX COMPLETE',L,checked,flush=True)
    return result
if __name__=='__main__':run_box(2)
