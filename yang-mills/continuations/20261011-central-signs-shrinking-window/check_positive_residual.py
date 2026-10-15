from pathlib import Path
import sympy as s,json,time
O=Path(__file__).resolve().parent;Q=s.Rational
x,t=s.symbols('x t');start=time.perf_counter();checks=[]
def ck(name,truth):
    ok=bool(truth);checks.append(dict(name=name,passed=ok));assert ok,name
def cm(M):return M.applyfunc(lambda z:s.expand(s.expand_complex(z)))
def eq(A,B):return all(s.expand(v)==0 for v in A-B)
def psd2(M):
    M=cm(M)
    return eq(M,M.H) and M[0,0]>=0 and M[1,1]>=0 and s.expand(M.det())>=0
q=(x+1)*(x+Q(1,4))*(x+4)
P=-Q(43,25)*x**4+x**3/2+Q(3801,400)*x*x+x/2-Q(43,25)
r=s.expand(q-x*P);D=(x+1)*r-q*q/100
for a,b,vals in [(0,1,[0,Q(2388,5),Q(5726,5),Q(16627,10),1650,1375]),(1,Q(3,2),[1375,Q(2475,2),Q(41377,40),Q(63941,80),606,Q(4725,8)]),(Q(3,2),2,[Q(4725,8),Q(2301,4),Q(59021,80),Q(24283,20),Q(11012,5),3984])]:
    ck(f'PST1 complete Bernstein identity {a},{b}',s.expand(400*(r-1-x).subs(x,a+(b-a)*t)-sum(v*s.binomial(5,i)*t**i*(1-t)**(5-i) for i,v in enumerate(vals)))==0)
    ck(f'PST1 complete coefficient signs {a},{b}',all(v>=0 for v in vals))
ck('PST1 full final ray',s.Poly(400*(r-1-x).subs(x,2+t),t).all_coeffs()==[688,6680,22519,31734,17816,3984])
bern=[Q(4251,1024),Q(53731,15360),Q(1301671,384000),Q(553683,128000),Q(225321,32000),Q(20151,1600),Q(8991,400)]
ck('Complete degree-six Bernstein identity',s.expand(D.subs(x,Q(3,2)+t/2)-sum(v*s.binomial(6,i)*t**i*(1-t)**(6-i) for i,v in enumerate(bern)))==0)
ck('All Bernstein coefficients positive',all(v>0 for v in bern))
ck('Small interval lower bound',Q(64,5929)>Q(1,100))
certs=[
('lower original ray',s.Poly(D.subs(x,2+t),t),[Q(171,100),Q(4327,200),Q(166987,1600),Q(191049,800),Q(415683,1600),Q(47439,400),Q(8991,400)]),
('upper resolvent',s.Poly(Q(43,25)*q*q-(x+1)*r,x),[Q(421,25),Q(7447,100),Q(40803,400),Q(21499,400),Q(1009,100),Q(18,25)]),
('contraction',s.Poly(q*q-r,x),[1,Q(439,50),Q(617,16),Q(26251,400),Q(533,16),Q(353,100),0]),
('signed plus',s.Poly(Q(43,25)*q*q+(x+1)*x*P,x),[Q(421,25),Q(7547,100),Q(43303,400),Q(25699,400),Q(817,50),Q(43,25)]),
('signed minus',s.Poly(Q(43,25)*q*q-(x+1)*x*P,x),[Q(86,25),Q(482,25),Q(11093,200),Q(35301,400),Q(1067,16),Q(989,50),Q(43,25)])]
for name,poly,vals in certs:
    ck(name+' exact identity',poly.all_coeffs()==vals);ck(name+' complete sign check',all(v>=0 for v in vals))
ck('Sharp upper constant',s.limit((x+1)*r/q**2,x,s.oo)==Q(43,25))
ck('Full cubic quotient',s.cancel(q/(x+1)**3-1-Q(9,4)*x/(x+1)**2)==0)
cs=[1,Q(256,3125),Q(108,3125),Q(108,3125),Q(256,3125),1]
for ell in range(1,5):
    ck(f'Moment ceiling {ell}',s.cancel((x**ell/(x+1)**5).subs(x,Q(ell,5-ell)))==cs[ell])
