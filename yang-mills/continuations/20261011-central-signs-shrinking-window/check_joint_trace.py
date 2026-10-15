from pathlib import Path
import json
import numpy as np
import sympy as sp
import mpmath as mp
O=Path(__file__).resolve().parent;rows=[];rng=np.random.default_rng(2026101501)
def yes(name,ok):rows.append(dict(name=name,passed=bool(ok)))
def eq(name,a,b,tol=3e-11):
    err=float(np.max(np.abs(np.asarray(a)-np.asarray(b))));scale=1+float(np.max(np.abs(a)))+float(np.max(np.abs(b)))
    rows.append(dict(name=name,passed=err<=tol*scale,error=err))
l,z=sp.symbols('lambda zeta',positive=True)
rem=l**3*(3*z+2*l)/(z*z*(l+z)**2)
yes('complete rational remainder identity',sp.cancel(z*l/(l+z)**2-l/z+2*l*l/z**2-rem)==0)
e=sp.Rational(1,4);R=sp.Integer(4);cm=4*e/(1+e)**2;cp=4*R/(1+R)**2
D1=cm/e+cp/R-1;D2=cm/e**2+cp/R**2-1;B3=cm/e**3+cp/R**3
yes('every original coefficient exact',(cm,cp,D1,D2,B3)==(sp.Rational(16,25),sp.Rational(16,25),sp.Rational(43,25),sp.Rational(232,25),sp.Rational(4097,100)))
dw=(z*sp.Rational(1,2)/(z+sp.Rational(1,2))**2+z*sp.Rational(3,2)/(z+sp.Rational(3,2))**2)/2-z/(z+1)**2
dc=dw-cm*dw.subs(z,e*z)-cp*dw.subs(z,R*z)
yes('rational actual moment defect sign',sp.limit(z*z*dw,z,sp.oo)==-sp.Rational(1,2))
yes('rational joint signed defect sign',sp.limit(z*z*dc,z,sp.oo)==sp.Rational(116,25))
fixture=dict(matrix=[[1,'1/2'],['1/2',1]],source=[1,0],compression='first coordinate',full_vacuum='adjoin independent zero eigenvector',single_difference=str(sp.factor(dw)),joint_difference=str(sp.factor(dc)))
def response(ev,c,z):return np.dot(abs(c)**2,z*ev/(ev+z)**2).real
def remainder(ev,c,z):return np.dot(abs(c)**2,ev**3*(3*z+2*ev)/(z*z*(ev+z)**2)).real
cm=float(cm);cp=float(cp);D1=float(D1);D2=float(D2);B3=float(B3)
for case in range(12):
    n=7;k=3;raw=rng.normal(size=(n-1,n-1))+1j*rng.normal(size=(n-1,n-1));H=np.zeros((n,n),complex);H[1:,1:]=raw.conj().T@raw+np.eye(n-1)
    J=np.eye(n,dtype=complex)[:,:k];A=J.conj().T@H@J;f=np.r_[0,rng.normal(size=k-1)+1j*rng.normal(size=k-1)];x=J@f
    K=(np.eye(n)-J@J.conj().T)@H@J;r=np.vdot(K@f,K@f).real
    h,V=np.linalg.eigh(H);ah,U=np.linalg.eigh(A);c=V.conj().T@x;ac=U.conj().T@f
    m=[np.dot(abs(c)**2,h**p).real for p in range(4)];mt=[np.dot(abs(ac)**2,ah**p).real for p in range(4)]
    eq(f'full moment norm isometry {case}',m[0],mt[0]);eq(f'full first moment identity {case}',m[1],mt[1]);eq(f'complete orthogonal second moment {case}',m[2]-mt[2],r)
    for shift in [.07,.4,3.,20.]:
        W=response(h,c,shift);Wt=response(ah,ac,shift);rr=remainder(h,c,shift);rt=remainder(ah,ac,shift)
        eq(f'full remainder at shift {case} {shift}',W,m[1]/shift-2*m[2]/shift**2+rr,tol=1e-9)
        eq(f'full mixed difference {case} {shift}',W-Wt,-2*r/shift**2+rr-rt,tol=1e-9)
        d=W-Wt-cm*(response(h,c,shift/4)-response(ah,ac,shift/4))-cp*(response(h,c,shift*4)-response(ah,ac,shift*4))
        rrj=rr-cm*remainder(h,c,shift/4)-cp*remainder(h,c,shift*4);rtj=rt-cm*remainder(ah,ac,shift/4)-cp*remainder(ah,ac,shift*4)
        eq(f'joint original shifts and all remainders {case} {shift}',d,2*D2*r/shift**2+rrj-rtj,tol=2e-8)
        lo=2*D2*r/shift**2-3*(mt[3]+B3*m[3])/shift**3;hi=2*D2*r/shift**2+3*(m[3]+B3*mt[3])/shift**3
        yes(f'joint two sided finite bound {case} {shift}',lo-1e-7<=d<=hi+1e-7)
    Z1=3*m[3]/r;Zcorr=3*(mt[3]+B3*m[3])/(D2*r);Zfull=max(8*D2*m[2]/(D1*m[1]),np.sqrt(12*m[3]/(D1*m[1])));shift=max(4*Z1,Zcorr,Zfull)
    ds=[response(h,c,t)-response(ah,ac,t) for t in [shift,shift/4,shift*4]]
    correction=ds[0]-cm*ds[1]-cp*ds[2];total=response(h,c,shift)-cm*response(h,c,shift/4)-cp*response(h,c,shift*4)
    yes(f'all actual single corrections negative {case}',max(ds)<0)
    yes(f'actual signed correction positive {case}',correction>=D2*r/shift**2*(1-1e-8))
    yes(f'complete full response negative {case}',total<=-D1*m[1]/(2*shift))
    for shift in [.3,2.]:
        RR=[np.linalg.inv(H+t*np.eye(n)) for t in [shift,shift/4,shift*4]];SS=[np.linalg.inv(A+t*np.eye(k)) for t in [shift,shift/4,shift*4]]
        full=RR[0]@RR[1]@RR[2]@x;small=SS[0]@SS[1]@SS[2]@f
        defect=-RR[0]@RR[1]@RR[2]@K@SS[2]@f-RR[0]@RR[1]@K@SS[1]@SS[2]@f-RR[0]@K@SS[0]@SS[1]@SS[2]@f
        eq(f'complete noncommuting common-vector map {case} {shift}',full-J@small,defect)
        coeff=[-43*shift**4/25,shift**3/2,3801*shift**2/400,shift/2,-43/25]
        fc=V.conj().T@full;sc=U.conj().T@small
        moments=[np.dot(abs(fc)**2,h**(i+1)).real for i in range(5)];smoments=[np.dot(abs(sc)**2,ah**(i+1)).real for i in range(5)]
        total=response(h,c,shift)-cm*response(h,c,shift/4)-cp*response(h,c,shift*4)
        stotal=response(ah,ac,shift)-cm*response(ah,ac,shift/4)-cp*response(ah,ac,shift*4)
        eq(f'five complete physical common moments {case} {shift}',total,shift*np.dot(coeff,moments))
        eq(f'five complete trace common moments {case} {shift}',stotal,shift*np.dot(coeff,smoments))
        eq(f'five joint moment differences {case} {shift}',total-stotal,shift*np.dot(coeff,np.array(moments)-smoments))
