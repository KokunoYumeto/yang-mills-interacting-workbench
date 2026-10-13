from pathlib import Path
import json,itertools,numpy as np
O=Path(__file__).resolve().parent
T=np.array([[[0,-1j/2],[-1j/2,0]],[[0,-.5],[.5,0]],[[-1j/2,0],[0,1j/2]]])
def skew(g):
 x,y,z=g;return np.array([[0,-z,y],[z,0,-x],[-y,x,0]])
def product(xs):
 out=np.eye(2,dtype=complex)
 for x in xs:out=out@x
 return out
rng=np.random.default_rng(130304);rows=[]
def ck(name,x,y):
 err=float(np.linalg.norm(x-y));scale=1+float(np.linalg.norm(x))+float(np.linalg.norm(y))
 assert err<2e-11*scale,(name,err,scale)
 rows.append(dict(name=name,relative_error=err/scale))
q=4;verts=list(itertools.product(range(q+1),repeat=3));edges=[]
for z in verts:
 for d in range(3):
  if z[d]<q:
   w=list(z);w[d]+=1;edges.append((z,tuple(w),d))
index={(z,d):i for i,(z,w,d) in enumerate(edges)}
stars={v:[] for v in verts}
for i,(v,w,d) in enumerate(edges):stars[v].append(i);stars[w].append(i)
for case in range(8):
 U=[]
 for e in edges:
  r=rng.integers(-8,9,size=3)/7;den=1+float(r@r);c=(1-float(r@r))/den;v=2*r/den
  U.append(c*np.eye(2)+2*sum(v[k]*T[k] for k in range(3)))
 U=np.array(U)
 if case==7:U[:]=np.eye(2)
 n=len(U);g=np.zeros((n,3));H=np.zeros((n,n,3,3));wval=0
 for z,d,k,coef in [((0,0,0),0,1,.7),((1,1,1),0,2,-1.1),((1,1,1),1,2,1.4)]:
  zd=list(z);zd[d]+=1;zk=list(z);zk[k]+=1
  ids=[index[(z,d)],index[(tuple(zd),k)],index[(tuple(zk),d)],index[(z,k)]]
  factors=[U[ids[0]],U[ids[1]],U[ids[2]].conj().T,U[ids[3]].conj().T]
  fval=float(np.trace(product(factors)).real);wval+=coef*fval
  diffs=[[T[a]@factors[p] if p<2 else -factors[p]@T[a] for a in range(3)] for p in range(4)]
  for p,e in enumerate(ids):
   for a in range(3):
    x=factors.copy();x[p]=diffs[p][a];g[e,a]+=coef*np.trace(product(x)).real
   H[e,e]+=-coef*fval/4*np.eye(3)
   for t,f in enumerate(ids):
    if e==f:continue
    for a in range(3):
     for b in range(3):
      x=factors.copy();x[p]=diffs[p][a];x[t]=diffs[t][b];H[e,f,a,b]+=coef*np.trace(product(x)).real
 def Q(v,f):
  a,b,d=edges[f]
  if v==a:return np.eye(3)
  assert v==b
  return -np.array([[-2*np.trace(T[i]@U[f]@T[j]@U[f].conj().T).real for j in range(3)] for i in range(3)])
 for e,(v,w,d) in enumerate(edges):
  if not np.any(g[e]) and not np.any(H[e]):continue
  chi=0.;res=0.;local=set([e])
  for point,sigma in [(v,1),(w,-1)]:
   Qe=Q(point,e);m=len(stars[point])-1;chi+=1/m
   D=H[e,e]+sigma*.5*skew(g[e])
   ck('gauge Hessian row with signed original transports',sum(H[e,f]@Q(point,f) for f in stars[point]),-sigma*.5*skew(g[e])@Qe)
   for f in stars[point]:
    if f==e:continue
    local.add(f);Z=H[e,f]@Q(point,f)@Qe.T+D/m;res+=float(np.sum(Z*Z))
   ck('diagonal symmetric and gauge skew orthogonality',np.sum(D*D),np.sum(H[e,e]*H[e,e])+.5*(g[e]@g[e]))
  outside=sum(float(np.sum(H[e,f]*H[e,f])) for f in range(n) if f not in local)
  row=float(np.sum(H[e]*H[e]));diag=float(np.sum(H[e,e]*H[e,e]));Ge=float(g[e]@g[e])
  ck('complete two-endpoint row defect',row,(1+chi)*diag+chi/2*Ge+res+outside)
  assert chi>=.4-1e-12

 if case in [0,7]:
  vertex_index={v:i for i,v in enumerate(verts)};K=np.zeros((3*n,3*len(verts)))
  for f,(v,w,direction) in enumerate(edges):
   K[3*f:3*f+3,3*vertex_index[v]:3*vertex_index[v]+3]=np.eye(3)
   K[3*f:3*f+3,3*vertex_index[w]:3*vertex_index[w]+3]=Q(w,f)
  ck('complete original gauge gradient',K.T@g.reshape(-1),np.zeros(K.shape[1]))
  e=index[((1,1,1),0)];keep=np.ones(3*n,dtype=bool);keep[3*e:3*e+3]=False
  Ke=K[3*e:3*e+3];Ko=K[keep];Ho=H[e].transpose(1,0,2).reshape(3,3*n)[:,keep]
  v,w,direction=edges[e];Bg=np.zeros((3,K.shape[1]));Bg[:,3*vertex_index[v]:3*vertex_index[v]+3]=-.5*skew(g[e]);Bg[:,3*vertex_index[w]:3*vertex_index[w]+3]=.5*skew(g[e])@Q(w,e)
  Y=Bg-H[e,e]@Ke;ck('full covariant row constraint',Ho@Ko,Y)
  def pinv_positive(L):
   ev,evc=np.linalg.eigh(L);inv=np.zeros_like(ev);good=ev>1e-10;inv[good]=1/ev[good]
   return (evc*inv)@evc.T,int((~good).sum())
  Li,nzero=pinv_positive(Ko.T@Ko)
  if case==7:assert nzero==3
  else:assert nzero==0
  F=Y@Li@Ko.T;Ar=Ho-F
  ck('pseudoinverse row at changing gauge rank',F@Ko,Y)
  ck('complete residual kills gauge map',Ar@Ko,np.zeros_like(Y))
  ck('full covariant row orthogonality',np.sum(F*Ar),0)
  eff=float(np.trace(Y@Li@Y.T))
  ck('full covariant graph energy',np.sum(Ho*Ho),eff+np.sum(Ar*Ar))
  chi=1/(len(stars[v])-1)+1/(len(stars[w])-1)
  assert eff>=chi*(np.sum(H[e,e]*H[e,e])+.5*(g[e]@g[e]))-1e-10
  rows.append(dict(name='full graph dominates two original stars',defect=eff-chi*(np.sum(H[e,e]*H[e,e])+.5*(g[e]@g[e])),gauge_zero_modes=nzero))
  Lfull,nzero=pinv_positive(K.T@K)
  c=rng.normal(size=n)+1j*rng.normal(size=n);weighted=(c[:,None]*g).reshape(-1);eta=K.T@weighted;pv=K@Lfull@eta
  ck('physical norm vertical loss',np.vdot(pv,pv),np.vdot(eta,Lfull@eta))
  ck('pointwise vertical projection idempotence',K@Lfull@K.T@pv,pv)
  ck('horizontal complement orthogonality',np.vdot(pv,weighted-pv),0)
  assert np.linalg.norm(pv)<=np.linalg.norm(weighted)+1e-10

