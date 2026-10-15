from pathlib import Path
import json
import numpy as np
import sympy as sp
import mpmath as mp
O=Path(__file__).resolve().parent;rows=[];rng=np.random.default_rng(2026101502)
def yes(name,ok):rows.append(dict(name=name,passed=bool(ok)))
def eq(name,a,b,tol=8e-10):
    err=float(np.max(abs(np.asarray(a)-np.asarray(b))));scale=1+float(np.max(abs(a)))+float(np.max(abs(b)));rows.append(dict(name=name,passed=err<tol*scale,error=err))
y,l,z=sp.symbols('Y lambda zeta',positive=True)
F=(-688*y*y+200*y+5177)/(25*(y+2)*(4*y+17)**2);h=2752*y**3-13296*y*y-110508*y-164041
yes('exact filter derivative',sp.cancel(sp.diff(F,y)-h/(25*(y+2)**2*(4*y+17)**3))==0)
yes('exact full upper difference',sp.cancel(F-sp.Rational(113,2500)+(y-2)*(1808*y*y+91400*y+226193)/(2500*(y+2)*(4*y+17)**2))==0)
yes('integer root isolation',h.subs(y,9)<0<h.subs(y,10));yes('derivative and convexity constants',sp.diff(h,y).subs(y,2)==-130668 and sp.diff(h,y,2).subs(y,2)>0)
kernel=z*l/(l+z)**2-sp.Rational(16,25)*(z/4)*l/(l+z/4)**2-sp.Rational(16,25)*(4*z)*l/(l+4*z)**2
yes('original signed kernel rational comparison',sp.cancel(kernel-F.subs(y,l/z+z/l))==0)
yes('full negative value retained',-F.subs(y,10)==sp.Rational(6847,108300)>sp.Rational(113,2500))
mp.mp.dps=100;beta=mp.findroot(lambda v:2752*v**3-13296*v*v-110508*v-164041,(9,10));km=-( -688*beta**2+200*beta+5177)/(25*(beta+2)*(4*beta+17)**2);kp=mp.mpf(113)/2500
constants=dict(beta=mp.nstr(beta,70),kminus=mp.nstr(km,70),kplus='113/2500',alpha=mp.nstr((kp-km)/2,70),d=mp.nstr((kp+km)/2,70))
km=float(km);kp=float(kp);alpha=(kp-km)/2;d=(kp+km)/2
def filt(ev,z):return z*ev/(ev+z)**2-(16/25)*(z/4)*ev/(ev+z/4)**2-(16/25)*(4*z)*ev/(ev+4*z)**2
for case in range(10):
    n=9;k=4;raw=rng.normal(size=(n-1,n-1))+1j*rng.normal(size=(n-1,n-1));H=np.zeros((n,n),complex);H[1:,1:]=raw.conj().T@raw+np.eye(n-1)
    ev,V=np.linalg.eigh(H)
    for zeta in [.03,.8,4.]:
        e1=21*zeta/4;e2=21*zeta*zeta/4;e3=zeta**3;qH=H@H@H+e1*H@H+e2*H+e3*np.eye(n)
        B=(V*filt(ev,zeta))@V.conj().T;us=[];xs=[];es=[];vs=[];ws=[];Js=[]
        for p in range(3):
            unit,_=np.linalg.qr(rng.normal(size=(n-1,n-1))+1j*rng.normal(size=(n-1,n-1)));J=np.zeros((n,k),complex);J[0,0]=1;J[1:,1:]=unit[:,:k-1]
            Q=np.eye(n)-J@J.conj().T;A=J.conj().T@H@J;K=Q@H@J;D=Q@H@Q;VV=K.conj().T@K;f=np.r_[0,rng.normal(size=k-1)+1j*rng.normal(size=k-1)]
            t=np.linalg.solve(A@A@A+e1*A@A+e2*A+e3*np.eye(k),f);u=J@t;x=J@f;e=x-qH@u
            vp=(A@VV+VV@A+K.conj().T@D@K+e1*VV)@t
            wp=(K@A@A+D@K@A+K@VV+D@D@K+e1*(K@A+D@K)+e2*K)@t
            eq(f'full cubic block residual {case} {zeta} {p}',e,-J@vp-wp)
            eq(f'orthogonal residual squared norm {case} {zeta} {p}',np.vdot(e,e),np.vdot(vp,vp)+np.vdot(wp,wp))
            eq(f'common inverse receives full forcing {case} {zeta} {p}',np.linalg.solve(qH,x)-u,np.linalg.solve(qH,e),tol=1e-7)
            us.append(u);xs.append(x);es.append(e);vs.append(J@vp);ws.append(wp);Js.append(J)
        U=np.column_stack(us);X=np.column_stack(xs);E=np.column_stack(es);Y=qH@U
        eq(f'all overlapping residual entries {case} {zeta}',E.conj().T@E,np.column_stack(vs).conj().T@np.column_stack(vs)+np.column_stack(vs).conj().T@np.column_stack(ws)+np.column_stack(ws).conj().T@np.column_stack(vs)+np.column_stack(ws).conj().T@np.column_stack(ws))
        cross=np.column_stack(vs).conj().T@np.column_stack(ws);yes(f'cross-patch mixed term nonzero {case} {zeta}',np.linalg.norm(cross-np.diag(np.diag(cross)))>1e-7)
        C=X.conj().T@B@X;T=Y.conj().T@B@Y;middle=C-T-alpha*(X.conj().T@X-Y.conj().T@Y)
        for scale in [.1,1.,10.]:
            bound=d/2*(scale*E.conj().T@E+(X+Y).conj().T@(X+Y)/scale)
            yes(f'full raw-coefficient matrix upper {case} {zeta} {scale}',np.linalg.eigvalsh(bound-middle).min()>-1e-7)
            yes(f'full raw-coefficient matrix lower {case} {zeta} {scale}',np.linalg.eigvalsh(bound+middle).min()>-1e-7)
        gamma=rng.normal(size=3)+1j*rng.normal(size=3);x=X@gamma;u=U@gamma;e=E@gamma;yy=Y@gamma
        true=np.vdot(x,B@x).real;trial=np.vdot(yy,B@yy).real
        pc=[-43*zeta**4/25,zeta**3/2,3801*zeta*zeta/400,zeta/2,-43/25];coef=V.conj().T@u
        eq(f'full trial five-moment identity {case} {zeta}',trial,zeta*sum(pc[i]*np.dot(abs(coef)**2,ev**(i+1)) for i in range(5)))
        center=alpha*(np.vdot(x,x).real-np.vdot(yy,yy).real)
        eq(f'exact centered oriented error {case} {zeta}',true-trial-center,np.vdot(e,(B-alpha*np.eye(n))@(x+yy)).real)
        yes(f'sharp centered interval {case} {zeta}',abs(true-trial-center)<=d*np.linalg.norm(e)*np.linalg.norm(x+yy)+1e-7)
        yes(f'no inverse-shift error factor {case} {zeta}',abs(true-trial)<=km*np.linalg.norm(e)*(2*np.linalg.norm(x)+np.linalg.norm(e))+1e-7)
        # Retain a deliberately dependent fourth trial column.
        Udep=np.column_stack([U,2*U[:,0]-U[:,1]]);Ydep=qH@Udep;GG=Ydep.conj().T@Ydep;HH=Ydep.conj().T@X;pinv=np.linalg.pinv(GG,hermitian=True)
        cc=pinv@HH@gamma;opt=Ydep@cc;err=x-opt;SS=X.conj().T@X;EE=SS-HH.conj().T@pinv@HH
        eq(f'dependent-frame full normal equation {case} {zeta}',GG@cc,HH@gamma)
        eq(f'optimized actual residual Gram {case} {zeta}',np.vdot(err,err),np.vdot(gamma,EE@gamma))
        eq(f'full optimal source orthogonality {case} {zeta}',np.vdot(opt,err),0)
        yes(f'full residual minimization improves old coefficients {case} {zeta}',np.linalg.norm(err)<=np.linalg.norm(e)+1e-7)
        s=np.vdot(x,x).real;r2=np.vdot(err,err).real;optresp=np.vdot(opt,B@opt).real
        eq(f'exact common-source norm difference {case} {zeta}',s-np.vdot(opt,opt).real,r2)
        eq(f'exact optimized sum norm {case} {zeta}',np.vdot(x+opt,x+opt).real,4*s-3*r2)
        yes(f'complete optimized signed interval {case} {zeta}',abs(true-optresp-alpha*r2)<=d*np.sqrt(max(0,r2*(4*s-3*r2)))+1e-7)
