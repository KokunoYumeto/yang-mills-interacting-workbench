"""Reproducible RD and GS diagnostics. Manufactured densities are not Yang--Mills samples."""
from pathlib import Path
from fractions import Fraction as F
import itertools,json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
O=Path(__file__).resolve().parent
records=[]
def check(name,value,expected,tol=2e-11,**meta):
    v=float(value);e=float(expected)
    error=abs(v-e);passed=error<=tol*(1+abs(e))
    records.append(dict(name=name,value=v,expected=e,absolute_error=error,tolerance=tol,passed=passed,**meta))
    assert passed,(name,v,e,error)
def truth(name,ok,**meta):
    records.append(dict(name=name,passed=bool(ok),**meta));assert ok,(name,meta)

def haar(n):
    t=np.arange(1,n+1)*np.pi/(n+1)
    return np.cos(t),2*np.sin(t)**2/(n+1)

# Independent geometric enumeration: every elementary face and all original oriented edges.
def cube_edges(v,q):
    v=np.asarray(v)
    E=set()
    for z in itertools.product(range(q+1),repeat=3):
        z=np.asarray(z)
        for d in range(3):
            if z[d]<q:E.add((tuple((v+z).tolist()),d))
    return E
def faces(m):
    result={}
    for z in itertools.product(range(m+1),repeat=3):
        for d,k in itertools.combinations(range(3),2):
            if z[d]==m or z[k]==m:continue
            zd=list(z);zd[d]+=1;zk=list(z);zk[k]+=1
            result[(z,d,k)]={(z,d),(tuple(zd),k),(tuple(zk),d),(z,k)}
    return result
for m in [5,7,9]:
    all_faces=faces(m)
    for q in [1,2,3]:
        for v in [(0,0,0),(1,1,1),(m-q,m-q,m-q),(0,1,m-q)]:
            E=cube_edges(v,q);inc=[(p,len(edges&E)) for p,edges in all_faces.items()]
            inside={p for p,c in inc if c==4};cross={p for p,c in inc if 0<c<4}
            C=2*q*(q+1)*sum(int(v[d]>0)+int(v[d]+q<m) for d in range(3))
            truth('cube-counts',len(E)==3*q*(q+1)**2 and len(inside)==3*q*q*(q+1) and len(cross)==C,m=m,q=q,v=v)
            truth('crossing-face-single-inside-edge',all(c==1 for p,c in inc if 0<c<4),m=m,q=q,v=v)
for q,K in [(1,1),(1,2),(2,2),(3,3)]:
    m=q+2*K+2;v=(K+1,)*3;all_faces=faces(m);crossings=[];insides=[]
    for k in range(K+1):
        E=cube_edges(tuple(t-k for t in v),q+2*k)
        crossings.append({p for p,edges in all_faces.items() if 0<len(edges&E)<4})
        insides.append({p for p,edges in all_faces.items() if len(edges&E)==4})
    truth('nested-crossing-disjoint',all(crossings[k].isdisjoint(crossings[l]) for k in range(K) for l in range(k)),q=q,K=K)
    truth('crossing-contained-next-cube',all(crossings[k]<=insides[k+1] for k in range(K)),q=q,K=K)

