from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent
fig=plt.figure(figsize=(14,9.2),facecolor='#f7f9fc')
ax=fig.add_axes([0,0,1,1]);ax.set_axis_off()
def text(x,y,s,size=17,color='#182b40',weight=None):
 ax.text(x,y,s,fontsize=size,color=color,weight=weight,va='top',transform=ax.transAxes)
def box(x,y,w,h,color):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',facecolor=color,edgecolor='#71859d',linewidth=1.2,transform=ax.transAxes))
text(.04,.965,'Actual Hessian bounds keep the full physical response',22,weight='bold')
text(.04,.914,r'Original radius-two metric:  $c_j=2/(\kappa_*a_j)$,  $d_j=N_j-V_j+1$,  $P=P_{\rm cyc}$',16)
box(.04,.50,.43,.34,'#e5f0f0');box(.52,.50,.44,.34,'#eee9f7')
text(.06,.817,'Every translated original ground state',17,weight='bold')
text(.06,.765,r'$K_\tau\geq-c_jP,\quad B_\tau=K_\tau+c_jP\geq0$',19)
text(.06,.704,r'$K_\tau=B_\tau-c_jP$',18)
text(.06,.647,r'$t_\tau=c_jd_j+(V_\tau(\mathbf{I})-E_0)/(3\kappa_*)$',16)
text(.06,.587,r'$U_j=c_jd_j+(4b_jM_j-E_0)/(3\kappa_*)$',16)
text(.54,.817,'Complete conditional matrix variance',17,weight='bold')
text(.54,.765,r'$\mathfrak{V}=\sum_\tau p_\tau(K_\tau-\overline{K})^2$',20)
text(.54,.698,r'$0\leq\mathfrak{V}\leq U_j\overline{B}-\overline{B}^{\,2}\leq U_j^2P/4$',17)
text(.54,.630,r'$\mathrm{Tr}\,\mathfrak{V}\leq(1-d_j^{-1})U_j^2$',19)
text(.54,.567,r'$\Delta\mathcal{F}(\mathbf{I})=6\,\mathrm{Tr}\,\mathfrak{V}$',19)
box(.04,.205,.92,.245,'#ffffff')
text(.06,.426,'Exact receiving map for every original complex face sample',17,weight='bold')
text(.06,.374,r'$Y_\varphi=\sum_p\varphi(x_p)K^{r_{\partial p}},\qquad \sigma_\varphi^2=\varphi^*C^{\rm face}\varphi$',19)
text(.06,.314,r'$Y_\varphi^*Y_\varphi\leq4\sigma_\varphi^2\mathfrak{V},\qquad K^x=\frac{a_j}{4}R\,\mathrm{diag}(\varphi_pr_{\partial p})R^{\mathsf{T}}-a_jY_\varphi$',18)
text(.06,.254,r'$|\mathrm{Tr}(Y_\varphi^*K^{f_z^0})|\leq2\sqrt{\sigma_\varphi^2\,\mathrm{Tr}\,\mathfrak{V}}\ \Vert K^{f_z^0}\Vert_{\rm HS}$',18)
text(.04,.164,'HCB8 also bounds the entire global conditional Hessian variance and mean square.',15)
text(.04,.126,r'Its exact upper function is $3b_jM_j/\kappa_*=(720000j^{14}+360000j^{10})/\kappa_*^2$.',15)
text(.04,.080,'Proof: HCB1–HCB10. All gauge directions, original face incidences and vacuum energy remain.',12)
text(.04,.047,'The resolvent Hessian is retained in the response. These upper functions do not assign a limiting spectral mass.',12)
for ext in ['png','svg']:
 fig.savefig(O/('ACTUAL_HESSIAN_BOUNDS.'+ext),dpi=180,facecolor=fig.get_facecolor())
plt.close(fig)
