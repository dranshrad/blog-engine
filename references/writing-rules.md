# Writing Rules

## Purpose-first sections

Open important sections with the conclusion, then support it:

```markdown
## Impact of X on Y

[Clear conclusion naming the entity and practical implication.]
[Source-backed context, dates, examples — no padding to a length target.]
```

## Titles

Pattern: `[Clear Topic]: [Specific Reader-Relevant Scope]`

- Accurate, distinctive, truncation-resilient
- No clickbait, ALL CAPS, or vague promises
- Natural terminology consistent with the page

## Key Takeaways (optional)

Use when a scan-friendly summary helps. 3–5 bullets; comprehensible alone:

```markdown
> **Key Takeaways**
> - [Core finding with statistic] ([Source], year)
> - [Second insight]
> - [Actionable takeaway]
```

Alternate labels by persona: "The Bottom Line", "What You'll Learn", "At a Glance", "In Brief".

## Headings

- One H1 (title only)
- H2 for main sections; H3 for subsections
- Never skip levels
- Mix declarative, noun-phrase, and question headings when natural
- Questions only when readers phrase the task that way

## Sentences and paragraphs

- Start paragraphs with the most important sentence
- One topic per paragraph; split when competing ideas hurt comprehension
- Vary rhythm; no fixed sentence-length quota
- Prefer active voice; flag passive only when it muddies meaning

## Readability

Match audience (see quality-scoring bands). Default: roughly grade 7–8 /
Flesch 60–70. Adjust for technical or consumer contexts. Readability is an
editorial heuristic, not a ranking or citation predictor.

## Visuals

- Prefer original screenshots, diagrams, or data graphics
- Stock: capture license, creator, source URL; download locally; never hotlink arbitrary CDNs
- Hero: 1200×630 (OG) or 1920×1080
- Alt text required; lazy-load below-fold; high fetch priority on LCP/hero
- Insert visuals when they clarify, prove, or summarize — roughly every 300–500 words when appropriate
- Alternate types (image / chart / callout); avoid consecutive duplicates of the same type

## Citation tiers

| Tier | Sources | Policy |
|------|---------|--------|
| 1 | Peer-reviewed, government, primary datasets | Prefer |
| 2 | Major institutions, official product docs, high-quality industry reports with methods | Prefer |
| 3 | Named experts with transparent methodology | OK |
| 4 | General news without primary cite, thin blogs | Avoid |
| 5 | Content mills, affiliate spam, anonymous claims | Never |

Inline pattern (flexible):

```markdown
According to [Publisher] ([Year]), [claim] ([URL or linked title]).
```

Record methodology and limitations when they change interpretation. Dates and
retrieval notes help when the fact is time-sensitive. Do not invent studies.

**Numbers already in a cited primary source** (software versions, listed prices,
step counts) do not need redundant sourcing merely because they are numbers.

## Self-promotion

Max one brand mention, typically in author bio context. CTAs should be useful
and single-focused, placed after value delivery.

## Internal linking

- 3–10 contextual links per post when a site corpus exists
- Descriptive anchors (not "click here")
- Hub ↔ spoke: pillars link to cluster posts and vice versa
- Prefer related next-step content in the conclusion

## Meta description

Page-specific, accurate, matches visible content. Lead with the reader outcome;
include the primary topic naturally. Avoid keyword stuffing.

## Style blacklist (advisory)

Flag for rewrite; presence alone does not prove AI authorship:

delve, tapestry, multifaceted, testament, pivotal, robust, cutting-edge,
furthermore, indeed, moreover, utilize (prefer use), leverage (prefer use),
comprehensive, landscape, crucial, foster, illuminate, underscore, embark,
endeavor, facilitate, paramount, nuanced, intricate, meticulous, realm

**Em dash (U+2014):** do not use in blog body. Replace with commas, hyphens,
colons, or split sentences.

## Information gain

Prefer content competitors lack: original data, transparent first-hand tests,
unique synthesis with sources, concrete examples, decision frameworks. Labels
like "unique insights" without substance earn nothing.

## Meaningful freshness

Update when facts, pricing, screenshots, methods, or recommendations change.
Do not bump dates for appearance alone.
