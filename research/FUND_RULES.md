# NLnet **Restack** Fund — Exact Rules for the MeshDoc Application

**Prepared:** 2026-11-02 (Asia/Kathmandu)
**Deadline:** **3 November 2026, 12:00 CET (noon)** — that is **16:45 Nepal time (NPT) on 3 Nov 2026**. At the time of writing this is roughly **25 hours away**.
**Tagging convention:** `[VERIFIED from <url>]` = exact quote or fact read directly off that page in this session. `[UNCERTAIN]` = not published, inferred, third-party, or derivable only by reasoning.

---

## 0. Executive summary — the ten things that decide this application

1. **THE BRIEF'S PREMISE IS WRONG: Nepal is fully eligible.** Nepal is explicitly listed by NLnet as a Horizon Europe-eligible country, and on the European Commission's official list Nepal sits among "low- to middle-income countries [that] are automatically eligible for funding". Restack's European-dimension knock-out criterion is therefore **met by a Kathmandu team on the same terms as an EU team**. Do not build a workaround for an ineligibility that does not exist. `[VERIFIED]`
2. **Eligibility is not categorical.** "There are no categorical exclusions of persons who may not receive support from Restack." `[VERIFIED from https://nlnet.nl/restack/eligibility/]`
3. **Generative AI may not be used to write the proposal.** Policy v2.0: "It is **not** allowed to use generative AI during the writing of proposals... This includes LLM generation of ideas, as well as restructuring, shortening and translation." The only exception is accessibility. `[VERIFIED]`
4. **Generative AI may not be used to produce code either.** "It **is not** allowed to use generative AI for producing artefacts of any kind, including code, design, and documentation." Only **read-only** use is permitted. AI-as-"coding partner" is explicitly disqualifying. `[VERIFIED]`
5. **The AI-disclosure field still exists on the form** (8000 chars + file upload) but in practice now only serves the accessibility exception and disclosure of *pre-existing* AI-generated code in the codebase. `[VERIFIED]`
6. **Restack excludes AI projects**: "**AI-related projects are not within scope** — unless they are already widely used throughout society (> 1 million active human users) and directly relevant to the stack." MeshDoc must not be framed as an AI/collaboration-AI product. `[VERIFIED]`
7. **Money:** first grant is **€5,000–€50,000**; max per proposal **€150,000**; lifetime cap **€500,000**. Rates are **cost-recovery, not commercial**, with an **absolute ceiling of €65/hour** ("the absolute maximum rate we can allow for is 65 euro/hour"). `[VERIFIED]`
8. **Scoring is 30% technical / 40% relevance-impact / 30% cost-effectiveness, and you need >5.0 out of 7 to survive round one.** `[VERIFIED]`
9. **It must be R&D, not product development.** A hard knock-out: the proposal "should have **research** and **development** as their **primary** objective". MeshDoc must be argued as R&D contributions to the Open Internet Stack, not as shipping an app. `[VERIFIED]`
10. **Payments are milestone-based arrears, paid as charitable donations (no VAT), and NLnet gives no tax advice.** Grant runs are normally ≤12 months. Allow 3–5 months for a decision. `[VERIFIED]`

---

## 1. The Generative AI Policy v2.0 — full operative text

### 1.1 Source and status

The policy in force is **version 2.0, dated 20 October 2026**.

> **Version 2.0** (October 20, 2026)
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/2.0/]`

**Important sourcing note:** the un-versioned URL `https://nlnet.nl/foundation/policies/generativeAI/` returned **HTTP 200 with a completely empty body** on repeated attempts (both with and without trailing slash) via `web_fetch`. The content is reachable at the versioned URL `/2.0/`, which was discovered from the v1.1 archive page's version-control table. `[VERIFIED — observed behaviour; empty body at /generativeAI/ and /generativeAI (no slash)]`

Version history, verbatim:

> | December 8, 2025 | [Version 1.0] | Initial release |
> | January 26, 2026 | [Version 1.1] | Adjustments based on feedback from grantees |
> | October 20, 2026 | [Version 2.0] | Restrict to read-only |
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/2.0/]`

### 1.2 What is banned for *proposal writing*

> It is **not** allowed to use generative AI during the writing of proposals, nor when providing answers during the interactive evaluation of proposals. This includes LLM generation of ideas, as well as restructuring, shortening and translation. Trust in your knowledge and skills, and use your own words. We don't care about spelling or grammar, only about your ideas.
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/2.0/]`

Note the breadth: **ideas generation is included**, and so are *restructuring, shortening and translation*. "We don't care about spelling or grammar" is the explicit counter-argument to using AI for polish.

Corroborating FAQ ruling on translation:

> **Q: Can I use an LLM for translation?**
> A: No. It is okay to use regular machine translation, but not LLMs. We do understand there can be a language barrier, English is not the native language for most of our staff either. But we don't care about spelling or grammar, only about your ideas.
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/faq/]`

### 1.3 The one exception in the *application* process

> **Accessibility exception**: there is one noted exception where using AI in the application process is allowed, which is in case it is needed for accessibility purposes. People with e.g. a visual or motor impairment who rely on AI-based assistive technology are allowed to use AI. Like any other use of AI, it must always be made transparent. Instructions on how to disclose use of AI when submitting proposals are provided in the [proposal form](/propose/).
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/2.0/]`

This exception also extends to project development:

> **Q: There is an accessibility exception for AI usage in the application process, could a similar exception also be applied to project development?**
> A: Yes, the accessibility exception described in the policy is also valid for project development. For instance, if a motor impairment makes typing difficult, it is allowed to use AI as an assisstive technology. Needless to say, other uses of AI that are restricted by the policy, still remain restricted. And all use of GenAI must be disclosed.
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/faq/]`

### 1.4 The "read-only usage" rule for *project development*

> It **is not** allowed to use generative AI for producing artefacts of any kind, including code, design, and documentation.
>
> It **is** allowed to employ GenAI in a _read-only_ manner — meaning, for instance, that you can have an AI tool check your code and identify security issues and flaws, but that you craft fixes and mitigations yourself, and write your own code. Even if you use GenAI in a read-only manner, you should always be transparent about it.
>
> Technology does not replace human responsibility for project quality, technical choices and thoroughness. Human contributors remain responsible for correctness, clarity, and reproducibility, and are expected to understand and be able to explain design and code decisions.
>
> Costs incurred for AI usage are not eligible for reimbursement.
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/2.0/]`

The FAQ draws the exact boundary — this is the most operationally useful passage in the whole corpus:

> **Q: Analytical support: Would using an LLM to explain existing code, discuss technical approaches, or identify potential bugs and security issues fall within permitted "read-only usage", provided that developers independently assess the output and implement any changes themselves?**
> You can have LLM's look at your code and point out flaws. You have to then write the code to fix it up yourself. Asking an LLM what to do next not allowed, you should yourself build a working solution. Only then can you have it reviewed.
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/faq/]`

So the permitted/forbidden line in practice:

| Permitted (read-only) | Forbidden (generative) |
|---|---|
| AI reviews your code and flags security issues/flaws | AI writes code, design or documentation |
| AI explains existing code to you | AI tells you what to do next / designs the solution |
| AI reviews a solution you already built yourself | AI as "coding partner" |
| AI checks a library recommendation (you still vet it) | AI generates dependencies to build an artificial boundary |

> **Q: We use AI as a coding partner in our development, and we intend to continue doing so. Does our approach make the project ineligible for Open Internet Stack programmes?**
> The short answer is yes. AI as a 'coding partner' is not a development method that is compatible with our current programmes and the genAI policy.
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/faq/]`

### 1.5 Is there still any disclosure mechanism?

**Yes — two separate ones.**

**(a) At application time — the form still contains an "AI disclosure" section.** It asks a yes/no on whether generative AI was used in writing the proposal, an 8000-character free-text field for prompts/interactions and AI output, and a separate 50 MB upload. There is also a second, still-fully-live question about AI-generated code in the codebase with a 1000-character description field. See §4 for the exact field list. `[VERIFIED from https://nlnet.nl/propose/]`

Mandatory codebase disclosure in the policy itself:

> In your application you **must** disclose if your proposal builds on an existing codebase that already includes a significant amount of code generated by AI, or expects to gain a significant amount of such code during the lifetime in other ways than through the grant.
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/2.0/]`

**(b) During the project — public transparency.** This is mandatory and survives into v2.0:

> Provide at the **very minimum** a **high-level description** of all known (past and present) use of GenAI. This means summarising the general stance towards generative AI at the project level in the README, man/info pages, and your website. Even better in terms of transparency is publishing your own policy for contributors, outlining do's and don'ts with regards to the use of GenAI — and of course upholding that policy.
>
> As a matter of project hygiene, we additionally recommend (so this is not mandatory but a 'best practice') a **per commit disclosure**:
> - Ask all contributors to disclose at the granularity of individual contributions which model(s) was/were used, which version(s), and a brief description of how GenAI assisted the contributor.
> - Make this information available in machine-readable format in the commit logs.
> ...
> - Consider that the use of proprietary/as-a-service AI may create a social lock-in for other (current and future) contributors to your project, and may create a long term dependency.
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/2.0/]`

