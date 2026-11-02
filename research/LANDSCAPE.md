# MeshDoc — Competitive Landscape and Prior Art

**Prepared for:** NLnet grant application (competitive-landscape / prior-art section)
**Date of research:** 2026-11-02 (all URLs checked this day, UTC unless stated)
**Author:** landscape-analyst (delegated research)
**Deliverable path:** `/home/logic/grant/research/LANDSCAPE.md` (only file written)

---

## 0. How to read this document (method and honesty rules)

**What was checked.** Every licence below was read from the project itself — a `LICENSE`/`COPYING`
file, the repository's machine-readable licence field (`api.github.com/repos/<owner>/<repo>`), the
project's own site, or the package manifest. Where a project is not on GitHub (GitLab, Gitea, IETF)
the equivalent source was used. Nothing here is copied from a licence-summary blog.

**Marking convention.** Each factual claim carries a marker:

- `[VERIFIED <url>]` — the claim was read directly from that URL on 2026-11-02.
- `[UNCERTAIN]` — we could not confirm it (dead site, no licence file, ambiguous source, or a
  negative search result). Treat as a question to resolve before submission, not as fact.

Where a single marker covers several facts in one bullet (for example a licence *and* a project
description both taken from the same repository page), the URL is the source for all of them.

**Three cautions for the proposal author**

1. **Licences can change.** SPDX strings below are a snapshot. Re-check any licence you cite in the
   final application, especially for projects we propose to depend on.
2. **"No licence file" is not "public domain".** Two projects below (`diamond-types`, parts of
   `p2panda`) expose no root licence file. Absence of a licence means *no permission granted*, so
   they cannot be reused; only read.
3. **Negative claims are the weakest.** Statements of the form "no project does X" are labelled
   `[UNCERTAIN]` unless they rest on a source that explicitly says so. The proposal should phrase
   them as "we found no … in our survey", not "none exists".

**Scope note.** MeshDoc's own design (ed25519+x25519 device identity, QR-shared workspace key,
CRDT structured types, encrypted+signed diffs, BLE + Wi-Fi Direct mesh, optional dumb relay, Android
reference client) is taken from the project brief and is *not* re-cited here; only external claims
about neighbours are cited.

---

## 1. Executive summary — the six strongest "we are different because…" claims

These are ordered by how hard they are for an incumbent to copy and how well the evidence supports
them. Each claim is followed by the *gap evidence* a reviewer can check.

### Claim 1 — MeshDoc carries **documents**, not chat, over a mesh. The nearest FOSS mesh apps carry messages, feeds or positions.

The five closest libre mesh/off-grid apps all define their payload as messages or posts:

- **Briar** is "a messaging app" whose P2P sync uses Bluetooth, Wi-Fi, Tor or memory cards, with an
  E2EE message store and a store-and-forward "Briar Mailbox" `[VERIFIED https://briarproject.org/how-it-works/]`.
  Its long-term roadmap explicitly lists "distributed applications such as crisis mapping and
  **collaborative document editing**" as *future* work `[VERIFIED https://en.wikipedia.org/wiki/Briar_(software)]`
  — i.e. the category MeshDoc targets is acknowledged and still unshipped there.
- **Meshtastic** "carries text messages and position reports across a wireless mesh of nodes, using
  LoRa" and its channels are "a named, encrypted group" keyed by a shared channel key
  `[VERIFIED https://meshtastic.org/docs/overview/]`.
- **qaul** is described by its NLnet grant abstract as "a privacy-preserving, internet-independent,
  off-the-grid, delay-tolerant P2P mesh messenger" `[VERIFIED https://nlnet.nl/project/P2P-channels/]`.
- **Manyverse** is a "peer-to-peer social network" built on SSB, syncing "through a shared local
  Wi-Fi or on the internet" `[VERIFIED https://manyver.se/]`.
- **Berty** ships the Wesh mesh-network protocol and a messenger on top of it
  `[VERIFIED https://berty.tech/]`.

**Gap evidence:** none of these offers a typed, mergeable *document* (checklist, supply form, geo
point, note) as the wire object; the unit of collaboration is a message or a feed entry. MeshDoc's
differentiator is not "mesh" but "**CRDT documents as the thing that travels**" — which none of the
above claims.

### Claim 2 — Encryption is at the **data layer** (encrypted, signed CRDT changes), not bolted onto the transport.

CRDT libraries deliberately leave security to the application. The NLnet-funded SecSync project
states the gap precisely: "While popular CRDT implementations like Yjs or Automerge offer several
designs and even implementations on how to asynchronously exchange data using servers, **there is no
plug & play implementation serving end-to-end encrypted systems**" `[VERIFIED https://nlnet.nl/project/Naisho/]`.
The CRDT projects themselves describe collaboration/sync, not confidentiality or authorship
signing: Automerge is "a local-first sync engine for multiplayer apps that works offline"
`[VERIFIED https://automerge.org/]`; Yjs is "shared data types for building collaborative software"
`[VERIFIED https://github.com/yjs/yjs]`; Loro is "make your JSON data collaborative and
version-controlled with CRDTs" `[VERIFIED https://github.com/loro-dev/loro]`.

**Gap evidence:** E2EE-CRDT work exists (SecSync, see §4) but is **server-mediated**: SecSync is "a
protocol to efficiently exchange and resolve e2e encrypted CRDTs" built around "snapshots as well as
operations logs referencing snapshots" `[VERIFIED https://nlnet.nl/project/Naisho/]`. MeshDoc makes
the *change itself* encrypted and signed by its author, so a relay can hold it without decrypting
and peers can authenticate authorship without a server. That combination — per-change signature +
workspace-key encryption + CRDT merge over an untrusted, intermittently connected mesh — is the
novel core.

### Claim 3 — The design target is **delay-tolerant anti-entropy**, not server sync. Mainstream CRDT sync assumes a server or a reliable socket.

The dominant sync paths for the leading CRDT engines are server- or socket-shaped: Automerge's
sync engine syncs "when you reconnect" `[VERIFIED https://automerge.org/]`; Yjs's ecosystem is
organised around provider modules and a `docs.yjs.dev` server-oriented documentation set
`[VERIFIED https://docs.yjs.dev]`; cr-sqlite is "convergent, replicated SQLite" with multi-writer
support but no DTN transport in its own description `[VERIFIED https://github.com/vlcn-io/cr-sqlite]`.
Meanwhile the standards world has the opposite gap: DTN is standardised (Bundle Protocol v7 is an
IETF Standards-Track RFC, January 2022) `[VERIFIED https://www.rfc-editor.org/rfc/rfc9171.txt]` and
the IETF DTN working group reports "multiple independent implementations … in both space and
terrestrial environments" `[VERIFIED https://datatracker.ietf.org/api/v1/group/group/?acronym=dtn]`,
but we found no project that defines how CRDT operations map onto bundles. `[UNCERTAIN — negative
search result; see §5 for what we did search]`

**Gap evidence:** MeshDoc's unit of transfer is the encrypted CRDT diff, and its relay is a "dumb
store-and-forward encrypted blob server". That is a *DTN-shaped CRDT profile*: application-agnostic
relays, epidemic anti-entropy between peers, and no requirement that any server understands the
document. No surveyed project occupies that intersection.

### Claim 4 — Humanitarian structured data is **convergent**, not form-submission. The humanitarian incumbents are server-authoritative.

The tools a reviewer will name are all server-centric:

- **KoboToolbox**: `kpi` is "the server for KoboToolbox" `[VERIFIED https://github.com/kobotoolbox/kpi]`.
- **ODK**: Collect is "an Android app for filling out forms"; Central is "a server that is easy to
  use, very fast" `[VERIFIED https://github.com/getodk/collect]` `[VERIFIED https://github.com/getodk/central]`.
- **DHIS2** is a platform to "collect, validate, analyse, visualize, and secure share of data", with
  data capture "anywhere, online and offline" — but the model is a national/central instance
  `[VERIFIED https://dhis2.org/]`.
- **Ushahidi** is "crowdsourcing solutions" for "citizen-generated data" deployed as a platform
  `[VERIFIED https://www.ushahidi.com/]`.
- **Sahana Eden** is a humanitarian management web platform (MIT-licensed, archived legacy repo)
  `[VERIFIED https://github.com/sahana/eden-legacy]`.

**Gap evidence:** offline *capture* is a solved problem in this family; offline *merge between
peers who never share a server* is not. KoBo/ODK submissions are records reconciled by a central
instance; they are not shared mutable objects. MeshDoc's checklist/supply-form/geo-point are CRDT
objects that converge pairwise, then reconcile with a relay or server later if one exists. This is
the direct answer to "why not KoBoToolbox?" — KoBo is the right tool when a server exists; MeshDoc
is for when it does not.

### Claim 5 — **Accountless identity + QR-shared workspace key** lets a team start working with zero infrastructure and zero registration.

- **Signal** uses "a centralized computing architecture" and its clients/server are AGPL-3.0-only
  `[VERIFIED https://en.wikipedia.org/wiki/Signal_(software)]` `[VERIFIED https://github.com/signalapp/libsignal]`.
- **SimpleX** has no user identifiers ("The only messaging network without any user identifiers")
  but is server-relayed (SMP servers) `[VERIFIED https://simplex.chat/]` `[VERIFIED https://github.com/simplex-chat/simplex-chat]`.
- **Matrix/Element** is federated client-server; Element Web and Synapse are AGPL-3.0
  `[VERIFIED https://github.com/element-hq/synapse]` — a homeserver is required.
- **Briar** is accountless and serverless, but its unit is messaging, not a shared workspace
  `[VERIFIED https://briarproject.org/how-it-works/]`.
- The closest *key-management* neighbour is **Keyhive** (Ink & Switch, NLnet NGI Zero Core
  2024–2026): "a synchronization engine for end-to-end encrypted group collaboration" with "edge
  names, invites and group key agreement for local first data"
  `[VERIFIED https://nlnet.nl/project/Keyhive/]` — but it is a sync engine, not a field data toolkit.

**Gap evidence:** MeshDoc's onboarding is a QR code that transfers a symmetric workspace key to a
device identity generated on-device. No account, no phone number, no server, no invite service. The
combination of *accountless identity* + *shared workspace key* + *structured documents* is not
offered by any surveyed project; Keyhive is the natural future upgrade path (see §6).

### Claim 6 — A **reusable permissive library stack** (Rust core + Android reference client), where the closest neighbours are apps or copyleft.

The mesh/CRDT neighbours are mostly application-shaped or copyleft, which limits embedding in
humanitarian tooling:

- qaul is AGPL-3.0 `[VERIFIED https://github.com/qaul/qaul.net]`
- SimpleX is AGPL-3.0 `[VERIFIED https://github.com/simplex-chat/simplex-chat]`
- Signal's protocol library libsignal is AGPL-3.0 `[VERIFIED https://github.com/signalapp/libsignal]`
- Earthstar is LGPL-3.0 `[VERIFIED https://github.com/earthstar-project/earthstar]`
- Meshtastic is GPL-3.0 (firmware and Android app) `[VERIFIED https://github.com/meshtastic/firmware]`
- Reticulum uses a custom, non-OSI licence with a no-harm clause and a ban on use in AI training
  data `[VERIFIED https://github.com/markqvist/Reticulum]`
