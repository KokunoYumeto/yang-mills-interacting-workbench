# Yang–Mills workflow and local-score energy refinement

Contribution commit f583ed5ddb13b3ca517c1bab2958f6a4be612d78, draft PR #5,
stacked on unmerged PR #4. The full new mathematical note is
`yang-mills/research-control/RESEARCH_NOTE.md`; start the workflow with
`yang-mills/AGENTS.md` and `yang-mills/research-control/WORKFLOW.md`.

The new checker needs only the Python standard library. From this archive root:

    python -B yang-mills/research-control/check.py --verify-receipt yang-mills/research-control/verification.json
    python -O -B yang-mills/research-control/check.py --verify-receipt yang-mills/research-control/verification.json

The inherited PR4 note and checker are included separately and unchanged.
Its checker needs SymPy. `evidence/` contains its actual local replay and the
fresh-copy and named command-line rejection record for the new checker.
Peer proof bodies are accessed through their exact source pins; this package
does not repackage those libraries or claim an offline full-source audit.

The checker output records finite fixture scope. It does not verify analytic
prose or establish the continuum mass gap. No paid or background task is running.
