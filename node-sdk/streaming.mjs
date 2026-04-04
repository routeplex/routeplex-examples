/**
 * RoutePlex Node.js SDK — Streaming
 *
 * Stream responses in real time using the SDK's chatStream() method.
 * Supports "buffered" (default, smooth chunks) and "realtime" (minimal latency).
 *
 * npm install @routeplex/node
 */

import { RoutePlex } from "@routeplex/node";

const client = new RoutePlex({ apiKey: process.env.ROUTEPLEX_API_KEY });

console.log("=== Buffered streaming (default) ===\n");

for await (const event of client.chatStream("Explain how streaming works in 3 sentences.")) {
  if (event.type === "delta") {
    process.stdout.write(event.content);
  } else if (event.type === "done") {
    console.log(`\n\nModel: ${event.modelUsed} (${event.provider})`);
    console.log(`Tokens: ${event.usage.totalTokens}`);
    console.log(`Latency: ${event.latencyMs}ms`);
  }
}

console.log("\n\n=== Realtime streaming ===\n");

for await (const event of client.chatStream("What is the capital of France?", {
  streamMode: "realtime",
})) {
  if (event.type === "delta") {
    process.stdout.write(event.content);
  } else if (event.type === "done") {
    console.log(`\n\nModel: ${event.modelUsed}`);
  }
}
