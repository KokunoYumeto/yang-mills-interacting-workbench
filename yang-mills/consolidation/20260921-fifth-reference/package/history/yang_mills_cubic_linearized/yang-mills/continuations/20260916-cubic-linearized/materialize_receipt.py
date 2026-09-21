#!/usr/bin/env python3
"""Recreate the complete observed receipt and require its exact original hash."""
from pathlib import Path
import hashlib, json, subprocess, sys, tempfile
ROOT = Path(__file__).resolve().parent
EXPECTED = "2e6a1433b9df7bb3f1ee584b7896e6ae9dae9f5a7836a5030af7a993711190c6"
SOURCES = {'CUBIC_SOURCE.md': 'd1e8fa24ce573ad1adfdaeecbb2ee6bfa1631717f9ce22b0f66d838981d5f240', 'LINEARIZED_RETURN.md': '931d8d2824062c6435dfe324cb9145bc6d8e7a450d37aa5f86a94f1190190453', 'README.md': '2fbb9f300d29ad35efd1ea3b2c9d07b29185308f3aeaefbfaf2738d180597a18', 'SOURCE_INTAKE.json': '23849c8a138107a287fd2b28f0e16d43056f80333ef1eb605df786c988c15eb9', 'coordinate_audit.py': 'de1d9841ebd4655194801cc053bc1f71393433e8c241d0d88cdae65fc82f7c9f', 'geometry.py': 'bd878efd339f05f320d051bee760bff0934ccfca10e9a2c1e6f26941a128cc1e', 'state.json': '310162656f69b84b8059d6e201a867c0ef632492058cc43838191526419c5a1d', 'verify.py': '45bd9ff364efc4d41b205702472ba0557d9248335bf4f6b879f55f1d2bec0502'}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def main():
    for name, wanted in SOURCES.items():
        if digest((ROOT / name).read_bytes()) != wanted:
            raise RuntimeError("source-identity-mismatch:" + name)
    target = ROOT / "verification.json"
    if target.exists() and digest(target.read_bytes()) != EXPECTED:
        raise RuntimeError("existing-receipt-mismatch")
    with tempfile.TemporaryDirectory(prefix="ym-cubic-receipt-") as td:
        out = Path(td) / "verification.json"
        command = [sys.executable, *(["-O"] if not __debug__ else []),
                   "-B", str(ROOT / "verify.py"), "--output", str(out)]
        result = subprocess.run(command, capture_output=True, timeout=180)
        if result.returncode or result.stdout or result.stderr:
            raise RuntimeError("producer-failed:" + result.stderr.decode())
        data = out.read_bytes()
        if digest(data) != EXPECTED:
            raise RuntimeError("regenerated-receipt-mismatch")
        target.write_bytes(data)
    print("PASS: complete 180403-byte receipt reproduced " + EXPECTED)

if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, subprocess.TimeoutExpired) as exc:
        sys.stderr.write("FAIL: " + str(exc) + "\n")
        raise SystemExit(1)
