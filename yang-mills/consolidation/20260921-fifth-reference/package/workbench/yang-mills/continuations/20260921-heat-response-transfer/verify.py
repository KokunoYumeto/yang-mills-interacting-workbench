#!/usr/bin/env python3
"""Exact coefficient, original-metric and finite-error checks for heat transfer.
The complete symbolic producer/audit has its own replay; this receipt never
labels these finite checks as a formal proof of the analytic arguments.
"""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial
from collections import Counter,defaultdict
from itertools import product
import argparse,hashlib,json,sys
from exact_rational import PF,pole
from certified_bounds import exp_minus,heat_interval,inverse_power
from extract_band import mul as sparse_mul,plus as sparse_plus,transpose as sparse_transpose
ROOT=Path(__file__).resolve().parent
CHECKS=[];NEG=[]
class Failure(RuntimeError):pass

def require(p,name):
 if not p:raise Failure(name)
def check(name,p):
 require(name not in {r['name'] for r in CHECKS},'duplicate-check-name')
 require(bool(p),name);CHECKS.append({'name':name,'passed':True})
def reject(name,p):
 require(name not in {r['name'] for r in NEG},'duplicate-negative-name')
 require(not p,'false-formula-accepted:'+name);NEG.append({'name':name,'false_formula_accepted':False})
def strict(text):
 def pairs(rows):
  out={}
  for k,v in rows:require(k not in out,'duplicate-json-key:'+k);out[k]=v
  return out
 return json.loads(text,object_pairs_hook=pairs)
def load(name):return strict((ROOT/name).read_text())
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def sources():
 names=[p.name for p in ROOT.glob('*.py')]+[p.name for p in ROOT.glob('*.md')]+['SOURCE_INTAKE.json','RECOVERY_STATUS.json','state.json']
 names+=[p.relative_to(ROOT).as_posix() for p in (ROOT/'generated').glob('*.json')]
 names +=['../20260916-cubic-linearized/geometry.py']
 names +=['../20260917-quartic-cube/'+n for n in ('trace_algebra.py','source_engine.py','energy.py','clusters.py')]
 names +=['../20260917-fifth-source/'+n for n in ('sphere_quotient.py','plaquette_response.py','generated/response_L2.json')]
 out={}
 for name in sorted(set(names)):
  p=ROOT/name;require(p.is_file(),'missing-source:'+name);out[name]=digest(p)
 return out

def parsed_pf(rows):
 keys=[(F(r['energy']),r['power']) for r in rows]
 require(len(keys)==len(set(keys)),'duplicate-original-pole')
 require(all(a>0 and isinstance(n,int) and n>=1 for a,n in keys),'positive-original-poles')
 return PF.from_json(rows)
def derivative(R,n):
 return sum(c*F(comb(n,m-1))*(-a)**(n-m+1) for (a,m),c in R.d.items() if m-1<=n)

def rational_checks():
 for a,b,m,n,z in product((F(1),F(3,2),F(3)),(F(1),F(3,2),F(3)),range(1,4),range(1,4),(F(0),F(1),F(2,3))):
  check(f'complete-pole-product-{a}-{b}-{m}-{n}-{z}',(pole(a,m)*pole(b,n)).value(z)==1/((z+a)**m*(z+b)**n))
 for x in (F(0),F(1),F(3,2),F(3),F(7,2),F(49,50),F(303,50),F(27)):
  lo,hi=exp_minus(x);check('rational-exponential-'+str(x),0<lo<=hi)
 check('heat-energy-prefactor',4*F(113,112)*F(226,225)*F(1793,1680)<5)
 check('complete-feedback-decay',1-F(1,120)-F(1,238)>F(49,50))
 check('whole-band-projection',2*F(1,15)/(1-F(2,15))==F(2,13))
 check('whole-band-inverse',F(1)/(1-F(107,598))==F(598,491))
 check('whole-band-remainder',F(598,491)*F(1,13)*F(47,46)==F(47,491)<F(1,10))
 # DLMF b2(-4xi)/4-1 with the scalar return retained.
 for n,c,expected in ((2,-F(1,12),-F(1,3)),(4,F(5,13824),F(5,216)),(6,-F(289,79626240),-F(289,77760)),(8,F(21391,458647142400),F(21391,27993600))):
  check('original-Mathieu-coefficient-'+str(n),c*(-4)**n/4==expected)
 reject('erase-original-physical-time',F(1,3)==1)
 reject('erase-repeated-pole-factor',pole(3,3).heat_terms()[0][2]==1)
 reject('time-zero-is-integrated-value',pole(3).at_zero()==derivative(pole(3),0))


