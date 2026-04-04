/**
 * Streaming — OpenAI SDK (TypeScript)
 *
 * Stream responses using the OpenAI TypeScript SDK with RoutePlex.
 * Just change the base URL — streaming works exactly like OpenAI.
 *
 * Docs: https://routeplex.com/docs/streaming
 * Usage: npx tsx streaming.ts
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

async function streamResponse(message: string): Promise<void> {
  const stream = await client.chat.completions.create({
    model: "routeplex-ai",
    messages: [{ role: "user", content: message }],
    stream: true,
  });

  for await (const chunk of stream) {
    const content = chunk.choices[0]?.delta?.content;
    if (content) {
      process.stdout.write(content);
    }

    if (chunk.usage) {
      console.log(
        `\n\nTokens: ${chunk.usage.prompt_tokens} in / ${chunk.usage.completion_tokens} out`
      );
    }
  }
}

async function main() {
  console.log("Streaming with OpenAI SDK + RoutePlex\n");
  await streamResponse("Explain the difference between REST and GraphQL in 3 sentences.");
}

main();
