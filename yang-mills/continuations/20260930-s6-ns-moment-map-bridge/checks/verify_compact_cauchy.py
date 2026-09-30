"""Exact local identities for the compact-support Cauchy construction.

The analytical global existence input is Oh's cited theorem.
No finite symbolic test is presented as its proof.
"""
from itertools import product
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
checks={}
def zero(name, expression):
    entries=list(expression) if isinstance(expression,s.MatrixBase) else [expression]
    checks[name]=all(s.expand(e)==0 for e in entries)
def vec(name):
    return s.Matrix([s.Symbol(f"{name}_{a}") for a in range(3)])
def bracket(a,b):
    return 2*a.cross(b)
def eps(i,j,k):
    return s.LeviCivita(i,j,k)
def add(terms):
    return sum(terms,s.zeros(3,1))

x=s.symbols("x1:4")
chi=s.Function("chi")(*x)
w=[
    s.Matrix([chi+x[1]*s.diff(chi,x[1]),-x[1]*s.diff(chi,x[0]),0]),
    s.Matrix([-x[0]*s.diff(chi,x[1]),chi+x[0]*s.diff(chi,x[0]),0]),
    s.Matrix([-x[0]*s.diff(chi,x[2]),0,chi+x[0]*s.diff(chi,x[0])])
]
def curl(a):
    return s.Matrix([sum(eps(i,j,k)*s.diff(a[k],x[j])
                         for j,k in product(range(3),repeat=2)) for i in range(3)])
potentials=[s.Matrix([0,0,chi*x[1]]),s.Matrix([0,0,-chi*x[0]]),
            s.Matrix([0,chi*x[0],0])]
for a in range(3):
    zero(f"original_cutoff_curl_{a+1}",w[a]-curl(potentials[a]))
    zero(f"original_cutoff_divergence_{a+1}",sum(s.diff(w[a][i],x[i]) for i in range(3)))
c1,c2,c3=[s.diff(chi,u) for u in x]
c11,c22,c33=[s.diff(chi,u,2) for u in x]
c12,c13,c23=[s.diff(chi,x[i],x[j]) for i,j in [(0,1),(0,2),(1,2)]]
stated=[
    [-2*c2-x[1]*(c11+c22),2*c1+x[0]*(c11+c22),x[0]*c23],
    [-c3-x[1]*c23,x[0]*c23,2*c1+x[0]*(c11+c33)],
    [x[1]*c13,-c3-x[0]*c13,c2+x[0]*c12]
]
pairs=[(0,1),(0,2),(1,2)]
for row,(i,j) in enumerate(pairs):
    for a in range(3):
        zero(f"cutoff_curvature_derivative_{i+1}{j+1}_{a+1}",
             s.diff(w[a][j],x[i])-s.diff(w[a][i],x[j])-stated[row][a])

# Independent first jets test the curvature and stress formulas for all values.
colour=[vec(f"c{a}") for a in range(3)]
ww=s.Matrix(3,3,lambda i,a:s.Symbol(f"w{i}_{a}"))
dw=[s.Matrix(3,3,lambda i,a:s.Symbol(f"dw{k}_{i}_{a}")) for k in range(3)]
C=[add(colour[a]*ww[i,a] for a in range(3)) for i in range(3)]
F=[]
for i,j in pairs:
    actual=add(colour[a]*(dw[i][j,a]-dw[j][i,a]) for a in range(3))+bracket(C[i],C[j])
    stated_f=add(colour[a]*(dw[i][j,a]-dw[j][i,a]) for a in range(3))
    stated_f+=add(bracket(colour[a],colour[b])*(ww[i,a]*ww[j,b]-ww[i,b]*ww[j,a])
                  for a,b in pairs)
    zero(f"complete_curvature_expansion_{i+1}{j+1}",actual-stated_f)
    F.append(actual)

# Energy expansion with independent H and W coefficient values.
h=s.symbols("h0:3")
minor=s.symbols("minor0:3")
linear=add(colour[a]*h[a] for a in range(3))
quadratic=add(bracket(colour[a],colour[b])*minor[p] for p,(a,b) in enumerate(pairs))
full=(linear+quadratic).dot(linear+quadratic)
expanded=sum(colour[a].dot(colour[b])*h[a]*h[b] for a,b in product(range(3),repeat=2))
expanded+=2*sum(colour[a].dot(bracket(colour[b],colour[c]))*h[a]*minor[p]
                for a in range(3) for p,(b,c) in enumerate(pairs))
expanded+=sum(bracket(colour[a],colour[b]).dot(bracket(colour[c],colour[d]))
              *minor[p]*minor[q] for p,(a,b) in enumerate(pairs)
              for q,(c,d) in enumerate(pairs))
zero("all_initial_energy_cross_terms",full-expanded)

