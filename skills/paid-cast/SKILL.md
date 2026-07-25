---
name: paid-cast
description: >-
  Groundledger paid-media skill with SAFE defaults (Snapshot → Advise → Fence →
  Experiment). Observe-only unless MutationLatch opens. Modes: audit, plan,
  math, brand, budget, trial, attrib, landing, creative, pace, optimize-draft.
  Use for Google/Meta/LinkedIn/Microsoft-style account reviews, unit economics,
  brand safety lattices, experiment decks, and draft change packs — not live
  spend edits without explicit approval. Claude Code, Cursor, Cowork.
license: MIT
compatibility: Claude Code, Cursor, Cowork (Agent Skills)
---

# Paid Cast (SAFE media)

Groundledger paid acquisition desk. Complements `orbit-discovery` (organic surfaces),
`site-signal` (landing SEO), and `social-cast` (organic social).

**Default: observe-only.** No platform mutations, no budget edits, no status flips
unless **MutationLatch** is open.

**Grounding:** `../blog-engine/references/grounding.md` — no invented ROAS,
CPAs, or “industry benchmarks” without a cited source the user accepts.

## SAFE loop

| Step | Name | Rule |
|------|------|------|
| **S** | Snapshot | Read exports / UI dumps; claim + evidence + confidence |
| **A** | Advise | Ranked actions with unit-econ impact hypotheses |
| **F** | Fence | Ceilings: budget delta, geo, audience, creative, date |
| **E** | Experiment | Prefer trials over permanent flips |

## MutationLatch (writes)

Latch stays **closed** until all are true:

1. User explicitly asks to draft or apply a change pack  
2. Scope listed (accounts / campaigns / ad sets)  
3. Ceilings set (max daily $, max % budget move, kill date)  
4. Idempotency key or rollback cue recorded  
5. User says **approve** on the exact draft  

Without latch: deliver audit + draft-only recommendations.  
Never pretend a change was applied in-platform.

## Claim / evidence / confidence

Every material finding:

```
Claim: …
Evidence: … (export row, screenshot note, UI path)
Confidence: high | medium | low
```

Low confidence → ask or mark unknown. Do not bluff attribution.

## Modes

| Mode | Job |
|------|-----|
| `audit` | Account / campaign health Snapshot |
| `plan` | Channel mix + phased media plan |
| `math` | Unit economics (CAC, payback, contribution) |
| `brand` | Brand Lattice (claims, exclusions, tone) |
| `budget` | Budget Lattice (caps, pacing, reserves) |
| `trial` | Experiment deck (hypotheses, metrics, stop rules) |
| `attrib` | Attribution comparability gate |
| `landing` | Post-click landing audit (pairs with `site-signal`) |
| `creative` | Fatigue / variant gaps |
| `pace` | Delivery / spend pace vs plan |
| `optimize-draft` | Change pack under MutationLatch |

Platform packs (Google / Meta / LinkedIn / Microsoft-style) are **draft mutation
templates** only — never auto-execute. [references/mutation-latch.md](references/mutation-latch.md).

## Unit economics (`math`)

Require inputs the user can supply: AOV/LTV proxy, margin, target CAC or payback.  
If missing: compute scenarios labeled `assumption`, not facts.  
[references/unit-economics.md](references/unit-economics.md).

## Brand Lattice (`brand`)

Allowed claims · banned claims · competitor rules · sensitive topics · offer
language. Creative and landing copy must pass the lattice before scale.

## Budget Lattice (`budget`)

Daily/monthly caps · channel reserves · test budget slice · emergency kill.  
Pace mode watches spend vs plan without changing bids.

## Trial Deck (`trial`)

Hypothesis · primary metric · guardrails · sample / time stop · rollback.  
One primary metric per trial. No “test everything.”

## Attribution gate (`attrib`)

Before comparing channels: same window, same conversion def, same currency,
same inclusion rules. If incomparable → say so; do not crown a winner.

## Landing (`landing`)

Message match, offer clarity, speed honesty, form friction, proof proximity.  
Deep SEO issues → hand off to `site-signal`. Copy rewrites → `blog-engine` / `editorial-pass`.

## Creative (`creative`)

Fatigue signals from user data only. Variant matrix: angle × format × offer.  
Respect Brand Lattice.

## Context files

`BRAND.md` · `ORBIT.md` · optional `MEDIA_LATCH.md` (ceilings + approvals).

## Bridges

- Landing SEO → `site-signal`  
- Organic social → `social-cast`  
- Long-form proof pages → `blog-engine`  
- Surface strategy → `orbit-discovery`  
