# Getting started with Clearcast

## 1. Install (Claude Code + Cursor)

```bash
git clone https://github.com/dranshrad/clearcast.git
cd clearcast
bash scripts/install.sh
```

Claude only: `bash scripts/install.sh --claude` → `~/.claude/skills/`  
Cursor only: `bash scripts/install.sh --cursor` → `~/.cursor/skills/`

**Cowork:** zip each `skills/<name>/` folder and upload under Customize → Skills.

## 2. Optional context files

`VOICE.md` · `BRAND.md` · `CAST.md` · `ORBIT.md` · `STUDIO.md` · `SITE_BASELINE.json` · `MEDIA_LATCH.md`

## 3. Grounding

Read [Grounding Law](https://github.com/dranshrad/clearcast/blob/master/skills/blog-engine/references/grounding.md) before drafting. No invented stats, rankings, or ROAS. Paid stays observe-only until MutationLatch.

## 4. First prompts

- “Use Clearcast blog-engine to draft … with a claim ledger.”
- “ORBIT triage for our product.”
- “site-signal audit https://example.com with PROBE recommendations.”
- “paid-cast audit this export — observe only.”
- “Atomize this article with social-cast.”
- “Draw cue P-audit from cue-deck.”

[← Home](index.html) · [Frameworks](frameworks.md) · [Ecosystem](ECOSYSTEM.md)
