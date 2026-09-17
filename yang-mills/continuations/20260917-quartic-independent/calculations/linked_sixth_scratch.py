from fractions import Fraction as F
from itertools import product,permutations
from math import comb
u=[F(4,27),F(4,39)]
rh=(F(1,24)+F(1,9)+F(1,39))/9
rj=(F(1,24)+F(4,39))/12
rep_adj=3*rh*rh+8*rj*rj
rep_dis=F(11,5184)
s2pair=F(1,4)*u[0]**2+F(3,4)*u[1]**2
T={}
T['none']=F(1,81)
T['one']=sum((F(9,2)+2*s+3)*(u[s]/3)**2*([F(1,4),F(3,4)][s]) for s in range(2))
T['path']=sum((F(1,9)+u[s]+u[t])**2/F(6+2*s+2*t)*([F(1,4),F(3,4)][s])*([F(1,4),F(3,4)][t]) for s,t in product(range(2),repeat=2))
T['common']=F(1,2)*(F(3,2)*(u[0]+u[1]))**2/F(15,2)+F(1,2)*(3*u[1])**2/F(21,2)
T['corner']=sum(m*((3-n)*u[0]+n*u[1])**2/(F(9,2)+2*n) for n,m in [(0,F(1,16)),(2,F(9,16)),(3,F(3,8))])

def energy6(M,edges,triples):
 deg=[sum(i in e for e in edges) for i in range(M)];J=len(edges)
 e2=-F(M,3);e4=F(5*M,216)-F(2*J,1053)
 normu2=F(M,576)+F(comb(M,2),81)+J*(s2pair-F(1,81))
 k3=3*sum((-F(5,216)+F(d,1053))**2 for d in deg)+F(M,8640)+(M*(M-1)-2*J)*rep_dis+2*J*rep_adj+sum(T[t] for t in triples)
 return -k3-e4*F(M,9)-e2*normu2
E1=energy6(1,[],[])
E2=energy6(2,[(0,1)],[])
weight2=E2-2*E1
print('u3 repeat',rh,rj,'adjenergy',rep_adj,'dis',rep_dis,'u2pair',s2pair)
print('triple energies',T)
print('E1',E1,'E2',E2,'pair weight',weight2)
for typ,edges in [('none',[]),('one',[(0,1)]),('path',[(0,1),(1,2)]),('common',[(0,1),(0,2),(1,2)]),('corner',[(0,1),(0,2),(1,2)])]:
 e=energy6(3,edges,[typ]);w=e-3*E1-len(edges)*weight2
 print(typ,'E6',e,'linked weight',w, float(w))
# all six faces of unit cube, face labels by opposite pairs
fs=range(6); adjacent=lambda a,b:a//2!=b//2
sm=F(0)
for order in permutations(fs):
 fac=F(1)
 for k in range(1,6):
  ss=order[:k];inner=sum(adjacent(a,b) for a in ss for b in ss if a<b)
  bd=4*k-2*inner;fac*=F(4,3*bd)
 sm+=fac
print('cube contribution',-sm/16, float(-sm/16),'sum',sm)
