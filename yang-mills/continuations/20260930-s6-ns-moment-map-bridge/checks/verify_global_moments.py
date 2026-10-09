"""Exact original chord sums, coincident Haar contractions and actual bound constants."""
from pathlib import Path
import itertools,json,hashlib
import sympy as s
import numpy as np
HERE=Path(__file__).resolve().parent;checks={}
def eq(name,a,b=0):
    assert s.simplify(s.expand(a-b))==0,name
    checks[name]=True
for m in [2,4]:
    n=m+1;h=s.pi/(2*n);c=s.cos(h);C=s.cot(h)
    v0=s.sqrt(s.Rational(1,n))
    v=[s.simplify(s.sqrt(s.Rational(2,n))*s.cos(s.pi*(2*l+1)/(2*n))) for l in range(n)]
    w=[s.simplify(-s.sqrt(s.Rational(2,n))*s.sin(s.pi*(l+1)/n)) for l in range(m)]
    rows=[[],[],[]]
    for i in range(1,n):
        for k in range(m):
            for l in range(n):
                vals=[-v[i]*w[k]*v0/s.sqrt(2),0,v0*w[k]*v[l]/s.sqrt(2)]
                for a in range(3):rows[a].append(s.simplify(vals[a]))
    for i in range(n):
        for k in range(n):
            if (i,k)==(0,0):continue
            for l in range(m):
                vals=[0,-v[i]*v0*w[l]/s.sqrt(2),-v0*v[k]*w[l]/s.sqrt(2)]
                for a in range(3):rows[a].append(s.simplify(vals[a]))
    eq(f"complete chord count m={m}",len(rows[0]),2*m**3+3*m*m)
    R=s.Matrix([[s.Rational(1,2)-c*c/n,0,0],[0,s.Rational(1,2)-c*c/n**2,-c*c/n**2],[0,-c*c/n**2,1-s.Rational(1,2*n)-c*c/n**2]])
    for a in range(3):
        for b in range(a,3):
            eq(f"exact full chord Gram m={m} {a},{b}",sum(x*y for x,y in zip(rows[a],rows[b])),R[a,b])
    D=sum(x*x*y*y for x,y in zip(rows[0],rows[2]))
    eq(f"coincident fourth contraction m={m}",D,s.Rational(3,8*n**3)*(1-2*c*c/n))
    targets=[s.sqrt(s.Rational(2,n))*C*(C-c),s.sqrt(s.Rational(2,n))*C*(C-c/n),s.sqrt(s.Rational(2,n))*((2-s.Rational(1,n))*C*C-c*C/n)]
    for a in range(3):
        eq(f"full absolute chord sum m={m} row={a}",sum(s.Abs(x) for x in rows[a]),targets[a])
    eq(f"complete edge fourth sum m={m}",sum(x**4 for x in w),s.Rational(3,2*n))

# Larger original boxes are numerical checks of the independently proved
# trigonometric sums, not exact-algebra or asymptotic proofs.
samples=[]
for m in [6,8,10,14]:
    n=m+1;h=np.pi/(2*n);c=np.cos(h);C=1/np.tan(h)
    v0=1/np.sqrt(n);v=np.sqrt(2/n)*np.cos(np.pi*(np.arange(n)+.5)/n);w=-np.sqrt(2/n)*np.sin(np.pi*(np.arange(m)+1)/n)
    rows=[]
    for i,k,l in itertools.product(range(n),range(n),range(n)):
        if i>0 and k<m:rows.append([-v[i]*w[k]*v0/np.sqrt(2),0,v0*w[k]*v[l]/np.sqrt(2)])
        if (i,k)!=(0,0) and l<m:rows.append([0,-v[i]*v0*w[l]/np.sqrt(2),-v0*v[k]*w[l]/np.sqrt(2)])
    matrix=np.asarray(rows);expected=np.array([[.5-c*c/n,0,0],[0,.5-c*c/n**2,-c*c/n**2],[0,-c*c/n**2,1-1/(2*n)-c*c/n**2]])
    err=float(np.max(np.abs(matrix.T@matrix-expected)));assert err<1e-12
    samples.append({"m":m,"chords":len(rows),"maximum_absolute_gram_error":err})

