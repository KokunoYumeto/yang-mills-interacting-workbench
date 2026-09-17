from source_engine import *
import json,time
from pathlib import Path

def allocations(cs,sizes):
    if len(sizes)==1:
      if sum(cs)==sizes[0]:yield (cs,)
      return
    for a in subcounts(cs):
      if sum(a)!=sizes[0]:continue
      b=tuple(x-y for x,y in zip(cs,a))
      for tail in allocations(b,sizes[1:]):yield (a,)+tail

class EnergySource(Source):
    def energy6(self,cs):
      # E6 = -4 <v1 Gamma(v1,v4)> -4 <v1 Gamma(v2,v3)>
      #      -2 <Gamma(v2,v4)> - <Gamma(v3,v3)>.
      pieces=[]
      for sizes,factor in (((1,1,4),-4),((1,2,3),-4),((2,4),-2),((3,3),-1)):
        v={}
        for tup in allocations(cs,sizes):
          if len(tup)==3:
            a,b,c=tup;term=multiply(self.v(a),gamma(self.v(b),self.v(c)))
          else:a,b=tup;term=gamma(self.v(a),self.v(b))
          v=add(v,scale(term,F(factor)))
        # The source and original Haar constant are retained separately.
        z=haar(v);pieces.append(z)
      return sum(pieces),pieces


class Rayleigh(Source):
    @lru_cache(None)
    def e(self,cs):
        val={}
        for i,k in enumerate(cs):
            if k:
                b=list(cs);b[i]-=1
                val=add(val,multiply(trace(self.words[i]),self.u(tuple(b))))
        return -haar(val)
    @lru_cache(None)
    def u(self,cs):
        if not sum(cs):return const(1)
        out={}
        for i,k in enumerate(cs):
            if k:
                b=list(cs);b[i]-=1;out=add(out,multiply(trace(self.words[i]),self.u(tuple(b))))
        n=sum(cs)
        for a in subcounts(cs):
            if not sum(a) or sum(a)==n:continue
            b=tuple(c-k for c,k in zip(cs,a))
            out=add(out,scale(self.u(b),self.e(a)))
        return inverse(out,self.spectrum(cs))
