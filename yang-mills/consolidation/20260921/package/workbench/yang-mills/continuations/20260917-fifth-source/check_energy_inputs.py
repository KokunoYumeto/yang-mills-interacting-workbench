"""Replay the actual sixth-order inputs by two retained coefficient recurrences."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import sys,json,time
from multiprocessing import Pool
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'20260917-quartic-cube'))
from energy import EnergySource,Rayleigh
from source_engine import g
from plaquette_response import cube,A6,B6,TRIPLE,CUBE

def job(t):
 name,ps,exps,target=t
 a=EnergySource(ps);b=Rayleigh(ps)
 cs=tuple(exps[p] for p in a.ps)
 x,pieces=a.energy6(cs);y=b.e(cs)
 if x!=y or y!=target:raise ArithmeticError('sixth-input:'+name+':'+str((x,y,target)))
 return {'name':name,'faces':a.ps,'multiplicity':cs,'logarithmic_energy':str(x),'linear_eigenvector_energy':str(y),'retained_pieces':list(map(str,pieces))}
def main():
 p=(0,0,0,0,1);q=(0,0,0,0,2);qc=(0,1,0,0,1)
 triples={k:v[0] for k,v in g.anchored()[2].items()}
 tasks=[('self',[p],{p:6},A6),('bent-ordered-pair',[p,q],{p:4,q:2},B6),('coplanar-ordered-pair',[p,qc],{p:4,qc:2},B6)]
 for typ,ps in triples.items():tasks.append((typ,ps,dict.fromkeys(ps,2),TRIPLE[typ]))
 ps=cube((0,0,0));tasks.append(('cube',ps,dict.fromkeys(ps,1),CUBE))
 rows=[]
 with Pool(4,maxtasksperchild=1) as pool:
  for r in pool.imap_unordered(job,tasks):rows.append(r);print(r['name'],r['logarithmic_energy'],flush=True)
 rows.sort(key=lambda r:r['name']);(ROOT/'generated/energy_input_checks.json').write_text(json.dumps(rows,indent=2)+'\n')
 print('COMPLETE',len(rows),flush=True)
if __name__=='__main__':main()
