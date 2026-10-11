"""Diagnostics for BQ1–BQ18. Manufactured curved states and projection matrices are not Yang–Mills samples."""
from pathlib import Path
import json,math
import numpy as np
import sympy as sp
from numpy.polynomial.chebyshev import chebgauss
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent;rows=[]
def check(name,error,tol=2e-9):
    error=float(error);assert abs(error)<=tol,(name,error,tol)
    rows.append(dict(name=name,error=error,tolerance=tol,passed=True))
x,y,A,B,C,kap,h=sp.symbols('x y A B C kap h',real=True)
tx=(1-x*x)/4;ty=(1-y*y)/4;wx=A+C*y;wy=B+C*x
def dx(f):return tx*sp.diff(f,x,2)-3*x*sp.diff(f,x)/4
def dy(f):return ty*sp.diff(f,y,2)-3*y*sp.diff(f,y)/4
def L(f):return -kap*(dx(f)+dy(f)+2*tx*wx*sp.diff(f,x)+2*ty*wy*sp.diff(f,y))
Kx=-3*x*wx/4+tx*wx**2;Ky=-3*y*wy/4+ty*wy**2
V=5+kap*(Kx+Ky);Vx=kap*(-3*A*x/4+tx*A*A);Vy=kap*(-3*B*y/4+ty*B*B)
comm=L(h*Kx)+h*(dx(V)+2*tx*wx*sp.diff(V,x))
assert sp.expand(comm)==0
check('exact symbolic full commutator with retained E0=5',0)
alpha=sp.diff(V-Vx-Vy-5,x);ca=sp.diff(kap*Kx-Vx,x);u=alpha-ca;v=kap*sp.diff(Kx,y)
Fx=sp.diff(V-kap*Kx,x);S=-3*x*wx/4+2*tx*wx**2
qy=sp.diff(S,y);Y=tx*C*wx;X=tx*ty*C*C
J=-(tx*sp.diff(u,x)-3*x*u/4+2*tx*wx*u)
force=-kap*(dy(S)+2*ty*wy*sp.diff(S,y))
for name,expr in [('boundary force cancellation',u-Fx),('first moment vector identity',qy-v/kap-2*Y),('entire second moment forcing',force-J+2*tx*wx*u+2*kap*X),('full residual weighted divergence',J+ty*sp.diff(v,y)-3*y*v/4+2*ty*wy*v)]:
    assert sp.expand(expr)==0,name
    check('exact symbolic '+name,0)
exprs=[alpha,ca,u,v,Fx,qy,Y,X,J,force,Kx,sp.diff(Kx,y)]
fn=sp.lambdify((x,y,A,B,C,kap),exprs,'numpy')
n=100;theta=np.arange(1,n+1)*np.pi/(n+1);nodes=np.cos(theta);weights=2/(n+1)*np.sin(theta)**2
xx=nodes[:,None];yy=nodes[None,:];base=weights[:,None]*weights[None,:]
txx=(1-xx**2)/4;tyy=(1-yy**2)/4
for i,(aa,bb,cc,kk) in enumerate([(a,b,c,k) for a,b,c in [(.2,.3,.07),(-.15,.21,-.04),(.33,-.2,.13),(.08,.04,.19),(-.2,-.17,.05),(.37,.1,-.11)] for k in [.7,1.,1.7]]):
    rho=np.exp(2*(aa*xx+bb*yy+cc*xx*yy));Z=np.sum(base*rho);mu=base*rho/Z
    vals=[np.asarray(t)+np.zeros_like(mu) for t in fn(xx,yy,aa,bb,cc,kk)]
    al,ca1,uu,vv,ff,qyd,YY,XX,JJ,forcing,kxx,kxy=vals
    avg=lambda t:np.sum(mu*t)
    ey=np.sum(mu*yy,axis=1)/np.sum(mu,axis=1);xi=cc*(yy-ey[:,None])
    T=avg(txx*xi**2);OO=avg(XX);bbound=avg(txx*al**2);F2=avg(txx*ff**2);v2=avg(tyy*vv**2)
    check(f'family{i}: exact projection orthogonality',avg(txx*ca1*uu)-v2)
    check(f'family{i}: complete two-projection identity',bbound-avg(txx*ca1**2)-F2-2*v2)
    check(f'family{i}: one-half off-diagonal remainder',v2-bbound/4+avg(txx*(ca1-al/2)**2))
    check(f'family{i}: force mean',np.max(np.abs(np.sum(mu*ff,axis=1))))
    check(f'family{i}: original quotient scalar',avg(kxx)+avg(txx*(aa+cc*yy)**2))
    check(f'family{i}: mixed Hessian force trace',kk*OO+avg(txx*xi*ff))
    check(f'family{i}: force projection remainder',F2-kk*kk*OO*OO/T-avg(txx*(ff+kk*OO/T*xi)**2))
    m1=kk*avg(tyy*qyd*qyd)
    check(f'family{i}: exact first moment cross term',m1-v2/kk-4*avg(tyy*vv*YY)-4*kk*avg(tyy*YY*YY))
    bzero=txx*(aa+cc*yy)*uu+kk*OO;zz=XX-OO
    check(f'family{i}: centered divergence mean',avg(JJ))
    check(f'family{i}: centered score force mean',avg(bzero))
    check(f'family{i}: centered mixed Hessian mean',avg(zz))
    m2=avg(forcing**2)
    expansion=avg(JJ**2+4*bzero**2+4*kk*kk*zz**2-4*JJ*bzero-4*kk*JJ*zz+8*kk*bzero*zz)
    check(f'family{i}: all six second-moment terms',m2-expansion)
