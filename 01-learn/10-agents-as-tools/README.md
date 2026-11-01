# Agents as Tools

These notebooks demonstrate how to wrap specialized agents as callable tools and coordinate them from an orchestrator agent.

## Notebooks

| Notebook | What it covers |
| --- | --- |
| [`agent-as-tools.ipynb`](./agent-as-tools.ipynb) | Core agents-as-tools patterns, including specialist agents, orchestration, and nested agents |
| [`agents-as-tools-interleaved.ipynb`](./agents-as-tools-interleaved.ipynb) | The same orchestration pattern using an OpenAI reasoning model that thinks between tool calls |

Start with `agent-as-tools.ipynb`, then use the interleaved-thinking notebook for the advanced variant.

## Prerequisites

- A Python environment with Jupyter
- Set `OPENAI_API_KEY` in your environment (optionally `OPENAI_MODEL_ID`, default `gpt-5-mini`)

## Run the notebooks

1. Install the shared dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start Jupyter from this directory:

   ```bash
   jupyter notebook
   ```

3. Open a notebook and run its cells in order.
