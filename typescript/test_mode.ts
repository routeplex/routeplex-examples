/**
 * Test Mode — TypeScript
 *
 * Force default-tier models only during development and CI.
 * Prevents auto-routing from selecting premium models.
 *
 * Docs: https://routeplex.com/docs/examples#test-mode
 * Usage: npx tsx test_mode.ts
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
  // Test mode keeps costs predictable — only default-tier models are used
  const response = await client.chat.completions.create(
    {
      model: "routeplex-ai",
      messages: [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: "What is the capital of France?" },
      ],
    },
    {
      headers: {
        "X-RoutePlex-Test-Mode": "true",
      },
    }
  );

  console.log("Response:", response.choices[0].message.content);
  console.log(`Model: ${response.model} (default-tier only)`);

  if (response.usage) {
    console.log(
      `Tokens: ${response.usage.prompt_tokens} in / ${response.usage.completion_tokens} out`
    );
  }

  // Combine test mode with prompt enhancement
  const enhanced = await client.chat.completions.create(
    {
      model: "routeplex-ai",
      messages: [{ role: "user", content: "fix my python code" }],
    },
    {
      headers: {
        "X-RoutePlex-Enhance": "true",
        "X-RoutePlex-Test-Mode": "true",
      },
    }
  );

  console.log("\nWith enhancement + test mode:");
  console.log("Response:", enhanced.choices[0].message.content?.slice(0, 200), "...");
  console.log(`Model: ${enhanced.model} (default-tier only)`);
}

main();
