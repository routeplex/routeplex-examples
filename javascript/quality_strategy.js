/**
 * Quality Strategy — Best Output
 *
 * Routes to the most capable model for complex reasoning, code generation,
 * or detailed analysis.
 *
 * Docs: https://routeplex.com/docs/routing-modes
 * Usage: node quality_strategy.js
 */

const API_KEY = process.env.ROUTEPLEX_API_KEY;
const BASE_URL = "https://api.routeplex.com";

if (!API_KEY) {
  console.error("Error: Set ROUTEPLEX_API_KEY environment variable");
  process.exit(1);
}

async function generateCode(description) {
  const response = await fetch(`${BASE_URL}/api/v1/chat`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      messages: [
        { role: "system", content: "You are an expert programmer. Write clean, documented code." },
        { role: "user", content: `Implement: ${description}` },
      ],
      mode: "routeplex-ai",
      strategy: "quality",
      max_output_tokens: 2048,
      temperature: 0.3,
    }),
  });

  if (!response.ok) {
    console.error(`Error ${response.status}: ${await response.text()}`);
    return null;
  }

  const data = await response.json();
  console.log(
    `Model: ${data.data.model_used} | Cost: $${data.data.usage.cost_usd}`
  );
  return data.data.output;
}

async function main() {
  const result = await generateCode(
    "A function that finds the longest common subsequence of two strings"
  );
  console.log(`\n${result}`);
}

main();
