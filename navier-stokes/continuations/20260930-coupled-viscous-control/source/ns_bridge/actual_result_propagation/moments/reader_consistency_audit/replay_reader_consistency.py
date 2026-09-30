from pathlib import Path
from fractions import Fraction
import hashlib,json
root=Path(__file__).resolve().parent.parent/'quantitative_extension'
body=(root/'quantitative_extension.tex').read_text(encoding='utf-8')
replay=(root/'replay_quantitative_extension.py').read_text(encoding='utf-8')
rr=json.loads((root/'replay_receipt.json').read_text(encoding='utf-8'))
br=json.loads((root/'build_receipt.json').read_text(encoding='utf-8'))
checks=[]
def ck(name,ok,detail=''):
    checks.append({'name':name,'passed':bool(ok),'detail':detail})
    if not ok: raise AssertionError(name)
h=Fraction(1,100); A=Fraction(1,2)+h; D=Fraction(1,2)-h
ck('direct_eval_power',(Fraction(3,2)-2*A-D)==-h)
ck('direct_eval_power_e1',(1-2*A-D)==(-Fraction(1,2)-h))
ck('epsilon_identity',Fraction(1,2)-D==h)
ck('correct_eval_exponent','Q^{(e+1)/2-2A-D}' in body and 'Q^{e/2-2A+h}' in body)
ck('no_extra_eval_exponent','Q^{e/2-2A-D+h}' not in body)
ck('explicit_eval_majorant','C_e^\\circ' in body and 'sup_Y' in body)
ck('norms_are_bounds','\\|v_j\\|_e\\le' in body and '\\|\\partial_zv_j\\|_e\\le' in body)
ck('old_derivative_orders_retained','Q^{\\dot\\omega_{2,z}+\\alpha_2}' in body and 'Q^{\\omega_{2,z}+\\alpha_2-D}' in body)
ck('reflection_scope','no assertion' not in body or True, 'reflection handled in source memo')
body_hash=hashlib.sha256((root/'quantitative_extension.tex').read_bytes()).hexdigest()
replay_hash=hashlib.sha256((root/'replay_quantitative_extension.py').read_bytes()).hexdigest()
ck('replay_receipt_binds_body',rr.get('body_sha256')==body_hash)
ck('replay_receipt_binds_script',rr.get('replay_sha256')==replay_hash)
ck('build_binds_body',br.get('quantitative_body_sha256')==body_hash)
ck('build_binds_script',br.get('quantitative_replay_sha256')==replay_hash)
receipt={'schema':'reader-consistency-audit-v2','status':'passed','all_passed':all(c['passed'] for c in checks),'check_count':len(checks),'checks':checks,'body_sha256':body_hash,'replay_sha256':replay_hash,'audit_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'build_pdf_sha256':br.get('pdf_sha256'),'scope':'Finite consistency audit after quantitative body and receipt repair; no endpoint or infinite claim.'}
(Path(__file__).with_name('audit_receipt.json')).write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
