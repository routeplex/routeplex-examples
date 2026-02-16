"""
Web Search — Real-Time Data
============================
RoutePlex automatically detects when your query needs real-time data and
searches the web before sending to the LLM. No extra setup required.

Triggers include: current events, prices, weather, scores, recent dates.

Docs: https://routeplex.com/docs/examples
Usage: python web_search.py
"""

import os
import requests

API_KEY = os.environ.get("ROUTEPLEX_API_KEY")
BASE_URL = "https://api.routeplex.com"

if not API_KEY:
    print("Error: Set ROUTEPLEX_API_KEY environment variable")
    exit(1)


def search_and_answer(question: str) -> str:
    """Ask a question that requires real-time data. Web search is automatic."""
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
    queries = [
        "What is the current price of Bitcoin today?",
        "What are the latest headlines in tech news?",
    ]

    for q in queries:
        print(f"\nQ: {q}")
        answer = search_and_answer(q)
        print(f"A: {answer}")


if __name__ == "__main__":
    main()
