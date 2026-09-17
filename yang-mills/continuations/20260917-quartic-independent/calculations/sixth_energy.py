"""Exact sixth ground-energy coefficient of the original three-dimensional box.

The proof of the finite linked expansion, including the six-distinct-face cube
term, is in proofs/SIXTH_ORDER_ENERGY.md. All arithmetic here is rational.
"""
from fractions import Fraction as Q
from itertools import combinations,permutations,product
from collections import Counter,defaultdict
from pathlib import Path
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'recovered'))
from geometry import pedges,pword,add,type3
ROOT=Path(__file__).resolve().parents[1]
WEIGHTS={'single':-Q(289,77760),'adjacent_pair':Q(22285,23654592),
 'path':-Q(4909,118272960),'common':Q(244,4312035),
 'corner':-Q(212,542997),'cube':-Q(83,1944)}

def small_cluster_energy6(M,edges,triples):
    # Whole-coefficient expression obtained before linked subtraction.
    u=[Q(4,27),Q(4,39)]
    a=(Q(1,24)+Q(1,9)+Q(1,39))/9;b=(Q(1,24)+Q(4,39))/12
    repeat_adj=3*a*a+8*b*b;repeat_dis=Q(11,5184)
    pair_mass=Q(1,4)*u[0]**2+Q(3,4)*u[1]**2
    tri={}
    tri['none']=Q(1,81)
    tri['one']=sum((Q(9,2)+2*s+3)*(u[s]/3)**2*[Q(1,4),Q(3,4)][s] for s in range(2))
    tri['path']=sum((Q(1,9)+u[s]+u[t])**2/(6+2*s+2*t)*[Q(1,4),Q(3,4)][s]*[Q(1,4),Q(3,4)][t] for s,t in product(range(2),repeat=2))
    tri['common']=Q(1,2)*(Q(3,2)*(u[0]+u[1]))**2/Q(15,2)+Q(1,2)*(3*u[1])**2/Q(21,2)
    tri['corner']=sum(w*((3-n)*u[0]+n*u[1])**2/(Q(9,2)+2*n) for n,w in [(0,Q(1,16)),(2,Q(9,16)),(3,Q(3,8))])
    deg=[sum(i in e for e in edges) for i in range(M)];J=len(edges)
    e2=-Q(M,3);e4=Q(5*M,216)-Q(2*J,1053)
    norm2=Q(M,576)+Q(M*(M-1),162)+J*(pair_mass-Q(1,81))
    energy3=3*sum((-Q(5,216)+Q(d,1053))**2 for d in deg)+Q(M,8640)
    energy3+=(M*(M-1)-2*J)*repeat_dis+2*J*repeat_adj+sum(tri[t] for t in triples)
    return -energy3-e4*Q(M,9)-e2*norm2

def cube_data():
    # Literal unit-cube faces, paired by their perpendicular coordinate.
    faces=[]
    for normal in range(3):
        dirs=tuple(i for i in range(3) if i!=normal)
        for side in (0,1):
            n=[0,0,0];n[normal]=side;faces.append(tuple(n)+dirs)
    words=[]
    for normal in range(3):
        dirs=tuple(i for i in range(3) if i!=normal)
        # e_i cross e_j = sign * e_normal
        sign=1 if (*dirs,normal) in ((0,1,2),(1,2,0),(2,0,1)) else -1
        for side in (0,1):
            f=faces[2*normal+side];w=pword(f)
            if sign!=(1 if side else -1):w=tuple((e,-s) for e,s in reversed(w))
            words.append(w)
    uses=defaultdict(list)
    for i,w in enumerate(words):
        for e,s in w:uses[e].append((i,s))
    if len(uses)!=12 or any(len(v)!=2 or sum(s for i,s in v)!=0 for v in uses.values()):raise ArithmeticError('cube-orientation')
    parent={}
    def find(x):
        parent.setdefault(x,x)
        if parent[x]!=x:parent[x]=find(parent[x])
        return parent[x]
    def join(a,b):parent[find(a)]=find(b)
    for e,v in uses.items():
        u=e[:3];w=add(u,e[3]);i,j=v[0][0],v[1][0]
        join((i,u),(j,u));join((i,w),(j,w))
    classes=len({find(x) for x in parent});haar=Q(2**classes,2**12)
    if classes!=8 or haar!=Q(1,16):raise ArithmeticError('cube-Haar')
    rows=[];total=Q(0);hist=Counter()
    for order in permutations(range(6)):
        factor=Q(1);boundary=[];sset=set()
        for k in range(5):
            sset.add(order[k]);multip=Counter(e for i in sset for e in pedges(faces[i]))
            size=sum(v%2 for v in multip.values());boundary.append(size);factor*=Q(4,3*size)
        total+=factor;hist[tuple(boundary)]+=1
        rows.append({'order':list(order),'boundary_edge_counts':boundary,'inverse_energy_product':str(factor)})
    independent=-Q(1,16)*(12*6*Q(11,162)**2+8*Q(9,2)*Q(8,81)**2)
    if -haar*total!=independent or independent!=WEIGHTS['cube']:raise ArithmeticError('cube-two-paths')
    return {'faces':[list(f) for f in faces],'edge_count':12,'color_loops':classes,'Haar_six_trace_product':str(haar),
      'ordered_insertion_sum':str(total),'linked_sixth_weight':str(-haar*total),'independent_half_path_value':str(independent),
      'boundary_sequence_histogram':[{'sequence':list(k),'multiplicity':v} for k,v in sorted(hist.items())], 'paths':rows}

