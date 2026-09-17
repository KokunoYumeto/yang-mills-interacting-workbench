# Source recovery and execution notes

The actual mounted initial input was the user's Markdown upload. A GitHub connector
read confirmed the pinned cubic PR8 and returned its source text and directory
metadata. The original geometry code was copied and its exact Git blob matched.
A `files.materialize` attempt for the connector response returned “Library access
is disabled for this conversation”; it produced no recovered file. An optional
network recovery helper is included and clearly marked as unexecuted here.

The first attempted interactive container execution was unavailable in this
runtime. The first producer processes were then run through ordinary subprocesses
and polled within this response. The final observed execution records use explicit
`subprocess.run` return codes, not a claim that a background job will finish later.
No asynchronous research service or scheduled task is running.

During local review, one form-feed escape in the draft TeX `\frac` and a JSON
integer-key serialization discrepancy in a provisional checker record were
repaired before the final complete replay. The final coefficient data, source
identities and proof text are bound by the final receipt. The original user input
was not modified. Early progress logs and working source versions are included
for provenance, with the final entry points identified by README.md.
