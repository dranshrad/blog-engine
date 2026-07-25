---
layout: default
title: Clearcast ecosystem and sister repositories
---

# Ecosystem

Clearcast (MIT) is the content skill suite. These **related public repositories** by the same author solve adjacent problems. They are **not** bundled into Clearcast and keep their own licenses (often AGPL-3.0).

## Primary sister repos

| Repository | What it is | Pair with Clearcast |
|------------|------------|---------------------|
| [voice-notes-to-anthropic-artifacts](https://github.com/dranshrad/voice-notes-to-anthropic-artifacts) | Local-first voice notes → STT + Anthropic tools → `~/Artifacts` | Feed transcripts into `blog-engine` / `social-cast` atomize |
| [llm-cst-refactorer](https://github.com/dranshrad/llm-cst-refactorer) | Format-preserving LibCST docstring/type-hint refactorer | Structure-safe code/docs beside content ops |
| [automated-self-correction-loop](https://github.com/dranshrad/automated-self-correction-loop) | Self-healing Python run/heal harness | Parallel to Clearcast stress-test / iterate loops for code |
| [anthropic-audio-gateway](https://github.com/dranshrad/anthropic-audio-gateway) | Browser audio ↔ Anthropic Realtime WSS gateway | Complements Frame & Tone / narration workflows |

## Also adjacent

| Repository | Note |
|------------|------|
| [clearcast](https://github.com/dranshrad/clearcast) | Canonical suite (this project) |
| [blog-engine](https://github.com/dranshrad/blog-engine) | Mirror / superseded entry → use Clearcast |
| [codex-ast-mapper](https://github.com/dranshrad/codex-ast-mapper) | AST → LLM-dense XML mapper |

## License reminder

Linking ≠ relicensing. Use each repo under its LICENSE file.
