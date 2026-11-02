# MeshDoc → NLnet Restack: Compliance & Strategy Brief

**Prepared:** 2026-11-02 ~10:15 UTC · **Deadline:** 2026-11-03 12:00 CET = 11:00 UTC = **16:45 Nepal time, 3 Nov** → **~24 h 45 m left**
**Applicant:** Arvion Technologies (Kathmandu, Nepal) · **Fund:** Restack (Open Internet Stack)
**Status of this document:** compliance analysis and research synthesis. **It is not proposal prose, and must not be submitted as such** — see §11.

---

## 0. Read this first

Three things decide whether this application is even *reviewed*:

| Gate | Verdict | Action needed |
|---|---|---|
| **Eligibility** — European dimension, Nepal | ✅ **PASSES.** Nepal is explicitly on NLnet's Horizon Europe-eligible list. | Just state it correctly. Do **not** apologise for being in Nepal. |
| **GenAI policy v2.0** — effective 2026-10-20, applies to this call | ⚠️ **HARD BLOCK.** AI may not be used to write the proposal *at all*. | You write the 7 answer fields yourself. This brief + the research pack gives you the substance so it takes ~3 h, not 3 days. |
| **Restack scope** — "AI-related projects are not within scope" | ⚠️ **Your current spec has an AI feature.** On-device translation will be read as an AI project. | **Cut translation from the funded scope.** This is the single biggest scoring fix. |

Your idea is genuinely a good fit for this fund. The Restack call text itself says it covers *"from productivity tools to 'local-first' infrastructure"*. You are aiming at a bullseye. The work is in removing the three things that would get you screened out, and in making the 40 %-weighted "relevance/impact" case concrete.

---

## 1. The five hard facts