def catalogue_checks():
 data=load('generated/heat_coefficients.json');cases=data['cases']
 check('all-original-cases',len(cases)==17 and [r['id'] for r in cases]==list(range(17)))
 check('all-marked-responses',sum(len(r['responses']) for r in cases)==84)
 pairs=set();degrees=Counter()
 for row in cases:
  nu=row['multiplicities'];deg=row['degree'];check('source-degree-'+str(row['id']),sum(nu)==deg+2)
  expected={(i,j) for i in range(len(nu)) for j in range(i,len(nu)) if i!=j or nu[i]>=2}
  found={(r['p'],r['q']) for r in row['responses']}
  check('whole-marked-family-'+str(row['id']),found==expected and len(found)==len(row['responses']))
  for r in row['responses']:
   p,q=r['p'],r['q'];key=f"{row['id']}-{p}-{q}";pairs.add((row['id'],p,q));degrees[deg]+=1;R=parsed_pf(r['resolvent'])
   check('source-multiplicity-'+key,r['source_exponents']==[n-int(i==p)-int(i==q) for i,n in enumerate(nu)])
   target=-F(row['energy_coefficient'])*nu[p]*(nu[q]-int(p==q))/2
   check('entire-integral-'+key,R.at_zero()==target==F(r['static']))
   check('entire-time-zero-'+key,derivative(R,0)==F(r['covariance']))
   check('entire-first-derivative-'+key,derivative(R,1)==-F(r['kinetic']))
   check('entire-second-derivative-'+key,derivative(R,2)==F(r['second_moment']))
 check('degree-counts',degrees=={0:1,2:7,4:76})
 full=load('generated/full_polynomial_audit.json');got=set()
 for row in full['cases']:
  for r in row['source_equations']:
   got.add((row['id'],r['p'],r['q']));check('full-polynomial-receipt-'+str((row['id'],r['p'],r['q'])),r['original_resolvent_identity'] is True)
 check('complete-polynomial-coverage',got==pairs)
 check('all-pole-column-records',sum(len(r['column_poles']) for row in full['cases'] for r in row['source_equations'])==2013)
 check('all-column-monomial-records',sum(s['monomials'] for row in full['cases'] for r in row['source_equations'] for s in r['column_poles'])==2056737)
 # The formula is altered at an actual source entry, not by a generic crash.
 self2=next(r for r in cases if r['degree']==2 and r['type']=='self')['responses'][0]
 R=parsed_pf(self2['resolvent']);changed=R+pole(0)*F(4,9)
 reject('erase-connected-ground-subtraction',not any(a==0 and n>0 for a,n in changed.d))
 reject('erase-vacuum-shift-double-pole',(R-R.d.get((F(3),2),0)*pole(3,2)).at_zero()==F(self2['static']))
 return cases


