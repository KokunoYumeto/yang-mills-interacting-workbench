from fractions import Fraction as F
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
def inverse(a):
    n=len(a);b=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for i in range(n):
        pivot=b[i][i];assert pivot
        b[i]=[x/pivot for x in b[i]]
        for j in range(n):
            if j!=i:
                scale=b[j][i];b[j]=[x-scale*y for x,y in zip(b[j],b[i])]
    return [row[n:] for row in b]
H0=[[F(3,2*i+2*j+3) for j in range(3)] for i in range(3)]
H1=[[F(3,2*i+2*j+5) for j in range(2)] for i in range(2)]
I0=inverse(H0);I1=inverse(H1)
lambda0=1/sum(I0[i][i] for i in range(3));lambda1=1/sum(I1[i][i] for i in range(2))
c0=F(15,16)*lambda0/F(39,8)
c1=F(15,16)*F(5,8)*lambda1/F(13,24)
c2=F(15,16)*F(15,8)**2*F(3,7)/F(5,8)
assert c0<=c1 and c0<=c2
cap_c=c0*F(47,384)**4
cap_simple=F(1,2**24)
assert cap_c>=cap_simple
for matrix,inv in ((H0,I0),(H1,I1)):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            assert sum(matrix[i][k]*inv[k][j] for k in range(len(matrix)))==F(i==j)
schur1=H1[1][1]-H1[0][1]**2/H1[0][0]
assert schur1==F(4,147)
vector_abs=F(15,16)*F(5,8)*schur1
assert vector_abs==F(25,1568)
special6=2*3*vector_abs*F(47,384)**3
assert special6==F(75,784)*F(47,384)**3
linear2=F(4,3)*F(15,8)*F(15,16)*F(3,5)*F(47,384)
assert linear2==F(705,4096)
assert F(4,9)*linear2==F(235,3072)
# Full polynomial norms and exact sphere moments.
moments={0:F(1),1:F(0),2:F(1,4),3:F(0),4:F(1,8)}
u2=moments[0]-2*moments[1]+moments[2]
u4=moments[0]-4*moments[1]+6*moments[2]-4*moments[3]+moments[4]
assert u2==F(5,4) and u4==F(21,8)
assert 1+u2+u4==F(39,8)
assert (F(3,4)+F(7,8))/3==F(13,24)
assert 4*(moments[2]-moments[4])==F(1,2)
# Boundary row and path factors, before any floating-point evaluation.
row_sum_prefactor=F(64)*F(3,8)
assert row_sum_prefactor/8==3
assert row_sum_prefactor/4==6
assert row_sum_prefactor/6==4
assert F(3,2)/2**4==F(3,32)
assert F(3)/2**4==F(3,16)
assert F(2)/2**4==F(1,8)
assert F(5000)*F(3,32)==F(1875,4)
assert F(5000,12)==F(1250,3)
out={'status':'all_exact_assertions_passed','H0':[[str(x) for x in row] for row in H0],'H0_inverse':[[str(x) for x in row] for row in I0],'H1':[[str(x) for x in row] for row in H1],'H1_inverse':[[str(x) for x in row] for row in I1],'lambda0_lower':str(lambda0),'lambda1_lower':str(lambda1),'scalar_delta4':str(c0),'vector_delta3':str(c1),'tensor_delta2':str(c2),'cap_radius8':str(cap_c),'cap_radius8_decimal':float(cap_c),'weaker_radius8_constant':str(cap_simple),'vector_schur_complement':str(schur1),'vector_fixed_cross_delta3':str(vector_abs),'special_vector_radius6':str(special6),'special_vector_radius6_decimal':float(special6),'pure_linear_radius2':str(linear2),'pure_linear_uniform_rational':str(F(4,9)*linear2),'row_sum_factors':[3,6,4],'path_B6_leading_factor':'3/32','path_energy_leading_rational':'1875/4','scope':'Exact rational certificates support PS7–PS12, PS17–PS26, PS58 and PS70–PS74; the mathematical proof is in the accompanying note.'}
(ROOT/'CAP_CONSTANT_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
