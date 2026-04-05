# Google's Agent Development Kit (ADK) BI Agent with Gradio

![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![uv](https://img.shields.io/badge/uv-managed-430f8e.svg?style=flat&logo=python&logoColor=white)
![Gradio Version](https://img.shields.io/badge/gradio-6.1.0-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

---

## System Pipeline

```
User Question
      ↓
Root Agent (Orchestrator)
      ↓
BI Unified Agent (Text-to-SQL)
      ↓
SQL Execution Tool
      ↓
Insight Agent (Visualization + Explanation)
      ↓
User Interface (Gradio / ADK Web)
```

The system follows a **sequential agent pipeline**, where each agent is responsible for a specific stage of the business intelligence workflow.

---

## Project Structure

```
.
├── assets/                        # Architecture diagrams
│   ├── Workflow.png
│   └── root_agent.png
│
├── gradio-adk-agent/              # Main project directory
│   ├── bi_agent/
│   │   ├── __init__.py
│   │   ├── agent.py               # Agent definitions and prompts
│   │   ├── tools.py               # Tool functions used by agents
│   │   ├── bi_service.py          # Business Intelligence service layer
│   │   ├── db_config.py           # Database configuration
│   │   ├── sql_executor.py        # SQL validation and execution
│   │   └── .env.example
│   │
│   ├── app.py                     # Gradio web interface
│   ├── AGENTS.md                  # Prompt templates
│   ├── pyproject.toml             # Project dependencies
│   └── uv.lock                    # Reproducible environment
│
├── README.md
└── Short Technical Report.md
```

---

## Prerequisites

Before running the project, ensure the following are installed:

- **Python 3.12**
- **uv** (Python package & environment manager)
- **Google API Key** from Google AI Studio
- **Microsoft SQL Server** access

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/ChronicleOfZealvy/Agentic_AI_Project.git
cd Agentic_AI_Project
cd gradio-adk-agent
```

---

### 2. Install dependencies

```bash
uv sync
```

This installs all project dependencies and creates a reproducible environment.

---

### 3. Configure Environment Variables

An environment variable template is provided in the `bi_agent` directory.

Copy or rename the template file:

```
bi_agent/.env.example → bi_agent/.env
```

Then open the `.env` file and update the values with your credentials.

Example configuration:

```
GOOGLE_API_KEY=your_gemini_api_key_here

MSSQL_SERVER=your_server_address
MSSQL_DATABASE=your_database_name
MSSQL_USERNAME=your_username
MSSQL_PASSWORD=your_password
```

The `.env` file is excluded from version control to protect sensitive credentials.

---

## Running the Project

### Run with ADK Web Interface

```bash
uv run adk web . --port 8000
```

Open in browser:

```
http://127.0.0.1:8000
```

---

### Run with Gradio Interface

```bash
uv run app.py
```

Open in browser:

```
http://127.0.0.1:7860
```

Both interfaces share the **same agent pipeline and backend services**.

---

## Key Capabilities

- Natural language → SQL query generation
- Guarded SQL execution with safety checks
- Schema-aware query reasoning
- Automated visualization generation
- AI-powered analytical explanations
- Dual interface support (ADK Web + Gradio)
- Fully reproducible Python environment using **uv**

---

## Documentation

For a detailed explanation of:

- System architecture
- Agent coordination
- Prompt design
- Safety mechanisms
- Evaluation methodology

please refer to:

**Short Technical Report**

```
Short Technical Report.md
```
