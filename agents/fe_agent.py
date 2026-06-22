from utils.llm import call_llm
from utils.prompt_loader import load_prompt


class FrontendAgent:

    def __init__(self):
        self.prompt = load_prompt("frontend")

    def generate_frontend(self, prd: str, ui: str):

        prompt = self.prompt.format(
            prd=prd,
            ui=ui
        )

        return call_llm(prompt)
