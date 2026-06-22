import argparse

from workflows.startup import StartupWorkflow
from ui.gradio import launch_gradio


def run_cli():

    idea = input("💡 Idea: ")

    workflow = StartupWorkflow()

    result = workflow.run(idea)

    print(result["prd"])


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--ui", action="store_true")

    args = parser.parse_args()

    if args.ui:

        launch_gradio()

    else:

        run_cli()


if __name__ == "__main__":
    main()
