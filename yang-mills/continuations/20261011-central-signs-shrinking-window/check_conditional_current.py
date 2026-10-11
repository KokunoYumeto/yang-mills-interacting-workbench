from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
O=Path(__file__).resolve().parent
checks=0;worst=0.;samples=[]
def eq(name,a,b,tol=2e-10):
 global checks,worst
 a=np.asarray(a);b=np.asarray(b)
 err=float(np.linalg.norm(a-b)/(1+np.linalg.norm(b)))
 assert err<tol,(name,err,a,b)
 checks+=1;worst=max(worst,err)
def positive(name,A,tol=1e-10):
 global checks
 v=np.linalg.eigvalsh((A+A.T)/2)
 assert v.min()>-tol,(name,v)
 checks+=1
n=96;nodes=np.cos(np.arange(1,n+1)*np.pi/(n+1))
weights=2/(n+1)*np.sin(np.arange(1,n+1)*np.pi/(n+1))**2
X=nodes[:,None];Y=nodes[None,:];gx=(1-X*X)/4
for aa,bb,cc in [(.3,-.2,.4),(-.6,.5,-.3),(.8,.2,.1),(.02,-.01,.9),(.4,.3,0.),(0.,.3,0.)]:
 ww=aa*X+bb*Y+cc*X*Y
 raw=np.exp(2*ww)*weights[None,:]
 cond=raw/raw.sum(axis=1,keepdims=True)
 marginal=raw.sum(axis=1)*weights
 Z=marginal.sum();marginal=marginal/Z
 joint=marginal[:,None]*cond
 mean=(cond*Y).sum(axis=1,keepdims=True)
 var=(cond*(Y-mean)**2).sum(axis=1,keepdims=True)
 gbar=aa+cc*mean;xi=cc*(Y-mean);wp=aa+cc*Y
 wbar2=2*cc*cc*var
 ss=gx*wbar2-3*X*gbar/4+2*gx*gbar*gbar
 pp=gx*gbar*xi
 tt=-gx*wbar2-3*X*xi/4+2*gx*xi*xi+2*pp
 SS=-3*X*wp/4+2*gx*wp*wp
 mu=lambda q:float(np.sum(joint*q))
 EX=lambda q:(cond*q).sum(axis=1,keepdims=True)
 eq('CG3 conditional gradient',EX(xi),0.)
 eq('CG3 Hessian radial entry',wbar2,2*EX(xi*xi))
 eq('CG4 full current',SS,ss+2*pp+tt)
 eq('CG4 conditional t',EX(tt),0.)
 eq('CG4 conditional p',EX(pp),0.)
 eq('CG4 conditional S',EX(SS),ss)
 eq('CG5 total conditional covariance',mu(SS*SS),mu(ss*ss)+mu((2*pp+tt)**2))
 kap=1.3;spacing=.23;z=.8;fac=kap*spacing**4
 Ng=spacing**4*mu(gx*gbar*gbar);Nd=spacing**4*mu(gx*xi*xi)
 eq('CG9 orthogonal norm',spacing**4*mu(gx*wp*wp),Ng+Nd)
 obs=X+X*X;obs1=1+2*X;lapobs=2*gx-3*X*obs1/4
 ell=spacing**2*mu(gx*gbar*obs1)
 eq('CG6 source',ell,-spacing**2*mu(lapobs)/2)
 eq('CG6 current source',ell,-spacing**2*mu(obs*ss))
 eq('CG9 null fluctuation source',spacing**2*mu(gx*xi*obs1),0.)
 A=fac*(mu(ss*ss)+4*mu(pp*pp))+z*Ng
 C=fac*mu(tt*tt)+z*Nd;D=2*fac*mu(tt*pp);Ci=1/C if C>1e-25 else 0.
 Schur=A-D*Ci*D;old=A+2*D+C
 eq('CG17 old matrix',old,fac*mu(SS*SS)+z*(Ng+Nd))
 eq('CG17 exact gain',old-Schur,C*(1+Ci*D)**2)
 h=.7;k=-1.2
 eq('CG15 square completion',h*h*A+2*h*k*D+k*k*C,h*h*Schur+C*(k+Ci*D*h)**2)
 kstar=-Ci*D*h
 eq('CG19 optimized energy',h*h*Schur,fac*mu((h*ss)**2)+z*Ng*h*h+fac*mu((2*h*pp+kstar*tt)**2)+z*Nd*kstar*kstar)
 if old>1e-25:
  new=kap*ell*ell/Schur if Schur>1e-25 else 0.
  previous=kap*ell*ell/old
  extra=kap*C*((1+Ci*D)*ell/old)**2
  assert new+1e-12>=previous+extra;checks+=1
 samples.append(dict(parameters=[aa,bb,cc],partition=Z,old_matrix=old,schur_matrix=Schur,scope='Manufactured smooth SU(2)^2 density with original radius2 metric; not the Yang–Mills state.'))
