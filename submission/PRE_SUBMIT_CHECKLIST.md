# Pre-submit checklist — 15 minutes, before you press Submit

Print this. Tick it. Do not submit without it.

**Deadline: 2026-11-03 12:00 CET = 11:00 UTC.** Submit by **09:30 UTC** to leave buffer.
You may resubmit; the last complete version before the deadline is the one assessed.

---

## A. Knock-out gates (fail any one → never reviewed)

- [ ] **Fund selected = Restack Fund** (not "Other / open call")
- [ ] **No AI/machine-translation/LLM feature anywhere in the proposal.** Search your draft for: `translation`, `translate`, `language pack`, `on-device model`, `AI`, `ML`, `neural`, `LLM`. Every hit must be deleted or be a plain i18n/Unicode reference.
- [ ] **European dimension addressed.** One sentence that the applicant and team are in Nepal, which is on the Horizon Europe-eligible list, and that the work is executed in Nepal. Do not apologise for it.
- [ ] **Primary objective is research and development** — the text reads as "we will design and build X", not "we will operate a service" or "we will run a pilot" (pilot is evidence, not the objective).
- [ ] **A recognised open-source licence is named** and the repo has a `LICENSE` file.
- [ ] **Language:** English throughout, and created by a human. Your own words.

## B. The GenAI disclosure

- [ ] You wrote the answer text yourself.
- [ ] AI-disclosure field answered truthfully — "No" for *writing*, plus a short high-level note if you used AI for research/reference material (the policy asks for transparency about any use).
- [ ] You did **not** tick "Yes, I used generative AI in writing this proposal" (that discloses a prohibited act unless the accessibility exception applies).
- [ ] The codebase question answered truthfully.

## C. Content completeness (all 7 answer fields)

- [ ] **Title** names the artefact and the category; no superlatives; no "AI".
- [ ] **Summary** ≤1,000 chars and contains: what is built, the gap, the mechanism, who benefits, what exists at the end.
- [ ] **Effort/budget** within €5,000–€50,000; per-task effort; **explicit rate and its derivation**; itemised expenses; total sum correct.
- [ ] **Comparison** names Automerge/Yjs, a mesh messenger (Briar or Meshtastic), and the field-data status quo (KoBoToolbox/ODK), and states what is different — accurately.
- [ ] **Challenges** names ≥8 real risks, each with why-hard + mitigation; includes the Android background-execution risk and the BLE/Wi-Fi-Direct feasibility risk with a fallback.
- [ ] **Ecosystem** names users, dependencies (including upstream projects you build on), and concrete engagement.
- [ ] **Background** gives 2–3 verifiable specifics, not a CV dump; says why you and why Nepal.
- [ ] **Other funding** answered — "none" is fine and better than silence.

## D. Claims discipline

- [ ] No claim of a working prototype you do not have.
- [ ] Performance figures (idle mW, latency, convergence counts) are framed as **targets with a measurement method**, not as results.
- [ ] Workspace id does **not** derive from the workspace key (key rotation would break it).
- [ ] Membership model stated consistently — signed membership log, not "possession of the key" *and* "set of public keys".
- [ ] Sybil/member-removal claims are precise: attribution yes; revocation of already-seen plaintext no.
- [ ] Relay threat model admits pseudo n metadata leakage and names the mitigation.
- [ ] Every named project is described accurately enough to survive a fact-check.

## E. Numbers and consistency

- [ ] Budget sums re-derived with a calculator — every subtotal and the total.
- [ ] Total figure identical in summary, effort field, and any attachment.
- [ ] Milestone count and names identical wherever they appear.
- [ ] Licence name identical in repo, summary, comparison.
- [ ] Timeline months sum to the period you claim.
- [ ] Rate × days = subtotal, for every line.

## F. Assets

- [ ] Repository URL opens, is public, has `LICENSE` and an honest README with a status line.
- [ ] Repo README separates *what exists* from *what the grant funds*.
- [ ] Support letter attached if you received one.
- [ ] One architecture diagram attached at most — nothing else.

## G. Mechanical

- [ ] Name, email, phone with country code filled in.
- [ ] Applicant type chosen (`SME company` for Arvion, or `Individual`).
- [ ] Country = Nepal.
- [ ] You are submitting **before 09:30 UTC**.
- [ ] You saved a copy of the submitted text and the timestamp in `submission/SUBMITTED.md`.
- [ ] **You stop editing after submitting the final version.**

---

## The one thing to remember if you only have ten minutes

Two edits matter more than everything else on this list:

1. **Remove the translation/AI feature.** One AI feature marks the application out of scope for Restack.
2. **Make the relevance case about the stack**, not only about disaster victims: the open stack has message tools and server-centric document tools, and nothing in between. MeshDoc is that middle layer, released for others to reuse.

Everything else is polish.
