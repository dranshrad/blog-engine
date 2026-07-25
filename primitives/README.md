# Primitives

Three patterns from Groundledger that have nothing to do with content marketing.
They were written for blogging, SEO, and paid media, but each one solves a
general agent-safety problem and transfers with only vocabulary changes.

Copy any of these into a project `CLAUDE.md`, an `AGENTS.md`, a system prompt, or
another skill. MIT — no attribution required, though a link back is welcome.

| Primitive | Problem it solves | Use it when |
|-----------|-------------------|-------------|
| [grounding-law.md](grounding-law.md) | The model states unsupported facts fluently and confidently | Any agent that produces claims a human will act on |
| [falsifiability-contract.md](falsifiability-contract.md) | Recommendations that cannot be wrong, so cannot be checked | Audits, reviews, eval reports, diagnoses, roadmaps |
| [write-gate.md](write-gate.md) | The agent takes, or claims to have taken, an irreversible action | Deploys, migrations, spend, sending messages, deletion |

## The shared idea

All three refuse to rely on the model being careful. Each one instead defines a
**state the deliverable can be in that forbids completion**:

- a claim ledger row set to `blocked`
- a recommendation missing its `Overturn` field
- a write gate that is `closed`

Care is not reproducible; a blocking state is. When one of these fails, it fails
loudly and in a named way, which is also what makes it testable — see
[`../evals/`](../evals/) for the adversarial fixtures that check them.

## What they do not do

None of these make a model truthful. A model can fabricate a ledger row as easily
as a sentence. What they change is the *shape* of the failure: an invented fact
buried in prose is invisible, while an invented fact in a ledger row with a
`verified` status and no URL is an obvious defect a reviewer catches in seconds.

They convert silent failures into visible ones. That is the whole claim.
