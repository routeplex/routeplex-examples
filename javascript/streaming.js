/**
 * Streaming — Native API (Fetch SSE)
 *
 * Stream responses in real time using the Fetch API and Server-Sent Events.
 * RoutePlex supports two streaming modes:
 *   - "buffered" (default): Smooth, sentence-aware chunks
 *   - "realtime": Minimal buffering, character-level delivery
 *
 * Docs: https://routeplex.com/docs/streaming
 * Usage: node streaming.js
 */

const API_KEY = process.env.ROUTEPLEX_API_KEY;
const BASE_URL = "https://api.routeplex.com";

if (!API_KEY) {
  console.error("Error: Set ROUTEPLEX_API_KEY environment variable");
  process.exit(1);
}

async function streamChat(message, streamMode = "buffered") {
  const response = await fetch(`${BASE_URL}/api/v1/chat`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      "Content-Type": "application/json",
      Accept: "text/event-stream",
    },
    body: JSON.stringify({
      messages: [{ role: "user", content: message }],
      mode: "routeplex-ai",
      stream: true,
      stream_mode: streamMode,
    }),
  });

  if (!response.ok) {
    console.error(`Error ${response.status}: ${await response.text()}`);
    return;
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, { stream: true });
    const lines = buffer.split("\n");
    buffer = lines.pop(); // keep incomplete line in buffer

    for (const line of lines) {
      if (!line.startsWith("data: ")) continue;

      const payload = line.slice(6);
      if (payload === "[DONE]") return;

      const event = JSON.parse(payload);

      if (event.type === "start") {
        // Stream started
      } else if (event.type === "delta") {
        process.stdout.write(event.content);
      } else if (event.type === "done") {
        console.log(`\n\n--- Stream complete ---`);
        console.log(
          `Model: ${event.model_used} (${event.provider}) | ` +
            `Tokens: ${event.usage.input_tokens} in / ${event.usage.output_tokens} out | ` +
            `Latency: ${event.latency_ms}ms`
        );
      }
    }
  }
}

async function main() {
  console.log("=== Buffered mode (smooth, sentence-aware chunks) ===\n");
  await streamChat("Explain how HTTP streaming works in 3 sentences.");

  console.log("\n\n=== Realtime mode (minimal buffering) ===\n");
  await streamChat("What is the capital of France?", "realtime");
}

main();
