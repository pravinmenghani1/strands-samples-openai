# Strands Agents Deployment Patterns (Python)

Reference patterns for deploying agents to production environments.

The agents use OpenAI models. Set `OPENAI_API_KEY` in your environment (optionally `OPENAI_MODEL_ID`, default `gpt-5-mini`) before deploying; it is passed to the runtime as an environment variable. AWS is still needed for hosting and for the Knowledge Base, DynamoDB and SSM resources the samples use.

## Index

| Folder | Platform | Description |
|--------|----------|-------------|
| [`01-lambda`](./01-lambda/) | AWS Lambda | Deploy agents as serverless functions |
| [`02-fargate`](./02-fargate/) | AWS Fargate | Run agents in serverless containers |
| [`03-agentcore`](./03-agentcore/) | Amazon Bedrock AgentCore | Host agents on purpose-built runtime |
| [`04-agentcore-multi-agent`](./04-agentcore-multi-agent/) | Amazon Bedrock AgentCore | Deploy multi-agent A2A orchestration |

[Strands Agents Documentation](https://strandsagents.com/)
