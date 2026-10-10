"""Exact finite incidence checks supplement the complete central-sign proof."""
from pathlib import Path
from itertools import product
import json

ROOT=Path(__file__).resolve().parent

def box(lengths, periodic):
    vertices=list(product(*(range(n if periodic else n+1) for n in lengths)))
    edges=[(v,i) for v in vertices for i in range(3)
           if periodic or v[i]<lengths[i]]
    edge_index={e:k for k,e in enumerate(edges)}
    def shift(v,i):
        w=list(v);w[i]=(w[i]+1)%lengths[i] if periodic else w[i]+1
        return tuple(w)
    faces=[]
    for v in vertices:
        for i in range(3):
            for j in range(i+1,3):
                if not periodic and (v[i]==lengths[i] or v[j]==lengths[j]):continue
                boundary=[(v,i),(shift(v,i),j),(shift(v,j),i),(v,j)]
                row=0
                for e in boundary:row ^= 1<<edge_index[e]
                faces.append((v,i,j,row))
    return vertices,edges,faces

def rank(rows):
    basis={}
    for row in rows:
        while row:
            k=row.bit_length()-1
            if k in basis:row ^= basis[k]
            else:basis[k]=row;break
    return len(basis)

records=[]
for periodic,tuples in [(False,[(1,1,1),(2,2,2),(2,3,4)]),
                       (True,[(3,3,3),(3,3,4),(3,4,4),(4,3,4),(4,4,3),(4,4,4)])]:
    for lengths in tuples:
        vertices,edges,faces=box(lengths,periodic)
        r=rank([x[3] for x in faces])
        augmented=rank([x[3] | (1<<len(edges)) for x in faces])
        exists=r==augmented
        criterion=not periodic or sum(n%2 for n in lengths)<=1
        expected_kernel=len(vertices)+(2 if periodic else -1)
        assert len(edges)-r==expected_kernel
        assert exists==criterion
        checked=False
        if exists:
            ordering=sorted(range(3),key=lambda i:lengths[i]%2) if periodic else list(range(3))
            before={i:ordering[:ordering.index(i)] for i in ordering}
            word=sum((sum(v[k] for k in before[i])%2)<<idx
                     for idx,(v,i) in enumerate(edges))
            assert all((row&word).bit_count()%2==1 for _,_,_,row in faces)
            checked=True
        records.append({'periodic':periodic,'lengths':lengths,'vertices':len(vertices),
                        'edges':len(edges),'faces':len(faces),'incidence_rank':r,
                        'augmented_rank':augmented,'existence':exists,
                        'exact_nullity':len(edges)-r,'explicit_assignment_checked':checked})

out={'all_passed':True,'scope':'Exact arithmetic examples; complete arbitrary-box proof is CS1–CS19.',
     'cases':records}
(ROOT/'CENTRAL_SIGNS_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'all_passed':True,'exact_cases':len(records)}))
