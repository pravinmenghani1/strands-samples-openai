"""Model utilities for evaluators."""

from strands.models.openai import OpenAIModel

from ...config import create_openai_model


def create_judge_model(model_id: str | None = None) -> OpenAIModel:
    """Create the OpenAI judge model (defaults to ``OPENAI_MODEL_ID`` or ``gpt-5-mini``)."""
    return create_openai_model(model_id)
