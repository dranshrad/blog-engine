#!/usr/bin/env python3
"""
Groundledger structural validator.

Checks the invariants the suite depends on but cannot enforce at runtime,
because a skill is prose and prose has no compiler. Run before every commit:

    python3 scripts/validate.py

Exit code 0 = clean, 1 = at least one ERROR. Warnings never fail the build.

The check that matters most is DUAL-LAYOUT PATH VALIDITY (check 5). Skills live
at `skills/<name>/` in this repo but at `~/.claude/skills/<name>/` once
installed — there is no `skills/` parent after install. A path like
`skills/blog-engine/references/grounding.md` therefore resolves in the repo and
breaks silently on every user's machine. Sibling-relative `../blog-engine/...`
is the only form correct in both layouts.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

REQUIRED_FRONTMATTER = ("name", "description", "license", "compatibility")
MAX_SKILL_LINES = 500  # AGENTS.md: depth belongs in references/
GROUNDING = "blog-engine/references/grounding.md"

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block, out, key = text[3:end], {}, None
    for line in block.splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if m:
            key = m.group(1)
            out[key] = m.group(2).strip()
        elif key and line.strip():
            out[key] += " " + line.strip()
    return out


def main() -> int:
    skill_dirs = sorted(d for d in SKILLS.iterdir() if d.is_dir())
    names = {d.name for d in skill_dirs}

    if not skill_dirs:
        err("no skills found under skills/")
        return report()

    for d in skill_dirs:
        sk = d / "SKILL.md"

        # 1 — every skill has an entry point
        if not sk.exists():
            err(f"{d.name}: missing SKILL.md")
            continue

        text = sk.read_text()
        fm = frontmatter(text)

        # 2 — frontmatter completeness
        for field in REQUIRED_FRONTMATTER:
            if field not in fm:
                err(f"{d.name}: frontmatter missing `{field}:`")

        # 3 — name must equal directory name (AGENTS.md), or routing breaks
        if fm.get("name") and fm["name"] != d.name:
            err(f"{d.name}: frontmatter name `{fm['name']}` != directory `{d.name}`")

        # 4 — context budget
        n = len(text.splitlines())
        if n > MAX_SKILL_LINES:
            err(f"{d.name}: SKILL.md is {n} lines (cap {MAX_SKILL_LINES}) — move depth to references/")
        elif n > MAX_SKILL_LINES * 0.9:
            warn(f"{d.name}: SKILL.md is {n} lines, approaching the {MAX_SKILL_LINES} cap")

        # 5 — dual-layout path validity (the silent-breakage check)
        for m in re.finditer(r"(?<![\w./-])skills/([a-z-]+)/", text):
            if m.group(1) in names:
                err(
                    f"{d.name}: repo-root path `skills/{m.group(1)}/...` breaks after install "
                    f"— use `../{m.group(1)}/...`"
                )

        # 6 — the Grounding Law must be reachable from every skill
        if d.name == "blog-engine":
            if "references/grounding.md" not in text:
                err("blog-engine: does not reference its own grounding.md")
        elif GROUNDING not in text:
            err(f"{d.name}: never references the Grounding Law ({GROUNDING})")
        elif f"../{GROUNDING}" not in text:
            err(f"{d.name}: references grounding.md by a non-sibling path — use `../{GROUNDING}`")

        # 7 — no residual pre-rename branding inside shipped skills
        if re.search(r"clearcast", text, re.I):
            err(f"{d.name}: contains pre-rename `Clearcast` branding")

    # 8 — every relative markdown link resolves from its own file
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts or "node_modules" in md.parts:
            continue
        for m in re.finditer(r"\]\(([^)]+)\)", md.read_text()):
            target = m.group(1).split("#")[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (md.parent / target).resolve().exists():
                err(f"{md.relative_to(ROOT)}: broken link -> {target}")

    # 9 — flat-install layout: skills ship WITHOUT the repo around them, so any
    # link escaping the skill root (../../docs/...) dangles on every machine.
    # This is the same defect class as check 5 in a different shape.
    import shutil, tempfile
    with tempfile.TemporaryDirectory() as tmp:
        flat = Path(tmp) / "skills"
        shutil.copytree(SKILLS, flat)
        for md in flat.rglob("*.md"):
            for m in re.finditer(r"\]\(([^)]+)\)", md.read_text()):
                target = m.group(1).split("#")[0].strip()
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                if not (md.parent / target).resolve().exists():
                    err(
                        f"{md.relative_to(flat)}: link `{target}` dangles in flat install "
                        f"— escapes the skill root; use an absolute URL"
                    )

    # 10 — the router must be able to reach every specialist
    router = SKILLS / "groundledger" / "SKILL.md"
    if router.exists():
        rt = router.read_text()
        for name in names - {"groundledger"}:
            if name not in rt:
                err(f"router: does not route to `{name}`")

    return report()


def report() -> int:
    for w in warnings:
        print(f"  WARN  {w}")
    for e in errors:
        print(f"  ERROR {e}")
    if errors:
        print(f"\n  {len(errors)} error(s), {len(warnings)} warning(s) — FAIL")
        return 1
    print(f"  {len(warnings)} warning(s), 0 errors — OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
