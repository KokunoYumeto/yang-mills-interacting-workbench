from pathlib import Path
import json,itertools,math
import numpy as np
import sympy as sp
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
O=Path(__file__).resolve().parent
rng=np.random.default_rng(61012009);checks=[]
def eq(name,a,b,tol=2e-10):
    error=float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    scale=max(1,float(np.max(np.abs(a))),float(np.max(np.abs(b))))
    assert error<=tol*scale,(name,error,scale)
    checks.append(dict(name=name,passed=True,error=error))
def M(v):
    x,y,z=v
    return np.array([[1j*x,y+1j*z],[-y+1j*z,-1j*x]])
def U(v,g):
    q=g*g*np.dot(v,v)/8
    return ((1-q)*np.eye(2)+g/math.sqrt(2)*M(v))/(1+q)
def coefficients(b):
    r=np.sum(b*b,axis=1)/8
    dot=lambda i,j:np.dot(b[i],b[j])
    triple=lambda i,j,k:np.dot(b[i],np.cross(b[j],b[k]))
    K=dot(0,1)*dot(2,3)-dot(0,2)*dot(1,3)+dot(0,3)*dot(1,2)
    A=[.5*np.dot(b.sum(axis=0),b.sum(axis=0)),
       sum(triple(*ijk) for ijk in itertools.combinations(range(4),3))/math.sqrt(2),
       -K/2,0.,4*np.prod(r)*sum(1/x for x in r) if np.all(r) else 4*sum(np.prod(r[list(ijk)]) for ijk in itertools.combinations(range(4),3))]
    for i,j in itertools.combinations(range(4),2):
        k,l=sorted(set(range(4))-{i,j})
        A[2]-=dot(i,j)*(r[k]+r[l]);A[4]+=dot(i,j)*r[k]*r[l]
    for i,j,k in itertools.combinations(range(4),3):
        l=next(iter(set(range(4))-{i,j,k}))
        A[3]-=triple(i,j,k)*r[l]/math.sqrt(2)
    return np.array(A),r
for n in range(120):
    b=rng.normal(size=(4,3))*10**rng.uniform(-1,1)
    g=10**rng.uniform(-2,1);A,r=coefficients(b)
    product=np.eye(2,dtype=complex)
    for v in b:product=product@U(v,g)
    D=2-np.trace(product).real
    exact=sum(g**k*A[k] for k in range(5))/np.prod(1+g*g*r)
    eq(f'ordered full rational face {n}',D/g**2,exact,1e-8)
    eq(f'quaternion sign {n}',M(b[0])@M(b[1]),-np.dot(b[0],b[1])*np.eye(2)+M(np.cross(b[0],b[1])))
    eq(f'unitarity {n}',U(b[0],g).conj().T@U(b[0],g),np.eye(2))
    w=U(b[0],g);x=np.trace(w).real/2
    y=np.array([w[0,0].imag,w[0,1].real,w[0,1].imag])
    eq(f'inverse coordinate {n}',2*math.sqrt(2)/g*y/(1+x),b[0])
# Exact symbolic Casimir and pullback metric, independent of the face tests.
x,y,z,g=sp.symbols('x y z g',positive=True,real=True)
v=sp.Matrix([x,y,z]);q=g*g*(v.dot(v))/8
coord=sp.Matrix([(1-q)/(1+q),*[g*t/sp.sqrt(2)/(1+q) for t in v]])
J=coord.jacobian(v)
metric=4*J.T*J
for i in range(3):
    for j in range(3):
        assert sp.factor(metric[i,j]-(2*g*g/(1+q)**2 if i==j else 0))==0
        checks.append(dict(name=f'exact radius-two metric {i},{j}',passed=True))
