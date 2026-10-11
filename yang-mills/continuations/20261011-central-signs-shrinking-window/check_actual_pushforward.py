from pathlib import Path
import json, datetime, math, re, hashlib
import sympy as s
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

root=Path(__file__).parent
y,F,A1,alpha,e,t,h,k,z,r,u,rho=s.symbols('y F A1 alpha e t h k z r u rho',positive=True)
B=s.symbols('B',real=True)
Bstar=-y*k/h
assert s.expand(y*z+2*B*k+B*B*h/y-(y*z-y*k*k/h+(B-Bstar)**2*h/y))==0
J=6*A1-3*y
B0=J/(32*F)
R=3*(16*F*y-h)/(32*F)+J*J*(16*F-h/y)/(1024*F*F)
Q0=y*z+2*B0*k+B0*B0*h/y
# Integrated integration-by-parts substitutes 2 E[B0 k] = -E[B0' h+B0 J].
Q0ibp=y*z-s.diff(B0,y)*h-B0*J+B0*B0*h/y
assert s.simplify(Q0ibp+R+J*J/(64*F)-3*y/2-y*z)==0

xx=s.symbols('xx',real=True)
v=s.Function('v')(xx); AA=s.Function('A')(xx)
q=v*v
left=s.diff((s.diff(q,xx)-AA*q)/2,xx)-(s.diff(q,xx)-AA*q)**2/(4*q)
assert s.simplify(left-(v*s.diff(v,xx,2)-(s.diff(AA,xx)/2+AA*AA/4)*v*v))==0

Mp,M,Ht,Zt,Rt=s.symbols('Mp M Ht Zt Rt',real=True)
pt=3*alpha*F/2; q0=8*alpha*F*F
At=1+pt*t-q0*t*t; Bt=e+3*alpha*F*A1*t
original=Mp+alpha*F*Zt+Rt-alpha*F/2*(t*t*Ht+t*(6*A1*M-3*Mp))-e*M
Dt=alpha*F*Zt+Rt+alpha*F*t*t/2*(16*F*Mp-Ht)
assert s.simplify(original-(At*Mp-Bt*M+Dt))==0
V,T,rr=s.symbols('V T rr',positive=True)
first=s.integrate(2*rr*s.exp(-rr*rr/(4*V)),(rr,0,2*V*T))
second=s.integrate(2*rr*s.exp(-T*rr+V*T*T),(rr,2*V*T,s.oo))
assert s.simplify(first+second-(4*V+2/(T*T)*s.exp(-V*T*T)))==0

# Exact Z2 central field on the unchanged original open cubic lattice.
m=4
links={}
for zz in np.ndindex(m+1,m+1,m+1):
    for direction in range(3):
        if zz[direction]<m:
            exponent=0 if direction==0 else zz[0] if direction==1 else zz[0]+zz[1]
            links[(zz,direction)]=(-1)**exponent
face_count=0
orientation_counts={}
for zz in np.ndindex(m+1,m+1,m+1):
    for d0 in range(3):
        for e0 in range(d0+1,3):
            if zz[d0]<m and zz[e0]<m:
                zd=list(zz);zd[d0]+=1
                ze=list(zz);ze[e0]+=1
                sign=links[(zz,d0)]*links[(tuple(zd),e0)]*links[(tuple(ze),d0)]*links[(zz,e0)]
                assert sign==-1
                face_count+=1
                orientation_counts[str((d0,e0))]=orientation_counts.get(str((d0,e0)),0)+1
assert face_count==3*m*m*(m+1)

# A literal original-path illustration. f(x)=prod_i (1-|x_i|/2)_+.
# All three translated mesh quadratures are exact for this tent.
j=20; a=1/(100*j); kap=1.; Fv=1.; Rphys=4.
qc=math.ceil(Rphys/a)+3
N=3*qc*(qc+1)**2; Mfaces=3*qc*qc*(qc+1); cross=12*qc*(qc+1)
g2=kap*a/2; av=kap*kap*a*a
Lambda=min(2*Mfaces,6*g2*math.sqrt(N*Mfaces))+2*cross
A1v=3*(2/a)**3
Tval=1/(4*Fv*math.sqrt(av))
Vval=3*av*Fv*A1v+4*Lambda*Fv*math.sqrt(av)/3
offsets=np.linspace(0,14000,401)
assert offsets[-1]<2*Vval*Tval
logbound=-offsets*offsets/(4*Vval)

