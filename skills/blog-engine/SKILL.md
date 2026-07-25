---
name: blog-engine
description: >-
  Clearcast long-form skill: CLEAR rubric, claim ledgers, adversarial Q-tests,
  YMYL intensifiers, residual-risk registers. Use for blog drafts, rewrites,
  briefs, evidence audits, citation checks, or publish readiness. Part of the
  clearcast suite with editorial-pass, social-cast, and orbit-discovery.
license: MIT
---

# Blog Engine (CLEAR Editorial System)

An original publish-readiness skill for Cursor. It is **not** a port, fork, or
thin rewrite of any third-party Claude Code blog plugin.

Industry basics (headings, schema, sourcing) are general craft. The workflows,
rubric, artifacts, and failure modes below are unique to this skill.

**Ship rule:** no draft is shown as final until CLEAR ≥ 85, every material claim
is ledgered, adversarial Q-tests pass, and residual risk is empty or accepted.

## When to load this skill

- New post, rewrite, brief, outline, or cluster plan
- “Is this publish-ready?” / evidence check / citation check
- YMYL topics (health, money, law, safety)
- Multi-audience posts that need intent purity

## Modes

| Mode | Goal |
|------|------|
| `draft` | Produce a new article from a job-to-be-done |
| `improve` | Rewrite with a diff contract (keep / change / delete) |
| `score` | Run CLEAR + emit claim ledger + residual risks |
| `brief` | Competitive teardown + angle + evidence plan |
| `map` | Outline as reader journey, not keyword outline |
| `verify` | Claim-by-claim source audit |
| `cite-probe` | Adversarial Q-test against AI-answer style questions |
| `cluster` | Intent-pure topic graph (one job per URL) |
| `adapt` | Channel packs (newsletter, LinkedIn, Reddit, short video) |
| `ymyl` | Extra medical/finance/legal gates |
| `calendar` | Publishing cadence tied to update triggers |

Default when the user only gives a topic: `draft` after one short JTBD question.

## CLEAR rubric (100 points)

Full checklist: [references/clear-rubric.md](references/clear-rubric.md)

| Letter | Dimension | Points |
|--------|-----------|-------:|
| **C** | Claim integrity | 25 |
| **L** | Lexical clarity | 15 |
| **E** | Entity coherence | 15 |
| **A** | Answer extractability | 25 |
| **R** | Reader-job fit | 20 |

Bands: 85–100 ship · 70–84 revise · <70 rebuild from map.

## Artifacts every draft must produce

Unlike checklist-only systems, every `draft` / `improve` run emits:

1. **Article** (markdown or detected platform format)
2. **Claim ledger** — every material fact with status `verified` / `attributed` / `author-supplied` / `blocked`
3. **Adversarial Q-test** — 5 questions an AI assistant might ask; draft must answer each in ≤120 words with a citeable passage
4. **Residual risk register** — open risks the human must accept or fix
5. **CLEAR scorecard**

Templates: [references/artifacts.md](references/artifacts.md)

## Draft pipeline

### 1. Lock the reader job (JTBD)

Write one sentence:

> When [situation], [reader] wants to [progress], so they can [outcome].

Reject keyword-only briefs. If the post tries two jobs, split into two URLs
(`cluster` mode) instead of stuffing one page.

### 2. Intent purity check

Fail if any of these are true:

- Title promises A, body delivers B
- >2 primary intents share the URL
- Comparison + tutorial + news dump in one page without a clear spine

### 3. Evidence plan before prose

Build the claim ledger skeleton first (empty rows OK). Prefer:

- Primary documents, datasets, official docs
- Named methodology
- Diverse publishers (see Source Diversity Index in [references/evidence.md](references/evidence.md))

**Never invent statistics, quotes, studies, or “internal data.”**
Author anecdotes require author-supplied specifics; otherwise omit first person.

### 4. Map the journey

Outline as stages, not a generic H2 list:

