import gradio as gr

from workflows.startup import StartupWorkflow

workflow = StartupWorkflow()


def generate_project(idea):

    result = workflow.run(idea)

    return f"""
# PRD

{result['prd']}

# UI

{result['ui']}

# Database

{result['schema']}
"""


demo = gr.Interface(
    fn=generate_project,
    inputs=gr.Textbox(
        lines=5,
        label="Startup Idea"
    ),
    outputs=gr.Markdown(),
    title="🚀 StartupGPT",
    description="Generate a complete startup from one idea."
)

if __name__ == "__main__":
    demo.launch()
