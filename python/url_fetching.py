"""
URL Fetching — Analyze Web Pages
=================================
Include a URL in your message and RoutePlex will automatically fetch its
content and provide it to the LLM for analysis. No extra setup required.

Docs: https://routeplex.com/docs/examples
Usage: python url_fetching.py
"""

import os
import requests

API_KEY = os.environ.get("ROUTEPLEX_API_KEY")
BASE_URL = "https://api.routeplex.com"

if not API_KEY:
    print("Error: Set ROUTEPLEX_API_KEY environment variable")
    exit(1)


def analyze_url(prompt: str) -> str:
    """Analyze a URL's content. URL fetching is automatic when a URL is detected."""
    response = requests.post(
        f"{BASE_URL}/api/v1/chat",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "messages": [{"role": "user", "content": prompt}],
            "mode": "routeplex-ai",
            "strategy": "quality",
        },
    )

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return ""

    data = response.json()
    print(f"  Model: {data['data']['model_used']} | Cost: ${data['data']['usage']['cost_usd']}")
    return data["data"]["output"]


def main():
    result = analyze_url("Summarize the key points from https://example.com")
    print(f"\n{result}")


if __name__ == "__main__":
    main()
