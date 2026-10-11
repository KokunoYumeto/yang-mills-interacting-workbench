from pathlib import Path
import datetime, hashlib, json, re
import numpy as np
import sympy as s
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parent
checks = []
def check(value, label):
    if not bool(value):
        raise AssertionError(label)
    checks.append(label)

a,k,chi,F,d,e,A0,A1,m,G,Gabs,E,E2,geom,loc = s.symbols(
    "a k chi F d e A0 A1 m G Gabs E E2 geom loc", positive=True)
alpha=k*k*a*a
h=3*A1-s.Rational(3,2)*d
mean_s=-3*A0+3*m/(2*a)
var_s=9*G/(4*a*a)-3*E/(2*k*a*a)+E2/(4*k*k*a*a)
finite=mean_s**2+var_s+geom+loc-chi/alpha*(e*d-d*d-Gabs/a**2)-chi*F*h
rhs=a*a*d*(e-d)+alpha*a*a*F*h-alpha*a*a/chi*mean_s**2+3*alpha*E/(2*chi*k)-alpha*E2/(4*chi*k*k)-alpha*a*a/chi*(geom+loc)
check(s.simplify(alpha*a*a/chi*finite-(Gabs+9*alpha*G/(4*chi)-rhs))==0,"CE19 every finite coefficient")
C,r,sc=s.symbols("C r sc",real=True)
j=-3*a**3*A0+s.Rational(3,2)*a*a*C-a*a*r/(2*k)
check(s.simplify(j.subs(r,k*(3*C-6*a*A0-2*a*sc))-a**3*sc)==0,"CE11 ground-transform current")
check(s.simplify(a*a*var_s-(s.Rational(9,4)*G-3*E/(2*k)+E2/(4*k*k)))==0,"CE18 centered score factors")
check(s.simplify(G-2*(E/E2)*E+(E/E2)**2*E2-(G-E**2/E2))==0,"CE21 complete projection remainder")
t,b,xx=s.symbols("t b xx",positive=True)
fun=E**2/b*(1-s.exp(-t*b/E))
check(s.simplify(s.diff(fun,E)-E/b*(2*(1-s.exp(-t*b/E))-(t*b/E)*s.exp(-t*b/E)))==0,"CE49 derivative in first energy")
check(s.simplify(s.diff(fun,b)-E**2/b**2*((1+t*b/E)*s.exp(-t*b/E)-1))==0,"CE49 derivative in second energy")
M=s.Matrix([[1,1,0],[1,0,1],[0,1,1]])
check(M.det()==-2,"CE6 orientation map invertible")
check(M.inv()*M==s.eye(3),"CE6 all inverse coefficients")

rng=np.random.default_rng(20261011)
max_error=0.
for n in range(160):
    aa=float(rng.uniform(.0001,.08))
    lam=np.exp(rng.uniform(-5,6,12))
    weights=rng.uniform(.01,2,12)
    ev=float(weights@lam); e2=float(weights@(lam**2))
    for tau in [.01,.2,1.,5.]:
        nn=float(weights@(-np.expm1(-tau*aa*lam)))/aa
        lo=ev*ev/(aa*e2)*(-np.expm1(-tau*aa*e2/ev))
        check(lo<=nn+1e-10*max(1,nn),"CE48 finite spectral lower bound")
        check(nn<=tau*ev+1e-10*max(1,nn),"CE33 finite spectral upper bound")
        z=e2/ev
        hz=-np.expm1(-tau*aa*z)/(aa*z)
        hp=((1+tau*aa*z)*np.exp(-tau*aa*z)-1)/(aa*z*z)
        hl=-np.expm1(-tau*aa*lam)/(aa*lam)
        rem=hl-hz-hp*(lam-z)
        err=abs(nn-lo-float(weights@(lam*rem)))
        max_error=max(max_error,err/max(1,nn))
        check(rem.min()>=-1e-10*max(1,float(abs(rem).max())),"CE47 tangent remainder sign")
        check(err<=1e-9*max(1,nn),"CE48 exact retained remainder")
        mask=lam<=100*aa
        en=float(weights[mask]@lam[mask])
        win=float(weights[mask]@(-np.expm1(-tau*aa*lam[mask])))/aa
        check(-1e-10<=tau*en-win<=50*tau*tau*aa*aa*en+1e-9,"CE36 original window factor 50")

