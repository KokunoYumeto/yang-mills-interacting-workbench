from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
import json, random, math, hashlib
import numpy as np
import mpmath as mp
import sympy as sy

ROOT=Path(__file__).resolve().parent
rng=random.Random(2026101103)
counts={}
def qm(a,b):
 c,x,y,z=a;d,u,v,w=b
 return (c*d-x*u-y*v-z*w,c*u+x*d+y*w-z*v,c*v+y*d+z*u-x*w,c*w+z*d+x*v-y*u)
def qa(a,b):return tuple(x+y for x,y in zip(a,b))
def qs(s,a):return tuple(s*x for x in a)
def qi(a):return (a[0],-a[1],-a[2],-a[3])
def qv(a):return np.array(a[1:])*2
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def rot(q,v):return qm(qm(q,(0,*v)),qi(q))[1:]
def unit():
 r=[F(rng.randint(-2,2),rng.randint(1,3)) for _ in range(3)]
 t=sum(x*x for x in r)
 return ((1-t)/(1+t),*(2*x/(1+t) for x in r))
I=(1,0,0,0);O=(0,0,0,0)
def edges(m):
 return [(i,k,l,d) for i in range(m+1) for k in range(m+1) for l in range(m+1) for d in (1,2,3) if (i,k,l)[d-1]<m]
def tree(x):
 i,k,l=x
 return [((0,0,r,3),1) for r in range(l)]+[((0,b,l,2),1) for b in range(k)]+[((a,k,l,1),1) for a in range(i)]
def end(e):
 z=list(e[:3]);z[e[3]-1]+=1;return tuple(z)
def invword(w):return [(e,-s) for e,s in w[::-1]]
def word(e):return tree(e[:3])+[(e,1)]+invword(tree(end(e)))
def chords(m):return [e for e in edges(m) if (e[3]==2 and e[0]>0) or (e[3]==3 and e[:2]!=(0,0))]
def fw(x,d,e):
 y=list(x);y[d-1]+=1;z=list(x);z[e-1]+=1
 return [((*x,d),1),((*y,e),1),((*z,d),-1),((*x,e),-1)]
def faces(m):return [(x,d,e,fw(x,d,e)) for x in [(i,k,l) for i in range(m+1) for k in range(m+1) for l in range(m+1)] for d,e in [(1,2),(1,3),(2,3)] if x[d-1]<m and x[e-1]<m]
def reflect(w,m):return [((m-e[0]-(1 if e[3]==1 else 0),e[1],e[2],e[3]),-s if e[3]==1 else s) for e,s in w]
def jmul(a,b):
 return (qm(a[0],b[0]),qa(qm(a[1],b[0]),qm(a[0],b[1])),qa(qa(qm(a[2],b[0]),qs(2,qm(a[1],b[1]))),qm(a[0],b[2])))
def jeval(w,U):
 r=(I,O,O)
 for e,s in w:
  a=U[e] if s==1 else tuple(qi(x) for x in U[e]);r=jmul(r,a)
 return r
def value(w,U):return jeval(w,{e:(q,O,O) for e,q in U.items()})[0]

