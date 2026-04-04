#!/usr/bin/env bash
# Streaming cURL Example
#
# Stream a RoutePlex response using Server-Sent Events.
# The --no-buffer flag ensures chunks print as they arrive.
#
# Docs: https://routeplex.com/docs/streaming
# Usage: chmod +x streaming.sh && ./streaming.sh

set -euo pipefail

if [ -z "${ROUTEPLEX_API_KEY:-}" ]; then
  echo "Error: Set ROUTEPLEX_API_KEY environment variable"
  echo "  export ROUTEPLEX_API_KEY='your-api-key-here'"
  exit 1
fi

echo "Streaming response from RoutePlex API..."
echo

curl --no-buffer -s https://api.routeplex.com/api/v1/chat \
  -H "Authorization: Bearer $ROUTEPLEX_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "What is streaming and why is it useful?"}],
    "mode": "routeplex-ai",
    "stream": true,
    "stream_mode": "buffered"
  }'
