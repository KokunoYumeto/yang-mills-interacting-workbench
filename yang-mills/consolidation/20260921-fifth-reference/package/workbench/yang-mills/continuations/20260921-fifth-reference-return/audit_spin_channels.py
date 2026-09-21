"""Recompute every new edge-channel identity in the original sphere quotient.

This uses the preserved quaternion map, separately from the spin-channel
recurrence and exact linear-program bound producer. Exact feasible duals are
checked without invoking a linear-program solver.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
import sys,json,hashlib,argparse,time
from multiprocessing import Pool
ROOT=Path(__file__).resolve().parent
F5=ROOT.parent/'20260917-fifth-source';Q4=ROOT.parent/'20260917-quartic-cube'
sys.path.insert(0,str(Q4));sys.path.insert(0,str(F5))
from trace_algebra import add,scale,electric,multiply,trace
from sphere_quotient import CoordinateMap,decode

def need(t,s):
 if not t:raise ArithmeticError(s)

def audit(index):
 ti=time.monotonic();rr=json.loads((ROOT/'generated/rows'/f'{index:04d}.json').read_text());sp=rr['spin']
 if sp is None:return {'index':index,'channel_expansion_used':False}
 src=json.loads((F5/'generated/fifth'/f'{index:04d}.json').read_text());k=len(sp['shared_edges'])
 vals=[(tuple(b),F(c),F(a)) for b,c,a in sp['channels']]
 partial=[];base={():F(1)}
 for w in src['original_words']:base=multiply(base,trace(w))
 for mask in range(1<<k):
  if mask==0:p=base
  else:
   bit=mask&-mask;i=bit.bit_length()-1;q=partial[mask^bit];p=add(q,scale(electric(q,sp['shared_edges'][i]),-F(1,2)))
  partial.append(p)
  need(p==decode(sp['partial_polynomials'][mask]),f'partial-polynomial-{index}-{mask}')
  lengths=sum(abs(c)*2**(sum(map(len,m))-len(m)) for m,c in p.items())
  need(lengths==F(sp['length_only_bounds'][mask]),'length-bound')
  axes={int(e):next(i for i in range(3) if uv[0][i]!=uv[1][i]) for e,uv in src['edge_coordinates']}
  dirs={int(e):1 if uv[1][axes[int(e)]]>uv[0][axes[int(e)]] else -1 for e,uv in src['edge_coordinates']}
  rb=[]
  for reflection in product((-1,1),repeat=3):
   total=F(0)
   for words,coef in p.items():
    factor=F(1)
    for word in words:
     signs=[(1 if e>0 else -1)*dirs[abs(e)]*reflection[axes[abs(e)]] for e in word]
     changes=sum(a!=b for a,b in zip(signs,signs[1:]+signs[:1]))
     need(changes>=2 and changes%2==0,'closed-original-word-signs')
     factor*=2**(len(word)-changes//2)
    total+=abs(coef)*factor
   rb.append(total)
  need(list(map(str,rb))==sp['reflection_bounds'][mask],f'reflected-bound-{index}-{mask}')
  need(max(rb)<=lengths,'orientation-improves-old-bound')
  need(max(rb)==F(sp['partial_bounds'][mask]),f'partial-bound-{index}-{mask}')
 A=[[int(all(bits[i]==0 for i in range(k) if mask>>i&1)) for bits,c,a in vals] for mask in range(1<<k)]
 bounds=list(map(F,sp['partial_bounds']));certnum=0
 counts=Counter(abs(e) for w in src['original_words'] for e in w)
 spins=[{e:F(bits[sp['shared_edges'].index(e)]) if counts[e]==2 else F(1,2) for e in counts} for bits,c,a in vals]
 for (bits,c,a),j in zip(vals,spins):need(c==sum(v*(v+1) for v in j.values()),'original-channel-Casimir')
 expected_names={'C','M'}|{str(e) for e in counts}
 need({z['objective'] for z in sp['certificates']}==expected_names,'all-channel-objectives')
 for cert in sp['certificates']:
  weights=list(map(F,cert['weights']));key=cert['objective']
  objective=[abs(a)*(c if key=='C' else sum(j.values()) if key=='M' else j[int(key)]) for (bits,c,a),j in zip(vals,spins)]
  need(weights==objective,'original-channel-objective')
  dual=list(map(F,cert['dual']));primal=list(map(F,cert['primal']));v=F(cert['value'])
  need(len(dual)==len(A) and len(primal)==len(weights)==len(vals),'certificate-shape')
  need(all(z>=0 for z in dual+primal),'certificate-nonnegative')
  need(all(sum(x*y for x,y in zip(row,primal))<=b for row,b in zip(A,bounds)),'primal-feasible')
  need(all(sum(dual[i]*A[i][j] for i in range(len(A)))>=weights[j] for j in range(len(vals))),'dual-feasible')
  need(sum(x*y for x,y in zip(dual,bounds))==v==sum(x*y for x,y in zip(primal,weights)),'dual-primal-objective')
  certnum+=1
 combined={};projcoeff={}
 for bits,c,a in vals:
  zeros=sum(1<<i for i,b in enumerate(bits) if b==0);ones=sum(1<<i for i,b in enumerate(bits) if b==1);m=ones
  while True:
   mask=zeros|m;coef=a*(-1)**m.bit_count();projcoeff[mask]=projcoeff.get(mask,F(0))+coef
   if m==0:break
   m=(m-1)&ones
 for mask,a in projcoeff.items():combined=add(combined,scale(partial[mask],a))
 diff=add(combined,scale(decode(src['coefficients']),-1));C=CoordinateMap(src['edge_coordinates']);polynomial=C.polynomial(diff)
 need(not polynomial,'complete-original-channel-identity-'+str(index))
 return {'index':index,'channel_expansion_used':True,'allowed_channels':len(vals),'partial_projections':len(A),'dual_certificates':certnum,'complete_sphere_residual':[],
         'raw_trace_residual_terms':len(diff),'chords':len(C.chords),
         'row_sha256':hashlib.sha256((ROOT/'generated/rows'/f'{index:04d}.json').read_bytes()).hexdigest()}

def main():
 p=argparse.ArgumentParser();p.add_argument('--workers',type=int,default=4);p.add_argument('--output',type=Path,default=ROOT/'generated/spin_audit.json');args=p.parse_args()
 result=[]
 with Pool(args.workers,maxtasksperchild=3) as pool:
  for row in pool.imap_unordered(audit,range(662)):
   result.append(row)
   if row['channel_expansion_used']:print(row['index'],row['allowed_channels'],flush=True)
 result.sort(key=lambda r:r['index']);out={'passed':True,'rows':result,'full_channel_identities':sum(r['channel_expansion_used'] for r in result),
   'dual_certificates':sum(r.get('dual_certificates',0) for r in result)}
 args.output.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
 print('COMPLETE',out['full_channel_identities'],out['dual_certificates'],flush=True)
if __name__=='__main__':main()
