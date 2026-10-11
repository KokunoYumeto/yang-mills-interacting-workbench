"""Reproducible bounded algebra checks and exact-bound scientific illustration.

Random SU(2) configurations check original oriented Hessian identities, not
ground-state sampling. The figure plots proved receiving bounds, not a density.
"""
from pathlib import Path
import json, math, re
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parent
rng=np.random.default_rng(202610113)
checks=[]
def record(name,error,tolerance=1e-10):
    error=float(abs(error))
    assert error<=tolerance,(name,error,tolerance)
    checks.append(dict(name=name,error=error,tolerance=tolerance))

y,e,F,alpha,A1,gamma,n=sp.symbols('y e F alpha A1 gamma n',positive=True)
phi=y/(e+y)
record("original phi derivative",0 if sp.simplify(sp.diff(phi,y)-e/(e+y)**2)==0 else 1)
record("original phi second derivative",0 if sp.simplify(sp.diff(phi,y,2)+2*e/(e+y)**3)==0 else 1)
u=sp.symbols('u',nonnegative=True)
record("gradient maximum derivative",0 if sp.simplify(sp.diff(u/(1+u)**4,u)-(1-3*u)/(1+u)**5)==0 else 1)
record("gradient maximum value",float((u/(1+u)**4).subs(u,sp.Rational(1,3))-sp.Rational(27,256)))
record("Hessian composition maximum",float((u/(1+u)**3).subs(u,sp.Rational(1,2))-sp.Rational(4,27)))
J=6*A1-3*y
lap=sp.diff((e+y)**(-n),y,2)*gamma+sp.diff((e+y)**(-n),y)*J
rew=n*(n+1)*gamma*(e+y)**(-n-2)-n*(6*A1+3*e)*(e+y)**(-n-1)+3*n*(e+y)**(-n)
record("shifted inverse full Laplacian",0 if sp.simplify(lap-rew)==0 else 1)
rminus,rplus=sp.symbols('rminus rplus',positive=True)
width=rplus/(rminus+2*rplus)-rminus/(2*rminus+rplus)
record("root width identity",0 if sp.simplify(width-(rminus+rplus)*(rplus-rminus)/(2*(rminus+rplus)**2+rminus*rplus))==0 else 1)
xx,ret=sp.symbols('xx ret')
record("retained bounded residual",0 if sp.simplify(2*xx/(1+xx)-1+ret/(1+xx)-(xx+ret-1)/(1+xx))==0 else 1)
sym_count=len(checks)

# Original radius-two generator matrices and full open cubic face orientations.
I=np.eye(2,dtype=complex)
sigma=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)]
T=[-0.5j*s for s in sigma]
def su2():
    q=rng.normal(size=4);q/=np.linalg.norm(q)
    return q[0]*I-1j*sum(q[k+1]*sigma[k] for k in range(3))
def cube(q):
    edges=[]
    for z in np.ndindex(*(q+1,)*3):
        for d in range(3):
            if z[d]<q: edges.append((z,d))
    eid={v:i for i,v in enumerate(edges)}
    faces=[]
    for z in np.ndindex(*(q+1,)*3):
        for d in range(3):
            for f in range(d+1,3):
                if z[d]>=q or z[f]>=q:continue
                zd=list(z);zd[d]+=1
                zf=list(z);zf[f]+=1
                faces.append([(eid[(z,d)],1),(eid[(tuple(zd),f)],1),(eid[(tuple(zf),d)],-1),(eid[(z,f)],-1)])
    return edges,faces
def prod(mats):
    ans=I.copy()
    for m in mats:ans=ans@m
    return ans
