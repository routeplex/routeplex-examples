/**
 * Prompt Enhancement — JavaScript
 *
 * Auto-rewrite vague prompts for better AI responses.
 * Works with both the native API and OpenAI SDK.
 *
 * Docs: https://routeplex.com/docs/prompt-enhancement
 * Usage: node prompt_enhancement.js
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
  // Enhancement via X-RoutePlex-Enhance header
  const response = await client.chat.completions.create(
    {
      model: "routeplex-ai",
      messages: [{ role: "user", content: "sort a list in python" }],
    },
    {
      headers: {
        "X-RoutePlex-Strategy": "quality",
        "X-RoutePlex-Enhance": "true",
      },
    }
  );

  console.log("Response:", response.choices[0].message.content?.slice(0, 200), "...");
  console.log(`Model: ${response.model}`);

  // Enhancement metadata in response (if available)
  if (response.x_routeplex?.enhancement) {
    const enh = response.x_routeplex.enhancement;
    console.log(`\nEnhancement applied: ${enh.applied}`);
    console.log(`Query type: ${enh.query_type}`);
  }

  // ── Standalone enhance endpoint (no API key required) ──────────────────
  console.log("\n--- Standalone Enhancement ---");
  const enhanceResp = await fetch("https://api.routeplex.com/api/v1/chat/enhance", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt: "compare react and vue" }),
  });

  const enhanceData = await enhanceResp.json();
  console.log(`Original: ${enhanceData.data.original_prompt}`);
  console.log(`Enhanced: ${enhanceData.data.enhanced_prompt}`);
  console.log(`Type:     ${enhanceData.data.query_type}`);
}

main();
