"""Original fifth-source local, total-spin, and marked-edge bounds.

All inherited coefficient files are read unchanged.  Input-subcluster bounds
and final-spin constraints are returned through explicit signed coordinate maps.
For distinct-face sources with at most two occurrences per edge, the complete
joint edge-spin channel recurrence is evaluated before any absolute bound.
"""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from functools import lru_cache
from itertools import product
import sys,json,argparse,time
from multiprocessing import Pool
ROOT=Path(__file__).resolve().parent
Q4=ROOT.parent/'20260917-quartic-cube'
F5=ROOT.parent/'20260917-fifth-source'
sys.path.insert(0,str(Q4));sys.path.insert(0,str(F5))
from source_engine import Source,coordinates,physical_spectrum,subcounts
from trace_algebra import add,scale,electric,multiply,trace
from channel_bounds import norm_budget,submultisets,Bbound
from enumerate_fifth import canonical,OPS
from exact_lp import maximize
import geometry as geom
from oriented_word_bounds import reflected_bounds
QC=json.loads((Q4/'generated/quartic_coefficients.json').read_text())
QB=json.loads((Q4/'generated/quartic_bounds.json').read_text())
QS=json.loads((Q4/'generated/quartic_spin_budgets.json').read_text())
QMAP={tuple(map(tuple,r['faces'])):i for i,r in enumerate(QC)}

def encode(poly):return [{'words':m,'coefficient':str(c)} for m,c in sorted(poly.items())]
def tb(poly):return sum(abs(c)*2**(sum(map(len,m))-len(m)) for m,c in poly.items())
def connected(ps):
 reach={ps[0]}
 while True:
  nxt=reach|{p for p in ps if any(geom.pedges(p)&geom.pedges(q) for q in reach)}
  if nxt==reach:return len(reach)==len(set(ps))
  reach=nxt

@lru_cache(None)
def derivative_bounds(ps):
 """Return bounds on sum_j j_e ||A_j(v_ps)||_1, in input edge coordinates."""
 es=sorted(geom.union(ps))
 if not connected(ps):return {e:F(0) for e in es}
 if len(ps)<=3:return {e:norm_budget(ps,lambda j,e=e:j.get(e,F(0))) for e in es}
 if len(ps)!=4:raise ValueError('unsupported-input-order')
 cp,(oi,off)=canonical(ps);idx=QMAP[cp];pm,sg=OPS[oi];row=QS['rows'][idx]
 cedges={frozenset(map(tuple,uv)):int(e) for e,uv in QC[idx]['edge_coordinates']}
 out={}
 for e in es:
  uv=geom.endpoints(e)
  transformed=frozenset(tuple(sg[i]*v[pm[i]]-off[i] for i in range(3)) for v in uv)
  ce=cedges[transformed];out[e]=F(row['t'][str(ce)])
 return out

@lru_cache(None)
def quartic_joint_spin(idx, selected):
 """Complete joint spin objective on the actual selected original edges."""
 row=QC[idx];br=QB['rows'][idx]
 words=tuple(tuple(w) for w in row['original_words']);mult=row['multiplicity']
 edges={int(e):tuple(map(tuple,uv)) for e,uv in row['edge_coordinates']};es=sorted(edges)
 wordlist=tuple(w for w,n in zip(words,mult) for _ in range(n))
 _,allowed=physical_spectrum(wordlist,edges)
 js=[dict(zip(es,(F(v,2) for v in jj))) for jj in allowed if any(jj)]
 total=F(br['selected_bound'])*max(sum(j[e] for e in selected)/sum(v*(v+1) for v in j.values()) for j in js)
 raw=F(0)
 for term in row['coefficients']:
  ws=term['words'];occ=Counter(abs(e) for w in ws for e in w)
  raw+=abs(F(term['coefficient']))*2**(sum(occ.values())-len(ws))*F(sum(occ[e] for e in selected),2)
 total=min(total,raw,sum(F(QS['rows'][idx]['t'][str(e)]) for e in selected))
 if len(set(map(tuple,row['faces'])))==1:
  chars=[(F(17,10368),F(1)),(-F(7,51840),F(2))]
  total=min(total,len(selected)*sum(abs(a)*j*(2*j+1)**3 for a,j in chars))
 spin=br['spin_certificate']
 if spin:
  she=spin['shared_edges'];cnt=Counter(abs(e) for w in wordlist for e in w)
  channels=[]
  for bits,c,a in spin['channels']:
   j={e:F(bits[she.index(e)]) if cnt[e]==2 else F(1,2) for e in es}
   channels.append((j,F(a)))
  A=[[int(all(j[e]==0 for i,e in enumerate(she) if mask>>i&1)) for j,a in channels] for mask in range(1<<len(she))]
  b=list(map(F,spin['partial_projection_bounds']))
  weights=[abs(a)*sum(j[e] for e in selected) for j,a in channels]
  value,_,_,_=maximize(A,b,weights);total=min(total,value)
 return total

