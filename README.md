# blog-engine

Cursor Agent Skill for writing, rewriting, and auditing blog content optimized for readers, Google search, and AI citation readiness (GEO/AEO).

MIT License.

## Install

**Personal (all projects):**

```bash
git clone https://github.com/dranshrad/blog-engine.git ~/.cursor/skills/blog-engine
```

**Project-only:**

```bash
mkdir -p .cursor/skills
git clone https://github.com/dranshrad/blog-engine.git .cursor/skills/blog-engine
```

Or copy `SKILL.md` and `references/` into `.cursor/skills/blog-engine/`.

## Usage

Ask Cursor to write or audit a blog post, or use commands such as:

- `write <topic>`
- `rewrite <file>`
- `analyze <file-or-url>`
- `brief <topic>`
- `outline <topic>`
- `geo <file>`
- `factcheck <file>`
- `cluster <seed>`

Every draft is scored on a 100-point rubric. Ship only at **90+** with zero P0 issues.

## Layout

```
SKILL.md
references/
  quality-scoring.md
  writing-rules.md
  geo-citation.md
  templates.md
LICENSE
README.md
```

## License

[MIT](LICENSE) © 2026 Divyansh Gupta
