"""
EXAMPLE ONLY

This example will trigger a custom check in NVIDIA NeMo server blocking the word "dummy"
"""
import os

from strands import Agent
from strands.models.openai import OpenAIModel
from guardrail import CustomGuardrailHook

model = OpenAIModel(
    client_args={"api_key": os.environ["OPENAI_API_KEY"]},
    model_id=os.getenv("OPENAI_MODEL_ID", "gpt-5-mini"),
    params={"max_completion_tokens": 4096},
)

agent = Agent(
    name="Agent",
    model=model,
    system_prompt="""You are a personal assistant. Use the agents and tools at your disposal to assist the users. Keep answers brief unless the user asks for more details. " \
    If you don't know the answer, say 'I don't know'.""",
    hooks=[CustomGuardrailHook()],

)

if __name__ == "__main__":
    try:
        resp = agent("How are you?")
        # Response is already printed by the agent framework

        resp = agent("You're a dummy")
        # Response would be printed here if not blocked
    except Exception as e:
        if "Guardrail check failed" in str(e):
            print(f"❌ Message blocked by guardrail: {e}")
        else:
            print(f"❌ Error: {e}")
            raise