rng=np.random.default_rng(20261011)
for i in range(30):
    d=12;r=3+i%7;s=2+i%8
    basis=np.linalg.qr(rng.normal(size=(d,r)))[0];P=basis@basis.T
    al=np.zeros(d);al[:s]=rng.normal(size=s);pa=P@al;ca=pa.copy();ca[s:]=0;vv=pa-ca;uu=al-ca
    check(f'projection{i}: complete norm identity',np.dot(al,al)-np.dot(ca,ca)-np.dot(uu,uu)-2*np.dot(vv,vv))
    check(f'projection{i}: half remainder',np.dot(vv,vv)-np.dot(al,al)/4+np.dot(ca-al/2,ca-al/2))
# Original cube crossing incidence and full vector-sum remainders.
for q in range(1,7):
    counts={}
    verts={(i,j,k) for i in range(q+1) for j in range(q+1) for k in range(q+1)}
    def add(z,e):
        z=list(z);z[e]+=1;return tuple(z)
    faces=[]
    for z in [(i,j,k) for i in range(-1,q+1) for j in range(-1,q+1) for k in range(-1,q+1)]:
        for d in range(3):
            for e in range(d+1,3):
                edges=[(z,d),(add(z,d),e),(add(z,e),d),(z,e)]
                inside=[a for a in edges if a[0] in verts and add(a[0],a[1]) in verts]
                if 0<len(inside)<4:
                    assert len(inside)==1
                    edge=inside[0];counts[edge]=counts.get(edge,0)+1;faces.append(edge)
    assert max(counts.values())<=2 and len(faces)==12*q*(q+1)
    check(f'cube{q}: exact original crossing count',len(faces)-12*q*(q+1))
    for edge,r in counts.items():
        vec=rng.normal(size=(r,3));exact=np.sum(vec,axis=0)@np.sum(vec,axis=0)
        expansion=r*np.sum(vec*vec)-sum(np.sum((vec[a]-vec[b])**2) for a in range(r) for b in range(a+1,r))
        check(f'cube{q}: edge{edge}: retained vector remainder',exact-expansion)
Cheat=2+2*math.sqrt(4+2*math.pi)
def bounds(j,kind):
    a=1/(100*j);R=1.;k=1.;ell=math.log(math.e+R/a)
    K=max(1,math.floor(math.sqrt(R/a) if kind=='sqrt' else R/(a*ell)))
    q=math.ceil(R/a)+3;n=q+2*K
    N=3*n*(n+1)**2;M=3*n*n*(n+1);cross=12*n*(n+1)
    Lam=min(2*M,3*k*a*math.sqrt(N*M))+2*cross
    Amax=N*min(8/(k*k*a*a),Cheat/(k*a))**2
    Omax=math.sqrt(2)*Lam/(k**3*a**3*math.sqrt(K))
    Fmax=2*Lam/(k*k*a**4*K)
    mmax=k*(math.sqrt(2*Lam/K)/(2*k*k*a*a)+2*math.sqrt(Amax*Omax))**2
    return a,K,Lam,Omax,Fmax,mmax
for kind in ['sqrt','log']:
    a,K,lam,omax,fmax,mmax=bounds(10**12,kind)
    # Explicit bounds converge to their proved constants; logarithmic collars converge slowly.
    LR=33.;MR=12*math.sqrt(2)*Cheat**2*LR
    tol=.25 if kind=='log' else 1e-5
    check(kind+': original finite Lambda coefficient',a*a*lam/LR-1,tol)
    check(kind+': mixed-Hessian upper function coefficient',a**5*math.sqrt(K)*omax/(math.sqrt(2)*LR)-1,tol)
    check(kind+': first-moment upper function coefficient',a**10*math.sqrt(K)*mmax/MR-1,.5 if kind=='log' else 1e-5)
