# Required Artifacts

These artifacts are part of the skill’s publish contract. They do not exist as a
bundled feature set in typical blog-plugin orchestrators.

## 1. Claim ledger

Markdown table (or JSON if the user asks):

```markdown
## Claim ledger

| ID | Claim | Type | Source | URL | Date | Status | Notes |
|----|-------|------|--------|-----|------|--------|-------|
| C1 | … | statistic | Publisher | https://… | 2026 | verified | method: survey n=… |
| C2 | … | definition | Official docs | https://… | 2026 | attributed | |
| C3 | … | anecdote | Author | — | — | author-supplied | user provided |
| C4 | … | statistic | — | — | — | blocked | remove or replace |
```

Status meanings:

- `verified` — source checked; supports the claim
- `attributed` — clearly cited; not re-fetched in this session but URL given
- `author-supplied` — user attested first-hand detail
- `blocked` — must fix before ship

## 2. Adversarial Q-test

```markdown
## Adversarial Q-test

### Q1. [question an AI user might ask]
- Passage: “…”
- Extractable alone: yes | no
- Patch: …

### Q2–Q5.
…
**Result:** 5/5 | fail
```

Question design rules:

- Mix definition, how-to, comparison, risk, and “who should” prompts
- Prefer natural language over keyword fragments
- At least one question should try to trap a weak section

## 3. Residual risk register

```markdown
## Residual risks

| ID | Risk | Severity | Mitigation | Owner decision |
|----|------|----------|------------|----------------|
| R1 | Stat may age in 90 days | medium | calendar update trigger | accept | fix |
| R2 | YMYL advice could be over-read | high | add clinician disclaimer | accept | fix |
```

Ship only if every `high` risk is fixed or explicitly accepted by the user.

## 4. Diff contract (improve mode)

```markdown
## Diff contract
- KEEP: …
- CHANGE: …
- DELETE: …
- MUST NOT: invent facts; date-bump without substance
```

## 5. Competitive teardown (brief mode)

```markdown
## Teardown matrix

| Competitor URL | Job they serve | Evidence density | Gaps we can own |
|----------------|----------------|------------------|-----------------|
| … | … | low/med/high | … |

## Our angle
One sentence that competitors cannot honestly claim without our evidence.
```
