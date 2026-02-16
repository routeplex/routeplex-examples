# Contributing to RoutePlex Examples

Thank you for your interest in contributing! Here's how you can help.

## Guidelines

### Adding a New Example

1. **Pick the right directory** — place your file under `python/`, `javascript/`, `typescript/`, or `curl/`.
2. **One file, one concept** — each example should demonstrate a single feature or use case.
3. **Must be runnable** — every example should work out of the box with a valid API key.
4. **Use environment variables** — always read the key from `ROUTEPLEX_API_KEY`, never hardcode it.
5. **Include error handling** — show proper error handling so users get helpful messages.
6. **Add a header comment** — include a brief description, link to relevant docs, and usage instructions.

### Code Style

- **Python:** Follow PEP 8. Use `requests` for HTTP examples, `openai` for SDK examples.
- **JavaScript:** Use modern ES syntax (`async/await`, `fetch`).
- **TypeScript:** Include proper types. Use the `openai` package.
- **cURL:** Use `bash` with proper quoting and `$ROUTEPLEX_API_KEY`.

### Submitting

1. Fork this repository
2. Create a feature branch (`git checkout -b add-example-name`)
3. Add your example
4. Test it with a real API key
5. Open a pull request with a description of what the example demonstrates

## Questions?

- [Documentation](https://routeplex.com/docs)
- [Discord](https://discord.gg/BaFcXQJA)
- [Email](mailto:support@routeplex.com)
