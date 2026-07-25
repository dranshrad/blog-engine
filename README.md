# Clearcast

**Original Cursor skill suite for long-form publishing, editorial refinement, social casting, and multi-surface discovery.**

MIT License © 2026 Divyansh Gupta

Clearcast is **not** a fork or mash-up of third-party Claude plugin trees. It was designed as one coherent system after studying the content landscape (blog engines, editorial pipelines, social skill packs, and multi-surface SEO knowledge bases) and then writing new frameworks, names, artifacts, and workflows from scratch.

## Skills

| Skill | Framework | Use for |
|-------|-----------|---------|
| [`clearcast`](skills/clearcast/) | Router | Pick the right skill / compose a pipeline |
| [`blog-engine`](skills/blog-engine/) | **CLEAR** | Articles with claim ledgers, Q-tests, YMYL gates |
| [`editorial-pass`](skills/editorial-pass/) | **SPARK** | Multi-pass polish with numbered intermediates |
| [`social-cast`](skills/social-cast/) | **SNAP + PULSE** | Hooks, posts, threads, atomize, calendars |
| [`orbit-discovery`](skills/orbit-discovery/) | **ORBIT** | Surface choice, clusters, dual scorecards |

### Unique suite features

- Claim ledger + adversarial Q-test + residual risk (blog)
- SPARK inspectable intermediates + voice lock + fact freeze (editorial)
- SNAP hooks + atomize cast packs + PULSE cadence (social)
- ORBIT loop + dual buyer/machine scorecard + intent-pure clusters (discovery)
- Optional project files: `VOICE.md`, `BRAND.md`, `CAST.md`, `ORBIT.md`

## Install

```bash
git clone https://github.com/dranshrad/clearcast.git
cp -R clearcast/skills/* ~/.cursor/skills/
```

Or copy only the skills you need into `.cursor/skills/` inside a project.

## Typical pipelines

**Flagship article → social week**
1. `orbit-discovery` `diagnose` / `brief`
2. `blog-engine` `draft` → stress tests
3. `editorial-pass` full SPARK (optional)
4. `social-cast` `atomize` → `calendar`

**Polish only**
1. `editorial-pass` with voice lock
2. Optional `blog-engine` `score`

**Social-only**
1. `social-cast` `context` → `hook` / `post` / `thread`

## Provenance

See [NOTICE](NOTICE) for non-affiliation and how this suite differs from materials reviewed during design.

Generic practices (cite sources, use headings, match platform norms) are industry craft. Named frameworks here (CLEAR, SPARK, SNAP, PULSE, ORBIT) and their artifacts are original to this repository.

## License

[MIT](LICENSE)
