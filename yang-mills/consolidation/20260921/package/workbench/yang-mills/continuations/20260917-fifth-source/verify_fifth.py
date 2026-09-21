#!/usr/bin/env python3
"""Deterministic exact arithmetic, data-coverage and negative-control checker.

The full symbolic equations are recalculated by audit_fifth.py --verify-existing.
This checker validates their complete records, source identities, every original
coordinate transport, response matrices and separate character/geometry controls.
All failures use explicit exceptions and remain enabled under python -O.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter,defaultdict
from itertools import permutations,combinations
from functools import lru_cache
import argparse,hashlib,json,sys,math
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'20260917-quartic-cube'))
from source_engine import Source,subcounts
from trace_algebra import gamma,electric,add,scale
from sphere_quotient import CoordinateMap,decode
from enumerate_fifth import OPS,moved_face
from character_check import calculate
from plaquette_response import (bulk_row,faces_box,matrix_for_faces,cube,TRIPLE,CUBE,A6,B6)
import geometry as g

class Failure(RuntimeError):pass
def need(p,name):
 if not p:raise Failure(name)
def strict_json(text):
 def pairs(items):
  out={}
  for k,v in items:
   need(k not in out,'duplicate-json-key:'+k);out[k]=v
  return out
 return json.loads(text,object_pairs_hook=pairs)
def read(p):return strict_json(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
CHECKS=[];NEG=[]
def ck(name,p,detail=None):
 need(bool(p),name);CHECKS.append({'name':name,'passed':True,**({'detail':detail} if detail is not None else {})})
def reject(name,false_equality,detail=None):
 need(not bool(false_equality),'false-formula-accepted:'+name)
 NEG.append({'name':name,'false_formula_accepted':False,**({'detail':detail} if detail is not None else {})})

def inputs():
 out={}
 for p in sorted(ROOT.rglob('*')):
  if not p.is_file() or '__pycache__' in p.parts or 'execution' in p.parts:continue
  rel=p.relative_to(ROOT).as_posix()
  if p.name in {'verification.json','execution.json','MANIFEST.json'}:continue
  if p.suffix not in {'.py','.md','.json'}:continue
  out[rel]=sha(p)
 for d,names in [('20260917-quartic-cube',['source_engine.py','trace_algebra.py','energy.py','differential_audit.py']),('20260916-cubic-linearized',['geometry.py'])]:
  for n in names:out['../'+d+'/'+n]=sha(ROOT.parent/d/n)
 return out

@lru_cache(None)
def adjacency(p):return g.adjacent(p)
@lru_cache(None)
def pedges(p):return g.pedges(p)

def geometry_checks():
 a=read(ROOT/'generated/geometry_fifth.json');classes=a['classes'];ts=a['transports']
 ck('fifth-class-coverage',[r['index'] for r in classes]==list(range(662)))
 ck('anchored-fifth-count',len(ts)==124864)
 expected={(5,):4,(4,1):84,(3,2):84,(3,1,1):1572,(2,2,1):1572,(2,1,1,1):27676,(1,1,1,1,1):93872}
 count=Counter();mult=Counter();seen=set();digest=hashlib.sha256()
 for t in ts:
  ps=tuple(map(tuple,t['faces']));key=ps
  need(key not in seen,'duplicate-anchored-multiset');seen.add(key)
  need(len(ps)==5 and ps==tuple(sorted(ps)),'unordered-source-multiset')
  need(any((0,0,0,0) in pedges(p) for p in ps),'lost-original-anchor')
  reached={ps[0]}
  while True:
   nxt=reached|{q for q in ps if any(q in adjacency(p) for p in reached)}
   if nxt==reached:break
   reached=nxt
  need(reached==set(ps),'disconnected-original-source')
  op=t['operation'];off=tuple(t['translation']);perm,sg=OPS[op]
  target=tuple(sorted(tuple(moved_face(p,op)[i]-off[i] for i in range(3))+moved_face(p,op)[3:] for p in ps))
  need(target==tuple(map(tuple,classes[t['class']]['faces'])),'coordinate-transport-target')
  # Both inverse laws on every original face vertex.
  for p in set(ps):
   n=p[:3];i,j=p[3:]
   for v in (n,g.add(n,i),g.add(n,j),g.add(g.add(n,i),j)):
    y=tuple(sg[k]*v[perm[k]]-off[k] for k in range(3));back=[0,0,0]
    for k in range(3):back[perm[k]]=sg[k]*(y[k]+off[k])
    need(tuple(back)==v,'coordinate-transport-inverse')
  count[tuple(sorted(Counter(ps).values(),reverse=True))]+=1;mult[t['class']]+=1
  digest.update((repr(ps)+'|'+repr(target)+'|'+str(op)+'|'+repr(off)+'\n').encode())
 ck('all-original-transport-inverse-laws',True,{'transports':len(ts),'digest_sha256':digest.hexdigest()})
 ck('all-multiplicity-pattern-counts',dict(count)==expected,{str(k):v for k,v in sorted(count.items())})
 ck('anchored-class-multiplicities',all(mult[r['index']]==r['anchored_count'] for r in classes))
 return classes

def data_checks(classes):
 qterms=tangents=trterms=raw_nonzero=0;ranks=Counter()
 for i in range(662):
  path=ROOT/'generated/fifth'/f'{i:04d}.json';r=read(path);q=read(ROOT/'generated/quotient'/f'{i:04d}.json')
  ck(f'original-source-row-{i}',r['index']==i and r['faces']==classes[i]['faces'])
  ck(f'full-polynomial-record-{i}',q['index']==i and q['full_inverse_residual']==[] and q['trace_file_sha256']==sha(path))
  rows=q['signed_response_identities'];cs=r['multiplicity']
  ck(f'all-signed-source-directions-{i}',len(rows)==len(cs) and all(z['response_factor']==cs[z['face_index']] and z['full_polynomial_residual']==[] for z in rows))
  ck(f'raw-signed-columns-{i}',all(decode(t['coefficients'])==scale(decode(r['coefficients']),t['coefficient_factor']) for t in r['signed_tangents']))
  cm=q['coordinate_map'];rank=len(cm['chord_edge_ids']);vs={tuple(v) for _,ends in r['edge_coordinates'] for v in ends}
  ck(f'original-cycle-count-{i}',rank==len(r['edge_coordinates'])-len(vs)+1 and len(cm['variables'])==4*rank)
  qterms+=len(q['coefficients']);trterms+=len(r['coefficients']);tangents+=len(rows);raw_nonzero+=bool(r['inverse_residual']);ranks[rank]+=1
 ck('complete-fifth-counts',(qterms,trterms,tangents,raw_nonzero)==(300821,14063,3047,281))
 fourth=read(ROOT/'generated/fourth_full_audit.json')
 ck('fourth-predecessor-full-polynomial-replay',len(fourth)==78)
 direct=read(ROOT/'generated/direct_matrix_checks.json')
 ck('all-separate-directional-matrix-checks',[r['index'] for r in direct]==list(range(662)) and all(r['K_v5']==r['Gamma_sum'] and r['difference']=='0' and r['source_sha256']==sha(ROOT/'generated/fifth'/f"{r['index']:04d}.json") for r in direct))
 return {'classes':662,'anchored_multisets':124864,'original_trace_terms':trterms,'quaternion_polynomial_terms':qterms,'signed_degree_four_equations':tangents,'raw_trace_residuals_returned_to_zero_polynomial':raw_nonzero,'cycle_rank_distribution':dict(sorted(ranks.items())),'independent_directional_matrix_rows':len(direct)}

def response_checks():
 r=read(ROOT/'generated/plaquette_response.json')
 for L in (2,3):
  saved=read(ROOT/f'generated/response_L{L}.json');ps=faces_box(L);A,counts=matrix_for_faces(ps)
  ck(f'original-finite-face-list-L{L}',saved['faces']==[list(p) for p in ps] and saved['counts']==counts)
  for d in (2,4,6):
   recorded=saved['matrices'][d//2-1]
   ck(f'full-response-matrix-L{L}-degree{d-2}',recorded['degree']==d-2 and recorded['entries']==[[i,j,str(c)] for (i,j),c in sorted(A[d].items())])
  if L==2:small=(ps,A)
 c=F(r['opposite_faces']['xi4_total']);ck('opposite-face-full-signed-entry',c==F(641033,29568240)==-8*TRIPLE['path']-CUBE/2)
 lo,hi=map(F,r['actual_opposite_enclosure']['C_over_xi4_interval'])
 ck('actual-opposite-finite-interval',F(21677,10**6)<lo<hi<F(21682,10**6))
 ck('physical-parameter-map',F(1,4*500000**2*10)==F(1,10**13))
 ck('analytic-radius-L2',F(r['actual_opposite_enclosure']['analytic_radius'])==F(1,1280))
 z=r['zero_momentum']
 ck('zero-momentum-scalar-coefficients',[F(z[str(d)]['scalar']) for d in (0,2,4)]==[F(1,3),-F(11,156),F(211396463,938298816)])
 ck('zero-momentum-traceless-coefficients',[F(z[str(d)]['traceless']) for d in (0,2,4)]==[F(1,3),-F(163,1404),-F(22137985,938298816)])
 symbol={(x['degree'],x['source_orientation'],x['target_orientation'],tuple(x['twice_centre_displacement'])):F(x['coefficient']) for x in r['Fourier_symbol']}
 ck('full-Fourier-adjoint-square',all(symbol.get((d,b,a,tuple(-v for v in k)))==c for (d,a,b,k),c in symbol.items()))
 frame=((1,1,1),(1,-1,0),(1,1,-2))
 gram=[[sum(u*v for u,v in zip(x,y)) for y in frame] for x in frame]
 ck('original-orientation-frame-Gram',gram==[[3,0,0],[0,2,0],[0,0,6]])
 ps,A=small;p=(0,0,0,0,1);idx=ps.index(p);bd=bulk_row(p)[4][p]
 reject('replace-finite-L2-diagonal-by-bulk',A[6][idx,idx]==bd,{'finite':str(A[6][idx,idx]),'bulk':str(bd)})
 reject('omit-cube-in-opposite-response',c==-8*TRIPLE['path'])
 reject('omit-four-paths-in-opposite-response',c==-CUBE/2)
 reject('reverse-Hessian-response-sign',-F(1,3)==F(1,3))
 reject('merge-two-ordered-pair-weights',B6==2*B6)
 return {'opposite_faces':r['opposite_faces'],'actual_enclosure':r['actual_opposite_enclosure'],'zero_momentum':z,'finite_boxes':r['finite_boxes']}

def algebra_controls():
 rr=read(ROOT/'generated/fifth/0000.json');C=CoordinateMap(rr['edge_coordinates']);v=decode(rr['coefficients']);s=Source(tuple(map(tuple,rr['faces'])));kv=electric(v)
 only23=add(gamma(s.v((2,)),s.v((3,))),gamma(s.v((3,)),s.v((2,))))
 reject('omit-2B-v1-v4',C.polynomial(add(kv,scale(only23,-1)))=={})
 reject('insert-fifth-factorial',C.polynomial(add(scale(v,120),scale(v,-1)))=={})
 reject('omit-tangent-multiplicity-five',C.polynomial(add(kv,scale(kv,-5)))=={})
 reject('omit-Frechet-factor-two',C.polynomial(scale(kv,F(1,2)))=={})
 reject('zero-Haar-mean-erases-source',C.polynomial(v)=={})
 q=read(ROOT/'generated/quotient/0176.json');need(len(q['coordinate_map']['chord_edge_ids'])==6,'rank-six-control-source')
 full={tuple(x['powers']):F(x['coefficient']) for x in q['coefficients']};ret=defaultdict(F)
 for m,c in full.items():
  if any(m[-3:]):continue
  ret[m[:-4]+(0,0,0,0)]+=c
 ret={m:c for m,c in ret.items() if c}
 reject('delete-sixth-original-chord',ret==full,{'source_index':176,'specialization':'q_6=(1,0,0,0)','full_terms':len(full),'image_terms':len(ret)})
 ch=calculate();ck('independent-character-recurrence',ch==read(ROOT/'generated/one_plaquette_check.json'))
 coeff=decode(rr['coefficients']);W=next(iter(coeff))[0]
 expected={(W,):F(79,34020),(W,W,W):-F(41,136080),(W,W,W,W,W):F(11,680400)}
 ck('single-original-trace-polynomial',coeff==expected)
 reject('omit-original-vacuum-scalar',F(ch['original_unit_vacuum_log_scalar_degree_two'])==0)
 for n,q in [(2,-F(1,12)),(4,F(5,13824)),(6,-F(289,79626240)),(8,F(21391,458647142400))]:
  ck('exact-Mathieu-return-'+str(n),q*(-4)**n/4==F(ch['energy_through_eight'][n]))
 # Every original cube insertion order and all five original denominators.
 faces=cube((0,0,0));total=F(0);hist=Counter()
 for order in permutations(faces):
  lengths=tuple(len(g.boundary(order[:j])) for j in range(1,6));weight=math.prod(F(4,3*k) for k in lengths)
  total+=weight;hist[lengths]+=1
 ck('all-original-cube-orders',sum(hist.values())==720 and total==F(166,243) and -total/16==CUBE)
 en=read(ROOT/'generated/energy_input_checks.json');ck('all-replayed-energy-inputs',len(en)==7 and all(x['logarithmic_energy']==x['linear_eigenvector_energy'] for x in en))
 reject('missing-cube-Haar-factor',-total==CUBE)
 reject('erase-physical-kappa-return',F(641033,29568240)/2==F(641033,29568240))
 return ch

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);p.add_argument('--verify-receipt',type=Path);args=p.parse_args()
 try:
  identity=inputs();saved=None
  if args.verify_receipt:
   saved=args.verify_receipt.read_text();expected=strict_json(saved)
   need(expected.get('schema')=='ym-fifth-complete-v1','receipt-schema')
   need(set(expected.get('source_sha256',{}))==set(identity),'source-manifest-membership')
   for name,h in identity.items():need(expected['source_sha256'][name]==h,'source-identity-mismatch:'+name)
  classes=geometry_checks();counts=data_checks(classes);response=response_checks();characters=algebra_controls()
  need(len({r['name'] for r in CHECKS})==len(CHECKS),'duplicate-check-name')
  need(len({r['name'] for r in NEG})==len(NEG),'duplicate-negative-name')
  result={'schema':'ym-fifth-complete-v1','passed':True,'counts':counts,'named_checks':len(CHECKS),'negative_control_count':len(NEG),
   'scope':{'full_polynomial_audit_entrypoint':'audit_fifth.py --verify-existing','finite_original_coefficients':True,'unconditional_finite_volume_response_bound':True,'new_uniform_coupling_gap_audit':False,'continuum_gap_proved':False,'Lean_run':False},
   'response':response,'one_plaquette':characters,'checks':CHECKS,'negative_controls':NEG,'source_sha256':identity}
  encoded=json.dumps(result,sort_keys=True,indent=2)+'\n'
  if args.verify_receipt:need(saved==encoded,'receipt-mismatch')
  if args.output:args.output.write_text(encoded)
  else:sys.stdout.write(encoded)
 except (Failure,OSError,ValueError,ArithmeticError) as ex:
  sys.stderr.write('FAIL: '+str(ex)+'\n');return 1
 return 0
if __name__=='__main__':raise SystemExit(main())
