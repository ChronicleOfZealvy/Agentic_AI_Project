# 🤖 Agentic AI for Business Intelligence

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Google ADK](https://img.shields.io/badge/Google%20ADK-Agent%20Dev%20Kit-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-AI-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-6.1.0-FF6700?style=for-the-badge&logo=gradio&logoColor=white)
![uv](https://img.shields.io/badge/uv-managed-430f8e?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

> 🎓 **Management Information System Project [DSBA 2/2]**
> A multi-agent Business Intelligence system powered by **Google's Agent Development Kit (ADK)** and **Google Gemini** — turning natural language into actionable data insights.

---

## 📖 Project Overview

**Agentic AI for Business Intelligence** is a full-stack intelligent analytics platform that bridges the gap between non-technical users and complex relational databases. Users simply ask questions in plain English, and the system automatically:

1. Translates the question into a safe, validated SQL query
2. Executes it against a Microsoft SQL Server database
3. Returns **auto-generated visualizations** and **AI-powered explanations**

The system is built on a **Unified Agentic Architecture** using Google's ADK, with Google Gemini as the underlying LLM powering all reasoning, generation, and analysis. It ships with two web interfaces: the **ADK Web UI** and a **Gradio App**.

---

## ✨ Features

- 🗣️ **Natural Language to SQL** — Ask business questions in plain English; the system generates accurate SQL automatically
- 🧠 **Schema-Aware Reasoning** — The agent dynamically retrieves database schema to ground its queries in real structure
- 🔐 **SQL Guardrails** — Only `SELECT` statements are permitted; destructive operations are strictly blocked
- 📊 **Auto Visualization** — Automatically selects the right chart type (bar, line, etc.) based on data shape
- 💬 **AI-Powered Explanations** — The Insight Agent generates plain-language summaries for non-technical users
- 🔁 **Error Feedback Loop** — If SQL fails, the error is fed back to the agent for automatic correction and retry
- 🖥️ **Dual Interface** — Supports both **ADK Web** and **Gradio** front-ends on the same backend
- 📦 **Reproducible Environment** — Fully managed via `uv` for consistent, hassle-free setup

---

## 🗂 Project Structure

```
Agentic-AI-Project/
│
├── assets/                          # Architecture & workflow diagrams
│   ├── Workflow.png                 # Overall agentic BI pipeline diagram
│   └── root_agent.png               # Root agent coordination diagram
│
├── gradio-adk-agent/                # 🔧 Main application directory
│   ├── bi_agent/
│   │   ├── __init__.py
│   │   ├── agent.py                 # Agent definitions, roles & prompt templates
│   │   ├── tools.py                 # Tool functions used by agents
│   │   ├── bi_service.py            # Business Intelligence service layer
│   │   ├── db_config.py             # Database connection configuration
│   │   ├── sql_executor.py          # SQL validation & safe execution
│   │   └── .env.example             # Environment variable template
│   │
│   ├── app.py                       # Gradio web interface entry point
│   ├── AGENTS.md                    # Detailed prompt templates
│   ├── pyproject.toml               # Project metadata & dependencies
│   └── uv.lock                      # Locked, reproducible environment
│
├── README.md
└── Short Technical Report.md        # Full system design documentation
```

---

## ⚙️ Installation

### Prerequisites

Ensure the following are available before getting started:

| Requirement | Version / Notes |
|-------------|----------------|
| 🐍 Python | 3.12+ |
| 📦 uv | Latest — [install guide](https://docs.astral.sh/uv/) |
| 🔑 Google API Key | From [Google AI Studio](https://aistudio.google.com/) |
| 🗄️ Microsoft SQL Server | Access credentials required |

### Step-by-Step Setup

**1. Clone the repository**

```bash
git clone https://github.com/pngkcwtk/Agentic-AI-Project.git
cd Agentic-AI-Project/gradio-adk-agent
```

**2. Install all dependencies**

```bash
uv sync
```

> This reads `pyproject.toml` and `uv.lock` to create a fully reproducible Python environment — no manual pip installs needed.

**3. Configure environment variables**

Copy the provided template:

```bash
cp bi_agent/.env.example bi_agent/.env
```

Then edit `bi_agent/.env` with your credentials:

```env
# Google Gemini API
GOOGLE_API_KEY=your_gemini_api_key_here

# Microsoft SQL Server
MSSQL_SERVER=your_server_address
MSSQL_DATABASE=your_database_name
MSSQL_USERNAME=your_username
MSSQL_PASSWORD=your_password
```

> ⚠️ The `.env` file is gitignored — your credentials will never be committed to version control.

---

## 🚀 Usage

You can run the project using either of the two available web interfaces. Both share the **same agent pipeline and backend**.

### Option A — ADK Web Interface

```bash
uv run adk web . --port 8000
```

Open in browser: `http://127.0.0.1:8000`

---

### Option B — Gradio Interface

```bash
uv run app.py
```

Open in browser: `http://127.0.0.1:7860`

---

### 💬 Example Queries to Try

```
"What are the top 5 products by total revenue this year?"
"Show me monthly sales trends for the past 6 months."
"Which region had the highest average order value last quarter?"
"How many customers placed more than 3 orders?"
```

---

## 📊 Workflow / Pipeline

```mermaid
flowchart TD
    A["USER QUESTION<br/>What were the top 5 sales regions in Q3?"]
    
    A --> B["Root Agent<br/>(Orchestrator)<br/>Routes & coordinates between agents"]
    
    B --> C["BI Unified Agent<br/>(Text-to-SQL Core)<br/><br/>
    1. Analyze intent<br/>
    2. Retrieve schema<br/>
    3. Generate SQL<br/>
    4. Validate & execute"]
    
    C --> D["SQL Execution Tool<br/>(Guarded)<br/>SELECT-only mode"]
    
    D --> E["Insight Agent<br/><br/>
    1. Select chart type<br/>
    2. Generate visual<br/>
    3. Write explanation"]
    
    E --> F["User Interface<br/>ADK Web (port 8000)<br/>Gradio App (port 7860)"]
```

**Pipeline Summary:**

1. 🗣️ User submits a natural language business question
2. 🎯 **Root Agent** receives the request and delegates to sub-agents
3. 🧠 **BI Unified Agent** analyses intent, retrieves schema, generates & validates SQL
4. 🛡️ SQL is executed via a controlled, SELECT-only tool
5. 📊 **Insight Agent** creates charts and plain-language explanations
6. 🖥️ Results are returned to the user through Gradio or ADK Web

---

## 🧠 Model / Method

### Agent Architecture

The system implements a **Unified Agentic Architecture** with three coordinated agents:

| Agent | Role | Key Responsibilities |
|-------|------|---------------------|
| 🎯 **Root Agent** | Orchestrator | Manages execution flow, delegates tasks to sub-agents |
| 🧮 **BI Unified Agent** | Text-to-SQL Core | Intent analysis, schema grounding, SQL generation & execution |
| 📊 **Insight Agent** | Visualization & NLG | Chart selection, data visualization, business explanation |

### Prompting Strategy

The system applies **structured, schema-aware prompting** to maximize accuracy and reduce hallucination.

**SQL Generation Prompt includes:**
- Explicit agent role definition
- Dynamic schema injection (only relevant tables)
- Strict `SELECT`-only enforcement
- Structured reasoning chain: entity identification → join logic → filtering → aggregation

**Visualization Prompt — Chart Selection Rules:**

| Data Type | Chart Selected |
|-----------|---------------|
| Time-series / trends | 📈 Line Chart |
| Categorical comparison | 📊 Bar Chart |
| Part-to-whole proportions | 🥧 Pie / Donut |
| Value distributions | 📉 Histogram |

### 🔐 Safety Measures

| Guardrail | Implementation |
|-----------|---------------|
| SQL Restriction | Only `SELECT` permitted; `DROP`, `DELETE`, `UPDATE`, `INSERT`, `ALTER` blocked |
| Tool-Based DB Access | LLM never touches DB directly — all access via `get_database_schema` and `execute_sql_and_format` |
| Schema-Grounded Prompting | Only relevant schema metadata injected per query to limit hallucination |
| Error Feedback Loop | SQL errors captured and returned to agent for automatic query self-correction |

---

## 📈 Evaluation / Results

### Evaluation Query Categories

| Category | Description | Example |
|----------|-------------|---------|
| 🔢 Aggregation | SUM, COUNT, AVG queries | "Total revenue by product category" |
| 🔍 Multi-condition Filtering | Complex WHERE clauses | "Orders > $500 from new customers in Q1" |
| 📅 Time-series Analysis | Trend over time | "Monthly sales over the past year" |
| ⚖️ Comparative Analysis | Group-by comparisons | "Region A vs Region B performance" |

### Evaluation Metrics

| Metric | What It Measures |
|--------|-----------------|
| ✅ SQL Execution Accuracy | Syntactic + semantic correctness of generated SQL |
| ⏱️ End-to-End Latency | Time from user query to final visualization output |
| 📊 Visualization Appropriateness | Whether chart type matches data structure |
| 💰 API Cost Efficiency | Model invocations and token consumption per query |

### Key Results

- ✅ The **Unified Agent** design reduced response latency and token usage vs. naive multi-agent approaches
- ✅ The **error feedback loop** successfully self-corrected invalid SQL without user intervention
- ✅ Schema-grounded prompting significantly reduced hallucinated table/column names
- ✅ Visualization selection aligned correctly with dataset dimensionality across all test query types

---

## 🛠 Technologies Used

### Core AI & Agent Stack

| Library / Tool | Purpose |
|---------------|---------|
| [Google ADK](https://google.github.io/adk-docs/) | Agent Development Kit — multi-agent orchestration framework |
| [Google Gemini](https://deepmind.google/technologies/gemini/) | LLM powering all agents (reasoning, SQL generation, insights) |

### Backend & Database

| Library / Tool | Purpose |
|---------------|---------|
| Python 3.12 | Core programming language |
| pyodbc | Microsoft SQL Server database driver |
| Microsoft SQL Server | Relational database backend |

### Frontend / UI

| Library / Tool | Purpose |
|---------------|---------|
| [Gradio 6.1.0](https://www.gradio.app/) | Web-based chat & visualization interface |
| ADK Web | Built-in ADK web UI for agent interaction |

### Developer Tooling

| Tool | Purpose |
|------|---------|
| [uv](https://docs.astral.sh/uv/) | Ultra-fast Python package & environment manager |
| python-dotenv | Secure environment variable management |

---

## 📄 Example Output

### 🗣️ Input Query
```
"Show me the top 5 products by total revenue last quarter."
```

### 🧮 Generated SQL
```sql
SELECT TOP 5
    p.ProductName,
    SUM(od.UnitPrice * od.Quantity) AS TotalRevenue
FROM Orders o
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE o.OrderDate >= DATEADD(QUARTER, -1, GETDATE())
GROUP BY p.ProductName
ORDER BY TotalRevenue DESC;
```

### 📊 Visualization Output
```
Bar Chart — Top 5 Products by Revenue (Last Quarter)
──────────────────────────────────────────────────────
Product A  ████████████████████████  $124,500
Product B  ████████████████████      $103,200
Product C  ████████████████           $84,700
Product D  ████████████               $63,100
Product E  ████████                   $41,800
```

### 💬 AI Insight Explanation
> *"Product A led revenue generation last quarter at $124,500 — 20% ahead of Product B. The top 3 products collectively account for ~68% of total revenue, suggesting a product concentration worth monitoring in portfolio strategy."*

---

## 📁 Documentation

For a full deep-dive into system design, refer to the **Short Technical Report** in the repository root:

```
Short Technical Report.md
```

It covers:
- 📐 Full system architecture with diagrams
- 🤝 Agent coordination design
- 🧩 Detailed prompting strategy
- 🔐 Safety mechanism implementation
- 📏 Evaluation methodology and results

---

## 👤 Author

| Field | Info |
|-------|------|
| 👤 **System Architect** | [@pngkcwtk](https://github.com/pngkcwtk) |
| 👤 **AI Logic** | [@Varanapat](https://github.com/Varanapat) & [@Patchara](https://github.com/PatcharaPongvech) |
| 👤 **UX/UI Designer** | [@jxxnvi8](https://github.com/jxxnvi8) & [@Thanist](https://github.com/TanistM) |
| 👤 **Research Assistant** | [@waanwara](https://github.com/waanwara) & [@Bussayamas]|
| 🎓 **Course** | Management Information System — DSBA 2/2 |
| 🔗 **Repository** | [Agentic-AI-Project](https://github.com/pngkcwtk/Agentic-AI-Project) |
| 🤖 **Powered By** | Google ADK + Google Gemini |

---

<div align="center">

Built with 🧠 intelligence & ☕ determination for **DSBA 2/2 — MIS Project**

*Transforming Business Intelligence through Agentic AI*

</div>
