"""Recompute every connected physical heat coefficient through degree four."""
from dynamic_source import *
from clusters import cubic_orbit
from pathlib import Path
from collections import Counter
from itertools import combinations,combinations_with_replacement
from multiprocessing import Pool
from math import comb
import json,time,argparse
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'20260917-fifth-source'))
from plaquette_response import cube,A4,B4,A6,B6,TRIPLE,CUBE

def case_list():
    anchor,pairs,triples=g.anchored() if 'g' in globals() else __import__('geometry').anchored()
    import geometry as geo
    sets={}
    for p in geo.incident(anchor):
      for n,c in ((2,-F(1,3)),(4,A4),(6,A6)):
        key=cubic_orbit((p,)*n)[0];sets[n,key]=('self',c)
    for p,q in pairs:
      key=cubic_orbit((p,p,q,q))[0];sets[4,key]=('pair',B4)
      for ps in ((p,)*4+(q,)*2,(q,)*4+(p,)*2):
        key=cubic_orbit(ps)[0];sets[6,key]=('pair',B6)
    for typ,tuples in triples.items():
      for ps in tuples:
        key=cubic_orbit(tuple(p for p in ps for _ in range(2)))[0];sets[6,key]=(typ,TRIPLE[typ])
    key=cubic_orbit(cube((0,0,0)))[0];sets[6,key]=('cube',CUBE)
    rows=[]
    for idx,((n,key),(typ,e)) in enumerate(sorted(sets.items())):
      cnt=Counter(key);ps=tuple(sorted(cnt));nu=tuple(cnt[p] for p in ps)
      marks=[(i,j) for i in range(len(ps)) for j in range(i,len(ps)) if (nu[i]>=2 if i==j else True)]
      rows.append({'id':idx,'degree':n-2,'type':typ,'faces':ps,'multiplicities':nu,'energy_coefficient':str(e),'marks':marks})
    return rows

def deriv_at_zero(R,n):
    return sum(c*comb(n,m-1)*(-a)**(n-m+1) for (a,m),c in R.d.items() if m>=1 and m-1<=n)

def job(task):
    tt=time.monotonic();D=Dynamic(tuple(tuple(p) for p in task['faces']));nu=task['multiplicities'];out=[]
    for p,q in task['marks']:
      cs=tuple(v-int(i==p)-int(i==q) for i,v in enumerate(nu));R=D.correlation(p,q,cs)
      target=-F(task['energy_coefficient'])*nu[p]*(nu[q]-int(p==q))/2
      cov=D.covariance(p,q,cs);kin=D.kinetic(p,q,cs);n2=D.second_moment(p,q,cs)
      if R.at_zero()!=target:raise ArithmeticError('integrated coefficient:'+str((task['id'],p,q,R.at_zero(),target)))
      if deriv_at_zero(R,0)!=cov:raise ArithmeticError('time-zero covariance')
      if deriv_at_zero(R,1)!=-kin:raise ArithmeticError('original kinetic first derivative')
      if deriv_at_zero(R,2)!=n2:raise ArithmeticError('original commutator second derivative')
      out.append({'p':p,'q':q,'source_exponents':cs,'resolvent':R.to_json(),'static':str(target),
           'covariance':str(cov),'kinetic':str(kin),'second_moment':str(n2)})
    result={**task,'responses':out};result.pop('marks')
    return result,time.monotonic()-tt

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--workers',type=int,default=4);ap.add_argument('--verify-existing',action='store_true');args=ap.parse_args()
    tasks=case_list();print('cases',len(tasks),'responses',sum(len(t['marks']) for t in tasks),flush=True)
    rows=[];times=[]
    with Pool(args.workers,maxtasksperchild=1) as pool:
      for row,secs in pool.imap_unordered(job,tasks):
        rows.append(row);times.append({'id':row['id'],'seconds':secs});print(row['id'],row['type'],len(row['responses']),secs,flush=True)
    rows.sort(key=lambda r:r['id']);text=json.dumps({'schema':'ym-physical-heat-coefficients-v1','cases':rows},indent=2)+'\n'
    path=ROOT/'generated'/'heat_coefficients.json'
    if args.verify_existing:
      if path.read_text()!=text:raise ArithmeticError('complete heat catalogue mismatch')
    else:path.write_text(text)
    print('COMPLETE',len(rows),sum(len(r['responses']) for r in rows),flush=True)
if __name__=='__main__':main()
