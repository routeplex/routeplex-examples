/**
 * Speed Strategy — Minimize Latency (OpenAI SDK)
 *
 * Fastest possible response via the OpenAI TypeScript SDK.
 *
 * Docs: https://routeplex.com/docs/routing-modes
 * Usage: npx tsx speed_strategy.ts
 */

import OpenAI from "openai";

const API_KEY = process.env.ROUTEPLEX_API_KEY;

if (!API_KEY) {
  console.error("Error: Set ROUTEPLEX_API_KEY environment variable");
  process.exit(1);
}

const client = new OpenAI({
  apiKey: API_KEY,
  baseURL: "https://api.routeplex.com/v1",
});

async function fastResponse(message: string): Promise<string | null> {
  const start = Date.now();

  // Strategy is passed via the X-RoutePlex-Strategy header
  const response = await client.chat.completions.create(
    {
      model: "routeplex-ai",
      messages: [{ role: "user", content: message }],
      max_tokens: 256,
    },
    {
      headers: { "X-RoutePlex-Strategy": "speed" },
    }
  );

  const elapsed = Date.now() - start;

  console.log(`Model: ${response.model} | Time: ${elapsed}ms`);
  if (response.usage) {
    console.log(
      `Tokens: ${response.usage.prompt_tokens} in / ${response.usage.completion_tokens} out`
    );
  }

  return response.choices[0].message.content;
}

async function main() {
  console.log("Speed strategy — fastest model selection\n");
  const result = await fastResponse("What is the capital of France?");
  console.log(`\nResponse: ${result}`);
}

main();
