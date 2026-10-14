from pathlib import Path
import itertools,json
import numpy as np
import mpmath as mp
O=Path(__file__).resolve().parent;rows=[];rng=np.random.default_rng(2026101404)
def yes(name,x):rows.append(dict(name=name,passed=bool(x)))
def eq(name,a,b,tol=1e-10):
    err=float(np.max(np.abs(np.asarray(a)-np.asarray(b))));scale=1+float(np.max(np.abs(a)))+float(np.max(np.abs(b)))
    rows.append(dict(name=name,passed=bool(err<tol*scale),error=err))
for case in range(10):
    w=rng.normal(size=(8,7));psi2=np.exp(2*w);psi2/=psi2.mean();rho=psi2.mean(axis=0);h=rho[None,:]/psi2
    rr=rng.normal(size=psi2.shape);bb=rng.normal(size=psi2.shape)
    eq(f'full actual conditional density identity{case}',np.mean(psi2*h*rr*bb),np.mean(rho[None,:]*rr*bb))
    eq(f'complete squared reweighted source identity{case}',np.mean(psi2*(h*bb)**2),np.mean(rho[None,:]*h*bb**2))
    osc=np.ptp(w,axis=0);yes(f'every conditional density ratio bound{case}',np.all(h<=np.exp(2*osc)[None,:]*(1+1e-12)))
    e=np.maximum(rng.uniform(0,2,size=7),rng.uniform(0,2,size=7));p=rho/rho.sum()
    yes(f'actual outside marginal exponent twenty-three{case}',np.sum(p*e**23)>=(np.sum(p*e**2))**11.5-1e-12)
mp.mp.dps=180;values=[]
old=json.loads((O.parent/'quantitative_loop_owner_20261014/QUANTITATIVE_LOOP_CHECKS.json').read_text())['original_regulator_floors']
for j in [1,2,3,10,100]:
    k=mp.mpf(4)/5;a=1/(mp.mpf(100)*j);L=j**4;N=3*(2*L)*(2*L+1)**2;M=3*(2*L)**2*(2*L+1);b=1/(k*a*a);c=2/(k*a)
    G=4*mp.pi**2*N*c*c;W=4*b*M/k+(3*N-1)*c;Bw=4*b*M/k+G;Q=3+2*(1+mp.sqrt(2))*mp.sqrt(G)+Bw+3*N*W+42*G
    QC=Q+6*(N-4)*(W+2*G)+(6+2*mp.sqrt(2))*G;RC=b*mp.exp(-16*mp.pi**2*c)/(k*QC);C4=532082;A4=8*mp.pi*c
    delta=min(mp.pi/4,RC/(8*C4*A4));ec=RC/(4*C4*mp.log(mp.cot(delta/2)));JJ=2*W+4*G+2*c+4*mp.sqrt(G)
    logBP=-56*mp.pi**2*c-mp.log(4)-7*mp.log(48*mp.pi)-21*mp.log(2*JJ*mp.sqrt(7))
    logm=mp.log(2*k*k)+logBP+23*mp.log(ec);E=4*k**3*JJ**2
    yes(f'complete original volume polynomial{j}',N==24*j**12+24*j**8+6*j**4 and M==24*j**12+12*j**8)
    AQ=207360000+1105920000*mp.pi**2;AJ=1920000+15360000*mp.pi**2;d0=3200*mp.pi**2/k
    logA=mp.log(k*k/2)-7*mp.log(48*mp.pi)-21*mp.log(2*mp.sqrt(7)*AJ/k**2)+23*mp.log(10000/(4*C4*d0*AQ))
    asymptotic_error=logm+869*mp.log(j)+84800*mp.pi**2*j/k-logA
    yes(f'every local floor factor positive{j}',min(RC,delta,ec,QC,JJ,E)>0)
    eq(f'local endpoint first contribution ratio{j}',float(4*C4*A4*delta/RC),.5)
    eq(f'local endpoint second contribution ratio{j}',float(2*C4*ec*mp.log(mp.cot(delta/2))/RC),.5)
    yes(f'original seven-link ball radius bound{j}',16*mp.pi*c/(2*JJ)<=1)
    val=dict(j=j,kappa='4/5',N=N,M=M,log10_R_C=mp.nstr(mp.log10(RC),25),log10_e_C=mp.nstr(mp.log10(ec),25),log10_m_C=mp.nstr(logm/mp.log(10),25),log_mass_over_j=mp.nstr(logm/j,25),log_asymptotic_quotient=mp.nstr(asymptotic_error,25),precision_digits=180)
    if j<=3:
        previous=mp.mpf(old[j-1]['log10_mass_floor']);yes(f'local formula improves prior evaluated bound{j}',logm/mp.log(10)>previous)
        val['previous_log10_floor']=str(previous)
    values.append(val)
