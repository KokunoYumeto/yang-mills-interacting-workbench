from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
fig,axs=plt.subplots(1,3,figsize=(13.5,5.1))
rows=[(r'$F_{10}\longrightarrow2q\Phi_0$',[12,0,0],r'$\|F\|^2\to12$, energy moment $12\delta_*$'),
 (r'$F_{21}\longrightarrow-2q^3\Phi_0$',[2700,2160,1440],r'$\|F\|^2\to6300$, energy moment $11340\delta_*$'),
 (r'$F_{21}+15F_{10}\longrightarrow-2(q^3-15q)\Phi_0$',[0,2160,1440],r'$\|F\|^2\to3600$, energy moment $8640\delta_*$')]
for ax,(title,y,cap) in zip(axs,rows):
 ax.bar([1,2,3],y,color=['#247e88','#976249','#8773a8'],width=.6)
 top=max(y)*1.25
 for x,v in enumerate(y,1):ax.text(x,v+top*.025,str(v),ha='center',fontsize=12)
 ax.set_xticks([1,2,3],['1','2','3']);ax.set_ylim(0,top)
 ax.set_xlabel(r'Excitation energy / $\delta_*$');ax.set_ylabel('Raw spectral mass')
 ax.set_title(title,fontsize=11,pad=18)
 ax.spines[['top','right']].set_visible(False)
 ax.text(.5,-.24,cap,transform=ax.transAxes,ha='center',fontsize=9)
fig.suptitle('Complete fixed-box spectral weights of the original phase vectors',fontsize=16,y=.98)
fig.text(.5,.08,r'Exact oscillator closure: $\mathrm{span}\{q\Phi_0,\,uq\Phi_0,\,q^3\Phi_0\}$. '
 r'Original two-dimensional compression residual: $864\delta_*^2$.',ha='center',fontsize=11)
fig.text(.5,.025,r'Fixed $L,a$, then $g\downarrow0$. All other oscillator modes remain in their vacuum. Proofs: SP1–SP16.',ha='center',fontsize=10)
fig.subplots_adjust(left=.06,right=.98,top=.8,bottom=.3,wspace=.33)
for ext in ['png','svg']:
 p=ROOT/('PHASE_SPECTRAL_WEIGHTS.'+ext);fig.savefig(p,dpi=180)
 if ext=='svg':p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8',newline='\n')
