#!/usr/bin/env python3
"""Rebuild original quartic certificates as canonical UTF-8/LF bytes.

Place beside the unchanged verify.py, or specify --source-dir. Output must be a
new directory. The original verifier's computation, tests, and hashes are used
unchanged; this wrapper only controls the serialization boundary.
"""
from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    source = args.source_dir.resolve()
    output = args.output_dir.resolve()
    if output.exists():
        parser.error("output directory must not already exist")
    if not (source / "verify.py").is_file():
        parser.error("source directory must contain the original verify.py")
    # Reserve the destination before expensive computation, without overwriting
    # any existing file or directory. A failed run leaves its evidence in place.
    output.mkdir(parents=True, exist_ok=False)
    sys.path.insert(0, str(source))
    spec = importlib.util.spec_from_file_location("_quartic_original_verify", source / "verify.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load the original verifier")
    verify = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(verify)
    result, files = verify.run()
    for name, text in files.items():
        (output / name).write_bytes(text.encode("utf-8"))
    (output / "verification.json").write_bytes(verify.dump(result).encode("utf-8"))
    print(verify.dump({
        "passed": True,
        "counts": result["counts"],
        "receipt_sha256": verify.digest(verify.dump(result).encode("utf-8")),
        "tables_sha256": result["generated_sha256"],
    }), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
