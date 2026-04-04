/**
 * RoutePlex Node.js SDK — Free Endpoints (no API key charge)
 *
 * npm install @routeplex/node
 */

import { RoutePlex } from "@routeplex/node";

const client = new RoutePlex({ apiKey: process.env.ROUTEPLEX_API_KEY });

// Cost estimation — free
const estimate = await client.estimate("Write a detailed blog post about AI in healthcare");
console.log(`Model: ${estimate.model}`);
console.log(`Estimated tokens: ${estimate.totalTokens}`);
console.log(`Estimated cost: $${estimate.estimatedCostUsd.toFixed(6)}`);
console.log(`Confidence: ${estimate.confidence}`);

console.log();

// Prompt enhancement — free
const result = await client.enhance("tell me about kubernetes");
if (result.changed) {
  console.log("Original: tell me about kubernetes");
  console.log(`Enhanced: ${result.enhancedPrompt}`);
  console.log(`Type: ${result.queryType}`);
} else {
  console.log("Prompt was already good!");
}

console.log();

// List models — free
const models = await client.listModels();
for (const m of models) {
  console.log(`  ${m.id.padEnd(25)} ${m.provider.padEnd(10)} ${m.tier}`);
}