I=s.eye(5);Z=I[:,1:3];examples=[]
for n in range(1,7):
    rr=s.Matrix([[2,1,Q(n,7),0],[0,2,1,Q(1,3)],[Q(1,5),0,2,1],[1,Q(n,11),0,2]])
    if n>=5:rr[0,2]+=s.I/3
    L=s.zeros(5);L[1:,1:]=cm(rr.H*rr+s.eye(4));z=Q(n+1,7)
    A=cm((L+z*I)*(L+z*I/4)*(L+4*z*I));Ai=cm(A.inv());G=cm((L+z*I).inv())
    K=cm(z*L*G**2-Q(16,25)*(z/4)*L*cm((L+z*I/4).inv())**2-Q(16,25)*(4*z)*L*cm((L+4*z*I).inv())**2)
    RP=cm(Q(43,25)*z*L**5-z*z*L**4/2-Q(3401,400)*z**3*L**3+Q(19,4)*z**4*L**2+Q(697,100)*z**5*L+z**6*I)
    NN=cm(z**3*Ai-K)
    ck(f'{n}: full R polynomial',eq(RP,z**3*A-A*A*K))
    ck(f'{n}: exact residual kernel',eq(Ai*RP*Ai,NN))
    us=[];ws=[];hs=[];ds=[]
    for dim in [3,4,5]:
        J=I[:,:dim];B=J.H*A*J;u=cm(J*cm(B.inv())*J.H*Z)
        us.append(u);ws.append(cm(A*u-Z));hs.append(cm(Ai*Z-u));ds.append(cm(hs[-1].H*A*hs[-1]))
    vv=[us[1]-us[0],us[2]-us[1]];ee=[cm(A*v) for v in vv]
    ck(f'{n}: actual residual differences',eq(ee[0],ws[1]-ws[0]) and eq(ee[1],ws[2]-ws[1]))
    ck(f'{n}: complete residual telescope',eq(ee[0]+ee[1],-ws[0]))
    for ell in range(6):
        for a,b in [(0,0),(0,1),(1,1)]:
            ck(f'{n}: mixed moment {ell}/{a}{b}',eq(vv[a].H*L**ell*vv[b],ee[a].H*L**ell*Ai**2*ee[b]))
        ck(f'{n}: whole moment ceiling {ell}',psd2(cs[ell]*z**(ell-5)*(ws[0].H*G*ws[0])-hs[0].H*L**ell*hs[0]))
    GR=s.BlockMatrix([[v.H*RP*w for w in vv] for v in vv]).as_explicit()
    GN=s.BlockMatrix([[a.H*NN*b for b in ee] for a in ee]).as_explicit()
    ck(f'{n}: complete Gram map',eq(GR,GN))
    ck(f'{n}: all mixed entries retained',eq(sum((v.H*RP*w for v in vv for w in vv),s.zeros(2)),ws[0].H*NN*ws[0]))
    w=ws[0];h=hs[0];delta=ds[0];br=cm(w.H*G*w);nr=cm(w.H*NN*w)
    ck(f'{n}: lower residual form',psd2(nr-z*br/100))
    ck(f'{n}: upper residual form',psd2(Q(43,25)*z*br-nr))
    ck(f'{n}: residual contraction',psd2(w.H*w-nr))
    ck(f'{n}: retained inverse-energy difference',eq(br-z*z*delta,w.H*L*(L+Q(17,4)*z*I)*Ai*w))
    C=Z.H*K*Z;Y=cm(A*us[0]);T=cm(Y.H*K*Y);M1=Z.H*L*Z;tau=z**-3
    ck(f'{n}: positive full-tail identity',eq(C-T,Z.H*K*A*h+h.H*A*K*Z-z**3*delta+nr))
    lower=C-T+tau*Q(43,25)**2*z*z*M1+(tau**-1+z**3)*delta-z*br/100
    ck(f'{n}: improved raw matrix lower bound',psd2(lower))
    XX=tau*Q(43,25)**2*M1+(tau**-1+Q(43,25)*z)*br
    ck(f'{n}: signed upper comparison',psd2(XX-(C-T)))
    ck(f'{n}: signed lower comparison',psd2(XX+(C-T)))
    xi=cm(G*w)
    ck(f'{n}: original resolvent equation and energy',eq((L+z*I)*xi,w) and eq(br,xi.H*L*xi+z*xi.H*xi))
    ck(f'{n}: positive form lower terms',psd2(nr-z**6*(h.H*h)-z**5*(h.H*L*h)))
    examples.append(dict(n=n,complex=n>=5,delta00=str(delta[0,0]),resolvent_energy00=str(br[0,0]),mixed_R00=str(GR[0,2]),signed_difference00=str((C-T)[0,0])))
result=dict(checks=len(checks),all_passed=all(c['passed'] for c in checks),seconds=time.perf_counter()-start,details=checks,examples=examples,scope='Exact rational complete polynomial certificates and noncommuting nested Hermitian fixtures, including two complex cases and a retained vacuum. These are algebra diagnostics, not Wilson-state measurements.')
(O/'POSITIVE_RESIDUAL_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k not in ['details','examples']}))
