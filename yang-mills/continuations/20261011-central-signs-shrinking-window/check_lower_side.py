from pathlib import Path
import hashlib, json, datetime, math, re
import sympy as sy
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

root = Path(__file__).parent
F, al, A1, d, h, z, t, R, e = sy.symbols('F al A1 d h z t R e', positive=True)
J = 6*A1-3*d
s = -(J+t*h)/2
Q = z+t*s+t*t*h/4-J*J/(4*h)
delta = 16*F*d-h
original = d+R+al*F*z-al*F*(t*t*h+t*J)/2
expanded = d+al*J*J/(64*d)-4*al*F*F*t*t*d+R+al*F*Q+al*J*J*delta/(64*d*h)+al*F*t*t*delta/4
assert sy.simplify(original-expanded) == 0
c=9*al/64; A0=1+c; beta=4*al*F*F; B=e+4*c*A1; C=4*c*A1*A1
P=(A0-beta*t*t)*d*d-B*d+C
rem=d*R+al*F*d*Q+al*J*J*delta/(64*h)+al*F*t*t*d*delta/4
assert sy.simplify(P+rem-d*(original-e)) == 0
p0=sy.sqrt(C/beta)
assert sy.simplify(p0-3*A1/(8*F)) == 0
assert sy.simplify(P.subs({t:0,d:e})-c*(e-2*A1)**2) == 0
varY, bs, cy = sy.symbols('varY bs cy', real=True)
assert sy.expand(varY*(varY+bs-2*cy)-(cy-varY)**2-(varY*bs-cy*cy)) == 0
u, v, ginv, dinv, av = sy.symbols('u v ginv dinv av', real=True)
inverse_unsplit=av-(e+3*al*F/2)*u+1-al*F*ginv+3*al*F*A1*v
inverse_split=1+(3*al*F*A1-16*al*F*F)*v-(e+3*al*F/2)*u+av+al*F*dinv
assert sy.simplify(inverse_unsplit.subs(ginv,16*F*v-dinv)-inverse_split)==0
V,T,rr=sy.symbols('V T rr', positive=True)
assert sy.simplify(sy.integrate(2*rr*sy.exp(-rr**2/(4*V)),(rr,0,2*V*T))+sy.integrate(2*rr*sy.exp(-T*rr+V*T*T),(rr,2*V*T,sy.oo))-(4*V+2*sy.exp(-V*T*T)/T**2))==0
kk,mk,mkp1,mkm1,ak,gk,dk=sy.symbols('kk mk mkp1 mkm1 ak gk dk',positive=True)
inverse_k=ak-(e+3*al*F*kk/2)*mk+mkm1-al*F*kk*(kk+1)*gk/2+3*al*F*kk*A1*mkp1
split_k=mkm1+al*F*kk*(3*A1-8*F*(kk+1))*mkp1-(e+3*al*F*kk/2)*mk+ak+al*F*kk*(kk+1)*dk/2
assert sy.simplify(inverse_k.subs(gk,16*F*mkp1-dk)-split_k)==0
DD,LL=sy.symbols('DD LL',positive=True)
root_x=(sy.sqrt(LL)+sy.sqrt(LL+4*DD))/2
assert sy.simplify(root_x**2-sy.sqrt(LL)*root_x-DD)==0
# Exact complete energy moment: mixed Hessian + shifted Hessian + conditional variance.
hmix,hqnorm,hgg,zq,cs,smarg,K=sy.symbols('hmix hqnorm hgg zq cs smarg K',real=True)
sfull=hqnorm+zq/2-2*hgg
tracefull=hqnorm+hmix+zq/2
assert sy.expand(tracefull+2*K*zq-smarg-(hmix+2*(hgg+K*zq)+(sfull-smarg)))==0
symbolic_checks=11

