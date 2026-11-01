import logging
import os
import sys

from ddgs import DDGS
from ddgs.exceptions import DDGSException, RatelimitException
from strands import Agent, tool
from strands.models.openai import OpenAIModel

# Configure logging
logging.getLogger("strands").setLevel(
    logging.INFO
)  # Set to DEBUG for more detailed logs


# Define a websearch tool
@tool
def websearch(
    keywords: str, region: str = "us-en", max_results: int | None = None
) -> str:
    """Search the web to get updated information.
    Args:
        keywords (str): The search query keywords.
        region (str): The search region: wt-wt, us-en, uk-en, ru-ru, etc..
        max_results (int | None): The maximum number of results to return.
    Returns:
        List of dictionaries with search results.
    """
    try:
        results = DDGS().text(keywords, region=region, max_results=max_results)
        return results if results else "No results found."
    except RatelimitException:
        return "RatelimitException: Please try again after a short delay."
    except DDGSException as d:
        return f"DuckDuckGoSearchException: {d}"
    except Exception as e:
        return f"Exception: {e}"


# --- OpenAI Model Configuration Setup ---
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: The 'OPENAI_API_KEY' environment variable is not set.", file=sys.stderr)
    print("Please export it in your terminal first: export OPENAI_API_KEY='sk-proj-...'", file=sys.stderr)
    sys.exit(1)

# Configure the explicit OpenAI client profile
openai_model = OpenAIModel(
    model_id="gpt-5-mini",  # Using your preferred OpenAI model name here
    client_args={
        "api_key": api_key,
    }
)


# Create a recipe assistant agent powered by OpenAI
recipe_agent = Agent(
    model=openai_model,  # Pass the explicit OpenAI model configuration object
    system_prompt="""You are RecipeBot, a helpful cooking assistant.
    Help users find recipes based on ingredients and answer cooking questions.
    Use the websearch tool to find recipes when users mention ingredients or to look up cooking information.""",
    tools=[websearch],
)


if __name__ == "__main__":
    print("\nRecipeBot: Ask me about recipes or cooking! Type 'exit' to quit.\n")

    # Run the agent in a loop for interactive conversation
    while True:
        user_input = input("\nYou > ")
        if user_input.lower() == "exit":
            print("Happy cooking!")
            break
        response = recipe_agent(user_input)
        print(f"\nRecipeBot > {response}")

