from pathlib import Path
import hashlib, json, math, re, datetime
import numpy as np
import sympy as s
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT=Path(__file__).resolve().parent
count=0
def check(value, label):
    global count
    if not bool(value): raise AssertionError(label)
    count+=1

# Exact symbolic identities. These are algebra checks, not samples of the ground law.
a,k,F,e,Y,q,ell,chi=s.symbols("a k F e Y q ell chi",positive=True)
alpha=k*k*a*a; b=1/(k*a*a); EQ=e*b/F
check(s.simplify(chi*F*a**6/k*(EQ*Y-b/F*Y**2)-chi/k**2*(a*a*Y)*(a*a*e-a*a*Y))==0,"CM54 physical factors")
R=s.symbols("R",positive=True)
L=24*R**2+9*k*R**3
K=(L+s.sqrt(L**2-s.Rational(81,4)*k*k*R**6))/2
check(s.simplify(s.series(K,R,0,5).removeO()-(24*R**2+9*k*R**3-s.Rational(27,128)*k*k*R**4))==0,"CM17 expansion")
c,A,t,h,d,delta,Qrem,Rrem=s.symbols("c A t h d delta Qrem Rrem",positive=True)
alp=s.symbols("alpha",positive=True)
c=9*alp/(4*chi); beta=alp*chi*F**2/4
J=6*A-3*d
base=d*(d+Rrem+alp*F*Qrem+alp*F*J**2/(4*h)-alp*F*t*t*h/4-e)
target=(1+c-beta*t*t)*d*d-(e+4*c*A)*d+4*c*A*A+d*Rrem+alp*F*d*Qrem+alp*J*J*delta/(4*chi*h)+alp*F*t*t*d*delta/4
check(s.simplify((base-target).subs(delta,chi*F*d-h))==0,"CM7 full polynomial and remainders")
mx,my,vx,vy,cxy=s.symbols("mx my vx vy cxy",real=True)
check(s.expand(2*vx+2*vy-(vx+vy+2*cxy)-(vx+vy-2*cxy))==0,"CM60 signed covariance")
p,cq,vol=s.symbols("p cq vol",positive=True)
split=(cq*vol)**(-p)
layer=vol*split + p/(1-p)/cq*split**(1-1/p)
check(s.simplify(s.powdenest(layer,force=True)-cq**(-p)*vol**(1-p)/(1-p))==0,"CM32 layer cake")
eps,A0,tt=s.symbols("eps A0 tt",positive=True)
vv=eps*tt/(A0+tt*tt)
check(s.simplify((tt*vv)*(eps-tt*vv)-A0*vv*vv)==0,"CM63 full root inversion")
check(s.simplify(s.diff(vv,tt)-eps*(A0-tt*tt)/(A0+tt*tt)**2)==0,"CM63 monotonicity interval")

# All three orientation incidence coefficients, with original four edge occurrences.
orient=[(0,1),(0,2),(1,2)]
for f0 in range(5):
 for f1 in range(5):
  for f2 in range(5):
   fs=np.array([f0,f1,f2],dtype=float)
   if not fs.max(): continue
   for n,(d0,d1) in enumerate(orient):
    summed=2*sum(2*fs[z] for z,ori in enumerate(orient) if d0 in ori)+2*sum(2*fs[z] for z,ori in enumerate(orient) if d1 in ori)
    formula=8*fs[n]+4*(fs.sum()-fs[n])
    check(summed==formula,"CM4 ordered edge incidence")
   ch=4+4*fs.sum()/fs.max()
   check(8<=ch<=16,"CM4 chi interval")

# Numeric root and mass inequalities over broad positive parameters, not actual energy samples.
for kval in [.01,.2,1.,7.,100.]:
 for rr in np.geomspace(1e-5,20,71):
  LL=24*rr*rr+9*kval*rr**3
  CC=81*kval*kval*rr**6/16
  dd=math.sqrt(LL*LL-4*CC)
  rp=(LL+dd)/2; rm=2*CC/(LL+dd)
  check(0<rm<=rp<=LL*(1+1e-14),"CM16 mass roots")
  check(abs(rm*rp-CC)<=1e-12*max(CC,1e-99),"root product")
  check(rp<=24*rr**2+9*kval*rr**3+1e-12*LL,"crossing and volume ceiling")

