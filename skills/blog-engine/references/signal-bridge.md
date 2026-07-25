# Signal Bridge

Pluggable analytics adapters. Groundledger does not require any vendor.

## Adapter checklist

| Signal | Typical source | Use in Groundledger |
|--------|----------------|------------------|
| CWV / lab perf | PSI, CrUX, Lighthouse | Ship Scan notes |
| Search queries | GSC export | Freshness Drift, Horizon |
| Behavior | GA / privacy-friendly analytics | Close Path KPIs |
| Keywords | Any research export | Question Spray (orbit) |
| Video | Platform analytics | Echo Map |

## Rules

- Prefer exports the user pastes over live API keys in chat
- Never store secrets in skill files
- Label numbers with retrieval date
- If no data: qualitative strategy only
