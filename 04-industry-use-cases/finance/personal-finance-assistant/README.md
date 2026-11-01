# Personal Finance Assistant Workshop

This three-part workshop teaches core Strands Agents patterns through educational budget and portfolio-analysis examples.

> **Educational use only:** The examples are not financial or investment advice. Verify any financial information with a qualified professional.

## Labs

Work through the notebooks in order:

| Notebook | What it covers |
| --- | --- |
| [`lab1-foundations.ipynb`](./lab1-foundations.ipynb) | Agent and tool fundamentals, visualizations, and Amazon Bedrock Guardrails |
| [`lab2-memory-integration.ipynb`](./lab2-memory-integration.ipynb) | Conversation history, agent state, request state, and long-term memory options |
| [`lab3-multi-agent-orchestration.ipynb`](./lab3-multi-agent-orchestration.ipynb) | Agents-as-tools orchestration, portfolio-analysis specialists, and human-in-the-loop decisions |

## Prerequisites

- A Python environment with Jupyter
- Set `OPENAI_API_KEY` in your environment (optionally `OPENAI_MODEL_ID`, default `gpt-5-mini`)
- For Lab 1's guardrail section only: AWS credentials with permission to create and use Amazon Bedrock Guardrails
- Internet access for dependencies and the market-data examples in Lab 3

Lab 2 explains the additional setup for its local, OpenSearch, and Mem0 Platform memory options. The notebooks install their Python dependencies.

## Run the workshop

Start Jupyter from this directory, open `lab1-foundations.ipynb`, and run each notebook's cells in order:

```bash
jupyter notebook
```

## Cleanup

Delete the Amazon Bedrock Guardrail created in Lab 1 when you finish. You can also remove any local memory, chart, or market-data files created while running the later labs.