1. **Deadline: 3 November 2026, 12:00 CET (noon).** There is a deadline on the 3rd of every *odd* month, so the next call after this is January 2027. [VERIFIED https://nlnet.nl/propose/]
2. **You can resubmit freely until the deadline.** The Guide for Applicants states that if multiple versions are submitted before the deadline, *"the last complete version will be used."* → **Submit a decent version tonight, then improve it tomorrow morning.** This removes most of the deadline risk. [VERIFIED https://nlnet.nl/restack/guideforapplicants/]
3. **Nepal satisfies the European dimension.** The eligible-country list includes *"− Namibia, Nepal, Netherlands, New Caledonia, New Zealand, …"* (list last updated 2026-10-13), and: *"People and organisations of these eligible countries can participate on the same terms as those from EU member states. Having 60% of the funds go to people from any of these countries, meets the European dimension criterium."* [VERIFIED https://nlnet.nl/OIS/european-dimension/] The Restack eligibility page adds a discretionary fallback: *"if the project is of exceptional quality and the proposer holds unique technical expertise proposals from outside of those geographic areas can be taken into consideration."* [VERIFIED https://nlnet.nl/restack/eligibility/]
4. **First-grant range is €5,000–€50,000**, paid in milestone tranches *after* work is done — not up front. [VERIFIED https://nlnet.nl/propose/] The **rate ceiling is €65/hour**, and the Office Hour is explicit that using it *hurts* you: *"The absolute maximum rate we can allow for is 65 euro/hour, but using the maximum rate impacts cost effectiveness, and thus can reduce chances of getting the project granted."* [VERIFIED https://nlnet.nl/officehour/#amount] A Nepal-based studio should price far below the ceiling — see `research/BUDGET_AND_MILESTONES.md`.
5. **Scoring is weighted and you must clear 5.0/7 to survive round one**: 30 % technical excellence/feasibility · **40 % relevance/impact/strategic potential** · 30 % cost effectiveness/value for money. [VERIFIED https://nlnet.nl/restack/guideforapplicants/] → The 40 % bucket is where you win or lose, and it is the weakest part of your current draft.
6. **It must be R&D, not product development.** A genuine knock-out criterion: proposals *"should have research and development as their primary objective"*, and those that fail *"will not be further reviewed and will be marked ineligible."* [VERIFIED https://nlnet.nl/restack/guideforapplicants/] → Your proposal must lead with the research/engineering questions (convergence under mesh partition, group-key management without a server, ciphertext routing that survives delay), with the Android app as the vehicle — not as the product.

---

## 2. Gate 2 in detail — the GenAI policy (this is the one that catches people)

Policy v2.0, dated 20 October 2026, effective immediately, **explicitly applies to the Restack call with the 3 November deadline** (confirmed in the announcement). [VERIFIED https://nlnet.nl/news/2026/20261020-AI-policy.html]

Verbatim, from https://nlnet.nl/foundation/policies/generativeAI/2.0/ :

> **GenAI within the application process**
> It is **not** allowed to use generative AI during the writing of proposals, nor when providing answers during the interactive evaluation of proposals. This includes LLM generation of ideas, as well as restructuring, shortening and translation. Trust in your knowledge and skills, and use your own words. We don't care about spelling or grammar, only about your ideas.

> **GenAI within your project**
> It is **not** allowed to use generative AI for producing artefacts of any kind, including code, design, and documentation.
> It **is** allowed to employ GenAI in a **read-only** manner — meaning, for instance, that you can have an AI tool check your code and identify security issues and flaws, but that you craft fixes and mitigations yourself, and write your own code.

> **Failure to comply may result in rejection of the proposal, submitted work not being accepted for payment, or ultimately in the termination of the running grant.**

The policy FAQ is blunter still, and it closes the "AI as pair programmer" escape hatch:

> **Q: We use AI as a coding partner in our development, and we intend to continue doing so. Does our approach make the project ineligible?**
> A: The short answer is yes. AI as a 'coding partner' is not a development method that is compatible with our current programmes and the genAI policy.

> **Q: Would using an LLM to explain existing code, discuss technical approaches, or identify bugs fall within permitted "read-only usage", provided developers assess the output and implement changes themselves?**
> A: You can have LLM's look at your code and point out flaws. You have to then write the code to fix it up yourself. **Asking an LLM what to do next [is] not allowed**, you should yourself build a working solution. Only then can you have it reviewed.

That last line is the one to internalise: **AI may review what you already decided; it may not decide for you.** Design decisions, architecture and code must originate with you.

And the stated rationale, which tells you exactly how they will read an AI-flavoured submission:

> We found ourselves having to process an avalanche of additional proposals lacking maturity and relevance. Upon closer inspection, proposals involving AI were on the whole of much lower quality than we are used to at NLnet — and at the same time very taxing and demotivating for our experts to wade through.

### What this means practically

- **Do not submit this brief, or anything derived from it, as your answer text.** The policy names *"restructuring, shortening and translation"* and even *"LLM generation of ideas"*. Pasting AI output is the named failure mode, and reviewers now pattern-match on it.
- **The application form still has an AI-disclosure field** (8,000 chars + prompt upload), but the "Yes, I used generative AI in writing this proposal" option now only legitimately applies under the accessibility exception. **Using it to declare research-only assistance is the honest route** if you used any AI in preparing — and the policy's transparency section says to always be transparent. Declaring research assistance is not itself a violation; declaring *writing* assistance is a confession under v2.0.
- **Consequence for the project itself:** if funded, you may not use GenAI to *produce* code, design or documentation. Read-only use (AI reviews your code, you write the fix) is allowed and must be disclosed. **So your repo must be your own writing.** Budget no money for AI tooling either — *"Costs incurred for AI usage are not eligible for reimbursement."*
- **Recommended hygiene if you win:** publish a short `CONTRIBUTING`-level GenAI policy in the repo and a one-line stance in the README. The policy calls this *"even better in terms of transparency"* and it costs you 20 minutes.

### The productive way to read this

The policy is not asking you to be less prepared — it is asking you to be *more yourself*. Everything in `research/` is **publicly available factual material** (fund rules, prior art, licences, protocol references, price points). Facts are not ideas. Use them as reference, close the documents, and write from what you now understand. Where this brief says "the reviewer will ask X", that is compliance mapping against published criteria, not a suggested sentence.

---

## 3. Gate 3 — the AI-scope problem in your draft

Restack, verbatim:

> **AI-related projects are not within scope** — unless they are already widely used throughout society (> 1 million active human users) and directly relevant to the stack…. the development, application and/or integration of artificial intelligence is complementary/orthogonal effort to the work supported within Restack. [VERIFIED https://nlnet.nl/restack/]

Note that **"integration"** is named. So the tempting fix — "we only *integrate* an existing translation model, we don't train one" — does not work. Your draft leads with translation as one of three flagship scenarios ("Aid worker + locals language gap… translated entirely on-device") and has a Language Pack concept, a translation view-layer design, and a cached-translation data path. A reviewer skimming the summary will classify this as an AI project and stop.

**Decision: remove translation from the funded scope entirely.**

- Delete the Language Pack concept, the en↔ne example, and the "translation view-layer" reasoning from the proposal.
- Replace the third scenario. You already have two strong ones (earthquake response; village health worker). A better third: **the handover/continuity case** — a team's workspace outlives the team; a new volunteer joins by scanning a printed QR and inherits the whole structured record with no server and no account. That is pure infrastructure value and it showcases membership + DTN, not AI.
- If the user cares about translation, it belongs in a **separate future application to a different fund**, and the proposal may contain exactly one neutral forward-looking clause: the document format is schema-versioned so that view-layer features (such as translation) can be added later without touching stored data. That is a design-property statement, not an AI deliverable. Do not promise it.

---

## 4. Scope surgery — 12 fixes to the current spec

Ordered by how much each one affects your score. Each is a *correctness or credibility* problem a technical reviewer will find.

**S1 — [CRITICAL] Workspace id is derived from the workspace key.** `id: hash(workspace_key)` breaks key rotation: rotating the workspace key (your own member-removal design) changes the workspace id, which invalidates the relay mailbox, every peer's stored references, and every outstanding change. Fix: derive the workspace id from an independent random identifier created once at workspace creation; the key is rotated freely and is *not* the id. This is a real design bug, and a crypto-literate reviewer will spot it.

**S2 — [CRITICAL] "Membership = possession of the workspace key" contradicts "members: set of public keys".** These are two different models. If possession *is* membership, the member set is unauthenticated and a stolen key is indistinguishable from a member. If the member set authorises, you need a **signed, append-only membership log** (a hash-chained or CRDT log of `{pubkey, role, epoch}` entries, signed by an existing member) so that any node can verify *"was this signing key a member at the causal point this change was authored?"*. Say which model you are building, and pick the second.

**S3 — [CRITICAL] The Sybil/member-removal paragraph is currently wrong.** Your draft says a stolen workspace key "lets you read but your forged changes are cryptographically attributable-and-rejectable". Attributable, yes. Rejectable only if (a) changes are verified against the membership log and (b) clients enforce it. And a *removed* member who kept the old key can still read all data encrypted under the old key forever — rotation does not and cannot revoke plaintext already seen. State this plainly. Honest limitation statements *raise* reviewer trust; overclaims destroy it.

**S4 — [HIGH] "Idle mesh under ~15 mW / <2 % battery/day" needs a measurement method or it reads as marketing.** Modern Android aggressively restricts background BLE scanning/advertising: Doze, App Standby buckets, and the `FOREGROUND_SERVICE_CONNECTED_DEVICE` type make "gossiping all day in a backpack" an OS-policy problem before it is a radio problem. Keep the target — but frame it as *the hypothesis the project will test*, and name the instrument (e.g. on-device `BatteryStats`/`dumpsys batterystats` delta over a fixed 8 h idle run on named device models, plus a bench measurement of the radio state machine). See `research/TECHNICAL_CASE.md` §3(a).

**S5 — [HIGH] Google Nearby Connections as the "fast path" undercuts your own thesis.** P2P_CLUSTER depends on Google Play Services — precisely the proprietary dependency Restack exists to remove, and unavailable on de-Googled Android, which is what privacy-conscious European humanitarian deployments use. Keep it strictly as a *developer-loop convenience behind the `MeshTransport` trait*, never a shipped dependency, and say so in one sentence. The FOSS path must be the product.

**S6 — [HIGH] The relay is described as "~300 lines" — that reads as low value, not as elegance.** Either make it genuinely modest-but-load-bearing (capability tokens, per-workspace storage quotas, abuse/DoS resistance, deletion/pruning policy, a documented threat model, an interoperability profile) and give it a WP of its own, or fold it into the sync work package. Do not advertise a small number as if it were the achievement.

**S7 — [MEDIUM] Relay metadata leakage is understated.** `hash(workspace_key)` as a mailbox id is a **stable pseudonym**: the relay can link every upload for that workspace over months, and correlate size/timing with activity. "Relay learns a workspace exists" is true but incomplete. If you fix S1 you get the chance to add rotating mailbox identifiers (derived from the workspace id + an epoch, rotated periodically) with the relay retaining old-epoch blobs for a bounded window. Mentioning this trade-off explicitly is a strong signal.

**S8 — [MEDIUM] CRDT schema migration across long partitions is hand-waved.** "Old schema versions are migrated, never dropped" is the right instinct, but migration in a CRDT must **commute with merge** — a replica on v2 merging a v1 change must not fork state. This is one of the genuinely hard, publishable parts of your project. Promote it from a footnote to a named work package and a named challenge. Same for tombstone growth/compaction over months-long partitions.

**S9 — [MEDIUM] "Two phones converge… 10⁵ random schedules, zero divergence" is a good headline — make it a method.** Name the fuzzer strategy (randomised partition/merge schedule generator over a simulated network with per-node causal delays, oracle = byte-identical canonical CRDT state), the seed corpus, and how many schedule lengths/depths. A reviewer's follow-up will be "how do you know your oracle is right?" — answer: differential testing against a second implementation of the same type (e.g. two different CRDT libraries, or an independent reference model).

**S10 — [MEDIUM] Android-only needs one honest sentence.** Restack reviewers will ask about reach and accessibility. Android dominance in the target region is a *good* reason; add that the Rust core is platform-neutral so a desktop/Linux client is a downstream possibility, and that the app must pass accessibility review (NLnet offers free accessibility scans — take them, it is a scoring signal).

**S11 — [MEDIUM] No named pilot partner.** Your success metric is "1 field pilot with a real organization, documented in FIELDNOTES.md" — but no organisation is named. The single highest-leverage thing you can do in the next 24 hours is get **one short letter of support** (an email PDF is fine) from a real Nepali or regional organisation that would pilot this: e.g. Nepal Red Cross Society, NSET (National Society for Earthquake Technology), DRN Nepal, a district health office, or a trekking/expedition operator. NLnet's form accepts attachments (optional) and the Guide says a common round-two question is *"how does upstream project D feel about your application"* — a named partner pre-empts that. Even a one-paragraph letter changes the 40 % bucket materially.

**S12 — [LOW] Open-source licence must be chosen explicitly.** "Open source" is not enough; the Guide requires *"a recognised open source license in its entirety"*, and NLnet is a strong EUPL/Apache-2.0/GPL shop. Pick one and write it into the repo and the proposal. `repo-template/LICENSE` in this pack contains real licence texts — delete the ones you do not use. If you want the widest reuse in commercial European deployments, **Apache-2.0**; if you want copyleft on the network service, **AGPL-3.0**; if you want a European-flavoured copyleft explicitly designed for this, **EUPL-1.2**.

**S13 — [HIGH] Ineligible costs that would sink the budget.** Three expense lines people instinctively add are explicitly not fundable:

| Not eligible | Verified rule |
|---|---|
| **Phones, laptops, workstations** | *"NLnet does not allocate grant money to basic operational IT cost, such as regular laptops, desktops/workstations, or mobile phones."* [https://nlnet.nl/foundation/policies/externalspending/] |
| **VPS / hosting / compute** | *"we are not generally able to fund hosted instances of software, or cover hosting costs"*; *"compute time renting would fall under operational expenses"* [https://nlnet.nl/officehour/#hardware] |
| **Work already done** | *"We cannot make donations for any effort completed prior to the grant."* [https://nlnet.nl/restack/faq/] |

Consequence: **budget zero expenses if you can**; the ask is for your time and nothing else. And because hosting is ineligible, the relay must be framed as **code to be developed** (a work package), never as **a service to be operated** — that single framing choice is the difference between eligible and ineligible.

---

## 5. Fact-check of the current draft (things that will be challenged)

| Current claim | Problem | Better framing |
|---|---|---|
| "translated entirely on-device, no data leaves either phone" | AI feature → out of scope | Remove (S3 above) |
| "Sybil-proof" | Overclaim; signing gives attribution, not Sybil resistance | "Every change is attributable to a signing key that must appear in the signed membership log" |
| "guaranteed by the CRDT, no conflicts" | True only for the data type's semantics | "Convergent by construction for the supported types; verified by differential fuzz testing" |
| "relay… cannot read anything" | True of content, false of metadata | "cannot read content; it does learn workspace pseudonyms, blob sizes and timing — mitigated by rotating mailbox ids" |
| "mesh hop range is tens of meters" | Correct and good — keep | Keep. This honesty scores. |
| "iOS mesh APIs are locked down" | Fair, but check: MultipeerConnectivity exists; it is more accurate to say no Wi-Fi Direct equivalent | "iOS lacks the equivalents of Wi-Fi Direct and background BLE advertising we depend on" |
| "15 mW idle" | Unmeasured | Target + measurement plan |
| "~300-line service" | Reads as low value | See S6 |
| "the grant is asking money to finish it" | Reads as "we already built it" — but you have not | Be precise about what exists today vs. what the grant funds. **Do not claim a working prototype you do not have.** |

**On that last line:** if you have no MeshDoc code yet, say so and sell the *plan*. NLnet funds development, and reviewers are experienced at spotting invented progress. Note also that your public GitHub currently shows ~40 "case study" repos all created on 2026-10-29 — a reviewer who looks will form an impression. Either (a) point the "repositories" field at one clean, purpose-built MeshDoc repo, or (b) make sure that repo is the obvious serious one. Do not let the portfolio dilute the signal.

---

## 6. Positioning — how to earn the 40 %

The 40 % "relevance/impact/strategic potential" weight is where your draft is thinnest, because it argues *user need* (disaster response) but not *stack need* (why the open internet stack is missing this piece).

**The stack argument to make (this is the missing story):** the open internet stack has excellent pieces for **messages** (Matrix, Briar, SimpleX) and excellent pieces for **documents** (Collabora, CryptPad, Nextcloud) — but the document tools are all **server-centric**, and the message tools do not carry structured records. There is **no reusable, serverless, end-to-end-encrypted layer for structured collaborative documents** — the thing an aid team actually fills in. Local-first sync libraries exist (Automerge, Yjs) but they are transport-agnostic data structures with no identity, no membership, no encryption boundary, no peer discovery, and no delay-tolerant relay. MeshDoc's contribution is that missing **middle layer**, released as a reusable stack so European public-sector and civil-society builders do not each rebuild it.

**Six differentiators to substantiate** (evidence and URLs in `research/LANDSCAPE.md`):
1. **Documents, not messages.** Briar/Meshtastic/SimpleX carry text; nothing carries a convergent structured record over a mesh.
2. **No server in the trust path.** KoBoToolbox/ODK (the actual status quo for field data collection) require a server; that is the dependency that fails in the scenario you are designing for.
3. **Anti-entropy + DTN, not live sessions.** Existing mesh apps assume both peers are present; you assume they never are.
4. **A reusable transport trait**, so the same sync core rides BLE, Wi-Fi Direct, LoRa-adjacent links, or sneakernet (USB) later.
5. **Anyone-can-host relay** → digital sovereignty in one binary; no dependency on the grantees after the grant ends.
6. **Standards path**: MLS (RFC 9420) for group key management, BPv7 (RFC 9171) concepts for the relay, and a documented wire format others can implement.

**NLnet publishes the strategic dimensions it rewards.** Hit them explicitly, because this is the 40 % bucket [VERIFIED https://nlnet.nl/restack/faq/#under-represented]:
- **effect on the technology landscape** — local-first instead of cloud SaaS; a missing middleware layer released as commons;
- **standardisation efforts under way** — MLS, BPv7, documented wire format;
- **human rights aspects** — censorship-resistant, surveillance-resistant coordination for civil society;
- **societal dialogue / resilience** — disaster-resilient communications infrastructure, and the fact that this is built in a region where the failure mode is routine;
- **role models for under-represented groups** — you are a small team in Nepal building infrastructure other regions will reuse; that is a legitimate strategic dimension and NLnet says so in writing.

**Upstream contributions to promise** (this is the single strongest ecosystem signal, and the Guide explicitly asks *"how will you engage relevant actors"*): a Rust `MeshTransport` crate with BLE + Wi-Fi Direct backends usable by any local-first project; a partition/merge fuzz harness published as a reusable testkit; CRDT schema-migration patterns written up for the local-first community; and the relay's interoperability profile. Each is small enough to actually deliver and concrete enough to verify.

---

## 6b. How the prose should read (calibration from NLnet's own material)

This matters as much as content, and it is the section where an AI-assisted draft is most obvious.

- **Short and to the point wins.** The form says *"be short and to the point… submitting a proposal can be quick!"* and the FAQ says you *"should be able to complete a proposal in less than an hour"*. The ~18,000-character total is a **ceiling, not a target**. [VERIFIED https://nlnet.nl/propose/ + https://nlnet.nl/restack/faq/]
- **A real submitted application is terse.** NLnet publishes a Forgejo NGI0 application (€50,000) that is a handful of bullet lines per field, not an essay. Read it as your calibration target: https://codeberg.org/forgejo/sustainability/raw/branch/main/2025/2025-08-01-nlnet-ngi0-commons-federation/application.md
- **"A new project with unknown contributors is a gamble."** That is NLnet in its own words, and it tells you the 2,000-character **Background** field carries more weight for you than for an established team. Prior shipped work, a public repo, and named collaborators belong there. [VERIFIED https://nlnet.nl/officehour/#relevant]
- **Budgets are checked for frugality by an independent committee member** — *"At least one of its members independently validates that… budgets are frugal"*. [VERIFIED https://nlnet.nl/restack/guideforapplicants/]
- **Accessibility is effectively a deliverable.** The sample MoU contains a *"Certified WCAG accessible"* milestone, and NLnet offers a free accessibility audit via HAN University of Applied Sciences. Include an accessibility task; it is free, it scores, and it is right. [VERIFIED https://nlnet.nl/restack/faq/#accessibility + sample_MoU.pdf]
- **Disclose any patents or competing commercial interests.** The FAQ says patents must be disclosed at application stage. [VERIFIED https://nlnet.nl/restack/faq/#patents]

---

## 7. Missing assets — and which ones you can fix in 24 hours

| Asset | Fixable today? | Effort | Value |
|---|---|---|---|
| One letter of support from a real pilot organisation | **Yes** — email tonight | 1 h | 🔥 highest |
| A clean public MeshDoc repo with licence + README | Yes | 1–2 h | high |
| A one-page project website (GitHub Pages is fine) | Yes | 45 min | medium |
| Named pilot partner (even without a letter) | Yes | — | high |
| Decided open-source licence | Yes | 10 min | required |
| A working demo / prototype | **No** — do not fake it | — | — |
| Published benchmark numbers | No | — | frame as targets |

---

## 8. The next 25 hours — plan in Nepal time

Deadline: **16:45 NPT on 3 November**. Work backwards from **14:00 NPT tomorrow**, so you are never typing at 16:40. All times below are Nepal time.

**Today (2 Nov, from ~16:00 NPT)**
- **Now → 17:00** — Email 3 potential pilot organisations for a one-paragraph letter of support. Nepali NGOs/agencies respond fast to a short, specific ask; ask for a reply by 10:00 tomorrow. Keep your message to five sentences. (Highest-leverage hour of the whole exercise.)
- **17:00 → 18:30** — Create the MeshDoc repository. Add licence, README (your words), and the design spec, cleaned per §4. Push it.
- **18:30 → 19:30** — Read `research/FUND_RULES.md` §6 and `research/LANDSCAPE.md`. Then **close them.**
- **19:30 → 22:30** — **Write the 7 form fields yourself**, in your own words, in a plain text editor. Use `submission/FIELD_PACK.md` only as a checklist of *what each field must contain*. Aim short: most fields will be better at 60–70 % of the character limit than at 100 %. Summary by 22:30, effort and comparison by 23:30, challenges by 00:30.
- **22:30 → 23:00** — **Submit version 1.** Do not polish. Submitting early converts deadline panic into iteration, and only the last complete version counts.
- **Then sleep.** The challenges field is where clarity matters most and it is the field most damaged by fatigue.

**Tomorrow (3 Nov)**
- **07:00 → 08:30** — Read version 1 cold. Cut 20 % of the words. Fix anything that does not sound like you. Tick every item in §4 of this brief.
- **08:30 → 10:00** — Read `research/TECHNICAL_CASE.md` and `research/BUDGET_AND_MILESTONES.md`; **re-derive every sum yourself**; make the numbers consistent across fields.
- **10:00 → 11:30** — Attach the support letter if it arrived. Fill the AI disclosure truthfully. Final consistency pass with `submission/FIELD_PACK.md`.
- **12:00 → 13:00** — **Submit the final version.** Then stop editing.
- **Hard stop: do not touch it after 14:00 NPT.** That leaves 2 h 45 m of buffer for the form or the network to misbehave.

---

## 9. Submission mechanics worth knowing

- The form asks: fund · title · project website/repos · summary (1,000 ch) · effort & budget breakdown with rate (4,000) · comparison with other efforts (4,000) · technical challenges (4,000) · ecosystem & users (2,000) · background/experience (2,000) · other funding (1,000) · attachments (optional, ≤50 MB) · AI disclosure (8,000 + upload) · contact & applicant type. [VERIFIED https://nlnet.nl/propose/]
- **Applicant type** for you: `SME company` (Arvion Technologies) — or `Individual` if you prefer to apply personally. Both are explicitly allowed; no legal entity is required to apply. [VERIFIED Restack FAQ]
- **Payment is per milestone, in arrears**, allocated by you across milestones. Use 4–5 milestones. [VERIFIED Restack FAQ]
- **Anonymity is possible** before award; irrelevant for a company application.
- **Assessment takes 3–5 months** from the deadline, not from submission.
- **Stage 2 is interactive**: reviewers ask clarifying questions and will check claims independently. Expect to be asked "what is the difference to Automerge/Briar/KoBo", "how do you back up the 15 mW claim", "is this rate justified", "how is this sustainable". Having read §5 and §6 is your preparation.
- **If rejected**: next call is January 2027 and the cycle is fast. A rejection with reviewer feedback is worth more than a month of guessing — treat this as attempt one of two.

---

## 10. Your idea — the honest assessment

**What is strong:** the problem is real and you are from where it is real; the "library stack first, app second" framing is exactly what NLnet rewards; the scope-exclusions list is genuinely good and reviewers do reward it; the mesh/DTN/CRDT combination is coherent; and there is a real gap in the stack.

**What was weak:** an AI feature that would have got you screened out; a workspace-id/key-rotation bug; a confused membership model; three unmeasured physics claims; a relay described so modestly it sounds trivial; and a relevance argument aimed at beneficiaries rather than at the stack.

**What is still missing and I cannot do for you:** a named pilot partner, a repository you wrote, and your own voice describing why *you* are the person to build this. Those three are what turn a well-scoped idea into a credible application.

---

## 11. The boundary — what this pack is and is not

NLnet v2.0 forbids AI-written proposals, and the penalty is rejection. So this pack deliberately contains **research, rules, evidence, arithmetic and checklists — not answer text**. `submission/FIELD_PACK.md` tells you what each field must accomplish and which verified facts belong in it; it does not contain paragraphs you can paste, because pasting is what the policy names.

If you used any AI in preparing this (this session included), the honest thing is to disclose **research/reference assistance** in the AI-disclosure field, describe it at a high level, and state that the proposal text is your own. If you would rather not rely on it at all, the research pack still stands on its own as public-source fact — you have simply skipped three days of reading.

## 12. Files in this pack

| File | What it is |
|---|---|
| `COMPLIANCE_AND_STRATEGY.md` | This document — read first, then don't reread |
| `research/FUND_RULES.md` | Verified fund rules, eligibility, scoring, exact quotes |
| `research/LANDSCAPE.md` | Prior art, competitors, licences, NLnet neighbours, upstream plan |
| `research/TECHNICAL_CASE.md` | Architecture, design decisions, hard problems, acceptance criteria |
| `research/BUDGET_AND_MILESTONES.md` | Rate research, 3 budget scenarios, WPs, timeline, milestone payments |
| `submission/FIELD_PACK.md` | Field-by-field requirements checklist + the facts that belong in each |
| `submission/CLAIM_LEDGER.md` | Every factual claim you may make, with a verifiable source |
| `submission/PRE_SUBMIT_CHECKLIST.md` | 15-minute final gate |
| `repo-template/` | Licence texts, `.gitignore`, issue templates for the MeshDoc repo |
