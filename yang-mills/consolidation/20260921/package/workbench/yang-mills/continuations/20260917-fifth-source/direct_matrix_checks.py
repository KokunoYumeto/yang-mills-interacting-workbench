"""Separate direct quaternion directional derivatives for all fifth classes.
This check uses the preserved matrix-jet implementation, not Fierz contractions.
Full polynomial identities are audited separately by audit_fifth.py.
"""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib,time
from multiprocessing import Pool
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'20260917-quartic-cube'))
from source_engine import Source,subcounts
from differential_audit import Audit,assignments
from sphere_quotient import decode

def job(path):
 row=json.loads(path.read_text());p=decode(row['coefficients']);s=Source(tuple(map(tuple,row['faces'])));cs=tuple(row['multiplicity'])
 A=Audit(assignments(len(row['edge_coordinates']),13));left=A.K(p);right=F(0)
 for mu in subcounts(cs):
  if sum(mu) in (0,5):continue
  nu=tuple(x-y for x,y in zip(cs,mu));right+=A.Gamma(s.v(mu),s.v(nu))
 if left!=right:raise ArithmeticError('direct-matrix-source:'+str(row['index']))
 return {'index':row['index'],'seed':13,'original_edge_count':len(row['edge_coordinates']),
         'K_v5':str(left),'Gamma_sum':str(right),'difference':'0',
         'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
def main():
 tic=time.monotonic();rows=[]
 with Pool(4,maxtasksperchild=2) as pool:
  for row in pool.imap_unordered(job,sorted((ROOT/'generated/fifth').glob('*.json'))):
   rows.append(row)
   if len(rows)%50==0:print('direct-matrix',len(rows),flush=True)
 rows.sort(key=lambda r:r['index'])
 (ROOT/'generated/direct_matrix_checks.json').write_text(json.dumps(rows,separators=(',',':'))+'\n')
 print('COMPLETE',len(rows),'elapsed',time.monotonic()-tic,flush=True)
if __name__=='__main__':main()
