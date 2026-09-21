from source_engine import *
from exact_lp import maximize
from pathlib import Path
import json
from functools import lru_cache

def trace_bound(poly):
    # Uniform in original orientation; no invariance of nuclear norm under link inversion is presumed.
    return sum(abs(v)*2**sum(len(w)-1 for w in m) for m,v in poly.items())

def spin_table(ps):
    ob=Source(ps);ws,ed=ob.words,ob.edges; n=len(ws)
    counts=Counter(abs(x) for w in ws for x in w)
    if n!=4 or max(counts.values())>2:return None
    shared=sorted(e for e,r in counts.items() if r==2);es=sorted(counts)
    spec,allowed=physical_spectrum(ws,ed)
    tuples=[]
    for js in allowed:
        dic=dict(zip(es,js));bits=tuple(dic[e]//2 for e in shared)
        tuples.append(bits)
    tuples=sorted(set(tuples))
    vals=[]
    def subset_spectrum(mask,bits):
        cc=Counter(abs(x) for i,w in enumerate(ws) if mask>>i&1 for x in w)
        j={e:(F(bits[shared.index(e)]) if r==2 else F(1,2)) for e,r in cc.items()}
        return sum(x*(x+1) for x in j.values())
    for bits in tuples:
        @lru_cache(None)
        def coefficient(mask):
            if mask.bit_count()==1:return F(1,3)
            c=subset_spectrum(mask,bits)
            if c==0:return F(0)
            v=F(0);a=(mask-1)&mask
            while a:
                b=mask^a
                if b:v+=(subset_spectrum(a,bits)+subset_spectrum(b,bits)-c)/(2*c)*coefficient(a)*coefficient(b)
                a=(a-1)&mask
            return v
        c=subset_spectrum(15,bits);vals.append((bits,c,coefficient(15)))
    base=const(1)
    for w in ws:base=multiply(base,trace(w))
    p0={0:base};bounds=[];A=[]
    for mask in range(1<<len(shared)):
        if mask:
            bit=(mask&-mask);i=bit.bit_length()-1;p=p0[mask^bit]
            p0[mask]=add(p,scale(electric(p,shared[i]),-F(1,2)))
        bd=trace_bound(p0[mask])
        A.append([int(all(bits[i]==0 for i in range(len(shared)) if mask>>i&1)) for bits,c,a in vals]);bounds.append(bd)
    objective=[abs(a)*c for bits,c,a in vals]
    val,x,y,steps=maximize(A,bounds,objective)
    return {'shared_edges':shared,'channels':[[list(b),str(c),str(a)] for b,c,a in vals],
            'bound':str(val),'partial_projection_bounds':list(map(str,bounds)),
            'dual':list(map(str,y)),'primal':list(map(str,x)),'pivots':steps}

