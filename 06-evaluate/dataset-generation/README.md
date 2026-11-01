# Tutorial 03: Dataset Generation for Agent Evaluation

This tutorial demonstrates automated test case generation for agent evaluation using the Strands Evals DatasetGenerator API. Learn how to generate diverse, high-quality test datasets and persist them for reuse across evaluation runs.

## What You'll Learn

- Generate test cases from scratch using topics
- Generate contextual test cases from agent tools and APIs
- Update existing datasets with edge cases and corner scenarios
- Save datasets to JSON files for reuse
- Load datasets from JSON files
- Use auto-rubric generation for evaluators
- Apply topic planning for diverse test coverage

## Prerequisites

- Python 3.11 or higher
- Set `OPENAI_API_KEY` in your environment (optionally `OPENAI_MODEL_ID`, default `gpt-5-mini`)
- Basic understanding of agent evaluation concepts

## Installation

1. **Clone or download this tutorial**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure OpenAI**:
   ```bash
   export OPENAI_API_KEY=your_openai_api_key
   export OPENAI_MODEL_ID=gpt-5-mini  # optional
   ```

## Tutorial Components

### Multi-Agent System

This tutorial uses a multi-agent decision-making system with parallel execution:

- **Financial Advisor**: Analyzes costs, ROI, and budget implications
- **Technical Architect**: Evaluates technical feasibility and implementation risks
- **Market Researcher**: Assesses market demand and competitive landscape
- **Risk Analyst**: Synthesizes all inputs for final recommendations

The agents execute in parallel:
```
finance_expert (entry) --> tech_expert --> risk_analyst (final)
                        └> market_expert ┘
```

### Three Dataset Generation Strategies

**1. from_scratch_async()**: Generate from topics
- Creates diverse test cases covering specified topics
- Includes auto-rubric generation
- Best for: Broad coverage testing

**2. from_context_async()**: Generate from agent context
- Uses agent's tools and capabilities to create relevant tests
- Supports topic planning for diversity
- Best for: Context-aware testing

**3. update_current_dataset_async()**: Update existing datasets
- Adds edge cases and corner scenarios to existing datasets
- Preserves original tests while adding new ones
- Best for: Iterative improvement

### Dataset Persistence

All datasets can be saved and loaded:
- **Save**: `dataset.to_file('dataset_name.json')`
- **Load**: `Dataset.from_file('dataset_name.json')`

## How to Run the Notebook

1. **Start Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

2. **Open the notebook**:
   Navigate to `03-dataset-generation.ipynb`

3. **Run all cells**:
   - Execute cells sequentially from top to bottom
   - Or use "Run All" from the Cell menu

4. **Review generated datasets**:
   The notebook will create three JSON files:
   - `scratch_dataset.json` - Dataset generated from topics
   - `context_dataset.json` - Dataset generated from agent context
   - `updated_dataset.json` - Dataset with added edge cases

## Expected Outcomes

After completing this tutorial, you will have:

1. **Working Multi-Agent System**: A decision-making system with parallel execution
2. **Three Generated Datasets**: Saved as JSON files for reuse
3. **Evaluation Results**: Performance metrics from auto-generated rubrics
4. **Understanding of Strategies**: Knowledge of when to use each generation method

### Generated Dataset Files

- **scratch_dataset.json**: 9 test cases covering technology investments, business automation, and market expansion
- **context_dataset.json**: 12 test cases based on multi-agent capabilities with topic planning
- **updated_dataset.json**: 15 test cases (original 9 + 6 edge cases)

## Key Concepts

### Auto-Rubric Generation

The DatasetGenerator automatically creates evaluation rubrics aligned with:
- The task description
- The topics or context provided
- The evaluator type (OutputEvaluator, TrajectoryEvaluator, etc.)

### Topic Planning

Use `num_topics` parameter to improve diversity:
- Automatically expands prompts into multiple topic areas
- Distributes test cases across topics
- Ensures comprehensive coverage
- Recommended: 3-6 topics for most use cases

### Difficulty Distribution

Generated test cases include:
- Easy cases (30%)
- Medium cases (50%)
- Hard cases (20%)

## Troubleshooting

### API Key Issues

**Error**: `KeyError: 'OPENAI_API_KEY'` or `AuthenticationError`

**Solution**:
- Set `OPENAI_API_KEY` in your environment before starting Jupyter
- Check that the key is valid and active

### Model Access Issues

**Error**: `NotFoundError` or model not available

**Solution**:
- Check that your OpenAI key can use the model in `OPENAI_MODEL_ID` (default `gpt-5-mini`)

### Dataset Generation Timeout

**Error**: Generation takes too long or times out

**Solution**:
- Reduce `num_cases` parameter (try 5-10 instead of 20+)
- Reduce `num_topics` if using topic planning
- Check network connectivity to the OpenAI API

### JSON File Errors

**Error**: Cannot save or load dataset files

**Solution**:
- Check write permissions in current directory
- Verify file path is correct
- Ensure JSON file is valid (no manual edits)
- Use absolute paths if relative paths fail

### Memory Issues

**Error**: Out of memory or kernel crashes

**Solution**:
- Reduce number of parallel workers: Set `max_parallel_num_cases` to 5
- Generate fewer test cases per batch
- Restart Jupyter kernel
- Close other memory-intensive applications

### Import Errors

**Error**: `ModuleNotFoundError` for strands packages

**Solution**:
- Reinstall dependencies: `pip install -r requirements.txt`
- Verify virtual environment is activated
- Check Python version (3.10+ required)
- Update pip: `pip install --upgrade pip`

## Next Steps

After completing this tutorial, explore:

- **Tutorial 04: Trajectory Evaluation** - Evaluate agent reasoning and action sequences
- **Tutorial 05: Multi-turn Evaluation** - Test conversational agents with ActorSimulator
- **Custom Dataset Generation** - Create domain-specific generation strategies
- **Production Workflows** - Integrate dataset generation into CI/CD pipelines

## Additional Resources

- [Strands Agents Documentation](https://github.com/awslabs/strands-agents)
- [Strands Evals Documentation](https://github.com/awslabs/strands-evals)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [DatasetGenerator API Reference](https://github.com/awslabs/strands-evals/blob/main/docs/dataset-generator.md)

## Support

For issues or questions:
- Check the troubleshooting section above
- Review the Strands Evals documentation
- Open an issue on the GitHub repository
- Check the OpenAI API status page

## License

This tutorial is provided as-is for educational purposes.
