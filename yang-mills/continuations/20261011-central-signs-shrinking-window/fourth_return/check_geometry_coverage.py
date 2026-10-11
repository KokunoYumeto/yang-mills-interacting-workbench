from project_fifth import ROOT,g
from fourth_matrix import triples_containing,cubes_containing
from clusters import cubic_orbit
from collections import Counter
import json

def main():
    saved=json.loads((ROOT/'FIFTH_FACE_PROJECTIONS.json').read_text())['projected_rows']
    reps={cubic_orbit(tuple(map(tuple,row['faces'])))[0]:row for row in saved}
    assert len(reps)==25
    p=(0,0,0,0,1)
    cases=[(p,)*5]
    for q in sorted(g.adjacent(p)):cases.extend([(p,p,p,q,q),(p,q,q,q,q)])
    for tri in triples_containing(p):
        others=[q for q in tri if q!=p]
        cases.append((p,others[0],others[0],others[1],others[1]))
    for cube in cubes_containing(p):cases.append(tuple(q for q in cube if q!=p))
    records=[];seen=set()
    for faces in cases:
        rep,witness=cubic_orbit(faces)
        assert rep in reps,faces
        row=reps[rep];seen.add(row['index'])
        records.append({'faces':faces,'canonical_faces':rep,'signed_permutation_translation':witness,'source_row':row['index']})
    assert seen=={r['index'] for r in saved}
    out={'anchor_output_face':p,'complete_concrete_cases':len(cases),'coordinate_representatives':len(seen),'all_25_representatives_reached':True,'classification_counts':dict(Counter(reps[cubic_orbit(f)[0]]['classification'] for f in cases)),'maps':records}
    (ROOT/'GEOMETRY_COVERAGE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
    print({k:v for k,v in out.items() if k!='maps'})
if __name__=='__main__':main()
