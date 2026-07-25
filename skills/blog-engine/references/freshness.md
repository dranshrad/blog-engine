# Freshness Drift

Decide refresh vs consolidate vs prune from performance or staleness signals.

## Inputs

- Current vs prior traffic/query export (if any)
- `dateModified` vs material change log
- Claim ledger rows that may have expired

## Classification

| Label | When | Action |
|-------|------|--------|
| Refresh | Still the right job; facts/UI stale | Update evidence + substance; then date |
| Consolidate | Overlaps another URL (collision) | Merge jobs; redirect plan |
| Prune | No demand / superseded | Unpublish or noindex plan |
| Hold | Stable and true | No date bump |

## Output

```markdown
## Freshness drift
| URL / title | Signal | Label | Triggers | Owner |
|-------------|--------|-------|----------|-------|
```

Never change dates without substantive edits.
