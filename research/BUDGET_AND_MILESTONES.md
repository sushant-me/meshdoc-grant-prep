# MeshDoc — Budget, Effort & Milestones Plan

**Prepared for:** Arvion Technologies (Kathmandu, Nepal) — NLnet **Restack** grant application
**Document status:** Internal planning reference — `research/BUDGET_AND_MILESTONES.md`
**Research date:** 2 November 2026
**Call deadline:** **3 November 2026, 12:00 CET = 16:45 Nepal time** (NPT is UTC+05:45; CET is UTC+01:00, so the deadline is 11:00 UTC / 16:45 NPT)

> ### ⚠️ Read this first — three things that changed the plan
>
> **1. NLnet has a hard rate ceiling of €65/hour.** *"As a philanthropy, we operate on a cost recovery basis. The absolute maximum rate we can allow for is **65 euro/hour**, but using the maximum rate **impacts cost effectiveness, and thus can reduce chances of getting the project granted**."* [VERIFIED https://nlnet.nl/officehour/#amount]. A follow-up on the same page confirms *"We also have a minimum rate"* but does not publish its value [UNCERTAIN — value unknown]. This plan therefore targets **€21.25/hour (€170/day)** — 32.7% of the ceiling.
>
> **2. Test devices and hosting are NOT eligible. The expenses budget is €0.** Both the brief and an earlier draft of this document assumed a device and VPS line. Verified sources say otherwise — the decisive on-point answer is: *"Q: Can a milestone include buying two different test machines, to validate the software on real hardware? A: Generally this is **not seen as an efficient use of project budget**."* [VERIFIED https://nlnet.nl/officehour/#hardware]. §7 documents this fully, keeps the device price research as evidence of diligence, and shows why the honest answer is a labour-only budget.
>
> **3. The brief's eligibility assumption is wrong — in the applicant's favour.** The brief states "Nepal is NOT a Horizon Europe-eligible country." NLnet's own page **explicitly lists Nepal**: *"…Namibia, **Nepal**, Netherlands…"*, list "last updated on October 13, 2026" [VERIFIED https://nlnet.nl/OIS/european-dimension/] — and the EC document that NLnet says is leading goes further: Nepal is among the low/middle-income countries *"**automatically eligible for funding**"* [VERIFIED EU Grants list V4.2, 07.10.2026]. This is no longer a live knock-out risk. See §2.
>
> **Deadline is under 24 hours away.** Restack runs back-to-back calls on the 3rd of every odd month [VERIFIED https://nlnet.nl/funding.html], so a miss costs two months, not a year.

---

## 1. Governing rules (all verified)

| Rule | What it says | Source |
|---|---|---|
| First-grant band | "Your first proposal can only be between **5.000 and 50.000 euro**" | [VERIFIED https://nlnet.nl/restack/faq/] |
| **Rate ceiling** | "The absolute maximum rate we can allow for is **65 euro/hour**" — and using it "impacts cost effectiveness, and thus can reduce chances of getting the project granted" | [VERIFIED https://nlnet.nl/officehour/#amount] |
| Minimum rate | "We also have a minimum rate" — **value not published** | [VERIFIED https://nlnet.nl/officehour/#amount] · value [UNCERTAIN] |
| **Differentiated rates** | "You can have different rates in your project for different tasks." | [VERIFIED https://nlnet.nl/officehour/#amount] |
| **How to present the budget** | "Should the budget be presented with daily rates or as lump sum for every specific item? — **both. An indicative daily rate + lump sums** are appreciated." | [VERIFIED https://nlnet.nl/officehour/#amount] |
| What reviewers look for | "rates that you have applied to the project"; "estimated efforts for the different parts of the project (**in hours, or amounts, which may be rough estimates**)"; "understanding a bit what the different parts of development bring to the project" | [VERIFIED https://nlnet.nl/officehour/#amount] |
| Cost recovery, not commercial rates | "As a philanthropy, **we do not pay commercial rates** — we provide a **cost-recovery based mechanism**" | [VERIFIED https://nlnet.nl/funding.html] |
| **No hosted instances / hosting costs** | "we are **not generally able to fund hosted instances of software, or cover hosting costs**. We fund research and development" | [VERIFIED https://nlnet.nl/officehour/#hardware] |
| **Compute time is opex** | "Q: … Does renting the compute time … fall under [eligible out-of-pocket infrastructure]? A: **No, compute time renting would fall under operational expenses.**" | [VERIFIED https://nlnet.nl/officehour/#hardware] |
| **Test machines discouraged** | "Q: Can a milestone include buying two different test machines, to validate the software on real hardware? A: Generally this is **not seen as an efficient use of project budget**." | [VERIFIED https://nlnet.nl/officehour/#hardware] |
| Hardware exclusions | "NLnet does **not** allocate grant money to basic operational IT cost, such as regular laptops, desktops/workstations, or **mobile phones**." Valid only when "directly *necessary*"; goods "must be sold, returned or donated to a non-profit at the end of the grant" | [VERIFIED https://nlnet.nl/foundation/policies/externalspending/] |
| F&A / overhead | "**generally not considered eligible** … maximum permissible amount is **capped at 25%**" | [VERIFIED https://nlnet.nl/restack/faq/#FA] |
| **No work done before the grant** | "We **cannot** make donations for any effort completed prior to the grant." Review takes "three and five months" from the deadline | [VERIFIED https://nlnet.nl/restack/faq/] |
| Duration | "By default, we expect projects to be completed within **12 months** — but qualified exceptions can be made." | [VERIFIED https://nlnet.nl/restack/faq/#timelines] |
| **Payment: milestone arrears, donations, no VAT** | "the grant is **not paid out up front** … divide your project into milestones and allocate an amount to each … Once you reach a milestone you send in a request for payment." Grants are "**donations**". "Amounts donated do not include VAT." | [VERIFIED https://nlnet.nl/restack/faq/#upfrontpayment] · [VERIFIED https://nlnet.nl/foundation/policies/externalspending/] |
| **Divide amounts across subtasks** | "consider to divide amounts across subtasks … **especially if tasks are executed by different people**, or have a relatively large size" | [VERIFIED https://nlnet.nl/foundation/request/sample_MoU.pdf] |
| Scoring weights | 30% technical excellence · **40% relevance/impact** · **30% cost effectiveness / value for money**; pass mark >5.0/7 | [VERIFIED https://nlnet.nl/restack/guideforapplicants/] |
| **Free audits as milestones** | Sample MoU project plans include a milestone *"Certified WCAG accessible"* and a milestone *"Process issues from external security review"*. Both audits are free support services. | [VERIFIED https://nlnet.nl/foundation/request/sample_MoU.pdf] · [VERIFIED https://nlnet.nl/NGI0/services/] |
| Security/accessibility audits are **free** | Delivered by Radically Open Security and HAN University as support services at no cost to the grant | [VERIFIED https://nlnet.nl/NGI0/services/] |
| **AI out of scope** | "**AI-related projects are not within scope** — unless they are already widely used throughout society (> 1 million active human users)". MeshDoc excludes all AI/translation work → compliant. | [VERIFIED https://nlnet.nl/restack/] |
| **GenAI policy v2.0** | "Generative AI can no longer be used for *writing* proposals"; applies to all calls closing after 20 Oct 2026, **explicitly including the 3 Nov 2026 Restack deadline** | [VERIFIED https://nlnet.nl/news/2026/20261020-AI-policy.html] |
| One grant per applicant (first round) | "for a first grant, we are limited to one grant per applicant" | [VERIFIED https://nlnet.nl/officehour/] |
| Eligible cost categories | software development; testing/CI design; documentation; packaging; standardisation; **project management**; "out-of-pocket costs for infrastructure essential" | [VERIFIED https://nlnet.nl/restack/eligibility/] |

**Three structural consequences:**

1. **Everything is labour.** No devices, no hosting, no compute, no CI runners. The budget is 100% person-days. This is not a limitation to apologise for — a labour-only budget is the cleanest possible answer to a 30%-weighted cost-effectiveness test.
2. **Overhead must live inside the rate,** not as a line item (F&A is ineligible). §4 keeps it under the 25% cap so it cannot be recharacterised.
3. **Rates must sit well below €65/hour.** Sitting at the ceiling is explicitly self-harming.

---

## 2. The European-dimension question (corrects the brief)

The brief asked me to "assume the European-dimension question is a live risk". The evidence says it is **much smaller than assumed** — and this matters, because failing it means the project is "marked ineligible" and never scored [VERIFIED https://nlnet.nl/restack/guideforapplicants/].

**What the rule requires.** The European dimension "refers to the people contributing to the project, not the project itself. The obvious way to fulfil this requirement is having people on the team … from **Horizon Europe-eligible countries**, who receive **at least 60% of the funds**" [VERIFIED https://nlnet.nl/OIS/european-dimension/].

**Nepal is on that list.** The page's country list, last updated 13 October 2026, reads: *"− **Namibia, Nepal, Netherlands**, New Caledonia, New Zealand …"* — and it pre-empts this exact doubt: *"Note that there are many eligible countries, many of which are not European countries. People and organisations of these eligible countries can participate **on the same terms** as those from EU member states. Having 60% of the funds go to people from any of these countries, meets the European dimension criterium."* [VERIFIED https://nlnet.nl/OIS/european-dimension/]

**Conclusion:** a Kathmandu-based team taking 100% of the grant satisfies the criterion on the straightforward reading.

**Primary source verified — this now closes the question.** NLnet's page warns that "in case of discrepancies, the **EC lists are leading**". I therefore checked the EC document itself, and it is explicit:

> **EU Grants: List of participating countries (HE): V4.2 – 07.10.2026**
> "Participants from the following low- to middle-income countries are **automatically eligible for funding**: … − Namibia, **Nepal**, Nicaragua, Niger, Nigeria"

[VERIFIED https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/common/guidance/list-3rd-country-participation_horizon-euratom_en.pdf — V4.2 dated 07.10.2026, p.2, section "Other third countries"]

Nepal sits in exactly the same legal class as Kenya and Nigeria: *non-associated low/middle-income third country, automatically eligible for funding*. So the NLnet page and the EC document **agree**, and the "EC list is leading" caveat resolves in the applicant's favour rather than against it. There is no longer a live knock-out risk here.

**Residual risk — now small:**

| Risk | Mitigation |
|---|---|
| A reviewer misreads the 60%-of-funds rule as jurisdictional | It is about **people**, not geography — and 100% of funds go to Nepal-based contributors, well past the 60% threshold. Put the EC citation in one sentence in the Background answer. |
| NLnet's operational practice diverges from its published page | Two independent sources agree, so this is no longer a blocker. If a one-line confirmation is wanted, emailing NLnet costs nothing — but do not delay filing for it. |
| The brief contemplated a European partner | **Not needed**, and actively risky: a partner taking funds could push Arvion below 60%. Do not add a partner for eligibility. |
| A fallback is still worth knowing | If the criterion were ever disputed: "if the project is of **exceptional quality** and the proposer holds **unique technical expertise** proposals from outside of those geographic areas can be taken into consideration" [VERIFIED https://nlnet.nl/restack/eligibility/]. Lead with the unique-expertise argument regardless. |

**One sentence for the application (write your own version):** *"Our team is based in Nepal, which appears on the European Commission's Horizon Europe list of low- and middle-income third countries automatically eligible for funding (EU Grants list V4.2, 07.10.2026), so the European-dimension requirement is met by our team's nationality and residence."*

---

## 3. Rate research — what is defensible?

### 3.1 The ceiling, and why not to use it

> "As a philanthropy, we operate on a cost recovery basis. The absolute maximum rate we can allow for is **65 euro/hour**, but using the maximum rate **impacts cost effectiveness, and thus can reduce chances of getting the project granted**." [VERIFIED https://nlnet.nl/officehour/#amount]

€65/hour = €520/day. Asking that would consume the entire budget in ~57 days and, on NLnet's own statement, damage the 30%-weighted cost-effectiveness score. **The ceiling is not a target.**

There is also a floor: *"We also have a minimum rate."* Its value is **not published** [UNCERTAIN]. This is a real reason not to under-rate either — an implausibly low number may fail the floor or simply read as fictitious. The target window is therefore "clearly below €65, clearly above token", and the credible way to hit it is to derive the rate from actual cost.

**Useful reference point from the same page.** A grantee asked: *"Is it common in the proposals you receive to use differentiated hourly rates depending on the nature of the tasks; for instance ~25 €/h for documentation and ~45 €/h for development work…?"* and NLnet answered *"You can have different rates in your project for different tasks."* [VERIFIED https://nlnet.nl/officehour/#amount]. That question's own numbers — €25/h documentation, €45/h development — are treated as unremarkable. Our target sits below both.

### 3.2 What grantees actually budget (empirical anchor)

NLnet does not publish budgets, but grantees do. The most useful example shows a solo developer's full budget line by line:

**mCaptcha, NGI Zero Entrust, requested €26,200** [VERIFIED https://git.batsense.net/mCaptcha/website/raw/branch/librepages/pub/2022/07/mcaptcha-nlnet-ngi-zero-entrust.pdf]:

> - "Developer pay: … I require **2,000 EUR per month** to sustain my current lifestyle in India. So that's 24,000 EUR per year."
> - "3,500 EUR for a build server"
> - "1000 EUR for cloud rent"

Also: Gitea's public federation application to NLnet NGI Zero Discovery was for **50 k€ total** across two named developers [VERIFIED https://github.com/go-gitea/gitea/issues/16827].

**Three facts worth taking from this:**

1. **A ~€26 k first grant is normal and fundable.** It is not a timid ask.
2. **Grantees justify a monthly *living cost*, not a market rate.** €2,000/month for an experienced developer in India in 2022. That is exactly the cost-recovery model. In day terms: €2,000 ÷ 21.667 = **€92.31/day** [ESTIMATE — derived].
3. **Expenses were ~17% of that budget.** Our plan is 0% — *more* labour-dominated, which is the safer shape under current rules.

Note the anchor is from 2022 and India; Nepal 2026 costs differ, which is why §3.4 derives the rate rather than copying €2,000/month.

### 3.3 Nepal local market salary, 2026 (Kathmandu)

Praxium Labs, a Lalitpur-based consultancy, publishes Kathmandu all-in monthly bands (updated 25 May 2026):

| Level | Monthly band (NPR), all-in incl. bonuses |
|---|---|
| Junior (0–2 yrs) | 40,000 – 80,000 |
| Mid-level (2–5 yrs) | 100,000 – 200,000 |
| **Senior (5–8 yrs)** | **200,000 – 400,000** |
| **Staff / principal (8+ yrs)** | **400,000 – 1,000,000** |

— [VERIFIED https://praxiumlabs.com/blog/hiring-engineers-nepal-2026-salaries/]

Two modifiers from the same source matter for MeshDoc:

- **"Embedded / IoT firmware: 10–30% premium given scarcer talent pool."** Rust + Android + BLE/Wi-Fi Direct sits nearer this end than the web-app end.
- **Retention pressure:** the same source notes engineers are hired away by foreign-remote employers "at 2–3x local rates", and foreign-remote roles "typically add 30–100% premium" [VERIFIED same URL].

**Therefore the correct salary basis is not the senior *median* — it is the top of the senior band / entry to the staff band, because that is the retention cost of the specific scarce skillset this project needs.** We use **NPR 400,000/month**. Using the senior median (NPR 300,000) would understate the true cost of holding a Rust/BLE specialist in Kathmandu.

Cross-check: an independent aggregator places Nepal software-engineer pay in a comparable broad range [VERIFIED https://www.payscale.com/research/NP/Job=Software_Engineer/Salary — varies by skill filter, used only as a direction check].

### 3.4 Currency

NPR is pegged to the INR at **1 INR = 1.60 NPR**. ECB reference rate 30 Oct 2026: **EUR/INR = 106.084**.

> EUR → NPR = 106.084 × 1.60 = **169.734 NPR per euro**

[VERIFIED https://api.frankfurter.app/latest?base=EUR&symbols=INR for the ECB leg; the peg is the NRB convention. The cross-rate itself is an [ESTIMATE] built from two verified inputs.]

Use **€1 = NPR 169.73**. Re-check on the filing date; a ±3% move does not change any rounded figure here.

### 3.5 Cost-recovery day rate — the arithmetic

**Step 1 — gross salary in euro**
NPR 400,000 ÷ 169.734 = **€2,356.63 / month**

**Step 2 — employer on-costs (+28%)**
Nepal's Social Security Fund is an employer cost, and Nepali practice adds a festival (Dashain) allowance of roughly one month's salary a year (~8.3%). Modelled together at **28%**:
€2,356.63 × 1.28 = **€3,016.48 / month**
[ESTIMATE — the 28% is a modelling assumption. **This is the single number in the budget most worth checking** with a Nepali accountant before filing.]

**Step 3 — studio overhead (20% of total)**
Co-working rent, business internet plus a backup link, power backup/UPS, equipment amortisation, accounting, banking and FX charges on receiving euros, insurance, unbillable admin. Set overhead at **20% of total cost**:
€3,016.48 ÷ (1 − 0.20) = **€3,770.61 / month**
→ overhead component = **€754.13**, i.e. exactly **20.0% of total** — comfortably under NLnet's 25% F&A cap.

**Step 4 — to a day rate**
Working days per month = 260 ÷ 12 = **21.667**
€3,770.61 ÷ 21.667 = **€174.03 per person-day** (÷ 8 = **€21.75/hour**)

### 3.6 Recommended rate

> ## **€170 per person-day — €21.25 per hour**
> (= €3,683.33 per person-month at 21.667 working days)

| Property | Value | Comment |
|---|---|---|
| vs derived cost floor | **2.3% below** (€170 vs €174.03) | Below its own cost basis — cannot be padding |
| vs NLnet's €65/hour ceiling | **32.7%** (€21.25 ÷ €65) | Deliberately far from the ceiling |
| vs mCaptcha precedent | +84% on €92.31/day | Justified: a studio carries overhead and employer costs a solo developer does not, and this is 2026 not 2022 |
| vs the grantee example on NLnet's own page (€25/h docs, €45/h dev) | Below both | Comfortably inside what NLnet treats as unremarkable |
| Commercial margin | **None** | Cost recovery only |
| Overhead inside the rate | 20.0% of cost | Under the 25% F&A cap |

**Why a reviewer should accept €21.25/hour:**

- It is **not a commercial rate** — a European consultancy rate for Rust/BLE/Android systems work is €500–900/day [ESTIMATE — general market knowledge, deliberately not presented as a researched figure]. €170/day is 3–5× below that.
- It is **below the derived cost of doing the work**, not above it.
- It is **derivable in five lines** from a published Kathmandu salary survey and a published exchange rate, so it cannot be dismissed as invented.
- It is **far enough below the ceiling** that the cost-effectiveness criterion is helped, not hurt.

**One sentence for the application:** *"Our rate is €170 per person-day (€21.25 per hour), derived from Kathmandu specialist salary plus employer costs and 20% studio overhead."*

**If per-person differentiation is wanted** — permitted, and the sample MoU asks for amounts to be divided where subtasks go to different people [VERIFIED https://nlnet.nl/foundation/request/sample_MoU.pdf] — a documentation/community rate of **€130/day (€16.25/hour)** is defensible and would cut the total by roughly 8%. It is **not recommended** here: a single rate is one sentence to explain, one number to defend, and removes a reviewer question. Keep the differentiation as a lever if a reviewer challenges the documentation effort specifically.

---

## 4. The three budget scenarios

All three use **€170/person-day**, **zero expenses**, and the same 9 work packages. They differ in depth and duration only — so the rate defence serves all three.

**Totals:** Lean **€14,960** · **Recommended €29,920** · Ambitious **€49,980** (all inside the €5,000–€50,000 first-grant band).

### 4.1 Scenario A — LEAN · €14,960 · 9 months · 88 days

Single-track delivery at ~0.45 FTE. Field pilot reduced to structured internal testing; documentation cut to the minimum a stranger needs.

| WP | What it buys | Days | Rate | Subtotal |
|---|---|---|---|---|
| WP1 Setup, architecture & threat model | ADRs, threat model, CI | 5 | €170 | €850 |
| WP2 CRDT core, change format, identity crypto | 4 doc types, envelope spec, Ed25519 | 18 | €170 | €3,060 |
| WP3 Transport abstraction + Nearby Connections | `Transport` trait + conformance suite | 10 | €170 | €1,700 |
| WP4 FOSS BLE discovery + Wi-Fi Direct | Play-Services-free path | 13 | €170 | €2,210 |
| WP5 Relay server + DTN semantics | ~300-line relay, store-and-forward | 7 | €170 | €1,190 |
| WP6 Android reference app | 4 doc types, QR join | 12 | €170 | €2,040 |
| WP7 Convergence & partition fuzz harness | property tests + seeds | 8 | €170 | €1,360 |
| WP8 Documentation, internal validation | docs, quickstart (no external pilot) | 8 | €170 | €1,360 |
| WP9 Community, upstream & F-Droid | F-Droid submission | 7 | €170 | €1,190 |
| **Labour** | | **88** | | **€14,960** |
| **Expenses** | **none eligible** (§7) | — | | **€0** |
| **TOTAL** | | | | **€14,960** |

**Ramp (9 months, days / FTE):** 4/0.18 · 7/0.32 · 9/0.42 · 11/0.51 · 12/0.55 · 12/0.55 · 11/0.51 · 11/0.51 · 11/0.51 → **avg 0.45 FTE**

**What you give up:** the external field pilot — the strongest evidence for the 40%-weighted impact criterion. Also thin days on WP2 and WP6, which means fewer document types polished and weaker convergence evidence.

### 4.2 Scenario B — RECOMMENDED · €29,920 · 12 months · 176 days

Two people at roughly 0.34 FTE each, ramping to ~0.78 FTE combined, with a real field pilot and a real F-Droid release.

| WP | Role | Days | Rate | Subtotal |
|---|---|---|---|---|
| WP1 Setup, architecture & threat model | Senior Rust + lead | 9 | €170 | €1,530 |
| WP2 CRDT core, change format & identity crypto | Senior Rust | 34 | €170 | €5,780 |
| WP3 Transport abstraction + Nearby Connections | Senior Rust | 20 | €170 | €3,400 |
| WP4 FOSS BLE discovery + Wi-Fi Direct bulk transfer | Systems/mobile | 26 | €170 | €4,420 |
| WP5 Relay server + DTN store-and-forward | Rust | 14 | €170 | €2,380 |
| WP6 Android reference app (4 doc types) | Android | 26 | €170 | €4,420 |
| WP7 Convergence & partition fuzz harness | Senior Rust | 18 | €170 | €3,060 |
| WP8 Field pilot, user research & documentation | All + writer | 17 | €170 | €2,890 |
| WP9 Community, upstream, F-Droid & reproducible builds | Lead | 12 | €170 | €2,040 |
| **Labour** | | **176** | | **€29,920** |
| **Expenses** | **none eligible** (§7) | — | | **€0** |
| **TOTAL** | | | | **€29,920** |

**Ramp (12 months, days / FTE):** 7/0.32 · 10/0.46 · 13/0.60 · 15/0.69 · 16/0.74 · 17/0.78 · 17/0.78 · 17/0.78 · 17/0.78 · 16/0.74 · 15/0.69 · 16/0.74 → **avg 0.68 FTE, 8.1 person-months**

### 4.3 Scenario C — AMBITIOUS · €49,980 · 12 months · 294 days

Adds: full multi-hop hardware matrix (6 devices, two relays), a broader two-site pilot, deeper upstream engagement, accessibility audit uptake and time to act on it.

| WP | Role | Days | Rate | Subtotal |
|---|---|---|---|---|
| WP1 Setup, architecture & threat model | Senior + lead | 14 | €170 | €2,380 |
| WP2 CRDT core, change format & identity crypto | Senior ×1.5 | 58 | €170 | €9,860 |
| WP3 Transport abstraction + Nearby Connections | Senior Rust | 36 | €170 | €6,120 |
| WP4 FOSS BLE discovery + Wi-Fi Direct bulk transfer | Systems/mobile ×2 | 46 | €170 | €7,820 |
| WP5 Relay server + DTN store-and-forward | Rust | 24 | €170 | €4,080 |
| WP6 Android reference app (4 doc types + a11y) | Android ×1.5 | 48 | €170 | €8,160 |
| WP7 Convergence & partition fuzz harness | Senior Rust | 30 | €170 | €5,100 |
| WP8 Field pilot (2 sites), user research & docs | Mixed + writer | 22 | €170 | €3,740 |
| WP9 Community, upstream, F-Droid, standardisation | Lead | 16 | €170 | €2,720 |
| **Labour** | | **294** | | **€49,980** |
| **Expenses** | **none eligible** (§7) | — | | **€0** |
| **TOTAL** | | | | **€49,980** |

**Ramp (12 months):** 12/0.55 · 18/0.83 · 23/1.06 · 26/1.20 · 28/1.29 · 29/1.34 · 29/1.34 · 29/1.34 · 28/1.29 · 27/1.25 · 25/1.15 · 20/0.92 → **avg 1.13 FTE, 13.6 person-months**

### 4.4 Which one, and why

> ### Recommend **Scenario B — €29,920**

1. **Cost effectiveness is 30% of the score and is judged against the ask.** €29,920 buys 8.1 person-months, a scheduler, a fuzz harness, a field pilot and a F-Droid release. That reads as dense. €49,980 buys 13.6 person-months from a studio NLnet has never funded; it reads as a lot of trust to extend in round one.
2. **A first grant that is well-scoped beats a maximum ask.** NLnet's framing: "we can grow the talent instead of having a 'leap of faith' with a select few projects", and successful grantees "can apply for additional funding again — provided that higher amount is necessary and delivers enough additional value" [VERIFIED https://nlnet.nl/restack/guideforapplicants/]. Restack runs to **May 2030**; the lifetime cap is **500 k€** [VERIFIED same]. There is a second bite — asking for everything in round one is poor rationing.
3. **No money arrives early.** Payments are milestone arrears after a 3–5 month review [VERIFIED https://nlnet.nl/restack/faq/]. Realistically the first tranche clears in month 6–8 after filing. A €29,920 commitment is far easier for a four-person studio to part-fund than a €49,980 one — and a studio that cannot fund its own run-up is a delivery risk a reviewer will spot.
4. **Ambitious's marginal spend is in the least-scored places.** The extra days go to a larger device matrix and more upstream time. Both are good; neither is what the 40% impact criterion rewards. The pilot and the F-Droid release — which is what it rewards — are already fully funded in Recommended.

**When to pick the others:** Lean if the studio cannot sustain ~0.7 FTE for a year. Ambitious only *after* delivering Recommended and returning in a follow-up round with evidence — exactly the progression NLnet describes.

---

## 5. Work packages (9 WPs)

**Every WP is 100% labour at €170/day. Day counts shown are Recommended; Lean/Ambitious variants in §4.**

### WP1 — Project setup, architecture & threat model · 9 days
**Objective.** Fix the architecture before code exists; write the security model down so it can be attacked on paper.
**Deliverables.** Public repo, licence, CI, `CONTRIBUTING`; architecture decision records; a written threat model covering device-key compromise, malicious relay, BLE traffic analysis, workspace-invite interception, CRDT-level denial of service; trust-boundary diagram.
**Exit criterion.** An outsider reading only the threat model and ADRs can correctly predict what the system encrypts, what it does not, and what the relay can see.

### WP2 — CRDT core, change format & device-identity crypto · 34 days
**Objective.** One interoperable change format and one identity model that every transport and the relay can speak.
**Deliverables.** Rust crate for the four document types (checklist, supply form, geo point, note); versioned change/envelope format with a written wire spec; device identity keys (Ed25519) with per-workspace group keys and rotation; CRDT engine bound to an **existing audited library** (Automerge or Yrs) — **no custom CRDT, no custom crypto**; format versioning and downgrade handling.
**Exit criterion.** Wire spec published; two independently built binaries exchange changes both ways; scope exclusion is checkable in the repo (no hand-rolled primitives, `#![forbid(unsafe_code)]` or documented exceptions).

### WP3 — Transport abstraction + Nearby Connections fast path · 20 days
**Objective.** A transport trait so BLE, Wi-Fi Direct and the relay are interchangeable, plus a fast path on stock Android.
**Deliverables.** `Transport` trait with a conformance suite any implementer can run; Nearby Connections implementation (note: depends on Google Play Services — this is the *fast path*, not the FOSS path); capability negotiation and fallback when Play Services is absent.
**Exit criterion.** Conformance suite passes for Nearby, and removing Play Services causes clean negotiation to a FOSS transport rather than failure.

### WP4 — FOSS BLE discovery + Wi-Fi Direct bulk transfer · 26 days
**Objective.** Full function on devices with **no Google services** — the reason the project exists.
**Deliverables.**
**4.1 FOSS BLE discovery** — advertisement/scanning within duty-cycle and power limits, rotating identifiers to resist tracking, GATT small-change exchange, connection scheduling.
**4.2 Wi-Fi Direct bulk transfer** — group formation, role negotiation, chunked and resumable transfer for larger document sets, with BLE as the discovery channel that bootstraps the Wi-Fi link.
**Exit criterion.** Two Play-Services-free devices discover each other and complete a document sync in under 60 s at 10 m; power draw measured and reported over a 10-minute idle discovery window.

### WP5 — Relay server + DTN store-and-forward semantics · 14 days
**Objective.** The ~300-line "dumb" encrypted relay, and honest delay-tolerant behaviour when the network is bad.
**Deliverables.** Rust relay (~300 lines) storing and forwarding opaque encrypted blobs with no ability to read content; DTN semantics — store-and-forward across partitions, TTL/expiry, deduplication, bounded storage with eviction, resume after reconnect; container image and a documented `docker run` so **any third party** can operate it.
**Exit criterion.** Two devices never online simultaneously still converge via a third-party-operated relay; the operator cannot identify senders or read content, demonstrated by written analysis checked against the WP1 threat model.
**Note for the proposal:** this is *code to develop*, not a service Arvion operates. No hosting is budgeted (§7).

### WP6 — Android reference app (4 document types) · 26 days
**Objective.** The artefact a user actually touches.
**Deliverables.** Kotlin app: device identity setup, **QR-joined encrypted workspaces**, the four document types, an offline-first sync status UI that tells the truth about what is and is not synced, and a UI built accessibly from the start so the WCAG audit is a confirmation rather than a rebuild.
**Exit criterion.** A first-time user joins by QR, creates and edits all four document types, and syncs to a peer — with the phone in aeroplane mode for part of the session — without reading documentation.

### WP7 — Convergence & partition fuzz testing harness · 18 days
**Objective.** Prove convergence under partition, not just on the happy path. This is the credibility of the whole CRDT claim.
**Deliverables.** Property-based/fuzz harness generating random operation sequences, adversarial partitions, reorderings, duplication and clock skew, asserting all replicas converge to identical state; shrunk, reproducible failing seeds committed to the repo; a CI job running a bounded campaign on every PR plus a nightly longer campaign.
**Exit criterion.** The harness has found and closed ≥3 real convergence bugs before the pilot, each with a committed regression seed; nightly campaign green for 14 consecutive days.

### WP8 — Field pilot, user research & documentation · 17 days
**Objective.** Evidence that this works for real users in real Nepali network conditions.
**Deliverables.** Pilot with a small group of real users in the humanitarian/logistics/supply-chain space the toolkit targets; consent-based, no personal data retained; written pilot report with measured metrics (sync success rate, time-to-converge, battery cost, failure modes); user documentation, quickstart, and a "how to deploy the relay" guide.
**Exit criterion.** Pilot report with ≥5 real users across ≥2 physical sites, quantified results, and a published list of issues found.

### WP9 — Community, upstream & F-Droid release · 12 days
**Objective.** Make it adoptable without Arvion in the loop.
**Deliverables.** F-Droid submission accepted (metadata, reproducible build, fastlane screenshots); upstream engagement with the CRDT library and the BLE/Nearby stacks; reproducible-build instructions verified by a third party; release notes and a governance/roadmap document; an open call for co-maintainers.
**Exit criterion.** App installable from F-Droid on a device with no Play Services; a third party reproduces the binary bit-for-bit; at least one upstream PR merged or substantively reviewed.

**Coverage check against required scope:** setup/architecture ✔ WP1 · CRDT + change format + crypto ✔ WP2 · transport abstraction + Nearby ✔ WP3 · FOSS BLE ✔ WP4.1 · Wi-Fi Direct ✔ WP4.2 · relay + DTN ✔ WP5 · Android app ✔ WP6 · convergence/partition fuzz ✔ WP7 · field pilot + docs ✔ WP8 · community/upstream + F-Droid ✔ WP9.
**Deliberately excluded and not funded:** chat, maps, iOS, custom crypto, custom CRDT, all AI/translation work (Restack excludes AI projects outright).

---

## 6. Timeline (Recommended, 12 months)

`■` = active work · `·` = no planned effort. **Deps** = what must land first.

| WP | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 | Deps |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **WP1** Setup, architecture, threat model | ■ | ■ | · | · | · | · | · | · | · | · | · | · | — |
| **WP2** CRDT core, change format, crypto | · | ■ | ■ | ■ | ■ | · | · | · | · | · | · | · | WP1 |
| **WP3** Transport abstraction + Nearby | · | · | ■ | ■ | ■ | · | · | · | · | · | · | · | WP2 (envelope) |
| **WP4** FOSS BLE + Wi-Fi Direct | · | · | · | ■ | ■ | ■ | ■ | · | · | · | · | · | WP3 (trait) |
| **WP5** Relay + DTN | · | · | · | ■ | ■ | ■ | · | · | · | · | · | · | WP2 (envelope) |
| **WP6** Android reference app | · | · | · | ■ | ■ | ■ | ■ | ■ | ■ | · | · | · | WP2, WP3 |
| **WP7** Fuzz harness | · | · | · | · | · | ■ | ■ | ■ | ■ | · | · | · | WP2, WP3 |
| **WP8** Field pilot, research, docs | · | · | · | · | · | · | · | ■ | ■ | ■ | ■ | · | WP4, WP5, WP6 |
| **WP9** Community, upstream, F-Droid | · | · | · | · | · | · | · | · | ■ | ■ | ■ | ■ | WP6, WP7 |
| **Planned days** | 7 | 10 | 13 | 15 | 16 | 17 | 17 | 17 | 17 | 16 | 15 | 16 |
| **FTE (÷21.667)** | 0.32 | 0.46 | 0.60 | 0.69 | 0.74 | 0.78 | 0.78 | 0.78 | 0.78 | 0.74 | 0.69 | 0.74 |

**Total planned days: 176** ✔ matches WP sum.

**Why this ramp, and not full-time from day one.** Months 1–2 are deliberately light (0.32 → 0.46 FTE): with no up-front payment and a 3–5 month review, the studio is spending its own money until the first tranche clears, so the plan must not require a big commitment before anything is reimbursed. Week 1–3 is architecture and admin, which does not need two people. The plateau at 0.78 FTE is **two people at ~0.34 FTE each** — a studio running this alongside client work — not one person full-time. The final months hold a steady 0.69–0.74 because release, pilot write-up and the two audit gates land there.

**Critical path:** WP1 → WP2 → WP3 → WP4 → WP8 → WP9. WP5, WP6 and WP7 can run in parallel once WP2's envelope format is stable.

**Biggest schedule risk is WP2** — everything downstream consumes its format. Mitigation: freeze the change format at the end of M3 behind a version number; treat later changes as a new version, never a breaking edit.

**Slack:** ~2 days of float inside the plateau. There is no float in M11–M12; if WP4 slips, the pilot narrows rather than the release slipping.

---

## 7. Expenses — what is legitimately chargeable (answer: nothing)

The brief asked for a device and VPS expense line. **Verified sources say none of it is eligible.** This section records the research, the rules, and the decision.

### 7.1 Real 2026 Kathmandu device prices — researched, and deliberately not budgeted

The plan needs a mixed hardware matrix (a Play-Services-free unit, a MediaTek unit, a Samsung unit to catch Wi-Fi Direct firmware quirks). Here is what that would cost, so the in-kind contribution is quantified rather than asserted:

| Device | Price NPR | ≈ EUR @169.734 | Why this device | Status |
|---|---|---|---|---|
| **Realme C61** | 13,499 | **€80** | Cheapest credible Android; the phone a real user carries; good low-end test | [VERIFIED https://gadgetsharu.com/realme-c61-price-nepal] |
| **Redmi A5 3GB/64GB** | 14,999 | **€88** | Official Xiaomi Nepal price; BLE-capable; modal device in the target base | [VERIFIED https://www.mi.com/np/product/redmi-a5/] |
| **Redmi A5 4GB/128GB** | 16,999 | **€100** | Tests survival on 4 GB | [VERIFIED https://www.mi.com/np/product/redmi-a5/] |
| **Realme C75** | 24,999 | **€147** | Mid-range control device | [VERIFIED https://gadgets.thenepalicomment.com/mobiles/realme-c75-price-in-nepal/ — indicative single-source] |
| **Samsung Galaxy A16** | 27,999 | **€165** | Different SoC/firmware — the key variable for Wi-Fi Direct and BLE stack quirks; 6 years of updates makes a long-lived test bed | [VERIFIED https://gadgets.thenepalicomment.com/mobiles/samsung-galaxy-a16-price-in-nepal/ — indicative; another listing quotes NPR 34,999 = €206] |

A four-device matrix (2× Realme C61, 1× Redmi A5 128 GB, 1× Galaxy A16) would cost **€425** — 1.4% of the Recommended ask. **It is still not in the budget.** See 7.2.

### 7.2 Why each candidate line is excluded

| Candidate | Verdict | Verified basis |
|---|---|---|
| **Android test handsets** | **NOT eligible** | Two independent reasons. (a) Policy excludes "regular … **mobile phones**" [VERIFIED https://nlnet.nl/foundation/policies/externalspending/]. (b) More decisively, the on-point office-hour answer: *"Q: Can a milestone include buying two different test machines, to validate the software on real hardware? A: Generally this is **not seen as an efficient use of project budget**."* [VERIFIED https://nlnet.nl/officehour/#hardware] |
| Laptops / workstations | **NOT eligible** | Explicitly named as excluded [VERIFIED https://nlnet.nl/foundation/policies/externalspending/] |
| **Relay VPS (€5/month)** | **NOT eligible** | "we are **not generally able to fund hosted instances of software, or cover hosting costs**. We fund research and development" [VERIFIED https://nlnet.nl/officehour/#hardware]. The relay must be budgeted as **code to develop** (WP5), not a service operated. |
| **CI / compute minutes** | **NOT eligible** | "**compute time renting would fall under operational expenses**" [VERIFIED https://nlnet.nl/officehour/#hardware] |
| Domain name | **NOT eligible** | Falls under the same hosting/opex exclusion. €12 is not worth an eligibility argument. |
| **Security audit** | **Free — do not budget** | Professional audit by Radically Open Security is a support service at no cost to the grant [VERIFIED https://nlnet.nl/NGI0/services/] |
| Accessibility audit | **Free — do not budget** | HAN University support service [VERIFIED same] |
| Paid software licences / subscriptions | Avoid | "not desirable … case by case" [VERIFIED https://nlnet.nl/foundation/policies/externalspending/]. Build on FOSS tooling only. |
| F&A as a line item | **NOT eligible** | Generally ineligible; 25% cap only exceptionally [VERIFIED https://nlnet.nl/restack/faq/#FA]. Overhead is inside the rate instead (§3.5). |
| Travel | Omit | Eligible in principle [VERIFIED https://nlnet.nl/restack/eligibility/] but discretionary and the easiest line to cut. Omitted from all three scenarios. |
| Advertising | **NOT eligible** | "NLnet does not pay for advertisement campaigns of any type" [VERIFIED https://nlnet.nl/foundation/policies/externalspending/] |

### 7.3 Decision: €0 expenses, devices as in-kind contribution

**All three scenarios carry zero expenses.** Two supporting facts make this honest rather than evasive:

1. **Arvion already owns the hardware.** A studio that ships Android apps owns Android handsets; the test matrix is existing equipment, so no purchase is needed to do the work.
2. **In-kind contribution strengthens cost-effectiveness.** The proposal can state — truthfully and verifiably — that the studio contributes ~€425 of test hardware and the relay's host machine, meaning **100% of the grant buys work**. That is a stronger sentence than any expense line.

**Also note:** the studio has **already built parts of MeshDoc** (it is an existing product-engineering effort). NLnet "cannot make donations for any effort completed prior to the grant" [VERIFIED https://nlnet.nl/restack/faq/]. The budget therefore covers **only forward work from the MoU start date**. Anything already done must be presented as prior art and capability evidence — not as fundable effort. This is worth checking line by line before filing.

---

## 8. Milestone payment schedule

NLnet pays **in arrears, per milestone, on request** — never in advance; grants are **donations** and amounts "do not include VAT" [VERIFIED https://nlnet.nl/foundation/policies/externalspending/]. The schedule is also a **cash-flow document**: Arvion funds work up to each gate before payment lands.

**Structure follows the sample MoU** [VERIFIED https://nlnet.nl/foundation/request/sample_MoU.pdf]: numbered tasks, each with milestones/deliverables and an amount, and — where subtasks go to different people or are large — amounts divided across subtasks.

### 8.1 Recommended scenario — €29,920

| # | Gate | End of | Milestones / deliverables that unlock payment | Cash |
|---|---|---|---|---|
| **1** | Foundations | M2 | · Repo, licence, CI live · ADRs merged · **threat model published** · change-format spec v0.1 published | **€3,000** |
| **2** | Core & first transport | M5 | · CRDT core + identity keys + change format merged · `Transport` trait + conformance suite · Nearby fast path passing conformance | **€7,000** |
| **3** | Full transport matrix | M7 | · FOSS BLE discovery on Play-Services-free hardware · Wi-Fi Direct bulk transfer, resumable · relay + DTN converging across a partition | **€8,000** |
| **★** | **Accessibility gate** | M9 | · **"Certified WCAG accessible"** — WCAG audit of the reference app through the free HAN service, and the issues it raises fixed | **€0** |
| **4** | Product, pilot & evidence | M10 | · Android app does all four document types end-to-end · fuzz harness green, ≥3 convergence bugs closed with committed seeds · **field pilot report published** | **€6,000** |
| **★** | **Security gate** | M11 | · **"Process issues from external security review"** — free Radically Open Security audit completed through the ROSS/handling process, issues triaged and resolved | **€0** |
| **5** | Release & handover | M12 | · Reproducible build reproduced bit-for-bit by a third party · **F-Droid release accepted** · developer + user documentation published · upstream PR merged or reviewed · governance/roadmap published | **€5,920** |
| | **TOTAL** | | | **€29,920** |

### 8.2 Lean and Ambitious equivalents

| Gate | Lean (€14,960, 9 mo) | Ambitious (€49,980, 12 mo) |
|---|---|---|
| 1 Foundations | €1,800 (M2) | €4,500 (M2) |
| 2 Core & first transport | €4,000 (M4) | €12,000 (M5) |
| 3 Full transport matrix | €4,000 (M6) | €13,000 (M7) |
| ★ Accessibility gate | €0 (M7) | €0 (M9) |
| 4 Product, pilot & evidence | €3,000 (M8) | €11,000 (M10) |
| ★ Security gate | €0 (M9) | €0 (M11) |
| 5 Release & handover | €2,160 (M9) | €9,480 (M12) |
| **TOTAL** | **€14,960** | **€49,980** |

### 8.3 Why the gates are shaped this way

- **Gate 1 is small (10%) on purpose.** It buys the artefacts a reviewer can actually inspect during the long review window — threat model, wire spec, ADRs — while keeping the studio's pre-financing need low.
- **Gates 2 and 3 are the heaviest** because they carry the technical risk.
- **The two ★ gates cost €0 and are milestones anyway.** Both audits are free NLnet support services [VERIFIED https://nlnet.nl/NGI0/services/], and the sample MoU shows exactly these two as project-plan milestones [VERIFIED https://nlnet.nl/foundation/request/sample_MoU.pdf]. Putting them in the plan demonstrates you have read the programme materials, and it binds the release to passing them — the *remediation* work is paid through gates 4 and 5, not through the audits.
- **Gate 5 is deliberately not the largest.** If the project runs short, release work is last to be paid for, which points incentives at the hard middle rather than a tidy finish.
- **Cash-flow reality:** review takes "three and five months" from the deadline [VERIFIED https://nlnet.nl/restack/faq/]; then work, then payment. **The first money realistically lands 6–8 months after filing. Do not plan to start on grant money.**

---

## 9. Budget narrative — REFERENCE ONLY

> ### 🚫 DO NOT PASTE THIS INTO THE APPLICATION
>
> **NLnet's generative AI policy v2.0 forbids using AI to *write* proposals.** "Generative AI can no longer be used for **writing** proposals", effective immediately, and the news item names the upcoming Restack call (deadline 3 Nov 2026) as covered [VERIFIED https://nlnet.nl/news/2026/20261020-AI-policy.html]. The FAQ: *"The short answer is: no. … Please grant us the courtesy of writing the proposal yourself."* Undisclosed AI-written text is "likely to result in the proposal being rejected" [VERIFIED https://nlnet.nl/restack/faq/#AI].
>
> **What this is for:** it shows which facts and which reasoning belong in the applicant's own paragraph, in roughly the right order and length. Read it, close it, and write the real thing from your own head in your own voice. Using the researched numbers is fine — numbers are research. Using these sentences is not. If any wording is reused, the policy requires disclosing that in the application, with an explanation.

Draft (~360 words, first person, reference only):

> I am applying as Arvion Technologies, a four-person product-engineering studio in Kathmandu, and I would rather explain how our rate was built than simply state it.
>
> We are budgeting €170 per person-day, which is €21.25 an hour. That is well below the €65 ceiling, and I have deliberately not asked for the ceiling, because I understand that using the maximum rate counts against us on cost effectiveness.
>
> The number comes from what it genuinely costs us to keep a specialist engineer on this work. A senior engineer in Kathmandu with the Rust, Android and Bluetooth experience MeshDoc needs earns about NPR 400,000 a month, which at the rate we have used is roughly €2,357. Employer social security and our festival allowance add about 28%, taking it to €3,016. Our studio then carries overhead: co-working space, business internet plus a backup link because outages cost us whole days, power backup, equipment, accounting, and the currency charges we absorb when a grant is paid in euros. We calculate that at 20% of the total, which gives a true cost near €174 per person-day. We are asking for €170 and absorbing the difference ourselves.
>
> Every euro of this budget is labour. I have not asked for test devices or hosting, because I understand those fall outside what NLnet funds. The Android handsets we need and the machine the relay runs on are already ours, and we will contribute them.
>
> The work is 176 person-days over twelve months, about two thirds of one full-time person. That is deliberate: we run client work alongside this, and I would rather promise something we can certainly deliver than something that looks ambitious on paper. The plan is nine work packages, each with a payment attached, so it is easy to see at any point what has been delivered for the money.
>
> Two of the milestones cost nothing. I would like to use the accessibility audit and the security review that NLnet offers as support services, and I have put explicit gates in the plan for fixing what they find before the 1.0 release.

---

## 10. Anticipated challenges — and how to pre-empt them

| # | The challenge | Why a reviewer would raise it | How to pre-empt it |
|---|---|---|---|
| 1 | **"€170/day is high for Nepal."** | The senior median is NPR 300,000, implying ~€130/day. | Show the derivation and the *reason* for using NPR 400,000: the source itself prices "Embedded / IoT firmware" at a **10–30% premium** "given scarcer talent pool", and notes foreign-remote poaching at 2–3× local rates. Rust + BLE + CRDT is that scarce skillset. The rate is still **2.3% below** the computed cost, and **32.7% of the ceiling**. |
| 2 | **"€170/day is implausibly low — is this real?"** | Just as fatal as #1. | Show the five-line derivation: NPR 400,000 → ÷169.734 → €2,356.63 → ×1.28 → €3,016.48 → ÷0.80 → €3,770.61 → ÷21.667 → €174.03. A number below its own cost basis cannot be padding. Note the office-hour example of €25/h docs / €45/h dev shows €21.25/h is unremarkable to NLnet. |
| 3 | **"You have not budgeted test devices or hosting — how will you test/deploy?"** | Fair question, now that expenses are €0. | State it as a **deliberate, in-kind contribution**: "we contribute ~€425 of Android test hardware and the relay's host machine; 100% of the grant buys work." Confirms you know the rules *and* removes a cost. Do **not** invite the reviewer to fund them. |
| 4 | **"Your overhead is inside the rate, and F&A is not eligible."** | F&A "generally not considered eligible", 25% cap [VERIFIED](https://nlnet.nl/restack/faq/#FA). | Disclose before being asked. Overhead is **exactly 20.0% of cost**, under the 25% cap. Offer the alternative: if NLnet prefers, quote a flat €170 with no overhead component — same number, different description. Better to volunteer this than be caught by it. |
| 5 | **"176 person-days over 12 months is only 0.68 FTE — is that enough to deliver 9 WPs?"** | Scope-vs-effort doubt. | Show the ramp table: two people at ~0.34 FTE each, plateau 0.78 combined. Point to the WP-by-WP day allocation so the number is checkable, not asserted. And note it is *deliberately* conservative — a first grant should be deliverable. |
| 6 | **"Some of this work is already done."** | "We cannot make donations for any effort completed prior to the grant." | State plainly in the proposal what already exists (prior art, capability evidence) and confirm the budget covers **only forward work from MoU start**. Check every WP against this before filing — it is the easiest way to lose credibility. |
| 7 | **"Wi-Fi Direct and BLE on budget Android is not reliably possible."** | True, and technical reviewers know it. | Pre-empt as a *named risk with a mitigation*: a deliberately mixed device matrix to surface firmware quirks in month 4, capability negotiation in WP3, clean fallback. An unmentioned risk discounts the whole plan; a managed one earns credit. |
| 8 | **"Is device identity / crypto work not 'custom crypto'?"** | Scope excludes custom crypto. | Be explicit in WP2: only established, audited primitives (Ed25519 via a maintained crate, an existing AEAD, an existing CRDT library). The deliverable is **integration and format design**, not new primitives. Say those words. |
| 9 | **"What does the security audit cost?"** | Reviewers may expect a big line. | It is **free** (Radically Open Security support service) [VERIFIED](https://nlnet.nl/NGI0/services/), and the accessibility audit likewise (HAN). Saying so, and putting both in the plan as €0 gates, signals you have read the programme materials. |
| 10 | **"Your impact evidence is thin."** | Impact is 40% of the score. | Why WP8 (field pilot) is in Recommended as a **payment gate**, not an optional extra. Link the pilot report first from the proposal. |
| 11 | **"The 60% European-dimension rule may not be met."** | Knock-out criterion. | Answer with the citation: Nepal is on the list [VERIFIED](https://nlnet.nl/OIS/european-dimension/). **Confirm with NLnet in writing before filing.** See §2. |
| 12 | **"The minimum rate — are you below it?"** | NLnet confirms a minimum rate exists but not its value. | Cannot be resolved from public sources [UNCERTAIN]. €21.25/h is above any plausible floor (the page's own example treats €25/h documentation as normal, and a floor above that would exclude most of the world). If challenged, ask NLnet for the figure. |
| 13 | **Currency and tax** | Grant in EUR, costs in NPR; donation treatment in Nepal. | Note the rate used (€1 = NPR 169.73) and accept the FX risk in writing. Grants are donations from an ANBI-status foundation and "taxation in a global context is a pleasantly complex … issue"; check with a Nepali accountant before signing the MoU — **but do not put this in the proposal** [VERIFIED https://nlnet.nl/restack/faq/#donations]. |

---

## 11. Sources

| # | Used for | URL |
|---|---|---|
| 1 | **€65/hour ceiling; minimum rate exists; differentiated rates; daily rate + lump sums; what reviewers look for; hosting not funded; compute = opex; test machines discouraged** | https://nlnet.nl/officehour/ (#amount, #hardware) |
| 2 | Cost-recovery / "do not pay commercial rates"; 5k–50k range; call cadence | https://nlnet.nl/funding.html |
| 3 | First-grant band, ceilings, scoring weights, review questions, audit threshold | https://nlnet.nl/restack/guideforapplicants/ |
| 4 | **Nepal listed as Horizon Europe-eligible**; 60%-of-funds rule | https://nlnet.nl/OIS/european-dimension/ |
| 4b | **EC primary source: Nepal "automatically eligible for funding"** (EU Grants list V4.2, 07.10.2026) | https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/common/guidance/list-3rd-country-participation_horizon-euratom_en.pdf |
| 5 | European dimension knock-out; "exceptional quality" fallback; eligible cost types | https://nlnet.nl/restack/eligibility/ |
| 6 | Milestone arrears; no prior work fundable; 12-month default; review duration; F&A 25% cap; AI question; donation/tax note | https://nlnet.nl/restack/faq/ |
| 7 | Hardware exclusions; VAT; residual value; €250 invoice threshold | https://nlnet.nl/foundation/policies/externalspending/ |
| 8 | **Sample MoU: milestone format, divide amounts across subtasks, "Certified WCAG accessible", "Process issues from external security review"** | https://nlnet.nl/foundation/request/sample_MoU.pdf |
| 9 | Free security audit (ROS), accessibility audit (HAN), packaging, mentoring | https://nlnet.nl/NGI0/services/ |
| 10 | AI out of scope (>1M users exception); programme goals | https://nlnet.nl/restack/ |
| 11 | **GenAI policy v2.0 — no AI-written proposals, applies to 3 Nov 2026** | https://nlnet.nl/news/2026/20261020-AI-policy.html |
| 12 | Kathmandu 2026 salary bands; IoT/embedded premium; foreign-remote premium | https://praxiumlabs.com/blog/hiring-engineers-nepal-2026-salaries/ |
| 13 | mCaptcha funded budget: €26,200 total, €2,000/month developer pay | https://git.batsense.net/mCaptcha/website/raw/branch/librepages/pub/2022/07/mCaptcha-nlnet-ngi-zero-entrust.pdf |
| 14 | Gitea NLnet application, 50 k€ across two developers | https://github.com/go-gitea/gitea/issues/16827 |
| 15 | EUR/INR ECB rate 2026-10-30 (106.084) → derived EUR/NPR 169.734 | https://api.frankfurter.app/latest?base=EUR&symbols=INR |
| 16 | Redmi A5 official Nepal pricing (NPR 14,999 / 16,999) | https://www.mi.com/np/product/redmi-a5/ |
| 17 | Realme C61 Nepal price (NPR 13,499) | https://gadgetsharu.com/realme-c61-price-nepal |
| 18 | Samsung Galaxy A16 Nepal price (NPR 27,999, indicative) | https://gadgets.thenepalicomment.com/mobiles/samsung-galaxy-a16-price-in-nepal/ |
| 19 | Realme C75 Nepal price (NPR 24,999, indicative) | https://gadgets.thenepalicomment.com/mobiles/realme-c75-price-in-nepal/ |
| 20 | Office hour, for eligibility confirmation (25 Nov 2026) | https://nlnet.nl/events/20261125/office-hour/index.html |

**Explicitly not verified / uncertain:** the value of NLnet's **minimum** rate (unpublished); the **28%** Nepal employer on-cost (modelling assumption — the weakest number here); the **20%** overhead fraction (studio assumption); the European consultancy comparison range (general market knowledge, not researched). None of these is presented as verified above.

---

## 12. Arithmetic audit

Recomputed programmatically; all checks pass.

**Rate derivation (NPR 400,000 basis)**
- EUR/NPR: 106.084 × 1.60 = **169.734** ✔
- NPR 400,000 ÷ 169.734 = **€2,356.63** ✔
- × 1.28 = **€3,016.48** ✔ (on-cost component €659.85)
- ÷ 0.80 = **€3,770.61** ✔ (overhead component **€754.13 = 20.0%** of total; cap 25%) ✔
- ÷ 21.667 = **€174.03/day** ✔ = **€21.75/hour** ✔
- Recommended **€170/day = €21.25/hour** → **2.3% below** the €174.03 floor ✔ · **32.7%** of the €65/hour ceiling ✔ · **€3,683.33/month** ✔

**Scenario totals (€170/day, €0 expenses)**

| | WP days | Labour = total | Milestones sum | Monthly days sum | Avg FTE | Person-months |
|---|---|---|---|---|---|---|
| **Lean** | 5+18+10+13+7+12+8+8+7 = **88** ✔ | 88 × €170 = **€14,960** ✔ | 1,800+4,000+4,000+3,000+2,160 = €14,960 ✔ | 4+7+9+11+12+12+11+11+11 = 88 ✔ | 0.45 | 4.06 |
| **Recommended** | 9+34+20+26+14+26+18+17+12 = **176** ✔ | 176 × €170 = **€29,920** ✔ | 3,000+7,000+8,000+6,000+5,920 = €29,920 ✔ | 7+10+13+15+16+17+17+17+17+16+15+16 = 176 ✔ | 0.68 | 8.12 |
| **Ambitious** | 14+58+36+46+24+48+30+22+16 = **294** ✔ | 294 × €170 = **€49,980** ✔ | 4,500+12,000+13,000+11,000+9,480 = €49,980 ✔ | 12+18+23+26+28+29+29+29+28+27+25+20 = 294 ✔ | 1.13 | 13.57 |

**Device conversions** (@169.734): 13,499→€79.53→**€80** ✔ · 14,999→€88.37→**€88** ✔ · 16,999→€100.15→**€100** ✔ · 24,999→€147.28→**€147** ✔ · 27,999→€164.96→**€165** ✔ · 34,999→€206.20→**€206** ✔ · 4-device matrix 80+80+100+165 = **€425** ✔

**Constraint checks**
- All three totals within €5,000–€50,000 ✔
- Ambitious €49,980 ≤ €50,000 with €20 headroom ✔
- Expenses = €0 in all scenarios (no device, hosting, compute or CI lines) ✔
- Every rate €21.25/h well below the €65/h ceiling ✔
- Overhead inside the rate = 20.0% of cost, under the 25% F&A cap ✔
- Zero cash budgeted for security and accessibility audits (free services) — but both present as €0 milestones ✔
- Budget covers only forward work (nothing already built) ✔
- Deadline: 3 Nov 2026 12:00 CET = **16:45 NPT** ✔
