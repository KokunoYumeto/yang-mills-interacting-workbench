#!/usr/bin/env python3
"""Exact raw-matrix response checks. Written analytic proofs are not certified."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sys
from fractions import Fraction as Q

HERE=Path(__file__).resolve().parent
YM=HERE.parents[1]
PARENT=YM/'research-control/check.py'

def need(ok, code):
    if not ok:
        raise ValueError(code)

def blob(path):
    data=path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

need(blob(PARENT)=='6c003b72d4447461b82dc696ec8f707438e3c7ab','parent-checker-drift')
need(blob(YM/'research-control/RESEARCH_NOTE.md')=='d138482ac7b40017560cef5a93b21ada4440ce13','parent-proof-drift')
spec=importlib.util.spec_from_file_location('ym_exact_parent',PARENT)
parent=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=parent
spec.loader.exec_module(parent)
M=parent.M; eye=parent.eye; diag=parent.diag

def zero(n,m): return M(n,m,(Q(0),)*(n*m))
def det(A):
    need(A.n==A.m,'det-square')
    n=A.n; ans=Q(0)
    for perm in itertools.permutations(range(n)):
        term=Q((-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n)))
        for i,j in enumerate(perm): term*=A.at(i,j)
        ans+=term
    return ans

def minor(A,rows,cols):
    return M.rows([[A.at(i,j) for j in cols] for i in rows],columns=len(cols))

def adj_inverse(A):
    d=det(A);need(d!=0,'adjugate-singular')
    n=A.n
    return M.rows([[(-1)**(i+j)*det(minor(A,[k for k in range(n) if k!=j],
        [k for k in range(n) if k!=i]))/d for j in range(n)] for i in range(n)])

def psd(A):
    if A.n!=A.m or A!=A.T:return False
    for size in range(1,A.n+1):
        for ix in itertools.combinations(range(A.n),size):
            if det(minor(A,ix,ix))<0:return False
    return True

def block(A,B,C,D):
    need(A.n==B.n and C.n==D.n and A.m==C.m and B.m==D.m,'block-shape')
    return M.rows([a+b for a,b in zip(A.to_rows(),B.to_rows())]+
                  [a+b for a,b in zip(C.to_rows(),D.to_rows())],columns=A.m+B.m)

def power(A,n):
    need(isinstance(n,int) and n>=0,'power-domain')
    P=eye(A.n)
    for _ in range(n):P=P@A
    return P

def cat_cols(A,B):return M.rows([a+b for a,b in zip(A.to_rows(),B.to_rows())],columns=A.m+B.m)
def cat_rows(A,B):return M.rows(A.to_rows()+B.to_rows(),columns=A.m)
def cm(A):return A,zero(A.n,A.m)
def ca(A,B):return A[0]+B[0],A[1]+B[1]
def cs(A,B):return A[0]-B[0],A[1]-B[1]
def cp(A,B):return A[0]@B[0]-A[1]@B[1],A[0]@B[1]+A[1]@B[0]
def ct(A):return A[0].T,A[1].T.scale(-1)
def cscale(A,z):
    a,b=z
    return A[0].scale(a)-A[1].scale(b),A[0].scale(b)+A[1].scale(a)
def crecip(z):
    a,b=z;need(a*a+b*b>0,'complex-zero')
    return a/(a*a+b*b),-b/(a*a+b*b)
def cresolvent(D,z):
    x,y=z;B=D-eye(D.n).scale(x)
    Qinv=(B@B+eye(D.n).scale(y*y)).inverse()
    return B@Qinv,Qinv.scale(y)

def stable_json(value):return json.dumps(value,sort_keys=True,indent=2)+'\n'
def reject_duplicates(pairs):
    out={}
    for key,value in pairs:
        need(key not in out,'duplicate-json-key');out[key]=value
    return out

def load(path):return json.loads(path.read_text(),object_pairs_hook=reject_duplicates)

def run():
    passed=[];negative=[]; numerical=[]
    def ck(name,truth):
        need(name not in passed,'duplicate-check-name')
        need(bool(truth),'check:'+name);passed.append(name)
    def neg(name,truth,code):
        try:need(bool(truth),code)
        except ValueError as exc:
            need(str(exc)==code,'wrong-negative:'+name)
            negative.append({'name':name,'rejected_by':code,'false_claim_accepted':False})
        else:raise ValueError('false-claim-accepted:'+name)

    # Declared exact matrices, NOT numerically evaluated Yang-Mills vacuum data.
    D=M.rows([[3,1,0],[1,4,1],[0,1,2]])
    G=M.rows([[2,1],[1,3]])
    W=M.rows([[1,2],[0,1],[2,-1]])
    K0=W.T@D.inverse()@W+M.rows([[2,1],[1,1]])
    raw=block(G,zero(2,3),zero(3,2),eye(3))
    energy=block(K0,W.T.scale(-1),W.scale(-1),D)
    generator=raw.inverse()@energy
    ck('positive-original-state-gram',psd(G) and det(G)>0)
    ck('positive-kernel-operator',psd(D) and det(D)>0)
    ck('positive-coupled-energy',psd(energy))
    ck('raw-metric-self-adjointness',generator.T@raw==raw@generator)
    ck('independent-inverse-kernel',D.inverse()==adj_inverse(D))
    neg('euclidean-adjoint-for-raw-generator',generator.T==generator,'raw-adjoint-required')
    ck('inverse-energy-budget',psd(K0-W.T@D.inverse()@W))

    V1=M.rows([[1],[1],[0]])
    V2=M.rows([[1,0],[1,2],[0,1]])
    V3=M.rows([[1,0,1],[1,2,0],[0,1,1]])
    for si,s in enumerate([Q(1,4),Q(2,3),Q(2)]):
        A=D+eye(3).scale(s);inv=A.inverse()
        exact=W.T@inv@W; F=K0+G.scale(s)-exact
        full_inverse=adj_inverse(energy+raw.scale(s))
        ck(f'full-block-resolvent-raw-gram-{si}',minor(full_inverse,[0,1],[0,1])==F.inverse())
        # i* resolvent i uses G on both sides, while the energy inverse is covariant.
        op_inverse=(generator+eye(5).scale(s)).inverse()
        ck(f'operator-resolvent-original-inclusion-{si}',G@minor(op_inverse,[0,1],[0,1])==G@F.inverse()@G)
        neg(f'drop-right-state-gram-{si}',G@minor(op_inverse,[0,1],[0,1])==G@F.inverse(),'right-gram-retained')
        previous=zero(2,2)
        for j,V in enumerate([zero(3,0),V1,V2,V3]):
            H=V.T@A@V;B=V.T@W
            X=H.inverse()@B;Y=V@X;R=W-A@Y
            lower=W.T@Y+Y.T@W-Y.T@A@Y
            ck(f'galerkin-normal-equation-{si}-{j}',V.T@R==zero(V.m,2))
            ck(f'residual-energy-identity-{si}-{j}',exact==lower+R.T@inv@R)
            ck(f'response-two-sided-{si}-{j}',psd(exact-lower) and psd(lower+(R.T@R).scale(1/s)-exact))
            ck(f'nested-trial-monotonicity-{si}-{j}',psd(lower-previous))
            ck(f'forcing-primitive-isometry-{si}-{j}',(A@V).T@inv@(A@V)==H)
            err=inv@W-Y
            ck(f'restored-state-error-{si}-{j}',err.T@err==R.T@inv@inv@R)
            metric=W.T@inv@inv@W
            eta=Q(1,3); rr=(R.T@R).scale(1/(s*s));yy=Y.T@Y
            lo=yy.scale(1-eta)-rr.scale(1/eta-1)
            hi=yy.scale(1+eta)+rr.scale(1+1/eta)
            ck(f'restored-state-two-sided-{si}-{j}',psd(metric-lo) and psd(hi-metric))
            if j==1 and si==0:
                neg('omit-residual-energy',exact==lower,'nonzero-residual-retained')
                neg('omit-restored-state-cross-terms',metric==Y.T@Y+err.T@err,'restored-mixed-entries')
                neg('replace-trial-state-gram',H==V.T@D@V+eye(V.m).scale(s),'trial-state-gram')
                numerical.append({'s':str(s),'trial':'(1,1,0)^T','response_exact':[[str(x) for x in row] for row in exact.to_rows()],
                    'lower':[[str(x) for x in row] for row in lower.to_rows()],
                    'upper':[[str(x) for x in row] for row in (lower+(R.T@R).scale(1/s)).to_rows()]})
            previous=lower
        ck(f'complete-trial-exact-{si}',previous==exact)

    # Exact finite moment construction and its full singular solution fiber.
    s=Q(2,3);A=D+eye(3).scale(s)
    N=[W.T@power(D,j)@W for j in range(5)]
    H=block(N[1]+N[0].scale(s),N[2]+N[1].scale(s),N[2]+N[1].scale(s),N[3]+N[2].scale(s))
    B=cat_rows(N[0],N[1]);Z=cat_cols(W,D@W)
    C=cat_rows(N[1]+N[0].scale(s),N[2]+N[1].scale(s))
    J2=block(N[2]+N[1].scale(2*s)+N[0].scale(s*s),N[3]+N[2].scale(2*s)+N[1].scale(s*s),
        N[3]+N[2].scale(2*s)+N[1].scale(s*s),N[4]+N[3].scale(2*s)+N[2].scale(s*s))
    ck('moment-energy-exact',H==Z.T@A@Z)
    ck('moment-shifted-cross-exact',C==Z.T@A@W)
    ck('moment-second-energy-exact',J2==Z.T@A@A@Z)
    ck('singular-moment-rank-retained',H.rank()==Z.rank()==3 and H.n==4)
    # First three actual columns form an invertible coordinate subfamily.
    Zfirst=minor(Z,[0,1,2],[0,1,2]);Y=A.inverse()@W
    X0=cat_rows(Zfirst.inverse()@Y,zero(1,2))
    ck('singular-normal-equation-literal-solution',H@X0==B and Z@X0==Y)
    kernel=cat_rows((Zfirst.inverse()@minor(Z,[0,1,2],[3])).scale(-1),eye(1))
    X1=X0+kernel@M.rows([[2,-3]])
    ck('singular-normal-equation-full-fiber',H@X1==B and Z@X1==Y and X0!=X1)
    rr=N[0]-C.T@X0-X0.T@C+X0.T@J2@X0
    ck('moment-residual-full-formula',rr==(W-A@Y).T@(W-A@Y))
    neg('unshifted-residual-cross-moments',rr==N[0]-B.T@X0-X0.T@B+X0.T@J2@X0,'shifted-cross-moments-required')
    try:H.inverse()
    except parent.Failure as exc:
        ck('singular-inverse-rejected-at-rank',exc.code=='inverse-singular')
    else:raise ValueError('singular-inverse-accepted')

    # Complex parameter checks in exact pairs of rational matrices.
    z=(Q(1,3),Q(2,3));w=(Q(-1,2),Q(3,4))
    def fl(z):
        res=cresolvent(D,z)
        F=cs(cs(cm(K0),cscale(cm(G),z)),cp(cp(cm(W.T),res),cm(W)))
        L=cp(res,cm(W));return F,L
    Fz,Lz=fl(z);Fw,Lw=fl(w)
    quotient=cscale(cs(Fz,ct(Fw)),crecip((z[0]-w[0],z[1]+w[1])))
    right=ca(cm(G),cp(ct(Lw),Lz))
    ck('complex-full-two-parameter-gram',cscale(quotient,(-1,0))==right)
    ck('complex-diagonal-imaginary-gram',Fz[1].scale(-1/z[1])==ca(cm(G),cp(ct(Lz),Lz))[0])
    ck('complex-lift-diagonal-gram-real',cp(ct(Lz),Lz)[1]==zero(2,2))
    neg('wrong-Weyl-imaginary-sign',Fz[1].scale(1/z[1])==ca(cm(G),cp(ct(Lz),Lz))[0],'upper-half-plane-sign')
    wrong=cscale(cs(Fz,Fw),crecip((z[0]-w[0],z[1]+w[1])))
    neg('omit-parameter-adjoint',cscale(wrong,(-1,0))==right,'parameter-conjugation')

    # Source SR6 instantiated with the actual shifted resolvents.
    sigma=Q(2);Tsigma=(D+eye(3).scale(sigma)).inverse()
    for s in [Q(1,4),Q(1),sigma]:
        X=(D+eye(3).scale(s)).inverse();H=(Tsigma).scale(sigma-s);theta=1-s/sigma
        ck('source-resolvent-equation-'+str(s),(eye(3)-H)@X==Tsigma)
        exact=W.T@X@W
        P=zero(3,3)
        for n in range(5):
            P=P+power(H,n)@Tsigma
            err=W.T@(X-P)@W
            ck(f'geometric-full-remainder-{s}-{n}',X-P==power(H,n+1)@X)
            ck(f'geometric-positive-error-{s}-{n}',psd(err))
            ck(f'geometric-energy-budget-{s}-{n}',psd(K0.scale(theta**(n+1))-err))
            ck(f'geometric-forcing-budget-{s}-{n}',psd((W.T@W).scale(theta**(n+1)/s)-err))
            if s==Q(1,4) and n==0:
                neg('wrong-geometric-exponent',X-P==power(H,n)@X,'N-plus-one-power')
                neg('omit-geometric-constant',P==zero(3,3),'geometric-constant-term')
    D0=diag([Q(0),Q(2),Q(3)]);W0=M.rows([[0],[1],[2]])
    M00=W0.T@diag([Q(0),Q(1,2),Q(1,3)])@W0
    for s in [Q(1,10),Q(1),Q(2)]:
        ck('zero-energy-kernel-forcing-'+str(s),psd(M00-W0.T@(D0+eye(3).scale(s)).inverse()@W0))
    for b in [1,2,8]:
        for a in [Q(1,2),Q(2,3)]:
            for g2 in [Q(1,5),Q(2)]:
                kappa=2*g2/a;xi=1/(4*g2*g2)
                ck(f'physical-score-coefficient-{b}-{a}-{g2}',kappa*kappa*b*b*32*xi==32*b*b/(a*a))

    state=load(HERE/'state.json')
    need(state['schema']=='ym-coupled-response-v1','state-schema')
    need(state['continuum_gap_proved'] is False,'unsupported-continuum-claim')
    need(state['analytic_machine_checked'] is False,'unsupported-analytic-claim')
    text=(HERE/'RESEARCH_NOTE.md').read_text()
    for claim in state['claims']:
        need('('+claim['anchor']+')' in text,'missing-proof-anchor:'+claim['anchor'])
        need(claim['scope']=='finite-regulator','scope-promotion')
    ck('claim-anchors-and-scope',True)
    need(len(passed)==len(set(passed)),'duplicate-check-name')
    return {'schema':'ym-coupled-response-receipt-v1','status':'passed','checks':passed,'check_count':len(passed),
        'negative_controls':negative,'negative_count':len(negative),'sample':numerical,
        'analytic_machine_checked':False,'continuum_gap_proved':False,'new_lean_run':False,
        'fixture_scope':'Exact rational block/moment matrices, including complex spectral parameters; no Yang-Mills vacuum integrals evaluated.',
        'local_inputs':{p.name:sha(p) for p in [HERE/'RESEARCH_NOTE.md',HERE/'check.py',HERE/'state.json',HERE/'README.md']},
        'parent_checker_blob':blob(PARENT)}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--verify-receipt',type=Path)
    args=ap.parse_args();r=run()
    if args.verify_receipt:need(r==load(args.verify_receipt),'receipt-drift')
    print(stable_json(r),end='')
if __name__=='__main__':
    try:main()
    except (ValueError,parent.Failure,OSError,KeyError,TypeError) as exc:
        print(stable_json({'status':'failed','error':str(exc)}),file=sys.stderr,end='');sys.exit(1)
