import asyncio
import os

from strands import Agent
from strands.models.openai import OpenAIModel
from strands_tools.a2a_client import A2AClientToolProvider

# initialize collection of A2A tools for the agent
provider = A2AClientToolProvider(known_agent_urls=["http://localhost:9000"])

# initialize agent with tools
model = OpenAIModel(
    client_args={"api_key": os.environ["OPENAI_API_KEY"]},
    model_id=os.getenv("OPENAI_MODEL_ID", "gpt-5-mini"),
)
agent = Agent(model=model, tools=provider.tools)
# you can also invoke the agent in a non-async context
# print(agent("pick an agent and make a sample call to test its functionality"))


# run the agent in an async context
async def main():
    await agent.invoke_async(
        "pick an agent and make a sample call to test its functionality"
    )


# run
asyncio.run(main())