# Actual full-density differentiation on two disjoint original four-link SU2 loops.
# This is a constructed positive density, not the Yang–Mills Wilson vacuum.
for coupling in [.2,-.3,.45]:
    n=160;theta=np.arange(1,n+1)*np.pi/(n+1);coord=2*np.cos(theta);weight=2*np.sin(theta)**2/(n+1);x=coord[:,None];yy=coord[None,:];G=4-x[:,0]**2
    dens=np.exp(2*coupling*x*yy);marg=dens@weight;norm=weight@marg
    mean=(dens@(weight*coord))/marg;m2=(dens@(weight*coord**2))/marg;m3=(dens@(weight*coord**3))/marg;var=m2-mean**2;third=m3-3*mean*m2+2*mean**3
    sigma=coupling**2*G**2*var;sprime=coupling**2*(-4*coord*G*var+G**2*2*coupling*third)
    f=coord**2+1j*coord;fp=2*coord+1j;gg=1+.3*coord+.2j*coord**2;gp=.3+.4j*coord;k=.8
    r=coupling*G[:,None]*(yy-mean[:,None]);wc=r*gg[:,None];Kf=-2*k*r*fp[:,None]
    lhs=np.sum(weight[:,None]*weight[None,:]*dens*np.conj(Kf)*wc)/norm
    adj=2*k*(sigma*gp+(sprime+sigma*(2*coupling*mean-coord/G))*gg)
    rhs=np.sum(weight*marg*np.conj(f)*adj)/norm
    eq(f'full conditional covariance adjoint with Haar derivative {coupling}',lhs,rhs)
    eq(f'actual conditional residual covariance {coupling}',np.sum(weight[:,None]*weight[None,:]*dens*abs(Kf)**2)/norm,4*k*k*np.sum(weight*marg*sigma*abs(fp)**2)/norm)
