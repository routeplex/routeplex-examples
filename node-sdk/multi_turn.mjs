/**
 * RoutePlex Node.js SDK — Multi-turn Conversation
 *
 * npm install @routeplex/node
 */

import { RoutePlex } from "@routeplex/node";

const client = new RoutePlex({ apiKey: process.env.ROUTEPLEX_API_KEY });

const response = await client.chat([
  { role: "system", content: "You are a helpful JavaScript tutor. Keep answers concise." },
  { role: "user", content: "What are arrow functions?" },
  { role: "assistant", content: "Arrow functions are a shorter syntax: const add = (a, b) => a + b;" },
  { role: "user", content: "How are they different from regular functions?" },
]);

console.log(response.output);