f=2*(1-q)/(1+q)
lap=(1+q)**2/(2*g*g)*sum(sp.diff(f,t,2) for t in v)-(1+q)/8*sum(t*sp.diff(f,t) for t in v)
assert sp.factor(lap+sp.Rational(3,4)*f)==0
checks.append(dict(name='exact fundamental trace Casimir',passed=True))
b=np.array([[1.,0,0],[0,1.,0],[0,0,0],[0,0,-1.]])
for gg in [.01,.1,.5,1,3]:
    A,r=coefficients(b)
    lhs=sum(gg**k*A[k] for k in range(5))/np.prod(1+gg*gg*r)
    rhs=(1.5-gg/math.sqrt(2)+gg**4/128)/(1+gg*gg/8)**3
    eq(f'cubic example {gg}',lhs,rhs)
# Entire periodic lattices: count every face and preserve the three-link placement.
for dimension in [2,3,4]:
    n=5;origin=(1,)*dimension
    move=lambda pos,d:tuple((pos[k]+(k==d))%n for k in range(dimension))
    active={(origin,0):np.array([1.,0,0]),(move(origin,0),1):np.array([0,1.,0]),(origin,1):np.array([0,0,1.])}
    for gg in [.07,.31]:
        totals=[]
        for sign in [1,-1]:
            total=0.;multi=0
            for pos in itertools.product(range(n),repeat=dimension):
                for d,k in itertools.combinations(range(dimension),2):
                    edges=[(pos,d),(move(pos,d),k),(move(pos,k),d),(pos,k)]
                    multi+=sum(e in active for e in edges)>1
                    matrices=[U(sign*active.get(e,np.zeros(3)),gg) for e in edges]
                    total+=2-np.trace(matrices[0]@matrices[1]@matrices[2].conj().T@matrices[3].conj().T).real
            assert multi==1;totals.append(total)
        eq(f'complete periodic density ratio dimension {dimension} coupling {gg}',-(totals[0]-totals[1])/gg**2,math.sqrt(2)*gg/(1+gg**2/8)**3)
mp.mp.dps=60
for gg in [mp.mpf('.2'),mp.mpf('1'),mp.mpf('3')]:
    for power in [0,1,2]:
        density=lambda r:4*mp.pi*r*r*gg**3/(4*mp.sqrt(2)*mp.pi**2)*(1+gg*gg*r*r/8)**-3
        value=mp.quad(lambda r:r**power*density(r),[0,mp.sqrt(8)/gg,mp.inf])
        exact=(mp.sqrt(8)/gg)**power*mp.beta((power+3)/2,(3-power)/2)/mp.beta(mp.mpf('1.5'),mp.mpf('1.5'))
        assert abs(value-exact)<=mp.mpf('1e-50')*max(abs(value),abs(exact))
        checks.append(dict(name=f'full Haar moment g={gg}, p={power}',passed=True))
# Stronger projection coefficient and direct singular-value cutoff.
for n in range(30):
    C=rng.normal(size=(20,6));Q=np.linalg.qr(rng.normal(size=(20,20)))[0]
    z=10**rng.uniform(-2,1);D=Q@np.diag(np.geomspace(.01,20,20)+z)@Q.T
    A=D@C;gamma=np.linalg.svd(A,compute_uv=False)[-1]**2
    noise=rng.normal(size=A.shape);noise*=.1*math.sqrt(gamma)/np.linalg.norm(noise)
    Ac=A+noise;v=rng.normal(size=20);c=np.linalg.lstsq(Ac,v,rcond=None)[0]
    qr=np.dot(Ac@c,Ac@c);r0=v-Ac@c
    eq(f'projection Pythagoras {n}',qr+np.dot(r0,r0),np.dot(v,v))
    assert np.linalg.norm(c)<=math.sqrt(2*qr/gamma)*(1+1e-10)
    assert np.linalg.svd(Ac,compute_uv=False)[-1]**2>=gamma/2
    checks.extend([dict(name=f'sharper coefficient {n}',passed=True),dict(name=f'direct singular-value threshold {n}',passed=True)])
