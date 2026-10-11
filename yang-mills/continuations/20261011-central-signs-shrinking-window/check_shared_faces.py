"""Original SU(2) word and differential identities; manufactured compact-state receiving maps. No Yang–Mills vacuum samples."""
from pathlib import Path
import json,itertools,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent
rows=[]
def check(name,error,tol=3e-8):
    error=float(error)
    assert abs(error)<=tol,(name,error,tol)
    rows.append(dict(name=name,error=error,tolerance=tol,passed=True))
sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)]
T=[-.5j*s for s in sig];I=np.eye(2,dtype=complex);Z=np.zeros((2,2),complex)
rng=np.random.default_rng(20261011072)
edges=[(z,d) for z in itertools.product(range(3),repeat=3) for d in range(3) if z[d]<2]
index={e:i for i,e in enumerate(edges)}
faces=[];planes=[]
for z in itertools.product(range(3),repeat=3):
    for d,e in itertools.combinations(range(3),2):
        if z[d]==2 or z[e]==2:continue
        zd=list(z);ze=list(z);zd[d]+=1;ze[e]+=1
        faces.append([(index[(z,d)],1),(index[(tuple(zd),e)],1),(index[(tuple(ze),d)],-1),(index[(z,e)],-1)])
        planes.append((d,e))
def invword(w):return [(e,-s) for e,s in reversed(w)]
def prod(fs):
    out=I.copy()
    for a in fs:out=out@a
    return out
def value(word,U):return prod([U[e] if s==1 else U[e].conj().T for e,s in word])
def incident(face,ed):
    k=next(i for i,(e,s) in enumerate(face) if e==ed)
    sign=face[k][1];A=face[k+1:]+face[:k]
    H=[(ed,1)]+A if sign==1 else A+[(ed,-1)]
    return sign,A,H,H if sign==1 else invword(H)
pairs=[]
fixtures={}
for p,q in itertools.combinations(range(len(faces)),2):
    shared=set(e for e,s in faces[p])&set(e for e,s in faces[q])
    if not shared:continue
    assert len(shared)==1
    ed=next(iter(shared))
    union=set(e for e,s in faces[p]+faces[q])
    assert len(union)==7
    contained=[r for r,f in enumerate(faces) if set(e for e,s in f)<=union]
    assert contained==[p,q]
    for pp,qq in [(p,q),(q,p)]:
        sp,ap,hp,xp=incident(faces[pp],ed);sq,aq,hq,yq=incident(faces[qq],ed)
        shape='coplanar' if planes[pp]==planes[qq] else 'perpendicular'
        fixture=(pp,qq,ed,sp,sq,ap,aq,hp,hq,xp,yq)
        fixtures.setdefault((shape,sp,sq),fixture)
        pairs.append(fixture)
check('all incident-face graphs have seven edges and exactly two contained faces',0)
assert {(s,t) for sh,s,t in fixtures}=={(-1,-1),(-1,1),(1,-1),(1,1)}
def jmul(a,b):
    return (a[0]@b[0],a[1]@b[0]+a[0]@b[1],a[2]@b[0]+2*a[1]@b[1]+a[0]@b[2])
def jinv(a):return tuple(x.conj().T for x in a)
def wordjet(word,U,ed,t):
    out=(I,Z,Z)
    for e,s in word:
        item=(U[e],t@U[e],t@t@U[e]) if e==ed else (U[e],Z,Z)
        if s==-1:item=jinv(item)
        out=jmul(out,item)
    return out
def tr(j):return tuple(np.trace(x).real for x in j)
def testjet(x,y):
    a,ad,add=tr(x);b,bd,bdd=tr(y)
    c,cd,cdd=tr(jmul(x,jinv(y)))
    return (a*b+.37*c+.13*a*a,
            ad*b+a*bd+.37*cd+.26*a*ad,
            add*b+2*ad*bd+a*bdd+.37*cdd+.26*(ad*ad+a*add))
