"""Independent finite enumeration checks; proofs are in the accompanying note."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import json, math
import mpmath as mp

mp.mp.dps = 70
ROOT = Path(__file__).resolve().parent
checks = []

def close(name, actual, expected, tol=mp.mpf('1e-55')):
    error = abs(actual-expected) / max(1, abs(actual), abs(expected))
    assert error < tol, (name, actual, expected, error)
    checks.append({'name': name, 'relative_error': str(error), 'passed': True})

def root_path(i,k,l):
    # Original ordered path: third direction, then second, then first.
    return ([(0,0,z,3) for z in range(l)]
            + [(0,y,l,2) for y in range(k)]
            + [(x,k,l,1) for x in range(i)])

def check_box(m):
    n=m+1
    h=mp.pi/(2*n); c=mp.cos(h); C=mp.cot(h)
    v=[mp.sqrt(mp.mpf(2)/n)*mp.cos(mp.pi*(i+mp.mpf('.5'))/n) for i in range(n)]
    w=[-mp.sqrt(mp.mpf(2)/n)*mp.sin(mp.pi*(i+1)/n) for i in range(m)]
    v0=1/mp.sqrt(n)
    chord_data=[]
    for i in range(1,n):
        for k in range(m):
            for l in range(n):
                word=root_path(i,k,l)+[(i,k,l,2)]+list(reversed(root_path(i,k+1,l)))
                occ=Counter(word)
                assert max(occ.values())<=2
                assert sum(occ.values())==2*(i+k+l+1)
                assert sum(x*x for x in occ.values())==2*i+4*k+4*l+2
                chord_data.append((-v[i]*w[k]*v0/mp.sqrt(2),v0*w[k]*v[l]/mp.sqrt(2),occ))
    for i in range(n):
        for k in range(n):
            if (i,k)==(0,0): continue
            for l in range(m):
                word=root_path(i,k,l)+[(i,k,l,3)]+list(reversed(root_path(i,k,l+1)))
                occ=Counter(word)
                assert max(occ.values())<=2
                assert sum(occ.values())==2*(i+k+l+1)
                assert sum(x*x for x in occ.values())==2*i+2*k+4*l+2
                chord_data.append((mp.mpf(0),-v0*v[k]*w[l]/mp.sqrt(2),occ))
    assert len(chord_data)==2*m**3+3*m**2
    coeff=[(abs(a),abs(b),o) for a,b,o in chord_data]
    sums={}
    for idx in range(2):
        sums[f'S{idx}']=sum(row[idx] for row in coeff)
        sums[f'L{idx}']=sum(row[idx]*sum(row[2].values()) for row in coeff)
        sums[f'A{idx}']=sum(row[idx]*sum(x*x for x in row[2].values()) for row in coeff)
    fac=mp.sqrt(mp.mpf(2)/n)
    S1=fac*C*(C-c)
    S3=fac*((2-mp.mpf(1)/n)*C*C-c*C/n)
    L1=fac*C*((3*m+1)*C-(2*m+1)*c)
    L3=fac*((6*m+mp.mpf(1)/n)*C*C-c*C)
    A1=m*fac*C*(5*C-4*c)
    A3=mp.mpf(m)/n*fac*((9*m+5)*C*C-2*c*C)
    for name,ex in [('S0',S1),('S1',S3),('L0',L1),('L1',L3),('A0',A1),('A1',A3)]:
        close(f'm={m}: {name}',sums[name],ex)
    D1=Counter(); D3=Counter()
    for a,b,occ in coeff:
        for e,num in occ.items():
            D1[e]+=a*num; D3[e]+=b*num
    all_edges=set(D1)|set(D3)
    exact=3*sum((2*S3*D1[e]+2*S1*D3[e])**2 for e in all_edges)
    occ_bound=12*(S3*mp.sqrt(S1*A1)+S1*mp.sqrt(S3*A3))**2
    length_bound=48*S1*S3*(S3*L1+S1*L3)
    coarse=192*(3*m*n*n)*S1*S1*S3*S3
    assert exact<=occ_bound and exact<=length_bound and occ_bound<coarse
    checks.append({'name':f'm={m}: complete incidence bounds','passed':True,
                   'exact_C':str(exact),'occurrence_bound':str(occ_bound),
                   'length_bound':str(length_bound),'old_coarse_bound':str(coarse)})

for m in (4,6,8,10):
    check_box(m)

# Use exact rationals for all displayed polynomial entries.
from fractions import Fraction as Q
def gm(k):
    if k%2:return Q(0)
    l=k//2
    return Q(math.factorial(2*l),math.factorial(l))*math.prod(Q(2*i+3,2) for i in range(l))
assert [gm(k) for k in (0,2,4,6)]==[1,3,45,1575]
pairs=[(1,0),(2,0),(2,1)]
G=[]; Cmat=[]
for p,q in pairs:
    ga=[];ca=[];d=(-1)**q-(-1)**p; degree=p+q
    for s,t in pairs:
        dd=(-1)**t-(-1)**s; other=s+t
        ga.append(d*dd*gm(degree+other))
        ca.append(d*dd*degree*other*(degree+other+1)*gm(degree+other-2))
    G.append(ga);Cmat.append(ca)
assert G==[[12,0,-180],[0,0,0],[-180,0,6300]]
assert Cmat==[[12,0,-180],[0,0,0],[-180,0,11340]]
assert (Cmat[2][2]-Cmat[0][2]**2/Cmat[0][0])/(G[2][2]-G[0][2]**2/G[0][0])==Q(12,5)
checks.append({'name':'R=2 original polynomial matrices and quotient energies','passed':True})

tau=mp.mpf(19)/2+3*mp.sqrt(10)
for n in (101,1001,10001):
    m=n-1; h=mp.pi/(2*n);c=mp.cos(h);C=mp.cot(h);fac=mp.sqrt(mp.mpf(2)/n)
    S1=fac*C*(C-c);S3=fac*((2-mp.mpf(1)/n)*C*C-c*C/n)
    A1=m*fac*C*(5*C-4*c);A3=mp.mpf(m)/n*fac*((9*m+5)*C*C-2*c*C)
    Cocc=12*(S3*mp.sqrt(S1*A1)+S1*mp.sqrt(S3*A3))**2
    T1=m*C*C/mp.sqrt(2*n);w1=mp.sqrt(2)*c*(C-c)/(n**mp.mpf('1.5'))
    prod=T1*(3*T1)*w1*(n*w1)
    N=3*m*n*n;M=3*m*m*n
    B3=216*(mp.mpf(N)*M)**mp.mpf('1.5')+480*mp.sqrt(N*M)
    sigma2=8*mp.sin(h)**2
    checks.append({'name':f'n={n}: asymptotic samples (not proofs)','passed':True,
        'Cocc_ratio_to_limit':str((Cocc/n**7)/(49152*tau/mp.pi**8)),
        'P_ratio_to_limit':str((prod/n**5)/(192/mp.pi**6)),
        'tail_ratio_to_limit':str((16*sigma2*prod*B3/n**12)/(35831808/mp.pi**4))})

note=(ROOT/'PHASE_MOMENTS_AND_ORIGINAL_PATH.md').read_text(encoding='utf-8')
assert '\x00' not in note
assert len(set(__import__('re').findall(r'\\tag\{(IP\d+)\}',note)))==22
assert not __import__('re').search(r'\bplain\b',note,flags=__import__('re').I)
receipt={'observed_at':datetime.now(timezone.utc).isoformat(),
         'scope':'Independent small-box enumeration and exact arithmetic checks; prose proofs establish general formulas.',
         'checks':checks,'all_passed':True}
(ROOT/'VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'all_passed':True,'checks':len(checks)}))