out=dict(checks=len(checks),all_passed=True,scope='Exact symbolic radius-two metric and Casimir; full rational SU(2) face multiplication; complete periodic 2D/3D/4D density-ratio counterexample; probability-Haar moment integrals; least-squares projection and singular-value bounds. No numerical evaluation of the original interacting residual.',results=checks)
(O/'STEREOGRAPHIC_CURRENT_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
# Figures plot specified exact expressions, not inferred vacuum spectra.
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
fig,axes=plt.subplots(1,2,figsize=(12,4.8),layout='constrained')
gg=np.linspace(.002,1.5,500)
axes[0].plot(gg,np.sqrt(2)*gg/(1+gg**2/8)**3,color='#006e82',lw=2.5,label='Exact log density ratio (SC15)')
axes[0].plot(gg,np.sqrt(2)*gg,'--',color='#b45631',label=r'Linear term $\sqrt{2}g$')
axes[0].set(xlabel='Original coupling g',ylabel=r'$\log[p(B)/p(-B)]$',title='Ordered cubic term survives the full face sum')
axes[0].legend(fontsize=9);axes[0].grid(alpha=.2)
radius=np.geomspace(.05,1e4,600);jac=1/(4*np.sqrt(2)*np.pi**2)*(1+radius**2/8)**-3
for power,color in [(2,'#006e82'),(3,'#b45631'),(4,'#7a4e9b')]:
    axes[1].loglog(radius,4*np.pi*radius**(power+2)*jac,label=f'p = {power}',color=color,lw=2)
axes[1].set(xlabel=r'Coordinate radius $|B|$',ylabel=r'$4\pi r^{p+2}J_1(r)$',title='Actual unfixed-link Haar radial integrand')
axes[1].text(.04,.04,'p < 3: finite integral\np ≥ 3: divergent integral\nExact statement for every regulator: SC7',transform=axes[1].transAxes,fontsize=10)
axes[1].legend();axes[1].grid(alpha=.2)
fig.suptitle('Exact stereographic calculation: ordered action and actual link marginal',fontsize=15)
for ext in ['png','svg']:fig.savefig(O/('STEREOGRAPHIC_CUBIC_AND_HAAR.'+ext),dpi=180)
plt.close(fig)
fig,ax=plt.subplots(figsize=(12,5.8),layout='constrained');ax.axis('off')
boxes=[(.03,.57,.27,.3,'Actual original state\nv = dX,  D = L₁ + z\nA = DC,  k = A*v\nAll exterior current rows retained\nTCR1–TCR8'),
       (.37,.57,.27,.3,'Cutoff columns and projection\nc̃ = Z̃⁻¹k̃\nqR = ‖v‖² − r̃²\n‖c̃‖ ≤ √(2qR / γ)\nTCR9–TCR11, TCR18–TCR21'),
       (.71,.57,.27,.3,'Full inverse error\nβ − Cc̃ = D⁻¹(v − Ac̃)\nΔ = √(κ/z)(r̃ + εR‖c̃‖)\nOriginal uncut metric N remains\nTCR3, TCR12'),
       (.12,.06,.76,.29,'Two-sided response → signed original window\n[√P − Δ]₊² ≤ W(z) ≤ [√P + Δ]²\nUse lower central response and upper subtracted responses at εz and Rwin z.\nThe cutoff error is controlled. The interacting residual r̃ remains to be evaluated.\nTCR12, TCR16–TCR17')]
from matplotlib.patches import FancyBboxPatch
for x0,y0,ww,hh,label in boxes:
    ax.add_patch(FancyBboxPatch((x0,y0),ww,hh,boxstyle='round,pad=.012',facecolor='#edf5f7',edgecolor='#346e7b',transform=ax.transAxes))
    ax.text(x0+ww/2,y0+hh/2,label,ha='center',va='center',transform=ax.transAxes,linespacing=1.5,fontsize=10)
for start,end in [((.31,.72),(.36,.72)),((.65,.72),(.7,.72)),((.84,.55),(.72,.37))]:
    ax.annotate('',xy=end,xytext=start,xycoords='axes fraction',arrowprops=dict(arrowstyle='->',color='#346e7b',lw=2))
ax.set_title('Original current residual and its complete physical receiver',fontsize=16,pad=12)
for ext in ['png','svg']:fig.savefig(O/('TWO_SIDED_CURRENT_MAP.'+ext),dpi=180)
plt.close(fig)
print(json.dumps(dict(checks=len(checks),all_passed=True,figures=2)))
