from pathlib import Path
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import numpy as np
import json, math

ROOT=Path(__file__).resolve().parent
def original(n):
    m=n-1
    edges=[(d,i,k,l) for d in (1,2,3) for i in range(n-(d==1)) for k in range(n-(d==2)) for l in range(n-(d==3))]
    pos={e:i for i,e in enumerate(edges)}
    def path(i,k,l):
        return [(3,0,0,r) for r in range(l)]+[(2,0,r,l) for r in range(k)]+[(1,r,k,l) for r in range(i)]
    v=np.sqrt(2/n)*np.cos(np.pi*(np.arange(n)+.5)/n)
    v[m//2]=0.
    w=-np.sqrt(2/n)*np.sin(np.pi*(np.arange(m)+1)/n)
    V=np.array([0 if d==1 else w[k]*v[l]/np.sqrt(2*n) if d==2 else -v[k]*w[l]/np.sqrt(2*n) for d,i,k,l in edges])
    N=len(edges); A=np.zeros((N,N)); D=np.zeros(N)
    tree=[[],[],[]]
    for r in range(m):
        for k in range(n):
            for l in range(n): tree[0].append(pos[1,r,k,l])
        for l in range(n): tree[1].append(pos[2,0,r,l])
        tree[2].append(pos[3,0,0,r])
    for eidx,(d,i,k,l) in enumerate(edges):
        ancestors=[pos[e] for e in path(i,k,l)]
        A[ancestors,eidx]=V[eidx]
        D[eidx]=V[eidx]+sum(V[r] for r in ancestors)
    return edges,V,A,D,tree,v,w

def nuclear(X): return np.linalg.svd(X,compute_uv=False).sum()
def rank(X): return int(np.linalg.matrix_rank(X,tol=1e-10))
def finite(n):
    m=n-1; vh2=2/n*np.cos(np.pi/(2*n))**2
    H=float(np.sum(1/(2*np.sin((2*np.arange(1,m+1)-1)*np.pi/(4*m+2)))))
    p=((2*m-1)+vh2*(m-1))/(4*n)
    a2=math.sqrt(p*(m-.5))
    f=3*math.sqrt(2*m-1)/math.sqrt(32*n**3)
    av=H/n+(math.sqrt(m*n-2)+math.sqrt(m))*f
    return {'n':n,'D_n':(3*m-1)/2,'AP_F2':p,'PA_F2':m-.5,'J_nuclear':H,'A2_nuclear_bound':a2,'AV_nuclear_bound':av,'R_n':p+av/2,'trace_positive_bound':(3*m-1)/2+p+av/2,'AV_T23_F2':f*f}

checks=[]
for n in [3,5,7]:
    edges,V,A,D,tree,v,w=original(n); m=n-1; A2=A@A; AV=A*V[None,:]
    L=A+np.diag(D); B=L.T@L-(L@L+(L@L).T)/2
    formula=A.T@A-(A2+A2.T)-(AV+AV.T)/2
    P=tree[1]+tree[2]; f=finite(n)
    ev=np.linalg.eigvalsh(B); trp=float(np.maximum(ev,0).sum()); trm=float(np.maximum(-ev,0).sum())
    J=(np.arange(m)[:,None]<np.arange(n)[None,:]).astype(float)
    c={'n':n,'N':len(edges),'normV2':float(V@V),'commutator_error':float(np.max(np.abs((D[:,None]-D[None,:])*A+A2+AV))),'B_error':float(np.max(np.abs(B-formula))),'trace_B':float(np.trace(B)),'D_n':f['D_n'],'trace_positive':trp,'trace_negative':trm,'R_n':f['R_n'],'A_rank':rank(A),'A_rank_formula':n**3-2*n-1,'A2_rank':rank(A2),'A2_rank_candidate':m*m-1,'AP_rank':rank(A[:,P]),'AV_rank':rank(AV),'block_ranks':[rank(AV[r,:]) for r in tree],'block_rank_formulas':[m*(n*n-2),m*n-1,m],'AP_F2':float(np.sum(A[:,P]**2)),'AP_F2_formula':f['AP_F2'],'PA_F2':float(np.sum(A[P,:]**2)),'PA_F2_formula':f['PA_F2'],'A2_nuclear':float(nuclear(A2)),'A2_nuclear_bound':f['A2_nuclear_bound'],'AV_nuclear':float(nuclear(AV)),'AV_nuclear_bound':f['AV_nuclear_bound'],'AV_block_F2':[float(np.sum(AV[r,:]**2)) for r in tree],'AV_T23_F2_formula':f['AV_T23_F2'],'J_singular_error':float(np.max(np.abs(np.linalg.svd(J,compute_uv=False)-1/(2*np.sin((2*np.arange(1,m+1)-1)*np.pi/(4*m+2))))))}
    assert c['commutator_error']<1e-13 and c['B_error']<1e-13
    assert abs(c['AP_F2']-c['AP_F2_formula'])<1e-13 and abs(c['PA_F2']-c['PA_F2_formula'])<1e-13
    c['block_rank_formulas']=[m*(n*n-2),m*n-2,m]
    Q=A.copy(); Q[P,:]-=A.T[P,:]
    c['complete_square_error']=float(np.max(np.abs(B-(Q.T@Q-A[:,P]@A[:,P].T-(AV+AV.T)/2))))
    c['exact_AV_row_nuclear']=[float(nuclear(AV[r,:])) for r in tree]
    c['refined_trace_negative_bound']=f['AP_F2']+sum(c['exact_AV_row_nuclear'])/2
    assert c['block_ranks']==c['block_rank_formulas'] and c['A_rank']==c['A_rank_formula']
    assert c['A2_rank']==m*m-1 and c['AP_rank']==m*m and c['AV_rank']==c['A_rank']
    assert c['complete_square_error']<1e-13
    print(json.dumps(c,indent=2),flush=True)
    assert abs(c['AV_block_F2'][1]-f['AV_T23_F2'])<1e-13 and abs(c['AV_block_F2'][2]-f['AV_T23_F2'])<1e-13
    assert trm<=f['R_n']+1e-12 and trp<=f['trace_positive_bound']+1e-12
    checks.append(c)
path=[]
for j in range(1,17):
    n=2*j**4+1; f=finite(n)
    f.update(j=j,kinetic_upper_kappa1=400*j*f['trace_positive_bound'],kinetic_ratio_j5=400*f['trace_positive_bound']/j**4,negative_ratio_j3=400*f['R_n']/j**2)
    path.append(f)
(ROOT/'SIGNED_KINETIC_CHECKS.json').write_text(json.dumps({'enumerated':checks,'original_path_kappa_star_1':path,'interpretation':'Finite matrix checks of proved identities and bound functions, not simulated vacuum data.'},indent=2),encoding='utf-8')
