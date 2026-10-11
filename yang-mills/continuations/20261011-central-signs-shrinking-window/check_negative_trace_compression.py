"""Bounded checks of the complete original-edge compression and root receiver."""
from pathlib import Path
import json, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent

def geometry(n):
    m=n-1
    edges=[(d,i,k,l) for d in (1,2,3)
           for i in range(m if d==1 else n)
           for k in range(m if d==2 else n)
           for l in range(m if d==3 else n)]
    ix={e:j for j,e in enumerate(edges)}
    def path(i,k,l):
        return [(3,0,0,r) for r in range(l)]+[(2,0,r,l) for r in range(k)]+[(1,r,k,l) for r in range(i)]
    v=np.sqrt(2/n)*np.cos(np.pi*(np.arange(n)+.5)/n)
    v[m//2]=0.0 # exact cosine node
    w=-np.sqrt(2/n)*np.sin(np.pi*(np.arange(m)+1)/n)
    V=np.array([0 if d==1 else w[k]*v[l]/np.sqrt(2*n) if d==2
                else -v[k]*w[l]/np.sqrt(2*n) for d,i,k,l in edges])
    N=len(edges);A=np.zeros((N,N));D=np.zeros(N)
    for j,e in enumerate(edges):
        ancestors=path(*e[1:])
        for f in ancestors:A[ix[f],j]=V[j]
        D[j]=V[j]+sum(V[ix[f]] for f in ancestors)
    T=A*V
    B=A.T@A-A@A-(A@A).T-(T+T.T)/2
    L=np.diag(D)+A
    U=[ix[(1,r,k,l)] for k in range(n) for l in range(n) for r in range(m)]
    Umat=np.eye(N)[:,U]
    Z=np.zeros((n,m))
    for q in range(1,n):
        Z[:q,q-1]=1/np.sqrt(q*(q+1))
        Z[q,q-1]=-q/np.sqrt(q*(q+1))
    J=np.array([[float(r<i) for i in range(n)] for r in range(m)])
    K=np.zeros((N,m**3));Gamma=np.zeros((len(U),m**3));cells=[]
    for k in range(m):
        for l in range(m):
            a=w[k]*v[l]/np.sqrt(2*n);b=-v[k]*w[l]/np.sqrt(2*n)
            radius=np.hypot(a,b)
            u=np.array([-b,a])/radius if radius else np.array([1.,0.])
            gamma=a*b*(b-a)/radius if radius else 0.
            c=k*m+l
            for i in range(n):
                K[ix[(2,i,k,l)],c*m:(c+1)*m]=u[0]*Z[i]
                K[ix[(3,i,k,l)],c*m:(c+1)*m]=u[1]*Z[i]
            Gamma[(k*n+l)*m:(k*n+l+1)*m,c*m:(c+1)*m]=gamma*J@Z
            cells.append((k,l,a,b,u,gamma))
    F=np.column_stack((Umat,K));P=F@F.T;Q=np.eye(N)-P
    C=np.block([[np.zeros((len(U),len(U))),-Gamma/2],
                [-Gamma.T/2,np.zeros((K.shape[1],K.shape[1]))]])
    tree=set(sum([path(i,k,l) for i in range(n) for k in range(n) for l in range(n)],[]))
    chords=[e for e in edges if e not in tree]
    return locals()

def maxabs(x):return float(np.max(np.abs(x))) if x.size else 0.

def check(n):
    g=geometry(n)
    for key in ('A','B','D','F','P','Q','C','T','K','Gamma','Umat','J','Z','V','L','N','m','cells','ix','chords','path'):
        globals()[key]=g[key]
    residuals={
        'B_from_original_L':maxabs(B-(L.T@L-(L@L+(L@L).T)/2)),
        'isometry':maxabs(F.T@F-np.eye(F.shape[1])),
        'A_K_zero':maxabs(A@K),
        'T_K_receiver':maxabs(T@K-Umat@Gamma),
        'compression':maxabs(F.T@B@F-C),
        'cross_block':maxabs(P@B@Q+P@(A@A+T/2)@Q),
    }
    sigma=np.array([1/(2*np.sin(k*np.pi/(2*n))) for k in range(1,n)])
    residuals['singular_values']=maxabs(np.linalg.svd(J@Z,compute_uv=False)-sigma)
    inv=np.zeros((n,m));inv[0,0]=-1
    for i in range(1,m):inv[i,i-1]=1;inv[i,i]=-1
    inv[m,m-1]=1
    residuals['inverse_J']=maxabs(J@inv-np.eye(m))
    residuals['inverse_endpoint_form']=maxabs(inv.T@inv-(2*np.eye(m)-np.eye(m,k=1)-np.eye(m,k=-1)))
    negative=float(np.maximum(-np.linalg.eigvalsh(B),0).sum())
    lower=.5*sum(abs(c[-1]) for c in cells)*sigma.sum()
    hsum=sum(1/(2*np.sin((2*r-1)*np.pi/(4*m+2))) for r in range(1,m+1))
    v0sq=2/n*np.cos(np.pi/(2*n))**2
    pn=(2*m-1+v0sq*(m-1))/(4*n)
    fn=np.sqrt(9*(2*m-1)/(32*n**3))
    upper=pn+.5*(hsum/n+fn*(np.sqrt(m*n-2)+np.sqrt(m)))
    assert lower-1e-9<=negative<=upper+1e-9
    rng=np.random.default_rng(103+n)
    X=rng.normal(size=(N,7));cov=X@X.T
    cov/=np.linalg.norm(X,2)**2
    whole=np.trace(B@cov)
    compressed=np.trace(P@B@P@cov)
    complement=np.trace(Q@B@Q@cov)
    cross=-2*np.trace(P@(A@A+T/2)@Q@cov)
    residuals['full_covariance_decomposition']=abs(float(whole-compressed-complement-cross))
    # Genuine configuration-dependent root blocks, tested on exact Gauss vectors.
    nc=len(chords);rot=[]
    for c in chords:
        axis=rng.normal(size=3);axis/=np.linalg.norm(axis);angle=rng.uniform(-2,2)
        Xc=np.array([[0,-axis[2],axis[1]],[axis[2],0,-axis[0]],[-axis[1],axis[0],0]])
        rot.append(np.eye(3)+np.sin(angle)*Xc+(1-np.cos(angle))*(Xc@Xc))
    rootmap=np.zeros((3*N,3*nc));Gauss=np.zeros((3,3*nc))
    for cidx,c in enumerate(chords):
        target=list(c[1:]);target[c[0]-1]+=1
        block=slice(3*cidx,3*cidx+3)
        rootmap[3*ix[c]:3*ix[c]+3,block]=np.eye(3)
        for f in path(*c[1:]):rootmap[3*ix[f]:3*ix[f]+3,block]+=np.eye(3)
        for f in path(*target):rootmap[3*ix[f]:3*ix[f]+3,block]-=rot[cidx].T
        Gauss[:,block]=np.eye(3)-rot[cidx].T
    j=rng.normal(size=3*nc)
    j-=Gauss.T@np.linalg.solve(Gauss@Gauss.T,Gauss@j)
    scores=(rootmap@j).reshape(N,3)
    residuals['root_Gauss']=maxabs(sum(scores[ix[e]] for e in [(1,0,0,0),(2,0,0,0),(3,0,0,0)]))
    residuals['chord_Gauss']=maxabs(Gauss@j)
    d2=cells[0][2]**2
    rootU=scores[[ix[(1,r,0,0)] for r in range(m)]]
    rootH=-(scores[[ix[(2,i,0,0)] for i in range(n)]]+scores[[ix[(3,i,0,0)] for i in range(n)]])/np.sqrt(2)
    residuals['root_mean_zero']=maxabs(rootH.sum(axis=0))
    residuals['root_receiver']=maxabs(J@rootH+rootU/np.sqrt(2))
    root_contraction=-cells[0][-1]*np.sum(rootU*(J@rootH))/3
    residuals['root_signed_contraction']=abs(float(root_contraction+d2*np.sum(rootU**2)/3))
    cell_total=0.;defect_total=0.
    for k,l,a,b,u,gamma in cells:
        G=scores[[ix[(1,r,k,l)] for r in range(m)]]
        h=u[0]*scores[[ix[(2,i,k,l)] for i in range(n)]]+u[1]*scores[[ix[(3,i,k,l)] for i in range(n)]]
        q=inv@G;s0=(u[0]+u[1])/2;delta=h-s0*q
        hp=h-h.mean(axis=0);dp=delta-delta.mean(axis=0)
        cell_total-=gamma*np.sum(G*(J@hp))/3
        defect_total-=gamma*(s0*np.sum(G**2)+np.sum(G*(J@dp)))/3
    residuals['full_flux_defect_receiver']=abs(float(cell_total-defect_total))
    residuals['score_compression_receiver']=abs(float(cell_total-np.sum(scores*(P@B@P@scores))/3))
    assert max(residuals.values())<2e-10,residuals
    return {'n':n,'original_edges':N,'compression_dimension':F.shape[1],
            'exact_formula_lower_evaluated':float(lower),'negative_trace':negative,
            'SK20_upper_evaluated':float(upper),'residuals':residuals,
            'root_cell_test_value':float(root_contraction)}

def coefficient(n):
    k=np.arange(n-1);x=np.pi*(k+.5)/n;h=np.pi/(2*n)
    a=-np.sin(x[:,None]+h)*np.cos(x[None,:])
    b=np.cos(x[:,None])*np.sin(x[None,:]+h)
    r=np.hypot(a,b);F=np.divide(np.abs(a*b*(b-a)),r,out=np.zeros_like(r),where=r>1e-14)
    return float(2*F.sum()/n**2)

def main():
    checks=[check(n) for n in (3,5,7)]
    grid=[3,5,9,17,33,65,129,257,513]
    coeff=[coefficient(n) for n in grid]
    result={'kind':'Floating-point checks; proofs are in NEGATIVE_TRACE_COMPRESSION.md',
            'matrix_checks':checks,'riemann_samples':dict(zip(map(str,grid),coeff))}
    (HERE/'NEGATIVE_TRACE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    plt.rcParams.update({'font.size':11})
    fig,axes=plt.subplots(2,2,figsize=(13,9),layout='constrained')
    ax=axes[0,0];ax.axis('off')
    ax.text(.02,.94,'Exact original-edge compression',fontsize=16,weight='bold',va='top')
    lines=[r'$U$: all direction-one edges',r'$K$: $x_{d,i}=u_d z_i$, $\sum_i z_i=0$',
           r'$u=(-v_3,v_2)/\sqrt{v_2^2+v_3^2}$',r'$A(U\oplus K)=0$, $T K\subset U$',
           r'$B_{UU}=B_{KK}=0$, $B_{UK}=-\gamma J_0/2$',
           r'$\gamma=v_2v_3(v_3-v_2)/\sqrt{v_2^2+v_3^2}$',
           'Both endpoint differences are retained.', 'Proof: TC1–TC6; original coefficients: SK8, SK14.']
    for i,line in enumerate(lines):ax.text(.02,.80-.095*i,line,va='top')
    ax=axes[0,1];xx=[c['n'] for c in checks]
    ax.plot(xx,[c['negative_trace'] for c in checks],'o-',label=r'$\operatorname{tr}B_-$ (full matrix)')
    ax.plot(xx,[c['exact_formula_lower_evaluated'] for c in checks],'s-',label='Compression lower bound')
    ax.plot(xx,[c['SK20_upper_evaluated'] for c in checks],'^-',label='SK20 upper bound')
    ax.set(xlabel='Original n = 2L + 1',ylabel='Deterministic trace',title='All original edges; bounded numerical samples')
    ax.legend(fontsize=9);ax.grid(alpha=.25)
    ax=axes[1,0];ax.plot(grid,coeff,'o-');ax.axhline(.18117843974321488,color='black',linestyle='--',label=r'$C_\gamma$ (independent integral)')
    ax.set(xscale='log',xlabel='Original n',ylabel=r'$n\sum_{k,l}|\gamma_{kl}|$',title='Riemann coefficient; proof TC7–TC8');ax.legend();ax.grid(alpha=.25)
    ax=axes[1,1];ax.axis('off')
    ax.text(.02,.94,'Actual vacuum: complete receiving map',fontsize=16,weight='bold',va='top')
    lines=[r'$\operatorname{tr}(B\mathsf{m})=$ compression + complement + cross',
           r'$G_{00}=Jq$, $h_{00}=-q/\sqrt{2}$ (root Gauss)',
           r'$\mathcal{C}_{00}=-\frac{d^2}{3}\,\mu\sum_r|g_{(1,r,0,0)}|^2<0$',
           r'$d^2=\frac{2}{n^3}\sin^2(\pi/n)\cos^2(\pi/(2n))$',
           'Every other cell retains its incoming and channel terms.',
           'The deterministic trace is not a vacuum lower bound.',
           'Proof: TC10–TC17; original root map: SK30–SK32.']
    for i,line in enumerate(lines):ax.text(.02,.80-.11*i,line,va='top',fontsize=11)
    fig.suptitle('Negative trace compression with all boundary and actual-score terms',fontsize=18)
    fig.savefig(HERE/'COMPRESSION.png',dpi=170);fig.savefig(HERE/'COMPRESSION.svg')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
