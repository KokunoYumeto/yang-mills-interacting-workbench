"""Exact rational arithmetic certificates for tr:local; no ODE simulation.

These checks are counted separately from the 56 symbolic transport identities.
Each check is one explicitly named scalar rational equality or inequality.
Analytic use, parameter monotonicity, branches, and continuation are proved in
LOCAL_ANALYTIC_AUDIT.md, not inferred from a numerical trajectory.
"""
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "third_return_body.tex"
a_max = Q(1,512)
L_min = Q(16384)
radius = Q(1,128)
checks = []


def check(name, left, relation, right):
    left, right = Q(left), Q(right)
    passed = {"<": left < right, ">": left > right, "=": left == right}[relation]
    checks.append({"name":name,"left":str(left),"relation":relation,
                   "right":str(right),"right_minus_left":str(right-left),
                   "passed":passed})
    assert passed, name


check("sin(s)>=s/2 Taylor remainder coefficient", a_max*a_max/6, "<", Q(1,2))
check("h lower bound after cube subtraction (squared comparison)", 1-a_max*a_max, ">", Q(127,128)**2)
check("h cube upper bound", Q(13,4)+radius, "<", 4)
check("g cube lower bound", Q(3,4)-radius, ">", Q(11,16))
check("g cube upper bound", 5+radius, "<", 6)
check("E cube lower endpoint", Q(1,8)-radius, "=", Q(15,128))
check("E cube upper bound", 2+radius, "<", 3)
check("F cube lower endpoint", Q(1,16)-radius, "=", Q(7,128))
check("F cube upper bound", 3+radius, "<", 4)
check("absolute omega cube upper bound", 10+radius, "<", 11)
check("actual transition absolute V bound", 7040*a_max/L_min, "<", Q(1,32))
check("absolute V cube upper bound", Q(1,32)+radius, "<", Q(1,16))
check("D cube lower bound", Q(63,64)**2, ">", Q(15,16))
check("D cube upper bound", 16+a_max*a_max, "<", 17)
check("Z upper bound from actual transition coefficient", Q(9,8)*a_max, "<", Q(1,128))
check("b upper scale", 4*a_max, "=", Q(1,128))
check("R positive lower bound", Q(11,16)**2/17, ">", Q(1,64))
check("Y positive lower bound (squared)", Q(1,64)-Q(1,128)**2, ">", Q(1,81))
check("x numerator lower bound", Q(63,64)*Q(11,16)-4*a_max*a_max, ">", Q(17,32))
check("x lower bound after division by 17", Q(17,32)/17, "=", Q(1,32))
check("g shear coefficient bound in units of a", 2*6/Q(63,64)+4, "<", 17)
check("second numerator bound in units of a", 3+Q(1,4)+Q(4,32), "<", 4)
check("absolute h derivative bound", 22*a_max/L_min, "<", 1)
check("absolute g derivative bound", 374*a_max/L_min+Q(1,4), "<", 1)
check("absolute E derivative bound", 22*a_max/(32*L_min)+Q(3,128), "<", 1)
check("absolute omega derivative bound", 6/L_min+Q(11,128), "<", 1)
check("absolute F derivative bound", 8*a_max*a_max/(15*L_min*L_min)+Q(68,128), "<", 1)
check("absolute V derivative damping term", Q(17,128)*Q(1,16), "=", Q(17,2048))
check("V derivative absorbs damping into one over sin(s)", Q(17,2048), "<", 1)
check("V derivative coefficient below complete vector field coefficient", 21, "<", 32)
check("unit row bound below complete vector field bound for sin(s)<=1", 1, "<", 32)
check("local dimensionless endpoint lies before the pulse", a_max/8192, "<", 1)
check("M times tau0 cancellation", Q(32,8192), "=", Q(1,256))
check("full local displacement is below cube radius", Q(1,256), "<", radius)
check("R finite upper bound for newest linear pair", (36+(4*a_max)**2)/Q(15,16), "<", 39)
check("y finite upper bound coefficient in units of a", (6+16)/Q(15,16), "=", Q(352,15))
check("actual transition newest angular lift upper bound", 640*a_max*a_max/L_min+16*a_max/3, "<", Q(1,64))
check("x finite upper bound", 6/Q(63,64), "<", 7)

receipt = {
    "audit":"Exact scalar rational checks for third steering local existence",
    "created_utc":datetime.now(timezone.utc).isoformat(),
    "count_scheme":"One named scalar rational equality or strict inequality per check; independent of the existing 56 symbolic identity count.",
    "source":str(SOURCE),
    "source_sha256":sha256(SOURCE.read_bytes()).hexdigest(),
    "script_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
    "check_count":len(checks),
    "all_passed":all(item["passed"] for item in checks),
    "checks":checks,
    "scope":"Finite arithmetic audit of the actual local theorem; no simulated solution, full trial, or third shooting root.",
}
(HERE/"local_rational_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({key:receipt[key] for key in ("audit","check_count","all_passed","count_scheme","source_sha256")},indent=2))