1. Orient (problem + stakes)
2. Decide (criteria / trade-offs)
3. Act (steps or recommendation)
4. Verify (how to know it worked)
5. Next (single CTA or next URL)

Form guidance: [references/forms.md](references/forms.md)

### 5. Write with extractable answers

- Open each major section with a declarative answer sentence
- Keep entity names stable
- Use tables only for real comparisons
- Summary box only when it helps scanning
- One focused CTA after value is delivered

Craft rules: [references/craft.md](references/craft.md)

### 6. Stress tests (blocking)

Run in order; any fail blocks “final”:

| # | Test | Pass criteria |
|---|------|---------------|
| 1 | Claim ledger | No `blocked` rows; material claims `verified` or `attributed` |
| 2 | Contradiction hunt | No internal conflicts (numbers, advice, definitions) |
| 3 | Adversarial Q-test | 5/5 questions answered by extractable passages |
| 4 | CLEAR score | ≥ 85 |
| 5 | YMYL intensifier | If topic is YMYL, all intensifier checks green |
| 6 | Accessibility | Alt text, link purpose, heading order, reading sequence |

### 7. Deliver

Return article + four artifacts. If blocked, return diagnostics only — do not
present a failing draft as ready.

## Improve pipeline (diff contract)

Before rewriting, state:

```markdown
## Diff contract
- KEEP: [voice, unique data, structure pieces]
- CHANGE: [weak evidence, muddy sections, missing answers]
- DELETE: [filler, duplicate intents, unsupported claims]
- MUST NOT: [invent facts, change dates without substance]
```

Then rewrite under that contract and re-run stress tests.

## Cite-probe (unique mode)

Simulate five user questions an AI system might receive about the topic.
For each:

1. Quote the exact passage from the draft that answers it
2. Note missing evidence
3. Propose a ≤40-word patch if the passage fails standalone extraction

This is outcome-oriented (would we be cited?) rather than schema folklore.

## YMYL intensifier

Trigger for health, finance, law, safety, or major life decisions:

- Require higher-tier sources and visible limitations
- Ban absolute guarantees
- Add “who this is / isn’t for”
- Prefer clinician/qualified reviewer attribution when the user supplies one
- Residual risk must include harm scenarios

Details: [references/ymyl.md](references/ymyl.md)

## Cluster mode (intent-pure graph)

Produce a graph where **each URL has one job**:

- Hub = orientation + decision map
- Spokes = single jobs (how-to, comparison, definition, data)
- Edges = descriptive anchors both ways
- Reject spokes that duplicate another spoke’s job

## Adapt mode

From one canonical article, emit channel packs that **change shape**, not just
truncate:

| Channel | Transform |
|---------|-----------|
| Newsletter | Hook + 3 bullets + one CTA |
| LinkedIn | POV opener + one proof + question |
| Reddit | Problem-first, no marketing voice, invite correction |
| Short video | 8s hook, 3 beats, end card |

## What this skill deliberately does not do

- No 30-subcommand mega-orchestrator
- No dependency on a private script farm or installers
- No community footers, marketplace packaging, or third-party brand voice
- No fake “Google guarantees” from schema or FAQPage tricks
- No authorship detection theater

## Progressive disclosure

| File | Load when |
|------|-----------|
| [clear-rubric.md](references/clear-rubric.md) | Scoring |
| [artifacts.md](references/artifacts.md) | Ledgers, Q-tests, risk registers |
| [evidence.md](references/evidence.md) | Sourcing, diversity, fact checks |
| [craft.md](references/craft.md) | Prose, structure, accessibility |
| [forms.md](references/forms.md) | Article shapes by job |
| [ymyl.md](references/ymyl.md) | High-stakes topics |

## Provenance

Copyright (c) 2026 Divyansh Gupta. MIT License.
This skill’s frameworks (CLEAR, claim ledger, adversarial Q-test, residual risk
register, intent purity, diff contract) are original to this repository.
Generic SEO/AEO practices are industry knowledge, not copied from a specific
plugin codebase.