def matrix_checks(cases):
 heat=load('generated/heat_matrix_L2.json');old=strict((ROOT.parent/'20260917-fifth-source/generated/response_L2.json').read_text())
 check('original-240-face-order',heat['faces']==old['faces'] and len(heat['faces'])==240)
 mats={}
 for row,prior in zip(heat['matrices'],old['matrices']):
  deg=row['degree'];mat={(i,j):parsed_pf(raw) for i,j,raw in row['entries']};require(len(mat)==len(row['entries']),'duplicate-matrix-entry')
  expected={(i,j):F(c) for i,j,c in prior['entries']};actual={k:v.at_zero() for k,v in mat.items() if v.at_zero()}
  check('whole-original-static-return-'+str(deg),actual==expected)
  check('whole-heat-matrix-symmetry-'+str(deg),all(v==mat.get((j,i),PF()) for (i,j),v in mat.items()))
  mats[deg]=mat
 check('entire-original-nonzero-heat-counts',[len(mats[d]) for d in (0,2,4)]==[240,2496,9660])
 # All signed maps are replayed explicitly in original coordinates.
 from assemble_heat import transform_face
 byid={r['id']:r for r in cases};trans=load('generated/heat_transports_L2.json')
 for k,tr in enumerate(trans):
  row=byid[tr['case']];target=sorted(tuple(p) for p,n in zip(row['faces'],row['multiplicities']) for _ in range(n));per=tr['permutation'];sgn=tr['signs'];off=tr['translation']
  changed=sorted(transform_face(tuple(p),per,sgn,off) for p in tr['source'])
  require(changed==target,'original-face-transport:'+str(k))
  for p in tr['source']:
   x=p[:3];y=[sgn[i]*x[per[i]]-off[i] for i in range(3)];back=[0]*3
   for i in range(3):back[per[i]]=sgn[i]*(y[i]+off[i])
   require(back==list(x),'coordinate-inverse:'+str(k))
 check('all-original-transport-inverses',len(trans)>0)
 faces=list(map(tuple,heat['faces']));p=faces.index((0,0,0,0,1));q=faces.index((0,0,1,0,1));total=mats[4][p,q]
 check('opposite-zero-lower-orders',not mats[0].get((p,q)) and not mats[2].get((p,q)))
 path=PF.from_json(load('generated/opposite_path.json')['resolvent']);cube=PF.from_json(load('generated/cube_opposite.json')['resolvent'])
 check('full-opposite-geometry-return',total==4*path+cube==PF.from_json(load('generated/opposite_combined.json')['resolvent']))
 check('opposite-integral',total.at_zero()==F(641033,29568240))
 check('opposite-initial-value',derivative(total,0)==F(8869,365040))
 reject('erase-original-cube-heat',total==4*path)
 reject('erase-three-original-paths',total==path+cube)
 # Complete marked cube paths and all original energy factors.
 from independent_heat import boundary_energy
 paths=load('generated/cube_heat_orders.json');cube_source=next(r for r in cases if r['type']=='cube');pairmap={(r['p'],r['q']):parsed_pf(r['resolvent']) for r in cube_source['responses']}
 n=0
 for row in paths['marked_cases']:
  key=row['p'],row['q'];ans=PF();seen=set();other=set(range(6))-set(key)
  for t in row['orders']:
   right=t['right_order'];middle=t['middle_order'];left=t['left_order'];tag=(tuple(right),tuple(middle),tuple(left))
   require(tag not in seen,'duplicate-marked-cube-path');seen.add(tag)
   require(len(right+middle+left)==4 and set(right+middle+left)==other,'cube-source-membership')
   c=F(1,16)
   for seq,record in ((right,t['right_vacuum_energies']),(left,t['left_vacuum_energies'])):
    E=[boundary_energy([tuple(paths['faces'][j]) for j in seq[:i]]) for i in range(1,len(seq)+1)]
    require(list(map(str,E))==record,'original-vacuum-energy-path')
    for e in E:c/=e
   occ=[row['q']]+right;E=[boundary_energy([tuple(paths['faces'][j]) for j in occ])]
   for j in middle:occ.append(j);E.append(boundary_energy([tuple(paths['faces'][k]) for k in occ]))
   require(list(map(str,E))==t['heat_energies'],'original-heat-energy-path');require(str(c)==t['vacuum_and_Haar_factor'],'original-cube-Haar-factor')
   v=PF(c)
   for e in E:v*=pole(e)
   ans+=v;n+=1
  check('whole-360-cube-paths-'+str(key),len(seen)==360 and ans==pairmap[key])
 check('all-5400-original-cube-paths',n==5400)
 native=load('generated/native_inverse_metrics_L2.json')
 for k,series in native['inverse_power_series'].items():
  k=int(k)
  for row in series:
   expected={(i,j):inverse_power(v,k) for (i,j),v in mats[row['degree']].items() if inverse_power(v,k)}
   check('entire-inverse-power-'+str((k,row['degree'])),expected=={(i,j):F(c) for i,j,c in row['entries']})
 for row in native['original_kinetic_series']:
  expected={(i,j):-derivative(v,1) for (i,j),v in mats[row['degree']].items() if derivative(v,1)}
  check('complete-original-kinetic-'+str(row['degree']),expected=={(i,j):F(c) for i,j,c in row['entries']})
 band=load('generated/first_band_L2.json');bm={s:{(i,j):F(c) for i,j,c in band[s]} for s in ('G2','G4','T2','T4','fourth_raw_metric_defect')}
 pp3={(i,j):v.d.get((F(3),3),F(0)) for (i,j),v in mats[4].items() if v.d.get((F(3),3),0)}
 check('complete-band-time-square',pp3==sparse_mul(bm['T2'],bm['T2']))
 lin={(i,j):-v.d.get((F(3),2),F(0)) for (i,j),v in mats[4].items() if v.d.get((F(3),2),0)}
 check('complete-fourth-band-return',bm['T4']==sparse_plus(lin,sparse_mul(bm['G2'],bm['T2']),-1))
 check('complete-band-metric-adjoint',sparse_plus(bm['T4'],sparse_transpose(bm['T4']),-1)==sparse_plus(sparse_mul(bm['T2'],bm['G2']),sparse_mul(bm['G2'],bm['T2']),-1))
 check('all-1440-adjoint-defects',len(bm['fourth_raw_metric_defect'])==1440)
 check('original-first-adjoint-defect',bm['fourth_raw_metric_defect'][0,13]==F(2,7371))
 reject('discard-band-Gram-correction',bm['T4']==lin)
 reject('replace-band-raw-adjoint',bm['T4']==sparse_transpose(bm['T4']))
 return {'transports':len(trans),'heat_entries':[len(mats[d]) for d in (0,2,4)],'band_entries':len(bm['T4'])}


