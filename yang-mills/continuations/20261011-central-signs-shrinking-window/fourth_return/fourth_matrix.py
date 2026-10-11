from fractions import Fraction as F
from collections import defaultdict,Counter
from itertools import product,combinations
from pathlib import Path
import json
from project_fifth import ROOT,g

SELF=F(7,3888)
B32=-F(301,2956824)
B14=-F(55,3639168)
H={'path_center':F(19,3032640),'path_end':F(19,59136480),
   'common':-F(4,616005),'corner':F(164,6283251)}
CUBE=F(107,34992)
SSELF=F(1,81)-15*SELF
SDIAG=-(9*B32+3*B14)
SOFF=-(6*B32+12*B14)

def faces_box(L):
    return tuple(n+(i,j) for n in product(range(-L,L+1),repeat=3)
                 for i,j in combinations(range(3),2) if n[i]<L and n[j]<L)
def cube(n):
    return tuple(sorted(p for i,j in combinations(range(3),2)
                        for p in [tuple(n)+(i,j),g.add(n,3-i-j)+(i,j)]))
def cubes_containing(p):
    return (cube(p[:3]),cube(g.add(p[:3],3-p[3]-p[4],-1)))
def triples_containing(p):
    out=set()
    for q in g.adjacent(p):
        for r in g.adjacent(p)|g.adjacent(q):
            if r not in (p,q):out.add(tuple(sorted((p,q,r))))
    return tuple(sorted(out))
def marked_type(p,triple):
    typ=g.type3(triple)
    if typ=='path':
        d=sum(q in g.adjacent(p) for q in triple if q!=p)
        return 'path_center' if d==2 else 'path_end'
    return typ
def eta(p,triple):return H[marked_type(p,triple)]

def original_matrix(L):
    ps=faces_box(L);p_set=set(ps);ids={p:i for i,p in enumerate(ps)}
    S=defaultdict(F);degree={}
    counts=Counter()
    for p in ps:
        i=ids[p];S[i,i]+=SSELF
        neigh=set(g.adjacent(p))&p_set;degree[i]=len(neigh)
        for q in neigh:
            S[i,i]+=SDIAG;S[i,ids[q]]+=SOFF
        for tri in triples_containing(p):
            if not set(tri)<=p_set:continue
            h=eta(p,tri);counts[marked_type(p,tri)]+=1
            S[i,i]-=3*h
            for q in tri:
                if q!=p:S[i,ids[q]]-=6*h
        for cub in cubes_containing(p):
            if not set(cub)<=p_set:continue
            for q in cub:
                if q!=p:S[i,ids[q]]-=3*CUBE
    S={k:v for k,v in S.items() if v}
    defects=[];anti=-6*(H['path_center']-H['path_end'])
    for (i,j),v in S.items():
        expected=anti*(degree[i]-degree[j]) if ps[j] in g.adjacent(ps[i]) else F(0)
        assert v-S.get((j,i),F(0))==expected
        if expected:defects.append({'p':ps[i],'q':ps[j],'degrees':[degree[i],degree[j]],
                                      'S4_pq':str(v),'S4_qp':str(S.get((j,i),F(0))),
                                      'difference':str(expected)})
    p=(0,0,0,0,1);q=(0,0,1,0,1)
    opposite=S[ids[p],ids[q]]
    assert opposite==-24*H['path_end']-3*CUBE==-F(90491,9856080)
    out={'schema':'original-j5-fourth-schur-matrix-v1','L':L,'faces':ps,
         'entries':[[i,j,str(v)] for (i,j),v in sorted(S.items())],
         'boundary_degrees':[degree[i] for i in range(len(ps))],
         'marked_triple_incidence_counts':dict(counts),
         'nonzero_entries':len(S),'antisymmetry_verified':True,
         'antisymmetric_ordered_entries':len(defects),'boundary_example':defects[0],
         'opposite_cube_entry':{'p':p,'q':q,'coefficient':str(opposite)}}
    (ROOT/f'FOURTH_SCHUR_L{L}.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
    return {k:v for k,v in out.items() if k not in ['faces','entries','boundary_degrees']}

def main():
    anchor=(0,0,0,0,1)
    n=Counter(marked_type(anchor,t) for t in triples_containing(anchor))
    row=abs(SSELF)+12*(abs(SDIAG)+abs(SOFF))+15*sum(n[k]*abs(v) for k,v in H.items())+30*CUBE
    col=abs(SSELF)+12*(abs(SDIAG)+abs(SOFF))
    col+=n['path_center']*(3*H['path_center']+12*H['path_end'])
    col+=n['path_end']*(9*H['path_end']+6*H['path_center'])
    col+=15*(n['common']*abs(H['common'])+n['corner']*H['corner'])+30*CUBE
    assert row==col
    result={'self':str(SSELF),'pair_diagonal':str(SDIAG),'pair_offdiagonal':str(SOFF),
            'antisymmetry_factor':str(-6*(H['path_center']-H['path_end'])),
            'bulk_marked_triples':dict(n),'uniform_absolute_row_and_column_bound':str(row),
            'uniform_haar_operator_bound':str(row),'uniform_haar_operator_bound_decimal':float(row),
            'finite_checks':[original_matrix(L) for L in [2,3]]}
    (ROOT/'FOURTH_MATRIX_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
