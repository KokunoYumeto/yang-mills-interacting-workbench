#!/usr/bin/env python3
"""Original anchored coefficient sums and exact volume-independent heat bounds.
This program evaluates rational constants; it does not formalize analytic proofs.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
import sys,json,argparse,hashlib
ROOT=Path(__file__).resolve().parent
PARENT=ROOT.parent/'20260921-heat-response-transfer'
sys.path.insert(0,str(PARENT))
from assemble_heat import HeatCatalogue,adj,triples_containing,cubes_containing
from certified_bounds import inverse_power,heat_interval,exp_minus
from exact_rational import PF

def need(x,n):
 if not x: raise ArithmeticError(n)
def encode(x):return json.dumps(x,sort_keys=True,indent=2)+'\n'

def anchored():
 p=(0,0,0,0,1);H=HeatCatalogue();clusters={(p,)*n for n in (2,4,6)}
 for q in adj(p):
  for a,b in ((2,2),(4,2),(2,4)):clusters.add(tuple(sorted((p,)*a+(q,)*b)))
 for t in triples_containing(p):clusters.add(tuple(sorted(q for q in t for _ in range(2))))
 for c in cubes_containing(p):clusters.add(tuple(sorted(c)))
 bounds=defaultdict(F);signed=defaultdict(lambda:defaultdict(F));records=[];counts=Counter();transport=[]
 for cluster in sorted(clusters,key=lambda c:(len(c),c)):
  row,back,mp=H.transport(cluster);degree=row['degree'];counts[degree,row['type']]+=1
  transport.append({'cluster':cluster,'case':row['id'],'degree':degree,'permutation':mp['permutation'],'signs':mp['signs'],'translation':mp['translation']})
  for j,rr in enumerate(row['responses']):
   pp,qq=back[rr['p']],back[rr['q']]
   if pp!=p and qq!=p:continue
   other=qq if pp==p else pp;v=PF.from_json(rr['resolvent'])
   vals={str(k):inverse_power(v,k) for k in (0,1,2)}
   vals['kinetic']=sum(a*c for (a,n),c in v.d.items() if n==1)-sum(c for (a,n),c in v.d.items() if n==2)
   vals['leakage']=vals['0']-6*vals['1']+9*vals['2']
   for k,value in vals.items():bounds[k,degree]+=abs(value);signed[k,degree][other]+=value
   records.append({'cluster':cluster,'case':row['id'],'response_index':j,'other_face':other,'degree':degree,'values':{k:str(v) for k,v in vals.items()}})
 return {'schema':'ym-uniform-anchored-coefficients-v1','anchor':p,'number_of_clusters':len(clusters),'counts':[{'degree':d,'type':t,'count':n} for (d,t),n in sorted(counts.items())],'bounds':[{'kind':k,'degree':d,'absolute_motif_bound':str(v),'bulk_signed_row_sum':str(sum(map(abs,signed[k,d].values())))} for (k,d),v in sorted(bounds.items())],'transports':transport,'contributions':records}

def constants(data):
 b={(r['kind'],r['degree']):F(r['absolute_motif_bound']) for r in data['bounds']}
 R0=F(3,256);x=F(1,1024);theta=x/R0;tail=theta**6/(1-theta*theta)
 radii={}
 for k in ('0','1','2','kinetic','leakage'):
  pref=512*F(2,3)**int(k) if k.isnumeric() else (606 if k=='kinetic' else 4608)
  radii[k]=x*x*b[k,2]+x**4*b[k,4]+pref*tail
 l0,u0=1-radii['0'],1+radii['0'];l1,u1=F(1,3)-radii['1'],F(1,3)+radii['1'];l2,u2=F(1,9)-radii['2'],F(1,9)+radii['2'];lK,uK=3-radii['kinetic'],3+radii['kinetic']
 d=F(117,40);beta=radii['leakage'];obs=l1*l1/(u0*u2);loss=beta/(d*l1);state_extra=beta/(d*d*l2);section=u1*uK/(l0*l0)-1
 need(1-F(256,3)*x>F(19,20)**2,'physical-gap-rational-bound')
 targets={'0':F(173,10**6),'1':F(116,10**6),'2':F(77,10**6),'kinetic':F(205,10**6),'leakage':F(1555,10**6)}
 for k,t in targets.items():need(radii[k]<t,'radius:'+k)
 need(obs>F(624,625),'observation-fraction');need(loss<F(1,625),'full-complement-Schur');need(state_extra<F(1,600),'restored-norm');need(section<F(1,1250),'old-force-section-energy')
 # The original opposite-face heat coefficient and a uniform-volume actual interval.
 v=PF.from_json(json.loads((PARENT/'generated/opposite_combined.json').read_text())['resolvent']);xx=F(1,10**10);q=xx/R0
 lo,hi=heat_interval(v,F(1));eh=exp_minus(F(3,2))[1];error=512*eh*q**6/(1-q*q)/xx**4
 il,iu=lo-error,hi+error
 need(F(85910,10**7)<il<iu<F(85920,10**7),'opposite-actual-interval')
 # The inherited coefficient lower bound h4(t)>=5/648 exp(-3t), t>=1.
 # Error ratio on [1,3] is largest at3, with all physical factors retained.
 ratio=F(512*648,5)*xx**2/R0**6/(1-q*q)/exp_minus(F(9,2))[0]
 need(ratio<F(24,1000),'whole-time-interval')
 eps=exp_minus(F(117,4))[1];det=1920*eps/(1-eps)
 need(det<F(4,10**10),'four-240-rank-return')
 return {'schema':'ym-uniform-heat-constants-v1','analytic_radius':str(R0),'heat_row_prefactor':'512','heat_decay_in_tau':'3/2','xi_max_native':str(x),'g_squared_min_native':'16','theta_native':str(theta),'native_tail_scalar':str(tail),'radii':{k:str(v) for k,v in radii.items()},'radii_upper_bounds':{k:str(v) for k,v in targets.items()},'spectral_intervals':{'G0':[str(l0),str(u0)],'G1':[str(l1),str(u1)],'G2':[str(l2),str(u2)],'kinetic':[str(lK),str(uK)]},'physical_gap_over_kappa_lower':str(d),'observation_fraction_lower':str(obs),'observation_fraction_outer':'624/625','complement_loss_relative_upper':str(loss),'complement_loss_outer':'1/625','restored_state_extra_relative_upper':str(state_extra),'restored_state_extra_outer':'1/600','state_section_energy_relative_upper':str(section),'state_section_energy_outer':'1/1250','opposite_faces':{'xi':str(xx),'tau':'1','coefficient_interval':[str(lo),str(hi)],'complete_C_over_xi4_interval':[str(il),str(iu)],'outer_interval':['85910/10000000','85920/10000000'],'time_interval':['1','3'],'time_error_ratio_upper':str(ratio)},'heat_horizon':{'T':'10/kappa','omitted_heat_upper':str(eps),'four_240_rank_error':str(det),'outer_error':'1/2500000000'}}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--verify-existing',action='store_true');p.add_argument('--out',type=Path);a=p.parse_args();out=a.out or ROOT/'generated';out.mkdir(parents=True,exist_ok=True)
 data=anchored();results={'anchored_coefficients.json':data,'uniform_constants.json':constants(data)}
 for name,obj in results.items():
  s=encode(obj)
  if a.verify_existing:need((out/name).read_text()==s,'generated-mismatch:'+name)
  else:(out/name).write_text(s)
  print(name,hashlib.sha256(s.encode()).hexdigest(),flush=True)
 print('COMPLETE',len(data['contributions']),'original marked contributions')
if __name__=='__main__':
 try:main()
 except (ArithmeticError,ValueError,OSError) as e:print('FAIL:',e,file=sys.stderr);raise SystemExit(1)
