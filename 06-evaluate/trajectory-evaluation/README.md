# Tutorial 04: Trajectory Evaluation

## Overview

This tutorial demonstrates how to evaluate agent trajectories - the sequences of tool calls, reasoning steps, and decisions agents make to complete tasks. Learn to evaluate not just what agents produce, but how they think and execute.

## What You'll Learn

- Understanding agent trajectories (tool calls, reasoning steps, sequences)
- Visualizing execution trajectories (Session → Trace → Spans)
- Using TrajectoryEvaluator with custom rubrics
- Evaluating optimal, suboptimal, and incorrect trajectories
- Implementing trajectory scoring functions (exact_match, in_order, any_order)
- Analyzing HOW agents think, not just WHAT they produce

## Prerequisites

- Python 3.11 or higher
- Set `OPENAI_API_KEY` in your environment (optionally `OPENAI_MODEL_ID`, default `gpt-5-mini`)
- Basic understanding of AI agents and multi-agent systems
- Familiarity with Jupyter notebooks

## Installation

### 1. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

### 3. Configure OpenAI

```bash
export OPENAI_API_KEY=your_openai_api_key
export OPENAI_MODEL_ID=gpt-5-mini  # optional, this is the default
```

## Running the Tutorial

### 1. Start Jupyter Notebook

```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Start Jupyter
jupyter notebook
```

### 2. Open the Notebook

Navigate to `04-trajectory-evaluation.ipynb` in the Jupyter interface.

### 3. Execute Cells

Run cells sequentially from top to bottom:
- Use `Shift + Enter` to execute each cell
- Review outputs and visualizations
- Experiment with modifying parameters

## Tutorial Structure

### 1. Introduction to Trajectories
- What is a trajectory?
- Why evaluate trajectories?
- Trajectory hierarchy (Session → Trace → Spans)

### 2. Multi-Agent System Setup
- Financial advisor agent
- Technical architect agent
- Market researcher agent
- Risk analyst agent
- Graph-based orchestration

### 3. Trajectory Scoring Functions
- exact_match_scorer: Strict sequence matching
- in_order_match_scorer: Allows extra steps
- any_order_match_scorer: Ignores order

### 4. Three Trajectory Scenarios
**Optimal**: Correct tools in correct order
- Expected execution path
- Maximum efficiency
- Perfect scores

**Suboptimal**: Extra or redundant steps
- Redundant tool calls
- Correct output but inefficient
- Increased costs and latency

**Incorrect**: Wrong tools or wrong order
- Missing critical steps
- Wrong execution sequence
- Incomplete analysis

### 5. TrajectoryEvaluator
- Custom rubric definition
- LLM-based trajectory assessment
- Automated evaluation workflow

### 6. Best Practices
- When to evaluate trajectories
- Choosing evaluation criteria
- Combining trajectory and output evaluation
- Production monitoring strategies

## Expected Outputs

### Execution Metrics
- Trajectory sequences for each scenario
- Scoring results (exact, in-order, any-order)
- Efficiency calculations
- Performance metrics

### Evaluation Results
- TrajectoryEvaluator scores with explanations
- Comparative analysis across scenarios
- Detailed trajectory visualizations
- Actionable improvement recommendations

### Key Insights
- Understanding optimal execution paths
- Identifying inefficiencies and redundancies
- Detecting missing or incorrect steps
- Optimization opportunities

## Troubleshooting

### Issue: OpenAI API Key Not Found

**Error**: `KeyError: 'OPENAI_API_KEY'`

**Solution**:
```bash
export OPENAI_API_KEY=your_openai_api_key
```

### Issue: Model Access Denied

**Error**: `PermissionDeniedError` or `Model not found`

**Solution**:
1. Check that your OpenAI key can use the model in `OPENAI_MODEL_ID` (default `gpt-5-mini`)
2. Confirm you're using the correct model ID

### Issue: Import Errors

**Error**: `ModuleNotFoundError: No module named 'strands'`

**Solution**:
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt

# Verify installations
pip list | grep strands
```

### Issue: Jupyter Kernel Not Found

**Error**: Kernel not available or not connecting

**Solution**:
```bash
# Install ipykernel in virtual environment
pip install ipykernel

# Register kernel
python -m ipykernel install --user --name=venv

# Select this kernel in Jupyter
```

### Issue: Trajectory Extraction Fails

**Error**: `AttributeError: 'GraphResult' object has no attribute 'execution_order'`

**Solution**:
- Ensure you're using the latest version of strands-agents
- Check that the graph is properly built and executed
- Verify the result object is from a graph execution

### Issue: Slow Execution

**Problem**: Cells take a long time to execute

**Solution**:
- Graph agent executions involve multiple LLM calls (expected behavior)
- Each agent in the graph makes its own inference
- Consider using a smaller model for testing
- Reduce the number of test cases if experimenting

## Key Concepts

### Trajectory
The complete sequence of actions (tool calls, reasoning steps, decisions) an agent takes to solve a task.

### Trajectory Evaluation
Assessing the quality, efficiency, and correctness of an agent's execution path, not just its final output.

### Scoring Functions
Mathematical functions that compare expected vs actual trajectories:
- **Exact Match**: Binary score (1.0 or 0.0) for exact sequence match
- **In-Order Match**: Proportion of expected steps present in correct order
- **Any-Order Match**: Proportion of expected steps present regardless of order

### Multi-Agent Trajectories
In multi-agent systems, trajectories show the coordination and handoffs between agents, revealing collaboration patterns.

## Additional Resources

### Documentation
- [Strands Agents Documentation](https://docs.strands.ai/agents)
- [Strands Evals Documentation](https://docs.strands.ai/evals)
- [OpenAI API Documentation](https://platform.openai.com/docs)

### Related Tutorials
- **Tutorial 01**: Built-in Evaluators - Foundation concepts
- **Tutorial 02**: Custom Evaluators - Creating domain-specific metrics
- **Tutorial 03**: Dataset Generation - Automated test case creation
- **Tutorial 05**: Multi-turn Evaluation - Actor simulation
- **Tutorial 06**: Multi-Agent Evaluation - Evaluating agent collaboration

### Best Practices Guide
- Combine trajectory and output evaluation for complete assessment
- Use exact_match for compliance-critical applications
- Use in_order_match for general correctness with flexibility
- Use any_order_match for independent parallel operations
- Monitor trajectory metrics in production
- Set efficiency benchmarks and track improvements

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review Strands documentation
3. Verify your OpenAI API key configuration
4. Check GitHub issues for similar problems
5. Check the OpenAI API status page for service issues

## License

This tutorial is provided as-is for educational purposes.

## Version

- Tutorial Version: 1.0
- Last Updated: 2025-11-25
- Compatible with: strands-agents >= 0.1.0, strands-evals >= 0.1.0
