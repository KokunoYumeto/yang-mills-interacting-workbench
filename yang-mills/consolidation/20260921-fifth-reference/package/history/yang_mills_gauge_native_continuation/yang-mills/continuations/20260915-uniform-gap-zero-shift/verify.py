#!/usr/bin/env python3
"""Exact algebra and rational endpoints for the uniform-gap/zero-shift note.

Finite fixtures accompany the written analytic proof; they do not certify it.
Uses the standard library and hash-pinned local predecessor helpers only.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import sys
from fractions import Fraction as Q

HERE=Path(__file__).resolve().parent
YM=HERE.parents[1]
ALM=YM/'continuations/20260915-actual-loop-moments'
CONTROL=YM/'research-control/check.py'
EXPECTED={
    ALM/'verify.py':'690f3cd1de505aae7d152bcb4ce97a032ea2a1c72f8cb8a2c68bd4d4578bb042',
    ALM/'RESEARCH_NOTE.md':'0ac4afbec39b2e878d5555af85a86803d9ba6ac5505dc7817f231e5533c0dd2b',
    CONTROL:'068e763b341e7c054cb3a4a48fc240e10e250d673646add2a6169da6bbd610a6'}

def require(ok: bool, name: str):
    if not ok: raise ValueError(name)

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def imported(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module

try:
    for path,wanted in EXPECTED.items():
        require(path.is_file(),'missing-predecessor:'+str(path.name))
        require(sha(path)==wanted,'predecessor-hash:'+str(path.name))
except (ValueError, OSError) as exc:
    print('FAIL: '+str(exc),file=sys.stderr)
    sys.exit(1)
old=imported('ym_zero_parent_alm',ALM/'verify.py')
ctl=imported('ym_zero_parent_control',CONTROL)
M=ctl.M; eye=ctl.eye

def zero(n,m):return M(n,m,(Q(0),)*(n*m))
def det(A):
    require(A.n==A.m,'det-square')
    out=Q(0)
    for p in itertools.permutations(range(A.n)):
        x=Q((-1)**sum(p[i]>p[j] for i in range(A.n) for j in range(i+1,A.n)))
        for i,j in enumerate(p):x*=A.at(i,j)
        out+=x
    return out

def submatrix(A,rows,cols):return M.rows([[A.at(i,j) for j in cols] for i in rows],columns=len(cols))
def psd(A):
    if A.n!=A.m or A.T!=A:return False
    for size in range(1,A.n+1):
        for rows in itertools.combinations(range(A.n),size):
            if det(submatrix(A,rows,rows))<0:return False
    return True

def inverse_cofactor(A):
    n=A.n;d=det(A);require(d!=0,'cofactor-singular')
    return M.rows([[Q((-1)**(i+j))*det(submatrix(A,[k for k in range(n) if k!=j],
        [k for k in range(n) if k!=i]))/d for j in range(n)] for i in range(n)])

def block(A,B,C,D):
    require(A.n==B.n and C.n==D.n and A.m==C.m and B.m==D.m,'block-shape')
    return M.rows([a+b for a,b in zip(A.to_rows(),B.to_rows())]+
                  [a+b for a,b in zip(C.to_rows(),D.to_rows())])

passed=[];negative=[]
def ck(name,ok):
    require(name not in passed,'duplicate-check:'+name)
    require(bool(ok),'check:'+name);passed.append(name)

def neg(name,false_claim):
    require(name not in negative,'duplicate-negative:'+name)
    require(not bool(false_claim),'false-formula-accepted:'+name)
    negative.append(name)

def representation_and_support():
    spins=[Q(n,2) for n in range(1,81)]
    ck('spin-generator-Casimir-bound',all(j<=Q(2,3)*j*(j+1) for j in spins))
    ck('generator-bound-polynomial-factor',all(Q(2,3)*j*(j+1)-j==j*(2*j-1)/3 for j in spins))
    neg('one-half-replaces-two-thirds',Q(1,2)<=Q(1,2)*Q(3,4))
    ck('plaquette-four-original-Casimirs',4*Q(3,4)==3)
    ck('sixteen-original-trace-index-tuples',len(list(itertools.product(range(2),repeat=4)))==16)
    ck('source-constant-retains-both-weights',4*2**4*16==1024)
    neg('delete-source-support-factor',4*16==1024)
    # Pinching on the original 2 tensor 2 coefficient space, with both outputs.
    P=M.rows([[0,0,0,0],[0,Q(1,2),Q(-1,2),0],[0,Q(-1,2),Q(1,2),0],[0,0,0,0]])
    T=eye(4)-P
    A=M.rows([[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]])
    ck('singlet-idempotent',P@P==P and P.T==P and T@P==zero(4,4))
    ck('pinching-retains-both-coefficient-traces',sum((P@A@P).at(i,i) for i in range(4))==Q(1,2)
       and sum((T@A@T).at(i,i) for i in range(4))==Q(1,2))
    ck('positive-coefficient-trace-norm-budget',psd(P@A@P) and psd(T@A@T)
       and sum((P@A@P+T@A@T).at(i,i) for i in range(4))==1)

    def norm(records):
        return max(sum(2**len(S)*sum(j*(j+1) for j in js)*amp
                       for S,js,amp in records if a in S) for a in range(3))
    def majorant(F,G):
        return max(sum(2**len(S|T)*3*sum(j*k for j,k in zip(js,ks))*af*ag
                       for S,js,af in F for T,ks,ag in G if a in S|T)
                   for a in range(3))
    labels=[frozenset(s) for k in range(1,4) for s in itertools.combinations(range(3),k)]
    for t in range(18):
        F=[];G=[]
        for i,S in enumerate(labels):
            j=tuple(Q(1+(t+i+e)%4,2) if e in S else Q(0) for e in range(3))
            k=tuple(Q(1+(2*t+i+e)%3,2) if e in S else Q(0) for e in range(3))
            F.append((S,j,Q(1+(i+t)%3,7+i)))
            G.append((S,k,Q(1+(2*i+t)%4,11+i)))
        ck('anchored-bilinear-majorant-'+str(t),majorant(F,G)<=Q(8,3)*norm(F)*norm(G))
    ck('support-union-product-weight',all(2**len(S|T)<=2**len(S)*2**len(T) for S in labels for T in labels))
    neg('sum-replaces-product-support-weight',2**7<=2**4+2**4)
    family={frozenset({0}):Q(-5),frozenset({0,1}):Q(2),frozenset({0,2}):Q(3)}
    primitive={S:a for S,a in family.items() if S!=frozenset({0})}
    rebuilt={S:a for S,a in primitive.items()};rebuilt[frozenset({0})]=-sum(primitive.values())
    ck('assembly-kernel-exact-primitive',sum(family.values())==0 and rebuilt==family)
    neg('zero-assembly-deletes-labelled-source',all(a==0 for a in family.values()))
    for n in range(1,10):
        js=[Q(1+(3*n+i)%8,2) for i in range(n)]
        c=sum(j*(j+1) for j in js)
        ck('Hessian-row-spin-bound-'+str(n),all(j*sum(js)<=Q(n+1,2)*c for j in js))
    ck('retained-support-row-weights',all(Q(m+1,2**m)<=1 for m in range(1,81)))
    ck('spatial-tail-weight-monotonicity',all(Q(m+2,2**(m+1))<=Q(m+1,2**m) for m in range(1,81)))
    off=M.rows([[0,1],[1,0]])
    neg('diagonal-only-Hessian-bound',psd(zero(2,2)-off))


def fixed_point_constants():
    x=Q(1,16384);B=1024*x;R=2048*x;alpha=Q(8,3)
    ck('endpoint-source-radius',B==Q(1,16) and R==Q(1,8))
    ck('closed-ball-invariance',B+alpha*R*R==Q(5,6)*R)
    ck('actual-contraction-factor',2*alpha*R==Q(2,3))
    ck('complete-Hessian-coefficient',Q(3,2)*2048==3072)
    ck('full-gap-coefficient-domain-endpoint',Q(1,2)-6144*x==Q(1,8))
    ck('literal-coupling-domain-g-eight',Q(1)/(4*Q(8)**4)==x)
    ck('physical-energy-lower-endpoint',2*8**2*Q(1,8)==8**2-Q(3072,8**2))
    neg('extend-fixed-point-domain-to-g-one',Q(1,4)<=x)
    neg('physical-kappa-can-be-omitted',2*Q(3,2)**2/Q(7,5)==1)
    C=[Q(math.comb(2*j,j),j+1) for j in range(40)]
    ck('Catalan-complete-quadratic-recurrence',all(C[n]==sum(C[j]*C[n-1-j] for j in range(n)) for n in range(1,40)))
    ck('Catalan-coefficient-bound',all(C[n]<=4**n for n in range(40)))
    theta=4*alpha*B
    ck('original-series-tail-ratio',theta==Q(2,3))
    p0=Q(0)
    for n in range(7):
        p1=B+alpha*p0*p0
        ck('majorant-monotone-iterate-'+str(n),p0<=p1<=R)
        p0=p1
    for P in range(1,8):
        finite=sum(C[p-1]*alpha**(p-1)*B**p for p in range(P+1,30))
        ck('certified-coefficient-tail-'+str(P),finite<=B*theta**P/(1-theta))
    ck('connected-label-size-induction',all((3*i+1)+(3*j+1)-1==3*(i+j)+1 for i in range(1,10) for j in range(1,10)))
    ck('vacuum-energy-scalar-retained',Q(2)*Q(1,50)*80-Q(7,3)*Q(2,7)==Q(38,15))


def coordinate_gamma2():
    P=old.P;X=old.X;var=old.var
    ids=[(g,a) for g in range(2) for a in range(3)]
    def dx(f,i):return X(f,*i)
    def delta(f):return sum((dx(dx(f,i),i) for i in ids),P(0))
    choices=[(var(0)*var(1),var(0)*var(2)+var(3)),
             (var(0)*var(4)+var(1)*var(5),var(2)+var(6))]
    for t,(u,f) in enumerate(choices):
        du={i:dx(u,i) for i in ids};df={i:dx(f,i) for i in ids}
        def L(h):return delta(h)+2*sum((du[i]*dx(h,i) for i in ids),P(0))
        gamma=sum((v*v for v in df.values()),P(0))
        lf=L(f)
        direct=L(gamma)/2-sum((df[i]*dx(lf,i) for i in ids),P(0))
        second=sum((dx(dx(f,j),i)**2 for i in ids for j in ids),P(0))
        drift=2*sum((df[j]*dx(du[i],j)*df[i] for i in ids for j in ids),P(0))
        ck('full-coordinate-Gamma2-'+str(t),old.sphere_reduce(direct-second+drift)==0)
        sym=P(0);anti=P(0)
        for g in range(2):
            for a in range(3):
                for b in range(3):
                    x=X(X(f,g,b),g,a);y=X(X(f,g,a),g,b)
                    anti+=(x-y)**2/4;sym+=(x+y)**2/4
        ck('original-commutator-curvature-half-'+str(t),old.sphere_reduce(anti-gamma/2)==0)
        ck('complete-second-derivative-split-'+str(t),
           old.sphere_reduce(sum((X(X(f,g,b),g,a)**2 for g in range(2) for a in range(3) for b in range(3)),P(0))-sym-anti)==0)
        neg('reverse-vacuum-Hessian-sign-'+str(t),old.sphere_reduce(direct-second-drift)==0)
        if t==1:
            diagdrift=2*sum((df[i]*dx(du[i],i)*df[i] for i in ids),P(0))
            neg('delete-Hessian-cross-link-entries',old.sphere_reduce(drift-diagdrift)==0)
    neg('coercivity-on-uncentered-vacuum',Q(0)>=Q(1,8))


def exact_zero_shift_polynomials():
    P=old.P;u=old.u;a=old.a;b=old.b
    F=2*old.qmul(u,a)[0];WP=2*old.qmul(u,b)[0]
    j=sum((old.X(F,0,i)*old.X(WP,0,i) for i in range(3)),P(0))
    tau=2*old.qmul(a,old.qinv(b))[0]
    j0=Q(3,8)*tau;j1=j-j0
    z=Q(4,27)*j0+Q(4,39)*j1
    ck('zero-shift-coefficient-identity',z==Q(4,39)*j+Q(16,351)*j0)
    ck('zero-shift-exact-source',Q(9,2)*Q(4,27)*j0+Q(13,2)*Q(4,39)*j1==Q(2,3)*j)
    ck('zero-shift-original-response-coefficient',12*old.integrate(Q(2,3)*j*z)==Q(8,39))
    ck('zero-shift-original-restored-coefficient',12*old.integrate(z*z)==Q(196,4563))
    ck('zero-shift-local-polynomial-supremum',Q(4,39)*12+Q(16,351)*9==Q(64,39))
    ck('zero-shift-local-derivative-sum',Q(4,39)*48+Q(16,351)*27==Q(80,13))
    ck('zero-shift-retains-both-energy-sectors',Q(3,4)/Q(9,2)+Q(1,4)/Q(13,2)==Q(8,39))
    neg('positive-shift-is-zero-shift',Q(28,165)==Q(8,39))
    neg('delete-triplet-zero-shift-weight',Q(3,4)/Q(9,2)==Q(8,39))


def raw_matrix_residuals():
    D=M.rows([[3,1,0],[1,4,1],[0,1,2]])
    G=M.rows([[2,1],[1,3]])
    W=M.rows([[1,2],[0,1],[2,-1]])
    Di=D.inverse()
    ck('zero-shift-inverse-independent-cofactors',Di==inverse_cofactor(D))
    ck('verified-kernel-floor-one',psd(D-eye(3)))
    exact=W.T@Di@W
    K0=exact+M.rows([[2,1],[1,1]])
    E=block(K0,W.T.scale(-1),W.scale(-1),D)
    H=block(G,zero(2,3),zero(3,2),eye(3))
    op=H.inverse()@E
    ck('full-original-energy-positive',psd(E))
    ck('raw-Gram-self-adjoint-zero-shift',op.T@H==H@op)
    ck('full-block-zero-shift-original-gram',G@submatrix(op.inverse(),[0,1],[0,1])==G@(K0-exact).inverse()@G)
    neg('erase-right-state-Gram',G@submatrix(op.inverse(),[0,1],[0,1])==G@(K0-exact).inverse())
    V=M.rows([[1,0],[1,2],[0,1]])
    source=V.T@D@V; forc=V.T@W
    canon=V@source.inverse()@forc
    trial=V@M.rows([[Q(1,3),Q(1,5)],[Q(1,7),Q(-1,4)]])
    r=W-D@trial;rc=W-D@canon
    low=W.T@trial+trial.T@W-trial.T@D@trial
    quotient=exact-canon.T@D@canon
    change=canon-trial
    ck('whole-zero-shift-residual-gram',exact-low==r.T@Di@r)
    ck('full-residual-bound-with-proved-floor',psd(r.T@r-r.T@Di@r))
    ck('restored-state-error-identity',(Di@W-trial).T@(Di@W-trial)==r.T@Di@Di@r)
    ck('restored-state-error-upper-bound',psd(r.T@r-r.T@Di@Di@r))
    ck('canonical-original-normal-equation',V.T@rc==zero(2,2))
    ck('canonical-entire-quotient-gram',quotient==rc.T@Di@rc and psd(quotient))
    ck('source-section-correction-primitive',r==rc+D@change)
    ck('section-correction-cross-term-zero',rc.T@change==zero(2,2))
    ck('complete-canonical-plus-primitive-energy',r.T@Di@r==quotient+change.T@D@change)
    neg('noncanonical-residual-is-quotient-norm',r.T@Di@r==quotient)
    neg('invent-kernel-floor-one-hundred',psd(D-eye(3).scale(100)))
    neg('remove-residual-mixed-entries',all((r.T@Di@r).at(i,j)==0 for i in range(2) for j in range(2) if i!=j))
    for s in (Q(1,10),Q(1),Q(5,2)):
        inv=(D+eye(3).scale(s)).inverse();Ms=W.T@inv@W
        ck('memory-zero-limit-order-'+str(s),psd(exact-Ms) and psd(exact.scale(s)-(exact-Ms)))
    # Full-domain lower versus one-dimensional trial upper, with actual inclusion.
    free=M.rows([[Q(1,2),0],[0,3]])
    ck('full-domain-floor-different-from-trial',psd(free-eye(2).scale(Q(1,2))))
    neg('single-state-reverses-variational-infimum',Q(1,2)>=3)
    # Constant Haar sector is deliberately retained in the original scalar space.
    neg('force-positive-energy-on-vacuum',0>=Q(1,8))


def rational_evaluation():
    at5=old.atan_interval(Q(1,5),55);at239=old.atan_interval(Q(1,239),16)
    lo=16*at5[0]-4*at239[1];hi=16*at5[1]-4*at239[0]
    ck('Machin-tangent-original-angle',(Q(120,119)-Q(1,239))/(1+Q(120,119)*Q(1,239))==1)
    ck('outward-rational-pi-bound',Q(314159265358979323846,10**20)<lo<hi<Q(355,113))
    pi=Q(355,113);x=Q(1,10**8);aa=Q(256,9);gap=Q(1,2)-6144*x
    ck('actual-zero-shift-domain',0<x<=Q(1,16384)<Q(3,64))
    ck('actual-positive-inverse-floor',gap==Q(49993856,10**8)>Q(1,8))
    ck('original-physical-coupling',Q(1)/(4*5000**2)==x and 2*5000==10000)
    sq=old.sqrt_upper
    delta=old.exp_minus_one_upper(1024*pi*x)
    eta=old.exp_minus_one_upper(1088*pi*x)
    zs=Q(196,4563);ms=Q(8,39);zm=Q(64,39);lz=Q(80,13)
    hz=x*(eta*lz/2+16*x*zm)
    rz=8*aa*x*x+16*x*x*lz+64*x*hz
    nz=sq((1+delta)*zs)
    terms=[delta*x*x*sq(zs),16*x**3*zm*lz,16*x*x*eta*eta*zm,
           16*aa*x**3*nz,4*hz*hz,128*x*x*nz*hz,rz*rz/gap]
    EM=sum(terms)/(x*x)
    EZ=delta*zs+(eta*zm)**2+2*nz*rz/(gap*x)+(rz/(gap*x))**2
    ck('actual-zero-shift-response-radius',0<EM<Q(94,10**7))
    ck('actual-zero-shift-metric-radius',0<EZ<Q(41,10**7))
    ck('actual-canonical-plus-primitive-energy-radius',0<rz*rz/(gap*x*x)<Q(22,10**12))
    ck('actual-trial-norm-positive',(1-delta)*zs-(eta*zm)**2>0)
    neg('uncertified-zero-shift-error',EM<Q(1,10**6))
    dc=old.exp_minus_one_upper(128*pi*x)
    B2=x*delta/4+sq(Q(5))*x*dc/6+4*aa*x*x
    emu=2*x/9*(B2+Q(3,2)*delta)+Q(8,3)*aa*x*x
    EG=B2+(2*x/3+emu)**2
    ck('unchanged-raw-state-Gram-bound',EG<Q(11,10**14))
    ck('unchanged-raw-kinetic-bound',B2<Q(11,10**14))
    energy_lo=3-B2-x*x*(ms+EM)
    energy_hi=3+B2-x*x*(ms-EM)
    norm_lo=1-EG+x*x*(zs-EZ)
    norm_hi=1+EG+x*x*(zs+EZ)
    trial_lo=energy_lo/norm_hi;trial_hi=energy_hi/norm_lo
    ck('actual-zero-shift-lift-norm-energy-positive',energy_lo>0 and norm_lo>0)
    ck('actual-zero-shift-trial-lower',trial_lo>3-Q(5,10**13))
    ck('actual-zero-shift-trial-upper',trial_hi<3+Q(5,10**13))
    ck('actual-full-gap-return-order',gap<trial_lo<=trial_hi)
    # The first moment bounds compactified tails at fixed physical parameters.
    for lam in (Q(1),Q(3),Q(100)):
        ck('spectral-high-tail-scalar-'+str(lam),all((1 if t>=lam else 0)<=t/lam for t in (Q(0),Q(1,8),Q(1),Q(10),Q(1000))))
    # The preserved running coordinate c=1/g^2 has this exact validity range.
    ck('running-path-domain-exact-endpoint',Q(1,64)**2/4==Q(1,16384))
    neg('extend-strong-coupling-to-running-c-one',Q(1)**2/4<=Q(1,16384))
    return {'xi':str(x),'g_squared':'5000','kappa':'10000/a','gap_lower_coefficient':str(gap),
        'response_center':str(ms),'response_radius_upper':old.dec(EM,18),
        'response_certified_radius':'0.0000094','response_original_factor':'kappa xi^2',
        'restored_center':str(zs),'restored_radius_upper':old.dec(EZ,18),
        'restored_certified_radius':'0.0000041','restored_original_factor':'xi^2',
        'quotient_plus_correction_radius_upper':old.dec(rz*rz/(gap*x*x),22),
        'quotient_plus_correction_certified_radius':'0.000000000022',
        'quotient_plus_correction_original_factor':'kappa xi^2',
        'delta_upper':old.dec(delta,18),'eta_upper':old.dec(eta,18),
        'response_seven_error_terms_divided_by_xi_squared_upper':[old.dec(t/(x*x),22) for t in terms],
        'raw_Gram_radius_upper':old.dec(EG,22),'kinetic_relative_radius_upper':old.dec(B2,22),
        'full_gap_enclosure':['0.49993856 kappa','(3+5/10^13) kappa'],
        'scope':'Analytical inequalities evaluated with rational outward endpoints; no vacuum samples or spin cutoff.'}


def volume_limit_checks():
    R=Q(1,8);q=Q(4,3)*R
    ck('actual-conditional-influence-row-bound',q==Q(1,6))
    ck('all-support-influence-weight-bound',all(Q(m-1,2**m)<=Q(1,4) for m in range(1,81)))
    ck('original-density-factor-in-influence',8*Q(1,2)*Q(4,3)*Q(1,4)==Q(4,3))
    for p in (Q(1,7),Q(2,7),Q(1,2),Q(5,7)):
        for r in (Q(3,2),Q(2),Q(5)):
            pp=p*r/(1+p*(r-1))
            TV=abs(pp-p)
            ck('finite-exponential-tilt-envelope-'+str(p)+'-'+str(r),TV<=(r-1)/(r+1))
    # Derivative of log(r)-2(r-1)/(r+1), as an exact rational identity.
    ck('tilt-log-envelope-derivative',all(1/r-4/(r+1)**2==(r-1)**2/(r*(r+1)**2) for r in (Q(1),Q(3,2),Q(2),Q(5))))
    neg('discard-positive-conditional-influence',abs(Q(2,3)-Q(1,2))<=0)
    C=M.rows([[0,Q(1,20),Q(1,40)],[Q(1,20),0,Q(1,30)],[Q(1,40),Q(1,30),0]])
    b=M.rows([[Q(1,100)],[Q(1,80)],[Q(1,120)]])
    row=max(sum(C.at(i,j) for j in range(3)) for i in range(3))
    ck('actual-finite-comparison-row-majorant',row<q)
    solution=(eye(3)-C).inverse()@b
    T=eye(3).scale(Q(2,3))+C.scale(Q(1,3))
    ck('heat-bath-comparison-equation',solution==T@solution+b.scale(Q(1,3)))
    ck('complete-comparison-matrix-inverse',(eye(3)-C).inverse()==inverse_cofactor(eye(3)-C))
    ck('comparison-positive-and-bounded',all(0<=solution.at(i,0)<=max(b.at(j,0) for j in range(3))/(1-q) for i in range(3)))
    partial=zero(3,1);power=eye(3)
    for n in range(7):
        partial=partial+power@b;power=power@C
        ck('all-paths-Neumann-remainder-'+str(n),solution-partial==power@solution)
    neg('delete-interior-comparison-coupling',solution==b)

    # Exact label-union recurrence, independent of representation coefficients.
    seeds=[frozenset({0,1,2,3}),frozenset({3,4,5,6}),frozenset({6,7,8,9})]
    def coefficients(allowed):
        out=[{}, {S:Q(1) for S in seeds if S<=allowed}]
        for p in range(2,7):
            row={}
            for k in range(1,p):
                for S,a in out[k].items():
                    for T,b in out[p-k].items():
                        if S&T:row[S|T]=row.get(S|T,Q(0))+a*b
            out.append(row)
        return out
    small=coefficients(frozenset(range(7)));large=coefficients(frozenset(range(10)))
    for p in range(1,7):
        ck('exact-cutoff-support-compatibility-'+str(p),small[p]=={S:v for S,v in large[p].items() if S<=frozenset(range(7))})
        ck('complete-labelled-cluster-size-'+str(p),all(len(S)<=3*p+1 for S in large[p]))
    neg('outside-labelled-cluster-can-be-reassigned-inside',frozenset({6,7,8,9})<=frozenset(range(7)))

    B=M.rows([[Q(1,20),Q(1,40)],[Q(1,40),Q(1,30)]])
    w=M.rows([[0],[1]])
    rowB=max(sum(B.at(i,j) for j in range(2)) for i in range(2))
    ck('complete-drift-matrix-row-majorant',rowB<=Q(3,2)*R)
    kappa=Q(7,3);t=Q(1,5);alpha=2*kappa*t
    partial=zero(2,1);P=eye(2)
    for n in range(8):
        partial=partial+(P@w).scale(alpha**(n+1)/math.factorial(n+1))
        scalar=sum(alpha**(j+1)*rowB**j/Q(math.factorial(j+1)) for j in range(n+1))
        ck('time-ordered-full-matrix-majorant-'+str(n),all(0<=partial.at(i,0)<=scalar for i in range(2)))
        ck('time-integration-factor-'+str(n),Q(n+1,math.factorial(n+1))==Q(1,math.factorial(n)))
        P=P@B
    ck('distant-coordinate-return-is-retained',partial.at(0,0)>0)
    neg('diagonal-only-drift-propagation',partial.at(0,0)==0)
    for k in (Q(1,2),Q(7,3),Q(10000)):
        ck('original-Brownian-generator-factor-'+str(k),(2*k)/2==k)
    neg('lose-Brownian-factor-two',Q(7,3)/2==Q(7,3))
    x=Q(1,10**8);pi=Q(355,113)
    lower=1/(1+old.exp_minus_one_upper(128*pi*x))
    physical_time=lower/(8*kappa)
    ck('nonzero-original-volume-limit-correlation',lower-4*kappa*physical_time==lower/2>0)


def extensive_energy_checks():
    F=2*old.u[0]
    v1=F/3;v2=-(F*F-1)/72
    wholeK=lambda p:4*old.K(p,0)
    grad=4*sum((old.X(v1,0,i)**2 for i in range(3)),old.P(0))
    ck('actual-single-plaquette-first-coefficient',wholeK(v1)==F)
    ck('actual-single-plaquette-second-coefficient',old.sphere_reduce(wholeK(v2)-(grad-Q(1,3)))==0)
    ck('actual-removed-scalar-energy-coefficient',old.integrate(grad)==Q(1,3))
    ck('actual-second-source-Haar-mean-zero',old.integrate(v2)==0)
    aa=Q(256,9)
    ck('extensive-ground-energy-cubic-constant',8*aa/3==Q(2048,27))
    ck('extensive-ground-energy-quartic-constant',aa*aa==Q(65536,81))
    for L in (2,3,4,10,50):
        m=2*L;edges=3*m*(m+1)**2;faces=3*m*m*(m+1)
        ck('original-extensive-count-ratio-'+str(L),Q(edges,faces)==Q(m+1,m)<=Q(5,4))
    neg('delete-extensive-ground-energy-correction',Q(1,3)==0)


def optimized_domain_checks():
    # The exact coefficient in the unchanged four-link word order.
    index=lambda t:sum(v*2**(3-i) for i,v in enumerate(t))
    aa=[[Q(0) for _ in range(16)] for _ in range(16)]
    for i0,i1,i2,i3 in itertools.product(range(2),repeat=4):
        aa[index((i1,i2,1-i2,1-i3))][index((i0,i1,1-i3,1-i0))]+=(-1)**(i0+i2)
    A=M.rows(aa);gram=A.T@A;absolute=gram.scale(Q(1,2))
    ck('original-plaquette-Fourier-absolute-square',absolute@absolute==gram)
    ck('original-plaquette-Fourier-squared-Gram',gram@gram==gram.scale(4))
    ck('original-plaquette-Fourier-trace-norm-eight',sum(absolute.at(i,i) for i in range(16))==8)
    ck('original-plaquette-Fourier-Haar-norm',sum(gram.at(i,i) for i in range(16))/16==1)
    neg('ordinary-trace-replaces-Fourier-trace-norm',sum(A.at(i,i) for i in range(16))==8)
    neg('Hilbert-Schmidt-norm-replaces-trace-norm',sum(gram.at(i,i) for i in range(16))==8**2)
    def kron(A,B):
        return M.rows([[A.at(i,k)*B.at(j,l) for k in range(A.m) for l in range(B.m)]
            for i in range(A.n) for j in range(B.n)])
    def cmul(A,B):return (A[0]@B[0]-A[1]@B[1],A[0]@B[1]+A[1]@B[0])
    def adj(A):return (A[0].T,A[1].T.scale(-1))
    def ctensor(A,B):return (kron(A[0],B[0])-kron(A[1],B[1]),kron(A[0],B[1])+kron(A[1],B[0]))
    def quat(q):
        q0,q1,q2,q3=q
        return M.rows([[q0,-q2],[q2,q0]]),M.rows([[-q3,-q1],[-q1,q3]])
    qs=[(Q(3,5),Q(4,5),0,0),(Q(5,13),0,Q(12,13),0),
        (Q(7,25),0,0,Q(24,25)),(Q(1,2),Q(1,2),Q(1,2),Q(1,2))]
    ck('original-rational-quaternions-unit',all(sum(x*x for x in q)==1 for q in qs))
    for shift in range(4):
        us=[quat(qs[(i+shift)%4]) for i in range(4)]
        word=cmul(cmul(cmul(us[0],us[1]),adj(us[2])),adj(us[3]))
        tensor=us[0]
        for u in us[1:]:tensor=ctensor(tensor,u)
        coeff=(A@tensor[0],A@tensor[1])
        ck('literal-original-Fourier-trace-word-'+str(shift),
           all(sum(coeff[k].at(i,i) for i in range(16))==sum(word[k].at(i,i) for i in range(2)) for k in range(2)))
    w=Q(5,4)
    ck('sharper-source-retains-exact-weights',4*w**4*8==Q(625,8))
    ck('auxiliary-norm-identity-map',all(w**m<=2**m<=(Q(8,5))**n*w**m for n in range(1,12) for m in range(1,n+1)))
    ck('sharp-Hessian-support-weight',max(Q(m+1)/w**m for m in range(1,81))==Q(256,125))
    ck('sharp-influence-support-weight',max(Q(m-1)/w**m for m in range(1,81))==Q(4096,3125))
    ck('sharp-Hessian-row-coefficient',Q(3,2)*Q(256,125)==Q(384,125))
    ck('sharp-influence-row-coefficient',Q(16,3)*Q(4096,3125)==Q(65536,9375))
    for d in range(8):
        md=max(3,d+1)
        ck('complete-sharper-spatial-tail-'+str(d),all(Q(m+1)/w**m<=Q(md+1)/w**md for m in range(d+1,81)))
    for root in (Q(1),Q(7,8),Q(3,4),Q(2,3),Q(163,288)):
        x=Q(3,2500)*(1-root*root);R=Q(3,16)*(1-root);B=Q(625,8)*x
        ck('summed-original-Catalan-majorant-'+str(root),R==B+Q(8,3)*R*R)
        ck('sharpened-full-curvature-coefficient-'+str(root),Q(1,2)-Q(768,125)*R==Q(144,125)*root-Q(163,250))
    edge=Q(451,552960);rcrit=Q(125,1536)
    ck('exact-sharper-domain-endpoint',1-Q(2500,3)*edge==Q(163,288)**2)
    ck('sharp-root-at-domain-endpoint',rcrit==Q(3,16)*(1-Q(163,288)))
    ck('actual-strict-contraction-envelope',Q(16,3)*rcrit==Q(125,288)<1)
    ck('actual-strict-influence-envelope',Q(65536,9375)*rcrit==Q(128,225)<1)
    ck('actual-complete-drift-envelope',Q(384,125)*rcrit==Q(1,4))
    ck('original-coupling-return',4*Q(138240,451)*edge==1)
    ck('closed-nine-halves-domain',Q(1)/(4*Q(9,2)**4)==Q(4,6561)<edge)
    ck('closed-nine-halves-square-certificate',Q(9683,19683)>Q(401,576)**2)
    ck('closed-nine-halves-gap-return',Q(144,125)*Q(401,576)-Q(163,250)==Q(3,20))
    neg('positive-gap-at-critical-Hessian-bound',Q(1,2)-Q(768,125)*rcrit>0)
    neg('extend-sharper-proof-to-g-four',Q(1)/(4*4**4)<edge)
    x=Q(1,10**8);N=10**30;rad=1-Q(2500,3)*x
    n=math.isqrt(rad.numerator*N*N//rad.denominator)
    rootlo=Q(n,N);roothi=Q(n+1,N)
    ck('outward-square-root-original-coupling',rootlo**2<=rad<roothi**2)
    d=Q(144,125)*rootlo-Q(163,250)
    ck('actual-sharper-physical-lower-edge',d>Q(49999519998,10**11))
    pi=Q(355,113);delta=old.exp_minus_one_upper(1024*pi*x);eta=old.exp_minus_one_upper(1088*pi*x)
    zs=Q(196,4563);ms=Q(8,39);zm=Q(64,39);lz=Q(80,13);astar=Q(256,9)
    hz=x*(eta*lz/2+16*x*zm);rz=8*astar*x*x+16*x*x*lz+64*x*hz
    nz=old.sqrt_upper((1+delta)*zs)
    terms=[delta*x*x*old.sqrt_upper(zs),16*x**3*zm*lz,16*x*x*eta*eta*zm,
           16*astar*x**3*nz,4*hz*hz,128*x*x*nz*hz,rz*rz/d]
    em=sum(terms)/(x*x)
    ez=delta*zs+(eta*zm)**2+2*nz*rz/(d*x)+(rz/(d*x))**2
    ck('actual-sharper-zero-shift-response-interval',em<Q(94,10**7))
    ck('actual-sharper-zero-shift-metric-interval',ez<Q(41,10**7))
    ck('actual-sharper-zero-shift-quotient-cost',rz*rz/(d*x*x)<Q(22,10**12))
    ck('original-running-path-domain-squared',Q(451,138240)/4==edge)
    return {'proved_domain':{'g_fourth_strict_min':'138240/451','xi_strict_max':'451/552960'},
        'full_physical_gap':'kappa [(144/125) sqrt(1-(2500/3) xi)-163/250]',
        'closed_domain':'g>=9/2','closed_gap_lower':'3 kappa/20 = 3g^2/(10a)',
        'actual_xi':str(x),'actual_g_squared':'5000','actual_kappa':'10000/a',
        'actual_gap_lower_rational':str(d),'actual_gap_safe_lower_coefficient':'0.49999519998',
        'response_center':str(ms),'response_radius_upper':old.dec(em,22),'response_certified_radius':'0.0000094',
        'response_original_factor':'kappa xi^2',
        'restored_center':str(zs),'restored_radius_upper':old.dec(ez,22),'restored_certified_radius':'0.0000041',
        'restored_original_factor':'xi^2',
        'quotient_plus_correction_radius_upper':old.dec(rz*rz/(d*x*x),24),
        'quotient_plus_correction_certified_radius':'0.000000000022',
        'quotient_plus_correction_original_factor':'kappa xi^2',
        'full_gap_enclosure':['0.49999519998 kappa','(3+5/10^13) kappa'],
        'source_Fourier_trace_norm':'8','source_majorant':'625 xi/8','support_weight':'5/4',
        'limiting_influence_row_upper':'128/225',
        'scope':'Exact source coefficient and rational return of the full written analytic bounds; no vacuum sampling or spectral truncation.'}


def heat_bath_gap_checks():
    r15=Q(9,64);r4=Q(7,64)
    ck('heat-bath-actual-coupling-domain',Q(1)/(4*15**2)==Q(1,900))
    ck('heat-bath-source-ball-fifteen',Q(625,8)*Q(1,900)+Q(8,3)*r15*r15==Q(643,4608)<r15)
    ck('heat-bath-source-contraction-fifteen',Q(16,3)*r15==Q(3,4)<1)
    ck('heat-bath-source-series-fifteen',Q(2500,3)*Q(1,900)==Q(25,27)<1)
    ck('heat-bath-actual-influence-fifteen',Q(65536,9375)*r15==Q(3072,3125)<1)
    ck('heat-bath-complete-drift-fifteen',Q(384,125)*r15==Q(54,125))
    ck('heat-bath-source-ball-four',Q(625,8)*Q(1,1024)+Q(8,3)*r4*r4==Q(2659,24576)<r4)
    ck('heat-bath-source-contraction-four',Q(16,3)*r4==Q(7,12))
    ck('heat-bath-actual-influence-four',Q(65536,9375)*r4==Q(7168,9375)<1)
    ck('original-score-conditional-oscillation-fifteen',32*Q(22,7)*Q(1,900)==Q(176,1575))
    ck('original-score-conditional-oscillation-four',32*Q(22,7)*Q(1,1024)==Q(11,112))
    ck('full-physical-gap-rational-fifteen',Q(3,4)*(1-Q(3072,3125))*(1-Q(176,1575))==Q(74147,6562500)>Q(1,100))
    ck('full-physical-gap-rational-four',Q(3,4)*(1-Q(7168,9375))*(1-Q(11,112))==Q(222907,1400000)>Q(3,20))
    ck('original-gap-energy-factor-fifteen',Q(1,100)*2==Q(1,50))
    ck('original-gap-energy-factor-four',Q(3,20)*2==Q(3,10))
    neg('unproved-domain-fourteen',Q(1)/(4*14**2)<=Q(1,900))
    neg('conditional-projection-constant-omitted',Q(3,4)==1)
    # Original conditional probabilities on a genuinely coupled four-point law.
    labels=list(itertools.product(range(2),repeat=2));weights=[Q(10),Q(11),Q(11),Q(10)]
    def projection(site):
        rows=[]
        for x in labels:
            keep=[j for j,y in enumerate(labels) if all(y[k]==x[k] for k in range(2) if k!=site)]
            mass=sum(weights[j] for j in keep)
            rows.append([weights[j]/mass if j in keep else Q(0) for j in range(4)])
        return M.rows(rows)
    P0=projection(0);P1=projection(1)
    G=M.rows([[weights[i] if i==j else 0 for j in range(4)] for i in range(4)])
    one=M.rows([[1],[1],[1],[1]])
    vac=one@(one.T@G).scale(Q(1,42))
    centered=G-G@vac
    generator=eye(4).scale(2)-P0-P1
    ck('actual-conditional-projector-zero',P0@P0==P0 and P0.T@G==G@P0 and P0@one==one)
    ck('actual-conditional-projector-one',P1@P1==P1 and P1.T@G==G@P1 and P1@one==one)
    ck('original-conditional-influence-measured',abs(P0.at(0,0)-P0.at(1,1))==Q(1,21))
    ck('original-raw-vacuum-projection',vac@vac==vac and vac.T@G==G@vac and one.T@G@one==M.rows([[42]]))
    ck('actual-heat-bath-weighted-self-adjointness',generator.T@G==G@generator and generator@one==zero(4,1))
    ck('actual-noncommuting-conditional-gap',psd(G@generator-centered.scale(Q(20,21))))
    ck('actual-conditional-gap-annihilator',generator@(generator-eye(4).scale(Q(20,21)))@(generator-eye(4).scale(Q(22,21)))@(generator-eye(4).scale(2))==zero(4,4))
    neg('commute-original-conditional-projections',P0@P1==P1@P0)
    neg('drop-mean-projector-in-heat-bath-gap',psd(G@generator-G.scale(Q(20,21))))
    F=2*old.u[0]
    energy=old.integrate(sum((old.X(F,0,i)**2 for i in range(3)),old.P(0)))
    ck('original-single-link-Haar-Poincare-factor',old.integrate(F*F)==1 and old.integrate(F)==0 and energy==Q(3,4))
    ck('original-Haar-Poincare-sharp-fundamental',Q(4,3)*energy==1)
    for N in range(1,9):
        q=Q(3,7)
        ck('complete-Poisson-oscillation-rate-'+str(N),N*(1-(1-Q(1,N)+q/N))==1-q)
    # Final actual-vacuum zero-shift return with the stronger proved floor.
    x=Q(1,10**8);N=10**30;rad=1-Q(2500,3)*x
    lower=Q(math.isqrt(rad.numerator*N*N//rad.denominator),N)
    ck('heat-bath-outward-source-radius',lower**2<=rad<(lower+Q(1,N))**2)
    r=Q(3,16)*(1-lower);q=Q(65536,9375)*r;pi=Q(355,113);beta=32*pi*x
    d=Q(3,4)*(1-q)/(1+old.exp_minus_one_upper(beta))
    ck('actual-heat-bath-gap-safe-lower',d>Q(74999514999,10**11))
    delta=old.exp_minus_one_upper(1024*pi*x);eta=old.exp_minus_one_upper(1088*pi*x)
    zs=Q(196,4563);ms=Q(8,39);zm=Q(64,39);lz=Q(80,13);A=Q(256,9)
    hz=x*(eta*lz/2+16*x*zm);rz=8*A*x*x+16*x*x*lz+64*x*hz;nz=old.sqrt_upper((1+delta)*zs)
    terms=[delta*x*x*old.sqrt_upper(zs),16*x**3*zm*lz,16*x*x*eta*eta*zm,
           16*A*x**3*nz,4*hz*hz,128*x*x*nz*hz,rz*rz/d]
    em=sum(terms)/(x*x)
    ez=delta*zs+(eta*zm)**2+2*nz*rz/(d*x)+(rz/(d*x))**2
    ck('actual-heat-bath-response-interval',em<Q(94,10**7))
    ck('actual-heat-bath-restored-metric-interval',ez<Q(319,10**8))
    ck('actual-heat-bath-canonical-quotient-cost',rz*rz/(d*x*x)<Q(142,10**13))
    ck('original-final-running-coupling-domain',Q(1,15)**2/4==Q(1,900))
    return {'proved_coupling_domain':{'g_squared_min':'15','xi_max':'1/900','stronger_subdomain_g_min':'4'},
        'full_original_gap':'kappa (3/4) [1-(65536/9375) r_xi] exp(-32 pi xi)',
        'r_xi':'(3/16)[1-sqrt(1-(2500/3)xi)]',
        'all_domain_safe_gap':'kappa/100 = g^2/(50a)',
        'all_domain_rational_gap_coefficient':'74147/6562500',
        'g_at_least_four_safe_gap':'3 kappa/20 = 3g^2/(10a)',
        'g_at_least_four_rational_gap_coefficient':'222907/1400000',
        'actual_xi':str(x),'actual_g_squared':'5000','actual_kappa':'10000/a',
        'actual_gap_lower_rational':str(d),'actual_gap_safe_lower_coefficient':'0.74999514999',
        'response_center':str(ms),'response_radius_upper':old.dec(em,24),'response_certified_radius':'0.0000094',
        'response_original_factor':'kappa xi^2',
        'restored_center':str(zs),'restored_radius_upper':old.dec(ez,24),'restored_certified_radius':'0.00000319',
        'restored_original_factor':'xi^2',
        'quotient_plus_correction_radius_upper':old.dec(rz*rz/(d*x*x),24),
        'quotient_plus_correction_certified_radius':'0.0000000000142',
        'quotient_plus_correction_original_factor':'kappa xi^2',
        'full_gap_enclosure':['0.74999514999 kappa','(3+5/10^13) kappa'],
        'scope':'Actual-vacuum source, full-domain conditional comparison and original zero-shift error bounds; no numerical vacuum samples or finite-spin replacement.'}


def no_duplicate_keys(pairs):
    out={}
    for k,v in pairs:
        require(k not in out,'duplicate-json-key:'+k);out[k]=v
    return out

def load(path):return json.loads(path.read_text(),object_pairs_hook=no_duplicate_keys)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--verify-receipt',type=Path)
    ap.add_argument('--candidate-state',type=Path)
    args=ap.parse_args()
    representation_and_support();fixed_point_constants();coordinate_gamma2()
    exact_zero_shift_polynomials();raw_matrix_residuals();nums=rational_evaluation();volume_limit_checks();extensive_energy_checks();sharp=optimized_domain_checks();hb=heat_bath_gap_checks()
    statepath=args.candidate_state or HERE/'state.json'
    state=load(statepath)
    require(state.get('target')=='four-dimensional continuum Yang-Mills mass gap','wrong-target')
    require(state.get('proved_coupling_domain')=={'g_squared_min':'15','xi_max':'1/900','stronger_subdomain_g_min':'4'},'wrong-proved-domain')
    require(state.get('continuum_gap_established') is False,'unsupported-continuum-promotion')
    require(state.get('actual_zero_shift_response_enclosed') is True,'missing-actual-response')
    require(state.get('fixed_spacing_volume_limit')=='unique vacuum and dynamics for g^2>=15','wrong-volume-limit-scope')
    for name in ('RESEARCH_NOTE.md','VOLUME_LIMIT.md','OPTIMIZED_DOMAIN.md','HEAT_BATH_GAP.md','verify.py'):
        require((HERE/name).is_file(),'missing-current-source:'+name)
    payload={'schema':'ym-uniform-gap-zero-shift-v1','exact_checks':passed,'negative_controls':negative,
        'certified_evaluation':nums,'sharpened_evaluation':sharp,'heat_bath_evaluation':hb,
        'source_sha256':{name:sha(HERE/name) for name in ('RESEARCH_NOTE.md','VOLUME_LIMIT.md','OPTIMIZED_DOMAIN.md','HEAT_BATH_GAP.md','verify.py')},
        'state_sha256':sha(statepath),
        'predecessor_sha256':{str(p.relative_to(YM)):h for p,h in EXPECTED.items()},
        'scope':'Finite exact algebra and rational evaluation of the written analytic estimates. No formal or independent proof audit, vacuum sampling, or remote CI run.'}
    text=json.dumps(payload,sort_keys=True,indent=2)+'\n'
    if args.verify_receipt:
        receipt=load(args.verify_receipt)
        require(receipt==payload and args.verify_receipt.read_text()==text,'receipt-mismatch')
    if args.output:args.output.write_text(text)
    sys.stdout.write(text)

if __name__=='__main__':
    try:main()
    except (ValueError,OSError,json.JSONDecodeError) as exc:
        print('FAIL: '+str(exc),file=sys.stderr);sys.exit(1)
