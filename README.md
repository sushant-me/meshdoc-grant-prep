# MeshDoc → NLnet Restack — grant preparation pack

**Deadline: 3 November 2026, 12:00 CET = 11:00 UTC = 16:45 Nepal time.** Roughly 24 hours from when this pack was prepared.

This pack exists to make your Restack application complete, accurate and credible. It contains research, rules, evidence, arithmetic and checklists. **It does not contain proposal prose**, and that is deliberate — see `COMPLIANCE_AND_STRATEGY.md` §2.

---

## Read in this order

| # | File | Why | Time |
|---|---|---|---|
| 1 | **`COMPLIANCE_AND_STRATEGY.md`** | The three gates that decide whether you are reviewed at all; 13 fixes to your spec; the 24-hour plan in Nepal time | 20 min |
| 2 | **`submission/FIELD_PACK.md`** | Field-by-field: what each answer must accomplish, and the traps | 15 min |
| 3 | `research/FUND_RULES.md` | Verified fund rules with exact quotes. Read §6 (scoring) at minimum | 20 min |
| 4 | `research/TECHNICAL_CASE.md` | Architecture, design decisions, the 12 hard problems, 20 acceptance criteria | 40 min |
| 5 | `research/BUDGET_AND_MILESTONES.md` | Rate derivation, 3 scenarios, 9 work packages, milestone payments | 25 min |
| 6 | `research/LANDSCAPE.md` | Prior art with verified licences; the six differentiators; upstream plan | 25 min |
| 7 | `submission/CLAIM_LEDGER.md` | Every claim, its source, and whether you may make it | 10 min |
| 8 | `submission/PRE_SUBMIT_CHECKLIST.md` | The 15-minute final gate | 15 min |

---

## The five things that matter most

1. **Nepal is eligible.** Nepal is on NLnet's Horizon Europe list *and* the EC list that NLnet defers to says Nepal is "automatically eligible for funding". No European co-applicant is needed. Do not apologise for being in Kathmandu.
2. **Remove the translation feature.** Restack excludes AI-related projects, and the exclusion names *integration* of AI as out of scope. This is the single biggest fix.
3. **You must write the answer text yourself.** NLnet's GenAI policy v2.0 forbids AI-written proposals, explicitly including "restructuring, shortening and translation" and "generation of ideas". This is why the pack stops at research and checklists.
4. **€0 expenses, one modest rate.** Phones, laptops, hosting and compute are all ineligible. Everything is labour. A defensible rate sits far below the €65/h ceiling.
5. **Fix the three self-inflicted technical errors** before they reach a reviewer: the workspace-id/key-rotation bug, the membership model contradiction, and the 15 mW vs 2 %/day arithmetic.

---

## Directory map

```
grant/
├── COMPLIANCE_AND_STRATEGY.md      ← start here
├── research/
│   ├── FUND_RULES.md               verified rules, eligibility, scoring, GenAI policy
│   ├── TECHNICAL_CASE.md           architecture, ADRs, hard problems, acceptance criteria
│   ├── BUDGET_AND_MILESTONES.md    rate derivation, scenarios, WPs, tranches
│   └── LANDSCAPE.md                prior art, licences, differentiators, upstream plan
├── submission/
│   ├── FIELD_PACK.md               per-field requirements and traps
│   ├── CLAIM_LEDGER.md             every claim + source + status (SAFE/VERIFY/AVOID)
│   └── PRE_SUBMIT_CHECKLIST.md     15-minute final gate
└── repo-template/                  drop-in files for the public MeshDoc repository
    ├── LICENSE-Apache-2.0          pick one, delete the rest
    ├── LICENSE-AGPL-3.0
    ├── LICENSE-EUPL-1.2
    ├── .gitignore
    └── README.md                   outline to fill in your own words
```

---

## What to do right now

1. Email three potential pilot organisations asking for a one-paragraph letter of support. This is the highest-value hour available to you.
2. Skim `COMPLIANCE_AND_STRATEGY.md` §0 and §4.
3. Open a plain text editor and start on the 1,000-character summary.

---

## A note on honesty

Every factual claim in `research/` is tagged `[VERIFIED <url>]` or `[UNCERTAIN]`. Where a number is an estimate, it says so. Where a design decision in your original spec is wrong, the pack says which and why. That is on purpose: the Restack Guide says reviewers verify facts and claims independently, and the strongest position you can be in is one where every sentence survives that check.

The three things the pack cannot give you are the three that will decide the application: a named pilot partner, a repository you wrote yourself, and your own voice explaining why you are the person to build this.
