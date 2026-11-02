# MeshDoc

> **Status: pre-implementation.** This repository currently contains the design specification.
> The implementation described below is what an NLnet [Restack](https://nlnet.nl/restack/) grant
> application proposes to fund. Nothing here is claimed to work yet.
>
> **TODO (you):** keep this status block until the first crate compiles. An honest repo is worth
> more to a reviewer than a hopeful one.

Offline-first, end-to-end-encrypted collaboration for teams whose connectivity is intermittent,
absent, or hostile — disaster response, community health work, and field operations.

<!-- TODO (you): two or three sentences in your own words on what this is and who it is for.
     Do not describe it as an AI project. Do not mention translation. -->

## The gap

<!-- TODO (you): describe the missing layer. Reference projects by name and be accurate.
     The argument to land: message tools exist, document tools exist, but the document tools
     are server-centric and the message tools do not carry structured records. -->

## What this repository will contain

| Component | Purpose | Status |
|---|---|---|
| `crates/meshdoc-core` | CRDT documents, change format, identity, workspace membership | not started |
| `crates/meshdoc-crypto` | XChaCha20-Poly1305 envelopes, signatures, key rotation | not started |
| `crates/meshdoc-sync` | Anti-entropy reconciliation, chunking, ACK and resume | not started |
| `crates/meshdoc-transport` | `MeshTransport` trait + mock transport for tests | not started |
| `crates/meshdoc-transport-ble` | BLE advertising discovery (FOSS path) | not started |
| `crates/meshdoc-transport-wifidirect` | Wi-Fi Direct bulk transfer (FOSS path) | not started |
| `relay/` | Store-and-forward encrypted blob relay, single binary | not started |
| `android/` | Reference client | not started |
| `fuzz/` | Partition/merge schedule fuzzer + convergence oracle | not started |

<!-- TODO (you): adjust names to the layout you actually intend to build, then keep it current. -->

## Design principles

<!-- TODO (you): 4-6 bullets. Suggested territory, but write them yourself:
     - every wire format is encrypted before it is transported
     - no server is required for correctness; the relay is optional and untrusted
     - every change is attributable to a signing key that appears in the membership log
     - the libraries are the deliverable; the app is the proof
     - document sizes stay small so mesh bandwidth stays free for what matters -->

## Non-goals

<!-- TODO (you): keep your original list — it is genuinely good and reviewers reward it.
     Explicitly out of scope: chat/messaging, maps and navigation, iOS, our own cryptography,
     our own CRDT implementation, and any generative-AI or machine-translation features. -->

## Licence

<!-- TODO (you): pick ONE and delete the other licence files in this directory.
     - Apache-2.0  — maximum reuse, including in European commercial and public-sector deployments
     - AGPL-3.0    — copyleft, including for network services
     - EUPL-1.2    — European copyleft designed for public-sector interoperability
     Then replace the line below. -->
Licensed under the **TODO-LICENCE**. See `LICENSE`.

## Contributing

<!-- TODO (you): keep this short. If the grant is awarded, the project must follow
     NLnet's GenAI policy v2.0: GenAI may be used read-only (review/analysis) but
     not to produce code, design or documentation, and use must be disclosed.
     A three-line policy here is worth the twenty minutes. -->

---

### Repository setup checklist

- [ ] Delete the unused files in `LICENSE-*` and add the chosen one as `LICENSE`
- [ ] Set the repository description on GitHub (one line, same as the summary claim)
- [ ] Add topics: `local-first`, `crdt`, `offline-first`, `bluetooth`, `mesh`, `e2ee`, `rust`, `android`
- [ ] Enable Issues; keep the templates in `.github/`
- [ ] Decide visibility — public is required for the grant, and early publication is a signal
- [ ] Add the design spec (`DESIGN.md`) in your own words
- [ ] Do **not** add a code of conduct or contributor guide you do not intend to maintain