for q in [1,2]:
    edges,faces=cube(q)
    pairseen=set()
    for face in faces:
        ids=[p[0] for p in face]
        for i in range(4):
            for j in range(i+1,4):
                pair=tuple(sorted([ids[i],ids[j]]))
                assert pair not in pairseen
                pairseen.add(pair)
    record(f"open cube {q} pair uniqueness",0)
    for sample in range(12):
        U=[su2() for _ in edges]
        weights=rng.uniform(0,2,len(faces))
        Hess=np.zeros((3*len(edges),3*len(edges)))
        W=[]
        for p,face in enumerate(faces):
            factors=[U[idx] if sign==1 else U[idx].conj().T for idx,sign in face]
            wp=np.trace(prod(factors)).real;W.append(wp)
            for i,(idx,sign) in enumerate(face):
                Hess[3*idx:3*idx+3,3*idx:3*idx+3]+=weights[p]*wp*0.25*np.eye(3)
                for j,(jdx,sj) in enumerate(face):
                    if i==j:continue
                    block=np.zeros((3,3))
                    for a in range(3):
                        for b in range(3):
                            fs=list(factors)
                            fs[i]=T[a]@U[idx] if sign==1 else -U[idx].conj().T@T[a]
                            fs[j]=T[b]@U[jdx] if sj==1 else -U[jdx].conj().T@T[b]
                            block[a,b]=-np.trace(prod(fs)).real
                    record(f"q{q} sample{sample} p{p} ordered block{i}{j}",np.sum(block**2)-(0.5+wp**2/16),2e-13)
                    Hess[3*idx:3*idx+3,3*jdx:3*jdx+3]+=weights[p]*block
        diagonal=0.0
        for k in range(len(edges)):
            s=sum(weights[p]*W[p] for p,face in enumerate(faces) if any(idx==k for idx,_ in face))
            diagonal+=3*s*s/16
        expected=diagonal+sum(weights[p]**2*(6+3*W[p]**2/4) for p in range(len(faces)))
        record(f"q{q} sample{sample} full Hessian identity",np.sum(Hess**2)-expected,1e-10)
        record(f"q{q} sample{sample} symmetry",np.max(np.abs(Hess-Hess.T)),1e-12)
        record(f"q{q} sample{sample} 21 bound",max(0,np.sum(Hess**2)-21*np.sum(weights**2)),1e-10)
geom_count=len(checks)-sym_count

# Positive finite laws check exact pair covariances, not the Yang-Mills vacuum.
for k in range(500):
    ee=10**rng.uniform(-2,3); yy=ee*rng.uniform(0,5,9)
    pp=rng.random(9);pp/=sum(pp)
    bb=yy/(ee+yy)
    mean=pp@bb;d=pp@yy
    G=pp@(bb-mean)**2
    R1=pp@(ee+yy)**-1;R2=pp@(ee+yy)**-2
    pair=(yy[:,None]-yy[None,:])**2
    den=(ee+yy[:,None])*(ee+yy[None,:])
    record(f"law{k} exact Gram",G-ee**2*(R2-R1**2),2e-13)
    record(f"law{k} pair Gram",G-ee**2/2*np.sum(pp[:,None]*pp[None,:]*pair/den**2),2e-13)
    cov=pp@((bb-mean)*(yy-d))
    record(f"law{k} pair covariance",cov-ee/2*np.sum(pp[:,None]*pp[None,:]*pair/den),2e-10)
    record(f"law{k} covariance lower",max(0,ee*G-cov),1e-10)
    xx=yy/ee;aa=rng.random(9)*3;res=xx+aa-1;clipped=np.minimum(xx,1)
    record(f"law{k} retained clipping",max(0,np.max((aa-1+clipped)**2-res**2)),1e-12)
law_count=len(checks)-sym_count-geom_count

for k in range(400):
    kappa=10**rng.uniform(-1,1); ff=10**rng.uniform(-1,1); j1=10**rng.uniform(-2,1)
    emin=4.5*kappa*j1;E=emin*(1+rng.uniform(0,30))
    C0=81*kappa*kappa*j1*j1/16
    disc=math.sqrt(max(0,E*E-4*C0))
    rm=(2*C0)/(E+disc);rp=(E+disc)/2
    bm=rm/(E+rm);bp=rp/(E+rp)
    record(f"limit{k} width",bp-bm-E*disc/(2*E*E+C0),1e-13)
    uv=rng.uniform(bm,bp,11);p=rng.random(11);p/=sum(p)
    X=uv/(1-uv);g=p@(uv-p@uv)**2
    cov=p@((uv-p@uv)*(X-p@X))
    record(f"limit{k} lower signed magnitude",max(0,(1+rm/E)**2*g-cov),1e-12)
    record(f"limit{k} upper signed magnitude",max(0,cov-(1+rp/E)**2*g),1e-12)
