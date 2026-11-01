# Tutorial 01: Getting Started with Built-In Evaluators

## Overview

This tutorial introduces the complete toolkit of built-in evaluators provided by Strands Evals. You'll learn how to measure different aspects of agent performance using standardized evaluation metrics, from response quality to tool selection accuracy.

## What You'll Learn

- Understand the purpose of each built-in evaluator
- Apply OutputEvaluator to assess response quality
- Use HelpfulnessEvaluator to measure user satisfaction
- Track task completion with GoalSuccessRateEvaluator
- Validate tool usage with ToolSelectionAccuracyEvaluator and ToolParameterAccuracyEvaluator
- Preview trajectory evaluation capabilities

## Prerequisites

### System Requirements

- Python 3.11 or higher
- An OpenAI API key

### OpenAI Setup

Set `OPENAI_API_KEY` in your environment (optionally `OPENAI_MODEL_ID`, default `gpt-5-mini`):
```bash
export OPENAI_API_KEY=your_openai_api_key
export OPENAI_MODEL_ID=gpt-5-mini  # optional
```

### Python Environment

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Installation

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify installation**:
   ```bash
   python -c "import strands; import strands_evals; print('Installation successful')"
   ```

## Running the Tutorial

### Option 1: Jupyter Notebook

1. **Start Jupyter**:
   ```bash
   jupyter notebook
   ```

2. **Open the notebook**:
   - Navigate to `01-built-in-evaluators.ipynb`
   - Run cells sequentially using Shift+Enter

### Option 2: JupyterLab

1. **Start JupyterLab**:
   ```bash
   jupyter lab
   ```

2. **Open the notebook**:
   - Navigate to `01-built-in-evaluators.ipynb`
   - Run cells sequentially using Shift+Enter

### Option 3: VS Code

1. **Open in VS Code**:
   ```bash
   code 01-built-in-evaluators.ipynb
   ```

2. **Select Python kernel**:
   - Choose your virtual environment as the kernel
   - Run cells using the play button or Shift+Enter

## Expected Outcomes

After completing this tutorial, you will:

1. **Understand Built-In Evaluators**: Know when to use each evaluator type
2. **Evaluate Response Quality**: Use OutputEvaluator and HelpfulnessEvaluator
3. **Track Task Completion**: Apply GoalSuccessRateEvaluator
4. **Validate Tool Usage**: Use ToolSelectionAccuracyEvaluator and ToolParameterAccuracyEvaluator
5. **Analyze Agent Reasoning**: Preview TrajectoryEvaluator capabilities
6. **Interpret Results**: Understand evaluation metrics and scoring

### Sample Output

The notebook will produce:
- Evaluation reports for each evaluator type
- Formatted results with scores, labels, and explanations
- Comprehensive summary of agent performance across all dimensions

## Troubleshooting

### Common Issues

#### Missing API Key
```
KeyError: 'OPENAI_API_KEY'
```
**Solution**: Set `OPENAI_API_KEY` in your environment before starting Jupyter

#### Model Access Error
```
Error: The model does not exist or you do not have access to it
```
**Solution**: Check that your OpenAI key can use the model in `OPENAI_MODEL_ID` (default `gpt-5-mini`)

#### DuckDuckGo Rate Limit
```
RatelimitException: Please try again after a short delay
```
**Solution**: Wait 30-60 seconds and re-run the cell. The websearch tool includes built-in rate limit handling.

#### Import Error
```
ModuleNotFoundError: No module named 'strands'
```
**Solution**: Ensure you've installed all dependencies: `pip install -r requirements.txt`

### Getting Help

If you encounter issues not covered here:

1. Check the [Strands documentation](https://docs.strands.ai)
2. Review your OpenAI API usage limits
3. Verify all dependencies are correctly installed
4. Ensure you're using Python 3.11 or higher

## Tutorial Structure

The notebook is organized into these sections:

1. **Introduction**: Overview and learning objectives
2. **Concept Explanation**: Understanding built-in evaluators
3. **Environment Setup**: OpenAI model configuration
4. **Agent Implementation**: Recipe Bot agent with websearch tool
5. **Test Cases**: Creating evaluation scenarios
6. **Quality Evaluation**: OutputEvaluator, HelpfulnessEvaluator, GoalSuccessRateEvaluator
7. **Tool Evaluation**: ToolSelectionAccuracyEvaluator, ToolParameterAccuracyEvaluator
8. **Trajectory Preview**: TrajectoryEvaluator demonstration
9. **Results Analysis**: Comprehensive summary and insights

## Next Steps

After completing this tutorial, consider:

- **Tutorial 02**: Learn to create custom evaluators for domain-specific needs
- **Tutorial 03**: Explore automated dataset generation
- **Tutorial 04**: Deep dive into trajectory evaluation
- **Tutorial 05**: Master multi-turn conversation evaluation

## Additional Resources

- [Strands Agents Documentation](https://docs.strands.ai/agents)
- [Strands Evals Documentation](https://docs.strands.ai/evals)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Recipe Bot Source Code](../../01-learn/01-first-agent/recipe-bot-cli/)

## License

This tutorial is part of the Strands evaluation framework examples.
