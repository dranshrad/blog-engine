# Clearcast — Agent Skills for Content, SEO, AEO & Paid Media

<p align="center">
  <img src="assets/og-cover.png" alt="Clearcast — CLEAR SPARK ORBIT SNAP PROBE SAFE agent skills" width="100%">
</p>

**Clearcast** is an MIT suite of Agent Skills for **Claude Code**, **Cursor**, and **Cowork**: publish-ready blogging, site SEO audits, observe-only paid media, multi-pass editing, platform-native social, and multi-surface strategy — with a hard ban on fabricated statistics.

> Docs: [dranshrad.github.io/clearcast](https://dranshrad.github.io/clearcast/) · Repo: [github.com/dranshrad/clearcast](https://github.com/dranshrad/clearcast)

Updated: 2026-07-25

## Why Clearcast?

Content and acquisition work should (1) help a reader finish a job, (2) be extractable for AI answers, (3) cast into social without inventing numbers, (4) audit sites with falsifiable recommendations, and (5) keep paid media **observe-only** until explicit approval. Clearcast ships **CLEAR**, **SPARK**, **ORBIT**, **SNAP/PULSE**, **PROBE**, **SAFE**, Studio Desk, and Cue Deck — plus a binding [Grounding Law](skills/blog-engine/references/grounding.md).

## Skills

| Skill | Framework | Use for |
|-------|-----------|---------|
| [clearcast](skills/clearcast/) | Router | Pick / compose skills |
| [blog-engine](skills/blog-engine/) | **CLEAR** | Articles, claim ledgers, Ship Scan, Cite Surface |
| [editorial-pass](skills/editorial-pass/) | **SPARK** | Multi-pass polish, Tone Retarget, Voice Canon |
| [social-cast](skills/social-cast/) | **SNAP + PULSE** | Hooks, posts, atomize, calendars, analytics |
| [orbit-discovery](skills/orbit-discovery/) | **ORBIT** | Surface bets, Echo Map, Close Path |
| [site-signal](skills/site-signal/) | **PROBE** | Site Health Dial, page-fit, cite-AI, drift, local SEO |
| [paid-cast](skills/paid-cast/) | **SAFE** | Paid audits, unit econ, brand/budget lattices; MutationLatch |
| [studio-desk](skills/studio-desk/) | Ops | Workspace Boot, versions, export, Ship Gate |
| [cue-deck](skills/cue-deck/) | Prompts | Reusable grounded cue cards |

## Install

### Claude Code

```bash
git clone https://github.com/dranshrad/clearcast.git
mkdir -p ~/.claude/skills
cp -R clearcast/skills/* ~/.claude/skills/
```

Plugin-style (from repo root, Claude Code):

```text
/plugin marketplace add dranshrad/clearcast
/plugin install clearcast@clearcast-marketplace
```

Or: `claude plugin install .` when this directory is the working tree (if your Claude Code build supports local plugin install).

### Cursor

```bash
git clone https://github.com/dranshrad/clearcast.git
mkdir -p ~/.cursor/skills
cp -R clearcast/skills/* ~/.cursor/skills/
```

### Cowork / skill zip upload

Zip each folder under `skills/<name>/` (must contain `SKILL.md`) and upload via **Cowork → Customize → Skills**. Upload all nine for the full suite, or start with `clearcast` + `blog-engine`.

Project-local (either client): copy into `.claude/skills/` and/or `.cursor/skills/`.

Details: [INSTALL.md](INSTALL.md) · [CLAUDE.md](CLAUDE.md) · [docs/getting-started.md](docs/getting-started.md).

## Grounding (no hallucinations)

Before any draft is “final”:

1. Material claims are on a **claim ledger** (`verified` / `attributed` / `author-supplied`)
2. No invented stats, studies, quotes, rankings, ROAS, or customer results
3. Uncertain points use soft language or are omitted
4. `blocked` ledger rows must be fixed or removed
5. Paid: no live spend changes unless **MutationLatch** is open and approved

Full rules: [skills/blog-engine/references/grounding.md](skills/blog-engine/references/grounding.md).

## Typical pipelines

**Content:** `orbit-discovery` → `blog-engine` → `editorial-pass` → `social-cast` → `studio-desk` ship  

**Site SEO:** `site-signal` `audit` → PROBE plan → `blog-engine` / `orbit-discovery` for fixes  

**Paid:** `paid-cast` `audit` (observe-only) → `trial` / `math` → latch-gated `optimize-draft` only with approval  


## Related repositories

| Project | Link |
|---------|------|
| Voice notes → Artifacts | [voice-notes-to-anthropic-artifacts](https://github.com/dranshrad/voice-notes-to-anthropic-artifacts) |
| LibCST LLM refactorer | [llm-cst-refactorer](https://github.com/dranshrad/llm-cst-refactorer) |
| Self-correction loop | [automated-self-correction-loop](https://github.com/dranshrad/automated-self-correction-loop) |
| Anthropic audio gateway | [anthropic-audio-gateway](https://github.com/dranshrad/anthropic-audio-gateway) |

See [docs/ECOSYSTEM.md](docs/ECOSYSTEM.md).

## License

[MIT](LICENSE) © 2026 Divyansh Gupta
