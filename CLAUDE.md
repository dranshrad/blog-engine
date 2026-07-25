# Groundledger — Agent Project Instructions

This repository is the **Groundledger** skill suite for grounded content work on Claude Code, Cursor, and compatible agents (including Cowork skill uploads).

## Load order

1. Read `skills/groundledger/SKILL.md` for routing.
2. Load only the skill needed for the task.
3. Always obey `skills/blog-engine/references/grounding.md` (anti-hallucination).

## Non-negotiables

- Never invent statistics, studies, quotes, or customer results.
- Material claims need a claim-ledger row (`verified` / `attributed` / `author-supplied`).
- Prefer omitting a number over fabricating one.
- Do not present drafts as final while ledger rows are `blocked`.

## Skill map

| Directory | Framework |
|-----------|-----------|
| `skills/groundledger/` | Router |
| `skills/blog-engine/` | CLEAR |
| `skills/editorial-pass/` | SPARK |
| `skills/social-cast/` | SNAP + PULSE |
| `skills/orbit-discovery/` | ORBIT |
| `skills/site-signal/` | PROBE |
| `skills/paid-cast/` | SAFE (+ MutationLatch) |
| `skills/studio-desk/` | Workspace ops |
| `skills/cue-deck/` | Prompt cards |

## Install targets

- Claude Code: `~/.claude/skills/<name>/` (or plugin install from this repo)
- Cursor: `~/.cursor/skills/<name>/`
- Cowork: upload each skill directory / release zip per client UI

## Composition defaults

Content: `orbit-discovery` → `blog-engine` → `editorial-pass` → `social-cast` → `studio-desk` ship  
SEO: `site-signal` → handoff to `blog-engine` / `orbit-discovery`  
Paid: `paid-cast` observe-only; mutations only with approved MutationLatch  
