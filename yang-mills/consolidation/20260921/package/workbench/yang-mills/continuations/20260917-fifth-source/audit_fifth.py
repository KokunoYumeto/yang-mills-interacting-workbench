"""Full polynomial-identity audit; point evaluation is not the acceptance test."""
from pathlib import Path
import sys,json,time,hashlib,argparse
from multiprocessing import Pool
from functools import partial
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'20260917-quartic-cube'))
from source_engine import Source,subcounts
from trace_algebra import gamma,add,scale,electric
from sphere_quotient import CoordinateMap,decode,encode_poly

def run_row(path, verify_existing=False):
 row=json.loads(Path(path).read_text());i=row['index'];dest=ROOT/'generated/quotient'/f'{i:04d}.json'
 if dest.exists() and not verify_existing:return i,'cached'
 if verify_existing and not dest.is_file():raise ArithmeticError('missing-polynomial-audit:'+str(i))
 tic=time.monotonic();C=CoordinateMap(row['edge_coordinates']);v=decode(row['coefficients'])
 s=Source(tuple(map(tuple,row['faces'])));cs=tuple(row['multiplicity']);kv=electric(v);signed=[]
 original_rhs={}
 for mu in subcounts(cs):
  if sum(mu) in (0,5):continue
  nu=tuple(x-y for x,y in zip(cs,mu))
  original_rhs=add(original_rhs,gamma(s.v(mu),s.v(nu)))
 actual_residual=add(kv,scale(original_rhs,-1))
 if original_rhs!=decode(row['source_rhs']):raise ArithmeticError('stored-source-rhs:'+str(i))
 if actual_residual!=decode(row['inverse_residual']):raise ArithmeticError('stored-inverse-residual:'+str(i))
 rem=C.polynomial(actual_residual)
 if rem:raise ArithmeticError('full-original-inverse-identity:'+str(i))
 for j,p in enumerate(s.ps):
  rho=tuple(x-int(k==j) for k,x in enumerate(cs));rhs={};terms=0
  for mu in subcounts(rho):
   if not sum(mu):continue
   nu=tuple(x-y for x,y in zip(cs,mu));factor=2*nu[j]
   rhs=add(rhs,scale(gamma(s.v(mu),s.v(nu)),factor));terms+=1
  defect=add(scale(kv,cs[j]),scale(rhs,-1));r=C.polynomial(defect)
  if r:raise ArithmeticError('full-tangent-identity:'+str((i,j)))
  signed.append({'face_index':j,'face':p,'source_degree_index':rho,'ordered_rhs_terms':terms,
                 'response_factor':cs[j],'full_polynomial_residual':[]})
 q=C.polynomial(v)
 sig={e:(-1 if sum(u[:next(k for k in range(3) if u[k]!=vv[k])])%2 else 1) for e,(u,vv) in C.edges.items()}
 for words,c in v.items():
  sign=1
  for w in words:
   for e in w:sign*=sig[abs(e)]
  if sign!=-1:raise ArithmeticError('fifth-original-parity:'+str(i))
 out={'schema':'ym-fifth-sphere-audit-v1','index':i,'coordinate_map':C.record(),
      'coefficients':encode_poly(q),'full_inverse_residual':[],
      'signed_response_identities':signed,'original_haar_mean':'0',
      'trace_file_sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest()}
 encoded=json.dumps(out,separators=(',',':'))+'\n'
 if verify_existing:
  if dest.read_text()!=encoded:raise ArithmeticError('polynomial-audit-output-mismatch:'+str(i))
 else:dest.write_text(encoded)
 return i,round(time.monotonic()-tic,3),len(q),len(signed),len(v)
def main():
 p=argparse.ArgumentParser();p.add_argument('--workers',type=int,default=4);p.add_argument('--indices',nargs='*',type=int)
 p.add_argument('--verify-existing',action='store_true')
 a=p.parse_args();paths=sorted((ROOT/'generated/fifth').glob('*.json'))
 if a.indices is not None:paths=[paths[i] for i in a.indices]
 (ROOT/'generated/quotient').mkdir(exist_ok=True)
 with Pool(a.workers,maxtasksperchild=2) as pool:
  for v in pool.imap_unordered(partial(run_row,verify_existing=a.verify_existing),paths):print(json.dumps(v),flush=True)
 print('COMPLETE',len(paths),flush=True)
if __name__=='__main__':main()
