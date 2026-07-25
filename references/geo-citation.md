# AI Citation Readiness (GEO / AEO)

GEO and AEO are shorthand for AI citation readiness. For Google Search, AI
Overviews / AI Mode optimization is SEO — not a separate discipline requiring
special markup or `llms.txt`.

The score below is an internal heuristic, not a calibrated probability of citation.

## Surfaces to consider

Most blog posts should target:

1. Owned site (organic ranking)
2. SERP including AI Overviews
3. AI assistants (ChatGPT, Perplexity, Claude, Gemini, Copilot, etc.)

Optional: communities/video echoes via repurposing. Local pack is out of scope
for pure blog content.

## Audit steps

### 1. Evidence-backed citability (4 pts)

Per important section:

- Context-independent if extracted
- Claim + evidence + attribution
- Answers a question without requiring adjacent sections

Scoring: 80%+ sections → 4; 60–79% → 3; 40–59% → 2; 20–39% → 1; else 0.

### 2. Purpose fit (3 pts)

- Intro names topic, audience, reader task
- Sections state the point without throat-clearing
- Headings/format match intent (questions/FAQs/tables only when they fit)

### 3. Entity clarity (3 pts)

- One unambiguous primary topic
- Consistent naming (avoid confusing synonym churn)
- Clear intro topic statement
- Title matches content focus

### 4. Extraction structure (3 pts)

Look for useful presence of:

- Standalone summary when helpful
- Comparison tables with headers
- Ordered lists for processes
- Definition-style term patterns
- Evidence-backed reusable explanations

4–5 elements → 3; 3 → 2; 1–2 → 1; else 0.

### 5. Crawler accessibility (2 pts)

- Primary content in rendered DOM for the target crawler
- Google: normal crawl/index; no special GEO file required
- Non-Google bots: robots.txt policy matches declared goals (GPTBot, ClaudeBot, PerplexityBot, etc.)
- Schema in rendered DOM matches visible content

## Practices that help readers (and often extractors)

| Practice | Notes |
|----------|-------|
| Cite authoritative sources | Traceability when the source supports the claim |
| Supported statistics | Include methodology/limits when material |
| Accurate quotations | Preserve expert context |
| Self-contained sections | No mandated chunk length from Google |
| Comparison tables | Use when comparisons are the task |
| Meaningful updates | Refresh facts, not just dates |

## Practices that do not earn special Google credit

- FAQPage purely for rich results / score gaming
- Keyword stuffing
- Separate “GEO markup” folklore as a Google requirement
- Date bumps without substance

## Evidence discipline for benchmarks

Only quote numeric AI-citation benchmarks when you can cite URL, publisher,
methodology, sample size, engine/version, query class, and retrieval date.
Otherwise label directional or omit the number.

## Report template

```markdown
## GEO audit

**AI Citation Readiness:** /15 (part of the 100-point system)

| Dimension | Score | Findings |
|-----------|------:|----------|
| Citability | /4 | |
| Purpose fit | /3 | |
| Entity clarity | /3 | |
| Structure | /3 | |
| Crawler access | /2 | |

**Highest-leverage fixes:**
1. …
```