# Spatial source norm inequalities with all phases and correlations retained.
for case in range(10):
    vals=rng.uniform(0,4,size=(20,9));p=rng.uniform(.1,1,size=20);p/=p.sum();phi=rng.normal(size=9)+1j*rng.normal(size=9);a=.01
    source=a/2*(vals@phi-p@(vals@phi));mass=np.dot(p,abs(source)**2);W=vals.sum(axis=1);Bq=p@W;U2=p@W**2
    bounds0=[a*a*np.sum(abs(phi))**2,a*a*np.sum(abs(phi)**2)*Bq,a*a*np.max(abs(phi))**2*U2/4]
    for i,bound in enumerate(bounds0):yes(f'centered spatial bound with full correlations {case} {i}',mass<=bound+1e-10)
    cov=(vals-(p@vals)).T@(p[:,None]*(vals-(p@vals)));eq(f'raw spatial covariance equality {case}',mass,a*a*np.vdot(phi,cov@phi).real/4)
values=[]
for j in [5,10,20,100]:
    k=mp.mpf(4)/5;a=1/(mp.mpf(100)*j);L=j**4;q=100*j;g2=k*a/2
    Nq=3*q*(q+1)**2;Mq=3*q*q*(q+1);Cq=12*q*(q+1);Lam=min(2*Mq,6*g2*mp.sqrt(Nq*Mq))+2*Cq;U2=min((4*Mq)**2,Lam**2+16*g2**2)
    Z=min(a*Mq,a*mp.sqrt(Mq*min(4*Mq,Lam)),a*mp.sqrt(U2)/2);old=2*a*Mq
    yes(f'original fitting cube exists {j}',q<2*L-1)
    eq(f'all original boundary counts {j}',Cq,2*q*(q+1)*6)
    yes(f'local source bound improves original full sample bound {j}',Z<old)
    values.append(dict(j=j,q=q,kappa='4/5',physical_side='1',a2_Lambda=mp.nstr(a*a*Lam,25),a_Z=mp.nstr(a*Z,25),original_Z=mp.nstr(old,25),improved_Z=mp.nstr(Z,25),limiting_aZ='15.6'))
yes('complete boundary coefficient convergence',abs(mp.mpf(values[-1]['a_Z'])-mp.mpf('15.6'))<abs(mp.mpf(values[0]['a_Z'])-mp.mpf('15.6')))
out=dict(checks=len(rows),all_passed=all(r['passed'] for r in rows),constants=constants,original_spatial_bounds=values,scope='Exact rational filter extrema; complex full cubic residual and five-moment identities; overlapping nonorthogonal patch matrices with raw complex coefficients; original radius-two four-link conditional-density adjoint with every Haar-density derivative; source bounds and full original counts. Matrix and constructed-density fixtures are not Yang–Mills vacuum samples.',rows=rows)
(O/'COMMON_RESIDUAL_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
assert out['all_passed'],[r for r in rows if not r['passed']]
