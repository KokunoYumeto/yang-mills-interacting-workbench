from pathlib import Path
import json
import numpy as np
import sympy as s
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
O=Path(__file__).resolve().parent
K=s.symbols('K',positive=True)
cpt=(9*s.Rational(3,4)**2/(4*K))**2/(21*3*s.Rational(1,27)+4*16*K)
csign=9*s.Rational(3,4)**2/(4*(9+4*K))
ct=9*s.Rational(4,9)**2/(4*(3*s.Rational(4,9)+4*2**2*K))
ratio=256*K**2*(s.Rational(7,3)+64*K)/(81*(36+16*K))
assert s.simplify(csign/cpt-ratio)==0
assert 536870912>10000*45684
K0=(33+s.sqrt(33**2-s.Rational(81,4)))/2
coeff=[float(e.subs(K,K0)) for e in [cpt,csign,ct]]
x,y,A,B,C,k,a,h1,h2=s.symbols('x y A B C k a h1 h2',real=True)
w=A*x+B*y+C*x*y;wx=s.diff(w,x);wy=s.diff(w,y)
gx=(1-x*x)/4;gy=(1-y*y)/4
def dx2(f):return ((1-x*x)*s.diff(f,x,2)-3*x*s.diff(f,x))/4
def dy2(f):return ((1-y*y)*s.diff(f,y,2)-3*y*s.diff(f,y))/4
V=k*(dx2(w)+dy2(w)+wx*wx*gx+wy*wy*gy)
Hxx2=3*x*x*wx*wx/16;Hyy2=3*y*y*wy*wy/16;Hxy2=C*C*gx*gy
Hxxgg=-x*wx**3*gx/4;Hyygg=-y*wy**3*gy/4;Hxygg=C*wx*wy*gx*gy
Sx=dx2(w)+2*wx*wx*gx;Sy=dy2(w)+2*wy*wy*gy
F=h1*wx*wx*gx+h2*wy*wy*gy;Sh=h1*Sx+h2*Sy
cube=h1*h1*Hxxgg+2*h1*h2*Hxygg+h2*h2*Hyygg
direct=k*a**4*((h1-h2)**2*Hxy2+Sh**2)
boch=k*a**4*(h1*h1*(Hxx2+Hxy2)+h2*h2*(Hyy2+Hxy2)
                 +(h1*h1*wx*wx*gx+h2*h2*wy*wy*gy)/2-2*cube)
trace=a**4*(h1*h1*dx2(V)+h2*h2*dy2(V))/2-2*k*a**4*cube
Cobs=a*(x*x+x*y+2*y*y)
pair=a*a*(s.diff(Cobs,x)*h1*wx*gx+s.diff(Cobs,y)*h2*wy*gy)
pairibp=-a*a*(h1*dx2(Cobs)+h2*dy2(Cobs))/2
expressions=[direct,boch,trace,cube+F*Sh/2,Sh,pair,pairibp,
             Hxx2+Hxy2+wx*wx*gx/2-dx2(V)/(2*k),
             Hyy2+Hxy2+wy*wy*gy/2-dy2(V)/(2*k),
             Sx*Sy-Hxy2+2*Hxygg]
fn=s.lambdify((x,y,A,B,C,k,a,h1,h2),expressions,'numpy')
n=84;nodes=np.cos(np.arange(1,n+1)*np.pi/(n+1))
weights=2/(n+1)*np.sin(np.arange(1,n+1)*np.pi/(n+1))**2
X,Y=np.meshgrid(nodes,nodes,indexing='ij');WW=weights[:,None]*weights[None,:]
checks=0;worst=0.;samples=[]
def eq(name,left,right,tol=1e-11):
    global checks,worst
    err=abs(float(left)-float(right))/(1+abs(float(right)))
    assert err<tol,(name,err,left,right)
    checks+=1;worst=max(worst,err)
for pars in [(.3,-.2,.4),(-.6,.5,-.3),(.8,.2,.1),(.02,-.01,.9)]:
    AA,BB,CC=pars;ww=AA*X+BB*Y+CC*X*Y
    density=WW*np.exp(2*ww);Z=float(density.sum());density=density/Z
    for hh in [(1,0),(0,1),(1,1),(1,-1),(.7,-.3),(-.4,-.9),(2,3)]:
        vals=fn(X,Y,AA,BB,CC,1.3,.02,*hh)
        vals=[float(np.sum(density*np.asarray(v))) for v in vals]
        eq('SG4 versus SG5, Ricci retained',vals[0],vals[1])
        eq('SG8 full potential trace',vals[0],vals[2])
        eq('SG10 exact current covariance',vals[3],0)
        eq('zero weighted divergence',vals[4],0)
        eq('SG11 full integration by parts',vals[5],vals[6])
        eq('SG7 edge one',vals[7],0)
        eq('SG7 edge two',vals[8],0)
        eq('SG22 offdiagonal covariance',vals[9],0)
        assert vals[0]>=0;checks+=1
    samples.append(dict(parameters=list(pars),Z=Z,manifold='SU(2)^2 with original radius2 metric',
        density='exp(2w)/Z against Haar probability; logarithmic density is w-log(Z)/2. This manufactured smooth-density check is not the Yang–Mills ground state.'))
