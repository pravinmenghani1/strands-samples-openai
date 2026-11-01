# Tutorial 07: A/B Testing Models in Agents

## Overview

This tutorial demonstrates how to systematically compare different language models in production agent systems through A/B testing. Learn to build multiple agent variants, evaluate them on identical tasks, and make data-driven model selection decisions based on quality, cost, and performance metrics.

## Tutorial Structure

This tutorial consists of two parts:

### Part 1: Building Agents (07a-ab-testing-build-agents.ipynb)
- Use ReAct airline assistant agent from python/04-industry-use-cases/logistics/
- Create three agent variants with different models
- Configure identical prompts, tools, and orchestration
- Test each agent independently with sample queries
- Save configurations for systematic evaluation

### Part 2: Evaluation (07b-ab-testing-evaluate.ipynb)
- Run all three agents on identical test dataset
- Compare evaluation scores side-by-side
- Analyze cost-performance trade-offs
- Generate statistical comparisons
- Produce model selection recommendations

## Models Compared

**GPT-5 nano** (gpt-5-nano)
- Fastest, most cost-effective
- Optimized for simple, high-volume queries
- Lower latency, lower cost per token

**GPT-5** (gpt-5)
- Strongest reasoning for complex tasks
- Highest cost per token

**GPT-5 mini** (gpt-5-mini)
- Balanced speed and capability
- Production-ready for most use cases

## What You'll Learn

- Build ReAct agents with custom orchestration
- Create multiple agent variants for A/B testing
- Configure identical capabilities across models
- Run systematic comparative evaluations
- Analyze cost-performance trade-offs
- Make data-driven model selection decisions
- Understand when to use each model type

## Prerequisites

- Completion of Tutorials 01-06 (recommended)
- Understanding of agent evaluation concepts
- Familiarity with Strands Agents and Strands Evals
- Set `OPENAI_API_KEY` in your environment (optionally `OPENAI_MODEL_ID`, default `gpt-5-mini`, for the evaluator judge)

## Installation

```bash
pip install -r requirements.txt
```

## Dataset

This tutorial uses the TauBench airline customer service dataset from the repository. The dataset includes:
- Flight search and booking queries
- Reservation modification scenarios
- Cancellation and refund requests
- Policy-based customer service inquiries

## Running the Tutorial

### Step 1: Build Agents
Open and run `07a-ab-testing-build-agents.ipynb`:
- Imports airline tools from python/04-industry-use-cases/logistics/custom-orchestration-airline-assistant/
- Creates three agent variants
- Tests basic functionality
- Exports configuration for evaluation

### Step 2: Evaluate Agents
Open and run `07b-ab-testing-evaluate.ipynb`:
- Loads agent configurations
- Runs systematic evaluation
- Generates comparative reports
- Provides model recommendations

## Key Concepts

### A/B Testing
Controlled comparison of variants to determine optimal configuration based on measurable outcomes.

### ReAct Agent Pattern
Reasoning and Acting pattern where agent iteratively thinks, acts with tools, and observes results.

### Model Selection Criteria
- **Quality**: Output accuracy and completeness
- **Cost**: Tokens consumed and pricing per model
- **Latency**: Response time and throughput
- **Capability fit**: Match between model strengths and task requirements

## Expected Outcomes

After completing this tutorial, you will:
- Understand how to structure A/B tests for agents
- Be able to build multiple agent variants efficiently
- Know how to evaluate models systematically
- Understand cost-performance trade-offs
- Make data-driven model selection decisions

## Tutorial Complexity

**Level**: Advanced
**Estimated time**: 60-90 minutes (both parts)
**Prerequisites**: Tutorials 01-06

## Agent Source

This tutorial uses the ReAct airline assistant agent from:
`python/04-industry-use-cases/logistics/custom-orchestration-airline-assistant/`

The agent includes 14 airline domain tools for comprehensive customer service operations.

## Support

For issues or questions:
- Review tutorial prerequisites
- Check that your OpenAI API key has access to the three models
- Verify required tools are in python/04-industry-use-cases/logistics/custom-orchestration-airline-assistant/
- Ensure all required tools are imported correctly

## Next Steps

After completing this tutorial:
- Experiment with additional models
- Test reasoning-effort variations
- Extend to multi-agent A/B testing
- Apply to your own agent use cases
