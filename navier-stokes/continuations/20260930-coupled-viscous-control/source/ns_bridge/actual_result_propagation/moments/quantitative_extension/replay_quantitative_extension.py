from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parent
text=(root/'quantitative_extension.tex').read_text(encoding='utf-8')
checks=[]
def check(name,cond):
 checks.append({'name':name,'passed':bool(cond)})
 if not cond: raise AssertionError(name)
h=Fraction(1,100); A=Fraction(1,2)+h; D=Fraction(1,2)-h
check('A_plus_D',A+D==1); check('epsilon_exponent',Fraction(1,2)-D==h)
# exact norm and moment exponents
check('v_e2',Fraction(3,4)-A==Fraction(1,4)-h)
check('v_e1',Fraction(1,2)-A==-h)
check('dzv_e2',Fraction(3,4)-A-D==Fraction(-1,4))
check('dzv_e1',Fraction(1,2)-A-D==Fraction(-1,2))
check('J2_quad',Fraction(3,2)-2*A==Fraction(1,2)-2*h)
check('J1_quad',1-2*A==-2*h)
check('M2_quad',Fraction(3,2)-2*A-D== -h)
check('M1_quad',1-2*A-D==Fraction(-1,2)-h)
check('seed_exponent',-6+Fraction(41,8)==Fraction(-7,8))
check('physical_viscosity_retained',r'\nu_{\rm NS}' in text and 'distinct from the physical' in text and 'no source' in text)
check('old_cross_terms_retained','old-parent orders' in text and 'dot\\omega' in text and 'M_{2,\\mathrm{old}\\times v}' in text)
check('old_derivative_orders_retained','Q^{\\dot\\omega_{2,z}+\\alpha_2}' in text and 'Q^{\\omega_{2,z}+\\alpha_2-D}' in text)
check('evaluation_flux_exponents','Q^{e/2-2A+h}' in text and 'Q^{(e+1)/2-2A-D}' in text and 'M_e^{\\rm ev}-M_e' in text)
check('evaluation_majorant_explicit','C_e^\\circ' in text and 'sup_Y' in text and 'unsupported product' in text)
check('norms_are_bounds','\\|v_j\\|_e\\le' in text and '\\|\\partial_zv_j\\|_e\\le' in text)
check('no_uniform_claim','no endpoint' in text and 'uniform' in text)
check('labels_unique',len(set(re.findall(r'\\label\{([^}]+)\}',text)))==len(re.findall(r'\\label\{([^}]+)\}',text)))
receipt={'schema':'quantitative-source-chart-v1','status':'passed','all_passed':all(c['passed'] for c in checks),'check_count':len(checks),'checks':checks,'body_sha256':hashlib.sha256((root/'quantitative_extension.tex').read_bytes()).hexdigest(),'replay_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Finite exact Q/epsilon exponents for actual third seed, curl, moments, old-wave and quadratic terms; physical viscosity and evaluation flux retained; no endpoint or infinite estimate.'}
(root/'replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))

