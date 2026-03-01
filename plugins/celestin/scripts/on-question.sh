#!/bin/bash
INPUT=$(cat)
PROMPT=$(echo "$INPUT" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('prompt',''))" 2>/dev/null || echo "")

if echo "$PROMPT" | grep -qiE "surf|golf|foot|australia|vietnam|sri lanka|costa rica|sea|mer"; then
  printf '🌊  Celestin'\''s eyes just lit up...\n'
elif echo "$PROMPT" | grep -qiE "ci.?cd|pipeline|github action|workflow|test|deploy"; then
  printf '⚙️   Getting into the CI zone...\n'
elif echo "$PROMPT" | grep -qiE "typescript|node|javascript|react|vue"; then
  printf '🟦  TypeScript mode on...\n'
elif echo "$PROMPT" | grep -qiE "why anthropic|motivation|join|apply"; then
  printf '🚀  This one matters to him...\n'
fi
