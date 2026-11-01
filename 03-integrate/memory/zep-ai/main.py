import os

from strands import Agent
from strands.models.openai import OpenAIModel

# Create an agent backed by an OpenAI model
model = OpenAIModel(
    client_args={"api_key": os.environ["OPENAI_API_KEY"]},
    model_id=os.getenv("OPENAI_MODEL_ID", "gpt-5-mini"),
)
agent = Agent(model=model)

# Ask the agent a question
agent("Tell me about agentic AI")
