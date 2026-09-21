"""Complete fifth source in original edge trace words and all signed derivatives.
The previous exact trace differential algebra is a preserved dependency.
"""
from pathlib import Path
import sys,json,time,argparse
from collections import Counter
from multiprocessing import Pool
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'20260917-quartic-cube'))
from source_engine import Source,subcounts
from trace_algebra import F,gamma,add,scale,electric

def encode(p):return [{'words':m,'coefficient':str(c)} for m,c in sorted(p.items())]
def produce(row):
 i=row['index'];dest=ROOT/'generated/fifth'/f'{i:04d}.json'
 if dest.exists():return i,'cached',dest.stat().st_size
 t=time.monotonic();ps=tuple(map(tuple,row['faces']));s=Source(ps);cs=tuple(Counter(ps)[p] for p in s.ps)
 v=s.v(cs);rhs={}
 for aa in subcounts(cs):
  if sum(aa) in (0,5):continue
  bb=tuple(x-y for x,y in zip(cs,aa));rhs=add(rhs,gamma(s.v(aa),s.v(bb)))
 resid=add(electric(v),scale(rhs,-1))
 out={'schema':'ym-fifth-source-row-v1','index':i,'faces':ps,'multiplicity':cs,
      'original_words':s.words,'edge_coordinates':sorted(s.edges.items()),
      'Casimir_spectrum':list(map(str,s.spectrum(cs))),
      'coefficients':encode(v),'source_rhs':encode(rhs),'inverse_residual':encode(resid),
      'signed_tangents':[{'face':p,'coefficient_factor':cs[j],
       'degree_four_index':tuple(x-int(k==j) for k,x in enumerate(cs)),
       'coefficients':encode(scale(v,cs[j]))} for j,p in enumerate(s.ps)]}
 dest.write_text(json.dumps(out,separators=(',',':'))+'\n')
 return i,round(time.monotonic()-t,3),len(v),len(resid)
def main():
 p=argparse.ArgumentParser();p.add_argument('--workers',type=int,default=4);p.add_argument('--indices',nargs='*',type=int)
 a=p.parse_args();rows=json.loads((ROOT/'generated/geometry_fifth.json').read_text())['classes'];(ROOT/'generated/fifth').mkdir(exist_ok=True)
 if a.indices is not None:rows=[rows[i] for i in a.indices]
 with Pool(a.workers,maxtasksperchild=3) as pool:
  for r in pool.imap_unordered(produce,rows):print(json.dumps(r),flush=True)
 print('COMPLETE',len(rows),flush=True)
if __name__=='__main__':main()
