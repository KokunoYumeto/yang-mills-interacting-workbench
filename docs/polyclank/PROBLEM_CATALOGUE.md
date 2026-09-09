# Short problem names, exact statements, portable catalogues

[Documentation home](README.md) • Proposed conventions, not a populated 7,000-problem registry

## Three identifiers serve different purposes

**A readable alias** gives people a short reference, for example ERDOS followed by an existing catalogue number. The full source namespace must accompany the alias because there are multiple Erdős lists. An internal index should preserve the original catalogue's identifier rather than inventing a competing number.

**A stable problem identity** identifies a question across locations and editions. Use an established source identity where possible; otherwise a workbench-scoped identifier gives decentralized minting without a central numbering authority. Names, people, dates and websites can change without requiring the mathematical question to become a new question.

**An exact statement revision** identifies the actual definitions, assumptions, quantifiers and alternatives being investigated. A materially different statement gets its own revision, with the relationship explained. The mathematical meaning of an edit cannot be inferred merely from a textual similarity score or hash.

A content hash fingerprints a particular serialized record or artifact. It is not a short explanation of the mathematics. A signing key identifies a publisher, not a theorem's truth. A DOI identifies a registered scholarly object; it is not the universal problem number.

## Questions from Stack Exchange and other discussions

Use the site namespace plus the stable question/post identifier as the source alias: distinguish Mathematics Stack Exchange from MathOverflow. Preserve the original link and the revision inspected. A username and posting date can be attribution metadata but are poor primary identifiers: users rename themselves, questions are edited, and similar names recur.

Retain the source question alongside the explicit mathematical statement extracted from it. Preserve its parameters, hypotheses and alternatives; a post may contain several subquestions or an ambiguous formulation. Record the extraction and do not silently correct or normalize it. Alias claims that two catalogues name the same problem should have provenance and, where necessary, an exact mathematical equivalence argument.

## The minimum discoverable record

Provide the readable title and identifiers; exact statement and definitions; original source and inspected version; related workbench descriptors; known results with their scopes; current challenges; and a dated research synopsis. The status must say who assessed it and from what evidence. An inaccessible or stale catalogue is not evidence that the question remains open.

Preserve distinctions such as all cases versus one family, finite bound versus universal quantifier, existence versus an algorithm and its guarantees, and fixed parameters versus uniform or simultaneous limits. Proof method is not itself a correctness grade. Stronger, generalized and equivalent are relationships to justify, not a single numeric score.

## Importing the owner's catalogue

The owner reports a catalogue of approximately 7,000 known open problems; its contents were not supplied or imported in this change. When available, preserve the source catalogue as a snapshot, retain its native IDs, extract candidate records, flag ambiguous entries, and check current status against primary sources before advertising any item as open or solved. Do not bulk-publish protected source text merely because it appears in the catalogue.

The importer should produce a report of collisions, missing sources, variants and unverified statuses. It should be interruptible and resume without duplicating records. The network can start with partial coverage; no participant must validate every problem before joining.

## Discovery without a mathematical gatekeeper

A registrar lists where records can be found and when endpoints were last reached. Mirrors can exchange those listings. An inclusion decision governs a registrar's directory, not whether a mathematical proof is true. Keep downloaded heads and access failures so a reader can see which peers were actually consulted.

No catalogue entry forces a job onto an idle participant. A researcher may choose an existing direction, propose a new one, work on an exposition, or contribute only checking. The current state enables that choice; it does not dictate it.
