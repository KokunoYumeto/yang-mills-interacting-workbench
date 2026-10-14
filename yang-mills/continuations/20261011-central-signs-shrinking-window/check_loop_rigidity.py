from pathlib import Path
import itertools,json
import numpy as np
import sympy as s
O=Path(__file__).resolve().parent;rows=[]
def eq(name,a,b,tol=4e-10):
    a=np.asarray(a);b=np.asarray(b);err=float(np.max(np.abs(a-b)));scale=1+float(np.max(np.abs(a)))+float(np.max(np.abs(b)))
    rows.append(dict(name=name,passed=bool(err<=tol*scale),error=err))
def yes(name,b):rows.append(dict(name=name,passed=bool(b)))
pauli=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex)];J=[-1j*p for p in pauli];T=[p/2 for p in J];I=np.eye(2,dtype=complex);rng=np.random.default_rng(20261014)
def product(v):
    out=I.copy()
    for q in v:out=out@q
    return out
def su2():
    q=rng.normal(size=4);q/=np.linalg.norm(q);return q[0]*I+sum(q[i+1]*J[i] for i in range(3))
def exp(angle,axis):return np.cos(angle)*I+np.sin(angle)*axis
eq('original bracket constant two',J[0]@J[1]-J[1]@J[0],2*J[2]);eq('original half-sized orthonormal generators',T[0]@T[1]-T[1]@T[0],T[2])
avec=s.Matrix([s.Rational(1,2),0,-s.Rational(1,2)]);bvec=s.Matrix([s.Rational(1,2),1,s.Rational(1,2)]);a2=avec.multiply_elementwise(avec)
yes('exact four-link coefficient determinant',s.Matrix.hstack(avec,bvec,a2).det()==s.Rational(1,4))
for case,weights in enumerate([[1.],[1.,1.],[1.,1.,1.,1.],[1.,2.,3.,5.],[1.,.5,2.,1.7,3.],[.2,.7,1.4,.6,2.3,1.1]]):
    m=len(weights);cum=np.cumsum(weights);links=[su2() for _ in weights];W=product(links);K=(W.conj().T-W)/4;trace=np.trace(W).real;grads=[]
    eq(f'full generator contraction case{case}',sum(np.trace(t@W).real*t for t in T),K)
    for e in range(m):
        before=product(links[:e]);after=product(links[e+1:]);grad=sum(np.trace(before@t@links[e]@after).real*t@links[e] for t in T)*weights[e];grads.append(grad)
    for i in range(1,m+1):
        dp=sum(product(links[:e])@grads[e]@product(links[e+1:i]) for e in range(i))
        eq(f'original weighted partial gradient{case}/{i}',dp,cum[i-1]*K@product(links[:i]))
    eq(f'complete trace derivative{case}',np.trace(sum(product(links[:e])@grads[e]@product(links[e+1:]) for e in range(m))).real,cum[-1]*(1-trace*trace/4))
    axis=J[1];q=[su2() for _ in range(m-1)];theta=.73
    Ps=[exp(theta*c/cum[-1],axis)@qq for c,qq in zip(cum[:-1],q)]+[exp(theta,axis)]
    original=[(I if i==0 else Ps[i-1].conj().T)@Ps[i] for i in range(m)]
    eq(f'recovered original factors{case}',product(original),exp(theta,axis))
    for i in range(m):eq(f'full theta speed and gradient{case}/{i}',-.5*cum[-1]*np.sin(theta)*(cum[i]/cum[-1])*axis@Ps[i],cum[i]*(-np.sin(theta)*axis/2)@Ps[i])
    eq(f'critical plus total holonomy{case}',exp(0,axis),I);eq(f'critical minus total holonomy{case}',exp(np.pi,axis),-I)
    if m==1:continue
    angles=np.pi*cum[:-1]/cum[-1];aa=np.sin(angles)*np.cos(angles);bb=np.sin(angles)**2;eps=1e-6
    for i,alpha in enumerate(angles):
        plus=exp(-alpha,J[2])@exp(alpha,np.cos(eps)*J[2]+np.sin(eps)*J[0]);minus=exp(-alpha,J[2])@exp(alpha,np.cos(eps)*J[2]-np.sin(eps)*J[0])
        eq(f'complete endpoint tangent{case}/{i}',(plus-minus)/(2*eps),aa[i]*J[0]-bb[i]*J[1],tol=2e-9)
    # Polynomial interpolation is evaluated with every original point retained.
    unit=1-np.prod(np.array([1-bb/value for value in set(bb)]),axis=0);eq(f'generated constant coefficient{case}',unit,np.ones(m-1))
    for i in range(m-1):
        vals=np.ones(m-1)
        for j in range(m-1):
            if j!=i:vals*=((aa-aa[j])*(aa[i]-aa[j])+(bb-bb[j])*(bb[i]-bb[j]))/((aa[i]-aa[j])**2+(bb[i]-bb[j])**2)
        expected=np.zeros(m-1);expected[i]=1;eq(f'all separated coefficient slots{case}/{i}',vals,expected)

