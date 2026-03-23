/**
 * RoutePlex Node.js SDK — Error Handling
 *
 * npm install @routeplex/node
 */

import {
  RoutePlex,
  AuthenticationError,
  RateLimitError,
  ValidationError,
  ProviderError,
  ContentPolicyError,
} from "@routeplex/node";

const client = new RoutePlex({ apiKey: process.env.ROUTEPLEX_API_KEY });

try {
  const response = await client.chat("Hello!");
  console.log(response.output);
} catch (err) {
  if (err instanceof AuthenticationError) {
    console.log("Invalid API key — check your ROUTEPLEX_API_KEY");
  } else if (err instanceof RateLimitError) {
    console.log(`Rate limited: ${err.code} — ${err.message}`);
  } else if (err instanceof ValidationError) {
    console.log(`Bad request: ${err.message}`);
  } else if (err instanceof ContentPolicyError) {
    console.log("Content blocked by moderation");
  } else if (err instanceof ProviderError) {
    console.log("All upstream providers failed");
  } else {
    throw err;
  }
}
