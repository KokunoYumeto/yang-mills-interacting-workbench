"""Independent audit replay for the released pulse frame identities.
Uses an exact unit-circle parametrization so the constraints
kt^2+kz^2=1 and kt*ktp+kz*kzp=0 are enforced structurally.
"""
from pathlib import Path
import hashlib, json
import sympy as S

s, sp, rho, rhop = S.symbols("s sp rho rhop", nonzero=True)
omega, a = S.symbols("omega a", real=True)
kt, kz, ktp, kzp = S.symbols("kt kz ktp kzp", real=True)
F, gt, gz = S.symbols("F gt gz", real=True)
fr, ft, fz, x, y = S.symbols("fr ft fz x y")
sub = {kt:S.cos(a), kz:S.sin(a), ktp:-omega*S.sin(a), kzp:omega*S.cos(a)}
def red(q):
    return S.factor(S.trigsimp(S.expand(q).subs(sub), method="fu"))

e = S.Matrix([1,-s*kt,-s*kz])
U = S.Matrix.hstack(e, S.Matrix([0,kz,-kt]))
Up = S.Matrix.hstack(S.Matrix([0,-sp*kt-s*ktp,-sp*kz-s*kzp]), S.Matrix([0,kzp,-ktp]))
Ul = S.diag(1/(1+s**2), 1) * U.T
n = rho*S.Matrix([s,kt,kz])
np = rhop*S.Matrix([s,kt,kz]) + rho*S.Matrix([sp,ktp,kzp])
K = S.Matrix([[0,-2*F,0],[2*F+gt,0,0],[gz,0,0]])
f = S.Matrix([fr,ft,fz])
t = U*S.Matrix([x,y])
checks = []
def check(name, expr):
    residue = red(expr)
    checks.append({"name":name, "passed": residue == 0, "residual": str(residue)})

I2 = S.eye(2)
for i in range(2):
    for j in range(2): check(f"left inverse entry {i},{j}", (Ul*U-I2)[i,j])
for i in range(2): check(f"frame is transverse entry {i}", (Ul*n)[i])
# A_phi is projected when acting on tangent amplitudes.
Aphi = -K + n*(n.T*K - np.T)/((n.T*n)[0])
zp = S.Matrix(S.symbols("xp yp"))
tprime = Up*S.Matrix([x,y]) + U*zp
check("projected tangent derivative", (n.T*(tprime-Aphi*t))[0])
# Correct coordinate matrix: the determinant term belongs over (1+s^2).
C = Ul*(-K*U-Up)
C_expected = S.Matrix([
    [s*(kt*gt+kz*gz-sp)/(1+s**2),
     (2*F*kz+s*(kt*kzp-kz*ktp))/(1+s**2)],
    [-(2*F*kz+gt*kz-gz*kt)+s*(kz*ktp-kt*kzp), 0],
])
for i in range(2):
    for j in range(2): check(f"moving-frame matrix entry {i},{j}", C[i,j]-C_expected[i,j])
f_expected = S.Matrix([(fr-s*(kt*ft+kz*fz))/(1+s**2), kz*ft-kt*fz])
for i in range(2): check(f"projected force entry {i}", (Ul*f-f_expected)[i])
# Correct pressure bracket: -n'·(y N) contributes +det(kt,kz;kt',kz').
pressure = S.expand(n.dot(K*t)-np.dot(t)+n.dot(f))
det = kt*kzp-kz*ktp
pressure_expected = rho*(
    x*(2*F*(1+s**2)*kt+kt*gt+kz*gz-sp)
    + y*(-2*F*s*kz+det)
    + s*fr+kt*ft+kz*fz
)
check("pressure numerator", pressure-pressure_expected)
gK, gN = gt*kt+gz*kz, gt*kz-gz*kt
check("shear energy transfer", t.dot(K*t)-(-s*gK*x**2+gN*x*y))
assert all(c["passed"] for c in checks), checks
root = Path(__file__).resolve().parents[1]
receipt = {
    "schema":"pulse-frame-audit-v2",
    "all_passed":True,
    "check_count":len(checks),
    "checks":checks,
    "source_pulse_tex":"../pulse_comparison.tex",
    "source_pdf_sha256":"8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81",
    "scope":"Independent replay of the frame, transversality, projected operator, force, pressure and shear identities. It does not reprove source estimates or covariance construction.",
    "findings":[
      "The existing audit replay's reducer does not enforce the unit-frame constraints after expansion; its first assertion fails even though the frame identity is true.",
      "The existing audit replay's C_expected (0,1) entry omits the denominator (1+s^2) on the rotating-frame determinant term.",
      "The existing audit replay's pressure_expected has the wrong sign on the determinant term in the y coefficient; the exact term is + (k_theta*k_z_p-k_z*k_theta_p).",
      "The pulse note's residual-map theorem requires n^T B=0 (columns spanning n^perp), not merely full rank plus transversality of one selected B L y.",
      "The note's diffusion discrepancy is signed m^2 d_N-q_v lambda_c^bullet (plus frame H terms), not m^2 d_N+lambda_c^bullet unless explicitly taking an absolute-cost convention."
    ],
    "replay_script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
(root/"pulse_frame_audit_receipt.json").write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"all_passed":True,"check_count":len(checks),"receipt":str(root/"pulse_frame_audit_receipt.json")}))
