# Submission field pack — requirements, traps, and facts to draw on

**Purpose:** a checklist for each field of the NLnet application form, so you can write your answer once and have it be complete.
**This contains no answer text.** Write your own words — NLnet policy v2.0 forbids AI-written proposals, and the penalty is rejection. Use this to make sure your answer is *complete*, not to source sentences.

**Form:** https://nlnet.nl/propose/ — character limits are enforced by the form.

---

## Field 1 — Select a fund
**Choose: `Restack Fund`.**
Rationale is in `COMPLIANCE_AND_STRATEGY.md` §1. Do not choose "Other / open call": Restack is the fund whose call text names local-first infrastructure explicitly, and it is the fund with a deadline tomorrow.

---

## Field 2 — Proposal title
**Limit:** one line. **Weight:** low, but it is the first thing read.

What a good NLnet title does: names the artefact, not the dream. Avoid superlatives and avoid "MeshDoc: A Revolutionary…".

Include, in some order: the project name, the technical category, and the deliverable form (library/stack). Mentioning "offline-first" or "local-first" and "encrypted" is worth it because it maps straight onto the call text.

**Trap:** do not put "AI" or "translation" in the title. See §3 of the strategy brief.

---

## Field 3 — Project website(s) / repositories
**Weight:** medium — reviewers *do* click. This field is where an empty or confused repo costs you.

Requirements:
- One URL that a reviewer can open and immediately understand what exists today.
- A **LICENSE** file that is a recognised open-source licence (see `repo-template/`). "All rights reserved" or no licence = ineligible, since the fund requires release "under a recognised open source license in its entirety".
- A README that separates **what exists** from **what the grant would build**. Do not let the reviewer guess.
- If your GitHub has many unrelated demo repos, don't link the profile — link the one repo.

**Trap:** linking a profile page that looks like a portfolio of generated case studies dilutes the signal. One clean repo beats ten.

---

## Field 4 — Project summary
**Limit:** 1,000 characters. **Weight:** this is what most reviewers read most carefully. It is also the field that gets you classified as "AI project" if you are careless.

Must accomplish, in ~150 words:
1. What the artefact is (a reusable library stack + reference Android client).
2. The gap it fills, in one clause (no serverless encrypted layer for *structured documents*).
3. The mechanism (CRDT changes, E2E encrypted, syncs over BLE/Wi-Fi Direct mesh and opportunistically via an anyone-can-host relay).
4. Who benefits (field teams: disaster response, health workers, NGOs — and the open stack generally).
5. What will exist at the end (released libraries under a named licence + a field-tested app + the relay).

**Traps:**
- No on-device translation, no language packs, no AI. One sentence maximum about the text stack, and it must be about Unicode/i18n rendering, not models.
- Avoid "revolutionary", "game-changing", "first ever". Reviewers discount all three.
- Do not claim a working prototype you do not have. If there is a spec and no code, say "the design is specified; the grant funds the implementation".
- Character budget is tight. Spend it on the stack, not on the earthquake story — the story belongs in the ecosystem/impact answer.

---

## Field 5 — Proposed effort (budget + breakdown)
**Limit:** 4,000 characters. **Weight:** 30 % of the score (cost effectiveness / value for money).

Must include, explicitly, because the form asks for it:
- **Total amount requested** in EUR, within €5,000–€50,000 for a first grant.
- **A breakdown by task** with (roughly) time/effort for each.
- **The rate you used** — hourly, daily or monthly — and *how it was derived*. NLnet pays cost-recovery, not commercial rates, so a consultancy day rate will be challenged in round two.
- **Any expenses**, itemised and small (test devices, a VPS, domain, CI).

Structure that survives review: 5–7 work packages → person-days each → subtotal → expenses → total, with the arithmetic visible. Tie each work package to a milestone so the payment schedule is obvious (payment is per milestone, in arrears).

**Traps:**
- A total that reads as a round "€50,000 because that is the cap". Ask for what the work costs.
- Missing rate justification — the Guide warns reviewers ask "the rate you have applied for task B is very high compared to the perceived value".
- **The €65/hour ceiling.** It is real, and the Office Hour says using it *reduces your chances*. Price well below.
- **Ineligible expenses that are tempting to include** — do not list any of these:
  - phones, laptops, workstations (explicitly excluded as "basic operational IT cost")
  - VPS, hosting, compute ("we are not generally able to fund hosted instances of software, or cover hosting costs")
  - work already completed ("We cannot make donations for any effort completed prior to the grant")
  - event sponsorship, advertising, company registration