limit_count=len(checks)-sym_count-geom_count-law_count

# Finite compression defect, independent from any claim of cyclic visibility.
for k in range(70):
    n0=7;r=3
    Q,_=np.linalg.qr(rng.normal(size=(n0,n0)))
    R=Q[:,:r]@Q[:,:r].T
    B=np.diag(rng.uniform(0,1,n0));eye=np.eye(n0)
    K=(eye-R)@B@R
    defect=R@B@B@R-R@B@R@B@R
    record(f"compression{k}",np.max(np.abs(defect-K.T@K)),1e-12)
compression_count=len(checks)-sym_count-geom_count-law_count-limit_count

# Figure uses an explicit admissible compact continuous spatial test:
# f(x)=prod_l (1-2|x_l|)_+, with kappa*=1, R=1, F=1,
# J1=1/8 and J2=1/27. E is an actual energy-coordinate argument of a proved bound.
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"axes.titlesize":12})
fig=plt.figure(figsize=(13.5,8.8),layout="constrained")
gs=fig.add_gridspec(2,2,height_ratios=[1.1,1])
ax=fig.add_subplot(gs[0,0]); ax2=fig.add_subplot(gs[0,1]);ax3=fig.add_subplot(gs[1,:]);ax3.axis('off')
kappa=F0=R0=1.0;j1=1/8;Emin=9/16;Emax=33
E=np.linspace(Emin,3,900);C0=81*j1*j1/16
dd=np.sqrt(np.maximum(0,E*E-4*C0));rp=(E+dd)/2;rm=2*C0/(E+dd)
blo=rm/(E+rm);bhi=rp/(E+rp)
ax.fill_between(E,blo,bhi,color="#4682B4",alpha=.25,label="Proved support interval")
ax.plot(E,blo,color="#174c75");ax.plot(E,bhi,color="#174c75")
ax.scatter([Emin],[1/3],color="#af473c",zorder=5)
ax.annotate(r"$E=9/16:\ b_Y\to1/3$",xy=(Emin,1/3),xytext=(1.1,.31),arrowprops=dict(arrowstyle="->",color="#af473c"),color="#963d33")
ax.set(xlabel=r"Actual energy coordinate $E=\lim_{\mathcal U}a_j^2e_j$",ylabel=r"Possible spectral values of $B$",ylim=(0,.52),xlim=(Emin,3),title="BM58–BM59 · Actual two-root support")
ax.text(.02,.03,r"Shown: $9/16\le E\le3$; allowed ceiling $E_{\max}=33$.",transform=ax.transAxes,fontsize=9)
ax.grid(alpha=.2)
rho_m=rm/E;rho_p=rp/E
ax2.fill_between(E,-(1+rho_p)**2,-(1+rho_m)**2,color="#d89845",alpha=.28)
ax2.plot(E,-(1+rho_p)**2,color="#8d5915");ax2.plot(E,-(1+rho_m)**2,color="#8d5915")
ax2.set(xlabel=r"Actual energy coordinate $E$",ylabel=r"Coefficient multiplying the actual Gram $g$",xlim=(Emin,3),ylim=(-4.05,-.95),title="BM64 · Signed retained-covariance interval")
ax2.text(.05,.07,r"$-(1+\rho_+)^2g\ \le\ \lim_{\mathcal U}\mathrm{Cov}(b_Y,\mathcal A/e)$"+"\n"+r"$\le\ -(1+\rho_-)^2g,\qquad g=\lim_{\mathcal U}\mathrm{Var}(b_Y)$",transform=ax2.transAxes,fontsize=10,bbox=dict(facecolor="white",edgecolor="none",alpha=.8))
ax2.grid(alpha=.2)
boxes=[
(.02,.46,.28,.35,"Original source-zero vacuum",r"$b_Y=Y/(e+Y)$; $e=F(E_0-E_{\rm out})/b$"+"\n"+r"$E_b=\Theta(a^2)$, $E_{2,b}=O(a)$"+"\n"+r"$G_b=\mathrm{Var}_{\mu}(b_Y)$ remains actual"),
(.36,.46,.28,.35,"Original shrinking window",r"$s_j=\kappa_*/j$; upper mass $O(a_j)$"+"\n"+r"$z=[(b_Y-\mu b_Y)\psi]=\mathcal Lz$"+"\n"+r"$z\in\ker A$, $\|z\|^2=g$"),
(.70,.46,.28,.35,"Original cyclic visibility",r"$g=\|Rz\|^2+\|(I-R)z\|^2$"+"\n"+r"$\|Rz\|^2=\sup d^*H^+d$"+"\n"+r"Both terms retained (BM37–BM38)")
]
from matplotlib.patches import FancyBboxPatch
for x0,y0,ww,hh,title,body in boxes:
    ax3.add_patch(FancyBboxPatch((x0,y0),ww,hh,boxstyle="round,pad=.012",facecolor="#f0f4f7",edgecolor="#6b8295",transform=ax3.transAxes))
    ax3.text(x0+ww/2,y0+hh-.045,title,ha="center",va="top",weight="bold",transform=ax3.transAxes,fontsize=11)
    ax3.text(x0+ww/2,y0+hh-.13,body,ha="center",va="top",transform=ax3.transAxes,fontsize=10,linespacing=1.65)
