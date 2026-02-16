"""
Quality Strategy
================
Best output for complex reasoning, code generation, detailed analysis,
or creative writing. Routes to the most capable models.

Docs: https://routeplex.com/docs/routing-modes
Usage: python quality_strategy.py
"""

import os
import requests

API_KEY = os.environ.get("ROUTEPLEX_API_KEY")
BASE_URL = "https://api.routeplex.com"

if not API_KEY:
    print("Error: Set ROUTEPLEX_API_KEY environment variable")
    exit(1)


def generate_code(description: str) -> str:
    """Generate code using quality-optimized routing."""
    response = requests.post(
        f"{BASE_URL}/api/v1/chat",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "messages": [
                {"role": "system", "content": "You are an expert programmer. Write clean, well-documented code."},
                {"role": "user", "content": f"Implement: {description}"},
            ],
            "mode": "routeplex-ai",
            "strategy": "quality",
            "max_output_tokens": 2048,
            "temperature": 0.3,
        },
    )

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return ""

    data = response.json()
    print(f"Model: {data['data']['model_used']} | Cost: ${data['data']['usage']['cost_usd']}")
    return data["data"]["output"]


def main():
    result = generate_code("A Python function that finds the longest common subsequence of two strings.")
    print(f"\n{result}")


if __name__ == "__main__":
    main()
