"""Build deterministic validation and SHA-256 records for this continuation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
VALIDATION = ROOT / "PUBLIC_VALIDATION.json"
MANIFEST = ROOT / "PUBLIC_MANIFEST.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def boolean_count(value: object) -> int:
    if isinstance(value, bool):
        return 1
    if isinstance(value, dict):
        return sum(boolean_count(child) for child in value.values())
    if isinstance(value, list):
        return sum(boolean_count(child) for child in value)
    return 0


def main() -> None:
    receipt_records = []
    for relative in [
        "checks/SP1_BUNDLE_BRIDGE_CHECK.json",
        "checks/SP1_MOMENT_MAP_BRIDGE_CHECK.json",
        "checks/THREE_COLOUR_CURVATURE_CHECK.json",
        "checks/HIGHER_CARRIER_EVOLUTION_CHECK.json",
        "checks/COMPACT_CAUCHY_CHECK.json",
        "checks/PERIOD_PHYSICAL_KERNEL_CHECK.json",
        "checks/COMPLEMENTARY_SECOND_MOMENT_CHECK.json",
        "checks/FULL_PACKET_RESOLVENT_CHECK.json",
        "checks/PACKET_MOMENTS_ESCAPE_CHECK.json",
        "checks/ODD_VACUUM_OBSERVABLE_CHECK.json",
        "checks/JOINT_PATH_GLOBAL_OBSERVABLE_CHECK.json",
    ]:
        path = ROOT / relative
        data = json.loads(path.read_text(encoding="utf-8"))
        receipt_records.append(
            {
                "path": relative,
                "sha256": sha256(path),
                "all_passed": data.get("all_passed") is True,
                "recorded_boolean_checks": boolean_count(data.get("checks", {})),
            }
        )

    source = ROOT / "sources" / "higher_rung" / "s6_higher_rung_24d_preprint.tex"
    png = ROOT / "figures" / "S6_NS_MOMENT_MAP_BRIDGE.png"
    svg = ROOT / "figures" / "S6_NS_MOMENT_MAP_BRIDGE.svg"
    source_files = sorted(
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "sources").rglob("*")
        if path.is_file()
    )
    validation = {
        "schema": "s6-ns-moment-map-public-validation-v1",
        "date": "2026-10-09",
        "result_scope": (
            "Corrected global classical bundle morphism, its fibrewise rank data, "
            "the interacting core, its exact nonzero static source, the higher-carrier "
            "pullback, full parameter connection, Gauss-preserving correction, and "
            "global source-free homogeneous core evolution; exact application of Oh’s "
            "global theorem to the original compact-support data; complete proofs of "
            "propagation, energy-zero set, parameter dependence, bundle descent, dilation "
            "and link holonomies; full cusp coupling, physical finite-lattice "
            "vectors, exact Gram and Hamiltonian kernels, corrected same-coupling "
            "path, first electric layer, complete interacting return, exact second "
            "complementary moment, cube contributions, nonzero next map, stronger resolvent bound, "
            "full-packet returns, complete electric cutoff, vacuum interval, spectral-transform error, "
            "complete packet moments, fixed-heat spectral escape, interacting evolution, "
            "actual fixed-box odd support, full raw limiting spectral measure, higher-carrier receiving map, "
            "proved original-path cutoff mass collapse and global group-coordinate observable with complete actual moments."
        ),
        "claim_boundary": (
            "Finite physical quantum vectors are constructed. No continuum "
            "reconstruction, gapless spectrum, or mass-gap contradiction is established."
        ),
        "analytical_input": {
            "author": "Sung-Jin Oh",
            "global_source": "https://arxiv.org/abs/1210.1557v2",
            "local_source": "https://arxiv.org/abs/1210.1558v2",
            "use": "Exact Main Theorem application; source conventions and hypotheses proved in CE1–CE7",
            "whole_source_proof_independently_recertified": False,
        },
        "receipts": receipt_records,
        "all_symbolic_receipts_passed": all(
            record["all_passed"] for record in receipt_records
        ),
        "retained_source": {
            "path": "sources/higher_rung/s6_higher_rung_24d_preprint.tex",
            "bytes": source.stat().st_size,
            "sha256": sha256(source),
            "expected_sha256": "8c526746de9b56a4fcd0a274df0c470092cc82a16e49857df539a1c9d033956f",
            "identity_passed": sha256(source)
            == "8c526746de9b56a4fcd0a274df0c470092cc82a16e49857df539a1c9d033956f",
        },
        "source_closure_file_count": len(source_files),
        "source_closure_files": source_files,
        "principal_figure": {
            "png_path": "figures/S6_NS_MOMENT_MAP_BRIDGE.png",
            "png_bytes": png.stat().st_size,
            "png_sha256": sha256(png),
            "png_signature_passed": png.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"),
            "svg_path": "figures/S6_NS_MOMENT_MAP_BRIDGE.svg",
            "svg_bytes": svg.stat().st_size,
            "svg_sha256": sha256(svg),
            "svg_signature_passed": "<svg" in svg.read_text(encoding="utf-8")[:1000],
            "visual_inspection": "completed before publication",
        },
    }
    validation["all_passed"] = (
        validation["all_symbolic_receipts_passed"]
        and validation["retained_source"]["identity_passed"]
        and validation["principal_figure"]["png_signature_passed"]
        and validation["principal_figure"]["svg_signature_passed"]
    )
    VALIDATION.write_text(
        json.dumps(validation, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    files = []
    for path in sorted(
        (candidate for candidate in ROOT.rglob("*") if candidate.is_file()),
        key=lambda candidate: candidate.relative_to(ROOT).as_posix(),
    ):
        if path == MANIFEST:
            continue
        files.append(
            {
                "path": path.relative_to(ROOT).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    manifest = {
        "schema": "s6-ns-moment-map-public-manifest-v1",
        "date": "2026-10-09",
        "root": "yang-mills/continuations/20260930-s6-ns-moment-map-bridge",
        "manifest_excludes_itself": True,
        "file_count": len(files),
        "files": files,
    }
    MANIFEST.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"validation_passed": validation["all_passed"], "files": len(files)}))


if __name__ == "__main__":
    main()