text=(ROOT/"CURRENT_COVARIANCE_EQUALITY.md").read_text(encoding="utf8")
tags=re.findall(r"\\tag\{CE(\d+)\}",text)
check(tags==[str(i) for i in range(1,51)],"CE1–CE50 ordered tags")
check(not any(ord(c)<32 and c not in "\n\r\t" for c in text),"source control characters")
blocks=re.findall(r"(?s)\\\[.*?\\\]|\\\(.*?\\\)",text)
for i,block in enumerate(blocks):
    depth=0
    for pos,c in enumerate(block):
        if c in "{}" and (pos==0 or block[pos-1]!="\\"):
            depth+=1 if c=="{" else -1
            check(depth>=0,f"group prefix {i}")
    check(depth==0,f"group balance {i}")
    check(block.count(r"\left")==block.count(r"\right"),f"delimiter balance {i}")

plt.rcParams.update({"font.size":12,"figure.facecolor":"white"})
fig,ax=plt.subplots(figsize=(15,9),constrained_layout=True)
ax.axis("off")
ax.text(.5,.965,"Actual current collapse and the surviving heat fluctuation",
        ha="center",weight="bold",fontsize=18,transform=ax.transAxes)
boxes=[
(.68,"Leading current: completely evaluated",
 r"$j_{\mathbf{f}}=a^3\Gamma(w,Y_{\mathbf{f}})=-3a^3A_{0,\mathbf{f}}+\frac{3}{2}a^2C_{\mathbf{f}}-\frac{a^2}{2\kappa_*}r_{\mathbf{f}}$"
 "\n"+r"$\mathcal{J}_{\mathbf{f}}=-3J_\Sigma(\mathbf{f})\iota,\qquad \mathcal{K}_{\mathbf{f}}=0,\qquad \mathcal{H}_{\rm cur}=\mathcal{H}_+$",
 "CE11–CE13: exact finite identity and bounded-word limit"),
(.40,"Next centered current: the same spatial covariance",
 r"$a^2(s_{\mathbf{f}}-\mu s_{\mathbf{f}})=\frac{3}{2}a(C_{\mathbf{f}}-m_{\mathbf{f}})-\frac{a}{2\kappa_*}r_{\mathbf{f}}$"
 "\n"+r"$[a^2(s_{\mathbf{f}}-\mu s_{\mathbf{f}})W\psi]=\frac{3}{2}(S_{\mathbf{f}}-\langle S_{\mathbf{f}}\rangle)W\Omega$",
 "CE14–CE15: squared receiving error = "+r"$a^2E_{2,\mathbf{f}}/(4\kappa_*^2)=O(a)$"),
(.12,"Further fluctuation: survives for every "+r"$\tau>0$",
 r"$v_{\tau,j}=a_j^{-1/2}(I-e^{-\tau a_j A_j})^{1/2}u_{\mathbf{f},j}$"
 "\n"+r"$0<\frac{e_{\mathbf{f}}^2}{D_{\mathbf{f}}}(1-e^{-\tau D_{\mathbf{f}}/e_{\mathbf{f}}})\leq\liminf\|v_{\tau,j}\|^2\leq\tau U_{\mathbf{f}}$",
 "CE46–CE50: full positive spectral remainder retained")]
for y,title,body,caption in boxes:
    ax.add_patch(FancyBboxPatch((.025,y),.95,.23,boxstyle="round,pad=.012",facecolor="#eff6f8",edgecolor="#176b87",transform=ax.transAxes))
    ax.text(.5,y+.185,title,ha="center",weight="bold",fontsize=14,transform=ax.transAxes)
    ax.text(.5,y+.106,body,ha="center",va="center",linespacing=1.8,fontsize=15,transform=ax.transAxes)
    ax.text(.5,y+.025,caption,ha="center",fontsize=11,transform=ax.transAxes)
ax.text(.5,.045,r"Original window $s_j=\kappa_*/j$: $\|[P_j^{\rm win}v_{\tau,j}]\|^2=\tau e_{\mathbf{f}}^{\rm win}$ (CE36).",
        ha="center",fontsize=13,transform=ax.transAxes)
ax.text(.5,.009,"The actual window-energy coefficient remains to be evaluated; whole-vector survival does not determine it.",
        ha="center",fontsize=11,transform=ax.transAxes)
fig.savefig(ROOT/"CURRENT_COVARIANCE_MAP.png",dpi=170)
fig.savefig(ROOT/"CURRENT_COVARIANCE_MAP.svg")
plt.close(fig)
out={"utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"passed":len(checks),
     "math_blocks":len(blocks),"source_sha256":hashlib.sha256((ROOT/"CURRENT_COVARIANCE_EQUALITY.md").read_bytes()).hexdigest(),
     "maximum_relative_spectral_identity_error":max_error,
     "scope":"Exact algebra and spectral identities on finite positive test measures; these diagnostics do not sample or determine the Yang–Mills ground-state covariance."}
(ROOT/"CURRENT_COVARIANCE_CHECKS.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf8")
print(json.dumps(out,indent=2))