- diamond-types ships no licence file at all `[VERIFIED https://github.com/josephg/diamond-types]`

By contrast, the permissive neighbours are narrow: Automerge (MIT) `[VERIFIED https://github.com/automerge/automerge]`,
Loro (MIT) `[VERIFIED https://github.com/loro-dev/loro]`, cr-sqlite (MIT) `[VERIFIED https://github.com/vlcn-io/cr-sqlite]`,
Keyhive and SecSync (Apache-2.0) `[VERIFIED https://github.com/inkandswitch/keyhive]` `[VERIFIED https://github.com/nikgraf/secsync]`
— none of which ship a mesh transport or a field app.

**Gap evidence:** a permissively licensed, library-first stack (transport crates + CRDT document
schema + relay) that an NGO or another mesh project can embed is absent. This is also the strongest
argument that MeshDoc's output is *infrastructure*, not another app — and it is what makes the
upstream-contribution plan in §6 credible.

**What these claims do *not* say.** MeshDoc is not first at mesh messaging (Briar/Serval/Bridgefy),
not first at CRDTs (Automerge/Yjs/Loro/cr-sqlite), not first at E2EE (Signal/MLS), and not first at
humanitarian data (KoBo/ODK/DHIS2). Its claim is the *intersection*: E2EE CRDT documents, authored
per change, merged by anti-entropy over intermittent BLE/Wi-Fi Direct links, with a dumb DTN relay,
shipped as a reusable library. The proposal should say exactly that and cite the neighbours below.

---

## 2. Comparison table

The table is split by category to stay readable. "Gap vs MeshDoc" is the sentence a reviewer can
lift into the "what is new" paragraph. Every licence cell carries the exact source we read; a
`[UNCERTAIN]` in that column means no licence file was found at the repository root and the project
must **not** be treated as reusable without clarification.

### 2.1 CRDT / local-first sync engines

| Project | Licence (evidence) | What it does / how data moves | Data model | E2EE | Server required | Gap vs MeshDoc |
|---|---|---|---|---|---|---|
| **Automerge** | MIT `[VERIFIED https://api.github.com/repos/automerge/automerge]` | JSON-like CRDT, local-first sync engine, offline queueing, Rust core + JS/WASM `[VERIFIED https://automerge.org/]` | JSON documents | No — app must supply | No server required, but sync assumes a sync endpoint/peer | Strong engine candidate, but no transport, no identity, no signature of changes |
| **Yjs** | MIT `[VERIFIED https://raw.githubusercontent.com/yjs/yjs/main/LICENSE]` | YATA CRDT shared types; large provider ecosystem; docs describe server-side sync `[VERIFIED https://docs.yjs.dev]` | Shared types (text/map/array) | No | Typically a sync server/provider | Huge ecosystem, but no offline mesh and no E2EE |
| **Loro** | MIT `[VERIFIED https://api.github.com/repos/loro-dev/loro]` | Rust JSON CRDT with movable list/rich text and version control; WASM bindings | JSON / rich text | No | No | Newer engine; same transport/identity gap |
| **diamond-types** | **None found** — no `LICENSE` at repo root; GitHub licence field `null` `[VERIFIED https://api.github.com/repos/josephg/diamond-types]` | "The world's fastest CRDT. WIP." — research-grade list CRDT | List/oplog | No | No | Not reusable (no licence); not a product |
| **cr-sqlite** | MIT `[VERIFIED https://api.github.com/repos/vlcn-io/cr-sqlite]` | SQLite extension adding multi-writer CRDT tables; sync over application transport | Relational tables | No | Optional sync service | Attractive for forms, but no E2EE, no mesh, no DTN |
| **SecSync** | Apache-2.0 `[VERIFIED https://github.com/nikgraf/secsync]` | Protocol + Yjs reference implementation for E2EE CRDT exchange using snapshots and operation logs; NLnet NGI Assure 2021–2024 `[VERIFIED https://nlnet.nl/project/Naisho/]` | Yjs documents, encrypted | **Yes** | Yes — snapshot/op exchange endpoint | Closest prior art to MeshDoc's crypto model; server-mediated, not mesh/DTN |
| **Keyhive** | Apache-2.0 `[VERIFIED https://api.github.com/repos/inkandswitch/keyhive]` | "Synchronization engine for end-to-end encrypted group collaboration"; edge names, invites, group key agreement; NLnet NGI Zero Core 2024–2026 `[VERIFIED https://nlnet.nl/project/Keyhive/]` | Documents + group key state | **Yes** | Designed for P2P/federated/central | Best future source for MLS-grade workspace keys; not a field toolkit |
| **Earthstar** | LGPL-3.0 `[VERIFIED https://api.github.com/repos/earthstar-project/earthstar]` | "Storage for private, distributed, offline-first applications"; P2P sync; NLnet encryption/safety work `[VERIFIED https://nlnet.nl/project/EarthstarEncryption/]` | Documents in shares | Encryption added by funded project | No | Adjacent, but not structured humanitarian types |

### 2.2 Mesh / off-grid transport and apps

| Project | Licence (evidence) | What it does / how data moves | Data model | E2EE | Server required | Gap vs MeshDoc |
|---|---|---|---|---|---|---|
| **Meshtastic** | GPL-3.0 firmware and Android `[VERIFIED https://api.github.com/repos/meshtastic/firmware]` `[VERIFIED https://api.github.com/repos/meshtastic/Meshtastic-Android]` | LoRa mesh; "text messages and position reports"; channels are shared-key encrypted groups, up to 8 channels, default public key `[VERIFIED https://meshtastic.org/docs/overview/]` | Messages, position | Channel PSK (shared), not per-author E2EE | No | Excellent radio layer; no documents, no CRDT, low bandwidth |
| **Briar** | GPL-3.0-or-later `[VERIFIED https://raw.githubusercontent.com/briar/briar/master/LICENSE.txt]` | P2P messaging over Bluetooth/Wi-Fi/Tor/USB, E2EE, Briar Mailbox store-and-forward `[VERIFIED https://briarproject.org/how-it-works/]` | Messages, forums, blogs | **Yes** | No | The closest philosophical neighbour; documents are a *future* roadmap item `[VERIFIED https://en.wikipedia.org/wiki/Briar_(software)]` |
| **qaul** | AGPL-3.0 `[VERIFIED https://api.github.com/repos/qaul/qaul.net]` | "Internet independent wireless mesh communication app"; NLnet-funded delay-tolerant mesh messenger `[VERIFIED https://nlnet.nl/project/P2P-channels/]` | Messages, channels | Claimed privacy-preserving `[VERIFIED https://nlnet.nl/project/P2P-channels/]` | No | Messenger, not documents; AGPL limits embedding |
| **Irdest** | `[UNCERTAIN]` — Gitea host unreachable from our network; no licence confirmed | Rust mesh stack: "wireless mesh networks over Bluetooth and direct WiFi connections"; "direct circuits … end-to-end encrypted"; NLnet 2021–2022 and BLE work 2023–2026 `[VERIFIED https://nlnet.nl/project/Irdest/]` `[VERIFIED https://nlnet.nl/project/Irdest-OpenWRT-BLE/]` | Network/routing primitives | **Yes** (circuit-level) | No | Closest BLE-mesh codebase; no documents, no CRDT payload |
| **Reticulum** | Custom "Reticulum License" (MIT-like + no-harm + no-AI-training clauses; not OSI) `[VERIFIED https://raw.githubusercontent.com/markqvist/Reticulum/master/LICENSE]` | Cryptography-based networking stack over LoRa, packet radio, Wi-Fi `[VERIFIED https://api.github.com/repos/markqvist/Reticulum]` | Packets/links | Yes, link-level | No | Transport only; licence restricts reuse and AI training; no collaboration layer |
| **Serval** | GPL-2.0 `[VERIFIED https://raw.githubusercontent.com/servalproject/serval-dna/master/GPL-2.0.txt]` | Mesh telephony plus **Rhizome** store-and-forward for messages/data `[VERIFIED https://en.wikipedia.org/wiki/Serval_Project]`; repository last pushed 2022 `[VERIFIED https://api.github.com/repos/servalproject/serval-dna]` | Voice, SMS, Rhizome files | Historically mesh-encrypted `[UNCERTAIN]` | No | Dormant; file sync but no CRDT merge semantics |
| **Bridgefy** | Proprietary SDK `[VERIFIED https://en.wikipedia.org/wiki/Bridgefy]` | BLE mesh SDK licensed to apps; adopted libsignal but "researchers have demonstrated that Bridgefy's usage of the Signal Protocol is insecure" `[VERIFIED https://en.wikipedia.org/wiki/Bridgefy]`; USENIX Security 2022 paper "Breaking Bridgefy, again" `[VERIFIED https://www.usenix.org/conference/usenixsecurity22/presentation/albrecht]` | Messages | Claimed, broken in research | No | Closed source, security history — a cautionary tale, not a dependency |
| **FireChat** | Proprietary (Open Garden); discontinued, no updates since 2018 `[VERIFIED https://en.wikipedia.org/wiki/FireChat]` | Bluetooth/Wi-Fi/Multipeer mesh messaging | Messages | `[UNCERTAIN]` | No | Dead; proves demand but not a viable prior-art dependency |
| **Manyverse** | MPL-2.0 `[VERIFIED https://gitlab.com/staltz/manyverse/-/raw/master/package.json]` | SSB-based social network; offline reads/writes; syncs "through a shared local Wi-Fi or on the internet" `[VERIFIED https://manyver.se/]` | Append-only SSB feeds | Feed encryption, not group docs `[UNCERTAIN]` | No | Social feed, not structured documents |
| **Berty** | Apache-2.0 OR MIT (both licence files present) `[VERIFIED https://api.github.com/repos/berty/berty/contents]` | Wesh mesh-network protocol + messenger `[VERIFIED https://berty.tech/]` | Messages | **Yes** (claimed) | No | Mesh messaging; no document types |
| **SimpleX** | AGPL-3.0 `[VERIFIED https://api.github.com/repos/simplex-chat/simplex-chat]` | "The only messaging network without any user identifiers"; SMP relay servers `[VERIFIED https://simplex.chat/]` | Messages | **Yes** | **Yes** (relays) | Privacy-first but server-mediated; no offline mesh |
| **Signal** | AGPL-3.0-only clients/server `[VERIFIED https://en.wikipedia.org/wiki/Signal_(software)]`; libsignal AGPL-3.0 `[VERIFIED https://api.github.com/repos/signalapp/libsignal]` | Centralized E2EE messaging `[VERIFIED https://en.wikipedia.org/wiki/Signal_(software)]` | Messages | **Yes** | **Yes** | Not offline, not accountless, AGPL library cannot be linked into permissive code |
| **Matrix / Element** | Element Web AGPL-3.0 `[VERIFIED https://api.github.com/repos/element-hq/element-web]`; Synapse AGPL-3.0 `[VERIFIED https://api.github.com/repos/element-hq/synapse]` | Federated client-server real-time comms over HTTP APIs `[VERIFIED https://en.wikipedia.org/wiki/Matrix_(protocol)]` | Rooms/events | Olm/Megolm E2EE | **Yes** (homeserver) | Server-dependent by design; cannot operate on a bare mesh |

