"""Run selected public-edition checks serially, with bounded subprocesses.

Standard-library Python only. Outputs are written to a new directory. Existing
proofs, programs and receipts are read but never rewritten. On Windows each
worker has a 2 GiB process-and-job limit; on POSIX it has a 2 GiB address-space
limit. Both use one available CPU and a 600-second wall timeout per check.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
from time import perf_counter

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FIRST = ROOT / "continuations/20260917-quartic-cube"
SECOND = ROOT / "continuations/20260917-quartic-independent"
LIMIT = 2 * 1024**3


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inputs():
    paths = []
    for folder in (FIRST, SECOND, FIRST.parent / "20260916-cubic-linearized"):
        paths.extend(p for p in folder.rglob("*") if p.is_file() and "__pycache__" not in p.parts)
    paths.extend(HERE.glob("*.py"))
    return {p.relative_to(ROOT).as_posix(): digest(p) for p in sorted(set(paths))}


def posix_limits():
    import resource
    resource.setrlimit(resource.RLIMIT_AS, (LIMIT, LIMIT))
    if not hasattr(os, "sched_getaffinity"):
        raise RuntimeError("A one-CPU hard limit is unavailable on this platform")
    available = os.sched_getaffinity(0)
    os.sched_setaffinity(0, {min(available)})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--checks", nargs="+", choices=("trace", "trace-optimized", "quaternion", "tangent", "bridge", "singleface", "gap-scalars"),
                        default=["trace", "trace-optimized", "quaternion", "tangent", "bridge", "singleface", "gap-scalars"])
    args = parser.parse_args()
    target = args.output_dir.resolve()
    if target.exists():
        parser.error("output directory already exists; choose a new directory")
    target.mkdir(parents=True, exist_ok=False)
    jobs = {
        "trace": (FIRST / "verify.py", ["--verify-receipt", "generated/verification.json"], False),
        "trace-optimized": (FIRST / "verify.py", ["--verify-receipt", "generated/verification.json"], True),
        "quaternion": (SECOND / "verify_public_catalogue.py", ["--package-root", "."], False),
        "tangent": (SECOND / "verify_portable_tangent.py", ["--package-root", "."], False),
        "bridge": (HERE / "compare_catalogues.py", [], False),
        "singleface": (HERE / "independent_singleface.py", [], False),
        "gap-scalars": (HERE / "check_gap_scalars.py", [], False),
    }
    record = {"schema": "ym-public-edition-execution-v1", "python": platform.python_version(),
              "platform": platform.system(), "started_at": datetime.now(timezone.utc).isoformat(),
              "inputs_before": inputs(), "checks": [], "passed": False,
              "interpretation": "Execution receipts for finite checks; not machine formalization of the analytic proofs."}
    environment = os.environ.copy()
    for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
        environment[key] = "1"
    try:
        for name in args.checks:
            script, options, optimized = jobs[name]
            folder = target / name
            folder.mkdir()
            command = [sys.executable, "-B"] + (["-O"] if optimized else [])
            if os.name == "nt":
                command += [str(HERE / "bounded_worker.py"), str(folder / "limits.json"), str(script)]
                extra = {}
                cap = "Windows Job Object: 2 GiB process and aggregate commit, one process, one CPU"
            elif os.name == "posix":
                command += [str(script)]
                extra = {"preexec_fn": posix_limits, "start_new_session": True}
                cap = "POSIX RLIMIT_AS: 2 GiB; one CPU by sched_setaffinity"
            else:
                raise RuntimeError("No supported hard resource-cap implementation")
            command += options
            started = perf_counter()
            process = subprocess.Popen(command, cwd=script.parent, env=environment,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, **extra)
            timeout = False
            try:
                stdout, stderr = process.communicate(timeout=600)
            except subprocess.TimeoutExpired:
                timeout = True
                if os.name == "posix":
                    import signal
                    os.killpg(process.pid, signal.SIGKILL)
                else:
                    process.kill()
                stdout, stderr = process.communicate()
            (folder / "stdout.txt").write_bytes(stdout)
            (folder / "stderr.txt").write_bytes(stderr)
            item = {"name": name, "script": script.relative_to(ROOT).as_posix(), "arguments": options,
                    "optimized": optimized, "exit_code": process.returncode, "timeout": timeout,
                    "seconds": perf_counter() - started, "resource_cap": cap, "wall_seconds": 600,
                    "stdout_sha256": digest(folder / "stdout.txt"), "stderr_sha256": digest(folder / "stderr.txt")}
            if (folder / "limits.json").exists():
                item["effective_limits"] = json.loads((folder / "limits.json").read_text())
            record["checks"].append(item)
            print(name + ": " + ("passed" if process.returncode == 0 and not timeout else "failed"), flush=True)
            if process.returncode or timeout:
                raise RuntimeError("Check did not complete successfully: " + name)
        record["passed"] = True
    finally:
        record["inputs_after"] = inputs()
        record["inputs_unchanged"] = record["inputs_before"] == record["inputs_after"]
        if not record["inputs_unchanged"]:
            record["passed"] = False
        (target / "execution.json").write_bytes((json.dumps(record, indent=2, sort_keys=True) + "\n").encode("utf-8"))
    if not record["passed"]:
        raise RuntimeError("Public-edition checks failed or input bytes changed")


if __name__ == "__main__":
    main()
