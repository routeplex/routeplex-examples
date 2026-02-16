"""
OpenAI SDK Compatible
=====================
Use the OpenAI Python SDK with RoutePlex as a drop-in replacement.
Just change the base URL and API key — everything else works the same.

Docs: https://routeplex.com/docs/openai-compatibility
Usage: pip install openai && python openai_compatible.py
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
    # Auto-routing with balanced strategy
    # Strategy is passed via the X-RoutePlex-Strategy header
    response = client.chat.completions.create(
        model="routeplex-ai",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What are three tips for writing clean code?"},
        ],
        extra_headers={"X-RoutePlex-Strategy": "balanced"},
    )

    print("Response:", response.choices[0].message.content)
    print(f"Model: {response.model}")
    if response.usage:
        print(f"Tokens: {response.usage.prompt_tokens} in / {response.usage.completion_tokens} out")


if __name__ == "__main__":
    main()