yes('exact limiting coefficient convergence diagnostic',abs(mp.mpf(values[-1]['log_asymptotic_quotient']))<abs(mp.mpf(values[-2]['log_asymptotic_quotient'])))
for t in [.0001,.01,.1,.5,1.]:
    tt=mp.mpf(t);v=(tt-mp.sin(tt))/(2*mp.pi)
    yes(f'original radius-two ball polynomial inequality{t}',v>=tt**3/(48*mp.pi))
# Original four crossing links with arbitrary SU2 values on every spectator.
I=np.eye(2,dtype=complex);J=[-1j*np.array([[0,1],[1,0]],complex),-1j*np.array([[0,-1j],[1j,0]],complex),-1j*np.array([[1,0],[0,-1]],complex)]
def su2():
    q=rng.normal(size=4);q/=np.linalg.norm(q);return q[0]*I+sum(q[i+1]*J[i] for i in range(3))
def shift(p,a):q=list(p);q[a]+=1;return tuple(q)
edges=[];faces=[]
for p in itertools.product(range(-1,2),repeat=3):
    for a in range(3):
        if p[a]<1:edges.append((p,a))
        for b in range(a+1,3):
            if p[a]<1 and p[b]<1:faces.append([((p,a),1),((shift(p,a),b),1),((shift(p,b),a),-1),((p,b),-1)])
cross=[(((0,0,0),0),1),(((1,0,0),2),1),(((0,0,1),0),-1),(((0,0,0),2),-1)];ci=faces.index(cross)
rule=np.array([I,-I,J[0],-J[0],J[1],-J[1],J[2],-J[2]]);grid=np.array(list(itertools.product(range(8),repeat=4)))
for trial in range(3):
    links={edge:su2() for edge in edges};links.update({edge:rule[grid[:,i]] for i,(edge,sgn) in enumerate(cross)});traces=[]
    for word in faces:
        hol=np.broadcast_to(I,(len(grid),2,2)).copy()
        for edge,sgn in word:
            mat=links[edge]
            if sgn<0:mat=mat.conj().swapaxes(-1,-2)
            hol=hol@mat
        traces.append(np.trace(hol,axis1=1,axis2=2).real)
    tc=traces[ci];eq(f'conditional crossing Haar mean at arbitrary outside{trial}',np.mean(tc),0)
    eq(f'conditional crossing exact squared norm{trial}',np.mean(tc**2),1)
    for i,tr in enumerate(traces):eq(f'full conditional face pairing outside{trial}/face{i}',np.mean(tr*tc),1 if i==ci else 0)
    pot=2*12500*36-12500*sum(traces);eq(f'complete conditional potential coefficient outside{trial}',np.mean(tc*pot),-12500)
# Weighted integration-by-parts identity on the original four-link trace and
# one independent original outside-link trace, with every density derivative.
n=64;ang=np.arange(1,n+1)*np.pi/(n+1);nodes=2*np.cos(ang);weight=2*np.sin(ang)**2/(n+1)
x,y=np.meshgrid(nodes,nodes,indexing='ij');ww=weight[:,None]*weight[None,:];gx=4-x*x;gy=1-y*y/4
for trial,(alpha,beta) in enumerate([(.35,-.04),(-.8,.11),(1.2,-.3)]):
    z=alpha*y+beta*y*y;zy=alpha+2*beta*y;dz=gy*2*beta-.75*y*zy
    rr=x*y+.3*x*x+.4*y*y;rx=y+.6*x;ry=x+.8*y
    sx=.2+.1*y;sy=.7+.1*x;ds=-3*x*sx-.75*y*sy
    dr=.6*gx-3*x*rx+.8*gy-.75*y*ry
    left=np.sum(ww*np.exp(z)*x*(dr+gx*rx*sx+gy*ry*sy))
    bracket=-3*x-gx*sx+x*(dz+gy*zy*zy-gy*zy*sy-ds)
    right=np.sum(ww*np.exp(z)*rr*bracket)
    eq(f'all original conditional density derivative terms{trial}',left,right)
out=dict(all_passed=all(r['passed'] for r in rows),checks=len(rows),rows=rows,evaluated_original_bounds=values,scope='Exact conditional density algebra and retained probability weights, exponent-23 convexity, original radius-two ball inequality and full original-parameter bound evaluations. Synthetic conditional arrays test only algebra; they are not computed Yang–Mills ground states.')
(O/'LOCAL_MEMORY_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(all_passed=out['all_passed'],checks=len(rows),failed=[r for r in rows if not r['passed']],values=values)));assert out['all_passed']
