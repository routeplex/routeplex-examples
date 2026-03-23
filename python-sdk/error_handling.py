"""
RoutePlex Python SDK — Error Handling

pip install routeplex
"""

import os
from routeplex import (
    RoutePlex,
    AuthenticationError,
    RateLimitError,
    ValidationError,
    ProviderError,
    ContentPolicyError,
)

client = RoutePlex(api_key=os.environ["ROUTEPLEX_API_KEY"])

try:
    response = client.chat("Hello!")
    print(response.output)
except AuthenticationError:
    print("Invalid API key — check your ROUTEPLEX_API_KEY")
except RateLimitError as e:
    print(f"Rate limited: {e.code} — {e.message}")
except ValidationError as e:
    print(f"Bad request: {e.message}")
except ContentPolicyError:
    print("Content blocked by moderation")
except ProviderError:
    print("All upstream providers failed")