- **The relay must be presented as code to develop, not a service to operate.** Hosting is ineligible; funding the code is not. One sentence of framing decides this.
- No mention of what NLnet's *free support services* replace (security audit, accessibility scan, licensing advice) — saying you will use them shows you read the fund, and saves budget. The sample MoU contains both an accessibility milestone and a "process issues from external security review" milestone; both are cash-free for you.

Draw the numbers from `research/BUDGET_AND_MILESTONES.md`, but **re-derive every sum yourself**. A budget that does not add up is the fastest way to lose the cost-effectiveness third.

---

## Field 6 — Comparison with other efforts
**Limit:** 4,000 characters. **Weight:** feeds relevance (40 %) and technical excellence (30 %).

The Guide says round two commonly asks *"what is the difference in approach to existing projects U, V and W"* — so answer it before they ask.

Cover, with named projects (URLs/licences in `research/LANDSCAPE.md`):
- **CRDT/sync libraries** (Automerge, Yjs, Loro) — you use one of these rather than writing your own; say which and why. The differentiator is that they are transport-agnostic data structures with no identity, membership, encryption boundary, discovery or relay.
- **Mesh messengers** (Briar, Meshtastic, SimpleX) — carry messages, not convergent structured documents; assume live sessions rather than anti-entropy over intermittent contact.
- **Field-data status quo** (KoBoToolbox / ODK, DHIS2, Ushahidi) — server-centric; the server is the thing that fails in your scenario. This is your most persuasive comparison because it is what your users actually use today.
- **Disaster platforms** (Sahana, HOT OSM, ATAK) — different layer; interop rather than competition.
- **Standards you align with** — MLS (RFC 9420) as the long-term group-key path, and Bundle Protocol concepts (RFC 9171) for the relay. Naming standards you *build toward* is rewarded.
- **What you will contribute back** — at least three concrete upstream contributions (a reusable transport crate, a partition-fuzz test harness, CRDT schema-migration write-up). The form asks *"have you considered contributing to any of the others?"* — so actually answer it: which projects, what contribution, and whether you have made contact.

**Traps:**
- Claiming novelty for components that already exist (you are not writing a CRDT — do not imply you are).
- Dismissing incumbents. Reviewers may know the KoBo team. Position as complementary.
- Listing projects you clearly have not looked at. Every named project must be described accurately — the Guide says they *independently verify facts and claims*.

---

## Field 7 — Technical challenges
**Limit:** 4,000 characters. **Weight:** 30 % technical excellence/feasibility — and this is the field that most distinguishes a real engineer from a pitch.

What makes this field score: naming a hard problem *precisely*, explaining why it is hard, and stating your mitigation plus how you would know you failed.

Include at minimum (details in `research/TECHNICAL_CASE.md` §3):
1. **Android background execution vs. the idle-energy target** — Doze, App Standby buckets, foreground-service constraints; the OS may forbid the thing the design needs.
2. **BLE discovery privacy** — static identifiers are trackable; rotating identifiers break reconnect logic.
3. **Wi-Fi Direct reliability across OEM Android** — group formation, group-owner negotiation, vendor divergence.
4. **CRDT growth over long partitions** — tombstones and metadata; compaction must not break convergence.
5. **Schema migration that commutes with merge** — replicas on different app versions must still converge.
6. **Key rotation during partition** — a removed member keeps the old key and can read data encrypted under it; partitioned members never learn of the rotation. Say what rotation does and does not achieve.
7. **Relay metadata leakage** — stable workspace pseudonyms, size/timing correlation; rotating mailbox ids as mitigation.
8. **Membership authentication without a server** — a signed append-only membership log and how "was this key a member when it authored this change?" is answered causally.
9. **Testing convergence credibly** — how you generate random partition/merge schedules and what your oracle is; plus differential testing against a second implementation.
10. **Blob transfer under tiny bandwidth** — prioritisation and fairness so documents sync before photos.