# Curved product test SU(2)xSU(2), original radius-two metric.
# w=A*x+B*y+C*x*y, with all partition factors and marginal derivatives retained.
x,wx=haar(160);y,wy=haar(161)
x=x[:,None];y=y[None,:];nu=wx[:,None]*wy[None,:]
nx=(1-x*x)/4;ny=(1-y*y)/4;lx=-3*x/4
n1=-x/2;n2=-.5;l1=-.75
cases=[(A,B,C,k) for A,B,C in [(0,0,0),(.25,.25,1/32),(.7,-.4,.2),(-.8,.2,-.6),(.1,-.3,.9),(-.2,-.7,.5)] for k in [.4,1.,2.3]]
for A,B,C,kappa in cases:
    w=A*x+B*y+C*x*y;weight=nu*np.exp(2*w);Z=weight.sum();weight/=Z
    mu=lambda f:float(np.sum(weight*f))
    cy=wy[None,:]*np.exp(2*(B+C*x)*y);cy/=cy.sum(axis=1,keepdims=True)
    m1=np.sum(cy*y,axis=1,keepdims=True);center=y-m1
    v2=np.sum(cy*center**2,axis=1,keepdims=True)
    v3=np.sum(cy*center**3,axis=1,keepdims=True)
    v4=np.sum(cy*center**4,axis=1,keepdims=True)
    d1=A+C*m1;d2=2*C*C*v2;d3=4*C**3*v3;d4=8*C**4*(v4-3*v2*v2)
    Ay=A+C*y;Bx=B+C*x
    S=lx*Ay+2*nx*Ay**2;s=lx*d1+nx*d2+2*nx*d1**2;qnoise=S-s
    Fh=nx*Ay**2;Fb=nx*d1**2;tau=nx*C*C*v2;jnoise=Fh-Fb-tau
    hesscontract=-x/4*Ay**3*nx
    hbarcontract=(d2*nx-d1*x/4)*d1**2*nx
    J=C*C*nx*ny
    # Independent direct differentiation of V and the exact marginal U.
    Vp=kappa*(-.75*Ay-.75*y*C+n1*Ay**2+2*ny*Bx*C)
    Vpp=kappa*(n2*Ay**2+2*ny*C*C)
    Vip=kappa*(-.75*A+n1*A*A);Vipp=kappa*n2*A*A
    Up=kappa*(n1*d2+nx*d3+l1*d1+lx*d2+n1*d1*d1+2*nx*d1*d2)
    Upp=kappa*(n2*d2+2*n1*d3+nx*d4+2*l1*d2+lx*d3+n2*d1*d1+4*n1*d1*d2+2*nx*(d2*d2+d1*d3))
    direct=mu(nx*(Upp-Vipp)+lx*(Up-Vip))
    Btrace=mu(nx*(Vpp-Vipp)+lx*(Vp-Vip))
    context=dict(A=A,B=B,C=C,kappa=kappa,partition=Z)
    check('RD6-direct-retained-derivative',direct,Btrace-4*kappa*mu(hesscontract-hbarcontract)-2*kappa*mu(J)-2*kappa*mu(qnoise**2),**context)
    check('RD8-current-square',direct,Btrace+2*kappa*mu(tau*s)-2*kappa*mu(J)-2*kappa*mu((qnoise-jnoise/2)**2)+kappa/2*mu(jnoise**2),**context)
    VH=3*x*x*C*C*v2/16;G2=C**4*v2*v2*nx*nx;GH=(d2*nx-d1*x/4)*C*C*v2*nx;Td=C*C*v2*nx
    check('RD12-full-ordered-Hessian-trace',direct,Btrace-2*kappa*mu(J+VH-4*GH+4*G2+.5*Td),**context)
    for a in [.01,.08]:
        shift=2/(kappa*a);Nd=a**4*mu(Td)
        check('RD7-semiconvex-shift',direct,Btrace+8/a**5*Nd-4*kappa*mu(hesscontract+shift*Fh-hbarcontract-shift*Fb)-2*kappa*mu(J)-2*kappa*mu(qnoise**2),**context,a=a,tol=1e-10)
        check('RD13-two-positive-tensor-trace',direct,Btrace-2*kappa*mu(J+VH+4*G2+(8/(kappa*a)+.5)*Td-4*(GH+shift*Td)),**context,a=a,tol=1e-10)
    check('conditional-current-mean',np.max(np.abs(np.sum(cy*qnoise,axis=1))),0,**context)
    check('conditional-gradient-mean',np.max(np.abs(np.sum(cy*C*center,axis=1))),0,**context)
    check('Hessian-covariance-map',np.max(np.abs(d2-2*C*C*v2)),0,**context)
    check('full-gradient-norm-split',mu(Fh),mu(Fb+Td),**context)
    check('weighted-divergence-Hessian',mu(hesscontract),-.5*mu(Fh*S),**context)

