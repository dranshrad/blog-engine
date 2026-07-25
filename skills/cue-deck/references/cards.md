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
**When:** Starting a Clearcast article.  
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