@lru_cache(None)
def precise_split_bound(a,b):
 if not connected(a) or not connected(b):return F(0)
 if len(a)>len(b):return precise_split_bound(b,a)
 if (len(a),len(b))==(2,3):return Bbound(a,b)
 if (len(a),len(b))!=(1,4):raise ValueError('fifth-split-order')
 shared=geom.pedges(a[0])&geom.union(b)
 if not shared:return F(0)
 cp,(oi,off)=canonical(b);idx=QMAP[cp];pm,sg=OPS[oi]
 ce={frozenset(map(tuple,uv)):int(e) for e,uv in QC[idx]['edge_coordinates']}
 selected=[]
 for e in shared:
  uv=geom.endpoints(e);im=frozenset(tuple(sg[i]*v[pm[i]]-off[i] for i in range(3)) for v in uv)
  selected.append(ce[im])
 return 4*quartic_joint_spin(idx,tuple(sorted(selected)))

@lru_cache(None)
def spin_case(ps):
 ws,ed=coordinates(ps);n=len(ws);cnt=Counter(abs(e) for w in ws for e in w)
 if n!=len(ps) or n!=5 or max(cnt.values())>2:return None
 she=sorted(e for e,c in cnt.items() if c==2);es=sorted(cnt)
 spectrum,allowed=physical_spectrum(ws,ed)
 bitslist=sorted({tuple(dict(zip(es,jj))[e]//2 for e in she) for jj in allowed})
 mask_count=1<<n
 cc=[]
 for mask in range(mask_count):cc.append(Counter(abs(e) for i,w in enumerate(ws) if mask>>i&1 for e in w))
 vals=[]
 for bits in bitslist:
  def cas(mask):return sum(F(bits[she.index(e)]*(bits[she.index(e)]+1)) if r==2 else F(3,4) for e,r in cc[mask].items())
  cv=[cas(mask) for mask in range(mask_count)];av=[F(0)]*mask_count
  for mask in range(1,mask_count):
   if mask.bit_count()==1:av[mask]=F(1,3);continue
   c=cv[mask]
   if c==0:continue
   a=(mask-1)&mask
   while a:
    b=mask^a
    if b:av[mask]+=(cv[a]+cv[b]-c)*av[a]*av[b]/(2*c)
    a=(a-1)&mask
  vals.append((bits,cv[-1],av[-1]))
 base={():F(1)}
 for w in ws:base=multiply(base,trace(w))
 proj={0:base};constraints=[];bounds=[];polys=[];orientation=[];length_bounds=[]
 for mask in range(1<<len(she)):
  if mask:
   bit=mask&-mask;i=bit.bit_length()-1;p=proj[mask^bit]
   proj[mask]=add(p,scale(electric(p,she[i]),-F(1,2)))
  rb=reflected_bounds(proj[mask],sorted(ed.items()));bd=max(rb)
  bounds.append(bd);orientation.append(list(map(str,rb)));length_bounds.append(str(tb(proj[mask])))
  constraints.append([int(all(bits[i]==0 for i in range(len(she)) if mask>>i&1)) for bits,c,a in vals])
  polys.append(encode(proj[mask]))
 js=[{e:F(bits[she.index(e)]) if cnt[e]==2 else F(1,2) for e in es} for bits,c,a in vals]
 objectives=[('C',[abs(a)*c for bits,c,a in vals]),('M',[abs(a)*sum(j.values()) for (bits,c,a),j in zip(vals,js)])]
 objectives += [(str(e),[abs(a)*j[e] for (bits,c,a),j in zip(vals,js)]) for e in es]
 cert=[];seen={}
 for name,weights in objectives:
  ww=tuple(weights)
  if ww not in seen:seen[ww]=maximize(constraints,bounds,weights)
  value,primal,dual,pivots=seen[ww]
  cert.append({'objective':name,'weights':list(map(str,weights)),'value':str(value),'primal':list(map(str,primal)),'dual':list(map(str,dual)),'pivots':pivots})
 return {'shared_edges':she,'channels':[[list(bits),str(c),str(a)] for bits,c,a in vals],
         'partial_bounds':list(map(str,bounds)),'partial_polynomials':polys,
         'reflection_bounds':orientation,'length_only_bounds':length_bounds,'certificates':cert}

def evaluate(index):
 start=time.monotonic();dest=ROOT/'generated/rows'/f'{index:04d}.json'
 row=json.loads((F5/'generated/fifth'/f'{index:04d}.json').read_text());ps=tuple(map(tuple,row['faces']))
 ws=tuple(tuple(w) for w in row['original_words']);edges={int(e):tuple(map(tuple,uv)) for e,uv in row['edge_coordinates']}
 es=sorted(edges);wordlist=tuple(w for w,m in zip(ws,row['multiplicity']) for _ in range(m))
 _,allowed=physical_spectrum(wordlist,edges)
 js=[dict(zip(es,(F(v,2) for v in jj))) for jj in allowed];js=[j for j in js if sum(j.values())]
 splits=[];bc=F(0)
 for a,b in submultisets(ps):
  da,db=derivative_bounds(a),derivative_bounds(b)
  separate=3*sum(da.get(e,F(0))*db.get(e,F(0)) for e in set(da)|set(db))
  joint=precise_split_bound(a,b);term=min(separate,joint);bc+=term
  splits.append({'left':a,'right':b,'bound':str(term),'separate_edge_bound':str(separate),'joint_bound':str(joint)})
 bm=bc*max(sum(j.values())/sum(s*(s+1) for s in j.values()) for j in js)
 bt={e:bc*max(j[e]/sum(s*(s+1) for s in j.values()) for j in js) for e in es}
 raw={tuple(tuple(w) for w in t['words']):F(t['coefficient']) for t in row['coefficients']}
 rm=F(0);rt={e:F(0) for e in es};rc=F(0)
 for m,c in raw.items():
  occ=Counter(abs(e) for w in m for e in w);bb=abs(c)*2**(sum(occ.values())-len(m))
  rm+=bb*F(sum(occ.values()),2);rc+=bb*sum(F(v*(v+2),4) for v in occ.values())
  for e,v in occ.items():rt[e]+=bb*F(v,2)
 outc=min(bc,rc);outm=min(bm,rm);outt={e:min(bt[e],rt[e]) for e in es}
 spin=spin_case(ps)
 if spin:
  for z in spin['certificates']:
   v=F(z['value']);key=z['objective']
   if key=='C':outc=min(outc,v)
   elif key=='M':outm=min(outm,v)
   else:outt[int(key)]=min(outt[int(key)],v)
 if len(set(ps))==1:
  # Exact displayed character coordinates, masses (2j+1)^3.
  chars=[(F(49,27216),F(1,2)),(-F(23,97200),F(3,2)),(F(11,680400),F(5,2))]
  outc=min(outc,sum(abs(a)*4*j*(j+1)*(2*j+1)**3 for a,j in chars))
  outm=min(outm,sum(abs(a)*4*j*(2*j+1)**3 for a,j in chars))
  st=sum(abs(a)*j*(2*j+1)**3 for a,j in chars);outt={e:min(t,st) for e,t in outt.items()}
 result={'index':index,'faces':ps,'branch_C':str(bc),'input_splits':splits,'raw_C':str(rc),'raw_M':str(rm),
         'C':str(outc),'M':str(outm),'T':{str(e):str(v) for e,v in outt.items()},'edge_coordinates':row['edge_coordinates'],'spin':spin}
 dest.write_text(json.dumps(result,separators=(',',':'))+'\n')
 return index,round(time.monotonic()-start,2),float(outc),float(outm),len(spin['channels']) if spin else 0

def main():
 p=argparse.ArgumentParser();p.add_argument('--workers',type=int,default=4);p.add_argument('--indices',type=int,nargs='*');p.add_argument('--resume',action='store_true');a=p.parse_args()
 (ROOT/'generated/rows').mkdir(exist_ok=True)
 ids=range(662) if a.indices is None else a.indices
 if a.resume:ids=[i for i in ids if not (ROOT/'generated/rows'/f'{i:04d}.json').exists()]
 with Pool(a.workers,maxtasksperchild=5) as pool:
  for r in pool.imap_unordered(evaluate,ids):print(json.dumps(r),flush=True)
if __name__=='__main__':main()