### 2.3 Humanitarian / disaster-response data

| Project | Licence (evidence) | What it does / how data moves | Data model | E2EE | Server required | Gap vs MeshDoc |
|---|---|---|---|---|---|---|
| **Ushahidi** | AGPL-3.0-or-later `[VERIFIED https://raw.githubusercontent.com/ushahidi/platform/main/LICENSE.md]` | Crowdsourced crisis/community reporting platform `[VERIFIED https://www.ushahidi.com/]` | Reports, posts | No | **Yes** | Web platform; no P2P merge, no E2EE |
| **HOT OSM Tasking Manager** | BSD-2-Clause `[VERIFIED https://api.github.com/repos/hotosm/tasking-manager]` | Coordinates humanitarian mapping in OpenStreetMap `[VERIFIED https://www.hotosm.org/]` | OSM map data | N/A | **Yes** | Mapping coordination, not field data collection/comms |
| **KoboToolbox** | `kpi` AGPL-3.0 `[VERIFIED https://api.github.com/repos/kobotoolbox/kpi]` | Server for ODK-style form collection `[VERIFIED https://github.com/kobotoolbox/kpi]` | Forms, submissions | No | **Yes** | Server-authoritative submissions, no CRDT, no mesh |
| **ODK** | Collect Apache-2.0 `[VERIFIED https://raw.githubusercontent.com/getodk/collect/master/LICENSE.md]`; Central Apache-2.0 `[VERIFIED https://api.github.com/repos/getodk/central]` | Android form filling + central server for submissions `[VERIFIED https://github.com/getodk/collect]` `[VERIFIED https://github.com/getodk/central]` | Forms, submissions | No | **Yes** (Central) | Offline capture, not offline convergence; no E2EE |
| **DHIS2** | BSD-3-Clause `[VERIFIED https://api.github.com/repos/dhis2/dhis2-core]` | National health information platform; capture "online and offline" `[VERIFIED https://dhis2.org/]` | Aggregate/event data | No | **Yes** | Health MIS, not peer-to-peer collaboration |
| **ATAK-CIV / TAK Server** | GPL-3.0 `[VERIFIED https://raw.githubusercontent.com/TAK-Product-Center/atak-civ/main/LICENSE.md]` `[VERIFIED https://raw.githubusercontent.com/TAK-Product-Center/Server/main/LICENSE.md]` | US Government geospatial/situational-awareness app with plugin architecture `[VERIFIED https://github.com/TAK-Product-Center/atak-civ]`; TAK Server is the backend | CoT messages, map overlays | Transport security `[UNCERTAIN]` | **Yes** (server for sharing) | Military SA tool; CoT messaging, not CRDT documents |
| **Sahana Eden** | MIT (archived `eden-legacy` repo) `[VERIFIED https://raw.githubusercontent.com/sahana/eden-legacy/master/LICENSE]` | Humanitarian management web platform for disaster/development `[VERIFIED https://github.com/sahana/eden-legacy]` | Web records | No | **Yes** | Archived; server web app; no offline mesh |

### 2.4 Delay-tolerant networking (DTN) standards and FOSS implementations

| Project | Licence (evidence) | What it does | What it does not do | Relation to MeshDoc |
|---|---|---|---|---|
| **RFC 4838** (DTN architecture) | IETF Informational, April 2007 `[VERIFIED https://www.rfc-editor.org/rfc/rfc4838.txt]` | Defines the DTN architecture and rationale | Not a wire format | Vocabulary/source for the relay design |
| **RFC 5050** (Bundle Protocol v6) | IETF Experimental, November 2007 `[VERIFIED https://www.rfc-editor.org/rfc/rfc5050.txt]` | First Bundle Protocol specification | Superseded by BPv7 | Historical context only |
| **RFC 9171** (Bundle Protocol v7) | IETF Standards Track, January 2022 `[VERIFIED https://www.rfc-editor.org/rfc/rfc9171.txt]` | Current bundle format, custody/status reporting | No CRDT/profile for documents | MeshDoc relay can be described as a *bundle-profile-like* store-and-forward layer; interop is a design option |
| **IETF DTN WG** | Active WG; published BPv7, BPSec, TCPCL; "multiple independent implementations exist … in both space and terrestrial environments" `[VERIFIED https://datatracker.ietf.org/api/v1/group/group/?acronym=dtn]` | Standardisation home | Does not define collaborative-document semantics | Natural standards venue for an upstream profile draft |
| **ION** (NASA JPL) | REUSE-style per-file licences: Apache-2.0, BSD-2-Clause, BSD-3-Clause, MIT, CC-BY-3.0 `[VERIFIED https://api.github.com/repos/nasa-jpl/ION-DTN/contents/LICENSES]` | NASA's BPv7 implementation `[VERIFIED https://api.github.com/repos/nasa-jpl/ION-DTN]` | Heavy, spacecraft-oriented; no CRDT | Interop target for relay conformance |
| **µD3TN** | AGPL-3.0 `[VERIFIED https://gitlab.com/d3tn/ud3tn/-/raw/master/LICENSE]` | Lightweight DTN implementation `[VERIFIED https://gitlab.com/d3tn/ud3tn]` | No CRDT profile | Useful for testing, but AGPL limits reuse |
| **DTN7** | GPL-3.0 (`dtn7-go`) `[VERIFIED https://raw.githubusercontent.com/dtn7/dtn7-go/main/LICENSE]`; Rust port `dtn7-rs` has no root licence detected `[UNCERTAIN]` `[VERIFIED https://github.com/dtn7/dtn7-rs]` | BPv7 software suite | No CRDT profile | Interop/testing target |

### 2.5 Group E2EE standards and implementations (MLS)

| Project | Licence (evidence) | What it does | What it does not do | Relation to MeshDoc |
|---|---|---|---|---|
| **RFC 9420** (MLS) | IETF Standards Track, July 2023 `[VERIFIED https://www.rfc-editor.org/rfc/rfc9420.txt]` | "Efficient asynchronous group key establishment with forward secrecy (FS) and post-compromise security (PCS)" for groups `[VERIFIED https://www.rfc-editor.org/rfc/rfc9420.txt]` | Does not define a document model or transport | The stated end-state for MeshDoc workspace keys; workspace key is the start, not the end |
| **OpenMLS** | MIT `[VERIFIED https://api.github.com/repos/openmls/openmls]` | Rust MLS implementation `[VERIFIED https://openmls.tech]` | No p2p/offline epoch orchestration | Best candidate to implement the MLS upgrade path |
| **mls-rs** (AWS Labs) | Apache-2.0 `[VERIFIED https://api.github.com/repos/awslabs/mls-rs]` | Rust MLS implementation | Same | Alternative implementation; licence-compatible |
| **mlspp** (Cisco) | BSD-2-Clause `[VERIFIED https://api.github.com/repos/cisco/mlspp]` | C++ MLS implementation | Same | Reference/interop implementation |
| **p2panda MLS integration** | Project funded by NLnet to "realize MLS in a fully decentralised setting" `[VERIFIED https://nlnet.nl/project/P2Panda-groups/]` | Brings MLS into a p2p SDK | Not a field app | Direct prior art for the "MLS over p2p" problem MeshDoc will face in phase 2 |

### 2.6 On-device translation (optional/future phase)

| Project | Licence (evidence) | What it does | What it does not do | Relation to MeshDoc |
|---|---|---|---|---|
| **Firefox Translations** | MPL-2.0; repository archived 2023 `[VERIFIED https://api.github.com/repos/mozilla/firefox-translations]` | Browser extension for client-side translation `[VERIFIED https://github.com/mozilla/firefox-translations]` | Not an embeddable library; archived | Prior art for on-device translation UX |
| **Bergamot** | MPL-2.0 `[VERIFIED https://api.github.com/repos/browsermt/bergamot-translator]` | C++ on-device MT engine `[VERIFIED https://api.github.com/repos/browsermt/bergamot-translator]` | No mobile SDK; last push 2024 | Candidate engine for an offline translation phase |
| **Argos Translate** | MIT (repository licence) `[VERIFIED https://api.github.com/repos/argosopentech/argos-translate]` | Offline Python translation library; models derived from OPUS-MT `[VERIFIED https://www.argosopentech.com]` | Python-first; model quality varies | Fastest route to a phase-1 offline translation prototype |
| **NLLB-200** | Models **CC-BY-NC-4.0** (non-commercial) `[VERIFIED https://huggingface.co/api/models/facebook/nllb-200-distilled-600M]` | 200-language MT model family `[VERIFIED https://huggingface.co/facebook/nllb-200-distilled-600M]` | **Non-commercial licence**; large models | High quality but a licence trap for a deployed public-interest tool |
| **OPUS-MT** | Models CC-BY-4.0 `[VERIFIED https://huggingface.co/api/models/Helsinki-NLP/opus-mt-en-de]` | Many small bilingual/multilingual models `[VERIFIED https://huggingface.co/Helsinki-NLP/opus-mt-en-de]` | Lower quality than NLLB; many model pairs | **Licence-clean** default for a future offline translation phase |

---

## 3. Per-project notes (URL, licence, what it does, what it does not do, relationship to MeshDoc)

### 3.1 CRDT libraries and the local-first community

**Automerge** — https://automerge.org / https://github.com/automerge/automerge — **MIT** `[VERIFIED https://api.github.com/repos/automerge/automerge]`.
*Does:* JSON-like CRDT with a local-first sync engine that works offline, queues changes and syncs on
reconnect; Rust core with JS/WASM bindings; large community (≈6.7k stars, actively pushed)
`[VERIFIED https://automerge.org/]`.
*Does not do:* no encryption, no device identity, no per-change authorship signature, no mesh
transport. Sync is peer/sync-server shaped, not DTN-shaped `[VERIFIED https://automerge.org/]`.
*MeshDoc relation:* the most likely CRDT engine for the document layer if MeshDoc does not
implement its own; MeshDoc adds the encryption/signature envelope and transport. Upstream
contribution: schema-migration patterns and a partition fuzzing harness (see §6).

**Yjs** — https://github.com/yjs/yjs — **MIT** `[VERIFIED https://raw.githubusercontent.com/yjs/yjs/main/LICENSE]`.
*Does:* YATA-based shared types with the largest provider ecosystem in local-first software; docs
describe server-side sync setup `[VERIFIED https://docs.yjs.dev]`.
*Does not do:* no encryption or author signatures; transport/persistence is delegated to providers.
*MeshDoc relation:* prior art and ecosystem benchmark. MeshDoc is not a JS-first application, so
Yjs is less likely as the core engine, but Yjs compatibility would be a cheap adoption win if a
web client is ever added.

