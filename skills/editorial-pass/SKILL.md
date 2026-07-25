---
name: editorial-pass
description: >-
  Groundledger SPARK multi-pass editor plus Tone Retarget, Locale Lock, Voice
  Specimens, Style Pattern Mine, and Voice Canon. Preserves author voice, never
  invents facts. Use when polishing drafts, retargeting tone, or building a
  style guide from samples.
license: MIT
---

# Editorial Pass (SPARK Chain)

Groundledger multi-pass editor. Locale is user-chosen (never forced).

**Core laws:** preserve author voice · obey Grounding Law (`blog-engine/references/grounding.md`) — fact freeze means no new invented claims.

## Modes

| Mode | Job |
|------|-----|
| `spark` | Full or partial SPARK chain (default) |
| `tone` | **Tone Retarget** — new tone, same substance |
| `locale-lock` | **Locale Lock** — en-US / en-GB / custom glossary |
| `specimens` | **Voice Specimens** — annotated samples |
| `mine` | **Style Pattern Mine** — patterns from samples |
| `canon` | **Voice Canon** — synthesize `VOICE.md` |

## SPARK passes

| # | Pass | Does | Must not |
|---|------|------|----------|
| 1 | Sanitize | Typos, grammar, markdown, locale consistency | Rewrite voice |
| 2 | Pace | Rhythm, cuts throat-clearing | Add claims |
| 3 | Architecture | Headings, order, intent flags | Invent facts |
| 4 | Reference | Flag unsourced claims | Fabricate sources |
| 5 | Knife | Tighten; optional SEO on visible truth | Keyword stuffing |

Skip/reorder/stop allowed. Full SPARK → write intermediates without pausing.

## Intermediates

Default `./editorial/<slug>/`:

```
00_original.md
01_sanitize.md … 05_knife.md
final.md
pass-log.md
```

Never overwrite the source; copy to `00_original.md` first.

## Voice lock

Before pass 1: [references/voice-lock.md](references/voice-lock.md). Revert flattening edits.

## Tone Retarget (`tone`)

Inputs: draft + target tone (e.g. warmer, more formal, less hype).  
Constraints: zero new claims; preserve meaning; emit diff summary of tone moves only.

## Locale Lock (`locale-lock`)

Apply chosen locale + optional glossary. Default `keep-as-is` if unspecified. Never force en-GB.

## Voice Specimens → Mine → Canon

1. **specimens** — store annotated samples under `./voice/specimens/`  
2. **mine** — extract recurring patterns (length, openers, humor, bans)  
3. **canon** — write/update `VOICE.md` for suite-wide use  

See [references/voice-canon.md](references/voice-canon.md).

## Fact freeze

No new stats/quotes/studies. Publish-ready evidence → `blog-engine` `verify`.

## Bridges

After Knife → optional `blog-engine` `score` or `social-cast` `atomize`. YMYL → blog-engine intensifier.
