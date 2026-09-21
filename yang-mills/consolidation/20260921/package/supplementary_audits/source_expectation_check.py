#!/usr/bin/env python3
"""Return signed source derivatives through the complete original vacuum density.

This route computes Cov_{exp(2v)/int exp(2v)}(W_p,partial_q v) directly.
It does not differentiate the stored energy polynomial to produce the answer.
The original trace/Haar engine is a shared dependency, explicitly retained.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import sys,json,argparse,hashlib
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'workbench/yang-mills/continuations/20260917-quartic-cube'))
from source_engine import Source,subcounts
from trace_algebra import add,scale,multiply,haar,trace,const
sys.path.insert(0,str(ROOT/'workbench/yang-mills/continuations/20260917-fifth-source'))
from plaquette_response import cube,A6,B6,TRIPLE,CUBE
import geometry as g

class Density(Source):
 @lru_cache(None)
 def density(self,nu):
  n=sum(nu)
  if not n:return const(1)
  ans={}
  for mu in subcounts(nu):
   if not sum(mu):continue
   lam=tuple(a-b for a,b in zip(nu,mu))
   ans=add(ans,scale(multiply(self.v(mu),self.density(lam)),F(2*sum(mu),n)))
  return ans
 @lru_cache(None)
 def mass(self,nu):return haar(self.density(nu))
 @lru_cache(None)
 def numerator(self,nu,p,q,kind):
  if kind=='W':return haar(multiply(trace(self.words[p]),self.density(nu)))
  ans=F(0)
  for alpha in subcounts(nu):
   v=list(alpha);v[q]+=1;term=scale(self.v(tuple(v)),alpha[q]+1)
   if kind=='Wz':term=multiply(trace(self.words[p]),term)
   ans+=haar(multiply(term,self.density(tuple(a-b for a,b in zip(nu,alpha)))))
  return ans
 @lru_cache(None)
 def mean(self,nu,p,q,kind):
  out=self.numerator(nu,p,q,kind)
  for mu in subcounts(nu):
   if not sum(mu):continue
   out-=self.mass(mu)*self.mean(tuple(a-b for a,b in zip(nu,mu)),p,q,kind)
  return out
 def covariance(self,nu,p,q):
  raw=self.mean(nu,p,q,'Wz');dis=F(0)
  for alpha in subcounts(nu):dis+=self.mean(alpha,p,q,'W')*self.mean(tuple(a-b for a,b in zip(nu,alpha)),p,q,'z')
  return raw-dis,raw,dis

def compute():
 p=(0,0,0,0,1);q=(0,0,1,0,1);r=(0,0,0,0,2)
 examples=[]
 def case(name,faces,source_exp,mark_p,mark_q,target):
  s=Density(faces);idx={p:i for i,p in enumerate(s.ps)};nu=tuple(source_exp.get(p,0) for p in s.ps)
  value,raw,dis=s.covariance(nu,idx[mark_p],idx[mark_q])
  if value!=target:raise ArithmeticError('vacuum-source-response:'+name+': '+str((value,target)))
  examples.append({'name':name,'faces':s.ps,'response_multiindex':nu,'marked_p':mark_p,'marked_q':mark_q,'density_moment':str(raw),'mean_product':str(dis),'connected_response':str(value),'energy_Hessian_check':str(target)})
 case('free-self',(p,),{},p,p,F(1,3))
 case('self-degree-four',(p,),{p:4},p,p,-15*A6)
 case('ordered-adjacent-cross',(p,r),{p:3,r:1},p,r,-4*B6)
 case('adjacent-diagonal-A',(p,r),{p:2,r:2},p,p,-6*B6)
 case('adjacent-diagonal-B',(p,r),{r:4},p,p,-B6)
 case('opposite-path',(p,r,q),{p:1,r:2,q:1},p,q,-2*TRIPLE['path'])
 for typ in ('common','corner'):
  found=None
  for a in sorted(g.adjacent(p)):
   for b in sorted(g.adjacent(p)|g.adjacent(a)):
    if b not in (p,a) and g.type3((p,a,b))==typ:found=(p,a,b);break
   if found:break
  x,y,z=found;case(typ+'-cross',found,{x:1,y:2,z:1},x,z,-2*TRIPLE[typ])
 six=cube((0,0,0));case('opposite-cube',six,{a:1 for a in six if a not in (p,q)},p,q,-CUBE/2)
 total=4*F(examples[5]['connected_response'])+F(examples[-1]['connected_response'])
 if total!=F(641033,29568240):raise ArithmeticError('full-opposite-vacuum-return')
 return {'schema':'ym-source-density-response-v1','passed':True,'scope':'exact original vacuum-density coefficient calculation; shared trace/Haar engine','cases':examples,'opposite_full_coefficient':str(total)}

def main():
 a=argparse.ArgumentParser();a.add_argument('--output',type=Path);a.add_argument('--verify-receipt',type=Path);args=a.parse_args()
 out=json.dumps(compute(),sort_keys=True,indent=2)+'\n'
 if args.verify_receipt and args.verify_receipt.read_text()!=out:raise ArithmeticError('source-density-receipt-mismatch')
 if args.output:args.output.write_text(out)
 else:sys.stdout.write(out)
if __name__=='__main__':main()
