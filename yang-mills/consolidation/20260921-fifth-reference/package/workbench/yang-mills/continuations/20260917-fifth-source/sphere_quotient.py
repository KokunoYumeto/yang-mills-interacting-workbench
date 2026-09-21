"""Exact tree-holonomy map to the original quaternion sphere coordinate algebra.
Each chord retains x0^2+x1^2+x2^2+x3^2=1. The displayed remainder uses
exponent 0 or 1 in each x0; all coefficients are rational.  The inverse
on gauge orbits and the injectivity proof are written in FIFTH_SOURCE.md.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
class Sphere:
 def __init__(self,rank):
  self.rank=rank;self.n=4*rank;self.zero=(0,)*self.n;self.one={self.zero:F(1)}
 @lru_cache(300000)
 def reduce(self,m):
  for k in range(self.rank):
   j=4*k
   if m[j]>=2:
    v=list(m);v[j]-=2;ans=defaultdict(int)
    for a,c in self.reduce(tuple(v)):ans[a]+=c
    for h in (1,2,3):
     v[j+h]+=2
     for a,c in self.reduce(tuple(v)):ans[a]-=c
     v[j+h]-=2
    return tuple((a,c) for a,c in ans.items() if c)
  return ((m,1),)
 def add(self,*ps):
  r=defaultdict(F)
  for p in ps:
   for m,c in p.items():r[m]+=c
  return {m:c for m,c in r.items() if c}
 def scale(self,p,c):return {m:a*c for m,a in p.items() if a*c}
 def mul(self,p,q):
  r=defaultdict(F)
  for m,c in p.items():
   for n,d in q.items():
    power=tuple(a+b for a,b in zip(m,n))
    for z,k in self.reduce(power):r[z]+=c*d*k
  return {m:c for m,c in r.items() if c}
 def variable(self,j):
  e=[0]*self.n;e[j]=1;return {tuple(e):F(1)}
 def qm(self,a,b):
  x,y,z,w=a;u,v,s,t=b;mul=self.mul;add=self.add;neg=lambda p:self.scale(p,-1)
  return (add(mul(x,u),neg(mul(y,v)),neg(mul(z,s)),neg(mul(w,t))),
          add(mul(x,v),mul(y,u),mul(z,t),neg(mul(w,s))),
          add(mul(x,s),neg(mul(y,t)),mul(z,u),mul(w,v)),
          add(mul(x,t),mul(y,s),neg(mul(z,v)),mul(w,u)))
 def conj(self,a):return (a[0],)+tuple(self.scale(p,-1) for p in a[1:])
class CoordinateMap:
 def __init__(self,edges):
  self.edges={int(k):(tuple(v[0]),tuple(v[1])) for k,v in edges}
  verts=sorted({v for vs in self.edges.values() for v in vs});parent={v:v for v in verts}
  def find(v):
   while parent[v]!=v:parent[v]=parent[parent[v]];v=parent[v]
   return v
  tree=[];chords=[]
  for e,(u,v) in sorted(self.edges.items()):
   a,b=find(u),find(v)
   if a!=b:parent[a]=b;tree.append(e)
   else:chords.append(e)
  if len({find(v) for v in verts})!=1:raise ValueError('coordinate-source-disconnected')
  self.root=min(verts);self.tree=tuple(tree);self.chords=tuple(chords);self.S=Sphere(len(chords));s=self.S
  self.identity=(s.one,{},{},{});self.U={e:self.identity for e in tree}
  for i,e in enumerate(chords):self.U[e]=tuple(s.variable(4*i+j) for j in range(4))
 @lru_cache(10000)
 def word(self,w):
  r=self.identity;s=self.S
  for e in w:r=s.qm(r,self.U[e] if e>0 else s.conj(self.U[-e]))
  return s.scale(r[0],2)
 @lru_cache(50000)
 def monomial(self,m):
  r=self.S.one
  for w in m:r=self.S.mul(r,self.word(w))
  return r
 def polynomial(self,p):
  out={};s=self.S
  for m,c in p.items():out=s.add(out,s.scale(self.monomial(m),c))
  return out
 def record(self):return {'root':self.root,'tree_edge_ids':self.tree,'chord_edge_ids':self.chords,
  'variables':[[e,a] for e in self.chords for a in range(4)],
  'sphere_relations':'x[c,0]^2+x[c,1]^2+x[c,2]^2+x[c,3]^2-1',
  'remainder_basis':'exponent of every x[c,0] in {0,1}; all other exponents original'}
def decode(rows):return {tuple(tuple(w) for w in r['words']):F(r['coefficient']) for r in rows}
def encode_poly(p):return [{'powers':m,'coefficient':str(c)} for m,c in sorted(p.items())]
