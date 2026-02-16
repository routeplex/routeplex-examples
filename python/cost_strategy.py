"""
Cost Strategy
=============
Minimize expenses for high-volume tasks like data extraction, basic Q&A,
or classification. Saves ~60% compared to always using premium models.

Docs: https://routeplex.com/docs/routing-modes
Usage: python cost_strategy.py
"""

import os
import requests

API_KEY = os.environ.get("ROUTEPLEX_API_KEY")
BASE_URL = "https://api.routeplex.com"

if not API_KEY:
    print("Error: Set ROUTEPLEX_API_KEY environment variable")
    exit(1)


def classify_text(text: str) -> str:
    """Classify text using cost-optimized routing."""
    response = requests.post(
        f"{BASE_URL}/api/v1/chat",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "messages": [
                {"role": "user", "content": f"Classify this text as positive, negative, or neutral: {text}"},
            ],
            "mode": "routeplex-ai",
            "strategy": "cost",
            "max_output_tokens": 50,
        },
    )

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return ""

    data = response.json()
    print(f"  Model: {data['data']['model_used']} | Cost: ${data['data']['usage']['cost_usd']}")
    return data["data"]["output"]


def main():
    texts = [
        "I love this product, it works perfectly!",
        "The delivery was late and the item was damaged.",
        "The package arrived on Tuesday.",
    ]

    for text in texts:
        print(f"\nText: {text}")
        result = classify_text(text)
        print(f"Classification: {result}")


if __name__ == "__main__":
    main()