# Check root domains including the zero and negative quadratic coefficients.
rng=np.random.default_rng(20261011)
numerical_checks=0
for _ in range(250):
    fv=10**rng.uniform(-1,1); aa=10**rng.uniform(-5,2); nn=10**rng.uniform(0,6)
    cc=9*aa/64; aa0=1+cc; bbeta=4*aa*fv*fv; ccap=4*cc*nn*nn
    emin=4*nn*(math.sqrt(cc*(1+cc))-cc)
    ee=emin*(1+10**rng.uniform(-5,1)); bb=ee+4*cc*nn
    DD=bb*bb-4*aa0*ccap
    assert DD>0
    rm=2*ccap/(bb+math.sqrt(DD)); rp=(bb+math.sqrt(DD))/(2*aa0)
    pshape=3*nn/(8*fv); lamb=rm/pshape; Tv=1/(4*fv*math.sqrt(aa))
    vvplus=fv*math.sqrt(aa)*(2*math.sqrt(ccap)+rp)/(2*(.75+cc))
    assert 0<rm<=rp<=ee*(1+1e-10)
    for mult in [0,.02,.5,1,math.sqrt(aa0/bbeta)/Tv,4,100,1e5]:
        tt=mult*Tv
        rmt=2*ccap/(bb+math.sqrt(DD+4*bbeta*ccap*tt*tt))
        assert rmt >= rm/(1+lamb*tt)*(1-2e-10)
        poly=(aa0-bbeta*tt*tt)*rmt*rmt-bb*rmt+ccap
        assert abs(poly) <= 5e-8*ccap
        numerical_checks+=2
    for tt in np.linspace(0,Tv,13):
        rpt=(bb+math.sqrt(DD+4*bbeta*ccap*tt*tt))/(2*(aa0-bbeta*tt*tt))
        assert rpt<=rp+2*vvplus*tt+1e-9*ee
        numerical_checks+=1

# The comparison ceiling is explicit; it is not an assigned actual energy.
j=20; a=1/(100*j); kap=1.; fv=1.; Rphys=4.
q=math.ceil(Rphys/a)+3
N=3*q*(q+1)**2; MQ=3*q*q*(q+1); CQ=12*q*(q+1)
aa=kap*kap*a*a; g2=kap*a/2
Lambda=min(2*MQ,6*g2*math.sqrt(N*MQ))+2*CQ
A1v=3*(2/a)**3  # exact all-three-orientation tent quadrature
cc=9*aa/64; aa0=1+cc; bb=Lambda+4*cc*A1v; ccap=4*cc*A1v*A1v
DD=bb*bb-4*aa0*ccap
rm=2*ccap/(bb+math.sqrt(DD)); rp=(bb+math.sqrt(DD))/(2*aa0)
pshape=3*A1v/(8*fv); Tv=1/(4*fv*math.sqrt(aa))
vm=rm*rm/(2*pshape)
vp=fv*math.sqrt(aa)*(2*math.sqrt(ccap)+rp)/(2*(.75+cc))
assert pshape>2
negative_first_bound=1/(rm*(1-1/pshape))
assert negative_first_bound>1/rm