**Loro** — https://loro.dev / https://github.com/loro-dev/loro — **MIT** `[VERIFIED https://api.github.com/repos/loro-dev/loro]`.
*Does:* Rust CRDT with movable lists, rich text, version control and WASM bindings
`[VERIFIED https://github.com/loro-dev/loro]`.
*Does not do:* same security/transport gap as Automerge/Yjs.
*MeshDoc relation:* viable alternative core engine; if MeshDoc defines an engine-agnostic diff
envelope, supporting Loro becomes a feature, not a rewrite.

**diamond-types** — https://github.com/josephg/diamond-types — **no licence file at repository
root; GitHub licence field is `null`** `[VERIFIED https://api.github.com/repos/josephg/diamond-types]`.
*Does:* research-grade "world's fastest CRDT. WIP." — a list/oplog CRDT with strong benchmark work.
*Does not do:* no licence grant, no product packaging, no transport/security.
*MeshDoc relation:* read-only inspiration; **do not copy code** — without a licence there is no
permission to reuse. Mention in related work only.

**cr-sqlite (Vlcn)** — https://github.com/vlcn-io/cr-sqlite — **MIT** `[VERIFIED https://api.github.com/repos/vlcn-io/cr-sqlite]`.
*Does:* SQLite extension that turns tables into convergent replicated relations; multi-writer CRDT
tables; useful when the document model is tabular (supply forms).
*Does not do:* no E2EE, no mesh transport, no identity/signature; sync is over an application-chosen
transport `[VERIFIED https://github.com/vlcn-io/cr-sqlite]`.
*MeshDoc relation:* a credible alternative for the "supply form" type; MeshDoc could provide the
secure transport that cr-sqlite lacks.

**Local-first community** — https://localfirstweb.dev/ `[VERIFIED https://localfirstweb.dev/]`;
foundational essay: "Local-First Software: You Own Your Data, in spite of the Cloud", Kleppmann &
Wiggins, September 2019 `[VERIFIED https://www.inkandswitch.com/local-first/static/local-first.pdf]`.
*Does:* defines the seven ideals (offline-first, multi-device, collaboration, long-term data
ownership, etc.) and hosts a directory/community.
*Does not do:* not a codebase.
*MeshDoc relation:* the proposal should position MeshDoc as local-first for the *no-cloud-at-all*
case; the essay's ideals are the vocabulary reviewers expect. Cite the essay once, not repeatedly.

**SecSync** — https://www.secsync.com / https://github.com/nikgraf/secsync — **Apache-2.0**
`[VERIFIED https://github.com/nikgraf/secsync]`; NLnet NGI Assure 2021–2024
`[VERIFIED https://nlnet.nl/project/Naisho/]`.
*Does:* protocol and Yjs reference implementation for E2EE CRDT exchange using encrypted snapshots
and operation logs; explicitly created because "there is no plug & play implementation serving
end-to-end encrypted systems" `[VERIFIED https://nlnet.nl/project/Naisho/]`.
*Does not do:* server-mediated exchange; no DTN/mesh transport; no device-to-device epidemic sync.
*MeshDoc relation:* **the single closest prior art for the crypto model** and the best citation for
"the gap is real". MeshDoc differs by removing the server and making each change independently
verifiable. Cross-reference and reach out (§5).

**Keyhive (Ink & Switch)** — https://github.com/inkandswitch/keyhive — **Apache-2.0**
`[VERIFIED https://api.github.com/repos/inkandswitch/keyhive]`; NLnet NGI Zero Core 2024–2026
`[VERIFIED https://nlnet.nl/project/Keyhive/]`.
*Does:* "synchronization engine for end-to-end encrypted group collaboration", edge names, invites,
group key agreement; designed for P2P/federated/central deployments and millions of documents
`[VERIFIED https://nlnet.nl/project/Keyhive/]`.
*Does not do:* not a field-data toolkit, not a transport, not a relay.
*MeshDoc relation:* the natural **phase-2 replacement for the QR workspace key** (MLS-grade group
key management without a central server). Proposal should name Keyhive as the collaboration target
and offer to test MeshDoc's offline/DTN assumptions against it.

**Earthstar** — https://github.com/earthstar-project/earthstar — **LGPL-3.0**
`[VERIFIED https://api.github.com/repos/earthstar-project/earthstar]`; NLnet-funded encryption and
local-sync work `[VERIFIED https://nlnet.nl/project/EarthstarEncryption/]`.
*Does:* offline-first storage/sync for private distributed apps.
*Does not do:* not structured humanitarian types; LGPL complicates static linking into a permissive
stack `[UNCERTAIN — linking analysis is legal advice, not verified here]`.
*MeshDoc relation:* adjacent prior art; cite as evidence that "encrypted local-first sync" is an
active NLnet theme.

### 3.2 Mesh / off-grid communication

**Meshtastic** — https://meshtastic.org / https://github.com/meshtastic/firmware — **GPL-3.0**
`[VERIFIED https://api.github.com/repos/meshtastic/firmware]`; Android app **GPL-3.0**
`[VERIFIED https://api.github.com/repos/meshtastic/Meshtastic-Android]`.
*Does:* LoRa mesh carrying "text messages and position reports"; named encrypted channels with a
shared channel key; up to eight channels; default channel key is public (`AQ==`), so users must
change it `[VERIFIED https://meshtastic.org/docs/overview/]`.
*Does not do:* no documents, no CRDT, no bulk Wi-Fi Direct transfer; bandwidth is LoRa-class, not
file-class `[VERIFIED https://meshtastic.org/docs/overview/]`.
*MeshDoc relation:* complementary radio layer, not a competitor. A Meshtastic bridge (CoT/text) is
a plausible future adapter; MeshDoc should *not* claim LoRa parity. The existing Meshtastic ATAK
plugin (GPL-3.0) `[VERIFIED https://github.com/meshtastic/ATAK-Plugin]` shows the plugin pattern.

**Briar** — https://briarproject.org / https://github.com/briar/briar — **GPL-3.0-or-later**
`[VERIFIED https://raw.githubusercontent.com/briar/briar/master/LICENSE.txt]`; NLnet-funded
"secure messaging app with offline capabilities" (2019) and Briar Desktop (2022)
`[VERIFIED https://nlnet.nl/project/Briar/]` `[VERIFIED https://nlnet.nl/project/Briar-beyond-Android/]`.
*Does:* P2P messaging over Bluetooth, Wi-Fi, Tor or memory cards; E2EE; Briar Mailbox for
store-and-forward between users online at different times `[VERIFIED https://briarproject.org/how-it-works/]`.
*Does not do:* no shared documents or structured records today; its own roadmap lists
"collaborative document editing" as long-term `[VERIFIED https://en.wikipedia.org/wiki/Briar_(software)]`.
*MeshDoc relation:* the most important cross-reference in the whole landscape — same values, same
transport family, adjacent gap. The proposal should cite Briar's roadmap line as external evidence
that document collaboration over mesh is unmet, and offer interoperability experiments (e.g. same
BLE/Wi-Fi Direct behaviour) rather than claiming novelty over Briar.

**qaul** — https://qaul.net / https://github.com/qaul/qaul.net — **AGPL-3.0**
`[VERIFIED https://api.github.com/repos/qaul/qaul.net]`; NLnet NGI0 Commons Fund, started 2025
`[VERIFIED https://nlnet.nl/project/P2P-channels/]`.
*Does:* "privacy-preserving, internet-independent, off-the-grid, delay-tolerant P2P mesh messenger";
configurable verifiable channels for open/trusted/spam-protected communication
`[VERIFIED https://nlnet.nl/project/P2P-channels/]`.
*Does not do:* messenger semantics, not documents; AGPL-3.0 limits embedding in permissive tools.
*MeshDoc relation:* the closest *delay-tolerant mesh messenger*. Cross-reference for
anti-entropy/queueing behaviour; consider borrowing test scenarios rather than code.

**Irdest** — https://irde.st (site unreachable from our network on 2026-11-02) /
https://git.irde.st/we/irdest — **licence `[UNCERTAIN]`** (Gitea host timed out; no licence
confirmed). NLnet NGI0 Discovery 2021–2022 `[VERIFIED https://nlnet.nl/project/Irdest/]` and NGI0
Entrust 2023–2026 for "Bluetooth LE connections" `[VERIFIED https://nlnet.nl/project/Irdest-OpenWRT-BLE/]`.
*Does:* "wireless mesh networks over Bluetooth and direct WiFi connections"; "direct circuits in a
Irdest network are end-to-end encrypted" `[VERIFIED https://nlnet.nl/project/Irdest/]`; route
scoring work funded 2023–2026 `[VERIFIED https://nlnet.nl/project/Irdest-Spec/]`.
*Does not do:* no document layer, no field app.
*MeshDoc relation:* the closest **BLE-mesh engineering** neighbour. Cross-reference the BLE
connection work; a shared BLE transport abstraction is a plausible joint upstream contribution.

**Reticulum** — https://reticulum.network / https://github.com/markqvist/Reticulum — **custom
"Reticulum License"** (MIT-like grant plus a no-harm clause and a prohibition on use in AI/ML
training data) `[VERIFIED https://raw.githubusercontent.com/markqvist/Reticulum/master/LICENSE]`.
*Does:* "cryptography-based networking stack for building unstoppable networks with LoRa, Packet
Radio, WiFi" `[VERIFIED https://api.github.com/repos/markqvist/Reticulum]`.
*Does not do:* no collaboration/document layer; the licence is **not OSI-approved**, so it is not a
safe dependency for a permissively licensed toolkit `[VERIFIED https://raw.githubusercontent.com/markqvist/Reticulum/master/LICENSE]`.
*MeshDoc relation:* cite as transport prior art; design for optional interop but avoid code reuse
unless the licence question is resolved. Good example to show reviewers that MeshDoc checked
licence compatibility.

**Serval Project** — https://servalproject.org (site timed out on 2026-11-02 `[UNCERTAIN]`) /
https://github.com/servalproject/serval-dna — **GPL-2.0**
`[VERIFIED https://raw.githubusercontent.com/servalproject/serval-dna/master/GPL-2.0.txt]`; last
repository push June 2022 `[VERIFIED https://api.github.com/repos/servalproject/serval-dna]`.
*Does:* mesh telephony plus **Rhizome**, a store-and-forward system for messages and data allowing
communication "without a stable live mesh connection" `[VERIFIED https://en.wikipedia.org/wiki/Serval_Project]`.
*Does not do:* dormant; no CRDT merge; no modern Android support `[UNCERTAIN]`.
*MeshDoc relation:* Rhizome is the closest ancestor of MeshDoc's relay idea — cite it honestly as
prior art and explain that MeshDoc adds CRDT convergence and change-level E2EE.