def reduced(X,Y):
    dx=dy=diag=0.
    for t in T:
        x=(X,t@X,t@t@X);y=(Y,t@Y,t@t@Y)
        dx+=testjet(x,(Y,Z,Z))[2]
        dy+=testjet((X,Z,Z),y)[2]
        diag+=testjet(x,y)[2]
    return dx,dy,(diag-dx-dy)/2
for trial in range(12):
    U=[]
    for _ in edges:
        q=rng.normal(size=4);q/=np.linalg.norm(q)
        U.append(q[0]*I+1j*sum(q[k+1]*sig[k] for k in range(3)))
    for p,q,ed,sp,sq,ap,aq,hp,hq,xp,yq in pairs:
        Hp=value(hp,U);Hq=value(hq,U);X=value(xp,U);Y=value(yq,U)
        gp=np.array([-tr(wordjet(faces[p],U,ed,t))[1] for t in T])
        gq=np.array([-tr(wordjet(faces[q],U,ed,t))[1] for t in T])
        raw=gp@gq
        G=Hp@(Hq.conj().T if sp*sq==1 else Hq)
        R=Hp@(Hq if sp*sq==1 else Hq.conj().T)
        six=ap+(invword(aq) if sp*sq==1 else aq)
        name=f'word{trial}:{p},{q},{ed}'
        check(name+': shared-edge contraction',raw-(np.trace(G).real-np.trace(R).real)/4)
        check(name+': six-edge trace map',np.trace(G).real-np.trace(value(six,U)).real)
        check(name+': aligned sign map',raw-(np.trace(X@Y.conj().T).real-np.trace(X@Y).real)/4)
        check(name+': full forward/inverse derivative',np.max(np.abs(gp+sp*np.array([np.trace(t@Hp).real for t in T]))))
    for key,fix in fixtures.items():
        p,q,ed,sp,sq,ap,aq,hp,hq,xp,yq=fix
        X=value(xp,U);Y=value(yq,U);dx,dy,k=reduced(X,Y)
        selected=sorted(set(e for e,s in faces[p]+faces[q]))
        weights={e:float(rng.uniform(.1,.9)) for e in selected}
        tp=sum(weights[e] for e,s in faces[p])/4
        tq=sum(weights[e] for e,s in faces[q])/4
        u=weights[ed];lap=lap_h=0.
        for ee in selected:
            one=sum(testjet(wordjet(xp,U,ee,t),wordjet(yq,U,ee,t))[2] for t in T)
            lap+=one;lap_h+=weights[ee]*one
            expected=dx+dy+2*k if ee==ed else dx if ee in {e for e,s in faces[p]} else dy
            check(f'lap{trial}:{key}: individual edge{ee}',one-expected)
        check(f'lap{trial}:{key}: full original seven-edge Casimir',lap-4*dx-4*dy-2*k)
        check(f'lap{trial}:{key}: full original weighted Casimir',lap_h-4*tp*dx-4*tq*dy-2*u*k)
        kap=.7;b=1.3
        f=testjet((X,Z,Z),(Y,Z,Z))[0]
        Dp=2-np.trace(value(faces[p],U)).real
        Dq=2-np.trace(value(faces[q],U)).real
        check(f'lap{trial}:{key}: retained weighted potential scalars',
              -kap*lap_h+b*(tp*Dp+tq*Dq)*f-(-kap*(4*tp*dx+4*tq*dy+2*u*k)+b*(2*tp+2*tq-tp*np.trace(X).real-tq*np.trace(Y).real)*f))