# Exact rational physical-link derivatives, before any gauge fixing.
for m in [1,2]:
 es=edges(m);U={e:unit() for e in es};V={e:F(rng.randint(-3,3),7) for e in es};z=(F(2,3),F(-1,5),F(3,7))
 ts={x:value(tree(x),U) for x in [(i,k,l) for i in range(m+1) for k in range(m+1) for l in range(m+1)]}
 p={x:sum(V[e] for e,s in tree(x)) for x in ts}
 Uj={e:(U[e],qm((0,*(V[e]*a/2 for a in rot(qi(ts[e[:3]]),z))),U[e]),O) for e in es}
 for e in chords(m):
  Z,dZ,_=jeval(word(e),Uj);hs=p[e[:3]]+V[e];ht=p[end(e)]
  exact=qa(qs(hs,qm((0,*(x/2 for x in z)),Z)),qs(-ht,qm(Z,(0,*(x/2 for x in z)))))
  assert dZ==exact,(m,e)
  formula=tuple(Z[0]*(hs-ht)*z[a]+(hs+ht)*cross(z,tuple(2*x for x in Z[1:]))[a]/2 for a in range(3))
  assert tuple(2*x for x in dZ[1:])==formula
  counts['exact_rational_rooted_derivatives']=counts.get('exact_rational_rooted_derivatives',0)+1
 # Direct derivatives of the transported coefficients check all signs
 # in the root-frame bracket, including ancestor and coincident edges.
 basis=[(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))]
 pairs=[(es[rng.randrange(len(es))],es[rng.randrange(len(es))]) for _ in range(18)]
 pairs += [(e,e) for e in es[:3]]
 pairs += [(e,f) for f in es for e,s in tree(f[:3])][:8]
 def coeff_der(e,alpha,f,beta):
  ae=rot(qi(ts[e[:3]]),basis[alpha])
  uj={ee:(q,qm((0,*(x/2 for x in ae)),q) if ee==e else O,O) for ee,q in U.items()}
  t,dt,_=jeval(tree(f[:3]),uj);mid=(0,*basis[beta])
  return qa(qm(qm(qi(dt),mid),t),qm(qm(qi(t),mid),dt))[1:]
 for e,f in pairs:
  alpha,beta=0,1;physical={}
  for ee in set([e,f]):
   vv=[F(0)]*3
   if ee==f:vv=[a+b for a,b in zip(vv,coeff_der(e,alpha,f,beta))]
   if ee==e:vv=[a-b for a,b in zip(vv,coeff_der(f,beta,e,alpha))]
   if e==f:
    cr=cross(rot(qi(ts[e[:3]]),basis[alpha]),rot(qi(ts[e[:3]]),basis[beta]))
    vv=[a-b for a,b in zip(vv,cr)]
   physical[ee]=rot(ts[ee[:3]],vv)
  ancestor_ef=any(ee==e for ee,s in tree(f[:3]));ancestor_fe=any(ee==f for ee,s in tree(e[:3]))
  for ee,vv in physical.items():
   coeff=int(e==f and ee==e)+int(ancestor_ef and ee==f)+int(ancestor_fe and ee==e)
   assert tuple(vv)==(F(0),F(0),F(-coeff))
  counts['exact_rational_root_frame_brackets']=counts.get('exact_rational_root_frame_brackets',0)+1

max_errors={}
def check(name,a,b,tol=3e-10):
 err=float(np.max(np.abs(np.asarray(a,dtype=float)-np.asarray(b,dtype=float))))
 max_errors[name]=max(max_errors.get(name,0),err)
 assert err<tol,(name,err,a,b)
 counts[name]=counts.get(name,0)+1