curved=checks
rng=np.random.default_rng(11061900)
for trial in range(96):
 m=4;dim=12
 gamma=np.zeros((dim,m));delta=np.zeros((dim,m))
 for i in range(m):
  gamma[i,i]=0. if trial%3==0 and i==0 else .2+rng.random()
  delta[m+i,i]=0. if trial%4==0 and i==1 else .2+rng.random()
 source=np.zeros(dim);source[:m]=rng.normal(size=m);source[2*m:]=rng.normal(size=dim-2*m)
 basis=np.column_stack([source,rng.normal(size=(dim,dim-1))]);U=np.linalg.qr(basis)[0]
 PP=U[:,:6]@U[:,:6].T;LL=U@np.diag(rng.uniform(.1,8,size=dim))@U.T
 z=.1+rng.random();kap=.5+rng.random()
 Ngg=gamma.T@gamma;Ndd=delta.T@delta
 A=gamma.T@PP@LL@PP@gamma+z*Ngg
 C=delta.T@PP@LL@PP@delta+z*Ndd
 D=delta.T@PP@LL@PP@gamma
 Ci=np.linalg.pinv(C,hermitian=True);Schur=A-D.T@Ci@D
 ell=gamma.T@source;hh=np.linalg.pinv(Schur,hermitian=True)@ell;kk=-Ci@D@hh
 old=A+D.T+D+C;oldh=np.linalg.solve(old,ell)
 eta=gamma@hh+delta@kk;beta=np.linalg.solve(LL+z*np.eye(dim),source)
 RR=kap*source@beta;bound=kap*ell@hh
 resid=beta-PP@eta
 eq('CG16 physical residual',RR,bound+kap*resid@(LL+z*np.eye(dim))@resid+kap*z*np.linalg.norm((np.eye(dim)-PP)@eta)**2)
 eq('CG17 complete gain matrix',old-Schur,(np.eye(m)+Ci@D).T@C@(np.eye(m)+Ci@D))
 positive('CG15 S lower norm',Schur-z*Ngg)
 positive('CG17 gain nonnegative',old-Schur)
 assert bound+1e-9>=kap*ell@oldh+kap*oldh@(old-Schur)@oldh;checks+=1
 eq('CG14 range with singular C',C@Ci@D,D)
 eq('CG15 kernel source',Schur@hh,ell)
matrix_checks=checks-curved

