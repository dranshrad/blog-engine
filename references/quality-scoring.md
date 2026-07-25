# Blog Quality Scoring (100 points)

Internal editorial-readiness heuristic. Not a Google ranking factor or calibrated
citation probability.

## Content quality (30)

| Check | Pts | Pass criteria |
|-------|----:|---------------|
| Coverage | 7 | Covers the reader task with useful subtopics, evidence, examples; no raw word-count target |
| Readability | 7 | Match audience; default Flesch 60–70 (55–75 OK); denser OK for technical/YMYL |
| Originality | 5 | Original data, case studies, distinctive sourced synthesis, or transparent first-hand evidence |
| Structure | 4 | Clear pacing for the audience; no fixed sentence/paragraph quota |
| Engagement | 4 | Summary box, callouts, or varied blocks when they help |
| Grammar/clarity | 3 | Clean prose; style-list terms are advisory only |

### Readability bands

| Audience | Grade | Flesch Ease |
|----------|-------|-------------|
| Consumer | 6–8 | 60–80 |
| Professional | 8–10 | 50–60 |
| Technical | 10–12 | 30–50 |
| Default | 7–8 | 60–70 |

## SEO (25)

| Check | Pts | Pass criteria |
|-------|----:|---------------|
| Heading hierarchy | 5 | H1→H2→H3, no skips; unique descriptive headings |
| Title clarity | 4 | Accurate, distinctive, matches visible content |
| Topic consistency | 4 | Title, headings, body describe the same reader task |
| Internal links | 4 | 3–10 contextual links; descriptive anchors |
| URL structure | 3 | Stable, readable, consistent casing |
| Meta description | 3 | Page-specific summary matching content |
| External links | 2 | 3–8 outbound links to tier 1–3 sources |

## E-E-A-T (15)

| Check | Pts | Pass criteria |
|-------|----:|---------------|
| Author attribution | 4 | Named author/editor or clear org editorial ownership + bio |
| Source fidelity | 4 | Material claims traceable to supporting sources; zero fabricated |
| Trust indicators | 4 | Contact, about, editorial policy (site-level) |
| Evidence basis | 3 | Verifiable sources, methodology, or supported original material |

No fixed citation form is required. Record dates, publisher, retrieval notes, and
methodology when they identify or change interpretation of a source.

## Technical (15)

| Check | Pts | Pass criteria |
|-------|----:|---------------|
| Schema baseline | 4 | Article/BlogPosting + Person + Organization + BreadcrumbList; FAQPage optional, no bonus |
| Image optimization | 3 | Descriptive alt; modern formats when possible; lazy except LCP |
| Structured elements | 2 | Tables, lists, comparison blocks where useful |
| Speed signals | 2 | Reasonable LCP; avoid render-blocking junk |
| Mobile | 2 | Responsive; no horizontal scroll |
| Social meta | 2 | og:title, og:description, og:image, twitter:card |

## AI citation readiness (15)

| Check | Pts | Pass criteria |
|-------|----:|---------------|
| Evidence-backed citability | 4 | Important sections self-contained + supported |
| Purpose fit | 3 | Clear purpose; intent-matched headings/format |
| Entity clarity | 3 | One primary topic; consistent naming |
| Extraction structure | 3 | Answer-first; tables with headers; process lists |
| Crawler access | 2 | Declared crawlers can reach primary content + schema |

## Score bands

| Score | Rating | Action |
|------:|--------|--------|
| 90–100 | Exceptional | Publish |
| 80–89 | Strong | Minor polish |
| 70–79 | Acceptable | Targeted fixes before publish |
| 60–69 | Below standard | Significant rework |
| < 60 | Rewrite | Restart from outline |

**Delivery rule:** ship only at 90+ with zero P0 issues.

## Priority classes

### P0 / Critical (block)

- Fabricated statistics
- Broken heading hierarchy (e.g. H1 → H3 skip)
- Material claims with no supporting source
- Missing accountability (author/org) when the site requires it
- Declared-target crawler cannot access primary content

### High

- Sections hide the conclusion or lack support
- Missing schema baseline types
- Sparse sourced evidence for a claim-heavy post
- Missing meta description / social tags
- No internal links
- Readability far outside audience band

### Medium

- Weak visual support where charts/images would clarify
- Tier 4–5 sources present
- Self-promotion > 1 mention
- Unsupported first-hand experience claims
- Inconsistent entity naming

### Low

- Mild pacing issues
- Missing alt text on decorative images
- Chart-type monotony

## Advisory style diagnostics (never score)

Report only; do not infer authorship:

- Sentence-length variance (monotony check)
- Hits on hollow phrases: "It's important to note", "In today's digital landscape",
  "Delve into", "Navigating the complexities", "Let's explore", and similar
- Em dash (U+2014) usage — project style: replace with commas/hyphens/colons/periods

## Scorecard template

```markdown
## Scorecard

| Category | Score | Notes |
|----------|------:|-------|
| Content quality | /30 | |
| SEO | /25 | |
| E-E-A-T | /15 | |
| Technical | /15 | |
| AI citation readiness | /15 | |
| **Total** | **/100** | |

**P0 issues:** none | [list]
**BLOCKING:** true | false
**Top fixes:**
1. …
```
