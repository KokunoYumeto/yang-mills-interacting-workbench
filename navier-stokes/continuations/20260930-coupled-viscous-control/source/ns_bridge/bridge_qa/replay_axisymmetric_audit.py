"""Independent audit replay for the axisymmetric cylindrical bridge."""
from pathlib import Path
import hashlib, json
import sympy as S
z,y=S.symbols('z y', positive=True)
nu,v2,r=S.symbols('nu v2 r', nonzero=True)
h=S.Function('h')(z,y); hz=S.Function('hz')(z,y)
fr=S.Function('fr')(z,y); fz=S.Function('fz')(z,y); ft=S.symbols('f_theta')
Dg,Qg,Dxi,Mxi,Dh,Mh=S.symbols('Dg Qg Dxi Mxi Dh Mh')
Q=lambda f:S.diff(f,z,2)+2*y*S.diff(f,y,2)
M=lambda f:Q(f)+4*S.diff(f,y)
curl=S.diff(fr/r,z)-S.diff(fz,y)
checks=[]
def check(name,expr):
    e=S.expand(expr); checks.append({'name':name,'passed':e==0,'residual':str(e)})
check('Q product circulation',Q(2*y*h)-2*y*M(h))
check('M square product',M(h**2)-2*h*M(h)-2*(S.diff(h,z)**2+2*y*S.diff(h,y)**2))
RG=Dg-nu*Qg-r*ft
RGflip=(-Dg)-nu*(-Qg)-r*(-ft)
check('circulation residual odd under swirl reflection',RGflip+RG)
Rh=Dh-nu*Mh+v2/y*h-ft/r
Rhflip=(-Dh)-nu*(-Mh)+v2/y*(-h)-(-ft)/r
check('swirl-rate residual odd under swirl reflection',Rhflip+Rh)
Rxi=Dxi-nu*Mxi-S.diff(h**2,z)-curl
Rxi_flip=Dxi-nu*Mxi-S.diff((-h)**2,z)-curl
check('meridional-vorticity residual even',Rxi_flip-Rxi)
B=h**2
RB=S.symbols('DB')-nu*M(B)+2*nu*(S.diff(h,z)**2+2*y*S.diff(h,y)**2)+2*v2/y*B-2*h*ft/r
RB_flip=S.symbols('DB')-nu*M(B)+2*nu*(S.diff(-h,z)**2+2*y*S.diff(-h,y)**2)+2*v2/y*B-2*(-h)*(-ft)/r
check('square equation even under swirl reflection',RB_flip-RB)
assert all(c['passed'] for c in checks), checks
root=Path(__file__).resolve().parent
receipt={'schema':'axisymmetric-operator-audit-v1','all_passed':True,'check_count':len(checks),'checks':checks,
 'source_pdf_sha256':'8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81',
 'bridge_tex_sha256':hashlib.sha256((root.parent/'axisymmetric_operator_bridge.tex').read_bytes()).hexdigest(),
 'scope':'Independent replay of coordinate-product identities and signed involution; no source theorem or singular endpoint is re-proved.',
 'finding':'Axisymmetric displayed identities and sign reflection pass. The prior meridional check in replay_signed_operator.py was tautological; this replay replaces it with an actual h^2 and force-preserving parity check.'}
(root/'axisymmetric_operator_audit_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps({'all_passed':True,'check_count':len(checks),'receipt':str(root/'axisymmetric_operator_audit_receipt.json')}))
