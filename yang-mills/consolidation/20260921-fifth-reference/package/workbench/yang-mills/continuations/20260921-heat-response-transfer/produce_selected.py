from dynamic_source import *
from pathlib import Path
import json,time,sys
ROOT=Path(__file__).resolve().parent
name=sys.argv[1]
p=(0,0,0,0,1);q=(0,0,1,0,1);r=(0,0,0,0,2)
if name=='opposite_path':ps=(p,q,r);exponents={p:1,q:1,r:2};indices=(p,q)
elif name=='cube_opposite':
 ps=(p,q,r,(0,1,0,0,2),(0,0,0,1,2),(1,0,0,1,2));exponents={s:int(s not in (p,q)) for s in ps};indices=(p,q)
elif name=='adjacent':ps=(p,r);exponents={p:1,r:1};indices=(p,r)
elif name=='adjacent_diag':ps=(p,r);exponents={p:0,r:2};indices=(p,p)
else:raise ValueError(name)
D=Dynamic(ps);cs=tuple(exponents[s] for s in D.ps);a,b=[D.ps.index(s) for s in indices]
t=time.monotonic();print(name,'begin',D.ps,cs,flush=True)
R=D.correlation(a,b,cs);print('correlation done',time.monotonic()-t,R.to_json(),flush=True)
C=D.covariance(a,b,cs)
row={'name':name,'faces':D.ps,'source_exponents':cs,'marked_indices':[a,b],'resolvent':R.to_json(),'static':str(R.at_zero()),'covariance':str(C),'heat':[{'energy':str(a),'degree':n,'coefficient':str(c)} for a,n,c in R.heat_terms()],'elapsed':time.monotonic()-t}
(ROOT/'generated'/f'{name}.json').write_text(json.dumps(row,indent=2)+'\n')
print(json.dumps(row,indent=2),flush=True)