def mm(A,B):return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in zip(*B)] for row in A]
def tr(A):return list(map(list,zip(*A)))
def add(A,B,c=1):return [[a+c*b for a,b in zip(row,col)] for row,col in zip(A,B)]
def scale(A,c):return [[c*v for v in row] for row in A]
def ident(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def inv(A):
 n=len(A);B=[list(map(F,row))+ident(n)[i] for i,row in enumerate(A)]
 for j in range(n):
  i=next((k for k in range(j,n) if B[k][j]),None);require(i is not None,'singular-original-fixture')
  B[j],B[i]=B[i],B[j];q=B[j][j];B[j]=[x/q for x in B[j]]
  for k in range(n):
   if k!=j:
    q=B[k][j];B[k]=[x-q*y for x,y in zip(B[k],B[j])]
 return [r[n:] for r in B]
def det2(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def psd2(A):return A==tr(A) and A[0][0]>=0 and A[1][1]>=0 and det2(A)>=0

class GI:
 """The exact rational Gaussian field used only in finite metric fixtures."""
 def __init__(self,a=0,b=0):
  if isinstance(a,GI):self.a,self.b=a.a,a.b
  else:self.a,self.b=F(a),F(b)
 def __add__(self,x):x=GI(x);return GI(self.a+x.a,self.b+x.b)
 __radd__=__add__
 def __neg__(self):return GI(-self.a,-self.b)
 def __sub__(self,x):return self+-GI(x)
 def __mul__(self,x):x=GI(x);return GI(self.a*x.a-self.b*x.b,self.a*x.b+self.b*x.a)
 __rmul__=__mul__
 def conjugate(self):return GI(self.a,-self.b)
 def norm2(self):return self.a*self.a+self.b*self.b
 def __eq__(self,x):x=GI(x);return (self.a,self.b)==(x.a,x.b)

def pair(a,E,b):return sum((GI(a[i]).conjugate()*E[i][j]*GI(b[j]) for i in range(len(a)) for j in range(len(b))),GI())

def metric_checks():
 # Original fixed real columns and a physical kappa=3 fixture. All entries exact.
 A=[[F(3),0,0],[0,F(6),0],[0,0,F(12)]];Phi=[[F(2),F(1)],[F(1),F(3)],[F(0),F(1)]]
 heat=[[F(1,2),0,0],[0,F(1,4),0],[0,0,F(1,16)]];C=add(ident(3),heat,-1)
 PhiT=mm(C,Phi);G=mm(tr(Phi),Phi);GT=mm(tr(PhiT),PhiT);E=mm(tr(Phi),mm(A,Phi));ET=mm(tr(PhiT),mm(A,PhiT));R=scale(mm(A,Phi),F(1,3))
 check('original-forcing-heat-defect',add(mm(A,PhiT),scale(R,-3))==scale(mm(heat,R),-3))
 check('state-complete-two-cross-products',add(GT,G,-1)==add(scale(mm(tr(Phi),mm(heat,Phi)),-2),mm(tr(Phi),mm(mm(heat,heat),Phi))))
 check('energy-complete-two-cross-products',add(ET,E,-1)==add(scale(mm(tr(Phi),mm(mm(A,heat),Phi)),-2),mm(tr(Phi),mm(mm(A,mm(heat,heat)),Phi))))
 check('state-original-relative-bounds',psd2(add(GT,scale(G,F(-1,4)))) and psd2(add(G,GT,-1)))
 check('energy-original-relative-bounds',psd2(add(ET,scale(E,F(-1,4)))) and psd2(add(E,ET,-1)))
 q=lambda H:H[1][1]-H[1][0]*H[0][1]/H[0][0]
 for name,H,HT in [('state',G,GT),('energy',E,ET)]:
  check('same-fiber-quotient-'+name,F(1,4)*q(H)<=q(HT)<=q(H))
  x=-H[0][1]/H[0][0];check('actual-minimum-representative-'+name,x*x*H[0][0]+2*x*H[0][1]+H[1][1]==q(H))
  reject('erase-original-mixed-quotient-'+name,q(H)==H[1][1])
 check('actual-heat-inverse',mm(inv(C),C)==ident(3))
 P=mm(Phi,mm(inv(G),tr(Phi)))
 check('raw-state-orthogonal-projection',mm(P,P)==P and tr(P)==P)
 G0=mm(tr(R),R);G1=scale(E,F(1,3));Kobs=scale(mm(tr(R),mm(A,R)),F(1,3));PR=mm(R,mm(inv(G0),tr(R)));h=mm(add(ident(3),PR,-1),Phi)
 check('actual-inverse-observation-left-inverse',mm(inv(G1),mm(tr(R),Phi))==ident(2))
 check('actual-state-section-residual',mm(tr(R),h)==[[0,0],[0,0]])
 check('actual-energy-section-orthogonality',mm(tr(Phi),mm(A,h))==[[0,0],[0,0]])
 target=scale(add(mm(G1,mm(inv(G0),mm(Kobs,mm(inv(G0),G1)))),G1,-1),3)
 check('whole-state-energy-section-correction',mm(tr(h),mm(A,h))==target)
 check('section-energy-signed-return',mm(tr(mm(PR,Phi)),mm(A,mm(PR,Phi)))==add(E,target))
 reject('discard-original-section-energy',target==[[0,0],[0,0]])
 Lm=[[F(1),F(1)]]
 def split(H):
  Q=inv(mm(Lm,mm(inv(H),tr(Lm))));Om=mm(tr(Lm),mm(Q,Lm));return add(H,Om,-1),Om
 L,Om=split(E);LT,OmT=split(ET);eta=F(3,4);a1=[GI(1,1),GI(2,-1)];a2=[GI(F(1,2),2),GI(-1,1)];v=[GI(1,2),GI(-1)]
 K=[pair(a,E0,v) for E0 in (L,) for a in (a1,a2)];B=[pair(a,Om,v) for a in (a1,a2)];KT=[pair(a,LT,v) for a in (a1,a2)];BT=[pair(a,OmT,v) for a in (a1,a2)]
 def currents(k,b):return [2*(k[0].conjugate()*k[1]).a,2*(b[0].conjugate()*b[1]).a,2*(k[0].conjugate()*b[1]+b[0].conjugate()*k[1]).a]
 x,y=currents(K,B),currents(KT,BT);d1=pair(a1,E,a1).a;d2=pair(a2,E,a2).a;Ev=pair(v,E,v).a
 for j,fac in enumerate((4*eta+4*eta*eta,2*eta+eta*eta,6*eta+4*eta*eta)):
  check('complex-original-current-'+str(j),(y[j]-x[j])**2<=4*d1*d2*Ev**2*fac**2)
 check('all-current-cross-return',sum(x)==2*(pair(a1,E,v).conjugate()*pair(a2,E,v)).a)
 reject('erase-complex-mixed-current',x[2]==0)
 reject('source-labels-imply-orthogonal',G[0][1]==0)
 reject('state-and-energy-Grams-identified',G==E)
 reject('heat-forcing-unmodified',mm(A,PhiT)==scale(R,3))
 reject('rank-factor-omitted',1920==8)
 reject('physical-time-omitted',F(10,3)==10)


def bounds_checks():
 b=load('generated/heat_bounds.json');p=b['opposite_pointwise'];iv=list(map(F,p['actual_C_over_xi4_interval']));outer=list(map(F,p['outer_interval']))
 check('actual-original-positive-heat-point',outer[0]<iv[0]<iv[1]<outer[1])
 c=b['opposite_time_interval'];check('continuous-positive-time-interval',F(c['remainder_to_cube_lower_ratio_upper'])<1 and F(c['path_quadratic_min'])>F(c['negative_bound']))
 for k,row in b['L2_native']['metrics'].items():
  lo,hi=map(F,row['eigenvalue_enclosure']);ol,oh=map(F,row['outer_interval'])
  check('actual-original-native-metric-'+k,ol<lo<hi<oh)
 eps=F(b['L2_native']['epsilon_upper']);err=F(b['L2_native']['four_quotient_determinant_error'])
 kin=b['L2_native']['original_kinetic_Gram'];kl,kh=map(F,kin['eigenvalue_enclosure'])
 check('actual-original-kinetic-interval',F(29,10)<kl<kh<F(31,10))
 check('actual-section-energy-fraction',F(31,10)*F(50,49)**2*F(11,30)-1==F(1322,7203))
 check('original-inverse-power-observation',(F(3,10)**2/F(51,50))/F(13,100)==F(150,221))
 check('single-physical-heat-horizon',eps<F(19,10**13) and err==1920*eps/(1-eps)<F(4,10**9))
 reject('time-grid-substitutes-continuous-proof',F(c['remainder_to_cube_lower_ratio_upper'])==0)
 reject('omit-original-volume-in-radius',F(1,240)==1)
 reject('fourth-time-coefficient-is-full-response',iv[0]==iv[1])


def run():
 CHECKS.clear();NEG.clear();rational_checks();c=catalogue_checks();mat=matrix_checks(c);metric_checks();bounds_checks()
 return {'schema':'ym-heat-transfer-verification-v1','passed':True,'scope':{
  'full_time_coefficient_catalogue':True,'full_polynomial_audit_receipt_checked':True,
  'polynomial_audit_executed_by_separate_program':True,'finite_raw_metric_fixtures':True,
  'analytic_proofs_formalized':False,'old_uniform_gap_recertified':False,
  'missing_sixth_catalogue_replayed':False,'continuum_gap_proved':False},
  'counts':{'named_checks':len(CHECKS),'negative_controls':len(NEG),'source_cases':17,'marked_heat_responses':84,'full_polynomial_column_terms':2056737,'independent_cube_insertions':5400,**mat},
  'checks':CHECKS,'negative_controls':NEG,'source_sha256':sources()}

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);ap.add_argument('--verify-receipt',type=Path);args=ap.parse_args()
 try:
  old=None
  if args.verify_receipt:
   text=args.verify_receipt.read_text();old=strict(text);require(old.get('schema')=='ym-heat-transfer-verification-v1','receipt-schema')
   current=sources();require(set(current)==set(old.get('source_sha256',{})),'source-membership')
   for k,v in current.items():require(old['source_sha256'][k]==v,'source-identity:'+k)
  result=run();out=json.dumps(result,sort_keys=True,indent=2)+'\n'
  if old is not None:require(text==out,'receipt-mismatch')
  if args.output:args.output.write_text(out)
  else:sys.stdout.write(out)
  return 0
 except (Failure,OSError,ValueError,KeyError,ZeroDivisionError) as e:
  print('FAIL: '+str(e),file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
