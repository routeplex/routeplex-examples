"""
Manual Mode — Specific Model Selection
=======================================
Choose a specific model. RoutePlex automatically handles fallbacks if the
primary model fails, ensuring 99.9%+ uptime.

Docs: https://routeplex.com/docs/routing-modes
Usage: python manual_mode.py
"""

import os
import requests

API_KEY = os.environ.get("ROUTEPLEX_API_KEY")
BASE_URL = "https://api.routeplex.com"

if not API_KEY:
    print("Error: Set ROUTEPLEX_API_KEY environment variable")
    exit(1)


def query_model(prompt: str, model: str = "claude-sonnet-4-20250514") -> str:
    """Send a prompt to a specific model with automatic fallback."""
    response = requests.post(
        f"{BASE_URL}/api/v1/chat",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "messages": [{"role": "user", "content": prompt}],
            "mode": "manual",
            "model": model,
            "max_output_tokens": 1024,
        },
    )

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return ""

    data = response.json()
    print(f"Requested: {model}")
    print(f"Used:      {data['data']['model_used']}")
    print(f"Cost:      ${data['data']['usage']['cost_usd']}")
    return data["data"]["output"]


def main():
    result = query_model("What are the SOLID principles in software engineering?")
    print(f"\n{result}")


if __name__ == "__main__":
    main()
