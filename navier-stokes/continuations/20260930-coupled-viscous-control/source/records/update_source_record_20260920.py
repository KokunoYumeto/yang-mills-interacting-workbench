from pathlib import Path
import hashlib, json, subprocess, urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sources" / "reconstruction_5e162f34"
OUT.mkdir(parents=True, exist_ok=True)
COMMIT = "5e162f34cd2d3581f890660e81fbf063509085d0"
BASE = "https://raw.githubusercontent.com/KokunoYumeto/openai-navier-stokes-latex/" + COMMIT + "/"
files = [
    "README.md", "evidence/source/OFFICIAL_LATEX_SOURCE_SEARCH_20260919.md",
    "evidence/source/SOURCE_FREEZE.json", "reconstruction/sections/pp007-012.tex",
    "reconstruction/sections/pp019-024.tex", "reconstruction/sections/pp025-030.tex",
    "reconstruction/sections/pp037-042.tex",
]
manifest = {}
for name in files:
    data = urllib.request.urlopen(BASE + name, timeout=25).read()
    target = OUT / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    manifest[name] = {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
corpus = Path("<user-root>/Documents/Papors/Chatnotes/Zeta-Function-Foundation")
query = subprocess.run(["python", "scripts/query_corpus.py", "--layer",
    "research_literature", "--index-level", "canonical", "--json", "Navier Stokes"],
    cwd=corpus, check=True, capture_output=True, encoding="utf-8")
(ROOT / "records" / "literature_route_20260920.json").write_text(query.stdout, encoding="utf-8")
record = {
    "source_id": "NS-166-RECON-5e162f34",
    "upstream_source_id": "NS-166",
    "version": COMMIT,
    "source_type": "independent_reconstruction_not_original_author_TeX",
    "source_author_as_recorded": "OpenAI",
    "reconstruction_public_author": None,
    "github": "https://github.com/KokunoYumeto/openai-navier-stokes-latex/tree/" + COMMIT,
    "zenodo": "https://zenodo.org/records/22852310",
    "doi": "10.5281/zenodo.22852310",
    "reported_pdf_sha256": "67bca97d638868c2fcb34b0ef1acdc4918cfcbb1a210afe98f0019a3c93fe8d9",
    "reported_zip_sha256": "48b42eaec06b602f42594a5bf6c679f79be7a8b3644bc2da6e434cab98f0dc0e",
    "pdf_zip_independently_downloaded_here": False,
    "fetched_files": manifest,
    "read_coverage": ["README.md", "evidence/source/OFFICIAL_LATEX_SOURCE_SEARCH_20260919.md"],
    "original_author_TeX": "not located by supplied bounded search; reconstruction kept distinct",
    "mathematical_use": "Version routing for finite angular/phase definitions. The new finite kernel proof is supplied in full locally.",
    "whole_source_proof_verified": False,
}
(OUT / "source_record.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"source_id": record["source_id"], "files_fetched": len(manifest)}))
