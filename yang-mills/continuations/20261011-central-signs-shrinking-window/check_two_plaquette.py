from pathlib import Path
import itertools,json
import numpy as np
import sympy as s
from scipy.special import roots_jacobi,roots_legendre
O=Path(__file__).resolve().parent;rows=[]
def exact(name,a,b=0):
    passed=bool(s.expand(a-b)==0);rows.append(dict(name=name,passed=passed))
def eq(name,a,b,tol=2e-10):
    a=np.asarray(a);b=np.asarray(b);err=float(np.max(np.abs(a-b)));scale=1+float(np.max(np.abs(a)))+float(np.max(np.abs(b)))
    rows.append(dict(name=name,passed=bool(err<=tol*scale),error=err))
def yes(name,b):rows.append(dict(name=name,passed=bool(b)))
x,y,z,k,b=s.symbols('x y z k b',real=True);Q=[x,y,z];r=s.Rational
D=4-x*x-y*y-z*z+x*y*z
G=s.Matrix([[4-x*x,z/2-x*y/4,3*y/2-3*x*z/4],[z/2-x*y/4,4-y*y,3*x/2-3*y*z/4],[3*y/2-3*x*z/4,3*x/2-3*y*z/4,6-3*z*z/2]])
drift=s.Matrix([-3*x,-3*y,-r(9,2)*z])
def lap(f):return s.expand(sum(G[i,j]*s.diff(f,Q[i],Q[j]) for i in range(3) for j in range(3))+sum(drift[i]*s.diff(f,Q[i]) for i in range(3)))
for j in range(3):exact(f'divergence component{j}',sum(s.diff(G[i,j],Q[i]) for i in range(3)),drift[j])
boundary=G*s.Matrix([s.diff(D,q) for q in Q])
for j,v in enumerate([2*x,2*y,3*z]):exact(f'boundary polynomial component{j}',boundary[j],-D*v)
exact('complete determinant',G.det(),r(3,16)*D*(128-12*x*x-12*y*y-3*x*y*z-2*z*z))
for signs in itertools.product([-1,1],repeat=2):
    M=s.diag(signs[0],signs[1],signs[0]*signs[1]);sub=dict(zip(Q,list(M*s.Matrix(Q))))
    for i in range(3):
        for j in range(3):exact(f'full center metric{signs}/{i}/{j}',G[i,j].subs(sub,simultaneous=True),(M*G*M)[i,j])
S=x+y;V=4*b-b*S
def H(f):return s.expand(-k*lap(f)+V*f)
H2=V*V-3*k*b*S
H3=V**3-9*k*b*V*S-9*k*k*b*S-2*k*b*b*(8-x*x-y*y+z-x*y/2)
exact('full unshifted second heat power',H(H(1)),H2);exact('full unshifted third heat power',H(H(H(1))),H3)
exact('third heat perimeter derivative',-s.diff(H3,z)/6,k*b*b/3)
for f,expected in [(x*x+y*y-2,-8*(x*x+y*y-2)),(x*y,z-r(13,2)*x*y),(z,-r(9,2)*z)]:exact(f'polynomial Laplacian {f}',lap(f),expected)
p1=S/(3*k);p2=(x*x+y*y-2)/(24*k*k)+4*x*y/(39*k*k)+8*z/(351*k*k)-1/(9*k*k)
exact('first full ground equation',-k*lap(p1)+4-S,4)
exact('second full ground equation',-k*lap(p2)+(4-S)*p1,4*p1-2/(3*k))
density2=s.expand(p1*p1+2*p2)
expected2=r(7,36)*(x*x+y*y-2)/(k*k)+r(150,351)*x*y/(k*k)+r(16,351)*z/(k*k)
exact('complete second density coefficient',density2,expected2)
def character_part(f,ix,iy):
    return s.expand(sum((sx**ix)*(sy**iy)*f.subs({x:sx*x,y:sy*y,z:sx*sy*z},simultaneous=True) for sx,sy in itertools.product([-1,1],repeat=2))/4)
exact('second invariant density',character_part(density2,0,0),r(7,36)*(x*x+y*y-2)/(k*k))
exact('second full perimeter moment',character_part(density2,1,1),(150*x*y+16*z)/(351*k*k))
exact('second cycle covariance',character_part(density2,1,1)-4*x*y/(9*k*k),(16*z-6*x*y)/(351*k*k))

