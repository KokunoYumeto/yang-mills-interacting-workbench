from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(13,8),layout='constrained')
ax.set_axis_off();ax.set_xlim(0,1);ax.set_ylim(0,1)
blue='#24577d';green='#24684d';red='#ac492d'
ax.text(.03,.95,'Common smooth coefficient: the retained zero atom',fontsize=23,weight='bold')
ax.text(.03,.85,r'$h_\varphi=(\varphi,\varphi,\varphi),\qquad\varphi\in C_c^1(\mathcal{Q})$',fontsize=22)
ax.text(.03,.72,r'$u=a_j\lambda:\quad'
        r'\langle h_\varphi,\widehat{\mathcal{M}}^\perp_j([\varepsilon,\infty])h_\varphi\rangle=O(a_j^2)$',fontsize=20,color=blue)
ax.text(.03,.63,'A surviving common-coefficient norm concentrates at u = 0.',fontsize=14)
ax.annotate('',xy=(.5,.47),xytext=(.5,.58),arrowprops=dict(arrowstyle='->',lw=2,color=green))
ax.text(.03,.43,r'$v=a_j^{1/3}\lambda,\qquad u=a_j^{2/3}v$',fontsize=23,color=green)
ax.text(.03,.29,r'$\int v^3\,d\nu_{\varphi,j}(v)'
        r'\ \longrightarrow\ \frac{3}{\kappa_*}\int_{\mathcal{Q}}|\nabla\varphi|^2$',fontsize=23,color=green)
ax.text(.03,.20,'Every limiting mass has no infinity atom at this finer scale.\n'
        'TFC22 strengthens this to a bounded second moment at the original energy λ.',fontsize=13)
ax.text(.03,.08,r'$r=\lambda/s_j=\frac{v}{100\kappa_*a_j^{4/3}}$',fontsize=21,color=red)
ax.text(.52,.08,'Finite v does not yet give a finite physical r.',fontsize=13,color=red)
fig.text(.5,-.02,'Proofs: TWO_FORM_FORCE_AND_COMMON_SPECTRUM.md, TFC15 and TFC18–TFC20. '
         'All three variables are explicit maps from the original energy λ.',ha='center',fontsize=10)
for ext in ['png','svg']:fig.savefig(O/('COMMON_FORCE_SCALE.'+ext),dpi=170,bbox_inches='tight')
