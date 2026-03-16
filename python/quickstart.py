"""
RoutePlex Quickstart
====================
Make your first API call to RoutePlex.

Docs: https://routeplex.com/docs/getting-started
Usage: python quickstart.py
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
    response = requests.post(
        f"{BASE_URL}/api/v1/chat",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "messages": [{"role": "user", "content": "Hello! What can you help me with?"}],
            "mode": "routeplex-ai",
            # No strategy needed — RoutePlex auto-routes based on prompt analysis
        },
    )

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        exit(1)

    data = response.json()
    print("Response:", data["data"]["output"])
    print(f"Model used: {data['data']['model_used']}")
    print(f"Cost: ${data['data']['usage']['cost_usd']}")


if __name__ == "__main__":
    main()
