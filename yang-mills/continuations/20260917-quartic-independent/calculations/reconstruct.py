"""Exact map from every anchored original multiset to its retained representative.

The signed coordinate permutation acts on original vertices; reversed edges
map to the inverse of their original SU(2) link. No coefficient rescaling or
extra factorial accompanies this pullback.
"""
from pathlib import Path
import json
from quartic_catalogue import enumerate_classes,TRANSFORMS,transform_face
ROOT=Path(__file__).resolve().parents[1]

def transformed_multiset(faces,index):
    fs=[transform_face(p,index) for p in faces]
    shift=tuple(min(p[k] for p in fs) for k in range(3))
    image=tuple(sorted(tuple(p[k]-shift[k] for k in range(3))+p[3:] for p in fs))
    return image,shift

def transform_edge(edge,permutation,signs,shift):
    """Return (positive original representative edge, traversal sign)."""
    n=edge[:3];axis=edge[3]
    v=tuple(signs[k]*n[permutation[k]]-shift[k] for k in range(3))
    target_axis=permutation.index(axis);orientation=signs[target_axis]
    lo=list(v)
    if orientation<0:lo[target_axis]-=1
    return tuple(lo)+(target_axis,),orientation

def build():
    stats,classes=enumerate_classes(4);rows=[]
    for i,(key,members) in enumerate(sorted(classes.items())):
        for original in sorted(members):
            for j,(perm,signs) in enumerate(TRANSFORMS):
                image,shift=transformed_multiset(original,j)
                if image==key:
                    rows.append({'class_index':i,'original_face_multiset':[list(x) for x in original],
                                 'coordinate_permutation':list(perm),'coordinate_signs':list(signs),
                                 'subtracted_translation':list(shift),'transform_index':j})
                    break
            else:raise ArithmeticError('missing-lattice-transport')
    return {'scope':'Every original anchored connected multiset, each once, with an explicit signed-coordinate transport and inverse-link orientation rule.',
            'original_anchor_edge':[0,0,0,0],'anchored_counts_by_order':stats,
            'vertex_map':'n_prime[k]=signs[k]*n[permutation[k]]-subtracted_translation[k]',
            'link_map':'transform_edge returns positive edge and orientation; negative orientation carries U_inverse.',
            'rows':rows}

if __name__=='__main__':
    data=build();(ROOT/'results/anchored_quartic_transports.json').write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    print('Stored all',len(data['rows']),'original signed-coordinate transports.')
