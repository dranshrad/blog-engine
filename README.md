# Clearcast — Cursor Agent Skills for Blog SEO, AEO, Social Content & Discovery

<p align="center">
  <img src="docs/assets/og-cover.svg" alt="Clearcast: CLEAR SPARK ORBIT SNAP Cursor skills for blog SEO AEO social and discovery" width="100%">
</p>

**Clearcast** is an open-source (MIT) suite of [Cursor](https://cursor.com) Agent Skills for publish-ready blogging, multi-pass editing, platform-native social posts, and multi-surface content strategy (search, AI answers, community, profiles).

> Docs site: [dranshrad.github.io/clearcast](https://dranshrad.github.io/clearcast/) · Canonical repo: [github.com/dranshrad/clearcast](https://github.com/dranshrad/clearcast)

Updated: 2026-07-25

## Why Clearcast?

Teams need content that (1) helps a human finish a job, (2) is extractable for AI answers (AEO/GEO readiness), and (3) casts into social without inventing stats. Clearcast ships original frameworks — **CLEAR**, **SPARK**, **ORBIT**, **SNAP/PULSE** — plus Studio Desk ops and a Cue Deck of prompt cards.

It is **not** a fork of third-party Claude Code blog/social plugins. See [NOTICE](NOTICE) and [docs/COVERAGE.md](docs/COVERAGE.md).

## Skills at a glance

| Skill | Framework | Use for |
|-------|-----------|---------|
| [clearcast](skills/clearcast/) | Router | Pick / compose skills |
| [blog-engine](skills/blog-engine/) | **CLEAR** | Articles, Ship Scan, Cite Surface, Freshness Drift, Locale Lattice |
| [editorial-pass](skills/editorial-pass/) | **SPARK** | Multi-pass polish, Tone Retarget, Voice Canon |
| [social-cast](skills/social-cast/) | **SNAP + PULSE** | Hooks, posts, atomize, calendars, Growth Action Stack |
| [orbit-discovery](skills/orbit-discovery/) | **ORBIT** | Surface bets, Echo Map, Close Path, Path Cards |
| [studio-desk](skills/studio-desk/) | Ops | Workspace Boot, versions, Export Pack, Ship Gate |
| [cue-deck](skills/cue-deck/) | Prompts | Reusable ORBIT/CLEAR cue cards |

## Install (Cursor)

```bash
git clone https://github.com/dranshrad/clearcast.git
mkdir -p ~/.cursor/skills
cp -R clearcast/skills/* ~/.cursor/skills/
```

Project-local: copy into `.cursor/skills/` instead. Details: [INSTALL.md](INSTALL.md) · [Getting started](docs/getting-started.md).

## Typical pipelines

1. **Strategy → article → social**  
   `orbit-discovery` triage → `blog-engine` draft → `editorial-pass` SPARK → `social-cast` atomize → `studio-desk` ship
2. **SEO audit** — `blog-engine` ship-scan + cite-surface  
3. **Voice guide** — `editorial-pass` specimens → mine → canon  
4. **Prompt** — `cue-deck` draw `C-draft`

## Related public repositories

| Project | Link |
|---------|------|
| Voice notes → Artifacts | [voice-notes-to-anthropic-artifacts](https://github.com/dranshrad/voice-notes-to-anthropic-artifacts) |
| LibCST LLM refactorer | [llm-cst-refactorer](https://github.com/dranshrad/llm-cst-refactorer) |
| Self-correction loop | [automated-self-correction-loop](https://github.com/dranshrad/automated-self-correction-loop) |
| Anthropic audio gateway | [anthropic-audio-gateway](https://github.com/dranshrad/anthropic-audio-gateway) |

Full pairing notes: [docs/ECOSYSTEM.md](docs/ECOSYSTEM.md).

## FAQ

**Does this guarantee rankings or AI citations?** No — it raises editorial and extractability readiness.  
**Google SEO / AEO?** Ship Scan, Cite Surface, ORBIT surface bets, and claim discipline target search + answer engines as one craft.  
**Copyright?** Original Clearcast expression under MIT; see NOTICE.

More: [docs/faq.md](docs/faq.md).

## License

[MIT](LICENSE) © 2026 Divyansh Gupta
