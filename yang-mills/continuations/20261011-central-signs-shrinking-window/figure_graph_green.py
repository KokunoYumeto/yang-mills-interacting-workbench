from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
# Import performs and records the accompanying independent finite checks.
from check_graph_green import graph,block
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'axes.titlesize':13,'figure.facecolor':'white','svg.fonttype':'none'})
edges,G=graph(3);H=np.linalg.inv(G)
fig,axes=plt.subplots(1,2,figsize=(12,5.4),layout='constrained')
for ax,M,title in [(axes[0],G,'Original face matrix, q = 3'),(axes[1],H,'Complete inverse on the same 36 edges')]:
    im=ax.imshow(M,cmap='viridis');fig.colorbar(im,ax=ax,shrink=.75)
    for pos in [11.5,23.5]:ax.axhline(pos,color='white',lw=.8);ax.axvline(pos,color='white',lw=.8)
    ax.set_xticks([5.5,17.5,29.5],['direction 1','direction 2','direction 3'])
    ax.set_yticks([5.5,17.5,29.5],['direction 1','direction 2','direction 3'])
    ax.set_title(title);ax.tick_params(axis='x',rotation=15)
fig.suptitle('Every original face pair and every retained boundary contribution',fontsize=15)
fig.supxlabel('Edge ordering: direction, then lexicographic original integer coordinates.\nGG1–GG5: 24 common component modes and 12 one-component boundary modes; G H = I.',fontsize=10)
for ext in ['png','svg']:fig.savefig(O/('EXACT_PATCH_GREEN_MATRIX.'+ext),dpi=180)
plt.close(fig)
v=json.loads((O/'GRAPH_GREEN_CHECKS.json').read_text());rows=v['original_path_diagnostics']
fig=plt.figure(figsize=(12,8),layout='constrained');gs=fig.add_gridspec(2,2,height_ratios=[1,1.05])
ax=fig.add_subplot(gs[0,0]);ax.plot([r['j'] for r in rows],[r['ratio'] for r in rows],'o-',label='equal-component diagnostic')
ax.axhline(1,color='black',ls='--',label='proved comparison limit')
ax.set(xlabel='original regulator index j',ylabel='Green form / (a × reference)',title='Common component: original source scale');ax.legend(fontsize=9);ax.grid(alpha=.2)
ax=fig.add_subplot(gs[0,1]);ax.semilogy([r['j'] for r in rows],[r['traceless_over_a_over_target'] for r in rows],'s-',color='#b24c20')
ax.set(xlabel='original regulator index j',ylabel='Green form / (a × same reference)',title='Pointwise component sum zero');ax.grid(alpha=.2)
ax=fig.add_subplot(gs[1,:]);ax.set_xlim(0,12);ax.set_ylim(0,3.3);ax.axis('off')
boxes=[(.1,1.4,2.3,'Original source k\nand actual matrix Z'),(3.1,1.4,2.3,r'$c_0=Z^{-1}k$'+'\nfull coefficient vector'),(6.1,1.4,2.3,r'$w=G^{1/2}Z^{-1}k$'+'\nexact graph image'),(9.1,1.4,2.7,r'$T=G^{-1/2}ZB$'+'\noriginal source frame')]
for x,y,width,txt in boxes:
    ax.add_patch(FancyBboxPatch((x,y),width,.9,boxstyle='round,pad=.07',facecolor='#edf3f7',edgecolor='#4a6578'))
    ax.text(x+width/2,y+.45,txt,ha='center',va='center',fontsize=10)
for x0,x1 in [(2.5,3),(5.5,6)]:
    ax.annotate('',xy=(x1,1.85),xytext=(x0,1.85),arrowprops={'arrowstyle':'->','lw':1.6})
ax.text(6,.72,r'$D=T^*T=B^*ZG^{-1}ZB,\quad r=B^*k$'+'\n'+r'$\|w\|^2=r^*D^+r+\|w-TD^+r\|^2$',ha='center',va='center',fontsize=14)
ax.text(6,2.95,'GG6–GG8 and GG14: matrix order, raw frame and full residual retained',ha='center',fontsize=12)
fig.suptitle('Evaluated source Green limit and its exact physical receiver',fontsize=15)
fig.supxlabel('Top panels use specified diagnostic face means 2 − a, not sampled Yang–Mills vacuum data.\nR = 0.04; a = 1/(100j); original fitting cube. Full tests and reference integral: GG10–GG12.',fontsize=10)
for ext in ['png','svg']:fig.savefig(O/('SOURCE_GREEN_LIMIT_AND_RECEIVER.'+ext),dpi=180)
plt.close(fig)
print(json.dumps({'figures':['EXACT_PATCH_GREEN_MATRIX','SOURCE_GREEN_LIMIT_AND_RECEIVER']}))
