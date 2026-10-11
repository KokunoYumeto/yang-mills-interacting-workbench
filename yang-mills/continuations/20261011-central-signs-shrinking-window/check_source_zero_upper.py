from pathlib import Path
import json,math,hashlib,datetime
import numpy as np
import sympy as s
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).parent
y,d,u2,F,A,alpha,L,Q,R,O,delta,slack=s.symbols('y d u2 F A alpha L Q R O delta slack',positive=True)
c=9*alpha/64
J=6*A-3*y
P=(1+c)*y*y-(F*L+4*c*A)*y+4*c*A*A
assert s.expand(P-(y*y-F*L*y+alpha*J*J/64))==0
UZ=Q+R+(36*A*A-36*A*d+9*u2)/(64*F)-3*d/2
received=s.expand(u2+alpha*F*UZ-alpha*F*(3*A-3*d/2)+slack+O+delta-F*L*d)
target=(1+c)*u2-(F*L+4*c*A)*d+4*c*A*A+alpha*F*(Q+R)+slack+O+delta-3*alpha*F*A
assert s.simplify(received-target)==0
old=F*L*d+4*alpha*F*F
new=((F*L+4*c*A)*d-4*c*A*A+3*alpha*F*A)/(1+c)
diff=(c*F*L*d-4*c*A*d+4*c*A*A+4*alpha*F*F*(1+c)-3*alpha*F*A)/(1+c)
assert s.simplify(old-new-diff)==0
U,S=s.symbols('U S',positive=True)
T=s.symbols('T',positive=True)
assert s.simplify(alpha*F*(U-3*S)**2/(4*T)-alpha*(U-3*S)**2/(64*U)-alpha*(U-3*S)**2*(16*F*U-T)/(64*U*T))==0
optimized=3*alpha*F*A-3*alpha*F*d/2+3*alpha*S/32-9*alpha*S*S/(64*U)
assert s.simplify(optimized-(3*alpha*F*A-3*alpha*(16*F*d-S)/32-9*alpha*S*S/(64*U)))==0

pauli=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex)]
gen=[-1j*x/2 for x in pauli]
rng=np.random.default_rng(610112)
def haar():
    q=rng.normal(size=4);q/=np.linalg.norm(q)
    return q[0]*np.eye(2)-1j*sum(q[k+1]*pauli[k] for k in range(3))
def lattice(m):
    edges=[];faces=[]
    for z in np.ndindex(m+1,m+1,m+1):
        for k in range(3):
            if z[k]<m:edges.append((z,k))
        for k in range(3):
            for l in range(k+1,3):
                if z[k]<m and z[l]<m:
                    zk=list(z);zk[k]+=1;zl=list(z);zl[l]+=1
                    faces.append(((z,k,l),[((z,k),1),((tuple(zk),l),1),((tuple(zl),k),-1),((z,l),-1)]))
    return edges,faces
edges,faces=lattice(2)
assert len(edges)==54 and len(faces)==36
inc={e:0 for e in edges}
for _,word in faces:
    for e,_ in word:inc[e]+=1
assert max(inc.values())==4 and sum(inc.values())==4*len(faces)
max_face_error=0.;max_gamma_ratio=0.;min_incidence_margin=float('inf')
for trial in range(25):
    links={e:haar() for e in edges};weights=rng.uniform(.01,1,len(faces));Fv=max(weights)
    grad={e:np.zeros(3) for e in edges};Y=0.;pointwise_defect=0.
    for ip,(_,word) in enumerate(faces):
        factors=[links[e] if sign==1 else links[e].conj().T for e,sign in word]
        product=np.linalg.multi_dot(factors);W=np.trace(product).real;D=2-W;Y+=weights[ip]*D
        pointwise_defect+=16*weights[ip]*(Fv-weights[ip])*D+4*weights[ip]**2*D*D
        for k,(e,sign) in enumerate(word):
            local=[]
            for T in gen:
                differentiated=(T@links[e]) if sign==1 else (-links[e].conj().T@T)
                terms=factors.copy();terms[k]=differentiated
                v=-np.trace(np.linalg.multi_dot(terms)).real
                local.append(v)
            max_face_error=max(max_face_error,abs(np.dot(local,local)-(D-D*D/4)))
            grad[e]+=weights[ip]*np.array(local)
    gamma=sum(np.dot(x,x) for x in grad.values())
    max_gamma_ratio=max(max_gamma_ratio,gamma/(16*Fv*Y))
    margin=16*Fv*Y-gamma-pointwise_defect
    min_incidence_margin=min(min_incidence_margin,margin)
    assert margin>-1e-9
    assert 16*Fv*Y-gamma>=4*Y*Y/len(faces)-1e-9
