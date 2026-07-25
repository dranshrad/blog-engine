---
name: editorial-pass
description: >-
  Multi-pass editorial refinement with inspectable numbered intermediates.
  Runs a configurable SPARK pass chain: Sanitize → Pace → Architecture →
  Reference → Knife. Preserves author voice, never invents facts, and can
  hand off to blog-engine stress tests. Use when polishing a draft, running
  an editing pipeline, or multi-pass prose refinement.
license: MIT
---

# Editorial Pass (SPARK Chain)

Original multi-pass editor for Clearcast. Not a UK-locale pipeline and not a
port of third-party writing-squad plugins.

**Core law:** preserve author voice. Fix clarity and correctness; do not
homogenize personality.

## SPARK passes

| # | Pass | Does | Must not |
|---|------|------|----------|
| 1 | **Sanitize** | Typos, grammar, broken markdown, consistency of spelling locale chosen by user | Rewrite voice |
| 2 | **Pace** | Rhythm, paragraph breaks, cut throat-clearing | Add new claims |
| 3 | **Architecture** | Headings, order, intent purity flags | Invent sections with new facts |
| 4 | **Reference** | Flag unsourced material claims; propose citation slots | Fabricate sources |
| 5 | **Knife** | Cut filler; tighten; optional SEO polish only on visible truth | Keyword stuffing |

User may skip, reorder, or stop after any pass.

## Locale

Ask once: `en-US` | `en-GB` | `keep-as-is`. Default `keep-as-is`.
Do not force British English.

## Workspace intermediates

Write under a working folder the user chooses (default `./editorial/<slug>/`):

```
00_original.md
01_sanitize.md
02_pace.md
03_architecture.md
04_reference.md
05_knife.md
final.md
pass-log.md
```

Never overwrite the user’s source file; always copy into `00_original.md` first.

## Pass log format

```markdown
## Pass log
| Pass | Changes (count) | Voice drift risk | Notes |
|------|----------------:|------------------|-------|
| Sanitize | 12 | low | … |
```

## Voice lock

Before pass 1, extract a short **voice lock** (see [references/voice-lock.md](references/voice-lock.md)):

- Sentence length tendency
- Formality
- Humor allowance
- Banned phrases (from `VOICE.md` if present)

Every pass must re-check the voice lock. If a pass would flatten voice, revert that change.

## Fact freeze

- No new statistics, quotes, or studies
- Reference pass only marks gaps (`[CITE NEEDED: claim]`) or links user-provided sources
- For publish-ready evidence, hand off to `blog-engine` `verify` / claim ledger

## Optional bridges

- After Knife → run `blog-engine` `score` if the piece is a blog post
- After Knife → run `social-cast` `atomize` if user wants social packs
- If YMYL topic → require `blog-engine` YMYL intensifier before calling it done

## Interaction pattern

After each pass:

1. Summarize what changed (≤5 bullets)
2. Ask: continue / skip next / stop / re-run this pass

If user said “run full SPARK”, continue without pausing until `final.md`.
