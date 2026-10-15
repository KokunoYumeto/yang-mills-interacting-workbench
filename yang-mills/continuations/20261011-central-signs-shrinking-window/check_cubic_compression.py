from pathlib import Path
import json
import numpy as np
import sympy as sp
O=Path(__file__).resolve().parent;rows=[];rng=np.random.default_rng(2026101504)
def yes(n,x):rows.append(dict(name=n,passed=bool(x)))
def eq(n,a,b,tol=2e-9):
 err=float(np.max(abs(np.asarray(a)-np.asarray(b))));scale=1+float(np.max(abs(a)))+float(np.max(abs(b)))
 rows.append(dict(name=n,passed=bool(err<=tol*scale),error=err))
def psd(n,A,tol=5e-8):
 ev=np.linalg.eigvalsh((A+A.conj().T)/2);rows.append(dict(name=n,passed=bool(ev.min()>=-tol*(1+np.max(abs(ev)))),min_eigenvalue=float(ev.min())))
e=sp.symbols('e',positive=True);C=sp.Matrix([[4+e,7+e],[7+e,10+e]])
yes('exact indefinite cubic correction',C.det()==-9)
L0=sp.Matrix([[1,0,1],[0,4,1],[1,1,2]])
yes('positive full fixture minors',[L0[:k,:k].det() for k in [1,2,3]]==[1,4,3])
I0=sp.eye(3);J0=I0[:,:2];Q0=I0-J0*J0.T;q0=(L0+I0)*(L0+I0/4)*(L0+4*I0);F0=sp.Matrix([1,0])
t0=(J0.T*q0*J0).inv()*F0;W0=Q0*q0*J0*t0
B0=L0*(L0+I0).inv()**2-sp.Rational(4,25)*L0*(L0+I0/4).inv()**2-sp.Rational(64,25)*L0*(L0+4*I0).inv()**2
yes('exact matched rational trial',t0==sp.Matrix([1482,-98])/31033)
yes('exact full rational complementary forcing',W0==sp.Matrix([0,0,75837])/62066)
yes('exact rational unfiltered orthogonality',((J0*F0).T*W0)[0]==0)
yes('exact nonzero signed filtered cross term',((J0*F0).T*B0*W0)[0]==sp.Rational(102961775980169187,7214417235183322850))

