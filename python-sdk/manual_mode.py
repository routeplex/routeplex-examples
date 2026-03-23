"""
RoutePlex Python SDK — Manual Model Selection

pip install routeplex
"""

import os
from routeplex import RoutePlex

client = RoutePlex(api_key=os.environ["ROUTEPLEX_API_KEY"])

# Pick a specific model
response = client.chat(
    "Write a Python function to check if a number is prime",
    model="gpt-4o-mini",
    max_output_tokens=1024,
    temperature=0.3,
)

print(response.output)
print(f"Model: {response.model_used}")
print(f"Tokens: {response.usage.total_tokens}")
