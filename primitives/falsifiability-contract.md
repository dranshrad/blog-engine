# Falsifiability contract (domain-neutral PROBE)

Every recommendation carries five fields. Missing any one, it is incomplete and
must not ship as final. Portable form of the PROBE contract in
[`../skills/site-signal/SKILL.md`](../skills/site-signal/SKILL.md).

| Field | Question it answers |
|-------|--------------------|
| **Proof** | What did I actually observe? A quote, a measurement, a log line, a diff — not an impression |
| **Relies-on** | What must be true or fixed first? Dependencies, ordering, assumptions |
| **Overturn** | **How would we know this was wrong?** The falsifier |
| **Beacon** | What leading indicator tells us it is working, before the outcome lands? |
| **Effort** | `now` / `week` / `month` / `backlog` |

## Why Overturn is the load-bearing field

The other four make a recommendation legible. Overturn makes it *checkable*.
Without it you cannot distinguish a good call from a lucky one, because there is
no state of the world that would have counted as failure. Recommendations
without falsifiers accumulate silently: nothing ever disproves them, so nothing
is ever retired.

If you cannot write the Overturn field, you do not have a recommendation — you
have a preference. Say so, or gather evidence until you do.

## Template

```markdown
### R1 — <one-line recommendation>

- **Proof:** <observed fact, quoted or measured>
- **Relies-on:** <dependency, or "nothing">
- **Overturn:** <the observation that would show this failed>
- **Beacon:** <leading indicator + where to read it>
- **Effort:** now | week | month | backlog
```

## Beyond SEO

The contract is domain-free. Useful for:

| Context | Proof | Overturn |
|---------|-------|----------|
| Code review | The offending line, quoted | The input that would prove the bug real, or prove it unreachable |
| Model eval | The failing cases, counted | A held-out slice where the gap disappears |
| Incident postmortem | Log/metric excerpt | The alternative cause that would explain the same signal |
| Infra proposal | Current measured cost or latency | The load profile under which this change makes it worse |
| Clinical reasoning | The finding on the study | The feature that, if present, breaks this diagnosis |

## Ordering rule

Sort by dependency, not by severity. A `now` item that relies on an unshipped
`week` item is not actually a `now` item. Build the graph first, then rank —
otherwise the list reads as urgent while being unexecutable.
