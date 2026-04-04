/**
 * Streaming — OpenAI SDK Compatible (JavaScript)
 *
 * Stream responses using the OpenAI Node.js SDK with RoutePlex.
 * Just change the base URL — streaming works exactly like OpenAI.
 *
 * Docs: https://routeplex.com/docs/streaming
 * Usage: npm install openai && node streaming_openai_sdk.js
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

async function main() {
  // stream: true returns an async iterator of ChatCompletionChunk objects
  const stream = await client.chat.completions.create({
    model: "routeplex-ai",
    messages: [
      { role: "system", content: "You are a helpful assistant." },
      { role: "user", content: "Write a haiku about streaming data." },
    ],
    stream: true,
  });

  console.log("Streaming response:\n");

  for await (const chunk of stream) {
    const content = chunk.choices[0]?.delta?.content;
    if (content) {
      process.stdout.write(content);
    }

    // Final chunk includes usage stats
    if (chunk.usage) {
      console.log(
        `\n\nTokens: ${chunk.usage.prompt_tokens} in / ${chunk.usage.completion_tokens} out`
      );
    }
  }
}

main();