for m in [4,6]:
 n=m+1;h0=math.pi/(2*n);v=np.sqrt(2/n)*np.cos(math.pi*(np.arange(n)+.5)/n);w=-np.sqrt(2/n)*np.sin(math.pi*(np.arange(m)+1)/n);pref=np.r_[0,np.cumsum(w)]
 es=edges(m);cs=chords(m);fs=faces(m);verts=[(i,k,l) for i in range(n) for k in range(n) for l in range(n)]
 V1={};V3={}
 for e in es:
  i,k,l,d=e
  V1[e]=(w[i]*v[k] if d==1 else -v[i]*w[k] if d==2 else 0)/math.sqrt(2*n)
  V3[e]=(w[k]*v[l] if d==2 else -v[k]*w[l] if d==3 else 0)/math.sqrt(2*n)
 a={e:V1[e] for e in cs};b={e:V3[e] for e in cs}
 ps1={x:sum(V1[e] for e,s in tree(x)) for x in verts};ps3={x:sum(V3[e] for e,s in tree(x)) for x in verts}
 d1={e:ps1[e[:3]]+V1[e]-ps1[end(e)] for e in cs};d3={e:ps3[e[:3]]+V3[e]-ps3[end(e)] for e in cs};r3={e:ps3[e[:3]]+V3[e]+ps3[end(e)] for e in cs}
 check('physical_cochain_norms',[sum(x*x for x in V1.values()),sum(x*x for x in V3.values()),sum(V1[e]*V3[e] for e in es)],[1,1,0])
 for e in cs:
  i,k,l,d=e
  check('original_additive_images', [d1[e],d3[e]],[2*(v[0]-v[i])*w[k]/math.sqrt(2*n) if d==2 else 0,2*(v[0]-v[k])*w[l]/math.sqrt(2*n) if d==3 else 0])
 check('row_pairings',[sum(a[e]*d1[e] for e in cs),sum(b[e]*d3[e] for e in cs),sum(a[e]*d3[e] for e in cs),sum(b[e]*d1[e] for e in cs)],[1,1,0,0])
 check('curl_frequency',sum(sum(s*V3[e] for e,s in face)**2 for x,d,e,face in fs),8*math.sin(h0)**2)
 check('lambda_sum',sum(abs(b[e]*d3[e]) for e in cs),2*math.cos(h0)/math.tan(h0)/n)
 # Retain all word occurrences, including both copies of shared prefixes.
 A1=0;A3=0
 for e in cs:
  ns={f:sum(1 for ff,s in word(e) if ff==f) for f,s in word(e)}
  A1+=abs(a[e])*sum(x*x for x in ns.values());A3+=abs(b[e])*sum(x*x for x in ns.values())
 C=1/math.tan(h0);c=math.cos(h0)
 check('full_squared_occurrence_sums',[A1,A3],[m*math.sqrt(2/n)*C*(5*C-4*c),m/n*math.sqrt(2/n)*((9*m+5)*C*C-2*c*C)],tol=2e-9)
 U={e:tuple(float(x) for x in unit()) for e in es};ts={x:value(tree(x),U) for x in verts};Z={e:value(word(e),U) for e in cs}
 u1=sum((a[e]*qv(Z[e]) for e in cs),np.zeros(3));u3=sum((b[e]*qv(Z[e]) for e in cs),np.zeros(3))
 B13=sum((a[e]*r3[e]*qv(Z[e]) for e in cs),np.zeros(3));A33=sum(b[e]*d3[e]*Z[e][0] for e in cs)
 Bu1=np.cross(u1,B13)/2
 Uj={}
 for e in es:
  ae=(0,*(V3[e]*np.array(rot(qi(ts[e[:3]]),u1))/2));ad=(0,*(V3[e]*np.array(rot(qi(ts[e[:3]]),Bu1))/2))
  Uj[e]=(U[e],qm(ae,U[e]),qa(qm(ad,U[e]),qm(ae,qm(ae,U[e]))))
 Zj={e:jeval(word(e),Uj) for e in es}
 du1=sum((a[e]*qv(Zj[e][1]) for e in cs),np.zeros(3));du3=sum((b[e]*qv(Zj[e][1]) for e in cs),np.zeros(3))
 check('original_Bu1',du1,Bu1)
 check('preserved_original_h',2*np.dot(u1,du1),0)
 check('original_BS',np.dot(du1,u3)+np.dot(u1,du3),A33*np.dot(u1,u1)+np.dot(u3,np.cross(u1,B13))/2)
 # Compute the full reflected observable directly on reflected signed words.
 rz={e:jeval(reflect(word(e),m),Uj) for e in cs}
 ru1=sum((a[e]*qv(rz[e][0]) for e in cs),np.zeros(3));ru3=sum((b[e]*qv(rz[e][0]) for e in cs),np.zeros(3))
 rdu1=sum((a[e]*qv(rz[e][1]) for e in cs),np.zeros(3));rdu3=sum((b[e]*qv(rz[e][1]) for e in cs),np.zeros(3))
 BS=np.dot(du1,u3)+np.dot(u1,du3);BSR=np.dot(rdu1,ru3)+np.dot(ru1,rdu3);BD=BS+BSR
 Xi=2*(A33-1)*np.dot(u1,u1)+np.dot(u3,np.cross(u1,B13))-BD
 check('full_reflected_commutator',BS-BSR,2*np.dot(u1,u1)+Xi)
 def full_g(zz,uu1,uu3):
  out={e:np.zeros(3) for e in es}
  for cc in cs:
   ell=a[cc]*uu3+b[cc]*uu1;cl=zz[cc][0]*ell;cr=np.cross(qv(zz[cc]),ell)/2
   for e,sg in word(cc):out[e]+=sg*cl+cr
  return out
 gg=full_g(Z,u1,u3);gr=full_g({e:rz[e][0] for e in cs},ru1,ru3)
 RU={}
 for e in es:
  ep=(m-e[0]-(1 if e[3]==1 else 0),e[1],e[2],e[3]);RU[ep]=qi(U[e]) if e[3]==1 else U[e]
 tr={x:value(tree(x),RU) for x in verts};gradf={}
 for e in es:
  ep=(m-e[0]-(1 if e[3]==1 else 0),e[1],e[2],e[3])
  om=qm(qm(tr[ep[:3]],qi(U[e])),qi(ts[e[:3]])) if e[3]==1 else qm(tr[ep[:3]],qi(ts[e[:3]]))
  gradf[e]=gg[e]-( -1 if e[3]==1 else 1)*np.array(rot(qi(om),gr[ep]))
 check('full_reflection_metric_pullback',sum(V3[e]*np.dot(u1,gradf[e]) for e in es),BS-BSR)
 for e in es[::max(1,len(es)//7)]:
  alpha=1;z=np.eye(3)[alpha];ae=rot(qi(ts[e[:3]]),z)
  uj={f:(U[f],qm((0,*(np.array(ae)/2)),U[f]) if f==e else O,O) for f in es}
  def DS(reflected):
   zj={cc:jeval(reflect(word(cc),m) if reflected else word(cc),uj) for cc in cs}
   aa=sum((a[cc]*qv(zj[cc][0]) for cc in cs),np.zeros(3));bb=sum((b[cc]*qv(zj[cc][0]) for cc in cs),np.zeros(3))
   da=sum((a[cc]*qv(zj[cc][1]) for cc in cs),np.zeros(3));db=sum((b[cc]*qv(zj[cc][1]) for cc in cs),np.zeros(3))
   return np.dot(da,bb)+np.dot(aa,db)
  check('full_original_phase_gradient',DS(False)-DS(True),gradf[e][alpha])
 # Divergence: calculate three independent physical directional derivatives.
 div=0
 for alpha in range(3):
  z=np.eye(3)[alpha]
  uj={e:(U[e],qm((0,*(V3[e]*np.array(rot(qi(ts[e[:3]]),z))/2)),U[e]),O) for e in es}
  dv=sum((a[e]*qv(jeval(word(e),uj)[1]) for e in cs),np.zeros(3));div+=dv[alpha]
 check('direct_physical_divergence',div,0)
 # Full potential Hessian, including coefficient derivatives and root transport.
 total_direct=0;total_formula=0
 for x,dd,ee,face in fs:
  pf=jeval(face,Uj);ph=qm(qm(ts[x],pf[0]),qi(ts[x]));qp=qv(ph)
  prefix=(I,O,O);K=np.zeros((3,3));BK=np.zeros((3,3))
  for e,sg in face:
   letter=Zj[e] if sg==1 else tuple(qi(t) for t in Zj[e])
   ins=prefix if sg==1 else jmul(prefix,letter)
   for alpha in range(3):
    mid=(0,*np.eye(3)[alpha]);R=qm(qm(ins[0],mid),qi(ins[0]));DR=qa(qm(qm(ins[1],mid),qi(ins[0])),qm(qm(ins[0],mid),qi(ins[1])))
    K[:,alpha]+=sg*V3[e]*np.array(R[1:]);BK[:,alpha]+=sg*V3[e]*np.array(DR[1:])
   prefix=jmul(prefix,letter)
  ku=K@u1
  first=np.dot(qp,ku)/2
  second=(ph[0]*np.dot(ku,ku)+np.dot(qp,BK@u1+K@Bu1-ps3[x]*np.cross(u1,ku)))/2
  check('full_face_first_variation',-2*pf[1][0],first)
  check('full_face_second_variation',-2*pf[2][0],second)
  total_direct+=-2*pf[2][0];total_formula+=second
 check('full_potential_second_variation',total_direct,total_formula,tol=2e-8)

# Exact symbolic operator check on radius-two SU(2), with nonconstant
# divergence-free coefficient. This is a differential identity test,
# not an alternative state used in a vacuum estimate.
z=sy.symbols('c x y z');c,x,y,zz=z
xf=[[-x/2,c/2,-zz/2,y/2],[-y/2,zz/2,c/2,-x/2],[-zz/2,-y/2,x/2,c/2]]
def X(i,f):return sy.expand(sum(xf[i][k]*sy.diff(f,z[k]) for k in range(4)))
coef=c*c+zz*zz
def B(f):return sy.expand(coef*X(2,f))
def K(f):return sy.expand(-sum(X(i,X(i,f)) for i in range(3)))
pot=2-2*c
def H(f):return sy.expand(3*K(f)+5*pot*f)
def Ai(i,f):return sy.expand(B(X(i,f))-X(i,B(f)))
def Qi(i,f):return sy.expand(B(Ai(i,f))-Ai(i,B(f)))
assert sy.expand(X(2,coef))==0
for f in [c*x+y*zz,c*c+x*y+zz,1+x*y*zz]:
 lhs=sy.expand(B(B(H(f)))-2*B(H(B(f)))+H(B(B(f))))
 rhs=sy.expand(-3*sum(Qi(i,X(i,f))+X(i,Qi(i,f))+2*Ai(i,Ai(i,f)) for i in range(3))+5*B(B(pot))*f)
 assert sy.expand(lhs-rhs)==0
 counts['exact_SU2_double_commutator']=counts.get('exact_SU2_double_commutator',0)+1
for i,j,k,sg in [(0,1,2,-1),(1,2,0,-1),(2,0,1,-1)]:
 for f in z:assert sy.expand(X(i,X(j,f))-X(j,X(i,f))-sg*X(k,f))==0
counts['exact_SU2_bracket_signs']=12

mp.mp.dps=70
def path(j,kappa=mp.mpf(1)):
 j=mp.mpf(j);m=2*j**4;n=m+1;h=mp.pi/(2*n);s=mp.sin(h);c=mp.cos(h);C=mp.cot(h)
 N=3*m*n*n;M=3*m*m*n;gg=kappa/(200*j);xi=10000*j*j/(kappa*kappa)
 S1=mp.sqrt(2/n)*C*(C-c);A1=m*mp.sqrt(2/n)*C*(5*C-4*c)
 E=min(20000*j*j*M/kappa,300*j*mp.sqrt(N*M));BW=min(2*M,6*gg*mp.sqrt(N*M));xx=4*S1*S1
 return [S1*S1/j**12,S1*A1/j**16,(E/kappa)/j**13,BW/j**11,(BW/(6*s*s))/(xx*j**7),xx*E/kappa/j**25,j**7*(2*xi*s*s*xx)/(E/kappa)]
limits=[256/mp.pi**4,2560/mp.pi**4,mp.mpf(7200),mp.mpf(18)/25,3*mp.pi**2/1600,7372800/mp.pi**4,1600/(9*mp.pi**2)]
samples=[]
for j in [2,4,16,256,65536]:
 vals=path(j);samples.append({'j':j,'values':[mp.nstr(v,35) for v in vals]})
 if j==65536:
  for a,b in zip(vals,limits):assert abs(a/b-1)<mp.mpf('1e-16')
counts['original_path_limit_checks']=7

receipt={'generated_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','counts':counts,'max_numerical_errors':max_errors,'path_columns':['S1_squared/j12','S1A1/j16','energy_over_kappa/j13','BW/j11','curvature_occupation_ratio/j7','variance_bound/j25','curvature_gain_times_j7'],'path_samples':samples,'path_limits':[mp.nstr(v,35) for v in limits],'scope':'Exact rational rooted derivatives, exact symbolic SU(2) commutators, full original/reflected noncommuting numerical derivatives and face Hessians; no vacuum sampling and no claimed spectral endpoint.','proof_sha256':hashlib.sha256((ROOT/'CONJUGATE_VARIANCE.md').read_bytes()).hexdigest()}
(ROOT/'CONJUGATE_CHECKS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS','counts':counts,'max_error':max(max_errors.values())},indent=2))
