from pathlib import Path
import json, math, hashlib
import numpy as np
import mpmath as mp

root=Path(__file__).resolve().parent
mp.mp.dps=65

def constants(n):
    n=mp.mpf(n); m=n-1; h=mp.pi/(2*n); s=mp.sin(h); c=mp.cos(h); C=mp.cot(h)
    S1=mp.sqrt(2/n)*C*(C-c)
    S3=mp.sqrt(2/n)*((2-1/n)*C*C-c*C/n)
    A1=m*mp.sqrt(2/n)*C*(5*C-4*c)
    A3=m/n*mp.sqrt(2/n)*((9*m+5)*C*C-2*c*C)
    Cocc=12*(S3*mp.sqrt(S1*A1)+S1*mp.sqrt(S3*A3))**2
    Hocc=9*(S3*A1+S1*A3+2*mp.sqrt(S1*A1*S3*A3))**2
    T=mp.sqrt(2/n)*C; vstar=mp.sqrt(2/n)*c
    Q3=(2/n)**mp.mpf('1.5')*(3*C-mp.cot(3*h))/4
    t=mp.sqrt(2)*c*c/(n**mp.mpf('1.5')*s)
    R2=2*(C-c)/n**2*(T**3/3+T/2+Q3/6+vstar/(2*s)*(T*T+1)+vstar*vstar*(1+n*vstar*vstar)*T/(4*s*s))
    R2c=R2-S1*t*t
    return dict(S1=S1,S3=S3,A1=A1,A3=A3,Cocc=Cocc,Hocc=Hocc,R1=S1*t,R2=R2,R2c=R2c,t=t)

def lattice(n):
    m=n-1
    vertices=[(i,k,l) for i in range(n) for k in range(n) for l in range(n)]
    edges=[(v,d) for v in vertices for d in range(3) if v[d]<m]
    edge_index={e:i for i,e in enumerate(edges)}
    def path(v):
        i,k,l=v
        return [edge_index[((0,0,t),2)] for t in range(l)]+[edge_index[((0,t,l),1)] for t in range(k)]+[edge_index[((t,k,l),0)] for t in range(i)]
    paths={v:path(v) for v in vertices}
    tree=set(e for p in paths.values() for e in p)
    chords=[e for e in range(len(edges)) if e not in tree]
    def v(r):return math.sqrt(2/n)*math.cos(math.pi*(r+.5)/n)
    def w(r):return -math.sqrt(2/n)*math.sin(math.pi*(r+1)/n)
    W=np.r_[0,np.cumsum([w(r) for r in range(m)])]
    a=[]; b=[]; rr=[]; Ts=[]; Rs=[]; words=[]
    for ce in chords:
        start,d=edges[ce]; i,k,l=start; end=list(start);end[d]+=1;end=tuple(end)
        word=[(e,1) for e in paths[start]]+[(ce,1)]+[(e,-1) for e in reversed(paths[end])]
        tv=np.zeros(len(edges));rv=np.zeros(len(edges))
        for e,sign in word:tv[e]+=sign;rv[e]+=1
        words.append(word);Ts.append(tv);Rs.append(rv)
        a.append(-v(i)*w(k)/math.sqrt(2*n) if d==1 else 0)
        b.append(w(k)*v(l)/math.sqrt(2*n) if d==1 else -v(k)*w(l)/math.sqrt(2*n))
        pstart=(v(l)*W[k]-v(0)*W[l])/math.sqrt(2*n)
        ii,kk,ll=end
        pend=(v(ll)*W[kk]-v(0)*W[ll])/math.sqrt(2*n)
        Vedge= w(k)*v(l)/math.sqrt(2*n) if d==1 else -v(k)*w(l)/math.sqrt(2*n)
        rr.append(pstart+Vedge+pend)
    return dict(n=n,m=m,edges=edges,paths=paths,chords=chords,words=words,a=np.array(a),b=np.array(b),r=np.array(rr),T=np.array(Ts),R=np.array(Rs))

def qmul(p,q):
    return np.r_[p[0]*q[0]-np.dot(p[1:],q[1:]),p[0]*q[1:]+q[0]*p[1:]+np.cross(p[1:],q[1:])]
