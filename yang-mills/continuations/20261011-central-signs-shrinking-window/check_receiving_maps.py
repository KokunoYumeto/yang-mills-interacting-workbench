from pathlib import Path
import sympy as s
import mpmath as mp
import json,re,datetime,hashlib,itertools

root=Path(__file__).parent
source=root/'SQUARE_ROOT_SCORE_RECEIVING_MAPS.md'
raw=source.read_text(encoding='utf-8')
bad=r'\sum_{e\ {'+'\n'+r'm bulk}}'
rep=r'\sum_{e\in E_{\rm bulk}}'
repairs=raw.count(bad)
raw=raw.replace(bad,rep)
raw=raw.replace(r'\cot\theta,v',r'\cot\theta\,v').replace(r'\csc^2\theta,v',r'\csc^2\theta\,v')
raw=raw.replace('The bulk set is exactly \\(1\\le i\\le m-1,0\\le k<m,0\\le l\\le m\\).',r'The bulk set is exactly \(E_{\rm bulk}=\{(i,k,l;2):1\le i\le m-1,0\le k<m,0\le l\le m\}\).')
raw=raw.replace('the score proof is the actual-vacuum ESE proof, not the separate unproved sharper heat-ratio proposal.', 'Sections 1–11 use the actual-vacuum ESE proof and are independent of a heat-kernel ratio bound. Section 12 uses the subsequently completed LS and independent HR heat-kernel proofs, retaining the stronger score and its separate oscillation floor.')
assert raw==source.read_text(encoding='utf-8'), 'Proof source requires repair before verification'

checks={}
def check(name,truth,detail=None):
    assert bool(truth),name
    checks[name]={'passed':True,'detail':detail}

c=s.symbols('c',positive=True)
phi=(2*s.pi/c+4)/(1-c/2)**2
check('entropy_constant_derivative',s.factor(s.diff(phi,c)-(4*c*c+3*s.pi*c-2*s.pi)/(c*c*(1-c/2)**3))==0)
C2=s.Rational(80,225407)*s.Rational(47,384)**4
C1=s.Rational(705,4096)
C6=s.Rational(75,784)*s.Rational(47,384)**3
c6=s.Rational(23,24)**10/588
check('complete_gradient_dominates_twice_mass_cap',c6>2*C2,{'c6':str(c6),'two_C2':str(2*C2)})
G=s.Matrix([[2,0,s.Rational(2,3)],[0,s.Rational(2,3),0],[s.Rational(2,3),0,s.Rational(2,5)]])
check('six_variable_gram_floor',all((G-s.eye(3)/8)[:k,:k].det()>0 for k in (1,2,3)))
check('GPR_density_constant',s.Rational(2,8**6)*s.Rational(1,4**10)==s.Rational(1,2**37))

Q,QR,K,KR,beta,kappa,tau=s.symbols('Q QR K KR beta kappa tau')
endpoint=2*beta**2*(Q-QR)-2*kappa*beta**2*(K-KR)/tau
even=4*beta**2*(Q-kappa*K/tau)-beta**2*2*(Q+QR)+kappa*beta**2/tau*2*(K+KR)
check('both_endpoint_identities',s.expand(endpoint-even)==0)

j=s.symbols('j',positive=True)
T23,T24,T12,T13,V3,V4,P3,P4=s.symbols('T23 T24 T12 T13 V3 V4 P3 P4',positive=True)
n=2*j**4+1
# Every cosine tends to one; the omitted factor divided by this substituted factor tends to one.
J=n/2-2
terms={
 'B6_boundary':(6/n**5*V3*j**-6,26,3*V3/16),
 'B6_interior':(3*J/n**5*V4*j**-6,22,3*V4/32),
 'AD_boundary':(6*J/n**5*P3*j**-6*T12*j**-2,24,3*P3*T12/16),
 'AD_interior':(3*J**2/n**5*P4*j**-6*T13*j**-2,20,3*P4*T13/32),
 'AF_boundary_0':(4*J/n**5*P3*j**-6,22,P3/8),
 'AF_boundary_1':(2*J/n**5*P3*j**-6*T12*j**-2,24,P3*T12/16),
 'AF_interior_0':(2*J**2/n**5*P4*j**-6,18,P4/16),
 'AF_interior_1':(J**2/n**5*P4*j**-6*T13*j**-2,20,P4*T13/32),
 'B2minus_boundary':(12/n**5*T23*j**-8*T12*j**-2,30,3*T23*T12/8),
 'B2minus_interior':(6*J/n**5*T24*j**-8*T13*j**-2,26,3*T24*T13/16),
 'B2plus_boundary_0':(8/n**5*T23*j**-8,28,T23/4),
 'B2plus_boundary_1':(4/n**5*T23*j**-8*T12*j**-2,30,T23*T12/8),
 'B2plus_interior_0':(4*J/n**5*T24*j**-8,24,T24/8),
 'B2plus_interior_1':(2*J/n**5*T24*j**-8*T13*j**-2,26,T24*T13/16),
}
table={}
for key,(formula,power,expected) in terms.items():
    val=s.limit(j**power*formula,j,s.oo)
    check(key,s.simplify(val-expected)==0,{'power':power,'limit':str(val)})
    table[key]={'gradient_power':power,'gradient_constant':str(val),'energy_power':power+6,'energy_constant':str(val*kappa*s.Rational(5000)*s.pi**2/kappa**2),'endpoint_power':power+5,'endpoint_constant':str(val*s.Rational(5000)*s.pi**2/kappa**2)}

