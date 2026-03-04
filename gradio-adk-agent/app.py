"""
Gradio UI for the Business Intelligence Agent Pipeline.
Improved Stable Version:
- Clear resets everything properly
- Technical Insight not duplicated
- Structured Data always renders safely
"""

import gradio as gr
import asyncio
import os
import json
import pandas as pd
import altair as alt
from dotenv import load_dotenv
from google.genai import types
from bi_agent import root_runner

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# =============================================================================
# Environment
# =============================================================================

if os.path.exists('.env'):
    load_dotenv()
else:
    load_dotenv(dotenv_path='bi_agent/.env')


# =============================================================================
# Backend
# =============================================================================

async def run_bi_pipeline_async(user_question: str):

    root_runner.app_name = 'agents'

    session = await root_runner.session_service.create_session(
        user_id='user',
        app_name='agents'
    )

    content = types.Content(role='user', parts=[types.Part(text=user_question)])

    events_async = root_runner.run_async(
        user_id='user',
        session_id=session.id,
        new_message=content
    )

    results = {}

    async for event in events_async:

        if event.actions and event.actions.state_delta:
            results.update(event.actions.state_delta)

        if hasattr(event, "candidates") and event.candidates:
            for candidate in event.candidates:
                if hasattr(candidate, "content") and candidate.content.parts:
                    for part in candidate.content.parts:
                        if hasattr(part, "text") and part.text:
                            results["raw_agent_text"] = (
                                results.get("raw_agent_text", "") + part.text
                            )

    return results


# =============================================================================
# Processing
# =============================================================================

async def process_request(message: str):

    if not message.strip():
        return "", pd.DataFrame(), None, "No question provided", "Failed", ""

    try:
        results = await run_bi_pipeline_async(message)

        raw_output = results.get(
            "raw_agent_text",
            results.get("final_insight", "")
        )

        parsed_json = {}

        # ================= JSON Extraction =================
        if isinstance(raw_output, str) and '{' in raw_output:
            try:
                start = raw_output.find('{')
                count, end = 0, -1

                for i in range(start, len(raw_output)):
                    if raw_output[i] == '{':
                        count += 1
                    elif raw_output[i] == '}':
                        count -= 1
                    if count == 0:
                        end = i + 1
                        break

                if end != -1:
                    parsed_json = json.loads(raw_output[start:end])
            except Exception:
                parsed_json = {}

        # ================= SAFE DataFrame =================
        df = pd.DataFrame()
        data_source = None

        if isinstance(parsed_json, dict) and "formatted_data" in parsed_json:
            data_source = parsed_json["formatted_data"]
        elif isinstance(results, dict) and "formatted_data" in results:
            data_source = results["formatted_data"]

        if data_source:
            try:
                if isinstance(data_source, str):
                    data_source = json.loads(data_source)

                if isinstance(data_source, dict) and "data" in data_source:
                    df = pd.DataFrame(data_source["data"])
                elif isinstance(data_source, list):
                    df = pd.DataFrame(data_source)
                elif isinstance(data_source, dict):
                    df = pd.DataFrame([data_source])
            except Exception:
                df = pd.DataFrame()

        # 🔥 IMPORTANT: Ensure Structured View always shows something
        if df.empty:
            df = pd.DataFrame({"Info": ["No structured data returned"]})

        # ================= Chart Code =================
        chart = None
        chart_code_raw = parsed_json.get("chart_code", "")
        python_code_out = ""

        if chart_code_raw:
            try:
                python_code_out = chart_code_raw.replace('\\n', '\n').replace('\\"', '"')
                namespace = {"alt": alt, "pd": pd, "df": df, "json": json}
                exec(python_code_out, namespace)
                chart = namespace.get("chart") or namespace.get("vis")
            except Exception:
                chart = None

        # ================= Summary Split =================
        full_summary = parsed_json.get("executive_summary", "")

        if not full_summary and isinstance(raw_output, str):
            full_summary = raw_output.split('{')[0].strip()

        if not full_summary:
            full_summary = "Analysis completed."

        lines = full_summary.split("\n")

        # Business Summary (Top 3 lines)
        short_summary = "\n".join(lines[:3])

        if len(lines) > 3:
            short_summary += "\n\n👉 Click 'View Technical Insights' to expand."

        # Technical Insight (Remaining lines ONLY)
        technical_only = "\n".join(lines[3:]).strip()

        if not technical_only:
            technical_only = "No additional technical breakdown available."

        return (
            python_code_out,
            df,
            chart,
            short_summary,
            "Analysis completed successfully.",
            technical_only
        )

    except Exception as e:
        return (
            "",
            pd.DataFrame({"Error": [str(e)]}),
            None,
            "⚠️ Agent completed but no structured data was returned.",
            str(e),
            ""
        )