for x0,x1 in [(.304,.354),(.644,.694)]:
    ax3.annotate("",xy=(x1,.66),xytext=(x0,.66),xycoords="axes fraction",arrowprops=dict(arrowstyle="->",lw=1.8,color="#516474"))
ax3.text(.5,.34,r"BM65: $[(Y/e)\mathcal W_j\psi_j]=X\mathcal W\Omega$,  $[(\mathcal A/e)\mathcal W_j\psi_j]=(I-X)\mathcal W\Omega$"+"\n"+r"$X=B(I-B)^{-1}$ on the augmented cyclic space; residual norm $O(a^{3/2})$.",ha="center",va="center",transform=ax3.transAxes,fontsize=12,linespacing=1.9)
ax3.text(.5,.11,r"Bound illustration: $\kappa_*=1$, $f(x)=\prod_{\ell=1}^3(1-2|x_\ell|)_+$, $F=R=1$, $J_1=1/8$, $J_2=1/27$."+"\n"+"The shaded intervals are proved bounds, not sampled ground-state distributions. No positive value of g is assumed.",ha="center",va="center",transform=ax3.transAxes,fontsize=9.5,linespacing=1.65)
fig.suptitle("The bounded actual-energy multiplier and its retained covariance",fontsize=16,weight="bold")
for textobj in fig.findobj(matplotlib.text.Text):
    s=textobj.get_text()
    s=re.sub(r'\\mathcal\s+([A-Za-z])',r'\\mathcal{\1}',s)
    s=re.sub(r'\\le(?![A-Za-z])',r'\\leq',s)
    textobj.set_text(s)
fig.savefig(root/'bounded_energy_multiplier.png',dpi=170)
fig.savefig(root/'bounded_energy_multiplier.svg')
plt.close(fig)

md=(root/'BOUNDED_ENERGY_MULTIPLIER.md').read_text(encoding='utf-8')
assert re.findall(r'\\tag\{BM(\d+)\}',md)==[str(i) for i in range(1,70)]
raw=(root/'BOUNDED_ENERGY_MULTIPLIER.md').read_bytes()
assert re.search(rb'\r(?!\n)',raw) is None
assert all(b>=32 or b in (9,10,13) for b in raw)
assert not re.search(r'\bplain\b',md,flags=re.I)
result={'status':'passed','seed':202610113,'symbolic_checks':sym_count,'oriented_su2_hessian_checks':geom_count,'finite_positive_law_identity_checks':law_count,'root_covariance_checks':limit_count,'compression_checks':compression_count,'check_count':len(checks),'max_error':max(c['error'] for c in checks),'checks':checks,'scope':'Original oriented SU(2) Hessian identities, exact algebra and bound checks. No simulated Yang-Mills vacuum or numerical continuum-law claim.','figure':'Exact proved support/covariance bounds and receiving diagram; explicit admissible compact test.'}
(root/'BOUNDED_ENERGY_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