assert max_face_error<1e-12

def constants(j,Rphysical=4.,kappa=1.):
    a=1/(100*j);q=math.ceil(Rphysical/a)+3
    N=3*q*(q+1)**2;M=3*q*q*(q+1);Ccross=12*q*(q+1)
    g2=kappa/(200*j);alpha=kappa*kappa*a*a;c=9*alpha/64
    Lam=min(2*M,6*g2*math.sqrt(N*M))+2*Ccross
    B=Lam+4*c*M;D=4*c*M*M;disc=B*B-4*(1+c)*D
    rp=(B+math.sqrt(disc))/(2*(1+c));rm=2*D/(B+math.sqrt(disc))
    eps=3*alpha*M/(1+c)
    return dict(j=j,a=a,q=q,N=N,M=M,Ccross=Ccross,alpha=alpha,c=c,Lambda=Lam,rminus=rm,rplus=rp,epsilon=eps)
const=constants(20)
aa=const['a'];ds=np.linspace(const['rminus'],const['rplus'],500)
oldcurve=aa**4*(ds*(const['Lambda']-ds)+4*const['alpha'])
newcurve=aa**4*((ds-const['rminus'])*(const['rplus']-ds)+const['epsilon'])
fig,ax=plt.subplots(figsize=(10.5,6.8))
fig.subplots_adjust(left=.11,right=.985,top=.89,bottom=.22)
ax.plot(aa*aa*ds,oldcurve,color='#B55427',lw=2.6,label='Earlier local moment upper bound')
ax.plot(aa*aa*ds,newcurve,color='#186993',lw=2.6,label='Retained kinetic square: ZU22–ZU26')
ax.fill_between(aa*aa*ds,newcurve,oldcurve,color='#F2D9B7',alpha=.75,label='Proved decrease in this upper envelope')
ax.set_xlabel(r'$a^2 d$, where $d=\mu W_Q$ is the actual unknown mean',fontsize=11)
ax.set_ylabel(r'$a^4\operatorname{Var}_\mu W_Q$ upper envelope',fontsize=11)
ax.set_title('Original-source local covariance: the mean-root interval remains',fontsize=14,pad=12)
for name,r in [('r₋',const['rminus']),('r₊',const['rplus'])]:
    ax.axvline(aa*aa*r,color='#555555',ls=':',lw=1)
    ax.text(aa*aa*r,-.038*max(oldcurve),name,ha='center',va='top',fontsize=12)
ax.set_ylim(-.085*max(oldcurve),1.13*max(oldcurve));ax.grid(alpha=.22)
ax.legend(loc='upper center',framealpha=.95,fontsize=9)
fig.text(.11,.055,'Original parameters: j = 20, κ* = 1, a = 1/2000, q = 8003; all boundary counts retained.\n'
         'This plots proved bounds for the auxiliary patch sum, not sampled ground-state data. Proof: ZU19–ZU26.',fontsize=9)
fig.savefig(root/'source_zero_upper_envelope.png',dpi=180)
fig.savefig(root/'source_zero_upper_envelope.svg')
plt.close(fig)

result={'observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'symbolic_ground_budget_rearrangement':True,'weighted_polynomial_identity':True,
        'old_new_difference':True,'optimized_square_rearrangement':True,'exact_optimized_defect_decomposition_ZU42':True,
        'original_m2_edges':len(edges),'original_m2_faces':len(faces),
        'quaternion_trials':25,'max_face_derivative_error':max_face_error,
        'max_gamma_to_upper_ratio':max_gamma_ratio,'min_weighted_incidence_margin':min_incidence_margin,
        'figure_finite_original_constants':const,
        'limit_samples':[{'j':j,'a2_rminus':(z:=constants(j))['a']**2*z['rminus'],'a2_rplus':z['a']**2*z['rplus']} for j in [10,20,100,1000]],
        'scope':'Exact symbolic and bounded pointwise checks supplement the analytic original-vacuum proof. Random configurations are Haar samples, not samples of the actual ground state.'}
(root/'SOURCE_ZERO_UPPER_CHECKS.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