A4,B4=s.symbols("A4 B4")
solution=s.solve([A4-3*B4,4*A4+12*B4-1],[A4,B4])
eq("sphere full fourth diagonal",solution[A4],s.Rational(1,8))
eq("sphere full mixed fourth",solution[B4],s.Rational(1,24))
eq("global q fourth diagonal",16*solution[A4],2)
eq("global q fourth tensor",16*solution[B4],s.Rational(2,3))
aa=s.symbols("a0:3",real=True);bb=s.symbols("b0:3",real=True)
moment=0
for c,d,e,f in itertools.product(range(3),repeat=4):
    colour_sum=0
    for alpha,beta in itertools.product(range(3),repeat=2):
        factors={}
        for chord,col in [(c,alpha),(d,alpha),(e,beta),(f,beta)]:factors.setdefault(chord,[]).append(col)
        value=s.Integer(1)
        for cols in factors.values():
            if len(cols)%2:value=0;break
            if len(cols)==2:value*=int(cols[0]==cols[1])
            elif len(cols)==4:
                p,q,r,t=cols
                value*=s.Rational(2,3)*(int(p==q)*int(r==t)+int(p==r)*int(q==t)+int(p==t)*int(q==r))
        colour_sum+=value
    moment+=aa[c]*bb[d]*aa[e]*bb[f]*colour_sum
expected=3*sum(a*a for a in aa)*sum(b*b for b in bb)+12*sum(a*b for a,b in zip(aa,bb))**2-5*sum(a*a*b*b for a,b in zip(aa,bb))
eq("all ordered Haar fourth contractions including coincidences",moment,expected)
n=s.symbols("n",positive=True)
c=s.cos(s.pi/(2*n))
H=3*(s.Rational(1,2)-c*c/n)*(1-1/(2*n)-c*c/n**2)-s.Rational(15,8)/n**3*(1-2*c*c/n)
eq("full Haar fourth limiting value",s.limit(H,n,s.oo),s.Rational(3,2))
j,kappa,g,a,sigma,A=s.symbols("j kappa g a sigma A",positive=True)
delta=2*sigma/a
eq("full phase receiving dictionary",(A*delta/(2*kappa)).subs(kappa,2*g*g/a),A*sigma/(2*g*g))
sigj=s.sqrt(8)*s.sin(s.pi/(4*j**4+2))
betaj=(sigma/(2*g*g)).subs({sigma:sigj,g:s.sqrt(kappa/(200*j))})
eq("full phase on original path",betaj,200*s.sqrt(2)*j/kappa*s.sin(s.pi/(4*j**4+2)))
eq("original phase limit",s.limit(j**3*betaj,j,s.oo),50*s.sqrt(2)*s.pi/kappa)
eq("Haar mass upper coefficient",s.limit(j**6*betaj**2*H.subs(n,2*j**4+1),j,s.oo),7500*s.pi**2/kappa**2)
eq("actual fourth-moment receiving scale",s.limit(1/(j**6*betaj**2),j,s.oo),kappa**2/(5000*s.pi**2))
S1,S3,N,M,xi=s.symbols("S1 S3 N M xi",positive=True)
eq("full first derivative coarse constant",2*S3*2*S1+2*S1*2*S3,8*S1*S3)
eq("full second derivative coarse constant",2*S3*2*S1+2*2*S1*2*S3+2*S1*2*S3,16*S1*S3)
eq("all colours in first-moment bound",3*N*(8*S1*S3)**2,192*N*S1*S1*S3*S3)
eq("all curvature score and boundary-face contributions",3*N*16*S1*S3+4*s.sqrt(3)*xi*(4*M)*8*S1*S3,S1*S3*(48*N+128*s.sqrt(3)*xi*M))
tc,td,te,tf,Tcd,Tef=s.symbols("tc td te tf Tcd Tef")
eq("all four physical word contributions",(2*Tcd-tc*td)*(2*Tef-te*tf),4*Tcd*Tef-2*Tcd*te*tf-2*tc*td*Tef+tc*td*te*tf)
proof=HERE.parent/("PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md" if HERE.name=="checks" else "GLOBAL_OBSERVABLE_FOUR_POINT_ESTIMATES_20261009.md")
out={"all_passed":True,"checks":checks,"check_count":len(checks),"proof_sha256":hashlib.sha256(proof.read_bytes()).hexdigest(),
    "larger_box_numerical_samples":samples,"numerical_samples_are_proofs":False,
    "scope":"Exact chord sums and Haar contractions supplement complete written proofs; actual-vacuum inequalities retain their distinct measures and full original path.","independent_review":False}
(HERE/"GLOBAL_FOUR_POINT_CHECK.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps({"all_passed":True,"exact_checks":len(checks),"supplementary_numerical_boxes":len(samples)}))
