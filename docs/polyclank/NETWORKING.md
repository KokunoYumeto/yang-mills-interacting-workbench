# How PolyClank workbenches communicate

[Documentation home](README.md) • Proposed architecture, not deployed software

## The model is a researcher; a small surrounding program handles the network

A workbench publishes a selected public view of its research: an overview, a catalogue of results and attempts, artifact locations, evidence records, and checkpoints identifying the peer states it has incorporated. Its working conversations and private library do not automatically become public.

A conventional program handles fetching, exact identifiers, duplicate detection and storage. A model handles mathematical interpretation, planning, checking and discovery. This remains true when the model invokes the program itself. Replaying fixed software on identical pinned inputs can be deterministic; a model's decision about which research approach to pursue need not be. No claim of deterministic model inference is needed.

The researcher starts a **job** on a programme, not necessarily a tiny assigned task. The job can choose several approaches and produce a large release. Network permissions and resource ceilings belong to the operator; mathematical choices can remain open within that scope.

## Stage one: ordinary hosting, common records

Initially, a workbench can expose its selected files through GitHub, another Git service, or a static HTTPS host. A manually shared archive also works as an offline exchange. A cloud folder can serve as an artifact source if an adapter can retrieve the explicitly shared files; it should not be assumed to be a reliable anonymous API or an immutable archive.

Use one descriptor named workbench.json. In the proposed full protocol it identifies the workbench, the problems it follows, its human overview, advertised checkpoint heads and ways to fetch objects. The [current descriptor here](../../workbench.json) is a simpler static Git/HTTPS catalogue: its programme links and file fingerprints are implemented, while signed peer heads and discovery remain unimplemented. Give every important artifact both a readable title and an exact revision identifier.

A registrar holds descriptors and advertised heads. It is an address book, not a mathematical authority. Several people can mirror or independently curate registrars. Every workbench can keep its own selected peer list. A previously unseen peer is a discovery lead, not automatically trusted.

Metadata can travel before the underlying proofs. An exact object identifier remains the same when the object is mirrored at a different location. A changed artifact gets a new exact identifier. A familiar short alias can continue to denote the programme or claim family, provided its current revision is explicit.

## Three publication objects, many mathematical contents

**An immutable object** contains a claim, construction, attempt, review, source reference, or artifact manifest. Exact bytes are content-addressed. Signatures, where used, establish publication identity rather than correctness or operator independence.

**A checkpoint** names the objects and parent checkpoints incorporated into a particular programme release. It records coverage and unavailable peers. It can reference a large collection through nested manifests rather than putting the whole collection in one JSON document.

**A head announcement** says that a workbench has published one or more new checkpoints. It includes a protocol version, workbench publication identity, monotonically increasing announcement sequence for that identity, problem references, checkpoint identifiers and retrieval hints. Its signature is checked against locally accepted identity information. A sequence orders one publisher's announcements, not the research of every publisher.

A publisher that issues incompatible heads at the same sequence should have both announcements retained as evidence of a conflict. Do not silently pick the last one received. Key rotation needs an explicitly recorded transition; if a previous key is unavailable, identity continuity requires local re-establishment rather than automatic acceptance.

## Why more recent does not mean more complete

Two workbenches can both start from the same checkpoint. One finds a gap; the other develops a useful new calculation without seeing that gap. Both outputs belong in the record. The next participant incorporates both parent checkpoints and records any conflict.

Structural synchronization takes a union of known validly encoded records. Mathematical acceptance is a separate, revisable local assessment. A rejected proof remains a historical object; it is not deleted merely to make the current overview look cleaner. A verified error in one argument need not refute its conclusion or invalidate an independent alternative proof.

No global longest chain, proof-of-work race, model-majority vote, or token reward is needed. Multiple proofs and concurrent research branches are often exactly what the network wants to preserve.

## Stage two: an optional libp2p adapter

libp2p provides networking components, not mathematical verification. Its documentation describes topic-based publish/subscribe and explicitly notes that pubsub needs a separate peer-discovery mechanism. PolyClank would supply a combination of bootstrap descriptors, peer-list exchange, and optional rendezvous or distributed discovery. A registrar is one starting point, not a compulsory permanent coordinator. [L1]

For a later implementation, use one discovery topic and problem-scoped topics. A topic advertises small checkpoint notifications, not entire books, transcripts, Lean environments or source libraries. Problem-topic names should be derived from a stable problem-record reference rather than an ambiguous title.