L=1;kappa=.8;a=.01;b=1/(kappa*a*a);vertices=list(itertools.product(range(-L,L+1),repeat=3));edges=[]
def shift(p,axis):q=list(p);q[axis]+=1;return tuple(q)
for p in vertices:
    for axis in range(3):
        if p[axis]<L:edges.append((p,axis))
faces=[]
for p in vertices:
    for i in range(3):
        for j in range(i+1,3):
            if p[i]<L and p[j]<L:faces.append([((p,i),1),((shift(p,i),j),1),((shift(p,j),i),-1),((p,j),-1)])
def hol(links,word):return product([links[e] if sign==1 else links[e].conj().T for e,sign in word])
def potential(links):return 2*b*len(faces)-b*sum(np.trace(hol(links,word)).real for word in faces)
e=((0,0,0),0);f=((0,0,0),2)
yes('unique full original crossing face',sum(any(edge==e for edge,sgn in w) and any(edge==f for edge,sgn in w) for w in faces)==1)
def val(theta,eta):
    links={e:I.copy() for e in edges};links[e]=exp(theta,J[2]);links[f]=exp(eta,J[2]);return potential(links)
for theta,eta in [(0.,0.),(.3,.3),(.4,-.2),(.9,.9),(1.1,.7)]:
    expected=3*b*(2-2*np.cos(theta))+3*b*(2-2*np.cos(eta))+b*(2-2*np.cos(theta-eta));eq(f'complete original crossing potential{theta,eta}',val(theta,eta),expected)
    diff=val(theta,eta)-val(theta,0)-val(0,eta)+val(0,0);eq(f'all four mixed potential terms{theta,eta}',diff,2*b*(-np.cos(theta-eta)+np.cos(theta)+np.cos(eta)-1))
    if theta==eta and theta>0:yes(f'strict actual nonseparability{theta}',diff<0)
# Rooted two-face words at the original coordinates of the proof.
left=[(((0,0,0),1),1),(((-1,1,0),0),-1),(((-1,0,0),1),-1),(((-1,0,0),0),1)]
right=[(((0,0,0),0),1),(((1,0,0),1),1),(((0,1,0),0),-1),(((0,0,0),1),-1)]
def reflect_vertex(p):return (-p[0],p[1],p[2])
for trial in range(5):
    links={edge:su2() for edge in edges};reflected={}
    for edge in edges:
        p,axis=edge
        if axis==0:target=(reflect_vertex(shift(p,0)),axis);reflected[edge]=links[target].conj().T
        else:target=(reflect_vertex(p),axis);reflected[edge]=links[target]
    U=hol(links,left);V=hol(links,right);UR=hol(reflected,left);VR=hol(reflected,right)
    eq(f'exact common-root reflection left{trial}',UR,V.conj().T);eq(f'exact common-root reflection right{trial}',VR,U.conj().T)
    eq(f'full original reflected potential{trial}',potential(reflected),potential(links));eq(f'retained perimeter under reflection{trial}',np.trace(UR@VR),np.trace(U@V))
out=dict(all_passed=all(r['passed'] for r in rows),checks=len(rows),rows=rows,scope='Direct original radius-two generator and weighted loop-flow contractions, complete critical-endpoint tangent and coefficient algebra, original Wilson crossing-face finite differences, and full-box reflection. These checks do not compute the actual ground or replace the global proof of rigidity and nonzero covariance.')
(O/'LOOP_RIGIDITY_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print(json.dumps(dict(all_passed=out['all_passed'],checks=len(rows),failed=[r for r in rows if not r['passed']])));assert out['all_passed']