def counts(L):
    m=2*L;M=3*m*m*(m+1);J=6*m*(3*m*m-1)
    return {'M':M,'J':J,'path':138*m**3-126*m*m-24*m+12,'common':12*m*m*(m-1),'corner':8*m**3,'cube':m**3}

def coefficients(L):
    x=counts(L);e6=WEIGHTS['single']*x['M']+WEIGHTS['adjacent_pair']*x['J']+sum(WEIGHTS[k]*x[k] for k in ('path','common','corner','cube'))
    m=2*L;closed=-Q(211396463*m**3+30959193*m*m+21845782*m+2336684,4691494080)
    if e6!=closed:raise ArithmeticError('finite-box-polynomial')
    return {'L':L,'original_counts':x,'ground_energy_over_kappa_coefficients':{'xi':str(2*x['M']),'xi2':str(-Q(x['M'],3)),
       'xi4':str(Q(5*x['M'],216)-Q(2*x['J'],1053)),'xi6':str(e6)},'Cauchy_radius':str(Q(3,8*x['M']))}

def enumerate_box(L):
    m=2*L;faces=[]
    for n in product(range(-L,L+1),repeat=3):
        for i,j in combinations(range(3),2):
            if n[i]<L and n[j]<L:faces.append(n+(i,j))
    byedge=defaultdict(list)
    for p in faces:
        for e in pedges(p):byedge[e].append(p)
    adj={p:set() for p in faces}
    for ps in byedge.values():
        for p,q in combinations(ps,2):adj[p].add(q);adj[q].add(p)
    triples=set()
    for p in faces:
        for q,r in combinations(adj[p],2):triples.add(tuple(sorted((p,q,r))))
    tc=Counter(type3(t) for t in triples)
    empirical={'M':len(faces),'J':sum(len(v) for v in adj.values())//2,
               'path':tc['path'],'common':tc['common'],'corner':tc['corner'],'cube':m**3}
    if empirical!=counts(L):raise ArithmeticError(('box-counts',L,empirical,counts(L)))
    return empirical

def main():
    cube=cube_data();(ROOT/'results/cube_sixth_paths.json').write_text(json.dumps(cube,sort_keys=True,indent=2)+'\n')
    data={'operator':'H/kappa=K+xi*(2M-S)','linked_sixth_weights':{k:str(v) for k,v in WEIGHTS.items()},
          'finite_boxes':[coefficients(L) for L in (2,3,4,5)],
          'independently_enumerated_counts':[enumerate_box(L) for L in (2,3,4)],
          'sixth_coefficient_per_plaquette_spatial_limit':str(-Q(211396463,14074482240)),
          'coefficient_limit_scope':'limit of this exact finite-order coefficient; no exchange with a nonperturbative infinite-volume series',
          'all_higher_orders_bound':'|R8| <= (3*kappa/4)*(|xi|/R)^8/(1-(|xi|/R)^2), R=3/(8M), |xi|<R',
          'cube_weight_from_two_independent_sums':cube['linked_sixth_weight']}
    (ROOT/'results/sixth_energy.json').write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    print(json.dumps(data,indent=2))
if __name__=='__main__':main()
