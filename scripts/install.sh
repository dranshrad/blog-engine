#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MODE="${1:---all}"

install_into() {
  local dest="$1"
  mkdir -p "$dest"
  cp -R "$ROOT/skills/"* "$dest/"
  echo "Installed Clearcast skills → $dest"
}

case "$MODE" in
  --claude)
    install_into "${HOME}/.claude/skills"
    ;;
  --cursor)
    install_into "${HOME}/.cursor/skills"
    ;;
  --all|"")
    if [[ -d "${HOME}/.claude" ]] || [[ "$MODE" == "--all" ]]; then
      install_into "${HOME}/.claude/skills"
    fi
    if [[ -d "${HOME}/.cursor" ]] || [[ "$MODE" == "--all" ]]; then
      install_into "${HOME}/.cursor/skills"
    fi
    ;;
  *)
    echo "Usage: $0 [--all|--claude|--cursor]" >&2
    exit 1
    ;;
esac

echo "Done. Restart the agent client if skills do not appear."