# Two-face coupling cannot be removed from the differential operator.
X=np.cos(.7)*I+1j*np.sin(.7)*sig[0];Y=X.copy()
gp=np.array([np.trace(t@X).real for t in T])
check('central product derivative is positive at a noncritical paired point',min(0.,gp@gp))
assert gp@gp>.1
check('central derivative vanishes at the identity',sum(abs(np.trace(t).real) for t in T))
# Manufactured compact differential identities for the full exterior receiving map.
# The signed potential below is constructed from a known positive periodic ground;
# this tests product differentiation, not the original plaquette vacuum.
xx=(2*np.pi*np.arange(160)/160)[:,None]
yy=(2*np.pi*np.arange(160)/160)[None,:]
for trial in range(24):
    A,B,C=rng.uniform(-.3,.3,3);kap=.6+.03*trial
    w=A*np.cos(xx)+B*np.cos(yy)+C*np.cos(xx-yy)
    wx=-A*np.sin(xx)-C*np.sin(xx-yy);wy=-B*np.sin(yy)+C*np.sin(xx-yy)
    wxx=-A*np.cos(xx)-C*np.cos(xx-yy);wyy=-B*np.cos(yy)-C*np.cos(xx-yy)
    psi=np.exp(w);psi/=math.sqrt(np.mean(psi*psi))
    mu=psi*psi;m=np.mean(mu,axis=1,keepdims=True)
    mx=np.mean(2*mu*wx,axis=1,keepdims=True)
    mxx=np.mean(mu*(2*wxx+4*wx*wx),axis=1,keepdims=True)
    phi=np.sqrt(m);aa=mx/(2*m);phixx=mxx/(2*m)-mx*mx/(4*m*m)
    chi=psi/phi;chix=chi*(wx-aa);chiyy=chi*(wyy+wy*wy)
    Vin=.41*(1-np.cos(xx));Vout=.29*(1-np.cos(yy));energy=3.
    V=energy+kap*(wxx+wx*wx+wyy+wy*wy);Vcross=V-Vin-Vout
    Ey=lambda f:np.mean(chi*chi*f,axis=1,keepdims=True)
    R=kap*np.mean(chix*chix,axis=1,keepdims=True)+np.mean(chi*(-kap*chiyy+Vout*chi),axis=1,keepdims=True)+Ey(Vcross)
    check(f'exterior{trial}: exact full marginal ground equation',np.max(np.abs(-kap*phixx+Vin+R-energy)))
    hx,hin,hcross=rng.uniform(.1,.9,3)
    Q=-kap*hx*(wxx+wx*wx)+hin*Vin+hcross*Vcross
    S=kap*hx*np.mean(chix*chix,axis=1,keepdims=True)+hcross*Ey(Vcross)
    Ah=-kap*hx*phixx+hin*Vin+S
    check(f'exterior{trial}: full weighted quotient and retained conditional kinetic',np.max(np.abs(Ah-Ey(Q))))
    avg=lambda f:np.mean(mu*f)
    avgb=lambda f:np.mean(m*f)
    mean=avg(Q);n=avg((Q-mean)**2)/(kap*kap)
    right=avgb((Ah-avgb(Ah))**2+Ey((Q-Ah)**2))/(kap*kap)
    check(f'exterior{trial}: complete physical variance decomposition',n-right)
    Cobs=np.cos(xx)+.3*np.sin(2*xx)
    check(f'exterior{trial}: exact inside-source receiving covariance',
          avg((Cobs-avg(Cobs))*(-(Q-mean)/kap))+avgb((Cobs-avgb(Cobs))*(Ah-avgb(Ah)))/kap)
# Exchange-even and exchange-odd exact covariance decomposition (finite vector diagnostic).
for trial in range(25):
    plus=rng.normal(size=4);minus=rng.normal(size=4);kap=.8+.04*trial
    vp=np.r_[plus,plus];vm=np.r_[minus,-minus]
    tp,tq,u=rng.uniform(0,1,3)
    centered=.5*(tp+tq-2*u)*vp+.5*(tp-tq)*vm
    rhs=((tp+tq-2*u)**2*(vp@vp)+(tp-tq)**2*(vm@vm))/(4*kap*kap)
    check(f'exchange{trial}: full retained even-odd covariance',centered@centered/(kap*kap)-rhs)
