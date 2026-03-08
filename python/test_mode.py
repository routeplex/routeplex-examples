"""
Test Mode
=========
Force default-tier models only during development and CI.
Prevents auto-routing from selecting premium models,
keeping costs predictable while you build and test.

Note: test_mode only affects routeplex-ai auto-routing.
In manual mode you pick the model explicitly, so test_mode has no effect.

Docs: https://routeplex.com/docs/examples#test-mode
Usage: python test_mode.py
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
    # ── Test mode via native API ─────────────────────────────────────────────
    # Safe for CI pipelines — will never route to premium models
    response = requests.post(
        f"{BASE_URL}/api/v1/chat",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "messages": [{"role": "user", "content": "Hello! Just testing."}],
            "mode": "routeplex-ai",
            "strategy": "balanced",
            "test_mode": True,
        },
    )

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        exit(1)

    data = response.json()
    print("Response:", data["data"]["output"])
    print(f"Model used: {data['data']['model_used']}  (default-tier only)")
    print(f"Cost: ${data['data']['usage']['cost_usd']}")

    # ── Test mode via OpenAI SDK ─────────────────────────────────────────────
    # Pass the X-RoutePlex-Test-Mode header when using the OpenAI SDK.
    try:
        from openai import OpenAI

        client = OpenAI(
            api_key=API_KEY,
            base_url=f"{BASE_URL}/v1",
        )

        sdk_response = client.chat.completions.create(
            model="routeplex-ai",
            messages=[{"role": "user", "content": "What is 2 + 2?"}],
            extra_headers={
                "X-RoutePlex-Strategy": "speed",
                "X-RoutePlex-Test-Mode": "true",
            },
        )

        print(f"\nOpenAI SDK response: {sdk_response.choices[0].message.content}")
        print(f"Model: {sdk_response.model}  (default-tier only)")
    except ImportError:
        print("\nSkipping OpenAI SDK example (pip install openai)")


if __name__ == "__main__":
    main()
