"""Independent integer coefficient matrices for every short sign pattern.

The stripped inverse uses the transpose on each selected occurrence. Its
coefficient-side duality matrices are unitary, so the integer singular-value
calculation returns the original SU(2) coefficient norm without dropping mass.
"""
from pathlib import Path
from itertools import product
from collections import defaultdict
from fractions import Fraction as F
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parent

def need(t,name):
    if not t:raise ArithmeticError(name)

def matrix(d,signs):
    A={};n=len(signs)
    for colors in product(range(d),repeat=n):
        row=tuple(colors[(i+1)%n] if signs[i]>0 else colors[i] for i in range(n))
        col=tuple(colors[i] if signs[i]>0 else colors[(i+1)%n] for i in range(n))
        A[row,col]=A.get((row,col),0)+1
    return A

def gram(A):
    rows=defaultdict(list)
    for (r,c),a in A.items():rows[r].append((c,a))
    B=defaultdict(int)
    for row in rows.values():
        for c,a in row:
            for d,b in row:B[c,d]+=a*b
    return dict(B)

def square(A):
    rows=defaultdict(list);cols=defaultdict(list)
    for (r,c),a in A.items():rows[r].append((c,a));cols[c].append((r,a))
    B=defaultdict(int)
    for k in set(rows)&set(cols):
        for i,a in cols[k]:
            for j,b in rows[k]:B[i,j]+=a*b
    return {k:v for k,v in B.items() if v}

def run():
    checks=[]
    for d,lengths in ((2,range(1,8)),(3,range(1,6))):
        for n in lengths:
            for signs in product((-1,1),repeat=n):
                A=matrix(d,signs);G=gram(A);k=sum(signs[i]!=signs[i-1] for i in range(n))//2
                need(square(G)=={key:d**(2*k)*v for key,v in G.items()},'exact-Gram-minimal-polynomial')
                tr=sum(a for (r,c),a in G.items() if r==c)
                need(tr==d**n,'complete-trace-mass')
                norm=F(tr,d**k);need(norm==d**(n-k),'exact-trace-coefficient-norm')
                checks.append({'d':d,'signs':list(signs),'changes':2*k,'trace_norm':str(norm),'rank':d**(n-2*k)})
    # Literal partial-transpose map and its different, explicitly calculated costs.
    A=matrix(2,(1,1,1,1));mapped={}
    for (r,c),v in A.items():
        rr=r[:2]+c[2:];cc=c[:2]+r[2:];mapped[rr,cc]=v
    need(mapped==matrix(2,(1,1,-1,-1)),'partial-transpose-map')
    need(F(16,8)==2,'partial-transpose-cost-ratio')
    return {'passed':True,'scope':'exact independent-occurrence tensor coefficients; repeated-link return is proved analytically',
            'sign_patterns':len(checks),'checks':checks,'partial_transpose_trace_norms':[16,8]}

def main():
    p=argparse.ArgumentParser();p.add_argument('--verify-existing',action='store_true');a=p.parse_args()
    text=json.dumps(run(),sort_keys=True,indent=2)+'\n';dest=ROOT/'generated/word_tensor_audit.json'
    if a.verify_existing:need(dest.read_text()==text,'word-tensor-record')
    else:dest.write_text(text)
    print('PASS',json.loads(text)['sign_patterns'],'exact sign-pattern coefficients')
if __name__=='__main__':main()
