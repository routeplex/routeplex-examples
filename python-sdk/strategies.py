"""
RoutePlex Python SDK — Routing Modes

RoutePlex supports two auto-routing modes:
1. Prompt-based (default) — analyzes your prompt and picks the best model
2. Strategy-based — you choose the priority (cost, speed, quality, balanced)

pip install routeplex
"""

import os
from routeplex import RoutePlex

client = RoutePlex(api_key=os.environ["ROUTEPLEX_API_KEY"])

# --- Prompt-based auto-routing (default) ---
# No strategy specified — RoutePlex analyzes your prompt to pick the best model.
# Simple prompts → fast/cheap model. Complex prompts → capable model.
simple = client.chat("What is 2+2?")
print(f"[auto-simple] {simple.model_used}: {simple.output}")

complex_q = client.chat("Compare the architectural tradeoffs between microservices and monoliths for a startup with 3 engineers")
print(f"[auto-complex] {complex_q.model_used}: {complex_q.output[:80]}...")

# --- Strategy-based routing ---
# You override auto-routing with a fixed priority.

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
