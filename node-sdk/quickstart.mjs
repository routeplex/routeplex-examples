/**
 * RoutePlex Node.js SDK — Quickstart
 *
 * npm install @routeplex/node
 */

import { RoutePlex } from "@routeplex/node";

const client = new RoutePlex({ apiKey: process.env.ROUTEPLEX_API_KEY });

const response = await client.chat("What is JavaScript?");
console.log(response.output);
console.log(`Model: ${response.modelUsed}`);
console.log(`Cost: $${response.usage.costUsd.toFixed(6)}`);
