/**
 * Cost Strategy — Minimize Expenses
 *
 * Classify and process high-volume tasks at lowest cost.
 * Ideal for data extraction, classification, and basic Q&A.
 *
 * Docs: https://routeplex.com/docs/routing-modes
 * Usage: node cost_strategy.js
 */

const API_KEY = process.env.ROUTEPLEX_API_KEY;
const BASE_URL = "https://api.routeplex.com";

if (!API_KEY) {
  console.error("Error: Set ROUTEPLEX_API_KEY environment variable");
  process.exit(1);
}

async function classifyText(text) {
  const response = await fetch(`${BASE_URL}/api/v1/chat`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      messages: [
        {
          role: "user",
          content: `Classify this text as positive, negative, or neutral: ${text}`,
        },
      ],
      mode: "routeplex-ai",
      strategy: "cost",
      max_output_tokens: 50,
    }),
  });

  if (!response.ok) {
    console.error(`Error ${response.status}: ${await response.text()}`);
    return null;
  }

  const data = await response.json();
  console.log(
    `  Model: ${data.data.model_used} | Cost: $${data.data.usage.cost_usd}`
  );
  return data.data.output;
}

async function main() {
  const texts = [
    "I love this product, it works perfectly!",
    "The delivery was late and the item was damaged.",
    "The package arrived on Tuesday.",
  ];

  for (const text of texts) {
    console.log(`\nText: ${text}`);
    const result = await classifyText(text);
    console.log(`Classification: ${result}`);
  }
}

main();