outside_before=checks
for trial in range(96):
 d=6;m=4;kap=.4+rng.random();z=.05+rng.random();spacing=.11
 U=np.linalg.qr(rng.normal(size=(d,d)))[0]
 lam=rng.uniform(.03,7,size=d);L=U@np.diag(lam)@U.T
 B=np.vstack([U@np.diag(np.sqrt(lam/kap))@U.T,np.zeros((2,d))])
 inv=np.linalg.inv(L+z*np.eye(d));T=z*inv
 q=rng.normal(size=d);vv=kap*spacing**2*B@inv@q;v=rng.normal(size=d+2)
 ff=lambda w:kap*np.linalg.norm(B.T@w-spacing**2*q)**2+z*np.linalg.norm(w)**2
 eq('CG27 full divergence-domain minimizer',ff(v),kap*spacing**4*q@T@q+kap*np.linalg.norm(B.T@(v-vv))**2+z*np.linalg.norm(v-vv)**2)
 eq('CG26 residual divergence',B.T@vv-spacing**2*q,-spacing**2*T@q)
 eq('CG26 complete correction norm',vv@vv,kap*spacing**4*q@L@inv@inv@q)
 pp=rng.normal(size=(d,m));tt=rng.normal(size=(d,m));ss=rng.normal(size=(d,m))
 Ng=np.diag(rng.uniform(.1,1,size=m));Nd=np.diag(rng.uniform(.1,1,size=m))
 fac=kap*spacing**4
 A=fac*(ss.T@ss+4*pp.T@pp)+z*Ng
 C=fac*tt.T@tt+z*Nd;D=2*fac*tt.T@pp
 Az=fac*(ss.T@ss+4*pp.T@T@pp)+z*Ng
 Cz=fac*tt.T@T@tt+z*Nd;Dz=2*fac*tt.T@T@pp
 MM=np.block([[A,D.T],[D,C]]);MZ=np.block([[Az,Dz.T],[Dz,Cz]])
 Q=np.column_stack([2*pp,tt])
 eq('CG29 complete removed matrix',MM-MZ,fac*Q.T@L@inv@Q)
 positive('CG29 improvement',MM-MZ)
 S=A-D.T@np.linalg.solve(C,D);Sz=Az-Dz.T@np.linalg.solve(Cz,Dz)
 positive('CG30 Schur improvement',S-Sz)
 ell=rng.normal(size=m);hh=np.linalg.solve(S,ell);kk=-np.linalg.solve(C,D@hh);qq=2*pp@hh+tt@kk
 lower=kap*ell@hh;gain=kap*fac*qq@L@inv@qq
 assert kap*ell@np.linalg.solve(Sz,ell)+1e-11>=lower+gain;checks+=1
outside_checks=checks-outside_before

fig,axes=plt.subplots(1,3,figsize=(16,8),gridspec_kw={'width_ratios':[1,1.04,1.1]})
fig.subplots_adjust(left=.025,right=.98,bottom=.19,top=.83,wspace=.24)
for ax in axes:ax.axis('off')
def box(ax,y,formula,caption):
 ax.text(.5,y,formula,ha='center',va='center',fontsize=13,bbox=dict(boxstyle='round,pad=.7',fc='#eff6f3',ec='#3d715a'),transform=ax.transAxes)
 ax.text(.5,y-.105,caption,ha='center',va='top',fontsize=10,transform=ax.transAxes)
axes[0].set_title('Original state; two independent weights',loc='left',fontsize=12,fontweight='bold')
box(axes[0],.83,r'$\psi(x,v)=\varphi(x)\chi(x,v)$',r'$\int \chi(x,v)^2\,dv=1$; every exterior link retained')
box(axes[0],.49,r'$\eta_{h,k}=\gamma_h+\delta_k$',r'$\gamma_h=a^2D_hdw_Q,\quad \delta_k=a^2D_kd\log\chi$')
box(axes[0],.14,r'$\langle dC,\eta_{h,k}\rangle=\ell^*h$',r'$\gamma\perp\delta$; the fluctuation has zero source overlap')
axes[1].set_title('Actual divergence, including exterior drift',loc='left',fontsize=12,fontweight='bold')
box(axes[1],.83,r'$-a^{-2}d_\mu^*\eta_{h,k}=s_h+2p_h+t_k$',r'$\mathbb{E}_x p_h=\mathbb{E}_x t_k=0$')
box(axes[1],.49,r'$q_1(P_{\mathcal{G}}\eta_{h,k})$',r'$=\kappa a^4\{\mu |s_h|^2+\mu |2p_h+t_k|^2\}$')
box(axes[1],.14,r'$S=A-D^*C^+D$',r'Exact minimization over $k$; all zero directions proved')
axes[2].set_title('Quantified gain and physical residual',loc='left',fontsize=12,fontweight='bold')
box(axes[2],.83,r'$M_{\rm old}-S$',r'$=(I+C^+D)^*C(I+C^+D)\geq0$')
box(axes[2],.49,r'$\mathcal{R}(z)\geq\kappa\ell^*S^+\ell$',r'At least the old bound plus the full CG18 gain')
box(axes[2],.14,r'$\mathcal{R}(z)=\kappa\ell^*S^+\ell+$',r'physical form residual + projection norm penalty (CG16)')
for ax in axes:
 for ya,yb in [(.67,.60),(.33,.25)]:
  ax.annotate('',xy=(.5,yb),xytext=(.5,ya),xycoords='axes fraction',arrowprops=dict(arrowstyle='->',color='#3d715a',lw=1.8))
