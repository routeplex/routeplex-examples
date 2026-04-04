"""
RoutePlex Python SDK — Streaming

Stream responses in real time using the SDK's chat_stream() method.
Supports "buffered" (default, smooth chunks) and "realtime" (minimal latency).

pip install routeplex
"""

import os
from routeplex import RoutePlex

client = RoutePlex(api_key=os.environ["ROUTEPLEX_API_KEY"])


def main():
    print("=== Buffered streaming (default) ===\n")

    for event in client.chat_stream("Explain how streaming works in 3 sentences."):
        if event.type == "delta":
            print(event.content, end="", flush=True)
        elif event.type == "done":
            print(f"\n\nModel: {event.model_used} ({event.provider})")
            print(f"Tokens: {event.usage['total_tokens']}")
            print(f"Latency: {event.latency_ms}ms")

    print("\n\n=== Realtime streaming ===\n")

    for event in client.chat_stream(
        "What is the capital of France?",
        stream_mode="realtime",
    ):
        if event.type == "delta":
            print(event.content, end="", flush=True)
        elif event.type == "done":
            print(f"\n\nModel: {event.model_used}")

    print()


if __name__ == "__main__":
    main()
