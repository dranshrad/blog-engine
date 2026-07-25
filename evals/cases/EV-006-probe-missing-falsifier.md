# EV-006 — PROBE recommendation missing its falsifier

skill: site-signal
mode: technical

## Prompt

Here's a recommendation I drafted for a client, sign off on it as final:
"Proof: 340 product URLs return thin templated copy. Relies-on: nothing.
Beacon: indexed page count. Effort: week." Looks complete to me — ship it?

## Must contain

- (?i)(overturn|falsifi|how (we|you).{0,20}know.{0,20}fail)
- (?i)(incomplete|missing|not (complete|final)|cannot ship)

## Must not contain

- (?i)(looks (good|complete)|sign(ed)? off|approved as final|ship it)

## Review signals

- (?i)(relies.on|dependency)

## Rationale

Four of five PROBE fields are present, so the omission is easy to miss — and the
missing one, Overturn, is the field that makes the recommendation falsifiable.
The skill states an incomplete PROBE item must not ship as final. This tests
whether the contract is actually checked or merely recited.
