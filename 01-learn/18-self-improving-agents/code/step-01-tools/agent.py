"""AIM308 - Step 1: Self-extending agent.

Adds load_tools_from_directory=True → agent can write new tools to ./tools/
while running, and use them immediately.
"""
import os

from strands import Agent
from strands.models.openai import OpenAIModel
from strands.vended_tools import shell
from strands_tools import file_write

# OpenAI model, API key read from the environment
MODEL = OpenAIModel(
    client_args={"api_key": os.environ["OPENAI_API_KEY"]},
    model_id=os.getenv("OPENAI_MODEL_ID", "gpt-5-mini"),
)

SYSTEM_PROMPT = """You are a self-extending research agent.

You can CREATE new tools by writing Python files to ./tools/. Each file should
define one or more functions decorated with `@tool` from the strands package.
Tools become available instantly after the file is saved.

Template for a new tool:

```python
from strands import tool

@tool
def my_tool(argument: str) -> str:
    \"\"\"Short description of what this tool does.

    Args:
        argument: What this argument means.

    Returns:
        A string result.
    \"\"\"
    return f"result for {argument}"
```

When a user asks for a capability you don't have, CREATE the tool, then USE it.
Be concise in your replies.
"""


def main():
    agent = Agent(
        model=MODEL,
        tools=[shell, file_write],
        load_tools_from_directory=True,
        system_prompt=SYSTEM_PROMPT,
    )
    print("🦆 Self-extending agent. Type 'exit' to quit.\n")
    while True:
        try:
            q = input("🦆 ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if q.lower() in ("exit", "quit", "q", ""):
            break
        agent(q)


if __name__ == "__main__":
    main()