density_checks=checks
rng=np.random.default_rng(11061802)
for trial in range(96):
    kap=.4+trial/80;zz=.1+trial/50
    AA=np.diag(rng.uniform(.02,9,size=7));PP=np.diag([1.,1.,0.,0.,0.,0.,0.])
    aa=rng.normal(size=(7,4));gg=PP@rng.normal(size=7)
    NN=aa.T@aa;KK=aa.T@AA@aa;projected=PP@aa
    Khat=projected.T@AA@projected
    ell=aa.T@gg;MM=Khat+zz*NN;hh=np.linalg.solve(MM,ell)
    DD=AA+zz*np.eye(7);bb=np.linalg.solve(DD,gg);res=bb-projected@hh
    RR=kap*gg@bb;lower=kap*ell@hh
    eq('SG31 full projected residual',RR,lower+kap*res@DD@res+kap*zz*np.linalg.norm((np.eye(7)-PP)@aa@hh)**2)
    assert lower>=kap*ell@np.linalg.solve(KK+zz*NN,ell)-1e-10;checks+=1
    assert np.linalg.eigvalsh(KK-Khat).min()>-1e-10;checks+=1
fig=plt.figure(figsize=(14,9))
gs=fig.add_gridspec(1,2,width_ratios=[1.1,1],left=.03,right=.97,bottom=.14,top=.84,wspace=.28)
ax=fig.add_subplot(gs[0,0]);ax.axis('off')
ax.set_title('Actual ground-gradient variational map',loc='left',fontsize=14,fontweight='bold')
rows=[
(.87,r'$\alpha_h=a_j^2D_h\,dw_j$', 'All original edge components; full weighted ground density'),
(.64,r'$q_1(\alpha_h)=\frac{a_j^4}{2}\mu_j\Delta_{h^2}V_j+\frac{4}{a_j}N_h-\mathcal{D}_h$',r'$\mathcal{D}_h=2\kappa_*a_j^4\mu_j(H+2/(\kappa_*a_j)I)(D_hg,D_hg)\geq0$'),
(.40,r'$\mathsf{M}(z)=\mathsf{K}+z\mathsf{N}>0,\quad h_*=\mathsf{M}(z)^{-1}\ell$', 'Every current covariance and exterior Hessian block retained'),
(.15,r'$\mathcal{R}_j(z)=\kappa_*\ell^*\mathsf{M}(z)^{-1}\ell+\kappa_*\|(\mathscr{L}_1+z)^{1/2}(\beta_z-\alpha_*)\|^2$', 'Exact full physical residual (SG24); no finite-space identification')]
for yy,label,cap in rows:
    ax.text(.5,yy,label,ha='center',va='center',fontsize=11.6,bbox=dict(boxstyle='round,pad=.7',fc='#edf5ef',ec='#477052'),transform=ax.transAxes)
    ax.text(.5,yy-.075,cap,ha='center',va='center',fontsize=8.8,transform=ax.transAxes)
for t,b in [(.76,.69),(.52,.45),(.285,.20)]:
    ax.annotate('',xy=(.5,b),xytext=(.5,t),xycoords='axes fraction',arrowprops=dict(arrowstyle='->',lw=1.7,color='#477052'))