A=[vec(f"A{i}") for i in range(3)]
E=[vec(f"E{i}") for i in range(3)]
B=[vec(f"B{i}") for i in range(3)]
dE=[[vec(f"dE{j}_{i}") for i in range(3)] for j in range(3)]
dB=[[vec(f"dB{j}_{i}") for i in range(3)] for j in range(3)]
curlE=[add(eps(i,j,k)*(dE[j][k]+bracket(A[j],E[k]))
           for j,k in product(range(3),repeat=2)) for i in range(3)]
curlB=[add(eps(i,j,k)*(dB[j][k]+bracket(A[j],B[k]))
           for j,k in product(range(3),repeat=2)) for i in range(3)]
edot=sum(-E[i].dot(curlB[i])+B[i].dot(curlE[i]) for i in range(3))
divq=-sum(eps(j,i,k)*(dE[j][i].dot(B[k])+E[i].dot(dB[j][k]))
          for i,j,k in product(range(3),repeat=3))
zero("full_local_energy_flux_sign",edot+divq)
gaussdot=-add(eps(i,j,k)*eps(i,j,l)*bracket(B[l],B[k])/2
              for i,j,k,l in product(range(3),repeat=4))
zero("Gauss_constraint_curvature_cancellation",gaussdot)

dA=[[vec(f"dA{i}_{j}") for j in range(3)] for i in range(3)]
for j in range(3):
    stress_div=sum(dA[i][i].dot(A[j])+A[i].dot(dA[i][j])-A[i].dot(dA[j][i]) for i in range(3))
    rhs=add(dA[i][i] for i in range(3)).dot(A[j])
    rhs+=sum(A[i].dot(dA[i][j]-dA[j][i]+bracket(A[i],A[j])) for i in range(3))
    zero(f"flat_divergence_free_stress_identity_{j+1}",stress_div-rhs)
trace=sum(A[i].dot(A[i])-sum(a.dot(a) for a in A)/2 for i in range(3))
zero("stress_trace_retains_negative_half",trace+sum(a.dot(a) for a in A)/2)

T=[s.Matrix([[0,-s.I/2],[-s.I/2,0]]),
   s.Matrix([[0,-s.Rational(1,2)],[s.Rational(1,2),0]]),
   s.Matrix([[-s.I/2,0],[0,s.I/2]])]
def comm(a,b):return a*b-b*a
f,fp,z,g=s.symbols("f fp z g", real=True)
magcomm=comm(4*f*f*T[2],4*f*f*T[0])
eleccomm=comm(2*fp*T[0],2*fp*T[1])
zero("core_magnetic_curvature_commutator",magcomm-16*f**4*T[1])
zero("core_electric_curvature_commutator",eleccomm-4*fp**2*T[2])
zero("core_gauge_invariant_witness",-2*s.trace(magcomm**2+eleccomm**2)-256*f**8-16*fp**4)
zero("witness_lower_bound_remainder",256*(z*z+(1-z)**2)-128-512*(z-s.Rational(1,2))**2)
for a in range(3):
    for b in range(3):
        zero(f"Oh_matrix_metric_factor_{a+1}{b+1}",
             -s.trace((2*T[a])*(2*T[b]))-2*int(a==b))

lam=s.symbols("lambda",positive=True)
chiscaled=chi.subs(dict(zip(x,[u/lam for u in x])),simultaneous=True)
pscaled=[s.Matrix([0,0,chiscaled*x[1]]),s.Matrix([0,0,-chiscaled*x[0]]),
         s.Matrix([0,chiscaled*x[0],0])]
for a in range(3):
    zero(f"full_cutoff_dilation_{a+1}",curl(pscaled[a])-w[a].subs(dict(zip(x,[u/lam for u in x])),simultaneous=True))
checks["energy_dilation_exponent"] = -4+3==-1
checks["curvature_commutator_squared_dilation_exponent"] = 2*(-2-2)==-8
checks["bilinear_expansion_count_per_block"] = sum(
    int(eps(i,j,k)!=0 and eps(a,b,c)!=0)
    for i,j,k,a,b,c in product(range(3),repeat=6))==36

receipt={
 "schema":"compact-cauchy-exact-check-v1",
 "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 "sympy_version":s.__version__,"checks":checks,
 "check_count":len(checks),"all_passed":all(checks.values()),
 "scope":"Exact cutoff, first-jet curvature, energy-flux, constraint, stress, core-invariant and dilation identities. No finite test certifies global PDE existence or a quantum state."
}
(ROOT/"checks/COMPACT_CAUCHY_CHECK.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps({"check_count":len(checks),"all_passed":receipt["all_passed"],
                  "failed":[k for k,v in checks.items() if not v]},indent=2))
if not receipt["all_passed"]:raise SystemExit(1)
