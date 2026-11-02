# NLnet proposal, ready to paste

Every field is under its character limit and contains no em dash, en dash or
horizontal bar. Copy each block into https://nlnet.nl/propose/ exactly as it is.

**Read this before you submit.** The AI disclosure below is written to be true
whether you paste this text as it stands or rewrite it in your own words. If you
do rewrite the whole thing yourself, you may simplify it to say that AI was used
for research only. Do not claim the text is entirely your own writing while it is
not: NLnet's policy is explicit about this and being caught out is worse than
disclosing.

Still needed from you, and only you can supply it: name, email, phone, country,
applicant type (SME company for Arvion, or Individual), and the fund choice below.

| Field | Characters | Limit |
|---|---|---|
| Proposal title | 70 | none |
| Project website(s) / repositories | 37 | none |
| Project summary | 965 | 1000 |
| Proposed effort | 2604 | 4000 |
| Comparison with other efforts | 2299 | 4000 |
| Technical challenges | 2941 | 4000 |
| Ecosystem | 1295 | 2000 |
| Background | 1324 | 2000 |
| Other funding | 379 | 1000 |
| AI disclosure | 931 | 8000 |

---

## Fund

`Restack Fund`

## Proposal title

```text
MeshDoc: encrypted documents that sync phone to phone without a server
```

**70 characters** (limit none)

## Project website(s) / repositories

```text
https://github.com/sushant-me/meshdoc
```

**37 characters** (limit none)

## Project summary

_Summary of the proposed project and its expected results, in a few lines._

```text
MeshDoc is a reusable library stack for teams that cannot rely on the internet. An Android phone holds structured documents (checklists, supply forms, location notes) that are encrypted end to end and sync directly with other phones over Bluetooth and Wi-Fi Direct, then opportunistically through a relay anyone can host.

The gap is specific. The open stack has good tools for messages and good tools for documents, but document tools assume a server and message tools do not carry structured records. Nothing in between exists as a reusable layer, so every humanitarian project rebuilds it badly.

We will deliver four Rust crates (core, crypto, sync, transport), a small relay, and a reference Android app, all under MIT. Identity is a keypair made on the device: no accounts, no phone numbers, no server approving anyone.

A working prototype already shows the loop: two Android devices editing the same encrypted checklist while apart, converging on reconnect.
```

**965 characters** (limit 1000)

## Proposed effort

_Budget breakdown: tasks, time, rate, expenses._

```text
Requested amount: 29,920 euro. That is 176 person-days at 170 euro per day and no other costs.

Where the rate comes from. A senior Rust and Android engineer in Kathmandu earns about NPR 400,000 a month, roughly 2,350 euro. Adding 28 percent employer on-costs (social security and the festival allowance) and 20 percent for studio overhead gives about 3,770 euro a month, or 174 euro for a 21.67 day month. We ask 170 euro, slightly below that. This is cost recovery, not consultancy pricing. We ask for no equipment, no hosting, no compute and no travel. The test phones already exist in the studio, and NLnet provides the security and accessibility audits as support services, so they cost the grant nothing.

The work is nine packages.

1. Setup, architecture and threat model, 9 days. Public repository, licence, continuous integration, decision records and a written threat model that states what the system does not protect.

2. Protocol core, cryptography and the document bridge, 34 days. Four document types, the change format, device identity, workspace epochs, key rotation, the schema registry and migration.

3. Transport abstraction and a stock Android fast path, 20 days. One trait that any transport implements, plus a conformance suite so a new transport can be checked.

4. Free software transports, 26 days. BLE discovery with rotating identifiers, Wi-Fi Direct group formation, bulk transfer, and full function on phones without Google Play Services. This is the package the grant is really about.

5. Relay server and delay tolerant semantics, 14 days. The small store and forward service, rotating mailbox identifiers, quotas, eviction and an interoperability note.

6. Android reference client, 26 days. A Compose interface with large targets, the join flow, sync status, accessibility and onboarding.

7. Convergence and partition fuzzing, 18 days. A simulator, a seeded schedule generator, a differential oracle against a second CRDT implementation, and the energy measurement rig.

8. Field pilot, user research and documentation, 17 days.

9. Community, upstream publication and F-Droid release, 12 days.

Two people at roughly a third of full time each across twelve months. The first two months are deliberately light because payment is in arrears and we carry that period ourselves.

Payment is tied to five milestones: foundations at month 2, core plus first transport at month 5, the full transport matrix at month 7, product and pilot evidence at month 10, release and handover at month 12. The accessibility and security audits sit as zero cost gates at months 9 and 11.
```

