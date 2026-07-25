---
name: studio-desk
description: >-
  Groundledger workspace ops: Workspace Boot, studios (Longform, Blog Desk, Op-Ed
  Shelf, Doc Templates), Draft Lineage, Version Vault, Cast Desk Status, Export
  Pack, Ship Gate, Collection Index. Use when scaffolding a writing workspace,
  versioning drafts, exporting, or preparing CMS handoff.
license: MIT
---

# Studio Desk

Groundledger workspace and publishing-ops skill.

## Modes

| Mode | Job |
|------|-----|
| `boot` | **Workspace Boot** + studio variant |
| `lineage` | **Draft Lineage** — next version with targeted edits |
| `vault` | **Version Vault** — archive old versions |
| `status` | **Cast Desk Status** — drafts / versions / shipped |
| `export` | **Export Pack** — md bundle / HTML / plain text notes |
| `ship` | **Ship Gate** — CMS/handoff checklist |
| `index` | **Collection Index** — TOC for a posts folder |

## Workspace Boot (`boot`)

Ask: studio variant + name + local path.

### Studios

| Studio | Layout |
|--------|--------|
| **Longform** | `drafts/` `research/` `notes/` `images/` `archive/` |
| **Blog Desk** | `drafting/` `published/` `briefs/` `archive/` |
| **Op-Ed Shelf** | `posts/<topic>/` `drafts/` `archive/` |
| **Doc Templates** | `templates/` `exports/` `archive/` |

Write a short `STUDIO.md` describing conventions. Do not create secrets. Optional: remind user they can `git init` — do not force public GitHub creation.

Folder rules: [references/studio-layout.md](references/studio-layout.md).

## Draft Lineage (`lineage`)

Copy current draft to `vN+1` (or dated stamp). Require a **diff contract** (KEEP/CHANGE/DELETE). Never overwrite `vN` in place.

## Version Vault (`vault`)

Move superseded versions into `archive/YYYY-MM/` with a one-line reason log.

## Cast Desk Status (`status`)

Scan workspace; summarize: active drafts, latest versions, published count, stale (>N days) items.

## Export Pack (`export`)

From a draft path, produce:

- Combined markdown (front matter + body)
- Optional HTML sketch (semantic article wrapper)
- Plain-text stripped copy
- Manifest listing files

Does not claim pixel-perfect PDF; note user may print HTML to PDF.

## Ship Gate (`ship`)

Handoff checklist: final path, CLEAR/Ship Scan status if blog, cast pack if social, CMS fields, URL slug, OG image, owner. Pair with blog-engine **Release Latch**.

## Collection Index (`index`)

Generate `INDEX.md` listing titles, dates, jobs, paths for a posts directory.

## Bridges

- Writing → `blog-engine` / `editorial-pass`
- Social → `social-cast`
- Strategy → `orbit-discovery`
