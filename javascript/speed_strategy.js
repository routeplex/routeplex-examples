/**
 * Speed Strategy — Minimize Latency
 *
 * Real-time chatbot with the fastest possible response time.
 *
 * Docs: https://routeplex.com/docs/routing-modes
 * Usage: node speed_strategy.js
 */

const API_KEY = process.env.ROUTEPLEX_API_KEY;
const BASE_URL = "https://api.routeplex.com";

if (!API_KEY) {
  console.error("Error: Set ROUTEPLEX_API_KEY environment variable");
  process.exit(1);
}

async function getChatResponse(userMessage) {
  const start = Date.now();

  const response = await fetch(`${BASE_URL}/api/v1/chat`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      messages: [{ role: "user", content: userMessage }],
      mode: "routeplex-ai",
      strategy: "speed",
      max_output_tokens: 256,
    }),
  });

  if (!response.ok) {
    console.error(`Error ${response.status}: ${await response.text()}`);
    return null;
  }

  const data = await response.json();
  const elapsed = Date.now() - start;

  console.log(
    `  Model: ${data.data.model_used} | Time: ${elapsed}ms | Cost: $${data.data.usage.cost_usd}`
  );
  return data.data.output;
}

async function main() {
  console.log("Speed strategy — fastest model selection\n");

  const result = await getChatResponse("What is the capital of France?");
  console.log(`\nResponse: ${result}`);
}

main();
