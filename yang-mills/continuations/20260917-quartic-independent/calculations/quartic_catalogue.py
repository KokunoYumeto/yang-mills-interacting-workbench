from itertools import permutations,product
from collections import defaultdict,Counter
from functools import lru_cache
import sys,json,time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'recovered'))
from geometry import incident,adjacent,pedges,add
TRANSFORMS=tuple((p,s) for p in permutations(range(3)) for s in product((-1,1),repeat=3))
@lru_cache(maxsize=None)
def transform_face(face,index):
 n=face[:3];i,j=face[3:];perm,sgn=TRANSFORMS[index]
 corners=(n,add(n,i),add(n,j),add(add(n,i),j))
 tc=[tuple(sgn[k]*v[perm[k]] for k in range(3)) for v in corners]
 lo=tuple(min(v[k] for v in tc) for k in range(3))
 dirs=tuple(k for k in range(3) if any(v[k]!=lo[k] for v in tc))
 return lo+dirs
@lru_cache(maxsize=None)
def canonical(faces):
 best=None
 for t in range(len(TRANSFORMS)):
  fs=[transform_face(p,t) for p in faces]
  shift=tuple(min(p[k] for p in fs) for k in range(3))
  key=tuple(sorted(tuple(p[k]-shift[k] for k in range(3))+p[3:] for p in fs))
  if best is None or key<best:best=key
 return best

def enumerate_classes(n=4):
 anchor=(0,0,0,0);current={(p,) for p in incident(anchor)};stats=[len(current)]
 for step in range(1,n):
  following=set()
  for fs in current:
   possible=set(fs)
   for p in fs:possible.update(adjacent(p))
   for p in possible:following.add(tuple(sorted(fs+(p,))))
  current=following;stats.append(len(current))
 classes=defaultdict(list)
 for fs in sorted(current):classes[canonical(fs)].append(fs)
 return stats,classes
if __name__=='__main__':
 t=time.monotonic();stats,classes=enumerate_classes()
 out={'anchored_counts_by_order':stats,'class_count':len(classes),'classes':[{'faces_with_multiplicity':key,'anchored_multiplicity':len(v),'partition':sorted(Counter(key).values(),reverse=True)} for key,v in sorted(classes.items())]}
 target=Path(__file__).resolve().parents[1]/'results'/'quartic_geometric_classes.json';target.write_text(json.dumps(out,indent=2)+'\n')
 print(stats,len(classes),Counter(tuple(c['partition']) for c in out['classes']),'seconds',time.monotonic()-t)