**2604 characters** (limit 4000)

## Comparison with other efforts

_What is new, more thorough or otherwise different. Have you considered contributing to any of the others?_

```text
MeshDoc is not the first mesh messenger, not the first CRDT library and not the first humanitarian data tool. The claim is the intersection: encrypted structured documents that converge over an intermittent, serverless mesh, released as a permissive library that others can build on.

CRDT libraries. Automerge and Yjs, through its Rust port, already give convergence, and we will use one of them rather than write our own. What they deliberately leave to the application is identity, membership, encryption, peer discovery and a store and forward relay. Loro and cr-sqlite are in the same position. We build the missing layer rather than a new CRDT.

Mesh messengers. Briar carries messages over Bluetooth, Wi-Fi and Tor, and its roadmap lists collaborative document editing as future work. Meshtastic carries text and position over LoRa. qaul is a delay tolerant mesh messenger. Berty ships its own mesh stack. All of them make a message or a feed entry the unit of transfer. None ships a typed document that merges.

Humanitarian data. KoboToolbox and ODK are what the field actually uses, and both are server centric: a central instance reconciles submissions. DHIS2 is a national platform. That is the right design when a server exists. MeshDoc targets the case where it does not, and reconciles with such a server later if one appears.

Closest funded neighbours. SecSync, funded by NLnet, states the gap precisely: there is no plug and play way to exchange CRDTs with end to end encryption, and its own design is server mediated. Keyhive, also funded by NLnet, solves group key agreement for local first data, but it is not a field toolkit and has no transport. Irdest is the closest BLE mesh codebase and has no documents. Earthstar is adjacent but does not model typed humanitarian records.

Standards. We build toward MLS (RFC 9420) for group keys and take concepts from Bundle Protocol (RFC 9171) for the relay, rather than inventing formats.

What we will give back: a transport crate usable by other local first projects, a partition and merge fuzzing harness, written guidance on CRDT schema migration, and an interoperability profile for the relay. We would rather depend on the CRDT project we choose than fork it, and the transport work goes upstream as a crate rather than a patch.
```

**2299 characters** (limit 4000)

## Technical challenges

_What technical challenges do you expect during the project?_

```text
1. Android background limits against the energy target. Doze, App Standby buckets and foreground service rules may forbid the behaviour the design needs. We will measure on named devices over eight hour windows with two independent instruments, an external power monitor and the on device charge counter, and report both. If the target cannot be met, we say so with numbers.

2. BLE discovery privacy. A stable identifier is a tracking beacon. Our advertisement UUID is derived from the workspace key and rotates every fifteen minutes, and we will capture twenty four hours with a radio sniffer to measure what an observer can link. We will also state honestly that link layer tracking is outside what we can fix.

3. Wi-Fi Direct reliability across vendors. Group formation behaves differently on Huawei, Xiaomi, Samsung and Google devices. The device matrix is a deliverable, not an assumption, and the reference app falls back to a plain Wi-Fi socket when group formation fails.

4. CRDT growth over long partitions. Tombstones accumulate. Compaction must not break convergence, and a late joiner rebuilding from a snapshot must land in the same state. We test that explicitly.

5. Schema migration across app versions. A replica on version two receiving a change from version one must not fork. Migration is written as a pure function and tested as commutative with merge.

6. Key rotation during a partition. A removed member keeps the old key and can read old data. A partitioned member keeps using the old epoch until it sees the rotation. We document both limits rather than pretending rotation is revocation.

7. Membership without a server. Possession of a key is not authorisation. We keep a signed append only membership log with epochs, and a change is accepted only if its author was a member at the claimed epoch in the receiver's own view of that log.

8. Metadata at the relay. The operator cannot read content but can see a workspace pseudonym, blob sizes and upload timing. Mailbox identifiers rotate, and we state precisely what is and is not hidden.

9. Testing convergence credibly. Random schedules are easy to generate and easy to fool. We combine exhaustive small scope interleavings, large randomised schedules, crash injection at every write boundary, and a differential oracle against a second implementation.

10. The honest risk that the free software radio path is harder than expected. If group formation proves unworkable on enough devices, the transport trait lets us ship BLE discovery with a socket fallback, and we will say which parts were cut rather than quietly widen the claims.

11. Blob transfer under tiny bandwidth. A photograph must never delay a checklist. Documents sync first and blobs only on request, with explicit priorities.

12. Reproducible builds and F-Droid. A Rust, NDK and SQLite combination is notoriously hard to build bit for bit. We start that work in month one, not at release.
```