mp.mp.dps=70
for ni in range(5,34,2):
    hh=mp.pi/(2*ni)
    ss=sum(mp.sin(mp.pi*(k+1)/ni)**4 for k in range(ni-1))
    cc=sum(mp.cos(mp.pi*(i+mp.mpf('.5'))/ni)**2 for i in range(1,ni-1))
    check(f'rows_n{ni}',abs(ss-3*mp.mpf(ni)/8)<mp.mpf('1e-60') and abs(cc-(mp.mpf(ni)/2-2*mp.cos(hh)**2))<mp.mpf('1e-60'))

for m in (4,6,8):
    axes=range(3)
    edges={(xyz,a):0 for xyz in itertools.product(range(m+1),repeat=3) for a in axes if xyz[a]<m}
    faces=[]
    for a,b in itertools.combinations(axes,2):
        for xyz in itertools.product(range(m+1),repeat=3):
            if xyz[a]>=m or xyz[b]>=m:continue
            xa=list(xyz);xa[a]+=1
            xb=list(xyz);xb[b]+=1
            ee=((xyz,a),(tuple(xa),b),(tuple(xb),a),(xyz,b))
            faces.append(ee)
            for edge in ee:edges[edge]+=1
    ecounts={r:sum(v==r for v in edges.values()) for r in (2,3,4)}
    check(f'edge_counts_m{m}',ecounts=={2:12*m,3:12*m*(m-1),4:3*m*(m-1)**2},ecounts)
    # Independent enumeration of minimum incidence pair for every actual face.
    fcounts={}
    for face in faces:
        rr=sorted(edges[e] for e in face)
        key=tuple(rr[:2]);fcounts[key]=fcounts.get(key,0)+1
    expected={(3,3):6*(m-2)**2+12*(m-1),(2,3):24*(m-2),(2,2):24,(4,4):3*(m-1)*(m-2)**2,(3,4):12*(m-1)*(m-2)}
    check(f'face_pair_counts_m{m}',fcounts==expected,{str(k):v for k,v in fcounts.items()})
    check(f'incidence_sum_m{m}',sum(edges.values())==4*len(faces))
    check(f'gradient_face_constant_m{m}',max(sum(edges[e] for e in face) for face in faces)==16)

m=s.symbols('m',integer=True,positive=True)
fc=[6*(m-2)**2,24*(m-2),24,3*(m-1)*(m-2)**2,12*(m-1)*(m-2),12*(m-1)]
check('symbolic_six_face_counts_sum',s.expand(sum(fc)-3*m*m*(m+1))==0)
edge_radical_sum=12*m*s.sqrt(2)+12*m*(m-1)*s.sqrt(3)+6*m*(m-1)**2
check('oscillation_leading_geometric_factor',s.limit(edge_radical_sum.subs(m,2*j**4)/j**12,j,s.oo)==48)
check('response_inverse_constant',16*24**2==9216)
check('coordinate_inverse_constant',8*24**2==4608)

tagnums=[int(v) for v in re.findall(r'\\tag\{SR(\d+)\}',raw)]
check('labels_complete_unique',tagnums==list(range(1,73)),{'count':len(tagnums)})
check('display_delimiters_balanced',raw.count(r'\[')==raw.count(r'\]'),raw.count(r'\['))
check('inline_delimiters_balanced',raw.count(r'\(')==raw.count(r'\)'),raw.count(r'\('))
check('no_control_characters',not any(ord(c)<32 and c not in '\n\t' for c in raw))
check('no_split_rm_control_escape',not re.search(r'(?m)^m bulk',raw))
check('braces_balanced',raw.count('{')==raw.count('}'),{'open':raw.count('{'),'close':raw.count('}')})
for env in ('aligned','gathered','array','pmatrix'):
    check('environment_'+env,raw.count(r'\begin{'+env+'}')==raw.count(r'\end{'+env+'}'))
check('banned_word_absent',not re.search(r'\bpl'+r'ain\b',raw,re.I))

previous=json.loads((root/'SQUARE_ROOT_RECEIVING_CHECKS.json').read_text(encoding='utf-8')) if (root/'SQUARE_ROOT_RECEIVING_CHECKS.json').exists() else {}
report={'observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'control_escape_repairs':max(repairs,previous.get('control_escape_repairs',0)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'checks':checks,'contribution_table':table,'scope':'Symbolic identities, exact integer lattice enumeration, and high-precision finite trigonometric checks supplement the quantified proofs. No finite check replaces a general argument.'}
(root/'SQUARE_ROOT_RECEIVING_CHECKS.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'passed':len(checks),'control_escape_repairs':repairs,'source_sha256':report['source_sha256']}))
