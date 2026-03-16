/**
 * Web Search — Real-Time Data
 *
 * RoutePlex auto-detects queries that need real-time data and searches
 * the web before sending to the LLM. No extra setup required.
 *
 * Docs: https://routeplex.com/docs/examples
 * Usage: node web_search.js
 */

const API_KEY = process.env.ROUTEPLEX_API_KEY;
const BASE_URL = "https://api.routeplex.com";

if (!API_KEY) {
  console.error("Error: Set ROUTEPLEX_API_KEY environment variable");
  process.exit(1);
}

async function searchAndAnswer(question) {
  const response = await fetch(`${BASE_URL}/api/v1/chat`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      messages: [{ role: "user", content: question }],
      mode: "routeplex-ai",
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
  const queries = [
    "What are the trending topics on tech news today?",
    "What is the current price of Bitcoin?",
  ];

  for (const q of queries) {
    console.log(`\nQ: ${q}`);
    const answer = await searchAndAnswer(q);
    console.log(`A: ${answer}`);
  }
}

main();