# The eight-link gauge-invariant GS comparison reduces exactly to independent Haar holonomies.
A=B=F(1,4);C=F(1,32)
truth('GS5-exact-rational-negative-coefficient',C*C-2*C*(A-C)*(B-C)==-F(33,16384))
truth('GS6-exact-rational-negative-bound',F(33,16384)*F(9,256)==F(297,4194304))
cov_samples=[]
for n in [32,64,128,192]:
    X,vx=haar(n);Y,vy=haar(n+1);X=X[:,None];Y=Y[None,:]
    a,b,c=float(A),float(B),float(C)
    W0=a*X+b*Y+c*X*Y;rho=vx[:,None]*vy[None,:]*np.exp(2*W0);Z=rho.sum();rho/=Z
    av=lambda f:float(np.sum(rho*f))
    gx=(1-X*X)/4;gy=(1-Y*Y)/4
    Se=-.75*X*(a+c*Y)+2*gx*(a+c*Y)**2
    Sf=-.75*Y*(b+c*X)+2*gy*(b+c*X)**2
    current=av(Se*Sf);rhs=av(gx*gy*(c*c-2*c*(a+c*Y)*(b+c*X)))
    wilson=4*(av(X*Y)-av(X)*av(Y))
    lower=math.exp(-13/4)/64;upper=-297/4194304*math.exp(-17/8)
    check('GS4-mixed-current-identity',current,rhs,n=n)
    check('GS4-e-current-zero',av(Se),0,n=n);check('GS4-f-current-zero',av(Sf),0,n=n)
    truth('GS6-negative-absolute-bound',current<=upper,n=n,current=current,upper=upper)
    truth('GS9-positive-Wilson-bound',wilson>=lower,n=n,covariance=wilson,lower=lower)
    # A second exact manufactured state checks every derivative and partition ratio in GS12.
    aa,bb,cc=-.3,.45,-.07
    Wa=aa*X+bb*Y+cc*X*Y;Za=np.sum(vx[:,None]*vy[None,:]*np.exp(2*Wa))
    r=Wa-W0-.5*math.log(Za/Z);ratio=np.exp(2*r)
    rx=(aa-a)+(cc-c)*Y;ry=(bb-b)+(cc-c)*X
    Be=-.75*X*rx+4*gx*(a+c*Y)*rx+2*gx*rx**2
    Bf=-.75*Y*ry+4*gy*(b+c*X)*ry+2*gy*ry**2
    Sae=-.75*X*(aa+cc*Y)+2*gx*(aa+cc*Y)**2
    Saf=-.75*Y*(bb+cc*X)+2*gy*(bb+cc*X)**2
    check('GS12-full-density-ratio',av(ratio),1,n=n)
    check('GS12-e-current-defect',np.max(np.abs(Sae-Se-Be)),0,n=n)
    check('GS12-f-current-defect',np.max(np.abs(Saf-Sf-Bf)),0,n=n)
    check('GS12-covariance-defect',av(ratio*Sae*Saf),av(ratio*(Se+Be)*(Sf+Bf)),n=n)
    potential=lambda u,v,t:-3*u*X-3*v*Y-6*t*X*Y+(u+t*Y)**2*(1-X*X)+(v+t*X)**2*(1-Y*Y)
    defect=-3*(aa-a)*X-3*(bb-b)*Y-6*(cc-c)*X*Y+2*((a+c*Y)*rx*(1-X*X)+(b+c*X)*ry*(1-Y*Y))+rx**2*(1-X*X)+ry**2*(1-Y*Y)
    check('GS12-complete-potential-defect',np.max(np.abs(potential(aa,bb,cc)-potential(a,b,c)-defect)),0,n=n)
    Ftest=1+.2*X-.13*Y+.08*X*Y
    check('GS11-unitary-state-map',av(ratio*np.exp(-2*r)*Ftest**2),av(Ftest**2),n=n)
    cov_samples.append(dict(n=n,Z=Z,current=current,wilson=wilson))
check('GS-quadrature-refinement-current',cov_samples[-1]['current'],cov_samples[-2]['current'],tol=1e-12)
check('GS-quadrature-refinement-Wilson',cov_samples[-1]['wilson'],cov_samples[-2]['wilson'],tol=1e-12)
def collar_bounds(j,kind,R=1.,kappa=1.):
    a=1/(100*j);q=math.ceil(R/a)+3;ell=math.log(math.e+R/a)
    K=max(1,math.floor(math.sqrt(R/a) if kind=='sqrt' else R/(a*ell)))
    Q=q+2*K;N=3*Q*(Q+1)**2;M=3*Q*Q*(Q+1);C=12*Q*(Q+1)
    Lam=min(2*M,3*kappa*a*math.sqrt(N*M))+2*C
    potential=a*a*Lam/(kappa*K)
    trace=9/kappa*(a*a*Q*(Q+1)-R*R)+3*a*a*Lam/(8*kappa*K)
    return dict(a=a,q=q,K=K,Lambda=Lam,ell=ell,potential=potential,trace=trace)
