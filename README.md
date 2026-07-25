# blog-engine

**CLEAR Editorial System** — an original Cursor Agent Skill for drafting, stress-testing, and shipping blog posts.

MIT License © 2026 Divyansh Gupta

## What makes this different

This is **not** a port of any third-party Claude Code blog plugin. It ships its own system:

| Feature | What it does |
|---------|--------------|
| **CLEAR rubric** | Claim · Lexical · Entity · Answer · Reader-job (unique weights) |
| **Claim ledger** | Every material fact tracked to a source status |
| **Adversarial Q-test** | 5 AI-style questions must be answerable from extractable passages |
| **Residual risk register** | Explicit accept/fix gate for open risks |
| **Intent purity** | One reader job per URL; multi-job posts get split |
| **Diff contract** | KEEP / CHANGE / DELETE rules before rewrites |
| **YMYL intensifier** | Extra blockers for health, money, law, safety |
| **Source Diversity Index** | Penalizes monoculture citations |
| **Update triggers** | Substance-based freshness, not date cosmetics |

Ship only when CLEAR ≥ 85 **and** stress tests pass.

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

## Modes

`draft` · `improve` · `score` · `brief` · `map` · `verify` · `cite-probe` · `cluster` · `adapt` · `ymyl` · `calendar`

## Layout

```
SKILL.md
references/
  clear-rubric.md
  artifacts.md
  evidence.md
  craft.md
  forms.md
  ymyl.md
LICENSE
README.md
NOTICE
```

## Provenance & copyright

- Frameworks named above are original to this repository.
- Generic SEO/AEO practices (headings, sourcing, schema hygiene) are industry knowledge.
- This repository does not copy skill text, rubrics, command trees, or delivery-contract language from third-party plugin codebases.

## License

[MIT](LICENSE)
