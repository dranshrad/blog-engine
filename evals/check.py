#!/usr/bin/env python3
"""
Groundledger eval checker.

Scores a saved agent reply against a bait case. This is a pattern checker, not a
judge: it proves that required artifacts appear and that obviously-fabricated
shapes do not. It cannot tell you a claim ledger is honest — only that one
exists. Read the output too.

    python3 evals/check.py --lint                       # validate the fixtures
    python3 evals/check.py CASE.md REPLY.md             # score one reply
    python3 evals/check.py --batch replies/             # score a directory

Batch mode maps `reply-EV-003.md` (or any filename containing `EV-003`) to the
case whose id is EV-003.

Exit code 0 = all scored replies passed (or lint clean), 1 = at least one FAIL.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CASES = Path(__file__).resolve().parent / "cases"
SECTIONS = ("Prompt", "Must contain", "Must not contain", "Rationale")


def parse_case(path: Path) -> dict:
    """Split a case file into its sections. Bullet lines under the pattern
    sections are regexes; everything else is prose."""
    text = path.read_text()
    case: dict = {"path": path, "id": path.name.split("-")[0] + "-" + path.name.split("-")[1]}

    m = re.search(r"^skill:\s*(\S+)", text, re.M)
    case["skill"] = m.group(1) if m else None

    blocks: dict[str, list[str]] = {}
    current = None
    for line in text.splitlines():
        h = re.match(r"^##\s+(.*)$", line)
        if h:
            current = h.group(1).strip()
            blocks[current] = []
        elif current:
            blocks[current].append(line)

    case["blocks"] = blocks
    case["must"] = _patterns(blocks.get("Must contain", []))
    case["must_not"] = _patterns(blocks.get("Must not contain", []))
    case["review"] = _patterns(blocks.get("Review signals", []))
    case["prompt"] = "\n".join(blocks.get("Prompt", [])).strip()
    return case


def _patterns(lines: list[str]) -> list[str]:
    out = []
    for line in lines:
        m = re.match(r"^\s*-\s+(.*\S)\s*$", line)
        if m:
            out.append(m.group(1))
    return out


def lint() -> int:
    cases = sorted(CASES.glob("EV-*.md"))
    errors: list[str] = []
    if not cases:
        print("  ERROR no cases found")
        return 1

    seen_ids = set()
    for p in cases:
        c = parse_case(p)
        for s in SECTIONS:
            if s not in c["blocks"]:
                errors.append(f"{p.name}: missing `## {s}` section")
        if not c["skill"]:
            errors.append(f"{p.name}: missing `skill:` line")
        if not c["prompt"]:
            errors.append(f"{p.name}: empty prompt")
        if not c["must"] and not c["must_not"]:
            errors.append(f"{p.name}: no assertions — case cannot fail")
        if c["id"] in seen_ids:
            errors.append(f"{p.name}: duplicate id {c['id']}")
        seen_ids.add(c["id"])
        for pat in c["must"] + c["must_not"] + c["review"]:
            try:
                re.compile(pat)
            except re.error as e:
                errors.append(f"{p.name}: bad regex {pat!r} ({e})")

    for e in errors:
        print(f"  ERROR {e}")
    if errors:
        print(f"\n  {len(cases)} case(s), {len(errors)} error(s) — FAIL")
        return 1
    print(f"  {len(cases)} case(s) well-formed — OK")
    return 0


def score(case_path: Path, reply_path: Path) -> bool:
    case = parse_case(case_path)
    reply = reply_path.read_text()

    missing = [p for p in case["must"] if not re.search(p, reply)]
    tripped = [p for p in case["must_not"] if re.search(p, reply)]
    flagged = [p for p in case["review"] if re.search(p, reply)]

    ok = not missing and not tripped
    label = "PASS" if ok else "FAIL"
    if ok and flagged:
        label = "REVIEW"

    print(f"  {label:6} {case['id']}  ({case['skill']})  <- {reply_path.name}")
    for p in tripped:
        m = re.search(p, reply)
        excerpt = reply[max(0, m.start() - 40) : m.end() + 40].replace("\n", " ")
        print(f"         forbidden pattern matched: {p}")
        print(f"           ...{excerpt.strip()}...")
    for p in missing:
        print(f"         required pattern absent:   {p}")
    for p in flagged:
        print(f"         review signal:             {p}")
    return ok


def main() -> int:
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 0

    if args[0] == "--lint":
        return lint()

    if args[0] == "--batch":
        if len(args) < 2:
            print("  ERROR --batch needs a directory")
            return 1
        replies = sorted(Path(args[1]).glob("*.md"))
        if not replies:
            print(f"  ERROR no .md replies in {args[1]}")
            return 1
        failures = 0
        for r in replies:
            m = re.search(r"(EV-\d+)", r.name)
            if not m:
                print(f"  SKIP   {r.name} (no EV-nnn in filename)")
                continue
            matches = list(CASES.glob(f"{m.group(1)}-*.md"))
            if not matches:
                print(f"  SKIP   {r.name} (no case {m.group(1)})")
                continue
            if not score(matches[0], r):
                failures += 1
        print(f"\n  {failures} failure(s)")
        return 1 if failures else 0

    if len(args) != 2:
        print("  ERROR expected: check.py CASE.md REPLY.md")
        return 1
    return 0 if score(Path(args[0]), Path(args[1])) else 1


if __name__ == "__main__":
    sys.exit(main())
