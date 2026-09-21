"""Orientation-uniform trace-coefficient upper bounds on original closed words.

Each occurrence is first an independent fundamental variable. The exact
coefficient norm is 2^(length - cyclic_sign_changes/2). Identifying repeated
edge variables is an actual compact-group homomorphism and contracts the
Fourier trace norm. All eight coordinate reflections are tested explicitly.
"""
from fractions import Fraction as F
from itertools import product

REFLECTIONS=tuple(product((-1,1),repeat=3))

def edge_axes(edge_coordinates):
    result={}
    for edge, uv in edge_coordinates:
        left,right=map(tuple,uv)
        d=tuple(right[i]-left[i] for i in range(3))
        active=[i for i in range(3) if d[i]]
        if len(active)!=1 or abs(d[active[0]])!=1:
            raise ArithmeticError('original-nearest-neighbor-edge')
        # Coordinate records always orient the positive numbered edge forward.
        result[int(edge)]=(active[0],1 if d[active[0]]>0 else -1)
    return result

def word_bound(word,axes,reflection):
    if not word:return F(2)  # explicit trace of the empty word
    signs=[(1 if e>0 else -1)*axes[abs(e)][1]*reflection[axes[abs(e)][0]] for e in word]
    changes=sum(signs[i]!=signs[i-1] for i in range(len(signs)))
    if changes%2:raise ArithmeticError('cyclic-sign-parity')
    return F(2)**(len(word)-changes//2)

def reflected_bounds(poly,edge_coordinates):
    axes=edge_axes(edge_coordinates)
    return tuple(sum(abs(c)*_monomial(m,axes,s) for m,c in poly.items()) for s in REFLECTIONS)

def _monomial(words,axes,s):
    value=F(1)
    for word in words:value*=word_bound(word,axes,s)
    return value

def uniform_bound(poly,edge_coordinates):
    return max(reflected_bounds(poly,edge_coordinates),default=F(0))
