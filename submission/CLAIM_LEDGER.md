# Claim ledger — every factual claim, with its source and its status

**Why this exists:** the Restack Guide states the review team *"will do independent verification of facts, methods and claims"*, and `research/FUND_RULES.md` records that facts get checked through an expert network. A single unverifiable claim in the proposal costs disproportionately. This ledger lets you check before they do.

**How to use it:** only make claims that appear here with status `SAFE`. For `VERIFY` items, either check them yourself before writing or phrase them as hypotheses. For `AVOID`, do not write them.

Status legend:
- **SAFE** — verified from a primary source this session; quote or paraphrase freely.
- **VERIFY** — plausible but not confirmed, or device/OS-dependent; phrase as "we expect / we will measure".
- **AVOID** — wrong, overclaimed, or out of scope for Restack.

---

## A. Fund rules (these are safe to cite directly)

| Claim | Status | Source |
|---|---|---|
| Deadline 3 Nov 2026 12:00 CET (16:45 NPT) | SAFE | https://nlnet.nl/propose/ |
| First grant €5,000–€50,000 | SAFE | https://nlnet.nl/propose/ |
| Max €150k/proposal, €500k lifetime per third party | SAFE | https://nlnet.nl/restack/guideforapplicants/ |
| Rate ceiling €65/hour; using it harms cost-effectiveness | SAFE | https://nlnet.nl/officehour/#amount |
| Cost-recovery basis, not commercial rates | SAFE | https://nlnet.nl/funding.html |
| Scoring 30 % technical / 40 % relevance / 30 % cost-effectiveness; pass >5.0/7 | SAFE | https://nlnet.nl/restack/guideforapplicants/ |
| Knock-out: must have R&D as primary objective | SAFE | https://nlnet.nl/restack/guideforapplicants/ |
| Nepal is a Horizon Europe-eligible country | SAFE | https://nlnet.nl/OIS/european-dimension/ |
| Nepal is "automatically eligible for funding" under the EC list | SAFE | EU Grants List of participating countries V4.2, 07.10.2026 |
| European dimension = people, ≥60 % of funds | SAFE | https://nlnet.nl/OIS/european-dimension/ |
| AI-related projects out of scope unless >1M active users | SAFE | https://nlnet.nl/restack/ |
| GenAI may not be used to write proposals (applies to this call) | SAFE | https://nlnet.nl/foundation/policies/generativeAI/2.0/ |
| GenAI may not produce code/design/documentation; read-only only | SAFE | same |
| Hosting, compute, phones, laptops not eligible | SAFE | https://nlnet.nl/officehour/#hardware + https://nlnet.nl/foundation/policies/externalspending/ |
| No payment for work done before the grant | SAFE | https://nlnet.nl/restack/faq/ |
| Milestone arrears payment; grants are donations, no VAT | SAFE | https://nlnet.nl/restack/faq/#upfrontpayment |
| Default duration ≤12 months | SAFE | https://nlnet.nl/restack/faq/#timelines |
| Assessment takes 3–5 months from the deadline | SAFE | https://nlnet.nl/restack/faq/ |
| F&A capped at 25 %, generally not eligible | SAFE | https://nlnet.nl/restack/faq/#FA |
| Free security audit (Radically Open Security) and accessibility audit (HAN) as support services | SAFE | https://nlnet.nl/NGI0/services/ |
| Sample MoU contains "Certified WCAG accessible" and "Process issues from external security review" milestones | SAFE | https://nlnet.nl/foundation/request/sample_MoU.pdf |
| Resubmission allowed; last complete version before deadline is used | SAFE | https://nlnet.nl/restack/guideforapplicants/ |

---

## B. Technical claims about your own design

These are claims *about MeshDoc*. They must be internally consistent and must not overstate.

