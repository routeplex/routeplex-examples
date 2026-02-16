/**
 * OpenAI SDK Compatible — JavaScript
 *
 * Use the OpenAI Node.js SDK with RoutePlex as a drop-in replacement.
 * Just change the base URL and API key.
 *
 * Docs: https://routeplex.com/docs/openai-compatibility
 * Usage: npm install openai && node openai_compatible.js
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
  // Strategy is passed via the X-RoutePlex-Strategy header
  const response = await client.chat.completions.create(
    {
      model: "routeplex-ai",
      messages: [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: "What are three tips for writing clean code?" },
      ],
    },
    {
      headers: { "X-RoutePlex-Strategy": "balanced" },
    }
  );

  console.log("Response:", response.choices[0].message.content);
  console.log(`Model: ${response.model}`);
  if (response.usage) {
    console.log(
      `Tokens: ${response.usage.prompt_tokens} in / ${response.usage.completion_tokens} out`
    );
  }
}

main();
