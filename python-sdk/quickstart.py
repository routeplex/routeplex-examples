"""
RoutePlex Python SDK — Quickstart

pip install routeplex
"""

import os
from routeplex import RoutePlex

client = RoutePlex(api_key=os.environ["ROUTEPLEX_API_KEY"])

# One-liner
response = client.chat("What is Python?")
print(response.output)
print(f"Model: {response.model_used}")
print(f"Cost: ${response.usage.cost_usd:.6f}")
