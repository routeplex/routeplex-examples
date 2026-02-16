"""
Speed Strategy
==============
Minimize latency for real-time applications like chatbots, live support,
or interactive tools. Prioritizes the fastest responding model.

Docs: https://routeplex.com/docs/routing-modes
Usage: python speed_strategy.py
"""

import os
import time
import requests

API_KEY = os.environ.get("ROUTEPLEX_API_KEY")
BASE_URL = "https://api.routeplex.com"

if not API_KEY:
    print("Error: Set ROUTEPLEX_API_KEY environment variable")
    exit(1)


def fast_response(message: str) -> str:
    """Get the fastest possible response."""
    start = time.time()

    response = requests.post(
        f"{BASE_URL}/api/v1/chat",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "messages": [{"role": "user", "content": message}],
            "mode": "routeplex-ai",
            "strategy": "speed",
            "max_output_tokens": 256,
        },
    )

    elapsed = time.time() - start

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return ""

    data = response.json()
    print(f"  Model: {data['data']['model_used']} | Time: {elapsed:.2f}s | Cost: ${data['data']['usage']['cost_usd']}")
    return data["data"]["output"]


def main():
    print("Speed strategy — fastest model selection\n")
    result = fast_response("What is the capital of France?")
    print(f"\nResponse: {result}")


if __name__ == "__main__":
    main()
