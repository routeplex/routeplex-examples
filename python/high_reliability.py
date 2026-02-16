"""
High-Reliability Production API
================================
RoutePlex automatically handles provider failures with built-in fallback.
Higher effective uptime compared to using a single provider directly.

Docs: https://routeplex.com/docs/examples
Usage: python high_reliability.py
"""

import os
import requests

API_KEY = os.environ.get("ROUTEPLEX_API_KEY")
BASE_URL = "https://api.routeplex.com"

if not API_KEY:
    print("Error: Set ROUTEPLEX_API_KEY environment variable")
    exit(1)


def critical_api_call(prompt: str) -> str:
    """Make a critical API call with automatic failover.

    Even if the primary model is temporarily unavailable, RoutePlex
    will automatically route to a fallback model — no extra code needed.
    """
    response = requests.post(
        f"{BASE_URL}/api/v1/chat",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "messages": [{"role": "user", "content": prompt}],
            "mode": "manual",
            "model": "gpt-4o",
        },
    )

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return ""

    data = response.json()
    print(f"Model used: {data['data']['model_used']}")
    return data["data"]["output"]


def main():
    result = critical_api_call("Summarize the key benefits of microservices architecture.")
    print(f"\nResponse:\n{result}")


if __name__ == "__main__":
    main()
