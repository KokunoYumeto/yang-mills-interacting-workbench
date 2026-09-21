#!/usr/bin/env python3
"""Exact return of the elementary nonzero-reference certificate."""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parent

def main():
 p=argparse.ArgumentParser();p.add_argument('--verify-existing',action='store_true');a=p.parse_args()
 R=F(3,256);c=F(2,3);checks=[]
 for n in range(2,52):
  q=F(1,n);xi=R*(1-q*q);rr=F(3,4)*(1-q);delta=(1-2*c*rr)**2/(4*c*32)
  if not (1-2*c*rr==q and delta==R*q*q and xi+delta==R):raise ArithmeticError('source-restart:'+str(n))
  checks.append({'q':str(q),'xi':str(xi),'radius':str(delta),'endpoint':str(xi+delta)})
 if R-F(1,1024)!=F(11,1024) or 1-F(256,3)*F(1,1024)!=F(11,12):raise ArithmeticError('actual-reference-square')
 out={'schema':'ym-reference-restart-v1','identity_proved_in':'ROUTE_ASSESSMENT.md:R1','finite_exact_checks':checks,'actual_reference':'1/1024','remaining_certificate_radius':'11/1024','old_and_new_right_endpoint':'3/256','no_actual_singularity_asserted':True,'source_sha256':{n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in ('ROUTE_ASSESSMENT.md','route_check.py')}}
 s=json.dumps(out,sort_keys=True,indent=2)+'\n';file=ROOT/'generated/route_verification.json'
 if a.verify_existing:
  if file.read_text()!=s:raise ArithmeticError('route-receipt-mismatch')
 else:file.write_text(s)
 print('COMPLETE',len(checks)+2,hashlib.sha256(s.encode()).hexdigest())
if __name__=='__main__':
 try:main()
 except (OSError,ValueError,ArithmeticError) as e:raise SystemExit('FAIL: '+str(e))
