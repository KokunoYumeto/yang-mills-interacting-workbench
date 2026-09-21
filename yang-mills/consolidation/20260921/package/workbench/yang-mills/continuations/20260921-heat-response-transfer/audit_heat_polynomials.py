"""Full original sphere-quotient audit of the resolvent source equations.
Each partial-fraction coefficient is verified as an entire polynomial.
"""
from dynamic_source import *
from produce_heat import case_list
from multiprocessing import Pool
from pathlib import Path
from collections import defaultdict
import json,time,argparse
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'20260917-fifth-source'))
from sphere_quotient import CoordinateMap,encode_poly

def times_z(c):
    out=PF()
    for (a,n),v in c.d.items():
      if n==0:raise ArithmeticError('polynomial component in a proper resolvent column')
      out+=v*pole(a,n-1) if n>1 else v
      out-=a*v*pole(a,n)
    return out

def audit(task):
    D=Dynamic(tuple(map(tuple,task['faces'])));C=CoordinateMap(sorted(D.edges.items()));nu=task['multiplicities'];out=[]
    for p,q in task['marks']:
      cs=tuple(n-int(i==p)-int(i==q) for i,n in enumerate(nu));h=D.h(q,cs)
      rhs=multiply(trace(D.words[q]),D.u(cs))
      for i,n in enumerate(cs):
        if n:
          a=list(cs);a[i]-=1;rhs=add(rhs,multiply(trace(D.words[i]),D.h(q,tuple(a))))
      for a in subcounts(cs):
        if sum(a):
          b=tuple(x-y for x,y in zip(cs,a));rhs=add(rhs,scale(D.h(q,b),D.e(a)))
      defect=add(electric(h),{m:times_z(v) for m,v in h.items()},scale(rhs,-1))
      groups=defaultdict(dict)
      for m,v in defect.items():
        for k,a in PF(v).d.items():groups[k][m]=a
      for k,poly in groups.items():
        if C.polynomial(poly):raise ArithmeticError('full original resolvent polynomial:'+str((task['id'],p,q,k)))
      # Keep the actual column, coefficient-by-coefficient in the original sphere coordinates.
      columns=defaultdict(dict)
      for m,v in h.items():
        for k,a in PF(v).d.items():columns[k][m]=a
      sizes=[]
      for k,poly in sorted(columns.items()):
        qq=C.polynomial(poly);sizes.append({'pole':[str(k[0]),k[1]],'monomials':len(qq)})
      out.append({'p':p,'q':q,'original_resolvent_identity':True,'residual_poles':len(groups),'column_poles':sizes})
    return {'id':task['id'],'coordinate_map':C.record(),'source_equations':out}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--workers',type=int,default=4);ap.add_argument('--verify-existing',action='store_true');args=ap.parse_args();rows=[]
    with Pool(args.workers,maxtasksperchild=1) as pool:
      for row in pool.imap_unordered(audit,case_list()):rows.append(row);print('polynomial',row['id'],len(row['source_equations']),flush=True)
    rows.sort(key=lambda r:r['id']);s=json.dumps({'schema':'ym-heat-full-polynomial-v1','cases':rows},indent=2)+'\n';p=ROOT/'generated/full_polynomial_audit.json'
    if args.verify_existing:
      if p.read_text()!=s:raise ArithmeticError('complete polynomial receipt mismatch')
    else:p.write_text(s)
    print('COMPLETE',len(rows),sum(len(r['source_equations']) for r in rows),flush=True)
if __name__=='__main__':main()
