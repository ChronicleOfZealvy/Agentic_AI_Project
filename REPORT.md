# Agentic AI for Business Intelligence

## Architecture

<p align="center">
  <img src="assets/root_agent.png" width="800"/>
</p>

<p align="center">
  <em>Figure 1: Unified Agentic Architecture</em>
</p>

The system follows a **Unified Agentic Architecture** where the `root_agent` orchestrates task execution.  
The `bi_unified_agent` performs intent analysis, schema grounding, and SQL generation in a single reasoning loop.  
It interacts with controlled tools:

- `get_database_schema`
- `execute_sql_and_format`

After successful SQL execution, the result is passed to the `insight_agent`, which selects an appropriate visualization and generates a plain-language business explanation.

An intelligent error-handling loop captures SQL execution errors and automatically refines queries until successful execution is achieved.  
This architecture improves accuracy, stability, and API efficiency compared to a multi-step pipeline.

---

## Prompts

The system uses structured and schema-aware prompting to improve reliability and interpretability.

### SQL Generation Prompt

The SQL agent prompt includes:

- Clear role definition (e.g., “You are a BI SQL agent.”)
- Relevant database schema context
- Strict instruction to generate **SELECT-only** queries
- Structured reasoning steps (entity identification, joins, filters, aggregation)

This reduces hallucinated tables and incorrect joins while improving semantic correctness.

### Visualization & Insight Prompt

The Insight Agent prompt instructs the model to:

- Analyze dataset structure
- Select an appropriate chart type (e.g., line for time-series, bar for categorical comparison)
- Generate a concise plain-language explanation

This enhances interpretability for non-technical users.

---

## Safety Measures

Multiple guardrails were implemented to prevent prompt injection and database misuse.

### SQL Restrictions
- Only **SELECT** statements are allowed.
- Destructive commands (DROP, DELETE, UPDATE, INSERT, ALTER) are blocked.
- SQL structure is validated before execution.

### Tool-Based Execution Control
The LLM cannot directly access the database.  
It must invoke predefined tools:
- `get_database_schema`
- `execute_sql_and_format`

This prevents arbitrary command execution.

### Schema-Grounded Context
Only relevant schema metadata is dynamically retrieved to reduce hallucination risk and limit information exposure.

### Error Feedback Loop
If execution fails:
1. The database error message is captured.
2. The error is fed back to the agent.
3. The agent regenerates a refined SQL query.

This ensures robustness and higher execution success rates.

---

## Evaluation Procedure

The system was evaluated using structured business queries categorized by complexity:

- Aggregation queries (SUM, COUNT, AVG)
- Multi-condition filtering
- Time-series analysis
- Comparative analysis

Each query was tested under both:
- Baseline multi-step pipeline architecture
- Optimized unified agent architecture

### Evaluation Metrics

1. **SQL Execution Accuracy**
   - Syntactic correctness
   - Semantic correctness

2. **Latency**
   - End-to-end response time

3. **Visualization Appropriateness**
   - Correct chart selection based on data structure

4. **API Cost Efficiency**
   - Number of model invocations
   - Token usage per query

The optimized architecture demonstrated improved SQL accuracy, lower latency, reduced token usage, and stable performance within rate limits.
