#!/usr/bin/env python3
"""Exact fixtures and research-record validation; no analytic proof certification."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent

class Failure(Exception):
    def __init__(self, code: str):
        self.code = code
        super().__init__(code)

def require(ok: bool, code: str) -> None:
    if not ok:
        raise Failure(code)

def unique_object(pairs):
    out = {}
    for key, value in pairs:
        require(key not in out, 'duplicate-json-key')
        out[key] = value
    return out

def load(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=unique_object)

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

@dataclass(frozen=True)
class M:
    n: int
    m: int
    data: tuple
    @staticmethod
    def rows(rows, columns=None):
        n = len(rows)
        m = len(rows[0]) if n else (0 if columns is None else columns)
        require(all(len(row) == m for row in rows), 'matrix-row-shape')
        return M(n, m, tuple(F(x) for row in rows for x in row))
    def at(self, i, j):
        return self.data[i*self.m+j]
    def to_rows(self):
        return [[self.at(i,j) for j in range(self.m)] for i in range(self.n)]
    @property
    def T(self):
        return M(self.m, self.n, tuple(self.at(i,j) for j in range(self.m) for i in range(self.n)))
    def __matmul__(self, other):
        require(self.m == other.n, 'matrix-product-shape')
        return M(self.n, other.m, tuple(sum((self.at(i,k)*other.at(k,j) for k in range(self.m)),F(0)) for i in range(self.n) for j in range(other.m)))
    def __add__(self, other):
        require((self.n,self.m)==(other.n,other.m), 'matrix-add-shape')
        return M(self.n,self.m,tuple(a+b for a,b in zip(self.data,other.data)))
    def __sub__(self, other):
        return self + other.scale(-1)
    def scale(self, scalar):
        return M(self.n,self.m,tuple(F(scalar)*a for a in self.data))
    def inverse(self):
        require(self.n == self.m, 'inverse-square')
        n = self.n
        a = [row+[F(i==j) for j in range(n)] for i,row in enumerate(self.to_rows())]
        for c in range(n):
            pivot = next((r for r in range(c,n) if a[r][c]),None)
            require(pivot is not None, 'inverse-singular')
            a[c],a[pivot]=a[pivot],a[c]
            v=a[c][c]; a[c]=[x/v for x in a[c]]
            for r in range(n):
                if r != c:
                    v=a[r][c]; a[r]=[x-v*y for x,y in zip(a[r],a[c])]
        return M.rows([row[n:] for row in a],columns=n)
    def rank(self):
        a=self.to_rows(); row=0
        for c in range(self.m):
            p=next((r for r in range(row,self.n) if a[r][c]),None)
            if p is None: continue
            a[row],a[p]=a[p],a[row]; v=a[row][c]; a[row]=[x/v for x in a[row]]
            for r in range(self.n):
                if r != row:
                    v=a[r][c]; a[r]=[x-v*y for x,y in zip(a[r],a[row])]
            row+=1
            if row == self.n: break
        return row

def eye(n):
    return M.rows([[int(i==j) for j in range(n)] for i in range(n)],columns=n)

def diag(v):
    return M.rows([[x if i==j else 0 for j in range(len(v))] for i,x in enumerate(v)])

def section(Q, L):
    W=(L@Q.inverse()@L.T).inverse()
    return Q.inverse()@L.T@W, W

def conditional(weights, groups):
    masses=[sum((weights[i] for i in group),F(0)) for group in groups]
    L=M.rows([[weights[i]/masses[j] if i in group else 0 for i in range(len(weights))] for j,group in enumerate(groups)])
    J=M.rows([[int(i in group) for group in groups] for i in range(len(weights))])
    return L,J,masses

def kkt_section(Q,L):
    # Independently assemble the constrained system Qx-L*nu=0, Lx=y.
    n,r=Q.n,L.n
    A=M.rows([[Q.at(i,j) for j in range(n)]+[-L.at(j,i) for j in range(r)] for i in range(n)] + [[L.at(i,j) for j in range(n)]+[0]*r for i in range(r)])
    rhs=M.rows([[0]*r for _ in range(n)]+eye(r).to_rows(),columns=r)
    return M.rows((A.inverse()@rhs).to_rows()[:n],columns=r)

def validate(state):
    require(state.get('schema')=='ym-research-control-v1','state-schema')
    require(state.get('target')=='4D interacting Yang-Mills existence and physical mass gap','target-retained')
    require(state.get('continuum_gap_proved') is False,'unsupported-continuum-claim')
    require(state.get('gauge_group')=='SU(2)','gauge-scope')
    require(set(state.get('constants',[]))=={'a_n','g_n','kappa_n','xi_n','b','E_0,n'},'physical-constants')
    sources=state.get('sources',[])
    ids=[s['id'] for s in sources]
    require(len(ids)==len(set(ids)) and len(ids)>0,'source-ids')
    for source in sources:
        require(re.fullmatch(r'[0-9a-f]{40}',source.get('blob','')) is not None,'source-pin')
        require(bool(source.get('read_scope')),'source-review-scope')
        require(source.get('review') in {'proof-read','partial-proof-read','validator-read','orientation-only'},'source-review-kind')
        path=Path(source['path'])
        require(not path.is_absolute() and '..' not in path.parts,'source-path')
    claims=state.get('claims',[]); cids=[c['id'] for c in claims]
    require(len(cids)==len(set(cids)) and bool(cids),'claim-ids')
    graph={c['id']:c.get('depends',[]) for c in claims}
    for claim in claims:
        require(claim.get('scope')=='finite-regulator','unsupported-scope')
        require(claim.get('evidence')=='written-proof-with-separate-fixtures','evidence-upgrade')
        require(claim.get('analytic_machine_checked') is False,'analytic-check-upgrade')
        require(re.fullmatch(r'L[0-9]+',claim.get('proof_anchor','')) is not None,'proof-anchor')
        require('('+claim['proof_anchor']+')' in (ROOT/'RESEARCH_NOTE.md').read_text(),'proof-anchor-body')
        require(bool(claim.get('quantity')) and bool(claim.get('parameter_dependence')),'quantity-and-parameters')
        require(all(i in ids for i in claim.get('sources',[])),'dangling-source')
        require(all(i in cids for i in graph[claim['id']]),'dangling-claim')
    seen=set(); active=set()
    def visit(v):
        require(v not in active,'dependency-cycle')
        if v in seen:return
        active.add(v)
        for w in graph[v]:visit(w)
        active.remove(v);seen.add(v)
    for v in graph:visit(v)
    for tr in state.get('transfers',[]):
        require(tr.get('source') in ids,'transfer-source')
        require(bool(tr.get('map')) and bool(tr.get('metric')) and bool(tr.get('target')),'transfer-map')
        require(tr.get('status') in {'instantiated','regression-only','candidate-not-imported'},'transfer-scope')
    require(state.get('next_quantity') and state.get('next_calculation'),'continuation-state')
    return True

def compare_intake(state,new):
    old={p['key']:p['revision'] for p in state['watched_revisions']}
    now={p['key']:p['revision'] for p in new['watched_revisions']}
    changed=sorted(key for key,value in old.items() if now.get(key)!=value)
    require(not changed,'source-drift:'+','.join(changed))

def run(state):
    passed=[]; rejected=[]
    def ck(name,truth):
        require(bool(truth),'fixture:'+name);passed.append(name)
    def neg(name,action,code):
        try:action()
        except Failure as exc:
            require(exc.code==code,'wrong-negative-failure:'+name)
            rejected.append({'name':name,'rejected_by':code,'false_claim_accepted':False})
        else:raise Failure('false-claim-accepted:'+name)
    validate(state);passed.append('research-record-structure')
    w=[F(i,21) for i in range(1,7)];G=diag(w)
    E= [[F(0) for _ in w] for _ in w]
    for i in range(6):
        for j in range(i+1,6):
            c=F(i+j+1,7);E[i][i]+=c;E[j][j]+=c;E[i][j]-=c;E[j][i]-=c
    E=M.rows(E);s=F(2,3);Q=E+G.scale(s)
    L,J,m=conditional(w,[[0,1],[2,3],[4,5]])
    L2,J2,m2=conditional(m,[[0,1],[2]])
    S,W=section(Q,L);S2,W2=section(W,L2);Sd,Wd=section(Q,L2@L)
    ck('conditional-right-inverse',L@J==eye(3))
    ck('conditional-adjoint-raw-measure',J.T@G==diag(m)@L)
    ck('conditional-state-orthogonality',J.T@G@(eye(6)-J@L)==M(3,6,(F(0),)*18))
    ck('minimum-section-independent-kkt',S==kkt_section(Q,L))
    ck('minimum-section-right-inverse',L@S==eye(3))
    ck('minimum-section-energy-gram',S.T@Q@S==W)
    ck('composite-minimum-section',Sd==S@S2)
    ck('composite-minimum-energy',Wd==W2)
    N=M.rows([[-w[1]/w[0],0,0],[1,0,0],[0,-w[3]/w[2],0],[0,1,0],[0,0,-w[5]/w[4]],[0,0,1]])
    ck('kernel-basis-exact',L@N==M(3,3,(F(0),)*9))
    Hn=N.T@Q@N; Gn=N.T@G@N; B=N.T@E@J
    Hs=N@Hn.inverse()@B
    ck('score-coupling-minimum-section-sign',S==J-Hs)
    ck('score-response-schur-form',W==J.T@Q@J-B.T@Hn.inverse()@B)
    ck('restored-state-metric-derivative',S.T@G@S==diag(m)+B.T@Hn.inverse()@Gn@Hn.inverse()@B)
    X=M.rows([[1,0,2],[0,1,1],[1,1,0],[2,-1,1],[0,2,-1],[1,3,2]])
    Z=L@X;R=X-S@Z
    ck('full-rectangular-residual-gram',R.T@Q@R==X.T@Q@X-Z.T@W@Z)
    ck('full-state-gram-including-mixed',X.T@G@X==Z.T@S.T@G@S@Z+Z.T@S.T@G@R+R.T@G@S@Z+R.T@G@R)
    ck('canonical-kernel-correction',X-S@Z==(X-J@Z)+(J-S)@Z)
    T=eye(6).to_rows();T[0][0]=F(2);T[0][1]=F(1);T[2][4]=F(-2,3);T=M.rows(T)
    St,Wt=section(T.T@Q@T,L@T)
    ck('raw-frame-section-inverse',St==T.inverse()@S)
    ck('raw-frame-observation-energy',Wt==W)
    ck('raw-frame-state-metric',St.T@(T.T@G@T)@St==S.T@G@S)
    Sempty,Wempty=section(Q,M(0,6,()))
    ck('empty-observation-retained',Sempty==M(6,0,()) and Wempty==M(0,0,()))
    # Conditional variance fixture: scores and the same probability measure retained.
    y=M.rows([[i*i-3*i+1] for i in range(6)]); mean=L@y; score=y-J@mean
    ck('score-conditional-mean-zero',L@score==M(3,1,(F(0),)*3))
    ck('score-integrated-fisher-identity',score.T@G@score==y.T@G@y-mean.T@diag(m)@mean)
    h=N@M.rows([[1],[-2],[3]])
    for group in range(3):
        inds=[2*group,2*group+1]
        Eh2=sum(w[i]*h.at(i,0)**2 for i in inds)/m[group]
        Es2=sum(w[i]*score.at(i,0)**2 for i in inds)/m[group]
        Ehs=sum(w[i]*h.at(i,0)*score.at(i,0) for i in inds)/m[group]
        ck('conditional-cauchy-schwarz-'+str(group),Ehs**2<=Eh2*Es2)
    for b in (1,2,4,8,16):
        for xi in (F(1,128),F(1,64),F(1),F(7)):
            eta=[min(2*F(2+j%3)*xi,F(16,3)*(2+j%3)**2*xi**2) for j in range(b)]
            ck('local-score-coefficient-'+str(b)+'-'+str(xi),F(4,b)*sum(eta)<=32*xi)
    # Observed-iterate test on a declared polynomial algebra, not a YM Hamiltonian.
    A=M.rows([[0,0,0,0],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
    row=M.rows([[0,0,0,1]]); rows=[]; power=eye(4)
    for _ in range(4):rows.extend((row@power).to_rows());power=power@A
    O=M.rows(rows)
    ck('delayed-observation-complete-stack',row.rank()==1 and O.rank()==4)
    row2=M.rows([[0,0,1,0]]);rows=[];power=eye(4)
    for _ in range(4):rows.extend((row2@power).to_rows());power=power@A
    ck('permanent-kernel-retained',M.rows(rows).rank()==3 and M.rows(rows)@M.rows([[0],[0],[0],[1]])==M(4,1,(F(0),)*4))
    # The Collatz specialization fiber from the inspected exact source.
    Xu=lambda q:F(1,2)+q/F(32)
    Xv=lambda q:F(1,8)+q/F(16)+q*q/F(32)
    for q in map(F,(-2,0,1,3,5)):
        ck('collatz-polynomial-fiber-'+str(q),Xv(q)-Xu(q)==(q-3)*(q+4)/32)
    ck('collatz-killed-polynomial-retained',Xu(F(3))==Xv(F(3))==F(19,32) and Xu(F(0))!=Xv(F(0)))
    # Individually named false formulas: exact inequality is their rejection witness.
    neg('fixed-section-as-energy-minimum',lambda:require(S==J,'fixed-section'), 'fixed-section')
    neg('drop-state-mixed-entries',lambda:require(X.T@G@X==Z.T@S.T@G@S@Z+R.T@G@R,'state-cross-term'),'state-cross-term')
    neg('naive-middle-form-in-tower',lambda:require(section(J.T@Q@J,L2)[0]==S2,'middle-form'),'middle-form')
    neg('replace-raw-norm-by-identity',lambda:require(section(E+eye(6).scale(s),L)[0]==S,'raw-metric'),'raw-metric')
    # A rare conditional fiber carries a centered score +5,-5; the other has score 0.
    rare_weights=[F(1,100),F(1,100),F(49,50)]
    rare_L,rare_J,rare_m=conditional(rare_weights,[[0,1],[2]])
    rare_score=M.rows([[5],[-5],[0]])
    rare_Gamma=rare_L@M.rows([[25],[25],[0]])
    rare_integral=sum(rare_m[i]*rare_Gamma.at(i,0) for i in range(2))
    ck('rare-fiber-score-mean-zero',rare_L@rare_score==M(2,1,(F(0),)*2))
    ck('rare-fiber-integrated-versus-pointwise',rare_integral==F(1,2) and rare_Gamma.at(0,0)==25)
    neg('integrated-score-as-pointwise-bound',lambda:require(rare_Gamma.at(0,0)<=rare_integral,'integral-to-supremum'),'integral-to-supremum')
    neg('one-step-kernel-as-permanent',lambda:require(row.rank()==O.rank(),'observed-iterates'),'observed-iterates')
    neg('specialization-recovers-history',lambda:require(Xu(F(0))==Xv(F(0)),'specialization-fiber'),'specialization-fiber')
    neg('delete-kernel-energy-coupling',lambda:require(J.T@E@N==M(3,3,(F(0),)*9),'energy-cross-term'),'energy-cross-term')
    neg('duplicate-json-key',lambda:json.loads('{"a":1,"a":2}',object_pairs_hook=unique_object),'duplicate-json-key')
    mutations=[('source-pin',lambda d:d['sources'][0].update(blob='bad'),'source-pin'),('evidence-promotion',lambda d:d['claims'][0].update(evidence='finite-fixture-only'),'evidence-upgrade'),('continuum-promotion',lambda d:d.update(continuum_gap_proved=True),'unsupported-continuum-claim'),('missing-physical-factor',lambda d:d.update(constants=['a_n']),'physical-constants'),('dangling-claim',lambda d:d['claims'][0].update(depends=['invented']),'dangling-claim'),('missing-proof-anchor',lambda d:d['claims'][0].update(proof_anchor='L9999'),'proof-anchor-body'),('path-escape',lambda d:d['sources'][0].update(path='../secret'),'source-path')]
    for name,change,code in mutations:
        d=copy.deepcopy(state);change(d);neg(name,lambda d=d:validate(d),code)
    fresh={'watched_revisions':copy.deepcopy(state['watched_revisions'])}
    compare_intake(state,fresh);passed.append('unchanged-source-intake')
    fresh['watched_revisions'][0]['revision']='0'*40
    neg('changed-peer-head',lambda:compare_intake(state,fresh),'source-drift:'+state['watched_revisions'][0]['key'])
    return {'schema':'ym-control-execution-v1','status':'passed','arithmetic':'exact rational; Python standard library','checks':passed,'check_count':len(passed),'negative_controls':rejected,'negative_count':len(rejected),'analytic_proof_checked':False,'lean_run_performed':False,'continuum_gap_proved':False,'fixture_scope':'finite weighted-graph, matrix, polynomial and metadata fixtures; not evaluated Yang-Mills vacuum integrals'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--validate-state',type=Path)
    parser.add_argument('--source-cache',type=Path)
    parser.add_argument('--compare-intake',type=Path)
    parser.add_argument('--verify-receipt',type=Path)
    args=parser.parse_args()
    state_path=args.validate_state or ROOT/'state.json'
    state=load(state_path);validate(state)
    if args.compare_intake:compare_intake(state,load(args.compare_intake))
    report=run(state)
    report['checked_state_sha256']=sha(state_path)
    report['local_inputs']={str(p.relative_to(ROOT.parent)):sha(p) for p in [ROOT/'RESEARCH_NOTE.md',ROOT/'WORKFLOW.md',ROOT/'state.json',ROOT/'check.py',ROOT.parent/'AGENTS.md']}
    parent=ROOT.parent/'continuations/20260914-vacuum-refinement-infrared/RESEARCH_NOTE.md'
    if parent.exists():
        require(blob(parent)=='0d79c733ff6209c991dd2b52474b1e399dd812db','parent-source-drift')
        report['parent_source']='pinned bytes matched'
    else:report['parent_source']='not in local package; not checked'
    report['cached_sources']=[]
    if args.source_cache:
        for source in state['sources']:
            path=args.source_cache/source['id']
            status='unavailable'
            if path.is_file():
                require(blob(path)==source['blob'],'cached-source-drift:'+source['id']);status='matched'
            report['cached_sources'].append({'id':source['id'],'status':status})
    if args.verify_receipt:
        require(report==load(args.verify_receipt),'execution-receipt-drift')
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=='__main__':
    try:main()
    except (Failure,ValueError,OSError,KeyError,TypeError) as exc:
        print(json.dumps({'status':'failed','error':str(exc),'analytic_proof_checked':False}),file=sys.stderr)
        sys.exit(1)