**Bridgefy** — https://bridgefy.me — **proprietary SDK** `[VERIFIED https://en.wikipedia.org/wiki/Bridgefy]`.
*Does:* BLE mesh SDK licensed to app developers; adopted the Signal protocol in 2020
`[VERIFIED https://en.wikipedia.org/wiki/Bridgefy]`.
*Does not do:* not open source; security research found the Signal adoption insufficient — USENIX
Security 2022, "Breaking Bridgefy, again: Adopting libsignal is not enough"
`[VERIFIED https://www.usenix.org/conference/usenixsecurity22/presentation/albrecht]`.
*MeshDoc relation:* cautionary prior art for the threat model: a mesh SDK with a good crypto
library can still be broken by protocol design. Use it to justify MeshDoc's per-change signature
and open review.

**FireChat** — no live site; discontinued, apps "have not been updated since 2018"
`[VERIFIED https://en.wikipedia.org/wiki/FireChat]`.
*Does:* historically, Bluetooth/Wi-Fi/Multipeer mesh messaging from Open Garden.
*Does not do:* anything today; proprietary; dead `[VERIFIED https://en.wikipedia.org/wiki/FireChat]`.
*MeshDoc relation:* evidence of demand and of the sustainability risk of closed mesh apps — a
strong argument for the library-first, open approach.

**Manyverse** — https://manyver.se / https://gitlab.com/staltz/manyverse — **MPL-2.0**
`[VERIFIED https://gitlab.com/staltz/manyverse/-/raw/master/package.json]`.
*Does:* SSB-based P2P social network; data lives on the phone; syncs "through a shared local Wi-Fi
or on the internet" `[VERIFIED https://manyver.se/]`.
*Does not do:* social feed semantics; no structured documents; append-only log rather than a
mergeable document CRDT `[UNCERTAIN — SSB is log-based, but Manyverse may layer additional merge logic]`.
*MeshDoc relation:* proves offline-first social sync is deployable; different data model.

**Berty** — https://berty.tech / https://github.com/berty/berty — **Apache-2.0 OR MIT** (both
licence files present) `[VERIFIED https://api.github.com/repos/berty/berty/contents]`.
*Does:* Wesh Network, "an open source, wild & asynchronous mesh network protocol", plus the Berty
messenger built on it `[VERIFIED https://berty.tech/]`.
*Does not do:* messaging, not documents.
*MeshDoc relation:* permissively licensed mesh-messaging peer; a candidate interop/collaboration
contact for transport-level work.

**SimpleX** — https://simplex.chat / https://github.com/simplex-chat/simplex-chat — **AGPL-3.0**
`[VERIFIED https://api.github.com/repos/simplex-chat/simplex-chat]`.
*Does:* "the only messaging network without any user identifiers"; all messages look like random
noise to servers; SMP relay servers `[VERIFIED https://simplex.chat/]`.
*Does not do:* server-relayed; not a mesh; no documents.
*MeshDoc relation:* best-in-class privacy onboarding, but opposite architecture. Cite for the
identity discussion: MeshDoc agrees on no accounts, disagrees on "no offline operation".

**Signal** — https://signal.org / https://github.com/signalapp/Signal-Android — **AGPL-3.0**
`[VERIFIED https://api.github.com/repos/signalapp/Signal-Android]`; protocol library **AGPL-3.0**
`[VERIFIED https://api.github.com/repos/signalapp/libsignal]`.
*Does:* centralized E2EE messaging with strong metadata protection `[VERIFIED https://en.wikipedia.org/wiki/Signal_(software)]`.
*Does not do:* no offline mesh; centralized architecture; registration is tied to a phone number
`[VERIFIED https://en.wikipedia.org/wiki/Signal_(software)]`.
*MeshDoc relation:* "why not Signal?" answer: (a) it needs connectivity and a central service;
(b) its protocol library is AGPL-3.0, so a permissive MeshDoc cannot link it; (c) the group model is
not a document CRDT. This should be stated plainly in the proposal — reviewers will ask.

**Element / Matrix** — https://element.io / https://github.com/element-hq/synapse — **AGPL-3.0**
(Synapse and Element Web) `[VERIFIED https://api.github.com/repos/element-hq/synapse]`
`[VERIFIED https://api.github.com/repos/element-hq/element-web]`.
*Does:* federated real-time communication over HTTP APIs; E2EE for rooms (Olm/Megolm)
`[VERIFIED https://en.wikipedia.org/wiki/Matrix_(protocol)]`.
*Does not do:* requires a homeserver; not designed for infrastructure-free operation.
*MeshDoc relation:* "why not Matrix?" — a homeserver is exactly the dependency MeshDoc removes. A
Matrix bridge is a future integration, not a competitor.

### 3.3 Disaster-response / humanitarian data

**Ushahidi** — https://www.ushahidi.com / https://github.com/ushahidi/platform — **AGPL-3.0-or-later**
`[VERIFIED https://raw.githubusercontent.com/ushahidi/platform/main/LICENSE.md]`.
*Does:* crowdsourced crisis/community reporting; deployable platform for citizen-generated data
`[VERIFIED https://www.ushahidi.com/]`.
*Does not do:* server-hosted web platform; no P2P sync; no E2EE `[VERIFIED https://github.com/ushahidi/platform]`.
*MeshDoc relation:* the canonical "crowdmap" — good front-end/reporting complement; MeshDoc could
feed it when connectivity exists.

**HOT OSM** — https://www.hotosm.org / https://github.com/hotosm/tasking-manager — **BSD-2-Clause**
`[VERIFIED https://api.github.com/repos/hotosm/tasking-manager]`.
*Does:* organises humanitarian mapping into OpenStreetMap tasks `[VERIFIED https://www.hotosm.org/]`.
*Does not do:* mapping coordination, not field data collection or comms.
*MeshDoc relation:* a geo-point type could export to OSM-compatible formats; HOT is a distribution
partner/audience, not a competitor.

**KoboToolbox** — https://www.kobotoolbox.org / https://github.com/kobotoolbox/kpi — **AGPL-3.0**
`[VERIFIED https://api.github.com/repos/kobotoolbox/kpi]`.
*Does:* server for KoBo/ODK-style form collection and data management
`[VERIFIED https://github.com/kobotoolbox/kpi]`.
*Does not do:* server-authoritative submissions; no CRDT; no E2EE; no mesh
`[VERIFIED https://github.com/kobotoolbox/kpi]`.
*MeshDoc relation:* **the "why not KoBoToolbox?" answer.** KoBo assumes a server and treats data as
submissions to be collected. MeshDoc assumes no server and treats data as shared objects that
converge. They are complements: MeshDoc can sync into KoBo when a link appears. The proposal should
say this explicitly and avoid implying KoBo is deficient — it is excellent at what it targets.

**ODK** — https://getodk.org / https://github.com/getodk/collect — **Apache-2.0** (Collect and
Central) `[VERIFIED https://raw.githubusercontent.com/getodk/collect/master/LICENSE.md]`
`[VERIFIED https://api.github.com/repos/getodk/central]`; ODK is "used to collect billions of data
points in challenging environments" `[VERIFIED https://github.com/getodk/collect]`.
*Does:* Android form filling (Collect) + server for submissions (Central).
*Does not do:* no CRDT convergence between devices; no E2EE; no mesh transport.
*MeshDoc relation:* same complement/contrast as KoBo; ODK's Apache-2.0 licence means its form
definitions (XForms) could be imported/exported by MeshDoc — a concrete interop win.

**DHIS2** — https://dhis2.org / https://github.com/dhis2/dhis2-core — **BSD-3-Clause**
`[VERIFIED https://api.github.com/repos/dhis2/dhis2-core]`.
*Does:* national health information system; capture "anywhere, online and offline"; analytics
`[VERIFIED https://dhis2.org/]`.
*Does not do:* server-centric national instance; not peer collaboration.
*MeshDoc relation:* the upstream health-system target for a "remote health worker" use case; a
DHIS2 export adapter is a plausible post-grant integration.

**ATAK / WinTAK / TAK Server** — https://github.com/TAK-Product-Center/atak-civ — **GPL-3.0**
`[VERIFIED https://raw.githubusercontent.com/TAK-Product-Center/atak-civ/main/LICENSE.md]`;
TAK Server **GPL-3.0** `[VERIFIED https://raw.githubusercontent.com/TAK-Product-Center/Server/main/LICENSE.md]`.
*Does:* US Government geospatial-temporal and situational-awareness app with a plugin architecture
`[VERIFIED https://github.com/TAK-Product-Center/atak-civ]`; ATAK is "an Android smartphone
geospatial infrastructure and military situation awareness app" `[VERIFIED https://en.wikipedia.org/wiki/Android_Tactical_Assault_Kit]`.
**WinTAK** is the Windows variant; we found no public source repository for it `[UNCERTAIN]`.
*Does not do:* CoT message/overlay sharing, not CRDT documents; server needed for wide-area sharing;
military provenance and GPL-3.0 limit civilian embedding.
*MeshDoc relation:* shows the value of an open plugin ecosystem in disaster software, and a
contrast: TAK's situational awareness vs MeshDoc's shared records. The Meshtastic ATAK plugin
(GPL-3.0) `[VERIFIED https://github.com/meshtastic/ATAK-Plugin]` is a useful bridge precedent.

**Sahana Eden** — https://github.com/sahana/eden-legacy — **MIT**
`[VERIFIED https://raw.githubusercontent.com/sahana/eden-legacy/master/LICENSE]`; the maintained
repository is archived `[VERIFIED https://api.github.com/repos/sahana/eden-legacy]`.
*Does:* humanitarian management platform covering disaster/development/environment workflows
`[VERIFIED https://github.com/sahana/eden-legacy]`.
*Does not do:* server web app; archived; no offline mesh sync.
*MeshDoc relation:* another example that humanitarian software is server/web-shaped; its domain
model (assessments, supplies) is a good source of document-type requirements.

### 3.4 Delay-tolerant networking standards and implementations

**RFC 4838** — https://www.rfc-editor.org/rfc/rfc4838.txt — IETF Informational, April 2007
`[VERIFIED https://www.rfc-editor.org/rfc/rfc4838.txt]`. Defines DTN architecture: store-and-forward,
custody, naming. *MeshDoc relation:* the intellectual ancestor of the relay; cite for terminology.

**RFC 5050** — https://www.rfc-editor.org/rfc/rfc5050.txt — IETF Experimental, November 2007
`[VERIFIED https://www.rfc-editor.org/rfc/rfc5050.txt]`. Bundle Protocol v6; superseded by BPv7.
*MeshDoc relation:* historical only; do not implement.

**RFC 9171 (BPv7)** — https://www.rfc-editor.org/rfc/rfc9171.txt — IETF Standards Track, January 2022
`[VERIFIED https://www.rfc-editor.org/rfc/rfc9171.txt]`. Current Bundle Protocol. *MeshDoc relation:*
the relay should be *described as* a DTN-style store-and-forward service; whether it speaks BPv7 is
a design decision. Recommendation: do not implement BPv7 in the grant period (large surface,
custody/status reporting, convergence layers); instead define a minimal "encrypted CRDT bundle"
profile and, if resources allow, an ION/µD3TN interop demo. State this explicitly so reviewers do
not think the team is unaware of the standard.

