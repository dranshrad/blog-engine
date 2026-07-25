# Install Groundledger

Works with **Claude Code**, **Cursor**, and **Cowork**.

## One-shot helper

```bash
git clone https://github.com/dranshrad/groundledger.git /tmp/groundledger
cd /tmp/groundledger
bash scripts/install.sh          # installs to Claude + Cursor if those dirs exist
bash scripts/install.sh --claude # ~/.claude/skills only
bash scripts/install.sh --cursor # ~/.cursor/skills only
```

## Claude Code (manual)

```bash
mkdir -p ~/.claude/skills
cp -R /path/to/groundledger/skills/* ~/.claude/skills/
```

Expected:

```
~/.claude/skills/groundledger/
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
/plugin marketplace add dranshrad/groundledger
/plugin install groundledger@groundledger-marketplace
```

Project instructions: keep [CLAUDE.md](CLAUDE.md) in the repo or copy grounding rules into your project `CLAUDE.md`.

## Cursor (manual)

```bash
mkdir -p ~/.cursor/skills
cp -R /path/to/groundledger/skills/* ~/.cursor/skills/
```

## After upgrading from Clearcast

```bash
rm -rf ~/.claude/skills/clearcast ~/.cursor/skills/clearcast
bash scripts/install.sh
```

Plugin users should re-add the marketplace: `dranshrad/groundledger` → `groundledger@groundledger-marketplace`.

## Cowork

1. For each skill under `skills/`, zip the folder so `SKILL.md` is at the zip root (or as the client requires).
2. **Cowork → Customize → Skills → Upload**
3. Repeat for all nine skills for full coverage.

## Project-local

```bash
mkdir -p .claude/skills .cursor/skills
cp -R /path/to/groundledger/skills/* .claude/skills/
cp -R /path/to/groundledger/skills/* .cursor/skills/
```

## Docs

https://dranshrad.github.io/groundledger/

## Optional context files

`VOICE.md` · `BRAND.md` · `CAST.md` · `ORBIT.md` · `STUDIO.md` · optional `SITE_BASELINE.json` · optional `MEDIA_LATCH.md`
