#!/usr/bin/env python3
"""
check_draft.py — pre-submission validator for the NLnet Restack application.

Runs the PRE_SUBMIT_CHECKLIST.md rules mechanically against a draft, so the
things that are easy to miss at 2am are caught by a script instead of a reviewer.

It does NOT write or rewrite anything. It only inspects text you wrote.

USAGE
    python3 check_draft.py draft.md
    python3 check_draft.py draft.md --rate 170
    python3 check_draft.py draft.md --json

DRAFT FORMAT
    One UTF-8 text file with a heading per form field. Headings are matched
    case-insensitively on any of the aliases below, e.g.:

        ## summary
        <your 1000-character summary>

        ## effort
        <budget breakdown>

    Recognised fields and their character limits (from nlnet.nl/propose/):
        title            (warn over 120)
        summary          1000
        effort           4000
        comparison       4000
        challenges       4000
        ecosystem        2000
        background       2000
        other_funding    1000
        ai_disclosure    8000

    Anything under an unrecognised heading is ignored.

EXIT CODE
    0 = no FAILs (warnings may exist)
    1 = at least one FAIL
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from typing import Iterable

# --------------------------------------------------------------------------
# Field definitions
# --------------------------------------------------------------------------

FIELDS: dict[str, dict] = {
    "title":         {"limit": None, "warn_over": 120, "aliases": ["title", "proposal title"]},
    "summary":       {"limit": 1000, "aliases": ["summary", "project summary", "project overview"]},
    "effort":        {"limit": 4000, "aliases": ["effort", "proposed effort", "budget", "requested support"]},
    "comparison":    {"limit": 4000, "aliases": ["comparison", "compare", "comparison with other efforts"]},
    "challenges":    {"limit": 4000, "aliases": ["challenges", "technical challenges"]},
    "ecosystem":     {"limit": 2000, "aliases": ["ecosystem", "ecosystem and engagement"]},
    "background":    {"limit": 2000, "aliases": ["background", "why you", "about us"]},
    "other_funding": {"limit": 1000, "aliases": ["other funding", "funding"]},
    "ai_disclosure": {"limit": 8000, "aliases": ["ai disclosure", "ai", "generative ai"]},
}

ALIAS_LOOKUP = {a: key for key, spec in FIELDS.items() for a in spec["aliases"]}

REQUIRED_FIELDS = ["summary", "effort", "comparison", "challenges", "ecosystem", "background"]

# --------------------------------------------------------------------------
# Rules
# --------------------------------------------------------------------------

# Restack excludes AI projects. Any of these in the proposal text risks
# reclassifying the project as an AI project and getting it marked ineligible.
AI_SCOPE_TERMS = [
    r"\btranslat(?:e|ed|es|ing|ion|ions)\b",
    r"\blanguage[\s-]?pack(?:s)?\b",
    r"\bon[\s-]device\s+(?:model|translation|inference|AI)\b",
    r"\bmachine\s+translation\b",
    r"\bneural\b",
    r"\bLLMs?\b",
    r"\bGPT\b",
    r"\bAI\b",
    r"\bA\.I\.\b",
    r"\bartificial\s+intelligence\b",
    r"\bmachine\s+learning\b",
    r"\bML\s+model\b",
    r"\bdeep\s+learning\b",
    r"\bquantized\s+model\b",
    r"\b(?:speech|vision|image)\s+recognition\b",
]

# Overclaims / factual traps flagged in submission/CLAIM_LEDGER.md.
CLAIM_TRAPS = [
    (r"sybil[\s-]?proof", "Ledger AVOID: signing gives attribution, not Sybil resistance."),
    (r"guaranteed\s+by\s+the\s+CRDT", "Ledger AVOID: say 'convergent by construction for the supported types'."),
    (r"hash\s*\(\s*workspace[_\s]?key", "Ledger AVOID: workspace id must NOT derive from the key (breaks rotation)."),
    (r"workspace[_ ]?id\s*[:=]\s*hash", "Ledger AVOID: workspace id must NOT derive from the key."),
    (r"<\s*2\s*%\s*(?:/|per\s*)day", "Ledger AVOID at 15 mW: 15 mW is ~2.34%/day. Claim <=15 mW OR <=2%, not both."),
    (r"the\s+first\s+(?:ever|attempt|project|tool)", "Overclaim: reviewers verify. Use 'in our survey we found no...'."),
    (r"first[\s-]ever", "Overclaim: remove."),
    (r"\bnone\s+exists\b", "Negative claim: say 'in our survey we found no...'."),
    (r"no\s+(?:other\s+)?project\s+(?:does|has|offers)", "Negative claim: soften and state the survey scope."),
    (r"keys?\s+(?:are\s+)?stored\s+in\s+the\s+(?:Android\s+)?[Kk]eystore", "Likely false: Keystore does not expose Ed25519/X25519 ops. Say 'encrypted under a hardware-backed wrapping key'."),
    (r"revolutionary", "Filler: reviewers discount it."),
    (r"game[\s-]chang\w+", "Filler: reviewers discount it."),
    (r"cutting[\s-]edge", "Filler: reviewers discount it."),
    (r"seamless\w*", "Filler."),
    (r"leverage\w*", "Filler."),
    (r"robust\s+solution", "Filler."),
    (r"state[\s-]of[\s-]the[\s-]art", "Filler unless citing a specific comparison."),
]

# A working prototype claim must be true.
PROTOTYPE_TRAPS = [
    r"\balready\s+(?:built|works|working|deployed|runs)\b",
    r"\bworking\s+prototype\b",
    r"\bwe\s+have\s+(?:built|implemented|shipped)\b",
    r"\bproduction[\s-]ready\b",
]

PLACEHOLDERS = [
    r"\bTODO\b", r"\bTBD\b", r"\bXXX\b", r"\bFIXME\b",
    r"\[insert", r"\[your", r"<[a-z_]+>", r"lorem\s+ipsum",
]

HOSTING_TRAP = r"\b(?:VPS|hosting\s+costs?|cloud\s+costs?|server\s+costs?)\b"
DEVICE_TRAP = r"\b(?:buy|purchase|test\s+devices?|test\s+machines?)\b"

EURO_RE = re.compile(r"€\s?([0-9][0-9.,]*)")
DAYS_RATE_RE = re.compile(
    r"(\d{1,4})\s*(?:person[\s-]?)?days?\s*(?:at|@|×|x)?\s*€\s?([0-9][0-9.,]*)",
    re.IGNORECASE,
)


# --------------------------------------------------------------------------
# Result model
# --------------------------------------------------------------------------

@dataclass
class Finding:
    level: str          # FAIL | WARN | INFO
    field: str
    code: str
    message: str
    excerpt: str = ""


@dataclass
class Report:
    findings: list[Finding] = field(default_factory=list)
    field_stats: dict[str, dict] = field(default_factory=dict)

    def add(self, level: str, fld: str, code: str, message: str, excerpt: str = "") -> None:
        self.findings.append(Finding(level, fld, code, message, excerpt))

    def count(self, level: str) -> int:
        return sum(1 for f in self.findings if f.level == level)


# --------------------------------------------------------------------------
# Parsing
# --------------------------------------------------------------------------

def split_sections(text: str) -> dict[str, str]:
    """Split a markdown draft into {field: body} on recognised headings."""
    heading_re = re.compile(r"^\s{0,3}#{1,6}\s*(.+?)\s*$", re.MULTILINE)
    marks = [(m.start(), m.end(), m.group(1).strip()) for m in heading_re.finditer(text)]

    sections: dict[str, list[str]] = {}
    for i, (start, end, raw_title) in enumerate(marks):
        # strip leading numbering: "3. Comparison" / "Field 6 - comparison"
        clean = re.sub(r"^[\d.)\-\s]*", "", raw_title).strip().lower()
        clean = re.sub(r"^(?:field|part)\s*\d+\s*[-–:.]?\s*", "", clean).strip()
        key = ALIAS_LOOKUP.get(clean)
        if key is None:
            # try a looser contains match, longest alias first
            for alias in sorted(ALIAS_LOOKUP, key=len, reverse=True):
                if alias in clean or clean in alias:
                    key = ALIAS_LOOKUP[alias]
                    break
        if key is None:
            continue
        body_end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        sections.setdefault(key, []).append(text[end:body_end].strip())

    return {k: "\n\n".join(v).strip() for k, v in sections.items()}


def strip_markdown(text: str) -> str:
    """Approximate the plain text NLnet will receive in a textarea."""
    t = re.sub(r"`{1,3}[^`]*`{1,3}", " ", text)          # code spans/blocks
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)          # images
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)       # links -> label
    t = re.sub(r"^\s{0,3}#{1,6}\s*", "", t, flags=re.M)  # headings
    t = re.sub(r"^\s{0,3}>\s?", "", t, flags=re.M)       # quotes
    t = re.sub(r"[*_]{1,3}([^*_]+)[*_]{1,3}", r"\1", t)  # emphasis
    t = re.sub(r"^\s*[-*+]\s+", "", t, flags=re.M)       # bullets
    t = re.sub(r"^\s*\d+[.)]\s+", "", t, flags=re.M)     # ordered
    t = re.sub(r"\n{2,}", "\n", t)
    return t.strip()


def count_chars(text: str) -> int:
    """Count characters the way a form textarea does (code points)."""
    return len(unicodedata.normalize("NFC", text))


def sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text).strip())
    return [p for p in parts if p]


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------

def check_presence(sections: dict[str, str], rep: Report) -> None:
    for fld in REQUIRED_FIELDS:
        if not sections.get(fld, "").strip():
            rep.add("FAIL", fld, "MISSING", f"Field '{fld}' is missing or empty.")


def check_lengths(sections: dict[str, str], rep: Report) -> None:
    for fld, body in sections.items():
        spec = FIELDS.get(fld)
        if not spec or not body.strip():
            continue
        n = count_chars(body)
        limit = spec.get("limit")
        warn_over = spec.get("warn_over")
        rep.field_stats[fld] = {"chars": n, "limit": limit}

        if limit and n > limit:
            rep.add("FAIL", fld, "TOO_LONG",
                    f"{n} characters, limit is {limit} — over by {n - limit}.")
        elif limit and n > limit * 0.98:
            rep.add("WARN", fld, "NEAR_LIMIT",
                    f"{n}/{limit} characters — trim before pasting to be safe.")
        elif limit and n < limit * 0.35 and fld != "ai_disclosure":
            rep.add("INFO", fld, "SHORT",
                    f"only {n}/{limit} characters — fine if complete, but check nothing is missing.")

        if warn_over and n > warn_over:
            rep.add("WARN", fld, "LONG_TITLE", f"{n} characters; {warn_over} is a sensible maximum.")


def check_patterns(fld: str, body: str, patterns: Iterable[str], level: str,
                   code: str, note: str | None, rep: Report) -> None:
    plain = strip_markdown(body)
    for pat in patterns:
        for m in re.finditer(pat, plain, re.IGNORECASE | re.UNICODE):
            s = max(0, m.start() - 40)
            e = min(len(plain), m.end() + 40)
            excerpt = plain[s:e].replace("\n", " ")
            msg = note if note else f"Matched '{m.group(0)}'."
            rep.add(level, fld, code, f"{msg} …{excerpt}…", excerpt)


def check_ai_scope(sections: dict[str, str], rep: Report) -> None:
    for fld, body in sections.items():
        for pat in AI_SCOPE_TERMS:
            for m in re.finditer(pat, strip_markdown(body), re.IGNORECASE):
                s = max(0, m.start() - 45)
                e = min(len(body), m.end() + 45)
                rep.add("FAIL", fld, "AI_SCOPE",
                        f"'{m.group(0)}' — Restack excludes AI-related projects. "
                        "Remove it or the proposal may be marked out of scope.",
                        strip_markdown(body)[s:e].replace("\n", " "))


def check_claim_traps(sections: dict[str, str], rep: Report) -> None:
    for fld, body in sections.items():
        if fld == "ai_disclosure":
            continue
        for pat, note in CLAIM_TRAPS:
            for m in re.finditer(pat, strip_markdown(body), re.IGNORECASE):
                rep.add("WARN", fld, "CLAIM_TRAP",
                        f"'{m.group(0)}' — {note}",
                        strip_markdown(body)[max(0, m.start() - 35):m.end() + 35].replace("\n", " "))


def check_prototype_claims(sections: dict[str, str], rep: Report) -> None:
    for fld, body in sections.items():
        if fld == "ai_disclosure":
            continue
        for pat in PROTOTYPE_TRAPS:
            for m in re.finditer(pat, strip_markdown(body), re.IGNORECASE):
                rep.add("WARN", fld, "PROTOTYPE",
                        f"'{m.group(0)}' — only claim this if it is true; reviewers check.",
                        strip_markdown(body)[max(0, m.start() - 35):m.end() + 35].replace("\n", " "))


def check_placeholders(sections: dict[str, str], rep: Report) -> None:
    for fld, body in sections.items():
        for pat in PLACEHOLDERS:
            for m in re.finditer(pat, body, re.IGNORECASE):
                rep.add("FAIL", fld, "PLACEHOLDER",
                        f"Leftover placeholder '{m.group(0)}'.")


def check_expenses(sections: dict[str, str], rep: Report) -> None:
    body = sections.get("effort", "")
    if not body:
        return
    plain = strip_markdown(body)
    for pat, why in [
        (HOSTING_TRAP, "Hosting and compute are ineligible costs."),
        (DEVICE_TRAP, "Test devices and machines are ineligible costs."),
    ]:
        for m in re.finditer(pat, plain, re.IGNORECASE):
            ctx = plain[max(0, m.start() - 60):m.end() + 60].replace("\n", " ")
            negated = re.search(r"\b(?:no|not|without|zero|€\s?0|ineligible|excluded)\b", ctx, re.IGNORECASE)
            if not negated:
                rep.add("WARN", "effort", "INELIGIBLE_COST",
                        f"'{m.group(0)}' appears as a cost. {why} …{ctx}…")


def check_budget_math(sections: dict[str, str], rate: float, rep: Report) -> None:
    body = sections.get("effort", "")
    if not body:
        return
    plain = strip_markdown(body)

    budget_items = []
    for m in DAYS_RATE_RE.finditer(plain):
        days = int(m.group(1))
        unit = float(re.sub(r"[.,]", "", m.group(2)))
        expected = days * unit
        budget_items.append((days, unit, expected))

        # find the most likely stated amount on the same line
        line_start = plain.rfind("\n", 0, m.start()) + 1
        line_end = plain.find("\n", m.end())
        line = plain[line_start: line_end if line_end != -1 else len(plain)]
        amounts = [float(re.sub(r"[.,]", "", a)) for a in EURO_RE.findall(line)]
        amounts = [a for a in amounts if a > unit]  # drop the rate itself
        if amounts and abs(amounts[-1] - expected) > 1:
            rep.add("WARN", "effort", "BUDGET_MATH",
                    f"{days} days x €{unit:,.0f} = €{expected:,.0f}, but the line states "
                    f"€{amounts[-1]:,.0f}. Check the arithmetic.")

    if budget_items:
        total = sum(i[2] for i in budget_items)
        amounts = sorted({float(re.sub(r"[.,]", "", a)) for a in EURO_RE.findall(plain)}, reverse=True)
        if amounts and not any(abs(a - total) <= 1 for a in amounts):
            rep.add("INFO", "effort", "BUDGET_TOTAL",
                    f"Line items sum to €{total:,.0f}; no stated figure matches exactly. "
                    "Verify the total by hand if this is a full breakdown.")

    # rate ceiling check
    for _, unit, _ in budget_items:
        if unit > 65:
            rep.add("FAIL", "effort", "RATE_CEILING",
                    f"Daily rate €{unit:,.0f} implies >€65/hour at 8h. NLnet caps at €65/hour.")
    if rate and budget_items:
        implied_hourly = rate / 8
        if implied_hourly > 65:
            rep.add("FAIL", "effort", "RATE_CEILING",
                    f"€{rate:,.0f}/day is €{implied_hourly:.2f}/hour, above the €65/hour ceiling.")


def check_filler(sections: dict[str, str], rep: Report) -> None:
    for fld, body in sections.items():
        if fld == "ai_disclosure":
            continue
        plain = strip_markdown(body)
        sents = sentences(plain)
        if not sents:
            continue
        long_sents = [s for s in sents if len(s.split()) > 40]
        if long_sents:
            rep.add("INFO", fld, "LONG_SENTENCE",
                    f"{len(long_sents)} sentence(s) over 40 words. Short and to the point reads better.")
        for phrase in ["in today's", "it is important to note", "needless to say",
                       "at the end of the day", "a wide range of"]:
            if phrase in plain.lower():
                rep.add("INFO", fld, "FILLER", f"Filler phrase: '{phrase}'.")


def check_consistency(sections: dict[str, str], rep: Report) -> None:
    """Same facts must appear the same way across fields."""
    joined = "\n".join(strip_markdown(b) for b in sections.values())

    licences = set(re.findall(r"\b(?:Apache-2\.0|AGPL-3\.0|GPL-3\.0|EUPL-1\.2|MIT|MPL-2\.0|LGPL-3\.0)\b", joined))
    if len(licences) > 1:
        rep.add("WARN", "cross", "LICENCE_MIXED",
                f"More than one licence named: {', '.join(sorted(licences))}. "
                "Name exactly one licence for your own project.")

    totals = {float(re.sub(r"[.,]", "", a)) for a in EURO_RE.findall(joined)}
    big = {t for t in totals if t >= 5000}
    if len(big) > 3:
        rep.add("WARN", "cross", "AMOUNT_SPRAWL",
                f"{len(big)} distinct amounts >= €5,000 appear. Make sure they are intentional "
                "(scenario totals are fine; contradictory ask figures are not).")


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

SYMBOL = {"FAIL": "FAIL", "WARN": "WARN", "INFO": "info"}


def render(rep: Report, rate: float) -> str:
    out: list[str] = []
    out.append("NLnet Restack draft check")
    out.append("=" * 60)
    out.append("")

    if rep.field_stats:
        out.append("Field lengths (character limits from the form)")
        for fld, st in rep.field_stats.items():
            limit = st["limit"]
            if limit:
                pct = st["chars"] / limit * 100
                bar = "#" * int(pct / 5)
                out.append(f"  {fld:<14} {st['chars']:>5}/{limit:<5} {pct:5.1f}%  {bar}")
            else:
                out.append(f"  {fld:<14} {st['chars']:>5} (no limit)")
        out.append("")

    order = {"FAIL": 0, "WARN": 1, "INFO": 2}
    findings = sorted(rep.findings, key=lambda f: (order[f.level], f.field, f.code))
    for level in ("FAIL", "WARN", "INFO"):
        group = [f for f in findings if f.level == level]
        if not group:
            continue
        out.append(f"{SYMBOL[level]} ({len(group)})")
        for f in group:
            out.append(f"  [{f.field}] {f.code}: {f.message}")
        out.append("")

    fails, warns = rep.count("FAIL"), rep.count("WARN")
    out.append("-" * 60)
    if fails:
        out.append(f"RESULT: {fails} blocking issue(s), {warns} warning(s). Fix the FAILs before submitting.")
    else:
        out.append(f"RESULT: no blocking issues, {warns} warning(s). Read the warnings and decide.")
    out.append("")
    out.append("This script cannot tell you whether the proposal is any good. It only")
    out.append("catches the mechanical mistakes. The judgement calls are yours.")
    return "\n".join(out)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Validate an NLnet Restack draft before submitting.")
    ap.add_argument("draft", help="path to the draft file (markdown or text)")
    ap.add_argument("--rate", type=float, default=0.0,
                    help="your daily rate in EUR, for the hourly-ceiling check (e.g. 170)")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = ap.parse_args(argv)

    try:
        with open(args.draft, encoding="utf-8") as fh:
            raw = fh.read()
    except OSError as exc:
        print(f"cannot read {args.draft}: {exc}", file=sys.stderr)
        return 2

    sections = split_sections(raw)
    rep = Report()

    if not sections:
        print("No recognised field headings found. Expected headings such as:\n"
              "  ## summary\n  ## effort\n  ## comparison\n  ## challenges\n"
              "  ## ecosystem\n  ## background", file=sys.stderr)
        return 2

    check_presence(sections, rep)
    check_lengths(sections, rep)
    check_ai_scope(sections, rep)
    check_claim_traps(sections, rep)
    check_prototype_claims(sections, rep)
    check_placeholders(sections, rep)
    check_expenses(sections, rep)
    check_budget_math(sections, args.rate, rep)
    check_filler(sections, rep)
    check_consistency(sections, rep)

    if args.json:
        print(json.dumps({
            "fields": rep.field_stats,
            "findings": [f.__dict__ for f in rep.findings],
            "fails": rep.count("FAIL"),
            "warns": rep.count("WARN"),
        }, indent=2))
    else:
        print(render(rep, args.rate))

    return 1 if rep.count("FAIL") else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
