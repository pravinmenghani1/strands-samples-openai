"""AIM308 - Step 0: Hello Agent.

The minimum viable Strands agent. OpenAI gpt-5-mini + one tool (shell).
"""
import os
import sys
from strands import Agent
from strands.models.openai import OpenAIModel
from strands.vended_tools import shell

# OpenAI model, API key read from the environment
MODEL = OpenAIModel(
    client_args={"api_key": os.environ["OPENAI_API_KEY"]},
    model_id=os.getenv("OPENAI_MODEL_ID", "gpt-5-mini"),
)


def main():
    agent = Agent(
        model=MODEL,
        tools=[shell],
        system_prompt=(
            "You are a helpful assistant. "
            "Use the shell tool when useful. Be concise."
        ),
    )
    query = " ".join(sys.argv[1:]) or "Hello, introduce yourself in one sentence."
    agent(query)


if __name__ == "__main__":
    main()
