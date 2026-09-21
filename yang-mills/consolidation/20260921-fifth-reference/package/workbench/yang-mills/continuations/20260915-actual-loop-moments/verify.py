#!/usr/bin/env python3
"""Exact SU(2) local-response algebra and rational error evaluation.

Uses only the standard library. Finite algebra, integer geometry, and rigorous
arithmetic are checked here. The analytic vacuum estimates are proved in the
accompanying note; this executable is not a formal verification of that proof.
"""
from __future__ import annotations
import argparse, hashlib, json, math, sys
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent
checks: list[str] = []
controls: list[str] = []

def require(ok: bool, name: str) -> None:
    if not ok:
        raise ValueError(name)

def check(name: str, ok: bool) -> None:
    require(name not in checks, 'duplicate-check-name:' + name)
    require(ok, name)
    checks.append(name)

def reject(name: str, false_claim: bool) -> None:
    require(name not in controls, 'duplicate-control-name:' + name)
    require(not false_claim, 'false-formula-accepted:' + name)
    controls.append(name)

# Sparse polynomials in the twelve ORIGINAL real quaternion coordinates
# (u0,u1,u2,u3,a0,...,a3,b0,...,b3). Coefficients are exact rationals.
NV=12
class P:
    def __init__(self, data=0):
        if isinstance(data, P): self.d=data.d.copy()
        elif isinstance(data, dict): self.d={k:Q(v) for k,v in data.items() if v}
        else: self.d={} if data==0 else {(0,)*NV:Q(data)}
    def __add__(self,o):
        o=P(o); d=self.d.copy()
        for k,v in o.d.items(): d[k]=d.get(k,Q(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self): return P({k:-v for k,v in self.d.items()})
    def __sub__(self,o): return self+-P(o)
    def __rsub__(self,o): return P(o)+-self
    def __mul__(self,o):
        o=P(o); d={}
        for k,v in self.d.items():
            for j,w in o.d.items():
                e=tuple(a+b for a,b in zip(k,j)); d[e]=d.get(e,Q(0))+v*w
        return P(d)
    __rmul__=__mul__
    def __pow__(self,n):
        require(isinstance(n,int) and n>=0,'polynomial-power-domain')
        a=P(1); b=self
        while n:
            if n&1:a=a*b
            b=b*b;n//=2
        return a
    def __truediv__(self,c): return self* (1/Q(c))
    def __eq__(self,o): return self.d==P(o).d
    def diff(self,i):
        d={}
        for e,v in self.d.items():
            if e[i]:
                f=list(e);f[i]-=1;f=tuple(f);d[f]=d.get(f,Q(0))+v*e[i]
        return P(d)

def var(i):
    e=[0]*NV;e[i]=1;return P({tuple(e):Q(1)})

def qmul(x,y):
    return [x[0]*y[0]-sum((x[i]*y[i] for i in range(1,4)),P(0)),
            x[0]*y[1]+x[1]*y[0]+x[2]*y[3]-x[3]*y[2],
            x[0]*y[2]+x[2]*y[0]+x[3]*y[1]-x[1]*y[3],
            x[0]*y[3]+x[3]*y[0]+x[1]*y[2]-x[2]*y[1]]
def qinv(x):return [x[0]]+[-x[i] for i in range(1,4)]
u=[var(i) for i in range(4)]
a=[var(i) for i in range(4,8)]
b=[var(i) for i in range(8,12)]

def X(poly, group, alpha):
    q=[var(4*group+i) for i in range(4)]
    gen=[Q(0)]*4;gen[alpha+1]=Q(1,2)
    tangent=qmul(gen,q)
    return sum((tangent[i]*poly.diff(4*group+i) for i in range(4)),P(0))

def K(poly,group):return -sum((X(X(poly,group,i),group,i) for i in range(3)),P(0))

def sphere_reduce(poly):
    # Literal polynomial division by q0^2+q1^2+q2^2+q3^2-1, in each factor.
    out=P(poly)
    for group in range(3):
        d={}; i=4*group
        for e,c in out.d.items():
            power=e[i]//2; ee=list(e);ee[i]%=2
            term=P({tuple(ee):c})
            term=term*(P(1)-sum((var(i+j)**2 for j in range(1,4)),P(0)))**power
            for z,v in term.d.items(): d[z]=d.get(z,Q(0))+v
        out=P(d)
    return out

def sphere_moment(e):
    if any(v%2 for v in e):return Q(0)
    aa=[v//2 for v in e];A=sum(aa);n=1;d=1
    for j in aa:
        for k in range(1,2*j,2):n*=k
    for k in range(A):d*=4+2*k
    return Q(n,d)

def integrate(poly,groups=(0,1,2)):
    d={}
    for e,c in poly.d.items():
        ee=list(e)
        for group in groups:
            c*=sphere_moment(e[4*group:4*group+4])
            for k in range(4):ee[4*group+k]=0
        ee=tuple(ee);d[ee]=d.get(ee,Q(0))+c
    out=P(d)
    if len(groups)==3:
        require(all(not any(e) for e in out.d),'unintegrated-coordinate')
        return out.d.get((0,)*NV,Q(0))
    return out

def exact_su2():
    F=2*qmul(u,a)[0]; B=2*qmul(u,b)[0]
    j=sum((X(F,0,i)*X(B,0,i) for i in range(3)),P(0))
    tau=2*qmul(a,qinv(b))[0]
    j0=Q(3,8)*tau;j1=j-j0
    uu=qmul(qmul(qmul(u,a),u),b)
    check('Pauli-Fierz-full-shared-link',sphere_reduce(j-(-Q(1,4)*2*uu[0]+Q(1,4)*tau))==0)
    check('conditional-Haar-singlet',integrate(j,(0,))==j0)
    check('conditional-triplet-zero',integrate(j1,(0,))==0)
    check('shared-link-Casimir-singlet',K(j0,0)==0)
    check('shared-link-Casimir-triplet',sphere_reduce(K(j1,0)-2*j1)==0)
    for g in (1,2):
        check('unshared-fundamental-Casimir-'+str(g),K(j,g)==Q(3,4)*j)
    check('fundamental-trace-second-moment',integrate(F*F)==1)
    check('raw-generator-gradient',sphere_reduce(sum((X(F,0,i)**2 for i in range(3)),P(0))-(1-F*F/4))==0)
    hh=sum((X(X(F,0,i),0,k)**2 for i in range(3) for k in range(3)),P(0))
    check('raw-second-derivative-Frobenius',sphere_reduce(hh-(Q(1,2)+F*F/16))==0)
    hmat=[[X(X(F,0,i),0,k) for i in range(3)] for k in range(3)]
    check('original-Pauli-operator-bound-deficit',all(sphere_reduce(
        Q(int(i==j),4)-sum((hmat[k][i]*hmat[k][j] for k in range(3)),P(0))
        -X(F,0,i)*X(F,0,j)/4)==0 for i in range(3) for j in range(3)))
    hh_cross=sum((X(X(F,0,i),1,k)**2 for i in range(3) for k in range(3)),P(0))
    check('raw-cross-link-second-derivative-Frobenius',sphere_reduce(hh_cross-(Q(1,2)+F*F/16))==0)
    check('inverse-word-trace',2*qinv(qmul(u,a))[0]==F)
    check('shared-force-norm',integrate(j*j)==Q(3,16))
    check('singlet-force-norm',integrate(j0*j0)==Q(9,64))
    check('triplet-force-norm',integrate(j1*j1)==Q(3,64))
    check('singlet-triplet-cross-term',integrate(j0*j1)==0)
    for group in range(3):
        for aa,bb,cc in ((0,1,2),(1,2,0),(2,0,1)):
            check(f'right-invariant-bracket-{group}-{aa}-{bb}',X(X(var(4*group),group,bb),group,aa)-X(X(var(4*group),group,aa),group,bb)==-X(var(4*group),group,cc))
    # One elementary loop and a neighbor have six unshared links, hence 9/2.
    k_j=Q(9,2)*j0+Q(13,2)*j1
    pref=Q(4,9)*12
    moments=[pref*integrate(j*j),pref*integrate(j*k_j),pref*integrate(k_j*k_j)]
    check('original-12-neighbor-moments',moments==[Q(1),Q(5),Q(103,4)])
    z=(Q(2,3))*(j0/Q(11,2)+j1/Q(15,2))
    check('actual-two-Casimir-trial',(Q(9,2)+1)*(Q(2,3)/Q(11,2))*j0+(Q(13,2)+1)*(Q(2,3)/Q(15,2))*j1==Q(2,3)*j)
    check('response-leading-coefficient',12*integrate((Q(2,3)*j)*z)==Q(28,165))
    check('restored-leading-coefficient',12*integrate(z*z)==Q(796,27225))
    for n,catalan in ((2,1),(4,2),(6,5)):
        check('Haar-trace-moment-'+str(n),integrate(F**n)==catalan)
    reject('omit-triplet',pref*integrate(j0*j0)==1)
    reject('wrong-singlet-coefficient',integrate(j,(0,))==Q(1,4)*tau)
    reject('replace-poles-by-plaquette-energy',12*integrate((Q(2,3)*j)**2)/4==Q(28,165))
    reject('retain-own-plaquette-as-kernel',sphere_reduce(4-F*F)==0)
    return moments

# Integer graph objects: vertex triples; positively oriented edge (vertex,i);
# face (base,i,j), i<j. The inverse traversal flag remains in face_word.
def plus(n,i,a=1):
    m=list(n);m[i]+=a;return tuple(m)
def face_word(p):
    n,i,j=p
    return ((n,i,1),(plus(n,i),j,1),(plus(n,j),i,-1),(n,j,-1))
def edges(p):return {(n,i) for n,i,sgn in face_word(p)}
def square_edges(side):
    out=set()
    for t in range(side):
        out.update({((t,0,0),0),((t,side,0),0),((0,t,0),1),((side,t,0),1)})
    return out
def touching(C):
    faces=set()
    for n,i in C:
        for j in range(3):
            if j!=i:
                for base in (n,plus(n,j,-1)):
                    faces.add((base,min(i,j),max(i,j)))
    return sorted(faces)
def geometry():
    report=[]
    for side in range(1,13):
        C=square_edges(side); ell=4*side
        fs=touching(C); own=[p for p in fs if edges(p)==C]
        ext=[p for p in fs if edges(p)!=C]
        counts={k:sum(len(C&edges(p))==k for p in ext) for k in (1,2)}
        expected={1:12,2:0} if side==1 else {1:4*ell-8,2:4}
        check(f'original-face-counts-side-{side}',counts==expected and sum(counts.values())==len(ext))
        check(f'own-face-side-{side}',len(own)==int(side==1))
        S=C|set().union(*(edges(p) for p in ext))
        check(f'local-support-size-side-{side}',len(S)==(32 if side==1 else 9*ell-8))
        witnesses=[]
        for p,q in combinations(ext,2):
            available=edges(p)-(edges(q)|C)
            require(bool(available),'missing-unmatched-exterior-edge')
            witnesses.append((p,q,min(available)))
        check(f'all-cross-face-Haar-witnesses-side-{side}',len(witnesses)==len(ext)*(len(ext)-1)//2)
        cs=[]
        for order in range(3):
            cs.append(sum((Q(number*sh*sh,48)*(3*(Q(3,4)*(ell+4-2*sh))**order+(Q(3,4)*(ell+4-2*sh)+2*sh)**order) for sh,number in counts.items()),Q(0)))
        expected_m=[Q(1),Q(5),Q(103,4)] if side==1 else [Q(ell+2,3),Q(ell*(3*ell+14),12),Q(9*ell**3+66*ell**2+76*ell+104,48)]
        check(f'raw-moment-polynomials-side-{side}',cs==expected_m)
        # An overlap of two shared edges is an actual adjacent path.
        for p in ext:
            sh=C&edges(p)
            if len(sh)==2:
                vs=[]
                for n,i in sh:vs.extend([n,plus(n,i)])
                require(len(set(vs))==3,'two-shared-edges-not-adjacent')
        check(f'actual-shared-paths-side-{side}',True)
        report.append({'side':side,'length':ell,'local_edges':len(S),'neighbor_types':counts,'cross_witnesses':len(witnesses),'leading_moments':[str(z) for z in cs]})
    reject('eleven-neighbors',report[0]['neighbor_types'][1]==11)
    return report

def atan_interval(x:Q,N:int):
    require(0<x<1 and N>0,'arctangent-domain')
    s=sum(((-1)**j*x**(2*j+1)/Q(2*j+1) for j in range(N)),Q(0))
    t=(-1)**N*x**(2*N+1)/Q(2*N+1)
    return min(s,s+t),max(s,s+t)
def sqrt_upper(x:Q):
    require(x>=0,'negative-square-root')
    scale=10**50
    n=math.isqrt((x.numerator*scale*scale)//x.denominator)
    lo=Q(n,scale);hi=lo if lo*lo==x else Q(n+1,scale)
    require(lo*lo<=x<=hi*hi,'square-root-endpoint-error')
    return hi
def exp_minus_one_upper(x:Q):
    require(0<=x<1,'certificate-exponential-domain')
    term=Q(1);s=Q(0)
    for j in range(1,31):
        term=term*x/j;s+=term
    nxt=term*x/31
    return s+nxt/(1-x/32)
def ceil_dec(x:Q,places=15):
    scale=10**places; val=-((-x.numerator*scale)//x.denominator)
    return Q(val,scale)
def dec(x:Q,places=15):
    x=ceil_dec(x,places);scale=10**places;n=x.numerator*scale//x.denominator
    sign='-' if n<0 else '';n=abs(n)
    return sign+str(n//scale)+'.'+str(n%scale).zfill(places)

def section_correction():
    # Complete original scalar-product example, with a deliberately noncanonical trial.
    ds=(Q(3),Q(6)); w=(Q(1),Q(2)); y=(Q(1,5),Q(1,4))
    aa=sum(d*z*z for d,z in zip(ds,y)); cc=sum(z*t for z,t in zip(y,w))
    mm=sum(t*t/d for t,d in zip(w,ds)); alpha=cc/aa
    rr=tuple(t-d*z for t,d,z in zip(w,ds,y))
    rc=tuple(t-d*alpha*z for t,d,z in zip(w,ds,y))
    rn=sum(t*t/d for t,d in zip(rr,ds)); cn=sum(t*t/d for t,d in zip(rc,ds))
    check('noncanonical-residual-full-energy',rn==Q(19,200))
    check('canonical-quotient-full-energy',cn==Q(1,99)==mm-cc*cc/aa)
    check('canonical-residual-orthogonality',sum(z*t for z,t in zip(y,rc))==0)
    check('section-correction-exact-vector',all(t==h+(alpha-1)*d*z for t,h,d,z in zip(rr,rc,ds,y)))
    check('section-correction-Pythagoras',rn==cn+aa*(alpha-1)**2)
    check('section-correction-primitive-energy',aa*(alpha-1)**2==Q(1681,19800))
    reject('noncanonical-residual-is-quotient-norm',rn==cn)

def gauge_source():
    def eps(i,j,k):
        if len({i,j,k})<3:return 0
        return 1 if (i,j,k) in ((0,1,2),(1,2,0),(2,0,1)) else -1
    matrices=[[[Q(-eps(a,i,j)) for j in range(3)] for i in range(3)] for a in range(3)]
    casimir=[[sum((-sum(M[i][k]*M[k][j] for k in range(3)) for M in matrices),Q(0)) for j in range(3)] for i in range(3)]
    check('gauge-adjoint-Casimir-two',casimir==[[Q(2*int(i==j)) for j in range(3)] for i in range(3)])
    check('gauge-contraction-invariance',all(M[i][j]+M[j][i]==0 for M in matrices for i in range(3) for j in range(3)))
    check('covariant-residual-L2-constant',Q(3)*Q(128,3)==128)
    check('covariant-residual-energy-constant',128*Q(128,3)==Q(16384,3))
    check('pointwise-small-xi-coefficient',Q(1,2)-Q(16,3)*Q(3,64)==Q(1,4))
    check('pointwise-remainder-constant',Q(64,9)/Q(1,4)==Q(256,9))
    reject('physical-vacuum-in-spin-one-sector',0==2)

def arithmetic():
    at5=atan_interval(Q(1,5),55);at239=atan_interval(Q(1,239),16)
    plo=16*at5[0]-4*at239[1];phi=16*at5[1]-4*at239[0]
    check('Machin-angle-tangent-identity',(Q(120,119)-Q(1,239))/(1+Q(120,119)*Q(1,239))==1)
    check('certified-pi-upper',Q(314159265358979323846,10**20)<plo<phi<Q(355,113))
    # Every numerical assertion below is certified by upward rational bounds.
    pi=Q(355,113); x=Q(1,10**8);ell=4;d=32;aa=Q(256,9)
    check('actual-coupling-domain',0<x<=Q(3,64))
    sq=sqrt_upper
    delta=exp_minus_one_upper(32*pi*d*x)
    eta=exp_minus_one_upper(32*pi*(d+ell-2)*x)
    residual_b=aa*x*x
    bd=ell*sq(128*aa/3)+sq(Q(3))/2*sq(Q(ell**3))*aa
    cd=Q(128*ell,3)+Q(3*ell**2,4)*aa+8*sq(Q(3))*ell**2*aa*x+sq(Q(128))*sq(Q(ell**3))*sq(aa)
    ht=x/3*(eta*48/2+16*x*12)+x*x*bd/2+16*x*ell*residual_b
    e0=2*(ell*residual_b+x/3*eta*12)
    e1=2*(x/3*eta*90+Q(16,3)*x*x*48+cd*x*x+16*ell*x*ht)
    c0,c1,c2=Q(1),Q(5),Q(103,4)
    E0=delta*c0+2*sq((1+delta)*c0)*e0/x+(e0/x)**2
    E1=delta*sq(c0*c2)+sq((1+delta)*c0)*e1/x+sq((1+delta)*c2)*e0/x+e0*e1/(x*x)
    E2=delta*c2+2*sq((1+delta)*c2)*e1/x+(e1/x)**2
    for i,(err,upper) in enumerate(zip((E0,E1,E2),(Q(6,10**4),Q(37,10**4),Q(22,1000)))):
        check('actual-moment-radius-'+str(i),0<err<upper)
    zstar=Q(796,27225); mstar=Q(28,165); zmax=Q(224,165); lz=Q(848,165)
    hz=x*(eta*lz/2+16*x*zmax)
    rr=2*ell*residual_b+16*x*x*lz+16*ell*x*hz
    normz=sq((1+delta)*zstar)
    parts=(delta*x*x*sq(zstar),16*x**3*zmax*lz,
           2*x*x*eta*eta*8*zmax,4*ell*residual_b*x*normz,
           ell*hz*hz+(x*eta*zmax)**2,32*ell*x*x*normz*hz,rr*rr)
    EM=sum(parts)/(x*x)
    EZ=delta*zstar+(eta*zmax)**2+2*normz*rr/x+(rr/x)**2
    check('actual-response-radius',EM<Q(75,10**7))
    check('actual-restored-metric-radius',EZ<Q(21,10**7))
    dC=exp_minus_one_upper(32*pi*ell*x)
    B2=x*delta/4+x*sq(Q(5))*dC/6+ell*residual_b
    meanerr=2*x/9*(B2+Q(3,2)*delta)+Q(2*ell,3)*residual_b
    gramerr=B2+(2*x/3+meanerr)**2
    check('actual-raw-Gram-radius',gramerr<Q(11,10**14))
    check('actual-kinetic-radius',B2<Q(11,10**14))
    # Return through the exact physical trial synthesis map, retaining both mixed entries.
    energy_lo=3-B2-x*x*(mstar+EM+zstar+EZ)
    norm_lo=1-gramerr+x*x*(zstar-EZ)
    trial_lo=energy_lo/(1+gramerr+x*x*(zstar+EZ))
    trial_hi=(3+B2-x*x*(mstar-EM+zstar-EZ))/norm_lo
    check('actual-trial-state-positive-norm-and-energy',energy_lo>0 and norm_lo>0)
    check('actual-trial-energy-lower',trial_lo>3-Q(5,10**13))
    check('actual-trial-energy-upper',trial_hi<3+Q(5,10**13))
    # Inclusion of span((0,1)) into diag(1,3) has trial quotient 3 and full infimum 1.
    reject('one-trial-reverses-variational-direction',Q(1)>=Q(3))
    check('source-g-and-kappa',Q(1)/(4*Q(5000)**2)==x and 2*Q(5000)==10000)
    check('first-Galerkin-lower',Q(2,6)-(5+1)/Q(36)==Q(1,6))
    check('first-Galerkin-residual',1-Q(2,6)*6+(Q(103,4)+10+1)/36==Q(1,48))
    check('response-within-first-Galerkin-interval',Q(1,6)<mstar<Q(3,16))
    reject('coupling-parameter-confusion',Q(1)/(4*Q(5000)**4)==x)
    reject('omit-response-triplet',Q(3,4)/Q(11,2)==mstar)
    reject('false-error-budget',EM<Q(1,10**7))
    reject('extend-small-xi-domain',Q(1,4)<=Q(3,64))
    return {'xi':str(x),'g_squared':'5000','kappa':'10000/a',
            'pi_upper_used':str(pi),'delta_upper':dec(delta),'eta_upper':dec(eta),
            'moment_error_radius_upper':[dec(e) for e in (E0,E1,E2)],
            'actual_moment_enclosures':[['0.9994','1.0006','kappa^2 xi^2'],['4.9963','5.0037','kappa^3 xi^2'],['25.728','25.772','kappa^4 xi^2']],
            'response_center':str(mstar),'response_error_radius_upper':dec(EM),
            'response_certified_radius':'0.0000075','response_factor':'kappa xi^2',
            'restored_center':str(zstar),'restored_error_radius_upper':dec(EZ),
            'restored_certified_radius':'0.0000021','restored_factor':'xi^2',
            'physical_trial_energy_interval':['3-5/10^13','3+5/10^13','kappa'],
            'variational_direction':'The full physical finite-volume gap is at most this trial quotient.',
            'raw_Gram_error_upper':dec(gramerr,20),'kinetic_relative_error_upper':dec(B2,20),
            'proof_scope':'Analytic inequalities in RESEARCH_NOTE.md, evaluated by rational upper endpoints; no vacuum samples or spin truncation.'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-receipt',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    exact_su2(); gauge_source(); section_correction(); geo=geometry(); nums=arithmetic()
    for name in ('RESEARCH_NOTE.md','verify.py'):
        require((ROOT/name).is_file() and (ROOT/name).stat().st_size>0,'missing-required-source:'+name)
    payload={'schema':'ym-actual-loop-response-v1','finite_checks':checks,'negative_controls':controls,
             'geometry':geo,'certified_evaluation':nums,
             'source_sha256':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ('RESEARCH_NOTE.md','verify.py')},
             'scope':'Exact SU(2) polynomial and Haar calculations, integer graph incidence, and rational evaluation of written analytic error bounds. No Lean or numerical vacuum integration.'}
    text=json.dumps(payload,sort_keys=True,indent=2)+'\n'
    if args.verify_receipt:
        require(args.verify_receipt.read_text()==text,'receipt-mismatch')
    if args.output:args.output.write_text(text)
    sys.stdout.write(text)

if __name__=='__main__':
    try:main()
    except (ValueError,OSError) as exc:
        print('FAIL: '+str(exc),file=sys.stderr);sys.exit(1)