for j in [5,10,100,1000]:
    for kind in ['sqrt','log']:
        d=collar_bounds(j,kind)
        a=d['a'];q=d['q'];K=d['K']
        truth('RD20-collar-fits-original-lattice',j**4-1-K>0 and j**4-1+q+K<2*j**4,j=j,kind=kind)
        for k in [0,K//2,K-1]:
            C=12*(q+2*k)*(q+2*k+1)
            for fraction in [0,.37,1]:
                deficit=fraction*d['Lambda']/K
                trace=3*a*a/8*(2*C-deficit)
                truth('RD20-full-scalar-and-deficit-bound',abs(trace-9)<=d['trace']+1e-10,j=j,kind=kind,k=k,deficit_fraction=fraction)
for R in [.4,1.,2.3]:
    d=collar_bounds(100_000_000,'log',R=R,kappa=.7)
    check('RD21-log-collar-floor-limit',d['a']*d['K']*d['ell'],R,tol=1e-7,R=R)
    d=collar_bounds(100_000_000,'sqrt',R=R,kappa=.7)
    L=9*.7*R**3+24*R**2
    check('RD22-full-trace-bound-coefficient',d['trace']/math.sqrt(d['a']),36*R**1.5/.7+3*L/(8*.7*math.sqrt(R)),tol=3e-4,R=R)
out=dict(description='Geometric enumeration, curved manufactured density identities, and exact GS comparison diagnostics; no actual Yang--Mills ground-state samples.',checks=len(records),all_passed=all(r['passed'] for r in records),records=records,comparison=cov_samples[-1])
(O/'RETAINED_DERIVATIVE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')

# Reproducible mechanism figures, with full constants and proof locators.
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':13})
fig,axs=plt.subplots(1,2,figsize=(12.5,6.0),gridspec_kw={'width_ratios':[1,1.18]})
ax=axs[0];ax.set_aspect('equal');ax.set_xlim(-2.5,6.8);ax.set_ylim(-3.0,6.5);ax.axis('off')
for k,color in [(2,'#aab8ce'),(1,'#6784ad'),(0,'#183f68')]:
    ax.add_patch(Rectangle((-k,-k),4+2*k,4+2*k,fill=False,lw=2,ec=color))
ax.add_patch(Rectangle((3,1),1,1,fc='#cbd9e9',ec='#183f68',lw=2))
ax.add_patch(Rectangle((4,1),1,1,fc='#f8d78b',ec='#9a6400',lw=2))
ax.plot([4,4],[1,2],color='#c74425',lw=5)
ax.annotate('one inside edge',xy=(4,1.5),xytext=(1.0,-1.6),arrowprops={'arrowstyle':'->','color':'#c74425'},color='#9a321c')
ax.text(-.0,4.35,r'$Q_{j,0}$',color='#183f68');ax.text(-.8,5.3,r'$Q_{j,1}$',color='#6784ad')
ax.set_title('A coordinate section of the nested cubes\nRD9–RD16; the actual cubes are three-dimensional')
ax.text(-2.3,-2.8,'A crossing face is inside the next enlarged cube.',fontsize=9.8)
ax=axs[1];ax.axis('off')
rows=[
 ('Exact original trace (unit edge magnitudes)',r'$\mathcal{B}_{\mathbf{1},j}=\frac{3b_j}{4}(2C_{Q_j^*}-\mu_j\mathcal{W}_\times)$'),
 ('Good boundary selection; actual ground measure',r'$\mu_j\mathcal{W}_\times(Q_j^*)\leq\Lambda_{j,K_j}/K_j$'),
 ('Scaled crossing potential tends to zero',r'$a_j^4b_j\mu_j\mathcal{W}_\times(Q_j^*)\longrightarrow0$'),
 ('The scalar 2 survives in the full trace',r'$\frac{a_j^4}{2}\mathcal{B}_{\mathbf{1},j}\longrightarrow9R^2/\kappa_*$'),
 ('Original supported weights: exact zero',r'$h=\mathrm{sgn}(t)\ \mathrm{or}\ h=t:\quad\mathcal{B}_h=0$')]
for i,(title,formula) in enumerate(rows):
    yy=.92-i*.195
    ax.text(0,yy,title,weight='bold',color='#183f68',transform=ax.transAxes,fontsize=11)
    ax.text(0,yy-.075,formula,transform=ax.transAxes,fontsize=15 if i<4 else 12.8)
fig.subplots_adjust(left=.045,right=.98,top=.86,bottom=.16,wspace=.12)
fig.suptitle('A small crossing potential does not erase its differentiated scalar term',fontsize=16,weight='bold',y=.97)
fig.text(.5,.045,'RD10 and RD16–RD19. The remaining Hessian and conditional-current terms retain their full values.\nGeometric section and exact proved limits; no numerical ground-state sample.',ha='center',fontsize=10)
for ext in ['png','svg']:fig.savefig(O/f'RETAINED_BOUNDARY_MAP.{ext}',dpi=175)
plt.close(fig)

fig=plt.figure(figsize=(12.0,6.3));ax=fig.add_axes([.07,.21,.39,.58])
vals=[cov_samples[-1]['wilson'],cov_samples[-1]['current']]
colors=['#207e79','#bb4a35']
ax.bar([0,1],vals,color=colors,width=.58)
ax.axhline(0,color='#2a3442',lw=1)
ax.set_ylim(-.002,.016)
ax.set_xticks([0,1],['Wilson traces','Distinct-edge currents'])
ax.set_ylabel('Covariance in the specified comparison density')
ax.set_title('Opposite signs in one gauge-invariant state')
for i,v in enumerate(vals):
    ax.annotate(f'{v:.8f}',(i,v),xytext=(0,7 if v>0 else -18),textcoords='offset points',ha='center',fontsize=11)
ax.ticklabel_format(axis='y',style='sci',scilimits=(0,0));ax.spines[['top','right']].set_visible(False)
axt=fig.add_axes([.52,.19,.45,.62]);axt.axis('off')
lines=[
 r'$\alpha_0=\beta_0=1/4,\quad\gamma_0=1/32$',
 r'$w_0=\alpha_0x+\beta_0y+\gamma_0xy$',
 r'$d\mu_{\mathrm{c}}=Z^{-1}e^{2w_0}\,dU$',
 'Exact proof bounds (GS6, GS9):',
 r'$\mathrm{Cov}_{\mu_{\mathrm{c}}}(\mathrm{Tr}\,U_p,\mathrm{Tr}\,U_q)$',
 r'$\qquad\geq e^{-13/4}/64>0$',
 r'$\mu_{\mathrm{c}}S_eS_f\leq-297e^{-17/8}/4194304<0$',
 'Exact state map to the programme (GS11–GS12):',
 r'$T_jF=e^{-(w_j-w_{\mathrm{c}})}F$',
 r'$T_j^{-1}\mathscr{L}_jT_j=\mathscr{L}_{\mathrm{c}}+V_j-V_{\mathrm{c}}-E_{0,j}$'
]
for i,t in enumerate(lines):
    axt.text(0,.98-i*.105,t,transform=axt.transAxes,fontsize=11.5 if i in [3,7,9] else 13)
fig.suptitle('Wilson covariance alone does not determine a ground-current sign',fontsize=16,weight='bold',y=.96)
fig.text(.5,.068,'GS1–GS12. The comparison density is constructed explicitly; it is not the original Yang–Mills ground.\nBars use reproducible Haar quadrature; the strict signs and displayed bounds have complete analytic proofs.',ha='center',fontsize=10.5)
for ext in ['png','svg']:fig.savefig(O/f'CURRENT_SIGN_COMPARISON.{ext}',dpi=175)
plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(12.0,5.4))
js=np.unique(np.geomspace(5,100000,220).astype(int))
for kind,color,label in [('sqrt','#183f68','Square-root collar (RD14)'),('log','#bf6330','Logarithmic collar (RD21)')]:
    ds=[collar_bounds(int(j),kind) for j in js]
    axs[0].loglog(js,[d['potential'] for d in ds],color=color,lw=2,label=label)
    axs[1].loglog(js,[d['trace'] for d in ds],color=color,lw=2,label=label)
axs[0].set_title('Upper bound for the scaled crossing potential')
axs[0].set_ylabel(r'$a_j^2\Lambda_{j,K}/(\kappa_*K)$')
axs[1].set_title('Upper bound for the full crossing-trace error')
axs[1].set_ylabel(r'RD20 bound on $|(a_j^4/2)\mathcal{B}_{\mathbf{1},j}-9R^2/\kappa_*|$')
for ax in axs:
    ax.set_xlabel(r'Original regulator $j$');ax.grid(alpha=.2);ax.legend(fontsize=9)
fig.suptitle('Both collar choices retain the complete boundary contribution',fontsize=15,weight='bold',y=.97)
fig.subplots_adjust(left=.08,right=.98,top=.84,bottom=.21,wspace=.27)
fig.text(.5,.045,r'RD20–RD22; $R=\kappa_*=1$, $a_j=(100j)^{-1}$, with the exact floor, ceiling, minimum and counts.'+'\nCurves evaluate proved upper functions, not measured crossing energies or quantum samples.',ha='center',fontsize=10)
for ext in ['png','svg']:fig.savefig(O/f'COLLAR_RATE_MAP.{ext}',dpi=175)
plt.close(fig)
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