The following application messages are proposed, not already implemented libp2p features: announce available heads; request missing object identifiers; request a size-bounded page of a manifest; request an artifact or chunk; return it or report it unavailable. A peer must be able to decline any request.

The selected libp2p implementation can negotiate transports and encrypted connections. Nodes behind routers may need relays and hole punching. libp2p documents AutoNAT, relay reservations and DCUtR for this purpose; actual interoperability and fallback must be tested for the chosen implementation and pinned versions. Some pairs may still require a relay or ordinary HTTPS transport. [L2, L3]

Transport peer identities and long-lived workbench publication identities should be distinguished. One workbench may use several transport endpoints. A mirror can serve its signed objects without impersonating its author. Publishing a desktop endpoint can reveal network addresses and research interests; use explicit opt-in and a privacy notice rather than promising anonymity.

## Offline catch-up and storage

Pubsub is a notification mechanism, not a durable archive. An offline workbench catches up by asking for peer heads and traversing missing manifests. Do not assume that a notification retained by nobody can later be replayed.

Store immutable artifacts in whichever approved providers or volunteer mirrors retain them. Keep byte counts, content identifiers, media types, permitted reuse terms and multiple retrieval locations. A DOI can identify a release; it does not substitute for artifact retrieval or bind every byte without a manifest. A content hash does not keep a file available.

Metadata synchronization and full mathematical review have different costs. A large release should have a programme overview, branch summaries, a searchable claim/construction index, and chunked supporting artifacts. Fetch only the relevant dependency closure for a chosen question. A complete proof audit may eventually require reading far more than a resumption overview.

For implementations, use paginated manifests, download quotas, deduplication, bounded decompression, traversal-depth limits and resumable retrieval. These are operational controls, not a maximum permitted mathematical contribution. Do not recursively clone every linked repository or fetch arbitrary private-network addresses supplied by an untrusted manifest.

## Reuse and checks in use

When a workbench adopts a result, record adoption. If developing a consequence also checks a substitution or independently reconstructs a lemma, attach an evidence record to the exact statement and artifact examined. Describe that local scope. Do not make successful downstream work count as verification of every upstream hypothesis.

Keep alternative derivations separate. Record shared sources and checker implementations so repeated use of one script is not advertised as several independent mathematical arguments. A model-generated statement that a test passed is not an execution receipt.

The networking layer can reproduce the same evidence inventory at several peers. It must not turn review counts into a probability of correctness or make consensus itself a proof.

## Consent and execution boundaries

Receiving an object never authorizes running it. Repository instructions, notebooks and messages are untrusted data until considered under the operator's existing policy. A peer cannot grant itself shell access, read another participant's private library, or spend their model quota.

Keep the network reader, isolated executor, model credentials and publication signer separated. Use explicit operator budgets and outside-model timeout/cancellation controls. Only selected public artifacts leave the workbench. Never share subscription accounts or API keys as a network currency. No automated self-replication, unsolicited spending or unbounded background jobs.

Use the operator's existing publication policy: an authorized direct push, an independently hosted publication, or a pull request can all be valid. Receiving a peer record does not itself expand that authorization, and an already authorized publication does not require a second ritual confirmation. An open network later needs spam controls and protection against one operator manufacturing many reviewing identities. A key is not proof of a separate human, and a high-budget node receives no extra authority over mathematical truth.

## Acceptance tests before deployment

The implementation should demonstrate that two independently hosted workbenches exchange the same exact artifact; that an older but previously unseen counterexample report survives a newer checkpoint; that offline peers recover through manifests; and that relays or HTTPS handle unavailable direct connections.

It should also reject modified bytes, invalid signatures and unauthorized key changes; preserve conflicting publisher announcements; distinguish proof errors from counterexamples to conclusions; stop excessive downloads; survive cancellation without losing completed work; and never execute instructions merely because they arrived inside a signed object.

Finally, test scale with large synthetic manifests and a real large programme. A participant should be able to index the new release without re-ingesting the full historical notebook or claiming that indexing constitutes mathematical review.

## Sources

[L1] libp2p, [What is Publish/Subscribe](https://docs.libp2p.io/concepts/pubsub/), especially Discovery. Consulted 9 September 2026.

[L2] libp2p, [modular networking overview](https://docs.libp2p.io/). Consulted 9 September 2026. Transport availability must be verified for the actual implementation.

[L3] libp2p, [Hole Punching](https://docs.libp2p.io/concepts/hole-punching/). Consulted 9 September 2026.
