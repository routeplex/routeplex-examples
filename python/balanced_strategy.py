"""
Balanced Strategy (Explicit Override)
=====================================
The "balanced" strategy is a fixed-weight override that optimizes the trade-off
between cost, speed, and quality using static weights.

By default (when no strategy is specified), RoutePlex uses auto-routing which
analyzes the prompt to dynamically choose the best model. Use "balanced" only
when you want deterministic fixed-weight routing instead of prompt-based analysis.

Docs: https://routeplex.com/docs/routing-modes
Usage: python balanced_strategy.py
"""

import os
import requests

API_KEY = os.environ.get("ROUTEPLEX_API_KEY")
BASE_URL = "https://api.routeplex.com"

if not API_KEY:
    print("Error: Set ROUTEPLEX_API_KEY environment variable")
    exit(1)


def ask(question: str) -> str:
    """General-purpose question answering with fixed balanced routing."""
    response = requests.post(
        f"{BASE_URL}/api/v1/chat",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "messages": [{"role": "user", "content": question}],
            "mode": "routeplex-ai",
            "strategy": "balanced",
        },
    )

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return ""

    data = response.json()
    print(f"  Model: {data['data']['model_used']} | Cost: ${data['data']['usage']['cost_usd']}")
    return data["data"]["output"]


def main():
    questions = [
        "Explain the difference between REST and GraphQL in two sentences.",
        "What are three best practices for database indexing?",
    ]

    for q in questions:
        print(f"\nQ: {q}")
        answer = ask(q)
        print(f"A: {answer}")


if __name__ == "__main__":
    main()
