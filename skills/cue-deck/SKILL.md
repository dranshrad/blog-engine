---
name: cue-deck
description: >-
  Groundledger Cue Deck: original prompt cards keyed to ORBIT stages and CLEAR
  modes (When, Inputs, Prompt, Output, Risks). Use when the user wants a
  reusable prompt, strategy cue, or agent instruction for content work.
license: MIT
---

# Cue Deck

Groundledger prompt cards. Every card that asks for facts inherits Grounding Law.

## Modes

| Mode | Job |
|------|-----|
| `list` | Show card index |
| `draw` | Emit one card by id or stage |
| `custom` | Build a new card from a user goal |

## Card schema

Every card uses:

```markdown
## Cue — [id]
**When:** …
**Inputs:** …
**Prompt:**
> …
**Output:** …
**Risks:** …
**Next skill:** blog-engine | orbit-discovery | site-signal | paid-cast | social-cast | editorial-pass | studio-desk
```

## Index

Load full text from [references/cards.md](references/cards.md):

| ID | Stage / mode |
|----|----------------|
| `O-jobs` | Observe — JTBD spray |
| `R-echo` | Reinforce — Echo Map |
| `B-brief` | Build — asset brief |
| `I-kpi` | Instrument — measurement |
| `T-retro` | Transmit — learnings |
| `C-draft` | CLEAR draft kickoff |
| `C-verify` | Claim Probe+ |
| `C-cite` | Cite Surface |
| `S-atom` | Social atomize |
| `S-readout` | Pulse readout |
| `E-spark` | SPARK kickoff |
| `D-ship` | Ship Gate |
| `P-audit` | PROBE site audit |
| `P-fit` | Page-fit check |
| `A-snap` | Paid Snapshot (observe-only) |
| `A-latch` | MutationLatch checklist |

When drawing, copy the prompt block verbatim into the agent turn, then execute via the **Next skill**.
