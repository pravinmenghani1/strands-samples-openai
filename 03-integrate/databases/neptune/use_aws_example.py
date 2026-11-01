
import argparse
import os
from strands import Agent
from strands.models.openai import OpenAIModel
from strands_tools import use_aws
from dotenv import load_dotenv

load_dotenv()


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Amazon Neptune agent using strands Agent use_aws tool")
    parser.add_argument("prompt", help="Prompt to send to the agent")

    # Parse arguments
    args = parser.parse_args()

    agent = Agent(
        model=OpenAIModel(
            client_args={"api_key": os.environ["OPENAI_API_KEY"]},
            model_id=os.getenv("OPENAI_MODEL_ID", "gpt-5-mini"),
        ),
        tools=[use_aws],
    )

    agent.tool.use_aws(service_name="neptune-graph", operation_name="execute_query", 
                    parameters={"query": "", "language":"OPEN_CYPHER"}, region="us-west-2", 
                    graph_id=os.getenv("NEPTUNE_GRAPH_IDENTIFIER"))

    agent(args.prompt)

if __name__ == "__main__":
    main()
