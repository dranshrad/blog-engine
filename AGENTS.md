# Agent conventions (Clearcast)

## Skill layout

Each skill is `skills/<name>/SKILL.md` with optional `references/`.

Frontmatter: `name`, `description`, `license` (MIT). Keep `name` = directory name.

## Grounding

All agents must follow `skills/blog-engine/references/grounding.md`.

## Clients

| Client | Skills path |
|--------|-------------|
| Claude Code | `~/.claude/skills/` or plugin |
| Cursor | `~/.cursor/skills/` |
| Cowork | per-skill zip upload |

## Size

Prefer SKILL.md under ~500 lines; put depth in `references/`.
