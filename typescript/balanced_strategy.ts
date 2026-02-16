/**
 * Balanced Strategy — General-Purpose Assistant (OpenAI SDK)
 *
 * Uses the OpenAI TypeScript SDK with RoutePlex as a drop-in replacement.
 * Balanced strategy optimizes the trade-off between cost, speed, and quality.
 *
 * Docs: https://routeplex.com/docs/openai-compatibility
 * Usage: npx tsx balanced_strategy.ts
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

interface Message {
  role: "system" | "user" | "assistant";
  content: string;
}

async function chat(messages: Message[]): Promise<string | null> {
  // Strategy is passed via the X-RoutePlex-Strategy header
  const response = await client.chat.completions.create(
    {
      model: "routeplex-ai",
      messages,
    },
    {
      headers: { "X-RoutePlex-Strategy": "balanced" },
    }
  );

  console.log(`Model: ${response.model}`);
  if (response.usage) {
    console.log(
      `Tokens: ${response.usage.prompt_tokens} in / ${response.usage.completion_tokens} out`
    );
  }

  return response.choices[0].message.content;
}

async function main() {
  const result = await chat([
    { role: "system", content: "You are a concise technical assistant." },
    {
      role: "user",
      content: "Explain the CAP theorem in three sentences.",
    },
  ]);

  console.log(`\nResponse: ${result}`);
}

main();
