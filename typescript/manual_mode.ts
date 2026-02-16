/**
 * Manual Mode — Specific Model with Fallback (OpenAI SDK)
 *
 * Choose a specific model. If it's unavailable, RoutePlex automatically
 * routes to a fallback model.
 *
 * Docs: https://routeplex.com/docs/routing-modes
 * Usage: npx tsx manual_mode.ts
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

async function queryModel(
  prompt: string,
  model: string = "claude-sonnet-4-20250514"
): Promise<string | null> {
  const response = await client.chat.completions.create({
    model, // Specific model — RoutePlex handles fallback automatically
    messages: [{ role: "user", content: prompt }],
    max_tokens: 1024,
  });

  console.log(`Requested: ${model}`);
  console.log(`Used:      ${response.model}`);
  if (response.usage) {
    console.log(
      `Tokens: ${response.usage.prompt_tokens} in / ${response.usage.completion_tokens} out`
    );
  }

  return response.choices[0].message.content;
}

async function main() {
  const result = await queryModel(
    "What are the SOLID principles in software engineering?"
  );
  console.log(`\n${result}`);
}

main();
