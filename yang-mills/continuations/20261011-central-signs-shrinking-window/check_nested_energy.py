from pathlib import Path
import sympy as s,json,time,math
import mpmath as mp
O=Path(__file__).resolve().parent;start=time.perf_counter();checks=[];Q=s.Rational
def ck(name,truth):
    ok=bool(truth);checks.append(dict(name=name,passed=ok));assert ok,name
def psd2(a):return a==a.T and a[0,0]>=0 and a[1,1]>=0 and a.det()>=0
x,t=s.symbols('x t');q=(x+1)*(x+Q(1,4))*(x+4)
P=-Q(43,25)*x**4+x**3/2+Q(3801,400)*x*x+x/2-Q(43,25)
k=x/(x+1)**2-Q(4,25)*x/(x+Q(1,4))**2-Q(64,25)*x/(x+4)**2
R=400*(q-x*P)
ck('Complete signed quotient',s.cancel(k-x*P/q**2)==0)
bern=[(0,1,[400,Q(4788,5),Q(8526,5),Q(23027,10),2370,2175]),(1,Q(3,2),[2175,Q(4155,2),Q(76577,40),Q(137541,80),1566,Q(12725,8)]),(Q(3,2),2,[Q(12725,8),Q(6461,4),Q(145421,80),Q(46683,20),Q(16812,5),5184])]
for a,b,vals in bern:
    ck(f'Complete Bernstein identity [{a},{b}]',s.expand(R.subs(x,a+(b-a)*t)-sum(v*s.binomial(5,i)*t**i*(1-t)**(5-i) for i,v in enumerate(vals)))==0)
    ck(f'All positive Bernstein coefficients [{a},{b}]',all(v>0 for v in vals))
ck('All large-x original remainder terms',s.Poly(s.expand(R.subs(x,2+t)),t).all_coeffs()==[688,6680,22519,31734,18216,5184])
positive=[Q(120787,2500),Q(3236561,10000),Q(36737113,40000),Q(244058747,160000),Q(64571959,40000),Q(38345957,40000),Q(4687,16),Q(109091,2500),Q(1849,625)]
ck('Complete squared-kernel polynomial',s.Poly(Q(43,25)**2*q**3-x*P**2,x).all_coeffs()==positive)
ck('Sharp square coefficient and all positive lower terms',all(v>0 for v in positive) and s.limit(x*P**2/q**3,x,s.oo)==Q(43,25)**2)
Z=s.eye(5)[:,1:3];I=s.eye(5);example=None
for n in range(1,13):
    rr=s.Matrix([[2,1,Q(n,7),0],[0,2,1,Q(1,3)],[Q(1,5),0,2,1],[1,Q(n,11),0,2]])
    L=s.zeros(5);L[1:,1:]=rr.T*rr+s.eye(4);z=Q(n+1,7)
    A=(L+z*I)*(L+z*I/4)*(L+4*z*I);Ai=A.inv()
    K=z*L*(L+z*I).inv()**2-Q(16,25)*(z/4)*L*(L+z*I/4).inv()**2-Q(16,25)*(4*z)*L*(L+4*z*I).inv()**2
    us=[];ws=[];hs=[];ds=[];Bs=[];Js=[]
    for dim in [3,4,5]:
        J=I[:,:dim];B=J.T*A*J;F=J.T*Z;u=J*B.inv()*F;w=A*u-Z;h=Ai*Z-u
        Js.append(J);Bs.append(B);us.append(u);ws.append(w);hs.append(h);ds.append(h.T*A*h)
    v0=us[1]-us[0];v1=us[2]-us[1];d0=v0.T*A*v0;d1=v1.T*A*v1
    ck(f'{n}: exact typed compression',Bs[0]==Bs[1][:3,:3])
    ck(f'{n}: original projected residual correction',v0==-Js[1]*Bs[1].inv()*Js[1].T*ws[0])
    ck(f'{n}: original form orthogonality',v0.T*A*v1==s.zeros(2) and us[0].T*A*v0==s.zeros(2))
    ck(f'{n}: two complete defect differences',ds[0]-ds[1]==d0 and ds[1]-ds[2]==d1)
    ck(f'{n}: exact terminal state and finite tail',hs[2]==s.zeros(5,2) and hs[0]==v0+v1 and ds[0]==d0+d1)
    ck(f'{n}: positive increments and retained total bound',psd2(d0) and psd2(d1) and psd2(z**-3*(Z.T*Z)-ds[0]))
    C=Z.T*K*Z;Y=A*us[0];T=Y.T*K*Y;M1=Z.T*L*Z;eta=z**-3
    ck(f'{n}: strengthened full matrix lower bound',psd2(C-T+eta*Q(43,25)**2*z*z*M1+(eta**-1+z**3)*ds[0]))
    cross=sum((Z.T*K*A*v+v.T*A*K*Z for v in [v0,v1]),s.zeros(2))
    tail=sum((v.T*A*K*A*w for v in [v0,v1] for w in [v0,v1]),s.zeros(2))
    ck(f'{n}: entire signed double sum',C-T==cross-tail)
    ck(f'{n}: filtered cross terms remain nonzero',v0.T*A*K*A*v1!=s.zeros(2))
    if n==1:
        example=dict(L=[[str(v) for v in row] for row in L.tolist()],zeta=str(z),filtered_cross_00=str((v0.T*A*K*A*v1)[0,0]),form_cross_00=str((v0.T*A*v1)[0,0]))
mp.mp.dps=60
def bounds(j,kappa=mp.mpf(4)/5,theta=mp.mpf(1)):
    j=mp.mpf(j);a=1/(100*j);g2=kappa*a/2;zeta=theta*kappa/j;qq=100*j
    N=3*qq*(qq+1)**2;M=3*qq**2*(qq+1);cross=12*qq*(qq+1);steps=j**4-50*j
    lam=min(2*M,6*g2*mp.sqrt(N*M))+2*cross;budget=min(4*M,lam)
    u2=min((4*M)**2,lam**2+16*g2**2);source=min(a*a*M*M,a*a*M*budget,a*a*u2/4)
    energy=4*kappa*a*a*min(M,budget)
    return dict(j=j,a=a,steps=steps,source=source,energy=energy,cross=mp.mpf(43)/25*mp.sqrt(energy*source/(zeta*steps)),quadratic=source/steps)
vals=[]
for j in [4,8,16,64,256,1024,10**4,10**8,10**16]:
    v=bounds(j);ck(f'Original full finite bounds j={j}',v['steps']>0 and v['cross']>0 and v['quadratic']>0)
    vals.append({k:mp.nstr(vv,45) for k,vv in v.items()})
kappa=mp.mpf(4)/5;lam=9*kappa+24;v=bounds(10**16)
ck('Full cross ceiling tends to exact coefficient172',abs(v['cross']*mp.sqrt(10**16)/(172*lam**mp.mpf('1.5'))-1)<mp.mpf('1e-15'))
ck('Full one-sided ceiling tends to exact coefficient2500',abs(v['quadratic']*(mp.mpf(10)**16)**2/(2500*lam**2)-1)<mp.mpf('1e-15'))
out=dict(checks=len(checks),all_passed=all(c['passed'] for c in checks),seconds=time.perf_counter()-start,details=checks,example=example,original_path_bounds=vals,scope='Exact rational complete multiplier, nested noncommuting matrix identities and full original-parameter bound evaluations. Matrix fixtures are not Yang–Mills ground states.')
(O/'NESTED_ENERGY_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k not in ['details','original_path_bounds','example']}))
