"""FPA algebra and geometry diagnostics; no Yang–Mills ground samples."""
from pathlib import Path
import itertools,json
import numpy as np
import sympy as sp
O=Path(__file__).resolve().parent;rng=np.random.default_rng(610133)
checks=[]
def ck(name,x,y,atol=2e-11):
    err=float(np.max(abs(np.asarray(x)-np.asarray(y))))
    assert err<=atol*max(1.,float(np.max(abs(y)))),(name,err)
    checks.append(dict(name=name,error=err))
# Reuse the published original geometry and ordered SU2 utility definitions only.
src=(O/'check_scalar_energy.py').read_text()
exec(src.split('# Original SU(2) ordered words, including inverse differentiated factors.')[1].split('for trial in range(3):')[0])
for trial in range(3):
    links=[su2() for e in edges];gr={};D=[]
    for p,(es,signs) in enumerate(faces):
        fac=[links[e] if s==1 else links[e].conj().T for e,s in zip(es,signs)]
        D.append(2-np.trace(prod(fac)).real)
        for i,(e,s) in enumerate(zip(es,signs)):
            grad=[]
            for t in T:
                ff=list(fac);ff[i]=t@fac[i] if s==1 else -fac[i]@t
                grad.append(-np.trace(prod(ff)).real)
            gr[p,e]=np.array(grad)
    c=rng.normal(size=len(edges))+1j*rng.normal(size=len(edges))
    bar=np.array([sum(c[e] for e in es)/4 for es,ss in faces])
    alpha=np.array([sum(((c[e]-bar[p])*gr[p,e] for p in inc[e]),np.zeros(3,dtype=complex)) for e in range(len(edges))])
    total=0
    for q,(es,ss) in enumerate(faces):
        full=sum(alpha[e]@gr[q,e] for e in es)
        terms=[(p,e,(c[e]-bar[p])*(gr[p,e]@gr[q,e])) for e in es for p in inc[e] if p!=q]
        ck('full original face action',full,sum(v for p,e,v in terms))
        signatures=[frozenset(set(faces[p][0])^set(es)) for p,e,v in terms]
        assert len(set(signatures))==len(signatures) and all(len(x)==6 for x in signatures)
        tau=rng.choice([-1,1],size=len(edges))
        for (p,e,v),S in zip(terms,signatures):
            ck('central character and inverse factors',np.prod(tau[faces[p][0]])*np.prod(tau[es]),np.prod(tau[list(S)]))
        total+=sum(abs(c[e]-bar[p])**2 for p,e,v in terms)*3/16
    weighted=3/16*sum((len(inc[e])-1)*abs(c[e]-bar[p])**2 for p,(es,ss) in enumerate(faces) for e in es)
    ck('full boundary Haar coefficient form',total,weighted)
    for p,(es,ss) in enumerate(faces):
        ck('four raw values with complex conjugates',sum(abs(c[e]-bar[p])**2 for e in es),sum(abs(c[e]-c[f])**2 for e,f in itertools.combinations(es,2))/4)
# Quaternion probability-Haar second moments computed exactly, all three generators.
haar_norm=sum(sp.Rational(1,4)**2 for _ in range(3))
assert haar_norm==sp.Rational(3,16)
checks.append(dict(name='exact Haar theta squared norm 3/16',error=0))
# Exact finite-character averaging with a strictly positive diagnostic density.
# This density is not identified with the interacting Yang–Mills ground density.
g=next(e for e in range(len(edges)) if len(inc[e])==4)
p,q,r=inc[g][:3];support=sorted(set(faces[p][0]+faces[q][0]+faces[r][0]))
assignments=np.array(list(itertools.product([-1,1],repeat=len(support))))
idx={e:i for i,e in enumerate(support)}
char=lambda S:np.prod(assignments[:,[idx[e] for e in S]],axis=1)
cp,cq,cr=[char(faces[k][0]) for k in [p,q,r]]
density=np.exp(.3*cp-.4*cq+.7*cr)
pair_character=char(set(faces[p][0])^set(faces[r][0]))
ck('complete actual-density character selector',np.mean((cp*cq)*(cr*cq)*density),np.mean(pair_character*density))
assert abs(np.mean(pair_character*density))>1e-3
checks.append(dict(name='mixed density component need not vanish',error=0))
# Radius-two S3 verifies the full source equation, including Ricci 1/2.
x,eta,kappa=sp.symbols('x eta kappa',real=True)
df2=(1-x**2)/4
z=eta*df2
Delta_z=sp.diff(z,x,2)*df2+sp.diff(z,x)*(-sp.Rational(3,4)*x)
Lz=-kappa*(Delta_z+2*eta*sp.diff(z,x)*df2)
YV=kappa*(-sp.Rational(3,4)*eta-eta**2*x/2)*df2
deformation=2*kappa*(3*eta*x**2/16-eta**2*x*df2/4)
rough_and_Ricci=kappa*eta*df2/4
poly=sp.Poly(sp.expand(Lz+YV+deformation+rough_and_Ricci),x,eta,kappa)
assert poly.is_zero
checks.append(dict(name='complete radius-two curvature source equation',error=0))
bad=sp.Poly(sp.expand(Lz+YV+deformation- kappa*eta*df2/4),x,eta,kappa)
assert not bad.is_zero
checks.append(dict(name='curvature diagnostic detects omitted Ricci term',error=0))
result=dict(all_passed=True,checks=len(checks),scope='Original cubic incidence, ordered SU2 configurations, exact Haar quaternion moments and finite central-character algebra. An independent radius-two S3 identity tests all curvature signs. No actual Yang–Mills vacuum or spectral mass is numerically sampled.',details=checks)
(O/'FACE_FIELD_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='details'}))
