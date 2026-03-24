<div align="center">

# RoutePlex Examples

**Working code examples for the [RoutePlex](https://routeplex.com?utm_source=github&utm_medium=readme&utm_campaign=examples) unified AI gateway.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![RoutePlex](https://img.shields.io/badge/RoutePlex-API-6366f1)](https://routeplex.com?utm_source=github&utm_medium=readme&utm_campaign=examples)
[![Docs](https://img.shields.io/badge/Docs-routeplex.com-green)](https://routeplex.com/docs?utm_source=github&utm_medium=readme&utm_campaign=examples)

[Get API Key](https://routeplex.com/app?utm_source=github&utm_medium=readme&utm_campaign=examples) · [Documentation](https://routeplex.com/docs?utm_source=github&utm_medium=readme&utm_campaign=examples) · [API Reference](https://routeplex.com/api-reference?utm_source=github&utm_medium=readme&utm_campaign=examples)

</div>

---

## Overview

RoutePlex is a unified AI gateway that lets you access 22+ models from OpenAI, Anthropic, and Google through a single API. These examples demonstrate real-world usage patterns including prompt-based auto-routing, strategy routing, failover, web search, URL fetching, and OpenAI SDK compatibility.

## SDK Examples (Recommended)

The easiest way to use RoutePlex is through the official SDKs:

```bash
pip install routeplex          # Python
npm install @routeplex/node    # Node.js
```

### Python SDK

| Example | Description |
|---------|-------------|
| [Quickstart](python-sdk/quickstart.py) | One-liner chat — your first SDK call |
| [Strategies](python-sdk/strategies.py) | Auto-routing + cost, speed, quality, balanced strategies |
| [Manual Mode](python-sdk/manual_mode.py) | Pick a specific model |
| [Multi-turn](python-sdk/multi_turn.py) | Conversation with message history |
| [Error Handling](python-sdk/error_handling.py) | Typed exceptions for every error case |
| [Free Endpoints](python-sdk/free_endpoints.py) | Cost estimation, prompt enhancement, list models |

### Node.js SDK

| Example | Description |
|---------|-------------|
| [Quickstart](node-sdk/quickstart.mjs) | One-liner chat — your first SDK call |
| [Strategies](node-sdk/strategies.mjs) | Auto-routing + cost, speed, quality, balanced strategies |
| [Manual Mode](node-sdk/manual_mode.mjs) | Pick a specific model |
| [Multi-turn](node-sdk/multi_turn.mjs) | Conversation with message history |
| [Error Handling](node-sdk/error_handling.mjs) | Typed exceptions for every error case |

---

## Raw API Examples (without SDK)

| Example | Language | Description |
|---------|----------|-------------|
| [Quickstart](python/quickstart.py) | Python | Minimal setup — make your first API call |
| [Customer Support](python/customer_support.py) | Python | Cost-optimized support chatbot (~60% savings) |
| [High Reliability](python/high_reliability.py) | Python | Automatic failover for production APIs |
| [OpenAI Compatible](python/openai_compatible.py) | Python | Drop-in replacement using the OpenAI SDK |
| [Cost Strategy](python/cost_strategy.py) | Python | Minimize expenses for high-volume tasks |
| [Speed Strategy](python/speed_strategy.py) | Python | Minimize latency for real-time apps |
| [Quality Strategy](python/quality_strategy.py) | Python | Best output for complex reasoning |
| [Balanced Strategy](python/balanced_strategy.py) | Python | Fixed-weight cost/speed/quality override |
| [Manual Mode](python/manual_mode.py) | Python | Choose a specific model with auto-fallback |
| [Web Search](python/web_search.py) | Python | Real-time data via automatic web search |
| [URL Fetching](python/url_fetching.py) | Python | Analyze web pages automatically |
| [Prompt Enhancement](python/prompt_enhancement.py) | Python | Auto-rewrite vague prompts for better results |
| [Test Mode](python/test_mode.py) | Python | Force default-tier models for dev/CI |
| [Speed Strategy](javascript/speed_strategy.js) | JavaScript | Real-time chatbot with minimal latency |
| [Quality Strategy](javascript/quality_strategy.js) | JavaScript | Best output for complex tasks |
| [Cost Strategy](javascript/cost_strategy.js) | JavaScript | Minimize expenses for high-volume |
| [Web Search](javascript/web_search.js) | JavaScript | Trending topics via auto web search |
| [OpenAI Compatible](javascript/openai_compatible.js) | JavaScript | OpenAI SDK drop-in replacement |
| [Prompt Enhancement](javascript/prompt_enhancement.js) | JavaScript | Enhancement via OpenAI SDK headers |
| [Balanced Strategy](typescript/balanced_strategy.ts) | TypeScript | Fixed-weight override (OpenAI SDK) |
| [Speed Strategy](typescript/speed_strategy.ts) | TypeScript | Fastest response (OpenAI SDK) |
| [Manual Mode](typescript/manual_mode.ts) | TypeScript | Specific model with auto-fallback |
| [Test Mode](typescript/test_mode.ts) | TypeScript | Force default-tier models (OpenAI SDK) |
| [Basic cURL](curl/basic.sh) | cURL | Simple request from the command line |

## Quick Start

### 1. Get an API Key

Sign up at [routeplex.com/app](https://routeplex.com/app?utm_source=github&utm_medium=readme&utm_campaign=examples) and create an API key.

### 2. Set Your Key

```bash
export ROUTEPLEX_API_KEY="your-api-key-here"
```

### 3. Run an Example

**Python:**
```bash
cd python
pip install -r requirements.txt
python quickstart.py
```

**JavaScript:**
```bash
cd javascript
npm install
node speed_strategy.js
```

**TypeScript:**
```bash
cd typescript
npm install
npx tsx speed_strategy.ts
```

**cURL:**
```bash
cd curl
chmod +x basic.sh
./basic.sh
```

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `POST /api/v1/chat` | Native RoutePlex chat endpoint |
| `POST /v1/chat/completions` | OpenAI-compatible endpoint |
| `POST /api/v1/chat/estimate` | Free cost estimation (no charge) |
| `POST /api/v1/chat/enhance` | Standalone prompt enhancement (no API key) |
| `GET /api/v1/models` | List available models |

Base URL: `https://api.routeplex.com`

## Routing Strategies

By default, when no strategy is specified, RoutePlex uses **auto-routing** — it analyzes the prompt to dynamically choose the best model. You can override this with an explicit strategy:

| Strategy | Best For | Description |
|----------|----------|-------------|
| *(none)* | General-purpose (default) | Auto-routes based on prompt analysis |
| `cost` | High-volume, simple tasks | Routes to most cost-effective model |
| `speed` | Real-time, interactive apps | Routes to fastest responding model |
| `quality` | Complex reasoning, analysis | Routes to most capable model |
| `balanced` | Fixed-weight override | Static cost/speed/quality trade-off (not prompt-aware) |

## Links

- [Documentation](https://routeplex.com/docs?utm_source=github&utm_medium=readme&utm_campaign=examples)
- [API Reference](https://routeplex.com/api-reference?utm_source=github&utm_medium=readme&utm_campaign=examples)
- [Models](https://routeplex.com/models?utm_source=github&utm_medium=readme&utm_campaign=examples)
- [Pricing](https://routeplex.com/pricing?utm_source=github&utm_medium=readme&utm_campaign=examples)
- [Discord](https://discord.gg/BaFcXQJA)

## License

[MIT](LICENSE)