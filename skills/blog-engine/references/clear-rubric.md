# CLEAR Rubric (100 points)

Original scoring model for this skill. Not a Google ranking factor.

## C — Claim integrity (25)

| Check | Pts | Pass |
|-------|----:|------|
| Material claims ledgered | 8 | Every non-obvious fact appears in the claim ledger |
| Verification quality | 7 | Primary/official sources preferred; methods noted when material |
| No fabrication | 5 | Zero invented stats, quotes, studies, or “internal” numbers |
| Source diversity | 3 | Source Diversity Index ≥ 0.6 (see evidence.md) |
| Uncertainty labeled | 2 | Soft claims marked; limits stated where needed |

## L — Lexical clarity (15)

| Check | Pts | Pass |
|-------|----:|------|
| Audience-matched density | 5 | Jargon earned; definitions near first use |
| Scannable rhythm | 4 | Short and long sentences mixed; no monotonous cadence |
| Concrete language | 3 | Prefer specifics over abstractions |
| Noise control | 3 | No hype fillers, fake urgency, or throat-clearing |

## E — Entity coherence (15)

| Check | Pts | Pass |
|-------|----:|------|
| Single primary entity | 5 | One main topic identity per URL |
| Stable naming | 4 | Same canonical name throughout |
| Title–body match | 3 | Title accurately describes the job delivered |
| Disambiguation | 3 | Competing meanings clarified early |

## A — Answer extractability (25)

| Check | Pts | Pass |
|-------|----:|------|
| Declarative section opens | 7 | Major sections start with a direct answer sentence |
| Standalone passages | 7 | Key answers make sense out of context |
| Structured comparisons | 4 | Tables/lists only when they clarify real choices |
| Q-test coverage | 4 | Adversarial Q-test 5/5 with quoted passages |
| Machine-visible structure | 3 | Clean headings; schema only when it mirrors visible content |

## R — Reader-job fit (20)

| Check | Pts | Pass |
|-------|----:|------|
| JTBD stated and fulfilled | 7 | Opening job matches closing outcome |
| Intent purity | 5 | One primary job per URL |
| Decision usefulness | 4 | Reader can act or decide after reading |
| Next step clarity | 4 | Single relevant CTA or next URL |

## Bands

| Score | Status |
|------:|--------|
| 85–100 | Ship (if stress tests pass) |
| 70–84 | Revise under diff contract |
| < 70 | Rebuild from journey map |

## Blocking failures (any one blocks ship)

- Fabricated or unsourced material claim
- Intent impurity (multi-job URL)
- Adversarial Q-test < 5/5
- YMYL intensifier failure
- Heading hierarchy skip that breaks reading order
- Empty claim ledger on a claim-heavy post

## Scorecard template

```markdown
## CLEAR scorecard

| Dimension | Score | Notes |
|-----------|------:|-------|
| C Claim integrity | /25 | |
| L Lexical clarity | /15 | |
| E Entity coherence | /15 | |
| A Answer extractability | /25 | |
| R Reader-job fit | /20 | |
| **Total** | **/100** | |

**Stress tests:** ledger / contradictions / Q-test / YMYL / a11y
**Ship:** yes | no
```
