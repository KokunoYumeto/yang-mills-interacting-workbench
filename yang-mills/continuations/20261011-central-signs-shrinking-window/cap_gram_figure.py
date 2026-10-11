from pathlib import Path
import json
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
mp.mp.dps=60
ROOT=Path(__file__).resolve().parent
q=mp.mpf
C2=q(24398405)/306317856079872;c6=(q(23)/24)**10/588
GH=mp.matrix([[1,1,q(5)/4],[1,q(5)/4,q(7)/4],[q(5)/4,q(7)/4,q(21)/8]])
LH=mp.cholesky(GH);LI=LH**-1
GV=mp.matrix([[q(1)/4,0],[0,q(1)/24]]);VI=mp.cholesky(GV)**-1
rows=[]
for i in range(25):
 r=mp.power(10,q(-2)+q(i)/12);R=r/2;delta=1-mp.cos(R)
 weight=lambda y:mp.sqrt(y*(2-delta*y))
 den=mp.quad(weight,[0,1])
 avg=lambda f:mp.quad(lambda y:weight(y)*f(delta*y),[0,1])/den
 CM=mp.matrix([[avg(lambda u:u**(a+b)) for b in range(3)] for a in range(3)])
 CV=mp.matrix([[avg(lambda u:u*(2-u)*(1-u)**(a+b)/3) for b in range(2)] for a in range(2)])
 scalar=mp.eigsy(LI*CM*LI.T,eigvals_only=True)[0]
 vector=mp.eigsy(VI*CV*VI.T,eigvals_only=True)[0]
 tensor=avg(lambda u:(u*(2-u))**2)/(q(5)/8)
 J=mp.quad(lambda t:mp.sin(t)**2,[0,R])
 I=[mp.quad(lambda t:mp.sin(t)**4*mp.cos(t)**k,[0,R]) for k in range(3)]
 V=[mp.quad(lambda t:mp.sin(t)**2*f(mp.cos(t)),[0,R]) for f in [lambda c:c*c+2,lambda c:c*(2*c*c+1),lambda c:4*c**4-2*c*c+1]]
 ds=16*(I[2]-I[1]**2/I[0])/J
 dv=2*(V[2]-V[1]**2/V[0])/J
 dt=q(2)/5*(4*I[2]+6*I[0])/J
 mass=min(scalar,vector,tensor);grad=min(ds,dv,dt)
 assert mass>=C2*r**8 and grad>=c6*r**6
 rows.append({k:mp.nstr(v,45) for k,v in dict(radius=r,mass_scalar=scalar,mass_vector=vector,mass_tensor=tensor,mass_minimum=mass,mass_proved=C2*r**8,gradient_scalar=ds,gradient_vector=dv,gradient_tensor=dt,gradient_minimum=grad,gradient_proved=c6*r**6).items()})
(ROOT/'CAP_GRAM_FIGURE_VALUES.json').write_text(json.dumps({'precision':60,'method':'Numerical quadrature and eigenvalues of the exact PS5–PS12 and PG5–PG17 matrices; mathematical inequalities are proved in the notes.','rows':rows},indent=2)+'\n',encoding='utf-8',newline='\n')
plt.rcParams.update({'font.size':12,'svg.hashsalt':'cap-gram-20261011'})
fig,axs=plt.subplots(1,2,figsize=(13,6.4));fig.patch.set_facecolor('#f8fafc')
xs=[float(x['radius']) for x in rows]
for ax,kind,color,power,title,denom in [(axs[0],'mass','#2563eb',8,'Complete polynomial mass','cap average of |P|² / full Haar norm²'),(axs[1],'gradient','#0f766e',6,'Complete gradient energy','cap average of |∇P|² / quadratic Haar norm²')]:
 ax.set_facecolor('#f8fafc')
 for block,sty in [('scalar','-'),('vector',':'),('tensor','-.')]:
  ax.loglog(xs,[float(x[kind+'_'+block]) for x in rows],sty,color=color,alpha=.65,label=block+' block, numerical')
 ax.loglog(xs,[float(x[kind+'_proved']) for x in rows],'--',color='#be123c',lw=2.3,label='proved uniform bound: radius$^{'+str(power)+'}$')
 ax.set_title(title,fontsize=16);ax.set_xlabel('Physical cap radius r (original radius-two metric)');ax.set_ylabel(denom)
 ax.grid(True,which='major',alpha=.22);ax.legend(fontsize=9,loc='upper left')
fig.suptitle('Exact cap matrices retain the affine terms',fontsize=20,y=.985)
fig.text(.5,.052,'Mass: PS5–PS12. Gradient: PG5–PG17; scalar and vector affine coefficients are minimized in their full Gram blocks.\nSolid/dotted curves use 60-digit quadrature of those matrices. Dashed bounds have complete analytical proofs.\nAveraging every cap centre transfers these bounds to the actual conditional vacuum densities.',ha='center',fontsize=10.5,linespacing=1.6)
fig.subplots_adjust(left=.09,right=.98,wspace=.32,bottom=.25,top=.86)
for ext in ['png','svg']:fig.savefig(ROOT/f'CAP_GRAM_COMPARISON.{ext}',dpi=180,metadata={'Creator':'Matplotlib'})
plt.close(fig)