plt.rcParams.update({'font.size':10,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(14,11),layout='constrained')
gs=fig.add_gridspec(4,2,height_ratios=[.85,1,1,.70])
ax=fig.add_subplot(gs[0,:]); ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
def box(x,y,w,h,label,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',facecolor=color,edgecolor='#334155'))
    ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=11)
box(.017,.30,.26,.54,'Original positive ground state\n'+r'$d\mu=\psi^2dU,\quad Y=\sum_p|f_p|(2-W_p)$'+'\nRadius-two metric; all vertex gauges','#e0f2fe')
box(.369,.30,.26,.54,'Exact weighted score square\n'+r'$P_t(d_t)+\mathcal{D}_t=0,\quad\mathcal{D}_t\geq0$'+'\nLR10–LR14; original source zero','#dcfce7')
box(.723,.30,.26,.54,'Two roots and retained energy\n'+r'$r_-\leq\mu Y\leq r_+\leq e$'+'\n'+r'$Y+\mathcal{A}=e+\alpha F s_Q$'+'  (LR35)','#fef3c7')
for x1,x2 in [(.285,.354),(.641,.71)]:
    ax.add_patch(FancyArrowPatch((x1,.57),(x2,.57),arrowstyle='->',mutation_scale=15,lw=1.5))
ax.set_title('Both root tails, inverse moments, and the exact retained-energy contraction',fontsize=15,pad=8)
ax.text(.5,.10,'Curves below use the proved comparison ceiling e ≤ FΛQ; the actual ground law is neither sampled nor assigned.',ha='center',fontsize=10)

ax1=fig.add_subplot(gs[1,0]); lo=np.linspace(0,min(.08*rm,5*math.sqrt(2*vm)),350)
uu=1-lo/rm
loglower=pshape*(lo/rm+np.log1p(-lo/rm))
ax1.plot(lo,loglower,color='#0369a1',lw=2.2,label='LR19: complete logarithmic bound')
ax1.plot(lo,-lo**2/(4*vm),'--',color='#64748b',label='LR19: quadratic consequence')
ax1.set_xlabel(r'Original deficit $r$ below comparison root $r_-(F\Lambda_Q)$')
ax1.set_ylabel('Log probability upper bound'); ax1.set_title(r'$\mu(Y\leq r_--r)$'); ax1.grid(alpha=.25); ax1.legend(fontsize=9)
ax2=fig.add_subplot(gs[1,1]); hi=np.linspace(0,5*math.sqrt(2*vp),350)
assert hi[-1]<2*vp*Tv
ax2.plot(hi,-hi*hi/(4*vp),color='#b45309',lw=2.2)
ax2.set_xlabel(r'Original excess $r$ above comparison root $r_+(F\Lambda_Q)$')
ax2.set_ylabel('Log probability upper bound'); ax2.set_title(r'$\mu(Y\geq r_++r)$  (LR23)'); ax2.grid(alpha=.25)
ax2.text(.04,.07,f'j={j}, a=1/2000, κ*=1; q={q}\nA₁={A1v:.6g}; ΛQ={Lambda:.6g}\nr₋={rm:.6g}; r₊={rp:.6g}',transform=ax2.transAxes,fontsize=9,bbox={'facecolor':'white','alpha':.9,'edgecolor':'#cbd5e1'})

ax3=fig.add_subplot(gs[2,0]); ax3.axis('off')
ax3.text(.02,.97,'Actual lower endpoint is controlled (LR18–LR30)',va='top',fontsize=12,weight='bold')
ax3.text(.02,.77,r'$M(-t)\leq(1+\lambda_-t)^{-p_0}\quad(t\geq0)$',fontsize=13)
ax3.text(.02,.55,r'$p_0=3A_1/(8F),\qquad\lambda_-=r_-/p_0$',fontsize=12)
ax3.text(.02,.33,r'$\mu Y^{-k}\leq r_-^{-k}\prod_{\ell=1}^{k}(1-\ell/p_0)^{-1}$',fontsize=12)
ax3.text(.02,.10,r'$\mu Y^{-k}=O(a^{2k}),\qquad\mu(Z_Q/Y)=O(a^{-2})$',fontsize=12)
ax4=fig.add_subplot(gs[2,1]); ax4.axis('off')
ax4.text(.02,.97,'Full retained sum is controlled (LR44–LR46)',va='top',fontsize=12,weight='bold')
ax4.text(.02,.77,r'$\operatorname{Var}(Y+\mathcal{A})=\mathcal{B}\leq\mathcal{B}_{\rm up}=O(a^{-1})$',fontsize=12)
ax4.text(.02,.55,r'$\operatorname{Cov}(Y,\mathcal{A})=c_Y-\operatorname{Var}Y$',fontsize=12)
ax4.text(.02,.33,r'$\operatorname{Var}\mathcal{A}-\operatorname{Var}Y=\mathcal{B}-2c_Y$',fontsize=12)
ax4.text(.02,.10,'The signed covariance is retained.\nThe root interval still has width O(a⁻²).',fontsize=11)
ax5=fig.add_subplot(gs[3,0]); ax5.axis('off')
ax5.text(.02,.93,'Next weighted contraction (LR52–LR57)',va='top',fontsize=12,weight='bold')
ax5.text(.02,.56,r'$\mu\left[((e-Y)_+-\mathcal{A})^2/Y^k\right]=O(a^{2k-1})$',fontsize=12)
ax5.text(.02,.16,'Every fixed integer k ≥ 1; original law and energy.\nFinite constants retain crossing and score terms.',fontsize=11)
ax6=fig.add_subplot(gs[3,1]); ax6.axis('off')
ax6.text(.02,.93,'Exact map for the signed test (LR58)',va='top',fontsize=12,weight='bold')
ax6.text(.02,.56,r'$\mathcal{A}_f=\mathcal{A}+2Y_-,\quad C_f+a\mathcal{A}_f=a(Y+\mathcal{A})$',fontsize=12)
ax6.text(.02,.16,r'$\operatorname{Var}(C_f+a\mathcal{A}_f)=a^2\mathcal{B}=O(a)$'+'\nOriginal variance retains the covariance term.',fontsize=11)
fig.text(.5,-.043,'Reproducible source: check_lower_side.py. Exact original-path counts; f(x)=∏ᵢ(1−|xᵢ|/2)₊, all three face orientations.\nThe curves are proved bounds in the original Y coordinate, not ground-density plots. Full proofs and boundary terms: LR1–LR58.',ha='center',fontsize=9)
fig.savefig(root/'lower_side_and_energy.png',dpi=180,bbox_inches='tight')
fig.savefig(root/'lower_side_and_energy.svg',bbox_inches='tight')
plt.close(fig)

raw=(root/'LOWER_SIDE_RETAINED_ENERGY.md').read_bytes()
assert re.search(rb'\r(?!\n)',raw) is None, 'isolated raw carriage return'
doc=raw.decode('utf8').replace('\r\n','\n')
assert not [(i,ord(ch)) for i,ch in enumerate(doc) if ord(ch)<32 and ch not in '\n\t']
for left,right in [(r'\(',r'\)'),(r'\[',r'\]')]:
    assert doc.count(left)==doc.count(right),(left,doc.count(left),doc.count(right))
depth=0
for i,ch in enumerate(doc):
    if ch in '{}':
        slash=0; k=i-1
        while k>=0 and doc[k]=='\\': slash+=1; k-=1
        if slash%2: continue
        depth+=1 if ch=='{' else -1
        assert depth>=0
assert depth==0
assert re.findall(r'\\tag\{(LR\d+)\}',doc)==['LR'+str(i) for i in range(1,59)]
env_stack=[]
for action,name in re.findall(r'\\(begin|end)\{([^}]+)\}',doc):
    if action=='begin': env_stack.append(name)
    else: assert env_stack.pop()==name
assert not env_stack
report={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'symbolic_checks':symbolic_checks,'finite_root_and_envelope_checks':numerical_checks,'source_serialization':'passed; controls, braces, delimiters, environment order, LR1–LR58','figure_parameters':{'j':j,'a':a,'kappa_star':kap,'q':q,'N_Q':N,'M_Q':MQ,'C_Q':CQ,'A1':A1v,'Lambda_Q':Lambda,'comparison_lower_root':rm,'comparison_upper_root':rp,'p0':pshape,'V_minus':vm,'V_plus':vp},'mathematical_scope':'Actual-law bounds and exact remainders; finite checks do not substitute for proof.'}
(root/'LOWER_SIDE_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps(report,indent=2))
