#!/usr/bin/env bash
# Basic cURL Example
#
# Make a simple RoutePlex API call from the command line.
#
# Docs: https://routeplex.com/docs/getting-started
# Usage: chmod +x basic.sh && ./basic.sh

set -euo pipefail

if [ -z "${ROUTEPLEX_API_KEY:-}" ]; then
  echo "Error: Set ROUTEPLEX_API_KEY environment variable"
  echo "  export ROUTEPLEX_API_KEY='your-api-key-here'"
  exit 1
fi

echo "Making request to RoutePlex API..."
echo

curl -s https://api.routeplex.com/api/v1/chat \
  -H "Authorization: Bearer $ROUTEPLEX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "Hello! What can you help me with?"}],
    "mode": "routeplex-ai"
  }' | python3 -m json.tool  # or pipe to: jq .
