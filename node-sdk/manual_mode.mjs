/**
 * RoutePlex Node.js SDK — Manual Model Selection
 *
 * npm install @routeplex/node
 */

import { RoutePlex } from "@routeplex/node";

const client = new RoutePlex({ apiKey: process.env.ROUTEPLEX_API_KEY });

const response = await client.chat("Write a function to check if a number is prime", {
  model: "gpt-4o-mini",
  maxOutputTokens: 1024,
  temperature: 0.3,
});

console.log(response.output);
console.log(`Model: ${response.modelUsed}`);
console.log(`Tokens: ${response.usage.totalTokens}`);
