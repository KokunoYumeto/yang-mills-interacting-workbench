# Source coverage and edition provenance

## Intake and recovery

The source export has 224,625 bytes, 7,110 lines and SHA-256 `7738120184cd5c3080637eabef0680a730bb5fe97ad054a0832a0cd3238766dd`. Its eleven complete final mathematical responses are preserved with exact line ranges and hashes in [transcript-mathematics/DELIVERY_MAP.json](transcript-mathematics/DELIVERY_MAP.json). Private prompts, tool traces and thinking text remain outside the public repository. The last three progress-only responses announce fourth-order work but supply no completed fourth-order delivery.

| Download | SHA-256 | Contribution |
| --- | --- | --- |
| `yang_mills_actual_loop_moments.zip` | `f31503f558d40b550e0afdbd1326d75aecae9bef63321341962be549228bed33` | Actual-loop note and checks, with preceding response/refinement/workflow source snapshots. |
| `yang_mills_gauge_native_continuation.zip` | `19040fd3e72c7a3c0a7a084375b0fe3bace560791ca7054af96c2f629182b323` | Cumulative uniform-gap, gauge-native, second-source, spatial-return and band/certificate proofs and checkers. |
| `yang_mills_cubic_linearized.zip` and `yang_mills_cubic_linearized (1).zip` | `c031cab99f782c7025000a2bee1bc7afb9c53d39a3651d4da8c41a876a51d2ef` | Identical deliveries of the cubic and linearized proofs, producer/replay sources and complete verification record. |

The three archive manifests were checked statically against their members. The original patches are identified in the [input manifest](provenance/SOURCE_INTAKE.json); the integration uses the full source bodies after comparison, rather than assuming that a patch is cumulative or applying it blindly over a newer tree.

For download redundancy, the gauge-native delivery contains all 31 distinct `yang-mills/` paths from the actual-loop delivery: 30 match exactly, and only the successive checkpoint differs. The newest cubic delivery is incremental: of the gauge-native delivery's 60 `yang-mills/` files, it shares only a changed checkpoint and omits the other 59. Its dependencies therefore cannot be recovered from that newest ZIP alone. [ARCHIVE_REDUNDANCY.json](provenance/ARCHIVE_REDUNDANCY.json) records the complete member comparison, including the repeated predecessor checkpoint in the earlier archive.

The later attachment named `ZETA_SEVEN_OBSERVABLE_20260916.patch` has Yang–Mills contents: 570,101 bytes, SHA-256 `50f5903bba72da27b8ca25a159d1ee72e52db11ea93cc6b7fe9d35605a4288b7`. It is byte-identical to the cumulative `yang_mills_gauge_native_continuation.patch` inside the gauge-native ZIP. Its 38 file changes add no missing material to this union. The filename does not establish the patch's subject.

## Git source closure

The receiving default-branch baseline is `fab69fdc4ac197159b8e6ae8d73a82bde2b20d55`. PR4 through PR6 supply the vacuum-refinement, energy-workflow and coupled-response chain. PR8 at `91434b6962062bd80439d4cb2cae9d2479264dde` supplies that ancestry and the cubic continuation. The sibling PR7 at `dd2cefd` supplies the separate full local-fibre proof. Exact full commit IDs and per-file origins are recorded in the intake manifest.

The union of those Git sources and the three archive payloads has 77 logical paths. Every overlapping mathematical proof, checker, state and receipt file agrees byte for byte. The only differing shared file is `research-control/CURRENT.md`, because it records successive checkpoints. All five source variants are retained under [provenance](provenance/); the live entry points identify the integrated edition. The original spectral reconstruction note is replaced by the source chain's explicit correction about escaping spectral labels; its baseline remains recoverable at the pinned receiving commit.

The downloaded `AGENTS.md` is historical workflow material, not a mathematical dependency or a current user instruction. It was not installed as repository policy by this consolidation. Full proof bodies, their parameter conventions and scoped receipts are retained unchanged. Historical claims such as “not published” or “no independent review” describe the source's own date; fresh validation and publication records are separate.

## Explicitly unavailable attachments

The intake does not contain the first `split_zero_yang_mills_research.zip`, the standalone smooth-continuum package, the later gauge-resolved full-proof package, or the full checker package named `yang_mills_zero_shift_local_fibres.zip`. Their absence does not erase the visible mathematics: the complete visible final responses are retained, and PR7 supplies its complete 1,031-line proof. However, a final response is not represented as the contents of an absent linked attachment, and missing verification programs are not reported as freshly replayed.

A bounded attempt to retrieve those attachments from the original conversation reached an explicit access-denied message in the available browser session. No replacement attachment was inferred from that failure. The mathematical responses and available Git sources remain preserved.

The earlier private-literature workbench ZIP/PDF and unrelated downloads are not replacements for the three missing continuation sources. Earlier published Yang–Mills foundations remain in the original source directories and readers, so this edition is usable within a full clone of the repository.

## Reader and reproduction

The reader is a complete-source reading edition with source paths and hashes, not a compression of the mathematical text. Its historical-response appendix preserves the earlier claims and later development. The [current state](CURRENT_RESEARCH.md) and [bounded audit reports](audits/) explain how to read the source sequence without promoting earlier or narrower results to a stronger theorem.

Fresh checker execution is described in [VALIDATION.md](VALIDATION.md). The original recorded JSON remains unchanged. Platform differences in newline and path serialization are handled by using the stated POSIX replay environment, not by editing source pins or claiming a mismatched receipt passed.
