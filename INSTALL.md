# Install Clearcast

Works with **Claude Code**, **Cursor**, and **Cowork**.

## One-shot helper

```bash
git clone https://github.com/dranshrad/clearcast.git /tmp/clearcast
cd /tmp/clearcast
bash scripts/install.sh          # installs to Claude + Cursor if those dirs exist
bash scripts/install.sh --claude # ~/.claude/skills only
bash scripts/install.sh --cursor # ~/.cursor/skills only
```

## Claude Code (manual)

```bash
mkdir -p ~/.claude/skills
cp -R /path/to/clearcast/skills/* ~/.claude/skills/
```

Expected:

```
~/.claude/skills/clearcast/
~/.claude/skills/blog-engine/
~/.claude/skills/editorial-pass/
~/.claude/skills/social-cast/
~/.claude/skills/orbit-discovery/
~/.claude/skills/site-signal/
~/.claude/skills/paid-cast/
~/.claude/skills/studio-desk/
~/.claude/skills/cue-deck/
```

Plugin marketplace (from a machine with Claude Code):

```text
/plugin marketplace add dranshrad/clearcast
/plugin install clearcast@clearcast-marketplace
```

Project instructions: keep [CLAUDE.md](CLAUDE.md) in the repo or copy grounding rules into your project `CLAUDE.md`.

## Cursor (manual)

```bash
mkdir -p ~/.cursor/skills
cp -R /path/to/clearcast/skills/* ~/.cursor/skills/
```

## Cowork

1. For each skill under `skills/`, zip the folder so `SKILL.md` is at the zip root (or as the client requires).
2. **Cowork → Customize → Skills → Upload**
3. Repeat for all nine skills for full coverage.

## Project-local

```bash
mkdir -p .claude/skills .cursor/skills
cp -R /path/to/clearcast/skills/* .claude/skills/
cp -R /path/to/clearcast/skills/* .cursor/skills/
```

## Docs

https://dranshrad.github.io/clearcast/

## Optional context files

`VOICE.md` · `BRAND.md` · `CAST.md` · `ORBIT.md` · `STUDIO.md` · optional `SITE_BASELINE.json` · optional `MEDIA_LATCH.md`
