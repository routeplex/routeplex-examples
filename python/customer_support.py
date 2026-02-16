"""
Customer Support Chatbot
========================
Route to cost-effective models for support queries. ~60% cost savings
vs always using premium models.

Docs: https://routeplex.com/docs/examples
Usage: python customer_support.py
"""

import os
import requests

API_KEY = os.environ.get("ROUTEPLEX_API_KEY")
BASE_URL = "https://api.routeplex.com"

if not API_KEY:
    print("Error: Set ROUTEPLEX_API_KEY environment variable")
    exit(1)


def answer_support_question(question: str) -> str:
    """Answer a customer support question using cost-optimized routing."""
    response = requests.post(
        f"{BASE_URL}/api/v1/chat",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "messages": [
                {"role": "system", "content": "You are a helpful support agent. Be concise and friendly."},
                {"role": "user", "content": question},
            ],
            "mode": "routeplex-ai",
            "strategy": "cost",
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
        "How do I reset my password?",
        "What are your business hours?",
        "Can I get a refund on my last order?",
    ]

    for q in questions:
        print(f"\nQ: {q}")
        answer = answer_support_question(q)
        print(f"A: {answer}")


if __name__ == "__main__":
    main()
