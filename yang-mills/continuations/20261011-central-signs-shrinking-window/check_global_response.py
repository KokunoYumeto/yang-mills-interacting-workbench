import sympy as s, json, pathlib, hashlib, datetime
root=pathlib.Path(__file__).parent
I=s.I
sigma=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.Matrix([[1,0],[0,-1]])]
T=[-I*z/2 for z in sigma]
q=s.symbols('q0:4',real=True)
U=q[0]*s.eye(2)+I*sum((q[k+1]*sigma[k] for k in range(3)),s.zeros(2))
D=s.Matrix(3,3,lambda a,b:s.expand(s.trace(T[a]*T[b]*U)))
frob=s.expand(sum(v*v for v in D))
assert s.expand(frob-(3*q[0]**2+2*sum(z*z for z in q[1:]))/4)==0
assert s.expand(16**2*frob-64*(3*q[0]**2+2*sum(z*z for z in q[1:])))==0
G=s.Matrix([[2,0,s.Rational(2,3)],[0,s.Rational(2,3),0],[s.Rational(2,3),0,s.Rational(2,5)]])
G0=G-s.eye(3)/8
minors=[s.factor(G0[:k,:k].det()) for k in range(1,4)]
assert all(v>0 for v in minors)
constant=s.Rational(2)/s.Integer(8)**6/s.Integer(4)**10
assert constant==s.Rational(1,2**37)
averaged_prefactor=s.cancel(128*(4/s.pi**2)**2/s.Integer(8)**6/((4/s.pi**2)*8)**2)
assert averaged_prefactor==s.Rational(2,8**6)
j,k=s.symbols('j k',positive=True)
M=3*(2*j**4)**2*(2*j**4+1)
xi=10000*j**2/k**2
poly=s.expand(M**2*(1+128*s.sqrt(3)*xi)**8)
assert s.Poly(poly,j).degree()==40
note=(root/'GLOBAL_PHYSICAL_RESPONSE.md').read_text(encoding='utf-8')
assert note.count(r'\(')==note.count(r'\)')==338
assert note.count(r'\[')==note.count(r'\]')
assert r'\tag{GPR40a}' in note and r'\tag{GPR40b}' in note
assert 'O(j^{40})' in note
out={'observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mixed_T_matrix':str(D),'mixed_T_frobenius_squared':str(frob),'stereographic_mixed_sum_on_unit_quaternions':'128 + 16 (w_p^0)^2, with w_p^0 = W_p(U_e^0,U_f^0,y)','gram_shift_principal_minors':[str(v) for v in minors],'averaged_prefactor':str(averaged_prefactor),'constant_without_e':str(constant),'path_response_inverse_polynomial_degree':40,'inline_math_pairs':338,'display_math_pairs':note.count(r'\['),'scope':'Exact symbolic checks of the general proof constants and restored math delimiters; no vacuum sampling or numerical gap claim.'}
(root/'GLOBAL_RESPONSE_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8',newline='\n')
print(json.dumps(out,indent=2))