# Finite quadratic-form product expansion: original local outside term retained.
rng=np.random.default_rng(10112026)
for n in range(400):
 ugrad=rng.normal(size=9); wgrad=rng.normal(size=9)
 x=float(rng.uniform(.001,30)); G=float(rng.normal())
 zgrad=rng.normal(size=9)
 # grad(sqrt(Y)*G) is a whole vector zgrad; no independent-law inference.
 A0=x*G*G*np.dot(wgrad,wgrad)
 B0=np.dot(zgrad,zgrad)
 cross0=2*math.sqrt(x)*G*np.dot(wgrad,zgrad)
 kinetic=np.dot(math.sqrt(x)*G*wgrad+zgrad,math.sqrt(x)*G*wgrad+zgrad)
 check(abs(kinetic-(A0+B0+cross0))<1e-10*max(1,kinetic,A0),"CM54 kinetic expansion")
 check(abs(cross0)<=2*math.sqrt(A0*B0)+1e-10,"CM54 cross bound")
 # Actual Cauchy remainder with unrestricted vector coordinates.
 check(np.dot(wgrad,wgrad)*np.dot(ugrad,ugrad)-np.dot(wgrad,ugrad)**2>=-1e-10,"CM53 Cauchy remainder")

# Mixed compression identities on a finite-dimensional algebraic sample.
# This checks the exact map, not Yang--Mills covariance or its Gram rank.
for n in range(160):
 U,_=np.linalg.qr(rng.normal(size=(7,7)))
 projection=U[:,:3]@U[:,:3].T
 aa=np.diag(rng.normal(size=7)); bb=np.diag(rng.normal(size=7))
 ka=(np.eye(7)-projection)@aa@projection
 kb=(np.eye(7)-projection)@bb@projection
 va=projection@aa@projection; vb=projection@bb@projection
 check(np.linalg.norm(projection@aa@bb@projection-va@vb-ka.T@kb)<1e-12,"CM42 product defect")
 check(np.linalg.norm(va@vb-vb@va-(kb.T@ka-ka.T@kb))<1e-12,"CM42 commutator sign")
 GG=np.block([[ka.T@ka,ka.T@kb],[kb.T@ka,kb.T@kb]])
 check(np.linalg.eigvalsh(GG).min()>-1e-12,"CM42 full positive Gram")

text=(ROOT/"SIMULTANEOUS_CENTRAL_MEASURE.md").read_text(encoding="utf-8")
check(not any(ord(c)<32 and c not in "\n\t\r" for c in text),"no raw control characters")
check("\r" not in text,"no interpreted carriage-return in loaded source")
tags=re.findall(r"\\tag\{CM(\d+)\}",text)
check(tags==[str(i) for i in range(1,64)],"all CM1--CM63 tags in order")
blocks=re.findall(r"\\\[(.*?)\\\]|\\\((.*?)\\\)",text,re.S)
for n,pair in enumerate(blocks):
 body=pair[0] or pair[1]
 depth=0
 for pos,char in enumerate(body):
  if char in "{}" and (pos==0 or body[pos-1]!="\\"):
   depth += 1 if char=="{" else -1
   check(depth>=0,f"math group prefix {n}")
 check(depth==0,f"math group balance {n}")
 check(body.count(r"\left")==body.count(r"\right"),f"left-right balance {n}")
check(text.count(r"\[")==text.count(r"\]"),"display delimiter counts")
check(text.count(r"\(")==text.count(r"\)"),"inline delimiter counts")
expected="7ddf0c7c480987aa02244b13720e74e888db2608914679d5adc3b0cda4b1d3e8"
check(hashlib.sha256((ROOT/"BOUNDED_ENERGY_MULTIPLIER.md").read_bytes()).hexdigest()==expected,"complete finite basis preserved")

plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.spines.top":False,"axes.spines.right":False})
fig,axes=plt.subplots(1,3,figsize=(16,5.3),constrained_layout=True)
r=np.geomspace(.005,3,500); kap=1.
Lr=24*r*r+9*kap*r**3; disc=np.sqrt(Lr*Lr-81*kap**2*r**6/4)
upper=(Lr+disc)/2; lower=(81*kap**2*r**6/8)/(Lr+disc)
ax=axes[0]
ax.loglog(r,Lr,":",color="#7b8794",lw=2,label=r"$24R^2+9\kappa_*R^3$")
ax.loglog(r,upper,color="#176b87",lw=2,label=r"$K_R=d_+(\mathsf{L}_R,R)$")
ax.loglog(r,lower,color="#a23b72",lw=2,label=r"$d_-(\mathsf{L}_R,R)$")
ax.set(xlabel="Physical cube side R",ylabel="Proved mass bounds",title=r"Original cube bounds ($\kappa_*=1$)")
ax.legend(fontsize=10); ax.grid(alpha=.2)
ax.text(.04,.03,"CM17, CM23, CM33\nParameter illustration; no ground-state sample",transform=ax.transAxes,fontsize=9)
ax=axes[1]
x=np.linspace(0,1,501)
ax.fill_between(x,0,np.minimum(1,x),color="#176b87",alpha=.16)
ax.plot(x,x,color="#176b87",lw=2)
ax.set(xlabel=r"$t/(c_Q |Q|)$",ylabel=r"$|\{h_{\xi,\sigma}<t\}\cap Q|/|Q|$",title="Actual density-component constraint",xlim=(0,1),ylim=(0,1))
ax.text(.07,.77,r"$h_{\xi,\sigma}>0$ a.e."+"\nPossible singular component retained",fontsize=10)
ax.text(.06,.04,"CM30–CM32: only the proved upper envelope\nis drawn; no density is assigned",fontsize=9)
ax.grid(alpha=.2)
ax=axes[2]; ax.axis("off")
entries=[
 ("Original signed sums",r"$C_{\mathbf{f},j}=a_jY_{\mathbf{f},j}$","CM1–CM2"),
 ("Actual central receiver",r"$[a_j C_{\mathbf{f},j}W_j\psi_j]=S_{\mathbf{f}}W\Omega$","CM13–CM18, CM40"),
 ("Locally finite spatial measure",r"$S_{\mathbf{f}}=\sum_\sigma\int f_\sigma\,d\mathsf{M}_\sigma$","CM19–CM28"),
 ("Actual covariance kernel",r"$\mathcal{C}_{\sigma\tau}=\mathbb{E}_\Omega[\nu_\sigma\otimes\nu_\tau]-m_\sigma\otimes m_\tau$","CM34–CM37")]
for n,(title,formula,loc) in enumerate(entries):
 yy=.81-.235*n
 ax.add_patch(FancyBboxPatch((.015,yy),.96,.17,boxstyle="round,pad=.012",facecolor="#eff6f8",edgecolor="#176b87",transform=ax.transAxes))
 ax.text(.5,yy+.13,title,ha="center",va="center",transform=ax.transAxes,fontsize=11,weight="bold")
 ax.text(.5,yy+.079,formula,ha="center",va="center",transform=ax.transAxes,fontsize=9)
 ax.text(.5,yy+.027,loc,ha="center",va="center",transform=ax.transAxes,fontsize=9,color="#4b5563")
 if n<3: ax.annotate("",xy=(.5,yy-.065),xytext=(.5,yy-.003),xycoords="axes fraction",arrowprops={"arrowstyle":"->","color":"#176b87"})
fig.suptitle("One original state path, one ultrafilter: spatial mass and its exact receiving maps",fontsize=15)
fig.savefig(ROOT/"central_measure_bounds.png",dpi=170)
fig.savefig(ROOT/"central_measure_bounds.svg")
plt.close(fig)

