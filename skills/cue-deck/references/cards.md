# Cue Cards (original)

## Cue — O-jobs
**When:** Demand language is unclear.  
**Inputs:** Product/ICP notes.  
**Prompt:**
> List 12 jobs-to-be-done as “When… wants… so they can…”. Cluster into hubs. Flag YMYL. No fake search volumes.
**Output:** JTBD list + hub candidates.  
**Risks:** Keyword stuffing disguised as jobs.  
**Next skill:** orbit-discovery

## Cue — R-echo
**When:** Brand proof is weak off-site.  
**Inputs:** Brand name, markets.  
**Prompt:**
> Build an Echo Map of where facts are already corroborated. List top 3 gaps and the smallest Reinforce action this week.
**Output:** Echo Map table.  
**Risks:** Invented review quotes.  
**Next skill:** orbit-discovery

## Cue — B-brief
**When:** Ready to build an owned asset.  
**Inputs:** Surface Bet Card.  
**Prompt:**
> Write an asset brief: JTBD, spine, evidence needs, KPI, kill criteria. Do not draft the article yet.
**Output:** Brief markdown.  
**Risks:** Skipping evidence plan.  
**Next skill:** blog-engine

## Cue — I-kpi
**When:** Traffic exists but business impact is fuzzy.  
**Inputs:** Page URL + goal.  
**Prompt:**
> Define one primary measurement event and two guardrail metrics. Map page sections to the event.
**Output:** Instrumentation plan.  
**Risks:** Vanity metrics only.  
**Next skill:** orbit-discovery

## Cue — T-retro
**When:** Ending a content cycle.  
**Inputs:** What shipped + results.  
**Prompt:**
> Classify assets: double / fix / kill. List update triggers. Transmit 3 learnings into next Horizon Brief.
**Output:** Retro + triggers.  
**Risks:** Date-bumping without substance.  
**Next skill:** orbit-discovery

## Cue — C-draft
**When:** Starting a Groundledger article.  
**Inputs:** JTBD + spine.  
**Prompt:**
> Draft under CLEAR rules. Emit claim ledger, Q-test, residual risks, scorecard. Invent zero statistics.
**Output:** Full draft package.  
**Risks:** Shipping under 85.  
**Next skill:** blog-engine

## Cue — C-verify
**When:** Claims look soft.  
**Inputs:** Draft path.  
**Prompt:**
> Run Claim Probe+: status, confidence, echo flags, fixes. Block fabricated numbers.
**Output:** Updated ledger.  
**Risks:** Accepting weak blogs as primary.  
**Next skill:** blog-engine

## Cue — C-cite
**When:** AI-answer visibility matters.  
**Inputs:** Draft path.  
**Prompt:**
> Run Cite Surface Audit; list citeable passages; patch plan ≤5 edits.
**Output:** Audit + patches.  
**Risks:** Schema folklore.  
**Next skill:** blog-engine

## Cue — S-atom
**When:** One long-form piece must feed a week.  
**Inputs:** Article/transcript.  
**Prompt:**
> Atomize into 3–7 atoms; build staggered cast pack; no invented stats in hooks.
**Output:** Cast pack.  
**Risks:** Same-hour cross-post spam.  
**Next skill:** social-cast

## Cue — S-readout
**When:** Metrics were pasted.  
**Inputs:** CSV or table.  
**Prompt:**
> Pulse Readout Deep: reach vs actions, hypotheses, one falsifiable experiment.
**Output:** Readout + experiment.  
**Risks:** “Post more” as only advice.  
**Next skill:** social-cast

## Cue — E-spark
**When:** Draft needs multi-pass polish.  
**Inputs:** Draft path + locale.  
**Prompt:**
> Run SPARK with voice lock and fact freeze. Write numbered intermediates.
**Output:** final.md + pass-log.  
**Risks:** Voice flattening.  
**Next skill:** editorial-pass

## Cue — D-ship
**When:** Ready for CMS/handoff.  
**Inputs:** Final draft path.  
**Prompt:**
> Run Ship Gate + remind Release Latch fields. List missing handoff items only.
**Output:** Gate checklist.  
**Risks:** Calling draft “final” while latch open.  
**Next skill:** studio-desk

## Cue — P-audit
**When:** User wants a site SEO audit.  
**Inputs:** URL(s) + optional GSC/export.  
**Prompt:**
> Run site-signal audit: Health Dial with coverage %, industry confirm, PROBE items only (Proof Relies-on Overturn Beacon Effort). No invented rankings or traffic.
**Output:** Dial + PROBE plan + watchlist.  
**Risks:** Scoring axes without evidence.  
**Next skill:** site-signal

## Cue — P-fit
**When:** Page type may fight the SERP job.  
**Inputs:** URL + query cluster (user-supplied).  
**Prompt:**
> Run page-fit: classify target type vs expected SERP shapes; gap scores; top PROBE fixes. Do not invent rank positions.
**Output:** Fit gaps + handoffs.  
**Risks:** Guessing SERP without export or stated assumptions.  
**Next skill:** site-signal

## Cue — A-snap
**When:** Paid account review without changing spend.  
**Inputs:** Exports / UI notes.  
**Prompt:**
> Paid-cast audit observe-only: claim + evidence + confidence per finding; unit-econ gaps listed as assumptions; no platform mutations.
**Output:** Snapshot + advise list.  
**Risks:** Invented ROAS/benchmarks.  
**Next skill:** paid-cast

## Cue — A-latch
**When:** User wants a draft change pack.  
**Inputs:** Scope + ceilings.  
**Prompt:**
> Open MutationLatch checklist only: scope, ceilings, idempotency, rollback, mark DRAFT — NOT APPLIED until user says approve on the exact pack.
**Output:** MEDIA_LATCH fields + change pack.  
**Risks:** Claiming live changes applied.  
**Next skill:** paid-cast
