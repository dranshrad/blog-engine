# Write gate (domain-neutral MutationLatch)

An agent that can take irreversible action defaults to **closed**: it may read,
analyse, and draft, but not execute. Portable form of
[`../skills/paid-cast/references/mutation-latch.md`](../skills/paid-cast/references/mutation-latch.md).

Applies to anything you cannot cheaply undo: deploys, migrations, spend, sending
messages, deleting data, publishing, granting access, filing tickets externally.

## Closed (the default)

**Allowed:** read state, summarise it, draft a change pack, explain trade-offs,
prepare exact commands for a human to run.

**Forbidden:** executing the change — and, equally, *narrating* it. Never write
"I've updated…", "Done, the budget is now…", "Deployed." when nothing ran. A
false completion report is worse than a refusal, because it ends the human's
attention on the task.

Mark every draft artifact visibly: `DRAFT — NOT APPLIED`.

## Opening the gate

All of these must be true. Any one missing keeps it closed.

```text
scope:            <exact objects: files, campaigns, tables, environments>
ceilings:         <numeric limits — max spend, max rows, max blast radius>
expiry:           <date/time after which the gate re-closes>
idempotency_key:  <so a re-run does not double-apply>
rollback:         <the exact inverse step, written before the forward step>
approval:         pending | approved
```

Ceilings must be **numeric**, or the literal word `unlimited` typed by the user.
"Reasonable", "as needed", and "use your judgement" do not open a gate.

Approval must name the specific draft. Blanket pre-approval of future changes is
not approval — scope drift is the failure mode it invites.

## Change pack format

Each item, in order:

1. Target — system + object identifier
2. Before → after
3. Why — the claim, and the evidence for it
4. Ceiling check — this item's cost against the declared limit
5. Rollback — the inverse step

Ship it as a checklist a human (or their own tooling) applies. **Do not hold the
credentials.** An agent that cannot execute cannot mis-execute, and the gate
becomes a property of the architecture rather than of the prompt.

## After execution

- Report only what you can verify happened — read the state back
- Distinguish *submitted* from *confirmed*
- If verification is unavailable, say the change is unconfirmed; do not infer
  success from the absence of an error
- Re-close the gate at `expiry`, and after any completed pack