pauli=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex)];T=[-1j*p/2 for p in pauli]
rng=np.random.default_rng(20261014)
def su2():
    q=rng.normal(size=4);q/=np.linalg.norm(q)
    return q[0]*np.eye(2)-1j*sum(q[i+1]*pauli[i] for i in range(3))
# Link order A,B,C,D,E,F,G; each original trace word keeps its orientation.
words=[[(1,1),(2,-1),(3,-1),(0,1)],[(4,1),(5,1),(6,-1),(1,-1)],[(4,1),(5,1),(6,-1),(2,-1),(3,-1),(0,1)]]
def wordmat(links,word,edge=None,generator=None,order=0):
    ans=np.eye(2,dtype=complex)
    for idx,sign in word:
        m=links[idx] if sign==1 else links[idx].conj().T
        if idx==edge:
            if sign==1:m=np.linalg.matrix_power(generator,order)@m
            else:m=m@np.linalg.matrix_power(-generator,order)
        ans=ans@m
    return ans
Gfun=s.lambdify((x,y,z),G,'numpy');dfun=s.lambdify((x,y,z),drift,'numpy')
for trial in range(12):
    links=[su2() for _ in range(7)];vals=np.array([np.trace(wordmat(links,w)).real for w in words]);U=wordmat(links,words[0]);VV=wordmat(links,words[1])
    eq(f'original perimeter cancellation{trial}',np.trace(U@VV),vals[2])
    deriv=np.zeros((21,3));dr=np.zeros(3)
    for edge in range(7):
        for alpha,generator in enumerate(T):
            for j,w in enumerate(words):
                if any(idx==edge for idx,sign in w):
                    deriv[3*edge+alpha,j]=np.trace(wordmat(links,w,edge,generator,1)).real
                    dr[j]+=np.trace(wordmat(links,w,edge,generator,2)).real
    eq(f'all21 original gradients matrix{trial}',deriv.T@deriv,Gfun(*vals))
    eq(f'all21 original second derivatives{trial}',dr,np.asarray(dfun(*vals)).ravel())
    yes(f'positive interior kinetic{trial}',np.linalg.eigvalsh(Gfun(*vals)).min()>0)
    # Independent original vertex gauge transformations, g_source U g_target^-1.
    vertices=[su2() for _ in range(6)];ends=[(0,1),(1,4),(3,4),(0,3),(1,2),(2,5),(4,5)]
    transformed=[vertices[i]@m@vertices[j].conj().T for m,(i,j) in zip(links,ends)]
    eq(f'full vertex gauge orbit{trial}',[np.trace(wordmat(transformed,w)) for w in words],vals)
    signs=rng.choice([-1,1],7);transformed=[v*m for v,m in zip(signs,links)]
    sig1=np.prod(signs[[0,1,2,3]]);sig2=np.prod(signs[[1,4,5,6]])
    eq(f'original seven signs{trial}',[np.trace(wordmat(transformed,w)) for w in words],vals*np.array([sig1,sig2,sig1*sig2]))

nodes,weights=roots_jacobi(16,.5,.5);trace=2*nodes;weights*=2/np.pi;cs,cw=roots_legendre(16);cw/=2
xx,yy,cc=np.meshgrid(trace,trace,cs,indexing='ij');wx,wy,wc=np.meshgrid(weights,weights,cw,indexing='ij');ww=(wx*wy*wc).ravel();xx=xx.ravel();yy=yy.ravel();cc=cc.ravel();zz=xx*yy/2-np.sqrt((4-xx*xx)*(4-yy*yy))*cc/2
def mean(f):return np.dot(ww,np.asarray(f))
eq('full original Haar mass',ww.sum(),1);eq('full trace moments',[mean(xx),mean(yy),mean(zz),mean(xx*xx),mean(yy*yy),mean(xx**4),mean(xx*yy*zz),mean(xx*xx*yy*yy)],[0,0,0,1,1,2,.5,1])
eq('original ground normalization coefficient',mean(s.lambdify((x,y,z,k),p1*p1+2*p2,'numpy')(xx,yy,zz,.8)),0)
eq('mixed diagonal Haar integral',mean(xx*xx*(4-xx*xx)),2)
eq('mixed cross Haar integral',mean(xx*yy*(zz/2-xx*yy/4)),0)
for phi in [[1,0],[0,1],[1,1],[1,-1],[1,1j],[.3+.7j,-1.1+.2j]]:
    p,q=phi;integrand=np.conj(p*xx*(4-xx*xx)+q*yy*(zz/2-xx*yy/4))*p*xx+np.conj(p*xx*(zz/2-xx*yy/4)+q*yy*(4-yy*yy))*q*yy
    eq(f'all raw complex mixed leading coefficients{phi}',mean(integrand),2*(abs(p)**2+abs(q)**2))

