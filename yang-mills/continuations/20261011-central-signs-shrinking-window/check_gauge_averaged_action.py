from pathlib import Path
import itertools,json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
O=Path(__file__).resolve().parent;checks=[]
def mult(q,r):
    return np.r_[q[0]*r[0]-np.dot(q[1:],r[1:]),q[0]*r[1:]+r[0]*q[1:]+np.cross(q[1:],r[1:])]
def conj(q):return q*np.array([1,-1,-1,-1])
def eq(name,a,b):
    assert np.max(np.abs(np.array(a)-np.array(b)))<2e-12,(name,a,b)
    checks.append(dict(name=name,passed=True))
basis=np.eye(4);design=np.concatenate([basis,-basis])
def terms(q):
    x=q[:,0];y=q[:,1:];v=np.zeros(5)
    dot=lambda i,j:np.dot(y[i],y[j])
    triple=lambda i,j,k:np.dot(y[i],np.cross(y[j],y[k]))
    for i in range(4):v[0]+=(1-x[i])*np.prod(1+x[[j for j in range(4) if j!=i]])/4
    for i,j in itertools.combinations(range(4),2):
        k,l=sorted(set(range(4))-{i,j})
        v[0]+=.5*dot(i,j)*(1+x[k])*(1+x[l])
        v[2]-=dot(i,j)*(1-x[k]*x[l])
        v[4]+=.5*dot(i,j)*(1-x[k])*(1-x[l])
    for i,j,k in itertools.combinations(range(4),3):
        l=next(iter(set(range(4))-{i,j,k}))
        v[1]+=triple(i,j,k)*(1+x[l])
        v[3]-=triple(i,j,k)*(1-x[l])
        v[4]+=(1-x[i])*(1-x[j])*(1-x[k])*(1+x[l])/4
    K=dot(0,1)*dot(2,3)-dot(0,2)*dot(1,3)+dot(0,3)*dot(1,2)
    v[2]-=2*K
    return v
for W in [np.array([1.,0,0,0]),np.array([-1.,0,0,0]),np.array([.6,0,0,.8]),np.array([0.,1,0,0])]:
    total=np.zeros(5);tensor=np.zeros((4,4,4,4))
    for root in basis:
        WW=mult(mult(root,W),conj(root))
        for q1,q2,q3 in itertools.product(design,repeat=3):
            q4=mult(mult(mult(conj(q3),conj(q2)),conj(q1)),WW)
            q=np.array([q1,q2,q3,q4]);total+=terms(q)
            tensor+=np.einsum('a,b,c,d->abcd',q1,q2,q3,q4)
    total/=2048;tensor/=2048;m=2*W[0]
    expected=np.array([1-5*m/64,-3*m/16,-15*m/32,-3*m/16,1-5*m/64])
    eq(f'complete five gauge averages trace={m}',total,expected)
    eq(f'all five sum to original deficit trace={m}',total.sum(),2-m)
    for a,b,c,d in itertools.product(range(4),repeat=4):
        tau=mult(mult(mult(basis[a],basis[b]),basis[c]),basis[d])[0]
        eq(f'exact tensor quadrature trace={m} indices={a}{b}{c}{d}',tensor[a,b,c,d],m*tau/128)
# Fierz force receiver tested directly against Pauli derivatives.
rng=np.random.default_rng(61012010)
sigma=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
T=[-.5j*s for s in sigma]
def matrix(q):
    x,a,b,c=q
    return np.array([[x+1j*a,b+1j*c],[-b+1j*c,x-1j*a]])
for n in range(80):
    values=rng.normal(size=(3,4));values/=np.linalg.norm(values,axis=1)[:,None]
    U,P,Q=map(matrix,values);A=U@P;B=U@Q
    lhs=sum(np.trace(t@A).real*np.trace(t@B).real for t in T)
    rhs=.5*np.trace(P@Q.conj().T).real-.25*np.trace(A).real*np.trace(B).real
    eq(f'original full force Fierz receiver {n}',lhs,rhs)
eq('unchanged path five coefficient cancellation',sum([27/16,-3/4,-15/8,-3/4,27/16]),0)
out=dict(checks=len(checks),all_passed=True,scope='Exact degree-two Haar cubature in each independent gauge variable checks all 256 four-link tensor entries at four holonomies and all five rational action averages. Direct original Pauli derivatives check the full force contraction. These verify analytic identities, not sampled vacuum data.',results=checks)
(O/'GAUGE_AVERAGED_ACTION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(10,5.8),layout='constrained')
m=np.linspace(-2,2,501);g=.5
ax.plot(m,(1-5*m/64)/g**2,lw=2.3,label=r'Each of $A_2/Q_g$ and $g^4A_6/Q_g$')
ax.plot(m,-3*m/(16*g*g),lw=2.3,label=r'Each of $gA_3/Q_g$ and $g^3A_5/Q_g$')
ax.plot(m,-15*m/(32*g*g),lw=2.3,label=r'$g^2A_4/Q_g$')
ax.plot(m,(2-m)/g**2,'k--',lw=2.5,label=r'Sum of all five: $(2-m_p)/g^2$')
ax.axhline(0,color='#888888',lw=.8)
ax.set(xlabel=r'Original plaquette expectation $m_p=\mu\,\mathrm{Tr}\,U_p$',
       ylabel='Exact vacuum expectation of the indicated term',
       title='All five rational action terms: exact gauge average (SC21)')
ax.text(.02,.03,'Shown at g = 0.5; formulas hold for every g > 0.\nTwo pairs of terms coincide. Each pair is counted twice in the sum.\nNo numerical vacuum distribution is assumed.',transform=ax.transAxes,fontsize=10,
        bbox=dict(facecolor='white',edgecolor='#cccccc',alpha=.95))
ax.legend(loc='upper right',fontsize=10);ax.grid(alpha=.18)
for ext in ['png','svg']:fig.savefig(O/('GAUGE_AVERAGED_ACTION.'+ext),dpi=180)
plt.close(fig)
print(json.dumps(dict(checks=len(checks),all_passed=True,figures=1)))