fig,ax=plt.subplots(figsize=(13,7));ax.set_xlim(0,13);ax.set_ylim(0,7);ax.axis('off')
def box(x0,y0,w0,h0,t,color):
    ax.add_patch(FancyBboxPatch((x0,y0),w0,h0,boxstyle='round,pad=0.12',facecolor=color,edgecolor='#50687e'))
    ax.text(x0+w0/2,y0+h0/2,t,ha='center',va='center',fontsize=11)
def arrow(a,b):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='->',mutation_scale=16,color='#33465c'))
ax.text(6.5,6.6,'Original conditional force: exact boundary projection',ha='center',fontsize=17,weight='bold')
box(.4,4.2,3.5,1.5,r'$E\,dV=b\,d\mathcal{W}_Q+b\alpha$'+'\n'+r'$\alpha=E\,d\mathcal{W}_\times$', '#e5eef6')
box(4.7,4.2,3.6,1.5,r'$\kappa\,dK_Q=b\,d\mathcal{W}_Q+bP\alpha$'+'\nFull original weighted projection $P$', '#e5eef6')
box(9.1,4.2,3.4,1.5,r'$F=bE(I-P)\alpha$'+'\n'+r'$d_{\rm out}K_Q=(b/\kappa)E^\perp P\alpha$', '#e6f2ed')
arrow((3.95,4.95),(4.55,4.95));arrow((8.4,4.95),(8.95,4.95))
box(.6,1.75,5.4,1.55,r'$\|\alpha\|_\mu^2\leq2\mu\mathcal{W}_\times$'+'\n'+r'$\|F\|_\mu^2\leq2b^2\mu\mathcal{W}_\times$'+'\nOriginal four-link derivatives; BQ8–BQ10', '#fff2da')
box(7,1.75,5.3,1.55,r'$\kappa\mathcal{O}_Q=-\langle\xi,F\rangle_\mu$'+'\n'+r'$\mathcal{O}_Q\leq(b/\kappa)\sqrt{2T_Q^\delta\mu\mathcal{W}_\times}$'+'\nEvery outside Hessian block retained; BQ11', '#fff2da')
arrow((10.8,4.1),(9.6,3.45));arrow((6.15,2.5),(6.85,2.5))
ax.text(6.5,.7,'The wholly inside derivative cancels exactly. The full ground state, scalar energy and every crossing face remain.\nP is not replaced by a local projection. Proofs: BQ1–BQ11; original lattice and metric in BQ1.',ha='center',fontsize=10)
fig.savefig(O/'BOUNDARY_PROJECTION_MAP.png',dpi=170,bbox_inches='tight');fig.savefig(O/'BOUNDARY_PROJECTION_MAP.svg',bbox_inches='tight');plt.close(fig)
js=np.unique(np.rint(np.logspace(1,9,180)).astype(np.int64))
fig,axs=plt.subplots(1,2,figsize=(12,5.3))
for kind,label,col in [('sqrt','Square-root collar','#316ca0'),('log','Logarithmic collar','#c37838')]:
    vals=[bounds(j,kind) for j in js]
    axs[0].loglog(js,[a**5*oo for a,K,la,oo,ff,mm in vals],label=label,color=col)
    axs[1].loglog(js,[a**10*mm for a,K,la,oo,ff,mm in vals],label=label,color=col)
for ax in axs:
    ax.set_xlabel(r'Original regulator $j$');ax.grid(alpha=.2);ax.legend(fontsize=9)
axs[0].set_ylabel(r'Upper bound for $a_j^5\mathcal{O}_{Q_j}$')
axs[1].set_ylabel(r'Upper bound for $a_j^{10}m_{1,j}$')
fig.suptitle('Actual-state estimates from the full original boundary counts',weight='bold')
fig.text(.5,.02,r'BQ12–BQ17; $R=\kappa_*=1$, $a_j=(100j)^{-1}$. All floors, ceilings and minimum branches retained.'+'\nCurves are proved upper functions, not measured ground-state values or spectral gaps.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.09,1,.93))
fig.savefig(O/'BOUNDARY_MOMENT_RATES.png',dpi=170,bbox_inches='tight');fig.savefig(O/'BOUNDARY_MOMENT_RATES.svg',bbox_inches='tight');plt.close(fig)
out=dict(description=__doc__,checks=len(rows),all_passed=True,results=rows)
(O/'BOUNDARY_FORCE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=len(rows),all_passed=True)))
