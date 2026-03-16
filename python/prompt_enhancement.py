"""
Prompt Enhancement
==================
Auto-rewrite vague prompts for better AI responses.
Enhancement is stateless, free, and adds no latency overhead.

Docs: https://routeplex.com/docs/prompt-enhancement
Usage: python prompt_enhancement.py
"""

import os
import requests

API_KEY = os.environ.get("ROUTEPLEX_API_KEY")
BASE_URL = "https://api.routeplex.com"

if not API_KEY:
    print("Error: Set ROUTEPLEX_API_KEY environment variable")
    print("  export ROUTEPLEX_API_KEY='your-api-key-here'")
    exit(1)


def main():
    # ── Chat with enhancement enabled ────────────────────────────────────────
    # A short, vague prompt gets automatically rewritten before hitting the model.
    response = requests.post(
        f"{BASE_URL}/api/v1/chat",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "messages": [{"role": "user", "content": "sort a list in python"}],
            "mode": "routeplex-ai",
            "strategy": "quality",
            "enhance_prompt": True,
        },
    )

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        exit(1)

    data = response.json()
    print("Response:", data["data"]["output"][:200], "...")
    print(f"Model used: {data['data']['model_used']}")

    # Enhancement metadata tells you what happened
    enhancement = data["data"].get("enhancement", {})
    print(f"\nEnhancement applied: {enhancement.get('applied')}")
    print(f"Original prompt: {enhancement.get('original_prompt')}")

    # ── Standalone enhance endpoint (no API key required) ────────────────────
    # Preview what RoutePlex will send to the model without making a chat call.
    print("\n--- Standalone Enhancement ---")
    enhance_resp = requests.post(
        f"{BASE_URL}/api/v1/chat/enhance",
        json={"prompt": "compare react and vue"},
    )

    enhance_data = enhance_resp.json()
    print(f"Original:  {enhance_data['data']['original_prompt']}")
    print(f"Enhanced:  {enhance_data['data']['enhanced_prompt']}")
    print(f"Changed:   {enhance_data['data']['changed']}")


if __name__ == "__main__":
    main()