**IETF DTN WG** — https://datatracker.ietf.org/wg/dtn/about/ — working group is active and reports
BPv7, BPSec and TCPCL published as Standards Track with "multiple independent implementations …
in both space and terrestrial environments" `[VERIFIED https://datatracker.ietf.org/api/v1/group/group/?acronym=dtn]`.
*MeshDoc relation:* the venue for an upstream "CRDT sync over BPv7" Internet-Draft in a later phase.

**ION** — https://github.com/nasa-jpl/ION-DTN — **REUSE-style per-file licences**: Apache-2.0,
BSD-2-Clause, BSD-3-Clause, MIT, CC-BY-3.0 `[VERIFIED https://api.github.com/repos/nasa-jpl/ION-DTN/contents/LICENSES]`.
*Does:* NASA JPL's DTN implementation `[VERIFIED https://api.github.com/repos/nasa-jpl/ION-DTN]`.
*Does not do:* no CRDT profile; heavy for Android.
*MeshDoc relation:* conformance/interop target if a BPv7 profile is ever published.

**µD3TN** — https://gitlab.com/d3tn/ud3tn — **AGPL-3.0**
`[VERIFIED https://gitlab.com/d3tn/ud3tn/-/raw/master/LICENSE]`.
*Does:* lightweight DTN implementation `[VERIFIED https://gitlab.com/d3tn/ud3tn]`.
*Does not do:* no CRDT profile; AGPL prevents reuse in permissive code.
*MeshDoc relation:* useful as a *test oracle* (run it beside the relay), not as a dependency.

**DTN7** — https://github.com/dtn7/dtn7-go — **GPL-3.0**
`[VERIFIED https://raw.githubusercontent.com/dtn7/dtn7-go/main/LICENSE]`; Rust port
https://github.com/dtn7/dtn7-rs has no root licence detected `[UNCERTAIN]`.
*Does:* BPv7 software suite `[VERIFIED https://github.com/dtn7/dtn7-go]`.
*MeshDoc relation:* same as µD3TN: interop testing, not reuse.

### 3.5 MLS — group E2EE

**RFC 9420** — https://www.rfc-editor.org/rfc/rfc9420.txt — IETF Standards Track, July 2023
`[VERIFIED https://www.rfc-editor.org/rfc/rfc9420.txt]`. Provides "efficient asynchronous group key
establishment with forward secrecy (FS) and post-compromise security (PCS)" `[VERIFIED https://www.rfc-editor.org/rfc/rfc9420.txt]`.
*MeshDoc relation:* the workspace symmetric key is a **deliberate phase-1 simplification**: it is
easy to share by QR, works offline, and has no group-state machine. It does **not** give forward
secrecy, post-compromise security, member removal, or per-member key rotation. MLS is the phase-2
answer. The proposal must say "workspace key is a starting point, not the end" — this document
provides the citations to support that sentence.

**OpenMLS** — https://openmls.tech / https://github.com/openmls/openmls — **MIT**
`[VERIFIED https://api.github.com/repos/openmls/openmls]`. Rust MLS implementation. *MeshDoc
relation:* preferred MLS implementation for the upgrade path; permissive licence, Rust-native.
The hard part is not the library but **epoch handling without a server** (commits over lossy mesh),
which is exactly what Keyhive and p2panda are funded to explore.

**mls-rs** — https://github.com/awslabs/mls-rs — **Apache-2.0**
`[VERIFIED https://api.github.com/repos/awslabs/mls-rs]`. AWS Labs Rust MLS implementation.
*MeshDoc relation:* alternative to OpenMLS; useful for cross-implementation interop tests.

**mlspp** — https://github.com/cisco/mlspp — **BSD-2-Clause**
`[VERIFIED https://api.github.com/repos/cisco/mlspp]`. Cisco C++ MLS implementation.
*MeshDoc relation:* reference implementation for conformance testing.

**p2panda MLS integration** — https://p2panda.org — funded by NLnet NGI0 Entrust to "integrate a
secure data encryption and fine-grained capability layer" and to "realize MLS in a fully
decentralised setting" `[VERIFIED https://nlnet.nl/project/P2Panda-groups/]`.
*MeshDoc relation:* the most direct prior art for "MLS without a server". Cross-reference and
coordinate; do not duplicate.

### 3.6 On-device translation (future/optional phase)

**Firefox Translations** — https://github.com/mozilla/firefox-translations — **MPL-2.0**; repository
archived in 2023 `[VERIFIED https://api.github.com/repos/mozilla/firefox-translations]`.
*Does:* browser extension for client-side translation `[VERIFIED https://github.com/mozilla/firefox-translations]`.
*Does not do:* archived, not an embeddable mobile library.
*MeshDoc relation:* proof that on-device translation is viable at browser scale; not a dependency.

**Bergamot** — https://github.com/browsermt/bergamot-translator — **MPL-2.0**
`[VERIFIED https://api.github.com/repos/browsermt/bergamot-translator]`.
*Does:* C++ on-device machine translation; last push 2024 `[VERIFIED https://api.github.com/repos/browsermt/bergamot-translator]`.
*Does not do:* no Android SDK; models need packaging.
*MeshDoc relation:* candidate engine if a translation phase is funded; MPL-2.0 is file-level
copyleft and compatible with an MIT/Apache core if kept as a separate module `[UNCERTAIN — legal
analysis not verified here]`.

**Argos Translate** — https://www.argosopentech.com / https://github.com/argosopentech/argos-translate
— **MIT** `[VERIFIED https://api.github.com/repos/argosopentech/argos-translate]`.
*Does:* "open-source offline translation library written in Python"; models derived from OPUS-MT
`[VERIFIED https://api.github.com/repos/argosopentech/argos-translate]`.
*Does not do:* Python-first; quality lower than NLLB.
*MeshDoc relation:* fastest prototype path; MIT code plus CC-BY-4.0 models is the licence-clean
combination.

**NLLB-200** — https://huggingface.co/facebook/nllb-200-distilled-600M — **CC-BY-NC-4.0**
(non-commercial) `[VERIFIED https://huggingface.co/api/models/facebook/nllb-200-distilled-600M]`.
*Does:* 200-language translation family `[VERIFIED https://huggingface.co/facebook/nllb-200-distilled-600M]`.
*Does not do:* the licence forbids commercial use; model size is large for low-end Android.
*MeshDoc relation:* **do not ship** without a licence decision; note it as a quality ceiling and
justify choosing OPUS-MT/Argos for a public-interest deployment.

**OPUS-MT** — https://huggingface.co/Helsinki-NLP/opus-mt-en-de — **CC-BY-4.0**
`[VERIFIED https://huggingface.co/api/models/Helsinki-NLP/opus-mt-en-de]`.
*Does:* many small bilingual models suitable for on-device use
`[VERIFIED https://huggingface.co/Helsinki-NLP/opus-mt-en-de]`.
*Does not do:* quality varies; language coverage is model-by-model.
*MeshDoc relation:* the licence-clean default for phase-3 translation.

---

## 4. NLnet-funded neighbours and cross-reference opportunities

### 4.1 How the scan was done

We parsed the complete NLnet project table at https://nlnet.nl/project/index.html (1,862 project rows
on 2026-11-02) and keyword-scanned it for: CRDT, local-first, offline, mesh, P2P, peer-to-peer,
delay-tolerant, DTN, Bundle Protocol, LoRa, Bluetooth/BLE, emergency, disaster, translator. We also
fetched the topic index at https://nlnet.nl/thema/ and read the individual project pages for the
closest matches. **Limitation:** the scan is English-keyword based; a project whose title/description
avoids our terms would be missed. Treat the list as "the closest projects we found", not "all
NLnet projects in the area" `[UNCERTAIN]`.

**Notable absence:** the keyword scan found **no NLnet project on Bundle Protocol / DTN / delay-
tolerant networking as such**, and no project combining humanitarian document workflows with
offline mesh sync `[UNCERTAIN — negative result of the scan above]`. The nearest emergency-related
projects are alerting, not collaboration: FOSS Warn `[VERIFIED https://nlnet.nl/project/FOSS-Warn/]`
and SMS cell-broadcast support for Linux `[VERIFIED https://nlnet.nl/project/SMS-CB/]`. The one
project that targeted "self-sustained community and emergency radio networking" (Radio-Meshnet) is
marked **archived — "the project as planned did not take place"**
`[VERIFIED https://nlnet.nl/project/Radio-Meshnet/]`. That is useful, careful evidence that the
*emergency-mesh* space is under-served rather than crowded — but do not overstate it; it may also
reflect difficulty of execution.

### 4.2 Closest NLnet-funded neighbours (ranked by overlap with MeshDoc)

