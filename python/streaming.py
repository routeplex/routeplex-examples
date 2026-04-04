"""
Streaming — Native API
======================
Stream responses in real time using Server-Sent Events (SSE).
RoutePlex supports two streaming modes:
  - "buffered" (default): Smooth, sentence-aware chunks (~100ms pacing)
  - "realtime": Minimal buffering (~10ms), character-level delivery

Docs: https://routeplex.com/docs/streaming
Usage: python streaming.py
"""

import os
import json
import requests

API_KEY = os.environ.get("ROUTEPLEX_API_KEY")
BASE_URL = "https://api.routeplex.com"

if not API_KEY:
    print("Error: Set ROUTEPLEX_API_KEY environment variable")
    print("  export ROUTEPLEX_API_KEY='your-api-key-here'")
    exit(1)


def stream_chat(message: str, stream_mode: str = "buffered"):
    """Stream a chat response using the RoutePlex native SSE format."""
    response = requests.post(
        f"{BASE_URL}/api/v1/chat",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Accept": "text/event-stream",
        },
        json={
            "messages": [{"role": "user", "content": message}],
            "mode": "routeplex-ai",
            "stream": True,
            "stream_mode": stream_mode,
        },
        stream=True,
    )

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return

    model_used = None
    for line in response.iter_lines(decode_unicode=True):
        if not line or not line.startswith("data: "):
            continue

        payload = line[6:]  # strip "data: "

        if payload == "[DONE]":
            break

        event = json.loads(payload)

        if event["type"] == "start":
            print(f"[Stream started — request_id: {event['request_id']}]")

        elif event["type"] == "delta":
            print(event["content"], end="", flush=True)

        elif event["type"] == "done":
            model_used = event["model_used"]
            usage = event["usage"]
            print(f"\n\n--- Stream complete ---")
            print(f"Model: {model_used} ({event['provider']})")
            print(f"Tokens: {usage['input_tokens']} in / {usage['output_tokens']} out")
            print(f"Latency: {event['latency_ms']}ms")


def main():
    print("=== Buffered mode (smooth, sentence-aware chunks) ===\n")
    stream_chat("Explain how HTTP streaming works in 3 sentences.")

    print("\n\n=== Realtime mode (minimal buffering) ===\n")
    stream_chat("What is the capital of France?", stream_mode="realtime")


if __name__ == "__main__":
    main()