# Exact radius-two Hessian by differentiating every original ordered matrix factor.
I=np.eye(2,dtype=complex);T=[-.5j*np.array([[0,1],[1,0]],complex),-.5j*np.array([[0,-1j],[1j,0]],complex),-.5j*np.array([[1,0],[0,-1]],complex)]
def prod(mats):
    ans=I.copy()
    for mat in mats:ans=ans@mat
    return ans
for case in range(20):
    mats=[];vel=rng.normal(size=(4,3));gens=[sum(v[i]*T[i] for i in range(3)) for v in vel]
    for _ in range(4):
        q=rng.normal(size=4);q/=np.linalg.norm(q);mats.append(q[0]*I+2*sum(q[i+1]*T[i] for i in range(3)))
    value=0j
    for i in range(4):
        terms=mats.copy();terms[i]=terms[i]@gens[i]@gens[i];value+=np.trace(prod(terms))
        for j in range(i+1,4):
            terms=mats.copy();terms[i]=terms[i]@gens[i];terms[j]=terms[j]@gens[j];value+=2*np.trace(prod(terms))
    yes(f'complete four-link Hessian constant {case}',abs(value)<=2*np.sum(vel**2)+1e-10)
# Full regulator formulas at 180 digits; no actual ground is sampled here.
mp.mp.dps=180;bounds=[]
for j in [1,2,3,10,100]:
    k=mp.mpf(4)/5;a=1/(mp.mpf(100)*j);L=j**4;N=3*(2*L)*(2*L+1)**2;M=3*(2*L)**2*(2*L+1);b=1/(k*a*a);c=2/(k*a)
    G=4*mp.pi**2*N*c*c;W=4*b*M/k+(3*N-1)*c;Bw=4*b*M/k+G;Q=3+2*(1+mp.sqrt(2))*mp.sqrt(G)+Bw+3*N*W+42*G
    QC=Q+6*(N-4)*(W+2*G)+(6+2*mp.sqrt(2))*G;RC=b*mp.exp(-16*mp.pi**2*c)/(k*QC);C4=532082;A4=8*mp.pi*c
    delta=min(mp.pi/4,RC/(8*C4*A4));ec=RC/(4*C4*mp.log(mp.cot(delta/2)));JJ=2*W+4*G+2*c+4*mp.sqrt(G)
    logBP=-56*mp.pi**2*c-mp.log(4)-7*mp.log(48*mp.pi)-21*mp.log(2*JJ*mp.sqrt(7));logm=mp.log(2*k*k)+logBP+23*mp.log(ec)
    xi=mp.mpf(7)/3;logr=mp.log(a*a*xi*xi/4)+logm
    U3=a*a*xi*xi*k**3/4*(6+4*W+4*mp.sqrt(G))**2;V3=a*a*xi*xi*k**3/4*(6+4*W+8*G+4*mp.sqrt(G))**2
    d2=mp.mpf(232)/25;b3=mp.mpf(4097)/100;logZ=mp.log(3*(V3+b3*U3)/d2)-logr
    AQ=207360000+1105920000*mp.pi**2;AJ=1920000+15360000*mp.pi**2;d0=3200*mp.pi**2/k
    logA=mp.log(k*k/2)-7*mp.log(48*mp.pi)-21*mp.log(2*mp.sqrt(7)*AJ/k**2)+23*mp.log(10000/(4*C4*d0*AQ))
    logcoeff=mp.log(3*(4*AJ**2+16*b3*960000**2)/(d2*k))-logA
    error=logZ-897*mp.log(j)-84800*mp.pi**2*j/k-logcoeff
    yes(f'original threshold finite positive {j}',mp.isfinite(logZ) and logZ>0)
    eq(f'raw amplitude cancels only in threshold ratio {j}',float(mp.log(3*(V3/xi**2+b3*U3/xi**2)/d2)-(logr-2*mp.log(xi))-logZ),0)
    bounds.append(dict(j=j,kappa='4/5',raw_xi='7/3',log10_Zcorr=mp.nstr(logZ/mp.log(10),25),log10_Zcorr_over_s=mp.nstr((logZ-mp.log(k/j))/mp.log(10),25),log_asymptotic_quotient=mp.nstr(error,25)))
