# Management Information System Project
![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![uv](https://img.shields.io/badge/uv-managed-430f8e.svg?style=flat&logo=python&logoColor=white)
![Gradio Version](https://img.shields.io/badge/gradio-6.1.0-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Context
- The system converts natural language questions into SQL queries, executes them against Microsoft SQL Server, and automatically generates visualizations and explanations using Google's Gemini AI.

## Prerequisites

- [uv](https://github.com/kirenz/uv-setup) installed (manages dependencies and virtual environment)
- A Google API key from [Google AI Studio](https://aistudio.google.com/api-keys)

## Setup

1. **Clone or download the repository**

   ```bash
   git clone https://github.com/ChronicleOfZealvy/Agentic_AI_Project.git
   ```

   Navigate into the project directory:

     ```bash
     cd gradio-adk-agent
     ```

2. **Install dependencies** (also creates the virtual environment)

   ```bash
   uv sync
   ```

3. **Get your API key** (free) from [Google AI Studio](https://aistudio.google.com/api-keys)


4. **Configure your API key**

   Rename the `.env.example` file to `.env` in the project root, and add your Google API key:

   ```bash
   GOOGLE_API_KEY=YourApiKeyHere
   ```

**Important**: The `.env` file is already listed in `.gitignore` and will **not** be committed to the repository, keeping your key private.

5. **Configure Environment**

Go to folder bi_agent and rename `.example.env` to `.env` and fill in your credentials:

```env
# Google API Key
GOOGLE_API_KEY=your_gemini_api_key_here

# SQL Server Configuration
MSSQL_SERVER=your_server_address
MSSQL_DATABASE=your_database_name
MSSQL_USERNAME=your_username
MSSQL_PASSWORD=your_password
```

## Running the Application

### Option 1: Run with Gradio (Web UI)

Start the Time Agent application with Gradio interface:

```bash
uv run app.py
```

> **Note**: You may see a warning about "App name mismatch detected" - this can be safely ignored.

### Option 2: Run with ADK Web

From the root directory, run with ADK web:

```bash
uv run adk web
```

This will start the ADK web interface where you can interact with the agent. 