| Claim | Status | Note |
|---|---|---|
| Every change is encrypted and signed by its author | SAFE | Design property; implement it |
| Identity is the public key; no accounts | SAFE | Design property |
| Workspace id is an independent random value, never derived from the key | SAFE | **Correction to the original spec — the spec's `hash(workspace_key)` breaks key rotation.** See `research/TECHNICAL_CASE.md` I2 |
| Membership is authorised by a signed append-only log with epochs | SAFE | Replaces "membership = possession of the key", which contradicts "set of public keys" |
| Removed members can still read data encrypted under old epochs | SAFE | Honest limitation; state it |
| Relay cannot read content | SAFE | True |
| Relay learns rotating pseudonymous mailbox ids | SAFE | Honest refinement of "relay learns a workspace exists" |
| Convergence for the supported types is guaranteed by the CRDT | SAFE | Qualify: "for the supported types" |
| MLS (RFC 9420) is the long-term group-key path | SAFE | Cite as direction, not deliverable |
| Bundle Protocol (RFC 9171) concepts inform the relay | SAFE | Cite as alignment, not implementation |
| Idle ≤15 mW | VERIFY | Target + measurement protocol; do not present as a result |
| <2 %/day battery | **AVOID as stated** | 15 mW × 24 h = 0.36 Wh; a 15.4 Wh battery gives **≈2.34 %/day**. Either claim "≤15 mW (≈2.3 %/day)" or target ≤12.8 mW for the 2 % claim. Do not mix the two |
| Sync latency <3 s p2p | VERIFY | Target with a defined measurement (AC-04a/b) |
| Relay sync on ≤50 kbps link | VERIFY | Target with a defined measurement (AC-08) |
| 10⁵ random schedules, zero divergence | VERIFY | Frame as the planned test, with the oracle defined |
| "Guaranteed by the CRDT, no conflicts" | AVOID as stated | Say convergent-by-construction for the supported types, and verified by differential fuzzing |
| "Sybil-proof" | AVOID | Signing gives attribution, not Sybil resistance |
| Forged changes are "rejectable" | VERIFY | Only if clients verify against the membership log — say that |
| BLE advertising in background all day | VERIFY | Android Doze/App Standby/FGS rules may forbid it; treat as a research question |
| Wi-Fi Direct works across OEMs | VERIFY | Known to vary; the device matrix is a deliverable |
| Android Keystore holds ed25519/x25519 keys | VERIFY (likely false) | Keystore generally does not expose those ops; the honest claim is "encrypted at rest under a hardware-backed wrapping key" |
| "~300-line relay" | AVOID as a brag | Frame the relay as a work package with a threat model, quotas and an interop profile |
| "iOS mesh APIs are locked down" | VERIFY | More accurate: iOS lacks Wi-Fi Direct and background BLE advertising equivalents |
| On-device translation / language packs | **AVOID entirely** | Out of scope for Restack (AI) |

---

## C. Claims about other projects (these get fact-checked against the maintainers)

All from `research/LANDSCAPE.md`; each carries a verified URL there. Describe them accurately or not at all.

| Project | Safe characterisation | Licence |
|---|---|---|
| Automerge | local-first sync engine for collaborative apps; MIT | MIT |
| Yjs / Yrs | shared data types for collaborative software; MIT | MIT |
| Loro | CRDT JSON document library; MIT | MIT |
| cr-sqlite | convergent replicated SQLite; MIT | MIT |
| Briar | P2P messaging over Bluetooth/Wi-Fi/Tor with a store-and-forward mailbox; collaborative document editing is on their *future* roadmap | GPL-3.0 |
| Meshtastic | LoRa text messages and position reports across a mesh; GPL-3.0 | GPL-3.0 |
| SimpleX | no user identifiers, but server-relayed (SMP servers); AGPL-3.0 | AGPL-3.0 |
| Manyverse | P2P social network on Secure Scuttlebutt | AGPL-3.0 |
| qaul | off-grid delay-tolerant P2P mesh messenger, NLnet-funded; AGPL-3.0 | AGPL-3.0 |
| Berty | Wesh mesh protocol + messenger | Apache-2.0 / MIT (check) |
| KoboToolbox | server-centric (`kpi` is the server) | AGPL-3.0 |
| ODK Collect / Central | Android form app + central server | Apache-2.0 |
| DHIS2 | national/central health information platform | BSD-3-Clause |
| Ushahidi | crowdsourced citizen-reporting platform | AGPL-3.0 |
| Keyhive (Ink & Switch, NLnet) | E2EE group collaboration sync engine — closest neighbour, Apache-2.0 | Apache-2.0 |
| SecSync (NLnet) | E2EE CRDT sync protocol, server-mediated — cites the exact gap you fill | Apache-2.0 |
| Reticulum | custom non-OSI licence with a no-harm clause — **cannot be described as OSI-open** | custom |

**Never write:** "no project does X" or "we are the first". Write "in our survey we found no project that…", and name the survey scope.

---

## D. Claims about the applicant (only you can verify these)

| Claim | Status | Note |
|---|---|---|
| Arvion Technologies, Kathmandu, Nepal | SAFE | Your own fact |
| Prior offline-sync work (`sync-kit`: operation log, vector clocks, LWW) | SAFE | Real repo; describe it accurately |
| Team members, roles, time commitment | SAFE | Only if true |
| Named pilot organisation | VERIFY | Only claim one you have a letter from |
| "Working prototype exists" | **AVOID** unless it does | Reviewers detect invented progress |
| Company registration / legal entity | SAFE | Arvion exists as an org on GitHub; confirm the legal status you claim |

---

## E. The three traps in one place

1. **Do not say `hash(workspace_key)` is the workspace id.** It breaks key rotation.
2. **Do not claim <2 %/day at 15 mW.** The arithmetic does not support it.
3. **Do not mention translation, language packs, or on-device models at all.** It reclassifies the proposal as an AI project, which Restack excludes.
