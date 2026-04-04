"""
Streaming — OpenAI SDK Compatible
==================================
Stream responses using the OpenAI Python SDK with RoutePlex.
Just change the base URL — streaming works exactly like OpenAI.

Docs: https://routeplex.com/docs/streaming
Usage: pip install openai && python streaming_openai_sdk.py
"""

import os
from openai import OpenAI

API_KEY = os.environ.get("ROUTEPLEX_API_KEY")

if not API_KEY:
    print("Error: Set ROUTEPLEX_API_KEY environment variable")
    exit(1)

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.routeplex.com/v1",
)


def main():
    # stream=True returns an iterator of ChatCompletionChunk objects
    stream = client.chat.completions.create(
        model="routeplex-ai",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write a haiku about streaming data."},
        ],
        stream=True,
    )

    print("Streaming response:\n")
    for chunk in stream:
        delta = chunk.choices[0].delta
        if delta.content:
            print(delta.content, end="", flush=True)

        # Final chunk includes usage stats
        if chunk.usage:
            print(f"\n\nTokens: {chunk.usage.prompt_tokens} in / {chunk.usage.completion_tokens} out")

    print()


if __name__ == "__main__":
    main()
