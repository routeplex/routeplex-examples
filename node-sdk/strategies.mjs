/**
 * RoutePlex Node.js SDK — Routing Modes
 *
 * RoutePlex supports two auto-routing modes:
 * 1. Prompt-based (default) — analyzes your prompt and picks the best model
 * 2. Strategy-based — you choose the priority (cost, speed, quality, balanced)
 *
 * npm install @routeplex/node
 */

import { RoutePlex } from "@routeplex/node";

const client = new RoutePlex({ apiKey: process.env.ROUTEPLEX_API_KEY });

// --- Prompt-based auto-routing (default) ---
// No strategy specified — RoutePlex analyzes your prompt to pick the best model.
// Simple prompts → fast/cheap model. Complex prompts → capable model.
const simple = await client.chat("What is 2+2?");
console.log(`[auto-simple] ${simple.modelUsed}: ${simple.output}`);

const complex = await client.chat(
  "Compare the architectural tradeoffs between microservices and monoliths for a startup with 3 engineers"
);
console.log(`[auto-complex] ${complex.modelUsed}: ${complex.output.slice(0, 80)}...`);

// --- Strategy-based routing ---
// You override auto-routing with a fixed priority.

// Cost — cheapest model
const cheap = await client.chat("Summarize: AI is transforming healthcare.", {
  strategy: "cost",
});
console.log(`[cost] ${cheap.modelUsed}: $${cheap.usage.costUsd.toFixed(6)}`);

// Speed — fastest response
const fast = await client.chat("What is 2+2?", { strategy: "speed" });
console.log(`[speed] ${fast.modelUsed}: ${fast.output}`);

// Quality — best model
const smart = await client.chat("Compare REST vs GraphQL with tradeoffs", {
  strategy: "quality",
});
console.log(`[quality] ${smart.modelUsed}: ${smart.output.slice(0, 80)}...`);

// Balanced — cost/speed/quality tradeoff
const balanced = await client.chat("Write a haiku about coding", {
  strategy: "balanced",
});
console.log(`[balanced] ${balanced.modelUsed}: ${balanced.output}`);
