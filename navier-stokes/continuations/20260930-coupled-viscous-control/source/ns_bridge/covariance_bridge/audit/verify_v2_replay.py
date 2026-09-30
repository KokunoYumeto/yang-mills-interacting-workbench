"""Run main v2 checks without writing its main-directory receipt."""
from pathlib import Path
import hashlib
import json

audit = Path(__file__).resolve().parent
main = audit.parent
script = main / "replay_covariance.py"
source = script.read_text(encoding="utf-8")
prefix, marker, suffix = source.partition("\nreceipt=dict(")
assert marker, "Receipt boundary missing: inspect changed replay before running it."
namespace = {"__file__": str(script), "__name__": "audit_replay"}
exec(compile(prefix, str(script), "exec"), namespace)
checks = namespace["checks"]
receipt = {
    "all_passed": all(c["passed"] for c in checks),
    "check_count": len(checks),
    "checks": checks,
    "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
    "tex_sha256": hashlib.sha256((main / "covariance_bridge.tex").read_bytes()).hexdigest(),
    "scope": "Independently reran all v2 assertions; their mathematical coverage is assessed separately in REWRITE_AUDIT.md.",
}
(audit / "v2_replay_audit_receipt.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps({k: receipt[k] for k in ("all_passed", "check_count", "script_sha256", "tex_sha256")}, indent=2))