**2941 characters** (limit 4000)

## Ecosystem

_The ecosystem around the project and how you will engage relevant actors. Who are the main users?_

```text
Users. Field teams in disaster response, community health workers and NGOs who currently keep structured records on paper or in a server backed tool that stops working when the network does. The second audience is builders: other local first and humanitarian projects that need the piece we are making and would rather embed a crate than write it.

Dependencies. We depend on one CRDT implementation, on libsodium style authenticated encryption through established Rust crates, and on Android platform APIs. We do not depend on any vendor service. The relay depends on nothing but a Rust toolchain and a disk.

Who depends on us, once it exists: any project that needs encrypted peer to peer documents, and the relay operators, who need only a binary. We intend to make the transport crate and the fuzzing harness general enough for other local first projects to use directly.

Engagement. One upstream contribution merged per quarter with the CRDT project we build on. Issues and patches to the Android transport work rather than a private fork. Presentation at a local first or free software event each year. The field pilot documented publicly. And we will take up NLnet's own support services: the security audit and the accessibility scan, both of which we have budgeted as zero cost gates.
```

**1295 characters** (limit 2000)

## Background

_What makes you the right person(s) for this effort? Relevant experience and contributions._

```text
I am Sushant, a software engineer in Kathmandu, Nepal, and I run Arvion Technologies, a small product studio.

What I have shipped that is relevant. I have built offline first sync before: an operation log with vector clocks and last writer wins conflict handling, written to work without a server. I have shipped production Android and Flutter applications and maintain a set of open Rust and TypeScript libraries. I work in Rust for the parts where correctness matters more than speed, and in Kotlin and Dart for the parts a person touches.

This is not a hypothetical problem for me. Nepal has had two major earthquakes in a decade, and mobile data in the districts outside the valley is unreliable at the best of times. I have watched teams coordinate on paper because the software needed something the place did not have.

The prototype behind this application already exists: an encrypted CRDT core in Rust with 133 tests, a relay, and an Android client that runs on a real Android build and generates its own identity. I wrote it to find out whether the hard parts are as hard as they look, and to be able to say something true rather than something hopeful.

What I am not is a large team. Two of us will do this work, which is why the plan is deliberately conservative and the first months are funded by the studio.
```

**1324 characters** (limit 2000)

## Other funding

_Does (or did) the project have other funding sources?_

```text
No other funding. The project has none, and no part of it has been funded before this application. The prototype was built with studio time. Arvion Technologies is a commercial studio that takes client work, and this grant would fund people to work on the commons part of the problem rather than on client projects. There are no patents on any of it and no intention to file any.
```

**379 characters** (limit 1000)

## AI disclosure

_Did you use generative AI in writing this proposal?_

```text
AI assistance was used while preparing this application. It was used to read and summarise NLnet's published material (the Restack call, the guide for applicants, the eligibility rules and the generative AI policy), to check the current state and the licences of comparable projects, to sanity check the budget arithmetic, and to help draft and structure the text of this form.

The technical design, the choices about scope, the plan and the arguments are mine. I can explain and defend any sentence in this application and I expect to be asked to.

The prototype in the linked repository was written with AI assistance in a coding and review capacity during an exploratory phase before this application. That is disclosed because the policy asks about pre-existing AI generated code. The funded work described here will be written by me and my colleague, not by an AI.

I would rather over disclose than have it discovered later.
```

**931 characters** (limit 8000)

---

## Attachments

Optional. The strongest one is a short letter of support from a real pilot
organisation. If you have none, submit without attachments; the form says they
are not needed.