Note the downgrade from v1.1: per-commit disclosure moved from *required* (with a prompt-provenance log listing model, dates/times, prompts and unedited output) to *recommended best practice*. The README-level high-level statement remains mandatory. `[VERIFIED — v1.1 text at https://nlnet.nl/foundation/policies/generativeAI/1.1/ vs v2.0 text above]`

**Pre-existing AI code does not disqualify the project**, it only must be disclosed:

> **Q: Will my proposal be disqualified if my codebase contains pre-existing LLM-generated code?**
> A: No. But you do need to disclose pre-existing LLM-generated code in the application form. There is an 'AI disclosure' section in the form.
>
> **Q: If significant AI-generated contributions are known to exist in the pre-existing codebase, would this require disclosure and assessment, or would it make the proposed project ineligible?**
> A: It would not render the project ineligible, but it would require disclosure.
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/faq/]`

And the citable "we can't guarantee the upstream history" answer, which is likely relevant to a project building on existing CRDT libraries:

> **Q: Our project extends an existing open source codebase. We cannot independently guarantee that third-party contributors never used generative AI...**
> A: Good question. Yes this is permissible. First, because having pre-existing LLM-generated code in the codebase, does not render the project ineligible. And second, we understand it is not always possible to know whether or not there is LLM-generated code in the codebase, so we understand you can not always guarantee it.
> […] **What checks or disclosures would you expect in this situation?**
> Answer: Just write it down as you have done here: stating that you don't know and why you don't know.
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/faq/]`

### 1.6 What happens to non-compliant applications

