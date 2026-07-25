---
name: orbit-discovery
description: >-
  Clearcast multi-surface discovery skill using the ORBIT loop: Observe demand,
  Reinforce off-site proof, Build owned assets, Instrument outcomes, Transmit
  learnings. Use for content strategy, topic clusters, surface selection, SEO
  planning, AI-answer presence, or when asking where to publish next.
license: MIT
---

# Orbit Discovery

Original Clearcast loop for choosing **where** and **why** to publish before
**what** to write. Not a copy of any CC-licensed SEO playbook.

```
Observe → Reinforce → Build → Instrument → Transmit → (repeat)
```

## Modes

| Mode | Output |
|------|--------|
| `diagnose` | Which ORBIT stage is blocking |
| `surfaces` | Ranked surface bets for a job |
| `cluster` | Intent-pure URL graph |
| `brief` | Asset brief with evidence needs + KPI |
| `scorecard` | Dual reader score: human buyer + machine extractability |
| `playbook` | Lightweight path for saas / services / media / local |

## ORBIT stages

| Stage | Question | Typical work |
|-------|----------|--------------|
| **O**bserve | What jobs are buyers trying to finish? | JTBD list, query themes, objection mining |
| **R**einforce | Where is the brand corroborated off-site? | Communities, profiles, reviews, mentions, video |
| **B**uild | What owned asset earns trust + extraction? | Pages, hubs, docs, tools |
| **I**nstrument | How will we know it worked? | Events, leads, citations watched, not vanity alone |
| **T**ransmit | What do we learn into the next cycle? | Retire losers, double winners, update triggers |

## Surfaces (choose explicitly)

Name the surface before writing:

1. Owned site / docs
2. Classic search results
3. AI answers / overviews
4. Community threads
5. Profiles & directories (incl. local where relevant)
6. Video / audio hubs
7. Social feeds (hand to `social-cast`)
8. Sales-assisted pages

Do **not** optimize every surface equally. Pick the one that moves the next business outcome.

## Diagnose workflow

1. State business outcome (lead, signup, trust, hire, etc.)
2. Inventory existing evidence (queries, reviews, analytics, sales notes)
3. Mark the blocked stage (O/R/B/I/T)
4. Propose the smallest asset that unblocks it
5. List claims that need verification before publish

## Cluster rules (intent-pure)

- One primary job per URL
- Hub = map + starter path
- Spokes = decide / act / orient / prove / update
- Bidirectional descriptive links
- Reject duplicate jobs

Hand long-form production to `blog-engine`. Hand social echoes to `social-cast`.

## Dual scorecard

Score any proposed asset 0–5 on each:

**Buyer**
- Job clarity
- Decision risk reduced
- Next action obvious

**Machine**
- Extractable answer opens
- Entity stability
- Evidence labels present

Ship into production only if both totals ≥ 10/15 **or** user accepts residual gaps in writing.

Details: [references/scorecard.md](references/scorecard.md)

## Evidence law

- No unsourced public statistics
- Prefer qualitative strategy language over fake benchmarks
- If citing a number, require publisher + URL + date in the brief

## Playbooks

Lightweight paths in [references/playbooks.md](references/playbooks.md). They are starting heuristics, not dogma.
