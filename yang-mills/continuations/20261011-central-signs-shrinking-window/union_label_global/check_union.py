from fractions import Fraction as Q
from pathlib import Path
import hashlib,json,datetime,re
root=Path(__file__).parent

def subs(mask):
    t=mask
    while True:
        yield t
        if not t:break
        t=(t-1)&mask

def zeta(f):
    return [sum((f[t] for t in subs(a)),Q(0)) for a in range(len(f))]

def mobius(g):
    return [sum(((-1)**((s^a).bit_count())*g[a] for a in subs(s)),Q(0)) for s in range(len(g))]

def union(f,g):
    h=[Q(0) for _ in f]
    for a,fa in enumerate(f):
        for b,gb in enumerate(g):
            h[a|b]+=fa*gb
    return h

checks=0
n=6;size=1<<n
v=[Q(0)]+[Q(((s*13)%17)-8,4096) for s in range(1,size)]
f=[Q(0)]+[Q(((s*7)%19)-9,37) for s in range(1,size)]
f[-1]-=sum(f)
zv=zeta(v);zf=zeta(f)
assert mobius(zv)==v and mobius(zf)==f;checks+=2
uvf=union(v,f)
assert zeta(uvf)==[a*b for a,b in zip(zv,zf)];checks+=1
diag=[1-2*a for a in zv]
assert all(diag);checks+=1
sol=mobius([a/d for a,d in zip(zf,diag)])
action=[a-2*b for a,b in zip(sol,union(v,sol))]
assert action==f;checks+=1
assert sum(sol)==0 and zeta(sol)[-1]==0;checks+=1
# Keep every lower label: this kernel vector is nonzero both before and
# after applying the full inverse.
assert any(f[:-1]) and any(sol[:-1]);checks+=1
source=[Q(0) for _ in range(size)]
source[0b001111]=Q(2,7);source[0b111100]=Q(-3,11)
cum_source=zeta(source)
c=union(v,v);cum_c=zeta(c)
assert cum_c==[a*a for a in zv];checks+=1
energy=[2*a-b for a,b in zip(cum_source,cum_c)]
scalar_formula=[2*a-b for a,b in zip(source,mobius(energy))]
assert scalar_formula==c;checks+=1
assert zeta(mobius(energy))==energy;checks+=1
interval_checks=0
for s in range(size):
    for u in range(size):
        coeff=sum((-1)**((s^a).bit_count()) for a in subs(s) if u&a==u)
        assert coeff==int(u==s)
        interval_checks+=1
norm_checks=0
for n0 in range(1,9):
    count=1<<n0
    cn=Q(n0+1)*Q(2)**(n0-2)
    for e in range(n0):
        assert Q(2)**(n0-1)+(n0-1)*Q(2)**(n0-2)==cn
        for s in range(1,count):
            lhs=Q(2)**(n0-(s|(1<<e)).bit_count())
            rhs=(Q(2)**(n0-1) if s&(1<<e) else 0)+Q(2)**(n0-2)*((s&~(1<<e)).bit_count())
            assert lhs<=rhs
            exact=sum(1 for a in range(count) if a&(1<<e) and a&s==s)
            assert exact==lhs
            norm_checks+=1
note=(root/'FULL_UNION_LABEL_INVERSE.md').read_text(encoding='utf-8')
assert note.count(r'\(')==note.count(r'\)')
assert note.count(r'\[')==note.count(r'\]')
tags=re.findall(r'\\tag\{([^}]+)\}',note)
assert len(tags)==len(set(tags))==47
out={'observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'union_and_inverse_checks':checks,'boolean_interval_checks':interval_checks,
     'exact_count_and_norm_inequalities':norm_checks,'largest_boolean_rank_checked':8,
     'kernel_test':'Nonzero zero-assembly input retains zero assembly under the full exact inverse.',
     'source_scalar_test':'Möbius formula for every removed union scalar agrees with full ordered union convolution.',
     'inline_math_pairs':note.count(r'\('),'display_math_pairs':note.count(r'\['),
     'proof_tags':tags,'proof_sha256':hashlib.sha256(note.encode()).hexdigest(),
     'scope':'Finite exact rational checks of the Boolean identities and constants. Physical supported spaces, elliptic inverses and analytic claims have their general proofs in the note; this scalar test algebra is not a substitute physical model.'}
(root/'EXACT_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='proof_tags'},indent=2))