signs=np.array(list(itertools.product([-1,1],repeat=7)));masks=list(range(128));chars=np.array([[np.prod(tau[[i for i in range(7) if mask>>i&1]]) if mask else 1 for mask in masks] for tau in signs])
R1=sum(1<<i for i in [0,1,2,3]);R2=sum(1<<i for i in [1,4,5,6]);cyc=[R1,R2,R1^R2];ends=[(0,1),(1,4),(3,4),(0,3),(1,2),(2,5),(4,5)]
cycles=[]
for mask in range(1,128):
    degree=np.zeros(6,dtype=int)
    for idx,(i,j) in enumerate(ends):
        if mask>>idx&1:degree[i]+=1;degree[j]+=1
    if np.all(degree%2==0):cycles.append(mask)
yes('all127 physical character constraints',set(cycles)==set(cyc) and len(cycles)==3)
eq('all128 Fourier characters retained',chars.T@chars,128*np.eye(128))
for sig1,sig2 in itertools.product([-1,1],repeat=2):eq(f'all center fiber size{sig1,sig2}',np.sum((chars[:,R1]==sig1)&(chars[:,R2]==sig2)),32)
for trial in range(3):
    X,Y,Z=[(.3,-.4,.6),(.7,.1,-.8),(0.,0.,1.)][trial];bb=.04;kk=.8
    # A positive polynomial test density from the computed Taylor coefficients.
    # It is not claimed to be an exact Wilson ground.
    tx=X*chars[:,R1];ty=Y*chars[:,R2];tz=Z*chars[:,R1^R2]
    psi=1+bb*s.lambdify((x,y,z,k),p1,'numpy')(tx,ty,tz,kk)+bb**2*s.lambdify((x,y,z,k),p2,'numpy')(tx,ty,tz,kk)
    prob=psi*psi/np.sum(psi*psi);mom=prob@chars;C=chars[:,1:].T@(prob[:,None]*chars[:,1:])-np.outer(mom[1:],mom[1:]);ci=np.array(cyc)-1;ni=np.array([m-1 for m in range(1,128) if m not in cyc])
    eq(f'full124 noncycle moments{trial}',mom[ni+1],np.zeros(124));eq(f'full cycle to noncycle blocks{trial}',C[np.ix_(ci,ni)],np.zeros((3,124)))
    rr=mom[cyc];rr1,rr2,rr12=rr
    expected=np.array([[1-rr1**2,rr12-rr1*rr2,rr2-rr1*rr12],[rr12-rr1*rr2,1-rr2**2,rr1-rr2*rr12],[rr2-rr1*rr12,rr1-rr2*rr12,1-rr12**2]])
    eq(f'full physical covariance block{trial}',C[np.ix_(ci,ci)],expected);yes(f'all127 covariance eigenvalues positive{trial}',np.linalg.eigvalsh(C).min()>0)
    inverse=chars[:,1:].T@((1/prob)[:,None]*chars[:,1:])/128**2
    eq(f'all127 original covariance inverse{trial}',C@inverse,np.eye(127))
    eq(f'cycle covariance full inverse{trial}',expected@inverse[np.ix_(ci,ci)],np.eye(3))
    probabilities=np.array([prob[(chars[:,R1]==u)&(chars[:,R2]==v)].sum() for u,v in itertools.product([-1,1],repeat=2)])
    spectrum=np.sort(np.concatenate([np.linalg.eigvalsh(expected),np.tile(4*probabilities,31)]))
    eq(f'all31 noncycle blocks and physical spectrum{trial}',np.linalg.eigvalsh(C),spectrum)
    eq(f'full cycle determinant{trial}',np.linalg.det(expected),256*np.prod(probabilities))
out=dict(all_passed=all(row['passed'] for row in rows),checks=len(rows),rows=rows,scope='Exact symbolic identities, original seven-link matrix derivatives, complete128sign algebra, and exact-degree Haar quadrature. Polynomial density checks test the finite-character identities only; they are not computations of the exact Wilson ground. Analytic ground, semigroup sign and full-lattice receiver proofs are in SHARED_LINK_TWO_PLAQUETTE.md.')
(O/'TWO_PLAQUETTE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print(json.dumps(dict(all_passed=out['all_passed'],checks=len(rows),failed=[row for row in rows if not row['passed']])));assert out['all_passed']
