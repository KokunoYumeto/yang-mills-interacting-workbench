from pathlib import Path
import itertools,json,numpy as np
O=Path(__file__).resolve().parent
# Reuse the retained original SU(2) links and analytic three-plaquette
# derivatives, then add the independently derived current-moment checks.
source=(O/'check_gauge_hessian_rows.py').read_text(encoding='utf8')
source=source[:source.index('# Actual-ground receiving constants')]
source=source.replace('for case in range(8):','snapshots=[]\nfor case in range(3):').replace('if case==7:','if case==2:').replace('if case in [0,7]:','if case in [0,1,2]:')
source+='\n  snapshots.append((case,U.copy(),g.copy(),K.copy(),Lfull.copy(),list(edges),dict(stars),dict(vertex_index)))\n'
ns={'__file__':str(O/'check_gauge_hessian_rows.py')}
exec(compile(source,'retained_gauge_hessian_inputs','exec'),ns)
ck=ns['ck'];inherited=len(ns['rows']);moments=[]
def psd(name,A):
    ev=np.linalg.eigvalsh((A+A.conj().T)/2);low=float(ev[0]);scale=1+float(np.linalg.norm(A))
    assert low>=-2e-10*scale,(name,low,scale)
    ns['rows'].append(dict(name=name,least_eigenvalue=low,scale=scale))
for case,U,g,K,Li,edges,stars,vid in ns['snapshots']:
    n=len(edges);nv=len(vid)
    D=np.zeros((3*n,n))
    for e in range(n):D[3*e:3*e+3,e]=g[e]
    B=K.T@D;A0=B.T@B;A1=(K@B).T@(K@B);V=B.T@Li@B
    Ge=np.sum(g*g,axis=1)
    ck('full vertex covariance diagonal',np.diag(A0),2*Ge)
    ck('full covariance constant kernel',A0@np.ones(n),np.zeros(n))
    ck('vertical-loss constant kernel',V@np.ones(n),np.zeros(n))
    ck('complete local A1 diagonal',np.diag(A1),np.array([(len(stars[v])+len(stars[w])+2)*Ge[e] for e,(v,w,d) in enumerate(edges)]))
    for _ in range(12):
        c=ns['rng'].normal(size=n)+1j*ns['rng'].normal(size=n)
        pair=0
        for v,i in vid.items():
            J=B[3*i:3*i+3,:];Sv=J.T@J
            ck('local vertex row sum',Sv@np.ones(n),np.zeros(n))
            for e,f in itertools.combinations(stars[v],2):pair-=Sv[e,f]*abs(c[e]-c[f])**2
        ck('signed local pair-difference energy',np.vdot(c,A0@c),pair)
        # All links in K remain, including those outside the chosen source.
        ck('complete transported local moment',np.vdot(c,A1@c),np.linalg.norm(K@B@c)**2)
    psd('original degree bound for local moments',12*A0-A1)
    Ai=np.linalg.pinv(A1,rcond=1e-11);receiver=A0@Ai@A0
    psd('full inverse moment block',np.block([[V,A0],[A0,A1]]))
    psd('complete inverse moment lower bound',V-receiver)
    psd('receiver dominates degree estimate',receiver-A0/12)
    psd('complete vertical norm upper bound',np.diag(Ge)-V)
    floor=np.array([4*Ge[e]/(len(stars[v])+len(stars[w])+2) for e,(v,w,d) in enumerate(edges)])
    assert np.min(np.diag(V)-floor)>=-2e-10
    ns['rows'].append(dict(name='every original single-edge diagonal bound',least_defect=float(np.min(np.diag(V)-floor))))
    moments.append((A0,A1,V))
    # The common scalar spatial weight uses the exact midpoint at mesh a.
    a=1/200;vec=np.array([1.,.3,.5]);M=float(np.linalg.norm(vec))
    c=np.array([a*(np.array(v)+np.eye(3)[d]/2)@vec for v,w,d in edges])
    eta=B@c;comm=np.zeros_like(eta)
    for v,i in vid.items():
        phi=a*np.array(v)@vec
        comm[3*i:3*i+3]=B[3*i:3*i+3,:]@(c-phi)
    ck('exact midpoint Gauss commutator',eta,comm)
    assert np.linalg.norm(eta)**2<=3*a*a*M*M*Ge.sum()+1e-12
    ev,evc=np.linalg.eigh(K.T@K);good=ev>1e-10
    weights=a**4*abs(evc[:,good].T@eta)**2/ev[good];r=ev[good]/a**2
    ck('original graph inverse norm total',weights.sum(),a**4*np.vdot(eta,Li@eta))
    ck('original graph scale first moment',r@weights,a*a*np.linalg.norm(eta)**2)
    for cutoff in [1.,100.,10000.,100000.]:
        assert weights[r>=cutoff].sum()<=(r@weights)/cutoff+1e-13
        ns['rows'].append(dict(name='retained graph-scale tail',case=case,cutoff=cutoff))
    # Averaging all signed permutation rotations of determinant +1 gives
    # the exact invariant rank-two tensor comparison in GCM2.
    rot=[]
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([-1,1],repeat=3):
            R=np.eye(3)[list(perm)]*np.array(signs)[:,None]
            if np.linalg.det(R)>.5:rot.append(R)
    x=ns['rng'].normal(size=3);y=ns['rng'].normal(size=3)
    ck('original Lie-component invariant covariance',sum(np.outer(R@x,R@y) for R in rot)/len(rot),np.eye(3)*(x@y)/3)
# A nontrivial average checks the pseudoinverse after averaging, not
# an unjustified interchange with the pointwise inverse.
A0=sum(x[0] for x in moments)/len(moments)
A1=sum(x[1] for x in moments)/len(moments)
V=sum(x[2] for x in moments)/len(moments)
psd('averaged full inverse-moment receiver',V-A0@np.linalg.pinv(A1,rcond=1e-11)@A0)
out=dict(all_passed=True,checks=len(ns['rows'])-inherited,inherited_gauge_checks=inherited,scope='Universal finite SU(2) graph/current identities using the retained three-plaquette function. Two nonflat and one flat configuration preserve all original edges and gauge zero modes. These arrays and their finite averages are not an approximation of the Yang–Mills vacuum; actual-state and continuum assertions follow from the written proof.',rows=ns['rows'][inherited:])
(O/'GAUGE_CURRENT_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
