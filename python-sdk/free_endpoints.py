"""
RoutePlex Python SDK — Free Endpoints (no API key charge)

pip install routeplex
"""

import os
from routeplex import RoutePlex

client = RoutePlex(api_key=os.environ["ROUTEPLEX_API_KEY"])

# Cost estimation — free
estimate = client.estimate("Write a detailed blog post about AI in healthcare")
print(f"Model: {estimate.model}")
print(f"Estimated tokens: {estimate.total_tokens}")
print(f"Estimated cost: ${estimate.estimated_cost_usd:.6f}")
print(f"Confidence: {estimate.confidence}")

print()

# Prompt enhancement — free
result = client.enhance("tell me about kubernetes")
if result.changed:
    print(f"Original: tell me about kubernetes")
    print(f"Enhanced: {result.enhanced_prompt}")
    print(f"Type: {result.query_type}")
else:
    print("Prompt was already good!")

print()

# List models — free
models = client.list_models()
for m in models:
    print(f"  {m.id:25s} {m.provider:10s} {m.tier}")
