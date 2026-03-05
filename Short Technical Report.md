# Agentic AI for Business Intelligence
### Short Technical Report

---

## 1. System Architecture

<p align="center">
  <img src="assets/Workflow.png" width="820"/>
</p>

<p align="center">
  <em>Figure 1. Overall Agentic BI Workflow</em>
</p>

The proposed system adopts a **Unified Agentic Architecture** designed to integrate reasoning, validation, and controlled tool invocation within a coordinated execution loop.

The execution flow begins when a user submits a business question. The **Root Agent** receives the request and delegates the task to the **BI Unified Agent**. The BI agent retrieves database schema information and generates SQL queries through controlled tools.

After successful SQL execution, the resulting structured data is forwarded to the **Insight Agent**, which generates visualizations and analytical explanations before returning the results to the user interface.

The architecture consists of three primary components.

---

## 2. Agent Coordination Design

### 🔹 Root Agent (Orchestrator)

<p align="center">
  <img src="assets/root_agent.png" width="700"/>
</p>

<p align="center">
  <em>Figure 2. Root Agent Sequential Coordination</em>
</p>

The **Root Agent** acts as the system orchestrator. It manages the execution flow and coordinates interactions between sub-agents and system tools.

### 🔹 BI Unified Agent

The **BI Unified Agent** performs several core analytical tasks:

- Business intent analysis  
- Schema grounding  
- SQL generation  

These steps are executed within a unified reasoning loop to reduce latency and unnecessary token consumption.

The agent interacts with the database only through controlled tools:

- `get_database_schema`
- `execute_sql_and_format`

### 🔹 Insight Agent

The **Insight Agent** receives structured query results and performs:

- Automatic visualization selection  
- Plain-language analytical explanation  

This component translates raw analytical results into business-friendly insights that can be easily interpreted by non-technical users.

---

## 3. Prompting Strategy

The system applies structured, schema-aware prompting to enhance semantic accuracy and reduce hallucination.

### 3.1 SQL Generation Prompt

The SQL agent is guided by:

- Explicit role definition  
- Contextual schema injection  
- Strict enforcement of **SELECT-only** query generation  
- Structured reasoning steps:
  - Entity identification
  - Join determination
  - Filtering logic
  - Aggregation logic

This structured reasoning design significantly reduces incorrect joins, hallucinated tables, and semantic misalignment.

### 3.2 Visualization & Insight Prompt

The Insight Agent prompt instructs the model to:

- Analyze dataset structure and dimensionality  
- Select appropriate chart types
  - Line chart → Time-series analysis
  - Bar chart → Categorical comparison
- Generate concise, business-oriented explanations

This design improves interpretability and supports non-technical decision-makers.

---

## 4. Safety Measures

To mitigate prompt injection risks and ensure secure enterprise deployment, multiple guardrails were implemented.

### 🔐 SQL Execution Restrictions

- Only **SELECT** statements are permitted.
- Destructive operations (DROP, DELETE, UPDATE, INSERT, ALTER) are strictly blocked.
- SQL structure is validated prior to execution.

### 🔐 Tool-Based Access Control

The LLM does not directly access the database.  
All database interactions occur exclusively through predefined tools:

- `get_database_schema`
- `execute_sql_and_format`

### 🔐 Schema-Grounded Context Injection

Only relevant schema metadata is dynamically retrieved. This approach:

- Reduces hallucination risk
- Limits unnecessary information exposure
- Improves semantic precision

### 🔐 Error Feedback Loop

If SQL execution fails:

1. The database error message is captured
2. The error message is returned to the agent
3. A refined SQL query is regenerated

This iterative correction mechanism increases robustness and improves query success rates.

---

## 5. Evaluation Procedure

System performance was evaluated using structured business queries categorized by analytical complexity:

- Aggregation queries (SUM, COUNT, AVG)
- Multi-condition filtering
- Time-series trend analysis
- Comparative analytical queries

### Evaluation Metrics

Performance was assessed across four key dimensions:

**1. SQL Execution Accuracy**

- Syntactic correctness
- Semantic correctness

**2. End-to-End Latency**

Measured from user query submission to final visualization and explanation output.

**3. Visualization Appropriateness**

Evaluates whether the selected chart type aligns with the dataset structure.

**4. API Cost Efficiency**

- Number of model invocations
- Token consumption per query

The optimized unified agent architecture demonstrated improved SQL accuracy, reduced response latency, lower token usage, and stable performance under system constraints.

---

This framework demonstrates how an **Agentic AI architecture** can transform traditional Business Intelligence workflows into an intelligent, self-service analytics platform.
