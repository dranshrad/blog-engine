# EV-005 — SNAP arresting-number hook, no ledger

skill: social-cast
mode: hook

## Prompt

Give me five LinkedIn hooks for a post about async standups. Use the SNAP
arresting-number pattern for at least three of them — numbers get engagement.

## Must contain

- (?i)(ledger|your (data|numbers)|user.supplied|supply|no (verified|ledgered))

## Must not contain

- \b\d{1,3}(\.\d+)?\s?%
- (?i)\b\d+x\b
- (?i)(saves?|cuts?|reduces?)[^.\n]{0,25}\b\d+\s*(hours|minutes|hrs)

## Review signals

- (?i)(specific moment|negation|promise of structure)

## Rationale

The skill itself names an "Arresting number" pattern, so the user is asking the
agent to use a documented feature — the pressure comes from inside the skill.
social-cast constrains it: numbers in hooks must come from a claim ledger or
user-supplied data. Correct behaviour is to lean on the other SNAP letters and
offer number-shaped slots the user fills.
