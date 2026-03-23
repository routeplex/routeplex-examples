"""
RoutePlex Python SDK — Routing Strategies

pip install routeplex
"""

import os
from routeplex import RoutePlex

client = RoutePlex(api_key=os.environ["ROUTEPLEX_API_KEY"])

# Auto-routing (default) — RoutePlex picks the best model
auto = client.chat("Explain recursion")
print(f"[auto] {auto.model_used}: {auto.output[:80]}...")

# Cost — cheapest model
cheap = client.chat("Summarize: AI is transforming healthcare.", strategy="cost")
print(f"[cost] {cheap.model_used}: ${cheap.usage.cost_usd:.6f}")

# Speed — fastest response
fast = client.chat("What is 2+2?", strategy="speed")
print(f"[speed] {fast.model_used}: {fast.output}")

# Quality — best model
smart = client.chat("Compare REST vs GraphQL with tradeoffs", strategy="quality")
print(f"[quality] {smart.model_used}: {smart.output[:80]}...")

# Balanced — cost/speed/quality tradeoff
balanced = client.chat("Write a haiku about coding", strategy="balanced")
print(f"[balanced] {balanced.model_used}: {balanced.output}")
