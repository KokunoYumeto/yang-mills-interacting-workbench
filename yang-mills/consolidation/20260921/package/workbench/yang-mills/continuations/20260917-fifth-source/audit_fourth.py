"""Replay the received predecessor's 78 full fourth-source polynomial identities."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import sys,json
from multiprocessing import Pool
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'20260917-quartic-cube'))
from source_engine import Source,subcounts
from trace_algebra import add,scale,electric,gamma,haar,const
from sphere_quotient import CoordinateMap,decode,encode_poly

def job(row):
 p=decode(row['coefficients']);s=Source(tuple(map(tuple,row['faces'])));cs=tuple(Counter(map(tuple,row['faces']))[f] for f in s.ps)
 C=CoordinateMap(row['edge_coordinates']);rhs={}
 for mu in subcounts(cs):
  if sum(mu) in (0,4):continue
  nu=tuple(x-y for x,y in zip(cs,mu));rhs=add(rhs,gamma(s.v(mu),s.v(nu)))
 rem=C.polynomial(add(electric(p),scale(rhs,-1),const(haar(rhs))))
 if rem or haar(p):raise ArithmeticError('fourth-full-source:'+str(row['index']))
 tangents=[]
 for j in range(len(cs)):
  rho=tuple(x-int(k==j) for k,x in enumerate(cs));rhs2={}
  for mu in subcounts(rho):
   if not sum(mu):continue
   nu=tuple(x-y for x,y in zip(cs,mu));rhs2=add(rhs2,scale(gamma(s.v(mu),s.v(nu)),2*nu[j]))
  rem2=C.polynomial(add(scale(electric(p),cs[j]),scale(rhs2,-1),const(haar(rhs2))))
  if rem2:raise ArithmeticError('fourth-full-tangent:'+str((row['index'],j)))
  tangents.append({'face':s.ps[j],'coefficient_factor':cs[j],'residual':[]})
 q=C.polynomial(p)
 return {'index':row['index'],'coordinate_map':C.record(),'coefficients':encode_poly(q),'residual':[],
         'Haar_mean':'0','signed_tangents':tangents}
def main():
 rows=json.loads((ROOT.parent/'20260917-quartic-cube/generated/quartic_coefficients.json').read_text())
 with Pool(4,maxtasksperchild=2) as pool:out=list(pool.imap(job,rows))
 (ROOT/'generated/fourth_full_audit.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
 print('COMPLETE',len(out),'polynomial coefficients',sum(len(r['coefficients']) for r in out),'signed identities',sum(len(r['signed_tangents']) for r in out),flush=True)
if __name__=='__main__':main()