# =============================================================================
# Clear (REAL RESET)
# =============================================================================

def clear_all():
    return (
        "",                         # user_input
        "",                         # sql_out
        pd.DataFrame(),             # data_out
        None,                       # chart_out
        "### 🔍 Waiting for query...",
        "",                         # status_log
        "",                         # full_summary_state
        gr.update(open=False)       # close logs accordion
    )


# =============================================================================
# UI
# =============================================================================

custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
.gradio-container { background: radial-gradient(circle at top right, #1e293b, #0f172a, #020617) !important; font-family: 'Inter', sans-serif !important; }
h1 { background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc) !important; -webkit-background-clip: text !important; -webkit-text-fill-color: transparent !important; font-weight: 800 !important; text-align: center !important; font-size: 2.8rem !important;}
.gradio-container label span { background-color: #6366f1 !important; color: white !important; font-weight: 600 !important; padding: 2px 8px !important; border-radius: 4px !important; }
.gradio-container :is(textarea, input), button.secondary, .gr-button:not(.btn-primary) { 
    background-color: #2d3748 !important; border: 1px solid rgba(255, 255, 255, 0.1) !important; color: white !important; 
}
button.secondary:hover, .gr-button:not(.btn-primary):hover { background-color: #6366f1 !important; border-color: #818cf8 !important; }
.btn-primary { background: #6366f1 !important; border: none !important; color: white !important; }
.gradio-container :is(.gr-form, .gr-box, .gr-padded, .gr-block, .form, .gr-accordion):not(.vega-actions-wrapper) { 
    border: none !important; box-shadow: none !important; background-color: transparent !important; 
}
"""

with gr.Blocks(fill_width=True, css=custom_css) as demo:

    gr.Markdown("# 🤖 Intelligent SQL Agent & Analytics")

    full_summary_state = gr.State()

    with gr.Row():

        with gr.Column(scale=1):

            user_input = gr.Textbox(label="💬 Database Inquiry", lines=4)

            gr.Markdown("### 💡 Example Questions")

            examples = [
                "List all products in the Bikes category.",
                "How many products are there in each category?",
                "What are the top 10 products by transfer price?",
                "Show me the product categories and their average prices."
            ]

            gr.Examples(examples=examples, inputs=user_input)

            with gr.Row():
                clear_btn = gr.Button("🗑️ Clear")
                submit_btn = gr.Button("🚀 Run Analysis", variant="primary")

            with gr.Accordion("🛠️ Technical Logs", open=False) as logs_acc:
                sql_out = gr.Code(label="Python Code / Generated SQL")
                status_log = gr.Textbox(label="Agent Status")

        with gr.Column(scale=2):

            chart_out = gr.Plot(label="Visualization Result")
            summary_out = gr.Markdown("### 🔍 Waiting for query...")
            explain_btn = gr.Button("📖 View Technical Insights")
            detailed_markdown = gr.Markdown()

            with gr.Accordion("📄 Structured Data View", open=True):
                data_out = gr.DataFrame(interactive=False)

    submit_btn.click(
        fn=process_request,
        inputs=[user_input],
        outputs=[
            sql_out,
            data_out,
            chart_out,
            summary_out,
            status_log,
            full_summary_state
        ]
    )

    explain_btn.click(
        fn=lambda x: x,
        inputs=[full_summary_state],
        outputs=[detailed_markdown]
    )

    clear_btn.click(
        fn=clear_all,
        outputs=[
            user_input,
            sql_out,
            data_out,
            chart_out,
            summary_out,
            status_log,
            full_summary_state,
            logs_acc
        ]
    )


if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft())