| Rank | Project (fund, years) | URL | Why it is close | Concrete action for MeshDoc |
|---|---|---|---|---|
| 1 | **SecSync** (NGI Assure, 2021–2024) | https://nlnet.nl/project/Naisho/ | E2EE + CRDT; states the no-plug-and-play-E2EE gap | **Cite as closest prior art**; propose a mesh transport adapter for SecSync (Apache-2.0, compatible) and a joint write-up on "server-mediated vs DTN E2EE-CRDT" |
| 2 | **Keyhive** (NGI Zero Core, 2024–2026) | https://nlnet.nl/project/Keyhive/ | Serverless group key agreement for local-first data; the exact phase-2 problem MeshDoc's QR workspace key defers | **Name as the migration target** for workspace keys; offer to test Keyhive's group-key flow under DTN epoch loss; coordinate with Ink & Switch |
| 3 | **Irdest** (NGI0 Discovery 2021–2022; NGI0 Entrust 2023–2026) | https://nlnet.nl/project/Irdest/ , https://nlnet.nl/project/Irdest-OpenWRT-BLE/ | BLE + direct-Wi-Fi mesh with E2EE circuits — the closest transport peer | **Cross-reference BLE work**; propose a shared BLE transport/test crate; ask about licence (unknown) before any code reuse |
| 4 | **qaul** (NGI0 Commons Fund, from 2025) | https://nlnet.nl/project/P2P-channels/ | "off-the-grid, delay-tolerant P2P mesh messenger" — closest app-level DTN peer | **Cross-reference**; compare anti-entropy/queueing designs; avoid duplicating configurable-channel work |
| 5 | **p2panda group encryption** (NGI0 Entrust, 2023–2025; System Service 2025; Pillow 2026) | https://nlnet.nl/project/P2Panda-groups/ | Explicitly funding "realize MLS in a fully decentralised setting" | **Coordinate on MLS-over-p2p epoch handling**; share failure cases from high-latency meshes |
| 6 | **Offline Translator** (NGI Mobifree, 2025) | https://nlnet.nl/project/OfflineTranslator/ | On-device translation with open models — MeshDoc's optional phase | If phase 3 is funded, **contact for model packaging/UX**; otherwise cite as the state of the art and keep translation out of scope |
| 7 | **RTranslator 3.0** (NGI Mobifree, 2025–2026) | https://nlnet.nl/project/RTranslator/ | Real-time local spoken translation on Android | Cite as proof the on-device translation UX is being solved; MeshDoc should integrate rather than rebuild |
| 8 | **Interpeer** (NGI0 Discovery 2019–2022; SDK NGI Assure 2022–2024) | https://nlnet.nl/project/Interpeer/ , https://nlnet.nl/project/Interpeer-SDK/ | "Secure and efficient peer-to-peer networking stack"; near-real-time p2p sync | **Transport-level interop candidate**; compare its layering to MeshDoc's transport trait |
| 9 | **Meshpoint** (NGI0 Commons Fund, 2026) | https://nlnet.nl/project/Meshpoint/ | "Add Babel routing and automatic mesh formation" | Cite as mesh-routing prior art; MeshDoc's anti-entropy is complementary to routing |
| 10 | **PulzeLab C1** (NGI0 Commons Fund, 2026) | https://nlnet.nl/project/LoraMessaging/ | "Portable standalone LoRa messaging device" | Hardware bridge candidate; pairs with a Meshtastic/LoRa adapter, not with MeshDoc core |
| 11 | **Earthstar** (NGI Assure 2021–2022; encryption/sync 2022–2024) | https://nlnet.nl/project/Earthstar/ , https://nlnet.nl/project/EarthstarEncryption/ | Encrypted offline-first P2P storage — adjacent model | Cite in related work; useful evidence that "encrypted local-first" is an active NLnet theme |
| 12 | **Briar** (NGI0 PET 2019; Briar Desktop NGI Assure 2022) | https://nlnet.nl/project/Briar/ , https://nlnet.nl/project/Briar-beyond-Android/ | NLnet has already funded the closest mesh-messaging project | **Cite the funding lineage**; position MeshDoc as the document layer Briar's roadmap still lacks |
| 13 | **Yrs / Yrs Undo / Yrs Weak Links** (NGI Assure 2021, 2022–2024; NGI0 Entrust 2023–2026) | https://nlnet.nl/project/Yrs/ , https://nlnet.nl/project/Yrs-Undo/ , https://nlnet.nl/project/Yrs-WeakLinks/ | Rust CRDT engineering funded repeatedly | Cite as proof NLnet values CRDT infrastructure; potential upstream home for a Rust fuzzing harness |
| 14 | **json-joy / Peritext** (NGI Assure 2023–2024; NGI Zero Core 2023–2026) | https://nlnet.nl/project/JSON-Joy/ , https://nlnet.nl/project/JSON-Joy-Peritext/ | JSON CRDT + rich text | Related work for document types; not a transport |
| 15 | **m-ld** (NGI Assure 2021–2023; Sustainable web apps 2022–2024) | https://nlnet.nl/project/m-ld/ , https://nlnet.nl/project/SustainableWebApps/ | Local-first collaborative linked data | Related work; cite for the "local-first principles" framing |
| 16 | **Titanic** (NGI Zero Core, 2025) | https://nlnet.nl/project/Titanic/ | "Database server to synchronize vast collections of CRDT documents" | Contrast: MeshDoc is the *no-server* case; useful foil |
| 17 | **"it"** (NGI0 Entrust, 2023–2026) | https://nlnet.nl/project/it/ | "Radically decentralised version control with CRDTs" | Related work for change/signature history; cite |
| 18 | **Condensation** (NGI Assure, 2022–2024) | https://nlnet.nl/project/Condensation/ | "CRDT-driven data store that guarantees data ownership" | Related work; cite |
| 19 | **TypeCell** (NGI Assure, 2021–2024) | https://nlnet.nl/project/TypeCell/ | CRDT collaborative editor | Related work; cite |
| 20 | **AtomicServer Local-First** (NGI0 Commons Fund, 2025–2026) | https://nlnet.nl/project/AtomicServer-LocalFirst/ | Local-first headless CMS | Related work; cite |
| 21 | **AVantGaRDe** (NGI0 Entrust, 2023–2026) | https://nlnet.nl/project/AVantGaRDe/ | "Reliable foundations of local-first graph databases" | Related work; verify claims before citing |
| 22 | **Practical Decentralised Search and Discovery** (NGI0 Discovery, 2019–2022) | https://nlnet.nl/project/MeshSearch/ | "Search and discovery inside mesh/adhoc networks" | Cite for discovery prior art; MeshDoc uses BLE advertising, not search |
| 23 | **Herbees** (NGI0 Commons Fund, 2025) | https://nlnet.nl/project/SimpleX-relay/ | "Scalable intermediated P2P messaging based on SimpleX" | Related work for relay-mediated messaging; contrast with dumb blob relay |
| 24 | **Hyper Hyper Space Sync Engine** (NGI Zero Core, 2025–2026) | https://nlnet.nl/project/HHS-SyncEngine/ | "Secure P2P data synchronisation" | Related work; cite |
| 25 | **LibreOffice CRDT** (NGI0 Entrust, 2023–2026) | https://nlnet.nl/project/LibreOffice-CRDT/ | Distributed real-time collaboration with CRDTs | Shows CRDT collaboration is a funded theme; different domain |
| 26 | **Open Cloud Mesh** (NGI Zero Core 2023; FileSender 2026) | https://nlnet.nl/project/OpenCloudMesh/ , https://nlnet.nl/project/FileSender-OCM/ | Federated large-file transfer | Related only if MeshDoc adds file attachments later |

### 4.3 Specific cross-reference language for the proposal

Use these formulations (they are defensible with the citations above):

- "NLnet has funded the components of this problem separately — SecSync for E2EE CRDTs, Keyhive
  for serverless group key agreement, Irdest and qaul for mesh transport, p2panda for MLS over p2p,
  Offline Translator for on-device translation — but **not their intersection**: E2EE CRDT
  documents, authored per change, converging over an intermittent mesh with a dumb DTN relay
  `[VERIFIED https://nlnet.nl/project/Naisho/]` `[VERIFIED https://nlnet.nl/project/Keyhive/]`
  `[VERIFIED https://nlnet.nl/project/Irdest-OpenWRT-BLE/]` `[VERIFIED https://nlnet.nl/project/P2P-channels/]`
  `[VERIFIED https://nlnet.nl/project/OfflineTranslator/]`."
- "Briar, the closest NLnet-funded neighbour, lists collaborative document editing as a long-term
  plan, not a shipped feature `[VERIFIED https://en.wikipedia.org/wiki/Briar_(software)]`; MeshDoc
  does not compete with Briar's messaging but supplies the missing document layer as a reusable
  library."
- "Radio-Meshnet, the only NLnet project explicitly aimed at emergency radio networking, is
  archived and did not take place `[VERIFIED https://nlnet.nl/project/Radio-Meshnet/]`; the need
  remains, and a software-first approach with an Android reference client is a lower-risk route to
  impact than custom radio hardware."

**Outreach list (in order):** SecSync (Nikolaus Graf) → Keyhive / Ink & Switch → Irdest → qaul →
p2panda → Offline Translator. Asking each for a letter of support or a named collaboration is a
cheap credibility boost for an NLnet application; do not claim endorsement before receiving it.

---

## 5. Upstream contribution plan (3–5 concrete, checkable deliverables)

The goal is to make the grant output **infrastructure that outlives the app**. Each item below
names the artefact, the licence, the neighbour that benefits, and the acceptance test. All are
scoped to be deliverable inside a typical NLnet grant period alongside the app.

### U1. `meshdoc-transport` — a permissive BLE + Wi-Fi Direct transport crate for Android/Rust

- **What:** a Rust crate with a transport trait (discovery, connect, framed send/recv, resume) and
  two implementations behind it: BLE GATT advertising/scanning and Wi-Fi Direct group sockets
  (Android via JNI), plus fragmentation/reassembly for MTU-sized links and a deterministic
  in-memory transport for tests.
- **Why it matters:** every mesh app in §3 re-implements this; BLE/Wi-Fi Direct behaviour on Android
  is famously fiddly. A small, tested, permissively licensed crate is directly reusable by
  **Irdest** (BLE work), **qaul**, and any Briar-like document layer.
- **Licence:** dual MIT OR Apache-2.0 (compatible with Automerge/Loro/OpenMLS/Keyhive choice).
- **Acceptance:** crates.io release; API docs; example app; at least one external project opens an
  issue/PR using it; CI matrix on two Android API levels + desktop simulator.
- **Risk:** Android JNI surface is large. Mitigation: ship the BLE path first, Wi-Fi Direct second,
  and keep the trait stable so the second implementation cannot break users.

### U2. DTN relay profile + reference relay ("encrypted CRDT bundle" profile)

- **What:** (a) a short specification of the payload MeshDoc relays — ciphertext + author signature
  + causal/version metadata + expiry — deliberately transport-agnostic and BPv7-mappable; (b) a
  reference relay server (Rust) implementing store-and-forward, quota, expiry and no plaintext
  access; (c) a conformance test suite and an interop demo that exchanges the same payload via
  µD3TN/ION at the wire level (no code reuse, to respect AGPL/mixed licences).
- **Why it matters:** DTN has standards but no CRDT application profile; CRDT sync has transports
  but no DTN shape. This is the most "standards-shaped" output of the project and the most likely
  to attract reviewer attention.
- **Licence:** specification text under CC-BY-4.0; code MIT/Apache-2.0; AGPL DTN implementations
  used only as external test oracles `[VERIFIED https://gitlab.com/d3tn/ud3tn/-/raw/master/LICENSE]`.
- **Acceptance:** spec v0.1 reviewed by at least one DTN researcher; relay passes the conformance
  suite; interop demo documented in the repo; after the grant, submit an Internet-Draft to the IETF
  DTN WG `[VERIFIED https://datatracker.ietf.org/api/v1/group/group/?acronym=dtn]`.
- **Risk:** scope creep into full BPv7. Mitigation: explicitly declare BPv7 out of scope for the
  grant; the profile is the deliverable.

### U3. CRDT schema-migration patterns for offline-first documents

- **What:** a documented, tested pattern for evolving MeshDoc document schemas (checklist v1 → v2)
  when peers may be offline for weeks: versioned schema ids in each change, migrate-on-merge,
  forward/backward compatibility rules, and a migration test corpus. Publish as a design note plus
  example code, and upstream the examples to Automerge and/or Loro.
- **Why it matters:** schema drift is the operational failure mode of offline CRDT deployments and
  is under-documented; this is a small, high-leverage contribution that the CRDT projects
  themselves lack.
- **Licence:** MIT/Apache-2.0 (upstreamable to Automerge MIT and Loro MIT).
- **Acceptance:** design note; migration test vectors; example PR/issue accepted or at least
  reviewed upstream; MeshDoc app demonstrates a real v1→v2 migration with mixed-version peers.
- **Risk:** upstream maintainers may prefer their own approach. Mitigation: publish standalone
  first, propose upstream second.

### U4. Partition/anti-entropy fuzzing harness ("mesh chaos" simulator)

- **What:** a deterministic, seedable simulator that drives the sync engine through partitions,
  reordering, duplication, clock skew, crash/restart, MTU loss and long delays, with property tests
  for convergence, idempotence, causal delivery and signature validity. Expose as a reusable crate
  plus a CI job any project can adopt.
