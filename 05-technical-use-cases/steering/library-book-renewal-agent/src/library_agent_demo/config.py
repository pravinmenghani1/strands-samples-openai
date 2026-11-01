"""Configuration management for different environments."""

import os

from dotenv import load_dotenv
from strands.models.openai import OpenAIModel

load_dotenv()

DEFAULT_OPENAI_MODEL_ID = "gpt-5-mini"


def get_openai_model_id() -> str:
    """Get the OpenAI model ID (``OPENAI_MODEL_ID``, default ``gpt-5-mini``)."""
    return os.getenv("OPENAI_MODEL_ID", DEFAULT_OPENAI_MODEL_ID)


def create_openai_model(model_id: str | None = None) -> OpenAIModel:
    """Create an OpenAI model using ``OPENAI_API_KEY`` from the environment."""
    return OpenAIModel(
        client_args={"api_key": os.environ["OPENAI_API_KEY"]},
        model_id=model_id or get_openai_model_id(),
    )


def get_log_level() -> str:
    """Get the configured log level."""
    return os.getenv("LOG_LEVEL", "INFO").upper()


def get_output_directory() -> str:
    """Get the directory for output files."""
    return os.getenv("OUTPUT_DIR", "./output")


def ensure_output_directory() -> str:
    """Ensure output directory exists and return path."""
    output_dir = get_output_directory()
    os.makedirs(output_dir, exist_ok=True)
    return output_dir