def qinv(q):return q*np.array([1,-1,-1,-1])
def qexp(z):
    r=np.linalg.norm(z)
    return np.r_[math.cos(r/2),z*(math.sin(r/2)/r if r else .5)]
def qprod(values):
    out=np.array([1.,0,0,0])
    for value in values:out=qmul(out,value)
    return out
def data(lat,U):
    Z=np.array([qprod([U[e] if sg==1 else qinv(U[e]) for e,sg in word]) for word in lat['words']])
    q=2*Z[:,1:]; c=Z[:,0];u=lat['a']@q;v=lat['b']@q
    return c,q,u,v,float(u@v)
def root_vector(lat,U,e,z):
    start,_=lat['edges'][e]
    t=qprod([U[f] for f in lat['paths'][start]])
    return qmul(qmul(qinv(t),np.r_[0,z]),t)[1:]
def word_hessian(lat,c,q,e,alpha,f,beta):
    ea=np.eye(3)[alpha];eb=np.eye(3)[beta]
    te=lat['T'][:,e];tf=lat['T'][:,f];re=lat['R'][:,e];rf=lat['R'][:,f]
    Je=c[:,None]*te[:,None]*ea+.5*re[:,None]*np.cross(ea,q)
    Jf=c[:,None]*tf[:,None]*eb+.5*rf[:,None]*np.cross(eb,q)
    gamma=float(e in lat['paths'][lat['edges'][f][0]])+.5*(e==f)
    axb=np.cross(ea,eb)
    H=-.25*(te*tf*q[:,alpha])[:,None]*eb+.5*rf[:,None]*np.cross(eb,Je)
    H+=gamma*(c[:,None]*tf[:,None]*axb+.5*rf[:,None]*np.cross(axb,q))
    return Je,Jf,H

report={'finite_rows':[],'hessian_checks':[],'algebra_checks':{},'asymptotic_checks':{}}
for n in [5,7,9]:
    lat=lattice(n);k=constants(n);aa=np.abs(lat['a']);bb=np.abs(lat['b']);R=lat['R'];rr=lat['r']
    sums={'S1':aa.sum(),'S3':bb.sum(),'A1':aa@(R*R).sum(1),'A3':bb@(R*R).sum(1),'R1':aa@rr,'R2':aa@(rr*rr)}
    sums['R2c']=sums['R2']-sums['R1']**2/sums['S1']
    errors={key:abs(val-float(k[key]))/max(1,abs(val)) for key,val in sums.items()}
    assert max(errors.values())<2e-13,errors
    for row,word in zip(R,lat['words']):assert row.max()<=2 and row.sum()==len(word)
    report['finite_rows'].append({'n':n,'N':len(lat['edges']),'chords':len(lat['chords']),'relative_errors':errors})

rng=np.random.default_rng(20261011)
lat=lattice(5);U=rng.normal(size=(len(lat['edges']),4));U/=np.linalg.norm(U,axis=1)[:,None]
c,q,u,v,S=data(lat,U)
test_pairs=[]
for ix,ce in enumerate(lat['chords'][:4]):
    test_pairs.append((ce,ix%3,ce,(ix+1)%3))
    ancestor=lat['words'][ix][0][0]
    test_pairs.append((ancestor,(ix+1)%3,ce,ix%3))
for _ in range(4):test_pairs.append(tuple([int(rng.integers(len(U))),int(rng.integers(3)),int(rng.integers(len(U))),int(rng.integers(3))]))
eps=2e-4
for e,al,f,be in test_pairs:
    Je,Jf,H=word_hessian(lat,c,q,e,al,f,be)
    _,_,Ht=word_hessian(lat,c,q,f,be,e,al)
    assert np.max(np.abs(H-Ht))<2e-14
    ae=lat['a']@Je;af=lat['a']@Jf;bevec=lat['b']@Je;bf=lat['b']@Jf
    exact=v@(lat['a']@H)+u@(lat['b']@H)+ae@bf+bevec@af
    ze=root_vector(lat,U,e,np.eye(3)[al]);zf=root_vector(lat,U,f,np.eye(3)[be])
    def value(te,tf):
        W=U.copy()
        if e==f:W[e]=qmul(qexp(te*ze+tf*zf),U[e])
        else:
            W[e]=qmul(qexp(te*ze),U[e]);W[f]=qmul(qexp(tf*zf),U[f])
        return data(lat,W)[-1]
    finite=(value(eps,eps)-value(eps,-eps)-value(-eps,eps)+value(-eps,-eps))/(4*eps*eps)
    error=abs(exact-finite)
    assert error<5e-7,(e,al,f,be,exact,finite,error)
    report['hessian_checks'].append({'indices':[e,al,f,be],'exact':exact,'finite_difference':finite,'absolute_error':error})

