/**
 * RoutePlex Node.js SDK — Routing Strategies
 *
 * npm install @routeplex/node
 */

import { RoutePlex } from "@routeplex/node";

const client = new RoutePlex({ apiKey: process.env.ROUTEPLEX_API_KEY });

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

// Balanced
const balanced = await client.chat("Write a haiku about coding", {
  strategy: "balanced",
});
console.log(`[balanced] ${balanced.modelUsed}: ${balanced.output}`);
