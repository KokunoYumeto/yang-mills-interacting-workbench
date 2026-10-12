"""Algebraic gain checks and original-grid source diagnostics; no vacuum sampling."""
from pathlib import Path
import itertools,json,math
from fractions import Fraction
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent
rng=np.random.default_rng(61012012);checks=[]
def eq(name,a,b,tol=1e-9):
    a=np.asarray(a);b=np.asarray(b)
    err=float(np.max(abs(a-b)));scale=max(1.,float(np.max(abs(a))),float(np.max(abs(b))))
    checks.append(dict(name=name,passed=err<=tol*scale,absolute_error=err));assert checks[-1]['passed'],checks[-1]
def le(name,a,b,tol=1e-10):
    checks.append(dict(name=name,passed=bool(a<=b+tol*max(1.,abs(a),abs(b))),lhs=float(a),rhs=float(b)));assert checks[-1]['passed'],checks[-1]
# Exact finite reducing operator models test the gain inequalities, not the YM state.
for trial in range(60):
    n=4;exact=6;total=12
    C=rng.normal(size=(total,n))+1j*rng.normal(size=(total,n))
    if trial%2==0:C[:exact,3]=C[:exact,0]+2*C[:exact,1]
    H=np.diag(rng.uniform(.05,3,total));v=np.zeros(total,complex);v[:exact]=rng.normal(size=exact)+1j*rng.normal(size=exact)
    zs=np.array([.03,.2,1.1])*(1+.05*trial);b=C.conj().T@v
    rows=[]
    for z in zs:
        A=(H+z*np.eye(total))@C
        B=np.concatenate([A[:exact],z*C[exact:]],axis=0)
        Z=A.conj().T@A;Zs=B.conj().T@B;M=Z-Zs;k=A.conj().T@v
        c=np.linalg.solve(Z,k);cs=np.linalg.solve(Zs,k)
        gain=float(np.vdot(k,cs-c).real)
        eq(f'complete gain identity {trial}/{z}',gain,np.vdot(c,M@c).real+np.vdot(cs-c,Zs@(cs-c)).real)
        rows.append((Z,Zs,M,k,gain))
    m=float(np.linalg.eigvalsh(rows[0][2])[0]);U=float(np.trace(rows[-1][0]).real)
    gains=[r[4] for r in rows]
    for i,(Z,Zs,M,k,gain) in enumerate(rows):
        le(f'evaluated gain floor {trial}/{i}',m/U**2*np.vdot(k,k).real,gain)
        eq(f'affine source {trial}/{i}',k,C.conj().T@H@v+zs[i]*b)
    for i,j in itertools.combinations(range(3),2):
        le(f'pair gain {trial}/{i}/{j}',m*(zs[j]-zs[i])**2*np.vdot(b,b).real/(2*U**2),gains[i]+gains[j])
    le(f'second largest gain {trial}',m*min(np.diff(zs))**2*np.vdot(b,b).real/(4*U**2),sorted(gains)[1])
# Exact angular map, full face incidence, and complex coefficients.
A=np.array([[1,1,0],[1,0,1],[0,1,1]])
L=3*np.eye(3)-np.ones((3,3))
eq('exact original orientation map',A.T@L@A,L)
for trial in range(50):
    f=rng.normal(size=3)+1j*rng.normal(size=3);t=A@f
    Jt=float(np.vdot(t,t).real);Jan=float(np.vdot(t,L@t).real)
    F=float(np.vdot(f,f).real);S=float(abs(f.sum())**2)
    eq(f'angular quadratic {trial}',Jan,3*F-S);eq(f'full source quadratic {trial}',Jt,F+S)
    h=rng.normal(size=4)+1j*rng.normal(size=4)
    full=sum(abs(h[i]-h[j])**2 for i,j in itertools.combinations(range(4),2))
    eq(f'unsigned full face identity {trial}',full,4*np.vdot(h,h).real-abs(h.sum())**2)
    le(f'face upper constant {trial}',full,4*np.vdot(h,h).real)
# Original a_j=(100j)^-1; physical support [-R/2,R/2]^3 and original fitting offset.
R=Fraction(2,25);Rf=float(R)
power=3
I0=Rf*float(sum(Fraction((-1)**k*math.comb(2*power,k),2*k+1) for k in range(2*power+1)))
I1=16*power*power/Rf*float(sum(Fraction((-1)**k*math.comb(2*power-2,k),2*k+3) for k in range(2*power-1)))
phi_norm2=I0**3;phi_energy=3*I1*I0**2
def phi(x):
    ys=[2*z/Rf for z in x]
    return np.prod(np.broadcast_arrays(*[np.maximum(1-y*y,0)**power for y in ys]),axis=0)
