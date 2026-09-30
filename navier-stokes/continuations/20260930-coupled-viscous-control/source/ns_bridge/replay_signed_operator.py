"""Exact algebra checks for the signed axisymmetric Navier--Stokes bridge."""
from pathlib import Path
import hashlib, json
import sympy as sp

z=sp.symbols('z', real=True)
y=sp.symbols('y', positive=True)
hfun=sp.Function('h')(z,y)
Qop=lambda f: sp.diff(f,z,2)+2*y*sp.diff(f,y,2)
Mop=lambda f: Qop(f)+4*sp.diff(f,y)
nu,r,v2=sp.symbols('nu r v2', nonzero=True)
G,h,xi,ft=sp.symbols('G h xi ft')
DG,QG,Dh,Mh,Dxi,Mxi,grad2=sp.symbols('DG QG Dh Mh Dxi Mxi grad2')
fmer=sp.symbols('fmer')
checks=[]
def check(name, expr): checks.append({'name':name,'passed':sp.expand(expr)==0,'residual':str(sp.expand(expr))})

RG=DG-nu*QG-r*ft
RGref=(-DG)-nu*(-QG)-r*(-ft)
check('circulation residual is odd',RGref+RG)
Rh=Dh-nu*Mh+v2/y*h-ft/r
Rhref=(-Dh)-nu*(-Mh)+v2/y*(-h)-(-ft)/r
check('swirl-rate residual is odd',Rhref+Rh)
Rxi=Dxi-nu*Mxi-sp.diff(hfun**2,z)-fmer
hneg=-hfun
Rxi_ref=Dxi-nu*Mxi-sp.diff(hneg**2,z)-fmer
check('meridional-vorticity residual is even under swirl reversal',Rxi_ref-Rxi)

check('Q(2 y h)=2 y M h',Qop(2*y*hfun)-2*y*Mop(hfun))
grad2_actual=sp.diff(hfun,z)**2+2*y*sp.diff(hfun,y)**2
check('M(h^2)=2 h M h+2|grad h|_Q^2',Mop(hfun**2)-2*hfun*Mop(hfun)-2*grad2_actual)

assert all(c['passed'] for c in checks)
here=Path(__file__).resolve().parent
receipt={'schema':'signed-ns-operator-replay-v1','all_passed':True,
         'checks':checks,'check_count':len(checks),
         'scope':'Signed involution and product identities only; no source theorem or blowup endpoint is re-proved.',
         'source_pdf_sha256':'8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81',
         'bridge_tex_sha256':hashlib.sha256((here/'axisymmetric_operator_bridge.tex').read_bytes()).hexdigest()}
(here/'signed_operator_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps({'all_passed':True,'check_count':len(checks),'receipt':'signed_operator_receipt.json'}))