yes('threshold coefficient converges in evaluated samples',abs(mp.mpf(bounds[-1]['log_asymptotic_quotient']))<abs(mp.mpf(bounds[-2]['log_asymptotic_quotient'])))
ee,vv,cc,dd=sp.symbols('epsilon R cminus cplus')
P=(l+ee*z)**2*(l+vv*z)**2-cc*ee*(l+z)**2*(l+vv*z)**2-dd*vv*(l+z)**2*(l+ee*z)**2
pp=[z**4*(ee**2*vv**2-cc*ee*vv**2-dd*vv*ee**2),2*z**3*(ee*vv*(ee+vv)-cc*ee*vv*(1+vv)-dd*vv*ee*(1+ee)),z*z*(ee**2+4*ee*vv+vv**2-cc*ee*(1+4*vv+vv**2)-dd*vv*(1+4*ee+ee**2)),2*z*(ee+vv-cc*ee*(1+vv)-dd*vv*(1+ee)),1-cc*ee-dd*vv]
for i in range(5):yes(f'complete common polynomial coefficient {i}',sp.expand(P).coeff(l,i)==sp.expand(pp[i]))
original=z*l/(l+z)**2-cc*ee*z*l/(l+ee*z)**2-dd*vv*z*l/(l+vv*z)**2
yes('full common denominator with original factors',sp.cancel(original-z*l*P/((l+z)**2*(l+ee*z)**2*(l+vv*z)**2))==0)
special=sp.expand(P.subs({ee:sp.Rational(1,4),vv:4,cc:sp.Rational(16,25),dd:sp.Rational(16,25)}));Y=l/z+z/l
yes('exact positive-band quadratic',sp.cancel(special-l*l*z*z*(-688*Y*Y+200*Y+5177)/400)==0)
ystar=(25+18*sp.sqrt(689))/172
yes('positive band root exact',sp.simplify(-688*ystar**2+200*ystar+5177)==0)
lo=(ystar-sp.sqrt(ystar**2-4))/2;hi=(ystar+sp.sqrt(ystar**2-4))/2
yes('positive band endpoint product',sp.simplify(lo*hi)==1)
for value in [.01,.1,.3,.5,1,2,3,10,100]:
    actual=float(special.subs({z:1,l:value}));yes(f'complete kernel sign at original energy {value}',(actual>0)==(float(lo)<value<float(hi)))
fixture['positive_band_at_zeta_one']=[str(lo),str(hi)]
out=dict(checks=len(rows),all_passed=all(r['passed'] for r in rows),scope='Exact symbolic remainders and original signed coefficients; complex positive-matrix compression diagnostics with a separate vacuum; direct original-radius four-link Hessians; 180-digit evaluation of the entire original regulator threshold. Matrix fixtures are not Yang–Mills ground data.',rational_fixture=fixture,evaluated_original_thresholds=bounds,rows=rows)
(O/'JOINT_TRACE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k not in ['rows','rational_fixture']}))
assert out['all_passed'],[r for r in rows if not r['passed']]