beta=9.638937558014562
km=-(-688*beta*beta+200*beta+5177)/(25*(beta+2)*(4*beta+17)**2);kp=113/2500;alpha=(kp-km)/2;dd=(kp+km)/2
def kernel(ev,z):return z*ev/(ev+z)**2-(16/25)*(z/4)*ev/(ev+z/4)**2-(16/25)*(4*z)*ev/(ev+4*z)**2
examples=[]
for case in range(12):
 n=12;m=7;nf=4
 raw=rng.normal(size=(n-1,n-1))+1j*rng.normal(size=(n-1,n-1));L=np.zeros((n,n),complex);L[1:,1:]=(raw.conj().T@raw)/8+np.eye(n-1)*.2
 if case%2==0:L[1,:]=0;L[:,1]=0;L[1,1]=.7
 J=np.eye(n,m,dtype=complex);Q=np.eye(n)-J@J.conj().T;A=J.conj().T@L@J;K=Q@L@J;D=Q@L@Q;V=K.conj().T@K
 F=np.zeros((m,nf),complex);F[1:]=rng.normal(size=(m-1,nf))+1j*rng.normal(size=(m-1,nf))
 if case%2==0:F[:,0]=0;F[1,:]=0;F[1,0]=1
 Z=J@F;S=Z.conj().T@Z;sig=np.linalg.eigvalsh(S).min();upper=np.linalg.eigvalsh(S).max();ev,U=np.linalg.eigh(L)
 for z in [.008,.2,1.7]:
  e1=21*z/4;e2=21*z*z/4;e3=z**3
  qL=L@L@L+e1*L@L+e2*L+e3*np.eye(n);qA=A@A@A+e1*A@A+e2*A+e3*np.eye(m)
  B=J.conj().T@qL@J;CC=A@V+V@A+K.conj().T@D@K+e1*V
  WW=K@A@A+D@K@A+K@V+D@D@K+e1*(K@A+D@K)+e2*K
  title=f'case{case}z{z}'
  eq(title+' full compressed cubic',B,qA+CC)
  eq(title+' full ordered complementary operator',WW,Q@qL@J)
  psd(title+' positive full compressed equation',B-e3*np.eye(m))
  t=np.linalg.solve(B,F);u=J@t;W=WW@t;Y=qL@u;t0=np.linalg.solve(qA,F)
  eq(title+' exact interior source matching',J.conj().T@Y,F)
  eq(title+' complete complementary forcing',Y,Z+W)
  eq(title+' all source complement inner products',Z.conj().T@W,np.zeros((nf,nf)))
  eq(title+' exact old new trial correction',t-t0,-np.linalg.solve(B,CC@t0))
  eq(title+' retained complementary correction',W,WW@t0-WW@np.linalg.solve(B,CC@t0))
  eq(title+' entire inverse tail',np.linalg.solve(qL,Z)-u,-np.linalg.solve(qL,W),1e-7)
  eq(title+' every source and trial vacuum projection',np.r_[Z[0],u[0],Y[0],W[0]],np.zeros(4*nf))
  R=W.conj().T@W;G=Y.conj().T@Y;H=Y.conj().T@Z
  eq(title+' source overlap equals full covariance',H,S)
  eq(title+' full Gram equals covariance plus residual',G,S+R)
  psd(title+' original source floor reaches full Gram',G-sig*np.eye(nf))
  psd(title+' coefficient inverse bound',np.eye(nf)/sig-np.linalg.inv(G))
  E=S-S@np.linalg.solve(G,S)
  eq(title+' all noncommuting residual expressions',E,R-R@np.linalg.solve(G,R))
  eq(title+' noncommuting mixed residual expression',E,S@np.linalg.solve(G,R))
  low=sig*R@np.linalg.inv(sig*np.eye(nf)+R);hi=upper*R@np.linalg.inv(upper*np.eye(nf)+R)
  psd(title+' exact residual lower sandwich',E-low);psd(title+' exact residual upper sandwich',hi-E)
  psd(title+' covariance residual order',S-E);psd(title+' forcing residual order',R-E)
  if case%2==0:eq(title+' zero residual direction retained',E[:,0],np.zeros(nf))
  Bf=(U*kernel(ev,z))@U.conj().T;Cresp=Z.conj().T@Bf@Z;T=Y.conj().T@Bf@Y
  eq(title+' all filtered mixed terms retained',T,Cresp+Z.conj().T@Bf@W+W.conj().T@Bf@Z+W.conj().T@Bf@W)
  pk=[-43*z**4/25,z**3/2,3801*z*z/400,z/2,-43/25]
  tt=sum(z*pk[ii]*(u.conj().T@np.linalg.matrix_power(L,ii+1)@u) for ii in range(5))
  eq(title+' complete five signed trial moments',T,tt)
  phi=rng.normal(size=nf)+1j*rng.normal(size=nf);coef=np.linalg.solve(G,S@phi);err=Z@phi-Y@coef
  eq(title+' optimal raw coefficient normal equation',Y.conj().T@err,np.zeros(nf))
  eq(title+' exact optimal residual Gram',np.vdot(err,err),np.vdot(phi,E@phi))
  perturb=rng.normal(size=nf)+1j*rng.normal(size=nf)
  eq(title+' full optimization Pythagoras',np.linalg.norm(Z@phi-Y@(coef+perturb))**2,np.linalg.norm(err)**2+np.linalg.norm(Y@perturb)**2)
  sv=float(np.vdot(phi,S@phi).real);r0=float(np.vdot(phi,R@phi).real);ro=float(np.vdot(phi,E@phi).real);cv=float(np.vdot(phi,Cresp@phi).real)
  val0=abs(cv-float(np.vdot(phi,T@phi).real)+alpha*r0);bound0=dd*np.sqrt(max(0,r0*(4*sv+r0)))
  valo=abs(cv-float(np.vdot(coef,T@coef).real)-alpha*ro);boundo=dd*np.sqrt(max(0,ro*(4*sv-3*ro)))
  yes(title+' unoptimized signed correction sign',val0<=bound0+1e-7)
  yes(title+' optimized signed correction sign',valo<=boundo+1e-7)
  if case==1 and z==.2:examples.append(dict(z=z,unfiltered_cross_norm=float(np.linalg.norm(Z.conj().T@W)),filtered_cross_norm=float(np.linalg.norm(Z.conj().T@Bf@W)),residual_eigenvalues=np.linalg.eigvalsh(R).tolist(),source_floor=sig,full_gram_floor=float(np.linalg.eigvalsh(G).min()),coefficient_count=nf))
out=dict(checks=len(rows),all_passed=all(r['passed'] for r in rows),scope='Exact block algebra and noncommuting positive-operator fixtures, including exact vacuum and singular residual directions; no Yang-Mills vacuum sampled.',examples=examples,rows=rows)
(O/'CUBIC_COMPRESSION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:out[k] for k in ['checks','all_passed','examples']}));assert out['all_passed'],[r for r in rows if not r['passed']]