a=lat['a'];r=lat['r'];us=[(a*r**k)@q for k in range(5)]
delta=us[0]@us[2]-us[1]@us[1]
mat=.5*(np.outer(a,a*r*r)+np.outer(a*r*r,a))-np.outer(a*r,a*r)
assert abs(delta-np.sum(mat*(q@q.T)))<1e-10
assert np.max(abs(np.diag(mat)))<1e-15
rank=int(np.linalg.matrix_rank(mat,tol=1e-10));assert rank<=3
div=0.
for ealpha in np.eye(3):
    div+=ealpha@(.25*(np.cross(np.cross(ealpha,us[1]),us[1])+np.cross(us[0],np.cross(ealpha,us[2]))))
assert abs(div-delta/2)<1e-11
t=float(constants(5)['t']);uc1=us[1]-t*us[0];uc2=us[2]-2*t*us[1]+t*t*us[0]
assert abs(delta-(us[0]@uc2-uc1@uc1))<1e-11
report['algebra_checks']={'coefficient_rank':rank,'signed_contraction':float(delta),'divergence':float(div),'centered_identity_error':float(abs(delta-(us[0]@uc2-uc1@uc1)))}

tau=mp.mpf(19)/2+3*mp.sqrt(10)
j=mp.mpf(10000);n=2*j**4+1;k=constants(n);beta=200*mp.sqrt(2)*j*mp.sin(mp.pi/(2*n));xi=10000*j*j
tests={
    'Hocc':(k['Hocc']/n**8,36864*tau*tau/mp.pi**8),
    'R2':(k['R2']/mp.sqrt(n),304*mp.sqrt(2)/(3*mp.pi**4)),
    'R2c':(k['R2c']/mp.sqrt(n),208*mp.sqrt(2)/(3*mp.pi**4)),
    'Gupper':(64*beta*beta*k['S1']**2*k['S3']**2/j**18,83886080000/mp.pi**6),
    'Eupper':(4*beta*beta*k['Cocc']/j**22,125829120000*tau/mp.pi**6),
    'Pupper':(4*beta*beta*k['Hocc']/j**26,188743680000*tau*tau/mp.pi**6),
    'Uupper':((4*mp.sqrt(xi)*k['S1']**2+k['S1']*k['R2c']/2)/j**13,102400/mp.pi**4),
    'Ucorrection':((k['S1']*k['R2c']/2)/j**8,3328/(3*mp.pi**6))}
for key,(value,limit) in tests.items():
    error=abs(value/limit-1);assert error<mp.mpf('1e-12'),(key,error)
    report['asymptotic_checks'][key]={'j':str(j),'value':str(value),'limit':str(limit),'relative_error':str(error)}
ledger=json.loads((root/'RAW_S6_SOURCE_USE_LEDGER.json').read_text(encoding='utf-8'))
report['source_integrity']=[{'provider':r['provider_id'],'matches':hashlib.sha256((root/r['path']).read_bytes()).hexdigest()==r['sha256']} for r in ledger['providers']]
assert all(x['matches'] for x in report['source_integrity'])
report['status']='all checks passed'
(root/'RAW_S6_HESSIAN_CHECKS.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'status':report['status'],'finite_boxes':len(report['finite_rows']),'hessian_checks':len(report['hessian_checks']),'maximum_hessian_error':max(r['absolute_error'] for r in report['hessian_checks']),'coefficient_rank':rank}))