def dphi(x,k):
    ys=[2*z/Rf for z in x];out=[]
    for d,y in enumerate(ys):
        out.append(-4*power/Rf*y*np.maximum(1-y*y,0)**(power-1)*(abs(y)<1) if d==k else np.maximum(1-y*y,0)**power)
    return np.prod(np.broadcast_arrays(*out),axis=0)
def face_slices(q,d,k):
    base=[slice(0,q+1)]*3;base[d]=slice(0,q);base[k]=slice(0,q)
    sd=base.copy();sd[d]=slice(1,q+1)
    sk=base.copy();sk[k]=slice(1,q+1)
    return tuple(base),tuple(sd),tuple(sk)
data=[]
for j in [2,3,5,8,12]:
    a=float(Fraction(1,100*j));q=8*j+3;Lbox=j**4;vQ=Lbox-4*j-1
    assert vQ>0 and vQ+q<2*Lbox
    x=[a*(np.arange(q+1)-4*j-1).reshape(tuple(q+1 if k==d else 1 for k in range(3))) for d in range(3)]
    orientations=[(0,1),(0,2),(1,2)]
    faces=[]
    for d,k in orientations:
        base,sd,sk=face_slices(q,d,k);xp=[np.broadcast_to(x[l]+(a/2 if l in [d,k] else 0),(q+1,)*3)[base] for l in range(3)]
        faces.append((d,k,base,sd,sk,phi(xp),xp))
    for coeff,label in [(np.array([1.,-.5,.7]),'anisotropic'),(np.ones(3),'common')]:
        t=A@coeff;Jan=float(np.vdot(t,L@t))*phi_norm2;Mf=float(max(abs(coeff)))
        for law in ['zero','smooth','concentrated']:
            b=[np.zeros((q+1,)*3) for _ in range(3)]
            w=[np.zeros((q+1,)*3) for _ in range(3)];dQ=0.
            for idx,(d,k,base,sd,sk,p,xp) in enumerate(faces):
                dp=np.zeros_like(p) if law=='zero' else a*(1+.2*np.cos(13*xp[0])*.5)
                if law=='concentrated':
                    # A layer of finite deficit has total order a^-2, but no small discrete derivative.
                    dp=dp+((abs(xp[2])<.51*a)&(idx==0)).astype(float)
                assert dp.min()>=0 and dp.max()<=4
                dQ+=float(dp.sum())
                val=-3*a**3/8*coeff[idx]*p*(2-dp)
                for out,sl in [(d,base),(k,sd),(d,sk),(k,base)]:
                    b[out][sl]+=val;w[out][sl]+=dp
            for d in range(3):
                end=[slice(None)]*3;end[d]=q;b[d][tuple(end)]=0;w[d][tuple(end)]=0
                for k in range(3):
                    if k==d:continue
                    for endval in [0,q]:
                        sl=[slice(None)]*3;sl[k]=endval;b[d][tuple(sl)]=0
            norm2=sum(float(np.sum(z*z)) for z in b)
            G=0.;Bnorm=0.;parallel=0.;cert=0.;err2=0.
            for d,k,base,sd,sk,p,xp in faces:
                vals=[b[d][base],b[k][sd],b[d][sk],b[k][base]]
                for u,v in itertools.combinations(vals,2):G+=float(np.sum((u-v)**2))
                Bnorm+=float(np.sum(sum(vals)**2))
                parallel+=float(np.sum((vals[0]-vals[2])**2)+np.sum((vals[1]-vals[3])**2))
                if label=='common':
                    for e,trans,up,lo in [(d,k,sk,base),(k,d,sd,base)]:
                        # Parallel-pair midpoint is the actual face center for its two directions.
                        eta=-3*dphi(xp,trans);diff=b[e][up]-b[e][lo]
                        cert+=2*(2/a*float(np.sum(diff*eta))-a**3*float(np.sum(eta*eta)))
                        # Independent summation-by-parts check with all four patch boundary sides.
                        ee=[np.broadcast_to(x[l]+(a/2 if l==e else 0),(q+1,)*3) for l in range(3)]
                        plus=[z+(a/2 if l==trans else 0) for l,z in enumerate(ee)]
                        minus=[z-(a/2 if l==trans else 0) for l,z in enumerate(ee)]
                        sbp=-float(np.sum(b[e]*(-3*dphi(plus,trans)+3*dphi(minus,trans))))/a
                        eq(f'exact raw summation by parts {j}/{law}/{e}/{trans}',float(np.sum(diff*eta))/a,sbp)
            eq(f'full strict-patch incidence {j}/{label}/{law}',G,16*norm2-Bnorm)
            le(f'full graph bound16 {j}/{label}/{law}',G,16*norm2)
            le(f'complete parallel-pair bound {j}/{label}/{law}',2*parallel,G)
            for d in range(3):
                xe=[x[l]+(a/2 if l==d else 0) for l in range(3)]
                bar=-1.5*a**3*t[d]*phi(xe)
                for k in range(3):
                    for val in ([q] if k==d else [0,q]):
                        sl=[slice(None)]*3;sl[k]=val;bar[tuple(sl)]=0
                err2+=float(np.sum((b[d]-bar)**2))
            omega=Mf*4*power/Rf*math.sqrt(3)*a/2
            bound=3*a**3*math.sqrt(3*q*(q-1)**2)*omega+3*a**3*Mf*math.sqrt(dQ)
            le(f'full original source error {j}/{label}/{law}',math.sqrt(err2),bound)
            if label=='common':le(f'full finite dual certificate {j}/{law}',cert,G/a**5)
            data.append(dict(j=j,a=a,q=q,label=label,law=law,G_over_a3=G/a**3,G_over_a5=G/a**5,graph_limit=9*Jan,spatial_lower=36*phi_energy,dual_certificate=cert,source_error_over_a3=err2/a**3))
            for C in [1.,5.,20.,100.]:
                badnorm=0.;ret=[z.copy() for z in b]
                for d in range(3):
                    bad=w[d]>C*a;badnorm+=float(np.sum(b[d][bad]**2));ret[d][bad]=0
                Gret=0.
                for d,k,base,sd,sk,p,xp in faces:
                    vals=[ret[d][base],ret[k][sd],ret[d][sk],ret[k][base]]
                    Gret+=sum(float(np.sum((u-v)**2)) for u,v in itertools.combinations(vals,2))
                le(f'exact retained-mask graph {j}/{label}/{law}/{C}',max(math.sqrt(G)-4*math.sqrt(badnorm),0)**2,Gret)
                le(f'complete omitted source count {j}/{label}/{law}/{C}',badnorm,36*Mf*Mf*a**5*dQ/C)