**Traps:**
- A challenges section that is really a feature list. Each item needs a *risk*, not an achievement.
- Hiding the risk that the FOSS BLE/Wi-Fi Direct path might not be feasible. State the fallback (Nearby Connections behind the transport trait as a development-only path) — a reviewer trusts a team with a fallback more than one with no risk.
- Anything that reads as AI/translation.

---

## Field 8 — Ecosystem and engagement
**Limit:** 2,000 characters. **Weight:** part of relevance (40 %).

Must answer the four questions the form asks:
1. **What is the ecosystem** — the local-first community, the CRDT library maintainers you build on, humanitarian/field-data practitioners, the F-Droid/Android FOSS world, and the standards bodies whose work you align to.
2. **Who depends on whom** — state the direction honestly: you depend on the CRDT library and on libsodium; others will depend on your transport and relay work. Naming your dependencies accurately is a credibility signal.
3. **Who the main users are** — be specific: field teams in disaster response, community health workers, NGOs, plus the *builders* who reuse the libraries. Name the organisation you have a letter from, if you get one.
4. **How you will engage actors** — concrete: an upstream contribution per quarter, filing issues/PRs with the CRDT project, a field pilot documented publicly, presenting at a local-first or FOSS event, and taking up NLnet's own support services (security audit, accessibility scan).

**Trap:** generic "we will post on social media" engagement. Name channels and cadence, and name real people/organisations where you can.

---

## Field 9 — Background / why you
**Limit:** 2,000 characters. **Weight:** indirect but decisive at the margin.

What reviewers want: evidence you can actually ship this. Cover:
- Relevant experience: Rust, Android, and specifically anything distributed-systems, crypto or offline-sync shaped. Point at real repos, real shipped work, real clients.
- Why you, why here: you are in Kathmandu; the problem is not hypothetical for you. That is a genuine advantage — state it once, without pathos.
- Who else is on the team and what they do, if more than one person.
- Evidence of working with others in the open: upstream contributions, issue threads, code review.
- Commitment: this is the work you want to do, not a contract.

**Trap:** a CV dump. Two or three concrete, verifiable examples beat a list. If your public GitHub is a large portfolio of similar demo repos, lead with your *specific* relevant work instead (e.g. the `sync-kit` offline-sync work — describe it honestly as an operation-log/vector-clock sync kit and say what it taught you about the problem).

---

## Field 10 — Other funding
**Limit:** 1,000 characters.

State plainly whether the project has other funding. If not, say no — that is normal and expected for a first NLnet grant. If you have any commercial interest in the outcome, disclose it (NLnet is fine with companies applying, but transparency about competing interests protects you later).

**Trap:** silence reads worse than "none". This is a trust field.

---

## Field 11 — Attachments
Optional, ≤50 MB, but **use it**: a one-page PDF or image of a letter of support from a pilot organisation is the single most persuasive supplementary item you can add. Also fine: one architecture diagram. Nothing else — the form says attachments are not needed and it wants the proposal self-contained.

---

## Field 12 — AI disclosure
**Limit:** 8,000 characters + optional upload.

Read `COMPLIANCE_AND_STRATEGY.md` §2 before filling this in. The truthful, defensible answer is one of:
- **"No, I did not use generative AI in writing this proposal."** — correct if the text is yours, which it must be. If you used AI for background research only, this is still the right answer for the *writing*, but see the next point.
- Transparency is required for any use at all. If you used AI to gather reference material or check your own claims, say so at a high level in the disclosure text: what you used, for what, and that the proposal text and technical decisions are your own. This is honest, it is not the banned use (writing), and the policy explicitly asks for transparency about read-only uses.

**Never** tick "Yes, I have used generative AI in writing this proposal" unless the accessibility exception genuinely applies — under v2.0 that is a disclosure of a prohibited act.

Also answer the codebase question truthfully: does the MeshDoc codebase contain AI-generated code? If you have not written it yet, the answer is no — and keep it that way, because the project-execution rule forbids GenAI-produced artefacts.

---

## Cross-field consistency check

Before submitting, confirm these are identical across fields:
- Total budget figure (summary / effort / budget narrative).
- Milestone count and names (effort / timeline / payment schedule).
- Licence name (repositories / summary / comparison).
- Named pilot organisation (ecosystem / background / attachment).
- What exists today vs. what the grant funds — stated the same way in the summary, the background and the repo README.