- **Why it matters:** this is the single strongest ecosystem signal in the plan. CRDT libraries test
  convergence under message permutation, but not under *mesh* conditions; mesh projects test
  routing, not CRDT convergence. A shared harness lets Automerge/Loro/qaul/Irdest test the
  intersection without building it themselves.
- **Licence:** MIT/Apache-2.0.
- **Acceptance:** harness published; MeshDoc CI runs it on every PR; at least one external project
  uses it in CI; documented failure cases (e.g. duplicate delivery after relay restart).
- **Risk:** "test infrastructure" is easy to under-fund. Mitigation: make it a first-class milestone
  with a demo of a real bug it caught.

### U5. MLS-over-DTN epoch handling (scoped, phase-2 bridge)

- **What:** a design note + reference implementation showing how MLS commits and Welcomes
  (RFC 9420) can be delivered over a lossy, high-latency, sometimes-partitioned mesh: ordering,
  idempotence, compaction, and recovery when an epoch change is only partially delivered. Build on
  OpenMLS (MIT) and align with Keyhive/p2panda's findings.
- **Why it matters:** MLS assumes an ordered group state machine; DTN has no ordering guarantees.
  This is the hardest unsolved part of MeshDoc's own roadmap and a genuine contribution to the MLS
  and p2p communities.
- **Licence:** MIT/Apache-2.0; OpenMLS is MIT `[VERIFIED https://api.github.com/repos/openmls/openmls]`.
- **Acceptance:** design note; reference implementation with tests for partial-epoch delivery;
  upstream documentation PR to OpenMLS or a joint note with Keyhive/p2panda; MeshDoc workspace-key
  migration demonstrated on a 5-device partition scenario.
- **Risk:** MLS state machine complexity. Mitigation: phase it after the core app ships; keep the
  workspace key as the supported default until the bridge is proven.

**Optional sixth (only if translation is funded):** a small Android on-device translation module
using Argos/OPUS-MT models (MIT + CC-BY-4.0) `[VERIFIED https://api.github.com/repos/argosopentech/argos-translate]`
`[VERIFIED https://huggingface.co/api/models/Helsinki-NLP/opus-mt-en-de]`, published as a reusable
library rather than an app feature — but this should not displace U1–U5.

**Why reviewers should believe these are real contributions, not promises:** each item has an
artefact, a licence, an acceptance test, and a named beneficiary among the neighbours in §3–§4.
Two of them (U1, U4) are usable by projects that have no interest in MeshDoc itself — which is the
definition of ecosystem value.

---

## 6. Honest limitations, uncertain claims and things to fix before submission

1. **Irdest licence is unknown.** Its Gitea host was unreachable from our network on 2026-11-02
   `[UNCERTAIN]`. Do not describe Irdest as reusable, and do not copy its code until the licence is
   confirmed by its maintainers.
2. **WinTAK has no public source found.** ATAK-CIV is GPL-3.0 and public
   `[VERIFIED https://raw.githubusercontent.com/TAK-Product-Center/atak-civ/main/LICENSE.md]`, but
   WinTAK (Windows) source was not located `[UNCERTAIN]`. The proposal should say "ATAK" and avoid
   claims about WinTAK's licence.
3. **`diamond-types` has no licence file.** It cannot be reused `[VERIFIED https://api.github.com/repos/josephg/diamond-types]`.
   If a reviewer asks why it is not a dependency, this is the answer.
4. **`p2panda` and `dtn7-rs` licence files were not detected at repository root** `[UNCERTAIN]`.
   Verify before citing them as reusable.
5. **Negative claims need careful wording.** "No project maps CRDT sync onto BPv7" is based on a
   keyword scan of NLnet plus targeted searches, not an exhaustive literature review `[UNCERTAIN]`.
   Phrase as "we found no …", and ideally add a sentence inviting correction.
6. **Manyverse's encryption model and Bridgefy's current crypto are not fully verified** `[UNCERTAIN]`.
   Cite only the sources above (site/abstracts/research paper), not details.
7. **Licence compatibility is a legal question.** Statements about MPL/LGPL/AGPL linking in this
   document are engineering judgements, not legal advice `[UNCERTAIN]`. Get a lawyer or the
   project's licence steward to confirm before making dependency claims in the application.
8. **Some project sites were unreachable** (irde.st, servalproject.org; getodk.org returned
   bot-protection content) on 2026-11-02. We used NLnet pages and repository metadata instead; note
   this if a reviewer asks for page-level citations.
9. **Figures are a snapshot.** Stars/dates were read on 2026-11-02 and will drift; the grant should
   cite projects, not star counts, unless the count is the point.
10. **NLnet project index scan is keyword-based** and English-only. It is evidence of the landscape,
    not proof of absence `[UNCERTAIN]`.

### Suggested final wording for the "what is new" paragraph

> MeshDoc is not the first mesh messenger (Briar, qaul, Meshtastic), the first CRDT library
> (Automerge, Yjs, Loro, cr-sqlite), or the first humanitarian data tool (KoboToolbox, ODK, DHIS2,
> Ushahidi). It is, to our knowledge, the first attempt to make **encrypted, signed CRDT documents**
> the unit that travels over an **intermittent BLE/Wi-Fi Direct mesh**, with a **dumb delay-tolerant
> relay** as the only optional server. The nearest prior art either stops at messages (Briar, qaul),
> assumes a server for E2EE CRDTs (SecSync), or solves group keys without a transport (Keyhive).
> MeshDoc's contribution is the intersection — delivered as a reusable, permissively licensed
> library, with upstream transport, relay-profile, schema-migration and fuzzing artefacts that
> outlive the app `[VERIFIED https://briarproject.org/how-it-works/]`
> `[VERIFIED https://nlnet.nl/project/Naisho/]` `[VERIFIED https://nlnet.nl/project/Keyhive/]`
> `[VERIFIED https://nlnet.nl/project/P2P-channels/]` `[VERIFIED https://meshtastic.org/docs/overview/]`.

---

## 7. Evidence ledger (one line per licence claim, for re-checking)

All checked 2026-11-02. Format: project — licence — evidence URL.

- Automerge — MIT — https://api.github.com/repos/automerge/automerge
- Yjs — MIT — https://raw.githubusercontent.com/yjs/yjs/main/LICENSE
- Loro — MIT — https://api.github.com/repos/loro-dev/loro
- diamond-types — none found — https://api.github.com/repos/josephg/diamond-types
- cr-sqlite — MIT — https://api.github.com/repos/vlcn-io/cr-sqlite
- SecSync — Apache-2.0 — https://api.github.com/repos/nikgraf/secsync
- Keyhive — Apache-2.0 — https://api.github.com/repos/inkandswitch/keyhive
- Earthstar — LGPL-3.0 — https://api.github.com/repos/earthstar-project/earthstar
- Meshtastic firmware — GPL-3.0 — https://api.github.com/repos/meshtastic/firmware
- Meshtastic Android — GPL-3.0 — https://api.github.com/repos/meshtastic/Meshtastic-Android
- Briar — GPL-3.0-or-later — https://raw.githubusercontent.com/briar/briar/master/LICENSE.txt
- qaul — AGPL-3.0 — https://api.github.com/repos/qaul/qaul.net
- Irdest — `[UNCERTAIN]` — https://nlnet.nl/project/Irdest/
- Reticulum — custom licence (non-OSI) — https://raw.githubusercontent.com/markqvist/Reticulum/master/LICENSE
- Serval — GPL-2.0 — https://raw.githubusercontent.com/servalproject/serval-dna/master/GPL-2.0.txt
- Bridgefy — proprietary — https://en.wikipedia.org/wiki/Bridgefy
- FireChat — proprietary/discontinued — https://en.wikipedia.org/wiki/FireChat
- Manyverse — MPL-2.0 — https://gitlab.com/staltz/manyverse/-/raw/master/package.json
- Berty — Apache-2.0 OR MIT — https://api.github.com/repos/berty/berty/contents
- SimpleX — AGPL-3.0 — https://api.github.com/repos/simplex-chat/simplex-chat
- Signal — AGPL-3.0-only — https://api.github.com/repos/signalapp/Signal-Android
- libsignal — AGPL-3.0 — https://api.github.com/repos/signalapp/libsignal
- Element Web — AGPL-3.0 — https://api.github.com/repos/element-hq/element-web
- Synapse — AGPL-3.0 — https://api.github.com/repos/element-hq/synapse
- Ushahidi — AGPL-3.0-or-later — https://raw.githubusercontent.com/ushahidi/platform/main/LICENSE.md
- HOT Tasking Manager — BSD-2-Clause — https://api.github.com/repos/hotosm/tasking-manager
- KoboToolbox kpi — AGPL-3.0 — https://api.github.com/repos/kobotoolbox/kpi
- ODK Collect — Apache-2.0 — https://raw.githubusercontent.com/getodk/collect/master/LICENSE.md
- ODK Central — Apache-2.0 — https://api.github.com/repos/getodk/central
- DHIS2 core — BSD-3-Clause — https://api.github.com/repos/dhis2/dhis2-core
- ATAK-CIV — GPL-3.0 — https://raw.githubusercontent.com/TAK-Product-Center/atak-civ/main/LICENSE.md
- TAK Server — GPL-3.0 — https://raw.githubusercontent.com/TAK-Product-Center/Server/main/LICENSE.md
- Sahana Eden (legacy) — MIT — https://raw.githubusercontent.com/sahana/eden-legacy/master/LICENSE
- ION — mixed REUSE (Apache-2.0/BSD/MIT/CC-BY-3.0) — https://api.github.com/repos/nasa-jpl/ION-DTN/contents/LICENSES
- µD3TN — AGPL-3.0 — https://gitlab.com/d3tn/ud3tn/-/raw/master/LICENSE
- DTN7 (go) — GPL-3.0 — https://raw.githubusercontent.com/dtn7/dtn7-go/main/LICENSE
- OpenMLS — MIT — https://api.github.com/repos/openmls/openmls
- mls-rs — Apache-2.0 — https://api.github.com/repos/awslabs/mls-rs
- mlspp — BSD-2-Clause — https://api.github.com/repos/cisco/mlspp
- Firefox Translations — MPL-2.0 (archived) — https://api.github.com/repos/mozilla/firefox-translations
- Bergamot — MPL-2.0 — https://api.github.com/repos/browsermt/bergamot-translator
- Argos Translate — MIT — https://api.github.com/repos/argosopentech/argos-translate
- OPUS-MT models — CC-BY-4.0 — https://huggingface.co/api/models/Helsinki-NLP/opus-mt-en-de
- NLLB-200 models — CC-BY-NC-4.0 — https://huggingface.co/api/models/facebook/nllb-200-distilled-600M
- RFC 4838 — Informational — https://www.rfc-editor.org/rfc/rfc4838.txt
- RFC 5050 — Experimental — https://www.rfc-editor.org/rfc/rfc5050.txt
- RFC 9171 — Standards Track — https://www.rfc-editor.org/rfc/rfc9171.txt
- RFC 9420 — Standards Track — https://www.rfc-editor.org/rfc/rfc9420.txt

*End of document.*
