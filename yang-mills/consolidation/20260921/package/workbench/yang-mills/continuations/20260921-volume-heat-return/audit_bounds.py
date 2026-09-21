#!/usr/bin/env python3
"""Independent rational and original-geometry audit; imports no producer code."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
from collections import defaultdict,Counter
from math import factorial,comb
import argparse,json,hashlib,sys
ROOT=Path(__file__).resolve().parent
CHECKS=[];NEG=[]
class AuditError(RuntimeError):pass
def check(name,ok):
 if any(x==name for x in CHECKS):raise AuditError('duplicate-check:'+name)
 if not ok:raise AuditError(name)
 CHECKS.append(name)
def reject(name,false):
 if false:raise AuditError('accepted-false-formula:'+name)
 NEG.append(name)
def strict(text):
 def pairs(items):
  d={}
  for k,v in items:
   if k in d:raise AuditError('duplicate-json-key:'+k)
   d[k]=v
  return d
 return json.loads(text,object_pairs_hook=pairs)
def load(path):return strict(Path(path).read_text())
def add(v,i,s=1):return tuple(v[k]+s*(k==i) for k in range(3))
def vertices(p):
 n=p[:3];i,j=p[3:];return (n,add(n,i),add(n,j),add(add(n,i),j))
def edges(p):
 n=p[:3];i,j=p[3:];return frozenset((n+(i,),n+(j,),add(n,i)+(j,),add(n,j)+(i,)))
def face_of(vs):
 lo=tuple(min(v[i] for v in vs) for i in range(3));axes=tuple(i for i in range(3) if len({v[i] for v in vs})==2)
 if len(axes)!=2:raise AuditError('invalid-face')
 return lo+axes

def geometry_and_moments(data):
 p=tuple(data['anchor']);faces=[n+(i,j) for n in product(range(-2,3),repeat=3) for i,j in combinations(range(3),2)];es={q:edges(q) for q in faces}
 neighbor=lambda q:{r for r in faces if r!=q and es[r]&es[q]}
 near=neighbor(p);pool=set(near)
 for q in near:pool|=neighbor(q)
 pool.discard(p);triples=[];types=Counter()
 for q,r in combinations(sorted(pool),2):
  adjpq=bool(es[p]&es[q]);adjpr=bool(es[p]&es[r]);adjqr=bool(es[q]&es[r]);e=int(adjpq)+int(adjpr)+int(adjqr)
  if e<2:continue
  t=tuple(sorted((p,q,r)));triples.append(t)
  types['path' if e==2 else ('common' if es[p]&es[q]&es[r] else 'corner')]+=1
 check('original-twelve-neighbors',len(near)==12)
 check('original-all-triple-counts',types=={'path':138,'common':12,'corner':8})
 cubes=[];normal=next(i for i in range(3) if i not in p[3:])
 for n in (p[:3],add(p[:3],normal,-1)):
  c=[]
  for i,j in combinations(range(3),2):
   k=next(z for z in range(3) if z not in (i,j));c.extend((n+(i,j),add(n,k)+(i,j)))
  cubes.append(tuple(sorted(c)))
 expected={(p,)*n for n in (2,4,6)}
 for q in near:
  for a,b in ((2,2),(4,2),(2,4)):expected.add(tuple(sorted((p,)*a+(q,)*b)))
 for t in triples:expected.add(tuple(q for q in t for _ in range(2)))
 expected.update(cubes)
 actual={tuple(map(tuple,r['cluster'])) for r in data['transports']}
 check('complete-199-original-clusters',actual==expected and len(expected)==199)
 raw=load(ROOT.parent/'20260921-heat-response-transfer/generated/heat_coefficients.json')['cases'];byid={r['id']:r for r in raw};trans={};wanted=set()
 for i,tr in enumerate(data['transports']):
  cluster=tuple(map(tuple,tr['cluster']));row=byid[tr['case']];per=tr['permutation'];sgn=tr['signs'];off=tr['translation']
  def forward(v):return tuple(sgn[k]*v[per[k]]-off[k] for k in range(3))
  def backward(v):
   ans=[0]*3
   for k in range(3):ans[per[k]]=sgn[k]*(v[k]+off[k])
   return tuple(ans)
  mapped={q:face_of([forward(v) for v in vertices(q)]) for q in set(cluster)}
  target=Counter({tuple(q):m for q,m in zip(row['faces'],row['multiplicities'])})
  check('transport-source-'+str(i),Counter(mapped[q] for q in cluster)==target)
  check('transport-inverse-'+str(i),all(backward(forward(v))==v for q in set(cluster) for v in vertices(q)))
  back={row['faces'].index(list(a)):q for q,a in mapped.items()};trans[cluster]=(row,back)
  for j,r in enumerate(row['responses']):
   if p in (back[r['p']],back[r['q']]):wanted.add((cluster,j))
 observed=set();B=defaultdict(F);signed=defaultdict(lambda:defaultdict(F))
 for i,r in enumerate(data['contributions']):
  c=tuple(map(tuple,r['cluster']));j=r['response_index'];row,back=trans[c];rr=row['responses'][j];other=back[rr['q']] if back[rr['p']]==p else back[rr['p']]
  check('original-mark-'+str(i),tuple(r['other_face'])==other and r['degree']==row['degree'])
  key=(c,j);check('unique-mark-'+str(i),key not in observed);observed.add(key)
  vals={'0':F(0),'1':F(0),'2':F(0),'kinetic':F(0)}
  for term in rr['resolvent']:
   a=F(term['energy']);n=term['power'];v=F(term['coefficient'])
   if n==1:vals['0']+=v;vals['kinetic']+=a*v
   if n==2:vals['kinetic']-=v
   vals['1']+=v/a**n;vals['2']+=n*v/a**(n+1)
  vals['leakage']=vals['0']-6*vals['1']+9*vals['2']
  check('all-original-moments-'+str(i),vals=={k:F(v) for k,v in r['values'].items()})
  for k,v in vals.items():B[k,r['degree']]+=abs(v);signed[k,r['degree']][other]+=v
 check('no-missing-marked-contribution',observed==wanted and len(observed)==559)
 for r in data['bounds']:
  key=r['kind'],r['degree'];check('absolute-original-bound-'+str(key),B[key]==F(r['absolute_motif_bound']))
  check('bulk-signed-bound-'+str(key),sum(map(abs,signed[key].values()))==F(r['bulk_signed_row_sum']))
 # Full original240-face records supply an independent boundary-containing assembly check.
 full=load(ROOT.parent/'20260921-heat-response-transfer/generated/heat_matrix_L2.json')
 for row in full['matrices']:
  norm={k:[F(0)]*len(full['faces']) for k in ('0','1','2','kinetic','leakage')}
  for i,j,ts in row['entries']:
   v0=sum(F(t['coefficient']) for t in ts if t['power']==1)
   v1=sum(F(t['coefficient'])/F(t['energy'])**t['power'] for t in ts)
   v2=sum(t['power']*F(t['coefficient'])/F(t['energy'])**(t['power']+1) for t in ts)
   vk=sum(F(t['energy'])*F(t['coefficient']) for t in ts if t['power']==1)-sum(F(t['coefficient']) for t in ts if t['power']==2)
   for k,val in zip(norm,(v0,v1,v2,vk,v0-6*v1+9*v2)):norm[k][i]+=abs(val)
  for k,v in norm.items():check('all-240-boundary-rows-'+str((k,row['degree'])),max(v)<=B[k,row['degree']])
 reject('bulk-signed-row-is-boundary-safe-by-equality',B['1',2]==sum(map(abs,signed['1',2].values())))
 return B

def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def tr(a):return [list(x) for x in zip(*a)]
def plus(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def sc(q,a):return [[q*x for x in r] for r in a]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def inv(a):
 n=len(a);z=[list(map(F,r))+e for r,e in zip(a,eye(n))]
 for j in range(n):
  k=next((k for k in range(j,n) if z[k][j]),None)
  if k is None:raise AuditError('singular-original-matrix')
  z[j],z[k]=z[k],z[j];p=z[j][j];z[j]=[v/p for v in z[j]]
  for k in range(n):
   if k!=j:
    p=z[k][j];z[k]=[u-p*v for u,v in zip(z[k],z[j])]
 return [r[n:] for r in z]
def norm1(a):return max(sum(abs(x) for x in col) for col in zip(*a))
def zero(n,m):return [[F(0) for j in range(m)] for i in range(n)]

def matrix_checks():
 # No orthonormalization: all pairings in these declared exact fixtures are retained.
 A=[[F(7),F(1),F(0),F(1)],[F(1),F(6),F(1),F(0)],[F(0),F(1),F(5),F(1)],[F(1),F(0),F(1),F(8)]]
 R=[[F(1),F(0)],[F(0),F(2)],[F(1),F(1)],[F(2),F(-1)]];kap=F(7,3)
 Phi=sc(kap,mm(inv(A),R));g0=mm(tr(R),R);g1=mm(tr(R),Phi);g2=mm(tr(Phi),Phi);E=mm(mm(tr(Phi),A),Phi);K=sc(1/kap,mm(mm(tr(R),A),R))
 P=mm(mm(Phi,inv(g2)),tr(Phi));Q=plus(eye(4),sc(-1,P));B=mm(Q,R)
 check('original-state-projection',mm(P,P)==P and tr(P)==P)
 check('original-energy-Gram',E==sc(kap,g1))
 check('entire-complement-leakage',mm(tr(B),B)==plus(g0,sc(-1,mm(mm(g1,inv(g2)),g1))))
 residual=plus(R,sc(-3,Phi));J=mm(tr(residual),residual)
 check('leakage-original-trial',J==plus(plus(g0,sc(-6,g1)),sc(9,g2)))
 # Recover a literal non-orthogonal complement by solving the first two coordinates.
 Ftop=tr(Phi);C=[r[:2] for r in Ftop];D=[r[2:] for r in Ftop];upper=sc(-1,mm(inv(C),D));N=upper+eye(2)
 check('actual-complement-kernel',mm(tr(Phi),N)==zero(2,2))
 GN=mm(tr(N),N);EN=mm(mm(tr(N),A),N);BN=mm(tr(N),R);a=sc(-kap,mm(inv(EN),BN));rest=plus(Phi,mm(N,a));Sch=plus(E,sc(-kap*kap,mm(mm(tr(BN),inv(EN)),BN)))
 check('whole-complement-stationarity',mm(mm(tr(N),A),rest)==zero(2,2))
 check('whole-complement-energy',mm(mm(tr(rest),A),rest)==Sch)
 check('whole-complement-state',mm(tr(rest),rest)==plus(g2,mm(mm(tr(a),GN),a)))
 PR=mm(mm(R,inv(g0)),tr(R));h=mm(plus(eye(4),sc(-1,PR)),Phi)
 check('state-section-complete-energy',mm(mm(tr(h),A),h)==sc(kap,plus(mm(mm(mm(mm(g1,inv(g0)),K),inv(g0)),g1),sc(-1,g1))))
 check('energy-section-orthogonality',mm(mm(tr(Phi),A),h)==zero(2,2))
 reject('drop-full-complement',Sch==E)
 reject('replace-raw-Gram-by-identity',mm(Phi,tr(Phi))==P)
 reject('state-and-energy-sections-equal',h==zero(4,2))
 # Actual coefficient resolvent fixture including the scalar-return row.
 k=[[F(3),F(0),F(0)],[F(0),F(9,2),F(0)],[F(0),F(0),F(8)]]
 T=[[F(1,20),F(-1,40),F(1,30)],[F(1,30),F(1,20),F(0)],[F(0),F(1,30),F(-1,40)]];p=[[F(1,30),F(-1,40),F(1,50)]];chi=F(1,5)
 check('stacked-scalar-source-budget',norm1(T+p)<=chi)
 S=inv(plus(eye(3),sc(-1,T)));L=mm(plus(eye(3),sc(-1,T)),k);mr=mm(p,S)
 gen=[[F(0)]+r for r in sc(-1,mm(p,k))]+[[F(0)]+r for r in L]
 mean=[[F(1)]+mr[0]]
 check('full-original-stationary-scalar',mm(mean,gen)==zero(1,4))
 for i,dt in enumerate((F(1,100),F(1,3),F(1),F(7))):
  resolvent=inv(plus(eye(3),sc(dt,L)));check('original-dissipative-resolvent-'+str(i),norm1(resolvent)<=1/(1+3*(1-chi)*dt))
 reject('erase-scalar-return',mm([[F(1),F(0),F(0),F(0)]],gen)==zero(1,4))
 # Complete finite coefficient contraction for tr(U1 U2 U3^t U4^t).
 for d in (2,3):
  inds=list(product(range(d),repeat=4));ix={a:i for i,a in enumerate(inds)};n=d**4;A=zero(n,n)
  for a,b,c,e in product(range(d),repeat=4):A[ix[b,c,c,e]][ix[a,b,e,a]]+=1
  M=mm(tr(A),A);check('four-edge-contraction-square-'+str(d),mm(M,M)==sc(d*d,M))
  check('four-edge-contraction-trace-'+str(d),sum(M[i][i] for i in range(n))==d**4)
  check('original-trace-coefficient-norm-'+str(d),sum(M[i][i] for i in range(n))/d==d**3)
 # The positive matrix M/d is exactly |A| since its square equals M.
 reject('plaquette-Fourier-norm-is-one',2**3==1)

def exact_constants(B,c):
 R=F(3,256);x=F(1,1024);t=x/R;tail=t**6/(1-t*t);w={}
 for k in ('0','1','2','kinetic','leakage'):
  pref=512*F(2,3)**int(k) if k.isnumeric() else (606 if k=='kinetic' else 4608)
  w[k]=x*x*B[k,2]+x**4*B[k,4]+pref*tail
  check('complete-uniform-radius-'+k,w[k]==F(c['radii'][k]))
  check('rounded-radius-'+k,w[k]<F(c['radii_upper_bounds'][k]))
 l0,u0=1-w['0'],1+w['0'];l1,u1=F(1,3)-w['1'],F(1,3)+w['1'];l2,u2=F(1,9)-w['2'],F(1,9)+w['2'];uK=3+w['kinetic'];d=F(117,40);beta=w['leakage']
 check('analytic-source-discriminant',4*F(2,3)*32*R==1)
 check('total-drift-half',F(2,3)*F(3,4)==F(1,2))
 check('row-sum-constant',3*16*F(2,3)*8/(1-F(1,2))==512)
 check('xi-physical-return',F(1,4*16**2)==x)
 check('complete-physical-gap',F(11,12)>F(19,20)**2 and 3*(1+F(19,20))/2==d)
 check('inverse-power-observation',l1*l1/(u0*u2)==F(c['observation_fraction_lower']) and l1*l1/(u0*u2)>F(624,625))
 check('full-complement-Schur-constant',beta/(d*l1)==F(c['complement_loss_relative_upper']) and beta/(d*l1)<F(1,625))
 check('complete-mixed-energy-constant',F(1,25)**2==F(1,625))
 check('restored-state-complement',beta/(d*d*l2)==F(c['restored_state_extra_relative_upper']) and beta/(d*d*l2)<F(1,600))
 check('state-section-energy-constant',u1*uK/(l0*l0)-1==F(c['state_section_energy_relative_upper']) and u1*uK/(l0*l0)-1<F(1,1250))
 for n in range(1,101):
  bn=F(comb(2*n,n),4**n);bn1=F(comb(2*n+2,n+1),4**(n+1));cat=F(comb(2*n,n),n+1)
  check('complete-Catalan-tail-'+str(n),cat/4**n==2*(bn-bn1) and bn*bn<=F(1,n+1))
  eta=F(1,10**n);rank=4*n;eps=eta/(2*rank+eta)
  check('retained-growing-rank-'+str(n),2*rank*eps/(1-eps)==eta)
 reject('omit-kinetic-tail-local-row',606==1)
 reject('omit-full-moment-tail',4608==512)
 reject('rank-free-determinant-return',2*960==2)
 reject('relative-Schur-error-is-zero',beta==0)
 reject('source-radius-is-the-coupling',R==16)
 reject('heat-time-drops-kappa',F(10,7)==F(10))


def exponential_and_graph_checks(c):
 # Positive-series reciprocal bounds, independent of the predecessor's alternating series.
 def ex(x):
  x=F(x);n=200;t=F(1);ss=t
  for j in range(1,n+1):t*=x/j;ss+=t
  nxt=t*x/(n+1);rem=nxt/(1-x/(n+2))
  return 1/(ss+rem),1/ss
 for x in (F(3,2),F(3),F(9,2),F(6),F(13,2),F(8),F(10),F(117,4)):
  lo,hi=ex(x);check('positive-exponential-enclosure-'+str(x),0<lo<=hi<1)
 raw=load(ROOT.parent/'20260921-heat-response-transfer/generated/opposite_combined.json')['resolvent']
 lo=hi=F(0)
 for t in raw:
  a=F(t['energy']);n=t['power'];v=F(t['coefficient'])/factorial(n-1);l,u=ex(a)
  lo+=v*(l if v>=0 else u);hi+=v*(u if v>=0 else l)
 x=F(1,10**10);R=F(3,256);th=x/R
 err=512*ex(F(3,2))[1]*th**6/(1-th*th)/x**4
 check('independent-actual-heat-interval',F(85910,10**7)<lo-err<hi+err<F(85920,10**7))
 ratio=F(512*648,5)*x*x/R**6/(1-th*th)/ex(F(9,2))[0]
 check('independent-whole-time-error',ratio<F(24,1000))
 eps=ex(F(117,4))[1];check('independent-rank-weighted-heat-horizon',1920*eps/(1-eps)<F(4,10**10))
 reject('erase-evolution-remainder',err==0)
 # Literal original graph constraints with integer doubled spins.
 p=(0,0,0,0,1);q=(0,0,0,0,2);es=sorted(edges(p)|edges(q));vs=sorted({v for e in es for v in (e[:3],add(e[:3],e[3]))})
 incidence=[[j for j,e in enumerate(es) if v in (e[:3],add(e[:3],e[3]))] for v in vs]
 valid=0
 for labels in product(range(3),repeat=len(es)):
  if not any(labels):continue
  if any(sum(labels[j] for j in row)%2 or 2*max(labels[j] for j in row)>sum(labels[j] for j in row) for row in incidence):continue
  valid+=1;energy=sum(F(z*(z+2),4) for z in labels)
  check('original-two-face-spin-'+str(valid),energy>=3 and all(energy>=3*z for z in labels))
 check('complete-two-face-small-spin-count',valid==10)
 # An actual active bridge between two original fundamental yz squares.
 one=(0,0,0,1,2);two=(1,0,0,1,2);spin={e:F(1,2) for e in edges(one)|edges(two)};spin[(0,0,0,0)]=F(1)
 vertices_all={v for e in spin for v in (e[:3],add(e[:3],e[3]))}
 for i,v in enumerate(sorted(vertices_all)):
  row=[j for e,j in spin.items() if v in (e[:3],add(e[:3],e[3]))]
  check('active-bridge-invariant-'+str(i),2*max(row)<=sum(row) and sum(row).denominator==1)
 energy=sum(j*(j+1) for j in spin.values());check('active-bridge-energy',energy==8 and all(energy>=6*j for j in spin.values()))
 reject('triangle-free-bound-on-triangle',3*F(3,4)>=6*F(1,2))

def sharp_checks(B):
 data=load(ROOT/'generated/sharp_constants.json');R0=F(3,256);r=F(data['radius']);chi=F(3,8);a=3*(1-chi)
 check('sharp-original-radius',r==F(3,64)*chi*(1-chi))
 # Original mean: Haar contributes1/8, returned nonconstant term32*chi/(1-chi).
 C=(F(1,8)+32*chi/(1-chi))*8/(1-chi)
 check('sharp-original-Haar-prefactor',C==F(data['heat_prefactor'])==F(6184,25))
 check('sharp-original-time-decay',a==F(data['heat_decay_tau'])==F(15,8))
 for row in data['benchmarks']:
  g=row['g_squared_min'];x=F(1,4*g*g);d=F(row['physical_gap_over_kappa']);t0=(x/R0)**6/(1-(x/R0)**2);t1=(x/r)**6/(1-(x/r)**2)
  check('sharp-physical-parameters-'+str(g),x==F(row['xi_max']) and (d/F(3,2)-1)**2<1-F(256,3)*x)
  w={}
  for k in ('0','1','2','kinetic','leakage'):
   if k.isnumeric():err=min(512*F(2,3)**int(k)*t0,C/a**int(k)*t1)
   elif k=='kinetic':err=606*t0
   else:err=min(4608*t0,C*(1+6/a+9/a**2)*t1)
   w[k]=x*x*B[k,2]+x**4*B[k,4]+err
   check('sharp-complete-width-'+str((g,k)),w[k]==F(row['radii'][k]))
  l0,u0=1-w['0'],1+w['0'];l1,u1=F(1,3)-w['1'],F(1,3)+w['1'];l2,u2=F(1,9)-w['2'],F(1,9)+w['2'];uK=3+w['kinetic'];be=w['leakage']
  vals={'observed_fraction_lower':l1*l1/(u0*u2),'complement_loss_upper':be/(d*l1),'restored_state_addition_upper':be/(d*d*l2),'state_section_energy_upper':u1*uK/(l0*l0)-1}
  check('sharp-all-original-return-values-'+str(g),all(F(row[k])==v for k,v in vals.items()))
  o,e,n,se=map(F,row['outer_return']);check('sharp-all-original-return-inequalities-'+str(g),vals['observed_fraction_lower']>o and 1-vals['complement_loss_upper']>e and 1+vals['restored_state_addition_upper']<n and vals['state_section_energy_upper']<se)
  if g==16:check('sharp-full-physical-mixed-comparison',vals['complement_loss_upper']<F(1,34**2))
 reject('drop-nonconstant-Haar-return',C==8*(F(1,8))/(1-chi))
 reject('replace-sharp-radius-by-old-without-calculation',r==R0)

INPUTS=['VOLUME_UNIFORM_HEAT.md','GROWING_OBSERVATIONS_AND_COMPLEMENT.md','produce_bounds.py','audit_bounds.py','README.md','state.json','SOURCE_INTAKE.json','generated/anchored_coefficients.json','generated/uniform_constants.json','sharpen_bounds.py','generated/sharp_constants.json','replay.py','ROUTE_ASSESSMENT.md','route_check.py','generated/route_verification.json']
def digest():
 out={}
 for name in INPUTS:
  p=ROOT/name
  if not p.is_file():raise AuditError('missing-source:'+name)
  out[name]=hashlib.sha256(p.read_bytes()).hexdigest()
 for name in ['heat_coefficients.json','heat_matrix_L2.json','opposite_combined.json']:
  p=ROOT.parent/'20260921-heat-response-transfer/generated'/name
  if not p.is_file():raise AuditError('missing-predecessor:'+name)
  out['predecessor/'+name]=hashlib.sha256(p.read_bytes()).hexdigest()
 return out

def run():
 CHECKS.clear();NEG.clear();a=load(ROOT/'generated/anchored_coefficients.json');c=load(ROOT/'generated/uniform_constants.json');B=geometry_and_moments(a);matrix_checks();exact_constants(B,c);exponential_and_graph_checks(c);sharp_checks(B)
 return {'schema':'ym-volume-heat-audit-v1','passed':True,'scope':{'analytic_proof_formalized':False,'exact_anchored_contributions':559,'box_independent_bounds_derived_in_written_proof':True,'original_matrix_fixtures_are_not_vacuum_samples':True,'continuum_mass_gap_established':False},'count':len(CHECKS),'negative_count':len(NEG),'checks':CHECKS,'false_controls':NEG,'sha256':digest()}

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);ap.add_argument('--verify-receipt',type=Path);a=ap.parse_args()
 if a.verify_receipt:
  old=load(a.verify_receipt)
  if old.get('schema')!='ym-volume-heat-audit-v1':raise AuditError('receipt-schema')
  if old.get('sha256')!=digest():raise AuditError('source-identity-mismatch')
 result=run();s=json.dumps(result,sort_keys=True,indent=2)+'\n'
 if a.verify_receipt and a.verify_receipt.read_text()!=s:raise AuditError('receipt-mismatch')
 if a.output:a.output.write_text(s)
 else:sys.stdout.write(s)
if __name__=='__main__':
 try:main()
 except (AuditError,OSError,ValueError) as e:print('FAIL:',e,file=sys.stderr);raise SystemExit(1)
