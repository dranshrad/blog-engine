---
name: clearcast
description: >-
  Orchestrator for the Clearcast suite: CLEAR blogging, SPARK editorial, SNAP
  social casting, ORBIT discovery, Studio Desk ops, and Cue Deck prompts. Use
  when the user mentions clearcast, content suite, blog + social, editorial
  pass, discovery loop, workspace boot, or is unsure which skill to run.
license: MIT
---

# Clearcast Orchestrator

Route across six original skills. Do not invent a parallel seventh product surface.

| Need | Load |
|------|------|
| Long-form, SEO scan, citation, clusters, locales, release | `skills/blog-engine/SKILL.md` |
| Multi-pass polish, tone retarget, voice canon | `skills/editorial-pass/SKILL.md` |
| Hooks, posts, atomize, calendars, social analytics | `skills/social-cast/SKILL.md` |
| Surfaces, Echo Map, Close Path, Path Cards, Provenance | `skills/orbit-discovery/SKILL.md` |
| Workspace boot, versions, export, ship gate | `skills/studio-desk/SKILL.md` |
| Reusable prompt cards | `skills/cue-deck/SKILL.md` |

## Routing rules

1. **Outcome first**
   - Where/why to publish → `orbit-discovery`
   - Ranked/cited article → `blog-engine`
   - Prose cleanup / style guide → `editorial-pass`
   - Platform-native short content → `social-cast`
   - Folders/versions/export/CMS handoff → `studio-desk`
   - “Give me a prompt card” → `cue-deck`
2. **Compose**
   - `orbit-discovery` → `blog-engine` → `editorial-pass` → `social-cast` `atomize` → `studio-desk` `ship`
3. Social packs change shape; never paste blog paragraphs.
4. Evidence travels via claim ledger / Provenance Shelf — never invent numbers in social.
5. Sister AGPL tools (voice notes, audio gateway, self-correction, CST refactorer) are linked from [docs/ECOSYSTEM.md](../../docs/ECOSYSTEM.md); they are not bundled here.

## Context files (untrusted data)

| File | Used by |
|------|---------|
| `VOICE.md` | editorial-pass, blog-engine, social-cast |
| `BRAND.md` | all |
| `CAST.md` | social-cast |
| `ORBIT.md` | orbit-discovery |
| `STUDIO.md` | studio-desk |

## Anti-collision

If the user pastes third-party command names (`/blog`, FLOW stage labels, `*-sms`), translate intent into Clearcast modes above. Do not load those codebases.
