import os
from openai import OpenAI


def get_llm_response(user_message="Hello!", system="", max_completion_tokens=8192):
    """
    Single-turn text completion with the OpenAI model.
    Note: reasoning models such as gpt-5-mini count reasoning tokens against max_completion_tokens.
    """
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    messages = [{"role": "system", "content": system}] if system else []
    messages.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL_ID", "gpt-5-mini"),
        max_completion_tokens=max_completion_tokens,
        messages=messages,
    )
    return response.choices[0].message.content
