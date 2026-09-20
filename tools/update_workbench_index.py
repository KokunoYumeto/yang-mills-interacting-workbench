#!/usr/bin/env python3
"""Regenerate the experimental static catalogue from the staged Git index.

Stage the intended public payload first, run this script, then stage its two
JSON outputs. Rerun after any payload change. --check compares without writing.
The script never stages files, changes source artifacts, or contacts a network.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "https://github.com/KokunoYumeto/yang-mills-interacting-workbench"
INSPECTED_MATH_SOURCE_COMMIT = "143f6773feb424ad9ed3a8d116653200f20346b7"
HISTORICAL_INDEX_COMMIT = "5835bf92c722cf095bc7ff3b13ad21c093c2d6c5"
OUTPUTS = ("workbench.json", "releases/2026-09-09/GITHUB_TREE_MANIFEST.json")

# These path identities come from PR #1's historical 22-file inventory.
# They persist when a file's bytes change; SHA-256 identifies the exact bytes.
LEGACY_PATHS = (
    "05_current_authored_ym_lanes_2026-09-09.zip",
    "06_CURRENT_YM_LANES_README.md",
    "07_CURRENT_YM_LANE_MANIFEST.json",
    "README.md",
    "check_fixed_coupling_analytic_disk_obstruction.py",
    "navier_stokes_checks.json",
    "navier_stokes_primary_manifest.json",
    "navier_stokes_source_bundle.zip",
    "navier_stokes_workbench.tex",
    "navier_stokes_workbench_208p.pdf",
    "quantum_coarse_graining_75p.pdf",
    "quantum_interacting_tensor_band_71p.pdf",
    "quantum_nonabelian_vertex_63p.pdf",
    "scaled_angle_prescribed_kernel_rates.md",
    "spatial_continuum_121p.pdf",
    "spatial_continuum_127p.md",
    "spatial_continuum_127p.pdf",
    "spatial_continuum_127p.tex",
    "spatial_continuum_129p.md",
    "spatial_continuum_129p.pdf",
    "spatial_continuum_129p.tex",
    "volume_uniform_vacuum_77p.pdf",
)
LEGACY_IDS = {path: f"ART-{number:03d}" for number, path in enumerate(LEGACY_PATHS, 1)}


def git(*arguments: str) -> bytes:
    return subprocess.run(
        ["git", *arguments], cwd=ROOT, check=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout


def staged_payload() -> list[dict]:
    """Read index entries, including already tracked unchanged files."""
    entries = []
    seen = set()
    for record in git("ls-files", "--stage", "-z").split(b"\0"):
        if not record:
            continue
        metadata, path_bytes = record.split(b"\t", 1)
        mode, oid, stage = metadata.decode("ascii").split()
        path = path_bytes.decode("utf-8", errors="strict")
        if stage != "0":
            raise ValueError(f"Resolve the unmerged index entry before generation: {path}")
        parts = PurePosixPath(path).parts
        if (
            not parts or PurePosixPath(path).is_absolute()
            or any(part in (".", "..") or part.casefold() == ".git" for part in parts)
            or "\\" in path or ":" in path
            or any(ord(character) < 32 for character in path)
            or PurePosixPath(path).as_posix() != path
        ):
            raise ValueError("The index contains a non-portable or Git-internal path")
        if path in seen:
            raise ValueError(f"Duplicate index path: {path}")
        seen.add(path)
        if path in OUTPUTS:
            continue
        if mode not in ("100644", "100755", "120000"):
            raise ValueError(f"The catalogue supports file blobs, not Git mode {mode}: {path}")
        entries.append({"path": path, "git_mode": mode, "git_blob_oid": oid})
    return sorted(entries, key=lambda entry: entry["path"])


def fingerprints(entries: list[dict], object_format: str) -> dict[str, tuple[int, str]]:
    """Hash raw staged blob bytes, independently of checkout newline conversion."""
    results = {}
    process = subprocess.Popen(
        ["git", "cat-file", "--batch"], cwd=ROOT,
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    try:
        for entry in entries:
            oid = entry["git_blob_oid"]
            if oid in results:
                continue
            process.stdin.write(oid.encode("ascii") + b"\n")
            process.stdin.flush()
            header = process.stdout.readline().decode("ascii").strip().split()
            if len(header) != 3 or header[0] != oid or header[1] != "blob":
                raise ValueError("Git could not return the requested staged blob")
            size = int(header[2])
            digest = hashlib.sha256()
            git_digest = hashlib.new(object_format)
            git_digest.update(f"blob {size}\0".encode("ascii"))
            remaining = size
            while remaining:
                chunk = process.stdout.read(min(remaining, 1024 * 1024))
                if not chunk:
                    raise ValueError("Unexpected end of staged blob")
                digest.update(chunk)
                git_digest.update(chunk)
                remaining -= len(chunk)
            if process.stdout.read(1) != b"\n" or git_digest.hexdigest() != oid:
                raise ValueError("Staged blob framing or Git object identity failed")
            results[oid] = (size, digest.hexdigest())
        process.stdin.close()
        if process.wait() != 0:
            raise ValueError("Git blob reader failed")
    finally:
        if process.poll() is None:
            process.kill()
            process.wait()
        for stream in (process.stdin, process.stdout, process.stderr):
            stream.close()
    return results


def artifact_id(path: str) -> str:
    if path in LEGACY_IDS:
        return LEGACY_IDS[path]
    return "ART-PATH-" + hashlib.sha256(path.encode("utf-8")).hexdigest()[:16]


def programme_ids(path: str) -> list[str]:
    if path.startswith("navier-stokes/") or path.startswith("navier_stokes_"):
        return ["NS"]
    if path.startswith("s6/"):
        return ["S6"]
    if path.startswith("yang-mills/") or (path in LEGACY_IDS and path != "README.md"):
        return ["YM"]
    return []


def programmes() -> list[dict]:
    return [
        {
            "id": "YM",
            "title": "Yang–Mills research workbench",
            "human_entry": "yang-mills/README.md",
            "human_reader": "yang-mills/consolidation/20260917/reader/yang_mills_quartic_cube_reader.pdf",
            "latest_continuation": "yang-mills/consolidation/20260919/README.md",
            "ai_entry": "yang-mills/AI_READING_INDEX.md",
            "source_directory": "yang-mills/",
            "research_state_document": "yang-mills/consolidation/20260919/README.md",
            "source_manifest": "yang-mills/consolidation/20260919/SOURCE_MANIFEST.json",
            "foundation_edition_doi": "10.5281/zenodo.22678364",
            "foundation_edition_url": "https://doi.org/10.5281/zenodo.22678364",
            "research_state": (
                "The 19 September continuation adds preserved sixth-source, eighth-energy "
                "and finite plaquette-response manuscripts, exact arithmetic checks and "
                "minimum-energy support maps. New spatial coefficient tables and the final "
                "execution package were not supplied; catalogue completeness and their "
                "response implications remain attributed to the source. The 17 September "
                "reader supplies the fourth-vacuum and sixth-energy calculation. "
                "The 14-16 September 2026 continuation consolidates complete available "
                "web-session proofs, gauge-native source dependencies, cubic/linearized "
                "finite-lattice calculations, retained historical mathematical responses, "
                "bounded analytical audits and fresh finite replay records. The source "
                "guide records missing attachments and exact provenance. The finite-lattice "
                "gap domain and earlier fixed-spacing infinite-volume uniqueness domain "
                "remain distinct. The interacting four-dimensional continuum mass-gap "
                "conclusion remains unestablished. The 9 September foundation edition "
                "and all its source bodies remain available."
            ),
            "description_basis": ["yang-mills/README.md", "yang-mills/AI_READING_INDEX.md",
                                  "yang-mills/consolidation/20260916/CURRENT_RESEARCH.md",
                                  "yang-mills/consolidation/20260919/README.md"],
        },
        {
            "id": "S6",
            "title": "S6 topology and related constructions",
            "human_entry": "s6/README.md",
            "human_reader": "s6/26_s6_key_advances_frozen_2026-09-06.pdf",
            "ai_entry": "s6/S6_FROZEN_PROJECT_GUIDE_2026-09-09.md",
            "source_manifest": "s6/S6_FROZEN_PROJECT_PACKAGE_MANIFEST_2026-09-09.json",
            "edition_doi": "10.5281/zenodo.22678442",
            "edition_url": "https://doi.org/10.5281/zenodo.22678442",
            "research_state": (
                "The full project checkpoint frozen on 6 September 2026 preserves the "
                "original transcription, historical annotations, later calculations, "
                "standalone papers, TeX/Bib sources and recorded checks. The five-page "
                "reader provides orientation; the complete 1,079-file archive is linked "
                "through the topic guide and Zenodo edition. This publication does not "
                "independently certify a global complex structure on S6, a CDP20 "
                "counterexample, or a Yang–Mills mass-gap theorem."
            ),
            "description_basis": ["s6/README.md", "s6/S6_FROZEN_PROJECT_GUIDE_2026-09-09.md"],
        },
        {
            "id": "NS",
            "title": "Navier–Stokes reconstruction and validation workbench",
            "human_entry": "navier-stokes/README.md",
            "human_reader": "navier-stokes/navier_stokes_workbench_208p.pdf",
            "latest_continuation": "navier-stokes/continuations/20260919-vacuum-hydrodynamics/README.md",
            "primary_source_reading_record": "navier-stokes/SOURCE_READING_20260920.json",
            "mirrored_primary_latex": "navier-stokes/sources/openai-source-faithful-20260920/upstream/reconstruction/main.tex",
            "mirrored_primary_pdf": "navier-stokes/sources/openai-source-faithful-20260920/upstream/output/pdf/source-faithful-reconstruction.pdf",
            "mirrored_primary_guide": "navier-stokes/sources/openai-source-faithful-20260920/README.md",
            "ai_entry": "navier-stokes/navier_stokes_workbench.tex",
            "source_manifest": "navier-stokes/navier_stokes_primary_manifest.json",
            "research_state_document": "navier-stokes/RESEARCH_STATE.md",
            "research_state_record": "navier-stokes/research-state.json",
            "overleaf_reader": "https://www.overleaf.com/read/hzthvczhdyxc#a60fc2",
            "edition_doi": "10.5281/zenodo.22678406",
            "edition_url": "https://doi.org/10.5281/zenodo.22678406",
            "research_state": (
                "The 19 September vacuum-hydrodynamics continuation recovers an exact "
                "nonlinear marked Einstein constraint-data encoding with a full-velocity "
                "left inverse, a linear Rindler shear response and finite pole-cluster "
                "calculation, and a distinct positive slab-stress regularity theorem. "
                "Unchanged manuscripts, earlier mathematical sources, proof exposition, "
                "compact symbolic/numerical checks and source hashes accompany the guide. "
                "No NS-time Einstein conjugacy, nonlinear blowup cancellation or S6 "
                "implication is established by these maps. "
                "The corrected 9 September 2026 reconstruction examines the supplied "
                "finite-time construction with positive viscosity, zero initial velocity "
                "and smooth compactly supported forcing. The 208-page reader preserves "
                "forcing, pressure, transport, nonlinear terms and correction-cycle "
                "calculations, including the actual-shear remainder and moving-plane "
                "projection. The source manifest and recorded checks accompany the "
                "reader. Complete independent analytical and Lean validation remains "
                "unfinished; the later local formal run is stopped without an endpoint or Comparator certificate."
            ),
            "description_basis": ["navier-stokes/README.md", "navier-stokes/RESEARCH_STATE.md",
                                  "navier-stokes/SOURCE_READING_20260920.json",
                                  "navier-stokes/sources/openai-source-faithful-20260920/README.md",
                                  "navier-stokes/continuations/20260919-vacuum-hydrodynamics/README.md"],
        },
    ]


def generate() -> dict[str, bytes]:
    if git("cat-file", "-t", INSPECTED_MATH_SOURCE_COMMIT).strip() != b"commit":
        raise ValueError("The inspected mathematical source commit is unavailable")
    object_format = git("rev-parse", "--show-object-format").decode("ascii").strip()
    if object_format not in ("sha1", "sha256"):
        raise ValueError("Unsupported Git object format")
    staged = staged_payload()
    hashes = fingerprints(staged, object_format)
    artifacts = []
    for entry in staged:
        size, digest = hashes[entry["git_blob_oid"]]
        artifacts.append({
            "id": artifact_id(entry["path"]), **entry,
            "bytes": size, "sha256": digest,
            "programme_ids": programme_ids(entry["path"]),
        })
    if len({entry["id"] for entry in artifacts}) != len(artifacts):
        raise ValueError("Artifact identity collision; do not publish this catalogue")
    paths = {entry["path"] for entry in artifacts}
    descriptions = programmes()
    for programme in descriptions:
        required = [programme[key] for key in ("human_entry", "human_reader", "ai_entry")]
        required += programme["description_basis"]
        if "source_manifest" in programme:
            required.append(programme["source_manifest"])
        if any(path not in paths for path in required):
            raise ValueError(f"A programme entry point is missing from the index: {programme['id']}")
    exclusions = [
        {"path": path, "reason": "Generated catalogue excluded to avoid recursive fingerprints."}
        for path in OUTPUTS
    ]
    coverage = (
        "Every stage-0 tracked public payload file in the Git index, except the two "
        "generated catalogues listed in excluded_generated_files. Includes preserved "
        "historical paths and staged documentation. Hashes and sizes describe Git blob "
        "bytes, not checkout bytes after newline conversion. Untracked and unstaged "
        "changes, Git internals, archive interiors and externally hosted files are not "
        "inventoried. Archive files themselves are inventoried."
    )
    canonical = json.dumps(artifacts, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    common = {
        "repository": REPOSITORY,
        "inspected_math_source_commit": INSPECTED_MATH_SOURCE_COMMIT,
        "commit_scope": (
            "This is the previously inspected mathematical source baseline, not the "
            "commit of these generated documents or a claim that staged changes are committed."
        ),
        "payload_source": "git_index_stage_0_blobs",
        "git_object_format": object_format,
        "coverage": coverage,
        "excluded_generated_files": exclusions,
        "artifact_count": len(artifacts),
        "payload_inventory_sha256": hashlib.sha256(canonical).hexdigest(),
        "payload_inventory_sha256_encoding": (
            "SHA-256 of the files/artifacts array serialized as UTF-8 JSON with sorted "
            "object keys, literal Unicode, no whitespace and no trailing newline; "
            "entries are sorted by repository-relative forward-slash path."
        ),
        "generator": "tools/update_workbench_index.py",
    }
    workbench = {
        "format": "polyclank-experimental-static-file-catalogue-0.2",
        "implementation_status": "Experimental static-file catalogue; no network protocol deployed.",
        "workbench_id": "KokunoYumeto/yang-mills-interacting-workbench",
        "title": "Yang–Mills, S6 and Navier–Stokes research workbenches",
        **common,
        "human_overview": "README.md",
        "historical_inventory": {
            "pull_request": REPOSITORY + "/pull/1",
            "document": REPOSITORY + "/blob/" + HISTORICAL_INDEX_COMMIT + "/workbench.json",
            "source_commit": "ed8cb4bee090d8f7cc14166199aebdef557d066e",
            "note": "The earlier 22-file snapshot is historical; its existing path IDs are retained.",
        },
        "id_policy": (
            "Preserve ART-001 through ART-022 for the original inventory paths. Additional "
            "paths use ART-PATH- followed by the first 16 hexadecimal digits of SHA-256 "
            "of the UTF-8 path; generation rejects collisions. IDs identify local paths; "
            "the sha256 and git_blob_oid fields identify their exact current payload bytes."
        ),
        "research_state_scope": (
            "Programme descriptions record the published research state and contribution "
            "scope from the linked guides. They prescribe no next mathematical tasks; "
            "participants choose their own investigations within their authorization. "
            "Complete proofs and qualifications remain in the source artifacts."
        ),
        "programmes": descriptions,
        "artifacts": artifacts,
        "validation": {
            "performed": "Staged blob identity, byte count, SHA-256, path and entry-point checks only.",
            "mathematical_checks_performed": False,
            "formal_replay_performed": False,
            "new_mathematical_reviews": [],
        },
        "network": {
            "deployed": False,
            "peer_discovery_performed": False,
            "signed_checkpoints_published": False,
            "scope": "Static discovery metadata; no signed checkpoint, federation receipt or automated reviewer is claimed.",
        },
    }
    manifest = {
        "format": "public-git-payload-manifest-1",
        "title": "Public repository payload fingerprints",
        **common,
        "verification_scope": "Publication integrity metadata; no mathematical verification or Zenodo byte replay is claimed by generation.",
        "files": artifacts,
    }
    if staged_payload() != staged:
        raise ValueError("The staged payload changed during generation; rerun after staging finishes")
    return {
        path: (json.dumps(document, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        for path, document in zip(OUTPUTS, (workbench, manifest))
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify generated output without writing")
    arguments = parser.parse_args()
    generated = generate()
    for relative, content in generated.items():
        target = ROOT / relative
        if target.is_symlink() or target.resolve().parent != target.parent.resolve():
            raise ValueError("Refusing a redirected generated output")
        if arguments.check:
            if not target.is_file() or target.read_bytes() != content:
                print(f"OUTDATED: {relative}", file=sys.stderr)
                return 1
        else:
            target.write_bytes(content)
    count = json.loads(generated[OUTPUTS[0]])["artifact_count"]
    print(f"{'Verified' if arguments.check else 'Generated'} 2 JSON catalogues covering {count} staged payload files.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, subprocess.CalledProcessError, OSError) as error:
        print(f"Catalogue generation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