plt.rcParams.update({'font.size':10,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(13,7.3),layout='constrained')
grid=fig.add_gridspec(2,2,height_ratios=[1.1,1.0])
ax=fig.add_subplot(grid[0,:]); ax.set_axis_off(); ax.set_xlim(0,1); ax.set_ylim(0,1)
def box(x,y,w,h,text,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',facecolor=color,edgecolor='#334155',linewidth=1.1))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=11)
box(.015,.46,.245,.44,"Original source-zero state\n"+r"$d\mu=\psi^2dU,\quad Y=\sum_p|f_p|(2-W_p)$"+"\nRadius-two metric; all vertex gauges",'#e0f2fe')
box(.365,.46,.255,.44,"Actual pushforward (FO11–14)\n"+r"$Y_\#\mu=\rho(y)\,dy,\quad 0\leq y\leq4A_1$"+"\n"+r"$(h\rho)'=(6A_1-3y+2k)\rho$",'#dcfce7')
box(.73,.46,.245,.44,"Complete projection (FO16–19)\n"+r"$B_*=-yk/h$"+"\n"+r"$\mu(YZ_Q)=\int yk^2\rho/h+\mathcal{T}_Y$"+"\n"+r"$\mathcal{T}_Y\geq0$ retained",'#fef3c7')
for xa,xb in [(.27,.353),(.63,.72)]:
    ax.add_patch(FancyArrowPatch((xa,.68),(xb,.68),arrowstyle='->',mutation_scale=16,color='#334155',linewidth=1.5))
ax.text(.5,.20,"Both currents hρ and kρ have zero endpoint values and no critical-value jumps.\nρ is the actual law; no density is guessed or plotted.",ha='center',va='center',fontsize=11)
ax.set_title("Exact maps, score projection, and a proved source-zero upper tail",fontsize=15,pad=8)

ax2=fig.add_subplot(grid[1,0])
ax2.plot(offsets,logbound,color='#0369a1',lw=2.4)
ax2.set_xlabel(r"Original excess $r$ above the explicit ceiling $\Lambda_f$")
ax2.set_ylabel(r"$\log$ of the proved probability upper bound")
ax2.set_title(r"$\mu(Y\geq\Lambda_f+r)\leq \exp[-r^2/(4\overline{V})]$"+"  (FO37)")
ax2.grid(alpha=.25)
ax2.text(.04,.08,f"j={j}, a=1/2000, κ*=1, F=1\nq={qc}; A₁={A1v:.6g}\nΛf={Lambda:.6g}; V̄={Vval:.6g}",transform=ax2.transAxes,bbox={'facecolor':'white','alpha':.88,'edgecolor':'#cbd5e1'},fontsize=9)

ax3=fig.add_subplot(grid[1,1]); ax3.set_axis_off()
ax3.text(.03,.93,"What is controlled (FO38–43)",fontsize=13,weight='bold',va='top')
ax3.text(.03,.76,r"$a^2\mu[(Y-e)_+^2]=O(a),\qquad e=F(E_0-E_{\rm out})/b$",fontsize=12,va='top')
ax3.text(.03,.57,r"$\operatorname{Var}_\mu Y=\mu[(Y-e)_+^2]+\mu[(e-Y)_+^2]-(e-d)^2$",fontsize=11,va='top')
ax3.text(.03,.35,"The actual mean d=μY is retained.\nThe lower-side term and e−d are not set to zero.\nThis is not a plotted vacuum density or a centered-variance claim.",fontsize=11,va='top',linespacing=1.5)
fig.text(.5,-.060,"Figure source: check_actual_pushforward.py. The curve uses the exact original-path lattice counts and the compact tent test f(x)=∏(1−|xᵢ|/2)₊.\nThe horizontal coordinate is the original scalar excess r. The explicit ceiling replaces e only through the proved inequality e≤Λf.",ha='center',fontsize=9)
fig.savefig(root/'actual_pushforward_maps.png',dpi=180,bbox_inches='tight')
fig.savefig(root/'actual_pushforward_maps.svg',bbox_inches='tight')
plt.close(fig)

doc=(root/'ACTUAL_PUSHFORWARD_OPTIMIZATION.md').read_text(encoding='utf8')
bad=[(i,ord(c)) for i,c in enumerate(doc) if ord(c)<32 and c not in '\n\t']
assert not bad
for opening,closing in [(r'\(',r'\)'),(r'\[',r'\]')]:
    assert doc.count(opening)==doc.count(closing),(opening,doc.count(opening),doc.count(closing))
braces=0
for i,c in enumerate(doc):
    if c in '{}':
        slashes=0;jj=i-1
        while jj>=0 and doc[jj]=='\\':slashes+=1;jj-=1
        if slashes%2:continue
        braces+=1 if c=='{' else -1
        assert braces>=0
assert braces==0
tags=re.findall(r'\\tag\{(FO\d+)\}',doc)
assert tags==['FO'+str(n) for n in range(1,57)]
begins=re.findall(r'\\begin\{([^}]+)\}',doc)
ends=re.findall(r'\\end\{([^}]+)\}',doc)
assert sorted(begins)==sorted(ends)
checks={
    'observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'functional_projection_identity':True,
    'fixed_square_receiving_identity':True,
    'conditional_scalar_ground_equation':True,
    'exact_exponential_test_identity':True,
    'two_branch_tail_integral':True,
    'central_link_field_m':m,'central_link_field_faces':face_count,
    'central_link_field_by_orientation':orientation_counts,
    'serialization_controls_delimiters_groups_environments':True,
    'formula_tags':tags,
    'illustration_constants':{'j':j,'a':a,'kappa':kap,'F':Fv,'q':qc,'N_Q':N,'M_Q':Mfaces,'C_Q':cross,'A1':A1v,'Lambda_f':Lambda,'Vbar':Vval,'T':Tval},
    'scope':'Original-lattice central-field check and algebraic checks; the figure plots a proved upper bound, not a sampled or guessed ground-state density.',
}
(root/'ACTUAL_PUSHFORWARD_CHECKS.json').write_text(json.dumps(checks,indent=2),encoding='utf8')
print(json.dumps(checks,indent=2))