# Reproducible diagram of the actual perpendicular graph and full-state map.
fig=plt.figure(figsize=(16,7),layout='constrained')
ax=fig.add_subplot(121,projection='3d')
graph=[((0,0,0),(1,0,0)),((1,0,0),(1,1,0)),((0,1,0),(1,1,0)),((0,0,0),(0,1,0)),
       ((1,0,0),(1,0,1)),((0,0,1),(1,0,1)),((0,0,0),(0,0,1))]
for i,(v,w) in enumerate(graph):
    ax.plot([v[0],w[0]],[v[1],w[1]],[v[2],w[2]],color='#c94b40' if i==0 else '#386aa3',lw=4 if i==0 else 2)
for v,label in [((0,0,0),'0'),((1,0,0),'e₁'),((0,1,0),'e₂'),((1,1,0),'e₁+e₂'),((0,0,1),'e₃'),((1,0,1),'e₁+e₃')]:
    ax.scatter(*v,color='#243444',s=20);ax.text(*v,label,fontsize=11)
ax.text(.35,0,-.17,r'$u=\frac{1}{2}$',color='#b43e33',fontsize=13)
ax.set_title('Two original faces, one shared edge\nEvery other edge has weight 1/6; both face averages are 1/4',fontsize=12)
ax.set_xlabel('first lattice coordinate');ax.set_ylabel('second lattice coordinate');ax.set_zlabel('third lattice coordinate')
ax.set_box_aspect((1,1,1));ax.view_init(elev=23,azim=-56)
ax.set_xticks([0,1]);ax.set_yticks([0,1]);ax.set_zticks([0,1])
bx=fig.add_subplot(122);bx.axis('off');bx.set_xlim(0,1);bx.set_ylim(0,1)
def box(y,text,color):
    bx.add_patch(FancyBboxPatch((.03,y),.94,.18,boxstyle='round,pad=.012',facecolor=color,edgecolor='#8393a2'))
    bx.text(.5,y+.09,text,ha='center',va='center',fontsize=11)
box(.77,'Seven original Haar links and six vertex gauges\nExact physical isometry to simultaneous class functions of (X,Y)\nAll ordered words, inverses and radius-two metrics retained.','#e8eff8')
box(.48,r'$\widetilde{H}^{(2)}=-\kappa(4\Delta_X+4\Delta_Y+2\mathcal{K})+b(D_X+D_Y)$'+'\n'+r'$\upsilon_h^{(2)}=2(u-t)(\Psi^{-1}\mathcal{K}\Psi-\langle\Psi,\mathcal{K}\Psi\rangle)$'+'\nStrictly positive norm for b > 0, κ > 0, u ≠ t.','#e4f1e8')
box(.15,'Actual full-lattice marginal keeps the exterior state:\n'+r'$(\widetilde{H}^{(2)}+\widehat{R}_B)\widehat{\varphi}_B=E_0\widehat{\varphi}_B$'+'\nWeighted fluctuation also retains $R_B$, $S_h$ and conditional variance.','#fff2db')
for y1,y2 in [(.76,.67),(.47,.34)]:
    bx.add_patch(FancyArrowPatch((.5,y1),(.5,y2),arrowstyle='->',mutation_scale=17,color='#5b6e80'))
bx.text(.5,.035,'SF10–SF27. Exact maps and finite-regulator positivity;\nno regulator-uniform mass or no-gap conclusion.',ha='center',va='center',fontsize=10)
fig.suptitle('The shared-edge interaction and its exact exterior-state terms',fontsize=17)
for ext in ['png','svg']:fig.savefig(O/f'SHARED_FACE_PHYSICAL_MAP.{ext}',dpi=160)
plt.close(fig)
result=dict(description=__doc__,checks=len(rows),all_passed=all(r['passed'] for r in rows),geometric_sign_fixtures=[list(x) for x in fixtures],original_ordered_pairs=len(pairs),rows=rows)
(O/'SHARED_FACE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
