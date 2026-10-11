"""Reproducible checks of PVC formulas. Finite matrices are identity checks only."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import hashlib
import json
import re
import numpy as np
import scipy.linalg as la
import scipy.integrate as integrate
import sympy as s

root = Path(__file__).resolve().parent
checks = []

def exact(name, expression):
    residual = s.simplify(expression)
    passed = residual == 0
    checks.append({"name": name, "kind": "exact", "passed": bool(passed),
                   "residual": str(residual)})
    if not passed:
        raise AssertionError((name, residual))

def close(name, actual, expected, tol=1e-7):
    residual = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    scale = max(1.0, float(np.max(np.abs(np.asarray(expected)))))
    passed = residual <= tol * scale
    checks.append({"name": name, "kind": "numerical", "passed": passed,
                   "absolute_residual": residual, "tolerance_times_scale": tol * scale})
    if not passed:
        raise AssertionError((name, residual, tol * scale))

def truth(name, passed, detail=""):
    checks.append({"name": name, "kind": "structural", "passed": bool(passed),
                   "detail": detail})
    if not passed:
        raise AssertionError((name, detail))

# Exact retained coefficients and the source-average integration weights.
d, M, L, xi, a, kap, R = s.symbols("d M L xi a kap R", positive=True)
exact("PVC28 quadratic coefficients",
      (6*M-3*d)**2 - 64*xi*d*(L-d)
      - ((9+64*xi)*d**2-(36*M+64*xi*L)*d+36*M**2))
u, rho = s.symbols("u rho")
U = [s.Integer(1), u]
for k in range(1, 4):
    U.append(s.expand(u*U[-1] + rho**2*k**2*U[-2]))
exact("PVC27 U2", U[2]-(u**2+rho**2))
exact("PVC27 U3", U[3]-(u**3+5*u*rho**2))
exact("PVC27 U4", U[4]-(u**4+14*u**2*rho**2+9*rho**4))
v, eps, h, t = s.symbols("v eps h t", positive=True)
exact("PVC18 pulse covariance factor",
      2/eps**2*s.integrate((eps-t)*t, (t, 0, eps))-eps/3)
exact("PVC19 pulse energy weight",
      6*s.integrate(v*(1-v), (v, 0, 1))-1)
exact("PVC20 pulse energy error",
      12/eps*s.integrate((1-v)*s.integrate(t, (t, eps*v/2, eps*v)),
                         (v, 0, 1))-3*eps/8)
exact("PVC48 two signed defect weights",
      2/h**2*s.integrate((h-t)**2, (t, 0, h))-2*h/3)
q = R/a
Nq = 3*q*(q+1)**2
Mq = 3*q**2*(q+1)
Lq = 3*kap*a*s.sqrt(Nq*Mq)+24*q*(q+1)
Lstar = 6*s.sqrt(s.Rational(3,2))*kap*a*s.sqrt(Nq*Mq)+48*q*(q+1)
exact("PVC31 a squared local budget limit",
      s.limit(a**2*Lq, a, 0, dir="+")-(9*kap*R**3+24*R**2))
exact("PVC44 a squared source budget limit",
      s.limit(a**2*Lstar, a, 0, dir="+")-
      (18*s.sqrt(s.Rational(3,2))*kap*R**3+48*R**2))
x = s.symbols("x")
exact("PVC32 lower-mean limit coefficient",
      s.limit(a**6*((6*Mq-3*x/a**2)**2-
                    64/(kap**2*a**2)*(x/a**2)*(Lq-x/a**2)), a, 0, dir="+")
      -(324*R**6-64*x*(9*kap*R**3+24*R**2-x)/kap**2))
I, l, dl, mfscaled = s.symbols("I l dl mfscaled")
exact("PVC35 energy lower constant",
      s.limit(kap**2*(3*mfscaled/a-18*I/a**2)**2/
              (4/(kap*a**2)*(l-dl)/a**2), a, 0, dir="+")
      -81*kap**3*I**2/(l-dl))
F = s.symbols("F", positive=True)
b = 1/(kap*a**2)
source_h = b/(2*a*F)
exact("PVC46 signed-test average constant squared",
      (16*kap*a**2*F**2*L/2)*(2*a*F*L/source_h)
      -(4*s.sqrt(2)*kap*a**3*F**2*L)**2)
exact("PVC46 nonnegative-test average constant squared",
      (16*kap*a**2*F**2*L/2)*(a*F*L/source_h)
      -(4*kap*a**3*F**2*L)**2)
c = s.symbols("c", positive=True)
phi = (2*s.pi/c+4)/(1-c/2)**2
exact("PVC37 inherited optimizer derivative",
      s.diff(phi, c)-(4*c**2+3*s.pi*c-2*s.pi)/(c**2*(1-c/2)**3))

# Exact rational unit quaternions check all four insertion orientations.
pauli = [s.Matrix([[0,1],[1,0]]), s.Matrix([[0,-s.I],[s.I,0]]),
         s.Matrix([[1,0],[0,-1]])]
generators = [-s.I*p/2 for p in pauli]
exact("PVC23 fundamental Casimir",
      sum((-T*T for T in generators), s.zeros(2))[0,0]-s.Rational(3,4))

def su2(n):
    z = [s.Rational((n+1)%5-2, 3), s.Rational((2*n+3)%7-3, 4),
         s.Rational((3*n+1)%9-4, 5)]
    norm = sum(v*v for v in z)
    cc = (1-norm)/(1+norm)
    vv = [2*v/(1+norm) for v in z]
    return cc*s.eye(2) + sum((2*generators[k]*vv[k] for k in range(3)), s.zeros(2))

for n in range(1, 9):
    A, U, B, C, D = [su2(n+k*9) for k in range(5)]
    for sig in (-1, 1):
        for tau in (-1, 1):
            Up = U if sig == 1 else U.inv()
            Uq = U if tau == 1 else U.inv()
            Lp = U*B*A if sig == 1 else B*A*U.inv()
            Lr = U*D*C if tau == 1 else D*C*U.inv()
            dp = []
            dq = []
            for T in generators:
                derivative_p = T*U if sig == 1 else -U.inv()*T
                derivative_q = T*U if tau == 1 else -U.inv()*T
                dp.append(-s.trace(A*derivative_p*B))
                dq.append(-s.trace(C*derivative_q*D))
            claimed = s.Rational(sig*tau,4)*(s.trace(Lp*Lr.inv())-s.trace(Lp*Lr))
            exact(f"PVC22 shared edge sample {n} signs {sig},{tau}",
                  sum(dp[k]*dq[k] for k in range(3))-claimed)
            defect = 2-s.trace(A*Up*B)
            exact(f"PVC22 self derivative sample {n} signs {sig},{tau}",
                  sum(z*z for z in dp)-(defect-defect**2/4))

# Full reduced projections and derivatives in a finite irreducible real matrix.
# This checks spectral identities; it does not approximate a Yang--Mills vacuum.
n = 7
H = np.diag(np.linspace(.3, 2.1, n))
for i in range(n-1):
    H[i, i] += 1
    H[i+1, i+1] += 1
    H[i,i+1] = H[i+1,i] = -1
Cf = np.diag([1.1, 2.4, -.8, .3, 1.7, -.2, .6])
Cg = np.diag([-.2, .8, 1.3, -1.7, .4, 1.6, -.5])

def ground(tt=0, ss=0):
    HH = H+tt*Cf+ss*Cg
    ev, vec = la.eigh(HH)
    psi = vec[:,0]
    if np.sum(psi)<0:
        psi = -psi
    P = np.outer(psi,psi)
    inv = (vec[:,1:]/(ev[1:]-ev[0])) @ vec[:,1:].T
    return ev[0], psi, P, inv, HH-ev[0]*np.eye(n)

E, psi, P, inv, A = ground()
Q = np.eye(n)-P
mf = psi @ Cf @ psi
mg = psi @ Cg @ psi
Xf = Cf-mf*np.eye(n)
Xg = Cg-mg*np.eye(n)
uf = Xf@psi
ug = Xg@psi
step = 2e-4
Ef, pf, Pf, Rf, _ = ground(step)
Eb, pb, Pb, Rb, _ = ground(-step)
close("PVC9 E first derivative", (Ef-Eb)/(2*step), mf)
close("PVC9 vacuum first derivative", (pf-pb)/(2*step), -inv@uf)
close("PVC9 P derivative", (Pf-Pb)/(2*step),
      -np.outer(inv@uf,psi)-np.outer(psi,inv@uf))
close("PVC9 reduced inverse derivative", (Rf-Rb)/(2*step),
      -inv@Xf@inv+inv@inv@Cf@P+P@Cf@inv@inv, tol=3e-7)
mixed = [ground(step,step),ground(step,-step),
         ground(-step,step),ground(-step,-step)]
close("PVC9 energy mixed derivative",
      (mixed[0][0]-mixed[1][0]-mixed[2][0]+mixed[3][0])/(4*step**2),
      -2*uf@inv@ug, tol=2e-6)
close("PVC9 vacuum mixed derivative",
      (mixed[0][1]-mixed[1][1]-mixed[2][1]+mixed[3][1])/(4*step**2),
      inv@(Xf@inv@ug+Xg@inv@uf)-(inv@uf)@(inv@ug)*psi, tol=3e-6)
close("PVC6 full reduced projection", A@inv, Q, tol=1e-11)
close("PVC6 reduced vacuum annihilation", inv@psi, np.zeros(n), tol=1e-11)

def source_values(tt):
    et, pt, Pt, Rt, At = ground(tt)
    mt = pt@Cf@pt
    Xt = Cf-mt*np.eye(n)
    ut = Xt@pt
    Gt = ut@ut
    Tt = ((np.eye(n)-Pt)@Xt@Xt@pt) @ Rt @ ut
    return Gt, Tt

G, T = source_values(0)
close("PVC47 centered variance derivative",
      (source_values(step)[0]-source_values(-step)[0])/(2*step),
      -2*T, tol=2e-7)
hh=.6
avg = integrate.quad(lambda tt:(hh-abs(tt))/hh**2*source_values(tt)[0],
                     -hh,hh,points=[0],epsabs=1e-11)[0]
defect = (integrate.quad(lambda tt:(hh-tt)**2*source_values(tt)[1],0,hh,
                        epsabs=1e-11)[0]
          -integrate.quad(lambda tt:(hh+tt)**2*source_values(tt)[1],-hh,0,
                         epsabs=1e-11)[0])/hh**2
close("PVC48 exact signed original-source defect", avg+defect, G, tol=1e-10)
truth("PVC48 finite check defect is nonzero", abs(defect)>1e-5,
      "The check forbids accidentally replacing the signed defect by zero.")

energy = uf@A@uf
close("PVC12 susceptibility integral",
      2*integrate.quad(lambda tt:uf@la.expm(-tt*A)@uf,0,100,epsabs=1e-11)[0],
      2*uf@inv@uf, tol=1e-10)
truth("PVC13 spectral Cauchy direction", G*G<=energy*(uf@inv@uf)+1e-12)

def pulse(epsilon, u=uf, v=ug):
    return integrate.quad(lambda tt:2*(1-tt)*(u@la.expm(-epsilon*tt*A)@v),
                          0,1,epsabs=1e-12)[0]

for epsilon in [.04, .13, .4, 1.2]:
    hessian_step=.001
    def logZ(tt,ss):
        z = np.exp(epsilon*E)*(psi@la.expm(-epsilon*(H+tt*Cf+ss*Cg))@psi)
        return np.log(z)
    e=hessian_step
    numerical_hessian=(logZ(e,e)-logZ(e,-e)-logZ(-e,e)+logZ(-e,-e))/(4*e*e)
    close(f"PVC17 mixed log pulse Hessian epsilon {epsilon}",
          numerical_hessian/epsilon**2,pulse(epsilon),tol=2e-6)
    bound=epsilon/3*np.sqrt((uf@A@uf)*(ug@A@ug))
    truth(f"PVC18 covariance pulse bound epsilon {epsilon}",
          abs(uf@ug-pulse(epsilon))<=bound+1e-12)
    er=6/epsilon*(pulse(epsilon/2)-pulse(epsilon))
    bound=3*epsilon/8*la.norm(A@uf)*la.norm(A@ug)
    truth(f"PVC20 energy pulse bound epsilon {epsilon}",
          abs(uf@A@ug-er)<=bound+1e-12)
    erdiag=6/epsilon*(pulse(epsilon/2,uf,uf)-pulse(epsilon,uf,uf))
    truth(f"PVC20 diagonal positivity epsilon {epsilon}",
          -1e-12<=erdiag<=uf@A@uf+1e-12)

# Actual original j path: check ceilings, branch, root rationalization,
# positive denominator and limit constants for representative exact parameters.
for kk in [.2, 1., 3.]:
    RR=.4
    Llimit=9*kk*RR**3+24*RR**2
    dlimit=(Llimit-np.sqrt(Llimit**2-81*kk**2*RR**6/4))/2
    for jj in [2, 8, 40, 200]:
        aa=1/(100*jj); g2=kk/(200*jj); bb=10000*jj*jj/kk
        qq=int(np.ceil(RR/aa))+3
        NN=3*qq*(qq+1)**2; MM=3*qq*qq*(qq+1); CC=12*qq*(qq+1)
        LL=min(2*MM,6*g2*np.sqrt(float(NN*MM)))+2*CC
        r=bb/kk
        ac=9+64*r; bc=36*MM+64*r*LL
        dc=bc*bc-144*ac*MM*MM
        dm=72*MM*MM/(bc+np.sqrt(dc))
        truth(f"PVC29 finite discriminant k={kk} j={jj}", dc>=0)
        truth(f"PVC34 finite denominator k={kk} j={jj}", 0<dm<LL)
        close(f"PVC29 lower root polynomial k={kk} j={jj}",
              (ac*dm*dm-bc*dm+36*MM*MM)/(36*MM*MM),0.,tol=2e-12)
    close(f"PVC32 lower root limit k={kk}", aa*aa*dm,dlimit,tol=2e-3)

proof = (root/"PHYSICAL_LOCAL_COVARIANCE.md").read_text(encoding="utf-8")
tags = re.findall(r"\\tag\{PVC(\d+)\}",proof)
counts = Counter(map(int,tags))
truth("All PVC1–PVC50 tags exactly once", counts==Counter(range(1,51)),
      str(dict(counts)))
truth("No old PC locators in proof", re.search(r"\bPC\d+",proof) is None)
truth("Inline TeX delimiters balanced", proof.count(r"\(")==proof.count(r"\)"))
truth("Display TeX delimiters balanced", proof.count(r"\[")==proof.count(r"\]"))
truth("No ASCII control-byte TeX damage",
      not any(ord(c)<32 and c not in "\n\r\t" for c in proof))
truth("No forbidden prose token", re.search(r"\bpl"+"ain"+r"\b",proof,re.I) is None)
at = root/"ANISOTROPIC_TEMPORAL_BRIDGE.md"
truth("Completed AT source preserved",
      hashlib.sha256(at.read_bytes()).hexdigest()==
      "820592c648301fecfe1f569c987e080e08de6496e783fa406e1f01085e91c0df")
result = {"timestamp":datetime.now(timezone.utc).isoformat(),
          "scope":"Algebra/orientations/limits, full-projection finite-matrix identity checks, source/pulse signs, and raw source structure. No matrix model replaces the actual original vacuum.",
          "proof_sha256_raw_bytes":hashlib.sha256(
              (root/"PHYSICAL_LOCAL_COVARIANCE.md").read_bytes()).hexdigest(),
          "total":len(checks), "by_kind":dict(Counter(c["kind"] for c in checks)),
          "all_passed":all(c["passed"] for c in checks), "checks":checks}
(root/"PHYSICAL_COVARIANCE_CHECKS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in result.items() if k!="checks"},indent=2))