bx=fig.add_subplot(gs[0,1])
bars=bx.bar(['PT27\nprevious bound','SG17\nsign field','SG20\ncontinuous field'],coeff,color=['#8a96a4','#28724b','#5b91aa'],width=.65)
bx.set_yscale('log');bx.set_ylim(1e-7,.5);bx.grid(axis='y',alpha=.2)
bx.set_ylabel(r'Proved coefficient in $\liminf_j\,\mathcal{R}_j(z)/a_j$',fontsize=11)
bx.set_title('Same original observable, stronger lower bounds',loc='left',fontsize=12,fontweight='bold')
for bar,val in zip(bars,coeff):bx.text(bar.get_x()+bar.get_width()/2,val*1.18,f'{val:.6g}',ha='center',fontsize=10)
bx.text(.5,.96,r'$\kappa_*=R=1,\quad f_{12}=f_{13}=f_{23}=\prod_{\ell=1}^3(1-2|x_\ell|)_+$',ha='center',va='top',fontsize=9.7,transform=bx.transAxes)
bx.text(.5,.88,r'$K=(33+\sqrt{33^2-81/4})/2$',ha='center',va='top',fontsize=11,transform=bx.transAxes)
fig.suptitle('SG1–SG28: exact trial energy, complete residual and quantitative comparison',fontsize=15)
fig.text(.52,.035,r'Coefficients of rigorous lower bounds, not quantum measurements. Their scale remains $a_j$; no positive unscaled limit is asserted.',ha='center',fontsize=10)
fig.savefig(O/'GROUND_GRADIENT_MAP.png',dpi=180,bbox_inches='tight')
fig.savefig(O/'GROUND_GRADIENT_MAP.svg',bbox_inches='tight')
plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(13.5,7.3),gridspec_kw={'width_ratios':[1,1.25]})
fig.subplots_adjust(left=.035,right=.97,bottom=.16,top=.86,wspace=.18)
ax=axs[0];ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
pos={'e_1':(.16,.72),'e_2':(.82,.72),'o':(.49,.20)}
for name,(xx,yy) in pos.items():
    ax.scatter([xx],[yy],s=2100,c=['#dceef7' if name!='o' else '#e7e7e7'],edgecolors='#426a8f',zorder=3)
    label=(r'$e_1\in Q$' if name=='e_1' else r'$e_2\in Q$' if name=='e_2' else r'$o\notin Q$'+'\n'+r'$h_o=0$')
    ax.text(xx,yy,label,ha='center',va='center',fontsize=13,zorder=4)
for e,f in [('e_1','e_2'),('e_1','o'),('e_2','o')]:
    xx,yy=pos[e];ux,uy=pos[f]
    ax.plot([xx,ux],[yy,uy],lw=2.3,color='#477052',zorder=1)
    ax.text((xx+ux)/2,(yy+uy)/2+.025,r'$\omega_{'+e+','+f+r'}$',ha='center',fontsize=13,bbox=dict(fc='white',ec='none',pad=1.5))
ax.set_title('Three vertices of the complete Hessian graph',fontsize=12,fontweight='bold')
ax.text(.5,.02,r'$\omega_{ef}=\mu\|H_{ef}\|_{\mathrm{HS}}^2\geq0$',ha='center',fontsize=14)
bx=axs[1];bx.axis('off')
bx.set_title('Exact removal, unchanged source overlap',loc='left',fontsize=13,fontweight='bold')
lines=[
(.85,r'$P_{\mathcal{G}}\alpha_h=-\kappa a^2d\mathscr{L}_0^{-1}S_h$'),
(.65,r'$q_1(\alpha_h)-q_1(P_{\mathcal{G}}\alpha_h)$'),
(.55,r'$=\kappa a^4\sum_{e<f}\omega_{ef}|h_e-h_f|^2$'),
(.34,r'$\widehat{\mathsf{K}}_{ef}=\kappa a^4\mu S_eS_f,\quad\widetilde{\mathsf{M}}=\widehat{\mathsf{K}}+z\mathsf{N}$'),
(.14,r'$\mathcal{R}(z)\geq\kappa\ell^*\widetilde{\mathsf{M}}^{-1}\ell\geq\kappa\ell^*\mathsf{M}^{-1}\ell$')]
for yy,label in lines:bx.text(.02,yy,label,fontsize=15,va='center')
fig.suptitle('SG29–SG33: the physical exact projection and its full exterior defect',fontsize=15)
fig.text(.5,.065,'Only three graph vertices are drawn. Every lattice-edge pair remains in SG32, including all exterior pairs.\nGraph connections record the actual mixed ground Hessian, not geometric adjacency. Both residual norms remain in SG31.',ha='center',fontsize=11)
fig.savefig(O/'GROUND_GRADIENT_GRAPH.png',dpi=180)
fig.savefig(O/'GROUND_GRADIENT_GRAPH.svg')
plt.close(fig)
result=dict(exact_algebra_checks=2,numerical_checks=checks,curved_density_checks=density_checks,projected_matrix_checks=checks-density_checks,worst_relative_residual=worst,
    coefficient_comparison=dict(K=float(K0),previous=coeff[0],sign=coeff[1],continuous=coeff[2],sign_improvement_factor=coeff[1]/coeff[0],proved_lower_improvement=10000),
    samples=samples,scope='Curved compact manufactured-density checks test the weighted identities with the original Ricci1/2. They are not actual Yang–Mills simulations. SG proofs are the mathematical evidence.')
(O/'GROUND_GRADIENT_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(result))