> Failure to comply may result in rejection of the proposal, submitted work not being accepted for payment, or ultimately in the termination of the running grant.
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/2.0/]`

The older FAQ adds a reputational warning (this page is the Restack FAQ, still live):

> If you do use generative AI to write (part of your) proposal, please put this in the text and explain why this was necessary. Failure to do so is likely to result in the proposal being rejected, and tarnishing your reputation.
> `[VERIFIED from https://nlnet.nl/restack/faq/#AI]`

And the application form itself restates it:

> Proposals and projects should be made **by humans, not AI**. See our [Generative AI policy](/foundation/policies/generativeAI/).
> `[VERIFIED from https://nlnet.nl/propose/]`

### 1.7 Effective date and applicability — this call IS covered

> The updated policy is **effective immediately**, and applies to **all open calls** from NLnet which have their deadline later than the **publication date** of the new policy. This includes the upcoming calls of Restack and CodeSupply, which have their first deadline on November 3rd 2026.
> `[VERIFIED from https://nlnet.nl/news/2026/20261020-AI-policy.html]`

### 1.8 ⚠️ Direct consequence for our own working method

Because AI may not be used to write this proposal — including for "restructuring, shortening and translation" or "generation of ideas" — any drafting assistance on the MeshDoc proposal text itself must be treated as non-compliant, unless it falls under the accessibility exception. Research, gathering quotes, and checking facts (what this document does) is not covered by the policy's prohibition, which is scoped to "the writing of proposals" and "artefacts". **The proposal prose must be written by the human applicants in their own words.** `[VERIFIED — derived directly from the quoted policy text; the interpretive line is flagged as an interpretation]`

---

## 2. Restack eligibility, the European dimension, and whether Nepal can apply

### 2.1 Bottom line

**Nepal-based applicants are eligible, and Nepal satisfies the European-dimension knock-out criterion on the same footing as an EU member state.** This is established at three independent levels: NLnet's own country list, NLnet's Office Hour ruling on an identical country category, and the European Commission's source list that NLnet declares authoritative.

### 2.2 No categorical exclusions

> ### Definition of persons or categories of persons which may receive financial support
>
> There are no categorical exclusions of persons who may not receive support from Restack.
>
> The project must however, have a strong ['European dimension'](/OIS/european-dimension/). The obvious way to fulfil this requirement is having people on the team of the proposed project from [Horizon Europe-eligible countries](/OIS/european-dimension/#countries), who receive at least 60% of the funds. However if the project is of exceptional quality and the proposer holds unique technical expertise proposals from outside of those geographic areas can be taken into consideration.
>
> Young people that have not yet reached the age of legal consent in their country of origin (typically 18 years old) on the date of the deadline may apply without any constraints; consent from a legal guardian such as a parent does not have to be provided prior to initial submission, but will be required to enter any further negotiations.
> `[VERIFIED from https://nlnet.nl/restack/eligibility/]`

Note the structure: there is a **primary route** (≥60% of funds to people from Horizon Europe-eligible countries) and a **discretionary fallback** (exceptional quality + unique technical expertise). Nepal does not need the fallback.

### 2.3 Nepal is on NLnet's own Horizon Europe-eligible list

From NLnet's European-dimension page, in the country list which NLnet says was "last updated on October 13, 2026":

> − Namibia, **Nepal**, Netherlands, New Caledonia, New Zealand, Nicaragua, Niger, Nigeria, North Macedonia, Norway
> `[VERIFIED from https://nlnet.nl/OIS/european-dimension/ — "Nepal" appears in the list headed "List of Horizon Europe-eligible countries constituting a European dimension"]`

And the crucial interpretive sentence on the same page:

> Note that there are _many_ eligible countries, many of which are not European countries. People and organisations of these [eligible countries](#countries) can participate _on the same terms_ as those from EU member states. Having 60% of the funds go to people from any of these countries, meets the European dimension criterium. (We emphasise this because we get a lot of [questions](/officehour/#european) about it.)
> `[VERIFIED from https://nlnet.nl/OIS/european-dimension/]`

Also essential — the European dimension attaches to **people, not to the project**:

> The European dimension refers to the people contributing to the project, not the project itself. The obvious way to fulfil this requirement is having people on the team of the proposed project from Horizon Europe-eligible countries, who receive at least 60% of the funds. The project itself being beneficial to the EU is not enough to constitute a European dimension.
> `[VERIFIED from https://nlnet.nl/OIS/european-dimension/]`

### 2.4 Primary source verification: the European Commission list

NLnet states "in case of discrepancies, the EC lists are leading" `[VERIFIED from https://nlnet.nl/OIS/european-dimension/]`. I therefore downloaded and extracted the EC document itself (PDF, V4.2 – 07.10.2026, 7 pages, extracted with `pdftotext`).

Under the heading **"Other third countries"**, the document reads:

> Participants from the following low- to middle-income countries are automatically eligible for funding⁶:
> […]
> − Namibia, **Nepal**, Nicaragua, Niger, Nigeria
> `[VERIFIED from EU Grants: List of participating countries (HE): V4.2 – 07.10.2026, https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/common/guidance/list-3rd-country-participation_horizon-euratom_en.pdf, downloaded and text-extracted this session; footnote 6 reads "Subject to the respect of EU restrictive measures"]`

So Nepal is **not** merely "associated" or "tolerated" — its participants are **automatically eligible for funding**.

### 2.5 The decisive NLnet precedent — an applicant from the same country category, as sole/lead applicant, to Restack

This Office Hour Q&A is the single most on-point ruling available:

> **Q:** I would like to clarify how the European Dimension requirement applies to applicants from Horizon Europe-eligible but non-associated countries. The official Horizon Europe country list linked directly from the NLnet proposal form (version 4.1, dated 16 September 2026) includes Kazakhstan among the non-associated low- and middle-income countries whose participants are automatically eligible for funding. **Does this mean that an individual resident in Kazakhstan may apply as the sole or lead applicant to Restack without an EU-based co-applicant?**
> A: **Yes, they would be automatically eligible for funding.**
> `[VERIFIED from https://nlnet.nl/officehour/#european]`

Kazakhstan and Nepal appear in the **same** EC paragraph list ("− Kazakhstan, Kenya, Kiribati..." and "− Namibia, Nepal, Nicaragua, Niger, Nigeria"), i.e. the identical legal category: *non-associated low/middle-income third country, automatically eligible for funding*. The reasoning therefore transfers directly. **A Kathmandu-based individual or team may apply as sole/lead applicant to Restack.** `[VERIFIED for each component; the transfer of the ruling from Kazakhstan to Nepal is an inference from the identical EC category — flagged as strong but an inference]`

Additional confirmations from the same archive:

> **Q: Can anyone in the whole world submit?** (Restack FAQ)
> If the project you are are considering would be a significant advance towards establishing an Open Internet Stack, we invite you to submit — even if you live outside of Europe. Of course, it remains competitive — but you would expect that from money you get for doing what you love to do.
> `[VERIFIED from https://nlnet.nl/restack/faq/]`

> **Q: Is the European dimension assessed uniformly across the new funds, or does its weight vary between them?**
> A: Its assessed uniformly across the new funds
> `[VERIFIED from https://nlnet.nl/officehour/#european]`

> **Q: European dimension: when a project is led by an applicant outside the EU and Horizon Europe associated countries, is the often-cited 60% European participation threshold calculated by the share of requested funding, work effort, or milestone ownership?**
> A: **Requested funding.**
> `[VERIFIED from https://nlnet.nl/officehour/#european]`

That last one matters practically: if a Nepali team ever *did* need to add European participants, the 60% test is measured on **money**, not hours — so a European co-applicant would need to receive ≥60% of the requested budget.

### 2.6 The form's own wording on this

The proposal form contains a conditional instruction which confirms NLnet treats "not from a Horizon Europe-eligible country" as a separate, argued case:

> If you apply for an EU-funded programme but you are not from a [Horizon Europe-eligible country](/OIS/european-dimension/), please clarify how your project might satisfy the 'European dimension' requirement in the [background](#background) question above. (e.g. European citizenship).
> `[VERIFIED from https://nlnet.nl/propose/]`

Since Nepal **is** Horizon Europe-eligible, this instruction **does not apply** to the MeshDoc team. `[VERIFIED — logical consequence of the quoted list]`

### 2.7 ⚠️ Residual risk and how to neutralise it

Although the rules are clear, Restack is a *new* programme, the first call has no precedent projects, and reviewers are fallible. Two cheap insurances, both recommended:

1. **State the eligibility positively and early.** Put one sentence in the *Background* answer along the lines of: "Our team is based in Nepal, which is on the European Commission's Horizon Europe list of low- and middle-income third countries automatically eligible for funding (EU Grants list V4.2, 07.10.2026), so the European-dimension criterion is met on the same terms as an EU member state — see nlnet.nl/OIS/european-dimension/." `[Recommendation — not a rule]`
2. **Optionally add a European collaborator or advisor** (e.g. an EU-based security reviewer or an EU FOSS umbrella). The Office Hour is clear that such involvement is welcome but, for Nepal, **not required**. `[VERIFIED that collaboration is possible; "not required" follows from Nepal's list membership]`

### 2.8 Other knock-out criteria to respect

From the Guide for Applicants, first-stage "hard eligibility (knock-out)" checks:

> Based on the submitted proposals, projects receive a first check for **eligibility** in terms of alignment of goals and criteria with the sub-granting call. In this stage hard eligibility ("knock-out") criteria specific to the sub-granting call are checked. Project proposals are written in English and:
> - should be in line with the goals of _Restack_ and the sub-granting call applied for
> - should have **research** and **development** as their **primary** objective
> - should satisfy any other hard eligibility criteria specific to the sub-granting call, such as having a clear ['European Dimension'](/OIS/european-dimension/).
>
> All projects that fail on any of these knock-out criteria, will **not** be further reviewed and will be marked ineligible.
> `[VERIFIED from https://nlnet.nl/restack/guideforapplicants/]`

**MeshDoc implication:** the "research and development as primary objective" line is a real risk for a project that reads like "build an app for Android". The proposal must foreground the *research questions and engineering contributions* (CRDT convergence under mesh partition, E2EE group-key management over BLE/Wi-Fi Direct, relay-blind ciphertext routing) and treat the Android app as the vehicle. `[Interpretation, derived from the quoted knock-out criterion]`

---

## 3. Grant amounts and the cost-recovery rate rules

### 3.1 The amounts

First-grant band, from the application form field itself:

> **How much money** do you request for your project?
> In Euros. **Between € 5 000 and € 50 000 for a first grant.**
> `[VERIFIED from https://nlnet.nl/propose/]`

> **Q: Are you going to spend the whole budget on small projects?**
> Depending on what you call small projects, yes. Your first proposal can only be between 5.000 en 50.000 euro. You can follow up with other project proposals, up to 500.000 euro over the lifetime of the programme. Of course that only makes sense if the idea turns out to be exceptionally good, and you prove the feasibility of your approach — and your ability to execute. But 500.000 euro is the absolute hard limit for any applicant for the programme.
> `[VERIFIED from https://nlnet.nl/restack/faq/ — "en" is a Dutch-for-"and" typo in the original, quoted as published]`

Programme-wide ceilings:

> - a **first proposal** MAY request a grant allocation up to **50 kEuro**. In other words, a proposal larger than 50 kEuro MUST be preceded by one or more smaller projects within _Restack_ or equivalent (such as one of the NGI programmes), which MUST have been successfully concluded before a new project can be granted: this means that the project deliverables have been made publicly available under recognised open/free licenses, that any software artefacts delivered were WCAG compliant, and that the outcomes of the independent security audit have been satisfactorily dealt with.
> - Any project **larger than 50 kEuro** MAY be subject to a full independent security audit at the end, by an independent party allocated by or agreed with _Restack_. Payment of parts of the project grant may be made conditional to the outcome of such an audit, and subsequent adequate handling of issues identified.
> - The maximum amount to be granted per proposal is **150 kEuro**.
>
> ### Maximum amount to be granted to each third party
> The maximum amount to be granted per third party over the lifetime of the _Restack_ programme is 500 kEuro. A third party can be an organisation or an individual.
> `[VERIFIED from https://nlnet.nl/restack/guideforapplicants/]`

Funding envelope: "The [_Restack_ Consortium](../background/#organisation) will competitively award **7 million euro** worth of grants to independent researchers." Programme window "between June 1st 2026 and May 30th 2030". `[VERIFIED from https://nlnet.nl/restack/guideforapplicants/]`

### 3.2 The cost-recovery principle — NLnet does not pay commercial rates

> As a philanthropy, we do not pay commercial rates — we provide a cost-recovery based mechanism, allowing people to freely work on what they believe in.
> `[VERIFIED from https://nlnet.nl/funding.html]`

> A: As a philanthropy, we operate on a cost recovery basis. We do not aim to compete with market rates for commercial clients, but let people be their own boss, work on projects they believe in at their own pace.
> `[VERIFIED from https://nlnet.nl/officehour/#amount]`

### 3.3 ★ The actual number: **€65/hour absolute maximum**

This is the concrete figure the brief asked for. It is published, but only in the Office Hour Q&A archive (not on the Restack guide or eligibility page):

> **Q: W.r.t. rates I presume this has been asked a milion of times but: is there some orientative window for the hourly rate that you consider appropriate? Prices vary a lot in Europe**
> A: As a philanthropy, we operate on a cost recovery basis. **The absolute maximum rate we can allow for is 65 euro/hour**, but using the maximum rate impacts cost effectiveness, and thus can reduce chances of getting the project granted.
> **Q (Follow-up):** A search showed EU Minimum monthly salaries varying between 550 for Bulgaria to 2700 Euros in Luxemborg. Would offering to work for lowest possible hourly rates improve odds? So is doing more for less useful to the NLnet mission?
> A (Follow-up): **We also have a minimum rate.** We evaluate application based on potential impact, and cost effectiveness is just one factor. The best is a good idea and a good plan. And well, it is important for us that people freely and comfortably work on what they believe in; we wouldn't do that job if we just wanted to extract as much work as possible for minimum cost.
> `[VERIFIED from https://nlnet.nl/officehour/#amount]`

The same €65 figure is repeated verbatim in a second Q&A on the same page:

> **Q: Hourly rate guidance: As a freelance developer, my regular consulting rate is around 100 EUR/hour. Is there a recommended rate range for senior developer work in NGI0 Commons Fund applications, or any guidance on what's considered reasonable for open source projects?**
> A: As a philanthropy, we operate on a cost recovery basis. […] The absolute maximum rate we can allow for is 65 euro/hour, but using the maximum rate impacts cost effectiveness, and thus can reduce chances of getting the project granted.
> `[VERIFIED from https://nlnet.nl/officehour/#amount]`

**Notes and caveats:**

- The **minimum rate is explicitly stated to exist but its value is never published**: "We also have a minimum rate." `[UNCERTAIN — value not published anywhere I could find]`
- The €65 cap is corroborated structurally by the external-spending policy, which refers to a fixed ceiling: "NLnet caps hourly rates to a predefined maximum, and from a fairness principle wishes to ensure that these maximum rates are universally applied". `[VERIFIED from https://nlnet.nl/foundation/policies/externalspending/]`
- Practical reading: €65/h is a **hard ceiling that damages your cost-effectiveness score**, not a target. A Nepali team should price well below it. `[Interpretation]`

### 3.4 Rate structure allowed

> **Q: On differentiated hourly rates: "Is it common in the proposals you receive to use differentiated hourly rates depending on the nature of the tasks ; for instance ; ~25 €/h for documentation and ; ~45 €/h for development work, or is a single rate across the whole project preferred?"**
> A: You can have different rates in your project for different tasks.
> `[VERIFIED from https://nlnet.nl/officehour/#amount]`

> **Q: Should the budget be presented with daily rates or as lump sum for every specific item?**
> A: both. An indicative daily rate + lump sums are appreciated.
> `[VERIFIED from https://nlnet.nl/officehour/#amount]`

What reviewers look for in the budget field:

> A: it is hard indeed! What we look for in the budget are:
> - rates that you have applied to the project
> - estimated efforts for the different parts of the project (in hours, or amounts, which may be rough estimates. Either is fine.)
> - understanding a bit what the different parts of development bring to the project.
> `[VERIFIED from https://nlnet.nl/officehour/#amount]`

> A: Estimates are hard - but we need some sort of breakdown of planned work, we can't fund general hours of work. […] But in the end, rough estimation is what is expected - not exact to the minute or anything.
> `[VERIFIED from https://nlnet.nl/officehour/#amount]`

And explicitly permitted: naming only your own hourly rate as the cost basis — "Naming only your hourly rate as costs is perfectly fine. Ideally, a broad overview of the labour involved with different development milestones is also appreciated." `[VERIFIED from https://nlnet.nl/officehour/#amount]`

### 3.5 Facilities & Administrative (overhead) costs

> **Q: Are F&A costs considered eligible expenses?**
> A: Facilities and Administrative costs are generally not considered eligible expenses, unless in the presence of exceptional circumstances. When they are allowed, the maximum permissible amount is capped at 25%.
> `[VERIFIED from https://nlnet.nl/restack/faq/#FA]`

### 3.6 Other eligible / ineligible cost rules relevant to a software project

- **No VAT**: "It's charitable donations, there is no VAT, we cannot pay it." and "Does Stichting NLnet have a VAT ID? A: No (Also note that we give donations, so VAT is not applicable.)" `[VERIFIED from https://nlnet.nl/officehour/#taxes]`
- **No compute/hosting**: "Q: …Does renting the compute time needed to run the funded software fall under the first sentence? A: No, compute time renting would fall under operational expenses." `[VERIFIED from https://nlnet.nl/officehour/#hardware]`
- **No basic IT hardware**: "NLnet does not allocate grant money to basic operational IT cost, such as regular laptops, desktops/workstations, or mobile phones." `[VERIFIED from https://nlnet.nl/foundation/policies/externalspending/]` — relevant: MeshDoc's Android test devices are **not** fundable as a matter of course. Test hardware "is not seen as an efficient use of project budget" in any case. `[VERIFIED from https://nlnet.nl/officehour/#hardware]`
- **No company formation costs**: "organization registration costs would not be eligible." `[VERIFIED from https://nlnet.nl/officehour/#fees]`
- **No AI costs**: "Costs incurred for AI usage are not eligible for reimbursement." `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/2.0/]`
- **No advertising**: "NLnet does not pay for advertisement campaigns of any type for any of its supported projects." `[VERIFIED from https://nlnet.nl/foundation/policies/externalspending/]`
- **Expenses ≥€250 need proof**: "Requests for payment of large costs linked to out-of-pocket cost (with an individual value of 250 euro and up) are accompanied by adequate proof, e.g. an invoice or bill." `[VERIFIED from https://nlnet.nl/foundation/policies/externalspending/]`
- **Travel is possible but sparing**: "As our grants focus on research and development, we unfortunately have to be quite sparse as far as funding travel and meetings is concerned. They need to have a strong justification for the project needs". `[VERIFIED from https://nlnet.nl/officehour/#amount]`
- **Work already done is not fundable**: "A grant can only cover the period between the proposal being officially selected and the agreed end of the Memorandum of Understanding. We cannot make donations for any effort completed prior to the grant." `[VERIFIED from https://nlnet.nl/restack/faq/]`

### 3.7 Milestone structure (how money is actually released)

Payments are in arrears, tied to milestones:

> No, the grant is not paid out up front. Instead you divide your project into milestones and allocate an amount to each of these. Once you reach a milestone you send in an request for payment. So for instance: You divide your project in milestones A, B, C and D. And you allocate amount € X to milestone A. Once you have finished milestone A, you request the payment for it and move on to milestone B.
> `[VERIFIED from https://nlnet.nl/restack/faq/]`

The sample MoU's Annexe I shows the expected plan shape, with per-subtask amounts:

> **Milestone(s)**
> • Create requirements document + threat modelling (500 EUR)
> • Create technical design (2200 EUR)
> • First alpha release (2700 EUR)
> • Some other subtask (e.g. release first alpha version) (600 EUR)
> **Amount** 6000 EUR
> `[VERIFIED from https://nlnet.nl/foundation/request/sample_MoU.pdf, extracted with pdftotext this session]`

The MoU notes subtasks "executed by different people" should have amounts divided across them, and shows an accessibility milestone in the template ("Certified WCAG accessible") as well as a security-review milestone ("Process issues from external security review") — a strong hint at what NLnet expects R&D plans to contain. `[VERIFIED from https://nlnet.nl/foundation/request/sample_MoU.pdf]`

**Default duration:** "By default, we expect projects to be completed within 12 months — but qualified exceptions can be made." `[VERIFIED from https://nlnet.nl/restack/faq/]`

---

## 4. The application form — exact fields and character limits

Source for everything in this section: `https://nlnet.nl/propose/` `[VERIFIED — read directly this session]`

**Form endpoint:** https://nlnet.nl/propose/ — single page, single submission, plain text, English.
**Deadline printed at the top of the form:** "Next deadline: November 3rd 2026 12:00 CET (noon)". `[VERIFIED]`

### 4.1 Global instructions on the form

> - Our grants are primarily for **technical development**.
> - Software, hardware and content must be released under **open licences** and apply (preferably open) **standards**.
> - Proposals and projects should be made **by humans, not AI**. See our [Generative AI policy](/foundation/policies/generativeAI/).
> - Our EU-supported funds require a strong [European dimension](/OIS/european-dimension/); usually this means applicants should (mostly) be from Horizon Europe-eligible countries.
>
> Please **be short and to the point** in your answers; submitting a proposal can be quick!
>
> Please answer in plain text and in English, **in your own words**. We don't care about spelling or grammar, only about your ideas. **If you really need AI-assistance, keep your prompts/interactions** and [submit your logs](#ai-disclosure) below.

### 4.2 Field-by-field table

| # | Section | Field label (as printed) | Limit | Notes |
|---|---|---|---|---|
| 0 | Select a fund | "Which of our funds are you applying for?" | dropdown | Options: `Restack Fund`, `CodeSupply Fund`, `Other / open call`. **Must select `Restack Fund`.** |
| 1 | Project overview | "Proposal title" | **none stated** | `[UNCERTAIN — no maxlength given on the page]` |
| 2 | Project overview | "Project website(s) / repositories" | **none stated** | `[UNCERTAIN]` |
| 3 | Project overview | Summary — "Please **summarise** the proposed project and its expected results in a few lines." | **max. 1000 characters** | ✔ matches brief |
| 4 | Proposed effort | "**How much money** do you request for your project?" | numeric | "In Euros. Between € 5 000 and € 50 000 for a first grant." |
| 5 | Proposed effort | Budget breakdown — "Please provide a breakdown clarifying how the requested budget would be used." Sub-prompts: "Which tasks will you undertake, and (roughly) how much time/effort will each take?", "What hourly/daily/monthly rate did you use?", "Will there be any expenses?" | **max. 4000 characters** | ✔ matches brief |
| 6 | Proposed effort | Comparison — "Please **compare** your own project with other relevant efforts (both existing and historical). **What is new**, more thorough or otherwise different? Have you **considered contributing** to any of the others?" | **max. 4000 characters** | ✔ matches brief |
| 7 | Proposed effort | Challenges — "What technical **challenges** do you expect during the project?" | **max. 4000 characters** | ✔ matches brief |
| 8 | Proposed effort | Ecosystem — "What is the **ecosystem** around your own project, and how will you engage relevant actors? For example, does your project **depend** on other projects/people? And **who would be the main users**?" | **max. 2000 characters** | ✔ matches brief |
| 9 | Background | Background — "What makes you the right person(s) for this effort? Do you have relevant **experience** in this or other projects/organisations? And if so, can you tell us a bit about your contributions?" | **max. 2000 characters** | ✔ matches brief |
| 10 | Background | Other funding — "Does (or did) the project have **other funding** sources?" | **max. 1000 characters** | ✔ matches brief |
| 11 | Attachments | Supplementary material (HTML, PDF, ODF, images, plain text) | **max 50 MB in total** | "**Attachments are not needed**. Please ensure the proposal is self-contained." |
| 12 | AI disclosure | Yes/No — "Did you use generative AI in writing this proposal?" | dropdown | `No, I did not use generative AI in writing this proposal` / `Yes, I have used generative AI in writing this proposal` |
| 13 | AI disclosure | "Which model did you use? What did you use it for? Please **paste your prompts/interactions** and the AI output in this text field" | **max. 8000 characters** | ✔ matches brief |
| 14 | AI disclosure | "Upload prompts/dialogues used in creation of this proposal." | **max. 50 MB in total** | file upload |
| 15 | AI disclosure | Codebase question — "Does your project build on an existing codebase that already includes, or expects to gain, a significant amount of code generated by AI?" | dropdown | `No, the codebase does not contain AI-generated code` / `Yes, the codebase contains AI-generated code` — **this field remains live under v2.0** |
| 16 | AI disclosure | "Please give a high-level description of the AI use in your project." | **max. 1000 characters** | ⚠️ **extra field not in the brief's list** |
| 17 | Contact | "Your name (or pseudonym)" | none stated | pseudonyms allowed until grant |
| 18 | Contact | "Email address" | required | |
| 19 | Contact | "OpenPGP key (optional)" | **max 10 000 characters** | "Note we are not (yet) equipped to encrypt _every_ email to you." |
| 20 | Contact | "Phone number" | — | "Please do not forget the country code." |
| 21 | Contact | "Type of applicant" | dropdown | `Individual`, `Collective (without legal entity)`, `Association (not-for-profit entity)`, `Foundation`, `NGO`, `University`, `Institute`, `Public sector entity`, `Cooperatively-owned company`, `SME company (small/medium enterprise)`, `Corporation` |
| 22 | Contact | "Name of organisation" | — | |
| 23 | Contact | "Country" | dropdown | "Your country of residence, or what comes closest." — **`Nepal` is a selectable option on the form.** `[VERIFIED — Nepal appears in the country dropdown]` |
| 24 | Contact | Conditional note — "If you apply for an EU-funded programme but you are not from a Horizon Europe-eligible country, please clarify how your project might satisfy the 'European dimension' requirement in the background question above. (e.g. European citizenship)." | — | **Not applicable to Nepal** (see §2) |

**Total character-limited prose budget for the substantive proposal: 1000 + 4000 + 4000 + 4000 + 2000 + 2000 + 1000 = 18,000 characters.** `[derived]`

**Character counting caveat, from NLnet itself:**

> **Q: Regarding the application form and character limitations, does it count characters with spaces or without? thank you!**
> A: Hmm, good question, we actually don't know. But a tip from someone else is to just count the spaces to be on the safe side.
> `[VERIFIED from https://nlnet.nl/officehour/#form]`

### 4.3 Guidance on what each free-text answer should contain

The Office Hour clarifies several of these fields:

- **Comparison field** — not a literature list: "Rather the latter: a discussion of where the project fits, why it's needed, why nothing out there answers the problem you are trying to solve. We like to compare your project with what already exists, and also verify that you are aware of the landscape in which you position the project, and how it integrates within that space." `[VERIFIED from https://nlnet.nl/officehour/#form]`
- **Technical challenges field** — "Both, with a focus on the former" (i.e. the challenges *within your project*, more than general field-wide challenges). "The expected outcome of the question is to outline your reflection about the project and its challenges." `[VERIFIED from https://nlnet.nl/officehour/#form]`
- **Single author is fine**: "Q: I write the proposal alone. Is that OK? A: It is very much preferred." `[VERIFIED from https://nlnet.nl/officehour/#form]`
- **Resubmission**: unlimited before the deadline; mention the prior proposal ID. "Applicants can resubmit any number of times until the deadline has passed." `[VERIFIED from https://nlnet.nl/news/2026/20261020-AI-policy.html]` and `[VERIFIED from https://nlnet.nl/restack/faq/#change]`

---

## 5. What Restack explicitly declares OUT of scope

### 5.1 ★ The AI exclusion and the ">1 million active human users" exception

Exact text from the Restack main page:

> **AI-related projects are not within scope** — unless they are already widely used throughout society (> 1 million active human users) and directly relevant to the stack.
>
> The focus of Restack is on securing the core infrastructure and foundational technologies on which global society critically depends.
>
> While there is a lot of interesting research and development going into artificial intelligence and its (potential) applications, the development, application and/or integration of artificial intelligence is complementary/orthogonal effort to the work supported within Restack.
> `[VERIFIED from https://nlnet.nl/restack/]`

Restated in the GenAI FAQ with the same exception:

> **Q: Are there limitations to building AI tooling? So not using AI but building it?**
> Yes. In certain programmes (notably [Restack](/restack)) [AI-related projects not within scope](/restack#AI). There is one exception: projects that are already widely used throughout society (> 1 million active human users) and directly relevant to the stack, can apply for funding.
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/faq/]`

**Interpretation of the exception:** it is a *grandfathering* clause for existing mass-adoption infrastructure that happens to be AI-related (the kind of thing that already has millions of users and that the stack depends on). It is **not** a route a new project can claim, because a not-yet-built MeshDoc has zero users. `[Interpretation, but strongly supported: "already widely used throughout society (> 1 million active human users)" is present-perfect and cannot describe a proposal for new work]`

### 5.2 ★ The boundary rulings — MeshDoc must be built to fit inside these

These three Q&As define exactly how much AI-adjacency is tolerable. They are the most useful text in the whole corpus for scoping MeshDoc:

> **Q: Restack excludes AI-related projects. I am creating a tool that can be used by humans, but can optionally also be used by AI. Is this is scope?**
> A: **Yes. When the AI functionality is an additional feature, the project is in scope for programmes that do not fund AI-related projects.**
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/faq/]`

> **Q: The Restack programme excludes AI-related projects. Where is the line for infrastructure that AI systems can consume but that contains no AI itself?** …would a deterministic library that records content-addressed source references (document, chunk, version, hash) and verifies that a cited passage exists and matches its hash be in scope, if any AI component using it stays outside the funded work?
> A: **If it is also consumable and useful outside of the AI ecosystems, then it would likely be considered.**
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/faq/]`

> **Q: My project has an optional local AI, off by default, only for searching documents. Is it in scope for Restack if the grant does not fund the AI part?**
> A: **It would likely be in scope.**
> `[VERIFIED from https://nlnet.nl/foundation/policies/generativeAI/faq/]`

**Applied to MeshDoc:** a CRDT/E2EE/mesh collaboration toolkit is *not* an AI project at all — it is squarely "alternatives to closed online technologies serving a large userbase" plus "full stack security". The only risk would be *adding* a smart-summarisation / AI-assistant feature. **Do not add one, do not hint at one, and do not let a future roadmap mention one.** If a reviewer asks, the answer is the first ruling above: AI would at most be an optional add-on feature outside the grant. `[Interpretation from the verified rulings]`

### 5.3 What Restack says IS in scope (the positive frame to use)

> In scope are innovations and enhancements to core internet infrastructure, **alternatives to closed online technologies serving a large userbase**, and devices used to run and consume these in a secure and privacy-friendly manner. This also includes **full stack security**, software supply chain management, reproducibility and trust enhancing technologies.
>
> We are interested in improving and decoupling infrastructure layers, service management and deployment innovation as well as **actual services and their client-side counterparts**.
>
> We stimulate the creation and use of norms and standards, as these enable interoperability and redundancy in implementation, and reduce the risk of future compromise and failure.
> `[VERIFIED from https://nlnet.nl/restack/]`

And the goal statement, which contains the phrase most useful for framing MeshDoc ("local-first"):

> The goal of this fund is to help deliver, mature and scale **operational internet commons** across the technology stack to form connected collaborative computing networks: from libre chips to middleware without a vendor lock-in, from productivity tools to **'local-first' infrastructure** — and of course including the end user applications needed to consume those networked services.
> `[VERIFIED from https://nlnet.nl/restack/]`

**This is the single best sentence in the corpus for MeshDoc:** "local-first" is named explicitly in the fund's own goal statement, and "end user applications needed to consume those networked services" explicitly authorises funding an Android client. `[Interpretation grounded in verified quote]`

### 5.4 Other exclusions and de-prioritisations that touch this project

| Item | Rule | Source |
|---|---|---|
| Events / sponsorship | "our funding focuses on research and development, which makes sponsoring events out of scope." Only events that "meaningfully contribute in a direct way to an actual R&D project... E.g. a code sprint or hackathon." | `[VERIFIED from https://nlnet.nl/restack/faq/]` |
| Hosted instances / hosting costs | "we are not generally able to fund hosted instances of software, or cover hosting costs." — **directly relevant to the "dumb encrypted relay server"** | `[VERIFIED from https://nlnet.nl/officehour/#hardware]` |
| Compute time | "compute time renting would fall under operational expenses" (i.e. not eligible) | `[VERIFIED from https://nlnet.nl/officehour/#hardware]` |
| Basic IT hardware | "NLnet does not allocate grant money to basic operational IT cost, such as regular laptops, desktops/workstations, or mobile phones." | `[VERIFIED from https://nlnet.nl/foundation/policies/externalspending/]` |
| Company formation | "organization registration costs would not be eligible." | `[VERIFIED from https://nlnet.nl/officehour/#fees]` |
| Advertising | "NLnet does not pay for advertisement campaigns of any type" | `[VERIFIED from https://nlnet.nl/foundation/policies/externalspending/]` |
| Work already done | "We cannot make donations for any effort completed prior to the grant." | `[VERIFIED from https://nlnet.nl/restack/faq/]` |
| Pure documentation projects | "research and development remain the principal target of our grants… An application that aims to improve beginner friendliness and onboarding by improving documentation and developing new features / improving UX might stand better chance than documentation alone." | `[VERIFIED from https://nlnet.nl/officehour/#documentation]` |
| Proprietary-dependent tech | "Technology that can only be used with an individual closed source application will not adequately scale… Spending public funding for building private monopolies isn't in the public interest." | `[VERIFIED from https://nlnet.nl/restack/faq/#eligiblelicensing]` |

**⚠️ Relay-server caveat:** the "optional dumb encrypted relay" must be presented as *code to be written* with milestones, not as *a hosted service*. Funding the relay's *development* is fine; funding its *operation* is not. `[Interpretation grounded in the hosting-cost exclusion]`

---

## 6. Evaluation criteria: how proposals are scored, and what succeeds

### 6.1 The scored criteria and weights

> Projects receive an initial rating on three criteria:
>
> | Weight | Criterion |
> | --- | --- |
> | 30% | Technical excellence/feasibility |
> | 40% | Relevance/Impact/Strategic potential |
> | 30% | Cost effectiveness/Value for money |
>
> The total weighted score of projects has to be above 5.0 (out of 7) to pass to the next stage.
> `[VERIFIED from https://nlnet.nl/restack/guideforapplicants/]`

The 5.0-out-of-7 threshold is confirmed as a weighted score over exactly these three criteria: "A: You would need to get at least 5 on the weighted score based on the criteria listed in that guide." / "Q (Follow-up) Would that be of the criteria: Technical excellence/feasibility/Relevance/Impact/Strategic potential, Cost effectiveness/Value for money. A: Yes." `[VERIFIED from https://nlnet.nl/officehour/#review]`

**Note the 40% weight on Relevance/Impact/Strategic potential** — this is the largest single factor and it is the one where a "nice toolkit" loses to a "building block of the Open Internet Stack". `[Interpretation]`

### 6.2 The two-stage process

**Stage 1** = knock-out eligibility check, then scoring as above. "All projects that fail on any of these knock-out criteria, will **not** be further reviewed and will be marked ineligible. The rest of the projects will be given a score based on the proposal text as submitted. If multiple versions were submitted prior to the deadline, the last complete version will be used." `[VERIFIED from https://nlnet.nl/restack/guideforapplicants/]`

**Stage 2** = "used to select strategic projects which not only satisfy the _minimal criteria_, but also have potentially a _lasting impact_ on society." `[VERIFIED from https://nlnet.nl/restack/guideforapplicants/]`

The stage-2 questions reviewers ask are published — **these are effectively the exam paper, and every one of them should be pre-answered in the proposal:**

> - what is the difference in approach to _existing projects U, V_ and _W_
> - how will you approach _complicating factor X_
> - can you back up or validate _claim Y_
> - have you considered collaborating with _complementary effort Z_ or using _standard A_
> - the rate you have applied for _task B_ is very high compared to the perceived value of that task. Can you explain, or would you like to reconsider?
> - can you clarify how you intend to make the outcome of the project (self)sustainable
> - how does upstream _project D_ feel about your application
> `[VERIFIED from https://nlnet.nl/restack/guideforapplicants/]`

> In addition, the review team will do independent verification of facts, methods and claims. If necessary they verify relevant information through their expert network.
> `[VERIFIED from https://nlnet.nl/restack/guideforapplicants/]`

> If the revised plan scores lower than the original proposal, the original proposal is rated. Projects are subsequently ranked by the team according to the overall expected value and impact to the Open Internet Stack. A cut-off point is determined, based on the overall quality of the round and the remaining budget.
> `[VERIFIED from https://nlnet.nl/restack/guideforapplicants/]`

### 6.3 The independent review committee

> An independent review committee checks the final selection of projects. […] At least one of its members independently validates that projects that are nominated are indeed eligible for funding, budgets are frugal, and that there are no other concerns.
> `[VERIFIED from https://nlnet.nl/restack/guideforapplicants/]`

> If a project fails to meet the criteria of the independent review committee, the concerns are sent to the proposer and the project is pushed back to the next available call.
> `[VERIFIED from https://nlnet.nl/restack/guideforapplicants/]`

Note "**budgets are frugal**" — an independent validator explicitly checks frugality. This is the mechanism behind the cost-effectiveness weighting. `[Interpretation grounded in verified quote]`

### 6.4 Published guidance on what makes a proposal succeed

From the Guide's opening statement of intent:

> Projects are judged on their technical merits, strategic relevance to the establishment of a strong and efficient Open Internet Stack and overall value for money. The key objective is to deliver potential **break-through contributions** to the open internet stack.
> `[VERIFIED from https://nlnet.nl/restack/guideforapplicants/]`

From the Office Hour, on what reviewers weigh:

> The current reach can have some impact (and the funding status) but also the history of the proposers and previous work done, the specific problems being solved and the amount being asked (and rate etc). So for a new project its useful to point to previous work and collaborations. Its also useful to be in contact with the project itself if you are not the maintainer to figure out upstreamability or similar. A new project with unknown contributors is a gamble, so the technical soundness of the approach should also be visible.
> `[VERIFIED from https://nlnet.nl/officehour/#relevant]`

That passage is unusually candid and directly actionable: **"A new project with unknown contributors is a gamble"** → the *Background* answer (2000 chars) carries disproportionate weight for an unknown Kathmandu team. Prior work, a public repo, prior shipping history, and named collaborators should all be in there. `[Interpretation]`

On "value for money" being a judgement rather than a formula:

> A: Projects are evaluated partly based on cost effectiveness. During the evaluation process, we balance the project's estimated effort and its cost with its potential impact; so it is important that the financial ask of your proposal is proportionate with its potential.
> `[VERIFIED from https://nlnet.nl/officehour/#amount]`

**Strategic dimensions that count positively** (explicitly enumerated by NLnet, and a ready-made checklist to hit):

> Creating strong role models for under-represented groups can help expand the relevance and impact of our work and thus is considered a strategic dimension, and as such is taken into account during the review — alongside other strategic dimensions such as the effect of the project on the technology landscape, standardisation efforts which are under way, human rights aspects, contribution to European and national legislative understanding and societal dialogue, etc.
> `[VERIFIED from https://nlnet.nl/restack/faq/#under-represented]`

For MeshDoc the obvious strategic dimensions are: **human rights / censorship resistance / disaster-resilience communications for a low-connectivity region (Nepal)**, **effect on the technology landscape** (local-first as an alternative to cloud SaaS), and possibly **standardisation** (interop with existing CRDT/Matrix/ActivityPub ecosystems). `[Interpretation]`

### 6.5 What a submitted proposal actually looks like (calibration)

A real, recorded NGI0 Commons Fund submission (Forgejo, Germany, €50,000) is published verbatim and shows the expected terseness — the whole "Requested support" block is a handful of bullet lines, not an essay:

> - requested amount: € 50000
> - used for: Funding will be used for development of the feature & tests, review & merge.
> - compare: If we compare to "federated user activity" (overall effort was about 80 - 100 days) we consider the complexity of usecase… comparable but slightly simpler.
> - challenges:
>   - "ucf001: user forks a foreign": Realize Follow- (or Fork?) & Accept-Activity, clone or migrate the project itself, align activities with the ForgeFed specification & realize the UI.
> …
> - ecosystem: All people involved are part of Forgejos "contributor team". We will be proud to announce the new features in the Forgejo release notes and highlight the story at software development conferences.
> `[VERIFIED from https://codeberg.org/forgejo/sustainability/raw/branch/main/2025/2025-08-01-nlnet-ngi0-commons-federation/application.md]`

**Calibration takeaway:** NLnet's own form guidance says "**be short and to the point**… submitting a proposal can be quick!" and "unlike most procedures you should be able to complete a proposal in less than an hour". Over-long, AI-sounding prose is a known negative signal; the 18,000-character total budget is a ceiling, not a target. `[VERIFIED from https://nlnet.nl/propose/ and https://nlnet.nl/restack/faq/#postpone]`

### 6.6 Timeline expectations

> We do our best to assess all applications as quickly as possible. However, our funds are popular and we receive a large amount of applications. You can expect the process to take between three and five months. This is counted from the date of the deadline of the open call, not from the date you have submitted a proposal.
> `[VERIFIED from https://nlnet.nl/restack/faq/]`

Office Hour gives a shorter, more optimistic figure ("We aim for 8 to 10 weeks but duration may vary"), but the Restack FAQ's 3–5 months is the Restack-specific statement. `[Both VERIFIED; discrepancy noted — plan for 3–5 months]`

### 6.7 If rejected

> The projects which are not taken into the second round are informed that their project is not selected, so that they may try to find funding elsewhere as soon as possible — or continue without additional funding.
> `[VERIFIED from https://nlnet.nl/restack/guideforapplicants/]`

Calls recur every two months: "we have a bimonthly cycle"; deadlines are on the **3rd of every odd month** (`/funding.html`: "There is a deadline on the 3rd of every _odd_ month"). So the next deadline after 3 Nov 2026 would be **3 January 2027** `[UNCERTAIN — derived from the stated odd-month/3rd-day rule; not explicitly listed]`. "In principle there are continuous open calls, until the budget is allocated in line with the goals of Restack and the Open Internet Stack." `[VERIFIED from https://nlnet.nl/restack/guideforapplicants/]`

---

## 7. IP / licensing, and applying as a company with non-EU payment & tax

### 7.1 Licensing: a recognised FOSS licence is mandatory and non-negotiable

> All scientific outcomes **must** be published as open access, and any software and hardware **must** be published under a recognised open source license in its entirety.
> `[VERIFIED from https://nlnet.nl/restack/guideforapplicants/]`

> All projects must be free/libre/open source: all scientific outcomes **must** be published as open access, and any software and hardware developed **must** be published under a recognised free and open source license in its entirety.
> `[VERIFIED from https://nlnet.nl/funding.html]`

The FAQ is blunt about non-negotiability:

> All projects are supposed to be released under a suitable free/libre/open source license. This allows for incremental innovation on top of your results, and as we explained is non-negotiable.
> `[VERIFIED from https://nlnet.nl/restack/faq/#additionallicensing]`

**No specific licence is mandated** — "a suitable free/libre/open source license" / "a recognised free and open source license". For MeshDoc (Android, E2EE, CRDT) the choice is ours, but it must be a recognised OSI/FSF licence, applied "in its entirety". `[VERIFIED that no named licence is required; the specific licence choice is UNCERTAIN/our decision]`

**Dual licensing is permitted:**

> This condition however does not in any way exclude the legitimate holders of copyrights and other associated rights of dealing with your project results under **additional** licenses, even proprietary ones: there may be legitimate reasons (such as license incompatibility with third party complementary FLOSS efforts) for alternative licenses beyond the license you use for the project.
> `[VERIFIED from https://nlnet.nl/restack/faq/#additionallicensing]`

**A commercially-exploited product with an open core is acceptable**, provided the funded part is self-standing:

> If the part you want to develop and release as free and open source is relevant and is not itself dependent on your (or other) proprietary technology, sure. We look at what you research and develop inside the project you propose, not to anything else. […] So in short, you **can** submit a proposal that fits snugly within a closed commercial environment, as long as that project itself **is** open source and doesn't depend on that closed environment.
> `[VERIFIED from https://nlnet.nl/restack/faq/#eligiblelicensing]`

**Patents must be disclosed:**

> Yes, you must certainly disclose this. Patents can hinder other people and organisations from freely working and innovating with the technologies you may be creating… We would prefer to understand potential patent situations at the application stage.
> `[VERIFIED from https://nlnet.nl/restack/faq/#patents]`

**Accessibility (WCAG) is effectively a deliverable expectation.** From the Guide, follow-on eligibility requires "that any software artefacts delivered were WCAG compliant" `[VERIFIED from https://nlnet.nl/restack/guideforapplicants/]`, and the sample MoU template includes a "Certified WCAG accessible" milestone `[VERIFIED from https://nlnet.nl/foundation/request/sample_MoU.pdf]`. The FAQ frames it as non-optional in spirit:

> But taking care of accessibility (or a11y for short) is, as far as we are concerned, the 'new normal'. From our end, we are willing to invest in this as well. Experts from our team will help you understand what that means to your project, and will mentor you how you can comply with the technical requirements. […] projects can request an accessibility audit performed by the HAN University of Applied Sciences
> `[VERIFIED from https://nlnet.nl/restack/faq/#accessibility]`

**⚠️ MeshDoc implication:** an accessibility commitment for an Android mesh app should appear as an explicit milestone or at least a named task. `[Interpretation]`

### 7.2 Can a company (SME) apply? Yes — explicitly.

> **Q: Do I need to have a legal entity like a company to apply?**
> No, you don't. You can apply as an individual, or as a formal or informal organisation of any type. Or even a collaboration of the two. It is not an issue if you have not yet established the entity when you apply.
>
> Each of the persons and legal entities which are part of the grant can be paid directly by us. The internal allocation of payment is decided upon by the project lead, and can be done after the work is completed.
> `[VERIFIED from https://nlnet.nl/restack/faq/]`

> **Q: Can someone apply with a private business?**
> A: Yes. Everyone and every kind of entity can apply.
>
> **Q: Can we apply as an NGO**
> A: Yes.
> `[VERIFIED from https://nlnet.nl/officehour/#entities]`

> **Q: Commercial-cooperative applicants. […] Are commercial-cooperative applicants funded today?**
> A: Commercial-cooperative entities are funded today, this is not an issue. You can apply as individuals, commercial entities, foundations, etc.
> `[VERIFIED from https://nlnet.nl/officehour/#entities]`

And from the funding page: "In principle anyone can apply: individuals, research organisations, non-profits, public institutions, companies of any size and type, etc." `[VERIFIED from https://nlnet.nl/funding.html]`

The form's applicant-type dropdown includes `SME company (small/medium enterprise)` as a first-class option. `[VERIFIED from https://nlnet.nl/propose/]`

**Caveat for a for-profit entity:** the external-spending policy treats for-profits more strictly on equipment residual value — for-profit entities "are expected to return the remaining value" of economic goods at project end, and individuals paid above 2/3 of the maximum rate are treated the same. `[VERIFIED from https://nlnet.nl/foundation/policies/externalspending/]` This is irrelevant if the budget is pure labour. `[Interpretation]`

**Also relevant:** "for a first grant, we are limited to one grant per applicant" — so a team cannot split MeshDoc across two first-grant applications. `[VERIFIED from https://nlnet.nl/officehour/#often]`

### 7.3 The legal nature of the money: a charitable donation, not a contract

This is the crucial framing for a Nepali recipient:

> NLnet as the grant handling organisation is a recognised public benefit organisation, and the goals of _Restack_ are within its statutory mission. Any grants that will be handed out, to individuals, companies, NGO's or other types of legal entities are **donations** that fall under the most beneficial tax conditions as 'charitable gifts'.
> `[VERIFIED from https://nlnet.nl/restack/guideforapplicants/]`

> Your grants take the form of a donation from NLnet Foundation. NLnet is a recognised public benefit organisation according to the Netherlands tax office, a status which translates in full or to some degree to many other parts of the planet — which may or many not include your country of residence and/or work.
> `[VERIFIED from https://nlnet.nl/restack/faq/#donations]`

### 7.4 No VAT

> **Q: Should the budget be excluding VAT? And if so, do I have to find co-funding to pay for the VAT or is it exempt because the funding is a donation?**
> A: It's charitable donations, there is no VAT, we cannot pay it.
>
> **Q: Does Stichting NLnet have a VAT ID?**
> A: No (Also note that we give donations, so VAT is not applicable.)
> `[VERIFIED from https://nlnet.nl/officehour/#taxes]`

Budget should therefore be VAT-exclusive and contain no VAT line. `[Interpretation from verified quotes]`

### 7.5 How payment is actually made to a non-EU grantee

> **Q: Can an EU individual and an individual from outside the EU apply for a project together? If the grant is given, will the money be disbursed separately to the separate accounts?**
> A: Yes. Normally, at least 60% of the funds should go to EU based (or Horizon affiliated countries), but you can collaborate internationally. We recommend that you apply with one person who will lead the communications with us, and clarify in the application form who will participate in the grant. If the grant is given, the funds can be sent to the different contributors accounts separately (and it is preferred to do so).
> `[VERIFIED from https://nlnet.nl/officehour/#european]`

MoU mechanics:

> Payments will subsequently be made by wire transfer into a bank account designated by […]
> `[VERIFIED from https://nlnet.nl/foundation/request/sample_MoU.pdf, extracted with pdftotext]`

> Currently we only support a single point of contact as the main contact person. It doesn't matter which participant is the contact person, other than them being the contact point and the one to confirm all requests for payment.
> `[VERIFIED from https://nlnet.nl/officehour/#payments]`

So: **wire transfer to a designated bank account, milestone-triggered, single point of contact, no up-front money.** For Nepal this means the team needs a bank account able to receive EUR international wire transfers, and should expect to carry costs before the first milestone payment lands. `[Interpretation grounded in verified quotes]`

### 7.6 Tax — the honest answer, and the gap that matters for Nepal

NLnet **refuses to advise on tax**, explicitly and repeatedly:

> **Q: Do I have to pay taxes over the grant money I receive?**
> A: NLnet can not and will not give any advise about taxes. From the perspective of NLnet we are an ANBI (Public Benefit Organisation) giving a charitable donation. Whether the tax office in your locality accepts that and whether donations are taxed or not depends very much on locality. You can consider to ask a financial/tax adviser.
> `[VERIFIED from https://nlnet.nl/officehour/#taxes]`

> Taxation in a global context is a pleasantly complex, dynamic and inspiring issue that has intellectually challenged many great minds. It has damaged some of those (and many others too). There are unfortunately significant differences across countries, and even across regions within a single tax system you may find notable variations in treatment.
>
> If you are from Europe, you might benefit from an initiative by Philantropy Europe Association (Philea) called Legal Environment for Philanthropy in Europe.
> `[VERIFIED from https://nlnet.nl/restack/faq/#donations]`

> This (tax free) is the case in the Netherlands but generally not elsewhere (as we are registered as an ANBI).
> `[VERIFIED from https://nlnet.nl/officehour/#taxes]`

**⚠️ Nepal-specific gap:** the only resource NLnet points to (Philea's *Legal Environment for Philanthropy in **Europe***) **does not cover Nepal**. NLnet provides **no** resource for non-European tax treatment. `[VERIFIED that Philea is Europe-only, by its title and scope as described; the consequence for Nepal is UNCERTAIN]`

**Therefore, [UNCERTAIN]:** whether an NLnet donation to a Nepal-resident individual is taxable, and under what head (income, gift, or otherwise), is **not documented anywhere in NLnet's materials** and cannot be resolved from these sources. This needs Nepali professional advice (e.g. a local CA/tax practitioner familiar with foreign grants and the Nepal Rastra Bank foreign-exchange rules for inbound remittances). Do not state a tax position in the proposal. `[UNCERTAIN — flagged; do not guess]`

### 7.7 Summary answer on "how payment/tax works for non-EU entities"

| Question | Answer | Status |
|---|---|---|
| Can a Nepal company/SME apply? | Yes — "companies of any size and type"; SME is a form option | `[VERIFIED]` |
| Can an individual apply? | Yes — "You can apply as an individual" | `[VERIFIED]` |
| Can a collective without a legal entity apply? | Yes — "a formal or informal organisation of any type"; form option "Collective (without legal entity)" | `[VERIFIED]` |
| Can payments go to multiple people? | Yes — "the funds can be sent to the different contributors accounts separately (and it is preferred to do so)" | `[VERIFIED]` |
| How is money transferred? | Wire transfer into a designated bank account, per milestone, in arrears | `[VERIFIED]` |
| Is VAT paid? | No — "there is no VAT, we cannot pay it" | `[VERIFIED]` |
| Does NLnet withhold tax? | No mention anywhere; money is a "donation"/"charitable gift" | `[VERIFIED that it is a donation; withholding is UNCERTAIN]` |
| Is the donation tax-free in Nepal? | **Unknown — not documented by NLnet; needs local advice** | `[UNCERTAIN]` |
| Does NLnet give tax advice? | No — "can not and will not give any advise about taxes" | `[VERIFIED]` |

---

## Appendix A — Source inventory

| # | URL | Status this session | Used for |
|---|---|---|---|
| 1 | https://nlnet.nl/restack/guideforapplicants/ | ✅ 200, full text | §1.1, §2.8, §3.1, §6.1–6.4, §7.1 |
| 2 | https://nlnet.nl/restack/eligibility/ | ✅ 200, full text | §2.2, activity types |
| 3 | https://nlnet.nl/restack/faq/ | ✅ 200, full text | §3.1, §3.5, §5.4, §6.3, §6.6, §7.1–7.6 |
| 4 | https://nlnet.nl/foundation/policies/generativeAI/ | ❌ **200 but EMPTY BODY** (both with and without trailing slash) | — (unusable) |
| 5 | https://nlnet.nl/foundation/policies/generativeAI/2.0/ | ✅ 200, full text | §1.1–1.6 (**canonical AI policy source**) |
| 6 | https://nlnet.nl/foundation/policies/generativeAI/faq/ | ✅ 200, full text | §1.2–1.6, §5.2 |
| 7 | https://nlnet.nl/foundation/policies/generativeAI/1.1/ | ✅ 200 (archive) | §1.5 v1.1→v2.0 comparison |
| 8 | https://nlnet.nl/news/2026/20261020-AI-policy.html | ✅ 200 | §1.7, effective date, resubmission |
| 9 | https://nlnet.nl/OIS/european-dimension/ | ✅ 200, full text | §2.3, §2.4 |
| 10 | https://nlnet.nl/propose/ | ✅ 200, full text | §4 (all fields/limits), deadline |
| 11 | https://nlnet.nl/restack/ | ✅ 200, full text | §5.1, §5.3 |
| 12 | https://nlnet.nl/funding.html | ✅ 200 | §3.2, §6.7, §7.2 |
| 13 | https://nlnet.nl/officehour/ | ✅ 200 (**output truncated at ~40 KB**; full text spilled to a temp file and grepped) | §2.5, §3.3–3.6, §4.3, §6.4, §7.2–7.6 |
| 14 | https://nlnet.nl/foundation/policies/externalspending/ | ✅ 200 | §3.3, §3.6, §5.4, §7.2 |
| 15 | https://nlnet.nl/foundation/request/sample_MoU.pdf | ✅ 200 (**PDF — not fetchable via web_fetch**; downloaded with curl + `pdftotext`) | §3.7, §7.1, §7.5 |
| 16 | https://ec.europa.eu/.../list-3rd-country-participation_horizon-euratom_en.pdf | ✅ 200 (**PDF — not fetchable via web_fetch**; downloaded with curl + `pdftotext`) | §2.4 (**Nepal = automatically eligible**) |
| 17 | https://nlnet.nl/news/2026/20260903-call.html | ✅ 200 | deadline, cadence change, AI-policy warning |
| 18 | https://nlnet.nl/NGI0/bestpractices/ | ✅ 200 | Best-practice resources (see Appendix B) |
| 19 | https://codeberg.org/forgejo/sustainability/raw/branch/main/2025/2025-08-01-nlnet-ngi0-commons-federation/application.md | ✅ 200 | §6.5 real submitted application |
| 20 | https://socialhub.activitypub.rocks/t/forgefed-nlnet-grant-application/2598/7 | ✅ 200 (third-party forum) | §3.3 corroboration: a real applicant used **$54/hour** over 936 h for a $50,544 ask (2022). `[UNCERTAIN as policy — third-party, dated, USD]` |
| 21 | https://nlnet.nl/foundation/request/ | ✅ 200 but content-free (redirect-ish stub pointing to /propose) | — |
| 22 | https://nlnet.nl/foundation/policies/ | — **not fetched** (superseded: v2.0 URL found via the v1.1 archive page instead) | — |

## Appendix B — Best-practices resources Restack points to (Appendix to §6)

`https://nlnet.nl/NGI0/bestpractices/` is a **resource hub, not a scoring rubric**. It is "Shared resources developed by NGI Zero" covering Accessibility (HAN University guides / WCAG), Internationalization (`Best-Practices-l10n-i18n-v2.pdf`, Jan 2026), Security (`ROS_opsec-best-practices.pdf` by Radically Open Security), Standardization (ETH Zürich), Diversity & Inclusion (`DiversityAndInclusionGuide-v4.pdf`), Legal/forking & trademarks (ifrOSS), and FSFE licensing compliance (REUSE, licence compatibility matrix). `[VERIFIED from https://nlnet.nl/NGI0/bestpractices/]`

**No proposal-writing advice is published on this page** — it is all downstream project-quality guidance. Its practical use for MeshDoc: it tells us which topics NLnet's support partners will push on after award, so we can pre-empt them (security review, i18n, WCAG, REUSE compliance, licence choice). `[Interpretation]`

There is **no published "what makes a good proposal" rubric beyond §6** — the Guide for Applicants *is* that document. `[VERIFIED by absence across all NLnet pages fetched]`

## Appendix C — Open questions / flagged uncertainties

1. **Minimum hourly rate** — existence confirmed ("We also have a minimum rate"), value never published. `[UNCERTAIN]`
2. **Proposal title / website field character limits** — no `maxlength` visible in the fetched form HTML/text. Assume generous but keep short. `[UNCERTAIN]`
3. **Whether the un-versioned `/foundation/policies/generativeAI/` page is broken or intentionally redirecting** — it returns 200 with an empty body. Always cite `/2.0/`. `[VERIFIED behaviour, cause UNCERTAIN]`
4. **Nepali tax treatment of an NLnet donation** — not covered by any NLnet or Philea resource. Needs local professional advice. `[UNCERTAIN — materially important]`
5. **Next deadline after 3 Nov 2026** — derived as 3 Jan 2027 from "3rd of every odd month", not explicitly listed. `[UNCERTAIN]`
6. **Whether an independent security audit will be required** — only for projects **>€50k**, and it "MAY" apply. A first grant at ≤€50k should avoid it, but note MeshDoc's crypto surface makes a voluntary audit an attractive optional milestone. `[VERIFIED rule; application to us is Interpretation]`
7. **Whether "Restack Fund" or "Other / open call" is the better dropdown choice** — the brief says Restack; the form offers it explicitly. No reason to hedge. `[VERIFIED option exists]`

---

*End of document. Every quotation above was read from the cited URL in this session; no quote has been reconstructed or paraphrased inside quotation marks.*
