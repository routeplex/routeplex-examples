<div align="center">

# RoutePlex Examples

**Working code examples for the [RoutePlex](https://routeplex.com) unified AI gateway.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![RoutePlex](https://img.shields.io/badge/RoutePlex-API-6366f1)](https://routeplex.com)
[![Docs](https://img.shields.io/badge/Docs-routeplex.com-green)](https://routeplex.com/docs)

[Get API Key](https://routeplex.com/app) · [Documentation](https://routeplex.com/docs) · [API Reference](https://routeplex.com/api-reference)

</div>

---

## Overview

RoutePlex is a unified AI gateway that lets you access 22+ models from OpenAI, Anthropic, and Google through a single API. These examples demonstrate real-world usage patterns including smart routing, failover, web search, URL fetching, and OpenAI SDK compatibility.

## Examples

| Example | Language | Description |
|---------|----------|-------------|
| [Quickstart](python/quickstart.py) | Python | Minimal setup — make your first API call |
| [Customer Support](python/customer_support.py) | Python | Cost-optimized support chatbot (~60% savings) |
| [High Reliability](python/high_reliability.py) | Python | Automatic failover for production APIs |
| [OpenAI Compatible](python/openai_compatible.py) | Python | Drop-in replacement using the OpenAI SDK |
| [Cost Strategy](python/cost_strategy.py) | Python | Minimize expenses for high-volume tasks |
| [Speed Strategy](python/speed_strategy.py) | Python | Minimize latency for real-time apps |
| [Quality Strategy](python/quality_strategy.py) | Python | Best output for complex reasoning |
| [Balanced Strategy](python/balanced_strategy.py) | Python | Optimal cost/speed/quality trade-off |
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
| [Balanced Strategy](typescript/balanced_strategy.ts) | TypeScript | General-purpose assistant (OpenAI SDK) |
| [Speed Strategy](typescript/speed_strategy.ts) | TypeScript | Fastest response (OpenAI SDK) |
| [Manual Mode](typescript/manual_mode.ts) | TypeScript | Specific model with auto-fallback |
| [Test Mode](typescript/test_mode.ts) | TypeScript | Force default-tier models (OpenAI SDK) |
| [Basic cURL](curl/basic.sh) | cURL | Simple request from the command line |

## Quick Start

### 1. Get an API Key

Sign up at [routeplex.com/app](https://routeplex.com/app) and create an API key.

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
npx tsx balanced_strategy.ts
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

| Strategy | Best For | Description |
|----------|----------|-------------|
| `cost` | High-volume, simple tasks | Routes to most cost-effective model |
| `speed` | Real-time, interactive apps | Routes to fastest responding model |
| `quality` | Complex reasoning, analysis | Routes to most capable model |
| `balanced` | General-purpose (default) | Optimizes cost/speed/quality trade-off |

## Links

- [Documentation](https://routeplex.com/docs)
- [API Reference](https://routeplex.com/api-reference)
- [Models](https://routeplex.com/models)
- [Pricing](https://routeplex.com/pricing)
- [Discord](https://discord.gg/BaFcXQJA)

## License

[MIT](LICENSE)