fig.suptitle('Conditional ground-current trials on the original Yang–Mills lattice',fontsize=17)
fig.text(.5,.055,'CG1–CG34: exact finite-regulator construction. The physical measure, energy and observable remain unchanged.\nC in the matrix formulas is the complete fluctuation block; C in the source pairing denotes the original observable.\nNo conditional Hamiltonian replaces the physical Hamiltonian, and no positive continuum value is assigned.',ha='center',fontsize=11)
for ext in ['png','svg']:fig.savefig(O/('CONDITIONAL_CURRENT_MAP.'+ext),dpi=170)
plt.close(fig)

fig,axes=plt.subplots(1,2,figsize=(14,8),gridspec_kw={'width_ratios':[1.3,1]})
fig.subplots_adjust(left=.035,right=.97,bottom=.27,top=.84,wspace=.28)
ax=axes[0];ax.axis('off')
rows=[
(.85,r'$q_{h,k}=2p_h+t_k,\quad \mathbb{E}_x q_{h,k}=0$','Actual conditional current; all outside links retained'),
(.56,r'$v=\kappa a^2d_{\rm out}(\mathscr{L}_{\rm out}+zI)^{-1}q$',r'Exact minimizer, including its full norm penalty (CG27)'),
(.27,r'$\mathcal{F}_q(v)=\kappa a^4\langle q,\mathcal{T}_zq\rangle$',r'$\mathcal{T}_z=z(\mathscr{L}_{\rm out}+zI)^{-1}$; no mode cutoff')]
for yy,form,cap in rows:
 ax.text(.5,yy,form,ha='center',fontsize=13,bbox=dict(boxstyle='round,pad=.65',fc='#edf4fa',ec='#436482'))
 ax.text(.5,yy-.09,cap,ha='center',fontsize=10)
for ya,yb in [(.71,.64),(.42,.35)]:
 ax.annotate('',xy=(.5,yb),xytext=(.5,ya),arrowprops=dict(arrowstyle='->',color='#436482',lw=1.8))
ax.set_title('Entire outside resolvent correction',loc='left',fontsize=13,fontweight='bold')
bx=axes[1];xs=np.linspace(0,5,500)
for zz in [.3,.8,1.5]:bx.plot(xs,zz/(xs+zz),label=f'z = {zz:g}',lw=2)
bx.set_xlabel(r'Outside spectral energy $\lambda$ (original units)')
bx.set_ylabel(r'Retained multiplier $z/(\lambda+z)$')
bx.set_ylim(0,1.04);bx.grid(alpha=.2);bx.legend()
bx.set_title('Exact operator multiplier, no spectral data',loc='left',fontsize=12,fontweight='bold')
fig.suptitle('Complete outside-current relaxation and the physical receiving map',fontsize=16)
fig.text(.5,.065,'CG23–CG34: every exterior spectral mode remains in the inverse. CG24 gives the exact original-Hamiltonian identity.\nCG30 retains both physical residual norms; CG32 keeps fixed-regulator and regulator limits in their stated order.\nThe curves show the proved scalar multiplier, not a measured quantum spectral distribution.',ha='center',fontsize=11)
for ext in ['png','svg']:fig.savefig(O/('OUTSIDE_CURRENT_MAP.'+ext),dpi=170)
plt.close(fig)

result=dict(numerical_checks=checks,curved_conditional_density_checks=curved,matrix_checks=matrix_checks,outside_correction_checks=outside_checks,worst_relative_residual=worst,samples=samples,scope='Curved disintegration checks and finite matrix diagnostics, including singular fluctuation blocks. These are not samples of the actual Yang–Mills ground. CG1–CG34 contain the complete proofs.')
(O/'CONDITIONAL_CURRENT_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=checks,curved=curved,matrix=matrix_checks,outside=outside_checks,worst_relative_residual=worst)))
