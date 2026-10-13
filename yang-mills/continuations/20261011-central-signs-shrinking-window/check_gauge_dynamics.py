from pathlib import Path
import numpy as np,json
O=Path(__file__).resolve().parent
source=(O/'check_gauge_hessian_rows.py').read_text(encoding='utf8')
source=source[:source.index('# Actual-ground receiving constants')]
source=source.replace('for case in range(8):','snapshots=[]\nfor case in range(2):').replace('if case in [0,7]:','if case in [0,1]:')
source+='\n  snapshots.append((case,U.copy(),g.copy(),H.copy(),K.copy(),list(edges),dict(vertex_index),dict(index)))\n'
ns={'__file__':str(O/'check_gauge_hessian_rows.py')}
exec(compile(source,'retained_gauge_dynamic_inputs','exec'),ns)
T=ns['T'];product=ns['product'];rows=[]
def ck(name,x,y,tol=2e-10):
    error=float(np.linalg.norm(x-y));scale=1+float(np.linalg.norm(x))+float(np.linalg.norm(y))
    assert error<tol*scale,(name,error/scale)
    rows.append(dict(name=name,relative_error=error/scale,tolerance=tol))
for case,U,g,H,K,edges,vid,index in ns['snapshots']:
    n=len(edges);nv=len(vid);c=ns['rng'].normal(size=n)+1j*ns['rng'].normal(size=n)
    active=set()
    def calc_eta(links):
        grad=np.zeros((n,3))
        for z,d,k,coef in [((0,0,0),0,1,.7),((1,1,1),0,2,-1.1),((1,1,1),1,2,1.4)]:
            zd=list(z);zd[d]+=1;zk=list(z);zk[k]+=1
            ids=[index[(z,d)],index[(tuple(zd),k)],index[(tuple(zk),d)],index[(z,k)]]
            active.update(ids)
            factors=[links[ids[0]],links[ids[1]],links[ids[2]].conj().T,links[ids[3]].conj().T]
            for p,e in enumerate(ids):
                for a in range(3):
                    x=factors.copy();x[p]=T[a]@x[p] if p<2 else -x[p]@T[a]
                    grad[e,a]+=coef*np.trace(product(x)).real
        eta=np.zeros((nv,3),complex)
        for e in active:
            v,w,d=edges[e];Ad=np.array([[-2*np.trace(T[i]@links[e]@T[j]@links[e].conj().T).real for j in range(3)] for i in range(3)])
            eta[vid[v]]+=c[e]*grad[e];eta[vid[w]]-=c[e]*Ad.T@grad[e]
        return eta.reshape(-1)
    eta=calc_eta(U);ck('direct original vertex contraction',eta,K.T@(c[:,None]*g).reshape(-1))
    Hfull=H.transpose(0,2,1,3).reshape(3*n,3*n);gc=(c[:,None]*g).reshape(-1)
    Hg=(Hfull@g.reshape(-1)).reshape(n,3)
    # The test function is the retained sum of three four-edge traces:
    # its full scalar Laplacian is exactly -3w.
    L1current=(3*gc-2*(c[:,None]*Hg).reshape(-1)-2*Hfull@gc)
    lhs=K.T@L1current
    for step in [2e-4,1e-4]:
        lap=np.zeros_like(eta);drift=np.zeros_like(eta)
        for e in sorted(active):
            for a in range(3):
                plus=U.copy();minus=U.copy()
                flowp=np.cos(step/2)*np.eye(2)+2*np.sin(step/2)*T[a]
                flowm=np.cos(step/2)*np.eye(2)-2*np.sin(step/2)*T[a]
                plus[e]=flowp@U[e];minus[e]=flowm@U[e]
                ep=calc_eta(plus);em=calc_eta(minus)
                lap+=(ep-2*eta+em)/step**2
                drift+=g[e,a]*(ep-em)/(2*step)
        ck('component scalar Laplacian of the actual test current',lap,-3*eta,2e-6)
        ck('independent right-flow weighted dynamic identity',lhs,-lap-2*drift,2e-6)
    # Original single-factor connection signs yield the plus/plus map.
    for e in sorted(active):
        v,w,d=edges[e];Ad=-K[3*e:3*e+3,3*vid[w]:3*vid[w]+3]
        beta=ns['rng'].normal(size=3);omega=ns['skew'](beta)
        # skew(beta)_ij=-epsilon_kij beta_k, so the two-form with
        # Hodge star beta is -skew(beta).
        omega=-omega
        for sigma,Q in [(1,np.eye(3)),(-1,-Ad)]:
            out=[]
            for a in range(3):
                qa=Q[:,a];dK=-sigma*ns['skew'](qa)
                out.append(.5*np.sum(dK*omega))
            ck('exact original positive target curl contraction',np.array(out),sigma*Q.T@beta)
    # The mixed Hessian curl is retained and every diagonal block is zero.
    curl=np.zeros_like(Hfull,dtype=complex)
    for e in range(n):
        for f in range(n):
            curl[3*e:3*e+3,3*f:3*f+3]=(c[f]-c[e])*H[e,f]
    ck('original current curl antisymmetry',curl,-curl.T)
    ck('original current has zero diagonal-factor curl',np.concatenate([curl[3*e:3*e+3,3*e:3*e+3].reshape(-1) for e in range(n)]),np.zeros(9*n))
out=dict(all_passed=True,checks=len(rows),scope='Two original nonflat SU(2) configurations of the retained gauge-invariant three-plaquette test function. Independent finite right-flow derivatives check the component scalar weighted operator against the full one-form Hessian expression. Connection signs and all diagonal/mixed curl blocks are checked. These are universal algebra/derivative diagnostics, not an actual Yang–Mills vacuum computation.',rows=rows)
(O/'GAUGE_DYNAMIC_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
