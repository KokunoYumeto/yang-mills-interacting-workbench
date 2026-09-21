import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'20260916-cubic-linearized'))
import geometry as g
from trace_algebra import *
from functools import lru_cache
from itertools import combinations_with_replacement
import time

def coordinates(ps):
    es=sorted(g.union(ps));ids={e:i+1 for i,e in enumerate(es)}
    ws=tuple(tuple(ids[e]*s for e,s in g.pword(p)) for p in ps)
    ed={i+1:g.endpoints(e) for i,e in enumerate(es)}
    return ws,ed

def subcounts(cs):
    return product(*(range(c+1) for c in cs))
class Source:
    def __init__(self,ps):
        self.ps=tuple(sorted(set(ps)))
        self.words,self.edges=coordinates(self.ps)
    @lru_cache(None)
    def spectrum(self,cs):
        ws=tuple(w for w,k in zip(self.words,cs) for _ in range(k))
        return physical_spectrum(ws,self.edges)[0]
    @lru_cache(None)
    def v(self,cs):
        n=sum(cs)
        if n==1:return scale(trace(self.words[cs.index(1)]),F(1,3))
        rhs={}
        for a in subcounts(cs):
            if sum(a) in (0,n):continue
            b=tuple(c-i for c,i in zip(cs,a))
            rhs=add(rhs,gamma(self.v(a),self.v(b)))
        if not rhs:return {}
        spec=self.spectrum(cs)
        return inverse(rhs,spec)

