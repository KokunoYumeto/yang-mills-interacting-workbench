from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import json,time
from project_fifth import ROOT,Source
from trace_algebra import add,scale,gamma,trace,multiply,haar,physical_spectrum,inverse

WORDS=[(4,),(1,3),(3,1),(2,2),(1,1,2),(1,2,1),(2,1,1),(1,1,1,1)]

def verify_case(ps):
    src=Source(ps);n=len(src.ps)
    v={}
    for degree in range(1,5):
        polys=[src.v(cs) for cs in product(range(degree+1),repeat=n) if sum(cs)==degree]
        v[degree]=add(*polys)
    def inv(poly):
        spectrum=set()
        for monomial in poly:spectrum.update(physical_spectrum(monomial,src.edges)[0])
        return inverse(poly,sorted(spectrum)) if poly else {}
    def project(poly):
        values=[haar(multiply(poly,trace(w))) for w in src.words]
        return add(*(scale(trace(w),a) for w,a in zip(src.words,values))),values
    def act(i,h):return scale(inv(gamma(v[i],h)),F(2))
    matrices={}
    for word in WORDS:
        A=[[F(0) for _ in ps] for _ in ps]
        for col,w in enumerate(src.words):
            h=trace(w)
            for ix,i in enumerate(reversed(word)):
                h=act(i,h)
                if ix<len(word)-1:
                    pp,_=project(h);h=add(h,scale(pp,-1))
            _,vals=project(h)
            for row,c in enumerate(vals):A[row][col]=-c
        matrices[','.join(map(str,word))]=[[str(x) for x in row] for row in A]
    total=[[sum(F(A[i][j]) for A in matrices.values()) for j in range(n)] for i in range(n)]
    self_value=-F(19,1296);diag_pair=F(15163,15769728);off_pair=F(347,438048)
    expected=[[self_value+(n-1)*diag_pair if i==j else off_pair for j in range(n)] for i in range(n)]
    assert total==expected,(total,expected)
    return {'faces':ps,'words':matrices,'sum':[[str(x) for x in row] for row in total],
            'expected_from_fifth_projection':[[str(x) for x in row] for row in expected],'all_eight_words_retained':True}

def main():
    t=time.monotonic()
    results=[]
    for ps in [[(0,0,0,0,1)],[(0,0,0,0,1),(0,1,0,0,1)],[(0,0,0,0,1),(0,0,0,0,2)]]:
        result=verify_case(ps);results.append(result)
        print(result['faces'],result['sum'],round(time.monotonic()-t,2),flush=True)
    (ROOT/'DIRECT_RETURN_WORD_CHECKS.json').write_text(json.dumps({'checks':results,'elapsed_seconds':time.monotonic()-t},indent=2)+'\n')
if __name__=='__main__':main()