fig,ax=plt.subplots(figsize=(15,6.2),constrained_layout=True);ax.axis("off")
ax.text(.5,.95,"Retained energy identity: the current defect is zero",ha="center",fontsize=16,weight="bold",transform=ax.transAxes)
ax.text(.5,.85,r"$\mathcal{K}_{\mathbf{f}}^{*}\mathcal{K}_{\mathbf{f}}+D_{\rm geom}+D_{\rm loc}="
        r"\frac{\chi}{\kappa_*^2}S_{|\mathbf{f}|}(E_{|\mathbf{f}|,Q}I-S_{|\mathbf{f}|})-9J_\Sigma(\mathbf{f})^2I$",
        ha="center",fontsize=18,transform=ax.transAxes)
boxes=[
 (.02,"Current defect",r"$j_{\mathbf{f},j}=a_j^3\Gamma(\log\psi_j,Y_{\mathbf{f},j})$"+"\n"+r"$P_+\mathcal{J}_{\mathbf{f}}=-3J_\Sigma(\mathbf{f})I$"+"\n"+r"$\mathcal{K}_{\mathbf{f}}=\mathcal{J}_{\mathbf{f}}+3J_\Sigma(\mathbf{f})\iota=0$","CM48–CM51; CE13"),
 (.35,"Complete geometric remainder",r"$a_j^6[Z_Q\Gamma Y_{\mathbf{f}}-\Gamma(w,Y_{\mathbf{f}})^2]$"+"\n"+r"$+\,a_j^6 Z_Q(\chi F Y_{|\mathbf{f}|}-\Gamma Y_{\mathbf{f}})$"+"\nAll ordered face derivatives retained","CM52–CM53"),
 (.68,"Original local-energy remainder",r"$\frac{\chi F a_j^6}{\kappa_*}\langle\sqrt{Y}\,u,\mathcal{R}_{\mathbf{f},Q}\sqrt{Y}\,u\rangle$"+"\n"+r"$\mathcal{R}_{\mathbf{f},Q}=b(W_Q-Y/F)$"+"\n"+r"$+(H_{\rm out}-E_{\rm out})+bW_\times$","CM45, CM52, CM54")]
for xx,title,body,loc in boxes:
 ax.add_patch(FancyBboxPatch((xx,.37),.30,.36,boxstyle="round,pad=.01",facecolor="#eff6f8",edgecolor="#176b87",transform=ax.transAxes))
 ax.text(xx+.15,.68,title,ha="center",fontsize=12,weight="bold",transform=ax.transAxes)
 ax.text(xx+.15,.54,body,ha="center",va="center",fontsize=11,linespacing=1.8,transform=ax.transAxes)
 ax.text(xx+.15,.405,loc,ha="center",fontsize=10,color="#4b5563",transform=ax.transAxes)
ax.text(.5,.27,"CM56 preserves every sign, scalar energy, crossing face and actual mean.",ha="center",fontsize=12,transform=ax.transAxes)
ax.text(.5,.19,r"For $\mathbf{f}\geq0$:  $\lim_{\mathcal{U}}a_j^2\mathrm{Var}_{\mu_j}C_{\mathbf{f},j}"
        r"=m(E-m)-9\kappa_*^2J_\Sigma(\mathbf{f})^2/\chi-\kappa_*^2\mathfrak{d}_{\mathbf{f},Q}/\chi$",
        ha="center",fontsize=15,transform=ax.transAxes)
ax.text(.5,.08,"CM58–CM60: actual covariance contraction, including the signed cross term. No covariance value is assigned.\n"
        "CE13 evaluates the current defect to zero; CE24–CE30 retain the geometric and local-energy terms.",
        ha="center",fontsize=11,linespacing=1.6,transform=ax.transAxes)
fig.savefig(ROOT/"retained_current_identity.png",dpi=170)
fig.savefig(ROOT/"retained_current_identity.svg")
plt.close(fig)
receipt={"observed_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"passed":count,
         "math_blocks_audited":len(blocks),"formula_tags":len(tags),
         "checks_scope":"Exact algebra, incidence, root constants, physical factors, finite quadratic/compression identities, source serialization; no numerical ground-state inference.",
         "figures":["central_measure_bounds.png","retained_current_identity.png"]}
(ROOT/"CENTRAL_MEASURE_CHECKS.json").write_text(json.dumps(receipt,indent=2),encoding="utf-8")
print(json.dumps(receipt,indent=2))
