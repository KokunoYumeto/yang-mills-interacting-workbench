from __future__ import annotations
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from itertools import product, combinations
from datetime import datetime, timezone
import json, sys, hashlib, time, argparse
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'verification_sources'))
from source_engine import Source,coordinates
from trace_algebra import multiply, trace, haar
import geometry as g

def decode(poly):
    return {tuple(tuple(w) for w in z['words']):F(z['coefficient']) for z in poly}

def face_from_parity(row):
    cnt=Counter(abs(e) for w,n in zip(row['original_words'],row['multiplicity']) for e in w for _ in range(n))
    edges={i:tuple(map(tuple,uv)) for i,uv in row['edge_coordinates']}
    parity={frozenset(edges[e]) for e,c in cnt.items() if c%2}
    if len(parity)!=4:return None
    verts=set().union(*parity)
    low=tuple(min(v[k] for v in verts) for k in range(3))
    axes=tuple(k for k in range(3) if len({v[k] for v in verts})>1)
    if len(axes)!=2:return None
    p=low+axes
    if {frozenset(g.endpoints(e)) for e in g.pedges(p)}!=parity:return None
    return p

def local_word(p,row):
    ed={frozenset(map(tuple,uv)):(i,tuple(uv[0]),tuple(uv[1])) for i,uv in row['edge_coordinates']}
    out=[]
    for e,s in g.pword(p):
        u,v=g.endpoints(e);i,a,b=ed[frozenset((u,v))]
        out.append(i*s*(1 if (u,v)==(a,b) else -1))
    return tuple(out)

def classify(faces,out):
    count=Counter(faces)
    n=len(count)
    if n==1:return 'self_5'
    if n==2:
        other=next(p for p in count if p!=out)
        return f'pair_output{count[out]}_other{count[other]}'
    if n==3:
        typ=g.type3(tuple(count))
        degree=sum(bool(g.pedges(out)&g.pedges(p)) for p in count if p!=out)
        return f'triple_{typ}_output_degree{degree}'
    if n==5:return 'five_cube_faces'
    return f'unclassified_{n}'

def main():
    t0=time.monotonic()
    results=[];zero=0
    parser=argparse.ArgumentParser(description='Optional comparison against the original complete fifth-source catalogue.')
    parser.add_argument('--catalogue-dir',required=True,type=Path)
    srcdir=parser.parse_args().catalogue_dir
    for file in sorted(srcdir.glob('*.json')):
        row=json.loads(file.read_text())
        face=face_from_parity(row)
        if face is None:zero+=1;continue
        poly=decode(row['coefficients'])
        w=local_word(face,row)
        value=haar(multiply(poly,trace(w)))
        faces=tuple(map(tuple,row['faces']))
        result={'index':row['index'],'faces':faces,'multiplicity':row['multiplicity'],
                'output_face':face,'output_word':w,'union_edges':row['edge_coordinates'],
                'classification':classify(faces,face),'projection':str(value),
                'source_file':'20260917-fifth-source/generated/fifth/'+file.name,'source_sha256':hashlib.sha256(file.read_bytes()).hexdigest(),
                'source_terms':len(poly)}
        results.append(result)
        print(row['index'],result['classification'],value,'seconds',round(time.monotonic()-t0,3),flush=True)
    groups={}
    for r in results:groups.setdefault(r['classification'],set()).add(r['projection'])
    out={'schema':'original-fifth-face-projections-v1','created_utc':datetime.now(timezone.utc).isoformat(),
         'source_rows':len(results)+zero,'parity_excluded_rows':zero,'projected_rows':results,
         'classes':{k:sorted(v) for k,v in sorted(groups.items())},'elapsed_seconds':time.monotonic()-t0}
    (ROOT/'FIFTH_FACE_PROJECTIONS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out['classes'],indent=2),flush=True)
if __name__=='__main__':main()
