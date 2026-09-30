"""Exact independent replay for the finite local spatial constants."""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone
import sympy as sp

HERE = Path(__file__).resolve().parent
LANE = HERE.parent.parent
Q = sp.Rational
checks = []

def zero(name, expr):
    value = sp.factor(expr)
    assert value == 0, (name, value)
    checks.append({"name": name, "passed": True, "exact_value": str(value)})

def positive(name, expr):
    value = sp.factor(expr)
    assert value.is_positive is True, (name, value)
    checks.append({"name": name, "passed": True, "exact_margin": str(value)})

a0 = Q(1, 512)
L0 = sp.Integer(16384)
positive("D_lower_from_cube", Q(63,64)**2-Q(15,16))
positive("D_upper_from_cube", 17-(16+a0*a0))
positive("R_lower_from_cube", Q(11,16)**2/17-Q(1,64))
positive("R_upper_from_cube", 39-(36+16*a0*a0)/Q(15,16))
positive("sqrt_R_below_7_squared", 49-39)
positive("matrix3_frobenius_margin_squared", 32**2-56*11)
positive("matrix2_difference_lower", 2-1)
positive("collar_first_exit_margin", Q(1,128)-Q(3,512))
positive("collar_time_below_1", 1-Q(3,16384))
zero("collar_displacement_exact", 32*Q(3,16384)-Q(3,512))
positive("source_p_above_1", Q(47*202,16)-3-1)
positive("source_r_above_2", Q(31*202+1,16)-2)
positive("source_second_slack_squared", 9-Q(68,11))
positive("older_support_u_positive", Q(47,16))
positive("older_support_v_positive", Q(31,16))
positive("numerator_bracket_below_25", 25-7*(Q(13,4)+a0/32))
positive("numerator_old_part_below_1", 1-25*Q(16,15)*a0/L0**2)
positive("rb_upper_squared", 16-10)
zero("newest_K_upper_product", 17*64-1088)
positive("S_coefficient_K_margin", 1089-1088)
positive("S_coefficient_B_margin", 1089-Q(9,8))
zero("collar_exponent_exact", 1089*Q(3,16384)-Q(3267,16384))
positive("collar_exponent_below_quarter", Q(1,4)-Q(3267,16384))
positive("rational_exp_upper_below_four_thirds", Q(4,3)-1/(1-Q(3267,16384)))
positive("amplitude_final_margin", 6-Q(16,3))

h, a, g, b = sp.symbols("h a g b", positive=True)
D = h*h+a*a
x = (h*g-a*b)/D
y = (a*g+h*b)/D
R = (g*g+b*b)/D
zero("coordinate_phase_length_identity", x*x+y*y-R)
zero("coordinate_adjacent_determinant", h*y-a*x-b)
zero("coordinate_adjacent_dot_product", h*x+a*y-g)
aa, ab, ba, bb = sp.symbols("aa ab ba bb", real=True)
M = sp.Matrix([[aa,ab],[ba,bb]])
zero("adjugate_frobenius_identity", sum(z*z for z in M.adjugate())-sum(z*z for z in M))

sig1,sig2,s,LL,K3,Pstar,N3,Z,dd,Gam = sp.symbols(
    "sig1 sig2 s LL K3 Pstar N3 Z dd Gam", positive=True)
E,F,cbar,Cbar = sp.symbols("E F cbar Cbar", positive=True)
zero("source_numerator_rescaling", (
    (sig1**2*E+sig1**2*cbar)*y+sig1**2*Cbar*x+b*sig2**2*F
    )/sig2**2-((sig1/sig2)**2*((E+cbar)*y+Cbar*x)+b*F))
X,W = sp.symbols("X W", positive=True)
Theta = -Pstar*X
Omega = -K3*Pstar*W/sig2
Theta_dot = N3/(K3*R)*Omega-dd*K3**2*R*Theta
Omega_dot = K3*Z*Theta-dd*K3**2*R*Omega
zero("physical_to_normalized_temperature", -Theta_dot/(Pstar*sig2*sp.sin(s))
    -(N3/(sig2**2*sp.sin(s)*R)*W-dd*K3**2/(sig2*sp.sin(s))*R*X))
zero("physical_to_normalized_vorticity", -sig2*Omega_dot/(K3*Pstar*sig2*sp.sin(s))
    -(Z/sp.sin(s)*X-dd*K3**2/(sig2*sp.sin(s))*R*W))
qq=sp.symbols("q",positive=True)
zero("exact_scale_ratio", (s/LL)**2/sp.sin(s)-s*s/(LL*LL*sp.sin(s)))
Q2=sp.symbols("Q2",positive=True)
zero("first_support_source_exponent", (Q2-1)/16+Q(1,16)-3*Q2+3+(47*Q2/16-3))
zero("second_support_source_exponent", (Q2-1)/16-2*Q2+(31*Q2+1)/16)

sources = [
    "third_return/third_return_body.tex",
    "third_return/local_spatial_body.tex",
    "third_transition/third_transition_body.tex",
    "third_transition_spatial/third_transition_spatial_body.tex",
    "finite_stage/third_growth_entry.tex",
    "finite_stage/actual_viscous_entry.tex",
    "second_return/second_return_body.tex",
    "third_return/local_spatial/constant_audit.md",
    "third_return/local_spatial/final_body_audit.md",
    "third_return/local_spatial/replay_constant_audit.py",
]
hashes = {p: hashlib.sha256((LANE/p).read_bytes()).hexdigest() for p in sources}
receipt = {
    "created_utc": datetime.now(timezone.utc).isoformat(),
    "scope": "Exact local cube, explicit 3/2 collar, matrices, unchanged source margins, newest amplitude rescaling and rational bounds only; no full steering or third return claim.",
    "all_passed": all(c["passed"] for c in checks),
    "check_count": len(checks),
    "checks": checks,
    "source_sha256": hashes,
}
out = HERE / "constant_audit_receipt.json"
out.write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"all_passed": receipt["all_passed"], "check_count": len(checks), "receipt": str(out)}, indent=2))
