# Model Providers in Strands Agents

Strands Agents takes a model-driven approach and is not tied to a single model or vendor. A *model provider* is the adapter that connects your agent to a specific model, and the SDK ships with providers for Amazon Bedrock, Anthropic, Ollama, LiteLLM, OpenAI, and more. This tutorial shows three of them in practice: running a model locally with Ollama, reaching OpenAI through LiteLLM, and calling OpenAI models through the Responses API.

## Tutorial Details

| Information          | Details                                                                 |
|----------------------|-------------------------------------------------------------------------|
| **Agent structure**  | Single agent                                                            |
| **Strands model providers** | `OllamaModel`, `LiteLLMModel`, `OpenAIResponsesModel`             |
| **Where they run**          | Your local machine (Ollama), OpenAI API (via LiteLLM and Responses API) |
| **Strands features** | Swapping model providers, passing a configured model to `Agent`         |

## Key Concepts

- **Model provider**: A class such as `OpenAIModel`, `OllamaModel`, or `LiteLLMModel` that adapts a specific model to the Strands `Agent`. You configure a provider instance and pass it as the `model` argument to `Agent`; the rest of your agent code stays the same.
- **Default provider**: If you create `Agent()` without a `model`, the SDK uses Amazon Bedrock with its default model. The other providers are opt-in. Install the matching extra and construct the provider yourself.
- **Install extras**: Providers that need extra dependencies are published as pip extras, for example `strands-agents[ollama]`, `strands-agents[litellm]`, and `strands-agents[openai]`. Install the extra for the provider you want rather than the underlying package on its own, so you get a version the SDK supports.

## Supported Model Providers

Strands Agents includes many model providers out of the box. Here are a few examples:

| Provider | Description |
|----------|-------------|
| [Amazon Bedrock](https://strandsagents.com/docs/user-guide/concepts/model-providers/amazon-bedrock/) | Default provider. Access foundation models from Anthropic, Meta, Amazon, and others through Amazon's managed service. |
| [Anthropic](https://strandsagents.com/docs/user-guide/concepts/model-providers/anthropic/) | Direct API access to Claude models. |
| [Ollama](https://strandsagents.com/docs/user-guide/concepts/model-providers/ollama/) | Run models locally for privacy or offline use. |
| [LiteLLM](https://strandsagents.com/docs/user-guide/concepts/model-providers/litellm/) | Unified interface for OpenAI, Azure OpenAI, Mistral, and many other providers. |
| [OpenAI](https://strandsagents.com/docs/user-guide/concepts/model-providers/openai/) | Direct access to OpenAI models, including the [Responses API](https://strandsagents.com/docs/user-guide/concepts/model-providers/openai-responses/). |

This is not the full list. See the [model providers documentation](https://strandsagents.com/docs/user-guide/concepts/model-providers/) for every built-in provider (Amazon Nova, Google Gemini, Mistral, Writer, SageMaker, and more) and for how to build a [custom provider](https://strandsagents.com/docs/user-guide/concepts/model-providers/custom_model_provider/).

## Prerequisites

- Python 3.10 or higher
- Basic understanding of Python
- Provider-specific requirements, called out in each sub-sample (Ollama installed locally for `01-ollama-model`; for the OpenAI samples, set `OPENAI_API_KEY` in your environment, optionally `OPENAI_MODEL_ID`, default `gpt-5-mini`)

## Tutorial Structure

Each sub-sample is self-contained and has its own `requirements.txt`.

| Path | Description |
|------|-------------|
| [01-ollama-model/ollama-file-ops-agent.ipynb](./01-ollama-model/ollama-file-ops-agent.ipynb) | Run a model locally with `OllamaModel` and build a file-operations agent (`file_read`, `file_write`, `list_directory`). |
| [02-openai-litellm/openai-litellm-agent.ipynb](./02-openai-litellm/openai-litellm-agent.ipynb) | Reach an OpenAI model through `LiteLLMModel` and give the agent `current_time` and `current_weather` tools. |
| [03-openai-responses-on-bedrock/openai-responses-agent.ipynb](./03-openai-responses-on-bedrock/openai-responses-agent.ipynb) | Call an OpenAI model with `OpenAIResponsesModel` and the Responses API. |

## Getting Started

1. **Install dependencies** for the sub-sample you want to run:
   ```bash
   cd 01-ollama-model        # or: 02-openai-litellm, 03-openai-responses-on-bedrock
   pip install -r requirements.txt
   ```

2. **Run the notebook** in that folder and run the cells in order.

## Project Structure

```
03-model-providers/
├── 01-ollama-model/
│   ├── ollama-file-ops-agent.ipynb
│   ├── requirements.txt
│   ├── images/
│   └── sample_file/
├── 02-openai-litellm/
│   ├── openai-litellm-agent.ipynb
│   ├── requirements.txt
│   └── images/
├── 03-openai-responses-on-bedrock/
│   ├── openai-responses-agent.ipynb
│   ├── requirements.txt
│   └── images/
└── README.md
```

## Cleanup

The Ollama notebook writes local files (for example `sample.txt` and `readme.md`) in its folder when you run the examples; delete them to reset. The LiteLLM and Responses notebooks call hosted model APIs only and create no persistent resources.

