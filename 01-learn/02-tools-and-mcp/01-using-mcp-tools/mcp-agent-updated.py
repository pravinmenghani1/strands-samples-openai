import os
import sys
import threading
import time
from datetime import timedelta

from mcp import StdioServerParameters, stdio_client
from mcp.client.streamable_http import streamable_http_client
from mcp.server import MCPServer
from strands import Agent
from strands.models.openai import OpenAIModel  # Added for OpenAI support
from strands.tools.mcp import MCPClient

# =====================================================================
# 1. STANDALONE CLIENT INITIALIZATION
# =====================================================================

# Setup stdio clients for the AWS Documentation MCP server
stdio_mcp_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx", args=["awslabs.aws-documentation-mcp-server@latest"]
        )
    )
)

# Setup multi-server clients
aws_docs_mcp_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx", args=["awslabs.aws-documentation-mcp-server@latest"]
        )
    )
)

iac_mcp_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx", args=["awslabs.aws-iac-mcp-server@latest"]
        )
    )
)


# =====================================================================
# 2. LOCAL CALCULATION SERVER & HTTP STREAM CLIENT SETUP
# =====================================================================

mcp = MCPServer("Calculator Server")

@mcp.tool(description="Calculator tool which performs calculations")
def calculator(x: int, y: int) -> int:
    return x + y

@mcp.tool(description="This is a long running tool")
def long_running_tool(name: str) -> str:
    time.sleep(25)
    return f"Hello {name}"

def main():
    mcp.run(transport="streamable-http")

# Start local server on a background thread so it can listen locally
thread = threading.Thread(target=main)
thread.daemon = True  # Ensures the thread closes when main script exits
thread.start()
time.sleep(2)  # Give the server a small moment to boot up safely

def create_streamable_http_transport():
    return streamable_http_client("http://localhost:8000/mcp")

streamable_http_mcp_client = MCPClient(create_streamable_http_transport)


# =====================================================================
# 3. GLOBAL OPENAI MODEL VALIDATION
# =====================================================================

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: 'OPENAI_API_KEY' environment variable is not set.", file=sys.stderr)
    print("Please execute: export OPENAI_API_KEY='sk-proj-...' in your terminal.", file=sys.stderr)
    sys.exit(1)

openai_model = OpenAIModel(
    model_id="gpt-5-mini",
    client_args={"api_key": api_key}
)


# =====================================================================
# 4. EXECUTION PIPELINES
# =====================================================================

# --- Pipeline A: Single Agent with Stdio Transport ---
print("\n--- Running Stdio Transport Pipeline ---")
with stdio_mcp_client:
    tools = stdio_mcp_client.list_tools_sync()
    agent = Agent(model=openai_model, tools=tools)
    response = agent("What is Amazon Bedrock pricing model. Be concise.")
    print(f"Response: {response}")

# --- Pipeline B: Single Agent with Streamable HTTP ---
print("\n--- Running Streamable HTTP Pipeline ---")
with streamable_http_mcp_client:
    tools = streamable_http_mcp_client.list_tools_sync()
    agent = Agent(model=openai_model, tools=tools)
    response = str(agent("What is 2 + 2?"))
    print(f"Response: {response}")

# --- Pipeline C: Interacting with Multiple MCP Servers ---
print("\n--- Running Multi-Server Pipeline ---")
with aws_docs_mcp_client, iac_mcp_client:
    tools = aws_docs_mcp_client.list_tools_sync() + iac_mcp_client.list_tools_sync()
    agent = Agent(model=openai_model, tools=tools)
    response = agent(
        "What is Amazon Bedrock pricing model. Be concise. Also what are the best practices related to CDK?"
    )
    print(f"Response: {response}")

