# Agent to Agent (A2A) protocol using Strands Agent SDK

An example Strands agent that helps with searching AWS documentation.

## Getting started

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
2. Set `OPENAI_API_KEY` in your environment (optionally `OPENAI_MODEL_ID`, default `gpt-5-mini`).
3. Start the A2A server using `uv run __main__.py`.
4. Run the test client `uv run test_client.py`.