# Groundledger — brand & entity card

| Field | Value |
|-------|--------|
| **Name** | Groundledger |
| **What it is** | MIT Agent Skills suite for Claude Code, Cursor, and Cowork |
| **Focus** | Grounded blogging (CLEAR), site SEO (PROBE), paid media observe-only (SAFE), SPARK editorial, SNAP/PULSE social, ORBIT discovery |
| **Author** | Divyansh Gupta ([@dranshrad](https://github.com/dranshrad)) |
| **License** | [MIT](https://github.com/dranshrad/groundledger/blob/master/LICENSE) |
| **Code** | https://github.com/dranshrad/groundledger |
| **Docs** | https://dranshrad.github.io/groundledger/ |
| **Machine map** | https://dranshrad.github.io/groundledger/llms.txt |

## Disambiguation

Formerly published as **Clearcast**. Renamed to **Groundledger** to avoid unrelated name collisions.

**Not affiliated with** Clearcast UK (ad clearance), ClearCast weather apps, ClearCast audio tools, or any other third-party “Clearcast/ClearCast” product.

## Install (one-liners)

```bash
git clone https://github.com/dranshrad/groundledger.git
cd groundledger && bash scripts/install.sh
```

Claude Code plugin:

```text
/plugin marketplace add dranshrad/groundledger
/plugin install groundledger@groundledger-marketplace
```

After renaming from Clearcast, remove stale `~/.claude/skills/clearcast` and `~/.cursor/skills/clearcast` if present.

## Google Search Console (indexing)

1. Open [Google Search Console](https://search.google.com/search-console)
2. Add property URL prefix: `https://dranshrad.github.io/groundledger/`
3. Verify ownership (HTML file upload into `docs/` then push, or another method Google offers)
4. Submit sitemap: `https://dranshrad.github.io/groundledger/sitemap.xml`
5. Optional: Bing Webmaster Tools with the same sitemap (helps Copilot surfaces)

## Suggested launch title (external post)

> Groundledger: Claude Code & Cursor agent skills for grounded blog SEO, AEO, and observe-only paid media

Link GitHub + docs; mention Grounding Law, PROBE, and SAFE as unique frameworks.

[← Home](index.html)