for law in ['zero','smooth']:
    row=next(x for x in data if x['j']==12 and x['label']=='anisotropic' and x['law']==law)
    le(f'finite anisotropic convergence diagnostic {law}',abs(row['G_over_a3']/row['graph_limit']-1),.01)
row=next(x for x in data if x['j']==12 and x['label']=='common' and x['law']=='zero')
le('finite common spatial reference diagnostic',abs(row['G_over_a5']/row['spatial_lower']-1),.01)
for law in ['zero','smooth','concentrated']:
    row=next(x for x in data if x['j']==12 and x['label']=='common' and x['law']==law)
    le(f'finite dual-limit diagnostic {law}',abs(row['dual_certificate']/row['spatial_lower']-1),.02)
# Mechanism figure: every displayed assertion refers to its complete proof.
plt.rcParams.update({'font.size':11})
fig,ax=plt.subplots(figsize=(13,7.7));ax.set(xlim=(0,13),ylim=(0,8));ax.axis('off')
def box(x,y,w,h,text,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.13',fc=color,ec='#475467'))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=12,linespacing=1.6)
def arrow(a,b):ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',lw=1.8,color='#344054'))
box(.3,5.9,5.5,1.5,'Original state and Wilson test\n'+r'$\mu_j=\psi_j^2dU,\quad X=C_{\mathbf{f}}-\mu_jC_{\mathbf{f}}$'+'\n'+r'$\mathsf{b}_e=-\frac{3a_j^3}{8}\sum_{p\ni e}f_{\sigma(p)}(x_p)\,\mu_j\mathrm{Tr}U_p$','#eff8ff')
box(7,5.9,5.5,1.5,'Complete face graph: QG5–QG13\n'+r'$\mathcal{G}(\mathsf{b})=\sum_p\sum_{e<f\in\partial p}|\mathsf{b}_e-\mathsf{b}_f|^2$'+'\n'+r'$\mathcal{G}(h)=16\|h\|^2-\sum_p|\sum_{e\in\partial p}h_e|^2$'+'\nLast identity uses the zero-extended strict-inside patch.','#eff8ff')
arrow((5.95,6.65),(6.8,6.65))
box(.3,2.7,5.5,2.2,'Directional component: QG7–QG13\n'+r'$a_j^{-3}\mathcal{G}(\mathsf{b}_{I_j})\ \longrightarrow\ 9J_{\rm an}$'+'\n'+r'$J_{\rm an}=\int\sum_{d<k}(t_d-t_k)^2$'+'\n'+r'$\ker J_{\rm an}:\quad f_{12}=f_{13}=f_{23}$'+'\nAll source-mean deficit terms remain in QG5–QG6.','#ecfdf3')
box(7,2.7,5.5,2.2,'Equal-component space: QG14–QG17\n'+r'$f_{12}=f_{13}=f_{23}=\varphi$'+'\n'+r'$\liminf\,a_j^{-5}\mathcal{G}(\mathsf{b}_{I_j})\geq36\mathcal{E}(\varphi)$'+'\nExact raw summation by parts; full zero extension.\nNo derivative convergence of vacuum means is assumed.','#fff4ed')
arrow((9.75,5.72),(3.05,5.06));arrow((9.75,5.72),(9.75,5.06))
box(1.1,.3,10.8,1.4,'Receiving map: QG18 and DF18–DF21\n'+r'$\mathsf{b}^*\mathsf{M}_\perp\mathsf{b}\geq A_0(a_j)\mathcal{G}(\mathsf{b})+2z\,\mathsf{b}^*\mathsf{K}^\perp\mathsf{b}$'+'\n'+r'Original $a_j^4$ or $a_j^6$ source bounds; full inverse and physical residual still enter the signed window.','#f2f4f7')
arrow((3.05,2.5),(4.2,1.87));arrow((9.75,2.5),(8.8,1.87))
fig.tight_layout()
for ext in ['png','svg']:fig.savefig(O/('SOURCE_GRAPH_AND_SPATIAL_RECEIVER.'+ext),dpi=180)
plt.close(fig)
fig,axes=plt.subplots(1,2,figsize=(13,5.5))
colors={'zero':'#175cd3','smooth':'#039855','concentrated':'#dc6803'}
for law in colors:
    rows=[x for x in data if x['label']=='anisotropic' and x['law']==law]
    axes[0].plot([x['j'] for x in rows],[x['G_over_a3'] for x in rows],marker='o',color=colors[law],label=law+' deficit array')
rows=[x for x in data if x['label']=='anisotropic']
axes[0].axhline(rows[0]['graph_limit'],color='black',ls='--',label=r'$9J_{\rm an}$')
for law in ['zero','concentrated']:
    rows=[x for x in data if x['label']=='common' and x['law']==law]
    axes[1].semilogy([x['j'] for x in rows],[x['G_over_a5'] for x in rows],marker='o',color=colors[law],label=law+': graph energy')
    if law=='concentrated':
        axes[1].semilogy([x['j'] for x in rows],[x['dual_certificate'] for x in rows],marker='s',color='#039855',label='concentrated: dual certificate')
axes[1].axhline(36*phi_energy,color='black',ls='--',label=r'$36\mathcal{E}(\varphi)$')
axes[0].set_ylabel(r'Original graph energy $\mathcal{G}/a_j^3$')
axes[1].set_ylabel(r'Original graph energy or certificate at $a_j^5$')
axes[0].set_title('Directional source: exact finite source formula')
axes[1].set_title('Common source: derivative-free lower limit')
for ax in axes:
    ax.set_xlabel(r'Original regulator index $j$');ax.grid(alpha=.25);ax.legend(fontsize=9)
fig.suptitle('Diagnostic face-mean arrays on the original grid; these are not vacuum samples.',fontsize=13)
fig.text(.5,.035,r'$a_j=(100j)^{-1}$, $R=2/25$, $\varphi(x)=\prod_d[1-(2x_d/R)^2]_+^3$.'+'\nThe concentrated layer retains the total deficit order but has large differences; the raw dual certificate still converges.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.13,1,.94))
for ext in ['png','svg']:fig.savefig(O/('SOURCE_GRAPH_ORIGINAL_GRID_DIAGNOSTICS.'+ext),dpi=180)
plt.close(fig)
out=dict(checks=len(checks),all_passed=all(c['passed'] for c in checks),scope='Finite reducing-operator gain inequalities, full complex face identity, original-grid source formula and exact zero-extension/summation-by-parts identities. Face-mean arrays are diagnostic inputs, not sampled Yang–Mills states. The analytic proofs control the actual state.',reference_integrals=dict(R=Rf,I0=I0,I1=I1,phi_norm2=phi_norm2,phi_energy=phi_energy),grid_data=data,results=checks)
(O/'SOURCE_GRAPH_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k not in ['results','grid_data']}))