# Actual-ground receiving constants: algebra only, no replacement state.
for kap in [.2,1.,3.7]:
 for j in [1,2,100,10000]:
  a=1/(100*j);chi=.4
  theta=(-1.5*a+np.sqrt(2.25*a*a+144/(kap*kap*(1+chi))))/8
  ck('actual kinetic root',4*theta**2+1.5*a*theta,9/(kap*kap*(1+chi)))
  assert theta<1.5/(kap*np.sqrt(1+chi))
  U0=theta/a;ell=18/(9+16*U0+4*np.sqrt(U0*(9+16*U0)))
  ck('retained individual face root',(9+16*U0)*ell**2-4*(9+16*U0)*ell+36,0)
out=dict(checks=len(rows),all_passed=True,scope='Original open cubic graph, right-field SU(2) convention, gauge-invariant three-plaquette trace function, all endpoint transport signs, connection term, boundary degrees and complete row defect. This test function is not the actual Yang–Mills ground logarithm; only the universal gauge identity is tested. Flat and nonflat full graph pseudoinverses, their gauge zero modes, full row remainders and exact vertical norm loss are checked. Actual-ground root checks are algebra diagnostics after the written SG substitution.',rows=rows)
(O/'GAUGE_HESSIAN_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(checks=len(rows),all_passed=True)))
