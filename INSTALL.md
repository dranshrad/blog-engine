# Install Clearcast

## Cursor (recommended)

```bash
git clone https://github.com/dranshrad/clearcast.git /tmp/clearcast
mkdir -p ~/.cursor/skills
cp -R /tmp/clearcast/skills/* ~/.cursor/skills/
```

You should see:

```
~/.cursor/skills/clearcast/
~/.cursor/skills/blog-engine/
~/.cursor/skills/editorial-pass/
~/.cursor/skills/social-cast/
~/.cursor/skills/orbit-discovery/
```

Restart Cursor or start a new agent chat, then ask for a blog draft, SPARK pass, social atomize, or ORBIT diagnose.

## Project-local

```bash
mkdir -p .cursor/skills
cp -R /path/to/clearcast/skills/* .cursor/skills/
```

## Optional context files

Create in the project root as needed:

- `VOICE.md` — tone
- `BRAND.md` — claims to avoid / positioning
- `CAST.md` — social pillars & platforms
- `ORBIT.md` — surfaces & KPIs
