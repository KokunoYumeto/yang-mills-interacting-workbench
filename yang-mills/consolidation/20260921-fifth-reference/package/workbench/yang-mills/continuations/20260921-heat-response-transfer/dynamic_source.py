"""Original-link resolvent coefficients for physical heat correlations.
The P_H u=1 section and its full norm are retained, together with centering.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'20260917-quartic-cube'))
from energy import Rayleigh
from source_engine import subcounts
from trace_algebra import *
from functools import lru_cache
from exact_rational import PF,pole
class Dynamic(Rayleigh):
    @lru_cache(None)
    def norm(self,cs):
        return sum(haar(multiply(self.u(a),self.u(tuple(x-y for x,y in zip(cs,a))))) for a in subcounts(cs))
    @lru_cache(None)
    def moment(self,p,cs):
        return sum(haar(multiply(multiply(self.u(a),trace(self.words[p])),self.u(tuple(x-y for x,y in zip(cs,a))))) for a in subcounts(cs))
    @lru_cache(None)
    def mean(self,p,cs):
        ans=self.moment(p,cs)
        for a in subcounts(cs):
            if not sum(a):continue
            b=tuple(x-y for x,y in zip(cs,a))
            ans-=self.norm(a)*self.mean(p,b)
        return ans
    @lru_cache(None)
    def project_monomial(self,m):
        spec=physical_spectrum(tuple(m),self.edges)[0]
        pol={m:F(1)};out=[]
        for c in spec:
            ans=pol
            for d in spec:
                if d!=c:ans=scale(add(electric(ans),scale(ans,-d)),F(1,c-d))
            if ans:out.append((c,ans))
        return out
    def resolvent_free(self,p):
        ans={}
        for m,v in p.items():
            for c,pr in self.project_monomial(m):
                vc=v*pole(c)
                for k,a in pr.items():
                    ans[k]=ans.get(k,PF(0))+a*vc
                    if not ans[k]:del ans[k]
        return ans
    @lru_cache(None)
    def h(self,q,cs):
        ans=multiply(trace(self.words[q]),self.u(cs))
        ans={m:PF(c) for m,c in ans.items()}
        for i,k in enumerate(cs):
            if k:
                b=list(cs);b[i]-=1
                ans=add(ans,multiply(trace(self.words[i]),self.h(q,tuple(b))))
        for a in subcounts(cs):
            if not sum(a):continue
            b=tuple(x-y for x,y in zip(cs,a))
            ec=self.e(a)
            if ec:ans=add(ans,scale(self.h(q,b),ec))
        return self.resolvent_free(ans)
    @lru_cache(None)
    def numerator(self,p,q,cs):
        ans=PF(0)
        for a in subcounts(cs):
            b=tuple(x-y for x,y in zip(cs,a))
            ans+=haar(multiply(multiply(self.u(a),trace(self.words[p])),self.h(q,b)))
        return ans
    @lru_cache(None)
    def uncentered(self,p,q,cs):
        ans=self.numerator(p,q,cs)
        for a in subcounts(cs):
            if not sum(a):continue
            b=tuple(x-y for x,y in zip(cs,a))
            ans-=self.norm(a)*self.uncentered(p,q,b)
        return ans
    @lru_cache(None)
    def correlation(self,p,q,cs):
        ans=self.uncentered(p,q,cs)
        for a in subcounts(cs):
            b=tuple(x-y for x,y in zip(cs,a))
            ans-=self.mean(p,a)*self.mean(q,b)*pole(0)
        if any(a==0 and n>0 for a,n in ans.d):raise RuntimeError('ground pole survived centering')
        return ans
    @lru_cache(None)
    def raw_covariance(self,p,q,cs):
        mom=sum(haar(multiply(multiply(multiply(self.u(a),trace(self.words[p])),trace(self.words[q])),self.u(tuple(x-y for x,y in zip(cs,a))))) for a in subcounts(cs))
        for a in subcounts(cs):
            if not sum(a):continue
            b=tuple(x-y for x,y in zip(cs,a))
            mom-=self.norm(a)*self.raw_covariance(p,q,b)
        return mom
    @lru_cache(None)
    def covariance(self,p,q,cs):
        return self.raw_covariance(p,q,cs)-sum(self.mean(p,a)*self.mean(q,tuple(x-y for x,y in zip(cs,a))) for a in subcounts(cs))
    @lru_cache(None)
    def expect_poly(self,poly_tuple,cs):
        poly=dict(poly_tuple)
        val=sum(haar(multiply(multiply(self.u(a),poly),self.u(tuple(x-y for x,y in zip(cs,a))))) for a in subcounts(cs))
        for a in subcounts(cs):
            if not sum(a):continue
            b=tuple(x-y for x,y in zip(cs,a))
            val-=self.norm(a)*self.expect_poly(poly_tuple,b)
        return val
    def kinetic(self,p,q,cs):
        pol=gamma(trace(self.words[p]),trace(self.words[q]))
        return self.expect_poly(tuple(sorted(pol.items())),cs)
    @lru_cache(None)
    def commutator(self,p,cs):
        up=self.u(cs);wp=trace(self.words[p])
        return add(electric(multiply(wp,up)),scale(multiply(wp,electric(up)),-1))
    @lru_cache(None)
    def second_moment(self,p,q,cs):
        val=sum(haar(multiply(self.commutator(p,a),self.commutator(q,tuple(x-y for x,y in zip(cs,a))))) for a in subcounts(cs))
        for a in subcounts(cs):
            if not sum(a):continue
            b=tuple(x-y for x,y in zip(cs,a))
            val-=self.norm(a)*self.second_moment(p,q,b)
        return val
